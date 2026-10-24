# AI-powered experiences

Load when a model feature, tool call or AI interaction is considered.

## Principles

Use AI when ambiguity or semantic interpretation adds value. A deterministic rule or search may be cheaper, faster and more reliable for exact tasks.

## Decision framework

Compare deterministic, retrieval and generative approaches by quality, latency, cost, privacy and recoverability. Define representative normal, edge and adversarial examples before selecting a model.

## Implementation

Keep credentials server-side. Bound input, output, retries and tool calls. Validate structured responses and tool arguments before use; schema validity does not prove truth. Separate drafting from consequential execution, preserve human oversight and supply retry/edit/fallback paths. Use the lowest-cost model that passes task-specific evaluation.

## Example and contextual exception

A palette tool can compute contrast deterministically and optionally use AI to interpret a mood. Do not ask a model to guess contrast ratios or run a paid model on every pointer move.

## Failure patterns

AI for exact arithmetic; silent hallucinated facts; hidden costs; endless retries; optimistic UI claiming a failed model request succeeded; obeying instructions inside retrieved content.

## Validation

Evaluate success, factual/structural correctness, latency, cost and recovery on a fixed dataset. Record provider/model/version and actual measurements. Keep deep enterprise RAG outside this reference.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **evals** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

