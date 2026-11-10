"""Check local links. Optional HTTP checks report availability, not accuracy."""
import argparse
import datetime as dt
import json
import re
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from common import ROOT, SKILL, read_json, validate_record


def markdown_errors(paths, boundary):
    errors = []
    for path in paths:
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            href = match.group(1).strip().strip('<>')
            if not href or href.startswith('#') or urlsplit(href).scheme in ('http', 'https', 'mailto'):
                continue
            href = unquote(href.split('#', 1)[0])
            target = (path.parent / href).resolve()
            if not target.is_relative_to(boundary.resolve()) or not target.is_file():
                errors.append(f'{path.name}: missing or outside boundary: {href}')
    return errors


def local_errors(root=SKILL):
    errors = markdown_errors(root.rglob('*.md'), root)
    try:
        sources = read_json(root / 'references/sources.json')
        seen = set()
        for source in sources:
            validate_record(source, 'source')
            if source['id'] in seen:
                raise ValueError('duplicate source ID')
            seen.add(source['id'])
            if dt.date.fromisoformat(source['reviewed_on']) > dt.date.today():
                raise ValueError('source review date is in the future')
            if source['status'] == 'reviewed' and not source['claims']:
                raise ValueError('reviewed source has no supported claims')
        for path in (root / 'references').glob('*.md'):
            for source_id in re.findall(chr(96) + r'([a-z-]+)' + chr(96), path.read_text(encoding='utf-8')):
                if source_id in {'typography','colour','wcag','animation','canvas','svg','three','games','discovery','evals'} and source_id not in seen:
                    errors.append(f'{path.name}: unknown source {source_id}')
    except (ValueError, OSError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    return errors


def probe(url, opener=urlopen):
    result = {'url': url, 'checked_at': dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        with opener(Request(url, headers={'User-Agent': 'CreativeDirector-LinkCheck/1.1'}), timeout=15) as response:
            response.read(1024)
            result.update(status='redirected' if response.geturl() != url else 'reachable',
                          http_status=response.status, final_url=response.geturl())
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        result.update(status='unresolved', error=str(exc))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--online', action='store_true')
    args = parser.parse_args()
    errors = local_errors()
    manifest = read_json(ROOT / 'release-manifest.json')
    paths = [ROOT / path for path in manifest['repository_files'] if path.endswith('.md')]
    errors.extend(markdown_errors(paths, ROOT))
    results = [probe(source['url']) for source in read_json(SKILL / 'references/sources.json')] if args.online else []
    print(json.dumps({'local_errors': errors, 'online': results}, indent=2))
    return bool(errors or any(result['status'] == 'unresolved' for result in results))


if __name__ == '__main__':
    raise SystemExit(main())
