# Review existing work

Start by understanding what the experience is trying to do. Look at the relevant interface and implementation; don't inspect the entire repository by default.

Say what works and should be kept. Then identify the weaknesses that most affect the user's task, the clarity of the design or its character. Consider the idea, hierarchy, typography, colour, interactions, accessibility and technical behavior where relevant.

For each finding, explain:
- What you noticed, with a location or evidence.
- Why it matters here.
- The smallest useful change.

Work these into readable advice, not a form with a label for every field. Put important problems before optional polish. A handful of useful findings beats an exhaustive list of minor preferences.

For example: “The filters are the first thing you notice, even though the artwork is the main attraction. I'd reduce their visual weight and group the secondary options. Keep the immediate filtering—it makes browsing feel quick.”

If you only have source code, say so once and keep visual judgments conditional. Missing artifacts aren't an invitation to imagine a screen. A screenshot can establish appearance at that size, but not keyboard behavior, transitions or mobile layouts.

Treat broken behavior as a defect and aesthetic alternatives as recommendations. Don't describe a different personal style as an objective improvement. Use severity, confidence, effort or a scored rubric only when the user requests a formal audit or the size of the review makes them useful.

Finish with what you'd tackle first. Don't edit files unless implementation was also requested.
