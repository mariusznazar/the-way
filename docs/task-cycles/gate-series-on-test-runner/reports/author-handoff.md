# Handoff — the one author of the change

You are the one author of a change without a plan, in a task cycle of the-way. The person who
requested the cycle has delegated intermediate choices to the orchestrator; any answer the
orchestrator gives you is not that person's approval.

- Worktree (work only here, from its root): `the task's worktree`
  on branch `task/gate-series-on-test-runner`, base `715ae20d9e817299bd81554e5fdcb6baaf465099` (the-way itself, no pin to move).
- Method: read `task-cycle/change/SKILL.md` of this worktree whole. Your variant, in the words of its
  row: **"the whole change as the one author"**. Read a file that skill names only when the step or
  variant that names it comes.
- Frozen task, read whole: `docs/task-cycles/gate-series-on-test-runner/task.md` (a copy of the
  accepted task document; its *To do*, *Questions to settle* answer, *Context*, *Decisions in play*,
  *Settlements to record* and *Out of scope* bind you).
- Spec: none (no open design choice). Plan: none.
- Report path: `docs/task-cycles/gate-series-on-test-runner/reports/author-report.md`.
- Answers of the cycle's start: trust boundary **yes** — `process-audit/audit_count.py` is the
  trust boundary of the part `process-audit`; every review will check crafted input there. No
  operation that cannot be undone.

## What the change is

Every change of `gate/run_tests.py` between two versions of the process starts a new series of the
gate times, as a change of `task-cycle/gate_times.py` does today; other series (cost, mechanism
measures) are not split by it. The audit names this as the reason of the split. Today
`instrument_series` in `process-audit/audit_count.py` splits a series of an instrument by one script
(constants `MEASURES_SCRIPT`, `GATE_SCRIPT`; `ancestry.differs(..., (script,))` already takes a tuple
of paths). `process-audit/SKILL.md` (paragraph *Measures are compared inside a series only*) and the
decision WAY-339 in `foundations/decisions.md` must say the same, WAY-339 changed as the settlement
row below gives. The settlement row, word for word:

> 1 | Każda zmiana `gate/run_tests.py` zaczyna nową serię czasów bramki, tak jak zmiana `task-cycle/gate_times.py`; zmienia to WAY-339. | decision

Task *To do* items, word for word:

> 1. Audyt zaczyna nową serię czasów bramki także przy wersji procesu, w której `gate/run_tests.py` różni się od poprzedniej wersji, i podaje to jako powód podziału; pozostałych serii ta zmiana nie dzieli.
> 2. Reguła audytu (`process-audit/SKILL.md`, akapit „Measures are compared inside a series only”) i decyzja WAY-339 mówią to samo, z WAY-339 zmienioną tak, jak niesie to wybrana odpowiedź.

Look for every place that says what splits the series of the gate times — the code, the text the
count prints (`measure_versions_lines`, the reason of `instrument_series`), the skill, the decision's
*Verification* and *Rationale*, `process-audit/test_audit_count.py` — and make them say the same.
The reason of a split must say which of the two scripts changed (the reason is shown to the human).
The reason line at the first version of the series stays as it is. Mind that `gate/run_tests.py` is
an instrument of the gate times only, never of the mechanism measures. Do not change
`task-cycle/gate_times.py`, `gate/run_tests.py`, the gate's tables (WAY-349, WAY-350) or the
product's gate command (out of scope).

## What you read (selected by the orchestrator, WAY-150)

Foundation entries, each whole (from its heading to the next heading), in
`foundations/decisions.md`: WAY-339 (the decision you change), WAY-349, WAY-350, WAY-328 (the-way
holds its own code and tests to no product guidelines: there are no guideline files to read).
Invariants, in `foundations/invariants.md`: `script-language`, `script-imports`,
`script-subprocesses`, `cross-part-imports`, `test-method-citation`, `tracked-file-private-paths`,
`foundation-file-kinds`. Part map: the entries `process-audit`, `task-cycle` and `gate` of
`foundations/part_map.md`.

Files you change, each whole before you change it: `process-audit/SKILL.md`; of
`process-audit/audit_count.py` and `process-audit/test_audit_count.py` read whole the passages you
touch and the functions around them (the files are very large); `foundations/decisions.md` — only
WAY-339's entry and what the foundation step names.

## Foundation step

Read `task-cycle/skill/foundation_step.md` whole and follow it for the entries the change writes:
WAY-339 changes in place, through the skill of its element (`record-decision`, the-way's own, found
as `.claude/skills/the-way-record-decision/SKILL.md`), whose steps for reading and searching the
foundation you take as it gives. The task's settlement row is accepted, so the entry is written on
it; the search of the foundation for entries WAY-339 touches runs once and its findings go in this
change or into your report. Run `python -B elements/common/foundation_check.py --skip-test-citations`
after writing the entry.

## Checks

Run the tests of the directory you change with `python -B gate/run_tests.py process-audit` (write the
new tests first and see them fail on the old code), and `python -B elements/common/foundation_check.py`.
Do not run the product's whole gate: its run is the orchestrator's. Commit explicitly by path
(`git add <paths>`), never `git add -A`; commit messages in English, as the history's are; the record
under `.runs/` is ignored and stays out of commits.

Return as `task-cycle/change/SKILL.md` gives: status, commits, a one-line check result, the report
path; the report holds your own-work check, **Unread material** and **Searches not found or
unclear** (`none` where none).
