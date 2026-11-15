# Executor report — slice 17 (the test of the invariant of size, marked violated)

## Status

`done`

## Commits

- `2b9914c` — Test the invariant of the size of functions and files, marked violated
  (base `fc9244f`; the one commit, by path, of `agent-instructions/test_size_invariant.py`, 96 insertions, 0 deletions)

## One-line check result

All focused checks passed; the full gate was not run (WAY-160). The first foundation-check run failed (exit 1) only because the new file was not yet tracked; it passes (exit 0) after the commit.

## Report path

`.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-17-report.md`

## Questions

None blocking. One point for the orchestrator (see *Concern* below): the size test finds three script files over 1000 lines at this base, where the trial figure cited in the task (answer 10) and in WAY-385's rationale says two. The invariant still reads `Violated: yes` correctly; no foundation edit was made, since the slice does not own it.

## Concern

The count at this base differs from the trial figures the task and WAY-385 quote (trial at `21ecb62`):

- functions over 80 lines: 11 — same as the decision (the same eleven names as the trial list);
- files over 1000 lines: 3 — the decision and task answer 10 say 2. The third is `elements/common/foundation_check.py` at 1003 lines (the trial file listed 989 lines). The other two are `process-audit/audit_count.py` at 3310 lines (trial 2991) and `task-cycle/cycle_stages.py` at 1178 lines (trial 1009).

WAY-385's rationale says the count was taken "at the commit of the review of the foundation", so this is a difference between that base and this one, not a contradiction within the decision. I did not verify which commits grew `foundation_check.py` by 14 lines after the trial; `git log` shows `b8ef139`, `7063f94` and `bdd1b1d` touched it. The slice needs no change for this, but the cycle should know that the rule's first measured failure list has three files, not two.

## Files changed

- `agent-instructions/test_size_invariant.py` — added, 96 lines (96 insertions, 0 deletions).

## Choices made

1. **Counting convention:** a function counts from its `def` line to `end_lineno` inclusive, with its nested functions inside that span; a method counts as a function; a file counts `len(source.splitlines())`. This matches the trial script's convention (`.runs/coding/sizes_count.py` in the main checkout, read as a reach, see below). Rejected: counting from the first decorator line. Cost if wrong: a decorated function with long decorators is undercounted by a few lines; no current function is near the threshold on that account.
2. **File set:** `git ls-files -z -- <the ten parts>`, keeping names ending `.py` whose basename does not start with `test_`. Rejected: walking the directories with `Path.rglob`, which would include untracked working files. Cost if wrong: none for the tracked set; the test follows git as the handoff requires.
3. **Expected-failure mark:** `@unittest.expectedFailure` on the second test only; the first (counting) test is unmarked, so the counting is checked while the invariant stands violated. The citation comment `# invariant: function-and-file-size` sits in the class directly above the marked test.
4. **Failure message:** one `self.fail` listing every function (`path:line name: N lines`) and every file (`path: N lines`) over a threshold, with the two counts in the first line.

## Checks run (command and exit code)

1. Test first, against the stubs (`function_sizes` returned `[]`, `file_lines` returned `0`):
   `python -B agent-instructions/test_size_invariant.py Counting` — exit `1`; both tests failed on their assertions (`Lists differ: [] != [('inner', 3, 2), ('method', 8, 2), ('outer', 1, 5)]`), so the failures are the expected ones, not a missing name.
2. After the implementation of the counter:
   `python -B agent-instructions/test_size_invariant.py Counting` — exit `0`, `Ran 2 tests … OK`.
3. The invariant's test seen failing once, before the mark was added:
   `python -B agent-instructions/test_size_invariant.py Size` — exit `1`, `AssertionError: 11 functions over 80 lines and 3 files over 1000 lines:` followed by:
   - `installation/install.py:564 run: 120 lines`
   - `process-audit/audit_count.py:1666 read_gate: 108 lines`
   - `process-audit/audit_count.py:2101 read_register: 82 lines`
   - `process-audit/audit_count.py:2293 analyse: 154 lines`
   - `process-audit/audit_count.py:3067 render: 157 lines`
   - `project-level/plan_state.py:248 provenance: 100 lines`
   - `project-level/plan_state.py:350 task_report: 102 lines`
   - `task-cycle/cycle_stages.py:403 read_codex_agent: 121 lines`
   - `task-cycle/cycle_stages.py:644 read_claude_agent: 99 lines`
   - `task-cycle/cycle_stages.py:1022 report: 100 lines`
   - `task-cycle/request_check.py:422 check: 116 lines`
   - `elements/common/foundation_check.py: 1003 lines`
   - `process-audit/audit_count.py: 3310 lines`
   - `task-cycle/cycle_stages.py: 1178 lines`
4. Expected-failure mark added; the whole file:
   `python -B agent-instructions/test_size_invariant.py` — exit `0`, `Ran 3 tests … OK (expected failures=1)`.
5. Mutation for a moment (the walk replaced by `ast.parse(source).body`, which leaves out the nested function and the method), then restored:
   `python -B agent-instructions/test_size_invariant.py Counting` — exit `1`, `FAIL: test_a_function_counts_the_functions_nested_in_it_and_a_method_is_a_function`, `Lists differ: [('outer', 1, 5)] != [('inner', 3, 2), ('method', 8, 2), ('outer', 1, 5)]`. Restored to `ast.walk(ast.parse(source))`; the file is committed in its restored form (the commit shows no mutation).
6. Lint: `<main checkout>\.runs\quality-venv\Scripts\ruff.exe check --config ruff.toml --no-cache --ignore-noqa agent-instructions/test_size_invariant.py` — exit `0`, `All checks passed!`.
7. Foundation check before the commit (file not yet tracked): `python -B elements/common/foundation_check.py` — exit `1`, `foundations/invariants.md:442: function-and-file-size reads test and no test cites it`. This is the expected result for an untracked citing file; not a defect of the test.
8. Foundation check after the commit: `python -B elements/common/foundation_check.py` — exit `0`, `0 errors`.
9. Not run: the full gate `python -B gate/run_tests.py` (forbidden, WAY-160); the slice's checks named no other command.

## Own-work check (requirement, check, result)

- **Requirement:** the invariant's test must list every function and file over a threshold with its size, and the first test must catch a counter that undercounts (a nested function left out).
- **Check:** the mutation in check 5, and the unmarked run in check 3 compared against the trial figures.
- **Result:** the mutation fails as expected (check 5). The unmarked run lists 11 functions, matching the decision and the trial's eleven names, and 3 files, which differs from the decision's 2 (see *Concern*). Both the counter and the listing behave as the requirement states.
- **Weakest point:** the function count depends on the convention of counting from the `def` line (choice 1). I checked it by reproducing the trial's count (11 functions over 80 with the same names); the file count is the part I could not reconcile with the decision, and I reported it instead of changing the threshold or the file set.

## Working copies

None made. The mutation was done in place in the worktree on the committed file and restored before the commit; the unmarked run's capture file under `.runs/` was removed after its listing was copied into this report (check 3). Nothing remains to remove.

## Unread material

- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` lines 652–1002 (Slices 18 to 23 and *Coverage*): not needed for slice 17; read only the header, the *Foundation entries* table, Slice 17, *Choices* and the end (*Orchestrator's additions*) — which the handoff names.
- Everything else the handoff names was read: the handoff and the method file whole (`task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`); the task at lines 30–35 and 108–129 and 527–528; the plan's Slice 17 section, *Choices* and the orchestrator's additions; the invariants `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`, `function-and-file-size` (`ruff-blocking-rules` read as its neighbour); the decisions WAY-08, WAY-51, WAY-16, WAY-360, WAY-361, WAY-385 (E7) and WAY-379 whole; part map `agent-instructions` lines 155–173.
- Not read: the worktree's `ruff.toml` (not named by this slice's handoff; ruff ran against it); `elements/common/foundation_check.py` (run only, not read).

## Reaches beyond the handoff

- `.runs/coding/sizes_count.py` and `.runs/coding/sizes.md` in the main checkout (`<main checkout>\.runs\coding\`): read to match the counting convention of the trial and to check the eleven-function count. Reason: the decision cites that trial as its source; the convention is not stated in WAY-385.
- `agent-instructions/test_linter_invariant.py` (slice 16's test in the same part): read whole for the file's style (module docstring, the `# invariant:` citation, the expected-failure placement).
- `task-cycle/change/SKILL.md` and `slice.md` were read whole as the method names.

## Searches not found or unclear

- Searched for the source of the trial figure of "2 files over 1000" at the current base: found the trial figures at `21ecb62` (`sizes.md`, `task.md` answer 10, WAY-385 rationale). Not found: any record of why `foundation_check.py` is 1003 lines here where the trial had 989; the cause is unclear and I did not trace it (the `git log` commits named above are candidates only).
- Searched the decision for whether a decorator counts toward a function's lines: not stated in WAY-385 or WAY-361; I followed the trial's `def`-line convention (choice 1).
