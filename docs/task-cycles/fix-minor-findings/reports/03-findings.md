# Findings file — the Minor findings of the review of the whole change (reports/02-review.md, PASS 820f963)

These are the Minor findings within the task, in the reviewer's words, copied from lines 63-92 of that report. No finding blocks. Fix each as it says or contest it with evidence.

1. **Within the task.** `foundations/decisions.md:8836` (and the same idea at `:8841`, *Rejected*): WAY-289's
   Rationale says that of the findings nobody will feel, "those within the task have been fixed already
   (WAY-161)". WAY-161 fixes only the Minor findings the review of the whole change lists; a Minor finding of a
   code review after it, of a slice review the whole-change review does not list, or one a fix left, is within
   the task and not fixed. The sentence restates WAY-161's reach more broadly and without its qualification.
   Why it matters: a later reader takes it that no in-task finding can be waiting unfixed. Grade: Minor, not
   Important under WAY-263, because it stands in a Rationale and *Rejected*, not in the rule text, and the rule
   text of WAY-289 and of WAY-161 are accurate; the behaviour the cycle follows is unaffected. Fix: write "those
   within the task that the review of the whole change lists have been fixed already (WAY-161)" and, in the
   *Rejected* clause, "the cycle fixes those the review of the whole change lists".
2. **Within the task.** `foundations/decisions.md:9105-9107` (WAY-297 *Rejected*, last clause): "a collision shown
   on a sentence is then repaired only by the fix for Minor findings, which the cycle gives up whole when the
   review of that fix finds a new serious finding, so the collision reaches the merge." As written the
   conclusion follows from the first branch only; the fix usually lands and the collision does not reach the
   merge. Why it matters: the reason given for rejecting "Minor always" is overstated. Evidence: compare with the
   original ("is then never repaired in the cycle"), which was true. Fix: "...repaired only by the fix for Minor
   findings of the review of the whole change, which the cycle gives up whole when the review of that fix
   finds a new serious finding, so that in those cases, and for a finding of a later review, the collision
   reaches the merge".
3. **Within the task.** `foundations/decisions.md:4454-4462` (WAY-162 body, new sentence): the one sentence
   holds the Minor-only fix, the revert, the request's lists, and then a "while in the code reviews after the
   review of the whole change, and for a Minor finding that remains after a fix, ..." contrast, and says Minor
   findings "that WAY-161 has fixed" where WAY-161 only has the cycle fix them. It is hard to parse, and
   the rule is correct only when read twice. Fix: split into two sentences (the Minor-only fix and its revert;
   then what the later reviews and a remaining Minor finding do), and write "that WAY-161 has the cycle fix".
4. **Within the task.** `task-cycle/skill/SKILL.md:402-403`: "the request opens on it, not blocked, with no
   further review of that code". Step 12 (`:415-419`) still has a fresh reviewer review the merge of the target
   branch where that changes the reviewed code, and the gate runs on the code the revert leaves (step 10). The
   phrase can be read as forbidding both. Fix: "with no review of the revert itself" or "no further review of
   the fix".
