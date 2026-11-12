PASS e6d05e2bf5da4728b7fa590565f5656d72329321

# Review of the fix, problem-cost-in-register

Range `18b4a3f..e6d05e2` (one commit, `e6d05e2`, 3 files). `git rev-parse HEAD` is
`e6d05e2bf5da4728b7fa590565f5656d72329321`, the head given. Method: `task-cycle/review/SKILL.md` and
`fix.md`. The findings file bounds this review: `reports/findings-minor.md` (Minor 1, 2 and 3 of my
review of the whole change). Blocking findings: 0. New Minor findings: 0. Remaining: 0.

## The three findings

1. **Stale count of tables in the template: fixed.** `process-audit/problem_register.md:39` now reads
   "Text outside the five tables is not read; write there what you like." `git grep -n "four tables"
   e6d05e2 -- process-audit` gives nothing. The file now says five tables at lines 29 and 39.
2. **Test name claims more than it checks: fixed.**
   `process-audit/test_audit_count.py:1303`, `test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing`,
   now runs two subtests, "an extra column" and "two columns swapped" (`Weight` and `Cost of an
   occurrence` swapped in the header of *Problems*, guarded by `assertNotEqual(PROBLEMS_HEADER,
   swapped)` so the swap really changes the header). Each asserts exit 1, the table `Problems` among
   the *Unknown values*, and the cycle still counted. Mutation of my own, in a copy of `e6d05e2`
   extracted by `git archive` into the scratchpad (the reviewed worktree untouched): a reordered header
   (same columns, other order) is made to count as a missing column. Result: the subtest "two columns
   swapped" fails (`AssertionError: 1 != 2 : ... lacks the column `Repository` of the table
   `Problems``), the subtest "an extra column" passes. So the test now fails exactly when a reordered
   header is turned into a missing field, which is the guard I asked for.
3. **Reflow damage in WAY-330: fixed.** `foundations/decisions.md` *Rationale* and *Rejected* of
   WAY-330 are rewrapped. Words: the word sequence of the WAY-330 section is identical at `18b4a3f` and
   `e6d05e2` (compared by splitting on whitespace, `True`), and so is that of the whole file (`True`),
   so no word was changed, moved or dropped anywhere. Line lengths: the lines of 123 and 110
   characters are gone; no line of WAY-330's *Rationale* or *Rejected* passes 100 characters. (The
   heading line of 172 characters is a question heading and was long before; line 10984 of 101
   characters is in WAY-331 and was not touched.)

## What the fix itself may have broken

The diff is the three changes above and nothing else (one word in a template line, a loop over two
header cases in a test, a rewrap). Test logic: the loop rewrites the register for each case and
asserts afresh, and `self.write_locations(...)` is called once before it, as the earlier version did;
no state leaks between subtests (the register is rewritten each time). No new Critical, Important or
Minor finding.

Open outside the fix, not reopened: Minor 4 of the review of the whole change (the exit code of the
level tables' row labels against WAY-344, outside the task) stays on the request's list, as the
findings file says.

## Checks run

| Check | Command / method | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | exit 0, `e6d05e2bf5da4728b7fa590565f5656d72329321` |
| Range | `git log --oneline 18b4a3f..e6d05e2`; `git diff 18b4a3f..e6d05e2` | exit 0; one commit, 3 files, +21 -13 |
| Tests of the part | `python -B gate/run_tests.py process-audit` (from the worktree, background) | exit 0; 129 tests OK, 295.8 s |
| Foundation check | `python -B elements/common/foundation_check.py` | exit 0; `0 errors` |
| Words of WAY-330 and of the whole file unchanged | `git show <rev>:foundations/decisions.md` for both revisions, split on whitespace and compared (script in `python -I -`) | both `True` |
| Line lengths of WAY-330 | `git show ... \| sed -n 10945,10985p \| awk 'length>100'` at both revisions | old: 123, 110 (and heading, WAY-331 line); new: heading and the WAY-331 line only |
| Stale count | `git grep -n "four tables" e6d05e2 -- process-audit` | no hit |
| Mutation of a reordered header | in `scratchpad/fixcopy` (a `git archive` of `e6d05e2`): `python -B -m unittest test_audit_count.RegisterCount.test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing` after editing `audit_count.py` | exit 1; the subtest "two columns swapped" fails, "an extra column" passes |
| Worktree clean | `git status --short` after all runs | empty |

Not run: the whole gate, by the handoff; `elements/common`, `agent-instructions` and private-path checks
(the fix changes two prose lines and a rewrap with the same words; the private-path content of the
lines is unchanged and I did not repeat the author's `private_paths_check.py` run).

## Reaches beyond the dispatch

None.

## Unread material

- Decisions: this review reads none of the foundation's decisions for its own selection; the fix
  touches the layout, not the meaning, of WAY-330, which I read whole in the review of the whole
  change. 0 whole, 0 by title for this review.
- `reports/fix-report.md`: read whole; `reports/findings-minor.md`, `reports/review-fix-handoff.md`,
  `task-cycle/review/fix.md`: read whole.
- The rest of `process-audit/test_audit_count.py` and of `audit_count.py`: not re-read; the fix does
  not touch them, and the whole `process-audit` run is green.

## Searches not found or unclear

None.
