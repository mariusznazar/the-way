# Report of correction 1, for the human's remarks on the open request

**Status:** done with concerns (one case of the timing script is still read wrong; it is named below with its evidence)

Worktree `the worktree root`, branch `task/small-fixes-from-ai-review-and-audit`, from `54b28445be17c4580cb2477c71dc6dd2b9076fc3`. Clean, not pushed.

## Commits (range `54b28445..2dd1bbb0`)

| Commit | What |
|---|---|
| `229a3b84` | The lines `decision:` (M2) and the corrected comment (M1) in `process-audit/test_process_versions.py` and `process-audit/test_series_summary.py` |
| `ff33314c` | The rule of the timing script and its tests, `task-cycle/gate_times.py` and `task-cycle/test_gate_times.py` |
| `2dd1bbb0` | A test name of `task-cycle/test_gate_times.py` shortened to the width the formatter keeps (the gate's formatter test failed on it at `ff33314c`; see the checks) |

## Each remark as made, and how it was met

### Item 1, the timing script (Minor finding 1, N1)

Remark: the rule must read both cases right (the one the old rule read right, the one my fix repaired), with a test for each, the confirmed input of N1 as one of them.

Rule written (`task-cycle/gate_times.py`, `Times.line`, `Times.summarise`, `Times.nested`). Besides what the segment before an earlier summary line held, the script now keeps, for the segment, the places (the number of lines `== ` at the start of a line read so far) of the last 100 lines that hold `== ` after text, each place once. At a summary line with `<m>` directories it checks whether one of those lines stands before exactly `<m> - 1` of the lines `== ` that follow it up to the summary line. If one does, it is the nested run's first directory (it stands after text), so the nested run has `<m> - 1` lines at the start of a line and `Times.nested` takes `min(lines, <m> - 1, surplus)`. If none does, the old rule stands: `min(lines, <m>, surplus)`. The marks are cleared at each summary line. Memory is bounded (a deque of at most 100 integers, which a new test floods); the exit code, the `Error:` forms and the relay are untouched; the numbers of a `Ran` and a summary line stay ASCII and of at most nine digits.

This differs from the reviewer's direction, which takes `<m> - 1` wherever the segment holds any such line. I judged that direction against the cases and kept the exactness check, because a nested run whose first directory stands at the start of a line (a printed output) and whose segment holds an unrelated line `== ` after text (for instance a traceback line of an earlier directory) would lose a line under it, while under mine such a segment is read by the old rule unless the unrelated line stands at exactly that place.

Cases, each run by the test file (`python -B -m unittest discover -s task-cycle -p "test_gate_times.py"`, 46 tests):

| Case | Test | Read |
|---|---|---|
| A: two directories each print a nested run | `test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time` (written at the fix; stays) | right |
| C: a nested run cut off before its summary line beside a whole one | `test_a_whole_nested_run_beside_one_cut_off_is_read_by_the_one_with_a_summary_line` (stays) | right, the cut-off run read as before (`y2` a block, `gate2` takes the nested run's first Ran line, as `test_a_nested_run_cut_off_before_its_summary_line_is_read_as_before` documents) |
| N1, the confirmed input: first directory `a` after text, `== b` whose failing test prints `    assert x == y`, `== c`, the nested summary of 3 directories, the enclosing `Ran` line, the run's own summary of 1 | `test_a_line_with_a_comparison_in_a_nested_failing_test_cuts_no_lines_taken` (new) | right: `[ ['gate', '0.500']]`. Failing first, at `2dd1bbb0`'s parent state of the rule: `[ ['gate', '0.001'], ['b', '0.500']]`, exit 1, `FAILED (failures=1)` |
| A line with `== ` after text in the enclosing traceback before the failure message | `test_a_line_with_a_comparison_before_the_failure_message_cuts_no_lines_taken` (new; passes before and after, it pins the neighbour) | right |
| Nested run with no line `== ` after text at all (crafted, first directory at the start of a line) | the tests already in the file, such as `test_the_lines_taken_are_those_before_a_summary_line_and_no_more_than_it_counts` | right (old rule) |
| Every other test already in the file | `task-cycle/test_gate_times.py` | unchanged and passing |
| Memory | `test_a_flood_of_lines_with_a_comparison_keeps_the_memory_bounded` (new) | peak under 2 MB |

Hand cases beyond the tests (one-off script, not kept): the case I reported in fix 1 (a line `    assert a == b` after the nested run's first line, before its summary) gives `[other 0.002, gate1 0.500]`, right.

Case still read wrong (the reason for the status): a nested run whose first directory stands at the start of a line, with a line that holds `== ` after text exactly between its first and second directory (for `<m> = 2`; in general with exactly `<m> - 1` lines `== ` after it). Hand input: `== gate`, `F`, a passing `x`, `    assert p == q`, a passing `y`, the nested summary of 2, `Ran 1 test in 0.5s`, the run's summary of 1. It gives `[ ['gate', None], ['x', '0.5']]` where `[ ['gate', '0.5']]` is right. The old rule read it right, the reviewer's direction would read it wrong in this and in more cases, and no rule of counts alone tells the two readings apart, since the line looks the same either way. It needs the nested output itself to hold such a line at that exact place, and in the-way only `gate/` prints a nested runner output. I did not write a test that pins the wrong reading.

The trust boundary: crafted input stays refused. The registry's refusal of impossible files (invariant `gate-times-refuses-impossible-entry`) is untouched and its tests pass; the new rule reads only bounded numbers and keeps bounded memory.

### Item 1, the markers `decision:` (Minor finding M2)

Before writing I read WAY-02 whole (`foundations/decisions.md:458-500`, its heading to the next heading) and WAY-12 whole (`:766-830`). Lines added, each quoting the start of a binding sentence of the decision it names, word for word, on its line, with nothing after the quotation; no binding sentence of any decision changed. After the change `python -B elements/common/foundation_check.py` gives exit 0, `0 errors`.

In `process-audit/test_process_versions.py` (tests found by name; the line numbers are those of the head):
- `test_medians_and_falls_of_three_versions_over_an_odd_and_an_even_number_of_cycles` (`:1293`): `decision: WAY-417 "The answer Q3, whether the median cost"`
- `test_the_gate_times_take_only_runs_with_no_other_gate_and_show_the_others_apart` (`:1354`): the same line
- `test_a_series_of_two_versions_with_two_cycles_each_has_an_image_of_each_kind` (`:1709`, Q1 in the image): `decision: WAY-417 "The answer Q1 of the audit, whether a contradiction"`, beside its two existing lines
- `test_the_count_of_remarks_gives_the_two_sides_and_no_answer_of_its_own` (`:1974`, Q1 on each side): the same Q1 line, beside its existing `WAY-417 "The answer Q2 of such a group"`
- `test_the_gate_times_compare_the_runs_compared_and_show_the_others_apart` (`:2012`): `decision: WAY-339 "The audit shows each series as an image of all its cycles"`, beside its WAY-350 line. That is the sentence of WAY-339 that holds "for the times of the gate both take only the runs that WAY-350 compares".

In `process-audit/test_series_summary.py`: `Q1Numbers.test_the_numbers_are_those_of_the_cycles_answering_each`, `CountImage.test_the_image_gives_q1_as_numbers_and_the_sums_of_q2` and `CountComparison.test_each_side_gives_q1_as_numbers_and_the_sums_of_q2_and_no_answer` carry the Q1 line; `GateComparison.test_each_measure_has_a_pair_of_rows_with_the_runs_compared_and_not_compared` carries the WAY-339 line.

Choice: I put the Q1 line also at `CountComparison`, which the review named only as "the sides"; it is the unit test of the same part as `:1974`. I did not add the WAY-350 sentence to the two tests of the rows of the versions, which the review did not ask for.

### Item 1, with it (Minor finding M1)

The comment at `process-audit/test_series_summary.py:93` ("Five cycles, as the verification of WAY-417 gives: …") now reads "Five cycles: two yes, two no and one unknown." (the review's own suggestion), and the test carries the Q1 line above it.

### Item 2

Nothing asked for WAY-161, WAY-263, WAY-363, WAY-365 and WAY-409: let through. WAY-02 read whole, as said above; the reviewer of the correction reads it whole too.

### Minor finding 2

Not changed (`process-audit/SKILL.md:258` and the docstring line of `process-audit/audit_count.py`).

## Return step (what the correction touches)

Compared with the code: WAY-339's clause on the gate times (the series and the comparison take the runs WAY-350 compares: the code that does it, `process-audit/series_summary.py` and `process-audit/version_analysis.py`, is untouched; the timing script only changes which lines it takes as nested); WAY-350 (registry and runs compared: untouched); the invariant `gate-times-refuses-impossible-entry` (the registry's refusal: untouched, its tests pass) and `command-runner-passes-exit-code` (the script ends with the command's own exit code: untouched, its tests pass); the clauses `tests:` of WAY-339 and WAY-417 against the lines added (each part they name is now reached through the sentence it holds). Nothing no longer matched; no entry and no part map changed.

## Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` | 0 | 46 tests OK (1 skipped on Windows); before the rule, 1 with `FAILED (failures=1)`, the N1 test |
| `python -B gate/run_tests.py task-cycle` | 0 | 557 tests OK (2 skipped on Windows) |
| `python -B gate/run_tests.py process-audit` | 0 | 344 tests OK (made after the commit `ff33314c`; no file of `process-audit` changed after it) |
| `python -B gate/run_tests.py elements/common` | 0 | 289 tests OK (made at `ff33314c`) |
| `python -B gate/run_tests.py agent-instructions` | 1, then 0 | at `ff33314c` it failed: the formatter test reported a test name of `task-cycle/test_gate_times.py` over 100 characters (`test_a_flood_of_lines_with_a_comparison_between_blocks_keeps_the_memory_bounded`); I shortened the name (`2dd1bbb0`), and the rerun gave exit 0, 53 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors`, run after the lines `decision:` and at the end |

The full gate of the product was not run.

## Own-work check (WAY-164)

Requirement most likely not met: "make the rule read both cases right" for every input a nested run can make. The check: the confirmed input of N1 as a test (seen failing, then passing), cases A and C, the enclosing-traceback case, every old test, and three cases by hand: the earlier `assert a == b` after the first line (right), a nested run at the start of a line with no marker (right, old rule), and a nested run at the start of a line with a marker at exactly the place of the nested first directory (wrong, described above). So it is not met for that last input, the one case that is named under "still read wrong".

Mutations considered: the old `tail` rule (the N1 test fails); `directories` in place of `directories - 1` where a marker stands (A and the N1 test fail); `directories - 1` always (the old tests of crafted output with no marker fail); the marks not cleared at a summary line (the second nested run of A would count the first's marks; the A test catches the wrong take only where counts coincide, so I do not claim it); the deque unbounded (the memory test fails).

## Reaches beyond the handoff

- `foundations/decisions.md` for WAY-02 and WAY-12 (whole, as the handoff asks) and the `tests:` clauses of WAY-339 and WAY-417 (read to pick the sentence for each line).
- `foundations/invariants.md:491-500` (`command-runner-passes-exit-code`).
- `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-return-step-report.md`, its M2 and the passages around it (the handoff names the file).

## Working copies

`.runs/correction-1/` held only logs of the test runs; removed. No remainder.

## Unread material

- The review of my fix (the source of the N1 input) and the report of the review of slice 2: not opened; I took the N1 input and the cases A and C from the handoff and my fix report.
- `review-return-step-report.md`: read lines 25-70 (M2) and searched for the rest; not read whole.
- WAY-350 and WAY-339 were read whole in the earlier round and not again; the invariant `gate-times-refuses-impossible-entry` was read at `:541-550` in the earlier round.
- `foundations/part_map.md`: not read.

## Searches not found or unclear

- The handoff's line numbers (`:2012`, `:1709`, `:1974`, `:1293`, `:1354`) are those of the head `1eaa3c4f`; the tests were found by name, and the lines I added moved the numbers.
- The reviewer's direction for the timing rule ("take `min(lines, <m> - 1, surplus)` where the segment holds a marker") is judged against cases in the report and not used as written; the reason is under "Rule written".
