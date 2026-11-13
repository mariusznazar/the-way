# Findings for the fix — review of the whole change, range 6814c6f..e51d835

Blocking findings: none. The Minor findings below are cut word for word from `reports/review-whole-change-report.md`; the reviewer listed each as within the task and marked none outside its scope. The reviewer graded and scoped them; the orchestrator moved none.

### Minor

1. **`foundation-review/SKILL.md:60-61` and `:81` do not mention the new kind of item.** Step 4 reads "the proposals about the foundation, the groups of
   remarks, and the data file". Step 7 reads "The review is done when the human has decided on every proposal and every group". Steps 2 and 6 were
   updated. WAY-354 requires that the human is asked at each such decision, and `with_the_human.md` step 2 does that. But the condition for marking the
   review done, which decides whether a tag is placed, does not name these decisions. Where the human names an existing task, `proposals.md` says "nothing
   is proposed", so the item is not a "proposal" in step 7's words, and the review could in the letter be marked done without asking. Evidence: the two
   quoted lines and `proposals.md:20-29`. Why it is Minor and not Important under WAY-263: step 6 does require asking at each, so the files do not do
   what the entry forbids, they only leave the end condition loose.
2. **WAY-354's *Rationale* (`foundations/decisions.md:11763-11765`) carries a rule in prose: "the review does not search".** The binding sentence
   says only that the review asks the human. WAY-05 (and `elements/decisions/template.md`) says that what a decision forces on later work stands in a
   binding sentence or a field, never in prose. `foundation-review/weak_points.md` (end of the new section) repeats it as an instruction: "The review
   does not look for the task". Fix: say it in the binding sentence, or drop it from the files.
3. **"as before" in the binding sentence of WAY-327** (`foundations/decisions.md:10839`), in its Verification ("the same three answers as before") and
   in `task-cycle/skill/request_template.md:337`. An entry describes the decision as it stands now, never the change (WAY-07, WAY-19). "As before"
   points at the earlier wording. A reader of the entry alone cannot tell what "before" was. Fix: state the remark as a standing rule, "the human who
   checks by hand writes a remark after the check". (After the repair reading below: WAY-297's binding sentence says "graded as before" and WAY-07
   says "as before it", so the phrase has precedent in the log. The finding stays Minor, graded on the point that the entry is read alone, not on
   WAY-07 or WAY-19 as a breach.)
4. **WAY-353's *Verification* names as a violation something its binding sentence does not forbid** (`foundations/decisions.md:11719-11721`: "a script
   is run before the cycle starts to check that every file, line and entry a task document names still exists"). The binding sentence says only how a
   place is pointed at and what the *Source* keeps. The script is a rejected way, and its place is *Rejected*. As a "violates" example it makes a later
   comparing agent fail a change that adds such a check although no sentence forbids it. Fix: drop that clause, or put the prohibition in the sentence if
   it is meant to bind.
5. **Concern (a), judged: the steps rule meets WAY-286 in its letter, with a gap** (`task-cycle/skill/request_template.md:332-338`). The rule says: no file
   name and no identifier in a step; where the way to the place is a file, the step describes the place; the item ends with its pointer to the lower
   part. That keeps WAY-286's top-part rule. But a check by hand often needs a command or a file the human must name. The rule does not say whether a
   step may carry a command, and the author reported this as unresolved (author report, choice 3). The example (`:378-391`) also ends the item with the
   steps and not with a pointer, so the reader of the rule cannot see where the pointer goes. In the same example, "If you want to look first, and write
   a remark with what you saw:" reads as an optional fourth way, while WAY-327's *violates* names "adds a fourth answer for them". The sentence is a
   invitation and not an answer, but it is close. Fix by wording: put the pointer after the steps in the example, state the command case in one
   sentence, and rephrase the invitation.
6. **Concern (b), judged: WAY-354's *Rationale* cites WAY-329 for more than WAY-329 says** (`foundations/decisions.md:11764-11765`: "an identifier of a
   task that an entry could name exists only for a task of a project plan (WAY-329)"). WAY-329 derives the identifier of a plan task's line and says
   nothing about tasks outside a plan. The sentence is an inference. It is faithful to the task document, whose *Context* makes the same attribution,
   and the author named it a reading. Fix: write it as the reason without the citation, or cite WAY-329 as "only plan tasks have an identifier derived
   by a decision".
7. **Form of two files.** `project-level/task/skill/final_review.md:10-13` re-wrapped lines unevenly: one line is 123 characters in a file that wraps near
   100. `project-level/task/skill/draft.md` repeats the rule of the template in its own words, so the rule now stands in three files (concern (c)).
   `final_review.md` carries it as a gate check, and `draft.md` and `template.md` as the writing rule. Judged: acceptable, because the task asks for the
   template and the skill, and each of the three says it once. The risk is drift in a later edit. No fix needed beyond the wrap.
