# Task 4 report

Status: DONE.

## RED
`python -B gate/run_tests.py instruction-files` -> `Ran 71 tests`, `FAILED (failures=10, errors=1, skipped=5)`.
The failing set is exactly the brief's: ERROR `test_each_sentence_is_tested_once_whatever_the_number_of_paths`;
FAIL (10 counting the two subtests of the agents-import test) for the two-segment warning, wrapped sentence,
home/root soundness, windows two-segment, agents import (x2), CRLF, files-alone-from-home, network spellings,
memory sentence. The three opposite-failure tests passed already.
Differences from the brief's counts: 71 vs 57 tests (the base has the Task 3 fix rounds' tests); skipped=5 vs 1
(link and POSIX-only tests are skipped on this Windows machine, and the new network class is Windows-only).

## GREEN
Same command: `Ran 71 tests`, `OK (skipped=5)`, exit 0. Output: `.runs/task-cycles/instruction-files-part/reports/check_4_tests_instruction_files.txt`.

## Reconciliation with the current file
- `is_network(token)` delegates to `network_shaped`: one rule for tokens and link targets (Windows only; elsewhere False).
- `resolve(token, bases)` returns False for a network token before any `os.path` call, also for the bare path and for
  every joined candidate (a join with a `\\host` path would otherwise yield a network path). Brief's version had no such guard.
- `local_form`, `network_shaped`, `leads_out`, `directory_link`, the explicit-stack walk were left untouched.
- Brief's new test class `NetworkPaths` clashed in name with the existing Windows-only class; it is named `NetworkTokens`
  and skipped off Windows (the rule is Windows-only, so a POSIX run would not note these tokens).
- Paragraph ends at list item, heading, table row (P4) as in the brief; its tests kept.
- Docstring, `bisect`, `BLOCK_START`, `SENTENCE_END`, `NOT_LOADED*`, `paragraphs`, `negates_loading`, `says_not_loaded`,
  `bare_path`, `segments`, `check_file` (new `agents_beside`) and `check` applied by intent.

## Runs
User's global file (`--file C:/Users/Mariusz/.claude/CLAUDE.md`): exit 0, `0 error, 0 warn, 4 info` (3 non-size):
`references\`, `full_template.md`, `mini_template.md` at line 46 as "a name relative to a place the sentence gives...".
Differences from the brief's expectation come from the changed input, not the code: the file now names
`scripts\locations.json` by an absolute path that exists (no WARN), and the memory sentence with `~\.claude\memory\`
is no longer in the file (no INFO about it). Output: `reports/check_4_global_file.txt`.

the-way (`.`): exit 0, `0 error, 1 warn, 3 info`; WARN `AGENTS.md:20` `_zadania\` does not exist (a relative
directory in the backlog line, resolves only in the author's notes); INFO skill-dir note. Output: `reports/check_4_the_way.txt`.

## Files changed
`instruction-files/check_instructions.py`, `instruction-files/test_check_instructions.py`.

## Concerns
- The `_zadania\` warning in the-way's own AGENTS.md is a two-segment-less name... it is a single segment in-repo, so it
  stays a warning (the one-segment note applies only outside the repository). Not a code defect; AGENTS.md is out of scope.
