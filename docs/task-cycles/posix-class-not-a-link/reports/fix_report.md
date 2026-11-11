# Fix report: review of the whole change (head `8fa6bac`)

**Status:** done
**Commit:** `15c2062` on `task/posix-class-not-a-link` (one commit, `foundations/decisions.md` only, 3 lines changed).

## Findings

1. **Minor, within the task — fixed.** WAY-323 *Rationale* said "Each of the twelve names is kept to, not matched by a
   pattern". The code does match the twelve names (an alternation in `POSIX_CLASS`), so the sentence was loose.
   Reworded in `foundations/decisions.md` (the *Rationale* paragraph, line 10594) to the reviewer's wording:
   "The twelve names are listed one by one, not matched by a general shape, so a text with another name between the
   colons stays listed, since it may be a note." The binding sentence and *Verification* were not touched.

   The finding is right; I did not hold it wrong.

## Checks (command, exit code)

- `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` — exit 0, `checked: 275 files, 0 listed`.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` — exit 0, 263 tests OK. Output saved to the scratchpad.
- `grep -n "listed one by one" foundations/decisions.md` — the reworded line is present (line 10594).

Not run: the full gate (not asked for).

## Unread material

none — the fix handoff, `fix_findings.md` and `task-cycle/change/fix.md` were read whole; the one file changed was already read whole in the earlier cycle.

## Searches not found or unclear

none
