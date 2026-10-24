# Creative Director

**Your AI coding agent can build it. Make sure it's worth building.**

Creative direction for Codex, Claude Code and compatible coding agents.

Creative Director helps turn ideas into distinctive digital experiences and improves existing applications through stronger design decisions, clearer interactions and thoughtful implementation. It adds structured judgment to your coding agent: what to build, what to preserve, what to simplify and how to know whether a change helped.

## What it does

Use it when a functional app still feels generic, when an idea needs direction, or when a redesign threatens to discard what already works. It supports websites, editorial interfaces, dashboards, browser games and generative art. Designers, developers and people building their first product can use it without adopting one visual style.

Six inferred modes cover direction, critique, refinement, discovery, design specifications and implementation. Critique is read-only unless you also request changes. Refinement starts with the existing project and preserves working behavior, data and identity. Specialist resources load only when relevant.

The default taste is **minimal foundations, expressive experiences**: clear structure with purposeful character. Maximalism, dense professional interfaces and experimental art remain valid. Your direction and project conventions override the defaults.

## Example requests

- “Use Creative Director to critique this app. Give prioritized remedies; don't edit.”
- “Keep our visual identity and fix this mobile gallery toolbar.”
- “Give this archive two distinct creative directions; don't implement yet.”
- “Translate this screenshot into layout, type and interaction rules. Mark assumptions.”
- “Improve the structural variety of this seeded artwork while preserving exports.”
- “Which features should this MVP omit?”

Pure backend debugging, factual questions and small text edits should not activate the skill.

## Before and after workflows

These are illustrative, not measured results:

| Before | Skill-guided outcome | Example |
| --- | --- | --- |
| “Make it modern” | A concept expressed through hierarchy, type roles and interactions | [Landing page](examples/landing-page.md) |
| Vague UI feedback | Located evidence, impact, remedy, effort and verification | [App critique](examples/app-critique.md) |
| A redesign replacing everything | Small changes preserving functioning behavior and identity | [Website refinement](examples/website-redesign.md) |
| Preview/export mismatch | One scene state across renderers | [App refinement](examples/app-refinement.md) |
| Random colours on identical compositions | Authored composition grammars and a reproducible review set | [Procedural art](examples/procedural-art.md) |

Also see [renderer selection](examples/creative-coding.md) and [product exploration](examples/product-ideation.md).

## Installation

The repository contains **one canonical installable folder**, `creative-director/`. Copy that whole folder, not just SKILL.md, into the chosen host's location. If you downloaded the release ZIP, its top-level `creative-director/` is the folder to install. Avoid installing competing versions under the same host.

| Agent | User scope | Project scope | Explicit invocation |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/creative-director/` | `<project>/.agents/skills/creative-director/` | `$creative-director` |
| Claude Code | `~/.claude/skills/creative-director/` | `<project>/.claude/skills/creative-director/` | `/creative-director` |

Both hosts can discover it from natural-language requests. Check that the host lists the skill; restart if changes are not picked up. Claude Code's paths here describe local sessions; cloud and other Claude products may have different discovery. Other Agent Skills hosts need their own documented installation location and supporting-resource access.

PowerShell example, run from the repository root, for **one** selected scope/host:

```powershell
# Codex, user scope:
$skillTarget = Join-Path $HOME '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillTarget | Out-Null
Copy-Item -LiteralPath './creative-director' -Destination $skillTarget -Recurse
# For a project, use '<project>/.agents/skills' instead.
# For Claude Code, use '~/.claude/skills' or '<project>/.claude/skills'.
```

POSIX equivalent for Codex user scope:

```sh
mkdir -p ~/.agents/skills
cp -R creative-director ~/.agents/skills/
```

Inspect an existing destination before updating so personal modifications are not overwritten. Keep personal profiles outside the installed folder. Automatic selection is host-dependent; installation-format validation is not proof of routing or execution quality.

Instructions were checked on **2026-10-24** against the [Agent Skills specification](https://agentskills.io/specification), [Codex guide](https://learn.chatgpt.com/docs/build-skills) and [Claude Code guide](https://code.claude.com/docs/en/skills). Actual paired host evaluations remain pending.

## How judgment and knowledge work

The small [SKILL.md](SKILL.md) selects a workflow and routes to relevant references. Technical guidance is distinct from [overridable taste](taste/README.md). The [source register](knowledge/sources.json) records primary URLs, review dates, version context, supported claims and limitations. One Three.js source is explicitly partial because only the manual shell could be retrieved; verify installed-version APIs before use.

[Structured comparisons](knowledge/comparisons.json) are synthetic examples. Add your own through the schema-validated CLI. [Personal configuration and case studies](knowledge/README.md) stay private unless deliberately approved for public use. Feedback produces candidate lessons; a separate human approval attestation is required before promotion. No script rewrites the canonical skill automatically.

This checkout's real project evidence is limited to a private documentation observation from one accessible local project and explicit instructions from this build session. It is not part of the release ZIP. No private screenshots, code, history or assets are bundled. Public examples are authored illustrations; technical references cite primary documentation. No user-study outcomes are claimed.

## Structure

```text
creative-director/
  SKILL.md              Activation, routing and core constraints
  agents/openai.yaml    Optional Codex UI metadata
  workflows/            Six modes and reference translation
  references/           Focused design and technical knowledge
  taste/                Contextual, overridable judgment defaults
  knowledge/            Schemas, source register and comparisons
  checklists/           Small checks for the relevant review stage
  scripts/              Validation, knowledge, evaluation and packaging tools
  tests/                30 scenarios, raw fixtures, Python tests and rubric
  examples/             Seven synthetic worked workflows
```

## Requirements and validation

The skill itself requires only a compatible agent that can read its supporting files. Python **3.10+**, standard library only, runs the optional tooling. No paid service, provider API, runtime server or third-party Python package is required. Browser tools and project-specific tests are optional host capabilities; missing evidence must be disclosed.

Run from the installable folder:

```sh
python scripts/validate_skill.py
python scripts/check_references.py
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/prepare_evaluation.py ../evaluation-runs/run-001 --scenario landing-critique
python scripts/package_release.py ../dist/creative-director-1.0.0.zip
```

Optional `python scripts/check_references.py --online` performs bounded network checks and exits nonzero on unresolved links. It does not establish semantic accuracy or update review dates. Frontmatter uses JSON object syntax, a valid YAML 1.2 subset, so deterministic parsing needs no YAML dependency. Other YAML styles require adapting the validator. JSON Schemas use a documented limited subset enforced by `scripts/common.py`; unknown schema keywords fail loudly. Any standard draft-2020-12 validator can also validate the schemas, with application-level consent and file checks handled by the CLI.

See [the evaluation rubric](tests/evaluation-rubric.md) for controlled baseline-versus-skill runs, human scoring and honest result records. Fixtures contain deliberate defects. The suite is not a certification of frontend quality.

## Limits and release status

Creative judgment remains contextual. The skill cannot certify accessibility, predict market demand or prove originality. Automated validation checks structure, records and packaging; it cannot demonstrate improved taste. Source availability and APIs change. Browser inspection, actual performance and cross-agent behavior must be verified in the environment where the skill is used.

Version **1.0.0** is prepared locally. Review [release readiness](checklists/release-readiness.md), commit the reviewed source, complete host evaluations, resolve or retain transparent source limitations, and approve publication before creating a public release. Nothing in the tooling publishes to GitHub or a directory.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Prefer a small evidence-supported correction with a regression scenario over more generic instructions. Do not contribute proprietary examples or third-party assets without permission. Released under the [MIT license](LICENSE).
