"""Check local Markdown links and registered sources. Online checks never assert truth."""
import argparse
import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from common import ROOT, inside, read_json, validate_record


def local_errors(root=ROOT):
    errors = []
    for path in root.rglob('*.md'):
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            href = match.group(1).strip().strip('<>')
            if not href or href.startswith('#') or urlsplit(href).scheme in ('http', 'https', 'mailto'):
                continue
            href = unquote(href.split('#', 1)[0])
            try:
                resolved = (path.parent / href).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                    raise ValueError('missing or outside skill')
            except ValueError as exc:
                errors.append(f'{path.relative_to(root)}: {href}: {exc}')
    try:
        sources = read_json(root / 'knowledge/sources.json')
        ids = set()
        for source in sources:
            validate_record(source, 'source', root)
            if source['id'] in ids:
                raise ValueError('duplicate source ID')
            ids.add(source['id'])
            if dt.date.fromisoformat(source['reviewed_on']) > dt.date.today():
                raise ValueError('source review date is in the future')
            if source['status'] == 'reviewed' and not source['claims']:
                raise ValueError('reviewed source has no supported claims')
        for path in (root / 'references').glob('*.md'):
            for source_id in re.findall(r'Technical source: \*\*([^*]+)\*\*', path.read_text(encoding='utf-8')):
                if source_id not in ids:
                    errors.append(f'{path.name}: unknown source {source_id}')
    except (ValueError, OSError) as exc:
        errors.append(str(exc))
    return errors


def probe(url, opener=urlopen):
    result = {'url': url, 'checked_at': dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        request = Request(url, headers={'User-Agent': 'CreativeDirector-LinkCheck/1.0'})
        with opener(request, timeout=15) as response:
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
    results = [probe(s['url']) for s in read_json(ROOT / 'knowledge/sources.json')] if args.online else []
    print(json.dumps({'local_errors': errors, 'online': results}, indent=2))
    return bool(errors or any(r['status'] == 'unresolved' for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
