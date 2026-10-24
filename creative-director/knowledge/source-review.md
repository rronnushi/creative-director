# Source review protocol

Stable design principles are authored heuristics. Official documentation supports specific technical claims, not the skill author's taste. Treat date/version fields as provenance rather than a warranty of freshness.

For each source: verify issuer and canonical URL; read the relevant section; record document version or “living documentation, no pinned release”; list only claims actually supported; distinguish successful retrieval from inaccessible or partial content. For library APIs record the project's installed version before implementation. Recheck living docs when API behavior matters. Do not bundle external documentation bodies or third-party assets.

The HTTP checker reports `reachable`, `redirected` or `unresolved` with status/error and timestamp. It does not detect soft-404s, establish authority, inspect JavaScript-only content or validate semantic accuracy. Inspect redirected destinations and inaccessible pages manually. An unresolved source cannot serve as sole evidence for a technical claim. In particular Three.js's manual shell is not proof of version-specific rendering APIs.
