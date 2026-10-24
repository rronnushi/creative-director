# Creative coding

Load when implementing procedural scenes, renderers, export or interactive graphics.

## Principles

Separate scene/state from renderer and UI. The same state should drive preview, resize and export; export resolution must not change the composition.

## Decision framework

Choose SVG for inspectable vectors and moderate scene sizes, Canvas for large raster mark counts, WebGL for appropriate GPU/3D workloads. Use evidence rather than an arbitrary particle threshold.

## Implementation

Use logical scene coordinates. Scale backing pixels for display density with a measured cap. Resize buffers only when size changes. Cache static work; batch drawing. In Three.js match drawing-buffer size to display size, update camera aspect/projection, dispose replaced resources and handle context loss. Verify against the project's installed version before using APIs.

## Example and contextual exception

A poster stores geometry, palette and seed once. A PNG export renders that state to a larger offscreen canvas; SVG export serializes the same geometry. If cross-origin images taint Canvas, use authorized CORS-enabled assets and explain export failure.

## Failure patterns

Regenerating on resize; independent randomness in preview/export; allocating textures each frame; unreadable controls on a full-screen canvas; choosing 3D for a flat static diagram.

## Validation

Verify same state across sizes and exports; open the downloaded artifact. Test touch, keyboard alternatives, memory after repeated generations and failure paths. Test SVG viewBox and Canvas pixel dimensions separately.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **canvas** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

