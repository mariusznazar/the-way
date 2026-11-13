# Handoff — planner

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the
orchestrator; your questions go to the orchestrator, never to the human, and no answer is the
human's approval.

Worktree (work from its root): `the task's worktree`
Branch: `task/audit-numbers-mechanism-measures`; base commit `2292f334d5499f45b68b00c477cd76a2effd7537`.
This is the-way itself, the top-level repository, no product and no `.the-way` submodule.

Stage and method: the plan of the change, with `plan-task`. Read whole, from the worktree:
`task-cycle/plan/SKILL.md`; read a file it names only when the step or variant that names it comes.
Boundary: the finished plan; write no code, no test and no foundation entry; return before any slice
is made.

Paths:
- frozen task (read whole): `.runs/task-cycles/audit-numbers-mechanism-measures/task.md`
- spec: none (no open design choice at the start)
- plan to write: `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md`
- size report: `.runs/task-cycles/audit-numbers-mechanism-measures/plan-size.md`
- your full report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/planner-report.md`

Answers of the start of the cycle:
- Trust boundary: yes. The change adds a script in `task-cycle/` that reads session records
  (untrusted per the part map's external context) and changes `process-audit/audit_count.py`, the
  trust boundary of `process-audit`. Mark the slices that touch these `trust boundary` in *Risk*.
  `task-cycle/cycle_stages.py` (the named trust boundary of `task-cycle`) must NOT be changed.
- Irreversible operation: no.
- Open design choice at start: none. Names and layout of the two new record files, the form of the
  audit's new section and of the missing-field checks are choices of how to make what the task
  settles: make them in the plan and list them in *Choices*.
- Moved pin: none. Checks failing on the base: pending (full gate on the base is running; do not run
  the gate yourself).

Part map and foundation selection (read each entry whole, by identifier; paths are in
`foundations/`):
- Parts touched: `task-cycle` (new scripts, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`),
  `process-audit` (`process-audit/audit_count.py`, its tests, `process-audit/SKILL.md`),
  `decisions` and `part-map` (foundation entries). `gate` is run by the new script but not changed.
  Part map entries: `task-cycle`, `process-audit`, `gate`, `decisions`, `part-map` and the External
  context table in `foundations/part_map.md`.
- Decisions in play of the task: WAY-337, WAY-339, WAY-344, WAY-160, WAY-331, WAY-341, WAY-38, WAY-328.
- Decisions whose *Scope* names `process-audit`: WAY-09 WAY-38 WAY-89 WAY-320 WAY-328 WAY-330
  WAY-331 WAY-332 WAY-333 WAY-334 WAY-335 WAY-336 WAY-337 WAY-338 WAY-339 WAY-340 WAY-341 WAY-342
  WAY-343 WAY-344 WAY-345 WAY-346.
- Decisions whose *Scope* names `gate`: WAY-09 WAY-16 WAY-38 WAY-51 WAY-53 WAY-55 WAY-60 WAY-61
  WAY-62 WAY-63 WAY-65 WAY-68 WAY-69 WAY-82 WAY-89 WAY-100 WAY-102 WAY-321 WAY-328 WAY-344.
- Decisions whose *Scope* names `task-cycle` (117): read those bearing on the cycle record, the
  stage report, the orchestrator's gate run and the scripts of the part, by identifier as the plan's
  *Read* needs them: WAY-147 WAY-148 WAY-158 WAY-159 WAY-160 WAY-229 WAY-260 WAY-294 WAY-296 WAY-308
  WAY-309 WAY-316 WAY-325 WAY-326 WAY-328 WAY-331 WAY-337 WAY-338 WAY-343 WAY-344; search the rest by
  topic as the method allows and name each reach.
- Invariants whose *Part* is `every`, `task-cycle` or `process-audit` (e.g. `script-language`,
  `script-imports`, `script-subprocesses`, `cross-part-imports`, `skill-entry-points`,
  `record-copy-image-check`, `record-copy-image-files`, `tracked-file-private-paths`), and any a test
  you plan to alter cites by `invariant: <identifier>`.
- Glossary entries of the terms used: gate, slice, part, cost of an occurrence, standing check.
- Guidelines: none. By WAY-328 the-way departs from the general coding and testing guidelines for
  its own code and tests in these parts; none is missing.

Task rows the plan must cover: every item 1–6 of *To do*, both acceptance criteria (no change to
`task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`,
`task-cycle/spec`; the series of cost unchanged — `TREE_PATHS` in `process-audit/audit_count.py` is
not edited), and each of the 8 rows of *Settlements to record* (rows 1–8, as *Foundation entries*:
which are new decisions, which change WAY-339 and WAY-344 in place, and part-map changes for the new
scripts, the trust boundary included).

Notes the orchestrator holds for the plan:
- The task's *Context* names `weryfikacja_usprawnienia_the_way_dane/s05_metrics.py` (lines 76–83)
  and `.../miary_kontekstu.md` as the source of the rewrite definition; they lie outside the
  repository in the author's notes. The task document spells the definition out in *Questions to
  settle*; use that text. A slice's executor cannot read outside the repository.
- WAY-344: every reading of a file by a script the change adds, or by a script whose reading the
  change reworks, has a test that gives the file without one of its needed fields and asserts the
  failure naming it (for the audit's reading of git history, exit 1 with `Error:` and the result
  written, per the task; for the new scripts, exit 2).
- The new gate-time script runs the product's gate (in the-way: `python -B gate/run_tests.py`; see
  `foundations/part_map.md` `test-runner-command`) and must not require the gate to be run in tests
  of the slice; tests feed it fake gate output.
- Keep each slice's *Checks* focused (WAY-160: never the full gate).

Return as `plan-task` section 5 gives: status, plan path, one-line check result, report path;
**Unread material** and **Searches not found or unclear** in the report.
