PASS ef083d12c70830d251a7ba950e38dca5a1419d42

# Report 18 — review of the fix of findings 2

Range reviewed: `8cbcac0b8dab89fcd56257955bd6f5c62c1194ff..ef083d12c70830d251a7ba950e38dca5a1419d42`
(`git rev-parse HEAD` = `ef083d12c70830d251a7ba950e38dca5a1419d42`), one commit `ef083d1`, one file:
`elements/part-map/test_cross_part_imports.py` (+36 −10). Bounded by `reports/15-findings-2.md`,
which holds I1 of report 14 only.

Counts: blocking 0, Minor 0, out of scope 0.

## Findings of the findings file

**I1 — fixed.** A command line of `sys.executable` whose script is joined on after the list no
longer passes in silence:

- `command()` (`elements/part-map/test_cross_part_imports.py:281-293`) reads a `+` whose left side
  is a command line, nested to the left, and adds the right side's elements where it is a list or
  tuple, `None` otherwise; `runs()` (:337-344) reads such a `+` once, marking its inner lists in
  `joined`.
- `command_line()` (:309-335) fails an element `None` and, after the loop, a command line that ran
  out of elements with no script, `-c`, `-` or `-m`: "runs a command line the check cannot read".
- The three forms from my probe now give: `[sys.executable, '-B'] + [<path>]` and
  `[sys.executable] + [<path>]` → forbidden `core/engine.py` → `shell/screen.py`;
  `cmd = [sys.executable]; cmd.append(<path>)` → the problem above. Not contested.
- The docstring (:14-21) says what the code does, including both new failures.

## The fix diff itself

Nothing new found. Probed forms beyond the fixtures (scratch `gaps2.py`, below), each as I would
expect: `[sys.executable, '-B'] + ARGS` and `[sys.executable] + (['-B'] + [<path>])` (right side
not a list) → problem; `[sys.executable, '-X', 'utf8']` (options only) → problem;
`prefix + ([sys.executable] + [<path>])` and `os.execv(sys.executable, [sys.executable] + [<path>])`
→ forbidden, read once; `([sys.executable, '-B'] + ['-m']) + ['shell.screen']` → forbidden
through the module; `[sys.executable, '-c', 'pass'] + ['x']` → no file, as `-c` gives. The tree's
one joined form (`gate/test_run_tests.py:55`) still reads its script first. Each part of the fix
has a fixture with teeth (my mutations below). The fixture `subprocess.run([sys.executable])`
moved from "no file" to "cannot read", as the finding's fix proposed.

## Declined to judge

- M1 (`-c` code not read) and M2 (two branches without a fixture) of report 14 — Minor, not in the
  findings file; they go to the request (WAY-161).

## Checks run

- `git rev-parse HEAD` → `ef083d1…`, exit 0; `git diff 8cbcac0..ef083d1` read whole.
- `python -B gate/run_tests.py elements/part-map` → exit 0, 28 tests OK.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- Probe
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\reviewer\gaps2.py`
  (12 command lines in the test's own fixture repository) → exit 0, results above.
- Real-tree listing `…\scratchpad\reviewer\runs_real.py` → 30 runs, 0 unknown (output
  `…\scratchpad\reviewer\runs_real2.txt`).
- Mutations `…\scratchpad\reviewer\mutate3.py` on a copy outside the tree (real-tree test pointed
  at the worktree), each `python -B -m unittest test_cross_part_imports`: unmutated → exit 0;
  trailing "cannot read" removed → exit 1 (3 subtests of `test_run_the_check_cannot_work_out_fails`);
  `+` branch removed → exit 1 (`test_each_form_of_a_run_is_seen`); `joined` skip removed → exit 1
  (`test_each_form_of_a_run_is_seen`, `test_run_the_check_cannot_work_out_fails`); `None` element
  read as a path → exit 1 (`test_run_the_check_cannot_work_out_fails`). None survived.
- `git status --short` in the worktree afterwards → empty.
- Not run: the whole gate — the orchestrator's.

## Reaches beyond the dispatch

None.

## Searches not found or unclear

none
