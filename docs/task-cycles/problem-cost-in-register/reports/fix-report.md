# Report of the fix — Minor findings of the review of the whole change

**Status:** done. **Head reached:** the commit below, on `task/problem-cost-in-register` (fix range from `18b4a3f`).

## Commit

One commit, by path: see `git log -1` on the branch (message "Fix the three Minor findings of the review: five tables in the template, a reordered header in the test, the wrap of WAY-330"). Files: `process-audit/problem_register.md` (1 line), `process-audit/test_audit_count.py` (+13 / -7), `foundations/decisions.md` (+8 / -6). Total 3 files.

## The three findings, as made

1. Stale count: `process-audit/problem_register.md` line 39 now reads "Text outside the five tables is not read; write there what you like." `grep -n "four tables"` on the file gives nothing now.
2. Test name claims more than it checks: `test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing` now runs two subtests, "an extra column" (as before) and "two columns swapped" (`Weight` and `Cost of an occurrence` swapped in the header of *Problems*). Each asserts exit 1, the table `Problems` refused in *Unknown values*, and the result written with the cycle counted. Name kept (it now says what it checks). Mutation check: with the reading of the header changed to take every column as absent, the test failed (2 subtests); restored before the commit (`git status` showed only the three files).
3. Reflow: the *Rationale* and *Rejected* of WAY-330 rewrapped; longest line of that range is 100 characters (was 123, 109, 110). Words unchanged.

Not fixed, as the handoff says: Minor 4 of the review (outside the task).

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Tests of the affected part | `python -B gate/run_tests.py process-audit` (background, 290 s) | 0 (129 tests OK) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| Private paths, prose files edited | `python -B task-cycle/private_paths_check.py process-audit/problem_register.md`, same for `foundations/decisions.md` | 0, 0 (0 listed) |
| Mutation of the header reading, then restored | `python -B -m unittest test_audit_count.RegisterCount.test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing` from `process-audit/` | 1 with the mutation, 0 after restoring |

Not run: the whole gate (the handoff forbids it); `elements/common` and `agent-instructions` tests (no file they cover changed since the last green run, only the two prose lines and one test).

## Own-work check

Requirement most likely unmet: the swapped-columns case must pass for the right reason, not by the extra-column logic. Check: the mutation above makes any header mismatch a missing field; the test failed, so it guards "no field is missing, so the table is refused". It passed on the real code.

## Reaches beyond the dispatch

None.

## Unread material

None beyond what the first report lists; I read the handoff, the findings file and the lines I edited (problem_register.md line 39, decisions.md lines 10960-10990, the test I changed). I did not read `reports/review-whole-report.md`; the findings file quotes it.

## Searches not found or unclear

None.
