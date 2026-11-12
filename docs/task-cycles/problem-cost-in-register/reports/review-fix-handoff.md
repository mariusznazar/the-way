# Handoff — review of the fix, `review-change`

You are the reviewer of the whole change, resumed to review the fix of your Minor findings once.
Read-only, same worktree `the task's worktree`.

- Range of the fix: `18b4a3f..e6d05e2` (one commit, `e6d05e2`; 3 files: `process-audit/problem_register.md`,
  `process-audit/test_audit_count.py`, `foundations/decisions.md`).
- Findings fixed: `reports/findings-minor.md` (your Minor 1, 2 and 3 of the review of the whole change,
  cut in your words; Minor 4 is outside the task and was left alone, as designed).
- Fix report: `reports/fix-report.md`.
- Task and answers at start as in `reports/review-whole-handoff.md` (trust boundary: yes; no
  irreversible operation).
- Judge: whether each of the three findings is fixed; whether the fix introduced anything new
  (only a new Critical or Important finding in the fix fails this review; a remaining or new Minor
  one does not block and goes to the request's list). Check that the rewrap of WAY-330 changed no
  word, and that the new subtest of the test fails when a reordered header is turned into a missing
  field (a mutation of your own, restored afterwards; the worktree must end clean).
- Run at least `python -B gate/run_tests.py process-audit` and
  `python -B elements/common/foundation_check.py`; not the whole gate.
- Report to `reports/review-fix-report.md` (first line `PASS <sha>` or `FAIL <sha>`, findings with
  grades and scope, checks with command and exit code, **Unread material**, **Searches not found or
  unclear**). Return the first line, a one-line check result and the path.
