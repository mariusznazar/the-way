# Handoff — the fix of a review's findings (resumed one author)

You are resumed as the one author of this cycle, for the fix. The orchestrator's delegation and
answers in `reports/author-handoff.md` stand. Nothing here is a human's approval.

- Variant of `make-change`: **the fix of a review's findings**. Read that part of
  `task-cycle/change/SKILL.md` again.
- Worktree: `the task's worktree root`, branch
  `task/backlog-line-for-plan-tasks`, reviewed head `9eb2bd637697fd5f3cccdb891091110054f9d292`.
  Your fix commits go on top; the fix's range runs from that head.
- Findings file, the reviewer's words, copied without change from its report:
  `docs/task-cycles/backlog-line-for-plan-tasks/reports/fix-findings.md` — one blocking finding (B1)
  and six Minor findings within the task. Fix all seven. The reviewer's full report, for the
  evidence behind them: `docs/task-cycles/backlog-line-for-plan-tasks/reports/whole-review-report.md`.
  You may answer, with evidence, a finding you hold wrong; the reviewer then judges it. You do not
  grade or rescope a finding.
- Bounds: touch only what a finding needs. The out-of-scope item of the review (a task returned to
  refinement keeps a Ready line) is not yours. No test is expected; if you add a rule to a skill
  file, keep it in one place and point to it (finding 4 asks exactly that).
- Do not take the return step; the orchestrator resumes you for it after the review of this fix.
- Run the checks of the files you change again, each with command and exit code:
  `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`,
  `python -B task-cycle/test_tracked_files_private_paths.py`, and re-run the one-off check of the
  identifier derivation on the inputs of Minor 2 plus the two you used. Do not run the
  `project-level` directory (12 minutes) and not the full gate; the orchestrator runs it.
- Commits: explicit paths, English messages, no `git add -A`.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/fix-report.md`
  — for each finding, fixed (with the commit and place) or contested (with evidence), plus
  **Unread material**, **Searches not found or unclear**, your own-work check, the checks with
  commands and exit codes, and any reach beyond this handoff. Return status, commits, a one-line
  check result and the report path.
