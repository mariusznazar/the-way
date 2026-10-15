# Slice 2 independent review

Worktree C:/Storage/repos/the-way-wt/lead-project. User delegated a complete implement-task cycle to a reviewable request; root answers intermediate questions provisionally. No human questions and no child agents. Read global C:/Users/Mariusz/.codex/AGENTS.md, worktree AGENTS.md and agent-instructions/README.md. Before vault playbooks read C:/Storage/The Brain/The Brain/Notes/Resources/(R) Obsidian/obsidian_rulebook.md, then C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/playbook_code_review.md and its delegated review-loop playbook. No vault writes.

Use full C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/task-reviewer-prompt.md. Return its separate spec-compliance and task-quality verdicts, anchored full findings, and precise static-vs-executed evidence. Read the diff package once; do not duplicate changed-file reads unless a hunk is cut off mid-unit. Named focused cross-boundary checks only; do not rerun green suites or crawl unrelated code. The checkout, index, HEAD and protected tests/foundation are read-only. No invariant was changed in this slice.

Brief .superpowers/sdd/plan/task-2-brief.md; author report .superpowers/sdd/plan/task-2-report.md; final report .superpowers/sdd/plan/task-2-review.md. Base2233cffd031838f9e68272824fb4899c93471cc3. Exact head/package appended before dispatch. Read whole source task/spec and applicable whole current foundation entries under WAY-150. Judge against source, not author's rationale or root approval.

Review all four listed files against each requirement. In particular inspect full turns for the five result phrases, question routing at every otherwise-human point of refine-task, refiner-only body ownership, final complete-document acceptance in manual and orchestrated modes, source authority distinguishing facts from prescriptions, quote rejection, deduplication/provenance survival, Human actions and candidate challenge routing, no ready while questions/gate remain, identity/resumption and serialized file turns. The leading skill is a later slice: flag its required integration as cannot verify, without pretending this slice proves live agents comply. Scenario walkthroughs are static semantic review, not a live execution test.

## Binding source text (verbatim from spec)

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


## Final dispatch

Head6e8efc5649044f5d79911370107b6f486068e81f; diff .superpowers/sdd/plan/review-2233cff..6e8efc5.diff. Model gpt-6.1-sol, integration judgment. Root read final four files/diff and full implementer report; focused suites227/98 pass. No author question.
