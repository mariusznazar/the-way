# Resolve the gaps

Ask about the most consequential missing answer first, with one sentence explaining what it blocks.
Put each answer under its question, with the ways not chosen where the human chose among ways
shown, as the template's *Questions to settle* gives (WAY-134), and update the document before
asking the next. If the answer is
in the approved project definition or foundation, quote the exact wording with its location
instead of asking the human; an inference is not an approved answer.

If two answers conflict, show both and ask which holds. If the answer changes the approved project
definition or a current foundation decision, route that change to its own process; do not silently
settle it inside the task. The exception is a choice the human opened though a decision holds it,
by a note or a change to the list of a run of `settle-technology`: that run is the process of the
change, and its result is an edit of that decision in this document (WAY-30, WAY-267).

Settle known product choices needed to state the task's outcome before the cycle. A choice of
implementation method stays with the cycle's plan, or with the choices of its cycle record where
no plan is written. An unanswered question that blocks taking the task keeps `Status: waiting for
human`; never turn it into an apparently executable `To do` item. A new choice discovered during
the cycle belongs in its decision record for the PR, except a reserved choice, which no cycle
settles.

Run `settle-technology` at this document, with a note saying what the run is for, in three cases;
only the first is decided by the rule of `project-level/technology/reserved_choices.md`, which you
read when the task's outcome needs a language, a framework, a library, a store of data, a way of
logging in or a place to run that no decision, approved definition or accepted answer settles:

- the task's outcome needs a reserved choice;
- the refinement started from a note, carried in the request or given by the named choice of a
  closed draft request (`draft.md`), whether the choice is under the rule or a decision holds it;
- the human asks for a run while the task is refined.

The document keeps `Status: waiting for human` until the human has settled what the run lists. In
orchestrated refinement you ask for the run through your conversation file and start no agent
(`orchestrated_mode.md`). A choice not under the rule stays with the cycle, and the tools of the
skills of guidelines stay on those skills' routes.

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

The list holds two items the check handles apart, how long the record of the logs lives, between
deployments too, and how a human learns of a failure of the running product (WAY-139):

- A skill that records the human's refusal to settle an item covers it.
- Where a decision of the foundation or an approved definition the task carries answers the item,
  quote it with its location and ask nothing; the *To do* gains the item that writes the answer
  into the skill. A logs decision silent on how long the record lives answers nothing here.
- Otherwise ask the human, once and for each item apart, whether to run `settle-technology` at this
  task with a note on what the skill leaves unsaid and no decision and no approved definition
  answers. A yes is the third case above, and is also the human's word that the run asks for where a
  logs decision stands; the *To do* gains the item that gives the skill the answer. A no gives the
  *To do* the item that records in the skill that the human leaves the item unsettled, and the
  question does not return.
- Where the product has no deployment skill at all, ask before offering the split: a task that only
  writes a skill has no deployment outcome and takes no check. The split task carries the answer or
  the refusal.
