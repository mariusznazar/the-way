# Report of executor 17 — slice 17, the measures of a real Codex cycle

**Status:** done

## Commits and files

- `e8bef72` Count a read of the decision log named with doubled backslashes in the source text of a Codex tool call
- `task-cycle/cycle_measures.py` +7 -5 (the description paragraph of the log path, the constant `SEPARATORS` replacing `BACKSLASH`, `names_log`)
- `task-cycle/test_cycle_measures.py` +19 -0 (two tests in `CodexReadsTest`)

## The real run (counts and facts only)

Source: the user's Codex home (read only) and the user's Claude Code home (read only: the directory listing `projects/*/<id>.jsonl` of `resolve`, no transcript opened by the script). Output: one file in `.runs/executor-17/` of the worktree, removed.

Cycle chosen: one whole Codex cycle of about 2.9 hours: its orchestrator rollout and its 5 subagent rollouts (the 79 rollouts under the Codex home, 15 of them orchestrators; 64 with a parent).

- Agents of each tool: Codex 6 (1 orchestrator, 5 subagents), Claude Code 0.
- Exit code 0; run read 79 first lines of rollouts (the subagent search) and wrote the one output file.
- Cycle-level measures: calls in all 514 (orchestrator 278, subagents 236), mean context per call, mean context per call of the orchestrator, share of context above 200000 tokens (16.0%), context of the orchestrator's first, middle and last call: all have a value. Cache written 5 minutes, 1 hour, written again by the orchestrator, calls of the orchestrator with a write again, written again by subagents, calls of subagents with a write again: all 6 are `unknown`, as the script's description says (Codex agents). Table of agents: the cache columns of each of the 6 rows are `unknown`; the call counts and the four decision-log columns have values.
- Checked against the rollouts: the orchestrator's 278 calls equal its 278 token usage records; subagent calls (27, 19, 144, 27, 19) equal their own records; the number of records of another thread inside a subagent rollout is 0 (no repeated parent records in this form); the 5 subagents found equal the 5 rollouts that name the orchestrator as parent. A subagent's last context (36557) below its middle one (102795) is a context collapse (`compacted` records are present in the real rollouts).
- Cache figures: the real record has the field `usage.cache_write_input_tokens`, which is 0 in all 6347 token usage records of the 79 rollouts, and has no lifetime split (5 minutes / 1 hour) and no cache read other than `cached_input_tokens` (non-zero in 6323 records). So the figures stay `unknown`: a zero that is no measure of a write. The script's description sentence "Codex's record gives no cache write" is inexact (the field exists and is always 0); I left the sentence, since the measure is right (unknown), and name it here as a remark.
- Decision-log columns of the chosen cycle: log reads 8, 4, 3, 10, 2, 7 for the six agents; index reads 0 for all. No rollout among the 79 holds an output with the title line `# decision_index.py:` in any position (the index postdates them), so the index columns could not be checked against real data; they are 0 and the real data gives no contrary case.
- The nested Claude Code helper: none found. The 79 rollouts hold no call of the command `claude` (a search of the input of every function and custom tool call for the command with a space after it: 0 hits, apart from the notes folder named "Claude code"), and the Claude Code sessions of the same days that name a Codex id (about two dozen sessions) are the user's own sessions that read or analysed Codex cycles, none started by one. So the measures of a nested helper being full could not be tested on real data: the slice's case "where the cycle has one" does not occur in the data; the script's Claude Code reading is covered by its tests only. Not a defect found.

## The defect found, and fixed

A read of the decision log was missed where the path stood in the input of a Codex `custom_tool_call`. That input is JavaScript source, in which a Windows path is written with each backslash doubled (`foundations` + two backslashes + `decisions.md`); the script turned each backslash into one slash and got `foundations//decisions.md`, which `LOG_PATH` does not match. Over all 6116 tool calls of the 79 rollouts: 767 call inputs name the log by a path of either slash form; the script counted 763; 4 custom tool calls missed (all in subagents of one other cycle). On that other cycle (16 subagents), the run before and after the fix differs in two agents' rows: one 2 reads / 32306 bytes -> 4 reads / 81741 bytes, another 0 reads / 0 bytes -> 2 reads / 74937 bytes; no other figure of the file changed. On the chosen cycle the fix changes nothing (0 differing lines).

Fix: `names_log` takes each run of backslashes and slashes as one slash (`SEPARATORS`), the path stays whole (`myfoundations`, `.md.bak`, `.md-old`, `x.md` are no log with doubled separators either); the description paragraph says so.

## Checks

- Test first, red on the base: `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` before the change in `cycle_measures.py`: exit 1, 1 failure (`test_a_path_in_a_source_text_with_its_backslashes_doubled_is_a_read_of_the_log`: `['10','1','0','0'] != ['0','0','0','0']`), 89 tests; the second new test (`test_a_doubled_separator_does_not_make_another_file_the_log`) passes on the base and guards the boundary of the fix.
- First attempt of the fix used the character class `[\/]` (one backslash), which dropped backslashes from the class: the same command failed 3 tests (exit 1), among them two old ones; corrected to `[\\/]`; second run below.
- Passing: `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`: exit 0, 89 tests, OK.
- The real run as above: exit 0 (before and after the fix, both cycles).
- Not run: the whole gate (WAY-160); no check of the index columns on real data (no such record exists).

## Own-work check (WAY-164)

Requirement most likely not met: "the run reads and writes nothing else outside `.runs/`" and "a measure wrong or empty where the script should give it is fixed". Check: `git status` after the run shows only the two files of the slice; a count of all tool calls of the 79 rollouts against the script's own `names_log` (the 767 vs 763 above) and a comparison of the output with the records (calls equal records; subagents equal the parent links). The first showed the defect; the rest showed no more.

## Choices

- One run on a real cycle with 5 subagents (rejected: the largest, with 17 subagents; cost: the nested-helper question is the same on any). A second run on another cycle only to measure the effect of the fix.
- Collapse of a run of separators into one slash (rejected: decoding the escapes of a JavaScript string literal — a parser for an input the script cannot know the language of; cost of the choice if wrong: `a//b` counts as `a/b`, the same file on every system the cycle runs on).
- Cache sentence of the description left as it is (rejected: rewording; it changes no figure, and the decision on the cache figures of Codex belongs to the task's other items; cost: the sentence says "gives no cache write" where the record gives a constant 0).

## Beyond the dispatch

None beyond the read of `task-cycle/change/SKILL.md`, `slice.md`, `WAY-339` (read whole at the range given), `task.md` lines 30-89 and the file `cycle_measures.py` / `test_cycle_measures.py` (the test file in the parts around the Codex tests and the reads tests, lines 245-305, 940-1060, 1150-1335).

No change of a test that holds a `decision:` line, no invariant's test changed.

## Unread material

- `foundations/decisions.md` WAY-344 (2741-2901) and WAY-308 (7055-7121), `foundations/part_map.md:101-112`, `task.md` lines 38 and 80-84 of the *Read* beyond the lines I read: I read WAY-339 whole and `task.md:30-89` (To do 11 and question 6 included); WAY-344, WAY-308 and the part map were not read: the change is a path comparison in the script and touches no rule of those.
- The rest of `test_cycle_measures.py` (lines 1-245, 305-940, 1060-1150, 1335 on), read only by names and where the failures led.

## Searches not found or unclear

- A nested Claude Code helper of a Codex cycle: not found in the 79 rollouts or in the Claude Code sessions of the same days (see above); how Codex would start one is not described in the task or the foundation passages I read.
- Real record with the title line of the index: none exists in the rollouts.

## Working copies

All in `.runs/executor-17/` of the worktree: the probe scripts (13 small files), the base copy of `cycle_measures.py`, and 4 output files of the script. Removed before return: `.runs/executor-17/` no longer exists (checked); no log or watcher left; nothing else was written outside `.runs/` and the two committed files.
