# Optional knowledge records

These files support maintenance. They are not installed with the skill.

- [Comparisons](comparisons.json) contain clearly labeled invented A/B examples. Real public feedback needs publication consent.
- [The profile example](profile.example.json) keeps the existing `.creative-director.local.json` format.
- The schema files describe comparisons, profiles, private case studies, feedback, candidates, approvals, sources and evaluation scenarios.

Keep visual assets separate from their annotations; asset paths in comparisons are relative to the installable skill folder. Only intentionally public assets belong there.

For feedback, use the feedback schema to record what was recommended, what happened and the supporting evidence. Then:

```sh
python scripts/knowledge.py candidate private/feedback/event.json private/candidates/proposal.json
python scripts/knowledge.py promote private/candidates/proposal.json --approval-file private/approval.json --output private/reviewed/rule.json
```

Run these from the repository root. Promotion needs a matching human approval record and a real regression-scenario ID. It records an attestation; it cannot authenticate a person's identity. Review the proposed rule and its exceptions before making any shared change.

See [the maintainer guide](../../docs/maintenance.md) for checks and packaging.
