"""Small, dependency-free helpers for repository tooling."""
import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'creative-director'
KEYWORDS = {'$schema', 'title', 'description', 'type', 'required', 'properties',
            'additionalProperties', 'items', 'minItems', 'minLength', 'maxLength',
            'enum', 'const', 'pattern', 'format'}


def parse_json(text):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'duplicate JSON key: {key}')
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=unique,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def read_json(path):
    return parse_json(Path(path).read_text(encoding='utf-8'))


def frontmatter(text):
    """Read the flat YAML fields this skill uses, without a YAML dependency."""
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        raise ValueError('missing frontmatter')
    try:
        end = lines.index('---', 1)
    except ValueError as exc:
        raise ValueError('unclosed frontmatter') from exc
    result = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.startswith((' ', '\t')) or ':' not in line:
            raise ValueError('frontmatter must use flat key/value fields')
        key, value = line.split(':', 1)
        value = value.strip()
        if key in result:
            raise ValueError(f'duplicate frontmatter key: {key}')
        if value.startswith('"'):
            value = parse_json(value)
        elif not re.fullmatch(r'[a-zA-Z0-9-]+', value):
            raise ValueError('quote frontmatter values containing spaces or punctuation')
        result[key] = value
    return result


def check(value, schema, location='$'):
    """Enforce our bundled JSON Schema subset; fail on unsupported keywords."""
    unknown = set(schema) - KEYWORDS
    if unknown:
        raise ValueError(f'{location}: unsupported schema keywords {sorted(unknown)}')
    kinds = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'integer': int}
    kind = schema.get('type')
    if kind and (kind not in kinds or type(value) is not kinds[kind]):
        raise ValueError(f'{location}: expected {kind}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{location}: invalid enum')
    if 'const' in schema and (type(value) is not type(schema['const']) or value != schema['const']):
        raise ValueError(f'{location}: invalid constant')
    if isinstance(value, dict):
        properties = schema.get('properties', {})
        if set(schema.get('required', [])) - value.keys():
            raise ValueError(f'{location}: missing fields')
        if schema.get('additionalProperties') is False and value.keys() - properties.keys():
            raise ValueError(f'{location}: unknown fields')
        for key in value.keys() & properties.keys():
            check(value[key], properties[key], f'{location}.{key}')
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            raise ValueError(f'{location}: too few items')
        for index, item in enumerate(value):
            check(item, schema.get('items', {}), f'{location}[{index}]')
    if isinstance(value, str):
        if len(value.strip()) < schema.get('minLength', 0) or len(value) > schema.get('maxLength', float('inf')):
            raise ValueError(f'{location}: invalid string length')
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            raise ValueError(f'{location}: invalid pattern')
        format_ = schema.get('format')
        if format_ == 'date':
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                raise ValueError('expected ISO date')
            dt.date.fromisoformat(value)
        elif format_ == 'uri':
            parts = urlsplit(value)
            if parts.scheme != 'https' or not parts.hostname or parts.username or parts.password:
                raise ValueError('expected public HTTPS URL')
        elif format_ is not None:
            raise ValueError(f'unsupported format {format_}')


def validate_record(value, name, root=ROOT):
    check(value, read_json(root / 'maintenance/knowledge' / f'{name}.schema.json'))


def inside(root, relative, require_file=True):
    if not relative or Path(relative).is_absolute() or '\\' in relative or ':' in relative:
        raise ValueError(f'invalid relative path: {relative}')
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f'path escapes root: {relative}')
    if require_file and not target.is_file():
        raise ValueError(f'missing file: {relative}')
    return target


def validate_comparison(record, root=ROOT):
    validate_record(record, 'comparison', root)
    if record['provenance'] == 'synthetic' and record['review_status'] != 'illustrative':
        raise ValueError('synthetic records must stay illustrative')
    if record['provenance'] == 'public-feedback' and not record['publication_consent']:
        raise ValueError('public feedback requires publication consent')
    for asset in record['visual_references']:
        inside(root / 'creative-director', asset)


def write_new(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write('\n')
