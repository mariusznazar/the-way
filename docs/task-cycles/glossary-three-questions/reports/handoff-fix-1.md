# Handoff — the fix of a review's findings (make-change), task `glossary-three-questions`

You are the one author, resumed. Your variant now, in the words of the method's table row:
**"the fix of a review's findings"**. Method: `task-cycle/change/SKILL.md` in the worktree; read the
file the method names for a fix (`task-cycle/change/fix.md`) when the step that names it comes.

- Worktree: `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions`, branch `task/glossary-three-questions`.
  Reviewed head: `24e092ca8dd8ae2e7b6165133552e7590f73dc8c`; the fix's range runs from it. Commit by explicit
  paths, English message, nothing under `.runs/`.
- Findings file (the review's blocking findings F1 and F2, in the reviewer's words):
  `docs/task-cycles/glossary-three-questions/reports/findings-1.md`
  Source report, for context only: `...\reports\review-1.md`. Minor and out-of-scope findings of that
  report are not fixed (they go to the request's lists); fix F1 and F2 only, and keep every meaning
  the task settled: the rewording must not move what WAY-104 and WAY-293 say.
- The template the findings rest on: `elements/decisions/template.md` (binding paragraph: one to
  three sentences; no *should* / *will*). Read the lines the findings cite.
- Run the affected checks again (`python -B elements/common/foundation_check.py .`, and
  `python -B gate/run_tests.py <directory>` for the directories you reach); not the full gate. Report
  each with its command and exit code. If you hold a finding wrong, answer with the evidence instead of
  changing the text.
- Report to: `docs/task-cycles/glossary-three-questions/reports/fix-1.md`
  with **Searches not found or unclear**. Return only: status, commits, a one-line check result, report path.
