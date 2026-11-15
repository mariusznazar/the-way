# Executor report — slice 14: the test of the rule of a command runner

**Status:** done with concerns

**Concern in one line:** the real signal test is skipped on this platform (win32), so the POSIX
signal path is not run here; a mock-based test covers the script's mapping on every platform.

## Commits

- `878c88d` — Cite the command-runner invariant from the exit-code tests of gate_times.py and test a signal's exit code
  (base `d389ff5`, branch `task/the-way-coding-and-testing-guidelines`)

## Files changed

- `task-cycle/test_gate_times.py` — 31 lines added, 4 removed
- `task-cycle/gate_times.py` — no change (`git diff --exit-code -- task-cycle/gate_times.py` exit 0, after the two temporary breaks were undone)

## What the slice did

- Added `import signal` to the test file.
- `PassThroughTest.test_exit_code_of_the_command_is_passed_on` (existing, cited and extended): now
  cites `# invariant: command-runner-passes-exit-code` and checks codes 2, 3 and 255 in a loop of
  subtests (before it checked only 3). 2 is also the script's own error code, so the test shows the
  command's 2 is passed on as the command's.
- New `test_a_command_killed_by_a_signal_gives_128_plus_the_signal_number`, cited with the same
  invariant. It runs a real child that sends itself SIGTERM and expects 143 (128 + 15), and checks the
  count cell of the record. Decorated `@unittest.skipIf(os.name == "nt", ...)` because Windows gives a
  killed process no signal number.
- New `test_a_signal_number_of_the_child_gives_128_plus_it_on_any_platform`, cited with the same
  invariant. It patches `gate_times.subprocess.Popen` to return a mock child whose `wait()` returns
  `-SIGTERM` and whose stdout is an empty real pipe; `run_gate_at` runs `main` in-process and the test
  expects return code 143. It runs on every platform, including this one.
- The citation sits above the decorator for the skipped test.
- No test of `gate/run_tests.py` carries the invariant (it wraps no one command); confirmed by a
  repository-wide grep: the only citations of `command-runner-passes-exit-code` are the three lines in
  `task-cycle/test_gate_times.py` (272, 283, 291).

## Checks run (command and exit code)

1. Baseline before edits: `python -B task-cycle/test_gate_times.py` — exit 0 (Ran 25 tests, OK).
2. Baseline lint: `"<main checkout>/.runs/quality-venv/Scripts/ruff.exe" check --config ruff.toml --no-cache --ignore-noqa task-cycle/test_gate_times.py` — exit 0.
3. After the edit, the pass-through class: `python -B task-cycle/test_gate_times.py PassThroughTest -v` — exit 0 (Ran 5 tests, OK, skipped=1 — the real signal test).
4. After the edit, the whole file: `python -B task-cycle/test_gate_times.py` — exit 0 (Ran 27 tests, OK, skipped=1).
5. Mutant A (temporary, `task-cycle/gate_times.py` `exit_code`: negative codes mapped to `1` instead of `128 - code`): `python -B task-cycle/test_gate_times.py PassThroughTest.test_a_signal_number_of_the_child_gives_128_plus_it_on_any_platform` — exit 1, `AssertionError: 143 != 1`. Mapping restored right after.
6. Mutant B (temporary, `task-cycle/gate_times.py` `main` last line `return code` changed to `return min(code, 1)`): `python -B task-cycle/test_gate_times.py PassThroughTest.test_exit_code_of_the_command_is_passed_on` — exit 1, three failures: `2 != 1` (code=2), `3 != 1` (code=3), `255 != 1` (code=255). Restored right after.
7. After restoring both mutants: `git diff --exit-code -- task-cycle/gate_times.py` — exit 0.
8. Final whole-file run: `python -B task-cycle/test_gate_times.py` — exit 0 (Ran 27 tests, OK, skipped=1).
9. Final lint: ruff `check --config ruff.toml --no-cache --ignore-noqa task-cycle/test_gate_times.py` — exit 0 ("All checks passed!").
10. `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 (0 errors).
11. Not run: the product's gate (`python -B gate/run_tests.py` without a directory), per WAY-160.
12. Not run: the real signal test on POSIX — it is skipped on this win32 machine; no POSIX runtime was available. The check "cited test shown failing" holds for the mock-based signal test (mutant A) and the exit-code test (mutant B), but not for the real POSIX signal test.

Initial "test first" note: the behaviour already existed in `gate_times.py`, so the new tests were
run against the committed code (passing) and then the behaviour was broken for a moment, as the
invariant rule gives (WAY-08). The two mutants above are that check.

## Own-work check (section 3 of make-change)

- **Requirement most likely unmet:** the signal branch of the script is verified against a real
  process on the platform where the invariant's signal clause applies (POSIX), and the exit-code
  pass-through holds for codes that are neither 0 nor 1.
- **Check:** (a) the mock-based signal test fails when the mapping is broken (mutant A); (b) the
  exit-code test fails when the code is changed on the way out (mutant B); (c) the real POSIX test
  exists and is skipped only on `nt`.
- **Result:** (a) and (b) confirmed (checks 5 and 6). (c) confirmed by reading the test; not run on
  this machine. The unmet part is the real POSIX run, which stays open for a POSIX machine or CI.

## Choices made

- **Signal coverage on two levels.** A real process test (POSIX only) and a mock test (every
  platform). Way rejected: only the real process test — on this win32 worktree it would be skipped,
  so the mapping branch would never run here and the mutant check could not be shown. Way rejected:
  a direct unit test of `exit_code()` — it checks the helper, not what `main` returns to the caller,
  and the invariant speaks of the script. Cost if wrong: the mock replaces `subprocess.Popen` in the
  process running the test; if `main` later reads the child's output by another route (not by the
  file descriptor), the mock test breaks, which shows up as a failure, not as a silent pass.
- **Codes 2, 3 and 255 in the extended test.** Way rejected: keep only code 3, as before, or add a
  single signal-only case. Cost if wrong: none measured; the three codes are cheap subprocesses.
- **Signal test skip wording:** `skipIf(os.name == "nt", ...)`, not a platform-probe. Cost if wrong:
  on a POSIX system where `os.kill(os.getpid(), SIGTERM)` leaves the child alive, the test fails
  instead of passing — that would be a real finding, not a skip.

## Adaptations of the plan (section 4 of make-change)

None. The plan's *Read* line ranges for `decisions.md` (WAY-08 at 1746-1774 and WAY-198 at 8560-8590)
and `invariants.md:166-174` are stale; the handoff's ranges (1750-1779, 8517-8548, 166-175) matched
the worktree and were used.

## Reach beyond the handoff (what, where, why)

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` in the worktree — the method files the
  handoff names; read whole.
- `task-cycle/gate_times.py:161-175` (`relay`) and `:262-271` (`exit_code`) — read to see how the
  child's stdout is read (through a file descriptor), so the mock test's pipe is right.
- `foundations/invariants.md:1-` headings list and `:116-146`, `:348-356`, `:466-478` — the
  headings were searched to locate invariants; the whole of `script-language`, `script-imports`,
  `script-subprocesses`, `cross-part-imports` and `test-method-citation` was read as the handoff names.
- `foundations/decisions.md:10014-10034` (WAY-390), read in full as the E8 entry for the kind
  `command-runner`.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md:14-30` (preamble of the foundation
  entries), `:545-573` (slice 14) and `:1003-1041` (*Choices* and *Orchestrator's additions*) — the
  handoff binds the choices and additions; the preamble and slice were read to check the slice text
  against the handoff.
- `task-cycle/test_gate_times.py` (whole) — the file the slice changes.
- `ruff.toml` — not read; only the lint result (exit 0) is used.

## Unread material

- `foundations/decisions.md` WAY-386, WAY-387, WAY-388, WAY-389, WAY-391 — the handoff's E8 names the
  six exemplar decisions; only WAY-390 (the one of this kind) was read. The others are the exemplars
  of other kinds and bind no code of this slice.
- `foundations/decisions.md` WAY-379 (the template decision, named by WAY-390's *Relations*) — not
  read; not named by the handoff.
- `foundations/invariants.md:186` (`gate-exit-code`) — not read; not named by the handoff. It is an
  adjacent invariant about the gate's exit code and was not needed for the test.
- `ruff.toml` — read by lint result only, not whole.
- `task.md` lines 33-35, 136-147, 532 — read as named.

## Searches not found or unclear

- Stale line ranges in `plan.md` slice 14 *Read* (listed above). The handoff's ranges were used.
- Whether the foundation's test-method-citation check accepts more than one citation of one
  invariant in a file: not verified — the check was run with `--skip-test-citations`, as the handoff
  and slice name, so the citation rule itself was not run.
- Whether the POSIX signal test passes on a real POSIX machine: unknown; not run here.

## Working copies

None made. The `.runs/executor-14/` directory was not created; the two mutants were made in the
worktree file and undone, with no copy.

## Questions

None.
