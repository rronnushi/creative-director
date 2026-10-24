"""Tooling regression tests; these do not execute or grade a coding agent."""
import copy
import datetime as dt
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from urllib.error import URLError
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from common import ROOT, check, inside, read_json, validate_comparison, validate_record, write_new
from check_references import local_errors, probe
from knowledge import add_comparison, candidate, promote
from package_release import package, release_files
from prepare_evaluation import prepare
from validate_skill import validate


class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.comparison = copy.deepcopy(read_json(ROOT / 'knowledge/comparisons.json')[0])
        self.event = {
            'id': 'identity-feedback', 'kind': 'rejected-recommendation',
            'context': 'Expressive festival page', 'recommendation': 'Remove all colour',
            'outcome': 'Rejected: preserve established identity', 'evidence': ['Human review note'],
            'proposed_principle': 'Preserve explicit identity during refinement',
            'exceptions': ['Approved rebrand'], 'confidence': 'medium',
            'regression_scenario': 'preserve-identity'}
        self.approval = {'candidate_id': 'identity-feedback-candidate', 'decision': 'approved',
                         'reviewer': 'Synthetic test reviewer', 'reviewer_type': 'human',
                         'reviewed_on': dt.date.today().isoformat(),
                         'rationale': 'Synthetic fixture only; not real human approval',
                         'regression_scenario': 'preserve-identity'}

    def clone(self):
        target = self.work / 'creative-director'
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('__pycache__'))
        return target

    def test_repository_validates(self):
        self.assertEqual(validate(), [])

    def test_links_validate(self):
        self.assertEqual(local_errors(), [])

    def test_comparison_valid(self):
        validate_comparison(self.comparison)

    def test_missing_rationale_rejected(self):
        del self.comparison['rationale']
        with self.assertRaises(ValueError):
            validate_comparison(self.comparison)

    def test_invented_provenance_rejected(self):
        self.comparison['provenance'] = 'real-user-trust-me'
        with self.assertRaises(ValueError):
            validate_comparison(self.comparison)

    def test_synthetic_cannot_be_user_review(self):
        self.comparison['review_status'] = 'reviewed'
        with self.assertRaises(ValueError):
            validate_comparison(self.comparison)

    def test_public_feedback_requires_consent(self):
        self.comparison.update(provenance='public-feedback', review_status='reviewed')
        with self.assertRaises(ValueError):
            validate_comparison(self.comparison)

    def test_missing_visual_asset_rejected(self):
        self.comparison['visual_references'] = ['assets/nonexistent.svg']
        with self.assertRaises(ValueError):
            validate_comparison(self.comparison)

    def test_traversal_rejected(self):
        with self.assertRaises(ValueError):
            inside(ROOT, '../README.md')

    def test_windows_path_rejected(self):
        with self.assertRaises(ValueError):
            inside(ROOT, 'C:/private/secret.svg')

    def test_backslash_path_rejected(self):
        with self.assertRaises(ValueError):
            inside(ROOT, 'tests\\fixtures\\reference.svg')

    def test_duplicate_json_key_rejected(self):
        path = self.work / 'bad.json'
        path.write_text('{"id":"a","id":"b"}', encoding='utf-8')
        with self.assertRaises(ValueError):
            read_json(path)

    def test_unsupported_schema_keyword_rejected(self):
        with self.assertRaises(ValueError):
            check({}, {'oneOf': []})

    def test_false_is_not_version_one(self):
        with self.assertRaises(ValueError):
            check(True, {'const': 1})

    def test_invalid_date_rejected(self):
        with self.assertRaises(ValueError):
            check('2026-02-30', {'type': 'string', 'format': 'date'})

    def test_blank_string_rejected(self):
        with self.assertRaises(ValueError):
            check('  ', {'type': 'string', 'minLength': 1})

    def test_candidate_does_not_promote(self):
        result = candidate(self.event)
        self.assertEqual(result['status'], 'candidate')
        self.assertEqual(self.event['outcome'], 'Rejected: preserve established identity')

    def test_candidate_requires_evidence_field(self):
        del self.event['evidence']
        with self.assertRaises(ValueError):
            candidate(self.event)

    def test_empty_evidence_cannot_become_candidate(self):
        self.event['evidence'] = []
        with self.assertRaises(ValueError):
            candidate(self.event)

    def test_promotion_requires_matching_approval(self):
        self.approval['candidate_id'] = 'other-candidate'
        with self.assertRaises(ValueError):
            promote(candidate(self.event), self.approval)

    def test_manual_empty_evidence_candidate_cannot_promote(self):
        proposal = candidate(self.event)
        proposal['evidence'] = []
        with self.assertRaises(ValueError):
            promote(proposal, self.approval)

    def test_rejected_approval_cannot_promote(self):
        self.approval['decision'] = 'rejected'
        with self.assertRaises(ValueError):
            promote(candidate(self.event), self.approval)

    def test_agent_cannot_attest_human_review(self):
        self.approval['reviewer_type'] = 'agent'
        with self.assertRaises(ValueError):
            promote(candidate(self.event), self.approval)

    def test_future_approval_rejected(self):
        self.approval['reviewed_on'] = (dt.date.today() + dt.timedelta(days=1)).isoformat()
        with self.assertRaises(ValueError):
            promote(candidate(self.event), self.approval)

    def test_promotion_requires_existing_regression(self):
        self.event['regression_scenario'] = 'missing-scenario'
        self.approval['regression_scenario'] = 'missing-scenario'
        with self.assertRaises(ValueError):
            promote(candidate(self.event), self.approval)

    def test_attested_promotion_retains_context(self):
        result = promote(candidate(self.event), self.approval)
        self.assertEqual(result['context'], self.event['context'])
        self.assertEqual(result['status'], 'approved-for-review')

    def test_new_write_cannot_overwrite(self):
        target = self.work / 'event.json'
        write_new(target, self.event)
        with self.assertRaises(FileExistsError):
            write_new(target, {})
        self.assertEqual(read_json(target), self.event)

    def test_add_duplicate_does_not_change_dataset(self):
        root = self.clone()
        before = (root / 'knowledge/comparisons.json').read_bytes()
        with self.assertRaises(ValueError):
            add_comparison(self.comparison, root)
        self.assertEqual((root / 'knowledge/comparisons.json').read_bytes(), before)

    def test_add_comparison_preserves_others(self):
        root = self.clone()
        previous = read_json(root / 'knowledge/comparisons.json')
        self.comparison['id'] = 'new-synthetic-record'
        add_comparison(self.comparison, root)
        self.assertEqual(read_json(root / 'knowledge/comparisons.json'), previous + [self.comparison])

    def test_missing_local_link_detected(self):
        root = self.clone()
        (root / 'references/visual-design.md').unlink()
        self.assertTrue(any('visual-design' in err for err in local_errors(root)))

    def test_invalid_frontmatter_rejected(self):
        root = self.clone()
        (root / 'SKILL.md').write_text('---\n{"name":"BAD"}\n---\nBody', encoding='utf-8')
        self.assertTrue(validate(root))

    def test_negative_activation_contradiction_rejected(self):
        root = self.clone()
        path = root / 'tests/scenarios.json'
        records = read_json(path)
        records[0]['activation'] = False
        path.write_text(json.dumps(records), encoding='utf-8')
        self.assertTrue(validate(root))

    def test_network_failure_not_success(self):
        def fail(*args, **kwargs):
            raise URLError('test offline')
        self.assertEqual(probe('https://example.org', fail)['status'], 'unresolved')

    def test_redirect_reported(self):
        class Response:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *args): return False
            def geturl(self): return 'https://example.org/new'
            def read(self, limit): return b'page'
        self.assertEqual(probe('https://example.org', lambda *a, **k: Response())['status'], 'redirected')

    def test_evaluation_pairs_are_pending_and_answers_hidden(self):
        output = self.work / 'pairs'
        manifest = prepare(output, ['landing-critique'])
        self.assertEqual(manifest['status'], 'pending-agent-execution')
        task = (output / 'landing-critique/baseline/task.md').read_text(encoding='utf-8')
        self.assertNotIn('unlabeled', task)
        self.assertNotIn('Creative Director', task)
        self.assertTrue((output / 'landing-critique/skill/landing.html').is_file())

    def test_unknown_evaluation_scenario_rejected(self):
        with self.assertRaises(ValueError):
            prepare(self.work / 'pairs', ['invented'])
        self.assertFalse((self.work / 'pairs').exists())

    def test_package_roundtrip_excludes_private(self):
        root = self.clone()
        (root / 'private').mkdir()
        (root / 'private/secret.json').write_text('{"secret":"private"}', encoding='utf-8')
        (root / '.creative-director.local.json').write_text('{}', encoding='utf-8')
        target = self.work / 'release.zip'
        report = package(target, root)
        with ZipFile(target) as archive:
            self.assertTrue(all('private' not in name and '.local.' not in name for name in archive.namelist()))
            self.assertEqual(archive.read('creative-director/SKILL.md'), (ROOT / 'SKILL.md').read_bytes())
            extracted = self.work / 'unpacked'
            archive.extractall(extracted)
        self.assertEqual(validate(extracted / 'creative-director'), [])
        self.assertGreater(report['entries'], 20)

    def test_private_manifest_entry_rejected(self):
        root = self.clone()
        (root / '.creative-director.local.json').write_text('{}', encoding='utf-8')
        path = root / 'release-manifest.json'
        manifest = read_json(path)
        manifest['files'].append('.creative-director.local.json')
        path.write_text(json.dumps(manifest), encoding='utf-8')
        with self.assertRaises(ValueError):
            release_files(root)

    def test_unlisted_public_file_rejected(self):
        root = self.clone()
        (root / 'references/new.md').write_text('New knowledge', encoding='utf-8')
        with self.assertRaises(ValueError):
            release_files(root)


if __name__ == '__main__':
    unittest.main()
