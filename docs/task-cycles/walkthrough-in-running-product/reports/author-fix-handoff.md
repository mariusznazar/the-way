# Handoff to the one author — the fix of a review's findings

You are the one author of this change, resumed. Your variant of `task-cycle/change/SKILL.md`, in the
words of its row: **"the fix of a review's findings"**. Read `task-cycle/change/fix.md` whole as the
method gives, and no other file of it unless its step comes.

- Worktree `the task's worktree`, branch
  `task/walkthrough-in-running-product`. The fix's range runs from the reviewed head `940893de`.
- Findings file (the reviewer's words): `.runs/task-cycles/walkthrough-in-running-product/reports/fix-findings.md`
  — six blocking findings (I1-I6) and six Minor findings within the task (M1-M6); read it whole. The
  frozen task `.runs/task-cycles/walkthrough-in-running-product/task.md` stays the only authority on
  what to make. The review's report is not yours to read.
- The review says that the round holds a contradiction with the settlements of the task or the
  foundation (I1, I3, I4, I5, I6 carry the mark): correct each to the settlement, not to your report's
  rationale. Where you hold a finding wrong, say so in the report with evidence (a passage of the
  task or of the foundation); do not skip it silently.
- Fix every finding of the file: the six blocking ones and the six Minor ones. Where fixing one
  needs to change another entry (WAY-33), do it in the same fix and name it. For I3, the task's
  *To do* 5 and row 5 are the authority: the error outside the scope that the author reports
  reaches the section for the human's decisions as one to make a task of or to let through; name the
  group (WAY-287) and settle the collision with WAY-289 by the decision that prevails, as
  `agent-instructions/README.md` ("Make the change", WAY-25) gives, or word WAY-408 and kind 8 so
  that they agree.
- Run again the affected focused checks (`python -B elements/common/foundation_check.py`, the
  directories whose files you changed with `python -B gate/run_tests.py <directory>`,
  `python -B task-cycle/private_paths_check.py <file>` for each changed file). No full gate.
- Commit by path, in English. Do not commit anything under `.runs/`.
- Your directory for working copies: `.runs/author-fix/`; remove it before you return. The paragraph
  "Working copies" of your first handoff stands.
- Report: `.runs/task-cycles/walkthrough-in-running-product/reports/author-fix-report.md`, as
  `task-cycle/change/SKILL.md` section 6 and `fix.md` give, with, for each finding, what you did
  and its evidence, **Unread material**, **Searches not found or unclear**, and your own-work check.
  Return status, commits, a one-line check result and the report's path.
