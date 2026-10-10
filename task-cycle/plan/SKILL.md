---
name: plan-task
description: Use when a ready the-way task's change has to be divided into slices before it is made — the plan a task cycle writes for every task, from the frozen task, its spec where one exists, the foundation and the code, or writes again after a spec or after a slice proved too large. Not for a project's plan of tasks, and never writes code.
---

# Plan a task's change

Writes the plan of one task's change: the foundation entries written before any code, and the
change divided into slices, each made by an agent of its own and reviewed by another (WAY-136). The
plan holds no code. The cycle that calls this skill, `implement-task`, holds the dispatch, the
record and every stage after the plan; this skill holds only how the plan is written.

This skill lives in `task-cycle/plan/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in, the directory `git rev-parse --show-toplevel` prints in the
session's working directory; in a product, it is the product's pinned `.the-way`. The script
`task-cycle/slice_size.py` is there, and each skill named below is the project skill of that name
with the `the-way-` prefix.

The planner is a fresh agent the orchestrator of `implement-task` dispatches. It writes only the
plan file the dispatch names, normally `.runs/task-cycles/<task-slug>/plan.md`, and sends its
questions back to the orchestrator; it never writes code, a test or a foundation entry, and never
asks the human.

## 1. Read

- The frozen task document in full: its outcome, *To do*, answered questions, *Questions carried to
  cycle* and the rows of *Settlements to record*.
- The spec, where the cycle wrote one; it binds where it settles more than the task, and the task
  binds where they differ.
- The task's sources: the approved project definition's projected entries the task carries or its
  plan item assigns.
- The product's foundation: the part map for the parts the change touches, the decisions whose
  *Scope* names them, the invariants of those parts and the glossary.
- The code and the tests the change touches, as far as is needed to name each slice's files. Read
  to cut slices, not to design the code.
- After a slice proved too large, its agent's report and the plan it came from.

## 2. Find an open design choice

Before cutting, look for an open design choice (WAY-135), which reading the code may show where
the task alone did not: an entry the change needs beyond the rows of *Settlements to record*, the
projected entries the task carries and the spec, or a way the code makes costly to turn back.
Where one stands, write no plan: return to the orchestrator a report of the choice, where it shows
and the ways open, so that a spec is written first. A choice of how to make what the task and the
foundation settle is no such choice: make it in the plan and list it under *Choices*.

## 3. Write the plan

Write the plan in this form; the script reads the slice headings and the fields *Change* and
*Read* as they stand here:

```markdown
# Plan — <task title>

- Task: <path of the frozen task>
- Spec: <path | none>
- Base: <the commit the task branch starts from>

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|

## Slices

### Slice 1 — <goal in a few words>

- **Goal:** <what is true once the slice is made>
- **Change:** `<path>` · `<path>`
- **Read:** `<path>` · `<path>:<first>-<last>`
- **Checks:** <the commands that show the goal holds; the failing test written first where the
  slice changes behaviour>
- **Depends on:** none | Slice <id> · <entry>

## Coverage

| What the task requires | Slices or entries |
|---|---|

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
```

- *Foundation entries* lists every entry the foundation step writes before the code: each row of
  *Settlements to record*, as its row number; each projected entry the task's code makes true or
  its plan item assigns; each entry the spec names; and an entry the change makes follow, such as a
  part-map change for a file the change adds. *From* names the row, the projected entry or the
  spec; *What depends on it* names the slices whose code needs it. An invariant's row names its
  check too, which an agent writes from the sentence and its method alone (WAY-69). Write `none`
  under the table where the change writes no entry. The plan names entries; it never words them.
- A slice is narrow: one goal, the files that goal changes, and checks that run when it is made. Cut
  along what a reviewer can judge alone. A small change is one slice; never add a slice for its
  own sake.
- *Change* names every file the slice changes or creates. *Read* names what its agent has to read
  to make it besides those files: a file whole, or `<path>:<first>-<last>` where a range is enough,
  such as the entries of a long log the slice rests on. Paths are relative to the repository root;
  none, written without backticks, stands for an empty field.
- *Checks* are commands that can actually run in the product, named with their arguments, and the
  checks the parts touched call for (WAY-13). A slice that changes behaviour names the test it
  starts from.
- Order the slices so that each comes after what it depends on. Two slices change the same file only
  where one depends on the other.
- No code: no function body, no test body, no text a file will hold. Name what is to exist — a
  file, a function, a command, a field — and what it is to do, and leave the making to the slice's
  agent.
- *Coverage* maps each required outcome and each item of *To do*, and each row of *Settlements to
  record*, to the slices or entries that meet it. A requirement mapped to nothing is a gap in the
  plan, never a question for later.
- *Choices* holds each choice of how to make the change that the plan takes, with the way rejected
  and what it costs if wrong; the orchestrator copies them into the cycle record.

## 4. Check the size of each slice

From the repository root run `python -B <the-way>/task-cycle/slice_size.py <plan>` — in a product
`.the-way/task-cycle/slice_size.py`. Split every slice it reports `too large`, fix every path that
leaves one `unchecked`, and run it again until every slice fits. A slice the script lets through
can still be too large for its agent: it measures only what is read and how many files change.
Keep the last report beside the plan as `plan-size.md`.

## 5. Return

Return to the orchestrator with the plan's path, the script's last report and the questions still
open, each with the answer you propose and its reason. The boundary is the finished plan: return
before any slice is made.

## Writing the plan again

- After a spec: write a new plan from the spec and the task; nothing of the earlier plan binds.
- After a slice proved too large: its code is gone (WAY-136). Split that slice in the plan, keep
  the slices already made and reviewed, and run the script again; the report of the slice's agent
  says where the size lay.
