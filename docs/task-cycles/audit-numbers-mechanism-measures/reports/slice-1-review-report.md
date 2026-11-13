FAIL f0a3829e601ab55dd9825bf0cbb57b1c1f688adc

# Review of slice 1 — the measures script, for Claude Code sessions

Head reviewed: `f0a3829e601ab55dd9825bf0cbb57b1c1f688adc` (`git rev-parse HEAD` confirmed). Range
`2292f334..f0a3829` holds two commits: `a030dbf` (foundation entries, not the slice's code) and `f0a3829`
(the slice).

Changed files (`git diff --stat 2292f334..f0a3829`):
- `task-cycle/cycle_measures.py` — +368
- `task-cycle/test_cycle_measures.py` — +448
- `foundations/decisions.md` — +228/-23 and `foundations/part_map.md` — +1 (commit `a030dbf`, written by the
  foundation-entries agent; read only as far as the dispatch names, see Unread material)

Counts: blocking 2 (Important), Minor 3, out of scope 0.

## Critical

none

## Important (blocking)

### I1. A hostile transcript or meta file ends the script with a traceback and exit code 1, not `Error:` and exit code 2

- Place: `task-cycle/cycle_measures.py:138-140` (`json.loads(line)` of a transcript line) and
  `task-cycle/cycle_measures.py:177-179` (`json.loads` of a `.meta.json`). Both catch only
  `json.JSONDecodeError`.
- What is wrong: `json.loads` raises two other errors on crafted input that the code does not catch:
  `RecursionError` for a deeply nested value, and a plain `ValueError` ("Exceeds the limit (4300 digits) for
  integer string conversion") for a number of more than 4300 digits. Both end the script with an uncaught
  traceback, exit code 1, no `Error:` line.
- Why it matters: the task says exit code 2 with `Error: <message>` on stderr for every failure, and the
  handoff names crafted input at these readings (the session records are untrusted input by the part map's
  External context). A step that closes the cycle and reads exit code 2 as "not read" sees exit code 1 with a
  traceback; the contract is "every failure", not "the failures the author thought of". Nothing is written, so
  no wrong file results; the defect is the contract at the trust boundary.
- Evidence (scratch files in the scratchpad, not in the worktree; command
  `python -B task-cycle/cycle_measures.py <file> --claude-home <home>`):
  - a line `[` x 200000 then `]` x 200000: `RecursionError: Stack overflow ... while decoding a JSON array`,
    exit 1;
  - an assistant line with `"input_tokens": 99...9` (5000 digits): traceback from `json.loads`, exit 1;
  - the same two inputs as an `agent-*.meta.json`: `RecursionError`, exit 1;
  - for comparison a float, a non-UTF-8 file, a line that is not a JSON object, `message` as a string and a
    missing `usage` all end with exit 2 and `Error:` naming the file and line.
- Fix direction: catch `ValueError` (the parent of `JSONDecodeError`) and `RecursionError` at both reads and
  name the file and line; add one test per reading that gives such a line.

### I2. Fields the script looks for data by — `timestamp`, `message.id` — are read as absent-means-default, against WAY-344

- Place: `task-cycle/cycle_measures.py:76-84` (`parse_time`: a missing or unreadable time is the earliest
  possible time), `:110` (`entry.get("timestamp")`), `:121-123` (a missing `message.id` becomes
  `line <n>`), `:158-159` (the order of calls rests on the time).
- What is wrong: WAY-344 (`foundations/decisions.md:11336-11431`) defines a field as any named thing the script
  looks for data by, a JSON key included, and says a missing field ends the script with exit code 2 naming the
  file and the field, "never guessing and never reading the absence as an empty value". The script needs the
  time to put the calls of an agent in the order of their time (task: "The calls of an agent are in the order
  of their time") and the id to count a response once. A line without them is silently placed first, or counted
  as a call of its own, so the first, middle and last call and every rewrite can be wrong, and the file says
  nothing. The executor's report (choices 3 and 4) names both as deliberate, on the ground that the handoff's
  list of needed fields holds six usage fields only. That list is the task's list of the usage fields; WAY-344
  binds the whole reading of each file the change adds (WAY-263: a change that does not do what the entry it
  writes or changes requires is Important).
- Why it matters: a transcript whose time key is renamed, the very case WAY-344 exists for, yields a plausible
  file with wrong contexts for first/middle/last call and wrong rewrites, and no error. A response written over
  several lines without an id would be counted several times and inflate the calls.
- Evidence: a transcript line with `"timestamp": 12345` runs with exit 0 and a call dated the earliest time
  (probe, scratchpad); no test gives a line without `timestamp` or `message.id` and asserts an error. The
  existing missing-field test covers `cache_creation` and `ephemeral_5m_input_tokens` only (WAY-344 asks one
  test per reading, which that satisfies; the finding is the unchecked fields, not the number of tests).
- Fix direction: raise `MeasuresError` naming the file, line and field for a missing or unreadable `timestamp`
  and a missing `message.id` of a non-synthetic assistant line, or have the orchestrator settle in writing that
  these two are outside WAY-344's reading and record it (a question for the orchestrator, not the human).

## Minor

### M1. `parse_time` says UTC and does not convert

`task-cycle/cycle_measures.py:77` docstring says "in UTC"; the code only attaches UTC to a naive time and
leaves another offset as it is (`:84`). Comparison of aware times is correct, so no figure is wrong; the
docstring is. Moot if I2 is fixed by rejecting unreadable times.

### M2. No test that a rewrite is counted within one agent, and none for several orchestrator sessions

The tests (`task-cycle/test_cycle_measures.py:215-269`) cover the four edges and the hand-worked cycle on one
session. Nothing gives two agents whose calls interleave in time to show the rewrite pairs consecutive calls of
the same transcript only, nor two sessions given together to show the orchestrator's first, middle and last call
take the sessions in the order of their time (`cycle_measures.py:260-261`). I read the code for both and it is
right; the tests would not catch a change that merged the agents' calls before pairing them.

### M3. Output ties and stream size

`cycle_measures.py:154` takes the later line of a response where two lines have equal `output_tokens`
(`cycle_stages.py:558` does the same, so the two scripts agree). A single transcript line of gigabytes would be
read whole by `for line in handle`; the file is streamed otherwise, and the count of ids held is bounded by the
number of responses. I set this at Minor: no cap is asked by the task, and a cap would be a choice of the cycle.

## Task and foundation fit (checked, no finding)

- Hand figures: I recomputed the cycle test's file by hand (contexts 1100, 4105, 4203, 510, 2901, 4502, 301,
  10: sum 17632, mean 2204; orchestrator 9408/3 = 3136; 5-minute 9800, 1-hour 5500; rewrites 3900 and 2400).
  They match the test's literals, which are written independently of the script.
- Definition of the rewrite (`:203-215`): `min(max(0, P.read + P.write - C.read), C.write)`, above 2000,
  collapsed when `C.context * 10 <= P.context * 7`; matches the settlement 7 and WAY-351. Mean half-up
  (`:218-221`) and share to one decimal half-up (`:224-229`) are exact integer arithmetic; middle at `(n-1)//2`
  (`:235`). `unknown` where nothing can be averaged, never zero.
- Missing field is never read as zero for the six usage fields and for `cache_creation` (`:101-124`); the error
  names the transcript path with the line and the dotted field; nothing is written on error (errors are raised
  before the output is opened).
- Table cell (`:163-167`): bars become `/`, every Unicode category C character (control, format, bidi override,
  lone surrogate) becomes a space and whitespace collapses, so a newline, U+2028 or a bar cannot break a row;
  probed with `a|b\nc\u2028d\u202ee\x00f\ud800g\u200bh`, non-string `description`/`agentType`, a list as meta
  and `null` fields: all gave one row each and exit 0.
- Output is bytes with LF; same input gave the same bytes in the tests.
- No import of a file of the-way; standard library only (test walks the imports); no subprocess; no absolute
  path in the new files (`test_tracked_files_private_paths.py` passes); `cycle_stages.py` and the other
  `task-cycle` directories are unchanged (`git diff --quiet` exit 0).
- The part-map row adds `task-cycle/cycle_measures.py` to the task-cycle Trust boundary; matches the
  dispatch's risk line.
- A real run against the session of this review's orchestrator (read-only) wrote the whole file with exit 0.
- The refusal of a Codex rollout (exit 2, `cycle_measures.py:143-145`) is an addition the task did not ask for
  in this slice; it is stated in the docstring and tested, and slice 2 adds Codex. I do not grade it.

## Declined to judge

- The Codex reading and the `unknown` cache values for Codex: a later slice's scope (the slice goal says Claude
  Code sessions).
- The foundation entries WAY-348, WAY-349, WAY-350, WAY-352 and the rest of the diff of
  `foundations/decisions.md` in `a030dbf`: written for other slices; judged only as far as WAY-344, WAY-347,
  WAY-351 and the part-map row, which this slice's script has to match.
- A cap on the size of a transcript line: the task asks none, and a cap is a design choice of the cycle (M3).

## Checks run

- `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` — exit 0, 30 tests OK.
- `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` — exit 0, 1 test OK.
- `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` — exit 0, 39 tests OK.
- `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` — exit 0.
- `python -B task-cycle/cycle_measures.py` (session from `CLAUDE_CODE_SESSION_ID`, real transcript, stdout only) — exit 0.
- Crafted-input probes on files made in the scratchpad (outside the worktree), each as
  `python -B task-cycle/cycle_measures.py <file> --claude-home <home>`: deeply nested line (exit 1, traceback),
  5000-digit number (exit 1, traceback), 300-digit number (exit 0, 300-digit value printed), float (exit 2),
  non-UTF-8 (exit 2), `message` as a string (exit 2), `timestamp` as a number (exit 0), blank and empty files
  (exit 0, `unknown`), hostile meta files (table intact; a deeply nested meta exit 1).
- Not run: the product's gate (by instruction); the check "fails on the base before the script exists" (the
  base has no `cycle_measures.py`, so the discovery cannot import it; I did not recreate the base in a separate
  worktree and rely on the executor's stub run, unverified by me).
- The reviewed worktree was not changed (`git status --short` empty before and after).

## Reaches beyond the dispatch

- `task-cycle/cycle_stages.py:515-613` and `:957-1004` (reading of the Claude Code transcript, resolve,
  main), to compare the session resolution and the response-per-id rule with the script's; the dispatch named
  the file whole.
- `git show --stat` of both commits and `git diff 2292f33..f0a3829 -- foundations/decisions.md` headings, to
  know which entries the foundation commit changed.
- `the author's rules file on scripts`, before writing the probe scripts (user's rule).
- `task-cycle/review/SKILL.md` whole, as the dispatch names it. I did not need `fix.md` or `whole_change.md`.

## Unread material

- `foundations/decisions.md` entries WAY-348, WAY-349, WAY-350, WAY-352 and the hunks near lines 11193-11230 and
  11399-11430 outside WAY-344: not read beyond headings; not named by the dispatch's *Read* for this slice
  (WAY-344, WAY-347, WAY-351 read whole).
- `foundations/part_map.md`: read the task-cycle entry (93-103) and External context (232-240) whole; the rest
  of the file not read.
- `task-cycle/test_cycle_stages.py:1-30` and `:225-247` named by the dispatch: not opened; the test form was
  taken from `test_cycle_measures.py` itself and `cycle_stages.py`.
- `task-cycle/cycle_stages.py`: lines 1-514 and 645-955 not read (Codex reading, stages, report).
- The task document and plan: read only the passages the handoff copies.

## Searches not found or unclear

- Where a nested subagent's transcript lies: the handoff and `cycle_stages.py:588-608` read one `subagents`
  folder (a nested subagent has `parentAgentId` in its meta); the script reads the same folder. I have no real
  transcript with a nested subagent to confirm the layout; unverified.
- The handoff does not say whether `timestamp` and `message.id` are needed fields in the sense of the task's
  "needed fields" sentence; I read WAY-344 as covering them (I2). If the orchestrator reads it otherwise, I2
  becomes a question and a decision to write down.
