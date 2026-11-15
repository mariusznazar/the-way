# Report of executor 8 — slice 8, task `scripts-after-foundation-review`

**Status:** done

**Commit:** `6e3ab99a5d540d97fe1755e617a9c66893e960ee` "Give the measures of a tool the cycle changed as unknown in the audit count" (on `task/scripts-after-foundation-review`, above `f1d6323`).

**Files changed** (`git diff --stat HEAD~1`): `process-audit/audit_count.py` (+107 / -14), `process-audit/test_audit_count.py`. No foundation entry is changed by this slice.

## What was made

- `process-audit/audit_count.py`
  - New constants `TOOL_GROUPS` (file, paths): `stages.md` with `COST_SCRIPTS`, `mechanism_measures.md` with `(MEASURES_SCRIPT,)`, `gate_times.md` with `GATE_SCRIPTS`. These are the constants Slice 6 uses for the series, not a second list. Also `STAGES_FILE`, `WORKING_NAME`, `WAITING_NAME`, `STAGES_VALUES`.
  - `Cycle.held`: the files of the copy that held a text (set in `fill`).
  - `changed_paths` (the `differs` test of `changed_reason`, now shared), `names_of`, `withdraw_values`, `note_changed_tools`; `main` calls `note_changed_tools(reads, ancestry)` right after the reads, before `analyse`, so every later table and median sees the unknown values.
  - The comment at `MEASURES_FILE` says "A copy that holds neither is of an earlier cycle or of one whose script failed." (To do 9). The module description and the preamble of the result each got a paragraph / sentence for the new rule.
- `process-audit/test_audit_count.py`: helper `own_cycle` (a cycle of the-way whose copy is in the-way's own history), `fresh`, `run_with_prices` in `AuditCountCase`; tests in `Times`, `MechanismMeasures`, `GateRunsMeasures`, `ProcessVersions`, `MeasureVersions`.

## How it finds the commit and why other repositories are left (asked by the slice)

- Version the cycle ran on: `cycle.pin`, resolved by `ancestry.commit` (the existing resolution, full hash by `git rev-parse --disambiguate`). Commit of the last copy: `cycle.later[-1]`, or `cycle.record` where no later copy exists (the same commit `fill` reads the values from: `commits[-1]` of `git log --diff-filter=A` over the record path, in the-way's own history). `git diff --quiet <version> <last> -- <paths>` through `Ancestry.differs`; exit 1 or any failure counts as changed.
- Only `read.key == "the-way"` is checked. The audited repository for that key is the checkout `Ancestry` reads, so both commits are in one history. A cycle of a product has its copy in the product's history, its pin names a commit of the-way, and its own change lies in the product, which holds none of these tools (item 8 holds for cycles of `the-way` only); comparing the two would be a diff across two repositories, which fails and so would count as changed. The test `Times.test_a_cycle_of_a_product_is_not_put_in_doubt_by_a_change_of_a_tool` fails when the key restriction is removed (mutation run).
- A copy of an earlier cycle is not put in doubt: a group is checked only where the copy held the file (`cycle.held`), so a copy with no `mechanism_measures.md` or `gate_times.md` keeps its own reason ("an earlier cycle, or a script that failed"); a cycle whose pin is unknown or does not resolve is left as it is (no version to compare; a failure of `git diff` itself counts as changed, but a failure to resolve the version is no diff).

## Trust boundary (handoff step 4)

The text of the input reaches the new code only as: `cycle.pin` (already validated by `SHORT_HASH` and resolved by git to a full hash before any diff; a crafted pin gives None and the cycle is left), commits from git output, and constant paths. The reason string is built from constants only (the paths of `TOOL_GROUPS`), so no text of a record reaches it. `git diff --quiet` is run through the existing `Git.execute` (no `GIT_` variables, no prompt, read only; `diff` is in the allowed list). No path of the input is followed; nothing is written outside the result. A crafted record cannot make the new code raise: `ancestry.commit` returns None on every failure, and `differs` catches `GitError`.

## Choices (with the way rejected and the cost if wrong)

1. **Post-processing after the reading, not a change of the reading.** `note_changed_tools` replaces the values after `fill` read the copy. Rejected: passing "changed" into `fill`, which needs the pin resolved before the reading (the pin comes out of the record `fill` reads) and a second `Ancestry` inside `read_repository`. Cost if wrong: the file of a changed tool is read and then discarded (a little wasted work); no result differs.
2. **The file of a changed tool is not read for the cycle: its fields missing are dropped (`missing`, `missing_in`) and the run is not ended with exit 1 by them.** WAY-339 says the audit gives the measures as unknown with the reason; a field missing of a file whose values are not read says nothing the reason does not. Rejected: keeping the error line. Cost if wrong: a defect of the file written by the changed tool shows only as unknown with the reason, not as exit 1 and an `Error:` line. This is a reading of WAY-339 / WAY-344 the orchestrator may want to confirm; one test (`MechanismMeasures.test_a_field_missing_from_the_file_of_a_changed_tool_...`) pins it.
3. **One line of reason per group in *Unknown values*, not one per value** for the mechanism measures (`Mechanism measures`) and the gate runs (`Gate runs`), as the existing "no such file" form gives; for the stage script, one line for each of the four values (working time, waiting for tools, cost, share of fix rounds). The earlier lines for those values (their own reasons) are removed.
4. **The number of fix rounds stands** (it comes from the record's item `Review rounds`, not from the stage script), whatever the cost was (it stays `unknown` where the cost was unknown before, as today).
5. **Reason text:** "the cycle changed the tool that wrote them: `<paths that differ>` changed between the version it ran on and the last copy of its record" (the paths named are those that differ, by the same per-path test as the series reasons). Rejected: naming the pin or commits in it (text of the input).
6. **Between the version and the last copy** the diff includes any commit that reached the task branch from the target (a merge of the target into the task branch would count as the cycle's change). Accepted: the slice names this commit; narrowing it needs the base of the cycle's branch, which the audit does not read. Cost if wrong: a cycle that merged a change of the tool from the target is marked as having changed it (unknown with a reason, not a wrong figure).

## Checks

Red on the base (before the code), all failures for the expected reason (the values were read as before instead of `unknown`):
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MechanismMeasures -k GateRunsMeasures -k Times -k ProcessVersions -k MeasureVersions` → exit 1, `Ran 77 tests`, `FAILED (failures=11)`: `GateRunsMeasures.test_a_cycle_corrected_after_the_tool_changed_is_judged_by_its_last_copy`, `...changed_a_tool_of_the_gate...` (two sub-tests), `...changed_every_tool...`, `MeasureVersions...changed_tool_of_a_measure...` (three sub-tests), `MechanismMeasures...changed_the_measures_script...` and `...a_field_missing_from_the_file_of_a_changed_tool...`, `ProcessVersions...changed_the_stage_script_stays_in_its_version...`, `Times...changed_the_stage_script_gives...`. The guards (a cycle that changes none, a product's cycle, an unresolved pin, a copy of an earlier form) pass on the base, as they must.
- The same command after the change → exit 0, `Ran 77 tests ... OK` (run again after the last renames of test methods).
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` → exit 0, `Ran 226 tests ... OK` (run before the final renames of six test methods and a comment wrap; the focused command above ran after them).
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` → exit 0, `Ran 3 tests ... OK`.
- No run of the whole gate (WAY-160).

Own-work check (requirement most likely not met: "a cycle of another repository is left as it is, and a copy of an earlier cycle is not put in doubt by it"): checks that break under mutation. Mutation 1, the key restriction removed → `Times.test_a_cycle_of_a_product_is_not_put_in_doubt_by_a_change_of_a_tool` FAILED (exit 1); mutation 2, the first copy read in place of the last → `GateRunsMeasures.test_a_cycle_corrected_after_the_tool_changed_is_judged_by_its_last_copy` FAILED (exit 1); mutation 3, the `held` guard removed → `MechanismMeasures.test_a_copy_of_an_earlier_cycle_holding_no_such_file_keeps_its_own_reason` FAILED (exit 1). The code was restored after each (file compared with a copy; the commit holds the restored code).

No test that holds a sentence of a decision (`decision:`) or an invariant's test was changed; `test_audit_series_scripts.py` was not touched (WAY-03: nothing to name).

## Reached beyond the handoff

- Read `task-cycle/change/slice.md` (the method names it for a slice) and, in `process-audit/audit_count.py`, the whole file except lines 1841-2130 (the register's reading, which no part of this slice touches) — see Unread material.
- Searched `foundations/` and `project-level/` for a rule of line length: none found; kept lines to 100 characters in what I wrote.

## Mismatch with the handoff

None for the checks. The handoff's range for `foundations/decisions.md` WAY-339 matched its text.

## Unread material

- `process-audit/audit_count.py` lines 1841-2130 (the register's constants and `read_register`) were not read; the rest was read whole. `foundations/part_map.md` and `foundations/invariants.md` entries were read as ranges named; the rest of `test_audit_count.py` was read where it holds the classes the slice names (`AuditCountCase`, `Times`, the measures and gate classes, `ProcessVersions`, `MeasureVersions` start), not whole (3692 lines).
- `foundations/decisions.md` WAY-339 and WAY-350 read whole; `task.md` read at the lines the slice names.

## Searches not found or unclear

- none. (`task.md` line numbers named by the slice are those of the base; the passages matched.)

## Problems observed

- None in the product code. One of my first tests asserted that the other two groups stand in a cycle that changed them; the failure was in the test, not the code, and was corrected before the commit (the failing run is not part of the checks above).

## Working copies

`.runs/executor-8/` of the worktree held a copy of `audit_count.py` for the mutation runs and the output of the two test runs; removed before the return. No other copy, worktree or clone was made; the temporary repositories of the tests are those the tests make in their own temporary directories and remove themselves.
