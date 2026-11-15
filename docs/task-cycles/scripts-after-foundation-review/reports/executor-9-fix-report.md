# Fix report — slice 9 of `scripts-after-foundation-review`, review finding I1

**Status:** `done`

**Commit:** `61171e9` on `task/scripts-after-foundation-review` — "Keep the unknown pins and per-issue values of the audit count in the first table" (author address `the author's e-mail address`, from the conditional git rule for the `mariusznazar` account; left as it is). Fix range: `b6f800c..61171e9`.

**Files changed:**
- `process-audit/audit_count.py`
- `process-audit/test_audit_count.py`

## Findings

- **I1 (Important, blocking) — fixed.** The values the ancestry check adds (`Process pin` of fixed issues), and the per-issue values (`the fix of issue …`, `waiting of issue …`), were folded into the register's pairs. Now they are given in full, one row each, in the first table of *Unknown values*, as before the slice. Only the values the register holds back (its refused rows, and the problems whose cycle is not read) are grouped by field and reason in the second table.
  - How: `analyse` keeps two lists. `held` holds `register.refused` and the problem rows the count cannot place; `unknown` holds the per-row values. `Analysis` has a new field `held`; `render` writes `unknown + versions + measured` into the first table and `held` into the pair table.
  - Description: the sentence at the top of the module, the sentence in the result list, and the constant comment now say that the register's held-back values are grouped and their full list stays in the register, and that every other unknown value is given in full. The intro paragraph of the section says the same.
  - Test: `RegisterCount.test_each_cycle_whose_pin_is_unknown_for_a_fixed_issue_keeps_its_own_row` — four cycles whose pins the history lacks (more than the three examples of a pair), each keeps its own row in the first table with its repository, record and reason; no `Process pin` row in the pair table.
  - Tests reverted to read the first table for the per-row values: `test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side`, the `ambiguous` test, the shallow-clone test, and the test of the reasons of `the fix of issue`.
- **M1 and the other Minor findings** — not fixed, as the handoff asks.

## Red check on `b6f800c`

Copy of the test file with the `b6f800c` script, in `.runs/executor-9/base-check/`, run with `-k test_each_cycle_whose_pin`: exit 1, 1 test, `FAIL` on the first table: `Lists differ: [] != a list of lists` — the `Process pin` values sit in the pair table on the base. The copy was removed.

## Checks (command and exit code)

1. Compile check: `python -B -m py_compile process-audit/audit_count.py process-audit/test_audit_count.py` — exit 0.
2. Focused command of the slice: `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Run -k RegisterCount -k CraftedInput` — exit 0, 69 tests (was 68 before the fix; one test added). Log: `reports/executor-9-fix-focused-run.txt`.
3. Whole file: `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` — exit 0, 228 tests. Log: `reports/executor-9-fix-whole-run.txt`.
4. `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` — exit 0, 3 tests. Log: `reports/executor-9-fix-series-run.txt`.
5. Red run on the base (above) — exit 1, 1 failure. Log: `reports/executor-9-fix-red-run.txt`.

No run of the whole gate.

## Choices

- Per the orchestrator's direction, the held-back set is `register.refused` plus the problem rows the count cannot place (the "no named repository holds" and the "shared record" reasons). Rejected: tagging each tuple with its origin; a field on the tuple is more change than the two-list split needs.
- The count of rows of a pair keeps its meaning; the examples are still the first three.

## Unread material

- `.runs/task-cycles/scripts-after-foundation-review/reports/slice-9-findings.md` and `executor-9-fix-handoff.md` read whole. `task-cycle/change/fix.md` read whole.
- `process-audit/audit_count.py`: read at the changed places (about lines 259–292, 438–446, 2296–2320, 2380–2432, the render section near 3180–3200) and not whole. Other parts as in the slice report.
- `reports/review-9-report.md` (the reviewer's full report, named by the findings file) was not opened; the findings file's text was used.
- The Minor finding M1 is in that report and was not read beyond the findings file's mention.

## Searches not found or unclear

- Whether the reviewer's evidence line about `test_a_fixed_issue_whose_pin_lacks_the_commit...` refers to the test at `test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side` (the name in the findings file does not exist in the test file). I took it to mean that test, which is the one that reads `Process pin` for that cycle.

## Working copies

- `.runs/executor-9/base-check/` (red run copy) — removed with `rm -rf`.
- `.runs/executor-9/` (check logs) — the logs were copied to `reports/` and the directory was removed.
- Nothing was written to the system temp folder by me. One redirect to `/tmp/x` was attempted by mistake and failed without creating a file.
