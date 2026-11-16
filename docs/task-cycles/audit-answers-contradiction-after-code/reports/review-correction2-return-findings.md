# Findings of the review of the return step after correction 2, for the fix

Cut word for word from `reports/review-correction2-return-report.md` (head `9547acd470f7a05cba43193ab9bf4b2e56a12e22`): the blocking finding only. The Minor findings of a review of a return step are not fixed (they go to the request's list).

### Important

**I-1. The sentences say that a `contradiction yes` of an entry of *Review rounds* gives `yes` whatever
else the record holds; the code reads that mark only where the item *Review rounds* itself is read, and
gives `unknown` where the item is doubled, holds an entry in neither form, names a findings file twice
or holds text beside its colon — one of them written by this commit in a form that contradicts itself.**

Places:
- `process-audit/audit_count.py:158-159` (written by this commit): "A yes of an entry of *Review rounds*
  stands over every unknown, that of the marker over every one but a doubled item *Discarded attempt*."
  Six lines later the same docstring lists, among the unknowns, "where *Review rounds* is missing,
  doubled or in neither form" (`:165`) — an unknown the entry's yes does not stand over.
- `process-audit/SKILL.md:225-229` (written by this commit): "`yes` where an entry of *Review rounds*
  says `contradiction yes` or *Discarded attempt*, held once by the record, gives the reason `open design
  choice` ...; a `yes` stands over the `unknown` of any other part of the record, save that the reason
  does not stand over a doubled *Discarded attempt*, which only the mark of an entry does". The
  qualifier "held once by the record" is given to *Discarded attempt* alone and the only exception
  named is the marker's, so a reader takes a doubled or out-of-form *Review rounds* that holds a
  `contradiction yes` entry for `yes`.
- `foundations/decisions.md:8077-8083` (WAY-404's *Verification*, left by the step): "yes where an entry
  carries the mark of a contradiction or the record holds the item once and it gives the marker `open
  design choice`, so that a yes stands over an unknown of any other part of the record, save that the
  marker does not stand over a doubled item, over which the mark of an entry alone stands". The same
  asymmetry: the item is qualified, the entry is not.
- `process-audit/record_items.py:283-284` (the docstring of `read_contradiction`, which this commit
  rewrote around this clause and left it): "It is yes where an entry of a round says `contradiction
  yes`"; likewise the module docstring `:24` "an entry that says `yes` is a yes".

What the code does: `read_contradiction` (`process-audit/record_items.py:287-289`) takes the round's
yes only from `read_rounds`, which returns None for the whole item where `rounds_item` finds it missing,
doubled, with text beside its entries or in neither form (`:95-122`), where an entry is in neither form
(`:148-152`) or where a findings file is named twice (`:154-155`); a None never gives yes, and with
*Discarded attempt* `none` or `size` the answer is unknown (`:300-302`). Probes at the head, *Discarded
attempt* `none` in each (`.runs/review-correction-2-return/probe.py`):
- R1 *Review rounds* doubled, one copy holding `findings \`reports/a.md\`, contradiction yes` →
  `(None, 'the item \`Review rounds\` does not give its entries, ...')`;
- R2 the `yes` entry beside an entry `the return step: fix` (neither form) → the same unknown;
- R3 the `yes` entry beside a second entry naming the same findings file → the same unknown;
- R4 the `yes` entry under `- Review rounds: prose` → the same unknown;
- R6 R1 with *Discarded attempt* `reason: \`size\`` → the same unknown;
- controls: R5 the `yes` entry in a well-formed item → `yes`; R7 R1 with the marker `open design
  choice` → `yes` (the marker's yes does stand over an unread *Review rounds*, as the sentences say).
No test holds R1-R4: `test_a_yes_stands_over_an_unknown_but_the_marker_not_over_a_doubled_item`
(`process-audit/test_record_items.py:392-422`) pairs the round's yes only with unknowns of *Discarded
attempt* and the marker's yes with an unread *Review rounds* (`:404`), never the round's yes with an
unread *Review rounds*.

Why it matters: the return step exists to make the sentences about Q1 say what the code does (WAY-11),
and the human's remark 2 of correction 2 asks the same. A reader who writes or audits a record by these
sentences expects `yes` for a cycle whose *Review rounds* holds a marked round and one slip (a second
copy of the item, an entry that opens with neither word, a findings file named twice), and the audit
answers `unknown`. The code is the side to keep: point 4 of the task's *To do* says an entry in neither
form still gives `unknown` with a reason, and reading the marks of an item not read would undo that.
The audit_count sentence is wrong on its own face ("every unknown" against its own list).
Fix (no code change): in the four places, say that the mark of an entry is read only where *Review
rounds* is held once and in its form (no entry in neither form, no findings file named twice, nothing
beside its colon), so that the round's yes stands over every unknown of *Discarded attempt* but not
over an unread *Review rounds*, over which the marker's yes alone stands; and add R1-R4 (unknown) and
R7 (yes) as subtests of the test above, which cites WAY-404.

Contradiction: yes — WAY-404 (its *Verification*, which the change writes: "yes where an entry carries
the mark of a contradiction ... so that a yes stands over an unknown of any other part of the record",
against `read_contradiction`).
