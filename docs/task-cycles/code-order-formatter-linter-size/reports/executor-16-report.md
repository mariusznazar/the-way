# Report — executor-16, Slice 16 (the analysis of versions and the report moved out of the audit's command)

## Status

`done` (with the small adaptation named under "Adaptations": `count_rows`, `cost_rows` and `money` stand in
`version_analysis.py`, not in `audit_report.py`).

## Commits and files

- `a30a04ff` Move the analysis of the versions into version_analysis.py and the writing of the report into
  audit_report.py, dividing analyse ... and render ... (base `95316c25`, one commit; the slice adds nothing, so
  no WAY-365 move precedes it).
- `process-audit/audit_count.py` 2241 -> 897 lines. The three files together: 1654 lines added, 1390 removed.
- `process-audit/version_analysis.py` new, 1056 lines. `process-audit/audit_report.py` new, 552 lines.
- Foundation and tests: unchanged. The part map is unchanged (neither module is a trust boundary; neither
  reads input from outside the product).

## What stands where

- `version_analysis.py`: `committed_date`, `Ancestry`, `counted`, `Analysis`, the divided `analyse`, `unknown_field`,
  `unknown_rows`, `Version`/`Series`/`Versions`, `median_of`, the changed-paths helpers, `withdraw_values`,
  `note_changed_tools`, the boundaries, `split_series`, `instrument_series`, `MeasureVersions`, the measure rows,
  `contradiction_of`, `too_large_of`, `process_versions`, `count_rows`, `cost_rows`, `money`; the constants of the
  series (`COST_SCRIPT`, `COST_SCRIPTS`, `COUNT_PATHS`, `MEASURES_SCRIPT`, `GATE_SCRIPT`, `GATE_SCRIPTS`,
  `GATE_TEST_RUNNER`, `TOOL_GROUPS`, `STAGES_FILE`, `WORKING_NAME`, `WAITING_NAME`, `STAGES_VALUES`, ...) with
  their comments.
- `audit_report.py`: `cell`, `duration`, `share_text`, `table`, `versions_lines`, `measure_versions_lines`,
  `measures_lines`, `gate_lines`, the headers of the tables, `RESULTS_ENTRY`, `write`, and `render` divided into
  `intro_lines`, `cycles_lines`, `cost_lines`, `measures_and_versions_lines`, `problems_by_cycle_lines`,
  `fixed_issues_lines`, `open_issues_lines`, `dropped_issues_lines`, `occurrence_cost_lines`,
  `unknown_values_lines`.
- `analyse` (219 lines) is divided into `cycles_by_record`, `place_problems`, `count_refused_rows`,
  `problems_by_cycle`, `fixed_issue_row`, `waiting_days` (with `unknown_waiting`), `open_issue_row`,
  `dropped_issue_row`; `analyse` itself is now about 45 lines. The largest function in any of the files is 81
  lines (`read_prices`, untouched).
- Dependency direction: `audit_count` -> `audit_report` -> `version_analysis` -> `record_reading` /
  `problem_register` / `stage_pricing`; no module imports `audit_count`.
- `audit_count.__all__` now lists the names the tests reach and the file no longer uses: `COST_SCRIPT`, `COST_SCRIPTS`,
  `COUNT_PATHS`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`, `MEASURES_SCRIPT`, `TOOL_GROUPS`, `Ancestry`, `Register`,
  `Version`, `cost_boundary`, `count_boundary`, `instrument_series`, `read_contradiction`. No `noqa` was added to
  reach them; the tests are unchanged. (`Git`, `GitError`, `Cycle`, `Prices`, `remarks_check`, `fill` are still
  used in the file.)

## Checks (command, exit code)

All from the worktree root.

| Check | Command | Exit |
|---|---|---|
| format | `<ruff> format --check --config ruff.toml process-audit/audit_count.py process-audit/version_analysis.py process-audit/audit_report.py` | 0 |
| lint | `<ruff> check --config ruff.toml --ignore-noqa` on the same three files | 0 |
| process-audit tests | `python -B gate/run_tests.py process-audit` (276 tests, 389 s; output in `executor-16-checks/gate-process-audit.txt`) | 0 |
| part-map tests, first run | `python -B gate/run_tests.py elements/part-map` before the commit | 1 |
| part-map tests, rerun | the same command after the commit `a30a04ff` (40 tests; `executor-16-checks/gate-part-map-2.txt`) | 0 |
| sizes | `executor-16-checks/size_check.py` (`function_sizes`, `file_lines` of `agent-instructions/test_size_invariant.py` against 110 and 1200) on `audit_count`, `version_analysis`, `audit_report`, `record_reading`, `problem_register`, `stage_pricing`, `record_items` | 0, no function over 110, no file over 1200 (largest file `record_reading.py` 1149) |
| import runs nothing | `python -B -c "import sys; sys.path.insert(0, 'process-audit'); import <module>" < /dev/null` for `version_analysis` and `audit_report` | 0 and 0, stdout and stderr 0 bytes each |

The failure of the first part-map run: `test_cross_part_imports.TheWay.test_the_way_imports_only_from_allowed_parts`
named `version_analysis` and `audit_report` as "not a file the check sees": the check reads the files git tracks
and the two new files were still untracked. After the commit it passes; the code did not change between the two
runs. The full gate was not run (handoff).

## Own-work check (WAY-164)

Requirement most likely not met: "no change of behaviour, exit codes, messages or the bytes of the report", above all
in the two divided functions and in a file with a trust boundary (`audit_count.py`).

Checks and what they showed (scripts in `executor-16-checks/`):

1. Before and after on the same input, command run as a process, base code against the new code, with a fixed `--today`:
   - the real history of this repository (a clone at the base, 118 cycles, the template register): stdout, stderr,
     exit code 0 and the bytes of `count-<date>.md` and `count-latest.md` identical (sha256
     `c6afdf4a7edd726445e2492d41660d42fd2bf9cfef5b1bed21dfc41c5ab2e6eb`);
   - a crafted register (`make_register.py`: issues open/fixed/dropped, a fix missing from the checkout, problems of
     unread cycles, refused rows by class and by weight, a problem of an unknown issue, a date added to the classes):
     exit 0 and the bytes identical (`78e6e877563634545514acd2caf293e2b68407685af919e63d1b6388a830cc84`);
   - a results directory that holds a directory named `.count-2026-11-19.md.tmp`: exit 2 and the same line
     `Error: cannot write count-2026-11-19.md in the directory of the key `audit_results` under `the-way`: Permission denied`;
   - a key that the locations file lacks: exit 2 and the same `Error:` line.
   - `run_cases.sh before|after` runs all four; every stdout, stderr and exit file compared equal with `cmp`.
2. `analyse` on 3000 seeded random inputs (`diff_analyse.py`: cycles with later copies and shared commits, pins that do
   not resolve, issues of the three fates, refused rows, problems of unread cycles; a stub for the ancestry), run twice,
   `today` 2026-11-19 and 2026-03-05 (to reach "its earliest copy is dated after the day of the run"): the seven
   tables of the `Analysis` of the base code and of the new code are byte-identical in both runs (the first run reached
   1811 open rows, 1771 fixed rows, 1906 inputs with unknown values).
3. `astcmp.py`: 101 top-level functions, classes and constants of the base `audit_count.py` found in the three new files
   with an identical syntax tree; the only differences are `__all__`, `analyse` and `render`, the two divided; nothing
   of the base is missing.
4. The test suite of `process-audit` (276 tests, which run the script as a process on temporary repositories) passes.

Trust-boundary comparison (`audit_count.py`): the crafted input above (a register with refused rows, an unresolvable
fix, a record of no cycle, a failing write, a missing key) gives the same verdict, exit code and message before and
after. The functions that read the untrusted files were not touched by this slice (they stand in `record_reading.py`
and `problem_register.py` since Slice 15).

Weakest point checked: the division of `analyse`, since the order in which values are appended to `unknown` decides the
order of the rows of *Unknown values* and the early returns of `waiting_days` replace an `if/elif` chain; check 2 compares the
list `unknown` (with its order) and `held` for 3000 inputs, and check 1 the bytes of the whole result.

Not checked: a before/after comparison of a repository that holds a commit adding the records of several cycles, other than through the 3000 random
inputs and the test suite; the walkthrough (`walkthrough.md`): the change alters no behaviour a user sees, the bytes
of the result and every message and exit code are shown unchanged above.

## Adaptations (slice.md, "when the plan and the code disagree")

1. The plan puts `count_rows`, `cost_rows` and `money` in `audit_report.py` ("from `count_rows` at the base to `render`
   and `write`"). `process_versions` (`version_analysis.py`) calls `count_rows` and `cost_rows`, and `cost_rows` calls `money`,
   while `audit_report.py` imports from `version_analysis.py` (the paths of the scripts, `Versions`, `Analysis`,
   `unknown_rows`), and a module must not import another that imports it. So `count_rows`, `cost_rows`, `money` and
   `MONEY` stand in `version_analysis.py`, and `audit_report.py` imports `money`. Small mismatch; the goal, the sizes and
   the behaviour are as the slice gives. Cost if wrong: Slice 17 or a reviewer who counts by the plan's list finds three names
   in the other module.
2. Names the plan did not place: `committed_date` (used by `read_repository` in `audit_count.py` and by
   `process_versions`) stands in `version_analysis.py` and `audit_count.py` imports it; `STAGES_FILE`, `WORKING_NAME`,
   `WAITING_NAME`, `STAGES_VALUES` (used by `fill` and by `TOOL_GROUPS`/`withdraw_values`) stand in `version_analysis.py` with
   `TOOL_GROUPS` and are imported by `audit_count.py`; `RESULTS_ENTRY` (used by `write` and by `main`) stands in
   `audit_report.py` and is imported by `audit_count.py`. The headers of the tables (`COST_HEADER`, `COUNT_HEADER`,
   `MECHANISM_HEADER`, `GATE_HEADER`, `UNKNOWN_HEADER`, `SERIES_COST`, `SERIES_COUNT`) and `SHARE` stand in `audit_report.py`,
   the only module that uses them.

## Choices (with the way rejected)

- Division of `analyse` by the work it does (placing the problems, refused rows, rows per cycle, one row per kind of
  issue), each part named for what it returns. Rejected: dividing at the two halves of the per-issue loop only, which
  leaves a part of 100 lines with no name of its own. Cost if wrong: a reviewer finds a part too coarse.
- `waiting_days` uses early returns and a small helper `unknown_waiting` for the four places that append the same
  kind of line to `unknown` and return `unknown`; the reasons and their order are those of the base. Rejected: copying the
  four `unknown.append(...)` blocks, which keeps `waiting_days` near 60 lines and repeats the block.
- `render` divided by section; each function returns the lines of its section, with the blank lines that
  stood between the sections in the base, so the join gives the same text.

## Reaches beyond the dispatch

None beyond the files the handoff names, apart from `process-audit/record_reading.py` and `process-audit/problem_register.py`
(read for the names the new modules import and their style; not changed) and `process-audit/test_audit_count.py` (searched for the
names it reaches as `audit_count.<name>`, and its test of the checkout without a repository key, which copies every
`process-audit/*.py` that is not a test, so the new modules need no change there). I read `task-cycle/change/slice.md` and
`.ai/rules/git.md` and `scripts.md` of the author's rules, as the instructions require.

## Unread material

- `foundations/decisions.md:8400-8537` WAY-339 read whole; `6616-6653` WAY-365, `2566-2595` WAY-48, WAY-385 read whole.
- `foundations/invariants.md`: `function-and-file-size` (458-467), `audit-series-script-paths` (408-417) and
  `cross-part-imports` (358-367) read whole.
- `foundations/part_map.md:125-136` read; `262-269` (External context) not read: the slice changes no exchange with the external
  context and the part map does not change.
- `task.md:32-32`, `task.md:108-108`, the plan and the frozen task: not read; the slice's text in the handoff was enough
  (the handoff names them, so this is stated).
- `foundations/decisions.md` WAY-382 and the other foundation entries F1, F3-F9: not read whole; the checks of the slice
  (format, lint, sizes) were run as the handoff gives.
- `guidelines/coding.md`, `coding-measuring-report.md`, `coding-shared-module.md`, `process-audit/stage_pricing.py:1-7`,
  `process-audit/test_audit_series_scripts.py`, `agent-instructions/test_size_invariant.py`: read whole.

## Searches not found or unclear

- None unclear. `TURN_SUFFIX` in `audit_count.py` is defined and used nowhere in the file (it was so at the base, left from the
  earlier slices); I did not remove it, outside this slice's *Change*.
- Note: the test of `cross-part-imports` sees only files git tracks, so a slice that adds a module fails
  `elements/part-map` until the module is committed.

## Working copies

- `.runs/executor-16/` (a clone of the worktree at the base `.runs/executor-16/clone` for the before/after runs, the
  results directories, the locations files, the build script and the scratch outputs): removed before return, as shown
  below. Kept in `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-16-checks/`: `astcmp.py`,
  `diff_analyse.py`, `size_check.py`, `make_register.py`, `run_cases.sh` and the two gate outputs. (They read paths under
  `.runs/executor-16/` and need that directory rebuilt to run again.)
- The results directories had to stand outside the repository the audit reads (the command refuses a results
  directory inside it), so the audit read the clone and wrote to a sibling directory in `.runs/executor-16/`.
