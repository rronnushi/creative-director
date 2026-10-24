# Responsive accessibility

Load when a surface changes size or has accessibility concerns.

## Principles

Preserve task completion across viewport sizes, zoom, input methods and assistive technology. Responsive design is content reprioritization as well as resizing.

## Decision framework

Start with semantic structure and logical reading order. Test the actual smallest useful layout; identify intentionally scrollable regions such as wide data tables rather than shrinking text to fit.

## Implementation

Use flexible tracks, min-width:0 where needed and content-driven wrapping. Provide keyboard focus, accessible names, labels and errors. Dialogs need appropriate focus entry, containment and return. Support reduced motion and alternatives to drag-only actions. WCAG 2.2 AA target size generally uses 24 by 24 CSS pixels with specified exceptions; larger targets can improve touch use.

## Example and contextual exception

At 320 CSS pixels, a toolbar can wrap beneath the artwork while preserving action order. A two-dimensional map may need intentional pan/zoom, but its surrounding controls still reflow. Do not hide the primary action to remove overflow.

## Failure patterns

Desktop CSS merely scaled down; visual order differing from reading order; focus hidden under sticky controls; treating an automated scan as full conformance.

## Validation

Test narrow/wide widths, 200% text and reflow context equivalent to 400% zoom on a 1280px viewport, keyboard-only completion and relevant screen-reader behavior. Record exactly what was tested, not a blanket compliance claim.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **wcag** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

