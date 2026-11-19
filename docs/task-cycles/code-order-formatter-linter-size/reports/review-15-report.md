PASS 95316c256de20d7e7a272a27246ecd244e14c4d5

# Review of slice 15 (range `efc2f090..95316c25`, head confirmed by `git rev-parse HEAD`)

Blocking findings: 0. Minor findings: 2. Out-of-scope findings: 0.

## Changed files (`git diff --numstat`, and lines of the file at head)

- `process-audit/audit_count.py` — +52 / -1417, 3606 -> 2241 lines
- `process-audit/problem_register.py` — new, 358 lines
- `process-audit/record_reading.py` — new, 1149 lines
- `foundations/part_map.md` — +2 (the two modules among the *Trust boundary* files of `process-audit`)

## Findings

### Critical

none

### Important

none

### Minor

1. `process-audit/record_reading.py:1-12` and `process-audit/problem_register.py:19` — the base that both modules need
   (`AuditCountError`, `GitError`, `Git`, `table_cells`, `is_separator`, `THE_WAY`, `MAX_BYTES`) lies in
   `record_reading.py`, so the register module depends on the reader of records, and a module named for the reading of
   a cycle's record holds git and the cells of a table. The slice asks only that what both need moves into a module
   and that no module imports `audit_count.py`; that holds (grep of both new files: the only mentions of
   `audit_count` are in their descriptions). The executor named the choice and its cost (choice 3). The cost is
   structural and lies below the thresholds, so Minor (WAY-363). Evidence: `problem_register.py:19`
   `from record_reading import MAX_BYTES, THE_WAY, AuditCountError, is_separator, table_cells`.
2. `process-audit/audit_count.py:613` (`read_prices`, 81 lines) and `:696`ff (`fill`, `read_repository`) stay in
   `audit_count.py`, while the slice's Goal gives the moved span as "from `header_fields` to `read_gate` at the base"
   and `read_prices` lay inside that span at the base (`efc2f090:process-audit/audit_count.py:976`). The executor's
   reasons are sound and checked: with `read_prices` the file would reach about 1230 lines (1149 + 81), over the 1200
   of WAY-385; `fill` and `read_repository` are not needed by the cut, and the slice lets them move only "where the
   cut needs them". The consequence is that `record_reading.py` stands 51 lines under the file threshold, so a later
   slice that moves `fill`, `read_prices` or other reading into it has no room and has to place it elsewhere.
   Minor: the slice's text and the code differ, the difference is named in the executor's report, and nothing in
   behaviour depends on it.

## Verified claims of the executor

- Node-for-node move: my own script (`reports/review-15-checks/astcmp.py`) compares `ast.dump` of every top-level
  function, class and constant of the old `audit_count.py` with the three files at head. Missing: none. Different:
  only `read_gate`. New names: `gate_header`, `gate_table_runs`, `add_gate_run`, `__all__`. Defined in more than one
  file: `display` only, the one-line alias `remarks_check.display` (as before). Distribution: 103 names stay in
  `audit_count.py`, 84 in `record_reading.py`, 26 in `problem_register.py`.
- The top-level statements other than definitions: the same set remains in `audit_count.py` (arguments, imports,
  `sys.path.insert`, `if __name__ == "__main__": sys.exit(main())`); the new modules hold imports and the
  `sys.path.insert` for `remarks_check`, and no call that runs anything.
- `read_gate` divided: read whole against the old (`efc2f090`), line by line. `gate_header` returns the index and the
  cells or None, with the missing fields put on the cycle in the same order; `gate_table_runs` holds the loop, the
  limits and the reasons for the rows after the table and the cut directories; `add_gate_run` holds one run; `reasons`
  is filled in the same order (table reasons, then each run's) and `dict.fromkeys(reasons)` is applied last as
  before. Each part has a name of its own; `read_gate` is 17 lines, the largest function of the new files is
  `gate_table_runs` with 76 lines.
- Differential on crafted input, independent of the executor's: 4000 generated `gate_times.md` texts (missing and
  reversed columns, fenced tables, rows of the wrong width, a text of None, bad cells, rows after the table) plus three
  hand-made cases that reach the limit of 500 runs, the limit of 50 directories, and a doubled directory with a row
  after the table. Old `read_gate` (loaded from `efc2f090`) and new compared on `unknown`, `missing`, `missing_in`,
  `gate_runs` and `gate_timed`: 0 different (`reports/review-15-checks/diffgate.py`; the generator reached runs in
  2160, a missing field in 1597, a wide row in 1018 and a row after the table in 478 of the 4000 texts).
- The names the tests reach as `audit_count.<name>` (20 listed in the slice, plus `read_contradiction`): all resolve
  (`reports/review-15-checks/names.py`: none missing). `__all__` is `["read_contradiction"]`, the one name
  `audit_count.py` no longer uses (its only user, `process_questions`, moved); every other listed name is used by
  `audit_count.py` itself, which `ruff check` confirms (F401 clear). No `noqa` serves the re-export; the `# noqa: E402`
  on the imports is the pattern of the file's other imports and `--ignore-noqa` run is clean. The tests do not patch
  module names (`grep patch|setattr|monkey`: none), so a name moved from the module a test reaches cannot silently
  stop a patch.
- Tests unchanged: the range holds no test file.
- Descriptions: both new modules open with what they hold, that they were moved out of `audit_count.py`, that they
  are imported, never run, run nothing when imported, and "Standard library only", as `stage_pricing.py:1-7` does.
  The description of `audit_count.py` is untouched by the diff.
- Part map: both modules added under *Trust boundary* of `process-audit`; `foundation_check.py` exits 0 and
  `elements/part-map` passes. Both read what comes from outside the product (the user's register, the records of
  cycles in the history of a user's repository), as WAY-48 requires.
- The mentions of `process-audit/audit_count.py` in foundation tables (WAY-342, 343, 346, 348, 352, the invariant of the
  series paths) name where the rule's description stands; `audit_count.py` keeps its whole description, so they stay
  true.

## Trust boundary (step 4 of the cycle)

The boundary files this range touches are `audit_count.py` (named in the part map) and the two new modules. Same
verdict, exit code and message before and after: the moved code is AST-identical, so crafted input reaches the same
code; the one rewritten function, `read_gate`, gave identical results on the crafted texts above; the suite drives
the command end to end (exit 0, 1 and 2, the `Error:` lines, the bytes of the result, the symbolic links that leave a
record, the register's refused tables) and passes. No operation that cannot be undone is held by the range.

## Declined to judge

- `audit_count.py` stays over the thresholds (2241 lines; `analyse` 219 lines and `render` 206 lines): the later
  slices of the plan divide it; this slice's goal is the two moves and `read_gate`.
- `agent-instructions/test_size_invariant.py` still counts with 80 and 1000, and the invariant `function-and-file-size`
  stays `Violated: yes`: not in this slice's change list.

## Checks (command, exit code)

Run from the worktree root; `<ruff>` is `the Ruff of the quality environment of the main checkout`.

- `python -B gate/run_tests.py process-audit` — 276 tests, 415 s, exit 0 (output kept in
  `reports/review-15-checks/tests_process_audit.txt`).
- `python -B gate/run_tests.py elements/part-map` — 40 tests, exit 0.
- `<ruff> format --check --config ruff.toml process-audit/audit_count.py process-audit/problem_register.py process-audit/record_reading.py` — exit 0 (3 files already formatted).
- `<ruff> check --config ruff.toml --ignore-noqa <the same three files>` — exit 0; the same without `--ignore-noqa` — exit 0.
- `python -B elements/common/foundation_check.py` — "0 errors", exit 0.
- `python -I -B .runs/review-15/size.py` (`function_sizes` and `file_lines` of `agent-instructions/test_size_invariant.py`
  on the modules, limits 110 and 1200) — exit 0: `problem_register.py` 358 lines, largest `read_register` 93;
  `record_reading.py` 1149 lines, largest `gate_table_runs` 76; no function over 110 and no file over 1200 in the two
  modules (`audit_count.py`: 2241 lines, `analyse` 219 and `render` 206, outside this slice).
- New interpreter, stdin an empty pipe: `: | python -I -B -c "import sys; sys.path.insert(0, 'process-audit'); import <module>"`
  for `problem_register` and `record_reading` — exit 0 each, stdout and stderr 0 bytes each.
- `python -I -B .runs/review-15/astcmp.py` — exit 0, result above.
- `python -I -B .runs/review-15/diffgate.py` — exit 0, 4000 cases, 0 different.
- `python -I -B .runs/review-15/names.py` — exit 0, no name missing.
- Not run: the full gate (the handoff forbids it); `agent-instructions` directory (not in the slice's checks).
- `git status --short` after the runs: clean.

## Reaches beyond the handoff

- `foundations/decisions.md:10784-10830` WAY-385, whole entry, since F2 is named without a range, to read the thresholds.
- `foundations/decisions.md:11370-11410` (the table of where the rules of decisions stand, WAY-342 to WAY-366) and a
  grep of `audit_count.py` and of the moved names in non-`.py` files: to see whether the move made a statement of the
  foundation or a document false. It did not.
- `agent-instructions/test_size_invariant.py:1-150`, whole to line 150, to use its counting functions.
- `process-audit/test_audit_count.py:4150-4235`, to see how the test of the checkout without a repository key copies the
  modules (it globs every non-test module of `process-audit/`, so the new files need no change of the test).
- `foundations/invariants.md:458-467, 548-557, 358-367` (the current ranges the handoff gives), and
  `foundations/invariants.md:498-506` (`shared-module-import-runs-nothing`), to compare the import check with it.

## Unread material

- `.runs/task-cycles/code-order-formatter-linter-size/task.md:32` and `:108` were read (the two lines the slice names).
  The passages of the task outside them stayed unread.
- `foundations/decisions.md` WAY-365 and WAY-48: read whole at the current ranges
  (`6615-6651`, `2565-2593`; the handoff's ranges `6616-6653` and `2566-2595` differ by one line and
  I read the entry as it stands). `foundations/invariants.md`: `function-and-file-size`,
  `audit-count-refuses-record-links` and `cross-part-imports` read whole at the current ranges
  (`458-467`, `548-557`, `358-367`); the invariant `script-imports` stayed UNREAD (the range `126-134` of
  the slice's Read holds other entries in this file and I did not look further). `foundations/part_map.md`
  `125-140` read; `262-269` (External context) read only as far as its first lines.
- `guidelines/coding.md`, `coding-measuring-report.md`, `coding-shared-module.md`: read whole.
- `process-audit/test_audit_count.py:2345-2366`, `3536-3616`, `3780-3800`, `4060-4140`, `4340-4350` and
  `process-audit/test_audit_series_scripts.py`: not opened by range; read by grep for `audit_count.<name>`, for
  patching, and `test_audit_count.py:4150-4235`; the suite as a whole was run.
- `process-audit/record_reading.py` and `problem_register.py`: read the descriptions and imports, the division of
  `read_gate`, and the constants block to line 170; the rest compared by `ast.dump` with the old file instead of
  being read line by line.
- `audit_count.py`: read whole the description (1-336), the imports and the constants (338-490) and the diff of the
  range; the body after line 490 compared by `ast.dump`.
- `.runs/task-cycles/code-order-formatter-linter-size/plan.md` (not named for me): unread.

## Searches not found or unclear

- Not found: the invariant `script-imports` at the range the slice's Read gives (`126-134`); that range
  holds other entries. Unclear: the ranges of the invariants in the slice's Read (`438-446`, `528-536`,
  `348-356`) are shifted by 20 lines against the current ones the handoff also gives; I read the current ones.

## Working copies

- `.runs/review-15/` (the old `audit_count.py` and its siblings from `efc2f090` in `old/` and `oldroot/`, the
  scripts, the test output, the import outputs): removed before return. Kept in
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-15-checks/`: `astcmp.py`, `diffgate.py`
  (needs the old copy at `.runs/review-15/oldroot/`, rebuilt by copying `efc2f090:process-audit/audit_count.py`,
  `stage_pricing.py`, `record_items.py` to `oldroot/process-audit/` and `task-cycle/remarks_check.py` to
  `oldroot/task-cycle/`), `size.py`, `names.py`, `tests_process_audit.txt`. No git worktree was made.
