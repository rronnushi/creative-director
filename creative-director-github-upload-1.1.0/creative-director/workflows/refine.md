# Improve existing work

Inspect the area the user wants changed and the existing components, styles, state and relevant tests. Identify what must stay: the main flow, visual identity, data, configuration and working interactions.

Fix the cause with the project's existing patterns. A palette mismatch may be shared-state trouble; an alignment problem may belong to one layout rule. Neither automatically needs a new architecture or design system.

Make the smallest change that fully handles the request. Don't add features or restyle neighboring sections just because you're there. If a wider change is necessary, explain why and respect the user's limits.

Check the changed behavior and nearby interactions. For layout work, use long content, a narrow screen and keyboard focus where relevant. For artwork, check resizing and export. Use a comparable before/after view when available.

Report what changed, what you checked and what remains uncertain. A successful build doesn't tell you whether the user likes the design.

Example: if a selected thumbnail and viewer show different colours, trace the selected seed and palette through both. Preserve the gallery layout and filters; make thumbnail, viewer and export use the same selected state.
