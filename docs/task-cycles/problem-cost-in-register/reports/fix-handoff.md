# Handoff — the fix of the Minor findings, `make-change`

Variant: "the fix of a review's findings". You are the one author, resumed for the fix. Same
delegation, worktree and rules as `reports/author-handoff.md`.

- Worktree `the task's worktree`, branch
  `task/problem-cost-in-register`, head `18b4a3f`. The fix's range runs from `18b4a3f`.
- Findings file: `reports/findings-minor.md` (three Minor findings of the review of the whole change,
  which passed). Fix exactly these three, in the reviewer's words; do not reopen the reviewer's
  Minor 4 (outside the task) and change nothing else.
- Run the affected checks again: `python -B gate/run_tests.py process-audit` (it takes about 4
  minutes; run it in the background), `python -B elements/common/foundation_check.py`, and the
  private-paths checks on the files you edit in prose. Do not run the whole gate.
- Commit by path; one commit.
- Report: `reports/fix-report.md`, as `make-change` gives for a fix, with **Unread material**,
  **Searches not found or unclear**, every check with its command and exit code, and the head you
  reach. Return status, commit, a one-line check result and the report's path.
