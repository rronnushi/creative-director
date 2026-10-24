# Creative Director

**Your AI coding agent can build it. Make sure it's worth building.**

Creative direction, design critique and thoughtful implementation for **Codex, Claude Code and compatible coding agents**.

Creative Director is an open-source Agent Skill that gives your coding agent a structured way to make creative and product decisions. Use it to develop a clear concept, review an interface, simplify a product or improve an existing app while preserving what already works.

## Why use it?

A working app still needs good decisions about hierarchy, interactions, visual identity and scope. Requests such as “make it better” often leave those decisions unclear.

Creative Director turns them into concrete work:

| When you need… | It helps your agent… |
| --- | --- |
| Direction for a vague idea | Define the audience, core task, concept and implementable visual rules |
| Feedback on an existing app | Identify specific problems, explain their impact and propose prioritized remedies |
| A focused improvement | Inspect the existing project and preserve working features, data and identity |
| A smaller, clearer product | Compare ideas, prioritize the useful core and identify what to leave out |
| A consistent interface | Specify typography, colour roles, layout, responsive behavior and interaction states |
| More intentional generative art | Use composition rules, controlled randomness, stable seeds and meaningful visual variety |

It is useful for developers, designers, solo builders and people building their first digital product. It supports websites, portfolios, editorial interfaces, dashboards, browser games and creative coding projects.

## Try it

After installation, open a project in Codex and ask:

```text
Use $creative-director to critique this app's design and usability.
Give prioritized, concrete recommendations. Do not modify any files.
```

For an implementation request:

```text
Use $creative-director to improve the mobile navigation.
Preserve the existing visual identity and working features.
Make only the changes needed and verify the result.
```

In Claude Code, use `/creative-director` instead of `$creative-director`. Both hosts also support natural-language skill discovery; actual selection depends on the host.

## What makes it useful

- **Specific critique.** Findings identify the problem, evidence, user impact, remedy, confidence and relative effort.
- **Respect for existing work.** Refinement starts with the current project rather than assuming it needs a rewrite.
- **Contextual judgment.** The default philosophy is *minimal foundations, expressive experiences*. Your brief and project identity take priority; maximalist and dense interfaces remain valid.
- **Honest verification.** Code inspection, rendered observations, measured results and subjective preferences stay distinct. The skill should say when it cannot verify something.
- **Selective knowledge.** A small entrypoint loads relevant workflows and references rather than every resource for every request.
- **Adaptable preferences.** Optional private profiles and case studies let you describe your own direction. Feedback becomes a candidate lesson, with human approval before promotion into shared guidance.

These are intended behaviors, not claims of measured improvements in conversion, originality or model performance.

## Install

Download this repository using **Code → Download ZIP**, then extract it. The folder you install is the inner **`creative-director/` folder containing `SKILL.md`**, not the entire repository.

| Agent | For all your projects | For one project |
| --- | --- | --- |
| Codex | `~/.agents/skills/creative-director/` | `<project>/.agents/skills/creative-director/` |
| Claude Code | `~/.claude/skills/creative-director/` | `<project>/.claude/skills/creative-director/` |

On Windows, `~` means your user folder, such as `C:\Users\YourName`.

For Codex on Windows, open PowerShell **in the extracted repository folder** and run:

```powershell
$skillTarget = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillTarget | Out-Null
Copy-Item -LiteralPath './creative-director' -Destination $skillTarget -Recurse
```

For Codex on macOS or Linux, run from the repository folder:

```sh
mkdir -p ~/.agents/skills
cp -R creative-director ~/.agents/skills/
```

Inspect an existing installation before copying over it. Start a new agent session and check that Creative Director is listed; restart the host if it does not appear. Keep the full skill folder together because its workflows and references are needed.

See the [complete installation and usage guide](creative-director/README.md) for Claude Code, project-level installation and technical details. Installation guidance links to the official host documentation there.

## How it works

One installable skill selects among six modes: **Direct, Critique, Refine, Discover, Design and Build**. You describe the task; you do not need to choose a mode yourself.

Its supporting files cover product thinking, creative direction, visual design, typography and colour, UX, accessibility, motion, frontend engineering, AI experiences, games and procedural graphics. Technical sources and subjective taste preferences are kept separate.

The skill uses the capabilities your coding agent already provides. It adds no runtime server, required paid API or provider-specific model dependency. Optional validation and knowledge tools use Python 3.10+ with the standard library.

## Examples

- [Critique an app without changing it](creative-director/examples/app-critique.md)
- [Refine a website while preserving its identity](creative-director/examples/website-redesign.md)
- [Develop a landing-page direction](creative-director/examples/landing-page.md)
- [Improve procedural artwork](creative-director/examples/procedural-art.md)
- [Explore and simplify a product idea](creative-director/examples/product-ideation.md)

These are clearly labeled synthetic illustrations, not customer testimonials or measured results.

## Validation and limitations

The local tooling suite has **39 passing tests**, plus offline metadata, reference and release-package checks. There are **30 evaluation scenarios**, including cases where the skill should not activate. One independent source-based critique was exercised.

Full baseline-versus-skill evaluations in Codex and Claude Code remain pending. Structure and tooling tests do not prove better creative outcomes. Browser inspection and performance measurements depend on the tools available in your session. The skill does not certify accessibility, originality or market demand.

See the [validation report](VALIDATION.md), [evaluation protocol](creative-director/tests/evaluation-rubric.md) and [primary-source register](creative-director/knowledge/sources.json) for the evidence and remaining gaps.

## Contribute

Useful contributions include specific failure reports, focused workflow improvements, primary-source corrections and regression scenarios. Keep proprietary project material and personal preferences private unless deliberately approved for sharing. See [the contribution guide](creative-director/CONTRIBUTING.md).

## License

[MIT](LICENSE). You can use, modify and redistribute Creative Director under the license terms.
