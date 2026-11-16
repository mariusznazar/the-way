# Finding of the review of the return step — for the fix

Reviewer's words, cut from `reports/review-return-report.md` (range `cdbde3d2..83aa64db`, FAIL). One blocking finding (Important, `Contradiction: yes`). The two Minor findings of that review are NOT part of this fix; they go to the request's list.

### Important

**1. The lower part of the request template still gives the walk's out-of-scope errors as the author's alone, while kind 8, corrected by this commit, and WAY-408 cover the executor of a slice as well.**

Place: `task-cycle/skill/request_template.md:535-536`, the paragraph **Findings outside the task's scope.**:

> each error outside the task's scope that an author's walk through the running product reported,
> with the author's words and where it showed (WAY-408);

This commit changed the sibling sentence of kind 8 (`request_template.md:261-264`) from "its author
reported" to "its author or executor reported", for the reason the author's report gives as its
point 2: "WAY-408 binds the executor of a slice as well". Kind 8 then sends each such error to
"*Findings outside the task's scope* below" — and the paragraph it sends it to still reads "an
author's walk" and "the author's words". The return step's job (`task-cycle/skill/return_step.md`,
first paragraph) is to correct whatever no longer matches the entries the change writes; it found
this mismatch, corrected it in one of the two places that restate the same sentence of WAY-408, and
left the other. The template now says two different things about the same item, and the lower part
restates WAY-408 without its qualification "or the executor of a slice" (WAY-408's first sentence:
"The author of a change or the executor of a slice corrects each case…"; its second paragraph: "An
error outside the task's scope that the walk finds is reported and not corrected, and the description
of the request puts each such error before the human"). WAY-406 makes every executor of a slice that
alters behaviour a user sees walk through its slice (task, row 3 of *Settlements to record*).

Why it matters: the orchestrator of a change made from a plan, writing the lower part, reads that
the list holds errors an *author's* walk reported, with *the author's* words; an error the executor
of slice 2 reported can be left out of the list, or attributed to an author that a planned change
does not have. WAY-263 grades a changed file that restates an entry the change writes "without a
qualification" as Important.

Evidence: the diff of the range (kind 8 changed, lines 533-537 untouched); `git log -L533,537` over
`9cffc9ba..83aa64db` shows the paragraph last changed in `cdbde3d2`, before the return step.

Fix: "each error outside the task's scope that the walk of an author or of the executor of a slice
reported, with its words and where it showed (WAY-408)" or equivalent.

Contradiction: yes — WAY-408 (the error of the walk of "the author of a change or the executor of a
slice" goes before the human), and row 3 of the task's *Settlements to record*.
