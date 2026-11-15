FAIL e1ab383eeb425a811a9f7a1a3663b027414a13f1

# Review of slice 5 — the measure of the log and the index in each agent's context

Range `4ef3fcb..e1ab383` (one commit, `e1ab383`), files `task-cycle/cycle_measures.py` and
`task-cycle/test_cycle_measures.py`. `git rev-parse HEAD` printed `e1ab383eeb425a811a9f7a1a3663b027414a13f1`.
Reviewed as a planned slice at a trust boundary (`task-cycle/cycle_measures.py`, part map, entry `task-cycle`).

Counts: blocking 1 (Important), Minor 2, out of scope 0.

## Findings

### Important

**I1. A missing container field of the reworked transcript reading is read as "no tool blocks" with exit 0, against WAY-344; a test pins it.**

- Place: `task-cycle/cycle_measures.py:311-315` (`read_claude_blocks`: `message = entry.get("message")`,
  `content = message.get("content") if isinstance(message, dict) else None`, then `return` when the content
  is not a list), `task-cycle/cycle_measures.py:431-434` (`read_codex_record`: `payload = entry.get("payload")`,
  return when it or its `type` is not there), `task-cycle/cycle_measures.py:271-274` (`result_text`: a `text`
  block without `text` is dropped, so the read counts 0 bytes); the test
  `task-cycle/test_cycle_measures.py:439-448` (`test_a_content_that_is_no_string_or_list_is_not_counted_and_ends_no_run`),
  whose value `"DELETE"` deletes `message.content` from an assistant line and a user line and asserts the run
  ends with exit 0 and those lines counted as nothing.
- What is wrong: this change reworks the reading of a Claude Code transcript (it now reads the content
  blocks of assistant and user lines) and of a Codex rollout (it now reads `response_item` records). WAY-344
  binds "the whole reading of each file whose way of reading the change reworks — every field of that
  file": a field the script needs that is missing ends it with exit code 2 and a message naming it, "never
  guessing and never reading the absence as an empty value"; its *Verification* lists as a violation "a
  change that reworks the reading of a file checks the field it added and leaves the other fields of that
  file unchecked". The change checks the block fields the plan enumerates (`id`, `name`, `input`,
  `tool_use_id`, `content`; Codex `call_id`, `name`, `arguments`/`input`, `output`) but reads the absence
  of the containers they live in as empty: an assistant or user line with no `message` or no
  `message.content`, a Codex `response_item` with no `payload`, and a `text`/`input_text` block with no
  `text` (this last one even counts as a read of 0 bytes).
- Why it matters: this is the quiet pass WAY-344 exists to prevent. If Claude Code renames
  `message.content` (or Codex renames `payload` of a `response_item`), every assistant line still passes
  `read_response` (it needs `message.usage`, not `content`), so the run ends with exit 0 and every agent's
  four figures read `0` — a false "no reads of the log" in exactly the measure WAY-339 adds to judge whether
  the change of the reading rule lowered the cost, and in the "before" figures this task puts in the request.
  The plan does not mandate the absence-as-empty reading: its sentence "a content that is no string or list
  ... end the reading with exit code 2 or are not counted" allows exit 2, and a missing content is no content
  of another type. Requiring the containers costs no real run: my count over the 150 latest Claude Code
  transcripts with their subagents (410 files, 46,951 assistant and 29,482 user lines with a list or text
  content) found no assistant or user line without `message` or `message.content`, and no tool
  result without `content`; in the 79 Codex rollouts no `response_item` payload lacked its type (I did not
  count a missing `payload` itself).
- Evidence: `.runs/review-5/crafted.py` cases `user_content_missing`, `assistant_content_missing`,
  `text_block_no_text`, `codex_payload_missing` — each exit 0, no `Error:`, figures `0 | 0 | 0 | 0` (the text
  block case `0 | 1 | 0 | 0`). The test above asserts this behaviour for the deleted content.
- What would fix it: on an assistant or user line, `message` and `message.content` read with `member` (a
  content present but not a list stays not counted, as the plan allows); on a `response_item`, `payload` read
  with `member`; a `text`/`input_text` block without `text` ends with exit 2 naming it; the `"DELETE"` subcase
  moves to a test that asserts exit 2 and the field's name. Whether a block's or payload's `type` (a
  discriminator: its absence means a kind the reading does not know) is under the same check is the fixer's
  judgement; I do not require it.

### Minor

**M1. A line so large that parsing it raises `MemoryError` ends with a traceback and exit 1, not exit 2.**

- Place: `task-cycle/cycle_measures.py:197-214` (`json_lines` catches `ValueError` and `RecursionError` around
  `json.loads`, and `OSError` and `UnicodeDecodeError` around the loop; `MemoryError` passes).
- What: the slice says a huge text "end[s] the reading with exit code 2 or [is] not counted, never with a
  traceback". `.runs/review-5/memory.py` patches `json.loads` to raise `MemoryError` and calls `main`: the
  error escapes `main`, which at the command line is a traceback and exit 1. Step 12 of
  `task-cycle/skill/SKILL.md:563-566` gives the orchestrator a route only for exit 2 with an `Error:` line.
- Why Minor and not Important: no wrong figure results — the run writes nothing — and the trigger is a single
  line that exhausts the memory of the machine; a 60,000,000-byte result (case `huge_60mb`) and a
  3,000,000-character input (the executor's test) are read and counted whole. Neither tool writes lines of
  that order. A fix is cheap: catch `MemoryError` in `json_lines` (around `json.loads` and the loop) and raise
  `MeasuresError` naming the file and the line.

**M2. A subtest that never runs.**

- Place: `task-cycle/test_cycle_measures.py:1150-1153` (`test_an_output_that_is_no_text_is_not_counted` loops
  over `None` and `continue`s at once).
- What: the `None` case asserts nothing; the comment says it is tested elsewhere (it is, at
  `task-cycle/test_cycle_measures.py:1159-1171`). Polish: drop `None` from the tuple.

## Considered and not a finding

- The trust boundary, crafted input of my own (`.runs/review-5/crafted.py`, 42 cases, each run as a separate
  process of the script): an id used by a call in the orchestrator and a result in its subagent, and the
  reverse, counts nothing in either (each agent has its own counter); the same id used by both, each with its
  own pair, counts in each; a result that is a mapping settles the call and a later text result for it is not
  counted (the slice's "second result" rule); a line whose `type` is a list, a `message` that is a list, a
  block with no type: not counted, exit 0; a deep input 900 levels inside a block, Codex arguments 100,000
  levels deep and a 5,000-digit number in Codex arguments: no traceback (the latter still finds the log by the
  raw text); a line-start pattern of 200,000 tabs and 200,000 digits five times: no backtracking blow-up; a
  60 MB result: counted whole, exit 0. Nothing from a transcript reaches the file but through `cell`: a
  subagent meta description and type, and a Codex `agent_path`, with bars, newlines, a `#` and U+2028 came out
  on one row with bars as `/`; the four new cells are `str(int)` of counters made in the script
  (`task-cycle/cycle_measures.py:607-610`).
- Path forms: `.` at a sentence end, `:120`, `~`, a Windows absolute path, `git show HEAD:`, `--log=`, quotes
  count; `.bak`, `-old`, `Foundations/Decisions.md` and `foundations//decisions.md` do not. The last two are
  misses the docstring does not name; they are rare and the docstring's list of approximations is not claimed
  to be exhaustive — not a finding.
- Index title forms: line 1 of a Read (`     1<TAB>`), the arrow form, the second line after CRLF count; a
  `grep -n` prefix (`1:`) and a BOM before the title do not. `elements/common/decision_index.py:193` writes
  UTF-8 without a BOM, so a file it writes is recognised. In 5,685 real Read results the first line had the
  `spaces, digits, TAB` form, so the recognition fits Claude Code's Read output.
- An `Agent`/`SendMessage` call whose prompt names the log counts the subagent's report as log bytes of the
  caller. This follows the slice's rule ("a text value of the tool's input") and the docstring states it
  (`task-cycle/cycle_measures.py:63-65`).
- Codex form: the executor's claim checked on the 79 rollouts under the Codex home by shape only:
  `function_call` (`arguments` a string, 1,125), `custom_tool_call` (`input` a string, 4,991), outputs a
  string or a list of `input_text`/`input_image` blocks; no `local_shell_call` record; 64 subagent rollouts,
  none sharing a call id with its parent and none holding another thread's usage records. Counting the four
  figures of a Codex agent rather than `unknown` is what the slice asks when the form is confirmed.
- No line was added before `## Agents`; the four columns end the table, in the slice's order; the full-file
  tests of the Claude, Codex and mixed cycles pin every line. `process-audit/` is unchanged in the range.
- The tests fail when the behaviour breaks: expected figures are literals worked by hand (I re-derived the
  two hand-worked cycles: orchestrator `15 2 70 1`, subagent `3 1 53 1`; Codex `16 3 53 1` and `3 1 0 0`);
  the Codex backslash case is found only through the parsed arguments, so dropping that parse fails it.
- Size: `task-cycle/cycle_measures.py` is 728 lines; the-way has no rule of size of its own (WAY-328), so a
  structure finding would be Minor; I raise none.

## Declined to judge

- `task-cycle/skill/SKILL.md:560-562` says the script "counts the context and the prompt cache of the cycle's
  agents" without the log and the index: the file is not in this slice's *Change*; the review of the whole
  change judges it.

## Checks

| Check | Command or method | Exit code / result |
|---|---|---|
| Head | `git rev-parse HEAD` | 0, `e1ab383eeb425a811a9f7a1a3663b027414a13f1` |
| Range | `git log --oneline 4ef3fcb..e1ab383`, `git diff --stat 4ef3fcb..e1ab383`, `git diff 4ef3fcb..e1ab383` | 0; one commit, two files |
| The slice's check 1 | `python -B -m unittest discover -s task-cycle -p test_cycle_measures.py` | 0, 79 tests OK |
| The slice's check 2 | `python -B -m unittest discover -s process-audit -p test_audit_count.py` | 0, 182 tests OK (346 s) |
| `process-audit` untouched | `git diff --quiet 4ef3fcb..e1ab383 -- process-audit` | 0 |
| Private paths in the two files | `python -B task-cycle/private_paths_check.py <file>` for each | 0 and 0, 0 listed |
| Crafted input | `python -B -I .runs/review-5/crafted.py <worktree>` (42 cases, each a subprocess of the script) | 0; results above and in I1 |
| `MemoryError` | `python -B -I .runs/review-5/memory.py <worktree>` (`json.loads` patched to raise) | 0; the error escapes `main` (M1) |
| Shapes of real transcripts and rollouts | `python -B -I .runs/review-5/survey.py <out>` (counts of keys and types only, no content) | 0; figures in I1 and above |
| Real sessions | `python -B -I .runs/review-5/real.py <worktree>`: the script on the 40 latest Claude Code sessions and the 15 Codex orchestrator rollouts | 0; 40 of 40 and 15 of 15 ended with exit 0, no traceback |
| Worktree untouched | `git status --short` | 0, empty |

Not run: the gate (the cycle's own run). A real line large enough to raise `MemoryError` (simulated instead).

## Reaches beyond the dispatch

- `elements/common/decision_index.py:1-60` and the lines found by searching `encoding=` (71, 188, 193): the
  usage, to see whether the command that writes the index names the log (it does not; it writes to
  `--output`), and whether the file is written with a BOM (it is not).
- A search of the worktree for lines beginning `# decision_index.py:` (none outside the index) and for
  `cycle_measures`, `## Agents` and the table header (to see what reads the file's table:
  `process-audit/audit_count.py` reads only the labels before `## Agents`).
- Real Claude Code transcripts under the Claude home and Codex rollouts under the Codex home, read for shapes
  and run through the script, counts only, as the slice's own Codex confirmation does.

## Working copies

- `.runs/review-5/` in the worktree held `survey.py`, `crafted.py`, `memory.py`, `real.py`, their outputs
  `survey.txt`, `crafted.txt`, `audit_tests.txt` and the folder `work/` of crafted transcripts and outputs.
  I removed the whole directory `.runs/review-5/` before returning (`Remove-Item -Recurse`; `Test-Path`
  then printed `False`). The scripts and their outputs are not kept: the outputs named real sessions in
  `work/`, and the figures the report needs are copied above. No worktree or clone was made. `git status
  --short` of the reviewed worktree was empty before and after.

## Unread material

`task-cycle/test_cycle_measures.py` lines 570-779 (unchanged by the range; see below). Read whole: the method `task-cycle/review/SKILL.md`; the handoff; the executor's report; the diff of
the range; `task-cycle/cycle_measures.py` whole; `task-cycle/test_cycle_measures.py` lines 1-569 and 780-1239
(every new and changed test and their helpers); lines 570-779, the rewrite and reading-error tests that the
range leaves unchanged, I did not read; WAY-339 (7275-7359), WAY-344 (2709-2820), WAY-48 (2384-2412), WAY-38 (2513-2537),
WAY-229 (5644-5734); part map entries `task-cycle` (96-106), `process-audit` (119-129), "External context"
(245-252); invariants 86-94 and 116-144; `process-audit/audit_count.py` 125-189 and 640-669;
`task-cycle/skill/SKILL.md` 545-572; the docstring and constants of `elements/common/decision_index.py`
(1-60). The task's passages were read as the handoff copies them.

## Searches not found or unclear

- The arrow form of the Read tool's line number (`N→`), which the regex allows: not found in the 5,685 real
  Read results I counted (all `spaces, digits, TAB`). Allowing it costs nothing; unclear whether any version
  of Claude Code writes it to the transcript.
- `local_shell_call` records in Codex rollouts: none found in the 79 rollouts, so the script's not counting
  them is unverified against a real form.
