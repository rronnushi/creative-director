# Build the experience

Use the existing framework and architecture. For a new project, choose the simplest approach that meets the requirements. A library should solve a real problem, not make a small tool look more substantial.

Build the main useful interaction first, then the loading, error, empty and input states it needs. Keep state ownership clear so controls, navigation, previews and exports agree.

Choose a renderer for the task: semantic HTML for UI, SVG for manageable vector scenes, Canvas for raster drawing, and WebGL when GPU rendering or 3D earns the extra work. See creative coding for scene state, resize and export.

Validate external data, handle stale requests and keep secrets off the client. For AI features, plan for invalid results, cancellation and useful recovery.

Run relevant project checks. Exercise the main flow and the parts the change could affect. Inspect narrow and wide layouts, keyboard use and downloaded exports when applicable. Measure suspected performance problems before claiming an improvement.

Finish with what works, what was checked and any important gaps. Local success is separate from a live deployment; publish only when authorized.
