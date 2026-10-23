---
name: plan-task
description: Use when a ready the-way task's change has to be divided into slices before it is made — after the cycle selects planning from the frozen task or a reviewed spec, or a one-author change or planned slice proves too large. Not for a project's plan of tasks, and never writes code.
---

# Plan a task's change

Writes the plan of one task's change: the foundation entries written before any code, and the
change divided into slices, each made by an agent of its own (WAY-136). A slice the plan marks as
touching a trust boundary or holding an operation that cannot be undone is reviewed by another
agent; the review of the whole change judges the rest. The plan holds no code. The cycle that
calls this skill, `implement-task`, holds the dispatch, the record and every stage after the plan;
this skill holds only how the plan is written.

This skill lives in `task-cycle/plan/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in, the directory `git rev-parse --show-toplevel` prints in the
session's working directory; in a product, it is the product's pinned `.the-way`. The script
`task-cycle/slice_size.py` is there, and each skill named below is the project skill of that name
with the `the-way-` prefix.

The planner is a fresh agent the orchestrator of `implement-task` dispatches when the change
needs division, including after a reviewed spec or an oversized one-author attempt (WAY-136).
A change one agent can hold is made without this skill or a preliminary plan; the cycle's
orchestrator makes that judgment from the task document. The planner writes only the
plan file the dispatch names, normally `.runs/task-cycles/<task-slug>/plan.md`, and sends its
questions back to the orchestrator; it never writes code, a test or a foundation entry, and never
asks the human.

## 1. Read

- The dispatch: the plan path, the report path, and what it names for you to read.
- The frozen task document whole — its outcome, *To do*, answered questions, *Questions carried to
  cycle* and the rows of *Settlements to record* — and the spec, where the cycle wrote one, whole:
  you divide the whole change. The spec binds where it settles more than the task, and the task
  binds where they differ.
- What the dispatch names of the task's sources — the approved project definition's projected
  entries the task carries or its plan item assigns — of the product's foundation, by identifier,
  and of its guidelines, each guideline file whole (WAY-150, WAY-213). Name in your report what you
  find missing or uncertain in the guidelines. With the styleguide read its order-of-work example,
  follow it or explain the departure; it is no required slice order.
- Where you need something the dispatch does not name, reach for it selectively: search for its
  identifier or a word and read the passage found — a foundation entry whole, never a whole file of
  the foundation; a guideline file of a further part whole (WAY-213). Name each reach in your
  report: what, where and why.
- The code and the tests the change touches, as far as is needed to name each slice's files and
  what each slice's agent has to read. Read to cut slices, not to design the code.
- After a one-author attempt proved too large, its report; the whole attempt, foundation entries
  included, has been discarded. After a planned slice proved too large, its report and plan;
  the slices already made remain, reviewed where their *Risk* called for it.

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
- **Read:** `<path>` · `<path>:<first>-<last>` <identifier or heading> · <identifier>
- **Model:** cheaper | same — <reason> | strongest — <reason>
- **Risk:** none | trust boundary — <which> | cannot be undone — <what> | trust boundary — <which> ·
  cannot be undone — <what>
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
  check too; one agent may write the sentence, its test and the code the test covers (WAY-69).
  Write `none` under the table where the change writes no entry. The plan names entries; it never
  words them.
- A slice is narrow: one goal, the files that goal changes, and checks that run when it is made. Cut
  along what a reviewer can judge alone. Its section is what its agent gets of the plan: the
  orchestrator copies it into the handoff word for word, and the agent does not open the plan
  (WAY-148); write it so that the agent can make the slice from that section and its *Read* alone.
  If the selected planning route yields only one useful
  slice, keep it as one; never add a slice for its own sake or divide inseparable work.
- *Change* names every file the slice changes or creates. *Read* is the whole reading of the
  slice's agent besides those files, since its handoff carries what *Read* names — the passages
  copied word for word, the entries and files by their address (WAY-148, WAY-150):
  - the passages of the task, the spec and the plan the slice needs beyond its own section, each as
    `<path>:<first>-<last>` — a whole section, or the lines of the items it needs — followed,
    outside the backticks, by the section's heading written without backticks, so that it can be
    found again once the file changes;
  - the foundation entries "Reading the foundation" selects for the parts the slice touches — their
    decisions and part-map entries, the invariants the slice reaches (WAY-62), the entries these
    link to as far as the slice needs and the glossary entries of its terms — and the entries the
    task names that bear on it: each as a range that contains the complete entry, all fields,
    rationale and rejected options included, since a search hit or paragraph cannot stand for it,
    followed by its identifier outside the backticks, such as `foundations/decisions.md:120-148`
    (WAY-12). The identifier is the entry's address and the range only its size at the plan's base;
    an entry the plan's *Foundation entries* writes is named by its row there, without backticks,
    since it does not exist yet and a new entry gets its identifier only when written;
  - the guideline files of the parts it touches, each whole, as `product-guidelines/reading.md`
    selects them (WAY-213);
  - a file of code or tests the slice needs, whole or as a range.

  The orchestrator checks *Read* in its review of the plan and may add to it. Paths are relative to
  the repository root; none, written without backticks, stands for an empty field.
- *Model* sets the class of model the slice's executor works on (WAY-229): `cheaper` than the
  orchestrator's — the default, for a slice that carries settled matters into code, such as
  applying a pattern the spec or the guidelines settle, a rename, or tests from an existing
  example; `same` as the orchestrator's — for ordinary implementation that takes decisions of its
  own; `strongest` available — for a change across many parts or one that needs design. A class
  other than `cheaper` carries one sentence of its reason after a dash. Name a class, never a
  model.
- *Risk* says whether the slice touches a trust boundary — files the part map names as one
  (WAY-48) — or holds an operation that cannot be undone (WAY-13), naming which, both on one line
  where both hold; `none` where it does neither. A slice with a risk gets a review of its own,
  except a plan's only slice, whose review is the review of the whole change; every other slice is
  judged by the review of the whole change (WAY-136).
- *Checks* are commands that can actually run in the product, named with their arguments. A slice
  that changes behaviour names the test it starts from.
- Order the slices so that each comes after what it depends on; the slices are made one after
  another in that order. Two slices change the same file only where one depends on the other.
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
Since *Read* is the whole reading of the slice's agent, the size it reports is what that agent
reads besides its section of the plan.
Keep the last report beside the plan as `plan-size.md`.

## 5. Return

Write the full report to the dispatch's report path, including the final size-report path,
guidelines found missing or uncertain, the chosen order's relation to the styleguide example, each
reach beyond the dispatch, and any questions still open with proposed answers and evidence. Return
under the cycle's file-transfer contract (WAY-148): the status, the plan's path, a one-line check
result naming failed or unchecked work, and the report's path; concerns stand in the report. The
status is `done`; `done with concerns` where the report holds a concern, a reach or a guideline
found missing or uncertain; `questions` where the plan waits for answers, written in the report;
or `returned` for an open design choice (section 2). The boundary is the finished plan: return
before any slice is made.

## Writing the plan again

- After a reviewed spec, only if the orchestrator selects planning again: write a new plan from
  the spec and task; nothing of an earlier plan binds. The same size judgment can instead send
  the settled change to one author without a plan.
- After a one-author attempt proved too large: its whole attempt, including its foundation
  entries, is gone (WAY-136). Divide the change from the task, any reviewed spec and its report;
  there is no completed slice to preserve from that attempt.
- After a slice proved too large: its code is gone (WAY-136). Split that slice in the plan, keep
  the slices already made, and run the script again; the report of the slice's agent
  says where the size lay.
