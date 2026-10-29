# Return-step report

Status: done

## Comparison with the repository

The task's accepted foundation settlement is row 1. `WAY-260` records that row's meaning: every
stage reports unsuccessful searches and unclear points, or `none`, apart from its reach account;
the orchestrator copies each non-`none` item verbatim with the stage and report path into *Process
remarks on the-way*, retaining repeats. The fix commit also restores the rejected alternatives and
their source costs from the settlement. No other row or projected entry was carried.

The task names WAY-148, WAY-125, WAY-256 and WAY-27 as decisions in play. Their meaning is unchanged
and the change does not make them false: the new rule derives from WAY-148, while the report methods
and file placement follow WAY-125 and WAY-256. The task's account of the process-remarks channel
continues to align with WAY-27. The author and fix reports record the foundation search and its
findings; I did not repeat that search.

The whole changed-file list contains only `foundations/decisions.md` and files under `task-cycle/`.
The decisions part map assigns the decision log to `decisions`; the task-cycle part map assigns all
changed process files to `task-cycle`. No file was added or removed, so no part-map entry needs
correction. The repository files agree with those assignments. No drift or further foundation
correction was found.

## Foundation entries and request meaning

- Decision written: `WAY-260` — każdy etap raportuje, czego szukał i nie znalazł albo co było
  niejasne, a orkiestrator przenosi każde takie zgłoszenie dosłownie do uwag procesowych, osobno,
  z nazwą etapu i ścieżką raportu.
- Other decisions changed: none.
- Invariants written or changed: none. No invariant test changed.
- Environment facts: none.
- Glossary terms: none.
- Part-map entries: none.
- Projected entries: none.
- Settlements to record: row 1 is written as `WAY-260`.
- Surfaces changed: none.
- `Violated` marks set or cleared: none.

## Checks

- `git diff --name-status d115159c554752601749efa8270ae76fbe02f4df..HEAD` — exit code 0; it lists
  only the decision log and task-cycle files described above.
- `python -B elements/common/foundation_check.py` — exit code 0; `0 errors`.
- `git diff --check d115159c554752601749efa8270ae76fbe02f4df..HEAD` — exit code 0.
- The orchestrator's `python -B gate/run_tests.py` — exit code 0, reported in the handoff as 613
  tests across 8 directories, with 5 Windows-specific skips in `instruction-files`. I did not
  rerun it.
- Not run: other Python tests; no executable behaviour or test contract changed.

## Choices, reaches and searches

- No new choices. The review fix changes only the rejected-options wording to preserve the accepted
  source alternatives and their costs.
- No reach beyond the return dispatch. The task, earlier reports, part map and relevant foundation
  entries were named inputs.
- Searches not found or unclear: none.
- The return step found no mismatch to correct and made no commit.
