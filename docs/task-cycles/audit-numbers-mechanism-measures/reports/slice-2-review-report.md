PASS 036d24ab0581775b646e0bd186ee3c799a5a2ab0

# Review of slice 2 — the measures script, for Codex sessions

Head reviewed: `036d24ab0581775b646e0bd186ee3c799a5a2ab0` (`git rev-parse HEAD` confirmed). Range `dae0de6..036d24a`, one commit.
Variant: a planned slice (slice 2).

Changed files (from `git diff --stat`):

- `task-cycle/cycle_measures.py` — 311 lines changed (+224 −87); the file is now 505 lines
- `task-cycle/test_cycle_measures.py` — 206 lines changed (+201 −5); the file is now 702 lines
- Both files together: 425 insertions, 92 deletions (the executor's figures match the diff).

## Findings

### Critical

none

### Important

none

### Minor

1. `task-cycle/cycle_measures.py:279-300` (`codex_subagents`) — the search for subagents reads the first line of every rollout under the Codex home, with no floor on age, so one unreadable first line (not JSON, not UTF-8, a directory named `rollout-*.jsonl`) in the whole history of the home ends every cycle's measures with exit 2. Evidence: scratch runs with an unrelated rollout whose bytes are `\xff\xfe` gave `Error: cannot read ...rollout-bad.jsonl: 'utf-8' codec can't decode byte 0xff`, exit 2, nothing written; a directory named `rollout-dir.jsonl` gave `Error: cannot read ...: [Errno 13]`, exit 2. This is the question the handoff puts to me. My grade: the strict form is within the task and WAY-344 — the slice says a rollout's `session_meta` needs `payload.id` and a missing one is exit 2 with the file named — and it is loud, never a missing subagent counted as nothing. So it is not blocking. Its cost is real: the file lies in the user's home, outside the cycle, and the damage grows with the age of the home. `task-cycle/cycle_stages.py:443-452` bounds it by reading only rollouts modified since the orchestrator's first turn. The same floor here (skip a rollout whose modification time is before the orchestrator's first call, since a subagent is written after its parent starts) would keep the loud failure for every file that could be a subagent and leave old files alone. Recommend it as a later change, with its test; nothing in this slice's requirements asks for it.
2. `task-cycle/cycle_measures.py:295` — a second rollout with the same `payload.id` as an already found one is dropped without a word (scratch run: two rollouts with id `d`, the file sorted first counted, the other absent, exit 0). Ids are unique in Codex's own records, so this needs a hand-made file; the effect is a missing subagent shown as nothing. Low likelihood; either report it as an error or keep it and say so in the docstring.
3. `task-cycle/test_cycle_measures.py:479` — one blank line before `class CodexTest` (two are the style the rest of the file keeps). `task-cycle/cycle_measures.py:70-73` and `:81-83` — "unknown" is held twice, as `None` fields of a `Call` and as the `cache_known` flag of an `Agent`; `rewrites()` (line 329) would raise `TypeError` on a Codex call if a later caller skipped the flag. Today every caller goes through `cache_sum` and `rewrite_totals`, which check the flag, so nothing is wrong now.

## Against the task and the foundation

Each requirement of slice 2 checked against the code and the tests:

- first line `session_meta` is a Codex orchestrator rollout; one naming `parent_thread_id` is refused as a session: `rollout_meta` (233), `read_codex_session` (302); test `test_a_subagent_rollout_named_as_a_session_ends_with_exit_2`. Met.
- subagents found by `parent_thread_id` of the orchestrator's id or of a subagent already found, name = `agent_path`, else `agent_nickname`, else id: `codex_subagents`, `rollout_meta`; hand-worked test with a grandchild found through the forked subagent, a nickname-only subagent and an unrelated rollout. Met.
- calls are only `token_usage_record` entries whose `payload.thread_id` is the agent's own, in time order, usage from `payload.usage`: `read_codex_calls` (259); the forked subagent repeats three records of its parent and counts only its two own, written out of time order. Met.
- context is `input_tokens` with the cached part not added again: test asserts first call 1000 where `cached_input_tokens` is 500. Met.
- cache written (5 minutes, 1 hour), cache written again and calls with a write again are `unknown` for a Codex agent; first, middle, last call, calls and means given; lines of the file `unknown` where any agent summed is Codex; the table gives `Codex` and `unknown`: `cache_sum`, `rewrite_totals`, `agent_row`; the whole file is compared line by line in `HandWorkedCodexTest` and `MixedCycleTest`. Met. I recomputed the hand figures: 1000+2000+3000+5000+6000+400+7 = 17407, 17407/7 = 2486.7, shown 2487; orchestrator mean 2000.
- needed fields `payload.usage.input_tokens`, entry `payload.thread_id`, `session_meta` `payload.id`: exit 2 with `Error:` naming file, line and field (`json_lines`, `member`, `whole`, `identifier`). Tests give a usage entry without `input_tokens` (the WAY-344 test the slice names), a non-integer `input_tokens`, a `session_meta` without `payload.id`, and a line nested 200000 deep. Met.
- sessions of both tools named together sum over both: `MixedCycleTest`; the Claude Code lines keep their numbers (`Cache written again by subagents: 0`). Met.
- the Claude Code reading is unchanged in behaviour: the refactor to `json_lines` keeps the same errors; its only difference is the order in which several missing fields are noticed. The 43 tests of the file, including the earlier Claude Code ones, pass.
- Foundation entries: WAY-344 (readings reworked: both the Claude Code reading, which kept every field check, and the new Codex reading are covered; one test per reading exists), WAY-347 (file of its own, no column of the stage report — untouched), WAY-351 (definition unchanged; used only for Claude Code agents), WAY-38 and `script-imports` (standard library only; the new import is `collections.abc`), `cross-part-imports` (no import of another file; its test passes), `tracked-file-private-paths` (the fixtures use `/root/design`, as `task-cycle/test_cycle_stages.py:92` already does; no absolute path of the patterns of WAY-309), the part map (`cycle_measures.py` is listed as the trust boundary of `task-cycle`, and the External context row marks session records untrusted).
- Nothing added that nobody asked for. No reserved choice taken.

## Hostile input at the trust boundary

Checked by reading the code and by scratch runs in the scratchpad:

- missing and renamed fields: `payload` not an object, `thread_id` absent, `usage` absent or `input_tokens` absent or a string or negative or boolean: each exit 2 naming file, line and field (`member` treats a non-object holder as a missing field).
- not JSON, not an object, nested 200000 deep, not UTF-8, an unreadable path: each exit 2 naming the file; the nested line names file and line number.
- huge counts: a rollout file is read line by line; an integer of 4290 digits gave a normal result (Python 3.14.3); the search holds only the ids and paths of the rollouts.
- bars and control characters in a name that reaches a cell: `agent_path` `a|b\nc<U+2028>d<ESC>[31m` came out as `a/b c d [31m` in one cell; every name goes through `cell` in `agent_row`, the orchestrator's name included. The only text of the input in an error line is a JSON decoder's message (no copy of the line) and a file path.
- a cycle of parents (`parent_thread_id` equal to an id already known, or to the orchestrator's own): the `known` set ends it.
- an unrelated rollout with a broken first line: exit 2 by design (Minor 1).

## Declined to judge

- The wording of the ticket for the closing step that calls the script, and how it reacts to exit 2 — outside this slice, which changes only the two files named.
- Whether the foundation's `task-cycle` part-map entry should name Codex as a source of session records — the External context row already says "session records"; not this slice's file.

## Checks run

- `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` — exit 0 (43 tests, OK).
- `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` — exit 0 (39 tests, OK).
- Scratch runs of `task-cycle/cycle_measures.py` over hand-made rollouts in the session scratchpad (a 4290-digit input, a hostile `agent_path`, duplicate ids, an empty rollout, a directory named like a rollout, a non-UTF-8 rollout): outcomes as in Minor 1, Minor 2 and the section above.
- Not run: the product's gate (by instruction); the "fail before the slice" run of the Codex tests, which I took from the executor's report (8 failures on the old refusal) and did not repeat; the test file's other classes were not mutated by me.
- `git status --short` of the reviewed worktree was empty before and after; nothing changed in it.

## Reaches beyond the handoff

- `git diff --stat dae0de6..036d24a`, `grep` of the worktree for `cycle_measures` and for `/root`, `foundations/part_map.md:102`, and the head of `task-cycle/private_paths_check.py` (what WAY-309 lists as a private path) — to check the invariant `tracked-file-private-paths` against the fixtures.

## Unread material

- `.runs/task-cycles/audit-numbers-mechanism-measures/task.md` and `plan.md`: not opened; the passages of the task were read as the copies in the handoff.
- `task-cycle/cycle_stages.py`: read lines 227-260 and 274-470 and 610-645; the rest not read.
- `task-cycle/test_cycle_stages.py:32-125`: not opened; the one fixture line I needed (`/root/design`, line 92) I found by search.
- `foundations/decisions.md`: WAY-344, WAY-347 and WAY-351 read whole; WAY-38 read to its *Rejected* paragraph's first lines (the first 30 lines of the range 1026-1051, cut at 200 columns); WAY-328 (`10868-10917`) not opened.
- `foundations/invariants.md`: `script-imports`, `cross-part-imports`, `tracked-file-private-paths` read whole.
- `foundations/part_map.md:93-103` and `232-240`: read whole.
- `task-cycle/cycle_measures.py`: lines 1-320 read as the diff, 85-100 and 180-222 as excerpts, 320-505 whole; the unchanged `read_subagent_name` and `member`/`whole` bodies read in the excerpts only.
- `task-cycle/test_cycle_measures.py`: the diff read whole; the unchanged part of the file not read beyond the lines around 470-482.

## Searches not found or unclear

none
