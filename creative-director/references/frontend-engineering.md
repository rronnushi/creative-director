# Frontend engineering

Load when selecting architecture, managing state, performance or release behavior.

## Principles

Prefer the existing architecture and a complete small solution. A dependency should remove a concrete burden large enough to justify bundle, maintenance and integration costs.

## Decision framework

Identify state ownership and lifecycle: persisted user data, route state, transient UI and derived render data. Pick one authoritative source per fact; avoid synchronization patches between duplicated state.

## Implementation

Reuse components/tokens. Clean up observers, listeners and animation loops. Validate external data at boundaries; cancel or ignore stale requests. Reserve media space and load expensive offscreen content on demand. Define a representative measurement task before optimizing.

## Example and contextual exception

A filtered gallery should derive both thumbnail and viewer from the same record. Copying palette generation into a separate viewer can create mismatches even if both components render correctly in isolation.

## Failure patterns

Framework rewrites for cosmetic changes; dependencies for trivial native behavior; effect chains synchronizing duplicate state; secrets in client bundles; announcing local build success as deployed verification.

## Validation

Run changed behavior tests and existing relevant checks. Exercise loading/error/empty and navigation. Confirm build base paths, exports and environment handling before release; verify deployment separately when authorized.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **animation** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

