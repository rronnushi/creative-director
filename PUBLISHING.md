# GitHub release process

Repository: https://github.com/rronnushi/creative-director.

Suggested public repository description:

> Creative direction, design critique and focused refinement for Codex, Claude Code and compatible coding agents.

Suggested topics: `agent-skills`, `codex`, `claude-code`, `creative-direction`, `design`, `ux`, `generative-art`.

## Source and versioning

Keep one canonical installable folder, `creative-director/`. Review and commit the public source on the repository's default branch. Confirm the validation workflow passes before tagging a release. Keep installation and evaluation limitations visible in the README and validation report.

## Upload through GitHub

1. Extract `creative-director-github-upload.zip` on your computer.
2. Open the extracted folder. It contains this file, `README.md`, `LICENSE`, `VALIDATION.md`, `.gitignore`, `.github/` and the installable `creative-director/` folder.
3. Open https://github.com/rronnushi/creative-director and choose **Add file → Upload files**.
4. Drag all the extracted files and folders into the upload area. Upload the contents, not the ZIP and not an extra enclosing folder. Include `.github/` and `.gitignore`.
5. Enter a commit message such as `Publish Creative Director v1.0.0 source` and choose **Commit changes**. The complete README replaces the initial placeholder README.
6. Open the **Actions** tab and check the validation results. The public README explains what the skill does, who it helps and how to install it.

The upload archive contains public source only. Personal profiles, private project material, local Git metadata and evaluation workspaces are excluded.

## Upload boundary

Upload the root `README.md`, `LICENSE`, `.gitignore`, `VALIDATION.md`, `PUBLISHING.md`, `.github/workflows/validate.yml` and the exact 65 public files listed in `creative-director/release-manifest.json`, under `creative-director/`.

Exclude `.creative-director.local.json`, `private/`, `evaluation-runs/`, `.test-tmp/`, `__pycache__/`, `.git/`, `.validation-deps/` and `dist/`. The release ZIP is a release attachment rather than a source file. Avoid local account details, private project examples and machine paths in the public source.

## After uploading

Verify the repository is public, the README renders, the default branch contains the canonical skill and the validation workflow passes. Record actual outcomes. The full paired host evaluations remain pending; publication must not imply they passed.

Optionally create a `v1.0.0` release with the verified installable ZIP and concise release notes. Review the release archive against the current source before attaching it. Do not create competing skill copies or publish private profiles.
