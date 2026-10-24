"""Validate the canonical skill, records, scenarios and local references offline."""
import json
from pathlib import Path
import re
from common import ROOT, check, inside, parse_json, read_json, validate_comparison, validate_record
from check_references import local_errors


def validate(root=ROOT):
    errors = local_errors(root)
    try:
        skill = (root / 'SKILL.md').read_text(encoding='utf-8')
        parts = skill.split('---', 2)
        if len(parts) != 3 or parts[0].strip():
            raise ValueError('SKILL.md requires delimited frontmatter')
        # JSON is a YAML 1.2 subset. Deliberately restrict authoring to this subset
        # so metadata can be parsed rigorously without a runtime YAML dependency.
        meta = parse_json(parts[1])
        check(meta, {'type': 'object', 'required': ['name', 'description'],
                     'additionalProperties': False, 'properties': {
                         'name': {'type': 'string', 'minLength': 1, 'maxLength': 64,
                                  'pattern': r'^[a-z0-9]+(?:-[a-z0-9]+)*$'},
                         'description': {'type': 'string', 'minLength': 1, 'maxLength': 1024},
                         'license': {'type': 'string', 'minLength': 1}}})
        if meta['name'] != root.name:
            raise ValueError('metadata name must match installable directory')
        if len(skill.splitlines()) > 150:
            raise ValueError('entrypoint exceeds project context budget of 150 lines')
        for workflow in ('direct', 'critique', 'refine', 'discover', 'design', 'build', 'reference-translation'):
            inside(root, f'workflows/{workflow}.md')
        comparisons = read_json(root / 'knowledge/comparisons.json')
        ids = set()
        for record in comparisons:
            validate_comparison(record, root)
            if record['id'] in ids:
                raise ValueError('duplicate comparison ID')
            ids.add(record['id'])
        validate_record(read_json(root / 'knowledge/profile.example.json'), 'profile', root)
        scenarios = read_json(root / 'tests/scenarios.json')
        if len(scenarios) < 25:
            raise ValueError('at least 25 scenarios required')
        ids, modes, negatives = set(), set(), 0
        for scenario in scenarios:
            validate_record(scenario, 'scenario', root)
            if scenario['id'] in ids:
                raise ValueError('duplicate scenario ID')
            ids.add(scenario['id'])
            if scenario['activation'] == (scenario['mode'] == 'NONE'):
                raise ValueError('scenario activation contradicts mode')
            modes.add(scenario['mode'])
            negatives += not scenario['activation']
            if not scenario['objective_checks'] or not scenario['human_criteria'] or not scenario['failure_conditions']:
                raise ValueError('scenario lacks evaluation criteria')
            for reference in scenario['references']:
                inside(root, reference)
            if scenario['fixture']:
                inside(root, scenario['fixture'])
        if modes != {'DIRECT','CRITIQUE','REFINE','DISCOVER','DESIGN','BUILD','NONE'} or negatives < 5:
            raise ValueError('scenario suite requires all modes and five negative cases')
        for path in root.rglob('*'):
            if path.is_file() and path.stat().st_size == 0:
                raise ValueError(f'empty file: {path.relative_to(root)}')
        return errors
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return errors + [str(exc)]


if __name__ == '__main__':
    errors = validate()
    print(json.dumps({'status': 'failed' if errors else 'passed', 'errors': errors}, indent=2))
    raise SystemExit(bool(errors))
