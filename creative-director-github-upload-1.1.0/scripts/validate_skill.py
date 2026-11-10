"""Validate an installed skill, plus repository-only records when available."""
import json
from common import ROOT, SKILL, check, frontmatter, inside, read_json, validate_comparison, validate_record
from check_references import local_errors, markdown_errors


def validate(root=SKILL):
    errors = local_errors(root)
    try:
        text = (root / 'SKILL.md').read_text(encoding='utf-8')
        meta = frontmatter(text)
        check(meta, {'type': 'object', 'required': ['name', 'description'],
              'additionalProperties': False, 'properties': {
                  'name': {'type': 'string', 'minLength': 1, 'maxLength': 64,
                           'pattern': r'^[a-z0-9]+(?:-[a-z0-9]+)*$'},
                  'description': {'type': 'string', 'minLength': 1, 'maxLength': 1024},
                  'license': {'type': 'string', 'minLength': 1}}})
        if meta['name'] != root.name:
            raise ValueError('name must match installable directory')
        if len(text.splitlines()) > 100:
            raise ValueError('entrypoint exceeds the project context budget')
        for workflow in ('direct','critique','refine','discover','design','build','reference-translation'):
            inside(root, f'workflows/{workflow}.md')
        inside(root, 'LICENSE')
        inside(root, 'agents/openai.yaml')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    return errors


def validate_repository(root=ROOT):
    errors = validate(root / 'creative-director')
    try:
        records = read_json(root / 'maintenance/knowledge/comparisons.json')
        ids = set()
        for record in records:
            validate_comparison(record, root)
            if record['id'] in ids:
                raise ValueError('duplicate comparison ID')
            ids.add(record['id'])
        validate_record(read_json(root / 'maintenance/knowledge/profile.example.json'), 'profile', root)
        scenarios = read_json(root / 'tests/scenarios.json')
        if len(scenarios) < 25:
            raise ValueError('evaluation suite is incomplete')
        ids, modes, negatives = set(), set(), 0
        for scenario in scenarios:
            validate_record(scenario, 'scenario', root)
            if scenario['id'] in ids:
                raise ValueError('duplicate scenario ID')
            ids.add(scenario['id'])
            if scenario['activation'] == (scenario['mode'] == 'NONE'):
                raise ValueError('activation contradicts mode')
            modes.add(scenario['mode'])
            negatives += not scenario['activation']
            if not scenario['objective_checks'] or not scenario['human_criteria'] or not scenario['failure_conditions']:
                raise ValueError('scenario lacks review criteria')
            for reference in scenario['references']:
                inside(root, reference)
            if scenario['fixture']:
                inside(root, scenario['fixture'])
        if modes != {'DIRECT','CRITIQUE','REFINE','DISCOVER','DESIGN','BUILD','NONE'} or negatives < 5:
            raise ValueError('missing positive or negative evaluation coverage')
        manifest = read_json(root / 'release-manifest.json')
        paths = [inside(root, path) for path in manifest['repository_files']]
        errors.extend(markdown_errors([path for path in paths if path.suffix == '.md'], root))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    return errors


if __name__ == '__main__':
    errors = validate_repository()
    print(json.dumps({'status': 'failed' if errors else 'passed', 'errors': errors}, indent=2))
    raise SystemExit(bool(errors))
