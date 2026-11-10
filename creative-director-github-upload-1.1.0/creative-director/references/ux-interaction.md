# Interaction, accessibility and motion

Use this when people may struggle to find, complete or recover from the main task.

Follow the journey from action to result. What does the person know at each step? What can fail? Can they recover without losing their input? Put required choices where they are easy to find; hide secondary complexity only when it helps.

Use native controls and clear labels where possible. Keep selection, filters and position when returning from a detail view. Distinguish no content, no matching results and a failed request: they need different next steps.

Start with meaningful HTML and a logical reading order. Check keyboard access, visible focus, names and labels. Dialogs need suitable focus entry, containment and return. Offer alternatives to drag-only interactions. Touch targets need space as well as readable labels; WCAG 2.2's 24 CSS pixel AA target criterion has specific exceptions.

On small screens, change the layout rather than shrinking everything. Let controls wrap, give flexible children room to shrink and preserve action order. A genuinely two-dimensional table or map may need intentional scrolling; the surrounding interface should still work at narrow widths and zoom.

Motion should explain an action, maintain orientation or be part of the experience itself. Give important feedback priority over ambience. Offer an equivalent reduced-motion state. Removing movement shouldn't remove information.

For ordinary UI movement, transform and opacity are useful starting choices. Avoid repeated layout reads and writes in a frame, pause unnecessary background work and profile expensive effects. Don't apply `will-change` everywhere or claim a frame rate you haven't measured.

Check the main flow with keyboard and touch where available, at narrow and wide sizes, with enlarged text and with failures. Say which checks you actually performed. An automated scan alone cannot establish accessibility.

Technical sources: `wcag` and `animation` in [sources](sources.json).
