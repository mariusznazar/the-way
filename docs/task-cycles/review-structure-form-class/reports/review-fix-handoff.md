# Handoff — the review of the fix, `review-structure-form-class`

## Delegation

You are the reviewer of the whole change (`FAIL 5353268`), resumed to review the fix of your findings once, as an agent that did not make it.
Read-only. The orchestrator is the one you ask; no human answers during the cycle.

## Where

- Worktree (read-only for you): `the worktree's root`; range of the fix `5353268..c6af26a`
  (three commits `a47195b`, `cd54d5a`, `c6af26a`; 8 files). Confirm `git rev-parse HEAD` is `c6af26a`.
- Findings file the fix was given: `docs/task-cycles/review-structure-form-class/reports/fix-findings.md` (I1 and M1–M5, in your words).
- The fix's report: `docs/task-cycles/review-structure-form-class/reports/fix-author-report.md`.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/review-fix-report.md`; its first line is
  `PASS c6af26a`, `FAIL c6af26a` or `questions`.

## Method

Read `task-cycle/review/fix.md` (named by `task-cycle/review/SKILL.md`, variant "the fix of earlier findings") and follow it: each finding of the
findings file as fixed or remains, and what the fix itself broke. Only a new Critical or Important finding in the fix fails this review; a Minor
finding that remains or is new does not block and goes to the request's list. Check in particular that the four places of I1 and WAY-355's
*Verification* now agree, that no sentence of the invariant's other uses was left saying the old thing, and that the three new tests of the script
fail when the behaviour breaks. Run the focused checks `python -B gate/run_tests.py task-cycle`, `python -B elements/common/foundation_check.py`,
each with command and exit code; do not run the whole gate.
Your report holds **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return the first line, the counts
of blocking and Minor findings, a one-line check result and the path of the report.
