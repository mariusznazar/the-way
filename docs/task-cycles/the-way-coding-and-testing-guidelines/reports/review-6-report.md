PASS 0905337ae73e940c90384ca19b958ce633670655

# Review of slice 6 (range `c07e286..0905337`, one commit `0905337`)

Reviewed variant: a planned slice. `git rev-parse HEAD` in the worktree is `0905337ae73e940c90384ca19b958ce633670655`,
the head given. Changed: `task-cycle/test_gate_times.py` +99 -57; `task-cycle/gate_times.py` not changed
(`git diff c07e286 0905337 --stat` names the test file only).

## Findings

### Critical

none

### Important

none

### Minor

1. `task-cycle/test_gate_times.py:343` (the cited test) and `:366` (the uncited one) - the invariant
   `gate-times-refuses-impossible-entry` has two clauses: the script deletes the impossible entry, and "counts that
   entry as no other run". The cited test `test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing`
   proves the deletion (it fails with the deletion broken, shown below) but not the second clause: once the entries
   are deleted, the count `2` is the same whether or not `count_others` skips a malformed entry. I broke
   `if malformed(begin, finish, end):` in `count_others` to `if False:`; the cited test still passed and only
   `test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing` (line 366, which carries no
   `# invariant:` line) failed. Failure scenario: a later change drops the count guard; the one test the
   invariant cites stays green and only a test that no citation names catches it. Grade Minor because the plan,
   the task (answer 21 and row 30) and the slice name the one cited test, the clause is guarded by a test of the same
   class, and the citation check (`test-method-citation`) is satisfied. Fix if wanted: cite the invariant on
   line 366 as well (a second `# invariant:` line is allowed). Within the task.

### Out of scope

none

## Declined to judge

none

## Against the slice

- Goal, no real clock: the test's own `now_ms` and `import time` are gone; `NOW = 1_760_000_000_123` is a fixed
  value and `run_gate_at` calls `gate_times.main` in the test's own process with `gate_times.now_ms` replaced by
  `mock.patch.object(..., return_value=now)` - the one double (the clock). The three tests that built entries from the
  clock (`test_other_runs_counted_from_the_registry`, the cited test, `test_a_malformed_entry_that_cannot_be_deleted_...`)
  use `NOW`. No script changed. The `time.sleep(1)` test now waits for events (files), not for a pause.
- Does the test of the registry still fail when behaviour breaks (my own mutations, below): the start/end/reversed
  clauses of `malformed`, the stale deletion, the count guard, and a clock not replaced (the `Started` cell and the
  own entry name `<NOW>_<NOW>_...` are asserted) are each caught.
- The new entry `touching` (ended exactly at the run's start) pins `finish > start`; `inside` is created while the
  command runs, so a count taken before the command would miss it. Both are sound and sharper than the old test.
- The runner test (`test_directories_that_end_out_of_the_order_of_their_names_each_get_their_own_time`): the
  gate runs its directories at the same time by default (`gate/run_tests.py` docstring), so `b` waits at module level for
  the file `a` makes when its test starts, which puts `b`'s timer after `a`'s; `a` waits for the file the test
  makes when the line `== b` arrives, so `a` ends after `b`'s report. Hence `a`'s printed time exceeds `b`'s by the
  gap between those events (tens of milliseconds against three decimals), and the old `> 0.9` became
  `float(a) > float(b)`. I reasoned through the order of events and ran the class six times (and the whole file
  three times, and the directory through the runner once): all green. The margin is by reasoning, not guaranteed,
  as the executor said; I find it adequate. Both waits are bounded at two minutes, a failure not a hang.
- The grep line (`time.sleep(0.02)` at `:159`) is in the source text of the loop written into the two test files
  of the runner test; it polls for a file and no expectation depends on its length. `time_ns` and `time.time()`
  are gone from the file. Left on the real clock: every other test runs the script as a process for exit code or
  streams and checks the `Started` and total cells by form only (the plan's *Choices* row for this case); the
  report names them.
- Foundation: the invariant's wording (E31, `foundations/invariants.md:518`) agrees with the code of `malformed` and
  `prepare` (`task-cycle/gate_times.py:193-220`) and the cited test's malformed list covers each clause
  (end more than a minute ahead, start more than a minute ahead for an ended and a running entry, end before
  start). WAY-395 (time from outside, no fixed pause, one double) and WAY-243 (wait for the event) are kept.
  `script-language`, `script-imports` (standard library and `gate_times` of its own part), `script-subprocesses`
  (git and the interpreter only), `cross-part-imports` (own part) hold. `import gate_times` follows `sys.path.insert`
  as the neighbours in `task-cycle/` do; E402 is not among the selected rules.
- Trust boundary: the slice changes no line of `task-cycle/gate_times.py`; it adds the citation and keeps the
  crafted-entry tests. I checked that the cited test's entries are the crafted ones the invariant describes and that
  breaking the script's guards fails the tests (mutations below). The `mock.patch.dict(os.environ, ...)` restores
  the environment after each call; stdout/stderr redirects are context-managed.

## Checks I ran (command, exit code)

- `python -B task-cycle/test_gate_times.py` three times in a row: exit 0, 0, 0 (25 tests, 3.3 to 4.1 s).
- `python -B task-cycle/test_gate_times.py RunnerOutputTest` six times: `OK` each.
- `python -B gate/run_tests.py task-cycle` (the directory, focused): exit 0, 530 tests OK.
- `.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa task-cycle/test_gate_times.py`
  (ruff of the main checkout `<main checkout>`): exit 0, `All checks passed!`.
- `python -B elements/common/foundation_check.py --skip-test-citations`: exit 0, `0 errors`.
- `python -B elements/common/foundation_check.py` (full, extra): its output holds no line naming `gate-times`
  (the citation of the new invariant is read; other lines concern other slices' invariants).
- `grep -n "time.sleep\|time_ns\|time.time()" task-cycle/test_gate_times.py`: one hit, line 159, justified above.
- `git diff c07e286 0905337 --stat -- task-cycle/gate_times.py`: empty.
- Mutations in a worktree of `0905337` (`.runs/review-6/wt`), each run with
  `python -B task-cycle/test_gate_times.py RegistryTest`, each undone with `git checkout -- task-cycle/gate_times.py`:
  - base: OK (5 tests);
  - `if stale or malformed(start, end, now):` to `if stale:` in `prepare`: FAIL, the cited test fails (shown failing once);
  - `if malformed(begin, finish, end):` to `if False:` in `count_others`: FAIL, `..._still_counts_for_nothing` fails only, the cited test passes (Minor 1);
  - `end < start` clause removed from `malformed`: FAIL, the cited test fails;
  - `start > now + slack` clause disabled: FAIL, the cited test fails;
  - `end > now + slack` clause removed: FAIL, both the cited test and the undeletable-entry test fail;
  - `start = now_ms()` replaced by the real clock in `main`: FAIL, the cited test and `test_other_runs_counted_from_the_registry` fail.
  Each run ended with a clean `git status` in the working copy.
- Not run: the product's gate (`python -B gate/run_tests.py` with no directory), by the handoff.

## Reach beyond the dispatch

- `gate/run_tests.py:1-80`: read to know whether the runner runs directories at the same time and when it prints a
  report, which the runner test's timing argument rests on.
- `foundations/decisions.md` WAY-395 and WAY-243 passages (read whole) to judge the waits and the double; the
  other named entries were read from the handoff's quotations of them and the task passages (see below).

## Working copies

`.runs/review-6/wt` (a worktree of `0905337`): removed with `git worktree remove --force` and `git worktree prune`;
the directory `.runs/review-6/` is removed too. No remainder.

## Unread material

- `foundations/decisions.md` WAY-48, WAY-235 and WAY-08: not opened whole; I read the wording of the invariant they
  give rise to (`foundations/invariants.md:518`) and the task's answer 21 that quotes them. WAY-243 and WAY-395 read
  whole. WAY-394 (E11) read through the task's row 25 and the plan, not whole.
- `.runs/.../task.md`: read lines 25-45, 155-185, 248-262 and 538-546 (the passages the handoff names; line numbers
  differ from the file, found by content); the rest unread.
- `.runs/.../plan.md`: the *Choices* and the orchestrator's additions read; Slice 6 from the handoff; the rest unread.
- The invariants of the orchestrator's additions: `script-language`, `script-imports`, `script-subprocesses`,
  `cross-part-imports` read whole; `test-method-citation` read whole. `foundations/part_map.md` (task-cycle lines)
  not opened (no file added).

## Searches not found or unclear

none
