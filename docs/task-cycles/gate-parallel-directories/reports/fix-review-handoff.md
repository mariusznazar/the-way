# Handoff — review of the fix, and the gaps of your first report

You are the reviewer of the whole change, resumed. Two tasks, in this order, one report:
`docs/task-cycles/gate-parallel-directories/reports/fix-review-report.md` (first line `PASS <sha>` or `FAIL <sha>`).

1. Review the fix once, as `task-cycle/review/fix.md` gives: range `264703f`..`9282e6f` (one commit),
   findings file `reports/whole-review-findings.md` (the five Minor findings within the task of your report),
   fix report `reports/fix-report.md`. Only a new Critical or Important finding in the fix fails this review;
   a Minor finding that remains or a new Minor one goes to the request's list.
2. Close the gaps of your first report on the final head `9282e6f`: read whole the decisions you named as
   bearing on the change and did not open (WAY-33, WAY-34, WAY-89, WAY-298, WAY-337, WAY-339, WAY-348,
   WAY-325, WAY-326), read `task-cycle/skill/SKILL.md` and `task-cycle/skill/request_template.md` whole,
   and the invariants of the parts `gate`, `task-cycle` and `agent-instructions` and the glossary entries of
   the terms the change's sentences use, whole; say in the report whether anything you read changes a
   grade or the PASS.

Worktree: `the root of the task's worktree`; read-only except the report.
Report as the method gives, with your checks (command and exit code), **Unread material** and
**Searches not found or unclear**.
