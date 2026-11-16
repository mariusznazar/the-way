# Findings of the review of the return step, for the fix

Cut word for word from `reports/review-return-report.md` (head `d3068ed09017a0d0807c9e51d580ec3ba8b64589`): the blocking finding only. The Minor finding of a review of the return step is not fixed (it goes to the request's list).

## Important

### I-1 — WAY-404 now says that a plain line or an entry at another indent beside the entries gives unknown; the code gives an answer for such items

**Place:** `foundations/decisions.md:7966-7968` (binding sentence of WAY-404, the clause added by this commit) and
`foundations/decisions.md:7976-7978` (its *Verification*, the clause added by this commit). The same broad wording
stands in the docstring this commit changed at `process-audit/audit_count.py:158-160` ("with its own reason where
*Discarded attempt* ... holds two markers outside a list of entries or a plain line or an entry at another indent
beside its entries").

**What is wrong.** The added clause reads: "an item that reads neither `none` nor a marker, written in any earlier
form, gives the answer unknown, and so does an item that holds two markers outside a list of entries, or a plain
line or an entry at another indent beside its entries (WAY-403)". *Verification* adds: "and that an item ... with a
plain line or an entry at another indent beside its entries, gives unknown." The code does not do that.
`discarded_reasons` (`process-audit/record_items.py:252-268`) reads an item whose lines are not entries at one
indent alone as the text of one attempt, and gives that attempt's reason where the text opens with `reason: ` and a
single marker; only a whole text that opens with no marker (for example one that opens with `- `) or holds two
markers gives unknown. And `discarded_entries` (`:224-238`) lets an entry deeper than the entries, after the first
one, through as a continuation, so an "entry at another indent" after the first is no cause of unknown at all. The
docstring of `discarded_reasons` that this same commit wrote says it rightly ("it gives that attempt's reason where
the text opens with one marker and holds no other (its details may be a list), and is not read otherwise"); the
decision drops that qualification.

**Evidence.**
- The suite itself contradicts the new sentence: `process-audit/test_record_items.py:142-151`,
  `test_one_attempt_on_the_line_under_the_item_with_its_details_as_a_list_is_read`, cites WAY-404 by a line
  `decision:` and asserts `yes`/`no` for an item of a plain line `reason: `<marker>`; 10:32` with two entries
  `- report reports/x.md`, `- reset to abc1234` beside it — a plain line beside entries, which WAY-404 now says gives
  unknown. `:191-195` and `:210-212` assert `no` for an entry deeper than the first entry, which the sentence calls
  "an entry at another indent beside its entries".
- Scratch run at `d3068ed` (probe `.runs/review-return/probe.py`, calling `record_items.read_contradiction`, with
  `- Review rounds: none`):
  - `- Discarded attempt:` / `  reason: `open design choice`; 10:32` / `  - report reports/x.md` / `  - reset to abc1234` -> `('yes', None)`
  - `- Discarded attempt: reason: `size`; details` / `    - a` / `  - b` -> `('no', None)`
  - `- Discarded attempt:` / `  - reason: `size`; details` / `    - reason: `open design choice`` / `  - reason: `reserved choice`` -> `('no', None)`
  Each holds a plain line or an entry at another indent beside the entries; none gives unknown.
- The form kept on purpose: the review of the correction (`reports/review-correction-report.md:24-29`) judged the
  author's choice to read such an item as one attempt "rather than `unknown` for any plain line" sound, because it
  keeps the details-as-a-list form answered. The return step's sentence states the rejected alternative.

**Why it matters.** WAY-263: the change restates an entry it writes more broadly than the code does, without the
qualification. A later change that brings the code in line with WAY-404 as written would turn the one-attempt
form with its details as a list — the form the template's *Discarded attempt* allows ("the details possibly as a
list", as the docstring of `discarded_reasons` says) — into unknown and break the test at `:142`; a writer of a
record who reads WAY-404 would avoid a form that is in fact read. The author's report (`author-return-report.md`,
item 1) claims the sentence now says what the code does; it says more.

**Fix direction (not binding).** Qualify both clauses as the docstring of `discarded_reasons` does: where the lines
under the item are not entries at one indent alone — the first line an entry at that indent and no plain line at
that indent or less — the whole is read as the text of one attempt, and it gives unknown unless it opens with
`reason: ` and one marker and holds no other. Bring the parenthesis of `audit_count.py:158-160` in line the same way
(its earlier parenthesis at `:152-153`, "the entries are read only as a list: ...", is already right).

Contradiction: yes — WAY-404 (an entry the change itself writes)

