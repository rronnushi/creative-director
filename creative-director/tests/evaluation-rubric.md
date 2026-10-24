# Baseline versus skill evaluation

Status: **full Codex and Claude Code paired evaluations pending**. Scenario files are test specifications, not measured outcomes. Python tests establish tooling invariants only. An independent smoke critique, if recorded, is not a cross-agent effectiveness study.

## Reproduce a pair

1. Run `python scripts/prepare_evaluation.py ../evaluation-runs/run-001 --scenario landing-critique` from the skill directory. Omit `--scenario` for all 30 pairs. Outputs contain tasks and available raw fixtures, never expected answers. Most scenarios are contextual briefs; supply the same authorized real project/artifacts to both arms for project-specific evaluation. Missing material should lead to an evidence limitation, not invented findings.
2. Use fresh isolated sessions of the **same agent/model/version/settings/tool permissions**, identical project snapshots, time and token budgets. Baseline must not discover Creative Director or its references in parent/user locations. Install it only for the skill arm. Keep private profiles identical or absent. Record all other skills and instructions.
3. Run each task in its own workspace. Retain transcripts, file diffs, tests, screenshots with viewport/state and actual measurements. Do not supply `scenarios.json` to the agent being tested. Reviewers can use it afterward.
4. For Codex use `$creative-director` for explicit checks and omit explicit invocation for natural activation checks. For Claude Code use `/creative-director`; also test natural-language routing in a fresh session. Verify actual resource loading from logs where available. Negative tasks should not load the skill.
5. Randomize output order and blind reviewers to treatment. Use at least two human reviewers for subjective comparisons where practical. Repeat several runs for variable generation; predeclare sample size and report all runs, failures and exclusions. Do not cherry-pick attractive outputs.
6. Mark objective checks pass/fail/not-assessed. Score human dimensions independently and attach evidence. Report paired differences and disagreements; small samples do not establish general effectiveness. Record unavailable browser or runtime evidence separately from failure.

## Anchored human rubric

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Requirement satisfaction | Misses core task | Main task met with material omissions | All explicit requirements met with evidence |
| Actionability | Vague advice | Some concrete changes | Remedies map to locations, actions and verification |
| Visual consistency | Conflicting hierarchy/system | Mostly coherent | Deliberate coherent roles across relevant states |
| Creative distinctiveness | Interchangeable defaults | Clear but familiar direction | Memorable task-specific concept expressed in decisions |
| Correctness | Verified substantive defects | Works with known gaps | Relevant behavior and boundaries verified |
| Scope discipline | Unrelated changes | Minor unnecessary expansion | Small complete solution respects constraints |
| Technical quality | Fragile or unmaintainable | Adequate architecture/checks | Appropriate existing patterns and meaningful validation |
| Complexity economy | Adds unjustified burdens | Some redundancy | Every major feature/dependency earns its cost |
| Preservation | Breaks working behavior/identity | Partially preserved | Relevant prior behavior and identity explicitly verified |

Use 2/4 for intermediate evidence, and not-assessed when the dimension cannot be judged. Scores are contextual human judgments, not objective measurements. Severe regressions cannot be hidden by averaging visual scores.

## Result record

Store private runs outside the package. Record: run/scenario ID, date, agent/model/build, skill Git revision, settings, task/artifact hashes, environment and tools, budgets, transcript/artifact paths, objective checks, per-dimension ratings with evidence, reviewer, exclusions and uncertainty. Baseline and skill must both actually execute before marking a pair complete. Pending entries have no score. Public results require review for private data and honest disclosure of sample size and limitations.
