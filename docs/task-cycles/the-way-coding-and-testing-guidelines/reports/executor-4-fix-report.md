# Report of the fix of the review's findings of slice 4

**Status:** done

**Commit:** `49be485` — "Require the session id, the thread and turn of a token record and the timestamp of a line in the reading of a Codex rollout" (range of the fix: `ced0fd9..49be485`).

## The finding (Important 1, fixed, none contested)

I checked the reviewer's evidence before changing code, on made-up rollouts of the test helpers through `cycle_stages.main`, and it held: a token record with no `thread_id` was skipped with exit 0, `session_meta` without `id` gave `KeyError`, a record without `turn_id` gave `KeyError: None`, and a timestamp of lowercase `…z` or an integer gave `ValueError` or `TypeError`.

Fixed, with the same helpers and wording as the first change (`required`, a new `required_time` use, `MissingFieldError`, exit code 2, `Error: <path>:<line>: …`):

| Field | How | Test (added) |
|---|---|---|
| `payload.thread_id` of every `token_usage_record` | `codex_tokens` reads it with a new helper `required_text` before telling the agent's own record from another's | `test_a_record_of_tokens_without_its_thread_ends_with_exit_code_2_naming_it` |
| `payload.turn_id` of a token record of the agent's own thread | `codex_tokens`; read before any line's `turn_id` is used as a key | `test_a_record_of_tokens_of_the_agent_without_its_turn_ends_with_exit_code_2_naming_it` |
| `payload.id` of the first line `session_meta`, in both reads (`read_codex_agent` and `codex_subagent_paths`) | the check stands in `codex_meta`, which both call, and gives the line number of the first non-blank line | `test_a_first_line_without_the_id_of_its_session_ends_with_exit_code_2_naming_it`, `test_a_subagents_first_line_without_the_id_of_its_session_ends_with_exit_code_2` |
| `timestamp` of every line whose `payload` is an object, absent, `null` or no time | `required_time`, as for Claude Code; before, a line with no `timestamp` was skipped and one with a bad value crashed | `test_a_line_without_its_timestamp_ends_with_exit_code_2_naming_it`, `test_a_timestamp_that_is_no_time_ends_with_exit_code_2_naming_it` (nine values) |
| the kind of the three ids | `required_text`: a value that is no text or is empty ends with `field <name> is not a text` | `test_an_id_or_a_turn_that_is_no_text_ends_with_exit_code_2_naming_it` |

The description at the head of the script now lists what the reading of a Codex rollout needs, and the exit-code paragraph names the Codex fields too. The fields the reviewer lists as a documented fallback stay as they were: `payload.model`, `payload.type`, the call fields, `agent_path`, `agent_nickname`, `parent_thread_id`, and a `payload` that is no object.

## Checks (command and exit code)

- Failing run, the new tests at the code of `ced0fd9`: `python -B task-cycle/test_cycle_stages.py CodexFieldsTest` — exit 1 (16 tests: 6 failures, 13 errors, all in the seven new tests; the nine tests of the first change passed). The errors are the crashes the fix removes (`KeyError`, `ValueError`, `TypeError`), the failures are exit 0 where 2 is expected. Log: `reports/executor-4-fix-failing-run.log`.
- After the fix: `python -B task-cycle/test_cycle_stages.py` — exit 0 (87 tests).
- `python -B process-audit/test_audit_count.py Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` — exit 0.
- `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/cycle_stages.py task-cycle/test_cycle_stages.py` — exit 1, only the TRY004 of `cycle_stages.py:598`, the line the slice did not touch (it was reported at the base). Nothing on a line the fix wrote.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0.
- Also, `python -B task-cycle/test_request_check.py` — exit 0 (it mentions `cycle_stages`).
- Not run: the full gate.

## Choices

- **`required_text` refuses a value that is no text, and an empty one** (the handoff asks only for "required"). Without it a list `turn_id` of a token record still ends in `TypeError` at the first use as a key (observed). Rejected: only `required`. Cost if wrong: a Codex id that is a number now ends the run with exit 2.
- **The id check is in `codex_meta`, so it covers every rollout whose first line is a `session_meta` that `codex_subagent_paths` reads under the home**, not only subagents' ones. Rejected: checking only where `meta["id"]` was read — the line number would be lost or wrong. Cost if wrong: a rollout of another session in the same home, newer than the orchestrator's first turn, whose first line lacks `id`, ends the run with exit 2 naming it.
- **A line with an object `payload` and no `timestamp` is no longer skipped** (Claude Code's half skips a line with no `timestamp`). Rejected: copying that skip — a token record with no `timestamp` would be skipped and its tokens lost, the symptom of cause 3. Cost if wrong: a Codex line with a payload and no time, which a real rollout may hold, ends the run.
- **`codex_tokens` reads the record before the generic `turn_id` of the line**, so that a bad `turn_id` of a token record is named and not a `TypeError`.

## Still not checked, observed (not in the findings file, not fixed)

- A line that is no JSON object, as a list: `AttributeError` at `entry.get` in `read_codex_agent` (observed).
- A `turn_id` of a line that is not a token record and is a list: `TypeError` at `first_seen.setdefault` (observed).
- The first line of a rollout under the home that is no object: `AttributeError` in `codex_meta` (read in code, not run).

## Working copies

`.runs/executor-4/` (a directory for a run of crafted input); removed before I returned, and `.runs/` holds only `task-cycles/`. The failing-run log stands in `reports/`.

## Unread material

- `task-cycle/change/SKILL.md` (this fix's variant) was read whole in the first round; `fix.md` and the findings file whole now.
- `reports/review-4-report.md`: not read (the findings file carries the finding word for word).
- `task-cycle/cycle_stages.py` lines 760-1085 (the writing of the report) and the middle of `task-cycle/test_cycle_stages.py`: not read, as in the first round.

## Searches not found or unclear

- None. The line numbers of the findings file (`:387`, `:411`, `:464`, `:488`, `:515`) point to the code of `ced0fd9` and I found each read at that place.
