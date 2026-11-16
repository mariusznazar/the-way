PASS 702525993aa85c5baa4cd239c64e0296e8d12948

# Review of the renumbering commit and of the second merge of the target branch (correction 2)

Reviewer: a fresh `the-way-stage` reviewer, method `task-cycle/review/SKILL.md` (`review-change`),
dispatched by `reports/review-merge2-handoff.md`.

Range, base `f5100d78` (the code the earlier reviews of correction 2 accepted):

1. `7957e5d0f68404095ea763e079dc6826c477c46d`: the renumbering, judged by `git diff f5100d78 7957e5d0`;
2. `702525993aa85c5baa4cd239c64e0296e8d12948`: the merge of `origin/foundations` at
   `3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898`, judged by `git diff 7957e5d0 70252599` and
   `git diff 30c947f...3cbaeb9f`.

`git rev-parse HEAD` in the reviewed worktree: `702525993aa85c5baa4cd239c64e0296e8d12948`, the head given.
The merge's parents are `7957e5d0` and `3cbaeb9f`; the merge base of the two is `30c947f`.

## Findings

Counts: 0 blocking, 0 Minor, 0 out of scope.

No Critical, Important or Minor finding.

### What was checked, with evidence

**The renumbering pass (`7957e5d0`) applied the map 403 → 404, 404 → 405 once, to whole numbers.**

- The commit changes 9 files, 40 lines added and 40 removed, all of them in the files the handoff lists:
  `foundations/decisions.md`, `process-audit/audit_count.py`, `process-audit/record_items.py`,
  `process-audit/test_audit_count.py`, `process-audit/test_record_items.py`, `task-cycle/review/SKILL.md`,
  `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/reserved_return.md`.
  No other file changed in that commit.
- `git diff --word-diff=porcelain f5100d78 7957e5d0`: every removed word is a `WAY-403` or `WAY-404`
  token and every added word the same token with the new number, with the same punctuation around it. Removed
  `WAY-403` tokens: 15; added `WAY-404` tokens: 15. Removed `WAY-404` tokens: 27; added `WAY-405`
  tokens: 27. No other word changed.
- By file, the old numbers at the lines of `git diff -U0 f5100d78 7957e5d0`: `foundations/decisions.md`
  4 (lines 7842, 8061, 8120, 8131) and 2 (8069, 8108); `audit_count.py` 1 and 1; `record_items.py` 1 and 1;
  `test_audit_count.py` 2 (3811, 3829) and 5 (3730, 3744, 3763, 3769, 3770); `test_record_items.py` 5
  and 14; `review/SKILL.md` 1 and 0; `skill/SKILL.md` 1 (235) and 2 (385, 394); `correction.md` 0 and 1;
  `reserved_return.md` 0 and 1. This agrees with the handoff's counts.
- Totals by `git grep -c -w` per commit: at `f5100d78` WAY-403 15, WAY-404 27, WAY-405 0; at `7957e5d0`
  WAY-403 0, WAY-404 15, WAY-405 27; at `30c947f` (merge base) and at `3cbaeb9f`, no WAY-404 or WAY-405;
  at `3cbaeb9f` WAY-403 5 (the target's own); at `70252599` WAY-403 5, WAY-404 15, WAY-405 27,
  WAY-406 0. So no reference was lost or doubled, and the target's 5 references to its WAY-403 stand
  as the target wrote them.
- The new numbers are the next free ones the target's rule gives: the target's log at `3cbaeb9f` has its
  highest entry at WAY-403 and its list of withdrawn identifiers (`foundations/decisions.md`,
  "## Withdrawn identifiers", line 10775 at the head) ends at WAY-371; so 404 and 405 are correct, in the
  order of the old numbers.

**No number of a decision of the target branch was changed.** The merge base `30c947f` holds no
WAY-403..406 at all, so every number the pass rewrote was the task's own; `git diff 3cbaeb9f 70252599`
shows the same 12 files and line counts as `git diff 30c947f 7957e5d0`, i.e. the merge left the target's
side as the target wrote it.

**The numbers agree within and around the two renumbered decisions** (head, `foundations/decisions.md`):

- WAY-404 (heading line 8152, "Who marks a contradiction with the settlements…"): *Based on* `none`,
  *Relations* `derives from WAY-135 · derives from WAY-339`; its prose names the marker of a discarded
  attempt as WAY-405 (line 8160), which is that decision.
- WAY-405 (heading line 8199, "How does the audit of the process read the reason of a discarded
  attempt?"): *Based on* `none`, *Relations* `derives from WAY-135 · derives from WAY-404` (line 8222);
  its prose cites WAY-404 for the reading of the second `reason: ` (line 8211).
- The new paragraph of the decision at line ~7930 (the review that passed with no fix) cites WAY-404
  for "a round with no contradiction with the settlements" (line 7933), which is WAY-404's subject.
- The `decision:` lines of the tests: those citing WAY-404 quote "The cycle writes the mark into the
  entry of the round in the record's item", which stands in WAY-404; those citing WAY-405 quote "The
  reason of a discarded attempt stands at the start of the record's item", "The audit of the process
  takes from this item, for its answer whether", "Where the lines are entries at one indent alone and
  nothing stands beside the colon", "Where the lines under the item are not entries at one indent
  alone" and "The item reads down to the next line at the left margin", each of which stands in WAY-405.
  `foundation_check.py` without `--skip-test-citations` confirms these citations (0 errors).
- The `tests:` clauses of the two decisions name no decision number, so nothing there to rewrite.
- The skill texts: `task-cycle/review/SKILL.md:162` and `task-cycle/skill/SKILL.md:235` cite WAY-404 for
  the mark of contradiction; `task-cycle/skill/SKILL.md:385` and `:394`, `task-cycle/skill/correction.md:50`
  and `task-cycle/skill/reserved_return.md:37` cite WAY-405 for the reason under *Discarded attempt*;
  `process-audit/audit_count.py:147` and `process-audit/record_items.py:8` cite both. Each points to the
  decision that carries the rule it cites.
- Headings at the head: `### WAY-403` (line 6243, the target's), `### WAY-404` (8152) and `### WAY-405`
  (8199), each once; `foundation_check.py` reports 0 errors, so no duplicate number.

**The merge (`70252599`) is the clean automatic merge.** `git merge-tree --write-tree 7957e5d0 3cbaeb9f`
gives the tree `68a30f5be3a08de788d9e203d72daa7abc92d6e7`, the same as `70252599^{tree}`: the merge
commit holds no hand resolution and no change beyond what the two sides brought.

**Do the two sides still hold together?** Yes, by the entries and files below.

Foundation entries the merge brought in, from `git diff 30c947f 3cbaeb9f -- foundations/decisions.md`,
that bear on the parts the change touches (`process-audit`, `task-cycle`, the decision log):

- **WAY-403** (new, target's; Scope decisions, task-cycle; derives from WAY-19 and WAY-02): a task
  renumbers its new decisions in a commit of its own before the merge, onto the next free numbers after
  the highest of the target's log, entry or withdrawn, in one pass, never touching the target's numbers,
  and records the map in the row of the reconciliation. The range does exactly that: a separate commit
  `7957e5d0` before the merge, the map 403 → 404, 404 → 405, the target's numbers untouched, and the row
  of the second reconciliation in `cycle.md` (line 105) gives the map "**403 → 404, 404 → 405**".
- **WAY-71** (changed by PR #141): a decision's *Relations* may now hold
  `TODO — <the decision, and where it is expected>`, and `foundation_check.py` checks the decisions
  named in *Relations* as references. The task's WAY-404 and WAY-405 hold no `TODO` in *Relations*;
  their related decisions (WAY-135, WAY-339, WAY-404) exist, which the check now verifies (0 errors).
- **WAY-126** (changed by PR #141): a change that writes a projected entry replaces the descriptive
  `TODO` that points at it. The task writes no projected entry (both *Origin* `none`); does not bear.
- **WAY-287** (changed by PR #141): the request lists each descriptive `TODO` of a decision's *Relations*
  too. The task's decisions hold none, so the request gains no item from them.
- **WAY-19** and **WAY-02** (not changed; named by WAY-403 as its ground): new decisions take the next free
  numbers; a reference names an entry by its number alone. The renumbered references are numbers alone.
- **WAY-160**: not touched by `git diff 30c947f 3cbaeb9f -- foundations/decisions.md`; the merge brought no
  change to it, and no sentence of the range bears on it.
- `foundations/environment_facts.md` (`foundations-branch-ruleset`, a second required check
  `tests-windows`): bears on no part the task touches.

What the target's checks and template ask of a decision, and the task's decisions against it:

- `elements/decisions/template.md` at the head: the fields *Scope*, *Based on*, *Relations*,
  *Verification*, *Origin*, then *Rationale* and *Rejected*; *Relations* `derives from WAY-x · …` |
  `TODO — …` | `none`. WAY-404 and WAY-405 carry every field, in that order, with values the template
  allows; `foundation_check.py` (which reports a missing field, a word a field does not take, a bare
  `TODO` or `derives from TODO` in *Relations*, and a dead reference in *Relations*) reports 0 errors.

The task's sentences and the target's sentences in the three files the handoff names:

- `task-cycle/skill/SKILL.md`: the task's sentences (lines 226–235 on the mark of contradiction in the
  findings file and the round's entry; 380–394 on *Discarded attempt*) sit in "Design and execution
  choice" and in the dispatch of fixes; the target's (step 12, lines ~588–594, and the new section "The
  renumbering of the task's decisions", ~686–722) sit in "Request and handoff". The target's step 12 has
  the merge reviewed "and the renumbering commit with it"; the task's record template gives that review
  an entry in *Review rounds* in either form (`findings …, contradiction yes|no` when it blocked,
  `review …, PASS` when it passed). No sentence of one side says what the other forbids.
- `task-cycle/skill/correction.md`: the target's changes are in the opening paragraphs (lines 8–12 and
  29–37, renumber before the merge, the renumbering commit in the reviewer's range); the task's is the
  sentence on *Discarded attempt* (lines 46–50). Read whole up to line 60 at the head: they read as one
  sequence (renumber, merge, review the merge; then the correction, whose discarded attempt is written
  with its marker).
- `task-cycle/record_template.md`: the target adds to the paragraph on events that the row of the
  reconciliation gives the map of old to new numbers; the task changed the items *Discarded attempt* and
  *Review rounds*. The audit's readers (`process-audit/record_items.py`, `audit_count.py`) read those two
  items and the lines `Process pin` and `Target branch and base`, not the rows of *Events* as numbers;
  the new sentence changes no form that they read (search: `record_template|Events` in
  `process-audit/*.py`).

**Tests.** The renumbering changes only the numbers in the `decision:` comments of the tests; no
assertion or input changed, so what the tests protect is unchanged. No invariant test changed in the
range on the task's side; the target's `elements/common/test_foundation_check.py` changed with its own
PR and passes on the merged tree.

## Declined to judge

- The rewrite of the original of the record under `.runs/task-cycles/audit-answers-contradiction-after-code/`
  (the row in `cycle.md` claims 129 references to WAY-403 and 200 to WAY-404 in 53 text files before
  the pass): the record is no code and, as WAY-403's own *Rationale* states, no reviewer of the merge checks
  its rewrite; I read only the row of the reconciliation (line 105) and the references to WAY-404/405 in
  `cycle.md`, which point to the right decisions in the lines I read (31–33, 59–102, 149–158).
- The target's own changes (PR #141, PR #142) on their own merits: reviewed in their own requests; I
  judged them only where they meet the task's change.

## Checks

All in a detached worktree of `70252599` at
`.runs/review-merge-2/wt`.

- `python -B gate/run_tests.py process-audit` — exit 0 (Ran 276 tests, OK).
- `python -B gate/run_tests.py task-cycle` — exit 0 (Ran 534 tests, OK, skipped=2).
- `python -B gate/run_tests.py elements` — exit 1, "no test found in elements": the runner discovers
  from the given directory and the tests of `elements/` lie in its subdirectories. Replaced by:
  - `python -B gate/run_tests.py elements/common` — exit 0 (Ran 257 tests, OK); this is the directory
    the merge changed (`foundation_check.py`, `test_foundation_check.py`, `rules.md`).
  - `python -B gate/run_tests.py elements/part-map` — exit 0 (Ran 40 tests, OK); the only other test
    directory under `elements/`.
- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- Other directories the merge changed that hold tests: `foundations/` holds no test file;
  `elements/decisions/` holds none; `task-cycle/` ran above.
- Manual: `git merge-tree --write-tree 7957e5d0 3cbaeb9f` against `git rev-parse 70252599^{tree}`
  (equal, `68a30f5b…`); word-level diff of the renumbering with token counts; `git grep -c -w` of
  WAY-403..406 at `f5100d78`, `7957e5d0`, `30c947f`, `3cbaeb9f`, `70252599`.
- The product's full gate: not run, as the handoff orders.

## Reaches beyond the dispatch

- `foundations/decisions.md`, the table "## Withdrawn identifiers" (from line 10775 at the head): to verify
  that the next free numbers after the target's log are 404 and 405 (highest withdrawn WAY-371).
- `foundations/decisions.md` lines 6243–6300 at the head: the target's WAY-403 whole, to compare the pass
  with it.
- `process-audit/*.py`, a search for `record_template|Events`: to check that the target's new sentence on
  the row of the reconciliation changes nothing the audit reads.
- `gate/run_tests.py`, a search for `no test found|discover`: to understand the exit 1 of `elements`.
- `.runs/task-cycles/audit-answers-contradiction-after-code/cycle.md` line 105 and a search for
  WAY-403..406 in it and in `task.md`: to compare the recorded map with the pass.

## Working copies

- A detached worktree of `70252599` at
  `.runs/review-merge-2/wt`, and the
  logs of the checks beside it in `.runs\review-merge-2\`: removed with `git worktree remove --force`,
  then `git worktree prune`, and the directory `.runs\review-merge-2\` deleted. A copy of the target's
  `foundations/decisions.md` written briefly into `.runs\review-merge-2\` (and, for a moment, as
  `.runs\review-merge-2-target-decisions.tmp`) was deleted before the checks. Nothing is kept in
  `reports/` beyond this report.

## Unread material

- `foundations/decisions.md`: read as the range's diffs, the target's diff of it, WAY-403 (target) whole,
  WAY-404 and WAY-405 whole (in the diff `30c947f..7957e5d0`), the diffs of WAY-71, WAY-126 and WAY-287;
  WAY-19, WAY-02 and WAY-160 not opened whole, since the merge did not change them and the range touches
  nothing they rule beyond what WAY-403 names them for.
- `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`: read as the diffs of both sides, not whole.
- `.runs/task-cycles/audit-answers-contradiction-after-code/task.md`: searched, not read whole.

## Searches not found or unclear

- The handoff says the frozen task refers to the decisions by the numbers of the pass: `task.md` holds no
  reference to WAY-403, WAY-404 or WAY-405 (`grep -c -w` gives 0); it names the decisions by the rows of
  its *Settlements to record*. Nothing in it needed renumbering, so this is no gap of the pass.
- `python -B gate/run_tests.py elements`, as the handoff gives it, finds no test (exit 1); the
  subdirectories were run instead.
