# Quality standards

Load for critique and final review. Assess the user's task and context, not conformity to one style.

| Dimension | Questions and evidence | Possible correction |
| --- | --- | --- |
| Concept and distinctiveness | Is there a useful promise and an organizing idea visible in composition/behavior? Compare representative surfaces, not branding adjectives. | Strengthen the primary loop or one signature decision before adding effects. |
| Visual coherence | Do hierarchy, alignment, type roles, palette and spacing follow a discernible system? Inspect real long content and relevant states. | Fix a shared token or layout relationship rather than hand-tuning every instance. |
| Interaction and usability | Can the audience discover, complete and recover from the main task with keyboard/touch? Check loading, empty, error and narrow layouts. | Clarify the next action, feedback and recovery; preserve user state. |
| Technical execution | Do behavior, export and responsive rendering work? What do tests, traces and implementation show? | Correct the cause with existing architecture; measure suspected bottlenecks. |
| Simplicity and restraint | Does each control, effect and dependency earn its cost? Is complexity intrinsic to the task? | Remove duplication or hide secondary choices without losing essential capabilities. |

Optional scores: 1 = core purpose obstructed; 2 = major weaknesses; 3 = adequate with material gaps; 4 = strong with limited gaps; 5 = unusually well resolved for the brief. Give evidence and context per dimension. Use **not assessed** when evidence is missing. Do not average unavailable evidence into a flattering total. A severe functional defect remains a defect regardless of visual scores.

Review order: complete the central task → preserve identity/functionality → verify coherence → consider distinctiveness and polish. A maximalist interface can score highly on restraint when its density and effects have clear roles. A sparse interface can score poorly when it hides essential information.

For findings use the contract in [CRITIQUE](../workflows/critique.md). Automated checks can verify behavior or measurements, not originality, usability for every user or aesthetic acceptance. Record tool/environment, viewport/state, source location and uncertainty. The comparative human evaluation protocol is [the rubric](../tests/evaluation-rubric.md).
