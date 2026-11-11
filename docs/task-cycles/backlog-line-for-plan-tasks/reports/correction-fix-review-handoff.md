# Handoff — review of the fix of the correction review's finding

You are the reviewer of this cycle, resumed to review the fix once. The orchestrator's delegation
stands; nothing here is a human's approval.

- Method: `task-cycle/review/SKILL.md`, and `fix.md` beside it (the review of a fix). Read it and
  follow it.
- Worktree (read-only): `the task's worktree root`,
  branch `task/backlog-line-for-plan-tasks`.
- Fix range: from the head you reviewed, `047a9e7606e90dc164762bebb0c6bc48dcd46eeb`, to
  `80126daf0834fc1d5fa589ebaea6e2cdff9db6f5` (one commit, `80126da`, one file:
  `foundations/decisions.md`). Compute the diff yourself and confirm `git rev-parse HEAD`.
- Findings file: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-fix-findings.md` —
  your B1, in your words, copied without change. The author's report, claims to verify:
  `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-fix-report.md`. Your three Minor
  findings of that review were not part of this fix and are not yours here.
- Judge B1 as fixed or remains. In particular: that WAY-154 now says the refiner brings the lines of
  the tasks tied to its task into agreement as the task place's rules give, in its binding part, its
  *Verification* and its *Rationale*'s accepted risk, and that the four skill files and `task_line.md`
  say no more than the entry (WAY-263); that WAY-154 holds one to three binding sentences; that
  nothing of how a line is handled (the task place's rules) entered WAY-154 or a skill; that the
  `the cycle's` mark and the entry agree with WAY-114; that no line added is over 100 characters;
  and whether the fix adds a new Critical or Important defect (a changed word or a lost
  qualification in the rest of WAY-154's text, checked word by word against `047a9e7`).
- Checks: `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`,
  `python -B task-cycle/test_tracked_files_private_paths.py`. Not the `project-level` directory and
  not the full suite.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-fix-review-report.md`,
  first line `PASS <head sha>` or `FAIL <head sha>`, B1 as fixed or remains, new findings,
  **Declined to judge**, each check with command and exit code, each reach beyond this dispatch,
  **Unread material** and **Searches not found or unclear**. Return the first line, the counts of
  blocking, Minor and out-of-scope findings, a one-line check result and the report path.
