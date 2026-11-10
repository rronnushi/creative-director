# Games and playful experiences

Use this when the experience has a playable loop, challenge or progression.

Describe the loop in one sentence: what the player does, what feedback they get and how that changes their next choice. Make the rules and consequences legible before adding effects.

Difficulty should come from learnable decisions or skills. Smaller touch targets, unclear collision rules and hidden information are rarely good substitutes. For procedural levels, check solvability where possible and keep representative seeds for replay.

Separate simulation from drawing. Base movement on elapsed time; use a bounded fixed-step approach where consistent physics matters. Clamp large time gaps after suspension so returning to a tab doesn't run a huge catch-up loop. Pause, restart and failure recovery are part of the experience.

Offer suitable keyboard and touch controls. Keep visual feedback clear while motion and sound add character. Consider slower or untimed options when speed isn't essential to the concept.

A tile puzzle can validate a solution before shuffling. Its challenge can grow through relationships between tiles while controls remain comfortable. A fast action game may need different accommodations and input testing.

Test a complete play/restart cycle, pause/resume, a range of seeds and longer sessions. Automated checks can establish rules or solvability; human playtesting is needed to assess fairness, feel and fun.

Technical loop guidance: `games` in [sources](sources.json).
