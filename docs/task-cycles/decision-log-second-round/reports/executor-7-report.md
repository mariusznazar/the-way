# Report of the executor of slice 7

**Status:** done

**Commits:** `a71a414` Remove the withdrawn decision numbers from the foundation review and instruction files skills and give each rule its reason

**Files changed** (33 lines added, 26 removed): `foundation-review/SKILL.md`, `proposals.md`, `remarks.md`, `weak_points.md`, `with_the_human.md`; `instruction-files/SKILL.md`, `judging.md`.

## Checks
- `python -B elements/common/foundation_check.py` — exit 1 (expected until the last slice); 392 lines, none naming a file of `foundation-review/` or `instruction-files/` (grep of its output for both directories: no hit).
- `python -B gate/run_tests.py instruction-files` — exit 0, 104 tests, OK (5 skipped, POSIX-only).
- `python -B agent-instructions/skill_entry_points.py` — exit 0, "entry points are current".

## Own-work check
Requirement most likely missed: a number of WAY-257, 301-305, 311 or 354 left in a file of the slice.
Check: `grep -rnE "WAY-(257|301|302|303|304|305|311|354)\b" foundation-review instruction-files` — no hit after the edits. None of these eight numbers is in the log as it stands (headings searched), so none falls under the "stays" rule.

## Reasons added (file, sentence, entry read at base ec7929d)
- `foundation-review/SKILL.md` (opening paragraph, after "(WAY-14)."): "A change to a decision passes the review of an agent that did not make it and the search of the foundation, and a review that made the change itself would turn into a small task cycle." — WAY-302 *Rationale*.
- `foundation-review/SKILL.md` (step 7, first bullet): "A tag stays where the review was made, also when the review changes nothing, and gives the count a starting point in git itself, with no file kept in step by hand." — WAY-301 *Rationale*.
- `foundation-review/proposals.md` (transitional state): "...gains no field: the tasks of a product lie outside its repository, so an entry has no name to give a task that stands in no project plan." — WAY-354 *Rationale*.
- `foundation-review/remarks.md` (opening paragraph): WAY-304 reason "Each review reads the remarks of the repository it answers for, so none of them judges a remark twice and the review of the-way does not grow with each product."; the missing rule sentence "No other periodic review reads these remarks." added first; WAY-303 reason "One review reads them together with the foundation, which rules out two judgments of the same remarks in two places that can disagree." — WAY-304 and WAY-303 *Rationale*.
- `foundation-review/weak_points.md` (end of the "Run the check" paragraph): "A check that only reads is cheap enough to run at every review, where a check that acts would cost more than the review." — WAY-305 *Rationale*.
- `instruction-files/judging.md` (row paragraph): "A human disputes a judgement row by row, and a row that holds two verdicts, or a proposal folded into another row's reason, can be disputed only as a whole." — WAY-311 *Rationale*.
- No reason added for WAY-257 (the section did not ask for it; `judging.md` already says the criterion is shown "so that the human can disagree with the criterion and not only with the verdict").

## Choices
- WAY-305: reason put at the "Run the check" paragraph, not at the listing, as the section's first choice gives; the other half of the *Rationale* (the weak point shows its cost only when someone reads today's state) is not written. Cost if wrong: one reason fewer in the file.
- WAY-354 in `proposals.md`: of the *Rationale*, I took the reason of "no field" because the sentence it follows is that rule; the reason why the review asks about transitional states is not written there.
- Where a bracket stood alone after a colon or at the end of a sentence ("(WAY-257):", "(WAY-302):"), the colon or full stop stays and the space before the bracket goes.

## Entries left under the "stay" rule
None: none of the eight numbers of the slice is among the ten that stay.

## Reaches beyond the dispatch
None.

## Unread material
`foundations/decisions.md:9771-9810` WAY-293 read to its Rationale start (lines 7171-7212 as it stands); the rest of its Rationale was not read. All other entries read whole at the base (WAY-257 too). The task passage `task.md:33-40` read (lines 25-49).

## Searches not found or unclear
None. (The plan's line numbers are of the base; numbers found by search.)

## Working copies
`.runs/executor-7/` held `base.md` (the base log) and output files of the checks; removed before return.
