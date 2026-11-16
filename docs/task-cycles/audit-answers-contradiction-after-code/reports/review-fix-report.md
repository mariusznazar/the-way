FAIL 428cc4553042992c6a9813e7dd0a9ef11f0e2ea1

# Review of the fix — audit-answers-contradiction-after-code

- Range: base `ab2c8c801b2ba9170a00ed6056b8b7c56b062868` to head
  `428cc4553042992c6a9813e7dd0a9ef11f0e2ea1`, one commit (`git rev-parse HEAD` in the reviewed worktree
  gives the head). Method: `review-change` with `task-cycle/review/fix.md`; the findings file
  `reports/review-whole-findings.md` bounds the review.
- Counts: 1 blocking (a new Important finding in the fix, which counts as one that remains, WAY-162),
  1 Minor (new in the fix), 0 out of scope. Of the findings file: I-1 fixed, M-1 fixed, M-2 fixed.

## The findings of the findings file

### I-1 — fixed

WAY-344 gains, in place, the sentence "Where the command that counts the audit reads a cycle's record
that lacks a line or an item it reads of it — the line `Process pin` or `Target branch and base`, or
the item `Process remarks on the-way`, `Discarded attempt`, `Review rounds`, `Plan` or `Slices returned
too large` — the record is of an earlier form and no field is missing: the command gives the values
that need it as unknown, with a reason that names the line or the item, no line `Error:` and no change
of the exit code" (`foundations/decisions.md:2877-2882`), a `tests:` clause in its *Verification*
(`:2901-2904`) and a sentence of *Rationale* (`:2945-2948`). Checked:

- It states what the code does. The readers of the record in the code are exactly these seven:
  `process_pin` reads `Process pin` and, for the-way's own cycles, `Target branch and base`
  (`process-audit/audit_count.py:752`, `:766`); `remarks_count` the item *Process remarks on the-way*
  (`:778-782`); `read_contradiction` and `read_rounds` *Discarded attempt* and *Review rounds*
  (`process-audit/record_items.py`); `read_plan` and `read_too_large` *Plan* and *Slices returned too
  large* (`audit_count.py:1141`, `:1159`). No other label of `cycle.md` is read. Each missing one gives
  `unknown` with a reason that names it and puts nothing on the cycle's missing fields, so no `Error:`
  line and no change of exit code.
- The test that cites it, `test_audit_count.ProcessPin.test_a_record_that_lacks_every_line_and_item_the_count_reads_is_of_an_earlier_form`
  (`process-audit/test_audit_count.py:412`), runs the command on a record with none of the lines and
  items and asserts exit code 0, no `Error:` and a reason naming six of the seven; *Review rounds* is not
  asserted there (Q1 stops at the missing *Discarded attempt*), but
  `test_a_record_without_the_item_discarded_attempt_or_review_rounds_gives_q1_unknown` and
  `test_record_items.FixRounds.test_a_record_without_the_item_gives_none_with_its_reason` hold it, so
  the decision's reading as a whole is held.
- WAY-344 and its dependants agree: WAY-294 narrows it for the reports of the remarks script and is not
  touched; the guidelines that point to it (`guidelines/coding.md:108-114`,
  `coding-measuring-report.md:36`, `coding-generator.md:38`) restate nothing narrowed; the docstring of
  `audit_count.py` ("A value a record ... does not give — an earlier form, a missing ... line ... — is
  `unknown`") and `process-audit/SKILL.md:182-186` say the same. The route is WAY-30's: the narrowing is
  a proposal on the task branch, which the merge leaves to the human; the orchestrator's marking of it
  as `the cycle's` in the request is outside this diff.

### M-1 — fixed

The template (`task-cycle/record_template.md:42-44`), the two paragraphs of `task-cycle/skill/SKILL.md`
(`:376-377`, `:384-385`), `task-cycle/skill/reserved_return.md:35-37`, `task-cycle/skill/correction.md:43-45`
and WAY-404 give one entry for each discarded attempt; the count reads `yes` where any entry's marker is
`open design choice` and gives two markers in one text a reason of its own, not the false "no marker".
Markers only, read at the start of each entry: *To do* 3 and 6 and question 5 hold. But the reading
that carries it adds a wrong answer — I-2 below.

### M-2 — fixed

WAY-404 reads "an item that reads neither `none` nor a marker, written in any earlier form, gives the
answer unknown" (`foundations/decisions.md:7963-7965`).

## New findings in the fix

### Important

**I-2. A record whose first discarded attempt stands on a line under the item and whose second is
added as an entry gives Q1 `no`, though it holds the marker `open design choice`.**

- Place: `process-audit/record_items.py` `discarded_entries` and `discarded_reasons` (the branch `if
  entries and not rest.strip()`): when the item's line is empty and any list entry stands under it,
  only the list entries are read, and every other line under the item — the text of the one-attempt
  form — is passed over in silence.
- Evidence (my probe at the head, script in my working directory, removed):
  ```
  - Discarded attempt:
    reason: `open design choice`; 10:32, report reports/x.md
    - reason: `size`; 14:05
  - Review rounds: none
  ```
  gives `('no', None)`. At `ab2c8c8` the same text gave `unknown` (two markers). Without the entry line
  it gives `('yes', None)`.
- Why it matters: this is the record a leader most plausibly writes for two discards. The one-attempt
  form with its text on the line under an empty item is a form the count reads and tests
  (`test_record_items.DiscardedAttemptReason.test_the_marker_on_the_line_under_an_empty_item_is_read`);
  for the second discard the skill now says "an entry of its own where the cycle discarded an attempt
  before" (`task-cycle/skill/SKILL.md:384-385`), not that the first text is to be rewritten as an entry
  (only the template says "one entry for each attempt"). The result is a false `no` for a cycle that had
  an open design choice — the answer on which the human weighs whether the cycle needed a spec, and the
  kind of false answer WAY-404 exists to remove. The code treats the same mixture inconsistently: text
  on the item's own line beside entries gives `unknown` ("holds more than one reason in a form that is
  not read"), text one line lower gives `no`.
- The same branch also changes an old answer the other way: an item whose text opens on the line under
  it and whose details follow as a list (`- Discarded attempt:` / `  reason: `open design choice`;
  10:32` / `  - report reports/x.md`) gave `yes` at `ab2c8c8` and now gives `unknown` ("an entry ...
  opens with no marker"), since the detail lines are taken for entries. Safe, but a form the earlier
  reading accepted is lost.
- Fix: read the entries form only where every non-blank line under the item at the entries' indent,
  outside fences, is a list entry; where a plain line stands beside entries, give `unknown` with the
  reason for text beside entries (as on the item's line), or read the whole as the one-attempt text,
  which gives `unknown` for two markers and keeps the details-as-a-list form. A test with each of the
  two records above.
- Contradiction: yes — WAY-404 (the reason "stands at the start of the record's item" and the audit
  takes "the markers alone"; here a marker at the start of the item's text is not read) and the task's
  *To do* 3 (`yes` where *Discarded attempt* has the marker `open design choice`).

### Minor

**N-1 (within the task). The paragraphs that write a second discarded attempt do not say that the first
becomes an entry.** `task-cycle/skill/SKILL.md:376-377`, `:384-385`,
`task-cycle/skill/reserved_return.md:36-37`, `task-cycle/skill/correction.md:43-45` say "an entry of its
own where the cycle discarded an attempt before" or "an entry beside the earlier ones"; only
`task-cycle/record_template.md:42-44` says that the item then holds nothing after the colon and one entry
for each attempt. A leader that reads the paragraph and adds an entry under a first attempt written on
the item's line gets `unknown` (`holds more than one reason in a form that is not read`). Wording: "and
the earlier attempt rewritten as an entry, as the template gives". With I-2 fixed this costs an
`unknown`, not a wrong answer.

## Declined to judge

none

## Checks run

- `python -B gate/run_tests.py process-audit`, worktree of the head — exit 0, 262 tests. They pass
  with I-2 in the code: no test gives a plain line beside entries under the item.
- `python -B gate/run_tests.py task-cycle`, worktree of the head — exit 0, 534 tests, 1 skipped.
- `python -B elements/common/foundation_check.py`, worktree of the head — exit 0, `0 errors`.
- Manual: crafted input at the new reading (my probes against `record_items.read_contradiction` at the
  head): numbered and `*` entries, an entry reading `none`, entries at mixed indents, control
  characters in an entry, 200,000 entries (0.36 s), 20,000 entries of 50 markers each (0.16 s), a fenced
  or deeper entry, text beside entries on the item's line and under it. No hang, no crash, every reason
  a fixed string; one wrong answer, I-2.
- Manual: the list of readers of `cycle.md` in `audit_count.py` and `record_items.py` against the
  narrowing of WAY-344 (search of `header_fields(`, `item_texts(` and the item constants).
- Not run: the product's full gate, by the handoff (WAY-160).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-294 (its binding sentence) and the lines that name WAY-344
  (`:7090-7139`, `:7871`, `:10035-10037`, `:10135-10143`) — whether the dependants of WAY-344 still agree.
- `guidelines/coding-generator.md:38` — a pointer to WAY-344.
- `process-audit/audit_count.py:745-805` (`process_pin`, `remarks_count`) and the test helper `record`
  (`process-audit/test_audit_count.py:60-67`) — to check the list of the narrowing and its test.
- The text of `process-audit/record_items.py` at `ab2c8c8` — for the answers before the fix.

## Working copies

A worktree of the head at
`.runs/review-fix/head`, and scripts,
probe outputs and test outputs in `.runs/review-fix/`.
The worktree was removed with `git worktree remove --force` (exit 0), then `git worktree prune`, and the
directory `.runs/review-fix/` was deleted; `git worktree list` names it no more and the reviewed
worktree is clean. Nothing is kept in `reports/`: the probe's input and output stand in I-2. No
remainder.

## Unread material

- `foundations/decisions.md`: WAY-344 and WAY-404 read whole at the head; WAY-294 by its binding
  sentence and the lines naming WAY-344, not whole; WAY-30, WAY-162 read whole in the review of the whole
  change, not again.
- `process-audit/test_audit_count.py`: the diff of the fix and the helpers it uses, not whole.
- Nothing else of the dispatch left unread.

## Searches not found or unclear

- The skill's paragraphs say "an entry of its own" for a second discarded attempt but not what becomes of
  the first (N-1).
