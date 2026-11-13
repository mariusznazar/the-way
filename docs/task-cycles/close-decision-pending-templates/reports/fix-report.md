# Fix report — the Minor findings of the review of the whole change

**Status:** done
**Commit:** `faee0f8` on `task/close-decision-pending-templates`, one commit holding only the three fixes (head before the fix: `2c27260`).

## Findings as fixed

1. **`elements/invariants/template.md`, the test sentence (finding 1, S3).** Fixed. The citation is now `(WAY-61, WAY-321)`. WAY-321 reads: "reports an invariant whose method reads `test` and which no line `invariant: <identifier>` in a file git tracks other than Markdown cites". It carries the Markdown clause the sentence states. Check: `foundation_check.py --skip-test-citations` exit 0, 0 errors.
2. **`elements/part-map/template.md`, external context row (finding 2, S9).** Fixed by the first of the two options the reviewer named: the unconfirmed first citation is removed and "A row names no part and no file." stands without a cite. The second, exact citation "(WAY-48)" stays. This removes the repetition and the attribution the reviewer could not confirm. The task asked for WAY-48 at this sentence, so this is a departure from the task's pairing, made on the reviewer's finding.
3. **`elements/environment-facts/template.md`, Source section (finding 3, item 5).** Fixed. The sentence now names the two entries that carry a `TODO` and the form each takes from WAY-71:
   "An invariant whose *Rests on* names a missing fact takes `TODO — <the fact, with its source>` there, and a decision whose *Based on* names a missing source takes `TODO — <what is missing, with its source>`; a change that leaves one there puts it before the human (WAY-71)."
   WAY-71 gives exactly these two forms for those two fields.

## Checks run

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors" (run before and after the rewrap).
- `python -B gate/run_tests.py elements/common` — exit 0, "Ran 144 tests ... OK".
- Diff check: 3 files, 8 insertions, 7 deletions; no added line over the file's width.
- Not run: the full gate (the orchestrator's); `foundations/decisions.md` and out-of-scope finding 4 untouched.

## Unread material

- `foundations/decisions.md` WAY-321 — read whole (heading to next heading); it was not in the dispatch, read to confirm finding 1.
- `elements/common/rules.md` — still unread (as in the author report); the fix did not depend on it.
- Nothing else new.

## Searches not found or unclear

- None new. The `*Based on*` italic marker is split across a line break in the Source sentence; markdown renders it, but the line break is a formatting choice the reviewer may want to see.
