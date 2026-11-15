PASS 4c03086723435b286e1a94c92c5b12e3028be12d

# Review of slice 6 — two kinds of series: the cost and the count of remarks

Range `61894c282d8e92625ba1730ee967975d9d32c4d9..4c03086723435b286e1a94c92c5b12e3028be12d`; `git rev-parse HEAD` is the head. One commit, two files: `process-audit/audit_count.py` and `process-audit/test_audit_count.py`. Counts: blocking 0, Minor 1, out of scope 0 (the Minor finding is in scope but does not block; the test of Slice 7 is declared below).

## Findings

### Critical

none

### Important

none

### Minor

1. `process-audit/audit_count.py:2908-2909` (section *Cost*): "a cost belongs to that series only, and a new list starts a new one (WAY-339)". After this slice a series of the cost also ends at a change of `task-cycle/cycle_stages.py`, so a price list is no longer the only thing a cost's series is told by (the module description at `audit_count.py:258`, "(the series the cost belongs to)", says the same). The sentence is not false (a new list does start a new series) but it reads as if the list were the whole rule. The section is not the *Process versions* section the slice rewrites, and Slice 7 reworks the cost, so the wording is better made right there. Evidence: the two sentences against `cost_boundary` (`audit_count.py:2404`).

## Against the task and the spec

- Task To do 5 and 6, D5: a series of the cost ends at a new price list or at a change of `task-cycle/cycle_stages.py`, and nowhere else (`cost_boundary`, `COST_SCRIPTS = (COST_SCRIPT,)`). A series of the count of remarks ends wherever the cost's ends (`count_boundary` calls `cost_boundary` first), then at a date of the register's list of classes, then at `COUNT_PATHS` (the four folders and `task-cycle/agent-types/the-way-stage.md`; `the-way-author.md` is not in it). Both splitters work on consecutive versions, so every cost boundary is a count boundary. `git diff --quiet` is kept, with a failure counting as changed (`Ancestry.differs`, unchanged).
- Each comparison stays inside its kind: Q1, Q2 and *Plans read* only in the table `### Count of remarks, series N`; the median cost, the number of cycles with a known cost and Q3 only in `### Cost, series N`; each table carries `Begins at this version: <reason>.` The reasons name the changed path. The description of the module, the sentences "deliberately conservative" and "errs toward fewer comparisons" (gone), the section text and `measure_versions_lines` were rewritten; the price (the cost cannot tell "the reviewer found more" from "the process got dearer") is stated in both places and matches WAY-339 *Rationale*. Q1, Q2, Q3 and the section *Measure versions* are kept. The column *Cycles* stands in both tables, which is a count of cycles, not a measure of either kind.
- WAY-339 (foundations/decisions.md, read whole at the given lines; it already holds the split, so the code does what the entry says): the code, the description and the tests agree with its "complies" and "violates" lists for the cost, the count of remarks and the measures of context and the gate (the series of the instruments are unchanged: `instrument_series` now uses `split_series`, with the same reasons).
- Invariants: `audit-series-script-paths` still holds (its test passes). It names the three scripts of the measures series; the new paths (`COST_SCRIPTS`, `COUNT_PATHS`) are guarded by the executor's own test `test_each_path_that_starts_a_series_is_a_path_git_tracks`. `script-language`, `script-imports`, `script-subprocesses`: no new import, no new program (git only).
- Nothing added that nobody asked for: the helper `changed_reason` and the extra test of tracked paths serve the slice.

## Trust boundary

`audit_count.py` is the process-audit's trust boundary. What the slice adds reads no new input: the paths are constants, the reasons are fixed text and those constants, and git is run with full commit hashes that `Ancestry.commit` already validated. A crafted record, register or locations file reaches the new tables only through the version's day and the existing counts and answers (unchanged code paths: `contradiction_of`, `too_large_of`, `money`, `table`, which escape cells). I read that the new `count_rows` and `cost_rows` put only `version.commit`, `version.day`, counts, answers and `money(median)` in cells. Versions that git cannot compare (hashes the checkout lacks) give exit 128 and count as changed in both kinds, tested (`test_a_git_that_cannot_compare_the_two_versions_counts_as_a_change_of_both_kinds`). No crash path, no write outside the places the script writes, no command run from input text.

## Tests

- The tests the slice names exist and cover each requirement: `the-way-stage.md` starts the count and none of the cost; a file under `task-cycle/review` and one under `task-cycle/change` start the count and none of the cost; `task-cycle/cycle_stages.py` starts both (`test_a_change_of_the_stage_script_starts_a_series_of_both_kinds`); a new price list starts both (`PriceBoundary`). Beside them: the table of every path with controls that start nothing (`the-way-author.md`, `cycle_measures.py`, `gate_times.py`, `gate/run_tests.py`, `task-cycle/skill/SKILL.md`, `README.md`), a class date on, before and after the versions, the unknown list, the failing git, a test that the two tables hold no column of the other kind, and an end-to-end test where a class dated on the day of v3 splits the count and the cost of v3 is compared with v2's.
- The expected values are written out by hand (medians, Q3, the reasons), not computed by the code under test. The tests read real git repositories built by the test's own `Repository` helper.
- I mutated the code in a worktree of the head and ran `-k ProcessVersions -k PriceBoundary -k MeasureVersions`: (a) the cost boundary also taking `COUNT_PATHS` made 10 tests fail (exit 1: the three files-under-the-count tests, the table test for each of the paths, the failing-git test, the measure test of the reviewer); (b) the count boundary without the cost boundary made 6 fail (`cycle_stages.py`, the price list, the table, the failing git, the old/newer form, the measure test). Both mutations are caught.
- WAY-03: the changed tests are no test of an invariant and none holds a sentence of a decision by a line `decision:`. `test_audit_series_scripts.py` is unchanged.

## Declined to judge

- `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` fails (same on the base): `audit_count.py` still reads the older header of the stage report; the reader of the two new write columns is Slice 7 (orchestrator's information, choice Q3). Set aside as outside this slice.
- `process-audit/SKILL.md:51,185-187,210`, `process-audit/problem_register.md:76`, `process-audit/price_list.md:9` still say that a class date or a change of the reviewer's instructions starts a series of the cost, and read series by the old one-table shape. Slice 10 of the plan is the slice that aligns that prose (plan table, "the process-audit prose is one slice after the code slices"), so it is not a finding here; it must not be missed there.

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `4c03086723435b286e1a94c92c5b12e3028be12d` |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (the full file, in the reviewed worktree, head) | 1: `Ran 193 tests`, `FAILED (failures=1)`; the one failure is `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` (the expected red test until Slice 7); no other test fails |
| `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` | 0, 3 tests OK |
| `-k ProcessVersions -k PriceBoundary -k MeasureVersions` on the head, in a worktree, with the cost boundary mutated (a) | 1, 10 failures, as intended |
| the same with the count boundary mutated (b) | 1, 5 failures and 1 error, as intended |
| the same command on the unmutated head | not run on its own: the full-file run above contains all of its 36 tests and only the expected one failed |

Not run: the whole gate (WAY-160); the audit on real history (the executor ran it: 101 cycles, exit 0).

## Reach beyond the dispatch

- `.runs/task-cycles/scripts-after-foundation-review/plan.md`: only a grep of the slice headings and the line of the table about the prose of `process-audit/` — to see which slice aligns the prose that the executor named in its report.
- `grep` over `process-audit/*.md` and `*.py` for "series" and "conservative"; and over the repository for `series_boundary`, `TREE_PATHS`, `VERSION_HEADER`, `.series`, `### Series`: no remaining use (and the only prose that still holds the old rule is in the list above).
- `process-audit/audit_count.py:250-262` and `2900-2916`: the sentences of the cost section (the Minor finding).

## Working copies

A worktree of the head and its mutated copies of `audit_count.py` stood in `.runs/review-6/` (`wt`, `orig.py`, two earlier copy directories `m1` and `m2` that I abandoned because the copied test had no neighbours to import); the full-file output stood in `.runs/review-6-full.txt`. All removed (`git worktree remove --force`, `git worktree prune`, `rm -rf`); `git status` of the reviewed worktree is clean.

## Unread material

- `process-audit/test_audit_count.py`: I read the diff of the range whole and the new tests in it, not the unchanged classes (`CycleFound`, `ProcessPin`, `Remarks`, `Times`, `CraftedInput`, `Locations`, `Cost`, `StagesForms`, `MeasuresCase`, `MechanismMeasures`, `GateRunsMeasures`, `RegisterCount`, `Run`); I ran them as part of the full file.
- `process-audit/audit_count.py`: I read the diff and the functions it touches (`Ancestry.differs`, `Versions`, `changed_reason`, `cost_boundary`, `count_boundary`, `split_series`, `instrument_series`, `process_versions`, `count_rows`, `cost_rows`, `versions_lines`, `measure_versions_lines`), not the whole file.
- `.runs/.../task.md` whole; `.runs/.../spec.md` only D5 (the lines the dispatch gives); `foundations/decisions.md` WAY-339 whole (the lines the dispatch gives, 7432-7585 against the current file); `foundations/invariants.md` 116-145 and 398-407, `foundations/part_map.md` 122-136 read whole. No guideline file named by the dispatch; none read.

## Searches not found or unclear

- The dispatch says the foundation entry WAY-339 stands at `foundations/decisions.md:7432-7585`; in the worktree the heading is a few lines earlier (the entry begins at about line 7430) and the lines given end inside the next entry (WAY-350). The entry itself is whole and unambiguous; nothing missing.
- None other.
