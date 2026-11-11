# Handoff — the correction, second instruction (resumed one author)

This replaces the direction of item 1 in `reports/correction-handoff.md` and
`reports/correction-findings.md`; everything else in them stands (item 3's five findings, the
return step again, the checks, the report path `reports/correction-report.md`). Work from the
uncommitted state you left in the worktree.

## What the human decided

The rule of item 1 and the way of handling a line are rules of the task place, not of the-way. The
human said so on the request, as the same principle the task already settles for the forms (task
settlement row 3: the forms come from the rules of the task place, not from text at the product or
in the-way's skills). The orchestrator has written the rule into the task place's rules, at the
human's word, outside the repository; you must not quote its words, path or content anywhere in a
tracked file. In the-way a skill and a decision only point to those rules.

## What stays in the-way, and what leaves it

Stays (the-way alone knows it): in which turn a refiner makes a line, in parallel and with no queue,
and the late line where the rules were not yet known (as it stands after the first review); that a
refiner never moves a line to ready and the orchestrator does it with the document's `Status:` and
the plan's row; where the dependencies come from (the `Depends on` column of the plan); how the
identifier is derived from the plan's file name and the task's name in the plan, with the two
conditions under which it is unambiguous; the orchestrator making a line already ready where none
stands at acceptance.

Leaves the-way (so it is removed from the skills and the decisions, not moved to another file of the
repository):

1. How a line is found and that a task that has one gets no second (`project-level/task_line.md`,
   the bullet that searches the place for a line that links the task's document or names the task).
2. What to do where another line already carries the identifier (the bullet of "Make the line", the
   clash sentence of "The identifier", and WAY-329's clause and its *Verification* example on it;
   this also settles Minor 1 of item 3, say so in the report).
3. How an existing line is changed: "touches nothing else of the line", and the check before a write
   (`task_line.md`, "The dependencies").
4. The rule of item 1 itself (the agreement of the lines at both ends of a dependency): it is
   **not** written into any skill or decision. In its place `task_line.md` carries one sentence: the
   refiner keeps the task's line, and the lines of the tasks it waits on and that wait on it, in
   agreement with the plan's dependencies as the rules of the task place give; where those rules do
   not say how, it asks the human once (as it asks where they give none of the forms).

WAY-107 gains one thing: how a line is handled — finding it, one line to a task, which fields an
agent may change, the agreement of the lines at both ends of a dependency, a clash of identifiers —
is also from the rules of the task place, never from text of the-way or of the product; the source
is the human's remark at the request, and the entry says so in the form the foundation step gives
(mark it as that step's mark for a change the human's remark makes). WAY-154 and WAY-329 lose what
leaves; WAY-329 keeps the derivation and its two conditions. Keep each of WAY-154 and WAY-107 within
one to three binding sentences (item 3, finding 4).

Item 3's other findings stand: the citation of WAY-329 on the right sentence, the rewrap of the long
lines, the word "line" for "entry". Where the-way text still names `Task rules` / `task-rules`,
extend `project-level/backlog_place.md` and `AGENTS.md` only as far as needed; add no form.

## Own-work check

The requirement most likely unmet now: that no tracked file of the-way holds a rule of handling a
line that the rules of the task place now hold (finding, one line to a task, which fields to change,
read before writing, the agreement of the lines, the clash of identifiers). Grep every changed and
every file of `project-level` and `product-guidelines` for them and report the command and exit
code; and check that the one-place sentence of "Make the line" is still the only place of the
moment of making a line.

Return the same: status, commits, one-line check result, report path. Commit nothing before the
checks pass.
