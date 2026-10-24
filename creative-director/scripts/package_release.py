"""Build an allowlisted ZIP and verify its entries; never include private configuration."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from common import ROOT, inside, read_json
from validate_skill import validate


def release_files(root=ROOT):
    manifest = read_json(root / 'release-manifest.json')
    if manifest['version'] != '1.0.0' or not manifest['files']:
        raise ValueError('invalid release manifest')
    files, seen = [], set()
    for relative in manifest['files']:
        path = inside(root, relative)
        original = root / relative
        if original.absolute() != original.resolve():
            raise ValueError(f'symlinked release path: {relative}')
        if relative in seen:
            raise ValueError('duplicate release entry')
        seen.add(relative)
        if any(part.startswith('.') or part in {'private', '__pycache__', 'evaluation-runs'} for part in Path(relative).parts):
            raise ValueError(f'private or generated path in release: {relative}')
        if path.suffix not in {'.md', '.json', '.yaml', '.py', '.svg', '.html', '.jsx'} and path.name != 'LICENSE':
            raise ValueError(f'unsupported release file: {relative}')
        files.append((relative, path))
    # Fail if a new public source is accidentally omitted from the allowlist.
    for directory in ('agents','references','workflows','taste','knowledge','checklists','examples','scripts','tests'):
        for path in (root / directory).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts and path.relative_to(root).as_posix() not in seen:
                raise ValueError(f'public file omitted from manifest: {path.relative_to(root)}')
    return files


def package(output, root=ROOT):
    errors = validate(root)
    if errors:
        raise ValueError('; '.join(errors))
    files = release_files(root)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Refuse overwrite so an earlier artifact remains available for comparison.
    with ZipFile(output, 'x', compression=ZIP_DEFLATED) as archive:
        for relative, path in sorted(files):
            archive.writestr(f'creative-director/{relative}', path.read_bytes())
    with ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP CRC check failed')
        expected = {f'creative-director/{relative}' for relative, _ in files}
        if set(archive.namelist()) != expected or any('\\' in name for name in archive.namelist()):
            raise ValueError('ZIP entries do not match allowlist')
        for relative, path in files:
            if archive.read(f'creative-director/{relative}') != path.read_bytes():
                raise ValueError(f'ZIP content mismatch: {relative}')
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return {'file': str(output), 'entries': len(files), 'sha256': digest}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(package(args.output), indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
