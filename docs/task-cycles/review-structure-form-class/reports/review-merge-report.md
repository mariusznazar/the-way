PASS 3e934b6

# Review of the reconciliation with the target branch, `review-structure-form-class`

Range `b596eec..3e934b6` (two commits: `c756236` the renumbering, `3e934b6` the merge of `origin/foundations` `8079485`).
`git rev-parse HEAD` is `3e934b6f79038eef813c3882a2732c6949144ef3`, as the dispatch gave.

Counts: blocking 0, Minor 0, out of scope 0.

## Findings

None. The two sides hold together.

### 1. The renumbering (`c756236`)

- `git diff b596eec c756236` is 12 files, 33 lines changed, 35 places (`--stat`: 33 insertions, 33 deletions). I paired each removed line with its
  added line by script: with the numbers of the WAY identifiers taken out, every pair is the same text, and each changed number goes from n to n+5 with
  n in 355 to 360. No line of text changes, no number outside 355 to 360 changes (0 bad pairs).
- Meaning of each number by the headings: old 355 (rule of size in the template) is now WAY-360, 356 (sizes from a product) 361, 357 (structure the review
  asks) 362, 358 (grade of structure) 363, 359 (grade of form) 364, 360 (addition over the threshold) 365. Each use sits next to the sentence of its own
  entry: for example `product-guidelines/coding/template.md:65` names the rule of size and cites WAY-360, `task-cycle/plan/SKILL.md:179` names the test
  that lists what stands over a threshold and cites WAY-361, `task-cycle/review/SKILL.md:128` the grade of structure and cites WAY-363,
  `task-cycle/review/SKILL.md:133` the grade of form and cites WAY-364, `task-cycle/change/SKILL.md:54` the move before an addition and cites WAY-365.
- Searched the whole tree (`git grep -E 'WAY-(35[3-9]|36[0-9])'`): in the 12 renumbered files, and in `foundations/decisions.md` inside this branch's six
  entries, only WAY-360 to WAY-365 occur (the six entries cite no other number of the range). WAY-355 to WAY-359 stand in files the target branch wrote
  (`project-level/task/skill/draft.md`, `project-level/task/template.md`, `task-cycle/record_template.md`, `task-cycle/skill/correction.md`,
  `task-cycle/skill/request_template.md`, and the entries themselves in `foundations/decisions.md`) and each of them means the target branch's entry
  (checked against the headings: WAY-355 which task fixes a defect, 356 where it is recorded, 357 the cause of a correction, 358 the causes the line gives).
  WAY-353 and WAY-354 stay, and are used only by `foundation-review/*` and `project-level/task/*`, which this branch does not touch.
- `product-guidelines/coding/task_document.md` is in the list of this branch's files and its line 25 now cites WAY-360 and WAY-361.

### 2. The resolution of the conflict (`foundations/decisions.md`)

- `git diff 8079485 3e934b6 -- foundations/decisions.md` has four hunks: `@@ -4912` (in-place addition to WAY-164), `@@ -6882` and `@@ -6893` (in-place
  additions to WAY-229), `@@ -11959` (the six entries WAY-360 to WAY-365, appended after WAY-359). Nothing else. The six entries read, entry by entry,
  as the dispatch says: the headings in the order of the old numbers, WAY-360 derives from WAY-173 and WAY-168, WAY-361 from WAY-360 and WAY-16, WAY-362
  from WAY-136 and WAY-361, WAY-363 and WAY-364 narrow WAY-161, WAY-365 derives from WAY-136 and WAY-360.
- `git diff b596eec 3e934b6 -- foundations/decisions.md` has, besides the renumbered headings and references, only text of the target branch: the five
  entries WAY-355 to WAY-359 and the four hunks at `@@ -9184`, `@@ -9210`, `@@ -9232`, `@@ -9246` (the in-place addition to WAY-287, the cause of a
  correction). It holds no addition of this branch other than the renumbering (the hunks at 4912 and 6882 are absent from it, so they were already in
  `b596eec`).
- Every other file: `git diff 8079485 3e934b6 --stat` lists 15 files, all of this branch's; the 8 other files the target changed since the merge base
  (`process-audit/problem_register.md`, `process-audit/test_audit_count.py`, `project-level/task/skill/draft.md`, `project-level/task/template.md`,
  `task-cycle/record_template.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md`, `task-cycle/test_remarks_check.py`) are
  identical to the target's, and no file other than `decisions.md` was changed by both sides, so the merge brought no second conflict.

### 3. Whether this branch's text holds against what the target branch brought

- Read whole: WAY-355, WAY-356, WAY-357, WAY-358, WAY-359 (as the diff of `3e934b6` against `b596eec` gives them), and the four hunks of the in-place
  addition to WAY-287, and the diffs of the 8 target files listed above.
- The target's subject is defects found after a merge: the line `Defect introduced by:` in the task document, the record's item *Corrections after the
  request opened*, kind 17 of the request template, two classes of the register of problems. This branch's subject is the rule of size of coding
  guidelines, the grades of structure and of form in the review, and the move before an addition over a threshold. I looked for a sentence of this branch
  that restates what the record, the request, the task document's header or the register carries, or the grading of a finding at the request, and found
  none: `grep` of `product-guidelines`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/change_file_sizes.py` for `Project
  relation`, `Defect introduced`, `Corrections after`, `problem_register`, `defect-found`, `known-problem-left`, `kind 17`, `item 17`, `record_template`,
  `request_template` gives no line.
- The two sides do not contradict each other where they meet: this branch's WAY-363 and WAY-364 send a Minor finding outside the task to the request's
  list and say nothing of a correction's cause; the target's WAY-358 pairs (`remark · defect`, `item · defect`) say nothing of a finding's grade;
  `known-problem-left` in the register and a Minor finding on the request's list are different things the two sides each keep in their own place.
- The text of this branch that writes about what a coding-guidelines task document carries (`product-guidelines/coding/task_document.md`) names the
  rule of size and the other items and not the header lines of `project-level/task/template.md`, so the new line `Defect introduced by:` is not made
  to look missing there.

## Declined to judge

None. I set nothing aside as outside the task. The whole change against the frozen task was not judged again: the merge changed no file of this
branch's task-cycle or product-guidelines text except the numbers, so it could not change that answer, and the change itself was reviewed in
`reports/review-whole-change-report.md`, `reports/review-fix-report.md` and `reports/review-return-step-report.md`.

## Checks run

- `python -B elements/common/foundation_check.py` in the worktree root: output `0 errors`, exit code 0.
- `python -B gate/run_tests.py task-cycle`: `Ran 385 tests`, `OK`, exit code 0 (Warning lines of test sessions of the audit's reader are the tests'
  own fixtures).
- A script of my own (`python -B -I`, in the heredoc) on `git diff -U0 b596eec c756236`: 33 removed lines paired with 33 added, 35 changed numbers,
  0 bad pairs (each n to n+5, n in 355 to 360, text otherwise equal).
- `git diff 8079485 3e934b6 -- foundations/decisions.md`, `git diff b596eec 3e934b6 -- foundations/decisions.md`, `git diff 8079485 3e934b6 --stat`,
  `git diff 65b6d70 8079485 --name-only`, `git grep -nE 'WAY-(35[3-9]|36[0-9])'` over the tree: results as above.
- Not run: `process-audit` tests (the dispatch gives the orchestrator's run, 180 tests, exit 0) and the whole gate (the orchestrator runs it).

## Reaches beyond the dispatch

- `git grep` for WAY-353 to WAY-369 over the whole tree: to see whether a file outside this branch's 12 renumbered files holds a number that now
  means something else. None does.
- `grep` of this branch's files for the names of the target's artifacts (list above): to see whether a sentence of this branch restates them.
- `git diff 65b6d70 b596eec -- product-guidelines/audit_end.md product-guidelines/coding/SKILL.md product-guidelines/coding/task_document.md` and the diffs of
  `task-cycle/review`, `task-cycle/plan`, `task-cycle/change`: to read this branch's sentences next to the target's.
- `git ls-files .runs` and the listing of the reports folder: to confirm that no record of the cycle is tracked and carries the old numbers.

## Unread material

- WAY-287 I read by the hunks of the in-place addition and their context in the diff, not the entry whole; it is the target's entry and the addition
  concerns the request's description after a correction, which no sentence of this branch restates.
- `task-cycle/test_remarks_check.py` and `process-audit/test_audit_count.py` (the target's tests, 25 and 9 added lines): not read; the orchestrator ran
  `process-audit` (180 tests, exit 0) and I ran `task-cycle` (385 tests, exit 0).
- The frozen task `docs/task-cycles/review-structure-form-class/task.md` and the earlier review reports: not read, by the dispatch (the change is not
  reviewed again).
- Everything else the dispatch names I read whole.

## Searches not found or unclear

none
