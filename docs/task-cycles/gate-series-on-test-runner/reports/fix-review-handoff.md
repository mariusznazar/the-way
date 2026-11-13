# Handoff — review of the fix

You are the reviewer of the whole change, resumed once to review the fix of your own findings.

- Worktree: `the task's worktree`, branch `task/gate-series-on-test-runner` (read-only for you).
- Method: `task-cycle/review/SKILL.md`, variant the review of a fix; read `task-cycle/review/fix.md` whole as it gives.
- Fix range: `909fcb9` (the reviewed head) to `b8dc239`; compute the diff yourself.
- Findings file the fix was given: `docs/task-cycles/gate-series-on-test-runner/reports/fix-findings.md` (your words: Important finding 1 and Minor findings 2–5, all within the task; finding 5 asked for no change).
- Fix report (claims to verify): `docs/task-cycles/gate-series-on-test-runner/reports/fix-report.md`.
- Frozen task: `docs/task-cycles/gate-series-on-test-runner/task.md`. Trust boundary: yes (`process-audit/audit_count.py`; the fix touches no code, only `foundations/decisions.md`).
- Report path: `docs/task-cycles/gate-series-on-test-runner/reports/fix-review-report.md`; first line `PASS <sha>` or `FAIL <sha>`; it holds **Unread material** and **Searches not found or unclear** (`none` where none). Only a new Critical or Important finding in the fix fails this review; a Minor finding that remains or is new does not block.
