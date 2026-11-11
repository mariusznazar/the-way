# Return step — guidelines-departure

**Status:** done. **Commits:** none (nothing needed correcting). Head stays `b4bfca8`; worktree clean.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors" (with the test-citation report, since the cycle's tests are done; no invariant was written, so none reads `test` without a citation).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors".
- `python -B gate/run_tests.py elements/common` — exit 0, 117 tests OK (the tests of the foundation check and the migration, which read the decision log). The full gate is the orchestrator's; not run.

## Return step (fields of the record)

- **Foundation compared with code:**
  - WAY-327 (written): its *Scope* against the part map's 16 parts — identical (checked by a set comparison in the author stage; the foundation check reports a *Scope* part the map does not hold and passes). Compared with the repository's files: no script, test or text reads or lists decisions by number or count in a way WAY-327 breaks (grep of `*.py` for WAY-215/217/327 found none; the Python files that read `decisions.md` are the foundation check, the migration and the installer, which take any decision); `README.md` line 88 ("the foundation of the-way itself: the process is built by its own rules") still holds, the departure being a decision of the-way's own log under WAY-173; `agent-instructions/README.md` names no guidelines. Nothing no longer matched.
  - WAY-215 (opens "Unless a departure under WAY-217 applies") and WAY-217 (a departure applies only within the scope the decision gives): compared with `product-guidelines/reading.md` ("A current decision of the product's log that departs … applies only to the parts and work it expressly covers (WAY-217)"; "A scoped departure removes that finding only within its scope"). They match WAY-327's use of both; no correction.
  - WAY-209 and WAY-244 (skills propose guidelines before the first code or tests of a product with none): they bind a skill's proposal; the-way's departure leaves them untouched, and `product-guidelines/coding` and `product-guidelines/testing` hold the skills as these decisions say. No correction.
  - WAY-173 (a departure is a decision of the product's log with its reason): the *Rationale* of WAY-327 gives the reason. WAY-09 (the directories that may stand on the main branch, none named `guidelines/`): the departure adds none, so WAY-09 matches; no correction.
  - Part map of the touched parts (`decisions`; the change touches `foundations/decisions.md`): its responsibility and files still match; no part added or changed. None of the invariants of the part `decisions` or `every` concerns the content of a decision.
  - No entry that names WAY-327 exists yet; no entry named by it changed.
- **Decisions written or changed:** WAY-327 (written in the foundation step, edited in place by the fix of the Minor findings); no other.
- **Invariants written or changed:** none (no rule set by the task, a decision or the human asks for one; the missing check that a new part reaches this *Scope* is a possible follow-up named in my author report, not set by anyone, so not written).
- **Environment facts:** none (the change rests on no source outside the product).
- **Glossary terms:** none ("departure" is used in the plain sense of WAY-217/WAY-173; no term used against its entry).
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task is independent and has no projected entries).
- **Rows of *Settlements to record* written:** row 1 — WAY-327; row 2 — WAY-327 (the same entry, as its second binding sentence).

## For the request (not fixed, as the handoff says)

- The third binding sentence of WAY-327 says "guidelines of the-way's own", which is wider than the decision's coverage (the coding guidelines and the testing guidelines only). Left as it stands.

## Unread material

- Read in part: `task-cycle/record_template.md` (only its *Return step* section and the lines around it, as the handoff names it for the fields); `README.md` (grep hits at lines 56, 88, 111-130, not the whole file); `foundations/part_map.md` (the `decisions` entry and the 16-part list, not whole); the other foundation entries my search touched, as in the author report.
- Read whole: the handoff, `task-cycle/skill/return_step.md`, WAY-327. `task-cycle/skill/foundation_step.md` not re-read (I read it whole in the author stage).

## Searches not found or unclear

none
