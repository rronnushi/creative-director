# Creative Director

**Your AI coding agent can build it. Make sure it's worth building.**

A creative direction skill for [Codex](https://openai.com/codex/), [Claude Code](https://www.anthropic.com/claude-code), and other compatible coding agents.

## Why I made this

I've been using coding agents to build websites, small apps, games, and generative art. They're great at getting things working. But I've often found myself going back and forth over the same things: a layout that feels generic, unnecessary features, inconsistent interactions, or a redesign that breaks something that was already good.

The code isn't always the problem. Sometimes the project just needs better direction.

I made Creative Director to bring more design thinking into that process. It helps an agent question an idea, explore different approaches, spot what's not working, and make more considered changes instead of simply generating more code.

It's not a design system or a preset visual style. It's a way to get a more useful creative partner out of the coding agent you're already using.

## What can you use it for?

- **Starting something new.** Work through an idea, explore directions, and decide what's worth building before writing code.
- **Reviewing an existing app.** Get a critique of its layout, typography, interactions, usability, and overall coherence.
- **Improving a design.** Fix what feels off without throwing away the parts that already work.
- **Making better product decisions.** Figure out what to prioritize, simplify, or leave out.
- **Creative coding.** Think through composition, variation, palettes, rendering, and the relationship between what you see on screen and what you export.
- **Turning references into implementation.** Use a screenshot or a visual direction to establish practical rules for layout, type, and behavior.

It works across websites, editorial interfaces, dashboards, browser games, and generative art projects. You don't have to like the same things I do for it to be useful.

## How I use it

You can mention Creative Director in a request, or invoke it directly. For example:

> Critique this app. Tell me what feels inconsistent and what you'd fix first. Don't change the code yet.

> I like the existing visual identity. Improve the mobile layout without redesigning everything.

> Give me two different directions for this portfolio before we start building.

> This procedural artwork has lots of colour variation, but the compositions all look the same. Help me fix that.

> What should I remove from this MVP?

You can also ask it to translate a reference image into layout and interaction rules, or to help implement an agreed direction.

Under the hood, the skill has six workflows: creative direction, critique, refinement, discovery, design specifications, and implementation. You don't need to select one every time; the agent can choose based on what you're asking. A critique shouldn't edit your project unless you've asked for changes.

## A few examples

These are written examples of how the skill approaches a problem, not measured before-and-after results.

| If you're dealing with... | Creative Director can help you... | Example |
| --- | --- | --- |
| A vague request to “make it modern” | Define a clearer visual direction | [Landing page](creative-director/examples/landing-page.md) |
| A UI that doesn't quite work | Identify specific issues and prioritize fixes | [App critique](creative-director/examples/app-critique.md) |
| A redesign that's getting out of hand | Improve the existing site without replacing everything | [Website refinement](creative-director/examples/website-redesign.md) |
| An app whose preview and export don't match | Bring both outputs back to the same underlying state | [App refinement](creative-director/examples/app-refinement.md) |
| Generative artwork that looks too repetitive | Build more variety into the compositions, not just the colours | [Procedural art](creative-director/examples/procedural-art.md) |

There are also examples for [creative coding](creative-director/examples/creative-coding.md) and [product exploration](creative-director/examples/product-ideation.md).

## Install

Download or clone the repository, then copy the **entire `creative-director/` folder** into your agent's skills directory. Don't copy `SKILL.md` on its own; the skill uses the supporting files too.

| Agent | Install for yourself | Install for one project | Invoke |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/creative-director/` | `<project>/.agents/skills/creative-director/` | `$creative-director` |
| Claude Code | `~/.claude/skills/creative-director/` | `<project>/.claude/skills/creative-director/` | `/creative-director` |

**macOS / Linux — Codex, personal install**

Run this from the repository root:

```bash
mkdir -p ~/.agents/skills
cp -R creative-director ~/.agents/skills/
```

**Windows PowerShell — Codex, personal install**

```powershell
$skillTarget = Join-Path $HOME '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillTarget | Out-Null
Copy-Item -LiteralPath './creative-director' -Destination $skillTarget -Recurse
```

For Claude Code, use `~/.claude/skills` as the destination instead. For a project-only install, use the project paths in the table.

If you already have an installation, check the destination before copying over it. Your agent may need a restart to pick up the new skill. Discovery and automatic activation depend on the host; the paths above are for local Codex and Claude Code sessions.

The installation guidance was checked on October 24, 2026 against the [Agent Skills specification](https://agentskills.io/specification), [Codex documentation](https://learn.chatgpt.com/docs/build-skills), and [Claude Code documentation](https://code.claude.com/docs/en/skills). End-to-end comparisons across the two hosts are still pending.

## What about taste?

I have my own preferences: clear layouts, restrained interfaces, good typography, and room for more expressive work when the project calls for it. That's the starting point, not a rule everyone has to follow.

Creative Director separates [design preferences](creative-director/taste/README.md) from [technical references](creative-director/references/) so you can change the former without losing the latter. If your project calls for something maximalist, playful, dense, or deliberately unconventional, that should take priority.

I also wanted it to be useful beyond giving opinions. The skill includes references, checklists, and examples to help an agent explain *why* it's suggesting a change and what to check after implementing it.

You can explore the [source register](creative-director/knowledge/sources.json), [example comparisons](creative-director/knowledge/comparisons.json), and [guidance for private project knowledge](creative-director/knowledge/README.md). The comparisons are authored examples, not proof of improved outcomes. New lessons require human approval; the skill doesn't rewrite itself automatically.

## What's in the repository?

```text
creative-director/
  SKILL.md              Entry point and core instructions
  agents/               Agent metadata
  workflows/            Different ways to approach a task
  references/           Design and technical guidance
  taste/                Editable design preferences
  knowledge/            Sources, schemas, and examples
  checklists/           Practical review checks
  scripts/              Validation and packaging tools
  tests/                Scenarios and evaluation rubric
  examples/             Worked examples
```

The skill itself doesn't need a server, API key, or paid service. A compatible coding agent needs to be able to read its files. Optional maintenance and evaluation scripts use **Python 3.10+** and the standard library.

To run the checks yourself, go into the `creative-director/` folder:

```bash
python scripts/validate_skill.py
python scripts/check_references.py
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/prepare_evaluation.py ../evaluation-runs/run-001 --scenario landing-critique
python scripts/package_release.py ../dist/creative-director-1.0.0.zip
```

You can also run `python scripts/check_references.py --online` to check the recorded links. These checks help catch structural and packaging problems; they don't prove that the advice is good or that a resulting interface is accessible or performant. The [evaluation rubric](creative-director/tests/evaluation-rubric.md) explains how to compare results more systematically.

For maintainers: the frontmatter uses JSON-style YAML so the validator doesn't need an external YAML package. The bundled schema tooling supports a documented subset of JSON Schema; see the scripts for details.

## What it won't do

Creative Director isn't a substitute for testing, user research, accessibility audits, or your own judgment. It can't guarantee originality or tell you whether an idea will succeed. It also isn't meant to handle unrelated backend debugging or general factual questions.

Some reference material is version-dependent, including the partially reviewed Three.js documentation. Check APIs against the version your project uses. Public examples are written illustrations, not anonymized private projects, and no private project files are included in the release package.

**Release status:** Version 1.0.0 has been prepared locally, but the public release and paired host evaluations are not yet confirmed. See the [release checklist](creative-director/checklists/release-readiness.md) for what's left.

## Contributing

If you find a case where the skill gives poor advice, misses something obvious, or makes a project worse, I'd be interested in a reproducible example and a suggested improvement. Focused changes are more useful than adding another page of generic instructions.

See [CONTRIBUTING.md](creative-director/CONTRIBUTING.md). Please only contribute examples and assets you have permission to share.

Released under the [MIT license](creative-director/LICENSE).
