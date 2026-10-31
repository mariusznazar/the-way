# The project plan

A project plan breaks an approved project definition into tasks: what each task delivers, what it
depends on, which tasks realize and write each projected entry, and where each open question of the
definition is resolved. The skill in `skill/` beside this file writes it, and
`project-level/plan_check.py` checks what a script can decide of it (WAY-142, WAY-146). The
decisions that set the rules below are cited beside them.

## What a plan is not

- It changes nothing in the foundation and nothing in the definition. The foundation gains each
  projected entry from the task that writes it (WAY-106, WAY-126); a change to the definition goes
  through its readiness gate again (WAY-118).
- It holds no second account of its tasks: no section repeating a task's fields, no table of its
  tasks for a tracker, no field naming the tasks a task can be worked on beside (WAY-142, WAY-144,
  WAY-147).

## Where it stands, and in what language

- The plan stands in the directory of the definition it breaks down, in a file of its own
  (WAY-142, WAY-107).
- Its text is in the language of the definition. The headings, the header lines, the column
  headings, the states and the markers below are in English, whatever that language (WAY-142).

## The form

```markdown
# <plan title>

Status: draft
Definition: <path of the definition, relative to the plan> — fingerprint <8 hex digits>

## Tasks

| # | Task | Goal | Depends on | In scope | Preparatory | State | Document |
|---|---|---|---|---|---|---|---|
| 1 | test-server | <what the task puts in place> | — | 24 | yes | to refine | — |
| 2 | forest-on-hex-grid | <what can be checked in the running product> | — | 10, 21, 23 | no | to refine | — |
| 3 | player-accounts | <…> | 1, 2 | 1, 2, 4 | no | to refine | — |

## Projected entries

| Entry | Realized by | Written by |
|---|---|---|
| (new) — Who can create and use a player account? | 3 | 3 |
| player-save-isolation | 3 | 3 |

## Open questions

- <the question, word for word> — definition: task: <name as the definition gives it> — plan: task 3
- <the question, word for word> — definition: breakdown — answer: <the answer> (<source>)

## Phases

none

## Change log

- YYYY-MM-DD — written from the definition at fingerprint <8 hex digits>
```

The headings stand once each, in this order, and no other second-level heading stands in the plan
(WAY-142).

## The header

- The `Status:` line reads `draft` until the plan is handed to the human, then
  `handed over YYYY-MM-DD` (WAY-142).
- The `Definition:` line names the definition by its path relative to the plan, and the fingerprint
  the definition's gate record holds. A definition whose text no longer gives that fingerprint has
  changed after its gate, and the plan stands on nothing until the definition passes the gate again
  and the plan is checked against it (WAY-142, WAY-118).

## Tasks

One row for each task; a task stands nowhere else in the plan (WAY-142). The columns, in this
order:

| Column | What it holds |
|---|---|
| `#` | the task's number, unique in the plan; other cells name a task by it |
| `Task` | the task's name: lower-case words joined by hyphens, unique in the plan, kept while the plan changes; the task enters its cycle under it, and the cycle names its record by it (WAY-147) |
| `Goal` | one sentence: what can be checked in the running product once the task is done, never a layer put in place; for a preparatory task, what it puts in place (WAY-143) |
| `Depends on` | the numbers of the tasks this one needs done before its cycle starts, separated by commas, or `—`; two cycles can run side by side only when neither task depends on the other directly or transitively. Dependencies do not block refinement (WAY-144) |
| `In scope` | the numbers of the items of the definition's In scope the task delivers — its top-level list items in order, the first being 1 — or `—` |
| `Preparatory` | `yes` for a preparatory task, `no` for any other; a preparatory task stands in the plan only where a task depends on it, and a technical element enters with the first task that uses it or with a preparatory task that task depends on (WAY-143) |
| `State` | one state of the list below |
| `Document` | a link to the task's document, or `—` until its refinement writes one; once the task is `done` and its document is removed, a link to its frozen copy in the product repository at the commit that archives its cycle record, `…/blob/<commit>/docs/task-cycles/<task>/<frozen task file>`, which the plan-state reader compares with that cycle's frozen task |

The states (WAY-142):

| State | When |
|---|---|
| `to refine` | the task has no document ready for its cycle; every task of a new plan reads it |
| `waiting for human` | the task's refinement waits for a human answer, a presented round package or acceptance of the complete document |
| `ready for cycle` | the human has seen and accepted the complete ready task document; unfinished dependencies still block its cycle start |
| `in cycle` | the task's cycle has started |
| `done` | the task's change is merged |
| `done — goal delivered in task <n>` | another task delivered this task's goal |
| `dropped — approved by human` | the human gave the task up |

A row goes back to `to refine` from `in cycle` or `ready for cycle` only as `lead-project` gives,
on the human's word (WAY-267).

During leading, agent turns, `questions` and question-specific `waits for task <n>` leave the row
`to refine`; a presented human package or `ready for approval` makes it `waiting for human`.
The latter is a conversation result, never a new task-document Status. A wait names the question
needing task n's result, is logged with its reason, and is proposed again once n is done;
`Depends on` alone never delays refinement (WAY-144, WAY-154).

A `done — goal delivered in task <n>` dependency supplies completion only when delivery through
the named task is established. `dropped — approved by human` does not establish delivery of its
goal: reconcile the plan before treating it as a satisfied dependency. No task gains
`ready for cycle` while a changed definition awaits its gate and subsequent plan recheck
(WAY-156). Plan states record progress, not permission for the project orchestrator to start cycles.

## Projected entries

One row for each projected entry of the definition, under its heading as the definition's
"Projected foundation changes" gives it after `#### `, word for word (WAY-142):

- *Realized by* names the numbers of the tasks whose work makes the entry true, at least one.
- *Written by* names exactly one of them: the task the plan assigns to write the entry (WAY-146).
  The first task whose code makes the entry true writes it, or the part of it its code makes true,
  and the task the plan assigns writes what of the entry the foundation does not yet hold, and an
  entry no code makes true (WAY-126). Each realizing task carries the entry as projected in its
  document's *Decisions in play*.
- A move that changes which task writes an entry is the human's to decide (WAY-145).
- Two tasks that realize the same entry go one after the other: one depends on the other, directly
  or through other tasks, unless a change log item lets the two go side by side on that entry and
  gives the reason. A pair with a task done, delivered by another task or dropped needs neither
  (WAY-230).

## Open questions

- Each open question of the definition stands as one item: the question word for word, then
  `— definition: ` and the place the definition gives it word for word, then where the plan
  resolves it (WAY-142):
  - `— plan: task <n>` — a task of the plan resolves it;
  - `— answer: <the answer> (<source>)` — the human answered it, the source reading
    `human, YYYY-MM-DD`, or the plan quotes the answer from the definition or the foundation, the
    source naming the file and the section or entry it is quoted from (WAY-145).
- The place the definition gives a question is its first assignment, and the plan decides from
  then on (WAY-145). A question resolved in another task than the one the definition names has a
  line in the change log giving the reason (WAY-145).
- A question that arises only in the breakdown goes to the human before the plan is handed over,
  and stands with `— definition: none` and the human's answer or the task the human places it in
  (WAY-145).
- A definition with no open questions leaves the section reading `none`.

## Phases

`none`, or one item for each phase: its name, the numbers of its tasks and what closes it
(WAY-142).

## Change log

One item for each change of the plan, oldest first: `- YYYY-MM-DD — <what changed> — <why>`. The
first item records that the plan was written and the fingerprint of the definition it was written
from (WAY-142).

Two tasks that realize the same projected entry go side by side, with no dependency between them,
only where an item in this form lets them, one item for each entry they share, the entry's heading
word for word as the definition gives it, a `|` written as itself, and the reason in the
definition's language (WAY-230):

```markdown
- YYYY-MM-DD — side by side: tasks <n>, <m> on "<entry>" — <why>
```

The breakdown shows each such item to the human when it hands the plan over (WAY-230).

## What the check decides, and what the critique judges

`plan_check.py` rejects a plan whose form it cannot read — the header, the sections, the columns,
the states, the names — and a plan in which a projected entry has no task realizing it or not
exactly one of them writing it, an item of In scope has no task, a task depends on a task the plan
does not hold or on itself through other tasks, a preparatory task has no task depending on it, two
tasks neither done, delivered nor dropped realize the same projected entry while neither depends on
the other and no change log item lets them go side by side on it (WAY-230), or an open question of
the definition does not stand word for word with a task or an answer (WAY-146; invariants
`project-plan-form` and `project-plan-check`).

The plan's independent critique judges what no script tells apart: whether each task that is not
preparatory ends with something checkable in the running product, whether each technical element
enters with the first task that uses it, whether each question stands where the definition puts it
or the change log gives its move, and whether a quoted answer settles its question (WAY-146). A
check a script can make is never left to the critique (WAY-146).
