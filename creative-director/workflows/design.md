# DESIGN

Use after the direction is known. Load visual design, typography/colour and UX references as needed.

Specify the main journey and information architecture, then component responsibilities. Define semantic tokens (surface, ink, muted ink, accent, error, spacing, type roles, radius) and show which component consumes each. Give actual initial values plus reasons and validation needs, not only mood words.

For each interactive component define default, hover, focus-visible, active, disabled, loading, empty, error and success states where applicable. Specify what persists when navigating, switching modes or resizing. State responsive transformations, including content ordering and controls at the narrowest supported width; do not merely say “mobile friendly.” Include keyboard semantics, accessible names, focus return and reduced motion.

Example: a gallery uses `repeat(auto-fit, minmax(min(100%, 14rem), 1fr))`; square specimens remain square, filter controls wrap, the viewer returns focus to the opening specimen. This is a candidate layout, not a rule for every gallery. Deliver enough specification for implementation plus any untested assumptions.
