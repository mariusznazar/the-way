# Findings of the review of correction 2, for the fix

Cut word for word from `reports/review-correction2-report.md` (head `17065c8b9b2349b4f5953ac98a15285e3d221787`): the blocking findings only. The Minor findings of a review of a correction are not fixed (they go to the request's list).

### Important

**I-1. The reading of a second reason in the text of one attempt is stated in three ways, and none is
what the code does — exactly on the shape of M-2 that the author flagged.**
Places: `foundations/decisions.md:8116-8118` (WAY-405's binding sentence: "its later lines are details
of that attempt, read for a second `reason: ` alone, so that a second attempt written in them with its
reason in other words is not read"; and `:8115-8116` "holds no other"); `foundations/decisions.md:8133-8134`
(*Verification*: "holds two markers ... read for a second marker alone");
`process-audit/audit_count.py:155` ("read for a second marker alone"); `process-audit/record_items.py:15-16`
("holds two markers ... read for a second marker alone").

What the code does: `discarded_reason` (`record_items.py:225`) counts `REASON_START = "reason: \`"` —
`reason: ` **followed by a backtick**, whatever word stands in the backticks. So:
- The binding sentence says more than the code. A later line `- reason: open design choice` (M-2's first
  shape, which the reviewer described as one that "holds no `reason: \``") holds a second `reason: `, so
  by the sentence it is read and gives unknown; the code gives `no` (probe B1: first attempt plain under
  the empty item, then `  - reason: open design choice` → `('no', None)`; B2, the same with the first
  attempt beside the colon → `('no', None)`). Nor is it "its reason in other words": the words are the
  marker's own, only the backticks are missing. The author's own test holds the code against the
  sentence it cites: `test_a_later_line_with_no_marker_is_a_detail_even_where_it_names_a_second_attempt`
  (`process-audit/test_record_items.py:236-246`, cites "Where the lines under the item are not entries at
  one indent alone") asserts `no` for `"  - reason: open design choice"` and `"  reason: open design
  choice"`; my mutation that makes the code read what the sentence says (`REASON_START = "reason: "`)
  fails exactly those two subtests.
- The *Verification* and the two docstrings say less than the code. A later line `- reason: \`budget\``
  is no marker (the markers are the three words), so by "read for a second marker alone" it is a
  detail and the attempt gives `size`; the code gives unknown, "holds more than one reason" (probe B3;
  B4 the same on one line, where the binding "holds no other" and the *Verification* "holds two markers"
  likewise say `size`).

Why it matters: this is the flagged judgment call. The choice itself (a malformed second attempt is a
detail, answer of the first attempt) is one the human's words allow; but the rule that is to "say what
the code does" tells a reader the opposite for the very shape it was written for, so a reader who
writes or audits a record by WAY-405 expects `unknown` where the audit answers `no`. The human named
wording wider than the code as the thing to remove. Fix (no code change): say, in all five places, that
the text is read for a second `reason: ` followed by a word in backticks (the opening `` reason: ` ``),
so that a second reason written without backticks or in other words is not read, and make "holds no
other" / "holds two markers" say the same.

Contradiction: yes — WAY-405 (its binding sentence and *Verification*, written by this change, against
the code `discarded_reason` and the change's own test).

**I-2. WAY-404's new *Verification* clause "whatever else the record holds, so that a yes stands over
an unknown" is wider than the code: a doubled item *Discarded attempt* is an unknown that the yes of
`open design choice` does not stand over.**
Place: `foundations/decisions.md:8078-8082`; the test that cites it,
`test_a_yes_stands_over_an_unknown_wherever_the_unknown_comes_from` (`process-audit/test_record_items.py:380-400`).
What the code does: `read_contradiction` (`record_items.py:284-289`) returns a yes of *Review rounds*
first, then returns unknown, "the record holds the item `Discarded attempt` more than once", before it
reads any marker of the item. Probe C1: `- Discarded attempt: reason: \`open design choice\`` and a second
`- Discarded attempt: reason: \`size\``, rounds marked `no` → `(None, 'the record holds the item
\`Discarded attempt\` more than once')`; C2 the same with an unmarked round → unknown; C3 a round marked
`yes` with the item doubled → `yes` (so the round's yes does stand over it, the item's does not). The
test's name says "wherever the unknown comes from", and its records cover an unmarked round, *Review
rounds* out of form, an unreadable item and a missing item, but not a doubled item, the one source where
the claim fails. `audit_count.py:162` itself lists "where it is missing or doubled" among the unknowns.
Why it matters: the clause was added for remark 2 (item 5) to say which answer wins; as written, "whatever
else the record holds" includes a second item *Discarded attempt*, and a reader takes the record above
for `yes`. Narrow and rare, but it is wording wider than the code, which the human asked to remove.
Fix: qualify the clause (e.g. "where the record holds the item once") or name the doubled item among
what a yes of the item does not stand over; no code change, and a subtest for the doubled item.
Contradiction: yes — WAY-404 (its *Verification*, written by this change, against `read_contradiction`).
