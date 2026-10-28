# The planning route

Step 8 of `implement-task`, read only on the planning route: the planner's dispatch, the review of
its plan, and what each slice's handoff carries.

## The planner and the review of the plan

Only on the planning route, dispatch a fresh planner with `plan-task`, the frozen task, any
reviewed spec and the checks the move of the pin carried (step 2). It writes `plan.md` and its
size report `plan-size.md` in the record's directory and returns before any slice is made;
where it returns an open design choice instead, continue at step 6 with its report. Review the
plan for coverage of every item of the task, every row of *Settlements to record*, every
projected entry the task carries and every check the move of the pin carried, fidelity to the
task's sources, no code, checks that can actually run and a size report in which every slice
fits.
Check each slice's *Read* against your own reading of step 2 and add to it in `plan.md` what the
slice needs and misses — a decision of a part it touches, an invariant it reaches (WAY-62), a
guideline file — then run the size script on the plan again; a slice it now reports too large
returns to the planner to be split. Check each slice's *Model* and *Risk*: a class other than the
default `cheaper` carries its reason (WAY-229), its *Checks* name focused checks and no run of
the gate (WAY-160), and a slice whose files the part map names as a trust boundary, or that holds
an operation that cannot be undone, is marked so — none where both answers of step 4 are no. Copy
its *Choices* into the questions table and record your go-ahead as provisional.

## A slice's handoff

A slice's executor gets, copied into its handoff, its section of the plan and the passages of the
task, spec and plan its *Read* names, and the reviewer of a slice the same selection; the plan's
*Read* is the source of that selection, which the planner proposes and you check and may add to in
the plan's review (step 8).
When you build a slice's handoff, name each foundation entry of its *Read* by its identifier with
its range in the worktree as it stands then, since the foundation step and earlier slices may have
moved it, and an entry the foundation step wrote by its identifier and its new range; find a passage
of the plan again by its heading where the plan changed, and a range of code or tests again where an
earlier slice changed its file. Give the current ranges beside the copied section; where they differ
from the plan's, the current ones hold.
