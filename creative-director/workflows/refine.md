# REFINE

Use for requested improvements to an existing project. Read only the references for affected areas.

1. Establish the change boundary and preservation list: working flow, identity, data/configuration and relevant performance behavior. Inspect existing components, tokens and tests. Record current behavior before edits.
2. Locate the cause instead of styling around a symptom. For an alignment problem inspect the shared layout; for palette mismatch inspect state/seed propagation. Avoid a new design system to fix one control.
3. Make the smallest complete change using existing patterns. Do not redesign unrelated surfaces or replace working logic. If wider work becomes necessary, explain the dependency and stay within authorization.
4. Run relevant tests/build checks. Exercise the affected interaction and adjacent state: keyboard focus, narrow width, loading/error where relevant. Compare rendered before/after when available; retain the same viewport/state.
5. Report changes, preservation checks, results and remaining limitations. Technical success does not establish aesthetic approval.

Example: filtered thumbnails and viewer use different colours. Preserve layout and filtering; pass the selected variant through the existing viewer state, then verify thumbnail, viewer, shared URL and exported image agree for the same seed. Do not rebuild the gallery.
