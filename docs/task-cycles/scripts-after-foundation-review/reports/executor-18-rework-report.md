# Report — executor of slice 18, rework (the list *Unknown values* grouped for every value)

**Status:** done
**Commit:** `881c1ea` ("Group every unknown value of the audit count by field and reason in one table"), on the task branch, by path: `process-audit/audit_count.py`, `process-audit/test_audit_count.py`, `process-audit/SKILL.md`.

## What was made

- `process-audit/audit_count.py`: the section *Unknown values* is one table, `Field | Values | Why | First examples`, one row for each pair of a field and a reason, over **every** unknown value (the cycles' values, the values of `analysis.unknown`, of the versions and of the measures, and the register's held-back values). The field is the value with the number of its row (`row of ...`), the name of an issue (`the fix of an issue`, `waiting of an issue`) and the commit of a version (`..., a version`) taken out; the count is the number of values of the pair, the examples are the first three in the order the values come, each `repository record: value`. Every cell goes through `cell`, as before, so a bar, a control character and a long text of crafted input reach the result as before (cut, one line, no bar). The old two tables, `register_unknown_rows` and `REGISTER_UNKNOWN_HEADER` are replaced by `unknown_rows`, `unknown_field` and `UNKNOWN_HEADER` (new constants `ISSUE_VALUE`, `VERSION_SUFFIX`).
- Text: the module description (the sentence in the paragraph on the register, and the description of the result's section), the intro paragraph of the section in the result and `process-audit/SKILL.md` (step 1 of the session) now say: the result keeps the count and three examples of each pair; the full list of a pair is in the register for the register's own values (its refused rows and the problems of a cycle it names), and in the copies of the cycles' records in git history and in a new run of the count for the cycles' values. The sentence "one line in *Unknown values*" in two places is now "a value in *Unknown values*". No sentence claims more.
- `process-audit/test_audit_count.py`: the helper `rows("Unknown values")` decodes the examples of the table into repository, record, value and reason (complete wherever a pair has at most three values, as in the tests that read them); `pair_rows()` is the whole table; `register_pair_rows()` is the pairs of a row or a table of the register. The test of slice 9's fix (four cycles of an unknown pin) now expects one pair with count 4 and three examples (the four cycles have one missing pin, so one reason). Four tests that expected only the register's pairs in the table read `register_pair_rows()`. No test holds a `decision:` line; no invariant's test changed.

## Tests, red first

New tests (in `RegisterCount`): `test_more_than_three_values_of_a_pair_are_counted_and_three_are_listed` (five cycles with no `stages.md`: one pair, count 5, three examples, no value past the third in the result), `test_issues_that_differ_only_in_their_names_make_one_pair_for_each_kind_of_value` (three fixed issues with one missing fix and two open issues of a cycle no repository holds: one pair each, names in the examples), and the changed `test_the_cycles_whose_pin_is_unknown_for_a_fixed_issue_make_one_pair_with_three_examples`.

- Red on the head (code unchanged, helpers new): `python -B -m unittest test_audit_count.RegisterCount.<the three tests>` from `process-audit/`, exit 1 (3 failures by assertion: the pair lists were empty or held other rows, the head giving one row for each value; a first run had one error of my own, a local name shadowing a function of the file, which I fixed before the red run counted).
- Green after the code: same command, exit 0, 3 tests OK.

## Checks (commands and exit codes)

- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`: first full run 230 tests, 4 failures (the four tests that expected only the register's pairs; fixed in the tests), exit 1; the final run 230 tests OK, exit 0.
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: 3 tests OK, exit 0.
- No run of the whole gate.

## The real run again (read only; counts and facts only)

Same method as the first run (a copy of the user's locations file, `audit_results` pointing to a directory under `.runs/executor-18/`, given by `--locations`; the original file, the register and the repositories only read; the result directory was not refused). Run on the code of the commit.

- Exit code **0**; **0 `Error:` lines** (stderr empty).
- *Unknown values*: **106 rows** in the one table (1605 values in all), against 1605 rows before this rework and 501 lines on the base. The section is 113 lines with its heading, intro and header. The run was made before the last edit of the tests only; the code is that of the commit.
- By kind (rows): per-version rows of the gate time falls 42 (a row for each directory and for the total time of the run, three versions in each) and of the measure falls 15 (one for each measure); Fix rounds share 7, Discarded attempt 5, Plan 4, Gate runs 4, "slices too large, a version" 4, Remarks 3, Working time without waiting for tools 3, Waiting for tools 3, Process pin 3, Slices returned too large 2, Mechanism measures 2, Cost 2, "cost falls, a version" 2, and one row each for Gate runs: Directory seconds, Gate runs: Directories, "contradiction only after code, a version", Mechanism measures of a version and Gate times of a version.
- The second table of the first run (the register's held-back values) had 0 rows and still has none: the register read without a refused row.
- The Codex and nested-helper measures: as in the first report, the register's repositories hold no Codex cycle, so none stand in *Mechanism measures*.

## Own-work check

- Requirement most likely unmet: the flood is cut (To do 10) without losing a reason, and nothing in the result claims more than it holds. Check: the real run above (106 rows for 1605 values, every pair with its count) and the three new tests; the sum of the "Values" column of the real result equals the 1605 values of the first run, so no value is lost, only grouped.
- A pair whose reason carries a specific name or commit does not group (the pin test needed one missing pin for its four cycles). The real run shows the kinds above; a reason naming a commit would show as several rows of one field. I did not normalise reasons.

## Choices and reaches beyond the handoff

- I normalised the field only by three patterns (row number, issue name, version commit); the reason is never changed, so a pair is exactly "field and reason". Rejected: normalising the reasons too — a reason is the text the human reads, and cutting a commit out of it would hide which one. Cost if wrong: some pairs of one kind appear in several rows.
- The directory name of a gate (`Gate time falls: Directory: <name>`) stays in the field: it is a kind of measure, not a name of one value. Rejected: one row for all directories — the series differ by directory.
- `process-audit/SKILL.md` was changed (one sentence of step 1): it repeated "the full list stays in the register" for the held-back values only. Beyond the handoff's *Change* list, within the part of the slice.
- Reached beyond the handoff: I read the commits `b6f800c` and `61171e9` (their diffs) to see what slice 9 and its fix changed, and the module text of `audit_count.py`; no other foundation entry.

## Unread material

The plan and task beyond the passages the first handoff copied; the decision log and invariants beyond the entries my first run read. I read the rework handoff whole.

## Searches not found or unclear

- None unclear. A `decision:` line in `test_audit_count.py`: not found (none).

## Working copies

`.runs/executor-18/` of the worktree (the copy of the locations file, the result directory, stdout and stderr, the log of the full test run) stood in the worktree and was removed before the commit; `/tmp` held a log of one test run, removed. No other copy was made.
