# UX and interaction

Load when navigation, task flows, state feedback or information density needs work.

## Principles

Expose the main task; make the result of an action understandable and reversible where practical. Progressive disclosure should hide secondary complexity, never the next required step.

## Decision framework

Map trigger → pending → result → recovery. For each stage ask what the user knows, what can fail and how to recover without losing input. Match density to expertise and frequency.

## Implementation

Prefer native controls and explicit labels. Preserve filters and scroll position when returning from a detail view. Distinguish an empty dataset from no search results and from a network error. For async work prevent duplicate mutations and announce results without unexpectedly moving focus.

## Example and contextual exception

A gallery with no matches should show active filters and a clear reset. A failed fetch should keep those filters and offer retry; silently showing an empty grid misdiagnoses the problem.

## Failure patterns

Hover-only actions; generic error messages; destructive defaults; spinners without status; automatically resetting user choices.

## Validation

Complete the primary journey with keyboard and touch. Exercise failure and retry, back navigation, slow responses and long labels. Confirm visible status agrees with actual state.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **wcag** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

