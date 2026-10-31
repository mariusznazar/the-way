---
name: lead-project
description: Use to lead a handed-over project plan through human-confirmed rounds of task refinement and evidence-backed state upkeep, or resume that work from its files. Not for defining or breaking down a project, refining one task directly, running task cycles or closing a project. Requires child agents.
---

# Lead a project plan

You are the project orchestrator: the agent in conversation with the human about a handed-over
plan (WAY-152). Keep its states current and coordinate refinement until the human accepts each
complete task document. The human starts cycles separately. Launch no `implement-task`, perform
no project closure and write no product foundation entries. After a merge, do not recheck ready
dependent documents; the task cycle checks and adapts sources at its own start.

This skill lives in `project-level/lead/skill/` of the-way. In the-way itself use the checkout or
worktree the session works in, which `git rev-parse --show-toplevel` names; in a product use its
pinned `.the-way`, verified against the product's gitlink. Each the-way skill named here is the
project skill with the `the-way-` prefix, never a personal copy.

## 0. Read and recover

- Resolve the product repository, its root `AGENTS.md` and `## Backlog` locations, the original
  plan, its definition and linked task documents. Do not infer the product from the plan's parent
  directory or the process checkout. Read `project-level/plan/template.md`,
  `project-level/task/template.md`, `project-level/lead/conversation_template.md`,
  `project-level/lead/answering.md` and "How a skill asks" in
  `elements/common/way_of_working.md`. The companion files define the single exchange contract;
  do not invent another transcript, tracker or session store.
- Select and read the product's current foundation by "Reading the foundation" in that shared
  file (WAY-150), including the complete part map and whole selected entries. Every dispatched
  actor repeats that method for its work. Read a large definition/plan by "Reading the definition
  and plan" in `project-level/plan/skill/SKILL.md` (WAY-151): complete inventories before selection,
  whole relevant units and expansion; preserve every borrowed skill's mandatory whole reads.
- Require a handed-over plan. Run `python -B <the-way>/project-level/readiness_check.py <definition>`
  and `python -B <the-way>/project-level/plan_check.py <plan>` on the original whole files and read
  their reports. A draft, finding, unreadable source or failed command is an obstacle, never
  agreement. Verify the definition's approved Status and actual human gate record as well;
  fingerprint/check agreement alone does not establish approval. A changed definition follows
  step 5 below; ordinary plan findings return to its
  owning workflow, not a task-body repair.
- Inspect existing `.runs/project-refinement/<task-name>.md` files for this plan. Verify each
  header's repository/plan/task identity before reuse; a same-named task from another plan must
  not be overwritten. Read all turns and source identities, pending human answers, final
  acceptance and next actor. Resume the recorded actor; an interrupted write is unfinished work.
  Reconcile an interrupted final acceptance by step 4, not by inferring agreement from a status.
  Recover a pending definition gate or plan recheck before permitting any readiness writes.
- Require child-agent capability for fresh refiners, the round answerer, independent critique,
  plan changes and definition gates. If unavailable, name the capability and blocked next step
  and wait; do not impersonate these actors, claim an independent review or launch task cycles.

## 1. Reconcile progress

- At every session start run
  `python -B <the-way>/project-level/plan_state.py <plan> <product-repository>` (WAY-153).
  Read repository, fetched integration ref/commit, proposals, exact evidence and all unchecked,
  conflict and error lines. The script only observes Git and never writes the plan. An exit code
  alone does not prove an unchanged or verified state.
- Apply only supported transitions, with a dated change-log line giving reason and evidence:
  `ready for cycle` to `in cycle` from the exact working/archived cycle trace, and `in cycle` to
  `done` from the record commit reachable in freshly fetched integration history. Both may be
  supported together for a stale ready row; log both without requiring an intervening run.
- Resolve outcomes Git leaves unchecked through the PR route the product chose. A verified
  merged PR supplies its actual link and completion evidence; an open PR proves no completion.
  If the tool is unavailable, ask the human with the collected evidence. A closed-unmerged PR or
  conflicting trace goes to the human without automatic correction; a failed fetch or lookup
  cannot become `done`. Do not invent a PR URL or use branch names as proof.
- You own ordinary State/Document-cell updates and their change-log entries. Pause these writes
  while a delegated structural plan edit owns that file (step 5). Run `plan_check.py` after plan
  changes and resolve findings before relying on them.
- If the last task is `done`, including an established goal delivered through another done task,
  tell the human that project closure is next and no closure skill exists. Stop there. Do not
  equate a dropped task with a delivered goal or perform closure or implementation.

## 2. Confirm a round

- Propose tasks still needing refinement, ranking by the number of distinct other tasks that
  depend on each, directly or transitively, descending; count a task reached by several paths
  once and break ties by existing task number ascending. Show the proposed members and reasons;
  wait for the human to confirm or change them. Introduce no parallel-work field or batch limit.
- Keep pending human material and question-specific waits visible. `Depends on` blocks cycle
  starts, never refinement (WAY-144). Dependent tasks may refine in the same round. Only a named
  question needing another task's result earns `waits for task <n>`; log its question/reason with
  the plan task left `to refine`. When reconciliation establishes n as done, propose the waiting
  task again in the nearest round; do not start it automatically or forget its pending question.
- Initialize/resume each confirmed task's ignored conversation from
  `project-level/lead/conversation_template.md`. Fill its source identities, absolute paths,
  current round conversations and next actor. Keep outstanding prior work visible when the human
  changes the round; do not erase its questions or recorded acceptance.

## 3. Run turns and bring the human material

1. Dispatch one fresh `refine-task` agent per confirmed task in orchestrated mode, in parallel
   on separate task documents/conversations. Supply only its conversation path and minimal
   actor/stage routing. Requirements and answers travel through files, never relayed in prompts.
   Permit one writer per file; refiners edit no shared plan, definition or foundation and launch
   no children. You perform all child dispatches their borrowed workflows request.
   For a refiner's *Child-work request* for a run of the step that settles technology (WAY-265),
   dispatch the research agents, the critiques and the tests of risks that
   `project-level/technology/task_run.md` and `settle.md` give, one run per canonical request, at
   the document of the affected task with the lowest number; its report's head names every
   affected task's document. Put their results in the conversation files; the refiner writes the
   documents.
2. Wait for refiner turns to finish, then dispatch exactly one answering agent for the round
   through one conversation path whose header names the others. It follows
   `project-level/lead/answering.md`, reads all round questions and alone writes their answer
   sections during that turn. It edits no task body. Check that a required-behavior answer is a
   sourced document quotation, never code or inference; code facts answer only current behavior
   and retain file:line/revision separately. Missing/conflicting sources stay unresolved.
   Resume that round's sole answerer for later answering turns; if a session interruption needs
   a replacement, recover from files and retire the previous writer before dispatching it.
3. Read the files to assemble one round package: unanswered questions, complete candidate tables
   for Settlements to record, Human-action placement, complete wording proposals, and every
   document quotation answer as question, full quotation and source (WAY-155). Keep code facts
   separately identified. Preserve the answerer's canonical question and affected tasks so an
   identical choice is asked once; distinct scopes remain distinct. Do not hide quotation answers
   behind a summary or offer recommendations as accepted decisions. A run's list to confirm and
   its table of choices go in the package once, and each choice the human makes is recorded as a
   human answer (step 6); a canonical request's run is presented once for all its affected tasks.
4. Before presenting the completed proposed set, dispatch one fresh independent `critique` on
   the whole set, its sources and applicable rules through `elements/common/critique/SKILL.md`
   (WAY-120). Put material and the critic's observations in the conversation files; prompts carry
   paths/routing. Verify each observation and record its verdict. Body corrections return to
   fresh refiners; a conflict with a human settlement goes back to the human. If critique cannot
   run, report the obstacle and wait before collective presentation; self-review is not a substitute.
5. Present the single package in plain conversation, in the task's language, following "How a
   skill asks". Put affected plan rows in `waiting for human` when this package is presented;
   turns in progress, `questions` and explicit waits otherwise keep `to refine`. Log updates with
   reasons. Candidate acceptance, action placement/completion and final document acceptance are
   separate human acts. After a choice enters an entry's binding meaning, ask the source-anchored
   WAY-113 question against it or record the applicable exception and reason.
6. Record the human's exact answers, question/row IDs and acceptance/rejection in the conversations
   before fresh refiner turns. A struck quotation is marked struck and its question returns to
   the human, once for all affected tasks, with ways/costs/recommendation; it cannot be reused as
   a settled answer. Only fresh refiners transfer resolved answers with their original provenance
   and the ways the human did not choose into Questions to settle and change task bodies. Verify
   this transfer, including canonical answers in every affected task, before advancing or removing
   a conversation.

Read each refiner's exact result and evidence using the companion contract's routing table:
`questions` repeats answerer/human/refiner turns as needed; `waits for task <n>` records a real
question-specific wait; `ready for approval` reaches step 4; `plan change` reaches step 5;
`obstacle` names what prevents a valid next action and what resolves it. No result is human
approval; `ready for approval` is not a task-document Status. A missing result or report is
unfinished work, not permission to advance. When repeating turns refresh sources and next actor;
do not repeat an already settled human choice unless its meaning or source changed.

## 4. Accept one complete document

- For each `ready for approval`, verify the current refinement checks: blocking questions settled,
  candidates accepted/rejected with accepted meanings preserved, required challenges answered,
  Human actions placed by the human and every pre-cycle action done, plan scope/dependencies/
  assignments matched, and definition approval still valid. No task becomes ready during step 5's
  definition gate or pending plan recheck. Dependencies may remain unfinished without invalidating
  this document's acceptance; they still prevent a cycle start.
- Show the exact complete current task document, one at a time, and explicitly ask the human to
  accept it. Wait for that answer before showing the next. A package, candidate or different
  document's acceptance does not accept this one. Requested changes go to a fresh refiner;
  present the complete revised document again, never edit its body yourself.
- Record the human's acceptance in its conversation first, with path and revision/content identity
  of the exact complete document. Only then change its `Status:` to `ready for cycle`, update the
  plan State and Document link, and log the acceptance with reason (WAY-154). Check the resulting
  link and run `plan_check.py`. If interrupted between writes, compare recorded acceptance with
  the actual document, allowing only the intended Status change; finish missing writes only if
  that acceptance still applies and the readiness checks still hold. A changed body needs renewed
  acceptance, not a reconstructed approval.
- Before deleting the exact conversation file, verify all resolved answers, original sources,
  the ways the human did not choose, accepted candidate meanings and required information survive
  in the task document (WAY-134); canonical
  answers must survive in every affected task and no remaining conversation may need an answer
  available only here. If transfer is incomplete, resume a fresh refiner first. Delete only this
  file after successful acceptance/transfer, never a directory sweep or recursive cleanup.

## 5. Route plan and definition changes

- Record the source mismatch, requested change and next actor in the originating conversation.
  An in-scope split, new task within approved scope, ordering or dependency change goes to a fresh
  `plan-project` agent in delegated mode (WAY-156). Stop your shared-plan writes until it returns;
  it follows all existing plan checks and logs each change/reason. Human questions and required
  critique requests return through the file, for you to dispatch/present and record. Read its
  result and rerun the whole-plan check before resuming state updates or affected refinement.
- A scope change or changing which task writes a projected entry is the human's decision
  (WAY-145). Present the complete proposed change, sources, consequences, ways/costs and
  recommendation; record the answer before the owning agent applies it. Moving a question
  within approved scope with its logged reason alone needs no definition gate; changing the
  definition does. Do not let a refiner expand its task to conceal either mismatch.
- Before a definition edit, record in the conversation that its gate and subsequent plan recheck
  are pending; make that block visible in every affected pending task conversation. A newly
  created conversation checks the same definition and pending change. These files, the definition
  Status/gate record and plan log retain resumption evidence; introduce no second state store.
  You may edit definition text only when its full text is already before you and no reading of
  other definition sections or foundation is needed. Otherwise delegate the edit. In both cases
  a subagent always performs `define-project` step 7 in delegated mode.
- You dispatch the gate's independent critique and pass observations back through the files;
  the gate agent performs the whole foundation collision search, checks and corrections required
  by that step. Present its human approval material yourself and record the human's approval
  before the gate agent writes approval/fingerprint/record. Never approve on the human's behalf
  or replace the delegated gate with your own check. Missing child/critic capability blocks it.
- After the gate succeeds, dispatch a fresh `plan-project` agent from step 0 to recheck the plan
  against the newly approved definition, with serialized shared-plan ownership and logged
  corrections. Keep readiness writes blocked until that recheck and its required checks/critique/
  human decisions finish. Record completion and the new source identities in the conversations
  and plan's change log before fresh affected refiners resume. A check passing the old fingerprint
  or approval alone does not complete this route.
