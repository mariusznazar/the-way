FAIL d3068ed09017a0d0807c9e51d580ec3ba8b64589

# Review of the return step — range `47a47fecbeec3957b13bf7b34eb120f5b035e0b1..d3068ed`

One commit, `d3068ed` ("Bring WAY-403, WAY-404 and the record template in line with the final reading of
Discarded attempt"), five files. `git rev-parse HEAD` in the worktree is `d3068ed09017a0d0807c9e51d580ec3ba8b64589`,
the head given. Reviewed against the task (`task.md`, *To do* 3–6, *Questions to settle* 1–5, *Settlements to
record* rows 1–4), WAY-403, WAY-404, WAY-263, and the final code `process-audit/record_items.py` at `d3068ed`.

Counts: blocking 1 (Important), Minor 1, out of scope 0.

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

## Minor

### M-1 — WAY-403's *Verification* gives overlapping yes and unknown without saying which wins

**Place:** `foundations/decisions.md:7933-7936`. "yes where an entry carries the mark of a contradiction or the item
gives the marker `open design choice`, ... unknown where an entry carries no mark". A record with an unmarked fix
round and *Discarded attempt* `reason: `open design choice`` meets both clauses; `read_contradiction`
(`record_items.py:278-295`) gives yes, since it returns on a yes before it checks unmarked rounds, and the tests
hold the same order (`test_record_items.py:275-277`, `:290-292`). The overlap of the round clauses was there before;
this commit widened it with the clause of the marker. A short "a yes stands over an unknown" would remove the
reading that an unmarked round makes the whole answer unknown. Minor: *Verification* names tests, and the binding
sentence does not claim an order.

## Claims of the author's report checked

- Docstrings only in the two `.py` files: confirmed. The hunk of `process-audit/audit_count.py` lies within the
  module docstring (lines 1-323); the two hunks of `process-audit/record_items.py` are the module docstring
  (`:1-22`) and the docstring of `discarded_reasons` (`:243-251`); no line of code changed. The trust boundary
  (`record_items.py`, lines of records read from git history) is therefore not touched in behaviour.
- WAY-403 binding sentence and *Verification* (row 1, questions 1 and 2): the added "with the marker of a discarded
  attempt (WAY-404)" agrees with row 4 and the code (`read_contradiction` reads both items); the yes and no clauses
  agree with `record_items.py:278-296` (no for `none`, `reserved choice`, `size`; an empty *Review rounds* gives no
  vacuously). Says no more than rows 1 and 4. Apart from M-1, sound.
- WAY-404 *Verification*'s first part and the binding sentence's first part are unchanged; the added parts are I-1.
- `task-cycle/record_template.md:42-45` ("all at one indent with no other line at that indent"): agrees with the
  writer's form the code reads as a list.
- `process-audit/SKILL.md:223-224` ("in any of its entries, where it holds one for each discarded attempt"): agrees
  with `read_contradiction` (`OPEN_DESIGN_CHOICE in reasons`).
- `record_items.py` module docstring, parenthesis at `:13-14` ("a text of two markers, or a plain line or an entry
  at another indent beside the entries, gives no answer"): it stands inside the sentence on the form of several
  attempts and is followed by "any other text, with no marker at its start, gives no answer", so read in place it
  does not deny the one-attempt form; not a separate finding, but the fix of I-1 may align it.

## Declined to judge

- The narrowing of WAY-344 and the new paragraph of WAY-337: not changed in this range; the handoff names only
  WAY-403 and WAY-404 as corrected here.
- The Minor findings M-1, M-2, M-3 and O-1 of `reports/review-correction-report.md`: earlier review, left by the
  handoff of the return step.

## Checks

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit` — exit 0, `Ran 269 tests`, `OK` (262 s, run in the background).
- Scratch run `python -B .runs/review-return/probe.py` — exit 0; output quoted under I-1.
- `git diff 47a47fe..d3068ed`, `git log 47a47fe..d3068ed`, `git rev-parse HEAD` — read by hand; one commit, five
  files, head matches.
- Not run: the product's full gate (by the handoff).

## Reaches beyond the dispatch

- `process-audit/test_record_items.py:40-300` — to see which forms the tests citing WAY-403 and WAY-404 hold; the
  evidence of I-1 and M-1.
- `reports/correction-1-remarks.md` (named in the handoff) and a search of `reports/review-correction-report.md`,
  `review-correction-findings.md`, `review-correction-fix-report.md`, `author-correction-fix-report.md` for "plain
  line", "details as a list", "another indent" — to learn whether the one-attempt form with its details as a list
  was kept on purpose (it was: `review-correction-report.md:24-29`).
- `a private note of the author` — the user's rule read before writing the probe.

## Working copies

`.runs/review-return/` at `the root of the task's worktree\.runs\review-return\`
held the probe script and the output of the test run; removed before this return. Its content that the report
needs is quoted above. No worktree was made.

## Unread material

- `foundations/decisions.md`: WAY-403 and WAY-404 read whole; WAY-263, WAY-135, WAY-337, WAY-339 read as the task
  quotes them (*Decisions in play*), not whole from the foundation — none of them is changed by this range, and
  the grade of I-1 rests on the method's own paragraph on WAY-263.
- `reports/review-correction-report.md` and the other earlier reports: read only the passages found by the search
  above.

## Searches not found or unclear

none
