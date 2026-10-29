# Resolve the gaps

Ask about the most consequential missing answer first, with one sentence explaining what it blocks.
Put each answer under its question, with the ways not chosen where the human chose among ways
shown, as the template's *Questions to settle* gives (WAY-134), and update the document before
asking the next. If the answer is
in the approved project definition or foundation, quote the exact wording with its location
instead of asking the human; an inference is not an approved answer.

If two answers conflict, show both and ask which holds. If the answer changes the approved project
definition or a current foundation decision, route that change to its own process; do not silently
settle it inside the task.

Settle known product choices needed to state the task's outcome before the cycle. A choice of
implementation method stays with the cycle's plan, or with the choices of its cycle record where
no plan is written. An unanswered question that blocks taking the task keeps `Status: waiting for
human`; never turn it into an apparently executable `To do` item. A new choice discovered during
the cycle belongs in its decision record for the PR.

For a plan member or source-only task, reconcile the questions assigned to it as described in the
corresponding file named in step 1. Answer a question that determines required product behavior in
this document; reproduce an implementation question under `Questions carried to cycle`. Do not let
a question in the task's scope disappear.

Name under *Human actions* the human action through which a human makes each effect the task has
outside the product's repository; a read outside the repository stays with the agent (WAY-140).
For each human action, propose its placement by that section's rule in the template, and have the
human place it, asked as "How a skill asks" says (WAY-140). A human action placed before the cycle
and not yet done keeps `Status: waiting for human`; mark it `done` once the human has performed it
(WAY-124).

When the task's outcome deploys the product or changes how or where it runs, check that the product
has a deployment skill covering every item of the list WAY-139 holds, in
`<the-way>/foundations/decisions.md`. Where it has none or an item is missing, add an item to *To
do* for that work and offer the human to split it into a task of its own, which step 1 then
handles (WAY-139). A task with no such outcome takes no check.
