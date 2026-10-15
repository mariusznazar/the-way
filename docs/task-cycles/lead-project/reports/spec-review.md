# Independent spec review: lead-project

Status: complete — no blocking findings.
Task-compliance verdict: pass at specification level.
Design-coherence verdict: pass at specification level.

Reviewed source revision: db77ba549cb9ece7d3e62bf29e1256973f62deab.
Worktree: C:/Storage/repos/the-way-wt/lead-project.
Author of this review: independent spec-review agent; not the spec designer.

## Blockers

None found. No missing task requirement, invented product outcome or contradiction with an unchanged applicable foundation rule warrants returning the design.

## Worth correcting

None established. The implementation considerations below are already required by the spec and are not requests to enlarge it.

## Nits

None reported.

## What the two review passes established

### 1. Document and task compliance

**Anchor:** C:/Storage/repos/the-way-wt/lead-project/.runs/task-cycles/lead-project/spec.md:7

**Review note:** The design preserves the frozen task's ownership boundaries: the project orchestrator leads refinement and maintains the plan, the human starts task cycles and accepts each complete task document, and project closure remains outside this skill.

**Evidence and reasoning:** I read the complete frozen task and complete spec. Task items 1–4 and 19 map to the outcome/components and handover change; items 5 and 12–13 map to state reconciliation and the result/state table; items 6–11 and 16–17 map to rounds, answering authority, file ownership and final acceptance; items 14–15 map to delegated plan edits and the definition gate; item 18 maps to dependency checks at cycle start. The real acceptance case is retained explicitly at spec.md:154. The task's accepted meaning changes to WAY-124, WAY-144 and WAY-134 are intentional changes, not defects against their previous wording. The new glossary meaning stays separate from the task-cycle orchestrator.

### 2. Prospective code contracts and integration

**Anchor:** C:/Storage/repos/the-way-wt/lead-project/.runs/task-cycles/lead-project/spec.md:95

**Review note:** The state reader has a feasible boundary with the existing code: reuse the plan parser in-process, extend parsed task values, verify definition readiness and approval, read Git evidence and report proposals without editing product documents.

**Evidence and reasoning:** I inspected project-level/plan_check.py, project-level/readiness_check.py, the complete task and plan templates and skills, define-project, relevant task-cycle source/record instructions, the installer skill registry and entry-point discovery/generation. The current Task data class does not retain State or Document; the spec explicitly anticipates extending it. The existing readiness checker accepts structurally valid status forms other than approved, so the new reader must implement the spec's explicit approval requirement rather than equating readiness_check.check() returning no findings with approval. The spec already requires rejection of unapproved definitions and a corresponding test; this is an implementation constraint, not an uncovered design choice.

The evidence table composes ready-to-in-cycle and in-cycle-to-done for a stale ready row, which is needed for the stated acceptance case. Completion uses freshly fetched remote integration history; missing evidence and host-only outcomes remain visible. Failed fetch cannot produce done. Exact task path matching, argument arrays, bounded Git operations and no PR-host executable in the reader are specified. Installer registration and regeneration of all entry-point sibling lists are assigned to their existing owners.

### 3. Workflow consistency

**Anchor:** C:/Storage/repos/the-way-wt/lead-project/.runs/task-cycles/lead-project/spec.md:67

**Review note:** Parallel refinement, a single round answerer and serialized writes of shared plan/definition files fit together. Human settlement, quoted evidence and final document acceptance remain distinct.

**Evidence and reasoning:** The contract prevents multiple writers of one conversation, keeps each refiner on its own document, pauses the orchestrator's plan writes during delegated structural edits, and routes child-agent requests through the project orchestrator. It distinguishes a code observation from a requirement, exposes quotation answers for rejection, and requires answers and provenance to survive in task documents before conversation cleanup. Definition edits retain the whole gate and fresh plan recheck; tasks cannot gain readiness while that gate remains open. Independent critique of the collective package remains required. These obligations preserve WAY-106, WAY-113, WAY-118, WAY-120, WAY-124, WAY-126, WAY-134, WAY-140 and WAY-145 under the task's accepted changes.

## Foundation selection and source record

Behaviorally touched parts: project-level, task-cycle, agent-instructions, installation. Read the complete current part map and inspected all current decision Scope fields, including wrapped values. The log has one current version per number and no Scope field missing from an entry. Expected Scope matches: 83; all were included in the reading, as complete entries. Explicitly named or linked entries expanded the selection with WAY-07, WAY-08, WAY-12, WAY-17, WAY-31, WAY-35 and WAY-49.

Read the applicable invariants selected from all Part fields, including every, the six WAY-09 dependants, the full glossary and environment-fact file. Searched the foundation for leading, orchestration, refinement, plan/task state, readiness and dependency concepts and checked incoming references to WAY-09, WAY-124, WAY-134 and WAY-144. No additional contradictory binding rule was identified. This review's search is supporting evidence only; it does not replace the foundation author's two required WAY-33 searches or the final independent WAY-10 assessment.

The 83 Scope matches, read in full, are WAY-01, 03, 09, 10, 11, 13, 16, 21, 25, 26, 27, 28, 30, 33, 34, 36, 37, 38, 44, 45, 46, 47, 48, 51, 55, 57, 62, 63, 65, 68, 69, 82, 89, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150 and 151; source: C:/Storage/repos/the-way-wt/lead-project/foundations/decisions.md, headings with those identifiers. WAY-31 is an additional explicit-task selection, not a Scope match.

## Checks and limits

This was one independent spec review with separate document and prospective-code passes. It changed no product file and launched no subagent. Git HEAD was verified as the supplied revision, and the tracked working tree was clean before this report. No implementation tests, live agent workflow trial, PR lookup or real loop2 acceptance run were performed: no implementation exists in this review range. The spec's verification section must be executed during implementation; this report is neither that evidence nor a pass of the full gate. New foundation wording still needs its required meaning acceptance and assessment.

Unresolved concerns affecting the next dispatch: none.
