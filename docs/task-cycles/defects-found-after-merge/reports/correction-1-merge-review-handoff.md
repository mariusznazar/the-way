# Handoff — the review of the merge of the target branch, correction 1, `defects-found-after-merge`

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; nothing
here is that person's approval. You did not make or review any part of this change. Read-only: change
nothing, commit nothing. Work from the worktree
`the task's worktree, which is the repository's root` (branch
`task/defects-found-after-merge`); start every command from its root.

## Stage and method

Stage: review the reconciliation with the target branch (the merge commit `73fb11d`). Method:
`task-cycle/review/SKILL.md` of this worktree; read it whole and a file it names only when the step
or variant that names it comes.

- The merge: `73fb11d`, parents `a3152c9` (this branch before the merge, already reviewed and
  passed) and `65b6d70` (the target branch `foundations` with pull request #108 merged, after this
  branch's base `6814c6f`). Look at it from both sides: `git diff a3152c9 73fb11d` (what the merge
  brought in and changed) and `git diff 65b6d70 73fb11d` (what this branch adds on the target
  branch now).
- The author's report: `.runs/task-cycles/defects-found-after-merge/reports/correction-1-merge-report.md`.
- The reason for the merge's one change of this branch's own text: both sides added decisions
  numbered WAY-353 and WAY-354; the target branch's two keep their numbers and this branch's five
  new decisions became WAY-355 to WAY-359, in their order (old 353→355, 354→356, 355→357,
  356→358, 357→359), with the references to them.
- Trust boundary: no. Irreversible operation: no.

## What to judge

The question of this review is whether the two sides still hold together:

1. The renumbering is complete and right: every reference to this branch's five decisions, in the
   files this branch wrote or changed, now carries the new number, and no reference of the target
   branch to its WAY-353 or WAY-354 was changed. Check with `git diff 6814c6f a3152c9` (the lines
   this branch added under the old numbers) against the same places in the merge, and by reading
   each decision's *Relations* and *Based on* lines.
2. No decision of the target branch changed, and no decision of this branch changed in meaning
   (`git diff a3152c9 73fb11d -- foundations/decisions.md` and the file against `65b6d70`).
3. What the target branch brought in that bears on the parts this change touches still agrees with
   it: the target branch's WAY-353 and WAY-354 (a task document's pointer to a place to change; the
   review of the foundation and transitional states), the change to WAY-327 and the fifth part of
   "What an item carries" in `task-cycle/skill/request_template.md`, the closing paragraph of
   `project-level/task/template.md` against this branch's line `Defect introduced by:`, the new
   paragraph of `project-level/task/skill/draft.md` against this branch's fill-in step, and the
   glossary term the target branch added. Check kind 17 of the request template against the
   target branch's change of kind 4.
4. The checks the merge touches: `python -B elements/common/foundation_check.py --skip-test-citations .`
   and `python -B gate/run_tests.py <directory>` for `task-cycle`, `process-audit`, `project-level`,
   `elements/common`, `agent-instructions` (the full gate is the orchestrator's, not yours).

The author reports that it read the target branch's WAY-353 and WAY-354 by heading and block
boundary only; you read them whole.

## What to read (selection by the orchestrator, WAY-150, WAY-213)

Decisions, each whole: WAY-353 and WAY-354 (the target branch's), WAY-355 to WAY-359 (this branch's),
WAY-287, WAY-327, WAY-286, WAY-337, WAY-306. Files: `task-cycle/skill/request_template.md`,
`task-cycle/skill/correction.md`, `task-cycle/record_template.md`,
`project-level/task/template.md` and `project-level/task/skill/draft.md` (each whole), the glossary
entry the target branch added. No product guidelines exist in this repository.

## Report

Write the full report to `.runs/task-cycles/defects-found-after-merge/reports/correction-1-merge-reviewer-report.md`
in the form the method gives; its first line `PASS <sha>` or `FAIL <sha>`. Include the checks you
ran with command and exit code, **Unread material** and **Searches not found or unclear** (each
`none` where none). Return only the first line, the finding counts by grade and the report's path.
