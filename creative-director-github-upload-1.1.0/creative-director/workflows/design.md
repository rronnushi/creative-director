# Make the direction buildable

Start with the main user journey and the content it needs. Describe the layout and component responsibilities, using the existing design system when one exists.

Choose concrete starting values for type roles, colour roles, spacing and component geometry. Explain relationships that matter: what leads, what supports it and which controls belong together. Avoid specifying every decorative detail before the main composition works.

Describe the states users will encounter: focus, selection, loading, empty results, errors and success. Include what persists when they navigate, change modes or resize. Only specify states relevant to the component.

Say how the layout changes on small screens: content order, wrapping, control placement and scrolling. Include keyboard behavior, labels, focus return and reduced motion where needed. “Responsive and accessible” alone is not a specification.

Keep the handoff proportionate. A focused change may need one layout rule and a few state notes; a new app may need a component outline and token table. Mark anything that needs a rendered check rather than guessing it is resolved.
