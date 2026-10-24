# Game and interactive experience design

Load when a playable loop, challenge or progression is involved.

## Principles

Make action → feedback → consequence legible. Difficulty should demand learnable skill rather than conceal rules or rely on unfair input timing.

## Decision framework

Write the core loop in one sentence. Identify the player's decisions, failure condition, recovery and progression. Distinguish procedural variety from difficulty. Choose the smallest playable vertical slice.

## Implementation

Separate simulation from rendering. Use elapsed time and a bounded fixed-step accumulator where deterministic physics matters; clamp large gaps after tab suspension. Support pause/restart and equivalent inputs. Seed procedural levels and validate solvability where feasible.

## Example and contextual exception

A tile puzzle can validate a generated solution path before shuffling. Difficulty can increase constraint density, not reduce touch targets. A timed action game may need a slower or untimed option instead of merely larger text.

## Failure patterns

Frame-rate-dependent movement; unbounded catch-up after tab return; invisible collision rules; procedural impossible states; juice effects that hide feedback.

## Validation

Test restart, pause/resume, touch/keyboard, failure recovery and long sessions. Replay fixed seeds. Verify rules and fairness with human playtesting; automated solvability does not prove fun.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **games** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

