FAIL 17065c8b9b2349b4f5953ac98a15285e3d221787

# Review of correction 2 — audit-answers-contradiction-after-code

Range: `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6..17065c8b9b2349b4f5953ac98a15285e3d221787`, two commits
(`1fbb9cc4` remark 1, `17065c8b` remark 2), six files. `git rev-parse HEAD` in the worktree gives the
head named in the handoff. Method: `task-cycle/review/SKILL.md` with `task-cycle/review/fix.md` (a
correction for the human's remarks; the remarks in `reports/correction-2-remarks.md` take the place of
a findings file).

Counts: 2 blocking (Important), 1 Minor within the task, 0 out of scope.

## Remarks: made or not

- **Remark 1 — made.** "unless it reads `none` or opens with `reason: ` and one marker and holds no other"
  (or its equivalent) stands in the four places: WAY-405's binding sentence
  (`foundations/decisions.md:8115`), its *Verification* (`:8132`, "gives no attempt where it reads
  `none`"), `process-audit/audit_count.py:161-162` ("the whole text, which does not read `none`, ...")
  and `process-audit/record_items.py:14-15` ("which gives no attempt where it reads `none`"). It is true
  of the code: `discarded_reason` returns `NO_ATTEMPT` where `remarks_check.reads_none` (exact `none`,
  stripped of ` \t*_`.`) holds (probes E2 `none` under the empty item, E3 `none`, E4 `None.` beside the
  colon: `no`; E1 `none` beside the colon with a plain line under it: unknown, the whole not reading
  `none`). A search of the repository (`.runs/` apart) for `unless it opens with`, `opens with no
  marker`, `not entries at one indent`, `no entries at one indent`, `holds two markers`, `only the start
  of the item` and for `Discarded attempt` in every non-test file finds no other place with the old,
  wider sentence: `task-cycle/record_template.md:38-46` says what the writer writes;
  `process-audit/SKILL.md:225-231` says `unknown` where the item "gives no reason", true with `none`;
  `task-cycle/skill/SKILL.md:383,392`, `reserved_return.md:35`, `correction.md:44` say how to write a
  discard.
- **Remark 2 — partly made.** Of the seven shapes:
  1. second reason in a detail line of an entry (M-1): made — the rule says only the first line of an
     entry is read (`decisions.md:8119-8121`); true (probe F5, author's test). 
  2. second attempt with a malformed reason word (M-2): the way taken (rule follows code, answer `no`)
     is the one the human's words allow, but **the sentence that states it is not true of the code**:
     finding I-1.
  3. the docstring of `audit_count.py` (M-3): made, except its phrase "read for a second marker alone",
     part of I-1.
  4. N-1 (an earlier report's claim): nothing to change, confirmed — no file of the repository says "a
     first entry shallower ... gives unknown" (search for `shallower` and `first entry .*deeper`: no
     match; positive control `deeper than the entry` found `foundations/decisions.md`).
  5. WAY-404's overlap of yes and unknown (M-1 of the return review): made, but the new clause says more
     than the code: finding I-2.
  6. text beside the colon with entries under it (M-1 of the return-fix review): made
     (`decisions.md:8114`, `:8131`); true (probes G1, G2, G3 and the author's test).
  7. a line at the margin ends the item (O-1): made (`decisions.md:8121-8122`, the template's item,
     `item_texts`' docstring); true (probes F2, F3, H1: a fence line at the margin ends the item too, which
     "a line at the left margin" covers).
- **Remark 3 (the merge of `foundations`)** — not in this range; reviewed by another agent.

## Findings

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

### Minor

**M-1 (within the task, outside the correction's diff). WAY-405's *Verification* "an item of several
entries gives yes where any of them has the marker `open design choice`" is wider than the code for an
entry whose first line holds a second reason.** `foundations/decisions.md:8129-8130` (unchanged in this
range). An entry `- reason: \`open design choice\`; reason: \`size\`` beside `- reason: \`size\`` gives
unknown, "an entry ... opens with no marker of its reason" (probe D1): `discarded_reasons` maps an entry
of two reasons to None (`record_items.py:259-261`). The new binding sentence ("an entry that opens with
no marker gives the answer unknown unless another entry gives yes", `:8118-8119`) is silent on an entry
that opens with a marker and holds another; only `record_items.py:251-252` says it. The same clause
stood at `2e31b74b`, so by `fix.md` it is a note, not a reopening; it would close with the same edit as
I-1.

## Declined to judge

- The merge commit `2e31b74b` and remark 3 (the merge of `foundations`, PR #140): outside this range, reviewed by another agent per the handoff.

## Nothing widened, nothing lost

- Code unchanged: the syntax trees with docstrings left out of `process-audit/record_items.py` and
  `process-audit/audit_count.py` are equal at `2e31b74b` and at the head (`ast_eq.py`, both `True`).
- Tests only added: `git diff 2e31b74b 17065c8b -- process-audit/test_record_items.py
  process-audit/test_audit_count.py` has no removed line (125 insertions). The tests that held WAY-337,
  WAY-344, WAY-404 and WAY-405 stand unchanged and pass (checks below).
- No answer changes: 23 shaped records and 6 crafted ones give identical answers at the base and the
  head (probe output compared, timings apart).
- Trust boundary `process-audit/record_items.py`: crafted input — 3,000 lines each one space deeper,
  200 lines of 2,000 tabs, 100,000 entries cut by bare CRs, a line of 200,000 `reason: \``, 20,000
  doubled items, 100,000 lines of alternating indents — each read in under 0.4 s, no exception, and an
  answer of unknown or the plain `no` of entries of `size`; no new wrong yes or no (code unchanged).
- The new tests fail when the code behind them breaks (mutations of `record_items.py` in a copy of the
  base with the head's `test_record_items.py`; each restored, the five tests pass after): a margin line
  kept in the item → the margin test fails (4 subtests); a second reason never counted → the tests of
  items 1, 2 and 6 fail; text beside the colon ignored → the test of item 6 fails; the round's yes read
  after the item → the test of item 5 fails; `REASON_START` without the backtick → the test of item 2
  fails on `reason: open design choice` (the evidence of I-1).

## Checks

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`), in a worktree of the
  head — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle`, in a worktree of the head — exit 0, `Ran 534 tests`, `OK
  (skipped=2)`.
- `python -B gate/run_tests.py process-audit`, in a worktree of the head — exit 0, `Ran 276 tests in 502.382s`, `OK`.
- `python -B -I .runs/review-correction-2/probe.py <worktree> <out>` at head and base — exit 0 each; the
  answers quoted above (B1-B4, C1-C3, D1-D3, E1-E4, F1-F5, G1-G3, H1, six crafted); identical at both.
- `python -B -I .runs/review-correction-2/ast_eq.py base wt process-audit/record_items.py
  process-audit/audit_count.py` — exit 0, `True` for both.
- `python -B -I .runs/review-correction-2/mutate.py base mut.txt` — exit 0; five mutations each exit 1 in
  the named tests, restored run exit 0.
- Not run: the product's full gate (by the handoff); `ruff` (not part of the focused checks the handoff
  names).

## Reaches beyond the dispatch

- `task-cycle/remarks_check.py` (`reads_none`, `split_lines`, `indent_of`, `MARKER`): what reads as
  `none`, how lines are cut and indents counted, for the probes.
- `process-audit/SKILL.md:222-233`, `task-cycle/record_template.md:36-46`, and the `Discarded attempt`
  lines of `task-cycle/skill/SKILL.md`, `reserved_return.md`, `correction.md`: the search of remark 1.
- `reports/review-correction-report.md` (M-1, M-2, M-3, O-1) and `request.md` *Minor findings* /
  *Findings outside the task's scope*: the word-for-word shapes of remark 2.

## Working copies

Under `.runs/review-correction-2/`:
a detached worktree of the head (`wt`), a detached worktree of `2e31b74b` (`base`, where the head's
`test_record_items.py` was copied for the mutations), the scripts `probe.py`, `ast_eq.py`, `mutate.py`,
and the outputs `head.txt`, `base.txt`, `mut.txt`, `pa.log`, `tc.log`. Both worktrees removed with `git worktree remove --force` (exit 0
each), then `git worktree prune`, and the directory `.runs/review-correction-2/` deleted; `git worktree
list` names neither, and the reviewed worktree is clean. No remainder.
Nothing kept in `reports/`: the probe inputs and answers the findings need are quoted in them.

## Unread material

- `process-audit/audit_count.py`: read in the passage of its docstring (lines 140-170) and the diff, not
  whole; the change in it is docstring only (syntax trees equal).
- `process-audit/test_record_items.py` and `process-audit/test_audit_count.py`: read in the diff, not whole.
- `foundations/decisions.md`: WAY-404 and WAY-405 read whole; WAY-337 and WAY-344 not read (no sentence of
  either is in the range; their tests are unchanged and pass).
- The frozen task `task.md`: not read; the handoff carries what it settles for this review (the trust
  boundary answer).
- The reports `review-return-report.md`, `review-return-fix-report.md`, `review-correction-fix-report.md`:
  read through the word-for-word quotations in `request.md` *Minor findings*, not whole.

## Searches not found or unclear

- "a first entry shallower than the later ones gives unknown" and `shallower`: no file of the repository
  (`.runs/` apart) — as the author says.
- No other place in the repository with the old sentence of remark 1 (searches listed under Remark 1).
- Whether "the item gives the marker" in WAY-404 can be read as excluding a doubled item: unclear by its
  words; I took "whatever else the record holds" as including it (I-2).
