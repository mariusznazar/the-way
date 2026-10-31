# Project-plan task

Use this file only when the task belongs to a project plan.

## Step 1: read its approved project basis

Read the approved definition and plan, whose form `project-level/plan/template.md` gives, and run
`python -B <the-way>/project-level/plan_check.py <plan>`; a finding returns to `plan-project`.
Identify the plan item by its name, dependencies, projected entries it realizes or writes and open
questions placed in it (WAY-142, WAY-145, WAY-147). A proposed split or scope change goes back to
the project plan before either resulting task is ready.

## Step 3: reconcile assigned questions

Reconcile every open question the plan places in this item. Answer a question that determines
required product behavior in the task document; reproduce an implementation question under
`Questions carried to cycle`. Do not let a question in scope disappear.

## Step 4: preserve the plan assignment

Use the plan to identify which entries the task is assigned to realize or write. Compare numbered
work, dependencies and projected entries with its plan item. A mismatch returns to the plan, not an
unrecorded change in the task document.

## A run of `settle-technology`

A run at the member's task stands at the member's own document, and the approved definition stays
untouched, so no gate returns (WAY-267). A choice that changes the cut of the work returns to the
plan as step 4 gives. A human who wants a projected decision of the definition changed goes the way
`resolve_gaps.md` gives for a change of an approved definition (WAY-118).

## Step 6: check the assignment

Check the plan item and assignments before readiness. A mismatch is an obstacle to readiness and
returns to the owning project workflow.
