# Author report — correction 1

**Status:** done. **Commit:** `637d7787` (range from `20332036`; 5 files, 64 added, 10 removed). The return step is not taken, as the handoff says.

## The remark and how it was met

The human's answer to item 1 (word for word, `reports/correction-1-remarks.md`): "fix it in this request, with the answer the reviewer proposes: the second rule narrows the first, and refinement puts what an adopted practice leaves out among the ways the person weighs, so the row that settles it names them. Write that answer into both rules where they stand, so that each names the other, and into the refinement step that builds the rows of settlements. The two new decisions of this request stay as they are now (without the reverted additions)."

- **(a) the second rule narrows the first.** `foundations/decisions.md`, WAY-134: *Relations* now `derives from WAY-33 · narrows WAY-114 · narrows WAY-100`, and a new second paragraph of binding sentences: where a row adopts a practice from outside, the refinement shows the human the parts the practice leaves out among the ways of the question, so the row's source keeps them and the decision's rejected options take them; where the source keeps none, the decision names what it takes in its binding sentences or *Rationale* as WAY-100 gives and puts no left-out part in its rejected options; "In this area this decision prevails over WAY-100, which asks a decision that adopts a practice to put what it leaves out in *Rejected*". Its *Verification* pair, *Rationale* (with the price) and *Rejected* (two ways: the cycle taking the left-out parts into *Rejected* by WAY-100 prevailing; the two rules left with no precedence) carry it.
- **(c, first half) each rule names the other.** WAY-100 has a new third paragraph of binding sentences naming WAY-134: a decision written from a row takes the ways in its *Rejected* from the row's source, which keeps the parts the practice leaves out where the human weighed them, "as WAY-134 gives; there WAY-134 prevails over the paragraph above"; a pair in *Verification* and a sentence of *Rationale*. WAY-100 cannot carry `narrows WAY-134` (it is the narrowed one), so it names it in its binding sentence.
- **(b) and (c, second half) the refinement step that builds the rows.** The step is the skill `find-foundation-entries` in task mode, called by `refine-task`: `elements/common/skill/task_variant.md` (step 2: a row that adopts a practice from outside is built `waiting`, not as the human's choice, unless its question showed the left-out parts as ways; otherwise the question of "How a skill asks" shows them before the row is accepted); `project-level/task/template.md` (*Questions to settle*: a question that settles such an adoption shows the left-out parts among its ways; *Settlements to record*, *Source*: such a row names among the ways each part the human turned down, and the cycle puts none there the source does not keep); `project-level/task/skill/find_settlements.md` (the refinement's own paragraph). The writer's side stands in `elements/decisions/template.md` (the bullet on the *Rejected* of a decision written from a row).
- **WAY-409 and WAY-410 stay as they are.** The new rule gives them what they already do: both name in *Rationale* what they take from the card and the paper, and hold in *Rejected* only the ways their rows' sources keep, with no left-out part. The check below confirms the two entries are byte-for-byte those of the reviewed head.
- **WAY-25.** The passage of the answer that gives the precedence is "the second rule narrows the first" (the second rule being, in the order of the remark's item, the rule on a decision written from a row, WAY-134, and the first the rule on a decision that borrows an outside practice, WAY-100). It is recorded as the template gives it: the prevailing decision names the other under `narrows` and states in its binding sentences the area where it prevails.

## Choices (way rejected, cost if wrong)

1. **Where the answer enters WAY-134: a second paragraph of binding sentences, not a longer first paragraph.** The first paragraph already holds a long sentence and the new rule answers a part of the question (what a row that adopts a practice does). Rejected: appending to the first paragraph. Cost: a paragraph to merge.
2. **WAY-100 names WAY-134 in its binding text, and states the precedence there too** ("there WAY-134 prevails"). The template puts the statement in the prevailing decision; I repeated it in the narrowed one because the human asked that each rule name the other and a reader of WAY-100 alone must not read the opposite rule. Rejected: a pointer without the outcome (a reader would meet two rules with no answer). Cost: the outcome stated in two places; both agree.
3. **The refinement builds such a row `waiting`** unless the question showed the left-out parts. Rejected: building it accepted as the human's choice, as for any row that repeats a choice between ways shown — that is what let the parts slip through unseen. Cost: one more question in a refinement that adopts a practice.
4. **`task-cycle/skill/foundation_step.md` and `elements/common/way_of_working.md` left as they are.** Both say the *Rejected* of a decision from a row takes the ways the row's source keeps, which the narrowed rule keeps true. Rejected: adding a pointer (no sentence became false). Cost if wrong: a reader of the foundation step does not see the exception; the decisions template carries it.
5. **The change of WAY-134's rule on *Rejected* edits an approved decision in place** (WAY-07), by the human's answer; no question to the orchestrator arose, since the answer gives the meaning (a narrowing and the refinement step).

## Search of the foundation (WAY-33): places and what I did

- `foundations/decisions.md`: searched for "rejected options", "source keeps", "ways not chosen", "leaves out"/"left out", `WAY-100`, `WAY-134`. Changed WAY-100 and WAY-134 only. Left: the decisions that derive from WAY-100 (many, such as WAY-164, WAY-229, WAY-256): their sentences hold, since the narrowing concerns only a decision written from a row; WAY-409 and WAY-410 (they comply, unchanged); the decisions whose *Rejected* hold "left out of what the decision takes from X" (written from the cycle's own sources, unaffected).
- `foundations/invariants.md`: searched for the two decisions, no invariant derives from them; no test holds a sentence of them (`decision: WAY-100` and `WAY-134` found in no file).
- `elements/decisions/template.md`: changed (the bullet on *Rejected* of a decision from a row). `elements/decisions/skill/*.md`: no sentence on *Rejected* of a row; left.
- `elements/common/skill/task_variant.md`, `build_table.md`: changed `task_variant.md` (step 2); `build_table.md` states only how a candidate that repeats a choice is built, true as it stands; left.
- `project-level/task/template.md`, `project-level/task/skill/find_settlements.md`: changed. `project-level/task/skill/orchestrated_mode.md`: copies a settled question whole with its *Not chosen*; true as it stands; left.
- `task-cycle/skill/foundation_step.md`, `elements/common/way_of_working.md`: left (choice 4).
- `product-guidelines/template.md`, `foundation-review/weak_points.md`, `project-level/definition_template.md`, `project-level/readiness_check.py`: mention *Rejected* in other senses; left.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0 (270 tests); `project-level` — exit 0 (279 tests); `task-cycle` — exit 0 (534 tests). Directories chosen because they hold a test that reads a file I changed or a file of the part. `elements/decisions` holds no test.
- Not run: the full gate (not mine; and the human's standing instruction on its start signal is the orchestrator's).

## Own-work check (WAY-164)

- Requirement most likely not met: "write the answer into both rules where they stand, so that each names the other, and into the refinement step", with the two new decisions unchanged.
- Check: `reports/author-correction-check.py ROOT BASEROOT`, 13 assertions: WAY-100 and WAY-134 each name the other; WAY-134's *Relations* carries `narrows WAY-100`; it states the area where it prevails, what a decision holds where the source keeps none, and that the refinement shows the parts as ways; WAY-100 says WAY-134 prevails for a row; the decisions template, the task-mode variant, the task template (both places) and `find_settlements.md` carry the answer; the entries WAY-409 and WAY-410 are identical to the reviewed head's.
- What it showed: 13 of 13 ok on the changed tree (exit 0); run on the reviewed head's files against themselves it failed 11 of 13, and the two assertions on WAY-409 and WAY-410 passed there as they must, so the check tells the changed text from the unchanged. It reads wording by pattern; it cannot show that the narrowing reads right to a later cycle, which the review of the correction must judge.

## Reaches beyond the handoff

- `elements/decisions/template.md` (changed, read whole in the first dispatch), `elements/common/skill/task_variant.md`, `build_table.md`, `project-level/task/template.md` (read whole now), `project-level/task/skill/find_settlements.md`: as the handoff points at the refinement step.
- `elements/common/way_of_working.md` lines 130-150 (the sentence on *Rejected*), by grep and a short read.
- The text of WAY-134 (*Rationale*, *Rejected*) and WAY-100 whole: read to edit them.

## Unread material

- `elements/common/skill/SKILL.md` and `elements/common/skill/read.md` (the skill `find-foundation-entries` itself): not read whole; the step the correction touches is its task variant.
- `project-level/task/skill/orchestrated_mode.md`: read only the line that copies a settled question (grep).
- `reports/review-return-report.md`: read its finding 2 and "Third question" only, as the handoff says.

## Searches not found or unclear

- A single "refinement step that builds the rows" was not found: the building is split between `elements/common/skill/task_variant.md` (the skill `find-foundation-entries` in task mode), `project-level/task/skill/find_settlements.md` (the call from `refine-task`) and `project-level/task/template.md` (what each section carries); I wrote the answer into each, which means the rule stands in three places that must stay equal.
- Which of the two rules the remark's "second" and "first" name was unclear from the item alone; I read it by the item's own order (a decision that borrows an outside practice first, a decision written from a row second), which agrees with the reviewer's recommendation "WAY-134 narrows WAY-100".

## Working copies

`.runs/author-correction/` of the worktree held a scratch copy of the changed files at the reviewed head (`base/`), the check script and the outputs of the checks; removed. Kept in `reports/`: `author-correction-check.py`. No worktree or clone was made.
