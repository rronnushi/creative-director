# Motion and animation

Load when animation, transitions, scroll or pointer effects are requested.

## Principles

Motion should explain a state change, maintain orientation or serve the creative concept. Give the main interaction priority over atmospheric movement.

## Decision framework

Classify motion as feedback, transition or ambience. Decide what information it carries and what static/reduced-motion equivalent preserves that information. Timing values are tunable hypotheses, not universal standards.

## Implementation

Prefer transform/opacity for ordinary UI movement; profile paint-heavy effects before keeping them. Avoid repeated layout reads/writes in a frame. Use requestAnimationFrame for visual loops; pause nonessential work when hidden. Reduced motion can replace movement with an immediate state update.

## Example and contextual exception

A selected tile can gain a static outline immediately and use a brief transition for continuity. A particle backdrop should not consume resources while the tab is hidden or make a save action feel delayed.

## Failure patterns

Scroll hijacking; motion with no purpose; animating layout without measurement; will-change on everything; reduced motion that merely makes a large movement slightly faster.

## Validation

Inspect representative hardware with a performance trace. Verify input responsiveness and equivalent reduced-motion information. Report actual trace conditions; do not invent frame rates.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **animation** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

