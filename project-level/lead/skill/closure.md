# Close the project

Read from step 1 of `SKILL.md` when its reconciliation of progress leaves every row of the plan in a
final state, as section 1 gives.

The closing writes into the plan and into notes the human keeps: the note of the next project, the
task place, the plan's change log. It reads the product's foundation and writes none of it, and it
changes nothing of the definition (section 8). A dropped task is one whose row reads
`dropped — approved by human`.

## 1. When the closing starts

The closing starts only when the reconciliation of step 1 of `SKILL.md`, every supported transition
applied with its line in the change log, leaves each row of the plan `done`,
`dropped — approved by human` or `done — goal delivered in task <n>` whose deliveries reach a `done`
task. Following them goes from the task the row names to the task that one names, where its row is
also a delivery, and so on. Read the plan again after the last write of that step, never from
memory.

Where a row stands in any other state — `in cycle` and `ready for cycle` among them — or is
`done — goal delivered in task <n>` whose deliveries never reach a `done` task, the closing does not
start: tell the human which row, by its number and name, and in which state, or that its deliveries
end in a dropped task or run in a loop, holds it, and go on with the rest of the skill. A dropped
task establishes no delivery and a loop establishes none, so the second kind of row is reconciled
with the human before any preview, as the plan template gives.
Where every row is final, tell the human that the project is ready to close and go on with
section 2. Nothing is written before section 6 has the human's acceptance.

## 2. What the closing item and the moves are made of

Read, and write nothing yet.

- **The counts.** Count apart the rows `done`, the rows `done — goal delivered in task <n>` and the
  dropped rows.
- **The scope not delivered.** Number the top-level list items of the definition's `In scope` from 1,
  as `project-level/plan_check.py` numbers them. An item is delivered where a task whose row is
  `done` or `done — goal delivered in task <n>` names its number in its `In scope` cell. List each
  other item with its number and its text.
- **What goes with a dropped task.** For each dropped task: its `Goal` cell word for word; each open
  question of the plan that ends `— plan: task <n>` for it, word for word with the place the
  definition gives it; and each projected entry whose `Written by` cell names it, even where a
  finished task also realizes the entry.
- **The foundation at a commit, for each such entry.** Take the commit from the line
  `integration: <ref> <commit>` that `project-level/plan_state.py` printed at this session; where it
  printed none, ask the human which commit of the product to search. Read the foundation files at
  that commit with git, never in the working tree. Search them by the key the plan keeps word for
  word in the entry's heading: for a decision `(new) — <question>`, the decision headings that hold
  the same question; for a change of a current decision, its number; for any other entry, its
  identifier or term. The wording of the entry's sentences is no key to search by. Then read the
  text of what the search finds and compare it with the projected change, since an entry that
  stands under the identifier of a change to a current entry stands whether or not the change was
  made. The result is one of:
  - the entry is absent: write `absent from the foundation at commit <commit>`;
  - the entry is found and holds the projected change: name it by its identifier, and where it holds
    only part of it because another task wrote that part (WAY-126), say it is partial and which part;
  - an entry stands under that identifier or term and does not hold the projected change: write that
    it stands at the commit without the change, and which part is missing;
  - a hit that cannot be told to be the same entry or to hold the change: put it to the human in the
    preview, with both texts, as a question, and write nothing for the entry until it is answered.

## 3. The place of each dropped task

For each dropped task the human chooses one of three places, as a question of decision "How a skill
asks" gives it, naming what each costs. The closing writes the move itself, only after the
acceptance of section 6. A plan with no dropped task has nothing to place, and sections 3 and 4 do
not apply.

1. **The next project.** The product's place for projects is the line `Projects` of its `## Backlog`
   section, found as `project-level/backlog_place.md` gives. The human names the note of the next
   project. Where that note exists, add a section about the task to it; create a file in the place
   for projects only where no such note exists. Where a section about this task already stands in
   the note, complete it and add no second one.
2. **A task of its own.** Create the task document in the task place, in the state `refining`, in
   the full layout of `project-level/task/template.md`, with `Project relation: source only:`
   followed by the definition. The task's line in the task place stays where it already stands, and
   the closing changes in it only what the rules of the task place allow, found as
   `project-level/task_line.md` gives, and links the new document only where those rules allow it
   and the preview shows it; it makes a new line, as that file gives, only for a task that has none.
   Where the plan's `Document` cell already links a task document for the task, the closing makes no
   second document in silence: the preview shows the existing document, with its path, its
   `Status:` and its `Project relation:`, and asks the human which document stands. The existing
   document is changed only as the human says in the preview.
3. **Given up for good.** The human gives a reason, which the closing item records. Nothing else is
   written for the task.

## 4. What travels with the task

To a note of the next project and to a task document go the task's goal, its questions of the plan,
and each projected entry that goes with it, with the result of the search of section 2, and a
reference to the closing item: the plan's file name, its change log and the date of the closing.
Where the plan's `Document` cell links a task document for the task, the section or the document
also refers to it, since it holds the answers given while the task was refined; a new document
carries that reference under *Context*.

- In a note, one section named for the task holds them.
- In a task document, the goal stands under *Need*, the questions under *Questions carried to
  cycle*, each projected entry under *Decisions in play* with its wording copied from the
  definition as the template gives for a task that uses a definition as a source only, the
  reference under *Context*, and every other section as the template gives for what is not yet
  known, `TODO` or `none`.

A question of the plan keeps its line in the plan's `Open questions` unchanged (WAY-145); where it
went is told by the closing item.

## 5. The closing item

The closing adds to the plan's change log one item, with the date of the closing and four nested
items, each of the last three reading `none` where nothing is to list. The words `project closed`
and the labels before each colon are markers kept in English; the rest is in the language of the
plan.

```markdown
- YYYY-MM-DD — project closed — <one sentence: the project closes with its tasks done, delivered in another task or dropped>
  - tasks: <a> done, <b> done — goal delivered in another task, <c> dropped
  - dropped: task <n> `<name>` — <its place: the note of the next project, the task of its own, or given up for good with the reason the human gave>
  - not delivered: item <k> of In scope — <its text>
  - projected entries a dropped task was to write: `<heading>` (task <n>) — <the result of the search of section 2>
```

Put one `dropped:` line for each dropped task, one `not delivered:` line for each item left over and
one line of the last kind for each projected entry that goes with a dropped task. The closing item
keeps a closed plan from passing as one whose whole scope is done.

## 6. The preview and the acceptance

Before it writes anything, show the human, in conversation, the whole of what will be written: the
text of the closing item, the change of the `Status:` line from `handed over YYYY-MM-DD` to
`closed YYYY-MM-DD`, and the full text of each move — the section for a note, the new file, the
task document, the change of a line or the new line. Put each doubtful hit of section 2 as a
question beside it, and each existing task document of section 3 with its question. Ask the human to
accept it. The choice of places in section 3 is no acceptance: write nothing until the human has
accepted the whole. A change the human asks for is made in the preview, and the whole is shown
again.

## 7. Writing

After the acceptance, write in this order: each move, the closing item, and last the `Status:` line
as `closed YYYY-MM-DD` with the date of the closing item, so that a plan reading `closed` always
holds its closing item and its moves. Run `project-level/plan_check.py` on the plan and
`project-level/plan_state.py` as step 1 gives; the first finds nothing and the second says the plan
is closed. Resolve a finding before you tell the human the project is closed.

A closing interrupted between writes leaves the plan reading `handed over`: finish the writes the
accepted preview gives, completing a section or a line that already stands and writing none twice,
or show the preview again where it is lost.

## 8. What the closing leaves as it is

The closing never changes the definition: its text, its approval record and its fingerprint stay,
and it goes through no readiness approval again (WAY-118). Where what the project delivered differs
from the definition, the closing item alone says so, by the items of `In scope` it lists as not
delivered. The closing also leaves the plan's rows, its open questions, the lines of the tasks that
are done and the product's foundation as they are.
