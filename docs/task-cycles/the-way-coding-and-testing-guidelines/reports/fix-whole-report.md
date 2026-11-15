# Report — the fix of the findings of the review of the whole change

**Status:** done with concerns (one flaky test outside the findings, below; two points of the findings contested in part).

Range of the fix: `be9b44d..f0482d0`, seven commits, 19 files, 194 insertions and 107 deletions.

## Commits

| Commit | Findings |
|---|---|
| `08b097c` | I-1 |
| `0d3c944` | I-2 |
| `06c15a0` | I-3, I-4, M-4 |
| `97c0d8c` | M-5, M-11, M-12 |
| `7d6ac17` | M-1 |
| `b7733e6` | M-2, M-3 |
| `f0482d0` | M-6, M-7, M-8, M-9, M-10 |

## Findings, how fixed, and the check

**I-1** (`08b097c`). Before: `python -B gate/run_tests.py elements/part-map` in a worktree of `be9b44d`: exit 1, `FAILED (failures=1)`, the three messages of the review. Fix: `process-audit/test_audit_count.py` — `run_count` no longer takes `script`; it starts the literal `SCRIPT`, and a second method `run_count_of_the_copy` starts the copy built in `self.home / "repos" / "checkout"` (a path in the temporary directory, which the check knows); the shared tail is `run_command`. `relation-model/test_fingerprint.py` — the code given to `-c` first assigns `here = sys.argv[1]`, the form the check reads (it follows names assigned from `sys.argv[i]`, not the use inside a call). The meaning of both tests is unchanged. After, each run on its own directory: `elements/part-map` exit 0 (40 tests), `process-audit` exit 0 (234), `relation-model` exit 0 (13); the final run of all eight affected directories is below.

**I-2** (`0d3c944`). Before: the test run alone 80 times in a row, `python -B .runs/fix-whole/loop.py <test> 80`: 2 failures in 80. Fix: `a` waits for the line `released` of the log, which the test itself appends when the runner it started has printed the line `== b` (new helper `runner_noting`, which reads the runner's output as it comes); `b` ends before the runner prints its report, so `b` is always first, whatever the load. After: 40 runs alone, 0 failures; and 45 runs with three such loops and a loop of the old code running at once, 0 failures (`loop2.py <test> 15` ×3 at the head). The test keeps its asserts on order, whole reports and the last line.

**I-3** (`06c15a0`). Both sentences now say "with its input open and empty": `foundations/invariants.md` (`shared-module-import-runs-nothing`) and `guidelines/coding-shared-module.md`. The test is unchanged.

**I-4** (`06c15a0`; the orchestrator's choice Q12, which the human accepts at the request). The sentence of `repository-changer-acts-only-when-told` now reads "…change no file that the repository tracks, other than a report that the human names with `--report`, and no working directory." `guidelines/coding-repository-changer.md`: the Good and Bad lines and the rule's paragraph follow the narrowed sentence; the paragraph about the status of `migrate_foundation.py` is deleted; the status is `copy`. One addition beyond the sentence: the decision WAY-389 (the cycle's own, written by the foundation step) restates the same sentence ("changes neither a file that the repository tracks nor a working directory…") and would otherwise disagree with the invariant, so I narrowed it with the same words. Way rejected: leave WAY-389 as written — it would say what the code does not do for `migrate_foundation.py`, the very fault of the finding. Cost if wrong: one decision text to restore. Check: `python -B elements/common/foundation_check.py` exit 0 (`0 errors`), citations included, at the end of the work. The cited test is unchanged.

**M-1** (`7d6ac17`). `# invariant: gate-times-refuses-impossible-entry` added above `test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing`. `python -B task-cycle/test_gate_times.py`: exit 0, 27 tests; `task-cycle` directory exit 0.

**M-2** (`b7733e6`). The docstring of `MissingFieldError` no longer says "Claude Code transcript". `required`, `TOKEN_DIGITS` with its comment, `required_count`, `required_text` and also `required_time` (the Codex reading calls it as well, so it had the same wrong place) moved under a new heading `# Fields a reading needs`, above `# Codex`. No change of code.

**M-3** (`b7733e6`). Test first: `CodexFieldsTest.test_a_line_that_is_json_but_no_object_ends_with_exit_code_2_naming_the_line` — before the fix `python -B -m unittest test_cycle_stages.CodexFieldsTest` (in `task-cycle/`) exit 1, `AttributeError: 'list' object has no attribute 'get'` at `read_codex_agent`; after: exit 0, 18 tests. Fix: `read_codex_agent` raises `MissingFieldError(f"{path}:{number}: the line is not a JSON object")` for such a line; `main` gives exit 2. New test `test_the_largest_count_of_fifteen_digits_is_read` (`10**15-1`, exit 0, report written; passes at once, since the code already accepts it). Contested in the wording of the direction: it says "as the Claude Code half does", but the Claude Code half skips a line that is no object (`cycle_stages.py`, `read_claude_agent`: `if not isinstance(entry, dict) ...: continue`) and does not end with exit 2. I followed the explicit demand (exit 2 and the message naming the rollout and the line) for the Codex half only and did not change the Claude Code half.

**M-4** goes with I-4: the paragraph is deleted.

**M-5** (`97c0d8c`; Q13). `guidelines/coding.md`, rule "How a script starts and ends": the sentence reads "A module that other scripts import and that has no more for the command line than a fixed `if __name__ == "__main__":` block, as a file of the kind `shared-module` has, is no such script, and this rule does not reach it." True of `relation-model/fingerprint.py`.

**M-6** (`f0482d0`). The comments of `NAMES`, `BLOCK`, `SIBLINGS` and `ENTRY_POINT` in `installation/test_install.py` name the README of the installation (its section "Files in the product" and the row it describes), without a line number of any code. The head of `install.py` holds one line only, so the README section is the document there is. `python -B gate/run_tests.py installation` exit 0.

**M-7** (`f0482d0`; Q14). `test_the_way_foundation_passes` now also keeps the message "`<name>` is withdrawn; name its successor" for each name in the rows of the part map's *Withdrawn identifiers* (read by the test from `foundations/part_map.md`, the message written out in the test; `foundation_check.py` unchanged). The check gives the same message for a withdrawn decision number, invariant or fact, so the filter is by the name, not the message alone; the comment of the test says so. Mutation shown: with `entry-format` (a withdrawn part) added to a `Part` field the test fails naming `foundations/invariants.md:455: `entry-format` is withdrawn; name its successor`; restored, it passes. `elements/common` exit 0 (190 tests).

**M-8** (`f0482d0`). README: "Two invariants of the foundation of the-way, `map-reference-target` and `test-method-citation`, are checked by one of these tests; the whole check of the foundation runs on its own by:". For the request: this follows from the choice of cause 23 of the task, not from a slip — the other findings of `foundation_check.py` on the-way's own foundation no longer fail the gate.

**M-9** (`f0482d0`). README, "What else is here": a line for `guidelines/` and one for `ruff.toml` with the two requirement files. `foundations/part_map.md`, sentence of `agent-instructions`: "…and for the guidelines of the-way's own code that those instructions point to." `check_instructions.py . --file README.md`: 0 errors, 1 warn (`.runs/quality-venv` dead path, present at the base too).

**M-10** (`f0482d0`). Each of `agent-instructions/test_linter_invariant.py` and `test_size_invariant.py` has a test that every file `git ls-files` lists with the suffix `.py` has its first directory in `PARTS`, naming the files otherwise. Failing run: with `relation-model` taken out of `PARTS` in both files, both tests fail naming `relation-model/fingerprint.py` and `relation-model/test_fingerprint.py` (exit 1); restored, `python -B -m unittest test_linter_invariant test_size_invariant` in `agent-instructions/`: OK, 7 tests, 2 expected failures. I did not add a shared helper: the two tests already repeat the tuple, and a third file would be a new part-map claim; the cost is the same ten lines twice.

**M-11** (`97c0d8c`; Q15). The head of `agent-instructions/skill_entry_points.py` says a `name:` or `description:` with no value ends with exit 1 and a missing line with exit 2; `guidelines/coding-generator.md` says the same of the exemplar. No code changed.

**M-12** (`97c0d8c`). The two sentences "While the entry … reads `Violated: yes`…" are replaced by "The review of each change compares the changed files with this rule." and "…with the thresholds.". They tell what the author is to do, no state.

## Checks (command, exit code)

At `f0482d0`, each in the worktree root, started in parallel:

| Command | Exit |
|---|---|
| `python -B gate/run_tests.py agent-instructions` | 0 |
| `python -B gate/run_tests.py gate` | 0 |
| `python -B gate/run_tests.py installation` | 0 |
| `python -B gate/run_tests.py elements/common` | 0 |
| `python -B gate/run_tests.py elements/part-map` | 0 |
| `python -B gate/run_tests.py process-audit` | 0 |
| `python -B gate/run_tests.py relation-model` | 0 |
| `python -B gate/run_tests.py task-cycle` | 0 |
| `python -B gate/run_tests.py instruction-files` | 0 |
| `python -B gate/run_tests.py product-guidelines` | 0 |
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `check_instructions.py . --file` on `README.md`, `guidelines/coding.md`, `coding-generator.md`, `coding-repository-changer.md`, `coding-shared-module.md`, `foundations/part_map.md` | 0 errors (README: the one warn above) |

The full gate (`python -B gate/run_tests.py`) was not run, as the handoff says.

Ruff on the changed `.py` files (`--ignore-noqa`): 2 reports, both on code I did not write: `task-cycle/cycle_stages.py` TRY004 at the `raise ValueError` of `required_time` (moved, not changed) and an F541 in an unchanged part of `task-cycle/test_cycle_stages.py`. The invariant `ruff-blocking-rules` reads `Violated: yes`.

## Own-work check (section 3)

The requirement most likely not met: I-2 — a test that is stable on a loaded machine. Check: 40 runs alone and 45 runs under the load of three parallel loops and a fourth loop of the same test on the old code; 0 failures out of 85 at the head, where the old code failed 2 of 80 alone.

## Concerns outside the findings

A test not in the findings is flaky, at the base as at the head: `gate/test_run_tests.py::DirectoriesAtOnce::test_a_number_of_jobs_limits_the_directories_that_run_at_once`. Run 40 times at `2d59321` and 40 times at the head at the same time: 5 failures each (`fix-whole-jobs-flake-base-runs.txt`, `fix-whole-jobs-flake-head-runs.txt`; a failing run, `fix-whole-jobs-flake-failing-run.log`, shows directory `b` waiting 120 s for `start a` and failing "did not meet the others" while `a` and `c` passed). I did not touch it; cause not found. It can turn the one run of the gate red.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-389 (read whole, one entry): to keep the decision consistent with the narrowed invariant (I-4).
- `elements/part-map/test_cross_part_imports.py` lines 170–650 (the checker's resolver) read, to find what it can work out for I-1.
- `README.md`, `installation/README.md`, `gate/run_tests.py` (the print of the reports), `elements/common/foundation_check.py` (messages, `table`): read in part for M-6, M-7, M-8, M-9 and I-2.

## Working copies

Stood and removed: `.runs/fix-whole/` (loop scripts, backups of two files, logs) and the two worktrees `.runs/fix-whole/base` (`2d59321`) and `.runs/fix-whole/before` (`be9b44d`) — removed with `git worktree remove --force` and `git worktree prune`; `git worktree list` shows neither. Kept in `reports/`: the three `fix-whole-jobs-flake-*` files. No remainder.

## Unread material

- The full report `reports/review-whole-report.md`, the plan `plan.md`, the task `task.md` and the reports of the executors: not read; the findings file and the handoff were enough.
- `task-cycle/change/slice.md`: not read (a fix does not read it).
- `guidelines/coding.md` read whole earlier only in the passages I changed (lines 20–50 and 80–125); the other guideline files I changed, whole.

## Searches not found or unclear

- The direction of M-3 says the Claude Code half ends with exit 2 and a message for a line that is no object; it does not (it skips such a line). Not found as described; see M-3.
- WAY-344 was not read: whether an empty value is a missing field there I did not look up; I followed the direction of Q15.

## Questions

None.
