# Handoff — review of the whole change

You review the whole change of one task as an agent that did not make it. You are read-only: change
no file of the worktree, commit nothing.

- Worktree (work from its root): `C:\Storage\repos\the-way\.runs\worktrees\logging-scope-decision-section`,
  branch `task/logging-scope-decision-section`.
- Method: `task-cycle/review/SKILL.md` of this worktree; read it whole and `task-cycle/review/whole_change.md`
  as it directs. Your dispatch: **the whole change**.
- Range to review: base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a` to head `fa445fd10d8ddc3af9126bf2873b61c1029746c2`
  (three commits `d6871fc`, `501a2a1`, `fa445fd`).
- Frozen task, whole: `.runs/task-cycles/logging-scope-decision-section/task.md`. No spec and no plan: the
  route is one author without a plan, no slices. The task did not move any pin (the-way is the top-level
  repository).
- The author's report (which you read after forming your own view of the diff, as your method says):
  `.runs/task-cycles/logging-scope-decision-section/reports/02-author-report.md`. It names departures and choices
  for you to judge: the edit in place of WAY-287 against a new number, the *Rationale* sentence added,
  the *Rejected* filled from the task's *Questions to settle* 1, the BOM stripped by reading with
  `utf-8-sig`, the removed in-memory BOM test.
- Answers of the start: touches a trust boundary — no (part map gives `task-cycle` and `decisions`
  none); holds an irreversible operation — no. Check, as your method gives, only that the change
  prepares nothing of the kind.
- The foundation entries the change writes: WAY-287 (row 1 of the task's *Settlements to record*). The
  foundation step is part of the range. The whole gate (`python -B gate/run_tests.py`) is run by the
  orchestrator, not you; you may run focused checks yourself (`python -B gate/run_tests.py task-cycle`,
  `python -B elements/common/foundation_check.py`), each reported with its command and exit code.
- You select your own foundation and guidelines by the parts of the change (`task-cycle`, `decisions`).
  The-way has no guidelines of its own for code or tests.
- Write the full report to `.runs/task-cycles/logging-scope-decision-section/reports/03-whole-review-report.md`.
  Its first line is `PASS <sha>` or `FAIL <sha>`. Return its first line, a one-line check result and the
  report path. Cover every task item and the settlement row, source fidelity (does each sentence of the
  new template item, the decision and the script's message follow the task and not more), and under
  **Searches not found or unclear** each thing looked for and not found or unclear, or `none`.
