# BUILD

Use the existing framework and frontend engineering reference. For graphics load creative coding; for procedural output also load generative art. Establish a complete primary interaction before adding polish.

Select the lightest renderer that fits the output: DOM for semantic UI, SVG for moderate vector scenes/export, Canvas for many raster marks, WebGL for measured scale or 3D needs. Keep state and rendering separable so resize/export do not silently regenerate content. Use existing dependencies; justify each addition by a concrete capability.

Implement the core task, then necessary loading/error/empty and input states. For APIs validate responses and handle cancellation; for AI use bounded structured outputs and a meaningful failure path. Keep secrets off the client. Run relevant existing tests and build. Inspect rendering, keyboard use, narrow/wide layouts and export if available. Measure performance in the target context before claiming speed. Report any unavailable evidence and avoid publishing without authorization.
