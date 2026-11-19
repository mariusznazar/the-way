# Report — executor-5, slice 5 (linter faults at four trust boundaries)

**Status:** done

## Commits and files

- `8fecce81` — Fix the linter's reports in four trust-boundary files, keeping the exit code and message of a timestamp that is no text. Base `2620dcc39afe19eacd781e1322718ad30762dcc8`.
- `installation/install.py` +2 -3, `instruction-files/check_instructions.py` +1 -2, `process-audit/audit_count.py` +3 -3, `task-cycle/cycle_stages.py` +2 -2 (8 added, 10 removed in all).

## What each fix is

- `installation/install.py`, UP022: `stdout=subprocess.PIPE, stderr=subprocess.PIPE` became `capture_output=True` in `git()`; the same two pipes, `check=False` stays.
- `installation/install.py`, PERF102: `for path, expected in files.items():` became `for path in files:` (`expected` was unused). Ruff's suggested `.keys()` would trigger SIM118, which the configuration has on.
- `instruction-files/check_instructions.py`, FURB188: the `if data.startswith(BOM): data = data[len(BOM):]` became `data = data.removeprefix(codecs.BOM_UTF8)` (`data` is bytes; same result).
- `process-audit/audit_count.py`, UP037 (three): quotes removed from `list["Read"]` (twice) and `list["Version"]`; the file has `from __future__ import annotations` (line 338), so the names are not evaluated at definition.
- `task-cycle/cycle_stages.py`, TRY004: in `required_time` the type check now stands before the `try` and raises `MissingFieldError(f"{where}: field timestamp is not a time")` itself; the `try` holds only `parse_time` and the conversion and still turns `ValueError`/`OverflowError` into the same `MissingFieldError`. No `TypeError` is raised, the rule stays on, no `noqa`. The one change in what the code does: a non-text timestamp's error no longer carries a chained `ValueError` as `__cause__`; the run's message and exit code do not show it, and `main` prints the message only.

## Checks

| Check | Command | Exit |
|---|---|---|
| Linter on the four files | `the Ruff of the quality environment of the main checkout check --config ruff.toml --no-cache --ignore-noqa installation/install.py instruction-files/check_instructions.py process-audit/audit_count.py task-cycle/cycle_stages.py` | before: 1 (7 reports: UP022, PERF102, FURB188, UP037 x3, TRY004); after: 0 |
| Formatter on the four files | `<ruff> format --check --config ruff.toml <the four files>` | before and after: 0 (`ruff format` run after the edit: "4 files left unchanged") |
| Installation tests | `python -B gate/run_tests.py installation` | 0 (73 tests, 438 s) |
| Instruction-files tests | `python -B gate/run_tests.py instruction-files` | 0 (105 tests, 5 skipped on Windows, 5 s) |
| Process-audit tests | `python -B gate/run_tests.py process-audit` | 0 (276 tests, 364 s) |
| Task-cycle tests | `python -B gate/run_tests.py task-cycle` | 0 (534 tests, 2 skipped on Windows, 93 s) |
| `cycle_stages.py` before and after on crafted input | `python -B task-cycle/cycle_stages.py <transcript> --output <path>` | exit 2 before and after, for each of four inputs, same message (see below) |

The full gate was not run (WAY-160).

## Own-work check (WAY-164)

Requirement most likely not met: for TRY004, `required_time` keeps what it does — a timestamp that is no text ends the run with exit code 2 and the message that the field timestamp is not a time, never a `TypeError` that escapes (WAY-344, task *To do* 3 and *Context*).

Check: four prepared transcripts, run with the script before the fix (at base) and after it, each compared. Their text and both outputs are in `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-5-evidence.txt`.

1. Claude Code transcript, line 1 `"timestamp": 12345` (the slice's case): before and after, exit 2, `Error: <path>:1: field timestamp is not a time`.
2. Codex rollout, `session_meta` then a line with `"timestamp": 12345` (the other caller of `required_time`): before and after, exit 2, `…:2: field timestamp is not a time`.
3. Claude Code transcript with `"timestamp": true`: same exit 2, same message.
4. Claude Code transcript with `"timestamp": "not a time"` (the `try` path still catching `ValueError`): same exit 2, same message.

The outputs are identical before and after for all four (compared with `diff`). The existing test `test_a_timestamp_that_is_no_time_ends_with_exit_code_2_naming_it` in `task-cycle/test_cycle_stages.py:2061` already holds 5, True, a list and bad strings, and passes. The other three trust-boundary files (`install.py`, `check_instructions.py`, `audit_count.py`) changed in ways that cannot give another verdict for any input (same pipes, an unused loop variable, same slice-or-not of a BOM prefix, annotations not evaluated); I made no crafted-input comparison for them beyond their focused tests passing.

## Weakest point checked

That removing the quotes of the three annotations in `audit_count.py` cannot fail at import, as `Read` (line 815) and `Version` (line 2568) are defined after the lines that name them: it holds only because of `from __future__ import annotations` at line 338, which I saw in the file and which the `process-audit` tests' import of the module confirms (276 tests pass). A dataclass field annotation is not evaluated either, since the module's dataclass decorators do not read it under the future import.

## Choices

- `for path in files:` over Ruff's `.keys()`: `.keys()` triggers SIM118 (on in `ruff.toml`). Cost if wrong: none; the behaviour is the same.
- TRY004: type check outside the `try`, raising `MissingFieldError`, over raising `TypeError` and catching it in the `except`: that would have kept a `TypeError` in the `try` for a rule's sake and the check outside is simpler. Rejected too: leaving `ValueError` with a `noqa`, which WAY-380 forbids.
- No test added: the slice's *Change* lists the four files only, and the behaviour of TRY004 is covered by the test cited above, which I did not break to see fail (it passes before and after, as the behaviour is kept).

## Reaches beyond the handoff

- Grep of `task-cycle/` for `is not a time` and a read of `task-cycle/test_cycle_stages.py:2055-2090`, to know whether the existing tests cover a non-text timestamp. Not named by the handoff; no gap in its selection, only my own check.

## Unread material

- The four changed files were not read whole (`audit_count.py` is over 2700 lines): I read the functions and lines the reports named and their surroundings, plus `cycle_stages.py` lines 1-60 and the two callers of `required_time`.
- `foundations/part_map.md:102-136` and `183-203`, the decisions and invariants, the task passages and the four guideline files: read whole as given. The guideline files carry no rule that touches these changes.

## Searches not found or unclear

none

## Working copies

`.runs/executor-5/` of the worktree held four prepared transcripts, the before/after outputs and the four test logs. I kept the transcripts and outputs in `reports/executor-5-evidence.txt` and removed the directory after the report was written. The test runs were finished before I returned; no background run is left.
