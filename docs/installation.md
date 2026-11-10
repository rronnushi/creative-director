# Install Creative Director

You need a coding agent that supports Agent Skills. Python and the development tools in this repository are not required to use the skill.

## Find the right folder

If you downloaded the skill release ZIP, extract it and find `creative-director/SKILL.md`.

If you downloaded this repository, the installable folder is the inner `creative-director` directory. Copy that whole folder, including its references and workflows.

## Codex

For all your projects, install at `~/.agents/skills/creative-director/`. For one project, use `<project>/.agents/skills/creative-director/`.

On Windows, open PowerShell in the extracted repository folder:

```powershell
$skillTarget = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillTarget | Out-Null
Copy-Item -LiteralPath './creative-director' -Destination $skillTarget -Recurse
```

On macOS or Linux, from that folder:

```sh
mkdir -p ~/.agents/skills
cp -R creative-director ~/.agents/skills/
```

Start a new Codex session and try:

```text
Use $creative-director to review this project. Don't edit anything yet.
```

## Claude Code

For all your projects, copy the folder to `~/.claude/skills/creative-director/`. For one project, use `<project>/.claude/skills/creative-director/`.

In a new local session, invoke `/creative-director`. Other Claude products and cloud sessions may use different installation methods.

## Updating an older copy

Keep your previous skill folder as a backup outside the host's skills directories, then replace it with the new folder. Don't merge the new files into an old installation: older versions included tests and development tools that would otherwise remain.

Keep project preferences outside the installed folder so updates don't overwrite them. If the host doesn't notice the update, restart it. Avoid leaving two installed copies with the same name.

Source: [Codex skill guidance](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills) and the [Agent Skills specification](https://agentskills.io/specification). The bundled source register records the documentation review dates; these instructions do not claim a new cross-agent installation test.
