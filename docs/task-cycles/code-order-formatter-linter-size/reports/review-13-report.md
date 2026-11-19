PASS 1f09e4d6adff2789f9fa4fe432bd73b546bd34d6

# Review of slice 13 — the reading of the transcripts moved out of the report of the stages

Range `d84a1fe9..1f09e4d6` (one commit, `1f09e4d6`); `git rev-parse HEAD` in the worktree is `1f09e4d6adff2789f9fa4fe432bd73b546bd34d6`.
Changed files: `task-cycle/cycle_stages.py` (1273 -> 582 lines), `task-cycle/stage_transcripts.py` (new, 755 lines),
`task-cycle/test_cycle_stages.py` (2399 lines), `foundations/part_map.md` (+1 line).

Blocking findings: 0. Minor: 1. Out of scope: 1 (the same Minor, see below).

## Findings

### Critical

none

### Important

none

### Minor

1. **`stage_transcripts.py` is named in no table of the guidelines of the kind `shared-module`** — `guidelines/coding-shared-module.md:13-15`
   (the table *Files of this kind* holds `relation-model/fingerprint.py` only). The module is one that other scripts import and
   its description says so (as that of `process-audit/stage_pricing.py` does, which the table does not name either), so a reader
   who opens the guideline of the kind does not meet it. The slice's *Change* lists no guideline file, and the task carries the
   question of the kind to the cycle (`task.md:108`), so this is outside the slice and outside the task of this range; the executor
   named it as its choice 4. Evidence: grep of `stage_transcripts` over `guidelines/` finds no hit in that file. Not blocking;
   scope: out of scope of this slice (a question the task carries to the cycle).

## What I verified

- **Moved code is unchanged.** `reports/review-13-ast-compare.py` parses the base `cycle_stages.py` and the two new files and compares
  the AST of each top-level function, class and assignment by name. All names of the base are present exactly once in the union of
  the two new files, none twice, and every one has an identical AST except `read_codex_agent` and `read_claude_agent`, the two
  that the slice divides. New names: `CodexScan`, `codex_agent`, `claude_counts`, `claude_usage`.
- **The two divisions read line by line against the base.** `read_codex_agent` (base 131 lines): the loop's state became fields of
  `CodexScan`; `read_event` and `read_response_item` carry the two branches (the two `continue`s of the call case became `return`s at
  the end of the iteration, so nothing that followed them is skipped differently); the turns, the sort and the note on open
  turns keep their order relative to every other effect (the sort moved before the note, which reads neither the sort nor the list
  it sorts); `codex_agent` builds the agent with the notes in the base order (open turns, files named, exec left out, call notes).
  A `None` turn in `own_turns` still raises the same `KeyError` at the same point (after the loop). `read_claude_agent` (base 114):
  `claude_counts` is the six `required*` reads in the base order, run at the same point of the loop; `claude_usage` builds the
  same `Usage` from the same counts.
- **Boundary, crafted input.** I ran the executor's compare script from my own directory against the base script (`git show d84a1fe9:...`)
  and the new `cycle_stages.py`: 51 crafted inputs (missing and null fields, floats, negatives, booleans, 16-digit counts, bad and
  non-text timestamps, `<synthetic>`, names with `..`, a bar and a lone surrogate, more than 20 names, a line nested 100000 deep,
  a non-UTF-8 and an empty file, Codex records without `thread_id`/`turn_id`/`usage`, another thread's bad count, a subagent
  rollout given as the orchestrator, exec calls that call a subagent tool, an unrecognised `_call`, missing session, no session,
  `--output`). Exit code, stdout and stderr equal byte for byte in all 51 (exit codes 0, 1 and 2 seen) and the written report file's
  bytes equal. Output kept in `reports/review-13-compare-output.txt`. A reading of the script's cases: they follow the requirements of
  the description of `cycle_stages.py` (the fields it says it needs), not only the code.
- **Slice's requirements.** `cycle_stages.py` stands at 582 lines, `stage_transcripts.py` at 755 (limit 1200); the largest function is
  `report` 108 lines in `cycle_stages.py` (unchanged since the base), `read_claude_agent` 91 and `read_codex_agent` 32 in the module;
  each new part has a name of its own and a one-sentence description. The description of `cycle_stages.py` stays whole there (the
  diff of that file removes no line of the docstring). The module's description says what it holds, that it was moved out of
  `cycle_stages.py` and that it is imported, never run, and runs nothing when imported; there is no import of `cycle_stages` in it.
  `cycle_stages.py` imports `Agent, Call, CycleStagesError, MissingFieldError, Session, Usage, read_session`, each of which the code
  below the import uses (counted by grep); the tests read no moved name through `cycle_stages`. `foundations/part_map.md:111` names the
  module among the *Trust boundary* files of `task-cycle`. `process-audit/audit_count.py` is untouched (Slice 17). The test that patched
  `datetime` of `cycle_stages` now patches it in `stage_transcripts`, where `read_codex_session` uses it; the cause is the move, the
  assertions are unchanged.
- **Foundation entries.** WAY-339 (`decisions.md:8404`) and `audit-series-script-paths` (`invariants.md:410`), written earlier (F9), already
  name the module; the code agrees. `cross-part-imports` and `script-imports`: the import is a sibling in the same directory and
  part. WAY-365: the slice is a move without a change of behaviour, as the decision requires. No invariant test was changed in this range.
- **Guidelines.** `guidelines/coding.md` (size, formatter, linter, field-missing rule WAY-344, the script start: the module is imported,
  so the rule on starting and ending does not reach it), `coding-measuring-report.md` (`cycle_stages.py` is a `copy`; no rule),
  `coding-shared-module.md` (importing runs nothing: checked below). No finding.
- **Tests.** The tests of the part were not weakened: 534 pass; the only changes to them are the source of the moved names, one patch
  target and the formatter's re-layout of lines. They would fail if the reading broke, since they assert tokens, waits, names and error
  messages of the transcripts as before. No code that exists to pass a test was found: the new methods hold no branch for a test's input.

## Checks I ran (command, exit code)

`<ruff>` = `the Ruff of the quality environment of the main checkout`; run from the worktree root.

| Check | Command | Exit |
|---|---|---|
| format | `<ruff> format --check --config ruff.toml task-cycle/cycle_stages.py task-cycle/stage_transcripts.py task-cycle/test_cycle_stages.py` | 0 ("3 files already formatted") |
| lint | `<ruff> check --config ruff.toml --ignore-noqa` on the same three files | 0 |
| foundation | `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| part-map tests | `python -B gate/run_tests.py elements/part-map` | 0 (40 tests) |
| tests of the part | `python -B gate/run_tests.py task-cycle` | 0 (534 tests, 2 skipped) |
| tests of the audit | `python -B gate/run_tests.py process-audit` | 0 (276 tests, 536 s, run in the background and read in stretches under four minutes) |
| sizes | `function_sizes` and `file_lines` of `agent-instructions/test_size_invariant.py` on both scripts | no function over 110; 582 and 755 lines |
| import runs nothing | `python -B -c "import sys; sys.path.insert(0,'task-cycle'); import stage_transcripts" < /dev/null` | 0, stdout 0 bytes, stderr 0 bytes |
| AST compare | `python -B .runs/review-13/cmp.py` (kept as `reports/review-13-ast-compare.py`) | 0; only the two divided functions differ |
| differential at the boundary | the executor's `compare.py` pointed at `.runs/review-13/exec/` with the base script from `git show d84a1fe9:task-cycle/cycle_stages.py` (output in `reports/review-13-compare-output.txt`) | 0; 51 cases, 0 different, output file bytes equal |
| whitespace | `git diff --check d84a1fe9..1f09e4d6` | 0 |

Not run: the full gate (the handoff forbids it).

## Declined to judge

- The change of the audit's list of scripts in `process-audit/audit_count.py` (it does not yet read the history of `stage_transcripts.py` as a change of the script that measures the cost, WAY-339): the handoff and the slice give it to Slice 17 (F9).
- The docstring of `agent-instructions/test_size_invariant.py` that still says 80 and 1000: another slice changes the thresholds.
- Whether `stage_transcripts.py` should enter the table of `guidelines/coding-shared-module.md` (see the Minor finding): the task carries it to the cycle.

## Reaches beyond the handoff

- `agent-instructions/test_size_invariant.py:43-53` (the signatures of `function_sizes` and `file_lines`), to call them as the slice's checks say.
- `foundations/part_map.md:100-115`, to see the entry of `task-cycle` in place.
- `grep` of `cycle_stages` and `stage_transcripts` across `*.py`, `guidelines/`, `foundations/` to find importers of `cycle_stages.py` that load it by path (none: `audit_count.py` and its tests run it as a process).

## Working copies

`.runs/review-13/` held `old.py` (the base script), `cmp.py`, `compare.py`, `exec/` (the old script and the crafted inputs of the compare run), the logs of the two gate runs and the empty import outputs. I kept `reports/review-13-compare-output.txt` and
`reports/review-13-ast-compare.py` beside this report and removed `.runs/review-13/` before returning (no worktree or clone was made).

## Unread material

- `foundations/decisions.md`: WAY-365 (6616-6653) and WAY-48 (2565-2593) read whole; WAY-339 (8400-8537) read in part, lines 8400-8412 and by grep the passages that name the two scripts, not the rest of its 138 lines.
- `foundations/invariants.md`: function-and-file-size, cycle-stages-refuses-crafted-names, audit-series-script-paths, cross-part-imports and script-imports read whole.
- `guidelines/testing.md`: not read (the slice changes the source of names in a test and one patch target; the executor's report and the diff of the test file show no new test); `guidelines/coding.md`, `coding-measuring-report.md`, `coding-shared-module.md` read whole.
- `task-cycle/test_cycle_stages.py`: the diff read whole, the file (2399 lines) not read whole.
- `process-audit/stage_pricing.py`: lines 1-12 only (the description it is the model of).
- F2 (WAY-385) and F9: read only through the passages above (`function-and-file-size`, `audit-series-script-paths`) and the handoff's thresholds; the entry WAY-385 itself not opened.
- `.runs/task-cycles/code-order-formatter-linter-size/task.md`: lines 25-40 and 106-110 (the To do and the questions carried to the cycle), as named.

## Searches not found or unclear

none
