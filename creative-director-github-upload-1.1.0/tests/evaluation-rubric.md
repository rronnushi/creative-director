# Check the skill through real use

Prepared scenarios are not executed evaluations. Full paired Codex and Claude Code evaluations remain pending.

Start with a few useful tasks: review an interface without editing, suggest a direction, refine one part of an existing app, work on seeded artwork and answer an unrelated request without activating.

For an optional baseline comparison, prepare isolated pairs:

```sh
python scripts/prepare_evaluation.py evaluation-runs/run-001 --scenario landing-critique
```

Give both sessions the same task, project snapshot, model settings, permissions and budget. Only the skill session should have Creative Director installed. Don't expose this guide or expected criteria to the agent during the task.

Afterward, review the actual output and changes:
- Did it handle the user's request?
- Was the advice specific, understandable and appropriately brief?
- Did it respect scope and preserve the existing identity and behavior?
- Did the work have a coherent direction?
- Did it distinguish observations from preferences and unchecked assumptions?
- Were the implementation and relevant checks sound?
- Did it avoid unnecessary features, dependencies and ceremony?

Use pass/fail/not-assessed for objective checks. For subjective comparisons, explain the preference and use more than one reviewer when practical. Numerical scores are optional, not proof.

Keep transcripts, diffs, screenshots and actual test results privately with the configuration used. Record failures and missing evidence. Don't publish private artifacts, invent scores or claim general improvement from a handful of examples.
