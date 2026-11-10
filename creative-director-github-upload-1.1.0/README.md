# Creative Director

**Your AI coding agent can build it. Make sure it's worth building.**

Creative Director helps your coding agent make better design decisions. Use it to work through an idea, review an interface or improve an app you've already built.

It gives Codex, Claude Code and other compatible agents a way to look beyond whether something works: does the idea make sense, is the interface clear, and does the result have a character of its own?

## When it helps

- **An idea needs direction.** Explore a few different approaches and turn the strongest one into concrete design choices.
- **An app works but feels unfinished.** Find the important problems in its layout, typography, navigation or interactions.
- **Something needs improving.** Make focused changes while keeping the identity and features you want to preserve.
- **A product has become too complicated.** Decide what matters and what can wait.
- **Generated artwork looks repetitive.** Improve its composition and variety while keeping seeds and exports consistent.

You don't need to learn a set of modes or write a long brief. Tell it what you're making and what you need help with.

## Try it

Start with a review that leaves your files alone:

```text
Use $creative-director to review this app.
What works, what feels weak, and what would you change first?
Don't edit anything yet.
```

Or ask it to make a specific improvement:

```text
Use $creative-director to improve this page on mobile.
Keep the current look and working features.
```

For a new project:

```text
Use $creative-director to help me find a direction
for a small website about urban photography.
I want it to feel distinctive without getting in the way of the photos.
```

In Claude Code, invoke it with `/creative-director`. See [a few example conversations](docs/examples.md) for the kind of advice it should give.

## Install

Download the skill ZIP when a release is available, or download this repository and find the inner `creative-director` folder. Copy that entire folder into your agent's skills directory.

| Agent | Install for your user |
| --- | --- |
| Codex | `~/.agents/skills/creative-director/` |
| Claude Code | `~/.claude/skills/creative-director/` |

On Windows, `~` is your user folder. Start a new session after installing. The [installation guide](docs/installation.md) includes copy commands, project-only installation and updating an older copy.

No extra API key or service is required. Your coding agent still needs its usual access.

## A point of view, with room for yours

The starting philosophy is **minimal foundations, expressive experiences**: get the structure right, then give the work a reason to be remembered.

That doesn't mean every project should look minimal. A dense dashboard, a loud festival page and a quiet portfolio need different decisions. Your brief and the project's existing identity take priority. You can also [add your own preferences](docs/preferences.md).

## What's included

The installed skill contains design guidance, practical workflows and focused references. Development tests and release tools stay in the repository; you don't need them to use it.

It should explain its recommendations and be clear about what it hasn't checked. It can't replace user research, visual review or testing in the real app.

Want to help improve it? See [Contributing](CONTRIBUTING.md). Creative Director is free to use, modify and share under the [MIT license](LICENSE).
