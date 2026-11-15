# Handoff — the fix of the Minor findings of the whole-change review

You are the one author, resumed, for the fix of a review's findings (`task-cycle/change/SKILL.md`,
variant "the fix of a review's findings", `task-cycle/change/fix.md` when the method names it).
Worktree `the root of the worktree`, branch
`task/weak-point-in-every-decision-question`, reviewed head `a3c97df`; your fix range starts there.

- Findings file: `reports/fix-minor-findings.md` (the five Minor findings of the review of the whole
  change, in the reviewer's words; its full report is `reports/review-whole-report.md`). Fix each
  within the task; where you hold one wrong, answer with the evidence instead of changing it.
- Run the affected checks again: `python -B elements/common/foundation_check.py` and the focused
  `python -B gate/run_tests.py <directory>` of each directory you change; never the full gate with no
  directory (the orchestrator's).
- Commit by path, English message. Write your report to
  `.runs/task-cycles/weak-point-in-every-decision-question/reports/author-fix-report.md` with the
  sections the method gives (**Unread material**, **Searches not found or unclear**, checks with
  command and exit code, own-work check).
- Directory for working copies: `.runs/author/` (as before); remove what you make there and say so.
