FAIL ced0fd992bd8c44bc88159950d958f46816e6c0a

# Review of slice 4 — range `43d7d9b..ced0fd9` (one commit, `ced0fd9`)

`git rev-parse HEAD` in the worktree is `ced0fd992bd8c44bc88159950d958f46816e6c0a`, the head given. The
tree was clean before and after my work.

Files changed: `task-cycle/cycle_stages.py` (+30 −13, 1147 lines at the head),
`task-cycle/test_cycle_stages.py` (+125 −0, 1598 lines at the head).

What the change does, checked against the slice's *Goal*: all of it that the slice names is there and
works. A token record of the agent's own thread with no `usage`, or with a `usage` that lacks or
mangles one of the three counts, ends `main` with exit 2 and `Error: <file>:<line>: no field
payload.usage.<name>` (or `field … is not a whole number`) on stderr, no result file; the same helpers
(`required`, `required_count`, `MissingFieldError`) and wording as the Claude Code half. `parse_time`
takes `Z` through `datetime.fromisoformat` directly. `# invariant: cycle-stages-refuses-crafted-names`
stands above the right test. The one finding below is about what the slice left unchecked in the same
reading, which WAY-344 binds.

## Blocking findings

### Important 1 — The reading of the Codex rollout, which the slice reworks, still reads a missing `thread_id` of a token record as "not this agent's", and crashes on a missing `id` and on a `timestamp` that is no time (WAY-344)

- Places: `task-cycle/cycle_stages.py:464` (`elif kind == "token_usage_record" and payload.get("thread_id") == own:`), `task-cycle/cycle_stages.py:411` (`parse_time(entry["timestamp"])`), `task-cycle/cycle_stages.py:387` (`own = meta["id"]`), `task-cycle/cycle_stages.py:413-416` with `:488` (`turn = payload.get("turn_id")`, then `first_seen[turn]`).
- What is wrong: WAY-344 binds, in a changed script, "the whole reading of each file whose way of reading the change reworks — every field of that file", and its *violates* list names "a change that reworks the reading of a file checks the field it added and leaves the other fields of that file unchecked". The slice reworks how the rollout's token records are read (new function `codex_usage`, `numbered_lines`, the `Usage` made at the line). It makes the three counts and `usage` required and leaves every other field of that reading as it was, naming them in the report as the slice asks. The plan's own table (the row at plan.md:1017) says that the review "finds a field whose absence the script still reads as empty and grades it against WAY-344" — this is that finding. Observed with the changed code on a made-up rollout (run in my own scratch copy, since removed):
  - A token record of the agent's own thread whose `thread_id` is absent or renamed: the line is skipped by the filter at `:464`, its tokens are counted as nothing, exit 0, no word. This is the very symptom of cause 3 (cost of the cycle understated, nobody told) through the neighbouring key. The warning of the script for "a subagent with no token usage" fires only where every record is lost, not when some are.
  - `session_meta` with no `payload.id`: `KeyError: 'id'` stack trace (read in code, `:387`; same read at `:515`).
  - A token record of the own thread with no `turn_id` and no other line of its turn carrying one: `KeyError: None`, a stack trace, observed (`craft` run: "no turn CRASH KeyError None"; the same at the base).
  - A line's `timestamp` of lowercase `…30z` (`ValueError`), or an integer (`TypeError`), stack trace, observed.
  These are not exit 2 with a message naming the file and the field, and the file is read as if the field were empty or the run dies without the message WAY-344 requires. The Claude Code half, which the slice copies, brings `timestamp`, `message` and `message.content` under the check for the same reason.
- The executor's reason for leaving `thread_id` and `turn_id` out ("the description of the script and its test records show neither to be always present") does not hold for the token record: every token record of every test comes from `tokens()` (`task-cycle/test_cycle_stages.py:61-65`), which always carries both `thread_id` and `turn_id`, and the new description names `thread_id` as what selects the agent's own records (`cycle_stages.py:100`). So the slice's own criterion for "named, not made required" does not apply to those two keys of a token record. For `session_meta.id` the description (line 18) and `codex_meta` treat the first line as `session_meta`; every test rollout carries `id`.
- Why it matters: the foundation rule is written for exactly this reading; the task's item 14 says "ends `cycle_stages.py` as WAY-344 requires"; the plan chose the narrow route knowingly and named this review as the place that grades it. A format change of Codex that renames `thread_id` or `turn_id` would again make the cycle's cost come out too low with exit 0.
- Evidence: observed outputs above (run through `cycle_stages.main` with a rollout of the test helpers); `git show 43d7d9b:task-cycle/cycle_stages.py` gives the same behaviour for each, so the change did not introduce them, it left them.
- Grade: Important, within the task (item 14 and WAY-344). The plan's *Choices* row (plan.md:1017) records the narrow route as a choice, and says the cost if wrong is this finding; the orchestrator decides whether to fix (make `thread_id` and `turn_id` of a token record, `session_meta.payload.id` and the `timestamp` of a line needed, one more test each, as the executor itself says: "one more `required(...)` and one test") or to put the question to the human. I grade it as the method asks and do not lower it for the rationale.
  Note on the fields that stay as a documented fallback and that I do not call a finding: `payload.model` of `turn_context` (absent gives no model, as the Claude half's documented fallback), `payload.type`, the call fields, `agent_path`, `agent_nickname`, `parent_thread_id`, `payload` that is no object. These do not make a count disappear.

## Minor findings

### Minor 1 — The docstring of `MissingFieldError` still says it is for a Claude Code transcript

`task-cycle/cycle_stages.py:133` — `"""A Claude Code transcript that lacks a field the reading needs, or holds one of the wrong kind."""`. The class is now raised for a Codex rollout too (`codex_usage` at `:372-381`). A reader of the class is told a smaller scope than it has. Fix: "A session file that lacks …".

### Minor 2 — `required` and `required_count`, now used by the Codex reading, stay under the heading `# Claude Code`

`task-cycle/cycle_stages.py:536-559` against `codex_usage` at `:371`. The executor named this as a choice (keep the diff to the slice). The helpers are shared and a reader looking under `# Codex` or for the shared place will not find them. No effect on behaviour. Worth a move, as a separate change or when the file is divided under the rule of size.

### Minor 3 — No Codex test fixes that a count of `10**15 - 1` is accepted

`task-cycle/test_cycle_stages.py:1297-1308` tests the refusal at `10**15` and at `-1`, `1.5`, `"7"`, `True`, `[1]`, but not the acceptance at the largest allowed value (the Claude half has that test). A change of `TOKEN_DIGITS` for the Codex half only cannot happen since the helper is shared, so this stays Minor; I ran `10**15 - 1` on the changed code and it is accepted (exit 0).

## Out of scope findings

none.

## Declined to judge

- `read_codex_agent` is about 117 lines and `cycle_stages.py` 1147 lines, over what the rule of size of WAY-385 (invariant `function-and-file-size`, `Violated: yes`) will allow; the plan's Choices (plan.md:1008, WAY-365) says no slice divides it before this one and the task that merges first brings the rule to bind. Set aside as outside the task.
- `TRY004` at `task-cycle/cycle_stages.py:567` (`raise ValueError(value)` in `required_time`): a line the slice did not touch; the plan leaves it under the violated invariant of the linter (plan.md:1018).
- A stack trace instead of `Error:` on a lowercase `z` timestamp: the same before the change (`replace("Z", …)` never covered it); included in Important 1 only as one of the fields of the Codex reading, not as a fault of the removal of the replacement.

## Checks run (command and exit code)

All from the worktree root unless stated.

- `python -B task-cycle/test_cycle_stages.py` — exit 0 (80 tests, OK).
- New tests failing on the base: in a worktree of `ced0fd9` of my own with `task-cycle/cycle_stages.py` replaced by `git show 43d7d9b:task-cycle/cycle_stages.py`, `python -B task-cycle/test_cycle_stages.py CodexFieldsTest` — exit 1, 9 tests, `failures=18, errors=6`. Log kept at `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/review-4-base-failing-run.log`. Restored and the same command at the head passes (part of the 80 above).
- Mutations of the head, each in my own worktree, each restored (`git checkout`):
  - `usage = required(payload, "usage", …)` → `payload.get("usage") or {}`: `CodexFieldsTest` fails (`failures=2`).
  - the cached-count `required_count` → `usage.get("cached_input_tokens", 0)`: fails (`failures=12, errors=2`).
  - the own-thread filter `and payload.get("thread_id") == own` removed: the whole file fails (`failures=1`, the forked-rollout test).
  - `parse_time` with `replace("Z", "+00:00")` restored: the tests pass (`OK`) — expected, since on Python 3.14 the two readings of a `Z` give the same time; no test can tell them apart, and none is needed.
- The cited invariant test, `python -B task-cycle/test_cycle_stages.py ClaudeFilesNamedTest.test_crafted_names_neither_break_a_row_nor_enter_the_column`: passes clean (exit 0, `OK`); broken for a moment (the test of `..` in `files_named` removed) — fails (`failures=1`); broken another way (the first-character test of a name removed) — fails (`failures=1`); both restored. A third break I tried, removing the `|` replacement in `cell`, did not fail the test: a name cannot hold `|` since `FILE_NAMED` (`cycle_stages.py:232`) takes only letters, digits, `_`, `-` and `.`, so that break is not one of the escape of names. The executor's own break (filter of a name reduced to `.md`) shown failing is in `reports/executor-4-invariant-failing-run.log`.
- `python -B process-audit/test_audit_count.py Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` — exit 0.
- `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/cycle_stages.py task-cycle/test_cycle_stages.py` — exit 1, one report only: TRY004 at `cycle_stages.py:567`, a line the slice did not write or change. Nothing on a line the slice wrote or changed (FURB162 of the base is gone).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 (`0 errors`).
- `python -B elements/common/foundation_check.py` (without the skip, for a look) — exit 1, 10 errors, none naming `cycle-stages-refuses-crafted-names`; the others are invariants of later slices.
- A scratch run of crafted Codex records through `cycle_stages.main` (script in my directory, removed): max count `10**15-1` exit 0; `1e30`, `NaN`, a dict as count, `usage` as a text, an integer or `{}` — each exit 2 with `Error: <rollout>:4: …` and no output file; timestamps with `Z`, `+00:00`, naive — exit 0; lowercase `z` — `ValueError` trace; a token record with no `turn_id` — `KeyError: None` trace. The last two give the same at the base (run with the base file side by side).
- Not run: the full gate, by the handoff.

## Reach beyond the dispatch

- `plan.md:1008` and `plan.md:1017-1018` (the *Choices* rows on the rule of size, on the narrow route of the Codex fields and on the linter's late reports): what the plan decided and expected of this review.
- `foundations/invariants.md` for `cycle-stages-refuses-crafted-names` and `function-and-file-size`, to check the citation and what size rule binds.
- `task-cycle/cycle_stages.py:1-135` (the description at the head), `:236-270`, `:366-500`, `:536-575`, `:955-965`, and `task-cycle/test_cycle_stages.py:61-70, 735-775` and the grep for `thread_id` and `turn_id`: to compare the description with the code and the criterion "shown always present".

## Unread material

- `foundations/part_map.md:101-111` (`task-cycle`): not read; the slice adds no file or part.
- The six invariants of the orchestrator's additions about files added at the root or under `guidelines/` (`repository-file-location`, `ci-checking-commands`, `tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target`, `derived-file-content`): not read; the slice adds no file.
- `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`: read the sentence of each (their first line), not the whole entry; the change adds no import, no subprocess and no file.
- `foundations/decisions.md` WAY-48, WAY-235, WAY-08, WAY-232, WAY-344: read whole.
- `task.md` passages named in the *Read*: read as named. `plan.md`: the slice, and the rows quoted above; not the rest.
- `task-cycle/cycle_stages.py` lines 590-955 and 965-1147 (the Claude Code reader after `required_time`, the report writing): not read beyond what the grep for `parse_time` and `MissingFieldError` showed; the slice changed nothing there.
- `task-cycle/test_cycle_stages.py`: read the diff whole and the lines named above; the other 1400 lines not read.

## Searches not found or unclear

- The task's anchor `task-cycle/test_cycle_stages.py:707` for the cited test no longer fits; the test is found by name (`ClaudeFilesNamedTest.test_crafted_names_neither_break_a_row_nor_enter_the_column`, now at `:742`).
- The handoff names a plan reading of what "stay as they are" means for the fields whose absence ends the run with a trace (not exit 2): unclear whether the plan meant those to be left too, or only the fallback ones; I read the plan's row at `:1017` as covering both and graded as one finding.

## Working copies

One worktree of `ced0fd9`, `.runs/review-4/wt`, with a scratch script and logs beside it: removed with `git worktree remove --force` and `git worktree prune`, then the directory `.runs/review-4/` removed. The base failing run's log was kept in `reports/review-4-base-failing-run.log`. No remainder.
