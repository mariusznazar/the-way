# Report — executor-15, slice 15 (the register of problems and the reading of records moved out of the audit's command)

## Status

`done with concerns` — the slice's checks all pass; the concerns are two places where the slice's text and the code could
not both hold (read_repository and fill stay; read_prices stays), named under *Choices* below.

## Commits (range `efc2f090..HEAD`)

- `2dbccee8` Move the register of problems into problem_register.py and the reading of a cycle's record into
  record_reading.py, dividing read_gate into the header, the runs of the table and one run
- `95316c25` Name problem_register.py and record_reading.py among the trust boundary files of process-audit

## Files changed (added / removed lines, `git diff --stat efc2f090..HEAD`)

- `process-audit/audit_count.py` — 51 added, 1418 removed (3606 -> 2239 lines)
- `process-audit/problem_register.py` — new, 358 lines
- `process-audit/record_reading.py` — new, 1149 lines
- `foundations/part_map.md` — 2 added (the two modules among the *Trust boundary* files of `process-audit`)

## What moved

- `problem_register.py`: `Problem` to `read_register` of the base with the constants only it used (`REGISTER_TABLES`,
  `LEVELS`, `COST_LEVELS`, `FATES`, `NAME`, ...), plus `FIXED`, `NONE`, `DATE_TEXT`, `FULL_HASH`, `SHORT_HASH` and
  `COST_LEVELS`/`LEVELS` which `audit_count.py` also uses and now imports.
- `record_reading.py`: `GateRun`, `Cycle`, `Read`; `header_fields` to `read_gate` of the base except `read_prices`; the
  constants only that code used, and `MEASURES_FILE`, `GATE_FILE`, `ABSENCE_CAUSES`, `MEASURE_LABELS`, `SHARE_LABEL`,
  `RECORDS`, `THE_WAY`, `MAX_BYTES` which `audit_count.py` also uses and now imports. It also holds what both new modules
  need and neither may take from `audit_count.py`: `AuditCountError`, `GitError`, `Git`, `table_cells`, `is_separator`
  (`problem_register.py` imports `AuditCountError`, `MAX_BYTES`, `THE_WAY`, `table_cells`, `is_separator` from it).
- No module imports `audit_count.py` (grep of both new files: no match).
- `read_gate` (153 lines) is now `read_gate` (17 lines) + `gate_header` (the table and its six columns, missing fields),
  `gate_table_runs` (the rows into runs, the limits and their reasons; 76 lines, the largest function of the new files)
  and `add_gate_run` (one run as the cells of the table of runs and as numbers). `reasons` is filled in the same order as
  before (scan, rows after the table, directories cut, then each run's cells).
- `audit_count.py` imports what it uses from both. `__all__ = ["read_contradiction"]` keeps `audit_count.read_contradiction`
  reachable, since `process_questions` (its only user) moved; no `noqa` for it. The other names the tests reach
  (`Git`, `GitError`, `Cycle`, `fill`, `Prices`, `Register`, `Version`, `Ancestry`, `cost_boundary`, `count_boundary`,
  `instrument_series`, `remarks_check`, the `*_SCRIPT*`, `COUNT_PATHS`, `TOOL_GROUPS`) are used by `audit_count.py`
  itself, so they need no `__all__` entry; all 20 names the three test files reach resolve (`hasattr` run).
- The description of `audit_count.py` (its docstring) is untouched. Each new module opens with a description that says what
  it holds, that it was moved out of `audit_count.py`, that it is imported, never run, and runs nothing when imported.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Tests of the part | `python -B gate/run_tests.py process-audit` (276 tests, 488 s; output in `reports/executor-15-checks/test_process_audit_final.txt`); an earlier run on the same code before two comment-only edits also passed (276 tests, 466 s) | 0 |
| Tests of part-map | `python -B gate/run_tests.py elements/part-map` (40 tests) | 0 |
| Formatter | `<ruff> format --check --config ruff.toml process-audit/audit_count.py process-audit/problem_register.py process-audit/record_reading.py` | 0 |
| Linter, comments ignored | `<ruff> check --config ruff.toml --ignore-noqa <same three files>` | 0 |
| Foundation check | `python -B elements/common/foundation_check.py` ("0 errors"; run after the commits, since it needs the new files tracked — before the commits it exited 1 on the two new part-map patterns only) | 0 |
| Size | `function_sizes`/`file_lines` of `agent-instructions/test_size_invariant.py` on the two modules: `record_reading.py` 1149 lines, largest function `gate_table_runs` 76; `problem_register.py` 358 lines, largest `read_register` 93 | no function over 110, no file over 1200 |
| Import runs nothing | new interpreter `python -I -B -c "import sys; sys.path.insert(0, 'process-audit'); import <module>"`, stdin an open empty pipe, as `relation-model/test_fingerprint.py` does it (`reports/executor-15-checks/import_check.py`) | 0 for each, stdout and stderr empty |

The full gate was not run (WAY-160). The tests were not changed.

## Trust boundary: same verdict, exit code, message

- Every top-level function, class and constant of the base is found again, node for node (`ast.dump`), in one of the three
  files, except `read_gate` and the three new functions (`reports/executor-15-checks/astcmp.py`): nothing else changed a
  token. `display` is the same one-line alias in each of the three files.
- `read_gate`: the old function (loaded from `efc2f090`) and the new one were run on 3000 generated `gate_times.md` texts
  (missing columns, reversed columns, fenced tables, rows of the wrong width, 520 runs, 55 directories, bad cells, rows after
  the table, a text of `None`) and compared on `unknown`, `missing`, `missing_in`, `gate_runs` and `gate_timed`: 6000
  comparisons, identical (`reports/executor-15-checks/diff_gate.py`).
- The register and the other reading of records are verbatim, and the suite's tests drive the command end to end
  (exit 0/1/2, `Error:` lines, bytes of the result) and pass.

## Own-work check (WAY-164)

- Requirement most likely not met: "no change of behaviour, exit codes, messages or the bytes of the report" for the division
  of `read_gate`, the one place where code was rewritten and not moved.
- Check: the differential above, which compares everything `read_gate` writes to a cycle, in order. It found no difference.
- Weakest point I checked: the order of `reasons`, since `dict.fromkeys(reasons)` keeps the first of equal pairs and
  *Unknown values* shows the order; `gate_table_runs` adds its reasons exactly where the loop had, and the per-run reasons
  after them, as before. The differential covers texts that give reasons from several of these places at once.
- Not checked: Windows-only paths of `Git.execute` (code verbatim, covered by the suite as run on this machine).

## Choices

1. **`fill`, `read_repository` and `committed_date` stay in `audit_count.py`** (the slice lets them move "where the cut needs
   them"; the cut does not need them — they use only what `record_reading.py` exports). Rejected: moving them too. With
   `Git`, the errors and the table cells in the same file, `record_reading.py` comes to about 1230 lines before the division of
   `read_gate`, over the 1200 of WAY-385; moving only `fill` leaves about 1195, with no room for the division. Cost if wrong: a
   later slice has to move them (they depend only on names `record_reading.py` already exports) and, then, put the shared
   `Git`/errors/cells in a third module or the register module. The consequence for the slice's text: `fill` is used by
   `audit_count.py` (by `read_repository`), so it needs no `__all__` entry.
2. **`read_prices` stays in `audit_count.py`** although it lies between `header_fields` and `read_gate` at the base: it reads
   the user's price list, not a cycle's record, and with it `record_reading.py` would be about 1230 lines. It imports
   `header_fields`, `table_cells`, `is_separator`, `MAX_BYTES` and `AuditCountError` from `record_reading.py`. Cost if wrong:
   one more function to move later.
3. **Shared base in `record_reading.py`** (`AuditCountError`, `GitError`, `Git`, `table_cells`, `is_separator`, `THE_WAY`,
   `MAX_BYTES`), and `problem_register.py` imports from it. Rejected: a third module for them (outside this slice's *Change*
   list), and `problem_register.py` as the host (git in a module named for the register). Cost if wrong: `problem_register.py`
   depends on `record_reading.py`; a later slice may lift the base into a module of its own.
4. **Division of `read_gate`** into `gate_header`, `gate_table_runs`, `add_gate_run` by what each does (the table and its
   columns; the rows into runs under the limits; one run into cells and numbers), not at a line.
5. The comment `# The price list` replaces `# Tables and the price list` in `audit_count.py` (the tables moved); the comment
   `# Reading a cycle` stands over `fill` there; a section comment `# Git` stands over `Git` in `record_reading.py`.

## Problems as observed

- `foundation_check.py` exits 1 while the two new patterns of the part map name files git does not yet track (observed:
  "matches no file git tracks"); it passes after the new files are committed. The slice's check was run after the commit.
- The slice names `fill` among the names that "`audit_count.py` no longer uses itself"; with `fill` kept it still uses it
  (see choice 1).

## Reaches beyond the handoff

- `agent-instructions/test_size_invariant.py` (read whole as far as line 150: it is named in *Read*); `relation-model/test_fingerprint.py:125-170`
  (to copy the way the invariant `shared-module-import-runs-nothing` starts its interpreter);
  `foundations/decisions.md` WAY-385 (the thresholds, whole entry; F2 is named but not given with a range);
  `process-audit/record_items.py:1-60` (its import pattern); `ruff.toml`; `.runs/task-cycles/code-order-formatter-linter-size/plan.md`
  headings of slices 15-19 (titles only, to see what the later slices are called).
- A `grep`/script run over `audit_count.py` for the use of every name (my own working script).

## Unread material

- `audit_count.py` was read whole for lines 1-2300 (the whole moved part and the module's head); lines 2300-3606 (analysis, the
  report, `main`) I read only where the names moved were used (`withdraw_values`, `note_changed_tools`, the code around
  `process_versions`, `main`), since that code did not change.
- `process-audit/test_audit_count.py:2345-2366`, `3536-3616`, `3780-3800`, `4060-4140`, `4340-4350`: read only the parts that import
  `audit_count` (2875-2895, 4520-4545) and the test of the checkout without a repository key (4150-4235); the rest of the
  named ranges I did not open (the suite ran in full for the part instead).
- `process-audit/test_audit_series_scripts.py`: not opened (names it reaches taken by regex; the suite passes).
- `foundations/invariants.md` ranges (WAY-365 / WAY-48 are read; `audit-count-refuses-record-links`, `cross-part-imports`,
  `script-imports`, `function-and-file-size`): read in the handoff's printed ranges only as extracted lines; `part_map.md:262-269` External context read.
- `task.md` passages (`32`, `108`): not opened; the slice text and the guidelines named were my source.

## Searches not found or unclear

- F2 (WAY-385) was given by name only; found by `grep -n "^### WAY-385"` and read whole.
- No test of the invariant `audit-count-refuses-record-links` was located by me; the suite as a whole passes (it holds
  the symlink cases of the record). I did not look for it by name.

## Working copies

- `.runs/executor-15/` (the old `audit_count.py` and sibling copies from `efc2f090`, `task-cycle/remarks_check.py` copy, scripts
  `build.py`, `build2.py`, `usage.py`, drafts, test output): kept only what the report needs in
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-15-checks/` (`diff_gate.py`, `import_check.py`,
  `astcmp.py`, `test_process_audit_final.txt`); the directory itself removed before return. No git worktree was made.
