# Report — the second correction for the human's remarks

**Status:** done with concerns (two concerns, below; neither blocks).

**Commits** (on `task/weekly-process-audit`, from `410113b`): `3417058` Read a denial of an open design choice only just before the phrase, and count the cycles an open issue came back in, not those it stands in.

**Files changed** (`git diff --stat 410113b HEAD`):

- `process-audit/audit_count.py`: 79 lines changed (module docstring, `read_contradiction` and two new helpers, the open-issue row, the paragraph and header of *Open issues*)
- `process-audit/test_audit_count.py`: 141 lines changed
- `process-audit/SKILL.md`: 5 lines changed (the matter of what still waits)

No other file was touched. The decision WAY-336 was read whole and is not changed (see (b)).

## Checks (command, exit code)

- Test written first for (a): `python -B -m unittest process-audit/test_audit_count.py -k discard -k crafted -k template` and `... -k denial`: failed, exit 1, for the expected reason (`'yes' != 'unknown'` on the template's own form; `'yes' != None` and `None != 'yes'` on the three subcases of the unit test). After the code: the same command, exit 0, 9 tests OK.
- Test written first for (b): the open-issue tests, run before the code: 7 failures, each on the count (`'0' != '1'` and similar) or on the missing header. After: exit 0.
- `python -B gate/run_tests.py process-audit`: exit 0, 124 tests OK.
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`: exit 0, `checked: 283 files, 0 listed`.
- `python -B agent-instructions/skill_entry_points.py`: exit 0, `entry points are current` (nothing to create or change; only the body of `process-audit/SKILL.md` changed, not its description).
- `python -B process-audit/audit_count.py --locations <temp> --repository the-way --today 2026-11-11 < /dev/null`, with a temporary locations file naming this worktree, a copy of the register's template and a temporary results directory: exit 0, `Wrote count-2026-11-11.md and count-latest.md: 72 cycles in 1 of 1 repositories.` The *Open issues* section shows the new paragraph and the header `Cycles its problems came back in`; the template register holds no issue, so the table is empty.

One check line: all of the above pass; the full suite was not run (the cycle runs it).

## (a) `read_contradiction`: how the correction makes it

`audit_count.py`: the guard no longer takes the words of the whole item. For each occurrence of "open design choice" (found in one pass, `phrase_starts`), `denied_before` reads at most 60 characters before it, cuts them after the last clause mark (`; : , . — – ( ) [ ] ! ? "`), and looks for a denying word (`no not none nor never without`, and now also `neither nothing`) among the last four words of what is left, or for a contracted `n't` / `n’t` in that clause. Any occurrence with a denial before it gives `unknown`; `yes` only where no occurrence has one. `none`, a `none ...` opening, a missing or doubled item and other text are unchanged. No pattern is retried: `str.find`, a bounded slice, a character scan back and the existing `[a-z]+` pattern with no nesting.

Example, the reviewer's:

- Before: `10:32, open design choice found in the auth flow; report reports/x.md; foundation entries none; reset to abc1234; next route: spec` gave `unknown` ("beside a word that may deny it": the `none` of `foundation entries none`).
- After: `yes`. Test: `test_the_templates_own_form_of_a_discarded_open_design_choice_reads_yes`, end to end through the result's Q1 cell.

Negated cases, unit test `test_a_denial_stands_only_where_it_comes_just_before_the_phrase` (each its own subTest): `a time overrun; no open design choice`, `it was not an open design choice`, `discarded without an open design choice`, `found no evidence of an open design choice`, `NO OPEN DESIGN CHOICE`, `never an open design choice`, `neither a size problem nor an open design choice`, `it wasn't an open design choice`, and a text with a denied occurrence after a plain one: all `unknown`. A plain `a time overrun` stays `unknown` (no phrase).

Crafted input, `test_crafted_discarded_attempts_break_no_cell_and_no_pattern`: a very long item (the phrase 20,000 times), `no ` 200,000 times before the phrase, 500,000 characters with no clause mark, control characters with a bar, a bar. Each gives `yes` or `unknown` with a reason, no exception, and the test finishes at once; the same five items run whole through the command leave no control character in the result.

## (b) The count of an open issue's cycles: how the correction makes it

`analyse` in `audit_count.py`: the column is `max(len(hit) - 1, 0)`, `hit` being the distinct cycles (a cycle copied again once) that hold a problem of the issue. It reads `at least n` where `refused + not_read` is above zero (refused rows of the issue, or problems of a cycle not read, may belong to a cycle not counted; the known cycles less one is a lower bound in every such case). The header is `Cycles its problems came back in`; the paragraph of the table, the module docstring and `process-audit/SKILL.md` say the same. The days of waiting, the other columns and the order (the register's) are untouched.

Example: one problem seen in one cycle.

- Before: `| slow-one | 1 | 1 | 0 | 10 | 0 |`. After: `| slow-one | 0 | 1 | 0 | 10 | 0 |`.
- Three cycles, one holding two problems of the issue (new test): `seen-thrice` was `3`, is `2`, its problems `4`.
- A problem of an unread cycle (the ghost repository) beside three known cycles: `at least 2`; a refused row beside two known cycles: `at least 1`.

**The ordering the handoff names is not implemented, on purpose.** The handoff says to except "the first of them (the earliest cycle by the commit of the *Record* ..., ties by the cycle's identity)". The number of cycles a problem came back in is the same whichever cycle is excluded, so the count needs no order, and an order would add a place for an unknown date to turn a count into `unknown` without reason. If the human wants the first cycle named, that is a new column, not this correction.

**WAY-336 read whole**: its verification says "the number of cycles in which its problem came back", which the new column is; none of its words is wrong, so it is not edited and `the-way-record-decision` was not used.

## Tests whose expectations changed for (b), and why none is weakened

All in `process-audit/test_audit_count.py`, the third cell (the cycle count) only; the other cells of those rows are unchanged:

- `test_open_issues_wait_from_the_cycle_commit_to_the_day_of_the_run`: `1` to `0` (one cycle holds the problem).
- `test_an_open_issue_waits_from_the_copy_its_problem_names`: `1` to `0` (one cycle, two copies).
- `test_open_issues_are_listed_in_the_register_order_not_by_their_returns`: `1` and `2` to `0` and `1` (cycles holding the problems: 1 and 2).
- `test_a_record_that_adds_the_records_of_two_cycles_names_neither`: `0` to `at least 0` (its one problem is of an unread cycle; before, the count did not say so).

Each asserts exactly what it did, against a count that is now derived by hand; none relaxed a pattern, skipped a test or dropped an assertion. The last is stricter than before. Three tests are new: `test_an_open_issue_counts_the_cycles_its_problems_came_back_in`, `test_the_count_of_returns_reads_at_least_where_a_row_or_a_cycle_is_missing`, `test_a_cycle_copied_again_is_one_cycle_in_the_count_of_returns`.

Lessons of the earlier reviews kept: no backtracking pattern, no new conversion (`days` unchanged), every cell still goes through `cell()` (the new code writes only numbers and fixed words), size caps unchanged, a cycle whose record fails is `unknown` for that cycle as before.

## Own-work check

The requirement most likely missed: "never a wrong `yes`" for Q1 under the narrower window. Check: the unit test above, with eight denial forms and a denied second occurrence, each `unknown`, and the template's own form `yes`. It showed all of them as expected. The residual that it does not catch is in Concerns.

## Choices and the ways rejected

- Window: the last four words in the same clause, 60 characters. Rejected: only the one word right before (`no evidence of an open design choice` would then read `yes`, a wrong `yes`); the whole item (the defect). Cost if wrong: a denial five or more words before the phrase gives a `yes`; a denial inside a long clause before a comma reads `unknown`.
- `at least n` also for an unread cycle (before, only a refused row made it). Rejected: leaving the unread cycle out of the count's wording, which would show an exact number that could be too low.
- No ordering of the cycles (above).
- One commit for both items: they touch the same three files; a split would have left the docstring in two halves.

## Concerns

1. A denial after the phrase now reads `yes`: `open design choice not found` (the old guard gave `unknown`). The handoff and the reviewer's direction say to look only before the phrase, so I did; the human can ask for a check of the rest of the clause too (cheap, same helper).
2. A denial before a comma is cut off: `not found, open design choice at the start` reads `yes`; I think that right, but it is a reading.

## Reaches beyond the handoff

None beyond the files the handoff names and the module docstring it names; I read `task-cycle/record_template.md` (the *Discarded attempt* line, with `grep -A6`) to check the template's form, and `scripts.md` of the author's rules before writing the one-off script that edited the test file.

## Unread material

- `task-cycle/change/SKILL.md`: read whole. `task-cycle/review/fix.md`: read its first 80 lines (the file is shorter than that or ends there; the part on a correction was in them).
- `process-audit/audit_count.py` (2129 lines): read lines 1 to 700, 820 to 950, 1490 to 1700 and 1930 to the end; not read whole (the parts on the price list, git reading, series and the stages cost, which the correction does not touch).
- `process-audit/test_audit_count.py`: read 1100 to 1430 and 1600 to the end; not read whole.
- `process-audit/SKILL.md`: read 30 to 50 and 128 to 158; not whole.
- WAY-336: read whole. No other foundation entry or guideline file was named by the handoff.

## Searches not found or unclear

- None unclear in the handoff beyond the ordering sentence, above.
- A search of the repository outside `.runs` for `problems stand`, `Cycles in which its` and `Open issues` found no other file that cites the old column.

## Gate fix

The gate run of `elements/part-map` failed in `test_cross_part_imports.TheWay.test_the_way_imports_only_from_allowed_parts`: my two new tests imported `remarks_check` after a `sys.path.insert`, which the cross-part import check cannot see from a test.

- **Commit:** the one after `3417058`, "Take remarks_check from audit_count in the new tests: the cross-part import check does not see a path-inserted import".
- **Changed:** in `process-audit/test_audit_count.py`, in `test_a_denial_stands_only_where_it_comes_just_before_the_phrase` and `test_crafted_discarded_attempts_break_no_cell_and_no_pattern`, `import remarks_check` became `remarks_check = audit_count.remarks_check` (2 lines). No assertion changed.
- **Other new tests:** the only other import in my new tests is `import audit_count`, the module of the test's own part, already imported in that form by the earlier test `PriceBoundary`; no other module of another part is imported.
- **Checks:** `python -B gate/run_tests.py elements/part-map` exit 0 (39 tests OK); `python -B gate/run_tests.py process-audit` exit 0 (124 tests OK); `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exit 0 (`checked: 283 files, 0 listed`).
