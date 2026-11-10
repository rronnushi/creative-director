"""Prepare paired manual evaluation workspaces. This does not execute an agent."""
import argparse
import json
from pathlib import Path
import shutil
from common import ROOT, read_json, write_new


def prepare(output, selected=None):
    output = Path(output)
    if output.exists():
        raise ValueError('output must be a new directory')
    scenarios = read_json(ROOT / 'tests/scenarios.json')
    if selected:
        scenarios = [s for s in scenarios if s['id'] in selected]
        if {s['id'] for s in scenarios} != set(selected):
            raise ValueError('unknown scenario ID')
    manifest = {'status': 'pending-agent-execution', 'pairs': []}
    for scenario in scenarios:
        for arm in ('baseline', 'skill'):
            work = output / scenario['id'] / arm
            work.mkdir(parents=True)
            task = scenario['input']
            if scenario['fixture']:
                source = ROOT / scenario['fixture']
                shutil.copyfile(source, work / source.name)
                task += f'\n\nRaw artifact: {source.name}'
            if arm == 'skill':
                task += '\n\nUse the Creative Director skill supplied by your host.'
            (work / 'task.md').write_text(task + '\n', encoding='utf-8')
        manifest['pairs'].append({'id': scenario['id'], 'status': 'pending',
                                  'baseline': f'{scenario["id"]}/baseline',
                                  'skill': f'{scenario["id"]}/skill'})
    write_new(output / 'manifest.json', manifest)
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--scenario', action='append')
    args = parser.parse_args()
    try:
        print(json.dumps(prepare(args.output, args.scenario), indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
