PASS 4e5f95fbc7a4e5383751dbb629aacc76e59894e0

# Review of slice 18 — the transitional exports of the audit's command removed

Range `6c748289..4e5f95fb` (one commit, `git rev-parse HEAD` matches the head given). Changed file:
`process-audit/audit_count.py`, 0 added, 32 removed; 900 lines before, 868 after.

## Findings

Blocking (Critical or Important): none. Minor: none. Out of scope: none.

What I verified, by claim most likely to be false first:

1. "No removed name is used in the body." `grep -nw` of each of the 13 removed names (`Register`,
   `COST_SCRIPT`, `COST_SCRIPTS`, `COUNT_PATHS`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`, `MEASURES_SCRIPT`,
   `TOOL_GROUPS`, `Version`, `cost_boundary`, `count_boundary`, `instrument_series`,
   `read_contradiction`) over the head `process-audit/audit_count.py` finds nothing. `Ancestry`, the one
   name of the old `__all__` that the body uses (line 820), stays imported (line 399).
2. "No one reaches a removed name as `audit_count.<name>`." The only reach into the module from outside
   is `process-audit/test_audit_count.py:2905-2920` (`import audit_count`, `audit_count.fill(`), and
   `fill` is a function the file defines itself. No `from audit_count import`, no `__all__`
   elsewhere in `process-audit` or `agent-instructions`. The other mentions of `audit_count` are path
   strings or prose.
3. "Removing `from record_items import read_contradiction` changes no behaviour." `record_items` stays
   imported by `record_reading` and others of the part; the line brought only the unused name, and the
   module holds no import-time work that this file relied on (it imports `remarks_check` as the
   audit does).
4. "Nothing else changes." The diff is deletions only: the 13 names, the whole `record_items` line,
   the two comment lines and the `__all__` list. The `sys.path.insert` line that `remarks_check`
   needs is untouched. No `noqa` other than the `E402` ones, no `fmt:` comment in the file.
5. The trust boundary (`process-audit/audit_count.py`): crafted input gives the same verdict, exit
   code and message before and after (check 6). The change is deletion of import lines; no operation
   that cannot be undone is in it.
6. Tests: no test added or changed; none needed, since no behaviour changes. The tests that stand
   (277 of the part) fail on a name the body still needs and lacks (NameError at call) and pass here.
7. Foundation and guidelines: the slice reaches `ruff-blocking-rules` (checked by check 1) and
   `formatter-layout` (check 2) for the one file, and the guideline `guidelines/coding.md` rule of
   size (868 lines, under the 1200 of WAY-385 as the slice's task line 32 states). No invariant test
   was changed. The file's header comment of the removed `__all__` described a transitional state
   that Slice 17 ended; its removal leaves no stale statement in the file.

## Declined to judge

none

## Checks run

| # | Command | Exit / result |
|---|---|---|
| 1 | `the Ruff of the quality environment of the main checkout check --config ruff.toml --no-cache --ignore-noqa process-audit/audit_count.py` | 0, "All checks passed!" |
| 2 | `<ruff> format --check --config ruff.toml process-audit/audit_count.py` | 0, "1 file already formatted" |
| 3 | `python -B gate/run_tests.py process-audit` (run to its end, exit recorded) | 0, "Ran 277 tests in 370.364s / OK"; log kept in `reports/review-18-evidence/gate_process_audit.log` |
| 4 | `python -B -c "print(len(open('process-audit/audit_count.py',encoding='utf-8').read().splitlines()))"` (the definition of `file_lines` of `agent-instructions/test_size_invariant.py`: `len(source.splitlines())`) | 0, 868 (at most 1200) |
| 5 | `grep -nw` of each removed name in the file; `grep -rn` of `audit_count.<name>`, `from audit_count`, `__all__` over the `.py` files | no hits in the body; the only outside reach is `audit_count.fill` |
| 6 | Crafted input at the boundary, base `6c748289` (a worktree) against head: `python -B process-audit/audit_count.py <args>` for 9 cases (missing locations file, invalid JSON, empty object, no `problem_register`, `problem_register` without `the-way`, a JSON list, bad `--today`, unknown option, `--help`) with absolute paths; stdout, stderr and exit code compared with `cmp` | 27 of 27 files identical (stdout, stderr, rc for each case); exit codes 2,2,2,2,2,2,2,2,0; messages e.g. "the locations file holds no key `the-way`", "is not JSON: line 1, column 2", "is not a JSON object", "the day is not written YYYY-MM-DD"; outputs kept in `reports/review-18-evidence/out/`, cases in `cases.txt` there |

Not run: a counting run over a real register (the happy path); the 277 tests of check 3 stand
for it, as in the executor's report. A first attempt of check 6 used relative paths that resolved
differently in the two checkouts and showed false differences; I rewrote the cases with absolute
paths and the result above is of that second run.

## Reaches beyond the handoff

- `grep` over `process-audit/`, `agent-instructions/` and the repository's `.py` files for
  `audit_count.<name>`, `from audit_count`, `__all__`: to confirm no one reaches a removed name; named
  by the method's "callers" step.
- `foundations/invariants.md:425-450` and `process-audit/record_items.py` imports (head lines): to read
  the invariant's current range and to settle the import side effect of removing the `record_items` line.
- `.runs/task-cycles/code-order-formatter-linter-size/task.md:32` (named by the slice; read).

## Working copies

- `.runs/review-18/base` (git worktree of `6c748289`, for the before side of check 6): removed with
  `git worktree remove --force` and `git worktree prune`; `git worktree list` no longer shows it.
- `.runs/review-18/` (inputs, outputs, the gate log, `cases.txt`): the log, the cases and the outputs
  were copied into `.runs/task-cycles/code-order-formatter-linter-size/reports/review-18-evidence/`, and the directory
  was removed.
- Remainder: none.

## Unread material

none — the method, the guideline `guidelines/coding.md` and the changed file's diff were read whole; the
invariant was read in a window covering both its named range and the handoff's current range; task line
32 was read.

## Searches not found or unclear

none
