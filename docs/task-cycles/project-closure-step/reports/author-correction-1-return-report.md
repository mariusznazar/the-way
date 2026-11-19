# Return step of correction 1 — task `project-closure-step`

**Status:** done. The step committed nothing: head stays `4101de84`, the worktree is clean. Worktree
`the task's worktree`, branch `task/project-closure-step`.

`task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md` read whole; the remark that asked for
work (item 2) is the correction's subject; items 1 and 3 (let through) and 4 to 12 (accepted) change nothing.

## Return step, as the record gives it

- **Foundation compared with code** (against `plan_check.py` at the head, `plan_state.py`, `closure.md` section 1, the
  lead skill's step 1, the plan template):
  - Invariant `project-plan-check`: its sentence ("in a plan whose `Status:` line reads closed … a task's goal is
    delivered in another task and following the deliveries from task to task never reaches a task that is done,
    because they end in a dropped task or run in a loop") matches `check_closed` and `delivery_ends`: the
    findings are at the row of each delivery whose chain ends in a dropped task or runs in a loop, for a closed
    plan only. A chain that ends in a row in another state is reported at that row by the clause before it; the
    sentence does not claim more. No mismatch.
  - `project-plan-form` (through the template): one `Status:` line, `closed YYYY-MM-DD`, a calendar date, a
    delivery in a task the plan lacks or in the task itself: all `form`, and the code keeps them `form`. No mismatch.
  - WAY-142: its sentence says a plan is closed once each task is "done, delivered in another task or dropped". A
    row in a loop is delivered by no task, so the state `done — goal delivered in task <n>` in the template means a
    delivery that was made; the sentence is the summary the template states exactly (the passage on states, the
    header bullet, "What the check decides"). No mismatch; no change.
  - WAY-411 to WAY-415: none restates the closed plan's rule or the closing's condition of start (searched the five
    entries for "delivered"; none holds it). The closing's condition lives in `closure.md` section 1 and `SKILL.md`
    step 1. No mismatch.
  - WAY-146 and WAY-153 (the task's *Decisions in play*): WAY-146's list of what the script checks is a list of
    kinds of what a plan's structure decides, which the closed-plan check is one more of (a check a script can
    make is left to no critique); WAY-153 speaks of a reader that proposes from Git evidence, and the reader reads
    none for a closed plan and reports a finding of the plan check, exit 1, as for any plan whose sources fail.
    No mismatch.
  - Part map, part `project-level`: names the closing of a project; nothing in the correction changes what it
    answers for or its files. No mismatch.
  - Plan template, `closure.md` section 1, `SKILL.md` step 1: the same rule, in the same words as the invariant
    ("whose deliveries reach a `done` task"; "end in a dropped task or run in a loop"). No mismatch.
- **Decisions written or changed:** none.
- **Invariants written or changed:** none in this step (the sentence of `project-plan-check` was extended by the
  correction, marked `the cycle's`: In a closed plan the check also rejects a goal delivered in another task when
  following the deliveries never reaches a done task / W planie zamkniętym kontrola odrzuca też cel dostarczony w
  innym zadaniu, gdy podążanie za dostawami nigdy nie dociera do zadania zrobionego; set by the human's remark 2 of
  the request).
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (`Project relation: independent`).
- **Rows of *Settlements to record* written:** none in this step.
- **Pair of examples added:** none.

## Q5 of the record: does it bind after the merge in a way the foundation must hold (WAY-36)

The choice: the closing step also holds a row whose chain of deliveries never reaches a done task, as it already
holds a row delivered in a dropped task. It stands only as text of the step's file (`closure.md` section 1) and of
the lead skill's step-1 bullet, and no entry carries it, as for Q1 and Q3 of the first return step's report. It is
an instruction of how an agent works that stands in one skill and carries no choice of real cost: the check of the
same rows in a closed plan is already held by the invariant `project-plan-check` and by the plan template, and the
hold only moves the same finding before the preview. The two are one sentence of the file, so Q3 and Q5 now read as
one condition ("deliveries never reach a done task"). No entry is written, no row stays beyond the questions table.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- No file changed in this step, so no test directory was run; the correction's own checks stand in its report.

## Working copies

None made; `.runs/author/` stands empty.

## Unread material

none.

## Searches not found or unclear

none.
