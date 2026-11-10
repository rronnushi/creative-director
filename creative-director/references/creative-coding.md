# Creative coding and generative art

Use this for procedural graphics, interactive scenes, seeds, resize and export.

Treat randomness as a way to explore an authored idea. Decide what stays consistent and what can vary: layout, focal point, rhythm, density, geometry and palette. More random parameters don't necessarily produce more interesting work.

Keep the scene separate from its controls and renderer. Store the seed, parameters and engine version needed to reproduce it. Use a stable seeded generator with deliberate input normalization. Separate palette and composition random streams when they should vary independently.

Preview, resize and export should use the same scene. A larger export needs more pixels, not a new composition. If an engine change alters old seeds, version it rather than quietly promising unchanged output.

Choose SVG for manageable vector scenes and vector export, Canvas for raster drawing, and WebGL for appropriate GPU or 3D work. Use logical scene coordinates. Resize buffers only when dimensions change; scale for pixel density with a sensible cap, cache static work and avoid allocating objects or textures every frame.

For Three.js, inspect the installed version before using APIs. Keep display size, drawing buffer and camera aspect in agreement; release replaced resources. The bundled Three.js source is marked partial, so it is not verified evidence for a particular API call.

Check variety with a small, fixed seed contact sheet. Compare silhouettes, focal placement, occupied space and rhythm—not just colour. For example, two subdivision grammars may add more useful variety than ten hue sliders. A controlled colour experiment may deliberately keep the geometry identical.

Repeat seeds, resize without regeneration and open the exported files. Check margins, dense/sparse cases, repeated generations and bounded generation loops. Handle export failures such as cross-origin Canvas restrictions clearly. Keep essential controls usable with keyboard and touch.

The `canvas`, `svg` and `three` entries in [sources](sources.json) cover technical context. Composition rules and judgments of variety are authored guidance that needs visual review.
