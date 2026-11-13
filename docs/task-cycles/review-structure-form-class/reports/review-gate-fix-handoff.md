# Handoff — the review of the fix of a failing gate check, `review-structure-form-class`

## Delegation

You review, as an agent that did not make it, one commit of a the-way task cycle: the fix of a test that failed in the orchestrator's run of the whole gate.
The orchestrator is the one you ask; no human answers during the cycle. You change nothing.

## Where

- Worktree (read-only for you): `the worktree's root`; range `3e934b6..0f35395` (one commit, one file,
  `task-cycle/test_change_file_sizes.py`). Confirm `git rev-parse HEAD` is `0f35395`.
- The fix's report: `docs/task-cycles/review-structure-form-class/reports/gate-fix-author-report.md`; the handoff it was given:
  `reports/gate-fix-handoff.md` (it holds the failure: `elements/part-map` test `test_the_way_imports_only_from_allowed_parts` reported
  `task-cycle/test_change_file_sizes.py:248` and `:252` as "runs a file the check cannot work out").
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/review-gate-fix-report.md`; its first line is
  `PASS 0f35395`, `FAIL 0f35395` or `questions`.

## Method

Read `task-cycle/review/SKILL.md` whole and follow it for "the fix of earlier findings" (and `task-cycle/review/fix.md`, which it names). The one finding is the
failing test; judge whether the fix makes it pass for the right reason, keeps what the test checked (an exit code 0 with a UTF-8 table for a name with
non-ASCII letters; exit 2 with an `Error:` line and an empty stdout for an absent commit), and breaks nothing. Run, each with command and exit code,
`python -B gate/run_tests.py elements/part-map`, `python -B gate/run_tests.py task-cycle` and `python -B elements/common/foundation_check.py`; do not run the whole
gate. Only a new Critical or Important finding fails this review; a Minor one goes to the request's list. Your report holds **Unread material** and
**Searches not found or unclear** (each `none` where there is nothing). Return the first line, the counts of blocking, Minor and out-of-scope findings, a
one-line check result and the report path.
