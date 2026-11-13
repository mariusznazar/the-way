# Fix report — gate-series-on-test-runner

**Status:** done
**Commit:** `b8dc239` — Restore the recorder violation of WAY-339 and name the test runner of the process (range from `909fcb9`)
**Check:** `python -B elements/common/foundation_check.py` passed (0 errors, exit 0), also with `--skip-test-citations`. No code or tests touched; `gate/run_tests.py process-audit` not re-run.

## Findings

1. **Blocking: restored.** The *violates:* bullet "a change of the script that records the gate times leaves their series whole" is back as it was, and the runner case is a separate bullet beside it. My earlier author report called the base wording a contradiction. The reviewer is right: it was a correct violating example. My mistake, not a fact about the entry.
2. **Minor, fixed.** The binding sentence, *violates* and *Rationale* now say "the test runner of the process" (in the binding sentence, "whose output gives the time of each directory"). No "of the gate" left for the runner.
3. **Minor, fixed.** *Rejected* now reads "the runs made between the move to parallel directories and this decision mixed with the earlier ones", with no reference to the change being merged.
4. **Minor, fixed.** The last *Rationale* sentence now gives the reason only: the test runner is part of the measurement of the gate times, since a change of how it runs the directories changes what each time measures, and its output is what the times are read from. The sentence on what the runner does today is gone.
5. **Structure, no change asked.** Answered as the finding gives: no change made.

## Own-work check

- Requirement: the decision keeps every violating and complying case it had, and says "the test runner of the process" where the code watches `gate/run_tests.py`.
- Check: read `foundations/decisions.md` WAY-339 after the edit; `foundation_check.py` run both ways (0 errors).
- Result: the recorder bullet is present (`git diff 909fcb9..b8dc239` shows the bullet restored), the runner bullet present beside it, and no "test runner of the gate" remains in the entry.

## Unread material

- `foundations/decisions.md` WAY-362, WAY-364 and WAY-366 were checked by search and by reading WAY-366's wording; not read whole. None of their text was changed.
- `reports/whole-review-report.md` was not read; the findings file is the handoff's named source.

## Searches not found or unclear

- none
