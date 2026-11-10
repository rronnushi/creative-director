# Contributing

The most useful contribution starts with a real task and a specific problem. Show what the agent did, what you expected and the context needed to understand the difference.

Keep changes focused. Prefer one useful correction to more general instructions. Examples should sound like something a person would ask and another person would answer. Don't turn personal taste into a universal design rule.

For technical advice, use primary documentation and record the version or review date in the source register. Clearly label invented examples. Don't contribute private project material or third-party assets without permission.

Run the relevant checks from the repository root:

```sh
python scripts/validate_skill.py
python scripts/check_references.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/package_release.py dist/creative-director-1.1.0.zip
```

The [maintainer guide](docs/maintenance.md) explains the optional feedback tools and test scenarios. Tests and release tools belong in the repository, never in the installed skill. When adding public files, update the root release manifest and check the archive contents.
