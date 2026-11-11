PASS 7bb25c33aef660b1923ed9f67c07fbe3ca939259

# Review of the fix of slice 5 (`c2a0169..7bb25c3`)

`git rev-parse HEAD` = `7bb25c33aef660b1923ed9f67c07fbe3ca939259`, confirmed. One commit, `7bb25c3`: `process-audit/audit_count.py` and `process-audit/test_audit_count.py`.
Method: `task-cycle/review/fix.md`. Read: the findings file `review_slice5_findings.md` (one blocking finding), the fix report `slice5_fix_report.md` (claims), the whole diff of the range.
Worktree read only (`git status --short` empty after the checks). Counts: 0 blocking, 2 Minor, 0 out of scope.

## Finding 1 (Important: a refused row invisible in the figures it belongs to) — FIXED

Evidence, scratch A rerun on `7bb25c3` (`scratch7.py`, one cycle, one open issue `open-one`, one problem row of it with the weight `Blocker`):
- *Problems by cycle*: `none | at least 0 | at least 0 | at least 0 | at least 0 | 1` (was `none 0 0 0 0`).
- *Open issues*: `open-one | at least 0 | at least 0 | 0 | unknown | 1` (was `… —`): the days are `unknown`, not "no problem yet", and an unknown row says why ("some of its problem rows are refused, so its waiting is not known").
- The fixed-issue case: the new test `test_a_refused_problem_of_a_fixed_issue_is_counted_in_its_row` gives `at least 1 | at least 0 | 0 | 0 | 1` (both sides read `at least`, since the refused row could belong to either); I read the test and the code, and the 87 tests pass.
- How: `Register.refused_problems` keeps the Repository, Record and Issue text of each refused row of *Problems* (including a row of the wrong width); `analyse` puts a refused row into the cycle its Repository and Record name (full hash, lower-cased, found among the cycles and their later copies) and into the issue it names (only when that issue is a valid row), counts them as *Refused rows*, writes the cycle's, fixed issues' holding/lacking, and open and dropped issues' counts as `at least n`, and gives `unknown` days to an open issue with any refused row. A row with neither a usable cycle nor a valid issue stays in *Unknown values* only, as the finding's direction allowed.
- Also run (scenario H): a refused row with an upper-case Record that is a later copy of a cycle, a row with a 3 MB Issue cell, a row with an ESC in the Repository, a row of two cells and an empty row. The cycle counts 3 refused rows (the upper-case later-copy row, the 3 MB-issue row, the short row), the open issue counts 2, the result holds no non-printable character, size 4.9 KB, 2.8 s. The ESC and empty rows name no read cycle and stay in *Unknown values*.

## Changed existing tests (11): none weakened

- Nine only gained the new last column (`0`, or `1` where a refused row is there): `test_a_fixed_issue_counts_apart_the_cycles_whose_pin_holds_the_fix`, `test_the_template_with_no_rows_counts_nothing_and_refuses_nothing`, `test_a_problem_whose_repository_is_not_read_stays_unknown`, `test_a_long_run_of_blanks_in_a_class_name_does_not_stall_the_count`, `test_a_table_missing_from_the_register_is_an_error_of_the_register`,
  `test_open_issues_wait_from_the_cycle_commit_to_the_day_of_the_run`, `test_a_cycle_committed_again_counts_its_problem_once`, `test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side`, `test_a_fix_the_history_lacks_leaves_its_issue_unknown`. I read each hunk: the figures asserted are the same, each cell compared by value, and the added cell is a count that must read `0` where nothing is refused, so each now also asserts that a refused row is not invented.
- Two changed for the fix, and both got stronger: `test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it` now expects `none | at least 0 x4 | 1` instead of `none 0 0 0 0` (the zero the review named); `test_crafted_rows_of_the_register_are_refused_with_a_reason_and_the_rest_counted` now expects `at least 0 | at least 1 | at least 0 | at least 0 | 4` instead of `0 1 0 0`. The count 4 is right by my reading of the seven crafted rows: rows 2, 4, 5 and 6 name the product cycle (class, weight, an issue refused for a bad fix, an issue in no row); row 3 has no hash and row 7 an unread repository.
- Added: `test_a_refused_row_of_a_cycle_and_an_issue_is_counted_not_hidden` (scratch A) and the fixed-issue test.

## Hostile input in what the fix changed

- The new column and `at least n`: `counted` formats an int; the column is `str(int)`; both pass through `table()` and so `cell()`. The new unknown reason is a constant sentence with an issue name that already passed `NAME` (at most 80 characters). No text of the register reaches the result through the new code.
- `refused_problems` keeps the raw cells (uncapped, within the 4 MiB read) only for dictionary and set lookups (`index.get((repository, record.lower()))` after a `FULL_HASH` fullmatch; `issue in valid_issues`); nothing of it is copied out, and no new pattern was added. A 3 MB issue cell ran in 2.8 s with the rest.
- Number and date conversions: none added; `days` stays `unknown` for a refused row without a date computation.
- Failure of a row: none aborts; the scenario H rows (empty row, short row, ESC, huge cell) all gave exit 0.

## Minor findings (do not block)

### Minor 1 — the exact columns beside the `at least` ones can still miss a refused row

Place: `analyse`: *Problems with an unknown pin* and *Problems whose cycle is not read* (fixed issues), *Problems whose cycle is not read* (open and dropped issues) stay exact `n` while the issue has refused rows. A refused row of a fixed issue whose cycle's pin is unknown or whose cycle is not read could belong to those columns, not to the holding or lacking ones, and the columns beside them say `at least`. The *Refused rows* column states the number, so the figure is not hidden, and the paragraph above each table says a count with a refused row reads `at least n`; but those two columns do not follow the rule the paragraph states. Direction: write them `at least n` as well, or say in the paragraph that they are exact.

### Minor 2 — the docstring was not updated for the new column and `at least`

Place: the module docstring of `process-audit/audit_count.py` (the paragraph on the register: "a row that does not read … refuses that row … and what depends on it is `unknown`", and the list of sections). The result's own paragraphs say what *Refused rows* and `at least n` mean, but the docstring, which the code states as its specification, still says "what depends on it is `unknown`". Direction: one sentence.

Carried over from my review of slice 5 and not in the findings file (not judged here, per `fix.md`): the days from the cycle's first commit, the unbounded work and output by register size, the untested ambiguous short hash.

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log c2a0169..7bb25c3`; `git diff c2a0169..7bb25c3` (read whole) | 0 |
| `python -B gate/run_tests.py process-audit` (worktree, bytecode off) | 0 — 87 tests OK, 364 s |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| scratch `scratch7.py` (outside the worktree; temporary repositories through the tests' helpers): scratch A and the hostile scenario H | A: `at least 0 … 1` and `unknown`; H: exit 0, 3 and 2 refused counted, no non-printable character |
| `git status --short` after the checks | empty |

Not run: the full suite; `foundation_check` (no foundation file touched); the executor's stdin run on this repository (not repeated).

## Reaches beyond the dispatch

- `scratch6.py`/`scratch7.py` helpers of the test module (`RegisterCount`, `register_text`, `problem_row`) — to build the scenarios.
- Nothing else.

## Unread material

- `slice5_fix_report.md` read whole; the review's full report is mine. `audit_count.py` read in the diff and the code around `analyse`; the rest of the file as in the review of slice 5. `task-cycle/review/fix.md` read whole.

## Searches not found or unclear

- Whether slice 6 or 7 reads these four tables by position (the fix report's concern): not found in what I read; the new column is last in each table, so a reader by column name or by position of the earlier columns is not broken.
