# Report — correction 1, task `scripts-after-foundation-review`

**Status:** done

**Commit:** `cf4fe175b01d0efb362c7ffad5e3089ebbf28695` on `task/scripts-after-foundation-review` (parent `3145e4f650a81fdbfa831092b2ea77c3ccc66b20`); author address checked: the private one.

## Remark carried out

Item 4 of `reports/correction-1-remarks.md`, as made: the rule that keeps the paths of the scripts that start a series now names the script that starts a series of the cost, and its test pins that path too. Items 1 to 3 and 5 to 13 were let through or accepted: nothing of them touched.

## Files changed (WAY-03: the invariant's sentence and its test change together)

- `foundations/invariants.md`, invariant `audit-series-script-paths`: +1 −1. The sentence now reads "to start a new series of the cost of cycles, of the measures of how a cycle's agents use context and the prompt cache or of the gate times — the script that measures the cost, `task-cycle/cycle_stages.py`, the script that counts those measures, ... — is a file git tracks." Method, Rests on, Derives from, Part and Violated unchanged (the part `task-cycle` was already named). Edited in place (WAY-07).
- `process-audit/test_audit_series_scripts.py`: +10 −8 (the sum of the commit is 11 insertions, 9 deletions with the invariant line).
  - The first test's paths now include `audit_count.COST_SCRIPT`: the path is a file git tracks.
  - The second test, renamed `test_the_paths_are_those_that_start_the_series` (was `..._the_two_series`; no other file cites the name), compares the set of every path in `audit_count.TOOL_GROUPS` (the audit's own list of the paths that start a series, which is what the audit splits by) with the four paths named in the test. A path added to or dropped from any group fails it.
  - The module docstring and one comment ("three scripts" to "four") follow.
- `process-audit/test_audit_count.py`: untouched, as told.

WAY-339 read whole with its *Verification*, which names this invariant (`invariants: audit-series-script-paths`) and stays true: it names no number of paths.

## Checks (command, exit code)

- Red, new case: on the head's `process-audit/audit_count.py` with `COST_SCRIPT` temporarily set to a path that does not exist (`task-cycle/cycle_stages_moved.py`), `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: exit 1, the first test fails with `['task-cycle/cycle_stages_moved.py'] != []`. The test of the head, which did not name the cost script, would stay green for the same move. Restored with `git checkout process-audit/audit_count.py` before the commit.
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` after: exit 0, 3 tests OK.
- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`): exit 0.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k PriceBoundary -k ProcessVersions`: exit 0, 25 tests OK.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k test_each_path_that_starts`: exit 0, 1 test OK (the test left as it is).
- Not run: the whole gate (the orchestrator runs it).

## Own-work check

Requirement: a move or rename of `task-cycle/cycle_stages.py` while the audit keeps the old path must fail a test, so that the series of the cost cannot silently stop splitting. Check: the break above (a path that does not exist as the cost script). It showed the first test red for the cost path. The second test does not fail for that break (it compares the constants with themselves); it catches a path added to or dropped from a group, as its comment says.

## Choices

- Second test compares `TOOL_GROUPS` (all the audit's paths) rather than adding the cost path to `GATE_SCRIPTS` check: the old comparison covered gate paths only; the new covers all three groups in one set. Rejected: keeping the old assertion beside it (redundant, since a change of the gate group changes the union). Cost if wrong: a path added to a group in `TOOL_GROUPS` by a deliberate change needs one more line in this test, which is its purpose.
- The sentence names `task-cycle/cycle_stages.py` in backticks, as `audit_count.py` is named in the same sentence; the other scripts keep their descriptions.

## Reach beyond the dispatch

None beyond the files named (also read `foundations/decisions.md` WAY-339 whole, as told, and `process-audit/audit_count.py` lines 405 to 510 for the constants).

## Unread material

`foundations/invariants.md` read around the invariant only (lines 385 to 424), not whole; `process-audit/audit_count.py` read in the part with the constants. Everything else named was read whole.

## Searches not found or unclear

None.

## Working copies

None made: directory `.runs/correction-1/` was never created; no logs left.
