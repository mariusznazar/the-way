# Handoff — the merge of the target branch into the request's branch (correction 1), `defects-found-after-merge`

Same delegation, worktree (`the task's worktree, which is the repository's root`),
branch and rules for commits as `reports/correction-1-author-handoff.md`. Stage: finish a merge that
is in progress; the method is `task-cycle/change/SKILL.md` as before, the variant that fits is "a
correction for the human's remarks" (the merge is part of the correction). Do not run the full gate
(the orchestrator's) and start no review.

## State

`git merge origin/foundations` is in progress in the worktree: nothing committed, one conflict in
`foundations/decisions.md`, the rest auto-merged and staged. `origin/foundations` is
`65b6d7007ec4fffad998612e5c521eee93c7b8b5` (it holds pull request #108, merged after this branch's
base `6814c6f`). Your commits and the earlier ones of the branch stand at head `a3152c9`. Do not
abort the merge, do not rebase and do not force anything.

## The collision

Both sides added decisions numbered WAY-353 and WAY-354. The target branch's two are already merged
into the foundation and keep their numbers: WAY-353 "How does a task document point at a place to
change in a file?" and WAY-354 "What does a review of the foundation do with a decision that
describes a transitional state?". This branch's five new decisions are renumbered, in order, to the
next free numbers:

| this branch's number so far | new number |
|---|---|
| WAY-353 (which task fixes a defect found after a merge) | WAY-355 |
| WAY-354 (where a defect found after a merge is recorded) | WAY-356 |
| WAY-355 (where the cycle records the cause of a correction) | WAY-357 |
| WAY-356 (what causes the line of a correction gives) | WAY-358 |
| WAY-357 (how the register template records the two defect classes) | WAY-359 |

## What to do

1. Resolve `foundations/decisions.md`: the target branch's WAY-353 and WAY-354 stay as the target
   branch has them, this branch's five follow in their order under their new numbers, with every
   reference inside them (*Relations*, *Based on*, rationale text) renumbered to match. No decision
   of the target branch changes.
2. Renumber every other reference to this branch's five decisions in what this branch wrote, and
   only there: find them in the lines this branch added — `git diff 6814c6f a3152c9` — in the files
   it touched (`task-cycle/record_template.md`, `task-cycle/skill/correction.md`,
   `task-cycle/skill/request_template.md`, `project-level/task/template.md`,
   `project-level/task/skill/draft.md`, `process-audit/problem_register.md`, the tests, and any
   other the diff shows; WAY-287, which this branch changed in place, included). Renumber from the
   highest number down, so that no number is changed twice. Leave every WAY-353 and WAY-354 that
   the target branch wrote or that its commits mention: those two are the target branch's.
3. Read what the target branch changed in the files this branch also changed (`git diff 6814c6f
   origin/foundations -- task-cycle/skill/request_template.md project-level/task/template.md
   project-level/task/skill/draft.md foundations/glossary.md`) and check that the two sides still
   hold together: the numbering of the kinds of items in the request template (kind 17 of this
   branch against what the target branch added), the header lines of the task template (this
   branch's line `Defect introduced by:` against the target branch's addition), the fill-in step in
   `draft.md`, and the glossary against the words this branch uses. Correct what collides, in the
   fewest words, and say what in the report.
4. Search the whole foundation once for any remaining stale reference to the old numbers of this
   branch's decisions (a grep of `WAY-35[3-7]` over the tracked files, read against the table above).
5. Check: `python -B elements/common/foundation_check.py --skip-test-citations .` and the tests of
   the directories you touched with `python -B gate/run_tests.py <directory>` (at least
   `task-cycle`, `process-audit`, `project-level`, `elements/common`, `agent-instructions` and
   `foundation-review`). Then commit the merge (`git add` by explicit paths, then `git commit` with a
   message in English that says that this is the merge of `foundations` and names the renumbering).

## What to read

Decisions each whole: the five of this branch (WAY-355 to WAY-359 as renumbered), WAY-353 and
WAY-354 of the target branch, WAY-287. `task-cycle/change/SKILL.md` as before.

## Report

Write the report to `.runs/task-cycles/defects-found-after-merge/reports/correction-1-merge-report.md`:
status, the merge commit, each file where a number changed with a count, what step 3 found and
corrected, checks with command and exit code, questions, concerns, **Unread material**, **Searches
not found or unclear** (each `none` where none). Return only the status, the commit, a one-line
check result and the report's path.
