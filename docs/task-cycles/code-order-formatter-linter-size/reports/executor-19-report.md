# Executor-19 report — slice 19: the size test turned strict and its mark cleared

**Status:** `done`

**Commit:** `d0a861d9` on `task/code-order-formatter-linter-size` (base `4e5f95fb`).
Commit message: "Set the size thresholds to 110 lines a function and 1200 a file and clear the expected failure of the size test".

**Files changed (by path, `git add` by name):**

| File | Added | Removed |
|---|---|---|
| `agent-instructions/test_size_invariant.py` | 4 | 8 |
| `foundations/invariants.md` | 1 | 1 |
| **Total** | **5** | **9** |

## What changed

1. `agent-instructions/test_size_invariant.py`:
   - `FUNCTION_LIMIT` 80 → 110, `FILE_LIMIT` 1000 → 1200 (F2, WAY-385).
   - Removed `@unittest.expectedFailure` from `Size.test_no_function_or_file_of_a_script_is_over_its_threshold`. The `# invariant: function-and-file-size` line stays.
   - Module description: the thresholds now read 110 and 1200. Removed the sentences about the invariant reading `Violated: yes`, the expected failure, and the unexpected success. Replaced them with one sentence: "The two tests stay apart so that the counting is checked on its own, whatever the invariant reports."
2. `foundations/invariants.md`, invariant `function-and-file-size`: `Violated: yes` → `Violated: no`.

## Checks (commands and exit codes)

Working copy: the worktree root `the worktree's root`. Ruff: `the Ruff of the quality environment of the main checkout` (ruff 0.17.1).

Test-first sequence (the invariant's test seen failing, then passing):

1. Mark removed, old thresholds (80/1000), then `python -B agent-instructions/test_size_invariant.py` → **exit 1**. The test fails on its assertion: "10 functions over 80 lines and 4 files over 1000 lines", listed in full in `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-19-run1.txt`. (Failed run, as the method asks.)
2. Thresholds changed to 110/1200, mark stays removed: `python -B agent-instructions/test_size_invariant.py` → **exit 0**, "Ran 4 tests … OK" (`executor-19-run2.txt`).

Focused checks named in the slice:

| Command | Exit | Result |
|---|---|---|
| `ruff format --config ruff.toml agent-instructions/test_size_invariant.py` | 0 | file left unchanged |
| `ruff format --check --config ruff.toml agent-instructions/test_size_invariant.py` | 0 | already formatted |
| `ruff check --config ruff.toml --ignore-noqa agent-instructions/test_size_invariant.py` | 0 | all checks passed |
| `python -B gate/run_tests.py agent-instructions` | 0 | 52 tests, OK; log `executor-19-gate-ai.txt` |
| `python -B elements/common/foundation_check.py` | 0 | "0 errors" |
| `grep` for `expectedFailure` / `expected failure` in `test_size_invariant.py` and `test_linter_invariant.py` | 1 (no match) | no expected failure left in either file |

The full gate (`python -B gate/run_tests.py` without a directory) was not run, per the handoff.

## Own-work check (WAY-164)

- **Requirement:** the size test runs strict, without the mark, at 110 lines for a function and 1200 for a file; the invariant reads `Violated: no`; the module description loses the violation sentences.
- **Check:** grep both test files for `expectedFailure`, `expected failure`, `Violated`, `violated`, `80`, `1000`. Nothing matched in the test files. The invariant line reads `Violated: no`. The gate and the file run pass.
- **Result:** met.
- **Weakest point:** the code has almost no room under the new limit. In the run at the old thresholds, the largest function was `installation/install.py:448 plan` at 109 lines, one below 110. `task-cycle/cycle_stages.py:416 report` is at 108. The largest file was `elements/common/migrate_foundation.py` at 1162 lines, 38 below 1200. The limit check uses `>`, so a function of exactly 110 lines still passes, as WAY-385 "at most 110" says. Any growth of `plan` by two lines fails the invariant.

## Choices made

- **Order of edits.** I removed the mark first and ran the test on the old thresholds, to see the test fail on the real code before changing the thresholds. This is the one failing run the method asks for.
- **Wording of the module description.** The sentence about why the two tests stay apart now gives a reason that does not mention the mark. I did not keep the old sentence with the mark removed, since it would describe a state that no longer holds. Rejected: a one-line description with no reason. Cost: none for the test's behaviour.
- **Commit message.** It names the changed invariant test (WAY-03) and the cleared mark (WAY-51), as both decisions ask.

## Reach beyond the handoff

- `.ai/rules/git.md` in the user's private instructions. A hook blocked the commit until I read it; I did, then committed. The commit is English, the add is by path, and the author address is the one git already had (`the author's private address`). The hook note is not a cycle matter.

## Concern for the orchestrator

WAY-51 says an invariant is marked violated only by a change that a human accepts, and that the request must name the change that sets or clears the mark. The handoff and the slice say the cycle's request names the cleared mark, and the commit message names it. Whether the human accepted this clearing is the orchestrator's to confirm; I did not treat the handoff as that approval.

## Unread material

- `.runs/task-cycles/code-order-formatter-linter-size/plan.md`: not opened. The slice text is taken from the handoff, which copies it word for word.
- `foundations/decisions.md` WAY-385 (line 10784): read to line ~10823 only. The "Rejected" sentence continues past that point, and the rest of the entry is unread.
- `task.md`: read at lines 28–44, which cover items 1–8 and the acceptance criteria. The handoff's *To do* and *Acceptance* ranges are inside that block.
- `task-cycle/change/ui_check.md` and `walkthrough.md`: not read. No user-visible behaviour changes, so section 3 does not call for them.
- `project-level/technology/reserved_choices.md`: not read. The work needs no language, framework or service choice.
- `F2`, `F4`–`F9` and the other foundation entries not named by this slice: not read.

## Searches not found or unclear

- `function-and-file-size` in `foundations/` gave 2 hits (`decisions.md:10797`, `invariants.md:458`). The decision's Verification line in WAY-385 names the invariant. Nothing else needed changing for this slice.
- None of the other searches came up empty.

## Working copies

No worktree, clone or scratch tree was made. The only files made are four text logs, kept in `.runs/executor-19/` under the worktree's ignored `.runs/`:
- `executor-19-run1.txt` (failing run, exit 1)
- `executor-19-run2.txt` (passing run, exit 0)
- `executor-19-gate-ai.txt` (gate, exit 0)
- `executor-19-foundation.txt` (foundation check, exit 0)

The same four logs are copied into `.runs/task-cycles/code-order-formatter-linter-size/reports/`. Nothing needs removal.

## Full gate

Not run, per the handoff. The orchestrator's or CI's full gate run is still needed.
