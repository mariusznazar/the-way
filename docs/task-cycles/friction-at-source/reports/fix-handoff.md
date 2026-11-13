# Handoff — the fix of the Minor findings of the review of the whole change

## What

You, the one author of the change `friction-at-source`, now make "the fix of a review's findings" (variant of `task-cycle/change/SKILL.md`; read
`task-cycle/change/fix.md` whole, as the skill gives for this variant). The review of the whole change returned `PASS e51d835` with no blocking finding and
seven Minor findings within the task; the cycle fixes each before the request opens (WAY-161). The findings file is
`reports/fix-findings.md`:
`docs/task-cycles/friction-at-source/reports/fix-findings.md`.
The reviewer's full report is `reports\review-whole-change-report.md` beside it; read it only where a finding needs its context.

## Where

- Worktree `the worktree's root`, branch `task/friction-at-source`, head `e51d835`. The fix's range starts from `e51d835`.
- Your report: `docs/task-cycles/friction-at-source/reports/fix-author-report.md`.

## Boundaries

- Each finding gets a fix by the wording its text gives, or an answer with evidence where you hold it wrong; a finding you hold wrong is answered in the report, never skipped silently.
  Where two fixes pull against each other, say which you took and why.
- Finding 5 asks for three wording changes (the pointer after the steps in the example, one sentence on a command in a step, the invitation rephrased). Settle the command question
  by the smallest reading that fits WAY-286 and WAY-327 and name it in the report; do not add a way to answer and do not touch the skeleton or the form-check script.
- A fix that changes a decision's entry changes it in place, in the same commit as the files that restate it (WAY-33, WAY-37), and the foundation check must pass on every commit you make.
- Run again the affected checks: `python -B elements/common/foundation_check.py`, `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py project-level`, and the private-paths check
  on each changed file (`python -B task-cycle/private_paths_check.py <file>`), each with its command and its true exit code (no pipe that hides the code), and the own-work check
  of the form check on the request template's example item again, as in your first report. Do not run the whole gate.
- Commit by path, in English, one commit or a few; do not push; do not touch other worktrees or the checkout of the repository.
- Do not take the return step: it comes after, as a separate resumption.
- Report as `make-change` gives for a fix, with **Unread material** and **Searches not found or unclear** (each `none` where there is nothing).
  Name the report file as above (it must not begin with `report`, `summary`, `findings` or `analysis`).
