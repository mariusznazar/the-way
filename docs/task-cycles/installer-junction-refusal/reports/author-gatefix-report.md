# Author gate-fix report — installer-junction-refusal

## Status

`done`

## Commits

- the one commit of this fix, `Reset one product between subtests instead of assigning self.product again` (only `installation/test_install.py`; hash in `git log -1` of the branch, after `e899494`). Not pushed.

## The failure and its cause (verified, not taken on trust)

- **Failing run on the unchanged head `e899494`:** `python -B gate/run_tests.py elements/part-map` → exit 1, `Ran 39 tests in 31.993s`, `FAILED (failures=1)`: `test_the_way_imports_only_from_allowed_parts` lists `installation/test_install.py:800: runs a file the check cannot work out` and `:819: ...` (the two lines the gate log gives).
- **Reading of the check** (`elements/part-map/test_cross_part_imports.py`, header): a path is worked out from, among others, "the names and `self.<name>` attributes the file assigns, where every plain assignment of the name gives the same value". The two runs are `command(sys.executable, "-B", str(check), ...)` and `... str(migrate) ...` in `test_empty_foundations_have_valid_form` and `test_empty_foundations_are_in_the_current_form`; each takes its path from `self.product`. `self.product` was assigned in `setUp` (`Path(self.temporary.name) / "product"`) and, in my helper `another_product`, again as `Path(self.temporary.name) / name` — two different values, so the check could not work it out. The hypothesis in the handoff is right.
- **Confirmation by the fix:** removing the second assignment (below) makes `python -B gate/run_tests.py elements/part-map` pass, with nothing else changed.

## The fix (test code of mine only)

In `installation/test_install.py`:

- `another_product(name)`, which assigned `self.product`, is replaced by `empty_product()`, which assigns nothing: it removes `self.product` with `shutil.rmtree(..., onexc=make_writable)`, makes the directory again and runs `git init -q` in it. The three tests that used it (the junction on the path of a written file, the junction at a stale entry's folder, the scans of stale files) call `empty_product()` at the start of each subtest, so each subtest still starts from a new empty Git repository as before. The outside folders those tests use were already named by their own variables.
- The local `writable` handler of `test_rejects_a_junction_at_the_submodule_directory` moved to a module-level `make_writable`, so the helper and that test share it.
- Kept: every assertion of the three tests, and all six `# invariant: installation-paths-through-links` citations (the four in `test_install.py` and the two in `test_agent_types_installation.py`; `grep` shows all six). The check, the existing tests and the foundation are untouched.
- One thing the reuse of one directory could break and I checked: `rmtree` of a product holding a junction must not follow it into the outside folder. It does not: the first test keeps its outside folder across subtests and asserts, before each subtest, that it holds the canary only (`sorted(...) == ["kept.md"]` and an unchanged tree), and it passes.

## Checks (command, exit code)

| Check | Command | Exit | Result |
|---|---|---|---|
| Failing run, unchanged head | `python -B gate/run_tests.py elements/part-map` | 1 | `FAILED (failures=1)`, the two lines above |
| Passing run, after the fix | `python -B gate/run_tests.py elements/part-map` | 0 | `Ran 39 tests`, `OK` |
| The junction tests and the two named tests | `python -B -m unittest installation.test_install -k junction -k stale_entry -k scan_for_stale -k empty_foundations -v` | 0 | `Ran 6 tests in 62.693s`, `OK`, all six `ok`, none skipped (the three junction tests, the scan test, `test_empty_foundations_have_valid_form`, `test_empty_foundations_are_in_the_current_form`) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Not run: the whole `python -B gate/run_tests.py installation` (about 14 minutes) and the whole gate. The change touches only the helper of three tests and a module-level function; the junction tests and the two tests the failure named ran. The orchestrator runs the whole gate after this fix.

Other checks that read test files: `elements/part-map` (the one that failed; run, above) reads every Python file git tracks and is the only one of the gate's checks that works out the runs of other files in tests; `foundation_check.py` reads the citations of the invariant (run, above). Another check of `gate/`, `elements/*` or `task-cycle/` reading `installation/*.py` was not found by name; nothing else in the change touches what they read (no import, no `sys.executable` run, no path added), which the part-map check passing for the same file confirms.

## Own-work check (WAY-164)

Requirement most likely not met by this fix: that the three tests still check what they checked, since the product directory is now emptied in place and not made new. The check: they ran after the change (the junction ones in the unittest run above); the junction test asserts the outside folder is unchanged at each subtest, which would fail if `rmtree` followed a junction or the reset left a stale pin or `.gitmodules` from the earlier subtest (the stale test installs for real, with `--apply`, so a left-over `.git` state would show as a different plan or an error); both passed. I did not rerun the failing run of the invariant's tests before the fix: their failing run is the first report's, and the fix changes no assertion.

## Reaches beyond the handoff

- `elements/part-map/test_cross_part_imports.py` lines 1-60 (the header), to check the hypothesis. No other file.

## Unread material

- The gate log `final-gate.log`: not read; the handoff gives the failing test and its two lines, which I reproduced with `python -B gate/run_tests.py elements/part-map`.
- The body of `elements/part-map/test_cross_part_imports.py` past its header: not read (the header states the rule; running the test confirmed the result).

## Searches not found or unclear

- None.
