# Report — correction for the human's remarks (request 106)

**Status:** done.

Worktree `the task's worktree`, branch `task/audit-numbers-mechanism-measures`, from head `e00264a`. Commits: `a686244` (WAY-350), `ab12299` (`task-cycle/gate_times.py` and its test), `72904f7` (`process-audit/audit_count.py`, its test, `process-audit/SKILL.md`), `2f9c200` (`task-cycle/skill/SKILL.md`).

## Remarks

1. **Registry entries with an impossible time.** Fixed in `task-cycle/gate_times.py`: `malformed(start, end, now)` is true for a start or an end more than a minute after the present (`CLOCK_SLACK_MS`) or an end before its start. `prepare` deletes such an entry at the start of a run, like a stale one, and `count_others` counts it for nothing even where the deletion fails. A running entry older than six hours and a name of another form are as before. Tests (`RegistryTest` in `task-cycle/test_gate_times.py`, failed first, both): five malformed entries (far end, far start, reversed, far-start running, end two hours ahead) are pruned and a valid running one and one that ends 30 seconds ahead stay and are counted (count 2); a malformed entry that cannot be deleted (a directory in its place) counts for nothing (count 0). WAY-350 says the same in one clause.
2. **Short sections.** Fixed in `process-audit/audit_count.py`: in *Measure versions* a version in which no cycle gives any mechanism value, or no run any time, has one row (`—` in the measure column, `0`, `unknown`) and one line in *Unknown values* (`Mechanism measures of version <commit>` or `Gate times of version <commit>`, with the reason: no cycle of this version gives a value, its copies hold no file (an earlier cycle, or a script that failed; the record's *Verification* says which) or give none). A version with at least one value keeps its rows and its per-measure lines as they were, a following version included. The section's opening lines say it. Tests (`MeasureVersions`): the rewritten `test_a_version_with_no_cycle_that_gave_a_value_has_one_row_and_one_line_of_reason`, failed first.
   - **Real history of this checkout** (scratch locations file, the register template as register, `--today 2026-11-13`, 76 cycles; the "before" count was run from `git archive HEAD` of `process-audit` and `task-cycle`, the "after" from the worktree):

     | Section | Lines before | Lines after |
     |---|---|---|
     | *Measure versions* | 944 (926 table rows) | 160 (142 table rows) |
     | *Unknown values* | 1614 (1611 rows) | 830 (827 rows) |
     | *Mechanism measures* | 83 (78 rows) | 83 (78 rows), per cycle, unchanged |
     | *Gate runs* | 8 (3 rows) | 8 (3 rows), per run, unchanged |
     | the whole file | 3146 | 1578 |

     The 56 versions with no value give 56 lines of *Mechanism measures of version* and as many of *Gate times of version* in place of the former per-measure lines of `Measure falls` (for example 171 and 114 lines for two measures alone). What is left in *Unknown values* is per cycle (`Fix rounds share` 139, `Mechanism measures` 75, `Gate runs` 75, `Discarded attempt` 72, the two times 72 each), not touched by this remark.
3. **Failed runs.** Fixed. `GateRun` carries `code`; `gate_values` puts a run on the compared side only when its count of others is 0 and its exit code is 0; a failed run, a run whose exit code is unknown and a run of unknown count are shown apart in the same columns. The two count columns are renamed *Runs compared* and *Runs not compared*; the opening lines of the section, the docstring of `process-audit/audit_count.py` and `process-audit/SKILL.md` (matter 4) say so; the reason of *Falls* reads "no run of the version that passed with no other gate". Tests (`MeasureVersions`, failed first, with the changed expectation of the existing test): a failed run alone, a run alone with an unknown code and a version whose only run failed. WAY-350 edited in place (binding paragraph, *Verification*, *Rationale*, *Rejected*); WAY-348, WAY-339 and WAY-349 hold no sentence about which runs are compared (searched the whole log for "alongside", "no other", "company", "another gate", "gate times"), so they are unchanged. `python -B elements/common/foundation_check.py`: exit 0, "0 errors".
4. **Failure of a measuring script.** Fixed. `task-cycle/skill/SKILL.md` step 12: where `cycle_measures.py` or `gate_times.py` ends with exit code 2 and an `Error:` line, the orchestrator records the command, the exit code and the line under *Verification* and in the request's *Checks* as a check that did not run, fixes the call where it was wrong and runs it again, never writes the file by hand, and a file that stays missing stays missing; step 10, where the gate script is named, points to it. `process-audit/audit_count.py`: the reason for a copy with no `mechanism_measures.md` or `gate_times.md` is "the copy holds no `<file>`: an earlier cycle, or a script that failed (the record's *Verification* says which)", also in the docstring; `process-audit/SKILL.md` says it in one sentence in matter 1. The test `test_a_copy_without_the_files_gives_unknown_values_with_their_reasons_and_no_error` has the new reason (see the last item of "Searches not found or unclear" for its failing run).

## Meaning of the foundation edit (marked `the cycle's`)

WAY-350 (and in it, the one clause on the registry):

- English: The audit compares the times of the gate only over runs that passed with no other gate alongside, and shows the runs that failed, or whose exit code is unknown, apart with the others, because a run that stopped early says how soon it failed and not how long the gate takes. A registry entry with an impossible time is deleted and counted for nothing.
- Polish: Audyt porównuje czasy bramki tylko po przebiegach, które zakończyły się powodzeniem i przy których nie działała żadna inna bramka, a przebiegi zakończone błędem albo o nieznanym kodzie wyjścia pokazuje osobno razem z pozostałymi, bo przebieg przerwany wcześnie mówi, jak szybko się wywrócił, a nie ile trwa bramka. Wpis rejestru z niemożliwym czasem jest usuwany i nie liczy się do niczego.

## Checks

| Command | Exit |
|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` (24 tests) | 0 |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (179 tests, 277 s, in the background, ended before the commits) | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` (49 tests) | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` | 0 |
| `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` (39 tests) | 0 |
| `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` | 0 |
| `python -B instruction-files/check_instructions.py .` (0 error, 0 warn) | 0 |
| `python -B elements/common/foundation_check.py` (0 errors) | 0 |
| `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` (after the commits) | 0 |

Tests written first and seen failing: `test_gate_times.py` (2 failures), `MeasureVersions` (4 failures, including the existing gate test whose expectation changed). The product's gate was not run.

## Own-work check

Requirement most likely not met: ruling 2's "one row" for a version with no value must not hide a version that has values in only one of the two instruments, and ruling 3 must not drop a failed run from the count. Check: the real-history run (the 56 versions with no value give one row each, the 142 table rows left hold the versions with values) and the test of a failed run, whose `Runs not compared` counts are worked out by hand (5.000 and 300.000 give 152.500). In the same real-history run the after-count exited 0 with 76 cycles.

## Unread material

None of the files the handoff names was left unread; `correction-remarks.md` and `correction-handoff.md` were read whole. The reviewers' reports (`return-step-review-report.md`, `whole-change-review-report.md`) were not read; the remarks hold their words.

## Searches not found or unclear

- The method names "the file it names for this variant" (`task-cycle/skill/correction.md` exists in the checkout); I read `task-cycle/change/SKILL.md` section 1's row for a correction and followed the remarks, and did not open `task-cycle/skill/correction.md` (the orchestrator's file, not the author's).
- "Reason ... 'no cycle of this version carries the file' or the like" (ruling 2): put the reason in *Unknown values*, not in the table cell, because the table has no reason column. The row's measure cell is `—`.
- The changed test for the absent-file reason was not seen failing before the code; afterwards I put the old reason back for a moment: the test failed (`FAILED (failures=1)`), and with the new reason it passes.
- WAY-348 and WAY-339 were searched for the sentence on which runs are compared and hold none.

## Choices, with the way rejected and its cost if wrong

- Registry: the slack of a minute for "the present", on the run's start clock in `prepare` and on the run's end clock in `count_others`. Rejected: no slack (a clock difference between two sessions would delete a valid entry). Cost if wrong: an entry whose end is 61 seconds ahead because of a clock is deleted, and the other run is not counted once.
- A malformed running entry (a start in the future) is deleted as well as an ended one, as the ruling reads. Cost if wrong: a running gate on a machine with a clock set ahead by more than a minute is not counted.
- Compared side: `others == 0` and `code == 0`. A run whose count is unknown and one whose code is unknown both go apart. Rejected: counting a run with an unknown code as passed (the file did not say).
- Table headers renamed *Runs compared* and *Runs not compared* (the opening lines give the meaning). Rejected: long headers naming every case in the cell. Cost if wrong: a reader of the table alone does not see why a run is not compared until he reads the lines above it.
- One row per empty version has `0` and `unknown` and the measure `—`; the version after an empty one keeps its per-measure lines of `Measure falls` ("no cycle of the previous version gives a value"), as ruling 2 keeps the rows of a version with a value as they are. Rejected: a single line for it too (a change of what ruling 2 says). Cost if wrong: after a run of empty versions, the first version with values adds up to 15 or more lines.
- Step 10 of `task-cycle/skill/SKILL.md` points to step 12 for the failure of a measuring script instead of repeating the rule. Rejected: the rule twice (two places to keep in step).
- WAY-350 edited with one clause on the registry's malformed entries, which the ruling did not list; it keeps the entry in step with the script. Cost if wrong: the entry says more than the human approved; it is in the list of the `the cycle's` edit above.
