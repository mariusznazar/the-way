# Handoff — the fix of the review's findings, `review-structure-form-class`

## Delegation

You are the one author of this change, resumed to fix the findings of the review of the whole change (`FAIL 5353268`). The orchestrator is the
one you ask; there is no human to ask. An agent that did not make the change reviews your fix once afterwards.

## Where

- Worktree (work from its root, and nowhere else): `the worktree's root`; branch
  `task/review-structure-form-class`; the fix's range starts at the reviewed head `5353268`.
- Findings file: `docs/task-cycles/review-structure-form-class/reports/fix-findings.md` (the blocking finding I1 and the Minor findings M1–M5 within the
  task, in the reviewer's words). The reviewer's full report is `reports/review-whole-change-report.md`; read it only where a finding needs it. M6 of that
  report lies outside the task's scope and is not to be fixed.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/fix-author-report.md`

## Method

Read `task-cycle/change/SKILL.md` again in its variant "the fix of a review's findings" (it names `task-cycle/change/fix.md`; read that file when the
variant comes). Fix every finding of the file: the blocking one (I1) and the Minor ones (M1–M5, WAY-161), each by the reviewer's "fix in kind" or by a
better one you name. Where you hold a finding wrong, answer it in the report with evidence; do not drop it silently. Run the affected checks again.
Edit WAY-355 in place for I1 (WAY-07); its binding sentence changes, so say in the report what each of the four places now says and that they agree
with its *Verification*. For M1, point to WAY-229 for the conditions of the experiment, as WAY-164 does. For M3 name both checks, as
`product-guidelines/coding/SKILL.md` does. For M4 let the first run (the script, which writes nothing) stay in the reviewed worktree.
For M5 add the tests for the status `T` and the escape of `|`, and make the backtick in a name not break the row if that can be done simply, else say so.

## Boundaries

- Commit on the branch, naming files by path, never `git add -A`; messages in English in the form of the existing log; do not push. Several commits are
  fine. Do not run the whole gate. Run the affected focused checks: `python -B gate/run_tests.py task-cycle`, `python -B elements/common/foundation_check.py`,
  `python -B task-cycle/private_paths_check.py <file>` on each file you change, and `python -B gate/run_tests.py instruction-files` and
  `python -B gate/run_tests.py agent-instructions` if a skill file changes. Give each check with its command and exit code.
- Report as `make-change` gives for a fix: status, commits, each finding as fixed or contested with evidence, checks, the own-work check, **Unread
  material** and **Searches not found or unclear** (each `none` where there is nothing). Write the report to the path above only (`fix-author-report.md`).
- Do not start the return step or any next stage.
