# Fix report 1 — Minor findings of the review of the whole change

**Status:** done
**Commit:** `7c3161a` Fix the findings of the review of the invariant method change (on top of `e3fcc20`; not pushed)
**Files:** `foundations/decisions.md` (+4 -3), `foundations/invariants.md` (+1 -1), `elements/common/foundation_check.py` (+1 -1)

## Findings

- **M1 — fixed.** WAY-61 *Rationale* now reads "A change is judged as a whole, once finished, so an invariant written before its test within one change may read `test` from its writing, and a later slice that writes the test leaves the entry as it is." (the reviewer's wording, rewrapped to the file's width). Check: `grep` of the passage in `foundations/decisions.md` and `foundation_check.py` below. The binding sentences of WAY-61 and the question-4 places are untouched.
  - The "smaller point" of M1 (the *Rejected* clause "`TODO` as the method until the test exists — it names nothing that keeps the rule meanwhile") is not changed: the suggested fix does not cover it, the clause is about the value `TODO`, never about `test`, and its reason is true as written; I hold it to be no error, only a reading the finding asks for. Contested lightly; blocks nothing.
- **M2 — fixed as suggested.** `foundations/invariants.md`: `test-method-citation` now has `Derives from: WAY-61 · WAY-321`. WAY-61's *Verification* now opens `invariants: test-method-citation. For the rest, an agent compares the change with the decision:` (the form of WAY-63), followed by the unchanged pair of examples. WAY-321's *Verification* still names the invariant. Both decisions thus name the invariant that derives from them.
- **M3 — fixed.** `foundation_check.py:499` docstring shortened to `"""Report each invariant that reads `test` and no line `check_citations` read cites."""`; `awk 'length($0)>100'` on the file prints no line.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (run twice: after the edits and after rewrapping the rationale).
- `python -B gate/run_tests.py elements/common` — exit 0, 117 tests OK (run twice, same reason).
- `python -B task-cycle/private_paths_check.py <file>` on the three changed files — exit 0 each.
- `awk 'length($0)>100' elements/common/foundation_check.py | wc -l` — 0.
- Not run: the full gate (the orchestrator's, WAY-160); `installation` and `elements/part-map` (their code is untouched by this fix; a docstring line and two foundation text edits).

## Own-work check

Requirement most likely unmet: the invariant and WAY-61 name each other consistently (decision's *Verification* lists the invariants that derive from it, and each names the decision). Check: `foundation_check.py` reports a *Verification* naming a missing invariant and a *Derives from* naming a missing decision; both resolve (exit 0). The test `test_the_way_foundation_passes` cites `test-method-citation` and passes. No behaviour of the script changed, so no new test.

## Searches not found or unclear

- None. The findings file named exact places; all found by text.
