# Handoff to the reviewer of the fix of correction 1

You reviewed correction 1 (`reports/review-correction-report.md`, `FAIL b3bd8f4`). The one author made one fix for
its blocking finding R-1, cut into `reports/review-correction-findings.md` (in
`.runs/task-cycles/audit-answers-contradiction-after-code/`), in your words. Review the fix range once, with
`review-change`, variant "the review of a fix", reading `task-cycle/review/fix.md` as the method says.

- Worktree (read-only for you): `the root of the task's worktree`.
- Range of the fix: base `b3bd8f4e1b401ab38ccf6e22f2fa96847c508490` to head `47a47fe` (one commit; two files:
  `process-audit/record_items.py`, `process-audit/test_record_items.py`).
- The author's fix report (claims to verify): `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction-fix-report.md`.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-correction-fix-report.md`.
  Your directory for working copies: `.runs/review-correction-fix/`.
- Trust boundary: yes (`process-audit/record_items.py`); check crafted input as before. Irreversible operation: no.

Judge whether R-1 is fixed as you worded it; that the reason the reading now gives for a line that is no entry or
stands at another indent fits both cases; that no answer that was right at `b3bd8f4` is lost (the six records of
`test_audit_count.ProcessVersions.test_the_marker_of_a_discarded_attempt_gives_q1`, the sub-entry case `deeper`,
the details-as-a-list form, the four denials of review #100) and that no new wrong `yes` or `no` appears. A new
Critical or Important finding in the fix counts as one that remains (WAY-162); Minor findings do not block.
Focused checks only (`python -B gate/run_tests.py process-audit`, `... task-cycle`,
`python -B elements/common/foundation_check.py`); **do not run the full gate**. Report each check with command
and exit code, **Unread material**, **Searches not found or unclear** and the line on your working copies
(made in `.runs/review-correction-fix/`, removed with `git worktree remove --force` then `git worktree prune`,
remainders named with full path and reason). Return the first line (`PASS <sha>` or `FAIL <sha>`), a one-line
check result and the report's path.
