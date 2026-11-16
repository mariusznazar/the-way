FAIL 1d7d105ced9da2e7a03ea93b57640fe4d081810d

# Review of the fix of the return step — range `d3068ed09017a0d0807c9e51d580ec3ba8b64589..1d7d105`

One commit, `1d7d105` ("Say in WAY-404 what the code does with an item whose lines are no entries at one indent
alone"), three files: `foundations/decisions.md`, `process-audit/audit_count.py`, `process-audit/record_items.py`.
`git rev-parse HEAD` in the worktree is `1d7d105ced9da2e7a03ea93b57640fe4d081810d`, the head given. Reviewed with
`task-cycle/review/SKILL.md` and `task-cycle/review/fix.md`, bounded by `reports/review-return-findings.md` (I-1).

Counts: blocking 1 (a new Important finding in the fix, which counts as one that remains, WAY-162), Minor 1, out of
scope 0.

## The findings of the findings file

### I-1 — fixed

The broad clause ("and so does an item that holds two markers outside a list of entries, or a plain line or an
entry at another indent beside its entries") is gone from WAY-404's binding sentence (`foundations/decisions.md:7966-7969`),
its *Verification* (`:7977-7980`), `process-audit/audit_count.py:159-160` and `process-audit/record_items.py:13-14`.
Each now says that an item whose lines are not entries at one indent alone is read as the text of one attempt. The
three forms of the finding's evidence agree with the new wording, and the probe at `1d7d105` gives the same answers
as at `d3068ed`. A plain first line with a marker and its details as entries gives `('yes', None)`, and the
sentence says it gives its reason. An entry deeper than the first entry after it gives `('no', None)`. The
sentence's dash, "the first line an entry at that indent and no plain line at that indent or less", lets a deeper
entry through, so it describes that answer too. The tests that cite WAY-404 (`process-audit/test_record_items.py:142`,
`:153`, `:171`, `:197`, `:191`, `:210`) agree. The start that tests cite by a line `decision:`, "The audit of the
process takes from this item, for its answer whether", is unchanged, and the foundation check passes with test
citations.

The new wording drops one case of the code, and that is a new Important finding (N-1 below). Under fix.md and
WAY-162 it counts as a finding that remains, so the review fails even though I-1 itself is fixed.

## New in the fix

### N-1 (Important) — the new clause makes an item that reads `none` on the line under it give unknown; the code gives no

**Place:** `foundations/decisions.md:7966-7969`, WAY-404's binding sentence. It now reads: "Where the lines under the
item are not entries at one indent alone — the first line an entry at that indent and no plain line at that indent
or less — the whole is read as the text of one attempt, and gives the answer unknown unless it opens with `reason: `
and one marker and holds no other (WAY-403)." Its *Verification* (`:7977-7980`) says the same: "which gives unknown
where it holds two markers or opens with no marker". The same omission is in both changed docstrings.
`process-audit/audit_count.py:159-160` lists, among the reasons of unknown, "where its lines are no entries at one
indent alone and the whole text holds two markers or opens with no marker". `process-audit/record_items.py:13-14`
says the whole text "gives no answer where it holds two markers or opens with no marker".

**What is wrong.** The code reads the whole text with `discarded_reason` (`process-audit/record_items.py:256`, `:210-221`).
It returns `NO_ATTEMPT` first where the text reads `none` (`remarks_check.reads_none`), so `discarded_reasons` gives
`['none']` and `read_contradiction` gives `no`. The new sentence's "unless" leaves `none` out. An item that reads
`none` as a plain line under its heading is a case of "lines under the item that are not entries", and it opens with
no marker. Read as written, the sentence says it gives unknown. The code gives no. The same follows from the
sentence for the commonest form of all, `- Discarded attempt: none` with no lines under it, if "the lines under the
item are not entries at one indent alone" is read as holding where there are no lines under the item. The
`audit_count.py` docstring shows that the qualification was known. The clause just before the new one says "where
*Discarded attempt* opens with no marker and does not read `none`", and the new clause drops "and does not read
`none`".

**Evidence.** Probe at `1d7d105` (`.runs/review-return-fix/probe.py`, calling `record_items.read_contradiction` on the
item and `- Review rounds: none`):
- `- Discarded attempt:` / `  none` -> `('no', None)`
- `- Discarded attempt:` / `  None.` -> `('no', None)`
- `- Discarded attempt: none` -> `('no', None)`. The test `process-audit/test_record_items.py:47-58` also asserts
  `("none", "no")` and `("None.", "no")` and cites WAY-404 by a line `decision:`.

**Why it matters.** This is the same class as I-1. Under WAY-263, the entry the change writes restates the code
"without a qualification". A change that brought the code in line with WAY-404 as now written would make an item
reading `none` under its heading answer unknown, a false unknown in the one measure this task exists to fill. The
fix's own-work check searched for the old broad wording and read the hits against the code. It did not test the
new sentence against the `none` path of `discarded_reason`.

**Fix direction (not binding).** Make it "gives the answer unknown unless it reads `none` or opens with `reason: ` and
one marker and holds no other". Apply the same to *Verification* ("gives no attempt where it reads `none`") and to
the two docstrings ("and does not read `none`").

Contradiction: yes — WAY-404 (an entry the change itself writes)

## Minor

### M-1 — WAY-404 no longer says what happens to an item with text on its own line and entries under it

**Place:** `foundations/decisions.md:7966-7969`. The code reads the item as a list only where nothing stands beside
its colon (`record_items.py:253`, `not rest.strip()`). Otherwise the whole text is one attempt, even where the lines
under the item are entries at one indent alone. So `- Discarded attempt: reason: `size`` with an entry
`- reason: `open design choice`` under it gives unknown with the reason of two markers. The probe confirms it, and
`test_record_items.py:204-209` asserts it. Before the fix this was covered by "two markers outside a list of
entries". The new sentence covers only items whose lines under them are not entries at one indent alone, so this
case is now silent. The first sentence's "or, where the cycle discarded more than one attempt, at the start of each
entry under the item" might lead a reader to read the entry's `open design choice` as a yes. Minor because the entry
is silent here, not wider than the code, and the template already says "nothing after the colon" for several
attempts. Adding "or where text stands beside the colon" to the condition would close it.

## Claims of the author's report checked

- Docstrings only in the two `.py` files: confirmed. The hunk of `audit_count.py` (`:156-161`) lies within the module
  docstring (lines 1-323), and the hunk of `record_items.py` (`:10-14`) lies within the module docstring (lines
  1-22). No line of code changed, so behaviour at the trust boundary (`record_items.py`) is unchanged.
- "No file keeps the broad wording": confirmed for the old phrases. The new phrases carry N-1.
- "The three probes of the finding give the answers the sentence now says": confirmed (see I-1).
- "I changed no test": confirmed. The diff touches no test file.
- Nothing the human did not accept: the new sentence describes the reading the cycle's correction kept and the
  review of the correction judged sound (`reports/review-correction-report.md:24-29`). It adds no behaviour beyond
  the N-1 omission.

## Declined to judge

- M-1 of `reports/review-return-report.md` (WAY-403's *Verification* and the precedence of yes): left out of the fix
  by the findings file.

## Checks

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit` — exit 0, `Ran 269 tests`, `OK` (333 s, in the background).
- Scratch run `python -B .runs/review-return-fix/probe.py` — exit 0. It gave `('no', None)` for the three `none`
  items, unknown with the two-markers reason for a marker on the item line beside an entry with another marker,
  `('no', None)` for a marker on the item line with details as entries, `('yes', None)` for a plain first line
  with a marker and its details as entries, and `('no', None)` for an entry deeper than the first.
- `git diff d3068ed..1d7d105`, `git log d3068ed..1d7d105`, `git rev-parse HEAD` — read by hand: one commit, three
  files, head matches.
- Not run: the product's full gate (by the handoff).

## Reaches beyond the dispatch

- `task-cycle/remarks_check.py:142-143` (`reads_none`) — to learn which texts read as `none`; the evidence of N-1.
- `process-audit/test_record_items.py:1-300` — the tests that cite WAY-404, to judge the new sentence against them.
- `process-audit/record_items.py:203-296` at `1d7d105` — the reading the sentence restates.

## Working copies

`.runs/review-return-fix/` at
`the root of the task's worktree\.runs\review-return-fix\` held the probe script
and the output of the test run. It was removed before this return, and what the report needs is quoted above. No
worktree was made.

## Unread material

none — the findings file, the fix report, the diff and WAY-404 were read whole. The earlier reports of the cycle
were read only in the passages cited.

## Searches not found or unclear

none
