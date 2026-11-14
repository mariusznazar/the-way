# Author report — fix of the review of the whole change

**Status:** done
**Commit:** `82d6431` (on top of reviewed head `c76debc`; worktree clean; no push).
**Files:** `foundations/decisions.md` (77 added, 72 removed lines; the removals are mostly rewrapped lines), `elements/decisions/template.md` (1 added, 1 removed).

## Findings

1. **Blocking, decisions template restated WAY-90 differently.** Agreed. The last sentence of the new
   point in `elements/decisions/template.md` now reads "A measurement whose report a reader can open at
   an address is a citation, and a fact where the point above asks for one (WAY-90)", the wording of the
   environment facts template. The two templates and WAY-90 now say the same.
2. **WAY-256.** Added the sentence at both places where the estimate stands: *Rationale* ("The
   estimate is this product's own, and its record is not open to a reader of this repository.", after
   the sentence with the five to fifteen percent) and *Rejected* ("(the estimate is this product's own,
   and its record is not open to a reader of this repository)"). It says "estimate", as the entry does.
3. **WAY-90 price.** One sentence added at the end of the rationale's new passage: "The price: a
   measurement of the product's own agents leaves no fact for the search of WAY-33 to find, so when the
   model it measured is replaced nothing flags the decision that rests on it; a finding of others about
   agents or models still gets its fact, as WAY-17 asks." WAY-17 is unchanged: it speaks of findings of
   others, which still get a fact, so the two are consistent.
4. **WAY-229 *Rejected*.** Clause added after "got a PASS in both": "(the same measurement, this
   product's own, whose record is not open to a reader of this repository)".
5. **Wrapping.** The paragraphs I had inserted into (WAY-90 *Rejected* and binding part, WAY-255,
   WAY-300, WAY-309, WAY-323, WAY-350, WAY-353, WAY-364, WAY-368, WAY-229) were rewrapped from the
   first inserted line to the end of their paragraph, to 100 characters, by a script
   (scratchpad, not committed). The "definition with no body" orphan line of WAY-368 is gone. The
   same text: `git diff c76debc --word-diff` shows only the changes of findings 3, 4 and 2 as words.
   In the paragraphs I rewrapped, the line breaks of text I did not touch moved with the rewrap, as a
   rewrap does; no word changed.

WAY-312 is unchanged, as the handoff says. No finding held wrong.

## Checks

| Command (worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`) |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 (`0 listed`) |
| `python -B task-cycle/private_paths_check.py elements/decisions/template.md` | 0 (`0 listed`) |
| `python -B gate/run_tests.py elements/common` | 0 (144 tests OK) |

Not run: the full gate (the cycle's run).

## Own-work check

- **Requirement most likely missed:** finding 5's "same text, no new meaning, nothing else changed" —
  a script rewrap could drop or join a word, or break a code span.
- **Check:** `git diff c76debc --word-diff=porcelain -U0 -- foundations/decisions.md`, lines that add
  or remove a word. **Showed:** only the words of findings 2, 3 and 4 (and the line breaks that
  carry them); no other word added or removed. A second check, the length in characters (UTF-8) of
  every line added against the base `3c572b9`: none over 100. (A first run of that check read the diff in
  the console's code page and counted the long dashes as three characters, reporting four lines too
  long; rerun in UTF-8 it reports none.)
- Second requirement: the two templates say the same as WAY-90 — compared the three texts by eye
  after the edit: all three say that a measurement with an open report is a citation and follows the
  fact rule, and one with a closed record stays in the prose with the sentence and no fact.

## Unread material

none beyond the previous report's list: this fix read the handoff, the findings file, and the
passages of the entries it edited (WAY-90, WAY-229, WAY-256 whole in the passages edited). I did not
open `reports/reviewer-whole-report.md`; the findings file was enough.

## Searches not found or unclear

none. (Whose skill the estimate of WAY-256 is stays unknown, and is answered by the sentence, as the
handoff chose.)
