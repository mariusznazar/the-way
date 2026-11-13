# Slice 2 report — The measures script, for Codex sessions

**Status:** done
**Commits:** `036d24a` (slice range `dae0de6..036d24a`, one commit)
**Files changed:** `task-cycle/cycle_measures.py` (+224 −87), `task-cycle/test_cycle_measures.py` (+201 −5)

## Checks

| Check | Command | Exit code |
|---|---|---|
| Codex tests before the change | `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` | 1 (43 run, 8 failures: the new Codex tests fail on the old refusal, `Error: ... is a Codex rollout`) |
| Measures tests after the change | same command | 0 (43 run, OK) |
| Cross-part imports | `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` | 0 (39 run, OK) |

Not run: the product gate (`gate/run_tests.py`), by instruction; the foundation check, not this slice's.

## Test-first

The Codex tests were written before the code. The failing run above is the first run, with the new tests and the old script. Each Codex test failed on its assertion (the refusal message or the missing `Error:` field), not on a missing module.

Changed test (a deliberate behaviour change, named): `test_a_codex_rollout_is_refused_with_exit_2` was removed. It asserted the refusal that this slice relaxes. Its replacements are in `CodexReadingErrorsTest`, including `test_a_subagent_rollout_named_as_a_session_ends_with_exit_2`, which keeps the refusal for a subagent's rollout.

## Own-work check (section 3)

- **Requirement most likely missed:** the Codex figures on a cycle with a forked subagent, where the copied history must not count and the `unknown` cells must appear exactly where the slice gives them.
- **Check:** `HandWorkedCodexTest` gives an orchestrator with three calls, a forked subagent repeating those records (plus two of its own written out of time order), a nickname-only subagent, a grandchild found through the forked one, and an unrelated rollout. The whole file is compared line by line with hand-worked figures (7 calls, mean 2487 from 17407 / 7, `unknown` cache lines). Result: passed.
- **Mutation reasoning (not run):** without the thread filter the forked subagent shows 5 calls; without the time sort its first call is 6000; without the breadth-first search the grandchild is missing; with `cached_input_tokens` added the first call is 1500, not 1000. Each is caught by a test named above.
- **Scratch run of the real script** (in the scratchpad, not committed):
  - an orchestrator rollout plus an unrelated rollout whose first line is not JSON: exit 2, `Error: ...rollout-2026-10-06T00-00-00-unrelated.jsonl:1: not JSON`. This is the choice in point 1 below.
  - the same without the unrelated file: exit 0, with the Codex figures.

## Choices

1. **The subagent search reads the first line of every rollout under `<codex home>/sessions`.** A rollout whose first line is not JSON, or whose `session_meta` lacks `payload.id`, ends the run with exit code 2, even when it is unrelated to the cycle. Alternative: skip unrelated rollouts whose first line cannot be read. Cost of the chosen way: one corrupt old rollout in the Codex home makes every cycle's measures exit 2 until the file is fixed or moved. Cost of the alternative: a corrupt rollout is silently skipped, which the rule against guessing a missing field does not allow for a reading the script does. My recommendation: keep it, since the error names the file, but the orchestrator should decide.
2. **No mtime floor in the search.** `task-cycle/cycle_stages.py` skips rollouts older than the orchestrator's first turn. Here the search skips that filter. The set of subagents found is the same, because ids are unique and the parent link is what matters; the cost is that every rollout in the Codex home is opened on each run.
3. **`session_meta` must carry `payload.id` on every rollout the search reads**, not only on those that name a parent. This follows the slice's rule that a session_meta needs `payload.id`; see point 1.
4. **Naming:** a Codex orchestrator's row reads `orchestrator <id>`, as a Claude Code one does; a subagent's row reads its `agent_path`, else `agent_nickname`, else its id, with no `(type)` suffix, as the slice gives.
5. **Calls:** each `token_usage_record` of the agent's own thread is one call, in order of its time, ties by line number. `cached_input_tokens` is not read, since the slice says the input already holds the part read from the cache.
6. **Shared reader:** the Claude Code reader and the Codex reader use one `json_lines` generator for the not-JSON, not-an-object and unreadable-file errors (naming file and line). The Claude response reader now reads its timestamp after the cache fields, so when several fields are missing at once, a different one may be named first. No other behaviour of the Claude reader changed.
7. **Mixed cycles:** a line that sums over a Codex agent is `unknown`; a line that sums only Claude Code agents keeps its number, as with the empty subagent group in the mixed test (`0`).

## Unread material

- `.runs/task-cycles/audit-numbers-mechanism-measures/task.md` lines 28-33 and 116-125: not opened; read as the copies in the handoff, which were used as given.
- `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md`: not opened, as the handoff said.
- Foundation entries named in the handoff: read whole, WAY-344, WAY-347, WAY-351, WAY-328 and WAY-38 (`foundations/decisions.md`); `script-imports`, `cross-part-imports` and `tracked-file-private-paths` (`foundations/invariants.md`); `task-cycle` and `External context` (`foundations/part_map.md`). Rows 1 and 7 of the settlements table, and the part-map row, were read in the handoff's copy.
- `task-cycle/cycle_stages.py` lines 274-470 and 619-642, and `task-cycle/test_cycle_stages.py` lines 1-130: read in full as ranged.
- Files read whole before change: `task-cycle/cycle_measures.py` and `task-cycle/test_cycle_measures.py`.

## Searches not found or unclear

none

## Reaches beyond the handoff

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`, read in full, as the handoff named the method.
- The head of `elements/part-map/test_cross_part_imports.py`, read to see what the check covers (no new imports were added to the script).
- `.claude/skills/the-way-make-change/SKILL.md`, to confirm this checkout is not a product.
