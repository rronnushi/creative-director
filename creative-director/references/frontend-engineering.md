# Frontend choices that support the design

Use this when the design depends on architecture, state, performance or reliable delivery.

Start with the project's existing framework, components and tokens. Add a dependency when it removes a concrete burden worth its download size, integration work and maintenance. Don't introduce a new framework for a cosmetic change.

Decide who owns each piece of state: saved user data, route state, temporary UI choices and derived render data. Keep one authoritative source for each fact. If a thumbnail, viewer and export disagree, check whether they're deriving the same state before adding synchronization patches.

Validate external responses at the boundary. Cancel or ignore stale requests, handle errors without losing input and keep credentials off the client. Clean up listeners, observers and animation loops when they are no longer needed.

Reserve space for media to avoid layout shifts. Load expensive offscreen content when useful and cache work that doesn't change. Before optimizing, define the interaction and environment you will measure. Source code can suggest a bottleneck but doesn't prove its impact.

For a gallery, shared state should connect selected record, palette variant, URL and export. For an editor, resizing the preview should not mutate the document. Keep these relationships clear enough to test without a large abstraction layer.

Run checks relevant to the change, then exercise the main flow and nearby states. Check routes, build base paths and downloaded artifacts where applicable. Local packaging and a live deployment are different checks; report them separately.

For browser animation performance, see `animation` in [sources](sources.json). Verify version-specific framework APIs against the installed version when they matter.
