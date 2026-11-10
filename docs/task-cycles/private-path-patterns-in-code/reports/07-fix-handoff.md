# Handoff 07 — the fix of a review's findings (the return step's review)

You are the one author of this change, resumed. Delegation, worktree, branch and rules of
`01-author-handoff.md` stand.

## What you make

"The fix of a review's findings": the method is `task-cycle/change/SKILL.md`, and `fix.md` beside it
(you have read it; read it again for what the report of a fix holds).

- Findings file: `.runs/task-cycles/private-path-patterns-in-code/reports/07-fix-findings.md`: the
  two blocking findings (Important, within the task) of the review of the return step, in the
  reviewer's words; the full review is `reports/06-return-step-review-report.md`, for context.
- Base of the fix: `3057f16`. Commit on top of it, by path.
- Finding 1 is in `foundations/part_map.md` (the surface you wrote); finding 2 is in
  `installation/README.md`. Where a finding is wrong, say so with evidence in the report instead of
  changing the text. Where you correct one of the two accounts, make all the accounts of the same
  promise read alike: the surface, the README section, WAY-324's sentences and the invariant's.
  Search for any other place that restates the command's promise (a `git grep` for
  `tracked_private_paths_check` and `tracked-private-paths-command`), and correct a place the same
  way if it differs.
- Focused checks after the edits: `python -B elements/common/foundation_check.py`,
  `python -B gate/run_tests.py installation` and `python -B gate/run_tests.py elements/part-map`.
  Do not run the whole gate.
- Change nothing else; do not touch the Minor finding of the review of the fix (README, UTF-16),
  which goes to the request's list.

## Report

Write `.runs/task-cycles/private-path-patterns-in-code/reports/07-fix-report.md` as `fix.md` gives:
each finding as made and how, each check with command and exit code, your own-work check, the
reaches beyond this handoff and **Searches not found or unclear** (`none` is an answer). Commit
before you return, and return your status, your commits, a one-line check result and the report's
path.
