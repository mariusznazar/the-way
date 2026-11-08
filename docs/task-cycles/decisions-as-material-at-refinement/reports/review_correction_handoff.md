# Handoff — review of a correction for the human's remarks

Stage: review of the correction, by `review-change`; read `task-cycle/review/fix.md` (it covers a
correction too). You are the reviewer of the whole change, resumed. Review-only: change no file.

- Worktree: the one you worked in before. Range: base `ff395cf82bce445339f47c495a917a01f70e8fc4`
  (the head of the request before the correction) to the head `git rev-parse HEAD` gives (commit
  `c8bf864`, one file, `foundations/decisions.md`, +13/-9); confirm it.
- The remarks, which bind, in place of a findings file:
  `docs/task-cycles/decisions-as-material-at-refinement/reports/correction_remarks.md`. They answer
  your own new Minor finding of the review of the fix; items 1–3 of the request are accepted and
  must not change.
- The correction report (claims to verify):
  `docs/task-cycles/decisions-as-material-at-refinement/reports/correction_report.md`.
- Judge whether the remarks are carried out and whether the correction broke anything: the binding
  sentence of WAY-113 (accepted) must be untouched; the *Rationale* and *Verification* must agree
  with it and with `elements/common/way_of_working.md` "How a skill asks"; no other file should
  still carry the stale reading. Only a new Critical or Important finding fails this review.
- No trust boundary, no irreversible operation. Do not run the full gate.

Write the report to
`docs/task-cycles/decisions-as-material-at-refinement/reports/review_correction_report.md` in the
worktree (first line `PASS <sha>`, `FAIL <sha>` or `questions`; checks with command and exit code;
reaches; **Searches not found or unclear**). Return the first line, the path and a one-line check result.
