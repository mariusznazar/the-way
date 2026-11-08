# Handoff — review of the whole change (task cycle `test-artifacts`)

You are a fresh reviewer; you did not make this change. Method: read `task-cycle/review/SKILL.md` whole in the worktree, and `whole_change.md` beside it as it directs. Read-only: change no tracked file.

- Worktree: `the worktree's root`, branch `task/test-artifacts`
- Range: base `f218b5542ae55b72a95832adde67591365abb72a` .. head `d0d3ce6` (two commits: `dd84fba`, `d0d3ce6`). The change is the whole change of the task; there was no plan and no spec; there were no slice reviews (one author without a plan).
- Frozen task (read whole; in Polish): `docs/task-cycles/test-artifacts/task.md` — a task of `Project relation: independent`.
- Author's report (claims to verify, not evidence): `docs/task-cycles/test-artifacts/reports/author_report.md`.
- Answers of the start: trust boundary: no; irreversible operation: no; open design choice: none; reserved choice: none. Route: one author, class `same`.
- The task moved no pin (the-way itself). Base checks: the full gate on the base passed (804 tests, exit 0).
- Report path (write your full report here): `docs/task-cycles/test-artifacts/reports/review1_report.md`. First line of the report: `PASS <sha>` or `FAIL <sha>`.

Select your own foundation and guidelines as `whole_change.md` / "Reading the foundation" give (the-way has no `guidelines/`). Check every item of *To do* 1–8 and every row 1–7 of *Settlements to record*, source fidelity against the task (the entries must not widen the task: the author reports two additions beyond literal row 6 and a change to WAY-165 and WAY-267/270 wording — judge each), and the places the author names in "Reaches" and "Concerns". Do not run the full gate (the orchestrator does); you may run focused tests of the directories the change touches. Return: status line, a one-line check result, the report path; Minor findings listed separately and any finding outside the task's scope marked as such.
