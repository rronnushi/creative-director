# Make it fit your taste

Start with a short note in your project's own instructions. Be specific about what you want and why:

> Keep the layout dense and editorial. The collection should feel easy to browse, with the artwork taking most of the space. Use expressive typography for headings, but keep controls compact and readable.

You can also name what should stay unchanged:

> Keep the existing palette and square previews. Improve navigation without redesigning the gallery.

Creative Director should use your direction ahead of its default preferences. It should still point out a real usability or technical problem and explain the tradeoff.

## Existing JSON profiles

The `.creative-director.local.json` format still works. Put it in your project root, not inside the installed skill. Its `preferences` entries describe a preference, context, reason, exception and whether it was explicit or inferred. Optional `case_files` point to private case studies.

A [sample profile](../maintenance/knowledge/profile.example.json) and validation tools remain in the repository for people who want them. You don't need to create records or use the CLI for ordinary design advice.

Keep profiles and private case studies out of public uploads. Don't mistake an implementation choice for something the user approved. Changes to shared skill guidance should be reviewed rather than learned automatically from one conversation.
