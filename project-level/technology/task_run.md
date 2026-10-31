# A run at a task

What a run of the skill `settle-technology`, whose `SKILL.md` lies beside this file, does at a task
document (WAY-267). The file is read at step 0 of such a run and holds only what differs from a run
at a definition: a step it does not change stands as it is, the task document and its note being
"the document". The form of the section *Technology* and of a settled question stands in
`project-level/task/template.md`.

## Start

In place of the first two bullets of `start.md`:

- Read the task document whole, the section on *Technology* of `project-level/task/template.md`, the
  section "Technology" of `project-level/definition_template.md` for the rules of weighing, and the
  section "How a skill asks" of `elements/common/way_of_working.md`.
- A task document in a running cycle is left alone, as `project-level/task/skill/draft.md` gives.
  Any other, an accepted one included, is set to `Status: refining` before anything else in it
  changes, as that file gives, so that an interrupted run never leaves a changed body under
  `ready for cycle`.
- A run that refinement starts for a reserved choice takes that choice as its note. A run given no
  note, at a document whose section *Technology* holds none and with no such choice, asks for the
  note once.

The bullet of `start.md` on reading the foundation stands. In place of its other bullets:

- Where the document has no section *Technology*, begin with *List* below.
- Where the section holds a list and the run has a note the section does not yet hold, write the
  note and follow *List* below for it first, whatever the items already there end with. Only then do
  the bullets below apply.
- Where the section holds a list, read its notes and items. An item ending `— open` is looked for
  under *Questions to settle* first; where a question written for that choice stands, the item ends
  `— settled: <question>`. Then, unless *List* has just shown it, show the list and ask whether it
  still holds; where the human adds or changes an item, follow *List* below for it. Then resume the
  step "Settle the open choices" with the open items, their preferences and what they wait for. A
  report `.runs/technology/<choice>.md` that reads `critique: passed` and names this document at its
  head is reused, and any other starts its research again.
- Where the list holds no open item, go to *Close* below.

The looks of `running_product.md` and `failure_notice.md` are not taken, here or at *List*: a matter
of an agent's way to the running product, or the matter of how a human learns of a failure, enters
the list only where the note touches it.

## List

`list.md` applies, except that:

- The items come from the note and the task document. Each note stands in the section as it was
  given, with its date.
- The rule of belonging selects nothing for a choice the human names.
- A choice a decision of the foundation holds opens only on the human's word, in the note or in a
  change to the list: it then stands `— open`, with the decision it changes nested under it. An
  agent never opens one. A decision silent on part of what a matter of the logs, the interface or
  the development data asks (`running_product.md`) holds nothing, where the note touches the
  matter: the item stands `— open`, with that decision nested under it as `Changes:`.
- A choice a projected decision of the approved definition the task carries settles stands
  `— projected: <question>`, and no run reopens it. A human who wants it changed goes the way
  `project-level/task/skill/resolve_gaps.md` gives for a change of an approved definition (WAY-118).
- The status line of a definition does not apply. From the showing of the list until the human has
  settled what the run lists, the document reads `Status: waiting for human`.

## Settle

Sub-steps 1 to 6 of `settle.md` stand, and:

- WAY-165 and WAY-166 apply where the note touches the logs, the interface or the development data,
  and WAY-270 where it touches how a human learns of a failure; WAY-166 binds the three matters
  only.
- A choice the human opened is no longer held, so it is tested.
- A constraint the task document states counts as a definition's constraint does.
- Where one run serves several tasks, each research agent also gets the path of each affected task's
  document.

## Write

In place of sub-step 7 of `settle.md`, with no `record-decision`:

- Write the choice under *Questions to settle* as a settled question, in the form the template
  gives: in the question that already asks that choice, or in a new one. A choice the human opened
  says in its *Answer* which decision it changes.
- End the item with `— settled: <question>`, the question reading as under *Questions to settle*,
  and write both before the next table.
- Start the next wave: every choice whose every dependency is now settled.

The step writes no row of *Settlements to record*: step 5 of `refine-task` takes the settled
question as a candidate, as it takes every answer, and the human cuts it.

## Close

In place of `close.md`:

- No item of the section ends `— open`.
- No readiness check runs.
- Set `Status: refining` and return to the step of `refine-task` that called the run, or, for a run
  the human started, to its step 3, so that its steps 4 to 6 run on the whole document and the human
  accepts all of it (WAY-124).

## Orchestrated

Where a project orchestrator leads the refinement, the refiner leads the run through its
conversation file and starts no agent: `project-level/task/skill/orchestrated_mode.md` gives the
routing (WAY-154).
