# Executor report — slice 6: linter faults in nine test files

**Status:** done

**Commits:** `d6442f89d3cef97e5762cdbd635180bcc556b7e6` — "Fix the linter's blocking reports in nine test files" (on `task/code-order-formatter-linter-size`, base `8fecce81`).

**Files changed (9 files, +9 / −17):**

| File | Change |
|---|---|
| `installation/test_agent_types_installation.py` | `stdout=PIPE, stderr=PIPE` → `capture_output=True` (UP022) |
| `installation/test_coding_guidelines_installation.py` | same (UP022) |
| `installation/test_installed_guidance.py` | same (UP022) |
| `installation/test_lead_installation.py` | same (UP022) |
| `installation/test_styleguide_installation.py` | same (UP022) |
| `installation/test_testing_guidelines_installation.py` | same (UP022) |
| `agent-instructions/test_instruction_files.py` | `line[:-1] if line.endswith("\r") else line` → `line.removesuffix("\r")` (FURB188) |
| `gate/test_skills_reach_the_way_sessions.py` | `startswith(".claude/") or startswith(".agents/")` → `startswith((".claude/", ".agents/"))` (PIE810); `ruff format` joined the list comprehension onto one line |
| `product-guidelines/test_skill_references.py` | `startswith("../") or … startswith("/")` → `startswith(("../", "/"))` (PIE810) |

No test was added, removed, skipped or weakened. No rule was turned off, `ruff.toml` is unchanged, and no `noqa` or `fmt:` directive was added.

## Checks

Ruff is `the Ruff of the quality environment of the main checkout` (ruff 0.17.1).

| # | Command | Exit | Result |
|---|---|---|---|
| 1 | `ruff check --config ruff.toml --no-cache --ignore-noqa` on the nine files, before the change | 1 | 9 faults: UP022 ×6, FURB188 ×1, PIE810 ×2 |
| 2 | `ruff format --check --config ruff.toml --no-cache` on the nine files, before the change | 0 | 9 files already formatted |
| 3 | `ruff format --config ruff.toml --no-cache` on the nine files (Slice 3 layout) | 0 | 1 file reformatted (the gate file), 8 unchanged |
| 4 | `ruff check --config ruff.toml --no-cache --ignore-noqa` on the nine files, after the change | 0 | All checks passed |
| 5 | `ruff format --check --config ruff.toml --no-cache` on the nine files, after the change | 0 | 9 files already formatted |
| 6 | `python -B gate/run_tests.py installation` | 0 | Ran 73 tests, OK (467 s) |
| 7 | `python -B gate/run_tests.py agent-instructions` | 0 | Ran 52 tests, OK (expected failures=2) |
| 8 | `python -B gate/run_tests.py gate` | 0 | Ran 36 tests, OK |
| 9 | `python -B gate/run_tests.py product-guidelines` | 0 | Ran 14 tests, OK |

Not run: the full gate (no directory argument), as the handoff forbids (WAY-160). No walkthrough was run: the change alters no behaviour a user sees in the running product. Runs 6–9 were in the foreground, or one background run that I waited for; none was left running.

The two expected failures in check 7 are the linter and size invariant tests marked as expected failures. Slices 8 and 19 clear those marks; this slice does not touch them.

## Own-work check (WAY-164)

- **Requirement:** the nine files must be fixed in the files, with no rule turned off, no `noqa`, no weakened test, and the behaviour of each test unchanged.
- **Check:** `git diff` for added lines matching `noqa`, `ruff:` or `fmt:` (none); `git diff -- ruff.toml` (0 lines); the diff reviewed by eye, which touches only the flagged lines and no assertion; the focused gate runs above; ruff run with `--ignore-noqa`.
- **Showed:** no added directive, `ruff.toml` untouched, only the flagged lines changed, and all four gate directories pass. Check 1 failed and check 4 passed on the same files, so the fix is the cause.

## Choices

- **UP022 via `capture_output=True`.** This is the same as `stdout=PIPE, stderr=PIPE` in `subprocess.run`, so behaviour is identical. Rejected: keeping the two arguments with a `noqa` (forbidden by WAY-233 and the invariant).
- **FURB188 via `removesuffix("\r")`.** `line[:-1]` after `endswith("\r")` removes exactly that one character, so the two are equal for every input. Rejected: no alternative needed.
- **PIE810 via a tuple.** The boolean `or` operands have no side effects, so reordering the `path == ".."` test is equivalent. Cost if wrong: none found; the gate's two tests cover the path logic.
- **Formatter.** As Slice 3 gives, `ruff format` was run on the nine files after the edits. It changed only the one list comprehension in the gate file.

## Weakest point checked

The changes are mechanical, so the weakest point is an equivalence I did not test directly: the `startswith` tuple and the `removesuffix` change have no dedicated test of their own. The gate directories that exercise these paths (`gate`, `product-guidelines`, `agent-instructions`, `installation`) all pass.

## Unread material

- Read whole: `task-cycle/change/SKILL.md`, `task-cycle/change/slice.md`, `guidelines/testing.md`, `guidelines/coding.md`, the vault's `.ai/rules/git.md`; the nine target files, whole.
- Read in part: `.runs/task-cycles/code-order-formatter-linter-size/task.md:31` (only that line, as the slice's Read names it); `foundations/decisions.md:10614-10655` (WAY-380), `:9935-9978` (WAY-233), `foundations/invariants.md:438-447` (`ruff-blocking-rules`), each read by its current range.
- Not read: `.runs/task-cycles/code-order-formatter-linter-size/plan.md` slice 6 section was read through the handoff's copy only; the foundation entries F1–F9 were not read (not named in this slice's Read); `walkthrough.md` and `ui_check.md` not read (no user-visible behaviour, so neither applies).

## Searches not found or unclear

- none.

## Reaches beyond the handoff

- Read `plan.md` slices 1–3 (lines 34–142) to resolve the handoff's "formatted as Slice 3 gives" phrase, which the slice's Change refers to. Slice 3 states the layout rule: changed `.py` files are formatted with `ruff format --config ruff.toml` before commit.
- Read `.ai/rules/git.md` (vault) after the rules hook asked for it before the commit.

## Working copies

- None made. My test logs were written to `.runs/` and removed after their results were recorded above; no worktree or clone was created.
