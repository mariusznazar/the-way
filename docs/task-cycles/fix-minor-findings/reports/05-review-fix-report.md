PASS a2a4b83a8acd1419261ecfbeb8a632fe733ba488

# Review of the fix of the four Minor findings

Range: base `820f963` (the head the whole change was reviewed at), head `a2a4b83`; `git rev-parse HEAD` confirmed
as `a2a4b83a8acd1419261ecfbeb8a632fe733ba488`. Computed myself with `git diff 820f963..a2a4b83` (two files:
`foundations/decisions.md`, `task-cycle/skill/SKILL.md`). This is the review of a fix whose findings file holds
Minor findings alone, so only a new Critical or Important finding fails it (`task-cycle/review/fix.md`, WAY-162).

## Each finding of the findings file

1. WAY-289 Rationale and *Rejected* overclaim ("those within the task have been fixed already"): **fixed.**
   `foundations/decisions.md:8836-8837` now reads "those within the task that the review of the whole change lists
   have been fixed already (WAY-161)", and `:8842-8843` "the cosmetics within the task that the review of the whole
   change lists anyway". Both match WAY-161's reach. The *Rejected* paragraph was only re-wrapped otherwise; I
   compared its clauses with the base and none was lost or changed.
2. WAY-297 *Rejected* conclusion followed from one branch only: **fixed.** `:9107-9109` now says the collision is
   repaired only by the fix for Minor findings of the review of the whole change, which the cycle gives up whole
   on a new serious finding, "so that in those cases, and for a finding of a later review, the collision reaches
   the merge". That is true: a later review's Minor finding is never fixed (WAY-161) and a given-up fix repairs
   nothing.
3. WAY-162 body: one overloaded sentence, and "that WAY-161 has fixed": **fixed**, with one new finding of the fix
   (Minor, below). The sentence is split at `:4454-4462`; the Minor-only fix, the review, the revert on a commit of
   its own, no third round, the request not blocked on the accepted code, and the lists with the new finding's
   grade are all kept; the contrast sentence ("In the code reviews after ...") now reads on its own; "that WAY-161
   has the cycle fix" is accurate. The Verification and Rationale of WAY-162 were not touched and still agree.
4. `SKILL.md` "with no further review of that code": **fixed.** `task-cycle/skill/SKILL.md:403-404` now says "with
   no review of the revert itself". Step 10 (gate on the code the revert leaves) and step 12 (review of the
   merge of the target branch) are no longer contradicted. The rest of the paragraph is unchanged.

## Blocking findings

none. No new Critical or Important finding in the fix diff.

## Minor findings

1. **Within the task; new in the fix; blocks nothing.** `foundations/decisions.md:4448-4462`, the binding text of
   WAY-162 now has four sentences (1 "In every code review ... counts as one that remains."; 2 "Where a blocking
   finding remains ... review rounds."; 3 "Where the review of the whole change leaves no blocking finding ...
   found it."; 4 "In the code reviews after the review of the whole change ... as WAY-161 gives them."). WAY-05
   (`:125`) and `elements/decisions/template.md:25,96` say a decision opens with one to three binding sentences;
   the base had three, so the split took it one over. The grade, with the reasoning for it: the grade paragraph
   of `review-change` makes a departure from a foundation entry Important when the change's files "do what the
   entry forbids, fail to do what it requires, or restate it differently". WAY-263's cases are about the entry the
   change writes being false to, or broader than, the rule it states (here WAY-161, WAY-289, WAY-162's own
   Verification); the WAY-162 text states each rule exactly as WAY-161 and the code do, so none of the three
   applies. WAY-05's count is a format limit: the sentences stay concrete and checkable, no later work follows a
   wrong text, `foundation_check.py` does not count sentences (exit 0), and two older entries are over the limit
   too by a rough count (WAY-80, WAY-229, left untouched). So I grade it Minor (style of an entry), not
   Important. It remains in the fix; a later reviewer who reads WAY-05 as strictly may grade it higher, which is
   why I name it. Fix if the cycle wants three: join sentence 4 to sentence 3 with a semicolon
   ("...found it; in the code reviews after the review of the whole change, and for a Minor finding that remains
   after a fix, the findings that do not block go unfixed to the request's lists as WAY-161 gives them."), which
   keeps the split of the over-long clause but not the extra full stop; or move the "later reviews" sentence into
   WAY-161, which already lists those findings.
   This is a finding of the fix. If the cycle's rule makes a Minor finding of a Minor-only fix go to the request's
   list, it goes there.

## Findings outside the task's scope

none (the earlier out-of-scope finding about the hand-made route is not in the fix's findings file and was not
touched).

## Declined to judge

- Whether WAY-05's limit should be enforced by `foundation_check.py` or relaxed, and the two older entries over
  it: a matter of the checker and of those entries, outside this task.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` — exit 0.
- `python -B gate/run_tests.py agent-instructions` — exit 0.
- `git diff 820f963..a2a4b83 --check` — exit 0, no whitespace error.
- Manual: a sentence count of the first paragraph of each entry in `foundations/decisions.md` (a rough regular
  expression run with `python -I`, read-only) listed WAY-80, WAY-162 and WAY-229 as over three sentences; counts
  are approximate and were used only to show the precedent.
- Not run: the full gate (the cycle's own run).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-05 (read whole) and `elements/decisions/template.md` lines 20-30 and 94-110: for
  the sentence limit the coordinator asked about.
- The fix report `reports/04-author-fix.md` read as claims; its statement that only the four findings were touched
  was checked against `git diff --stat` (two files, hunks in WAY-162, WAY-289, WAY-297 and one phrase in
  `SKILL.md`).

## Searches not found or unclear

- `foundation_check.py` does not report the sentence count of binding text; I found no check that enforces
  WAY-05's "one to three", so the limit is held only by review.
- Unclear: whether the intended grade for a binding-text form limit is the style grade or WAY-263's; the review
  skill names WAY-263 only for entries restating or departing from another entry's rule. I chose Minor and gave
  the reason above.
