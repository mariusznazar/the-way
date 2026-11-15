# Report — executor of slice 2, task `scripts-after-foundation-review`

**Status:** done

**Commit:** `bb84a50` "Read a Claude Code transcript under WAY-344 in the stage script" on `task/scripts-after-foundation-review` (base of the slice `879a14c`). Author address checked: `the author's e-mail address`.

## Files changed

| File | Added | Removed |
|---|---|---|
| `task-cycle/cycle_stages.py` | about 107 | about 26 |
| `task-cycle/test_cycle_stages.py` | 250 | 0 |
| `task-cycle/skill/SKILL.md` | 2 | 2 |

(git: 3 files, 359 insertions, 28 deletions.)

## What the change does

- `task-cycle/cycle_stages.py`: the reading of a Claude Code transcript (`read_claude_agent`) checks the closed list of D4.
  - Of every `user` or `assistant` line that has a `timestamp`: `timestamp` as a time (a null, a non-text or an unparsable value, or one that overflows on conversion to UTC, ends the run), `message`, `message.content`.
  - Of an `assistant` line whose model is not `<synthetic>`: `message.usage` and its four counts, each a non-negative whole number (a `bool`, a fraction, a text, a list and a negative number are refused).
  - A new `MissingFieldError(CycleStagesError)`; `main` returns 2 for it and 1 for the other `CycleStagesError`. The message is `Error: <transcript path>:<line of the file>: no field <field>` or `... field <field> is not a whole number` or `... is not a time`.
  - The module description now holds the list, what stays lenient, and the exit-code paragraph (2 for a missing field, 1 for the rest).
  - The fields that stay as they are are not checked: line with no `timestamp` skipped before the type is looked at, `type`, `isMeta`, `message.model`, `message.id` (the `uuid` stands for it), `message.stop_reason`, the lenient reading of content blocks.
  - `message.usage.cache_creation` and its lifetimes are not read (Slice 3).
  - The reading of a Codex rollout and of `agent-<id>.meta.json` is not changed (see the shared helper below).
- `task-cycle/test_cycle_stages.py`: new class `ClaudeFieldsTest` (10 tests). The existing fixtures needed no change: `answer`, `prompt`, `result`, `call_result` already hold every needed field.
- `task-cycle/skill/SKILL.md` (step 12): the sentence now names `task-cycle/cycle_stages.py` beside `cycle_measures.py` and `gate_times.py`.

## Test first: failing run and passing run

- Failing, on the base code with the new tests: `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`, exit 1, `Ran 60 tests`, `FAILED (failures=27, errors=34)` (subtests counted). The first test, `test_a_needed_field_that_is_missing_ends_the_script_with_exit_code_2_naming_it`, failed by its assertion (exit code 0 where 2 was expected), the count absent read as zero. The errors are the crafted-input tests: a trace from the base code (a `TypeError` on an unhashable id, an uncaught `ValueError` for a timestamp, a `UnicodeDecodeError`, a `RecursionError`).
- Pin test `test_the_fields_that_stay_lenient_read_as_they_always_did` passes on the base (`python -B -m unittest task-cycle.test_cycle_stages.ClaudeFieldsTest.test_the_fields_that_stay_lenient_read_as_they_always_did`, exit 0), as the slice asks (it pins what does not change).
- Passing, after the change: `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`, exit 0, `Ran 60 tests`, `OK`.

## Checks run (command, exit code)

- `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`: exit 0, 60 tests.
- `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`: exit 0, 87 tests (script untouched).
- Mutations tried and caught, the file restored each time: dropping `value < 0` from `required_count` gave 26 failures; replacing the line-type filter with `if False:` gave 1 failure (`test_a_line_of_another_kind_is_no_line_the_reading_checks`).
- Not run: the whole gate (WAY-160), as the handoff says.

## The own-work check

- Requirement most likely not met: the new check refuses a real Claude Code transcript that holds a line shaped differently from the fixtures (the list is closed and the real files are the ground truth), or it reaches a field beyond the list.
- Checks: (1) ran the script on the eight most recent real Claude Code transcripts on this disk, each with the subagents it has (`python -B task-cycle/cycle_stages.py <path> --output .runs/executor-2/real.md`): all eight exit 0, no `Error:`. (2) The pin test above (what stays lenient) passes on base and after.
- It showed no missing field in real transcripts, and the pins hold.

## Choices (with the way rejected and the cost if wrong)

1. **The time of a line is parsed after the line's type is known, only for `user` and `assistant` lines.** The base parsed the time of every line with a `timestamp` first. The spec says the needed `timestamp` is of "such a line". A line of another type with a bad `timestamp` is now skipped instead of ending the script. Rejected: parsing every line (a field of a line the reading does not use would end the run). Cost if wrong: a garbage `timestamp` on a `summary` line passes without an error.
2. **A `timestamp` key present with `null` ends the script (exit 2, "no field timestamp"); only an absent key skips the line.** The spec says "a null is absent" and also "a line with no `timestamp` is skipped (the first statement)". I read the skip as the key test of the first statement, as the base has it. Rejected: skipping a null (the line would silently drop its tokens). Cost if wrong: a null-timestamp line that real files hold ends a run; none was met in eight real transcripts.
3. **The time is returned in UTC; a naive time is taken as UTC, as `cycle_measures.py` does.** Rejected: keeping the offset (the sort then fails on a mix of naive and aware times, a crash on crafted input).
4. **A non-text `message.model`, `message.id`, `uuid`, `block.type`, `block.name`, `block.id` and `block.tool_use_id` count as absent (`text_of`).** The spec lists these fields as lenient. A list in them crashed the base (unhashable key) and a number could reach the report. A tool call whose `id` is no text is then a call of a type the reader does not recognise, with the existing warning. Rejected: leaving the base behaviour (a trace on crafted input, the handoff's trust boundary). Cost if wrong: a numeric `id` that real files hold would pair no result; none found.
5. **`numbered_lines` is a new function and `read_lines` wraps it.** The Codex reading uses `read_lines`; both now catch `UnicodeDecodeError`, `RecursionError`, `MemoryError` and any `ValueError` (a number of more than 4300 digits) as "not JSON", exit 1, where the base let them out as a trace. This touches the shared line reader and so, in effect, the Codex reading's behaviour on crafted bytes; no Codex field is checked and no Codex test changed.
6. **`one_line` encodes with `errors="replace"`**: a lone surrogate in a model name made `write_text` fail with a trace; it is now `?`. A line that is no JSON object is skipped as a line with no `timestamp` (cycle_measures ends the run on it; the slice's list says a line with no `timestamp` is skipped). `read_session` refuses a first line that is no object with the existing "neither a Codex rollout nor a Claude Code transcript" error, exit 1.
7. **The extra tests of crafted input are mine, beyond the one the slice asks.** The slice asks for one test of a missing field and the pin tests. I wrote a test with subtests for every needed field and each count against the five wrong shapes, because the handoff names a trust boundary and asks that crafted input cannot crash the script.

## Invariant or decision tests

No test changed that holds the sentence of a decision by a line `decision:` or an invariant's test (WAY-03). No existing test was changed or weakened; only added.

## Reaches beyond what is named

- `foundations/decisions.md:2741-2901` (WAY-344) read whole; WAY-38 and the three invariants read at the ranges the handoff gives; `foundations/part_map.md:101-112`; `task-cycle/cycle_measures.py:1-330` (the handoff names 1-110; I read to line 330 for `member`/`whole`/`read_time`/`json_lines`, the form of the check).
- `~/.claude/projects/*/*.jsonl` (real transcripts, read through the script only, for the own-work check).
- `a rule or note file of the author's, outside the repository`, as the global instructions ask before a commit.

## Unread material

The spec lines 1-49 and 78-264 and 329 onward; the task document outside what the handoff copies (none was named beyond `spec.md:57-61`, `265-327`, `task.md:134`); the plan outside the slice. `task.md:134-134` itself I did not open (the slice text and WAY-344 give the same sentence). `foundations/invariants.md:116-145` was read whole.

## Searches not found or unclear

- None not found.
- Unclear: how a `null` `timestamp` stands to "a line with no `timestamp` is skipped" (choice 2).
- Residual, not fixed: a count of more than 4300 digits in several lines could add up to a number that `f"{value:,}"` refuses to format (Python's int-string limit), a trace on a transcript made for it. The spec asks for "a non-negative whole number" and sets no upper bound; I did not invent one. A review may ask for a bound.
- Residual: `agent-<id>.meta.json` that is valid JSON but no object (a list) still crashes `meta.get`; the handoff says that reading does not change.

## Working copies

`.runs/executor-2/` held a copy of `cycle_stages.py` (for the mutation checks) and the output of the real-transcript runs. Removed before return (`rm -rf`); nothing remains. No worktree or clone was made.
