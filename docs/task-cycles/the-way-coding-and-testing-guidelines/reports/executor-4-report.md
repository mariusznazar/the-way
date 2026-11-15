# Report of the executor of slice 4

**Status:** done

**Commit:** `ced0fd9` — "End the stages script with exit code 2 at a missing token count of a Codex record and read a time with the letter Z as it is" (on the base `43d7d9b`).

## Files changed

| File | Added | Removed |
|---|---|---|
| `task-cycle/cycle_stages.py` | 30 | 13 |
| `task-cycle/test_cycle_stages.py` | 125 | 0 |

In `cycle_stages.py`:
- New function `codex_usage(payload, where)` reads `payload.usage` with `required`, then its three counts with `required_count`. These are the helpers of the Claude Code half, with its wording and `MissingFieldError`.
- `read_codex_agent` reads the file with `numbered_lines` instead of `read_lines`, and calls `codex_usage` for each `token_usage_record` of the agent's own thread (`thread_id` equal to the rollout's id). A record of another thread, which a forked rollout repeats from its parent, is not read, as before.
- `Usage` is built at the line, so the loop at the end only wraps it in a `Record`.
- `parse_time` is `datetime.fromisoformat(text)`; the replacement of `Z` is gone (cause 30, the place of this file; FURB162 no longer reports).
- The description at the head of the script no longer says that the reading of a Codex rollout checks no field. A paragraph states what it checks, and the exit-code paragraph names the Codex field next to the Claude Code one.

In `test_cycle_stages.py`:
- New class `CodexFieldsTest` with 9 tests: one each for a record with no `usage` and for a record without `input_tokens`, `cached_input_tokens` and `output_tokens`. Plus one for a `null` and a list as `usage` or count, one for the counts that are no whole number (-1, 1.5, "7", True, [1], 10**15, each of the three counts), one for a subagent's rollout naming that rollout, one for a record of another thread in a forked rollout, and one for a record with every count (zeros included) reading as before.
- `# invariant: cycle-stages-refuses-crafted-names` above `test_crafted_names_neither_break_a_row_nor_enter_the_column`.
- The made-up Codex records of the tests need no change: every one comes from the helper `tokens()`, which already gives `usage` with all three counts. I found no test whose Codex record lacks a field now needed.

## Checks (command and exit code)

- Failing run, at the base code with the new tests only: `python -B task-cycle/test_cycle_stages.py CodexFieldsTest` — exit 1 (9 tests, 18 failures, 6 errors). The failures are `2 != 0` (the script ended with 0 and counted zero tokens), and the errors are the script's own `TypeError` on a string or list count. Log: `reports/executor-4-failing-run.log`. A first failing run had a wrong expected row in my test of the forked rollout; I corrected the test and kept the log of the second run. The code was unchanged between the two.
- After the change: `python -B task-cycle/test_cycle_stages.py` — exit 0 (80 tests).
- Invariant test shown failing once: with `files_named` broken for a moment (the filter of a name reduced to `not name.endswith(".md")`, so lengths, `..` and a first character no longer refuse), `python -B task-cycle/test_cycle_stages.py ClaudeFilesNamedTest.test_crafted_names_neither_break_a_row_nor_enter_the_column` — exit 1 (a list of 200,212 characters instead of two names). Log, with the long line cut: `reports/executor-4-invariant-failing-run.log`. Restored from a copy and the same command — exit 0; `git diff` showed `cycle_stages.py` as the intended change only.
- `python -B process-audit/test_audit_count.py Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` — exit 0.
- `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/cycle_stages.py task-cycle/test_cycle_stages.py` — exit 1, one report: TRY004 at `cycle_stages.py:567`, the line of `required_count` that the slice did not touch (line 550 at the base). The FURB162 of the base is gone. Nothing on a line the slice wrote or changed.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0.
- Not run: the full gate (WAY-160), and `foundation_check.py` without `--skip-test-citations`, which I ran once for a look: it reports 10 errors and none names `cycle-stages-refuses-crafted-names`. The other nine invariants of Foundation entries that cite tests of later slices are not mine.

## The own-work check (WAY-164)

The requirement I judged most likely not met: "ends with exit code 2 and a first line `Error:` that names the file, the line and the field, and writes no result", also for crafted input at this trust boundary, and across the places a rollout is read (an orchestrator's, a subagent's, a forked one).

- Tests: the message is asserted whole (`Error: <path>:4: no field payload.usage.<name>\n`), with the output file not existing, for the orchestrator's rollout and a subagent's rollout (the path of the subagent's file); a forked rollout holding a parent record with no count reads with exit 0 and no warning.
- A run of crafted input at `read_codex_agent`, made in a script of my own in a directory of `.runs/` that I removed:
  - `usage` as a list, a text or an integer, and as `{}`: exit 2, `no field payload.usage.input_tokens`.
  - A count that is a list, `1e30` or NaN: exit 2, `is not a whole number`.
  - A timestamp `…30Z`: exit 0.
  - Outside what the slice changes: a timestamp that is an integer ends with `TypeError`, a lowercase `…30z` with `ValueError`, and a token record with no `turn_id` with `KeyError` (stack trace, no exit code 2). See below.

## Fields of the changed function that do not end with exit 2

WAY-344 binds the whole reading of a file whose reading a change reworks, and the handoff says the other fields stay. I read `read_codex_agent` and `codex_meta`. What is not checked, and so does not end with exit code 2:

- **Not checked, with a fallback or a skip:**
  - A line whose `payload` is no object, or with no `timestamp`: skipped.
  - `type` of a line, `payload.type`, `payload.model` of a `turn_context` (absent gives no model), `payload.thread_id` (a record with none is not the agent's and is not counted), `payload.call_id`, `payload.name`, `payload.input`, `payload.role`, `payload.content`, `payload.recipient`, `payload.message`, `payload.internal_chat_message_metadata_passthrough.turn_id`, and of `session_meta` `agent_path`, `agent_nickname` and `parent_thread_id`.
- **Not checked, and crash with a stack trace instead of exit 2 (observed on crafted input):**
  - `session_meta.payload.id`: `meta["id"]` is a `KeyError` where it is absent (read in the code, not run).
  - A `timestamp` that is no time: an integer gives `TypeError`, a text such as lowercase `…z` gives `ValueError`. Before my change an integer gave `AttributeError`; the class of the crash is the same.
  - `payload.turn_id` of a token record of the agent's own thread when no other line of that turn carries a `turn_id`: `first_seen[turn]` gives `KeyError: None`.
- The keys `total_tokens` and `thread_id` of a record are not read (the first) or read as the filter (the second). I did not make `turn_id` or `thread_id` required: the description of the script and its test records show neither to be always present for every line, and the handoff says not to make such a key required. Where the human wants them under the rule, the place is `read_codex_agent`, and each is one more `required(...)` and one test.

## Reach beyond the handoff

None. I read `task-cycle/change/SKILL.md` and `slice.md`, the passages of the task named by the *Read*, the end of `plan.md` ("Orchestrator's additions"), `foundations/decisions.md` WAY-344, WAY-48, WAY-235, WAY-08 and WAY-232 whole, and `foundations/invariants.md` entries `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation` and `cycle-stages-refuses-crafted-names` whole. I also read `ruff.toml` and the two files of the slice whole, except the middle of the test file (see Unread material).

## Working copies

A directory `.runs/executor-4/` with a copy of the good `cycle_stages.py` (for the moment of the break) and a log, a directory `craft/` of the crafted-input run, and a log `.runs/executor-4-fail.log`: all removed before I returned (`.runs/` holds only `task-cycles/`). The two failing-run logs stand in `reports/`.

## Choices

- **Same helpers for the counts, which refuse more than a missing count.** `required_count` also refuses a negative number, a decimal, a boolean, a text and a count of 15 digits or more, with "is not a whole number", as for Claude Code (the handoff says "the same helpers and the same wording"). Rejected: checking only presence — a Codex count of `"7"` would stay a stack trace on the sum. Cost if wrong: a real Codex rollout whose count is a decimal now ends the run with exit 2; the real format of Codex was not measured here (the task says the same for cause 3).
- **The check stands where the record is read, with the line number from `numbered_lines`.** Rejected: a check after the loop — the line number would be gone. Cost: `Usage` is made inside the loop, which changes the type of `raw`.
- **Records of other threads in a forked rollout are not checked.** The parent's own rollout is where they are read. Rejected: checking them too — one malformed record of a parent would then end the run twice, naming a subagent's file, and the test of the forked rollout protects this. Cost if wrong: none, they were not counted before either.
- **`required` and `required_count` stay under the heading `# Claude Code`** though the Codex function now uses them; no move, to keep the diff to the slice. A reader looking for them under `# Codex` will not find them; a move above `# Codex` is a separate change.
- **Test names and the `decision:` comment.** The four tests of a missing field carry `# decision: WAY-344 "Each reading of a file that the rule covers has one test"`, the same quoted passage the Claude Code test of the reading carries.

## Weakest point

The tests of "not a whole number" assert the exact message for six values per count, but no test fixes that a Codex count of exactly 10**15 - 1 is accepted (the Claude Code half has one). A mutation of `TOKEN_DIGITS` is caught by that half's test, since the helper is shared. Mutations I thought of and the test that catches each: reading `usage` after the thread filter's removal — the forked-rollout test; a wrong field name in one of the three counts — the test of that count; `get(..., 0)` instead of `required` — the four tests of a missing field; the line number off by one — the assertion of `:4:`; a result written before the error — `assertFalse(output.exists())`.

## Problems as observed

- The handoff file did not exist yet when I was dispatched; I read it after the coordinator's message. No effect on the work.
- A mismatch with the slice text: "the tests whose made-up Codex records lack a field now needed are given it" — none lack it (see above).

## Unread material

- `foundations/part_map.md:101-111` (`task-cycle`): not read; the slice adds no file and no part.
- `foundations/invariants.md`: of the entries the orchestrator's additions name for a slice that adds files at the root or under `guidelines/`, none applies to this slice, and I did not read `repository-file-location`, `ci-checking-commands`, `tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target` and `derived-file-content`.
- `task-cycle/test_cycle_stages.py`: read the lines 1-140, 256-282, 508-770, 903-1000, 1100-1250 and 1343-1372 and the list of its tests; the rest I did not read, and none of it reads a Codex token record other than through `tokens()`.
- `task-cycle/cycle_stages.py`: read lines 1-760 and 960-972 and 1085-1130; the report-writing part (lines 760-1085) I did not read.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` and `plan.md`: only the passages the handoff names, and the end of the plan.

## Searches not found or unclear

- The handoff file `executor-4-handoff.md` was not found at my first read (it was written after the dispatch); read afterwards.
- A test that gives a Codex record without a field in the tests of the task-cycle part: searched `token_usage_record` in all `.py` files outside `.runs/`; found only the helpers `tokens()` of `test_cycle_stages.py` and `test_cycle_measures.py` (the latter is `cycle_measures`, not this slice) — none without a field.
- The line anchors the task gives for the cited test (`task-cycle/test_cycle_stages.py:707`) no longer fit; the test is `test_crafted_names_neither_break_a_row_nor_enter_the_column` and I found it by name.
- The audit's test that runs this script as a step of a whole path passes; whether another test elsewhere (`task-cycle/test_request_check.py` mentions `cycle_stages`) reads a Codex rollout, I did not check.
