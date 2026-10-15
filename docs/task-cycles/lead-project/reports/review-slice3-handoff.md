# Slice 3 independent review

Worktree C:/Storage/repos/the-way-wt/lead-project; branch task/lead-project. User delegated implement-task through a reviewable request; root handles intermediate questions provisionally. Read C:/Users/Mariusz/.codex/AGENTS.md, worktree AGENTS.md, agent-instructions/README.md. Before vault playbooks read C:/Storage/The Brain/The Brain/Notes/Resources/(R) Obsidian/obsidian_rulebook.md; then C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/playbook_code_review.md and its delegated review-loop file. No vault/product writes, branch/index mutations, human questions or child agents.

Use full Superpowers6.4.1 subagent-driven-development/task-reviewer-prompt.md under C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/. Read supplied diff package once; unchanged code only for a named focused cross-boundary risk. Read omitted continuations only where needed to judge an incomplete hunk and name that reason. No broad suite rerun; static workflow review does not establish live agent compliance. Return two verdicts and full anchored findings in .superpowers/sdd/plan/task-3-review.md.

Brief .superpowers/sdd/plan/task-3-brief.md; report .superpowers/sdd/plan/task-3-report.md. Base6e8efc5649044f5d79911370107b6f486068e81f; exact head/package appended at dispatch. Read full task/spec and current complete selected foundation entries by WAY-150. All five paths must have their intended change. Judge source fidelity independently, including root's implementation rulings where relevant.

Named integration risks: consumer instructions must match existing plan_state CLI and conversation/answerer/refine-task contract; all actor dispatches and human questions pass through the correct owner; no nested child requirement gets stranded. Inspect whole semantic paths for fresh parallel refiners, one fresh round answerer, confirmed ranked round, complete human package/quote rejection/candidate challenge/critique, refiner-only body writes, one-document acceptance and interruption recovery, durable answer cleanup, waits waking, serialized structural plan changes, projected-entry reassignment/scope human authority, definition edit delegation and always-delegated step7 gate plus critique/human approval/fresh plan step0. No ready while gate open. Dependencies gate cycle starts but never refinement; delivered-in and dropped differ. Verify new skill neither starts cycles nor closes projects. Existing foundation and invariant checks are read-only.

Wrapper generation/installation are later slices; report their integration as cannot verify rather than asserting they work. Evaluate any interim test failures on their actual cause; root has not pre-graded them. Full generation and all required suites must pass before final completion.

## Binding source text (verbatim from spec)

## Outcome and boundaries

The new `lead-project` skill gives the human one project orchestrator for a handed-over plan. It reconstructs progress from the plan, task documents and temporary conversation files, reconciles plan states with evidence, proposes a human-confirmed refinement round, and coordinates fresh agents until the human accepts each complete task document.

The project orchestrator never launches `implement-task`; the human launches task cycles separately. It does not close the project: when the last task is done it says closure is next and that no closure skill exists. It writes no product foundation entries. After a task merges it does not revalidate ready dependent task documents; `implement-task` checks current sources when a cycle starts.

No daemon, second task tracker, persistent session store or automatic PR-host adapter is added. A session can resume from the existing plan, its task documents and `.runs/project-refinement/<task-name>.md` files. Project plans and task documents remain in the locations the product's `AGENTS.md` Backlog section names.

## Components and ownership

| Component | Responsibility |
|---|---|
| `project-level/lead/skill/SKILL.md` | Project orchestration, state reconciliation, round selection, dispatch, human package, final acceptance and plan/definition change routing. |
| `project-level/lead/conversation_template.md` | The one file conversation contract, actor permissions, statuses and resumption rules. |
| `project-level/lead/answering.md` | The answering-agent instructions, reached through the conversation file; this is not a second user-invoked skill. |
| `project-level/plan_state.py` | Python 3.14, standard-library state reader; starts only Git, emits proposals and evidence, never edits the plan or task documents. |
| `project-level/task/skill/SKILL.md` | Existing refinement with an orchestrated mode; manual refinement retains direct conversation and gains explicit complete-document acceptance. |
| Existing plan/definition/task-cycle skills and templates | Carry the accepted changes to dependency semantics, handover and delegated question/critique routing. |
| Entry-point generator and installer registry | Expose `the-way-lead-project` both in the-way and in newly installed product repositories. |

The skill and companion files follow this worktree or the product's pinned `.the-way`; every the-way skill handoff uses the `the-way-` prefix. The new skill's description distinguishes leading a handed-over plan from defining/breaking down a project, refining one task, and running a task cycle. No global skill or personal file is a runtime dependency.

Only one actor writes a particular conversation at a time. Different refiners write different task documents and conversations in parallel; they never change the shared plan, definition or foundation. The project orchestrator owns ordinary plan state/Document-cell updates and their change-log lines. A dispatched plan-project agent owns a structural plan edit while that edit runs; the project orchestrator pauses its own plan writes until the agent returns.

## Start and resume

1. Resolve the product repository, process pin, Backlog locations, original plan and its definition. Require a handed-over plan. Run existing readiness and plan checks on the original whole files. Missing/unreadable sources, a draft plan, an invalid definition approval or a finding are visible obstacles; they never mean the sources passed. A changed definition returns through its gate and then plan-project step 0.
2. Select the product foundation by WAY-150, including the complete part map, all current matching Scope entries and relevant links, invariants and glossary terms. All participating agents do this for their own work. For a large plan/definition, use complete inventories and whole relevant units as WAY-151 describes, without weakening any mandatory whole-source read of another skill.
3. Run `python -B <the-way>/project-level/plan_state.py <plan> <product-repository>`. Review evidence and resolve unchecked PR outcomes through the product's chosen PR route. Apply only supported transitions, each with a dated change-log line naming the evidence and reason. A failed command or incomplete observation is not an unchanged/verified state.
4. Resume pending conversations by their identity, current turn and next actor. Reconcile final human acceptance recorded before an interruption with the actual document and plan. Never infer acceptance from a quotation, an agent status, or an empty question list.
5. Propose a round from tasks still needing refinement. Rank first by how many distinct tasks depend on them, directly or transitively; break ties by existing task number. This is a proposal the human can change, not a new plan field or a cycle-start rule. Pending human questions and explicit waits remain visible. A task waiting for task n is proposed again when the state read shows n done. `Depends on` alone never blocks refinement.


## A round of refinement

1. After the human confirms the round, initialize or resume its conversation files and dispatch one fresh refiner per task, in parallel. Each follows refine-task in orchestrated mode, writes only its task document and its own turn, records unresolved questions and returns one exact result phrase. It never asks the human or starts a child agent.
2. Once the refiner turns have finished, dispatch one answering agent for the round, with the path of one conversation whose header names the other round conversations. It reads all questions before adding answers, and is the sole writer of those answer sections during its turn. A document quote with a precise source may settle how things are to be; code may settle only how they currently are. Neither inference nor another agent's unsourced proposal is an answer.
3. If no authorized source settles a question, write the human question with variants, costs and recommendation. Where different tasks ask the same question, choose one canonical question and cross-reference it from the others, showing which tasks it affects; distinct scopes are not silently merged. The canonical answer must be copied with its source into every affected task document before its conversation is deleted, so a surviving conversation never relies on a deleted one.
4. The project orchestrator gathers one package for the whole round: unresolved questions, candidates for Settlements to record, placement of Human actions, complete wording proposals, and a list of answers supplied by document quotation, each as question, quotation and source. Code facts remain separately identified and sourced in conversations/task documents; they are not presented as document quotations or human choices. A human-struck quotation answer becomes a question to the human.
5. The existing collective-review rule still applies: the project orchestrator dispatches one independent critique of the complete proposed set before presenting it, checks its observations and resolves them without silently changing human settlements. It performs all child dispatches that a borrowed project skill needs; refiners, plan agents and gate agents return requests through the conversation instead of attempting nested dispatch or speaking to the human.
6. The project orchestrator writes human answers into the conversation files before dispatching fresh refiners. Choices that enter an entry's binding meaning receive the question against the choice required by WAY-113, unless its stated exception applies. Candidate acceptance, Human-action placement and final document acceptance are distinct acts.
7. Each fresh refiner checks sources, transfers resolved answers with provenance into Questions to settle, updates the document, and repeats the applicable refine-task checks. It carries accepted candidates whole, rejects none on its own, and does not write foundation entries. Refinement repeats as needed; missing answers never become executable requirements.

The orchestrated-mode instruction explicitly applies to every question the refiner would otherwise ask: task location, scope/wording, conflicting source decisions, Human actions, candidate selection and challenge questions, and final document approval. The source-finding work of find-foundation-entries is still used in task mode; its human-presentation steps return material through the conversation and do not authorize the refiner to approve it.

## Final task acceptance

For each `ready for approval` task, the project orchestrator presents the complete current task document, one at a time. Human acceptance of another task or a round package is not acceptance of this document. A requested change returns to a fresh refiner; the project orchestrator does not edit its body.

After the human accepts the exact complete document, the project orchestrator changes only its `Status:` line to `ready for cycle`, changes the plan row to that state, ensures the Document link names the resulting document and logs the acceptance. All readiness requirements, including completed pre-cycle Human actions and settled candidate rows, still hold. Store the human acceptance in the conversation before these writes so an interruption is recoverable.

Before deleting the exact conversation path, verify that all resolved answers, their sources, accepted candidate meanings and required task information live in the task document, and that no remaining round conversation needs an answer available only in this file. Remove that file only; no directory sweep or recursive cleanup. The final document is the retained result, not the transient discussion. Manual refine-task likewise shows the whole final document and waits for the human's acceptance before it writes `ready for cycle`.

## Plan and definition changes

An in-scope split, new task within approved scope, ordering or dependency change goes to a fresh plan-project agent. It follows the existing plan checks and records every change with its reason. Changing which task writes a projected entry remains the human's decision under WAY-145; a new scope choice goes to the human, never becomes an agent's adjustment of the plan.

A definition change always goes through its readiness gate. The project orchestrator may make the text change itself only when the full text being changed is already before it and it needs no additional definition section or foundation reading. Otherwise a subagent makes it. A subagent always performs define-project step 7; the project orchestrator dispatches the independent critique and passes its observations back through files, and the human approves through the project orchestrator. A fresh subagent then runs plan-project step 0 and rechecks the plan against the newly approved definition. While the gate is open, no task receives `ready for cycle`.

The task cycle's source checks explicitly require a plan member's dependencies to be done before its cycle starts. A task already `ready for cycle` can wait for dependencies without losing human acceptance. A plan's `done — goal delivered in task <n>` state supplies completion through its named task only when that completion is established; `dropped — approved by human` alone does not prove delivery of a dependency's goal and calls for plan reconciliation. No cycle is launched by leading a project.


## Final dispatch

Head74750b340769fe1c397adaff12ece77acc8350e7; package .superpowers/sdd/plan/review-6e8efc5..74750b3.diff. Model gpt-6.1-sol for five-file integration judgment. Root read all five final files/diff and verified hashes unchanged at commit; full report read. Project-level227/task-cycle41 pass; gate97/98 with one explicitly disclosed missing/stale wrappers test. The latter is assigned Slices5-7; independently assess all other claims.
