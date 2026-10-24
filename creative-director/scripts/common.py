"""Dependency-free validation for the deliberately small bundled JSON Schema subset."""
import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
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
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))


def read_json(path):
    return parse_json(Path(path).read_text(encoding='utf-8'))


def check(value, schema, location='$'):
    """Validate supported keywords; reject unknown ones rather than silently ignoring."""
    unknown = set(schema) - KEYWORDS
    if unknown:
        raise ValueError(f'{location}: unsupported schema keywords {sorted(unknown)}')
    kinds = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'integer': int}
    kind = schema.get('type')
    if kind:
        if kind not in kinds:
            raise ValueError(f'unsupported type {kind}')
        if type(value) is not kinds[kind]:
            raise ValueError(f'{location}: expected {kind}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{location}: invalid enum {value!r}')
    if 'const' in schema and (type(value) is not type(schema['const']) or value != schema['const']):
        raise ValueError(f'{location}: expected constant {schema["const"]!r}')
    if isinstance(value, dict):
        missing = set(schema.get('required', [])) - value.keys()
        if missing:
            raise ValueError(f'{location}: missing {sorted(missing)}')
        properties = schema.get('properties', {})
        if schema.get('additionalProperties') is False and value.keys() - properties.keys():
            raise ValueError(f'{location}: unknown fields {sorted(value.keys() - properties.keys())}')
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
        if schema.get('format') == 'date':
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                raise ValueError(f'{location}: expected ISO date')
            dt.date.fromisoformat(value)
        elif schema.get('format') == 'uri':
            parts = urlsplit(value)
            if parts.scheme != 'https' or not parts.hostname or parts.username or parts.password:
                raise ValueError(f'{location}: expected public HTTPS URL')
        elif schema.get('format') not in (None, 'date'):
            raise ValueError(f'{location}: unsupported format')


def validate_record(value, name, root=ROOT):
    check(value, read_json(root / 'knowledge' / f'{name}.schema.json'))


def inside(root, relative, require_file=True):
    """Reject absolute paths, traversal and symlink escapes in public records."""
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
        raise ValueError('synthetic records must remain illustrative')
    if record['provenance'] == 'public-feedback' and not record['publication_consent']:
        raise ValueError('public feedback requires publication consent')
    for asset in record['visual_references']:
        inside(root, asset)


def write_new(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write('\n')
