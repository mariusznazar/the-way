PASS a3152c967c05f4013e37598104174ce0280eec64

# Review of correction 1, `defects-found-after-merge`

Range: `716b22a..a3152c9` (one commit, one file: `task-cycle/skill/request_template.md`, +6 -1).
`git rev-parse HEAD` = `a3152c967c05f4013e37598104174ce0280eec64`, the head given. Worktree clean.

Counts: blocking 0, Minor 2 (within the task), out of scope 1.

## The remark: made

The remark (item 3 of *Fix or let through*) asks for the sentence, or an example of it, that a
correction only refreshing the target branch carries with `target-branch · none`, so the writer does
not improvise it. **Made.** `task-cycle/skill/request_template.md:319-321` gives, in kind 17, that the
cycle judged nothing for this pair and an example sentence ("This correction only refreshed the
branch from the target branch at your request; nothing else changed, and the cycle made no judgment
of whether the task required anything."). The two items of *Needed from you* are outside the
repository and the diff does not touch them.

The correction adds a second example, for a correction with two sources (`request_template.md:321-324`).
It is the same sentence of the same kind in the case `correction.md` and WAY-356 already name ("each
pair once", "two pairs"), so I judge it within the remark, not an addition nobody asked for.

## Agreement with the decisions and files

- WAY-287 (complies case: one sentence in *You accept by merging* saying the correction answered
  the remark and whether the cycle judged the task required it) and WAY-356 (`none` only with
  `target-branch`; each pair once; the description shows the pairs in one sentence): the new text
  agrees. It restates `none` as "the cycle judged nothing" and does not widen or narrow the rule.
- WAY-355, `task-cycle/record_template.md:190-211` (the line of a correction and the source/kind
  meanings): agrees; `target-branch` = a correction that exists only to refresh at the human's request,
  which the example says ("at your request").
- `task-cycle/skill/correction.md` (step "Rewrite `request.md` ... with the pairs of the correction in
  one sentence as the item of kind 17"): agrees and needs no change.
- WAY-286 (top part in plain words, no file names, no identifiers of entries): the two example
  sentences hold no file name, no WAY number and no pair notation; the pair notation
  `target-branch · none` stands only in the instruction to the writer, outside the sentences placed in
  the description. "Target branch" is the same word the template uses elsewhere in the top part.
- WAY-289, WAY-306, WAY-337: not reached by the diff (they concern items 8, 4, 9, 14, the review of
  the merge and the cost).
- A reader of the text: `task-cycle/request_check.py` judges headings and the three groups, not the
  content of an item; `task-cycle/test_request_check.py` reads the template only for the skeleton
  block and the *For you to decide* example block (`:898-922`), neither of which the diff touches.

## Findings

### Critical, Important

none

### Minor (within the task)

1. **`task-cycle/skill/request_template.md:321-323` — "a defect the task required".** In the
   two-source example, "your remark about a defect the task required" reads, to the human, as if the
   task required the defect. What `remark · defect` means is that the task or the foundation required
   what the correction changed, or that it is a regression (WAY-356, `record_template.md:207-210`).
   The phrase is borrowed from the *complies* case of WAY-356, which has the same wording, so the
   correction agrees with the decision; the effect is only a sentence the writer copies that a human
   may read twice. A wording such as "your remark, and the cycle judged that the task required what
   it asked to change" says it without the misreading. Blocks nothing.
2. **`request_template.md:323-324` — "which the cycle judged nothing about".** The relative clause
   follows "at your request", so "which" can be read as the request, not the refreshing. Evidence:
   reading the sentence alone. A short sentence or a semicolon before "and the cycle judged nothing
   about the refresh" removes it. Blocks nothing.

### Out of scope (stated as such)

3. **`request_template.md:457` (the variants table, row "A correction").** The state line of a
   correction is to carry "corrected for your remarks" in the why; for a refresh-only correction there
   are no remarks of the human to correct for, so the writer improvises that line too, the same kind of
   gap as the remark. It is outside the remark (which names the sentence of kind 17) and the correction
   did not touch the row, so nothing here fails. A candidate for a later remark or task.

## Declined to judge

- Whether kind 17 should also give an example for `not-required`: the remark names only the
  refresh-only pair; the existing sentence of the kind already covers the other pairs.
- The wording of the earlier sentence of kind 17 and the rest of the template: unchanged by the
  diff (its line `the merge.` is rewritten only to carry the new sentences after it; its wording is
  the same).
- Whether a test of the wording is needed: the author argues none; the template's prose is an
  instruction to the writer and the check judges no content (WAY-290). I agree and set it aside.

## Checks I ran (from the worktree's root)

- `git diff 716b22a..a3152c9`, `git log 716b22a..a3152c9`, `git rev-parse HEAD`: as above.
- `git diff --check 716b22a..a3152c9` — exit 0.
- `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` — exit 0
  ("checked: 1 files, 0 listed").
- `python -B -m unittest task-cycle/test_request_check.py` — exit 0 (74 tests, OK).
- `python -B gate/run_tests.py task-cycle` — exit 0 (367 tests, OK).
- `python -B elements/common/foundation_check.py --skip-test-citations .` — exit 0 (0 errors).
- Manual: read the two new sentences against the top-part rule of WAY-286 and the pair meanings of
  WAY-356; result as under "Agreement" above.
- Not run: the full gate (the cycle's own run, not repeated).

## Reaches beyond the dispatch

- `grep -rn "request_template" --include=*.py .` and `grep -rn "kind 17|item 17|cause of a
  correction"` over `*.md`, `*.py` outside `.runs` and `foundations/`: to find readers of the changed
  text. Found `task-cycle/test_request_check.py:24,900,914` (skeleton and example block only),
  `task-cycle/skill/correction.md:49` and `request_template.md:457` (the variants row, see finding 3).
- `task-cycle/review/fix.md` (named by `SKILL.md` for the review of a correction): read whole.
- `request_template.md` lines 898-922 of the test file and `request_check.py` by grep only, to see
  what reads the template.

## Unread material

Everything the dispatch names was read whole: WAY-287, WAY-356, WAY-355, WAY-286, WAY-306, WAY-337;
WAY-289 read whole except the last lines of its *Rejected* paragraph (after "the same ..." at the
end of the part I read); `request_template.md` and `correction.md` whole; `record_template.md` the
item *Corrections after the request opened* and its paragraph (lines 190-215). Also not read: the
author's report's section on its own foundation search (read), the frozen task (not needed),
`task-cycle/request_check.py` (grep only).

## Searches not found or unclear

none
