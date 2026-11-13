PASS 49ab2fa299748b22e3a69f71c00be1a6ac457d41

# Review of slice 7 — series by instrument, medians per version, comparison with the previous version

Head reviewed: `49ab2fa299748b22e3a69f71c00be1a6ac457d41` (`git rev-parse HEAD` matches). Range `9209ecb..49ab2fa`, one commit.
Variant: a planned slice. Worktree and index untouched (`git status --short` empty before and after).

Blocking findings: 0. Minor: 3. Out of scope: 0.

## Changed files (`git diff --numstat 9209ecb..49ab2fa`)

- `process-audit/audit_count.py`: +239 / -5 (the executor's report says +222; the numstat is the figure)
- `process-audit/test_audit_count.py`: +297 / -0

## What I verified

- Series by instrument. `instrument_series` (`audit_count.py:2297`) splits the date-ordered `Versions.ordered` by `Ancestry.differs(previous, version, (script,))`, i.e. `git diff --quiet` on that one script, exit 1 or `GitError` counts as changed. It consults nothing else: no price list, no class dates, no `TREE_PATHS`. `MEASURES_SCRIPT` and `GATE_SCRIPT` each drive their own series. The comparison is with the previous version of the series (`blocks[-1].versions[-1]`), the same way the cost series are made.
- The cost series are untouched. `process_versions` gains one line (`result.ordered = versions`); `series_boundary` and `TREE_PATHS` (`audit_count.py:318-319`) are unchanged. `Ancestry.changed` now calls `differs(..., TREE_PATHS)` with the same git command and the same failure rule. `git diff 2292f334… HEAD -- process-audit/audit_count.py | grep TREE_PATHS` shows only the call in `changed`, no changed assignment. This covers the handoff's item (3): `test_a_change_of_an_instrument_starts_only_the_series_of_its_own_measures` makes a change of `cycle_measures.py` and of `gate_times.py` between versions and asserts the cost series stay `[v1, v2, v3]`, `[v4]` while `cycle_stages.py` plus the reviewer's file still split the cost; the twin test shows the other way round.
- Medians and `Falls` against the passage of the task and WAY-339, WAY-348, WAY-350. `median_of` is the cost's own function (middle one, or mean of the two middle ones, `Decimal`); `format(value, "f")` writes `7.5`, `105.000`, `12.75%`. `Falls` is `yes` for strictly lower, `no` otherwise, `unknown` for the first version of a series or an unknown median on either side, each with its reason in *Unknown values* (`falls_answer`, `audit_count.py:2333`). I recomputed the hand figures of the two median tests (odd 7, even 7.5, 5.5; the share 12.75, 12.0, 12.25; the gate table of five versions) and they are right.
- Gate table. `gate_values` puts a run with `others == 0` on the alone side, any other run, an unknown count (`None`) included, on the apart side, and a malformed (wrong-width) row has both `None` and enters neither list. Median and `Falls` use only the alone side; the apart side is shown in the last two columns and never compared. A version with no run alone gets `unknown` with the reason `no run of the version with no other gate gives this time`. Directories: a directory's median takes the runs that give its time. The opening lines say how the series are made and that numbers of one series are never set beside those of another.
- Trust boundary. Everything that reaches a cell was already validated by Slice 6's readers before `measure_number` and the `GateRun` constructor see it (`measure_fits`, `GATE_STARTED`, `GATE_TOTAL`, `GATE_OTHERS`, `GATE_SECONDS`: digits only, bounded length), so `Decimal(...)` and `int(...)` cannot raise on crafted text. Directory names are cut to `TEXT_CAP` and go through `table`/`cell` (bars written `\x7c`, control characters escaped); the unknown-values rows go through `cell` too. A directory written twice in a run counts once and is reported. The limits of 500 runs and 50 directories per run stay in force. The crafted test (a name with a bar and `\x1b`, a 500-character name, 700 runs, wrong-width rows) asserts no unprintable character, no 201-character run of `d`, seven cells in every row and the exact row count.
- Tests fail for the right reason. The executor's three mutations (median over all runs, `TREE_PATHS` added to the instrument's test, `<=` for `<`) are plausible against the assertions I read: the gate test names the apart values that would pull the median down if they entered (10.000 and 1.000), the series test asserts the exact versions of each series for both instruments, and the medians test asserts `no` for the equal median. The price-list test uses a fake ancestry and `Version` objects directly (a single run has one price list, so no real run can split at it); it asserts that `instrument_series` asks git about the one script only and that `series_boundary` still gives "the price list changed" for the same two versions. That is adequate for the plan's "a new price list starts a series of the cost and none of the measures".
- Foundation. WAY-339, WAY-348 and WAY-350: the code and the section's opening text say what they require (only the instrument starts the series of the measures; the median of each measure per version and the comparison within a series; the median over runs with no other gate, the rest apart, a version with no run alone gets no comparison). No invariant test is changed by the range. `process-audit/SKILL.md` not mentioning the new section is slice 8's, as the handoff says.

## Findings

### Critical

none

### Important

none

### Minor

1. A failed run enters the median. `process-audit/audit_count.py:2383-2388` (`gate_values` puts a run on the alone side by `run.others == 0` alone). A run with exit code 1 or 2 and no other gate beside it counts. `gate/run_tests.py` does not stop at the first failing directory (it runs all and collects `failed`), so an exit-1 run is a full run and is a fair sample; but an exit-2 run that ends before the directories (the gate cannot start, no report) has a small total and would lower the version's median total and could make `Falls` read `yes`. This is what the task item 5 and WAY-350 say (only the count of other gates decides), so it is not a defect of the slice; it is a design point for the task's author. Cost of leaving it: a version with an early abort looks faster; cost of excluding by exit code: more rules in a count whose decision names one criterion. A comparison of the exit code column in the *Gate runs* section already shows such runs, so the information is not lost. Evidence: the code line above and `gate/run_tests.py` lines 48-117.
2. The number of rows is not capped by distinct directories. `process-audit/audit_count.py:2374-2392` (`gate_values`, `gate_rows`): each distinct directory name of each version gets a row, and each unknown `Falls` of it a row in *Unknown values*. Work and size are linear in the directory entries read, which Slice 6 already bounds per file (500 runs, 50 directories, the file-size limit), so this matches the existing *Gate runs* section and the crafted test checks the 500-run case. It stays unbounded in the number of cycles in the history, as the other sections do. Not a regression of a different kind; named so the return step can decide whether a total cap is wanted. The executor reports this as its choice 7.
3. The executor's report states `audit_count.py` as +222; the numstat gives +239 / -5. No effect on the change.

## Declined to judge

- `process-audit/SKILL.md` not naming `## Measure versions` (the handoff gives it to slice 8).
- The Minor findings of slices 5 and 6, and the Slice 6 readers themselves (grouping of consecutive rows into a run, the 500-run limit), which are before this range.

## Checks I ran

- `git rev-parse HEAD` → `49ab2fa299748b22e3a69f71c00be1a6ac457d41`.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MeasureVersions -k ProcessVersions` → exit 0, 22 tests, 49.5 s.
- `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` → exit 0, 1 test.
- `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py | grep -n TREE_PATHS` → only the call in `Ancestry.changed` (lines 688 and 694 of the diff), no changed assignment; `grep -n "^TREE_PATHS"` shows the assignment as it was.
- `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` → exit 0.
- Not run: the whole `test_audit_count.py` (several minutes; the handoff said to run the focused classes) and the product's gate (forbidden). The red-before run of the new tests was not repeated by me: the new tests were not run against the base, so "fail before the slice" rests on the executor's account; I did check by reading that each asserts a section and rows that the base cannot produce.
- Mutations: I did not repeat the executor's mutations; I judged the assertions by reading them.

## Reaches beyond the handoff

- `gate/run_tests.py` (grep for `fail`, `break`, `return`, `exit`, and lines 48-117 by the output): to see whether a failed run is a full run (Minor 1).
- `process-audit/audit_count.py` outside the diff: lines 340-380 (constants), 1405-1575 (the readers of Slice 6, for what reaches `GateRun`), 2235-2310 and 2455-2530 (`Series`, `Version`, `median_of`, `series_boundary`, `process_versions`), 2600-2640 (`cell`, `table`), 2796-2812 (*Unknown values* rendering): to judge the change at its callers and at the trust boundary.
- `process-audit/test_audit_count.py`: grep for the helper definitions only (`gate_row`, `gate_file`, `measures_file`, `MEASURE_VALUES`); the bodies of the `ProcessVersions` helpers the new class borrows I did not read.
- `foundations/decisions.md` WAY-348 (11519-11548), WAY-341 (11254-11275), WAY-339 (11193-11233), WAY-350 (11582-11608), `foundations/part_map.md:115-124`: all named in the handoff's list of foundation entries.

## Unread material

- `foundations/decisions.md` WAY-331 (10990-11013), WAY-328 (10868-10917), WAY-338 (11166-11192), WAY-343 (11310-11335) and `foundations/invariants.md:86-95` (tracked-file-private-paths): not read; the invariant is checked by its test (exit 0), the others bear on the earlier slices' readers and on the cost question the slice does not change.
- `.runs/task-cycles/audit-numbers-mechanism-measures/task.md` and `plan.md`: not opened; the handoff copies the passages word for word and I judged against those.
- `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`: not opened (the slice reads files they write, whose form Slice 6's readers fix).
- `process-audit/audit_count.py` between lines 600 and 1400 and 1580-2230 (the readers of records, the register, `Ancestry` beyond `differs`), and `process-audit/test_audit_count.py` outside the diff: not read whole.

## Searches not found or unclear

- none. (One slip, already marked by the handoff: the plan's Slice 6 text says the "first five cells" repeated in a directory row; it did not matter here.)
