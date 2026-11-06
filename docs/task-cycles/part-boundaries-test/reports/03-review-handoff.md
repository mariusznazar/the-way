# Handoff 03 — review of the whole change

## Delegation

You review, as an agent that did not make it, the whole change of a the-way task cycle, dispatched
by the orchestrator of `implement-task`. The person who requested the cycle delegated every
intermediate choice to the orchestrator; ask no human. Send questions to the orchestrator in your
report (first line `questions`). Read-only: change no file of the repository, commit nothing.

## Where you work

- Worktree (read from its root): `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test`
- Branch `task/part-boundaries-test`. Range: base `dfd50e513c09bebe9d09d74209cd28612565da83` (`foundations`) .. head `b4a5509` (confirm with `git rev-parse HEAD`).
- Do not read `.runs/task-cycles/part-boundaries-test/cycle.md`. Read only the frozen task, the author's report and this handoff under `.runs/`.

## Your method

- Method: `task-cycle/review/SKILL.md` in the worktree — read it whole; you review **the whole change**, so read `task-cycle/review/whole_change.md` when its step comes. Read a file the method names only when the step that names it comes.
- You select your own foundation and guidelines (WAY-150, WAY-213), by "Reading the foundation" in `elements/common/way_of_working.md` and `product-guidelines/reading.md`. The-way has no `guidelines/` directory; the task's last question under *Questions to settle* records that it does not wait for them (a WAY-215 departure Mariusz decided).

## Inputs

- Frozen task, read whole: `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test\.runs\task-cycles\part-boundaries-test\task.md` (in Polish; the repository is written in English). No spec, no plan: one-author route.
- Author's report: `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test\.runs\task-cycles\part-boundaries-test\reports\02-author-report.md` — claims to verify, not evidence.
- Answers of the cycle's start: trust boundary — no (the test reads only the repository's own files); irreversible operation — no; open design choice — none.
- The orchestrator's answer to the task's *Questions carried to cycle*, given to the author as binding: running another part's script (`runpy.run_path`, a new process) is **not** an import under the invariant of row 3; the invariant and its test cover `import` and `from … import` statements, resolved against the importing file's own directory, the repository root and the directories a file adds to `sys.path`. Source: row 3 and *To do* 3. The request puts it before Mariusz.
- Out of scope (task): the invariant and test in loop2.

## Checks

Run what your method gives, focused: e.g. `python -B gate/run_tests.py elements/part-map`, `python -B elements/common/foundation_check.py`. Do not run the whole gate (`python -B gate/run_tests.py` with no argument): the orchestrator runs it in this worktree while you review, so do not create, change or delete files in the worktree (a mutation you want to try goes into a copy outside the worktree, e.g. your own scratch directory, never into the tracked tree).

## Report

Write your full report to `C:\Storage\repos\the-way\.runs\worktrees\part-boundaries-test\.runs\task-cycles\part-boundaries-test\reports\04-review-report.md` as the method gives it — first line `PASS <sha>`, `FAIL <sha>` or `questions`, graded findings with their places, the checks with command and exit code, and **Searches not found or unclear**. Return the report's first line, a one-line check result and the report's path.
