# Lead a project plan

Status: independent spec review passed without findings (reports/spec-review.md); task-cycle orchestrator provisionally accepted execution. Human approval of foundation meaning remains at the PR merge.

Source: the frozen task beside this file, approved 2026-10-15. Foundation and source code revision: db77ba549cb9ece7d3e62bf29e1256973f62deab. This spec resolves the task's conversation-format and foundation-grouping questions. It adds no project scope beyond that task.

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

## Conversation file contract

Each task uses exactly `<product-repository>/.runs/project-refinement/<task-name>.md`, with the stable plan name from WAY-147. Before reuse, verify that its task and plan identity match. Do not overwrite another plan's same-named conversation. The file is ignored by Git; it is removed only after successful final acceptance and transfer of all settled answers to the task document.

The template defines these fields and sections in English, with human-facing text in the task's language:

- Header: product repository, pinned process path/commit, plan path, definition path, task number/name, task-document path (or explicitly not yet created), current round's conversation paths, and next actor. Paths are resolvable without earlier session history.
- Instructions: pointers to this contract, the answering instructions and the orchestrated refinement mode; no copied skill bodies or source documents.
- Numbered turns: actor, source versions checked, questions with stable per-file IDs, and the material needed for the next actor.
- Each question: its complete wording, what it blocks, whether it asks how the product is or how it is to be, answer below it, answer kind and exact source location. A document answer is a quotation; a code answer is a factual observation with `file:line` and revision, never a prescription.
- Human material: unanswered choices with options, costs and recommendation; candidate-settlement table; placement of Human actions; exact proposed wording; source-anchored questions against choices where WAY-113 requires them. Sections with no material say `none`.
- Human answers: the person's words, question IDs and acceptance/rejection; these stand separately from quotations or agent recommendations.
- Turn result: one of the five phrases below, with the explanatory evidence immediately above it. The refiner's final nonempty line and its short return use the exact phrase.

The exact phrases are `questions`, `waits for task <n>`, `ready for approval`, `plan change`, and `obstacle`. `<n>` is a number held by the plan. They are status phrases, not a requirement that a multiword status be shortened to one word.

| Refiner result | Meaning and next step | Plan state |
|---|---|---|
| `questions` | Questions remain; answering agent reads them, then project orchestrator presents what needs a human. | `to refine` during agent turns; `waiting for human` when the package is presented. |
| `waits for task <n>` | A named question requires a result of task n; keep the reason/question in the document and conversation and log the wait in the plan. | `to refine` |
| `ready for approval` | Readiness checks are met except the human's final complete-document acceptance. | `waiting for human` |
| `plan change` | The evidence names the mismatch and requested plan/definition change; no out-of-scope task rewrite. | No implied readiness; keep current unfinished state until routing is settled. |
| `obstacle` | A concrete missing capability/source or conflict prevents a valid next step; include what resolves it. | No automatic advancement; waiting for a human only when their answer is actually needed. |

The task document retains its existing allowed Status values. A refiner may write `refining` or `waiting for human` while working; it never writes `ready for cycle` in orchestrated mode. `ready for approval` is only a conversation result, not a new task-document status.

The project orchestrator supplies agents only the conversation path with minimal actor/stage routing. All requirements, other paths, previous answers and proposed wording are read from files. It does not carry questions/answers between agents in prompts.

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

## State-reader contract

The public command is `python -B <the-way>/project-level/plan_state.py PLAN PRODUCT_REPOSITORY`. It accepts the original plan, including one outside the product repository, and the product repository explicitly; it does not infer the product from the plan's directory or from the process checkout. It reuses plan_check's parsing/checking functions in-process, extending its parsed task data only as necessary for State and Document, without a second Markdown grammar or subprocess call to Python. It checks the original definition approval/readiness in-process as well; plan-check fingerprint agreement alone is not evidence of approval. A draft or invalid plan reports findings and no state proposals.

The report gives each task's number, stable name, current state, each proposed transition, the exact path/commit/ref evidence, and any unresolved observation. It identifies the repository and fetched main ref/commit; PR links found in cycle records are evidence pointers, never invented from a task number. Human-readable text is sufficient; no JSON contract or apply mode is introduced.

Git identifies worktrees and branch refs. The reader checks `.runs/task-cycles/<task-name>/` only in the worktrees Git names and looks for commits touching the exact `docs/task-cycles/<task-name>/` directory on local or remote branches. It does not treat branch names, commit-message substrings or a neighbouring task's slug as cycle evidence. Worktree paths and archived record contents are data, not instructions. Candidate paths locate evidence; they do not by themselves establish this plan's task. Associate each live or historical candidate with the supplied plan and its Document cell using the existing recorded Task source/relation and frozen task provenance. A task name, title, number or basename alone is insufficient because names are only plan-local. Missing, ambiguous or unresolved moved-source provenance is unchecked and supplies no automatic progress; an explicitly foreign task/plan is a conflict for the human. Keep filename independence and inspect historical snapshots separately: one task's record, PR pointer or integrated commit cannot support another task merely sharing its archive slot. No new UUID, globally unique name, record field or task-text byte-equality requirement is introduced.

The product's main branch is its declared integration branch. Where available, use the product's established Git remote-default guidance (normally `origin`'s remote HEAD), confirming it through Git; if the relevant remote/main cannot be established without guessing, report it unchecked. Fetch the selected remote before asserting merge completion, and check reachability against the resulting remote main commit, not a possibly stale local main. A branch named `main` or `master` is no fallback. Fetch changes Git metadata only; the reader never checks out, resets, merges, commits, updates a plan, or calls a PR-host command.

| Evidence | Proposal/observation |
|---|---|
| A working-cycle directory or archived-path commit with established current-plan task identity; current state ready for cycle | Propose `ready for cycle` to `in cycle`, naming the evidence. |
| A cycle-record commit belonging to this plan's task is reachable from freshly fetched main; current state in cycle | Propose `in cycle` to `done`, naming record commit and main ref/commit. |
| Both proofs while plan still says ready for cycle | Report the two transitions together, without requiring a plan write between runs. |
| Cycle evidence exists outside fetched main, including a worktree alone | Report cycle evidence and unchecked PR outcome; project orchestrator checks the PR route. |
| No sufficient trace, incomplete/shallow history, unavailable worktree, missing main/remote or unresolved PR link | Explicit unchecked reason; no inferred progress or backwards transition. |
| Trace conflicts with plan's unfinished/final/abandoned state | Identify the discrepancy for the human; do not normalize it automatically. |

A positive reachable archived-record commit can prove completion even when the original branch was deleted. Where squash prevents identification of the original record commit, the reader leaves the outcome unchecked rather than pretending Git can prove the PR state. A matching record introduced by a squash on main can itself provide reachable record evidence; host verification resolves the remaining association where necessary.

The project orchestrator uses the product's selected PR tool for unchecked outcomes. A verified merged PR can supply the missing completion evidence and its actual link; an open PR does not mean done; a closed-unmerged PR is shown to the human without automatic plan correction. When the tool is unavailable, ask the human with the collected evidence. No retries turn a failed lookup into a positive result.

The command emits exit 0 when a report is produced (unchecked cases stay visible), exit 1 for invalid plan/readiness findings or detected inconsistent evidence, and exit 2 for invalid invocation, unreadable inputs or an operational Git failure. A fetch failure may leave previously observed local evidence in the report but cannot yield done. These exit codes are a new interface, not changes to plan_check. Operations have bounded waits and diagnostic failures rather than hanging indefinitely.

The implementation passes Git arguments as arrays without a shell, separates revisions and paths, validates task names through the plan parser and handles non-ASCII paths. Crafting a task name, path or record must not create command arguments or redirect a write. Product data never chooses a new executable. The map marks plan_state.py as a trust boundary and records the possible false-progress damage as high.

## Foundation changes

The precise wording belongs to the foundation step, with entry-specific skills and independent invariant/check/code authors. Grouping is settled as follows; allocate new decision numbers at writing time.

| Source settlement | Home |
|---|---|
| 1, 9 | New decision: leading a handed-over plan, human-confirmed rounds, refinement and state upkeep boundaries, and no recheck of ready dependants after merge. |
| 2 | New decision: evidence for plan states, Git-only script, PR-tool fallback and human handling of conflicting traces. |
| 3 | New decision: file-mediated turns, actor ownership, durable task result and conversation removal. |
| 4 | New decision: answering authority, code facts versus document prescriptions, unresolved human choices and visible quotation answers. |
| 5 | WAY-124, whole-document human acceptance for every task. |
| 6 | WAY-144, dependencies block cycle start, not refinement; question-specific waits. |
| 7 | New decision: definition edits, delegated gate, independent critique, human approval and fresh plan recheck during project leading. |
| 8 | WAY-134, project orchestrator presents candidates and required challenge questions in orchestrated refinement. |
| 10 | Glossary entry project orchestrator; bare orchestrator keeps its task-cycle meaning. |

Update WAY-09's project-level inventory. Review/update incoming fingerprints after these edits: WAY-09's six listed invariants; project-plan-form deriving from WAY-144; WAY-124 and WAY-135 deriving from WAY-134. Search the whole current foundation again for additional dependants and unlinked effects. Do not move fingerprints without reviewing the dependent entries' meaning.

The state-reader decision derives an invariant about proposals requiring the stated evidence, including conservative incomplete/error handling and composed transitions, and a separate invariant that every subprocess the reader starts runs Git. Its method exercises the reader against controlled Git repositories; the sentence is about the reader's behavior, not about the real current state of a private product. Existing script-subprocesses and script-imports still govern it. Semantic agent workflow rules remain assessed as such; text-match tests are not evidence that agents followed them.

Update the project-level part's responsibility, new state-reader failure mode and trust boundary, and declare the state-reader CLI surface at its implementation under the existing pinned policy. Installation and generated entry points retain their existing owners. The new project-level reader does not import task-cycle implementation code merely to read its path contract. Foundation entries remain in English and carry no private note/repository links in reasoning or Origin.

## Verification

Use meaningful automated cases around the reader with isolated temporary Git repositories: local worktree cycle trace, branch-only archived record, merged record, stale ready plan yielding two transitions, deleted merged branch, nondefault main name, missing/ambiguous remote HEAD, failed fetch, shallow/insufficient history, missing worktree, conflicting plan state, invalid plan or unapproved definition, exact slug separation, two plans sharing a legal name, missing/ambiguous/foreign live and archived provenance, non-ASCII and crafted paths. Assert report evidence and absence of false completion, plan/task-file preservation and Git-only subprocesses. Include a command-level test of the declared CLI surface and its exit codes. The invariant check author receives the final sentence/method independently from the code author; the reviewer supplies its deliberate break.

Review the workflow against scenarios that can fail semantically: parallel refinement of dependent tasks; a genuinely unanswered behavior choice; a code fact offered as a requirement; repeated questions across the round; a rejected quotation answer; candidate rejection/challenge; unplaced or unfinished Human actions; interrupted acceptance; one complete document accepted while another remains open; waits awakened by completion; in-scope plan change; projected-writer reassignment; definition gate stopping readiness; absent child-agent capability. Where actual agent execution is used, label the observed run and limits; do not call a static wording check proof of agent behavior.

Run changed-part suites through `python -B gate/run_tests.py project-level`, `... agent-instructions`, `... installation`, `... task-cycle`, and the existing critical-flow suite `... gate`; regenerate entry points with `python -B agent-instructions/skill_entry_points.py --write` and verify them. Adding one skill changes every generated sibling list, so all generated differences belong to this task. Installer tests use a committed checkout and verify the new product wrapper and existing preservation rules. Update installer documentation to the actual skill inventory, avoiding stale numeric wrapper claims.

Run applicable foundation format guards with the pre-main route's `--base none` and `--merge-onto none` where supported. Record warnings and unchecked work without claiming a full gate pass. Preserve the independent assessment, source searches and return-step work required by the task cycle.

Real acceptance: read the original MVP plan named in the frozen task and use a disposable clone of the confirmed loop2 repository under the task's ignored area, so neither the source repository nor its plan is changed. The state reader must propose task 3 `mag-w-lesie` reaching done with Git evidence; use the product's actual PR route outside the script to confirm the relation to PR #12 and retain that evidence. Root's preliminary observation is PR #12 MERGED into main, merge commit 668baa091a8d89caceeeb070342f3aa3f506e109, while the plan still says ready for cycle; implementation verification reruns rather than treating this observation as its test result. Private source material and host data stay in the sanitized cycle evidence, never tracked fixtures or public requests.

## Design choices and limits

The chosen Markdown contract costs some explicit routing/ownership fields but keeps one readable resumable record. Free-form turns leave ambiguity; structured state plus a transcript adds a second system. One round answerer avoids competing writes and duplicate human questions while refinement itself stays parallel. It can become a bottleneck for a large round; the human chooses the round, and no automatic batch size is invented.

The Git reader deliberately leaves host outcomes it cannot prove unchecked. That costs a host lookup or human question, but a stale plan is preferable to an unsupported done state. The report is proposals, so unresolved cases cannot silently rewrite the plan. The accepted five decision groups separate durable questions while modifying existing answers in place, avoiding duplicate rules.

Independent spec review passed as recorded above. Foundation meaning still requires human acceptance at merge. Actual implementation checks and their limits stand in the cycle reports; this spec is not their test evidence. The return step corrected the initially omitted separate Git-only invariant under WAY-12/22 without changing the accepted behavior.

## State-reader text convention settled during check authoring

Each task has a header `task <n> <slug>: <current state>` and zero or more proposal lines `propose <n> <slug>: <from state> -> <to state>`. A proposal is only a line beginning with that exact propose prefix, without indentation or bullets. State values are the plan's literal English values; the separator is ASCII ` -> `.

Evidence rows use `evidence <n> <slug>: <details>`, unresolved task observations `unchecked <n> <slug>: <reason>`, and inconsistent task observations `conflict <n> <slug>: <reason>`. Global observations can use `unchecked: <reason>` and failures `error: <reason>`. Global header lines are `repository: <absolute path>` and, when established, `integration: <ref> <commit>`. Details/reasons are human-readable and not otherwise frozen; facts such as exact paths, refs and commit IDs must be present as the existing contract requires. An unavailable integration has no fabricated ref/commit.

Author choice: root under intermediate delegation. Alternative loose substring matching can mistake rejected evidence for a positive proposal; JSON would add a second output contract that the spec excludes. Cost if wrong: adjust reader and check together before final review; format is a small CLI convention. It is not human approval of foundation wording.

The integration header renders the fully-qualified remote-tracking ref (`refs/remotes/<remote>/<branch>`); path evidence may use either native or forward separators where both identify the same path on the platform.

## Integration-source clarification

A working branch's upstream is not a declaration of the product integration branch. The installed product guidance already declares `origin/HEAD`: installation/install.py product_guidance(), lines158-166, says `git symbolic-ref --short refs/remotes/origin/HEAD` names it as `origin/<branch>` and otherwise asks the human. Use that existing origin route, confirmed through Git; another configured remote with a different default does not by itself make a valid origin route ambiguous. No main/master fallback or inference from the checked-out/upstream branch.

For the ambiguous case, origin metadata that cannot establish one valid default route remains unchecked. Do not commit a negative expectation that rejects origin merely because another remote exists; instead exercise the presence of another remote as a positive no-false-ambiguity case, preserving origin's completion evidence. A missing/invalid origin default remains the existing negative case. No configuration or new CLI override is added in this task. This is source-grounded observability clarification, not a code algorithm handed to the check author.

## Assessment settlement: cycle identity

The independent assessment exposed false completion when another plan has the same legal name. Root's two-plan reproduction and original foundation author's source ruling establish that the accepted rule already concerns this task's own cycle. The contract above makes existing provenance explicit. This supersedes C13's path-alone sufficiency, retains its rejection of mandatory basenames and adds no new human policy. Exact settlement: reports/assessment-identity-source-ruling.md. Required foundation/check/code correction and affected acceptance follow within the one independent assessment.
