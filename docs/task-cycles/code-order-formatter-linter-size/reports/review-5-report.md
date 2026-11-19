PASS 8fecce8112318e179b5c0256d8fd2ca445a2904d

# Review of slice 5 (linter faults at four trust boundaries), range 2620dcc3..8fecce81

`git rev-parse HEAD` of the worktree is `8fecce8112318e179b5c0256d8fd2ca445a2904d`, the head given. One commit in the range; 4 files changed, 8 insertions, 10 deletions (the diff touches no other file: no test, no foundation entry, no `ruff.toml`).

## Findings

**Blocking: none. Minor: none. Out of scope: none.**

### What I verified, claim by claim

- `installation/install.py`, UP022: `stdout=subprocess.PIPE, stderr=subprocess.PIPE` became `capture_output=True`, which sets exactly those two pipes; `input=stdin`, `text`, `encoding`, `check=False` unchanged; the callers read `.stdout`/`.stderr` as text as before. No behaviour change.
- `installation/install.py`, PERF102: `for path, expected in files.items()` became `for path in files`. `files` is a `dict[Path, str]` (line 454); `expected` was not used in the loop body (lines 528-535 read), so the iteration is the same keys in the same order. Ruff's `.keys()` suggestion would hit SIM118, so the bare iteration is the right form; no rule is turned off.
- `instruction-files/check_instructions.py`, FURB188: `data` is bytes; `data.removeprefix(codecs.BOM_UTF8)` equals "slice off the BOM if present, else unchanged". The `cut` and the `UnicodeDecodeError` branch below it read `data` after the removal exactly as before.
- `process-audit/audit_count.py`, UP037 (three): the quotes of `list["Read"]` (twice) and `list["Version"]` are gone. The file has `from __future__ import annotations` at line 338, so annotations are not evaluated; `Read` and `Version` are defined later in the file, which is fine under it. No `get_type_hints`, `__annotations__`, `inspect.signature` or `eval(` in the file that would evaluate them. The 276 tests import and run the module.
- `task-cycle/cycle_stages.py`, TRY004: `required_time` now refuses a non-text value before the `try` with `raise MissingFieldError(f"{where}: field timestamp is not a time")`; the `try` holds only `parse_time` and the conversion and still turns `ValueError`/`OverflowError` into the same `MissingFieldError`. The message and the exception class are those of before; `main` catches `MissingFieldError`, prints `Error: <message>` and returns 2. No `TypeError` can escape, no `noqa`, the rule stays on (WAY-380), and WAY-344's exit code 2 with a message naming the file, line and field is kept. The one difference, the lost `__cause__` of a chained `ValueError` for a non-text value, is not shown by `main` and no test reads it (the task-cycle tests pass).
- No `noqa` and no `fmt:` comment in the diff.
- The existing test `task-cycle/test_cycle_stages.py:2061` (`test_a_timestamp_that_is_no_time_ends_with_exit_code_2_naming_it`) gives 5, None, a list, True and bad strings in the timestamp of a line and asserts the exit code and the message (or `no field timestamp` for None). It fails if the refusal of a non-text were lost or became a `TypeError`, so the WAY-344 test the decision requires for this reading stands. The slice adds no test; none was asked for in its *Change*, and the behaviour is kept.

### Contradiction marks

No blocking finding, so none to mark.

## Declined to judge

- The 17 reports that `ruff check --ignore-noqa` still gives on the rest of the repository (other slices of the plan fix them) and the `Violated: yes` of `ruff-blocking-rules` in `foundations/invariants.md`: outside this slice, which fixes four files only. The four files give none.

## Checks run

All from the worktree root `the worktree's root` (my own worktrees of the head and of the base, in `.runs/review-5/`, so the reviewed worktree was not run in).

| Check | Command | Exit |
|---|---|---|
| Linter on the four files | `the Ruff of the quality environment of the main checkout check --config ruff.toml --no-cache --ignore-noqa installation/install.py instruction-files/check_instructions.py process-audit/audit_count.py task-cycle/cycle_stages.py` | 0 ("All checks passed!") |
| Formatter on the four files | `<ruff> format --check --config ruff.toml <the four files>` | 0 ("4 files already formatted") |
| Linter over the repository, to see what is left | `<ruff> check --config ruff.toml --no-cache --ignore-noqa .` | 1 (17 reports in other files, none in the four) |
| Instruction-files tests (worktree of head) | `python -B gate/run_tests.py instruction-files` | 0 (105 tests, 5 skipped) |
| Task-cycle tests | `python -B gate/run_tests.py task-cycle` | 0 (534 tests, 2 skipped) |
| Installation tests | `python -B gate/run_tests.py installation` | 0 (73 tests) |
| Process-audit tests | `python -B gate/run_tests.py process-audit` | 0 (276 tests) |
| Crafted input at `cycle_stages.py`, base against head | `python -B <worktree>/task-cycle/cycle_stages.py <file> --output <path>` on 13 prepared transcripts (timestamp: number, float, null, list, object, true, "not a time", empty, missing, valid, naive, `9999-12-31T23:59:59-23:59` which overflows, and a Codex rollout whose second line has a list timestamp) | exit and message identical at base and head for all 13 (`diff` printed no difference); non-text, bad text, empty and overflowing values: exit 2, `field timestamp is not a time`; null: exit 2, `no field timestamp`; valid, naive and missing: exit 0 as before. Outputs kept in `reports/review-5-cycle-stages-before.txt` and `reports/review-5-cycle-stages-after.txt` |
| Crafted input at `check_instructions.py`, base against head | `python -B <worktree>/instruction-files/check_instructions.py <repo> --file <y.md>` on a repo holding a file with a BOM and text, a BOM-only file, a file with a doubled BOM, and a UTF-16 file | output and exit code identical at base and head (exit 0) |

Not run, and why: `install.py` and `audit_count.py` were not given crafted input of their own at base and head. Their changes (same two pipes; an unused loop variable; annotations not evaluated) cannot change a verdict for any input, and their focused suites pass. The full gate was not run, as the handoff forbids.

## Reaches beyond the handoff

- `guidelines/coding.md`, the three kind files and the part map were read as named. Beyond them: `task-cycle/test_cycle_stages.py:2050-2080`, to judge whether the test of the non-text timestamp would catch the requirement unmet; `task-cycle/cycle_stages.py` lines 1-60, 480-500 and 1225-1275, and `installation/install.py` lines 450-560 and the grep of `files`, for the callers and for `main`'s handling of `MissingFieldError`. No foundation entry outside the handoff.

## Working copies

All stood under `.runs/review-5/` of the task's worktree: worktrees `wt` and `wt2` of the head `8fecce81`, `base` of `2620dcc3`, prepared transcripts, a repository for the BOM check, and the test logs. I removed the three worktrees with `git worktree remove --force` and then `git worktree prune`, and deleted the directory `.runs/review-5/`. I kept only the two files of outputs named above in `reports/`. No remainder.

## Unread material

none. Read whole: the review skill, the handoff, the executor's report, the task lines 31 and 98, WAY-380, WAY-344 and WAY-48, the five invariants and `ruff-blocking-rules`, the part-map ranges, and the four guideline files. The four changed files were read at the diff and its surroundings, not whole (`audit_count.py` is over 2700 lines), which the review of a diff of this size does not need.

## Searches not found or unclear

none
