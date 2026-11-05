# Handoff — review of the whole change

You review the whole change of one task as an agent that did not make it. The person who requested
this cycle has delegated intermediate choices to the orchestrator; nothing here is the human's
approval. You alone grade and scope your findings.

- Worktree (work from its root, read-only; branch `task/stage-remarks-check`):
  `C:\Storage\repos\the-way\.runs\worktrees\stage-remarks-check`
- Method: `task-cycle/review/SKILL.md` in that worktree, read whole; the review of the whole
  change — read `task-cycle/review/whole_change.md` as it says. You select your own foundation
  entries and guidelines (the-way has no `guidelines/` directory).
- Range: base `b96cfff` (current `origin/foundations`) to head `5e90498`. Compute the diff yourself
  (`git diff b96cfff..5e90498`) and confirm `git rev-parse HEAD` is `5e90498`.
- Frozen task, whole: `.runs/task-cycles/stage-remarks-check/task.md`. No spec, no plan (one
  author, no slices).
- The author's report, claims to verify:
  `.runs/task-cycles/stage-remarks-check/reports/01-author-report.md`. No slice reviews existed;
  you judge the whole range.
- Answers at start: trust boundary: no; irreversible operation: no; no reserved choice. The task
  moved no pin.
- External material the task rests on, read-only, outside the repository: the nightly digest
  `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py`
  (`_opens_block`, `extract_remark_blocks`) and the archives
  `31ac651`, `b311814`, `d79c8e4` in `C:\Storage\repos\loop2` (read with `git show`, never
  checked out), for the task's second acceptance criterion. You may re-run the author's acceptance
  commands in a scratch directory outside the worktree; do not write into the worktree.
- Checks already known: base `python -B gate/run_tests.py` at `b96cfff`: 667 tests, exit 0. The
  orchestrator runs the full gate on the change; you do not. You may run
  `python -B gate/run_tests.py task-cycle`.
- Check in particular: that the script's listing matches the task's *To do* 1 and the acceptance
  criteria (both report forms, only items other than `none`, matching word for word inside the
  block the digest cuts); that the process text (SKILL step 12, step 9.4, correction, blocked
  variants) leaves no commit that adds the record without the check; that the rule for a listing
  held wrong equals the task's row 2; that the template form meets the digest's cut; that WAY-294 to
  WAY-296 carry rows 1–3 faithfully and do not contradict WAY-260/148/290/291.

Write the report to `.runs/task-cycles/stage-remarks-check/reports/02-whole-review-report.md` as
the method gives it; its first line is `PASS <sha>` or `FAIL <sha>`, then the graded findings, the
checks you ran with command and exit code, and **Searches not found or unclear** (each item or
`none`). Return the status line, a one-line check result and the report path.
