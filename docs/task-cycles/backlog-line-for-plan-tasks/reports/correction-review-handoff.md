# Handoff — review of the correction for the human's remarks

You are the reviewer of the whole change, resumed to review a correction once. The orchestrator's
delegation stands; nothing here is a human's approval beyond what the remarks file quotes as his
words.

- Method: `task-cycle/review/SKILL.md`, and `fix.md` beside it (a correction made for the human's
  remarks is reviewed as a fix, the remarks standing in place of a findings file). Read it and follow
  it.
- Worktree (read-only): `the task's worktree root`,
  branch `task/backlog-line-for-plan-tasks`.
- Correction range: from `7ca864236afac802d03ebb74d3fbe66bee1b755d` (the commit that removed the
  record's copy; its tree equals that of `06144e9`, which your earlier reviews covered) to
  `047a9e7606e90dc164762bebb0c6bc48dcd46eeb` (one commit, `047a9e7`). Compute the diff yourself and
  confirm `git rev-parse HEAD`.
- The remarks, which bind the correction: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-findings.md`
  (item 1: the human's rule; item 3: five Minor findings in the reviewers' words), and the human's
  later direction in `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-handoff-2.md`
  (what stays in the-way and what leaves it, because the handling of a line is a rule of the task
  place and not of the-way, as the task's own settlement 3 says for the forms). The author's report,
  claims to verify: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-report.md`.
  The rules of the task place lie in the human's private notes, outside the repository; you do not
  review them and quote nothing of them. You review the-way's side: that the correction holds no
  rule of handling a line that is the place's, and that what stays is the-way's own.
- Judge each of the six remarks (item 1 and the five of item 3) as made or not made, and whether the
  correction adds a new Critical or Important defect. In particular:
  - the rewrap: the author rewrapped whole paragraphs of WAY-154, WAY-329, WAY-107, WAY-320 and
    WAY-27, so the diff of `foundations/decisions.md` is large (141 / 142 lines in all). Judge
    whether a changed word or a lost qualification hides in it; check each rewrapped paragraph's
    words against `06144e9` and the entries' meaning, not only the line lengths;
  - WAY-107's added third binding sentence and the "the cycle's" mark, with WAY-114 and WAY-263;
  - the one sentence in `project-level/task_line.md` ("as the rules of the task place give; where
    they do not say how, ask the human once") and its pointers in four files.
- Also judge, as part of this correction, whether the part map or any other entry the correction
  touches is still true; the author states it compared them.
- The findings of the earlier reviews that stand on the request's list are not yours to re-grade:
  the Ready line a task returned to refinement keeps; the four small points of item 3 that this
  correction fixes are yours to judge as fixed.
- Checks: `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`,
  `python -B task-cycle/test_tracked_files_private_paths.py`. Not the `project-level` directory and
  not the full suite; they are the orchestrator's.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-review-report.md`,
  first line `PASS <head sha>` or `FAIL <head sha>`, each remark as made or remains, **Declined to
  judge**, each check with command and exit code, each reach beyond this dispatch, **Unread material**
  and **Searches not found or unclear**. Return the first line, the counts of blocking, Minor and
  out-of-scope findings, a one-line check result and the report path.
