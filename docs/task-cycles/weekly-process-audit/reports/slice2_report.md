# Slice 2 report — the wait for tools in the stages of a cycle

**Status:** done with concerns

**Commits:** `876710c` — Count the wait for tools and the tokens by model of each stage (2 files, +406 / −29).

**Files changed:**
- `task-cycle/cycle_stages.py` (+235 / −29)
- `task-cycle/test_cycle_stages.py` (+171 / −0)

## What was done

`cycle_stages.py` now reads each tool call from its start to its result, in Claude Code and Codex transcripts. Calls that start a subagent, send it a message or wait for it are left out. The report gains, per stage, a start time (UTC), the time waiting for tools, and tokens by model and kind (input, cached input, output). The summary splits the working time into waiting for tools and working time without it; the two add up to the working time the report gave before.

The docstring of `cycle_stages.py` says what counts as a wait for a tool.

Existing report lines are kept in place. The new figures are added lines and a new section, `## Stages: start, waiting for tools and tokens by model`, below the existing per-model table.

## Tool names taken for subagent calls, and where they are read

- **Claude Code:** the `name` of a `tool_use` block in an assistant entry (`message.content`), in the orchestrator's transcript and in each subagent transcript. Subagent calls left out: `Agent` (seen in the orchestrator's transcript), `SendMessage` (seen across the transcripts), and `Task` (the older name of `Agent`; not observed in the data, included as a guess). Results are `tool_result` blocks, matched by `tool_use_id`.
- **Codex:** the `name` of a `response_item` payload of type `function_call` or `custom_tool_call`, in the orchestrator's rollout and in each subagent rollout. Subagent calls left out: `spawn_agent`, `wait_agent`, `send_message`, `followup_task` (seen in `~/.codex/sessions/2026/10/26/`). Results are `function_call_output` or `custom_tool_call_output`, matched by `call_id`. A Codex `exec` call (a script) whose input calls one of these subagent tools is left out, with a warning.

## Checks

| Check | Command | Result |
|---|---|---|
| Failing tests before the change | `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` | exit 1, 6 failures (the six new tests, on their assertions) |
| Tests after the change | same command | exit 0, 33 tests OK |
| Mutation: `SendMessage` counted as a tool | sed on a copy of the module, run the same command | exit 1, 2 failures (caught); module restored, `cmp` confirmed |
| Mutation: unreadable call shown as zero (`if False`) | same | exit 1, 1 failure after an assertion for the stage cell was added (before that addition the mutation survived); module restored, tests pass again |
| Real session, Claude Code (own orchestrator session) | `python -B task-cycle/cycle_stages.py b065500f-249b-4808-a8bf-172d19a2724a --output <scratchpad>\stages_new.md` | exit 0; one Warning: the in-flight Bash call of this session has no result yet, so its wait is unknown |
| Real session, Codex | `python -B task-cycle/cycle_stages.py 01a17a1b-5a08-7331-8cbb-ea51880661c1 --codex-home %USERPROFILE%\.codex --claude-home %USERPROFILE%\.claude --output <scratchpad>\codex_new.md` | exit 0; no warnings |
| Old lines kept (finished Codex session) | old script from `git show HEAD:task-cycle/cycle_stages.py` and the new one, same session | exit 0 both; 0 old lines missing from the new report |
| Compile | `python -B -m py_compile task-cycle/cycle_stages.py task-cycle/test_cycle_stages.py` | exit 0 |
| Line length | awk, lines over 100 characters | none in the changed files |

Not run: the full suite of the-way (left to the cycle's run before the request, per WAY-160).

Scratch outputs are in `a scratch file outside the repository` (`stages_new.md`, `codex_new.md`, `codex_old.md`, `stages_old.md`, `old\cycle_stages_old.py`). No transcript content is in this report; only counts and warnings.

## Own-work check (`make-change` section 3)

- **Requirement:** the waiting time and the working time without it, added together, give the working time the report gave before; and a call the reader cannot read is never shown as a zero wait.
- **Check:** the real Codex session, and the tests `Waiting for tools: unknown` and `unknown (at least …)`.
- **Result:** Codex: waiting 0:34:06 + working without it 4:15:18 = 4:49:24, the joined working time. Claude Code (live session, one unreadable call): waiting at least 0:03:02 + working without it at most 0:33:47 = 0:36:49, the joined working time. Unreadable calls are shown as `unknown`.

## Choices made

1. **A new section for stage starts, waits and per-model tokens, not new columns on the existing table.** Rejected: adding columns to the existing table. Cost: stage names repeat across two tables, and the file is longer.
2. **A cycle's waiting time shows `unknown (at least …)` as soon as one call has no readable result or an unrecognised type.** Rejected: counting such a call as zero (breaks "never a wait of zero"), or leaving it out silently. Cost: one lost call makes the cycle's total unknown; the audit has to read the `at least` figure.
3. **A Codex `exec` script that calls a subagent tool is left out of the waits, with a warning.** Rejected: counting it as tool time (it would mix in subagent time) or marking it unknown (it would make the whole cycle unknown). Cost: the script's own tool time is lost; the warning gives only the count.
4. **Codex subagent calls are kept only if they start inside the subagent's own turns.** This drops calls copied in from a forked parent's history. Rejected: de-duplication by call id. Cost: a real call outside the turn windows would be dropped silently; this filter is not tested against a real forked rollout.
5. **A result with no matching call is ignored, with no warning.** Rejected: warning on it. Reason: the existing fixtures in `ClaudeCodeTest` contain such results, and their assertions on warnings are exact, so a warning would break the existing tests. Cost: a call lost from the transcript would not be flagged.
6. **Stage waits: each call counts in the stage running when it starts, as its tokens do. The cycle total counts each moment once.** Cost: per-stage waits can overlap when stages run in parallel, so their sum can exceed the cycle total. The summary uses the total.
7. **`TaskStop` and `Monitor` (Claude Code) count as tool waits; they are not subagent calls.** Cost: small; these calls are normally short.

## Concerns

- **Cache writes are inside `Input`.** For Claude Code, `input_tokens` plus cache-creation tokens plus cache-read tokens are folded into one input figure, as before. The audit cannot price cache writes apart from uncached input. This matters for slice 4 (pricing); I did not change it, as it is the reader's existing behaviour. Suggest the orchestrator decides before slice 4.
- **Newer Codex rollouts put `turn_id` under `turn_attribution` in `task_started`.** The reader reads the top-level `turn_id`. I saw this in a subagent rollout (`rollout-2026-10-26T22-56-00-…`). I verified only that the sampled Codex session (01a17a1b…) gives no warnings; I did not verify the effect on that subagent's turns.
- **Live sessions show their in-flight call as unknown** (seen on this session). This is correct behaviour, but a check run during a cycle will always carry that warning.
- **Orphan results are silent** (see choice 5).

## Reaches beyond the handoff

- Read transcript shapes directly, to find the tool names: `~/.claude/projects/C--Storage-repos-the-way/b065500f-….jsonl` and its `subagents/` folder; `~/.codex/sessions/2026/10/26/` (rollouts `01a17a1b-…` and `01a17a36-…`). Names and counts only; no content is reproduced here.
- Read `foundations/invariants.md` only at `script-language`, `script-imports`, `script-subprocesses`, as the handoff names.
- Did not read `project-level/technology/reserved_choices.md`: the change needs no new language, library or store, and uses the standard library only as before.

## Unread material

- Plan `.runs/task-cycles/weekly-process-audit/plan.md`: not read, per the handoff; only the copied rows and section were used.
- `foundations/decisions.md` WAY-148: read 4141–4208 as named; the lines after 4208 were not read.
- WAY-89 and WAY-255: read in the named ranges only; their `Based on` sources were not opened.
- Invariants `python-stdlib-modules` and `python-version-declared` (Rests on / Verification of the named invariants): not read.
- `task-cycle/skill/SKILL.md` step 12: read 428–443 (the named passage is 433–441).
- `task-cycle/change/SKILL.md` and `slice.md`: read whole.
- `task.md` 23–36 and 67–71: read as named.
- Foundation rows 8 and 9 and WAY-334 / WAY-335 (decisions 10798–10840): read.

## Searches not found or unclear

- **`close_agent` (Codex):** not seen in the rollouts I looked at (one large rollout's tool names, and the name counts in the rollouts I sampled). If it exists, it would be counted as a tool wait; its time is short.
- **`TaskOutput` (Claude Code):** not seen in the orchestrator's or subagents' transcripts. Not included in the subagent list. If Claude Code uses it to wait for a background subagent, its time would be counted as a tool wait.
- **`Task` (Claude Code, older name of `Agent`):** not observed; included in the subagent list as a guess.
- **Codex plain shell calls:** the function-call name for a plain shell command was not seen in the data (only `exec`, as a custom tool); the tests use `shell` as a fixture name only.
- **Codex fork handling:** whether a forked subagent's copied history carries timestamps before its own turns was not checked on a real forked rollout.
- **Codex `turn_attribution` (see Concerns):** effect not verified.
