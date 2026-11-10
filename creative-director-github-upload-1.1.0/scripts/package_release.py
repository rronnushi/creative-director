"""Build a small skill ZIP or a public GitHub upload ZIP from explicit file lists."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from common import ROOT, inside, read_json
from validate_skill import validate_repository

BLOCKED = {'private', '.git', '__pycache__', '.test-tmp', 'evaluation-runs', 'dist', '.validation-deps'}


def selected_files(boundary, names, skill=False):
    seen, result = set(), []
    for relative in names:
        path = inside(boundary, relative)
        parts = Path(relative).parts
        if relative in seen:
            raise ValueError('duplicate release entry')
        seen.add(relative)
        if any(part in BLOCKED for part in parts) or any(part.endswith('.local.json') for part in parts):
            raise ValueError(f'private or generated path in release: {relative}')
        if skill and parts[0] not in {'SKILL.md','LICENSE','agents','references','workflows'}:
            raise ValueError(f'development file in skill release: {relative}')
        if (boundary / relative).absolute() != path:
            raise ValueError(f'symlinked release path: {relative}')
        if path.suffix not in {'.md','.json','.yaml','.yml','.py','.svg','.html','.jsx'} and path.name not in {'LICENSE','.gitignore'}:
            raise ValueError(f'unsupported release file: {relative}')
        result.append((relative, path))
    return result


def release_files(root=ROOT):
    manifest = read_json(root / 'release-manifest.json')
    if not manifest['version'] or not manifest['files']:
        raise ValueError('invalid release manifest')
    skill = root / 'creative-director'
    files = selected_files(skill, manifest['files'], skill=True)
    seen = {name for name, _ in files}
    for directory in ('agents','references','workflows'):
        for path in (skill / directory).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts and path.relative_to(skill).as_posix() not in seen:
                raise ValueError(f'unlisted skill file: {path.relative_to(skill)}')
    return files


def public_files(root=ROOT):
    manifest = read_json(root / 'release-manifest.json')
    return selected_files(root, manifest['repository_files']) + [
        (f'creative-director/{name}', path) for name, path in release_files(root)]


def package(output, root=ROOT, repository=False):
    errors = validate_repository(root)
    if errors:
        raise ValueError('; '.join(errors))
    files = public_files(root) if repository else [
        (f'creative-director/{name}', path) for name, path in release_files(root)]
    if len({name for name, _ in files}) != len(files):
        raise ValueError('duplicate archive path')
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'x', compression=ZIP_DEFLATED) as archive:
        for relative, path in sorted(files):
            archive.writestr(relative, path.read_bytes())
    with ZipFile(output) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != {name for name, _ in files}:
            raise ValueError('ZIP integrity check failed')
        for relative, path in files:
            if '\\' in relative or archive.read(relative) != path.read_bytes():
                raise ValueError(f'ZIP content mismatch: {relative}')
    return {'file': str(output), 'entries': len(files), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--repository', action='store_true', help='prepare source files for a manual GitHub upload')
    args = parser.parse_args()
    try:
        print(json.dumps(package(args.output, repository=args.repository), indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
