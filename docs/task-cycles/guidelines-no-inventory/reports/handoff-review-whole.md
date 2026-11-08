# Handoff — review of the whole change

Delegation: the person who requested this cycle delegated intermediate choices to the orchestrator;
you review as an agent that did not make the change. Read-only: change no tracked file, commit nothing.

Worktree (work from its root): `the root of the worktree`
Branch `task/guidelines-no-inventory`. Range to review: base `deded3fd297a862e0160611827c564f95bb9037a`
to head `6df733c` (two commits: `cd9d5af`, `6df733c`; `git diff deded3f..6df733c`).

Method: read `task-cycle/review/SKILL.md` whole, and `task-cycle/review/whole_change.md` when the
step that names it comes. You select your own foundation entries and guidelines by the parts of the
change (the-way has no `guidelines/` of its own); the parts are `decisions`, `environment-facts`,
`product-guidelines`.

Frozen task (read whole): `.runs/task-cycles/guidelines-no-inventory/task.md`. No spec, no plan: the
route is one author without a plan. Author's report:
`.runs/task-cycles/guidelines-no-inventory/reports/author-report.md` (the first return of the report was
`blocked` for the source of row 3; the orchestrator supplied the source, see the report's "Choices").
Answers of step 4: no trust boundary; no irreversible operation. The pin did not move.

What the change must carry: *To do* 1 and 2, rows 1–3 of *Settlements to record* (each written whole as
an entry of its kind, its meaning the row's, its wording the author's), the WAY-130 / *Decisions in play*
consistency, and a search of the whole foundation. Judge coverage of every task item, settlement row and
source fidelity (the fact's quoted passages against
`git -C the local clone of the game repository show 9c0dfc8faa7b3024dfa1e488b18b955f087b57a0:docs/task-cycles/proba-krotszych-wytycznych/request.md`,
read only), and whether the private repository's name appears anywhere but the fact's *Source* line.
The orchestrator's checks so far: `python -B elements/common/foundation_check.py` exit 0; the base's
gate passed (804 tests). The orchestrator runs the full gate itself later; you need not.

The harness forbids a subagent to write report files: return the whole report as text in your reply, its
first line `PASS 6df733c` or `FAIL 6df733c` (or `questions`), as your method gives the report, with the
checks you ran (command and exit code), and **Searches not found or unclear** (`none` is an answer).
