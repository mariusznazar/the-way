# Author report — the fix of the review of the return step after correction 2 (I-1)

**Status:** done

**Range:** `9547acd470f7a05cba43193ab9bf4b2e56a12e22..` the one commit of this fix (`f5100d78`; `git rev-parse HEAD` in the worktree gives it). Files: `foundations/decisions.md`, `process-audit/SKILL.md`, `process-audit/audit_count.py` (docstring), `process-audit/record_items.py` (docstrings), `process-audit/test_record_items.py`. No code changed: the syntax trees of the two `.py` files with docstrings left out equal those at `9547acd4`.

## I-1 — fixed

I took the finding's way: the mark of an entry is read only where *Review rounds* is held once and in its form, so the round's yes stands over the unknowns of *Discarded attempt* but not over an unread *Review rounds*, over which the marker's yes alone stands. Each sentence was probed against `read_contradiction` before I wrote it (12 records: R1 to R8 of the finding, R1 with the mark in the second copy, and three more: a `yes` round with a doubled *Discarded attempt*, with *Review rounds* missing, and the marker in a doubled *Discarded attempt*):

| Record (Discarded attempt `none` unless said) | Answer |
|---|---|
| R1 *Review rounds* doubled, either copy holding the `contradiction yes` entry | unknown, "does not give its entries" |
| R2 the entry beside an entry in neither form | unknown, same |
| R3 the entry beside a second entry naming the same findings file | unknown, same |
| R4 text beside the colon (`- Review rounds: prose`) with the entry under it | unknown, same |
| R6 R1 with `reason: \`size\`` | unknown, same |
| R5 the entry in a well-formed item | `yes` |
| R7 R1 with the marker `open design choice` (also R8 with an entry in neither form) | `yes` |
| the entry with *Discarded attempt* doubled | `yes` |
| the marker with *Discarded attempt* doubled and readable rounds marked `no` | unknown, "more than once" |

Sentences changed:
- WAY-404 *Verification* (`foundations/decisions.md`): "yes where an entry of the item *Review rounds* carries the mark of a contradiction, that item being held once and in its form (no entry in neither form, no findings file named twice, nothing beside its colon), or the record holds the item *Discarded attempt* once and it gives the marker `open design choice`, so that each yes stands over the unknown that the other item gives and over that of an unmarked round, while a *Review rounds* that is not read gives no yes, nor does a doubled *Discarded attempt*; ... unknown where an entry carries no mark, or an item is missing, doubled or not read, and no yes stands". WAY-404's binding sentence says no such thing ("the audit takes from that mark, with the marker") and stays.
- `process-audit/SKILL.md`, Q1: the entry's yes is conditioned on *Review rounds* "held once and in its form", and "each `yes` stands over the `unknown` that the other item gives, but a *Review rounds* that is not read (doubled, with an entry in neither form, with a findings file named twice or with text beside its colon) gives no `yes` of its own, nor does a doubled *Discarded attempt*".
- `process-audit/audit_count.py` docstring: the self-contradicting "stands over every unknown" is replaced by "Each yes stands over the unknown that the other item gives, but the mark of an entry is read only where *Review rounds* is held once and in its form (...), and the marker only where *Discarded attempt* is held once" (two lines re-wrapped).
- `process-audit/record_items.py`: module docstring ("an entry that says `yes` is a yes where the item is held once and in its form (otherwise its entries are not read)") and the docstring of `read_contradiction`.

Other places searched (`stands over`, `says .contradiction yes`, `It is yes where`, `an entry that says` in `foundations/decisions.md`, `process-audit/`, `task-cycle/record_template.md`, `task-cycle/skill/`, `task-cycle/review/SKILL.md`): no other sentence claims that a round's yes stands over an unread item. The record template says only how an entry is written; I left it alone.

**Tests.** `test_each_yes_stands_over_the_unknown_of_the_other_item_but_an_unread_item_gives_no_yes` (renamed from `test_a_yes_stands_over_an_unknown_but_the_marker_not_over_a_doubled_item`, whose name said less; it cites WAY-404 as before) now holds: for five unread forms of *Review rounds* (doubled, the copy with the mark second, an entry in neither form, a findings file named twice, text beside the colon) with *Discarded attempt* `none`, `size` and `reserved choice`, the answer is unknown with "does not give its entries", and with the marker `open design choice` it is `yes`; and the entry in a well-formed item gives `yes`. Mutations of `read_rounds`/`rounds_item` in the worktree, restored afterwards (diff against a saved copy equal): allowing a findings file twice, allowing a doubled item, allowing text beside the entries, skipping the entry in neither form — each fails this test (exit 1) and the existing tests of those shapes.

## Not done, as the handoff says

m-1 and m-2 of the review: not fixed. No code changed; nothing beyond I-1.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- `python -B -m unittest test_record_items` in `process-audit` — exit 0, 36 tests.
- `python -B gate/run_tests.py process-audit` — exit 0, `Ran 276 tests in 549.244s`, `OK`.
- `python -B gate/run_tests.py task-cycle` — exit 0, `Ran 534 tests in 131.202s`, `OK (skipped=2)`.
- Not run: the product's full gate (by the handoff); `ruff` (not installed).

## The own-work check

- **Requirement most likely unmet:** WAY-11/WAY-263 — each sentence says what the code does, no wider and no narrower; the earlier rounds were caught on this each time.
- **Check:** the probe table above, run on the code before any sentence was written, then each new sentence read against the table row by row (both yes, each of the five unread forms, the doubled *Discarded attempt*), and the mutations.
- **What it showed:** the new sentences give every row of the table; one wrong thing I noticed on the way: the first draft of the audit_count docstring left a line over-long after the re-wrap, fixed before the run.

## Reaches beyond the handoff

None.

## Working copies

`.runs/author-correction-2-return-fix/` (`.runs/author-correction-2-return-fix/`) held `probe.py`, a backup of `record_items.py` and the outputs of the two gate runs; removed before this return.

## Unread material

none — the handoff, the finding, WAY-404's entry, the Q1 passages of `process-audit/SKILL.md` and `audit_count.py`, `record_items.py` and the test were read.

## Searches not found or unclear

none.
