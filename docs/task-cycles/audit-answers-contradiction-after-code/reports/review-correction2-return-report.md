FAIL 9547acd470f7a05cba43193ab9bf4b2e56a12e22

# Review of the return step after correction 2 — audit-answers-contradiction-after-code

Range: `5a39a328346ad9a8d12e37732f52a86a164e3d17..9547acd470f7a05cba43193ab9bf4b2e56a12e22`, one commit
(`9547acd4`, "Bring the audit skill, the record template and two docstrings in line with how Q1 is
read"), four files: `process-audit/SKILL.md` +11/-6, `process-audit/audit_count.py` +3/-1 (docstring),
`process-audit/record_items.py` +3/-3 (docstring), `task-cycle/record_template.md` +1/-1. `git rev-parse
HEAD` in the reviewed worktree gives the head named in the handoff. Method: `task-cycle/review/SKILL.md`,
with `task-cycle/skill/return_step.md` for what the step compares and writes.

Counts: 1 blocking (Important), 2 Minor within the task, 0 out of scope.

## Findings

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

### Minor

**m-1 (within the task, in the diff). The commit carries the gap of M-1 and m-2 — an entry of a list of
attempts that holds a second `reason: ` followed by a backtick — into two new sentences, one of which
now names the second reason for the text of one attempt and not for an entry.** M-1 of
`reports/review-correction2-report.md` and m-2 of `reports/review-correction2-fix-report.md` are known;
the picture changes by these places:
- `process-audit/audit_count.py:157-158`: "opens with the marker `reserved choice` or `size` (each of
  its entries does, where it holds several)" — an entry `reason: \`size\`; reason: \`size\`` beside an
  entry `reason: \`size\`` opens with the marker; probe D2 gives `(None, 'an entry of the item
  \`Discarded attempt\` opens with no marker of its reason')`, not `no`.
- `process-audit/SKILL.md:230-235`: `no` "where ... *Discarded attempt* ... gives only the reasons
  `reserved choice` and `size`" (D2: it does; the code gives unknown), and the new list of what gives
  `unknown` — "a text or an entry with no reason at its start, or a text of one attempt that holds a
  second `reason: ` followed by a backtick" — names the second reason for a text and not for an entry,
  so a reader of the list takes D2 for `no`. The `yes` clause "(in any of its entries ...)" stood before
  this commit (M-1's shape, D1 → unknown).
The shape is rare and the earlier findings already send it to the request's list; the fix is one
clause with theirs: "or an entry that holds a second `reason: ` followed by a backtick" beside the
text's in both places.

**m-2 (within the task, in the diff). The template's new clause hangs under "since".**
`task-cycle/record_template.md:45-46`: "every line of the item stands indented under this line, since a
line at the left margin ends the item, and the text of one attempt holds no other `reason: ` followed by
a backtick". Read as written, the second clause is a second reason for the indent. Its meaning is clear
enough and the rule it states is true of the code (probe T1: a second `reason: \`size\`` in the text of
one attempt → unknown, "holds more than one reason"); a full stop or "; the text of one attempt holds
..." would set it apart.

## Sentences compared that hold

- WAY-337 (second paragraph, `foundations/decisions.md:7838-7842`): an entry `review ..., PASS` is no
  fix round and a round with no contradiction — probe N2 (`review` entry, entries `size` and `reserved
  choice`) → `no`; `round_of` gives it mark `no`, `review_rounds` gives it no file.
- WAY-344 (the record's narrowing, `:2929-2934`): a record without the item gives unknown with a
  reason naming it and no `Error:` — probe M2 (no *Discarded attempt*) → `(None, 'the record holds no
  item \`Discarded attempt\`')`; `rounds_item` names *Review rounds* likewise.
- WAY-405 (whole): beyond M-1, m-2 and m-1 above, as the review of the fix of correction 2 found; T1
  agrees with its "holds no second `reason: ` followed by a backtick".
- Part map, `process-audit`, *Trust boundary* (`foundations/part_map.md:134-135`): names both modules.
- The template's item *Review rounds* (`task-cycle/record_template.md:57-`): the two forms, `none`.
- SKILL.md's new `no` clause for *Review rounds*: probe N1 (`none` and `none`) → `no`, N2 → `no`.
- SKILL.md's save clause: R7 → `yes` over a doubled *Review rounds*; a doubled *Discarded attempt* with
  the marker gives unknown (the earlier review's probes C1, C2, C4, unchanged code).

## The return step's bounds

- No entry written, none proposed or listed for later (`reports/author-correction2-return-report.md`,
  *Entries written*: none; the diff touches no file of `foundations/`). No invariant written. No
  widening: four files, prose and docstrings.
- No executable line changed: the syntax trees with docstrings left out of
  `process-audit/record_items.py` and `process-audit/audit_count.py` are equal at `5a39a328` and
  `9547acd4` (both `True`). No probe of hostile input was needed at the trust boundary.
- The author's own-work check named WAY-11 for the skill and template and searched by `Discarded
  attempt`, `Review rounds`, `contradiction`; it compared the sentences with the *Discarded attempt* side
  of the code and missed the *Review rounds* side (I-1).
- Earlier open Minor findings: M-1 and m-2 — picture changed, m-1 above; m-1 of the fix review (long
  lines) — unchanged by this commit (`process-audit/audit_count.py:155` and `:163-165` untouched).

## Declined to judge

none

## Checks

All in a detached worktree of the head under `.runs/review-correction-2-return/`:
- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit` — exit 0, `Ran 276 tests in 661.651s`, `OK`.
- `python -B gate/run_tests.py task-cycle` — exit 0, `Ran 534 tests in 159.002s`, `OK (skipped=2)`.
- `python -B -I .runs/review-correction-2-return/probe.py wt base probe_out.txt` — exit 0: the syntax-tree
  comparison (`True`, `True`) and the probes R1-R7, D1-D3, N1-N2, T1, M1-M2 quoted above.
- Not run: the product's full gate (by the handoff).

## Reaches beyond the dispatch

- `.runs/task-cycles/audit-answers-contradiction-after-code/task.md`, *To do* points 3-4 (searched for
  `Review rounds`, `unknown`): whether the code's unknown for an entry in neither form is settled (it
  is, point 4), to say which side the fix of I-1 keeps.
- `reports/author-correction2-report.md` item 5: whether the round's yes over an unread *Review rounds*
  was raised before (it was not).
- `foundations/part_map.md:124-135` (the part `process-audit`), `foundations/decisions.md` WAY-337 and
  WAY-344 whole, WAY-404 and WAY-405 whole.

## Working copies

Under `.runs/review-correction-2-return/`:
detached worktrees `wt` (`9547acd4`) and `base` (`5a39a328`), the script `probe.py`, the outputs
`probe_out.txt`, `pa.log`, `tc.log`, and `line37.txt` (one line of an earlier report). Both worktrees
removed with `git worktree remove --force` (exit 0 each), then `git worktree prune`, and the directory
deleted (`Test-Path` gives `False`); `git worktree list` names neither, and the reviewed worktree is
clean. No remainder.
Nothing kept in `reports/`: the probe answers the findings need are quoted here.

## Unread material

- `process-audit/audit_count.py`: read in its Q1 docstring passage (lines 135-174) and the diff, not
  whole; no executable line changed.
- `process-audit/test_record_items.py`: read at lines 1-40 and 392-427 and by search, not whole.
- `task.md`: read at *To do* (lines 24-33) and by search, not whole.
- `process-audit/SKILL.md`: read at lines 205-249 (the matter of the version series), not whole.

## Searches not found or unclear

- A test that pairs a `contradiction yes` entry with a doubled or out-of-form *Review rounds*: none in
  `process-audit/test_record_items.py` (searched for `more than once`, `doubled`, `twice`, and read the
  test of the yes over an unknown).
- An earlier finding of the round's yes over an unread *Review rounds* in the cycle's reports: none
  (searched for `Review rounds` doubled, out of form, missing, `does not give its entries`).
