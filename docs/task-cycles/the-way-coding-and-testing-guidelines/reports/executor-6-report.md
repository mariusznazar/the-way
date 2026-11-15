# Report of executor 6 — slice 6

**Status:** done

**Commits:** `0905337` Give the tests of the gate times script a fixed clock and an event in place of a pause, and cite the refusal invariant of its registry (base `c07e286`).

**Files changed:** `task-cycle/test_gate_times.py` +99 −57. `task-cycle/gate_times.py` not changed
(`git diff -- task-cycle/gate_times.py` empty after each break).

## What was done

- The test's own `now_ms` (real clock) and `import time` are gone. A constant `NOW = 1_760_000_000_123`
  (2025-10-09 08:53:20.123 UTC, checked with `datetime.fromtimestamp`) and a helper
  `GateTimesTest.run_gate_at(now, command)`: it calls `gate_times.main` in the test's own process with
  `gate_times.now_ms` replaced by `mock.patch.object(..., return_value=now)` (the one double: the clock),
  the output and error output captured, `HOME`/`USERPROFILE` the test's own; it returns a
  `CompletedProcess` like `run_gate`. The module is imported with `sys.path.insert(0, str(HERE))`, as the
  neighbours in `task-cycle/` do.
- The three tests that built registry entries from the clock use `run_gate_at(NOW, ...)` and entries
  written from `NOW`:
  `test_other_runs_counted_from_the_registry` (the command no longer sleeps or reads the clock: the entry
  `inside` is named in the test from `NOW` and made by the command while it runs; added the entry
  `touching`, ended exactly at the run's start and not counted; asserts the Started cell equals
  `2025-10-09 08:53:20.123` and the own entry is named `<NOW>_<NOW>_<token>.run`, which shows the clock was
  replaced),
  `test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing` (cited
  `# invariant: gate-times-refuses-impossible-entry`),
  `test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing`.
- `test_directories_that_end_out_of_the_order_of_their_names_each_get_their_own_time` (the `time.sleep(1)`):
  no pause now. This test needs no time of the run; it needs `a` to end after `b`. `a` writes a file when
  it starts and waits for a second file; the test process runs the script with `Popen`, reads its output as
  it comes (the script relays it as it comes, the runner flushes each report whole when its directory
  ends) and makes the second file when the line `== b` arrives, so `a` ends after `b`'s report is out.
  `b` waits for `a`'s start file at module level, before its own timer starts, so `b`'s printed time lies
  inside `a`'s; the old `assertGreater(a, 0.9)` became `assertGreater(float(a), float(b))`. Both waits are
  loops over a file with a bound of two minutes (an event wait, not a pause the expectation depends on).

## Checks (command and exit code)

| Check | Result |
|---|---|
| `python -B task-cycle/test_gate_times.py` run 1 / 2 / 3 | exit 0, exit 0, exit 0 (25 tests, about 3.2 s each) |
| `python -B task-cycle/test_gate_times.py RunnerOutputTest` ten times in a row | ten `OK` |
| the cited test with `if stale or malformed(start, end, now):` in `prepare` changed to `if stale:` (`python -B task-cycle/test_gate_times.py RegistryTest`) | exit 1: `test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing` fails at `self.assertNotIn(name, listing)`, `farend.run` still in the registry |
| undone: `git checkout -- task-cycle/gate_times.py`; `git diff -- task-cycle/gate_times.py` | empty |
| the cited test passing after the undo (the three full runs above, run after the undo) | exit 0 |
| second break, not asked: `if malformed(begin, finish, end):` in `count_others` changed to `if False:` | exit 1: `test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing` fails (`'0' != '1'`); undone, diff empty |
| third break, for the new `touching` entry: `finish > start` changed to `finish >= start` | exit 1 (count `2` expected, `3` found); undone, diff empty |
| `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/test_gate_times.py` | exit 0, `All checks passed!` |
| `python -B elements/common/foundation_check.py --skip-test-citations` | exit 0, `0 errors` |
| `python -B elements/common/foundation_check.py` (extra, after the commit) | not exit 0 for the invariants other slices cite; `grep -c gate-times` of its output is `0`, so the citation of `gate-times-refuses-impossible-entry` is read |
| `grep -n "time.sleep\|time_ns\|time.time()" task-cycle/test_gate_times.py` | one hit, line 159 (below) |

Test-first note: the cited test is one that already had the behaviour; it was seen failing by breaking
the behaviour for a moment (the second row above), then undone.

## The grep hit left

`task-cycle/test_gate_times.py:159`, `time.sleep(0.02)` in the source text of the loop `waiting_for`, which
is written into the two test files of the runner test. It polls for a file between checks; the loop ends
when the file exists, and no expectation depends on the length of the sleep (the bound of 6000 rounds is a
timeout for failure). No `time_ns` or `time.time()` is left.

## Own-work check (section 3)

- The requirement most likely not met: "tests no longer depend on the real clock or on constant sleeps" —
  the test that waits for another process is the place a race could remain. Weakest point of the slice: the
  runner test, which needs `a` to end after `b` and `b`'s time to lie inside `a`'s. Check made: reasoned
  through each order of starts (b's timer starts only after `a`'s start file; `a`'s timer ends after
  `b`'s report is read by the test), and ten runs in a row of the class, all `OK`. The margin between the two
  printed times is the time of `b`'s exit, the relay and `a`'s next poll (tens of milliseconds, against a
  needed 1 ms at three decimals); that margin is a measured-by-reason, not a guaranteed, bound.
- Trust boundary (`task-cycle/gate_times.py`, not changed): crafted input checked at the script: a registry
  with entries of 200-digit times (running and ended), an Arabic-Indic digit start and `0_0_d.run`, run in
  `.runs/executor-6/` (removed): exit 0, all four entries deleted, no crash; plus the existing tests of the
  file (malformed entries, bars and 5000-character directory lines, 2000 blocks, a directory in place of an
  entry).
- Mutations considered: a count taken before the command (caught: `inside` is made while the command
  runs), `finish >= start` (caught by `touching`), the deletion and the count guard (caught, above), a
  clock not replaced (caught by the Started cell and the own entry name), a wrong pairing of a directory
  and its time (caught by the equality with the times the runner printed; differing times are forced by the
  containment above).

## Tests left on the real clock (the Choices row: a test that must run the script as a process keeps it)

All other tests run the script as a process for its exit code or streams (`RowsTest`, `CapTest`,
`PassThroughTest`, `ErrorTest`, `test_unusable_registry_...`, `test_default_registry_...`). None of them
expects a time: the Started and total cells are checked by form (regex) only.

## Reach beyond the handoff

None. The invariants of the orchestrator's additions were read (`script-language`, `script-imports`,
`script-subprocesses`, `cross-part-imports`, `test-method-citation`); the test imports only the standard
library and a file of its own part; no program is started beyond git and the interpreter.

## Working copies

`.runs/executor-6/` held one registry and one output for the crafted-input check; removed (no remainder).

## Problems seen

None in the product. Three details: the handoff's line numbers of `task.md` passages differed from the
file (the passages were found by content); the plan's Slice 6 text says the entries are built from "a fixed
value" — the clock stands at one instant, so the entry that "ended inside the run" ends 5 seconds after
that instant (a run of zero length cannot hold an entry); `import gate_times` carries no `# noqa: E402`
(E402 is not among the selected rules, so a `noqa` would stand for nothing).

## Unread material

- `task.md`: read in part — lines 30-43 (items 4-17), 155-185 (answers 16-21), 250-262 (cause 4) and
  540-546 (settlements 27-32); the ranges the handoff gives differed from the file, so I read by
  neighbourhood and by content. The rest of the task is unread.
- `plan.md`: Slice 6 as given in the handoff, *Choices* (1003-1019) and the orchestrator's additions
  (1021-end) read; the rest of the plan is unread.
- Everything else the handoff names was read whole: the foundation entries E31, WAY-394 (E11), WAY-395
  (E12), WAY-48, WAY-235, WAY-08, WAY-243, the invariant `test-method-citation` and the five invariants of
  the additions, the part `task-cycle`, `gate_times.py` whole, `test_gate_times.py` whole.

## Searches not found or unclear

none
