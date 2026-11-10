# Maintaining Creative Director

Users only need the `creative-director` folder. Everything here is for people changing the skill.

## Check a change

Run the commands in [Contributing](../CONTRIBUTING.md) from the repository root. The validator checks skill metadata, links and the optional structured records. Tests cover the tools and packaging, not whether the design advice is good.

The root [release manifest](../release-manifest.json) lists installed files separately from repository files. Update it deliberately when adding or removing public files. Build the skill ZIP with `python scripts/package_release.py dist/creative-director-1.1.0.zip`; add `--repository` for a GitHub upload ZIP. Existing archives are not overwritten.

Keep source code, tests and docs in Git. Keep private profiles and generated runs out. The packager uses explicit lists as well as path checks; don't rely on gitignore alone.

## Technical sources

The [source register](../creative-director/references/sources.json) keeps URLs, dates, document versions, supported claims and gaps. These dates are not automatically refreshed when copy changes. Recheck an API against the project's installed version before using it.

`python scripts/check_references.py --online` checks whether registered links respond. It doesn't prove that their content supports a claim. Failed requests stay unresolved. Offline checks need no network.

## Optional feedback tools

The [knowledge records](../maintenance/knowledge/README.md) preserve the comparison dataset, existing JSON profile format and reviewed-feedback tools. They are for advanced maintenance, not a requirement for giving design advice.

To add a comparison, use `python scripts/knowledge.py add-comparison record.json`. To validate an existing profile, use `python scripts/knowledge.py validate-profile path/to/.creative-director.local.json`.

For feedback, record the event privately and create a candidate. A separate human approval record is needed to promote it. The command creates a reviewable record; it doesn't rewrite the skill. One subjective opinion shouldn't become a universal rule.

## Try the behavior

Use the [evaluation guide](../tests/evaluation-rubric.md) for a small, realistic check before broad testing. Keep expected answers out of the agent's task. Record what happened; don't turn prepared scenarios into claims of executed results.

Frontmatter uses simple flat YAML fields with quoted descriptions. The helper parses only that form. Record validation supports the JSON Schema keywords used in the bundled schemas and rejects unsupported ones; it is not a general-purpose schema engine.
