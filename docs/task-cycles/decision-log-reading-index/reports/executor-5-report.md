# Report of executor 5 — slice 5, the measure of the log and the index in each agent's context

## Status

`done`.

## Files and commits

- `e1ab383` Count in cycle_measures the bytes and reads of the decision log and of its index for each agent
  - `task-cycle/cycle_measures.py`: +217 / -18
  - `task-cycle/test_cycle_measures.py`: +457 / -16
- `process-audit/audit_count.py` and its test are untouched, as the slice says.

## What the change does

- Four columns end the table of agents: `Decision log bytes`, `Decision log reads`, `Decision index bytes`,
  `Decision index reads`. No line was added among the cycle-level lines before `## Agents` (the full-file
  tests of the Claude, Codex and mixed cycles still assert every one of those lines).
- Claude Code: a `tool_use` block of an assistant line is paired by id with the `tool_result` block of a later
  user line. A read of the log is a call whose input holds, at any depth, a text value that names a path
  ending with `foundations/decisions.md` (backslash taken as a slash, with a boundary before and after, so
  `foundations/decisions.md.bak` and `myfoundations/decisions.md` are no hits). A read of the index is a
  result whose text holds a line beginning `# decision_index.py:` (the number a Read tool puts before a line
  allowed in front). Bytes are the UTF-8 bytes of the result text; list results are the `text` blocks joined
  with nothing between.
- Codex: confirmed from real rollouts under the Codex home (79 files; only shapes read, no content copied
  anywhere). The tool records are `response_item` records whose payload is `function_call` (`arguments`, a JSON
  text), `custom_tool_call` (`input`, a text), and the payloads `function_call_output` and
  `custom_tool_call_output` (`output`, a text or a list of `input_text` and `input_image` blocks), paired by
  `call_id`. So the four figures of a Codex agent are counted, not `unknown`.
- The docstring says what is counted and what stays approximate (the passage the slice lists, plus the points
  in "Choices").

## Checks

| Check | Command | Exit |
|---|---|---|
| First failing test (a transcript with one Read of the log), before the code | `python -B -m unittest discover -s task-cycle -p test_cycle_measures.py -k test_a_read_of_the_log` | 1 (assertion: `['10','1','0','0'] != ['0','0','0','0']`) |
| Same test after the code | same | 0 |
| The slice's check 1, 79 tests | `python -B -m unittest discover -s task-cycle -p test_cycle_measures.py` | 0 |
| Private paths in my two files | `python -B task-cycle/private_paths_check.py <file>` for each | 0, 0 listed |
| The slice's check 2 | `python -B -m unittest discover -s process-audit -p test_audit_count.py` | 0 (182 tests, OK, 327 s) |
| Mutation of the code (10 mutants, run by a script in `.runs/executor-5/`, code restored and compared byte for byte) | `python -B -I .runs/executor-5/mutate.py` | 10 caught, 0 survived |

The tests that a crafted transcript gives are in `CraftedReadsTest` and `CodexReadsTest`: a content that is no
string or list (assistant and user lines, also missing); blocks that are no objects, or have a `type` that is
a list or a number; a result that is a number, mapping, boolean, or a list with no text; an input that is a
string, list, number, mapping; an input nested 3000 deep; an input text of 3,000,000 characters; a text of
200,000 near matches; a result of 3,000,000 bytes; a lone surrogate; an id repeated, a result before its
call, a second result, a result with no call, a call with no result; lines of another type; ids and tool
names with a bar and a newline (nothing but numbers reaches the file); each of the five missing fields in
Claude Code (one test with a `subTest` per field) and the six of Codex.

## Own-work check (WAY-164)

- Requirement most likely not met: a crafted transcript ends the reading with a traceback, or the recognition
  does not hold on a real transcript, since the tests use transcripts written by hand.
- Check, first part: crafted input. My crafted-input tests found the first gap before the commit: a Codex record
  whose `payload.type` is a list ended with `TypeError: cannot use 'list' as a dict key` (the test
  `test_a_record_that_is_no_tool_record_is_not_counted` errored on it, the test run's exit code was 1); fixed
  by checking that the type is a string, rerun passed. A second gap in my own tests (the assistant-line result
  and the user-line call were tested together and so one mutant survived) was closed by splitting the test.
- Check, second part: the script run on real sessions. `.runs/executor-5/real_run.py` ran the script on the 12
  latest Claude Code sessions of the-way and 6 of the product loop (with their subagents) from `~/.claude`,
  and `.runs/executor-5/real_codex.py` on all 15 Codex orchestrator rollouts under `~/.codex` (with
  subagents): 18 of 18 and 15 of 15 ended with exit 0. Sums of the four figures: Claude Code 1,603,610 log
  bytes in 519 reads, 11,437 index bytes in 5 reads; Codex 13,338,491 log bytes in 763 reads, no index read
  (no index existed in those cycles). I did not inspect the content of any result; the figures only show that
  real forms (string and list results, `is_error`, image blocks, `api-request-blob` lines) are read without an
  error.

## Choices

1. The index recognised by the common line start `# decision_index.py:` (not by one full title). Rejected:
   one full title — a reworded title would silently count zero; the cost if wrong: a quoted title at a
   line start counts as an index read (said in the docstring). It is anchored at a line start, so a read of
   `decision_index.py` itself (the title is inside quotes there) does not count; a test pins this.
2. Each `tool_use` id counts once; a repeated id is one call and counts as a read of the log where any of its
   lines names the log. Rejected: the last line wins — a crafted second line could hide a read; the cost if
   wrong: a read counted that the later block would not have named.
3. Only lines of type `assistant` give calls and only lines of type `user` give results. Lines of type
   `api-request-blob`, which real transcripts hold (they repeat blocks), are not read — otherwise every call
   would count twice. The slice says "a later line"; the type restriction is mine.
4. A result that is a list with no text block counts as an empty text (a read of 0 bytes); a result that is
   a number, a mapping or a boolean is not counted at all.
5. The field `name` of a call is required (the slice names it) but not used in the count.
6. A result with `is_error` counts the text of the error (the slice says nothing of it); said in the
   docstring. Rejected: skipping it — a rule the slice does not give.
7. The lone surrogate counts as three bytes (`surrogatepass`), so a crafted text ends no run. Rejected:
   `replace` (one byte), a coin toss; the tests pin three.
8. The Codex tool records of a rollout are counted without a thread filter, since the records carry no
   thread id. In the rollouts I looked at, no call id of a subagent's rollout occurs in its parent's. If a
   forked rollout repeats them, they count again (in the docstring).
9. `read_calls` became `read_claude_agent` and returns the calls with the reads (one pass); `read_codex_calls`
   returns a pair as well. Nothing else calls them (only `main` and the tests through `main`).
10. Tests: the Claude Code test cases of the reads derive from a new helper class `ReadsTestCase`; the
    expected figures are literals worked out by hand in comments, not computed.

## Mismatches and reaches

- Mismatch (small): the handoff's line ranges for the decisions differ from the plan's; I used the handoff's.
  WAY-339's text as F7 left it matches the slice.
- Mismatch: the part of `task-cycle/skill/SKILL.md` (step 12, lines 560-562) says `cycle_measures.py` "counts
  the context and the prompt cache of the cycle's agents". It is correct but does not mention the log and the
  index; it is not in this slice's *Change*, so I left it. For the orchestrator's decision.
- Reaches beyond the dispatch: none, except reading real transcripts and rollouts on this machine to confirm
  their form (the slice asks for it for Codex; for Claude Code I did the same).
- Size: `task-cycle/cycle_measures.py` is now 728 lines and its test 1,240. The slice and the plan do
  not name a move first (WAY-365); I did not look up whether the guidelines of the-way hold a size rule.

## Working copies

- `.runs/executor-5/` (ignored, in the worktree) holds `real_run.py`, `real_codex.py` and `mutate.py`, which
  stay as the record of the own-work checks. I removed the files they wrote (`out.md`, `outc.md`, which hold
  the names of real sessions), the backup `cm_backup.py` and `audit_tests.txt`. Nothing else stands outside
  that directory; the code was restored and compared with its backup byte for byte after the mutation run.
- A second copy of the `process-audit` test run, which I started by mistake while the first still ran, was
  stopped (its process ended); it left no file.

## Not run

- The product's full gate (the orchestrator runs it).
- A test of a line so large that `json.loads` raises `MemoryError`: I did not craft one (it needs hundreds of
  megabytes); a `MemoryError` is not caught in `json_lines`. It is a guess that the cost would be a traceback
  on a line of that size; the 200000-deep and the 5000-digit lines already end with exit 2 (existing tests).

## Unread material

none. Read whole: the two files changed, the method and slice method files, the decisions WAY-339, WAY-38,
WAY-48, WAY-344, WAY-229 (each whole), `part_map.md` entries `task-cycle` (from line 96, to its end), `process-audit`
and "External context", `invariants.md` lines 86-144 (three invariants; I read 86-145 in one range), the
docstring and first 120 lines of `elements/common/decision_index.py`, `process-audit/audit_count.py` lines
125-190 and 640-670 (the ranges named, 129-145 and 179-185 inside the first), and `task-cycle/skill/SKILL.md`
545-572. The parts of `task.md` named in the *Read* were copied word for word into the handoff, and I used
those copies; I did not open `task.md` or `plan.md`.

## Searches not found or unclear

- The index's title line: the handoff names `TITLE` and `TITLE_SECTIONS` as "the first title" and the common
  prefix; both are written at the top of the index by lines 132 and 148 of `decision_index.py`, so the
  prefix test works on a file written by the script. Not unclear.
- Where the Read tool's line-number prefix is made (a tab after the number in `cat -n` form; some displays
  show an arrow): I allowed both a tab and the arrow character in front of the title line. Not verified
  against a real transcript that holds a Read of the index (none exists yet).
- Whether a real Codex forked rollout repeats the parent's `response_item` records: not found in 79 rollouts
  (no shared call id); unclear for forks of another kind.
