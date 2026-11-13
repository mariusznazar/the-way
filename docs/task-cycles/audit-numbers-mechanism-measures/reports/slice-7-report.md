# Report — slice 7 (series by instrument, medians per version and the comparison with the previous version)

**Status:** done

**Commits:** `49ab2fa` (one commit; the slice's range is `9209ecb..49ab2fa`, base `9209ecb`).

## Files changed

- `process-audit/audit_count.py`: +222 / -5 (the 5 removed lines: the body of `Ancestry.changed`, now a call of the new `Ancestry.differs`, and the signature lines of `render` and of `main`'s call)
- `process-audit/test_audit_count.py`: +297 / -0 (class `MeasureVersions`, module helper `gate_run`, constant `TOTAL`)

## What was made

- `Ancestry.differs(earlier, later, paths)`: `git diff --quiet` over `paths`, exit 1 or any failure counts as changed. `Ancestry.changed` now calls it with `TREE_PATHS`; the assignment of `TREE_PATHS` is untouched.
- `Versions.ordered`: `process_versions` keeps the versions in their date order (one assignment; the cost series are made as before).
- `instrument_series(versions, ancestry, script)`: splits the ordered versions into series by a change of `script` alone. `MEASURES_SCRIPT = task-cycle/cycle_measures.py`, `GATE_SCRIPT = task-cycle/gate_times.py`.
- `GateRun` and `Cycle.gate_timed`: the runs of `gate_times.md` as numbers (others as int, total and directory seconds as `Decimal`), filled in `read_gate` beside the string rows of Slice 6 (which are unchanged).
- `measure_versions`, `mechanism_rows`, `gate_rows`, `gate_values`, `falls_answer`, `median_text`, `measure_number`: the medians (`median_of`, the rule of the cost) and `Falls`; `measure_versions_lines` writes `## Measure versions` after `## Process versions`, with one subsection per series, `### Mechanism measures, series N` and `### Gate times, series N`.
- The unknown `Falls` answers go to *Unknown values* as `Measure falls: <label>, version <commit>` and `Gate time falls: <measure>, version <commit>` with the reason.
- The module docstring has a paragraph on the measure versions.

## Checks (command and exit code)

| Check | Exit |
|---|---|
| Red run, before the code (only the stub `instrument_series` returning `[]` existed): `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MeasureVersions` — 8 tests, all failing by assertion (9 failures with subtests; the section was missing, the unit test failed on its assertion) | 1 |
| Green run: same command | 0 (8 tests) |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MeasureVersions -k ProcessVersions` after the commit | 0 (22 tests) |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (whole file, run once in the background, waited for, before the commit) | 0 (172 tests, 260 s) |
| `git diff 2292f334… HEAD -- process-audit/audit_count.py`, searched for `TREE_PATHS` (at HEAD before this slice's commit, and the working tree against the base after the edit): no changed line holds the assignment; the only changed lines with the name are the call in `changed` | no changed assignment |
| `git diff --quiet 2292f334… HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the commit | 0 |

Not run: the product's gate (`gate/run_tests.py`), as the handoff says. Mutations tried by hand and restored (the file was restored from a copy; the committed file is the unmutated one): the gate median over all runs (`median_of(alone + apart)`) failed the gate test; adding `TREE_PATHS` to the instrument's `differs` call failed three tests (series, price list, reviewer/stages/classes); `<=` instead of `<` in *Falls* failed the medians test.

## Own-work check

- Requirement most likely not met: the second acceptance criterion, that the cost series stay as they were and the added scripts start no new cost series, while the measure series are split by the two scripts alone.
- Check: `test_a_change_of_an_instrument_starts_only_the_series_of_its_own_measures` makes four versions of a fake the-way, the second changing `task-cycle/cycle_measures.py`, the third `task-cycle/gate_times.py`, the fourth the reviewer's file and `cycle_stages.py`, and asserts the cost series `[v1, v2, v3]` and `[v4]`, the mechanism series `[v1]` and `[v2, v3, v4]`, the gate series `[v1, v2]` and `[v3, v4]`, with no third series of any kind and no comparison across a split. The twin test `test_the_reviewer_the_stage_script_and_the_list_of_classes_split_no_series_of_measures` shows the other way round (cost splits four times, the measures never). The existing `ProcessVersions` tests, which also change the two scripts between versions, still pass.
- It showed: all pass; the three mutations above fail the intended tests.

## Choices

1. **What the two counts of the gate table count.** `Runs with no other gate` and `Runs with another gate or an unknown count` count the runs *that give the time of the row* (a run alone whose total is unknown is in neither count and has its reason in *Unknown values* from Slice 6). The plan's wording leaves it open whether the count is of all alone runs or of those giving the value; I chose the second so that the count matches the number of values behind the median, as *Cycles with a value* does. Cost if wrong: a run with an unknown time is not visible in the table (it is in the per-cycle section and *Unknown values*). The section's opening lines say it.
2. **A directory written twice in one run** counts once, at its first time, and the run gets a reason in *Unknown values* (`Gate runs: Directories`). The writer never does this; a crafted file would otherwise count one run twice in a directory's median.
3. **A version with no run still has the `Total time of the run` row** (counts 0, medians `unknown`), so a version never vanishes from its series. A directory has a row only where some run of the version lists it; a version lacking a directory its predecessor had gets no row for it, and the next version's *Falls* for it is `unknown` with the reason that the previous version has no run giving it.
4. **The median is written as the exact `Decimal`** (`format(value, "f")`): `7.5` for a half, `105.000` for totals kept to three decimals, `65.0` for a directory kept as printed, the share `12.75%`. No rounding is applied to a median.
5. **Measure column of the gate table**: `Total time of the run` and `Directory: <name>` (the name cut to 200 characters as in the Slice 6 section, escaped by the table writer); directories are in order of name after the total.
6. **A failed gate run is not left out.** The plan says only the count of other gates decides which runs enter the median; a run with a non-zero exit code whose count is `0` enters it. I noticed this, did not change it, and report it as a possible concern for the task's author.
7. **No cap on the distinct directories of a version.** The number of rows is bounded by the total number of directory entries read, which Slice 6 already bounds per file (500 runs, 50 directories per run, 4 MiB), so the work and the result are linear in the input; a crafted test (700 runs, a 500-character name, a bar and control characters, wrong-width rows) checks it. Cost if wrong: a crafted history could make a long table; the same holds for the *Gate runs* section.
8. **Test class** `MeasureVersions` borrows the helpers of `ProcessVersions` by assigning its functions as class attributes (it does not subclass it, so that none of the 13 `ProcessVersions` tests run twice).

## Reaches beyond the handoff

None. All foundation entries and passages read were those the handoff names (WAY-338, WAY-339, WAY-328, WAY-331, WAY-343, WAY-348, WAY-350 whole in the ranges given; WAY-341 and the invariant `tracked-file-private-paths`, the `process-audit` part map entry read by their ranges).

## Unread material

- `.runs/task-cycles/audit-numbers-mechanism-measures/task.md` and `plan.md`: not opened; the handoff carries the passages word for word (as the handoff allows).
- `foundations/decisions.md` WAY-339 (11193-11233), WAY-341 (11254-11275), WAY-338 (11166-11192), WAY-343 (11310-11335), WAY-348 (11519-11548), WAY-350 (11582-11608), WAY-328 (10868-10917), WAY-331 (10990-11013): read whole. `foundations/invariants.md:86-95` and `foundations/part_map.md:115-124`: read whole.
- `task-cycle/cycle_measures.py` and `task-cycle/gate_times.py`: not opened; the forms were taken from the handoff and the Slice 6 readers.
- The rest of `process-audit/audit_count.py` between lines 600 and 1340 (the readers of records and the register) and from 1640 to 2000 (the register): not read; I read the file from the start to line 360, the readers of the two files and of the copy (1340-1630), `Ancestry`, the process-version code and `render`/`main`.
- `process-audit/test_audit_count.py`: read lines 1-220, 1380-1650 and 2360-end; the rest not read.

## Searches not found or unclear

- `process-audit/SKILL.md` (lines 123 and 157) lists the sections of the count and the steps of the session ("What each version of the process shows" for each series of *Process versions*); it does not mention `## Measure versions`. It is not in this slice's *Change*, so I left it; a later slice or the return step should add the new section there.
- The plan's Slice 6 says "first five cells" of a directory row repeated; the handoff already marks it as a slip. Nothing in this slice depended on it.
- The plan names the section's subsection titles nowhere; I chose `### Mechanism measures, series N` and `### Gate times, series N` (they do not collide with the `### Series N` of *Process versions* or with the `## Mechanism measures` section of Slice 6).

## Problems observed

None beyond choice 6 above and the SKILL.md gap.
