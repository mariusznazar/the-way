# Fix report — finding I-1

**Status:** done
**Commit:** `f604e93` docs: WAY-287 rejected states the general item's reason and the word search as the task gives them (`foundations/decisions.md`, 3 added / 2 removed)
**Base:** `fa445fd` (reviewed head)

## I-1: fixed

The finding holds. The entry's *Rejected* stated "No other decision asks for that" as a fact, and gave the general item's reason as "a list the human reads in full, so that its `none` says less", which is not in the task's *Questions to settle* 1.

Fix, in WAY-287 *Rejected* only:
- the reason now reads as the task gives it: it would encourage moving everything into the section, though its `none` is to mean the request can be merged;
- the categorical sentence is replaced by the task's qualification: a search of the log by the words "at the merge", "sees" and "merges" found no second such case; that is a word search, not proof.

Nothing else changed. WAY-274 untouched. The Minor findings are not touched.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| Task-cycle tests, at head `f604e93` (before the merge) | `python -B gate/run_tests.py task-cycle` | 0 | `Ran 94 tests`, `OK` |

## Searches not found or unclear

- The reviewer's aside that WAY-114 (about line 2085) and WAY-172 (about line 4808) have the human see something at the merge: not checked here. The fix does not depend on it; the qualification now says only what the task's search found.
- Nothing else searched for this fix.

## Addendum — repair of the report (no code, no commit)

Added on the branch head `23bb052` (the target merged in; the fix commit `f604e93` is in its history). Nothing above this addendum was changed.

### Own-work check (section 3 of the make-change skill)

- **Requirement most likely unmet:** the WAY-287 *Rejected* still states as fact what the task gives as a word search, or adds a reason the task does not give.
- **Check:** re-read WAY-287 *Rejected* (`foundations/decisions.md`, the paragraph beginning "C. Leave the rule as it is.") against `.runs/task-cycles/logging-scope-decision-section/task.md`, *Questions to settle* 1, third *Not chosen* (line 45: "przeszukanie dziennika nie znalazło drugiego takiego przypadku, a taka pozycja zachęcałaby do zrzucania do sekcji wszystkiego, choć jej `none` ma znaczyć „można scalić”") and *Context* (line 64: "to wyszukiwanie po słowach, nie dowód").
- **Commands and exit codes:**
  - `grep -n "No other decision asks\|reads in full\|says less" foundations/decisions.md`: no matches, exit 1. The dropped sentence and the author's own reason are gone.
  - `grep -n "not proof" foundations/decisions.md`: one match at line 8655 (the qualification is present).
- **What it showed:** the entry now gives the source's reason ("would encourage moving everything into the section, though its `none` is to mean the request can be merged") and the word search with its three words ("at the merge", "sees", "merges") as *Context* gives them, marked "a word search, not proof". The reading matches the task.

### Other sections the list asks for

- **Files changed:** `foundations/decisions.md` in the fix commit `f604e93`: 3 added, 2 removed; the fix changed three lines of WAY-287 *Rejected*.
- **Checks run at the new head, as command and exit code:**
  - `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
  - `python -B gate/run_tests.py task-cycle` at head `f604e93` (before the merge): exit 0, `Ran 94 tests`, `OK`. At head `23bb052`: exit 0, `Ran 139 tests`, `OK` (the merged target added tests, `test_remarks_check.py`).
- **Reaches beyond the dispatch:** none.
- **Choices, with the way rejected and its cost if wrong:**
  - Kept the three words of *Context* in the qualification. Rejected: the bare "word search, not proof" without them. Cost if wrong: the reader cannot tell which search was made.
  - Used the source's reason as given, not a shorter paraphrase. Rejected: the paraphrase "so that its `none` says less" (the author's own reason). Cost if wrong: the entry gives a reason the task does not give.
- **Searches not found or unclear:**
  - The user's script rule (`.ai/rules/scripts.md`) was not read before my earlier Python edits in this cycle; it was read during this repair. The line endings were unchanged: `git diff --numstat` showed only the intended lines. Those earlier scripts wrote no backslash literals.
  - Nothing else new; the earlier "Searches not found or unclear" section stands.
