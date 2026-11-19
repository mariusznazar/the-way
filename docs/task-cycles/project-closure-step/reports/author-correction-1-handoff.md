# Handoff — correction 1 after the human's remarks (task `project-closure-step`)

You are the one author, resumed (same class) for a correction after the human's remarks on the open
request https://github.com/mariusznazar/the-way/pull/150. Variant of `make-change`: **a correction for the
human's remarks** (`task-cycle/change/SKILL.md`). Work in the same worktree and branch
(`the task's worktree`, `task/project-closure-step`), from the head
`935109fba7458cef123b1e2b749a32f48902b34b` (the request's last head; the record's copy is already removed
from the tree). Commit by path, English messages, no full gate (CI is the final gate). Run the affected
checks and report each with its command and exit code. Your directory for working copies is `.runs/author/`
(the paragraph on working copies in your first handoff holds). Report:
`.runs/task-cycles/project-closure-step/reports/author-correction-1-report.md`, with **Unread material**,
**Searches not found or unclear**, your own-work check and the line on working copies, as `make-change` gives
a report.

## The remarks that bind

The human's remarks, word for word, are in
`.runs/task-cycles/project-closure-step/reports/correction-1-remarks.md` (named here so that you may read it;
the other files of the record directory are still not yours). They bind. Where an item lets something through
or accepts it, nothing changes. The remark that asks for work:

> 2. **A closed plan passes the check although two of its tasks are each marked "delivered by the other"** —
> **fix in this request**: the check refuses a closed plan where following "delivered by another task" never
> reaches a task that is done (a loop of such rows, of any length), with a test for the pair and for a longer
> loop. It is a small addition to the check this request already changes, and the harm is the one the closing
> exists to prevent; a task for it would cost a whole cycle to read the same code again.

Items 1 and 3 (the closing step never run on a real project; no rule for the case where the existing task
document stands) are let through with no task, and items 4–12 of the request are accepted: change nothing for
them. This is the one round of remarks.

## What the correction does

1. `project-level/plan_check.py`: in a closed plan, in the condition `closed` you wrote, a row
   `done — goal delivered in task <n>` is refused where following the delivery — from that row to the task it
   names, from that task, if its row is also `done — goal delivered in task <m>`, to task m, and so on — never
   reaches a task whose row is `done`. Today the chain is refused only where its next task is
   `dropped — approved by human`; a loop (two rows delivering one another, and a longer loop of three or more,
   with or without rows leading into it) is not. Keep every earlier finding as it is (a delivery by a task the
   plan lacks and a delivery in the task itself stay `form`; a chain that reaches a `done` task still passes; the
   check still runs only on a closed plan). Mind the trust boundary: the follow must end on crafted input —
   long chains, a loop with a tail, shared tails, a self-reference, a plan of a thousand rows — never recurse
   without a bound, and report each refused row at its own line as the check reports the others. State in your
   report which way you report (one finding for each row on a chain that fails, or for the row at the start
   only) and why.
2. Tests in `project-level/test_plan_check.py`, citing the invariant `project-plan-check` as the earlier ones
   do: for the pair, for a longer loop (three or more), for a chain into a loop, and for the unchanged passing
   and failing cases next to them. Show each new test failing on the code before this correction and passing
   after it (record both runs). Check whether `project-level/test_plan_state.py` needs a case, and add one only
   if the reader's behaviour on such a plan is new.
3. The places that state the rule, which the correction brings into step: the sentence of the invariant
   `project-plan-check` in `foundations/invariants.md` (today: a goal delivered by a task that is dropped),
   `project-level/plan/template.md` ("What the check decides" and any sentence that gives the narrower rule),
   WAY-142 and the entries WAY-411 to WAY-415 where they restate it (search the whole foundation once, WAY-33),
   and the step's file `project-level/lead/skill/closure.md`, section 1, and the lead skill's step-1 bullet:
   the closing already holds a row delivered in a dropped task (the orchestrator's earlier choice, Q3 of the
   record, which the human accepted as item 5 of the request); the same reason holds for a row whose chain never
   reaches a done task, so the closing holds it the same way, tells the human which row and why, and starts no
   preview. This extension is a choice of the cycle; name it in your report and give its cost if wrong. Where a
   sentence you change is held by a test through a line `decision:` or `invariant:`, change the test with it.
   Keep every word you choose to the settled vocabulary ("dropped", "closing item").
4. Nothing else: do not change what the remarks let through or accept, do not touch the Minor findings of the
   reviews, and do not widen the check to a closed plan's other states.

Size and form: `plan_check.py` stands at 1041 lines (WAY-385: file 1200, function 110, counted on formatted
code); the formatter and linter tests of `agent-instructions` hold the standing rules. Rules of the repository as
in your first handoff (`AGENTS.md`, `guidelines/coding.md`, `coding-check.md`, `testing.md`).

## What to return

Your status, your commits, the one-line check result and the report path. The report names the checks the
correction touched with command and exit code (at least `python -B gate/run_tests.py project-level`,
`product-guidelines`, `agent-instructions`, `python -B elements/common/foundation_check.py`, and the entry-point
check if a skill file changed), the new and the changed entries marked `row <n>`, `projected` or `the cycle's`
with one sentence of each entry's meaning in English and one in Polish, and quotes word for word any pair of
examples you add. The return step and the reviews come after; do not start them.
