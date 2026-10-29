# The human's remarks on request #53 — correction

Request: https://github.com/mariusznazar/the-way/pull/53, branch `task/rejected-from-refinement`,
head `718c9dc9ad0f728761c7c9ce2eee0a69e6c05b48`.

Mariusz, 2026-10-29, in the session that ran the cycle, answering whether the two Minor findings
below are corrected in this request before the merge: „popraw proszę”. The two findings, in the
reviewers' words (`reports/04-review-report.md`, Minor 1 and 2; repeated in
`reports/08-return-review-report.md`):

1. **`elements/decisions/skill/SKILL.md:36` now restates a rule the template holds.** The change
   adds to `elements/decisions/template.md:57–58` "`none considered` in *Rejected* says the human
   weighed no other way", while the skill keeps "`none considered` in *Rejected* is the human's
   statement." Before the change the rule stood only in the skill; after it, it stands in both —
   the very case WAY-35 rejects ("rules restated in the skill next to the template — two copies
   that drift"). […] Fix: drop the skill's line 36 (the skill reads the rule from the template).

2. **`task-cycle/skill/foundation_step.md:22–24` paraphrases the exception without
   `none considered`.** It says a decision's *Rejected* "takes the ways not chosen that the row's
   source keeps, or `unknown`, as the decisions' template gives". The pointer to the template makes
   it correct, but a writer reading only this step sees two outcomes where WAY-134 sentence 3 and
   the template give three. Fix: name all three or drop the paraphrase and keep only the pointer.

These remarks bind. Nothing else is to change.
