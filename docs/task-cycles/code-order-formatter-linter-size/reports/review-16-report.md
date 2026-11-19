PASS a30a04ff540657346094bf51e195003d2a442a9d

# Review of slice 16 (range `95316c25..a30a04ff`, one commit)

`git rev-parse HEAD` in the worktree is `a30a04ff540657346094bf51e195003d2a442a9d`, the head given.

## Findings

Blocking: 0. Minor: 2. Out of scope: 0.

### Critical

none

### Important

none

### Minor

1. **The comment over `__all__` of `process-audit/audit_count.py` is untrue for one name.**
   Place: `process-audit/audit_count.py:425-427` (the comment) and `:435` (`"Ancestry"`).
   The comment reads "The names below are no longer used in this file; they are imported so that the tests
   reach them as `audit_count.<name>`". `Ancestry` is used in the file: `process-audit/audit_count.py:849`,
   `ancestry = Ancestry(Git(the_way))`. The other 13 names of the list are used nowhere else in the file (checked
   by `ast`: the unused imports are exactly those 13 names). Effect: a reader who trusts the comment may drop
   `Ancestry` from the import and break `main`; or, trusting the list, take the import for dead. `Ancestry` need
   not stand in `__all__` at all, since the file uses it, so ruff would not report it.
   Evidence: `grep -n "\bAncestry\b" process-audit/audit_count.py` gives lines 404, 435 and 849.

2. **Foundation text still says `process-audit/audit_count.py` reads the history of the series scripts.**
   Place: `foundations/invariants.md:410` (`audit-series-script-paths`) and the docstring of
   `process-audit/test_audit_series_scripts.py:1-8` ("The reader, `audit_count.py`, is imported").
   After this slice the constants that name those paths (`COST_SCRIPT`, `MEASURES_SCRIPT`, `GATE_SCRIPT`,
   `GATE_TEST_RUNNER`, `TOOL_GROUPS`) and the `git diff --quiet` reading stand in
   `process-audit/version_analysis.py`; the test still reaches them as `audit_count.<name>` through `__all__`,
   which is what the slice asks for until Slice 17. The invariant's requirement (each path is a file git
   tracks) is unchanged and its test passes, so nothing is wrong now; the sentence names a file that no longer
   holds the reading. Whether Slice 17 or a later one rewrites it is outside what I was given (the plan and the
   record are not mine to read); I name it so that it does not go unnoticed. The slice's *Change* names three
   `.py` files and no foundation file, so it is not a miss of this slice.

### Declined to judge

- `TURN_SUFFIX` (`process-audit/audit_count.py:462`) is defined and used nowhere in the file. It stood so at the
  base (the executor names it); it is not in the range and outside the slice's *Change*.
- `agent-instructions/test_size_invariant.py` still states 80 lines and 1000 lines in its docstring (the
  thresholds are changed by another point of the task's *To do*); outside this slice.
- The two `Questions carried to cycle` of the frozen task that I read (task.md:108, the kind of the modules moved
  out and whether the tests import from the new place) are settled by the slice itself (modules are of the kind
  `shared-module`; tests unchanged, names reached through `__all__`); I did not judge the answer as a choice of the task.

## What I checked, against the slice

Goal, line by line.

- **Moved without change of behaviour.** My own comparison of syntax trees (`astcmp.py` in
  `review-16-checks/`): of the base `audit_count.py`'s top-level functions, classes and constants, every one
  stands in the three new files with an identical tree (names compared and `ast.dump`), save `__all__`,
  `analyse` and `render`, the three the slice changes; none is missing; no name stands twice except
  `display` (one line, `remarks_check.display`, in each module that uses it). The new names are the divided parts
  (`Placed`, `cycles_by_record`, `place_problems`, `count_refused_rows`, `problems_by_cycle`, `fixed_issue_row`,
  `unknown_waiting`, `waiting_days`, `open_issue_row`, `dropped_issue_row`, `intro_lines`, `cycles_lines`,
  `cost_lines`, `measures_and_versions_lines`, `problems_by_cycle_lines`, `fixed_issues_lines`,
  `open_issues_lines`, `dropped_issues_lines`, `occurrence_cost_lines`, `unknown_values_lines`).
  A line-multiset comparison of base against the three new files found every comment and every string line of the
  base again; what is missing are only the lines of the two divided functions that were re-cut (brackets,
  `days = ...`, `lines += [`), and the old comment over `__all__`.
- **`analyse` divided (F2).** I read the base function and the new `analyse` with its eight helpers whole
  (`version_analysis.py:225-523`). Order of the `unknown.append` calls, the early returns of `waiting_days` against
  the base's `if / elif` chain (refused, then no members, then an unread cycle, then an unknown date, then a
  negative wait), the order of changes of `uncounted` (problems first, then refused rows), and the ordering of
  `dict.fromkeys` over `unknown` and `held` are those of the base. The 3000-input differential (below) agrees.
  Largest function of `version_analysis.py`: `mechanism_rows` 50 lines.
- **`render` divided (F2).** `render` (`audit_report.py:520`) joins the lines of ten functions, one per section; the
  blank lines that stood between sections of the base are at the start of the later section, or at the end of
  `measures_and_versions_lines`. The bytes of the result are identical on three inputs (below). Largest function of
  `audit_report.py`: `versions_lines` 58 lines.
- **Sizes.** `audit_count.py` 897, `version_analysis.py` 1056, `audit_report.py` 552, `record_reading.py` 1149,
  `problem_register.py` 358, `stage_pricing.py` 167, `record_items.py` 350 lines; no function over 110 in any of them
  (largest `read_prices` 81).
- **No import of `audit_count.py`.** Neither new module names it except in its description; the direction is
  `audit_count` to `audit_report` to `version_analysis` to `record_reading`, `problem_register`, `stage_pricing`.
  The test of `cross-part-imports` passes (`elements/part-map`).
- **`__all__`, no `noqa` for it, tests unchanged.** 14 names are listed; each name the tests reach as
  `audit_count.<name>` (my own search: `Ancestry`, `COST_SCRIPTS`, `COUNT_PATHS`, `Cycle`, `Git`, `GitError`,
  `Prices`, `Register`, `Version`, `cost_boundary`, `count_boundary`, `fill`, `instrument_series`,
  `read_contradiction`, `remarks_check`; `COST_SCRIPT`, `MEASURES_SCRIPT`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`,
  `TOOL_GROUPS` in `test_audit_series_scripts.py`) resolves. The range touches no test. The new `noqa: E402`
  comments are the ones the base already put on every import after `sys.path`; `ruff check --ignore-noqa` passes on
  the three files, so none turns a blocking rule off. The range adds no other `noqa`.
- **Descriptions.** Each module's opening paragraph says what it holds, that it was moved out of
  `audit_count.py`, that it is imported and never run, and that it runs nothing when imported.
- **Trust boundary and the part map.** The functions that take in the user's files stand in `record_reading.py`,
  `problem_register.py` and `record_items.py` (Slice 15, listed in the part map) and the main `audit_count.py` (still
  a boundary, still holding `main`, the locations file and the results directory); `version_analysis.py` takes
  parsed values (`measure_number` reads what `read_measures` kept) and runs git on a checkout (git is trusted in the
  part map's external context) and `audit_report.py` only writes. Neither reads input from outside the product, so
  the part map does not change (WAY-48); the range does not touch `foundations/part_map.md`.
- **No operation that cannot be undone.** The command only writes the two result files into the directory of the
  key; the slice touches no deletion or rewrite.
- **Test that passes for the code's own value.** The tests are not changed; they run the script as a process on
  made repositories, so they reach the new modules. No code branch or value exists to satisfy a test.
- **Executor's report.** Its claims about files, sizes, checks and the adaptation (three names `count_rows`,
  `cost_rows`, `money` stand in `version_analysis.py` because `process_versions` calls them and `audit_report`
  imports that module) are true; the adaptation is the only one that keeps "a module never imports `audit_count.py`" and
  has no cycle between the two new modules. It is a place the slice text did not give, not a fault.

## Checks I ran (command, exit code)

All from the worktree root `the worktree's root`. `<ruff>` is
`the Ruff of the quality environment of the main checkout`.

| Check | Command | Exit |
|---|---|---|
| format | `<ruff> format --check --no-cache --config ruff.toml process-audit/audit_count.py process-audit/version_analysis.py process-audit/audit_report.py` | 0 ("3 files already formatted") |
| lint | `<ruff> check --no-cache --config ruff.toml --ignore-noqa` on the same three files | 0 |
| tests of the part | `python -B gate/run_tests.py process-audit` (276 tests, 394 s; copy of the output `review-16-checks/gate-pa.txt`) | 0 |
| tests of the part map | `python -B gate/run_tests.py elements/part-map` (40 tests; `review-16-checks/gate-pm.txt`) | 0 |
| sizes | `python -B .runs/task-cycles/code-order-formatter-linter-size/reports/executor-16-checks/size_check.py` (calls `function_sizes` and `file_lines` of `agent-instructions/test_size_invariant.py`, against 110 and 1200; I read the script before I ran it: it only reads and prints) | 0, "violations 0" |
| import runs nothing | `python -B -c "import sys; sys.path.insert(0, 'process-audit'); import <module>" < /dev/null` for `version_analysis` and `audit_report` | 0 and 0; stdout 0 bytes, stderr 0 bytes each; `audit_count` not in `sys.modules` after importing both |
| syntax trees | `python -B .runs/review-16/astcmp.py` (my script, copy in `review-16-checks/astcmp.py`) | 0; only `__all__`, `analyse`, `render` differ |
| names the tests reach | `python -B .runs/review-16/names.py` (copy in `review-16-checks/names.py`) | 0; every name resolves (the one "MISSING py" is the text `audit_count.py` in a string of a test, no name) |
| whole command, real history | the base worktree (made by me at `95316c25`) as the repository, the template register, `--today 2026-11-19`: base script against head script, 118 cycles | 0 and 0; stdout identical; `count-2026-11-19.md` and `count-latest.md` identical, 265440 bytes, sha256 `c6afdf4a...e2eb` (the executor's figure) |
| whole command, crafted register | `make_register.py` (adapted copy of the executor's: issues open, fixed and dropped, a fix absent from the checkout, problems of unread cycles, refused rows by class and by weight, a problem of an unknown issue, a late class), base script against head script, run on `--today 2026-11-19` and on `--today 2020-01-01` (to reach "its earliest copy is dated after the day of the run") | 0 and 0 each; result files byte-identical |
| crafted input at the boundary (`audit_count.py`) | the same command, base against head, with: a results directory that holds a directory `.count-2026-11-19.md.tmp`; a repository key the locations file lacks; a locations file without the key `problem_register`; `--today garbage`; `--prices nosuch.md` | exit 2 each, stdout, stderr and exit code identical (`cmp`); messages, e.g. `Error: cannot write count-2026-11-19.md in the directory of the key `audit_results` under `the-way`: Permission denied` |
| `analyse`, 3000 seeded inputs | executor's `diff_analyse.py` (read before; it builds cycles, a register and a stub of the ancestry and dumps the seven tables of `Analysis`), run against the base `process-audit/` and the head one, `today` 2026-03-05 and (my copy `diff_analyse2.py`) 2026-11-19 | 0; `cmp` of the dumps equal in both runs (1811 open rows, 1771 fixed rows, 1958 and 1906 inputs with unknown values) |

I did not run the full gate, and not `agent-instructions` (the size test there is an expected failure until a later point of the
task).

One slip of mine, fixed: to run the second day of the differential I first edited the executor's
`executor-16-checks/diff_analyse.py` in place with `sed -i` (date 2026-03-05 to 2026-11-19), and at once restored the
line (`today = date(2026, 3, 5)`, line 68, confirmed). The file's content is as it was; its modification time is
13:42:54 on 2026-11-19. The file lies under the ignored `.runs/`; `git status` of the worktree is clean.

## Reaches beyond the dispatch

- `foundations/decisions.md:10784-10838` WAY-385 (F2) and the other six entries of the handoff by their ranges: as the
  handoff names them; read whole.
- `foundations/decisions.md` search for `audit_count` (lines 11159, 11394-11402) and `foundations/invariants.md:410`,
  `guidelines/testing.md`, `process-audit/SKILL.md`, to see whether a text names where moved code stands (finding
  Minor 2). Those lines of the settlement table (WAY-342 and others) name `audit_count.py` as the place of a rule; I did not
  judge them (they are the record of earlier settlements, not claims of this slice).
- `process-audit/test_audit_series_scripts.py` read whole (the handoff names it); `process-audit/test_audit_count.py`
  searched for `audit_count.<name>` and `import audit_count` only.
- `process-audit/record_reading.py` and `problem_register.py`: `grep` for `sys.path`, to see whether inserting the
  directory of `task-cycle` at import is the practice of the sibling modules (it is, in both and in `record_items.py`).
- `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-16-checks/` (`size_check.py`,
  `diff_analyse.py`, `make_register.py`), the executor's scripts that I read and reused.

## Working copies

- `.runs/review-16/` held a git worktree of `95316c25` (`.runs/review-16/base`), the base copy of
  `audit_count.py`, the locations files, the registers, the result directories of the runs and my scripts. I removed
  the worktree with `git worktree remove --force` and `git worktree prune` (the list of worktrees afterwards holds
  the four that stood before), and the directory with `rm -rf`. Kept beside this report in
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-16-checks/`: `astcmp.py`, `names.py`,
  `make_register.py`, `diff_analyse2.py`, `cases.sh`, and the outputs `gate-pa.txt` and `gate-pm.txt`. The scripts
  read paths under `.runs/review-16/`, which must be rebuilt to run them again. Nothing remains.

## Unread material

- `.runs/task-cycles/code-order-formatter-linter-size/task.md`: read lines 30-34 (*To do*, point 2 and the lines around it)
  and 106-110 (*Questions carried to cycle*); of the points of *To do* I read points 2 to 6 where they stood in
  these ranges; not read whole, and the plan (`plan.md`) not read: the handoff names only these two passages and says the
  record is not mine.
- `foundations/part_map.md:262-269` (External context) read; `:125-136` read.
- F2 = WAY-385 read whole; WAY-365, WAY-48, WAY-339, `function-and-file-size`, `audit-series-script-paths`,
  `cross-part-imports` read whole by their ranges. F1, F3-F9 (the other foundation entries listed in "The
  foundation entries written earlier") not read: the handoff gives them for the slices that wrote them, and this
  slice names F2 only.
- `guidelines/coding.md`, `coding-measuring-report.md`, `coding-shared-module.md`, `process-audit/stage_pricing.py:1-7`,
  `process-audit/test_audit_series_scripts.py`, `agent-instructions/test_size_invariant.py`: the first five read
  whole; `test_size_invariant.py` read only in its opening (lines 1-5 and the functions I called through
  `size_check.py`, not its tests).
- The moved code was verified by syntax-tree comparison and by differential runs, not read line by line outside
  `analyse`, `render` and the changed headers; the rest of the 1100 lines of `version_analysis.py` was read for structure only.

## Searches not found or unclear

- none that blocks. Unclear: the handoff's "Answers of step 4" asks for crafted input at the boundary files this
  range touches; the range touches one (`audit_count.py`), and the functions that read the files from outside
  stand in `record_reading.py`, `problem_register.py` and `record_items.py`, untouched here. I therefore crafted input
  at the command's own surface (locations file, key, results directory, option values, register rows) and not at the
  record readers, which this range does not reach.
