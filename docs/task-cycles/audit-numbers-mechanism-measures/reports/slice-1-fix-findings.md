# Findings to fix — slice 1

Blocking findings of the review of slice 1 (`reports/slice-1-review-report.md`, head `f0a3829e601ab55dd9825bf0cbb57b1c1f688adc`), copied word for word from the reviewer's report. The review's Minor findings are not part of this fix.

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
