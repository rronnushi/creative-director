"""Add comparisons and prepare human-reviewed knowledge changes; no automatic learning."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import tempfile
from common import ROOT, read_json, validate_comparison, validate_record, write_new


def add_comparison(record, root=ROOT):
    validate_comparison(record, root)
    path = root / 'knowledge/comparisons.json'
    records = read_json(path)
    if any(r['id'] == record['id'] for r in records):
        raise ValueError('comparison ID already exists')
    # Atomic replacement avoids a partially written dataset if interrupted.
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        json.dump(records + [record], handle, indent=2, ensure_ascii=False)
        handle.write('\n')
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def candidate(event):
    validate_record(event, 'feedback')
    if not event['evidence']:
        raise ValueError('feedback requires evidence before becoming a candidate')
    return {'id': event['id'] + '-candidate', 'feedback_id': event['id'], 'status': 'candidate',
            'proposed_principle': event['proposed_principle'], 'context': event['context'],
            'exceptions': event['exceptions'], 'evidence': event['evidence'],
            'regression_scenario': event['regression_scenario']}


def promote(proposal, approval, root=ROOT):
    validate_record(proposal, 'candidate', root)
    validate_record(approval, 'approval', root)
    if not proposal['evidence']:
        raise ValueError('candidate evidence cannot be empty')
    if approval['candidate_id'] != proposal['id'] or approval['decision'] != 'approved':
        raise ValueError('matching human approval required')
    if dt.date.fromisoformat(approval['reviewed_on']) > dt.date.today():
        raise ValueError('approval date cannot be in the future')
    if approval['regression_scenario'] != proposal['regression_scenario']:
        raise ValueError('regression scenario must match candidate')
    scenarios = read_json(root / 'tests/scenarios.json')
    if proposal['regression_scenario'] not in {s['id'] for s in scenarios}:
        raise ValueError('regression scenario does not exist')
    return {'id': proposal['id'], 'status': 'approved-for-review',
            'rule': proposal['proposed_principle'], 'context': proposal['context'],
            'exceptions': proposal['exceptions'], 'approval': approval,
            'feedback_id': proposal['feedback_id']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    add = sub.add_parser('add-comparison'); add.add_argument('record', type=Path)
    profile = sub.add_parser('validate-profile'); profile.add_argument('profile', type=Path)
    prepare = sub.add_parser('candidate'); prepare.add_argument('event', type=Path); prepare.add_argument('output', type=Path)
    promotion = sub.add_parser('promote'); promotion.add_argument('candidate', type=Path)
    promotion.add_argument('--approval-file', required=True, type=Path)
    promotion.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'add-comparison':
            add_comparison(read_json(args.record))
        elif args.command == 'validate-profile':
            profile = read_json(args.profile)
            validate_record(profile, 'profile')
            for relative in profile['case_files']:
                path = Path(relative)
                if path.is_absolute() or ':' in relative:
                    raise ValueError('private case paths must be relative to the profile')
                validate_record(read_json(args.profile.parent / path), 'case')
        elif args.command == 'candidate':
            write_new(args.output, candidate(read_json(args.event)))
        else:
            write_new(args.output, promote(read_json(args.candidate), read_json(args.approval_file)))
        print('Completed. Review the diff before committing or sharing.')
        return 0
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
