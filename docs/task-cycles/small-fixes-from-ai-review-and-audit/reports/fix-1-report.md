# Report of the fix of the review of the whole change (fix 1)

**Status:** done

Worktree `the worktree root`, branch
`task/small-fixes-from-ai-review-and-audit`, from the reviewed head
`f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`. The worktree is clean. Nothing is pushed.

## Commits (range `f52c5657..5d160f9d`)

| Commit | What |
|---|---|
| `f2c7f093` | I1: the twelve `decision:` lines of `process-audit/test_process_versions.py` |
| `f358aa42` | I2, Minor 4, Minor 8, the new string of Minor 5: WAY-417 narrowed, `process-audit/SKILL.md` and the prose of `process-audit/audit_report.py` brought in line |
| `0d0c7266` | Minor 1, 2, 3: `task-cycle/gate_times.py` and `task-cycle/test_gate_times.py` |
| `44d5055e` | Minor 7: `mechanism_comparison` (`process-audit/series_summary.py`, its test), the prose of the comparison in `process-audit/SKILL.md` and `process-audit/audit_report.py`, and the docstring of `process-audit/audit_count.py` (its two long lines of Minor 5 and the same clause) |
| `aec570d8` | Minor 9: the dead helper removed from `process-audit/test_audit_count.py` |
| `3fab989a` | Minor 5, the docstring of `task-cycle/gate_times.py` and one line of its test (my own new lines, kept to 100 characters) |
| `5d160f9d` | Minor 5: the replaced paragraphs of the 15 skills of point 9, `elements/common/reaching_another_skill.md` and `task-cycle/skill/return_step.md` rewrapped to 100 characters |

## Each finding

### I1 — fixed

Each `decision:` line of the twelve now quotes the start of a binding sentence, word for word, on its line, with nothing after the closing quote. The sentences, by line of the test file at the head:

| Line at head | Test | Decision and sentence quoted |
|---|---|---|
| 1745 | `test_the_rows_of_the_versions_stay_and_give_q1_as_numbers_of_their_cycles` | WAY-417 "The answer Q1 of the audit, whether a contradiction" |
| 1765 | `test_a_version_has_no_reason_for_its_q1_and_each_cycle_keeps_its_own` | WAY-417 "The answer Q1 of the audit, whether a contradiction" |
| 1778 | `test_the_image_stands_under_the_heading_of_the_series_before_its_table_per_version` | WAY-339 "The audit shows each series as an image of all its cycles" (it was a sentence of WAY-339 cited as WAY-417's) |
| 1975 | `test_the_count_of_remarks_gives_the_two_sides_and_no_answer_of_its_own` | WAY-417 "The answer Q2 of such a group" |
| 1991 | `test_a_mechanism_measure_falls_where_the_median_after_the_fix_is_lower` | WAY-417 "The answer Q3, whether the median cost" |
| 2013 | `test_the_gate_times_compare_the_runs_compared_and_show_the_others_apart` | WAY-350 "The audit compares the times of the gate between versions" |
| 2050 | `test_a_version_that_is_later_by_date_but_lacks_the_fix_lands_before_it` | WAY-339 "The audit shows each series as an image of all its cycles" |
| 2080 | `test_a_series_with_cycles_on_one_side_of_the_fix_only_has_no_comparison` | WAY-339 "The audit shows each series as an image of all its cycles" |
| 2095 | `test_a_fix_that_the_checkout_lacks_gives_no_comparison_and_an_unknown_value` | WAY-339 "The audit shows each series as an image of all its cycles" |
| 2129 | `test_a_change_of_the_review_splits_the_count_so_that_each_part_has_one_side` | WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337" (the sentence that says what ends a series of the count) |
| 2159 | `test_a_fixed_issue_whose_fix_is_not_a_commit_and_the_other_fates_give_no_comparison` | WAY-339 "That comparison is made for each fixed issue of the register" |
| 2176 | `test_a_version_whose_answer_is_unknown_stands_on_neither_side` | WAY-339 "The audit shows each series as an image of all its cycles"; the pointer to WAY-330 moved into the comment under the line, as "(WAY-330: an unknown value comes with its reason)", since the line may carry no text after the quotation |

Choices of sentence: 2050, 2080 and 2095 each cite the one sentence of WAY-339 that holds the passage they had quoted ("never its date, deciding its group", "both groups of that series"); 1975 cites the Q2 sentence because the test asserts the sums of each side; 2129 cites the first sentence of WAY-339, which says that a change of the reviewer's instructions ends a series of the count, which is what that test is about. The reviewer lists the sentences; the check accepts all.

Evidence:
- Before: `python -B elements/common/foundation_check.py` at `f52c5657` (a worktree of it, removed): exit 1, `12 errors`; `python -B -m unittest elements.common.test_foundation_check.FoundationCheckTest.test_the_way_foundation_check_reports_no_error` there: exit 1, `FAILED (failures=1)`. This is the invariant `own-foundation-check-report`'s test, seen failing.
- After: the same two commands at the fixed head: exit 0, `0 errors`; exit 0, `OK`. `python -B gate/run_tests.py elements/common`: exit 0, 289 tests OK.
- No other `decision:` or `invariant:` line of the files of slices 6 and 7 is reported (`0 errors`).

### I2 — fixed, way (a)

The Q2 sentence of WAY-417 (`foundations/decisions.md:9002-9005`) now reads: "The answer Q2 of such a group is the answer that the sum of the slices planned and the sum of the slices returned too large over its cycles whose plans are read give, and the image of a series and each side of a comparison show the two sums beside it." The *Verification* examples hold nothing of Q2, so they stay. WAY-339 is not touched.

`process-audit/SKILL.md` (the paragraph of "The answers are these") and the prose of `process-audit/audit_report.py` (the paragraph under the *Process versions* heading) say the same: Q2 is the answer the sums give; the image and each side show the two sums; the row of a version shows *Plans read* and the answer. While rewriting that paragraph I corrected one more sentence of it that was wrong against the result: it said Q3 "stands only in the row of a version", while a series of the cost also gives Q3 beside the side after of a comparison. No code and no expected value of a test changed.

Check: `python -B elements/common/foundation_check.py` exit 0, `0 errors` (it reads the binding sentences of WAY-417 and the lines citing it); `python -B gate/run_tests.py process-audit` exit 0, 344 tests OK.

### Minor 1 — fixed (`task-cycle/gate_times.py`, the rule of the cap)

Rule written: besides the old counts, each summary line now keeps one more number: how many lines `== ` at the start of a line stand after the last line of its segment that holds `== ` after text (`Times.mark`, the fourth element of the tuple in `latest` and `earlier`). Where the segment holds such a line, the nested run begins there (its first directory is that line's), so `Times.nested` takes `min(lines after that line, <m>, surplus)` in place of `min(lines, <m>, surplus)`. Where the segment holds no such line the old rule stands unchanged, which is what the tests of crafted output with no text before a nested directory (`test_the_lines_taken_are_those_before_a_summary_line_and_no_more_than_it_counts` and the like) need. Memory is still bounded: four integers for each of at most 100 kept summary lines; the exit code, the `Error:` forms and the relay are untouched.

Tests written first, seen failing (`cd task-cycle; python -B -m unittest test_gate_times.NestedRunTest`: exit 1, `FAILED (failures=5)`: the two for this finding and the three for Minor 2 and 3 below):
- `test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time` (case A): got `[other 0.002, gate1 0.001, y1 0.600]`, expected `other 0.002, gate1 0.500, gate2 0.600`.
- `test_a_whole_nested_run_beside_one_cut_off_is_read_by_the_one_with_a_summary_line` (case C, which I wrote from the handoff's words, since I did not read the review of slice 2: a whole nested run in `gate1` beside one cut off before its summary line in `gate2`): got `[other 0.500, gate2 0.004, y2 0.005]`, expected `[other 0.002, gate1 0.500, gate2 0.004, y2 0.005]`. The cut-off run is read as `test_a_nested_run_cut_off_before_its_summary_line_is_read_as_before` documents (`y2` stays a block and `gate2` takes the first Ran line of its text); only the whole run is now read right.
- After: the same command, exit 0, 43 tests OK; `python -B gate/run_tests.py task-cycle`: exit 0, 554 tests OK (2 skipped on Windows).

What the rule costs: it takes any line with `== ` after text as the start of a nested run. If a later line of the same segment, after the nested run's first line and before its summary line, also holds `== ` after text (a traceback source line such as `assert a == b` in the nested run's own failure report), the nested run is read as beginning there and the lines before it are taken as blocks (under-taking). I ran this case by hand: `[other 0.002, gate1 0.001, y1 0.500]`, which is the misreading the old rule gave for A. The old rule over-took in the case A shape and this one under-takes in a shape that needs the nested output itself to hold a line `... == ...` after text. Choosing the first such line of the segment instead of the last would reverse the failure (a spurious line before the nested run). I kept the last, as the reviewer's direction does; neither is tested, and in the-way only `gate/` prints a nested runner output.

### Minor 2 — fixed

The time a `Ran` line gives is now `[0-9]{1,9}(?:\.[0-9]{1,9})?`; a `Ran` line with more digits is no time line (the next `Ran` line is the block's time), and the count of tests in it is `[0-9]{1,9}`. The kept strings are at most 19 characters, so the 100 pieces keep nothing near `LINE_LIMIT` each. Tests (seen failing in the run above): `test_a_ran_line_with_a_time_no_run_prints_is_no_time` (5000 digits: got the huge string, expected `0.5`) and `test_a_flood_of_blocks_with_huge_times_keeps_the_memory_bounded` (300 blocks each with a time of 100000 digits: peak 10124940 bytes, limit 2000000).

### Minor 3 — fixed

`SUMMARY` now uses `[0-9]{1,9}` for both numbers. Test, written first and seen failing in the same run: `test_a_summary_line_of_digits_no_run_prints_is_no_summary_line` (Arabic-Indic digits; got `[a unknown, c 0.003]`, expected `[a 0.001, b 0.002, c 0.003]`).

### Minor 4 — fixed

`process-audit/SKILL.md` (the sentence "Name together, in one matter, the series whose rows give nothing but `unknown`") now reads "(for Q1, a series whose every version reads `yes 0 · no 0 · unknown n`)" after it, the reviewer's clause.

### Minor 5 — fixed

- `process-audit/audit_count.py`: lines 157/160/201 of the finding were rewrapped (the docstring only); 157 was 99 characters, 160 and 201 were over 100. The check that the syntax tree of the file apart from the module docstring equals that at the base `268b2b07`: true (a one-off script comparing `ast.dump` with the first statement replaced by `pass`; not kept).
- `process-audit/audit_report.py`: the new string at line 176 rewrapped as part of I2.
- `elements/common/reaching_another_skill.md`, the replaced paragraphs of the 15 skills (the files in the diff `268b2b07..f52c5657` that carry `reaching_another_skill.md`, the paragraph of each from its first line to its end) and `task-cycle/skill/return_step.md` (the paragraph through its sentence ending "no entry is written."): rewrapped to 100 characters. No word changed. Not rewrapped: `elements/environment-facts/template.md` (point 1's verbatim sentence; its line 111 is 102 characters) and `task-cycle/record_template.md` (line 206, 101 characters), which the finding does not name.
- Checks: `python -B gate/run_tests.py agent-instructions` exit 0 (53 tests OK, run after the commits so that the files are tracked); `python -B gate/run_tests.py product-guidelines` exit 0 (14 tests OK).

### Minor 6 and 10 — no action, as the handoff says

6 is taken into I2. 10 (the sentence of the part map for `elements-common`) is left to the return step.

### Minor 7 — fixed, one of the two ways with a narrower condition

Chosen: the reviewer's way (b), that a comparison stands only where a value stands, but with the condition "a cycle of either side gives a value of any measure" in place of "a value on both sides". `mechanism_comparison` returns no rows and no unknown values where no cycle of either side gives a value of any of the 15 measures.

Why this and not (a), one row with `—`: the task's rule asks for a comparison where cycles stand on both sides of a fix, and for the gate times it already limits itself, in the same point, to runs compared; a comparison with no median on either side has nothing to compare and nothing to quote, while a row of `—` per issue would still make a table of nothing for each fixed issue of a register that grows. Why "either side" and not "both": a side that has data against one with none is information (the fall is `unknown` with its reason), the existing tests of the unit and of the whole result expect those 30 rows, and the finding names only the empty case, so the smallest change is the empty case. What it costs: a reader of the result no longer sees that an issue stood in the series with no data on either side; the versions' own rows of `—` and their lines in *Unknown values* say that no cycle of those versions gave a value. If the human wants a line per such issue, it is one unknown value to add.

Tests: `test_cycles_on_both_sides_that_give_no_value_of_any_measure_give_no_comparison` (written first; `cd process-audit; python -B -m unittest test_series_summary.MechanismComparison`: exit 1, `FAILED (failures=1)`: got 30 rows, expected none) and `test_a_value_on_one_side_alone_still_gives_the_comparison_with_its_unknown_falls` (passes before and after: it keeps the neighbouring behaviour from being narrowed). After: `python -B -m unittest test_series_summary` exit 0, 49 tests OK; `python -B gate/run_tests.py process-audit` exit 0, 344 tests OK. The prose of `process-audit/SKILL.md`, `process-audit/audit_report.py` and the docstring of `process-audit/audit_count.py` says where the comparison of the mechanism measures stands.

### Minor 8 — fixed

The sentence in `process-audit/audit_report.py` now reads that *Unknown values* says why the answer of a version or the verdict of a comparison is unknown, a cycle's Q1 included, and that the reason of an unknown answer of an image or of a side follows from the lines of its versions.

### Minor 9 — fixed

`AuditCountCase.section` (`process-audit/test_audit_count.py:304-311`) removed, not corrected: its only users are in `process-audit/test_process_versions.py` and `VersionsCase.section` (`:91`) overrides it; no other test file calls `section`. `python -B gate/run_tests.py process-audit` exit 0.

## Checks (each as command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` | 0 | 289 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 554 tests OK, 2 skipped on Windows |
| `python -B gate/run_tests.py process-audit` | 0 | 344 tests OK (about 9 minutes while other runs went at once) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 53 tests OK |
| `python -B gate/run_tests.py product-guidelines` | 0 | 14 tests OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| Failing runs of the tests written first: `cd task-cycle; python -B -m unittest test_gate_times.NestedRunTest` | 1 | 5 failures for the expected reasons (above) |
| `cd process-audit; python -B -m unittest test_series_summary.MechanismComparison` | 1 | 1 failure (above) |
| At `f52c5657`: `python -B elements/common/foundation_check.py` and the invariant's test | 1 and 1 | 12 errors; `FAILED (failures=1)` |

The full gate of the product was not run, as the method says. The `process-audit` run was made after the last commit that changes `process-audit`; the `task-cycle` run after the last commit that changes `task-cycle` files (`3fab989a`, whose rewrap was also followed by `python -B -m unittest test_gate_times`, 43 tests OK, before the commit). The linter and the formatter are run by the invariants' tests inside `agent-instructions`, which passed; no `ruff` of my own was run, as it is not installed outside the gate's environment.

## Own-work check (WAY-164)

Requirement most likely unmet: point 8 of the task, "the lines `== …` of a nested run are no directories, and the directory where the test failed gets its own time", for an output the planned rule did not foresee. The check: cases A and C as tests, and by hand the case where the nested output itself holds a line with `== ` after text (a source line of a traceback). It showed that A and C are now read right, and that the by-hand case is misread in the other direction, the under-taking described under Minor 1; it is not covered by a test and not fixed, since it needs a choice between two heuristics that the reviewer's direction already made. A second weak point: the narrower condition of Minor 7 (either side) is my reading of the finding; the report above gives both its reason and its cost.

Mutations considered: the old `lines` in place of the tail (A and C fail); `\d` back in `SUMMARY` (the Unicode test fails); no bound on the `Ran` time (the two tests of Minor 2 fail); the `any(...)` guard of `mechanism_comparison` removed (the new unit test fails), or turned into `all(...)` for both sides (the one-sided test fails). Not caught by any test: a nested run with a line `== ` after text inside its own text (the by-hand case).

## Reaches beyond the handoff

- `elements/common/foundation_check.py`, the passages `check_decision_line` and the text of the check's description (lines 60-100 and 840-960), to learn what a quotation must be.
- `foundations/decisions.md`, the heading of WAY-330 only (to quote it in a comment).
- `process-audit/version_analysis.py` (`count_rows`, `mechanism_rows`, `compare_series`'s neighbours, the `Series` class), `process-audit/series_summary.py` whole, and the passages of `process-audit/audit_report.py` and `process-audit/test_series_summary.py` and `process-audit/test_process_versions.py` that the findings name, to settle I2 and Minor 7.
- `task-cycle/test_gate_times.py` lines 1-370 whole (the nested-run tests), the rest by search.
- `git diff 268b2b07 HEAD` of `process-audit/SKILL.md`, `process-audit/audit_count.py`, the 15 skills and `task-cycle/skill/return_step.md`, to see which paragraphs the cycle replaced.
- `the author's global rule file for scripts` and `git.md` (the author's rules for scripts and commits).
- `agent-instructions/test_linter_invariant.py` by search, to see how the linter and the formatter run.

## Working copies

- A worktree of `f52c5657` at `.runs/fix-1/head`, made to see the check fail at the head: removed with `git worktree remove --force`, then `git worktree prune`.
- The directory `.runs/fix-1/` (logs of the test runs, a listing of paragraphs): removed. No remainder.
- One-off scripts of Python were given by the shell and left no file.

## Unread material

- `plan.md`: not opened, as the handoff says.
- Decisions: WAY-339, WAY-350 and WAY-417 read whole. WAY-385 (`11143-11190`), WAY-416, WAY-199, WAY-127 and WAY-256: not read. The change did not add to a function over a threshold of the rule of size (the additions to `Times` are a few lines), so I did not need WAY-385; I did not check function sizes against it.
- Invariants: `gate-times-refuses-impossible-entry` (`541-550`) read; `own-foundation-check-report`, `audit-count-refuses-record-links`, `command-runner-passes-exit-code`, `ruff-blocking-rules`, `formatter-layout`, `function-and-file-size` and `audit-series-script-paths`: not read as entries (their tests ran in the gate directories above).
- `foundations/part_map.md` entries `task-cycle`, `process-audit`, `elements-common`: not read.
- Guidelines: `guidelines/coding.md`, `guidelines/testing.md`, `guidelines/coding-command-runner.md`, `guidelines/coding-measuring-report.md` and `guidelines/coding-shared-module.md` read whole.
- Files I changed: `task-cycle/gate_times.py`, `process-audit/series_summary.py`, `task-cycle/test_gate_times.py` lines 1-370 and the rest by search, `process-audit/SKILL.md` lines 205-300, `process-audit/audit_report.py` lines 60-200 and 228-275 and 322-345, `process-audit/audit_count.py` lines 1-30 and 138-210, `process-audit/test_series_summary.py` lines 1-60 and 370-440, `process-audit/test_process_versions.py` the passages around the twelve lines and 1985-2040, `process-audit/version_analysis.py` lines 585-660, 771-850 and 1000-1045: read in those parts only, not whole, since the files are large.

## Searches not found or unclear

- Cases A and C of the review of slice 2 are not in my handoff beyond A's actual and expected rows and C's one-line description; I built the inputs of both tests myself from those words (the names `gate1`, `gate2`, `x1`, `y1` are mine). If the reviewer's own inputs differ, they are not covered by what I wrote.
- The handoff says to check "each of the twelve lines and also any other `decision:` or `invariant:` line of the files of slices 6 and 7 that the check reports": the check reports no other.
- The handoff's wording "the Markdown files of point 9" and "the 15 skills": I took them to be the 15 `SKILL.md` files that carry the sentence `elements/common/reaching_another_skill.md` in `git diff 268b2b07..f52c5657`, which are 15 (the 16 files listed under the commit's paragraphs include `task-cycle/skill/return_step.md`, which is not a skill).
