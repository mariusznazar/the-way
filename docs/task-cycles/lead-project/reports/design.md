# Design-stage report

Status: complete — spec ready for independent review; no implementation or planning.

## Authority and versions

- Worktree: C:/Storage/repos/the-way-wt/lead-project.
- Base/foundation: db77ba549cb9ece7d3e62bf29e1256973f62deab.
- Frozen source: ../task.md, approved 2026-10-15; human intermediate choices delegated to the root task-cycle orchestrator, not to the designer.
- Method: installed Superpowers 6.4.1 brainstorming, read from C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/brainstorming/SKILL.md; adapted by task-cycle/skill/SKILL.md step 6. This is architectural because it adds a project orchestration flow, file conversation contract and Git state reader.
- Boundaries: only ../spec.md and this report; no code, product plan changes, planner dispatch or commits.

## Intent

Lead a handed-over project plan through parallel refinement and explicit human acceptance of complete task documents, and reconcile its states with evidence. The project orchestrator never starts task cycles and never closes the project. The frozen task settles the role boundaries; conversation format and grouping of foundation entries remain design choices.

## Questions, options and rulings

### 1. File-mediated refinement

Proposal sent to root: one Markdown conversation per task with a header naming product repository, pinned the-way, plan, definition, task document, round task files and next actor; numbered turns contain numbered questions, source-backed answers below each, human questions/answers, candidate settlements, Human actions and wording proposals. Each refiner turn ends with exactly one phrase: `questions`, `waits for task <n>`, `ready for approval`, `plan change`, `obstacle`. These are status phrases despite the source saying “one word”. Refiner alone edits task body; answerer only conversation; project orchestrator writes routing and human-answer material and the final task Status line. Fresh refiners import settled answers with sources. One answering agent handles the round after all parallel refiner turns finish and reads every conversation to deduplicate. Subsequent refiner turns run in parallel.

Alternatives: a free-form transcript is shorter but makes resume and ownership ambiguous; JSON state beside prose enables mechanical validation but adds a second state system. Recommendation: one readable Markdown template under project-level/lead, no separate persistent ledger.

Root ruling: provisional orchestrator go-ahead under the task delegation, based on To do 4, 7–12 and settlement 3. Keep factual code answers distinct from the package's list of document quotations; factual answers remain sourced in the conversation. A quotation is never human approval. Delete only the exact conversation file, after acceptance of the complete document and persistence of all settled answers. This is not human approval of a future foundation entry.

### 2. Git state reader

Proposal: stdout text report with no apply mode and no host subprocess; validate the original whole plan through the existing plan_check Python API; discover worktrees and local/remote branches with Git; use exact docs/task-cycles/<task-name>/ history and a freshly fetched, Git-identified remote default branch. Show task number/name/current state, proposed transition sequence, concrete worktree or commit/ref evidence and unchecked/error reasons. A ready task can yield both ready-to-in-cycle and in-cycle-to-done in one report. Missing or ambiguous main/remote, failed fetch and insufficient history never establish done. A branch record outside main establishes cycle activity while its PR outcome remains unchecked. The project orchestrator resolves host status through the product's PR route, never through this script; conflicts and closed-unmerged requests go to the human unchanged. No automatic downgrades of final states.

Alternatives: guessing main/master can select the wrong branch; putting a host CLI in the script violates the accepted Git-only boundary. The report reads PR links from records when available and never invents one. The reader handles untrusted plan/path inputs with safe Git argument lists and no shell; project-level/plan_state.py is a trust boundary.

Root ruling: provisional go-ahead under task To do 5 and WAY-38/48/147. Git confirms the remote default, never a branch-name guess. Real verification may use a local clone under the cycle's .runs area so the source product's refs remain unchanged; root independently checked the real PR. Invalid or unapproved source material must remain a finding, not imply success. The installer registry addition needed to expose the new skill is authorized scope, including WAY-141 and installer checks.

### 3. Foundation grouping

Recommendation: five new decisions answer five separate questions: A, who leads a handed-over plan and its boundaries and rounds (settlements 1 and 9); B, how plan states follow evidence (2); C, how agents exchange work and own files (3); D, what the answerer may settle and what the human sees (4); E, how definition changes pass the gate during leading (7). Amend WAY-124 for whole-document human acceptance (5), WAY-144 for dependencies blocking cycle starts only (6), WAY-134 for candidate/challenge presentation by the project orchestrator (8), and WAY-09 for project-level contents. Add the glossary term project orchestrator (10). Add one evidence-backed state-reader invariant, retaining level 2 for semantic workflow promises. Update incoming fingerprints and the map.

Alternatives: one large decision mixes independently changing questions; one decision per numbered task item duplicates existing rules. Raised concern: whether the no-cycle/no-close clauses require separate non-goals under WAY-26.

Root ruling: provisional approval of grouping, not eventual exact entry wording. These are role boundaries, not bans on cycles or closure in the product; WAY-26 does not require separate product non-goals. Preserve each accepted row whole in meaning, row 9 in A. Foundation author establishes the invariant sentence independently and check author remains separate from code author. Finish spec and return for independent spec review, without dispatching that review.

## Reading and checks

Read the frozen task whole, repository AGENTS.md, agent-instructions/README.md, shared way_of_working.md, complete part map, complete plan/task templates, complete refine-task/plan-project/define-project skills, find-foundation-entries skill, plan_check.py, skill_entry_points.py, installer registry/wrapper/guidance implementation, installation README, and the user's skill conventions. The task-cycle design boundary and installed brainstorming method were read. No visual companion was needed: the questions concern authority, text and evidence, not visual design.

Foundation selection uses behavioral parts project-level, task-cycle and agent-instructions, expanded to installation after its hard-coded SKILLS registry was found. The root confirmed this follows WAY-44: the holder of a multi-part foundation file does not itself add every decision scoped to that holder. The initial complete multiline Scope inspection yielded 82 matches; installation adds WAY-141, yielding 83. All current entries are /1; no selected entry is merely a discovered heading. Whole reads include rationale and rejected options. Output truncation was repaired by smaller rereads, including WAY-21/25–28, WAY-126/127, WAY-136, WAY-137–145, and the relevant environment-fact passages.

Additional whole decision reads: WAY-02, 04, 05, 07, 08, 12, 14, 17, 19, 31, 35, 40, 49, 52, 53, 61, 95–99. These support existing-entry edits, fingerprint dependants, the new CLI surface, generated files, glossary meaning and invariant verification. The decision template was read to check grouping and role boundaries; this stage writes no foundation entry and does not substitute for the later entry skills' mandatory templates/examples.

Inspected all invariant Part fields, then read every matching `every`, project-level and agent-instructions entry; no invariant currently names task-cycle. Read the six WAY-09-dependent entries and decision-guard-stale-reference explicitly. Relevant entries include project-plan-form, project-plan-check, project-definition-form, project-readiness-gate, project-technology-record, skill-entry-points, script-language/imports/subprocesses, file-part-assignment, path-pattern-reach, the foundation/search/assessment records, glossary and link checks. The initial invariant inventory used the wrong heading depth and produced one block; positive inspection showed entries use `##`, the inventory was rerun with that delimiter, and no conclusion used the first result.

Read the glossary whole, including Avoid spellings; no project orchestrator term exists. Read the environment facts file, with the truncated path-rule/reward-hacking/oracle passages reread. Those are pinned sources for existing foundation choices, not freshly verified external claims; their watches were not run. No new fact is proposed merely from agent behavior or the private acceptance example.

## Whole-foundation search findings

At db77ba549cb9ece7d3e62bf29e1256973f62deab, searched all five foundation elements for lead-project, plan state, orchestrator, refinement, parallel work, dependencies/Depends on, cycle record/task-cycles and incoming WAY-09/124/134/144 references. Read complete relevant hits. Findings and dispositions:

- WAY-124 and WAY-134 are the existing readiness and candidate-presentation homes; change their accepted meanings, do not add duplicate decisions.
- WAY-144's binding wording and Verification currently apply dependencies to all side-by-side work; narrow their meaning to cycle starts as the task explicitly settles. The derived project-plan-form sentence still describes syntax, so review and refresh its dependency fingerprint without automatically raising its version.
- WAY-09's inventory and the part map omit leading/state reading; revise both and refresh its six invariant dependants after semantic review.
- WAY-125 and task-cycle map use bare orchestrator; preserve that meaning and use the accepted project orchestrator term for the new role.
- WAY-106 forbids project-level foundation writes; candidates remain task rows and definition changes remain projected/gated.
- WAY-120/shared collective-review rule still applies to the round's complete proposal package; dispatch its critique from the project orchestrator, not a nested refiner.
- WAY-145 reserves projected-writer reassignment to the human; an in-scope plan edit is not blanket approval to move that assignment.
- WAY-118 preserves the repeated gate after definition changes. The new orchestration delegates its execution and blocks task readiness during it.
- No current foundation entry duplicates the new plan-state reader or file-conversation contract. The incomplete methods of existing generic invariants are existing debt, not proof this feature is checked.

The foundation-writing stage must repeat/expand the search for its exact entries, and the pre-merge search must use the then-current integration tip. This design search is not either future result.

## Coverage and implementation choices

- Task items 1–4 and settlement 9: outcome/boundaries/start-resume sections.
- Item 5: state-reader contract, conservative Git/PR boundary and composed ready-to-done report.
- Items 6–13: round proposal, conversation ownership, evidence authority, one human package, full-document approval, plan states and explicit waits.
- Items 14–15: delegated plan changes and definition gate with fresh plan recheck.
- Items 16–18: orchestrated refine-task mode, universal final acceptance and cycle-start dependency check.
- Item 19: the component table's existing handover adaptation means plan-project step 7 explicitly points to lead-project next. Preserve this exact frozen-task requirement in the plan; no need for another behavior choice.
- Acceptance: verify the original plan against actual loop2 history in an isolated clone and independently check its actual PR relation through the host route. No mutation of the source repository or plan.
- Settlements 1–10: the spec's foundation table maps every accepted meaning; grouping adds no new scope.

Small reversible implementation choices in the spec: distinct transitive dependants then task number for round ordering; stdout text with exit 0 report/1 invalid or inconsistent evidence/2 operational error; reuse existing plan/readiness Python APIs rather than subprocesses or a second grammar; no configurable storage layer. These elaborate the approved three design sections and remain reviewable in the spec. They are not recorded as human decisions.

## Self-review and evidence limits

Completed inline review for missing requirements, invented approvals, contradictory ownership, missing sources, scope and placeholders. Corrected the design distinctions while drafting: exact status phrases rather than single-word tokens; code facts versus document quotations; question deduplication surviving deletion; final acceptance recoverable after interruption; draft/invalid plan not a successful state check; approved definition validated beyond a matching fingerprint; a stale ready state can report both transitions together. No unresolved placeholder remains in the spec. The new invariant's exact sentence and decision numbers deliberately belong to the foundation step, not to a missing design answer.

Read/inspection commands returned exit 0. `git status --short` returned no tracked/untracked product changes; `git rev-parse HEAD` still gives the base. No product code, generated entry point, foundation entry or plan was changed by this stage; no commit was made. Only spec.md and this report were written.

No implementation tests or host verification were run by this agent. Root reported initial baseline tests 376 total, including installer 26/26, and real PR #12 MERGED into main at 668baa091a8d89caceeeb070342f3aa3f506e109 while plan task 3 remained ready for cycle. This is preparatory evidence from root, not my independently verified acceptance result. Root prepared `.runs/task-cycles/lead-project/acceptance-loop2` as a no-checkout local clone with the verified real origin URL; implementation verification may check out inside that clone. Runtime reader behavior, actual agent-following behavior and final source searches remain unchecked until their assigned stages.

## Return

Design complete at ../spec.md. Root read the spec whole and requested no further design change before independent review. All three design questions have provisional orchestrator rulings above. No unresolved choice blocks that review. Exact foundation wording, independent invariant/check authorship, bounded subprocess mechanics and testing remain subsequent work, not approval obtained here. The spec itself has not yet passed independent review; the designer does not dispatch it or invoke the planner.

## Scope selection ledger

Expected current Scope matches: 83. Read whole: 83. Missing expected matches: 0. Sources below refer to foundations/decisions.md at the recorded base commit; supplemental linked reads are listed above.

| Entry | Source line | Read |
|---|---|---|
| WAY-01/1 | foundations/decisions.md:6 | whole |
| WAY-03/1 | foundations/decisions.md:71 | whole |
| WAY-09/1 | foundations/decisions.md:234 | whole |
| WAY-10/1 | foundations/decisions.md:305 | whole |
| WAY-11/1 | foundations/decisions.md:343 | whole |
| WAY-13/1 | foundations/decisions.md:414 | whole |
| WAY-16/1 | foundations/decisions.md:480 | whole |
| WAY-21/1 | foundations/decisions.md:623 | whole |
| WAY-25/1 | foundations/decisions.md:708 | whole |
| WAY-26/1 | foundations/decisions.md:737 | whole |
| WAY-27/1 | foundations/decisions.md:763 | whole |
| WAY-28/1 | foundations/decisions.md:794 | whole |
| WAY-30/1 | foundations/decisions.md:857 | whole |
| WAY-33/1 | foundations/decisions.md:949 | whole |
| WAY-34/1 | foundations/decisions.md:980 | whole |
| WAY-36/1 | foundations/decisions.md:1043 | whole |
| WAY-37/1 | foundations/decisions.md:1070 | whole |
| WAY-38/1 | foundations/decisions.md:1097 | whole |
| WAY-44/1 | foundations/decisions.md:1228 | whole |
| WAY-45/1 | foundations/decisions.md:1259 | whole |
| WAY-46/1 | foundations/decisions.md:1285 | whole |
| WAY-47/1 | foundations/decisions.md:1326 | whole |
| WAY-48/1 | foundations/decisions.md:1353 | whole |
| WAY-51/1 | foundations/decisions.md:1423 | whole |
| WAY-55/1 | foundations/decisions.md:1541 | whole |
| WAY-57/1 | foundations/decisions.md:1602 | whole |
| WAY-62/1 | foundations/decisions.md:1782 | whole |
| WAY-63/1 | foundations/decisions.md:1813 | whole |
| WAY-65/1 | foundations/decisions.md:1890 | whole |
| WAY-68/1 | foundations/decisions.md:1921 | whole |
| WAY-69/1 | foundations/decisions.md:1955 | whole |
| WAY-82/1 | foundations/decisions.md:2315 | whole |
| WAY-89/1 | foundations/decisions.md:2471 | whole |
| WAY-100/1 | foundations/decisions.md:2783 | whole |
| WAY-101/1 | foundations/decisions.md:2809 | whole |
| WAY-102/1 | foundations/decisions.md:2832 | whole |
| WAY-103/1 | foundations/decisions.md:2859 | whole |
| WAY-106/1 | foundations/decisions.md:2987 | whole |
| WAY-107/1 | foundations/decisions.md:3013 | whole |
| WAY-108/1 | foundations/decisions.md:3039 | whole |
| WAY-109/1 | foundations/decisions.md:3070 | whole |
| WAY-110/1 | foundations/decisions.md:3093 | whole |
| WAY-111/1 | foundations/decisions.md:3117 | whole |
| WAY-112/1 | foundations/decisions.md:3146 | whole |
| WAY-113/1 | foundations/decisions.md:3176 | whole |
| WAY-114/1 | foundations/decisions.md:3212 | whole |
| WAY-115/1 | foundations/decisions.md:3241 | whole |
| WAY-116/1 | foundations/decisions.md:3272 | whole |
| WAY-117/1 | foundations/decisions.md:3300 | whole |
| WAY-118/1 | foundations/decisions.md:3329 | whole |
| WAY-119/1 | foundations/decisions.md:3363 | whole |
| WAY-120/1 | foundations/decisions.md:3390 | whole |
| WAY-121/1 | foundations/decisions.md:3422 | whole |
| WAY-122/1 | foundations/decisions.md:3459 | whole |
| WAY-123/1 | foundations/decisions.md:3518 | whole |
| WAY-124/1 | foundations/decisions.md:3557 | whole |
| WAY-125/1 | foundations/decisions.md:3603 | whole |
| WAY-126/1 | foundations/decisions.md:3648 | whole |
| WAY-127/1 | foundations/decisions.md:3695 | whole |
| WAY-128/1 | foundations/decisions.md:3754 | whole |
| WAY-129/1 | foundations/decisions.md:3796 | whole |
| WAY-130/1 | foundations/decisions.md:3822 | whole |
| WAY-131/1 | foundations/decisions.md:3862 | whole |
| WAY-132/1 | foundations/decisions.md:3894 | whole |
| WAY-133/1 | foundations/decisions.md:3932 | whole |
| WAY-134/1 | foundations/decisions.md:3967 | whole |
| WAY-135/1 | foundations/decisions.md:4015 | whole |
| WAY-136/1 | foundations/decisions.md:4063 | whole |
| WAY-137/1 | foundations/decisions.md:4120 | whole |
| WAY-138/1 | foundations/decisions.md:4160 | whole |
| WAY-139/1 | foundations/decisions.md:4210 | whole |
| WAY-140/1 | foundations/decisions.md:4249 | whole |
| WAY-141/1 | foundations/decisions.md:4304 | whole |
| WAY-142/1 | foundations/decisions.md:4328 | whole |
| WAY-143/1 | foundations/decisions.md:4380 | whole |
| WAY-144/1 | foundations/decisions.md:4418 | whole |
| WAY-145/1 | foundations/decisions.md:4448 | whole |
| WAY-146/1 | foundations/decisions.md:4494 | whole |
| WAY-147/1 | foundations/decisions.md:4534 | whole |
| WAY-148/1 | foundations/decisions.md:4565 | whole |
| WAY-149/1 | foundations/decisions.md:4605 | whole |
| WAY-150/1 | foundations/decisions.md:4647 | whole |
| WAY-151/1 | foundations/decisions.md:4685 | whole |
