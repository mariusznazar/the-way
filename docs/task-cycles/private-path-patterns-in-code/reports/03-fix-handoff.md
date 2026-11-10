# Handoff 03 — the fix of a review's findings (Minor findings of the review of the whole change)

You are the one author of this change, resumed. Delegation, worktree, branch and rules of
`01-author-handoff.md` stand.

## What you make

"The fix of a review's findings": the method is `task-cycle/change/SKILL.md`, and `fix.md` beside it
for the findings file, what is not yours to fix and what the report of a fix holds (read it whole
now).

- Findings file: `.runs/task-cycles/private-path-patterns-in-code/reports/03-fix-findings.md`: three
  Minor findings of the review `PASS 287a02712e683f4a3694d5ef46b795b253a1b1fc` (full review in
  `reports/02-whole-change-review-report.md`, for context only). Each is within the task and is yours
  to fix; there is no blocking finding.
- Base of the fix: `287a027`. Commit the fix on top of it, by path, as one or more commits.
- Finding 1 is the number in WAY-320's rationale; edit the decision in place (WAY-07), keeping every
  other word. Findings 2 and 3 are the README section in `installation/README.md`: say all the exit
  codes the command gives and that every backticked text of the sentence is read as a file name, and
  say what *Derives from* a product's invariant names (a decision of the product's own, since a
  decision of the-way at the pinned commit is no decision entry of the product; check the invariant
  template and the foundation skills for what a product can write there, and write only what they
  allow). Where a finding is wrong, say so with evidence in the report instead of changing the code.
- After the README edit, run `python -B gate/run_tests.py installation`, and after the decision edit
  `python -B elements/common/foundation_check.py`; re-run the focused checks of any file you change
  (the command's exit codes in the README are checked against `task-cycle/tracked_private_paths_check.py`).
  Do not run the whole gate.
- Do not change anything else: the part-map surface for the new command is the return step's, which
  comes after this fix. A Minor finding names no slice and changes nothing in the class.

## Report

Write `.runs/task-cycles/private-path-patterns-in-code/reports/03-fix-report.md` as `fix.md` gives,
with each finding as made and how, each check with its command and exit code, your own-work check,
the reaches beyond this handoff and **Searches not found or unclear** (`none` is an answer).
Commit before you return, and return your status, your commits, a one-line check result and the
report's path.
