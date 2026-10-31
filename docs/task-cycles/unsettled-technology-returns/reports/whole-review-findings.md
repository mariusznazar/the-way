# Findings of the review of the whole change

Copied word for word from `reports/whole-review.md`, whose first line is `FAIL e21d286`. The reviewer's
grades and scope stand. Minor findings and those outside the scope are not fixed.

#### 1. A second run's note is lost at a document that already has a section *Technology*

- **Place:** `project-level/technology/task_run.md:24-34`, and *Close* at `:79-87`.
- **Comes from:** slice 1, `6fb58f6`. The spec's decision 1, "Resuming", is silent on it too, and
  silence is not permission.
- **Requirement:** To do 8 and To do 1. The template and spec keep "one item for each run's note",
  so several runs at one document are designed for.
- **What is wrong:** *List* is entered in two cases only: the document has no section, or the human
  adds or changes an item when shown the list. A run given a new note at a document whose section
  already holds a list is told neither to write the note nor to list its choice. Where every item
  is settled, `:34` sends it straight to *Close*.
- **Example, followed literally:**
  1. A task's refinement settles "where accounts are kept", so its section reads `— settled: ...`.
  2. The cycle meets an error tracker, stops and opens a blocked draft. The human closes it.
  3. `draft.md:15-18` makes the named choice the note, and `resolve_gaps.md:29-30` runs the step.
  4. `task_run.md` shows the list, finds no open item and goes to *Close*: no item is open, return
     to step 3.
  5. `final_review.md` finds no `— open`, so the document can be accepted with the choice that
     stopped the cycle still unsettled and its note unwritten. The next cycle stops on it again.
- **Why it matters:** this is the return path the task exists to build. It works only if the human
  happens to add the item when shown the list, and the list does not show the note. An open item
  has the same gap in a milder form: the note's choice is not added beside it.
- **Evidence:** hand trace above through `task_run.md`, `draft.md:15-18`, `resolve_gaps.md:23-31`,
  `final_review.md:7-8`. Slice 1's own trace looked for definition-only instructions, so it could
  not catch this.
- **Fix:** in *Start*, before the bullets on a list: a run given a note the section does not yet
  hold writes the note and follows *List* for it, and only then the rest applies.

#### 2. The stage agent that most often meets the choice reads the rule only once it has already decided to stop

- **Place:** `task-cycle/change/SKILL.md:102-116`.
- **Comes from:** slice 4, `dc13d6a`.
- **Requirement:** To do 7, "no stage settles it", and the spec's decision 3, "The moment an agent
  recognises": each pointer names the moment by what the agent sees, the work needing a language, a
  framework, and so on.
- **What is wrong:** the pointer opens "Before you return `returned`, check the first case". An
  executor that takes a new library, store or framework for "a choice of how to make what they
  settle", which `:104-105` calls its own to make, is not about to return `returned`, so it does
  not reach the pointer and never reads `reserved_choices.md`. That misjudgment is the very thing
  the rule exists to catch: today's silent choice in the code. The other two pointers are not gated:
  `task-cycle/plan/SKILL.md:63` and `task-cycle/spec/design.md:18` both open "Where the change/design
  needs". The agent that writes the code is the one left with the weaker form.
- **Also:** a fix's agent reaches the same gate. The spec gives "an agent that cannot remove the
  choice from the change returns `reserved`", but that sentence stands only in
  `task-cycle/skill/reserved_return.md:26-27`, which the fix's agent does not read, and `fix.md` does
  not carry it.
- **Why it matters:** the reviewer stays a second chance, but by then the code stands on the choice,
  the situation the task names. The spec accepts that an agent may miss the moment; it does not
  accept a pointer that fires only after the agent has seen it.
- **Evidence:** reading of the three pointers side by side. Slice 4's own-work check named "no
  method copies the rule", not recognition, so a grep for the path passed it.
- **Fix:** open that paragraph as the other two do, "Where the work needs a language, ...", standing
  on its own before the two cases.

#### 3. WAY-267 says more than the files do, in two clauses

- **Place:** `foundations/decisions.md:7706-7713`, and *Verification* at `:7729-7731`.
- **Comes from:** the plan's *Foundation entries*, `443442f`. The spec's table of entries has the
  same short wording as the first clause; its decision 5 has the qualification.
- **Graded by:** WAY-263: a change's files that fail to do what its entry requires, or a restatement
  more broadly or without a qualification, is Important.
- **What is wrong:**
  - "under the same name" binds every task. Spec decision 5 gives the name only to a plan member:
    "An independent task's cycle names its record as step 5 gives; nothing ties it to the earlier
    name", and step 5 (`task-cycle/skill/SKILL.md:121-122`) is unchanged. WAY-267's own *Rationale*
    argues from a plan's task alone. Its *Verification* lists a numbered name as a breach with no
    such limit, so an independent task's new cycle breaches the entry by following step 5.
  - "says that nothing else ran and why" is false of a stop after a reviewed spec or a slice. The
    file gives "each of the stages above that did not run" (`reserved_return.md:73-74`), and slice 5
    says so in its choice 2 and its searches. The *Verification* list has the same fixed form.
  - Lesser, same sentence: "holding only the commit that adds its record and the commit that removes
    it" omits the commit that moved the pin, which `reserved_return.md:34` keeps. *Verification*
    states it, so this alone would not block.
- **Fix:** "under the same name" limited to a task of a project plan; "says what did not run and
  why"; *Verification* to match. No change to any file but the entry.
