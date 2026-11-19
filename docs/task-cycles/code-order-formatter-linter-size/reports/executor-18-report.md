# Executor-18 report — Slice 18: the transitional exports of the audit's command removed

**Status:** done

**Commit:** `4e5f95fb` on branch `task/code-order-formatter-linter-size` — "Remove the export list of audit_count.py and the imports that stood only for it"

**Base:** `6c748289faddbbd41893ae99abe17dd0c92c5d68` (slice base; range is one commit)

**Check result:** all focused checks passed (ruff check, ruff format --check, `gate/run_tests.py process-audit` exit 0, 277 tests OK); no check failed or was skipped.

## Files changed

- `process-audit/audit_count.py`: 0 added, 32 removed lines.
  - Removed the `__all__` list (14 names) and its two comment lines.
  - Removed the 13 imports that the list alone kept alive: `Register` from `problem_register`; `COST_SCRIPT`, `COST_SCRIPTS`, `COUNT_PATHS`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`, `MEASURES_SCRIPT`, `TOOL_GROUPS`, `Version`, `cost_boundary`, `count_boundary`, `instrument_series` from `version_analysis`; and the whole line `from record_items import read_contradiction` (its only name was unused in the body).
  - Kept `Ancestry` (used at line 852 of the body) and the `sys.path.insert` line, which `remarks_check` needs.
  - Method: `ruff check --select F401 --fix` on this one file (it reported exactly the 13 names above, and nothing else), then `ruff format` (left the file unchanged).
  - Length: 900 lines before, 868 after (`wc -l`).

## Checks

Each check, its command and exit code:

| # | Check | Command | Exit |
|---|---|---|---|
| 1 | Lint baseline before the change | `the Ruff of the quality environment of the main checkout check --config ruff.toml --no-cache --ignore-noqa process-audit/audit_count.py` | 0 ("All checks passed!") |
| 2 | Lint after the change | same command | 0 |
| 3 | Format after the change | `<ruff> format --check --config ruff.toml process-audit/audit_count.py` | 0 ("1 file already formatted") |
| 4 | Focused gate directory (first run, backgrounded) | `python -B gate/run_tests.py process-audit` | exit code lost: the foreground call was moved to the background and its wrapper's exit was not recorded; its log held only progress dots |
| 5 | Focused gate directory (rerun, exit recorded) | `python -B gate/run_tests.py process-audit > .../gate_process_audit.log 2>&1; echo $?` | 0 — log ends "Ran 277 tests in 386.128s / OK" |
| 6 | Crafted-input comparison, before vs after | `run_cases.sh` in the evidence directory: 8 cases (missing locations file, invalid JSON, empty object, no `problem_register`, bad `--today`, unknown option, `--prices` case, `--help`) | identical stdout, stderr and exit code for all 8 cases (exit codes 2, 2, 2, 2, 2, 2, 2, 0) |
| 7 | Size of the test file `agent-instructions/test_size_invariant.py` (the slice's own count) | `wc -l` (its `file_lines` is `len(source.splitlines())`) | 139 lines, at most 1200 |

Tests written first: none. This is a removal of unused names and imports; no test was added or changed, so no invariant test was seen failing.

Notes on checks 4 and 5: the first foreground run was moved to the background by the harness and its exit code was lost; check 5 is the rerun, and its exit code is the one reported. A parallel direct `python -m unittest discover -s process-audit` run was started as a cross-check, but its log had not finished when I stopped it (process killed by me, exit file never written); it is not a result and is not reported as one.

Gaps in check 6: all 8 cases exercise the error paths and the module import. The `--prices` case exits at the register lookup before the price list is read, so it does not test the price-list path. The happy path (a real counting run) is covered only by the 277 gate tests in check 5, not by my crafted inputs.

## Own-work check (section 3, WAY-164)

- Requirement most likely not met: "nothing else changes", i.e. a removed import that the body or another module still needed would break the run at import time or at a call.
- Check: ruff F401 on the file after the change (exit 0, clean); a grep for every removed name in `process-audit/audit_count.py` (no remaining uses in the body), and for `audit_count.<name>` or `from audit_count import` in the repository (only `audit_count.fill`, used by `process-audit/test_audit_count.py`, is reached; that name is not in the removed set); then check 5 (277 tests OK) and check 6 (identical outputs on error paths).
- Showed: no removed name is used; the test suite and the error paths behave as before.

## Trust boundary

`process-audit/audit_count.py` is a file with a trust boundary (the part map names it). Verdict, exit code and message were compared on the 8 crafted inputs above: identical before and after (check 6). The happy-path verdict is covered by the gate tests (check 5), not by the crafted set.

## Choices and adaptations

- Removed the `record_items` import line entirely (not just the name), because its only name was the unused `read_contradiction`. Cost if wrong: if `record_items` had an import-time side effect that audit_count relied on, the removal would change it. Not verified beyond the passing tests; `record_items` is still imported by other modules of the part.
- Kept `Ancestry` in the `version_analysis` import, because the body uses it.
- No adaptation of section 4 was needed: the plan and the code agreed (the names were exactly those the slice describes).

## Reaches beyond the handoff

- `task-cycle/change/SKILL.md`, `slice.md`: read whole (named by the method).
- `guidelines/coding.md`: read whole (named by the slice).
- `foundations/invariants.md`: read lines 420-450 (the slice names 428-436, the handoff's current range is 438-447; I read the window covering both).
- `task.md`: read line 32 (the To do item, named by the slice).
- `ruff.toml`: read whole, to confirm the configuration the checks use (not named by the handoff).
- `agent-instructions/test_size_invariant.py` lines 50-62: to confirm the `file_lines` definition (named by the slice's check).
- `process-audit/audit_count.py`: read whole (it is the changed file).
- Rule files of the vault (`.ai/rules/scripts.md`, `.ai/rules/git.md`): surfaced by the rules hook on my Bash calls; read as delivered.

## Unread material

none — every file, passage and guideline the handoff names was read; the foundation invariant was read in a wider window than its named lines.

## Searches not found or unclear

- None found. Searches that returned nothing: `audit_count.<name>` and `from audit_count import` in any `.py` file outside `process-audit/audit_count.py` other than `test_audit_count.py` (which uses only `audit_count.fill`).
- Unclear: `pgrep` is not installed in this shell, so my first watch reported a false "finished" for the gate run; the watch was then switched to a CIM-based process check. This affected only my waiting, not the result.

## Working copies

- `.runs/executor-18/` (before/after crafted-input outputs, inputs, `run_cases.sh`, gate logs) — copied into `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-18-evidence/` and removed from the worktree. No git worktree was created for this slice, so nothing needed `git worktree remove` or prune.
- Partial unittest log `.runs/executor-18/unittest_process_audit.log` — removed with the directory; the run was stopped, its result is not reported.
- Remainder: none.

## Evidence

- Gate log (exit 0, 277 tests OK): `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-18-evidence/gate_process_audit.log`
- Crafted-input outputs before/after: `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-18-evidence/before/` and `.../after/`
