# Knowledge and reviewed learning

Technical sources, subjective taste and project evidence are separate layers. Use only relevant records. The [source register](sources.json) stores primary links, document/version context, review date, supported claims and retrieval status. References contain original summaries rather than copied manuals. A reachable URL does not establish that a claim is true or current.

## Comparisons

[Comparisons](comparisons.json) follow [the comparison schema](comparison.schema.json). Each record contains a task, context, references, options, preference, rationale, judgment category, principle, exceptions and confidence/review status. Bundled examples are synthetic, not historical user feedback. An empty visual-reference list means a text-only example, not a missing screenshot. Visual assets belong in `assets/comparisons/`; annotations reference their paths relative to the skill root. The validator checks every path exists and stays inside the skill.

Add a record without overwriting others:

```sh
python scripts/knowledge.py add-comparison path/to/record.json
python scripts/validate_skill.py
```

Use a stable unique ID. State whether the provenance is synthetic or approved public feedback; record publication consent for the latter. Do not put private project names or assets in public records by default.

## Personal configuration

Copy [the profile example](profile.example.json) to `.creative-director.local.json` in the target project root. Both that filename and `private/` should be ignored in that project's Git configuration. Profiles live outside the installed skill to survive upgrades. Validate using `python scripts/knowledge.py validate-profile /path/to/.creative-director.local.json`.

Describe preferences with context, reason, exception and evidence level (`explicit` or `inferred`). Use paths relative to the profile directory for private case files. Load only files permitted by the session; a profile cannot grant filesystem permissions. Case studies use [the case schema](case.schema.json). Record objectives, accepted/rejected decisions, constraints, reasoning, lessons, generalizable principles and exceptions. An unknown decision is an empty list, never an invented rejection. Distinguish documentation observations from explicit user approval.

## Feedback lifecycle

1. Record approved/rejected recommendations, corrected implementations, repeated failures or successes under the ignored `private/feedback/` folder using [the feedback schema](feedback.schema.json). Preserve evidence and uncertainty.
2. Run `python scripts/knowledge.py candidate private/feedback/event.json private/candidates/proposal.json` to create a proposal. The source event remains unchanged. A single subjective event is a local hypothesis, not a universal rule.
3. Human review should inspect provenance, scope, counterexamples, recurrence and relevant regression coverage. A reviewer writes a separate approval file using [the approval schema](approval.schema.json). The CLI records an attestation; it cannot authenticate a human identity.
4. Only after that review: `python scripts/knowledge.py promote private/candidates/proposal.json --approval-file private/approval.json --output taste/reviewed/my-rule.json`. A promotion requires matching IDs, an approved decision, human attestation, rationale, date and a regression scenario ID. No overwrites. Promotion creates a reviewable record; it does not rewrite SKILL.md or silently load every rule. Route an approved rule from taste only after reviewing a Git diff.
5. Version-control intentionally selected public changes and regression tests; keep proprietary evidence private. Git-ignore is not a privacy audit. Public packaging uses an allowlist and excludes private data independently.

## Source checks

Run `python scripts/check_references.py` offline for local links, asset paths and source metadata; use `--online` for a bounded HTTP GET per registered URL and JSON status output. Network failures are reported as unresolved, never rewritten as successful reviews. A human must reread changed/version-sensitive guidance and update the register. See [source review](source-review.md).
