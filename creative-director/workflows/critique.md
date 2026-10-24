# CRITIQUE

Read quality standards. Inspect the requested surface and relevant implementation. Record evidence available: files/lines, screenshots with viewport, interaction steps, tool output. If only code is available, make a code-based review and mark visual assessment pending.

1. State the product's apparent purpose and what already works, citing evidence.
2. Evaluate the five dimensions in quality standards. Check the main task before incidental decoration. Cover relevant responsive, accessibility and performance risks without turning the review into an unrelated audit.
3. Write each finding as: **priority — problem; evidence/location; classification; user impact; remedy; confidence; effort; verification**. Suggested priority: P0 blocks the core task, P1 seriously impairs it, P2 improves clarity/coherence, P3 optional polish. Confidence is high/medium/low based on evidence, not rhetorical certainty. Effort is S/M/L relative to this project.
4. Order by impact, then confidence and effort. Group repeated symptoms under one root cause. Distinguish verified defects from stylistic alternatives. Preserve successful identity and interactions in remedies.
5. Finish with the smallest useful change sequence and unverified areas. Do not change files for a critique-only request.

Example: P1, verified defect, high confidence, S: at 360px the fixed 420px filter bar exceeds its container (screenshot and CSS rule). It hides the submit action. Allow wrapping and use `min-width: 0` on the flex child; verify keyboard reachability and no page overflow at 320/360px. “Make it modern” is not a finding.
