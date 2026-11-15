# Return step 2 report — correction 1, task `scripts-after-foundation-review`

**Status:** done

Worktree `the root of the task's worktree`, head `cf4fe175b01d0efb362c7ffad5e3089ebbf28695`. Commits: none (nothing needed a change).

## Foundation compared with code (what the correction touches)

The correction `cf4fe17` changes `foundations/invariants.md` (the sentence of `audit-series-script-paths`) and `process-audit/test_audit_series_scripts.py`.

- Invariant `audit-series-script-paths`: the sentence now names the series of the cost and the script that measures it, `task-cycle/cycle_stages.py`, beside the scripts of the measures of context and cache use and of the gate times. The code agrees: `COST_SCRIPT = "task-cycle/cycle_stages.py"` in `process-audit/audit_count.py` (line 415), and the test reads the four paths (`COST_SCRIPT`, `MEASURES_SCRIPT`, `GATE_SCRIPT`, `GATE_TEST_RUNNER`) and compares them with every path of `TOOL_GROUPS`, the list the audit uses to give a changed tool's values as unknown. Fields: *Derives from* WAY-339 stands (the decision that splits the series); *Part* `process-audit · task-cycle · gate` already holds `task-cycle`, where `cycle_stages.py` lies, so no change. *Method* `test`, cited by `# invariant: audit-series-script-paths` in the test.
- WAY-339 *Verification* names `invariants: audit-series-script-paths` and its clause `tests:` says nothing of what the invariant covers; no sentence of it says the path of the cost script is unguarded. Nothing to change.
- Search of the whole foundation for `audit-series-script-paths` (decisions: `foundations/decisions.md` WAY-339 only; invariants; the test) and for "guarded": no sentence says that the cost script's path is not guarded. Nothing to change.
- Part map entries `process-audit` and `task-cycle`: unchanged by the correction, and still true (`task-cycle/cycle_stages.py` is a trust boundary of `task-cycle`; `process-audit/audit_count.py` of `process-audit`).

## Decisions written or changed

None.

## Invariants

None written or changed by me. **Closed point:** my first report said the invariant was not extended and that the request would propose it; the correction extends it at the human's remark (item 4 of the remarks), so that point is closed and the request no longer proposes it. The listing of the check names no file for it (the test file changed in the correction).

## Environment facts, glossary terms, part-map changes, projected entries

None.

## Rows of *Settlements to record* written, each with its place

Unchanged from `return-step-report.md`; the correction touches none of the eight rows.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py`: exit 0, "0 errors", one `listed:` (`guidelines-file-place`, as before).
- `python -B -m unittest discover -s process-audit -p test_audit_series_scripts.py`: exit 0 (3 tests).
- No run of the whole gate.

## Own-work check

Requirement most likely unmet: that no sentence of the foundation still says the cost script's path is unguarded or lists the invariant's scripts as the two series only. Check: search of `foundations/`, `elements/` and the code for `audit-series-script-paths` and "guarded" (above): the invariant's sentence and the test's docstring and comments are the only places that list the scripts, and both name the four. It held.

## Observations

- `process-audit/test_audit_series_scripts.py` line 2 is 115 characters long (the docstring line the correction re-filled around the new words). It is a comment in a reviewed file and not a foundation entry; I left it.

## Unread material

- `reports/correction-1-report.md`, `reports/review-correction-1-report.md`, `reports/correction-1-remarks.md`: not read; the handoff's summary and the diff of `cf4fe17` were enough.
- `process-audit/audit_count.py`: only the lines holding `COST_SCRIPT` and `TOOL_GROUPS` (seen in the first run) were looked at.

## Searches not found or unclear

none

## Working copies

None made; `.runs/return-step/` was removed after the first run and not recreated.
