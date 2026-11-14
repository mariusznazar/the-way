# Handoff: the fix of the Minor findings of the review of the whole change

You are the one author, resumed. The review of the whole change returned `PASS 44c1d99` with three
Minor findings within the task, which the cycle fixes before the request opens. The findings file is
`reports/whole-review-findings.md` (in `.runs/task-cycles/oversized-plan-tasks/`); read it whole.

- Worktree and branch as before; method `task-cycle/change/SKILL.md`, variant "the fix of a review's findings"; read `task-cycle/change/fix.md` when that variant names it.
- Fix all three findings, each with the smallest change that removes the cause, and no more:
  1. Finding 1 (decisions.md, *Rejected*): state the threshold item without the case figure, or add the clause the reviewer suggests; prefer the shorter way that keeps the reason (a threshold fitted to one case would stop a task that is right to stand).
  2. Finding 2 (cut_tasks.md): use the reviewer's wording, "A task too large is put to the human to split", keeping WAY-13's "its size chooses nothing else" and the later sentences consistent with it.
  3. Finding 3 (critique_plan.md): say that the author hands the critic the size test, its text, with the request.
- Keep the WAY-146 binding sentence, `cut_tasks.md`, `critique_plan.md` and `plan/template.md` saying the same test and the same routing; if you change a sentence of the decision, check the other three still agree (WAY-263).
- Run `python -B elements/common/foundation_check.py` and `python -B -m unittest discover -s project-level -p "test_*.py"` again (command and exit code). Do not run the gate.
- Commit on the branch (git add by path). Write `reports/author-fix-report.md` as the method gives (checks with command and exit code, Unread material, Searches not found or unclear, own-work check, an answer for each finding), and return status, commit, one-line check result and the report path.
