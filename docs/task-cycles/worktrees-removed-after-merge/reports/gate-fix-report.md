# Gate fix report — worktrees removed after merge

**Status:** done

**Commit:** `9a6b6fa` (Run the script in the tests in a form the check of cross-part imports can read), from head `eb5d28e`. One file: `task-cycle/test_remove_merged_worktrees.py`.

## The failure and its cause

`elements/part-map/test_cross_part_imports.py` reads, with `ast`, every command line of `sys.executable` and needs the script's path worked out from constants, `__file__`, `Path` joins and names or `self.<name>` attributes the file assigns; "parameters … are not read". My helper `Fixture.run` took the script as a parameter (`script: Path = SCRIPT`) and built `[sys.executable, "-B", str(script), …]`, so line 111 was "a file the check cannot work out". The cause is my test's form, as the handoff says; the base has no such failure.

## The fix

- `Fixture.run` has no `script` parameter and names the module constant `SCRIPT` (`HERE / "remove_merged_worktrees.py"`), which the check resolves.
- The one test that ran a copy of the script from inside a task directory (`test_the_directory_that_holds_the_script_is_not_removed`) now goes through a second helper, `Fixture.run_copy`, which runs `self.copy`, an attribute assigned once in `Fixture.__init__` (`self.worktrees / "merged" / ".runs" / "copy" / "remove_merged_worktrees.py"`); the test copies the script there and calls `run_copy`. The check resolves it (a path under the temporary directory, which it treats as outside the repository).
- Both subprocess calls of the file therefore pass the check; nothing of `elements/part-map/` and no check was changed, and what the tests of the script assert is the same (the same 46 tests).

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK (before the fix: one failure, the line above) |
| `python -B -m unittest task-cycle.test_remove_merged_worktrees` | 0 | 46 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 440 tests OK |

Not run: the full gate (the orchestrator's). The part-map run before the fix I did not repeat; its failing output stands in the orchestrator's log.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** that the fix changes only the form of the call, so every test still tests what it did, and that the copy test still runs the script from inside the task directory it must not remove.
- **Check:** the three runs above, from the changed file; the copy test is in the 46 and passes, and it asserts that the directory stands after `--apply` (it would fail if the copy were not the script that runs: the directory would then be removed).
- **Showed:** all three exit 0.

## Unread material

- none: the handoff's `elements/part-map/test_cross_part_imports.py` read in its docstring and the lines the check names for a run (the code near 354–400 I read only through the docstring's statement of the rule; the failing log was not opened since the handoff quotes it).
- `task-cycle/test_gate_times.py` and its neighbours: not opened; the docstring settled which forms pass and the run proved it.

## Searches not found or unclear

- none

## Working copies

None made (no throwaway repository by me in this step; `.runs/` holds only `task-cycles/`; the output files of the checks were removed). Remainder: none.
