---
name: plan-project
description: Use when an approved project definition of a product that uses the-way has to be broken into tasks — the breakdown that writes the project plan, a plan to resume from its status line, or a plan to check again after its definition passed the readiness gate anew. Not for a task's plan of slices, and never refines a task.
---

# Plan a project

Leads the breakdown: the step after the readiness gate that turns an approved project definition
into its plan — the tasks, what each depends on, which tasks realize and write each projected
entry, and where each open question is resolved. The form of a plan and the rule of each part stand
in `project-level/plan/template.md`; how a skill asks stands in `elements/common/way_of_working.md`;
this skill holds the order of the work. The decisions that set its rules are cited below.

This skill lives in `project-level/plan/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The project
level's directory, `project-level/`, is there, and each skill named below is the project skill of
that name with the `the-way-` prefix.

The breakdown reads the product's foundation and the definition and writes nothing in either
(WAY-106). It writes no task document; each task is refined later through `refine-task`.

## Delegated work while leading a plan

When `lead-project` dispatches you through a refinement conversation path, read that file and
`project-level/lead/conversation_template.md` first. Verify its product, plan and process pin,
read all turns and the requested change, and follow this workflow with these routing differences
(WAY-156):

- Own the structural plan edit while your turn runs. The project orchestrator pauses its own
  State/Document/log writes; refiners write only separate task documents/conversations. Edit no
  task body, definition or foundation. Record each plan change with its reason and run the
  existing whole-original checks; preserve stable task names and unaffected states.
- Return every human question, scope choice, projected-entry writer reassignment and handover
  request through the conversation with complete material, ways/costs/recommendation as applicable,
  then return to the project orchestrator. Its recorded human answers authorize only the choices
  they actually settle. Do not speak to the human, approve on their behalf or start child agents.
- Request step 6's independent critique through the file, including the complete authoritative
  plan and source paths. The project orchestrator dispatches it and records its report for you;
  verify and settle its observations as step 6 requires. Missing critique remains a block.
- After a definition's new gate, start at step 0 and recheck the plan from its complete inventories
  against the newly approved definition, completing all affected steps and required critique and
  human decisions. The old fingerprint mismatch shows the recheck needed; once the new gate is
  verified, update the plan's fingerprint with its logged reason rather than demand another gate
  for that same approved change. Return check results, source identities, changes and next action
  through the conversation. No task gains readiness while the gate/recheck remains pending.

## 0. Start or resume

- Read `project-level/plan/template.md` in full, and the section "How a skill asks" of
  `elements/common/way_of_working.md`.
- When the human names an existing plan, run
  `python -B <the-way>/project-level/plan_check.py <plan>` on the original whole file and read it
  by "Reading the definition and plan" below (WAY-151). A plan whose status reads `draft` goes on
  from the first step its sections leave unfinished; a plan handed over changes only as its
  change log records, and a finding that the definition's fingerprint no longer matches means the
  definition changed after its gate: it goes through `define-project` step 7 again, and the plan is
  checked against it from step 1. If the definition has already passed that new gate, verify its
  approval and proceed with that recheck rather than reopen the same gate.
- Otherwise begin with step 1.

## 1. Read

- Run `python -B <the-way>/project-level/readiness_check.py <definition>` on the original whole
  definition; it must report nothing. A finding returns the definition to `define-project`, and
  the breakdown waits; so does an In scope that holds no list of items for the plan to number.
  Read the definition by "Reading the definition and plan" below (WAY-151).
- Select and read the product's current foundation by "Reading the foundation" in
  `elements/common/way_of_working.md` (WAY-150), including the decisions the definition names.
  The complete part map's *Depends on* tells which work has to come first.
- Read the product's files only as far as the cut needs: what is already there, so that no task
  puts in place what exists.
- Read the product's guidelines of the parts the approved scope touches by
  `product-guidelines/reading.md` (WAY-218), each whole, and keep what it finds missing or
  uncertain in the working evidence.

## Reading the definition and plan

The original definition and plan remain authoritative (WAY-151). Run every readiness, fingerprint
and plan check on those whole files at their original paths, never on selected excerpts or a
reduced copy. Selection is no reading cap; read a small file whole where useful.

- Before choosing work at start or resume, inspect the complete heading structure, status and
  header, gate record and document revisions. Inventory every top-level In scope item in its
  original order and numbering, every projected-entry heading, and every open question with its
  exact wording and assigned place. For an existing plan, inventory every task's number, name,
  state and dependencies, every projected-entry realizing and writing assignment, every question
  with its placement or answer, and the locations of phases and change-log content.
- Accumulate the complete inventories in manageable batches with ordinary file/search tools.
  Read table rows and question items as complete units, including wrapped continuations. Keep
  their source revisions and locations in temporary working evidence; this is no second plan or
  maintained product format. Refresh the inventories when either source changes.
- Use status and unfinished sections to choose where to resume. For that work, read complete
  scope items, task rows, projected entries and questions, with dependency and assignment context.
  Read relevant Goal, Background, Out of scope, Inputs and constraints, Deliverables, Success,
  Risks, Touched parts and decisions, and Technology content. Read a projected entry whole before
  assigning what makes it true or writes it. Read a quoted answer at its original definition or
  foundation source, with the context needed to judge its meaning; a summary cannot settle unseen
  source meaning.
- Expand whenever a choice, boundary, dependency, source reference or ambiguity may change the
  cut or a question's interpretation. Before a resumed edit, read every other row, assignment and
  question its dependency or meaning reaches, even far from the unfinished section. A new complete
  breakdown processes every scope item, projected entry and exact question: batching brings in
  context when needed and omits none of the project. Whole-plan checks run after a change.

## 2. Cut the tasks

- Cut the definition's In scope into tasks, each ending with something that can be checked in the
  running product, never with a layer put in place (WAY-143). A large task is split; its size
  chooses nothing else (WAY-13).
- Bring a technical element in with the first task that uses it. Write a preparatory task only for
  work that task cannot start without, and make that task depend on it (WAY-143).
- For each missing styleguide or general coding file found by the shared reading, place a
  guidelines task before its consumers and make them depend on it; reuse an adequate task the
  plan already holds. Respect scoped departures and the guidelines-writing task's exemption.
  Assign a genuinely first kind's exemplar, kind guidelines and index row to the task creating
  its first file, not to a separate prerequisite; an existing unindexed kind needs WAY-200's
  comparison through `maintain-coding-guidelines`. Keep extensions of existing guidelines with
  their consuming task unless the human separates them. Follow step 5 for questions or work
  beyond the approved definition, never silently enlarge it. Refinement checks these findings
  again and waits for a prerequisite's merge only where its question needs that result.
- Give each task its number, its name and its goal in the definition's language, the tasks it
  depends on and the items of In scope it delivers, as the template gives them (WAY-147, WAY-144).
  Every task of a new plan reads `to refine`.
- `Depends on` constrains cycle starts, not refinement: a cycle starts only when its dependencies
  are done, and cycles run beside one another only when neither depends on the other directly or
  transitively. Dependent tasks may be refined together; a refinement waits only for a named
  question needing another task's result (WAY-144).
- Something the definition leaves out that the cut seems to need is a question for the human in
  step 5 (WAY-145).

## 3. Assign the projected entries

- Give every projected entry of the definition its row: the tasks whose work makes it true, and
  the one of them that writes it into the foundation (WAY-142, WAY-126).
- An entry no task of the cut makes true shows a task missing or an entry the project does not
  need; either is a question for the human in step 5, never an entry left without a row.

## 4. Place the open questions

- Write each open question of the definition, word for word, with the place the definition gives
  it, and give it its place in the plan (WAY-142, WAY-145):
  - a question the definition sends to a task goes to the task of the plan the definition's words
    name; where the cut puts it in another task, write a line in the change log giving the reason;
  - a question the definition sends to the breakdown is answered here, by the human or by a quote
    from the definition or the foundation naming where it stands, or goes to a task; never answer
    it from your own reading of the code.
- A move that changes which task writes a projected entry is a question for the human in step 5
  (WAY-145).
- A question that arises only in the breakdown is a question for the human in step 5, and stands
  with `— definition: none` once answered or placed (WAY-145).

## 5. Write, check and ask

- Write the plan in the definition's directory with the status `draft`, the fingerprint
  `python -B <the-way>/project-level/readiness_check.py <definition> --fingerprint` prints, and the
  first line of its change log. Give its full path in the same message.
- Run `python -B <the-way>/project-level/plan_check.py <plan>` and fix each finding; it must report
  nothing before the critique.
- Ask the human, in one round, what steps 2–4 left for the human: questions that arose in the
  breakdown, moves that change which task writes an entry, a task or an entry the definition leaves
  unsettled. Write each answer into the plan, with its line in the change log where it changes the
  plan, before the next question.

## 6. The critique

- Run `critique` once on the exact authoritative plan, with the definition, the product's complete
  part map, relevant foundation and applicable rules as its sources (WAY-120, WAY-146, WAY-151).
  The critic reads the complete plan, in manageable batches if useful, and every source unit
  needed for all tasks, technical elements, question moves and quoted answers. The author's
  selection and inventories never limit the critic's inspection; complete the whole plan's
  semantic judgment before reporting the critique complete. Ask it to judge, besides what that
  skill checks, what no script tells apart: whether each task that is not preparatory ends with
  something checkable in the running product, whether each technical element enters with the first task that uses it, whether each
  question stands where the definition puts it or the change log gives its move, and whether a
  quoted answer settles its question. Never ask it what `plan_check.py` decides.
- Verify each observation, give each a verdict, and correct the plan; a correction that changes a
  human's answer, or which task writes an entry, goes back to the human. If an independent critic
  cannot run, say so and wait; the author's own reading does not stand for it.
- Run `plan_check.py` again; it must report nothing.

## 7. Hand over

- Show the human the whole table of tasks, the questions answered or placed in this breakdown, each
  move from the definition's placement with its reason, and each remark of the critique you
  rejected with why. The human corrects the plan; apply each correction, with its line in the change
  log, and run `plan_check.py` again.
- On the human's word, set the status to `handed over YYYY-MM-DD` and add the line to the change
  log. Point to `lead-project` as the next step: it proposes human-confirmed rounds, delegates
  member-task refinement through `refine-task` and maintains evidenced plan states (WAY-152).
  The human starts cycles separately, under each task's stable name (WAY-147); leading starts
  none. In delegated mode return this handover material through the conversation.
