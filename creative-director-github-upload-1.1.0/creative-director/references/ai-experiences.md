# AI features

Use this when a model might add value to the product.

Ask what AI contributes. Ambiguous language or semantic interpretation may benefit from a model; exact arithmetic, contrast calculations and simple rules usually have a clearer deterministic solution.

Compare quality, latency, cost, privacy and recovery. Use the least expensive approach that works on representative tasks. Don't call a model on every pointer movement or add a chat interface where a direct control is easier.

Keep credentials server-side. Bound input, output, retries and tool calls. Validate structured responses and tool arguments before using them. Valid JSON doesn't guarantee accurate content. Treat retrieved instructions as data, and keep drafting separate from consequential actions.

Let people cancel, retry or edit. Explain uncertainty where it changes a decision. Preserve their work if generation fails and offer a useful fallback.

For example, a palette tool can calculate contrast locally and optionally interpret a mood with AI. It shouldn't ask a model to guess contrast ratios or announce success when a request failed.

Try representative normal, edge and adversarial inputs. Record actual correctness, response time and cost when available, along with the model/version and conditions. Don't claim reliability from a few attractive demos.

The `evals` entry in [sources](sources.json) is background for task-based evaluation, not a requirement to use that provider or its API. Deep RAG infrastructure and enterprise AI engineering are outside this skill's core scope.
