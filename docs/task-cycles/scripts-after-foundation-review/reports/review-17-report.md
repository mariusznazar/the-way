PASS e8bef720a34924cb4b32bd0f136f51c006e2b504

# Review of slice 17 (base c01fe56763983c7a366ecda82067c06e4dd50582, head e8bef720a34924cb4b32bd0f136f51c006e2b504)

`git rev-parse HEAD` is the head. One commit in the range, two files: `task-cycle/cycle_measures.py`, `task-cycle/test_cycle_measures.py`. The only change to the script is that `names_log` takes each run of backslashes and slashes as one slash (`SEPARATORS`, replacing `BACKSLASH`), plus the description paragraph. Two tests are new, in `CodexReadsTest`. No invariant test is changed and no test holds a `decision:` line (WAY-03: none to name).

## Findings

Blocking (Critical/Important): none.

Minor:

1. `task-cycle/cycle_measures.py:51` — the changed description paragraph has a line of 111 characters, while the paragraph is wrapped at about 100 (the file has 2 lines over 102, the base had 1). Only polish; no effect on behaviour. Evidence: `awk 'length>102'` on the base and on the head.
2. `task-cycle/cycle_measures.py:~28-29` (module description, "Codex's record gives no cache write") — the real record has the field `cache_write_input_tokens` in the usage of every token usage record, and it is always 0. I counted it: the field is present in all 6448 records of the 79 rollouts, and it is non-zero in none. The measure is right (`unknown`: a constant 0 is no measure of a write), but the sentence is inexact. The executor named this and left it, and the task asks only that the figures be `unknown`. Polish: a sentence that says "the record's field is always 0, so the figures are unknown".

Out of scope: none beyond the two Minor findings above, which are within the script touched by this slice.

## What I verified

- The fix is right. `SEPARATORS` is the class "a backslash or a slash" taken in runs, the path stays whole (`LOG_PATH` is unchanged, so `myfoundations`, `.md.bak`, `.md-old` stay other files). The class is linear, so there is no regex-backtracking risk on crafted input. A run of any length becomes one slash, so `foundations//decisions.md` also counts; that is the same file on every system the cycle runs on.
- The tests: the first new test uses a source-text call with doubled backslashes and expects a read of 10 bytes (it fails on the base per the executor's report; the base regex cannot match the doubled form, which I confirmed against the real data below). The second test guards the boundary of the fix (four other names stay no log) with `subTest`. Both assert a figure the script does not compute for itself.
- On real data (my own read-only run, in my own directory): the cycle with 16 subagents run with the base script and the head script, both exit 0, empty stderr. The two outputs differ in exactly two agent rows, as the executor reported (one 32306 bytes / 2 reads -> 81741 / 4, another 0 / 0 -> 74937 / 2); no other line differs.
- Independent count over all 6116 function and custom tool calls of the 79 rollouts: a loose pattern of my own (`foundations`, a run of separators, `decisions.md`, with the same ends) gives 767 call inputs; `names_log` of the head gives 767; no call differs. The executor's count of 767 against 763 on the base is therefore confirmed in form, and the fix leaves no gap and no false positive on this data.
- The report's counts for the run (6 Codex agents in the chosen cycle, no nested Claude Code helper in the data, cache figures `unknown`) are claims about a cycle I did not re-run in full; I verified the cache field fact (Minor 2) and the 79 rollouts / 15 orchestrators / parent counts (the counts of children per orchestrator include 5, 5, 16 and 17). A nested helper being absent from the data is not a defect of the script, and the task allows the executor to report it as it did (the Claude Code reading stays covered by tests).
- Trust boundary: the change handles text of a session record only as a string to match; no path is opened, no command run, nothing is written outside the output file; no crash is possible from the new code (a regex substitution on a string). Hostile input cannot reach a result unescaped through this change (a read is a count and a byte length).
- Own-work check of the executor: the requirement "a measure wrong or empty where the script should give it is fixed" is where the work is weakest, and its check (the count of all calls against the script's own function) would catch it; I reproduced that check independently.

## Checks I ran

- `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` in the worktree: exit 0, 89 tests, OK.
- `python -B task-cycle/cycle_measures.py <orchestrator id> --output .runs/review-17/out_base.json` (base copy of the script) and the same with `task-cycle/cycle_measures.py` of the head: both exit 0; the diff of the two outputs is the two rows above.
- A scratch count of 6116 tool calls of the 79 rollouts (767 / 767).
- A scratch count of the usage field `cache_write_input_tokens` (6448 records, present in all, non-zero in none).
- Not run: the whole gate (WAY-160), as the handoff gives. The "new test red on the base" I did not re-run; I reasoned it from the regex and confirmed the base misses exactly the doubled-backslash calls on real data (the 767 against the base's two changed rows). Unverified by me as a command.

## Declined to judge

- Whether the cache figures of Codex should stay `unknown` or use the always-zero field: set aside; the task asks that they be `unknown` as the description says, and the executor kept it.
- The index columns on real data (no real record has the title line `# decision_index.py:`): set aside; there is no such data to run on.

## Reaches beyond the dispatch

- `.runs/task-cycles/scripts-after-foundation-review/task.md:30-40` and `:78-86` (To do 8-11, question 6) — to read the passages the handoff names.
- The 79 rollouts under the user's Codex home, read only, for the count of tool calls and of the cache field (counts only, no path or content kept).

## Working copies

All in `.runs/review-17/` of the worktree (probe scripts, a copy of the base script, two output files). Removed before return; `.runs/review-17/` no longer exists; `git status` of the worktree is clean. No watcher or timer started.

## Unread material

The foundation entries WAY-339, WAY-344, WAY-308 and `foundations/part_map.md:101-112` named in the handoff: I read none of them whole. The change is a path comparison in the script and a description sentence of the script; no entry's rule is changed by the change, and the decision log's own text is not written by it. The rest of `test_cycle_measures.py` and `cycle_measures.py` beyond the diff, the description and the places I ran: I read only the diff, the description (lines 1-60) and the lines around the changed functions.

## Searches not found or unclear

- None, apart from what the executor named (no nested Claude Code helper and no real record with the index title line exist in the data).
