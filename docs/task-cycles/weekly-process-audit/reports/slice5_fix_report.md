# Slice 5 fix report: refused rows of the register

**Status:** done

**Commit:** `7bb25c3` (Count refused problem rows in the cycles and issues they name), on `task/weekly-process-audit`, range `c2a0169..7bb25c3`.

**Files changed** (`git show --numstat 7bb25c3`):

| File | Added | Removed |
|---|---|---|
| `process-audit/audit_count.py` | 62 | 18 |
| `process-audit/test_audit_count.py` | 50 | 13 |

## Finding 1 (Important): refused rows invisible in the figures they belong to

Held as right. A refused row listed only in *Unknown values* left a cycle at `none 0 0 0 0` and an open issue at `—`, which read as "no problem".

**How it is fixed:**
- `Register.refused_problems` keeps the Repository, Record and Issue text of each refused row of *Problems*.
- `analyse` places a refused row in the cycle its Repository and Record name, when the Record is a full hash and the cycle is read, and in the issue its Issue names, when that issue is valid. A row with neither stays in *Unknown values* only.
- A count that has a refused row in it reads `at least n`. This applies to the cycle's class rows and *Fixed issues* holding/lacking cells, and to the *Open issues* and *Dropped issues* counts.
- Each of *Problems by cycle*, *Fixed issues*, *Open issues* and *Dropped issues* has a new *Refused rows* column. A cycle with refused rows and no valid problem gets a `none` row reading `at least 0`.
- An open issue with refused rows has `unknown` days, with an unknown row saying so. Its days are not `—`.
- The paragraphs above the tables say what *Refused rows* and `at least` mean.

**Test added first:** `RegisterCount.test_a_refused_row_of_a_cycle_and_an_issue_is_counted_not_hidden` (the review's scratch A). On `c2a0169` it failed with `[... 'none', '0', '0', '0', '0'] != [... 'at least 0' ...]`, which is the reviewer's point. Also added: `RegisterCount.test_a_refused_problem_of_a_fixed_issue_is_counted_in_its_row`, for the fixed-issue case the review named.

**Existing tests updated** (named, because their expectations gained the new column or changed for the fix):
- Column added (`0` or `1` appended, no assertion weakened): `test_the_template_with_no_rows_counts_nothing_and_refuses_nothing`, `test_a_problem_whose_repository_is_not_read_stays_unknown`, `test_a_long_run_of_blanks_in_a_class_name_does_not_stall_the_count`, `test_a_table_missing_from_the_register_is_an_error_of_the_register`, `test_a_fixed_issue_counts_apart_the_cycles_whose_pin_holds_the_fix`, `test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side`, `test_a_fix_the_history_lacks_leaves_its_issue_unknown`, `test_a_cycle_committed_again_counts_its_problem_once`, `test_open_issues_wait_from_the_cycle_commit_to_the_day_of_the_run`.
- Changed for the fix: `test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it` (the cycle now reads `at least 0 ... 1`, which is the reviewer's own example of a test pinning the hidden zero); `test_crafted_rows_of_the_register_are_refused_with_a_reason_and_the_rest_counted` (the cycle's count row is now `at least 0 | at least 1 | at least 0 | at least 0 | 4`; the four refused rows that name this cycle are counted, the fifth row naming an unread repository is not).

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B -m unittest test_audit_count.RegisterCount.test_a_refused_row_of_a_cycle_and_an_issue_is_counted_not_hidden`, before the code change | 1 | failing: `Lists differ: a list holding the row of 'product' with zeros != [...'at least 0'...]`, the zero the review names |
| `python -B -m unittest test_audit_count.RegisterCount` after the code change, before the new fixed-issue test | 0 | 14 tests OK |
| `python -B -m unittest test_audit_count.RegisterCount.test_a_refused_problem_of_a_fixed_issue_is_counted_in_its_row` | 1 then 0 | first run failed on my own wrong expectation (lacking side must read `at least 0` too; the code was right); corrected; then passed |
| `python -B gate/run_tests.py process-audit` | 0 | 87 tests OK (386 s) |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | checked 279 files, 0 listed |
| `python -B -m py_compile process-audit/audit_count.py process-audit/test_audit_count.py` | 0 | ok |
| run on this repository, stdin closed: `python -B process-audit/audit_count.py --locations <scratchpad>\run5\locations.json --today 2026-11-11 <&-` | 0 | `Wrote count-2026-11-11.md and count-latest.md: 71 cycles in 1 of 1 repositories.` Temporary register as in slice 5: `open-demo` shows `1 \| 1 \| 0 \| 34 \| 0`; `ghost` row in *Unknown values* |

The gate ran on the final tree: no source file changed after it started.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** a refused row still hides in a count: a cycle or issue shows an exact figure while a row that belongs to it is out.
- **Check:** scenario A (the open issue with a `Blocker` row) and the fixed-issue refused row, each asserting the exact table cells; plus the crafted-rows test, which counts four refused rows into one cycle.
- **What it showed:** each affected cell reads `at least n` or `unknown`; the untouched cells keep their exact values, and the stdin run's figures agree with the earlier run.

## Questions

None.

## Concerns

- The *Refused rows* column is a new column in four tables. Anything that reads these tables positionally (slice 6, the weekly session) must read the new column; I did not check the slice 6 plan for that.
- A refused row whose Record is valid but whose cycle no named repository holds stays in *Unknown values* only, as the handoff says. It therefore does not show in any count. That is by design; the unknown row is the only trace.
- The `at least n` form is a judgement. The review's direction allowed "unknown, or at least n"; I chose `at least n` for counts and `unknown` for days.

## Reaches beyond the handoff

- `process-audit/problem_register.md` read, to confirm the table forms the new tests use (through the template only).
- I wrote a one-off Python script (a heredoc) to add the new column to expected rows in the test file. I had not read the user's script rules first; I read them afterwards (`.ai/rules/scripts.md`), and checked the file kept its line endings (LF in both HEAD and the working tree; the diff is small).

## Unread material

- `.runs/task-cycles/weekly-process-audit/reports/review_slice5_report.md` (the full review): not read; the handoff names the findings file as what to fix, and the one finding stands in it whole.
- `task-cycle/change/fix.md`: read whole.

## Searches not found or unclear

- Whether slice 6's plan reads the four tables by position: not checked (see Concerns).
