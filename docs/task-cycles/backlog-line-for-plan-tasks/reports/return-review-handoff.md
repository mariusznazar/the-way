# Handoff — review of the return step's commits

You are a reviewer of a the-way task cycle and made none of this change. The orchestrator's
delegation stands; nothing here is a human's approval.

- Method: `task-cycle/review/SKILL.md`, read whole. This is a review of the return step's commits:
  section 2 judges them against the task and the foundation entries the return step writes or
  corrects (no `whole_change.md`, no `fix.md`).
- Worktree (read-only): `the task's worktree root`,
  branch `task/backlog-line-for-plan-tasks`.
- Range: base `9d5743d7648b4a5095fba28a7d6ab100cd078c3b` to head
  `06144e9713221bbcc680752ed0ba400e75813a34` (one commit, `06144e9`). Compute the diff yourself and
  confirm `git rev-parse HEAD`. The code the commit sits on has had its whole-change review
  (`PASS` after one fix); do not review it again.
- The return step's rules: `task-cycle/skill/return_step.md` (read whole). The step compares with the
  files the entries the change writes or changes, those the task names, those the search of the
  foundation found and the part map of the touched parts; it writes entries as the foundation step
  does (`task-cycle/skill/foundation_step.md`) and for a choice that binds after the merge (WAY-36).
- Frozen task, passages to judge against, by their file (the whole file is yours to read):
  `docs/task-cycles/backlog-line-for-plan-tasks/task.md` — *Settlements to record* rows 1-5,
  *Decisions in play*, *Questions carried to cycle*.
- Entries by identifier, each whole: WAY-329 (new in this commit), WAY-154, WAY-107, WAY-320
  (changed here only in *Verification* of WAY-154 and by rewrapping), WAY-27 (unchanged), WAY-36,
  WAY-11, WAY-33, WAY-71, WAY-95 and the glossary; the `project-level`, `decisions` entries of
  `foundations/part_map.md` and the element's rules for a decision entry
  (`elements/decisions/template.md` and its skill).
- The return step's report, claims to verify:
  `docs/task-cycles/backlog-line-for-plan-tasks/reports/return-report.md`. In particular judge:
  WAY-329's `Based on: none` and its `the cycle's` mark; its *Rejected* and *Verification* against the
  form WAY-134 and the element's template give; the choice to write no entry for choices 2-5 of the
  author's report (they stay rows of the cycle record's questions table); and whether the part-map
  clause is a fair statement of the part's responsibility.
- The findings of the earlier reviews that stand on the request's list for the human (not for you to
  re-grade): the older word "entry" in `read_sources.md`; the out-of-scope item that a task
  returned to refinement keeps a Ready line.
- Checks: `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`,
  `python -B task-cycle/test_tracked_files_private_paths.py`. Not the `project-level` directory and
  not the full suite; they are the orchestrator's.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/return-review-report.md`,
  first line `PASS <head sha>` or `FAIL <head sha>`, findings by grade, **Declined to judge**, each
  check with command and exit code, each reach beyond this dispatch, **Unread material** and
  **Searches not found or unclear**. Return the first line, the counts of blocking, Minor and
  out-of-scope findings, a one-line check result and the report path.
