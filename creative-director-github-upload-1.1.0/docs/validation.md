# Development checks

Version 1.1.0 was checked locally on 2026-11-10.

- The metadata, local links, source records and maintenance datasets passed validation.
- All 42 tooling tests passed, including installed-skill and source-archive round trips, private-file exclusion, profile compatibility and human approval requirements.
- The installed folder contains 20 files, down from 65. Its text and data occupy about 35 KB instead of 146 KB. Tests, evaluation fixtures, schemas and Python tools are no longer installed.
- The README is 546 words, down from 966. Everyday critique no longer requires scores, severity codes or a fixed set of audit fields.
- An independent agent tried two requests: a read-only review of the HTML fixture and a direction for an urban-photography site. It gave specific advice without audit labels, stated the lack of rendering evidence and made no edits. This is a small behavior check, not a controlled effectiveness study.

Existing private profiles and case records still validate. They are not included in either public archive. The previous public source was saved as a local rollback ZIP before restructuring.

The source review dates have not been refreshed by this wording change. The Three.js source remains marked partial; version-specific APIs still need checking when used. No new online link results or live GitHub CI results are claimed here.

Full paired Codex and Claude Code evaluations remain pending. The [evaluation guide](../tests/evaluation-rubric.md) describes how to run them. These local checks do not establish better creative outcomes, complete accessibility or cross-platform compatibility.
