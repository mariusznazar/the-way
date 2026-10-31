# A project refinement conversation

One ignored file at `<product-repository>/.runs/project-refinement/<task-name>.md` carries one
plan task's refinement (WAY-154). Use the stable plan name. Before creating or resuming it,
verify the repository, plan and task identity; do not overwrite a same-named task of another
plan. Resolve all paths without session history. The instructions below belong to the checkout
being worked on, or to the product's pinned `.the-way`, not a global skill copy.

Headings, fields, result phrases and `none` / `TODO` stay in English. Write questions, proposed
task text and human answers in the task's language. Replace placeholders with sourced values;
examples and recommendations are never human decisions. Sections without material say `none`.

## Ownership and turns

- The project orchestrator initializes the header, chooses the next actor and serializes writers
  on each file. Parallel refiners write different conversations/tasks; one answering agent reads
  the whole round after refiners return. Dispatch supplies only this file's path and minimal
  actor/stage routing; all source paths, questions and previous answers are read here.
- A refiner follows `project-level/task/skill/SKILL.md` in orchestrated mode. Only it creates or
  changes this task document's body. It writes its numbered turn, questions and human material,
  checks sources and copies resolved answers with provenance and the ways the human did not choose
  into the task's Questions to settle.
  It never writes the shared plan, definition or foundation, asks the human, starts a child agent,
  launches implementation or records its own recommendation as acceptance.
- The answering agent follows `project-level/lead/answering.md`. It fills answers below questions
  and prepares human questions in these files; it edits no task document, plan or foundation.
- The project orchestrator records the human's words, question IDs and explicit acceptance or
  rejection separately from sourced answers. It presents one round package including every
  document quotation answer as question, quotation and source, candidates, Human-action placement
  and complete proposed wording. A struck quotation becomes an unanswered human question.
  It dispatches required independent critique of the complete proposed set before presentation;
  refiners return any required child-work request here instead of dispatching children.
- Candidate selection, placement/completion of Human actions, required questions against choices
  (WAY-113) and acceptance of the complete final document are separate acts. Record each; an
  accepted package, candidate row or another task never approves this complete document.

Append numbered turns; never erase an unanswered question or replace a human answer with an
agent's inference. IDs such as `Q1` are stable within this file; identify a cross-file question by
its absolute conversation path and ID. For a duplicate choice, keep one canonical question and
list every affected task/ID in both files. A request for a run of the step that settles technology
is no question: where two members name one choice with the same scope, one request is marked
canonical with its affected tasks, as for a question. Keep distinct scopes separate. Copy the canonical
answer itself, its original source and its ways not chosen into every affected task, not only a
link to this file.

On resumption, read the header and all turns, check source revisions and pending human material,
then continue from the recorded next actor. An unfinished write, missing source/capability,
changed answer or conflicting source is visible unfinished work, never inferred approval. Reopen
an affected question when its source no longer holds. A human-struck quotation cannot be reused
as a settled answer. No source or child capability means a concrete obstacle/request with what
will resolve it, not a fabricated settlement or nested dispatch.

## Fillable file

```markdown
# Refinement: <task-name>

Product repository: <absolute path>
Process: <absolute checkout or pinned .the-way path> - commit <revision>
Plan: <absolute path>
Definition: <absolute path>
Task: <number> - <stable task-name>
Task document: <absolute path, or not yet created>
Round conversations:
- <absolute path, including this file>
Next actor: refiner | answering agent | project orchestrator
Instructions:
- <absolute process path>/project-level/lead/conversation_template.md
- <absolute process path>/project-level/lead/answering.md
- <absolute process path>/project-level/task/skill/SKILL.md - orchestrated mode

## Turn <number>

Actor: <refiner | answering agent | project orchestrator>
Sources checked: <file/entry/section and revision or content identity; findings, or none>

### Questions

#### Q<stable number>

Question: <complete question>
Blocks: <what cannot be stated or done without the answer>
Asks: how the product is | how the product is to be
Affected tasks: <task numbers, conversation paths and question IDs>
Canonical question: <this question, or absolute conversation path and ID>
Answer: TODO
Answer kind: pending | document quotation | code fact | human
Source: <exact document location and revision; code file:line and revision; or human and date>
Answer review: pending | supplied | struck by human | resolved
Human question: <if unresolved: full question, options, costs of each and recommendation;
  for assessment an open question; otherwise none>

### Human material

Candidates: <complete candidate table with the five columns from Settlements to record,
  plus each row's stable ID, waiting/accepted/rejected state and human source; or none>
Human actions: <each action, proposed placement and reason, human placement/completion or TODO>
Wording: <complete current task document for wording/final review, or exact proposals; or none>
Questions against choices: <choice ID, quoted anchor, complete WAY-113 question and answer,
  or the applicable exception with its reason; or none>
Technology run: <the list of choices to confirm and the table of choices with consequences, once
  a run has produced them, each choice with its stable ID and waiting/chosen state; or none>
Child-work requests: <needed critique or other delegated work and full paths of material; for a
  run of the step that settles technology, the choice, the note the run is for and the path of this
  task document; or none>

### Human answers

<question/row IDs, date, the human's exact words and explicit acceptance/rejection; or none>

### Transfer and final acceptance

Transferred: <question IDs, durable task locations, original sources and ways not chosen; or none>
Final document acceptance: <pending, rejected with requested changes, or human/date/exact words
  accepting the complete document identified by path and revision/content identity>
Evidence and next step: <reason for result; exact blocking question/task, requested change or
  obstacle and what resolves it; readiness checks where applicable>

<one exact refiner result phrase>
```

The five refiner results are closed; the final nonempty line of its turn/file and its short
return are identical, with no extra label or punctuation (substitute the actual task number):

| Result | Evidence and routing | Plan state |
|---|---|---|
| `questions` | Questions or human material remain; next the round answerer, then the project orchestrator for human material. | `to refine` during agent turns; `waiting for human` when the package is presented. |
| `waits for task <n>` | A named question needs the result of task n, which exists in the plan; retain the question/reason in the task and conversation. The project orchestrator logs the wait and proposes the task again when n is done. Dependencies alone do not block refinement. | `to refine` |
| `ready for approval` | All applicable refinement checks pass except final acceptance of this complete document; next the project orchestrator presents it whole, one document at a time. | `waiting for human` |
| `plan change` | Name the source mismatch and requested plan/definition change for the owning workflow; do not expand the task silently. | No implied readiness; keep the unfinished state until routing is settled. |
| `obstacle` | Name the missing source/capability or unresolved conflict and what resolves it. | No automatic advancement; human waiting only when their answer is needed. |

These results are not task-document Status values. A refiner never writes `ready for cycle` in
orchestrated mode. Answering/project-orchestrator turns record their next step without inventing
a refiner result or claiming readiness.

## Acceptance and cleanup

Record human acceptance of the exact complete document before any final status writes. The
project orchestrator then changes only its `Status:` line to `ready for cycle`, updates the plan's
State/Document cells and logs acceptance; it changes no task body. A requested correction returns
to a fresh refiner and a changed document needs renewed complete-document acceptance. No task
becomes ready while a definition gate is open or a required refinement check remains unmet.

Before removing this exact file, verify that all resolved answers and original sources, the ways
the human did not choose, accepted candidate meanings and necessary task information live in the
task document. Verify transfer of
canonical answers into every affected task and that no surviving conversation relies on an
answer available only here. Delete only this conversation, never sweep its directory. If transfer
is incomplete, resume a refiner first. After interruption, reconcile the recorded acceptance,
its exact document and actual task/plan status without inferring acceptance from an empty list.
