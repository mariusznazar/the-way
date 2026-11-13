# Fix report — slice 1 (fix of the review's findings)

**Status:** done

**Commits:** `f0a3829..dae0de6` on `task/audit-numbers-mechanism-measures`
- `dae0de6` Read a missing time or id as an error, and catch the JSON reader's other errors

**Files changed** (the slice's own files only):
- `task-cycle/cycle_measures.py` — 22 lines changed
- `task-cycle/test_cycle_measures.py` — 74 lines changed

## Findings

**I1 — fixed.** A hostile transcript or meta file ended with a traceback and exit 1.
- How: the transcript line read and the meta read now catch `ValueError` and `RecursionError` (the parent of `JSONDecodeError` included). A transcript line error names the file and line; a meta error names the meta file.
- Checks: `test_a_line_nested_too_deeply_ends_with_exit_2_naming_the_file_and_line` (200000-deep line), `test_a_number_of_more_than_4300_digits_ends_with_exit_2_naming_the_file_and_line` (5000-digit number in an assistant line), `test_a_meta_file_with_a_number_of_more_than_4300_digits_ends_with_exit_2_naming_it`. Each asserts exit 2, an `Error:` line naming the file (and line where there is one), and nothing written.
- Mutation check (scratchpad copy): narrowing the transcript catch back to `JSONDecodeError` killed by the tests; narrowing the meta catch back killed by the tests.

**I2 — fixed, per the orchestrator's ruling.** `timestamp` and `message.id` are needed fields.
- How: `read_time` replaces `parse_time`; a missing or unreadable `timestamp` ends with exit 2 and an `Error:` naming the file, line and `timestamp`. A missing, empty or non-text `message.id` ends the same way, naming `message.id`. The `line <n>` id fallback and the earliest-time fallback are removed.
- Checks: `test_a_response_without_message_id_ends_with_exit_2_naming_the_line_and_field`, `test_a_response_without_timestamp_ends_with_exit_2_naming_the_line_and_field`, `test_a_response_with_unreadable_timestamp_ends_with_exit_2_naming_the_field` (`timestamp: 12345`).
- Mutation check: restoring the id fallback is killed by the tests. Reading the timestamp with `.get` (a missing value then gets the "not a time" wording, not "no field") still exits 2 with the file, line and `timestamp` named; the test passes, so that mutant is equivalent for the contract, not a gap.
- Note: the new tests were written after the code in this fix, not before. The mutation checks above show they fail on the old behaviour.

## Checks

Run from the worktree root, after the fix commit:
1. `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` — exit 0, 35 tests OK.
2. `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` — exit 0.
3. `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` — exit 0.
4. `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` — exit 0.

Real session, read-only: `python -B task-cycle/cycle_measures.py` (the session id from `CLAUDE_CODE_SESSION_ID`) — exit 0, 27 lines written to stdout, no stderr.

Not run: the product's gate, by instruction.

## Own-work check

Requirement most likely unmet: a hostile input that still escapes as a traceback at a reading not covered by the new tests. Check: the reads are the transcript line `json.loads`, the meta `json.loads`, and the field reads; each new error path has a test, and the real-session run succeeds. Result: no escape found in the tests above; the real session still reads.

## Unread material

- None of the dispatch's named files were skipped. `task-cycle/change/fix.md` and `SKILL.md` were read whole. The findings file and the handoff were read whole.
- `reports/slice-1-review-report.md` (the reviewer's full report) was not opened; the findings file was taken as the statement of the findings, as the handoff directs.

## Searches not found or unclear

- None beyond the previous report's open points (nested subagent folder layout; Codex refusal).

## Reaches beyond the handoff

- None to other files. Read the user's scripting rule before the earlier probe; no new reach.

## Choices made

1. A `message.id` that is an empty string counts as missing and ends with exit 2. Rejected: accepting an empty id as a value. Cost if wrong: a transcript with empty ids would stop the run; none is known.
2. The timestamp error wording is "not a time" for a present but unreadable value, and "no field timestamp" for a missing one. Rejected: one wording for both. Cost: none for the contract.
3. The minor findings M1–M3 of the review are not touched, per the handoff.
