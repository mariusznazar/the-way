# Findings of the review of correction 1, for the fix

Reviewer's report: `reports/review-correction-report.md`, first line `FAIL 637d7787cade17fa6d338e70df0ce4c85a8e478b`. Range `20332036..637d7787`. The one blocking finding, in the reviewer's words. The report's Minor finding is no part of the fix: a Minor finding of a correction's review is not fixed and goes to the request's list.

### Important — within the correction

**1. The refinement step now makes a row that repeats the human's choice wait for the human's
acceptance when it adopts an outside practice. WAY-134 forbids that, and the task template, the
third copy of the step, still says such a row enters accepted.**

Place: `elements/common/skill/task_variant.md:33-38` ("A candidate that adopts a practice from
outside the product (WAY-100) is built `waiting` and not as the human's choice unless the question
that settled it showed the parts the practice leaves out among its ways … before the row is
accepted") and `project-level/task/skill/find_settlements.md:29-31` ("where the human did not see
them as ways, the row waits and a question shows them, before the row is accepted").

What is wrong. WAY-134, the entry this correction changes, keeps its rule that a row repeating a
choice the human made between ways shown enters accepted:

- binding sentence (`foundations/decisions.md:5283-5285`): the task document keeps "those that
  repeat a choice the human made between ways shown included unless the human struck them";
- *violates* (`:5344-5346`): "a row that repeats the human's choice between ways shown waits for the
  human's acceptance like a row the agent derived";
- *Rejected* (`:5398-5399`): "every row accepted separately, as before — a second consent to the
  same choice".

The new second paragraph of WAY-134 (`:5304-5310`) asks the refinement to show the left-out parts
among the ways of the question. It says nothing about the row's state, and it creates no exception
to the rule above. The remark does not either: it asks that refinement put the left-out parts among
the ways the person weighs. A row such as row 1 of this task — the answer to question 1, chosen
among ways shown, whose *Not chosen* holds no part of the card or the paper — would under
`task_variant.md` start `waiting`. Step 5 does not close until it is accepted, so the human gives a
second consent to a choice already made: exactly WAY-134's *violates* example.

The three copies of the step also disagree. `project-level/task/template.md:208-209`, which
`task_variant.md` step 1 orders read "in full", keeps the unqualified "A row that repeats a choice
the human made between ways shown enters accepted, and the human cuts only the rows the agent
derived (WAY-134)". So does `elements/common/skill/build_table.md:17-21` ("is built `accepted`, not
`waiting`"), and `task_variant.md:39-41` repeats it four lines below the new exception. A refiner
reading the template and `build_table.md` builds the row accepted; one reading the new bullet builds
it waiting.

This is the author's own choice 3 (`author-correction-report.md`), which the answer does not give.
Its reason — building the row accepted "is what let the parts slip through unseen" — does not hold:
an accepted row can still get the question that shows the left-out parts. The answer then goes into
the row's *Source*, as `task_variant.md` step 4 already does for a question against a choice ("write
each answer into the row, with the ways that question showed and the human did not take in the row's
*Source*").

Why it matters. Each refinement of a task that adopts an outside practice re-asks the human to
accept a choice already made. That is the second consent WAY-134 rejected. A refiner following the
task template does the opposite, so the step behaves differently depending on which file is read.

What would fix it, the narrowest way: in `task_variant.md` and `find_settlements.md`, drop the
`waiting` state and keep the question. The row repeating the human's choice enters `accepted` as the
human's choice. Where its source keeps no left-out part, the question of "How a skill asks" shows
those parts as ways, and the parts the human turns down go into the row's *Source* (or the *Not
chosen* of its question) before the table closes. Making the row wait would instead need WAY-134's
first paragraph, its *violates* and its *Rejected* changed — a change of meaning the remark does not
give.

Grade: Important by WAY-263. The change's files do what an entry the change itself changes
forbids, and they restate it more broadly than the entry allows.

Contradiction: yes — WAY-134 (its first binding paragraph, and its *violates* example "a row that
repeats the human's choice between ways shown waits for the human's acceptance like a row the agent
derived").
