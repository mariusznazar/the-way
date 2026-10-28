# A plan member's cycle

Read at step 1 of `implement-task` when the task's `Project relation:` makes it a member of a
project plan.

Before a plan member's cycle starts, verify that its definition's approval still holds and that
every task in its `Depends on` is done (WAY-144), from the delivering task's evidence and never
from a label alone: `done — goal delivered in task <n>` counts only through that task's
delivery, and `dropped — approved by human` delivers nothing, so the mismatch returns to the
plan's reconciliation. While a dependency is unfinished, or the definition's approval or its
plan's recheck is pending, the task waits without losing its acceptance; start no branch.
