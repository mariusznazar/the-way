# Return step — gate-series-on-test-runner

**Status:** done with one correction in the change
**Commits of the return step:** `5b87cb1` — Rewrap the Rejected paragraph of WAY-339 to the entry's width (on top of `b8dc239`; the change's range is `715ae20..5b87cb1`)
**Check:** `python -B elements/common/foundation_check.py --skip-test-citations` and `python -B elements/common/foundation_check.py` both pass (0 errors). Code and tests were not touched by this step.

## Comparison

- **WAY-339** (the decision the change edits): the binding sentence, *Scope* (`process-audit`, `task-cycle`, `gate`), *Verification* and *Rationale* match the code. The code splits the mechanism measures on `task-cycle/cycle_measures.py` only, and the gate times on `task-cycle/gate_times.py` or `gate/run_tests.py`, with the reason naming the changed file(s). The *Rejected* paragraph had lines far beyond the entry's width after the fix; rewrapped in `5b87cb1`. No wording changed.
- **WAY-349** (times reach the record, through the script): matches; it says "in whatever order they come", which fits the parallel directories.
- **WAY-350** (only passing runs with no other run alongside are compared): matches the audit code's `gate_rows` behaviour that the change did not touch.
- **Part map**, `process-audit`, `task-cycle`, `gate`: all three entries still match their files. `gate` says the command runs every test of the-way; the test runner's parallel default (WAY-366) is not contradicted. No change.
- **Environment facts**: the change rests on no source outside the product. Nothing written.
- **Glossary**: no term of the change needs an entry; `gate` and "directory" carry no conflicting meaning. Nothing written.
- **Invariants**: the task sets no rule; none written. The change does not alter an existing invariant (`script-imports`, `cross-part-imports`, `test-method-citation`, and the others checked earlier).
- **Settlements**: row 1 of *Settlements to record* is already written into WAY-339 (`b8dc239` and earlier). Nothing missed by the foundation step.

## Unread material

- `foundations/decisions.md` WAY-362, WAY-364 and WAY-366 were checked by search and by reading WAY-366's wording; not read whole. None was changed.
- `foundations/part_map.md` and the glossary were checked by search and by reading the three part-map entries and the `gate` glossary line; the rest of the glossary was not read.

## Searches not found or unclear

- none
