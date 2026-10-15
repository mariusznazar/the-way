# Plan — Lead a project plan

- Task: `.runs/task-cycles/lead-project/task.md`
- Spec: `.runs/task-cycles/lead-project/spec.md`
- Base: `db77ba549cb9ece7d3e62bf29e1256973f62deab`

The frozen task binds over the reviewed spec. This plan contains no implementation or proposed foundation wording. New decision identifiers are allocated by the foundation author. Names A–E below identify the five groups settled in the spec, not additional product identifiers.

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| A — leading a handed-over plan, confirmed rounds, no cycle launch/closure, no recheck of ready dependants after merge | new decision | Settlements rows 1 and 9; spec Outcome, Start and resume | Slices 2–7 |
| B — evidence-backed plan state proposals, Git-only reader, PR fallback and human handling of conflicts | new decision | Settlement row 2; spec State-reader contract | Slice 1, Slice 3; evidence and subprocess invariants below |
| C — file-mediated turns, actor ownership, durable task answers and exact conversation cleanup | new decision | Settlement row 3; spec Conversation file contract and Final task acceptance | Slices 2–3 |
| D — answer authority, code observations versus prescriptions, unresolved choices and visible quotation answers | new decision | Settlement row 4; spec A round of refinement | Slices 2–3 |
| WAY-124/1 — complete-document acceptance for every task; review dependency on amended WAY-134 | decision amendment in place | Settlement row 5; To do 17; spec Final task acceptance | Slices 2–3 |
| WAY-144/1 — dependencies constrain cycle starts, not refinement; explicit question-based waits | decision amendment in place | Settlement row 6; To do 18; spec Plan and definition changes | Slices 2–3 |
| E — definition changes, delegated gate, independent critique, human approval and fresh plan recheck | new decision | Settlement row 7; To do 15; spec Plan and definition changes | Slice 3 |
| WAY-134/1 — candidate presentation and challenge routing through the project orchestrator | decision amendment in place | Settlement row 8; To do 10 and 16 | Slices 2–3 |
| project orchestrator | glossary term | Settlement row 10; preserve task-cycle meaning of bare orchestrator | Slices 2–4 |
| WAY-09/1 — project-level inventory includes leading and state reading | decision amendment in place | To do 1 and 5; spec Foundation changes | Slices 1–3 |
| WAY-135/1 incoming dependency on WAY-134, and any further incoming dependants found by the foundation search | reviewed dependent decision references | WAY-31; task Decisions in play; spec Foundation changes | All implementation slices |
| repository-file-location, element-directory-contents, relation-model-directory-contents, invariant-example-target, map-example-target, glossary-example-target | reviewed invariant dependency fingerprints; preserve sentences unless their meaning requires change | WAY-09 amendment and WAY-31; task Decisions in play | All implementation slices |
| project-plan-form/1 | reviewed invariant dependency fingerprint on WAY-144 | Settlement row 6; WAY-31; spec Foundation changes | Slices 1–3 |
| State-reader evidence invariant; independent check at `project-level/test_plan_state_invariant.py` | new invariant, identifier/sentence/method authored in foundation stage | Decision B; spec Foundation changes and Verification | Slice 1; code reviewer writes its deliberate break from the sentence |
| State-reader Git-only invariant; independent check at `project-level/test_plan_state_subprocesses_invariant.py` | required derived invariant added by return-step completeness correction R2 | Accepted settlement 2; Decision B; WAY-12/22 | Final review and post-assessment deliberate-break acceptance under WAY-149 |
| project-level responsibility, high false-progress failure mode, reader trust boundary and pinned state-reader CLI surface declared at `project-level/plan_state.py` main | part-map amendment and new surface | To do 1 and 5; spec Components and State-reader contract; WAY-44/48/49 | Slices 1–3 |

The foundation stage writes `foundations/decisions.md`, `foundations/invariants.md`, `foundations/glossary.md`, and `foundations/part_map.md`, through each entry's own project skill, before dependent implementation. It searches all five elements for incoming and unlinked effects, records the first search and preserves the later search against the integration tip. No environment fact is currently required; discovering one whose choice the task/spec does not settle returns to the orchestrator. No product projected entries are assigned: this is an independent task.

The invariant sentence author, check author and covered-code author must be three different agents. The separate foundation-stage check author receives the final sentence and method, not implementation design, and writes only `project-level/test_plan_state_invariant.py` from that contract. Inputs and expected results are independent literals. It runs against controlled Git repositories and the public reader CLI, with ordinary fixture construction allowed but no production computation of expected answers. The initial missing-reader failure is recorded, not hidden by a skip. The implementation author may read and run this check but may not edit it. A code reviewer who did not write the check supplies and records the deliberate break at the acceptance point for a foundation-stage check, then restores code and reruns clean. Existing invariant test files remain read-only throughout implementation.

Foundation commands: `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`; `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`; `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none`; `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`. Record all warnings and unchecked findings. A method/surface pointing to a file created by its dependent stage can report its absence before code exists; do not fabricate a stub or claim the guard passed. Rerun after the file exists. One independent assessment covers the completed foundation change and invariant check; it receives the filtered diff/files, not these operational reports.

## Slices

### Slice 1 — Report plan progress with Git evidence

- **Goal:** The new CLI validates original whole sources and reports only supported activity/completion transitions, exact evidence and explicit unresolved observations, without editing the plan or task documents.
- **Change:** `project-level/plan_state.py` · `project-level/plan_check.py` · `project-level/test_plan_state.py`
- **Read:** `.runs/task-cycles/lead-project/task.md` · `.runs/task-cycles/lead-project/spec.md` · `elements/common/way_of_working.md` · `foundations/part_map.md` · `foundations/invariants.md` · `foundations/glossary.md` · `foundations/decisions.md:1097-1126` · `foundations/decisions.md:1353-1422` · `foundations/decisions.md:1955-2028` · `foundations/decisions.md:2471-2532` · `foundations/decisions.md:3329-3362` · `foundations/decisions.md:4338-4581` · `project-level/readiness_check.py` · `project-level/plan/template.md` · `project-level/definition_template.md` · `project-level/test_plan_check.py` · `installation/install.py:138-176` · `task-cycle/record_template.md` ? `foundations/decisions.md:4739-4912` ? `project-level/test_plan_state_invariant.py`
- **Checks:** Begin with a failing ordinary test in `project-level/test_plan_state.py` for a ready row with a matching merged record producing both transitions and evidence. Add controlled repositories for worktree-only activity, branch-only archive, deleted merged branch, nondefault main, missing/ambiguous remote HEAD, failed fetch, shallow history, unavailable worktree, conflicting states, exact slugs, crafted/non-ASCII paths, invalid/draft plans and unapproved definitions. Exercise the public command and exit codes 0/1/2, bounded Git failures, original input preservation and Git-only subprocesses. Run `python -B gate/run_tests.py project-level` and `python -B gate/run_tests.py gate`; independently authored invariant check must pass once the reader exists. Do not change plan_check's CLI/exit codes or its protected tests. The code reviewer supplies the invariant break. Run the real acceptance command described below after this slice and retain the Git and host association evidence.
- **Depends on:** Foundation decision B, WAY-09, state-reader invariant/check and map/surface entries.

### Slice 2 — Refine through a resumable conversation file

- **Goal:** A fresh refiner and the round answerer can exchange sourced questions and answers through the agreed single-file contract; only the refiner edits task body, and manual refinement also waits for full-document human acceptance.
- **Change:** `project-level/lead/conversation_template.md` · `project-level/lead/answering.md` · `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
- **Read:** `.runs/task-cycles/lead-project/task.md` · `.runs/task-cycles/lead-project/spec.md` · `elements/common/way_of_working.md` · `elements/common/skill/SKILL.md` · `foundations/part_map.md` · `foundations/glossary.md` · `foundations/decisions.md:3176-3271` · `foundations/decisions.md:3557-3606` · `foundations/decisions.md:3971-4024` · `foundations/decisions.md:4259-4313` · `foundations/decisions.md:4428-4510` · `project-level/plan/template.md` ? `foundations/decisions.md:4739-4912`
- **Checks:** Before editing, document failing scenarios against current wording: a refiner asks the human directly, code is offered as a prescription, and a task with no candidates becomes ready without final acceptance. After editing, walk complete turns for each exact result phrase, same question in two tasks, rejected quotation, pending/placed Human actions, candidate challenge/rejection, accepted answer transfer with source, missing source/capability, and resumption. Check that final refiner line/return are identical phrases, ready for approval is not a task Status, all otherwise direct human questions return through the file, and canonical answers survive cleanup. Run `python -B gate/run_tests.py project-level` and `python -B gate/run_tests.py gate`. These are semantic review scenarios, not text-match tests proving agents complied; record any actual trial separately.
- **Depends on:** Foundation A, C, D, amended WAY-124/134/144 and project orchestrator term.

### Slice 3 — Lead rounds and route plan or definition changes

- **Goal:** The project orchestrator resumes from files, reconciles state, runs confirmed rounds, presents one package and accepts whole documents one at a time; dependencies block cycle starts and definition gates block readiness.
- **Change:** `project-level/lead/skill/SKILL.md` · `project-level/plan/skill/SKILL.md` · `project-level/plan/template.md` · `project-level/skill/SKILL.md` · `task-cycle/skill/SKILL.md`
- **Read:** `.runs/task-cycles/lead-project/task.md` · `.runs/task-cycles/lead-project/spec.md` · `elements/common/way_of_working.md` · `elements/common/critique/SKILL.md` · `foundations/part_map.md` · `foundations/glossary.md` · `foundations/decisions.md:2987-3038` · `foundations/decisions.md:3176-3271` · `foundations/decisions.md:3329-3421` · `foundations/decisions.md:3557-3757` · `foundations/decisions.md:3971-4024` · `foundations/decisions.md:4259-4581` · `foundations/decisions.md:4664-4738` · `project-level/task/template.md` · `project-level/task/skill/SKILL.md` · `project-level/readiness_check.py` · `project-level/plan_check.py` · `project-level/definition_template.md` ? `foundations/decisions.md:4739-4912` ? `project-level/plan_state.py` ? `project-level/lead/conversation_template.md` ? `project-level/lead/answering.md`
- **Checks:** Begin with scenario evidence of missing orchestration/handover/dependency rules. Review end to end: parallel refinement of dependent tasks; distinct transitive-dependant ranking and task-number tie break; one round answerer; one deduplicated human package with full quotation answers; critique dispatched by the project orchestrator; quote rejection returning to the human; refiner-only body changes; exact final acceptance recorded before Status/plan writes; interruption recovery; exact-file deletion only after transfer; explicit waits reoffered when their task is done; in-scope plan edit with serialized shared writes; human scope/projected-writer choice; delegated definition gate with human approval and fresh step-0 plan recheck; no ready during that gate; absent child-agent capability; all-done closure notice and no task-cycle dispatch. Review task-cycle start with unresolved dependency, delivered-in dependency and dropped dependency. Run `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py gate`. The last command will expose incomplete entry points until Slices 5–7; retain that expected failure, do not suppress it. No static string assertion stands for agent behavior.
- **Depends on:** Slices 1 and 2; all workflow foundation entries and amended WAY-144.

### Slice 4 — Expose leading in installed products

- **Goal:** A new installation exposes the pinned lead-project skill in both tool directories and preserves existing product files and installer semantics; documentation names the actual inventory without stale wrapper counts.
- **Change:** `installation/install.py` · `installation/README.md` · `installation/test_lead_installation.py`
- **Read:** `.runs/task-cycles/lead-project/task.md` · `.runs/task-cycles/lead-project/spec.md` · `foundations/part_map.md` · `foundations/decisions.md:980-1042` · `foundations/decisions.md:3699-3757` · `foundations/decisions.md:4314-4337` · `installation/test_install.py` · `installation/test_installed_guidance.py` ? `foundations/decisions.md:4739-4912` ? `project-level/lead/skill/SKILL.md`
- **Checks:** Start with a failing ordinary installation test in the new file showing the absent wrapper. Test preview/apply/repeat from a committed checkout, both wrappers byte-identical, expected pinned source path and sibling name, source availability after clone/submodule initialization, preserved product foundation/instructions and mismatch refusal. Keep existing invariant test files read-only. Run `python -B gate/run_tests.py installation` and `python -B gate/run_tests.py gate`; installer integration tests use the source commit containing Slice 3, not the old base. Critical-flow wrapper failures remain explicit until Slice 7.
- **Depends on:** Slice 3; existing WAY-34/127/141 and the accepted lead-project scope.

### Slice 5 — Generate foundation entry skill wrappers

- **Goal:** Both tools' five foundation entry wrappers contain the complete new sibling inventory, mechanically produced by the existing generator.
- **Change:** `.claude/skills/the-way-record-decision/SKILL.md` · `.agents/skills/the-way-record-decision/SKILL.md` · `.claude/skills/the-way-record-environment-fact/SKILL.md` · `.agents/skills/the-way-record-environment-fact/SKILL.md` · `.claude/skills/the-way-record-glossary-term/SKILL.md` · `.agents/skills/the-way-record-glossary-term/SKILL.md` · `.claude/skills/the-way-record-invariant/SKILL.md` · `.agents/skills/the-way-record-invariant/SKILL.md` · `.claude/skills/the-way-update-part-map/SKILL.md` · `.agents/skills/the-way-update-part-map/SKILL.md`
- **Read:** `.runs/task-cycles/lead-project/task.md` ? `.runs/task-cycles/lead-project/spec.md` · `.runs/task-cycles/lead-project/reports/planner-routing.md` · `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py` · `foundations/part_map.md` · `foundations/decisions.md:3699-3757` ? `foundations/decisions.md:4739-4912` ? `project-level/lead/skill/SKILL.md` ? `elements/common/critique/SKILL.md` ? `elements/common/skill/SKILL.md` ? `elements/decisions/skill/SKILL.md` ? `elements/environment-facts/skill/SKILL.md` ? `elements/glossary/skill/SKILL.md` ? `elements/invariants/skill/SKILL.md` ? `elements/part-map/skill/SKILL.md` ? `instruction-files/SKILL.md` ? `project-level/plan/skill/SKILL.md` ? `project-level/skill/SKILL.md` ? `project-level/task/skill/SKILL.md` ? `project-level/technology/SKILL.md` ? `task-cycle/plan/SKILL.md` ? `task-cycle/skill/SKILL.md`
- **Checks:** Use discover/produce in-process and write only these ten generated outputs, never hand-edit wrapper prose. Compare these exact output bytes with the generator's produce result, including each tool pair. Run `python -B agent-instructions/skill_entry_points.py` to report remaining work without writing it; run `python -B gate/run_tests.py agent-instructions` and `python -B gate/run_tests.py gate`, recording incomplete sibling-list failures until the other batches land.
- **Depends on:** Slice 3; WAY-127. Full skill frontmatter inventory must be stable.

### Slice 6 — Generate shared and task-cycle wrappers

- **Goal:** Both tools' shared/instruction/task-cycle wrappers expose the same complete sibling inventory.
- **Change:** `.claude/skills/the-way-critique/SKILL.md` · `.agents/skills/the-way-critique/SKILL.md` · `.claude/skills/the-way-find-foundation-entries/SKILL.md` · `.agents/skills/the-way-find-foundation-entries/SKILL.md` · `.claude/skills/the-way-maintain-instruction-files/SKILL.md` · `.agents/skills/the-way-maintain-instruction-files/SKILL.md` · `.claude/skills/the-way-implement-task/SKILL.md` · `.agents/skills/the-way-implement-task/SKILL.md` · `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md`
- **Read:** `.runs/task-cycles/lead-project/task.md` ? `.runs/task-cycles/lead-project/spec.md` · `.runs/task-cycles/lead-project/reports/planner-routing.md` · `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py` · `foundations/part_map.md` · `foundations/decisions.md:3699-3757` ? `foundations/decisions.md:4739-4912` ? `project-level/lead/skill/SKILL.md` ? `elements/common/critique/SKILL.md` ? `elements/common/skill/SKILL.md` ? `elements/decisions/skill/SKILL.md` ? `elements/environment-facts/skill/SKILL.md` ? `elements/glossary/skill/SKILL.md` ? `elements/invariants/skill/SKILL.md` ? `elements/part-map/skill/SKILL.md` ? `instruction-files/SKILL.md` ? `project-level/plan/skill/SKILL.md` ? `project-level/skill/SKILL.md` ? `project-level/task/skill/SKILL.md` ? `project-level/technology/SKILL.md` ? `task-cycle/plan/SKILL.md` ? `task-cycle/skill/SKILL.md`
- **Checks:** Generate only the named ten paths with discover/produce, compare their bytes against produce and verify identical tool pairs. Run `python -B agent-instructions/skill_entry_points.py`, `python -B gate/run_tests.py agent-instructions` and `python -B gate/run_tests.py gate`; retain incomplete project wrapper failures until Slice 7.
- **Depends on:** Slice 3; WAY-127. Full skill frontmatter inventory must be stable.

### Slice 7 — Generate project wrappers and verify the complete inventory

- **Goal:** All existing project skills and lead-project have current wrappers in both tools, and full generation changes nothing outside this final batch.
- **Change:** `.claude/skills/the-way-define-project/SKILL.md` · `.agents/skills/the-way-define-project/SKILL.md` · `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md` · `.claude/skills/the-way-refine-task/SKILL.md` · `.agents/skills/the-way-refine-task/SKILL.md` · `.claude/skills/the-way-settle-technology/SKILL.md` · `.agents/skills/the-way-settle-technology/SKILL.md` · `.claude/skills/the-way-lead-project/SKILL.md` · `.agents/skills/the-way-lead-project/SKILL.md`
- **Read:** `.runs/task-cycles/lead-project/task.md` ? `.runs/task-cycles/lead-project/spec.md` · `.runs/task-cycles/lead-project/reports/planner-routing.md` · `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py` · `foundations/part_map.md` · `foundations/decisions.md:3699-3757` ? `foundations/decisions.md:4739-4912` ? `project-level/lead/skill/SKILL.md` ? `elements/common/critique/SKILL.md` ? `elements/common/skill/SKILL.md` ? `elements/decisions/skill/SKILL.md` ? `elements/environment-facts/skill/SKILL.md` ? `elements/glossary/skill/SKILL.md` ? `elements/invariants/skill/SKILL.md` ? `elements/part-map/skill/SKILL.md` ? `instruction-files/SKILL.md` ? `project-level/plan/skill/SKILL.md` ? `project-level/skill/SKILL.md` ? `project-level/task/skill/SKILL.md` ? `project-level/technology/SKILL.md` ? `task-cycle/plan/SKILL.md` ? `task-cycle/skill/SKILL.md`
- **Checks:** Run `python -B agent-instructions/skill_entry_points.py --write` after both earlier batches; its diff must contain only these ten paths, or be empty after API generation of the batch. Then `python -B agent-instructions/skill_entry_points.py` must report current. Compare all 30 outputs and both tool pairs with produce(discover(ROOT)). Run `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py gate`, `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py installation`. No incomplete-wrapper failure remains acceptable at completion.
- **Depends on:** Slices 3, 5 and 6; WAY-127. Final aggregate installer check also follows Slice 4.

## Independence and execution

Slices 1 and 2 are useful independent work after their foundation prerequisites: separate files, separate CLI and conversation contracts, and independent reviews. Slice 3 joins them. After Slice 3, Slice 4 and the disjoint wrapper batches 5 and 6 can in principle be implemented/reviewed separately with stable source frontmatter and isolated workspaces; none writes another's files. Slice 7 must follow both earlier batches so its required whole-generation command has no unexpected write. The recommendation does not permit simultaneous writes in this worktree. Adopted Superpowers 6.4.1 subagent-driven-development forbids parallel implementation subagents: execution is sequential, one fresh author and independent reviewer per slice, followed by the whole-change review. The root records that ruling before execution. Parallel refinement described by the delivered feature is a different workflow and remains required.

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome: lead a handed-over plan to human-accepted ready tasks and maintain real states | A–E; Slices 1–3, exposed by 4–7 |
| To do 1: new lead-project skill | A; Slice 3; Slices 4–7 expose it |
| To do 2: human starts cycles separately | A; Slice 3 |
| To do 3: closure notice with no closure implementation | A; Slice 3 |
| To do 4: resume solely from plan/documents/conversations | C; Slices 2–3 |
| To do 5: Git state proposals, evidence, fetch, host fallback and conflict handling | B and invariant/map/surface; Slices 1 and 3 |
| To do 6: human confirms dependency-prioritized round | A; Slice 3 |
| To do 7: parallel fresh refiners, file turns, exact statuses, fresh answer transfer | C; Slices 2–3 |
| To do 8: refiner task body ownership, orchestrator Status only | C; Slices 2–3 |
| To do 9: quote/factual-code answer authority, prescriptions only from documents, deduplication | D; Slice 2 |
| To do 10: round package, candidates, Human actions, exact wording, challenge, quoted answers and rejection | D and WAY-134; Slices 2–3 |
| To do 11: whole document one at a time, human acceptance, both statuses, conversation deletion | WAY-124 and C; Slices 2–3 |
| To do 12: refinement states to refine/waiting for human | C; Slices 2–3 |
| To do 13: logged waits, resume proposal after named task completes | WAY-144; Slices 1–3 |
| To do 14: delegated in-scope plan changes, human scope changes | A; Slice 3 |
| To do 15: limited direct definition text edit, delegated gate/critique, human approval, fresh plan check, readiness stop | E; Slice 3 |
| To do 16: orchestrated refine-task never asks human directly | C, D, WAY-134; Slice 2 |
| To do 17: complete-document acceptance also in manual refinement | WAY-124; Slice 2 |
| To do 18: dependencies block cycles rather than refinement | WAY-144 and project-plan-form dependent review; Slices 2–3 |
| To do 19: plan-project handover points to lead-project | A; Slice 3 |
| Acceptance: original loop2 MVP plan task 3 mag-w-lesie proposes done with PR #12 evidence | Slice 1 real acceptance run, repeated during final verification if relevant implementation changes |
| Settlement 1 | A; Slice 3 |
| Settlement 2 | B, state-reader invariant/map/surface; Slices 1 and 3 |
| Settlement 3 | C; Slices 2–3 |
| Settlement 4 | D; Slices 2–3 |
| Settlement 5 | WAY-124; Slices 2–3 |
| Settlement 6 | WAY-144; Slices 2–3 |
| Settlement 7 | E; Slice 3 |
| Settlement 8 | WAY-134; Slices 2–3 |
| Settlement 9 | A; Slice 3 |
| Settlement 10 | project orchestrator glossary term; Slices 2–4 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Keep the Git reader and ordinary parser-extension tests in one implementation slice, with minimal Task state/document additions | A parser-only slice with no delivered state observation | Slice 1 carries more integration context; if too large, return it for split rather than retaining partial code |
| Put new ordinary tests in test_plan_state.py and test_lead_installation.py; protect existing invariant test files | Add ordinary assertions to the existing protected test files | Small fixture duplication is preferable to giving executors authority to edit invariant tests |
| Separate conversation/refiner ownership from leading/shared-plan routing, then integrate them | One author changes all workflow and reader files | The join needs explicit contract review in Slice 3; split prevents one oversized review |
| Generate three ten-file wrapper batches using existing discover/produce, final whole --write | Hide paths, exceed CHANGE_LIMIT or add a generator filtering feature | Temporary incomplete wrappers and extra sequential reviews; no runtime interface change |
| Explicit future read prerequisites, add them to Read and rerun size before dependent dispatch | Fabricated stub files or a claim that unknown text was already measured | One mechanical plan update per dependency; a later size increase can require splitting |
| Semantic scenario review for workflow prose, automated controlled Git tests for the reader | Assert skill wording strings and call that proof of agent behavior | Static review cannot establish actual agent compliance; any observed workflow trial must name its limits |

## Future prerequisites and measurement

Root ruling: `.runs/task-cycles/lead-project/reports/planner-routing.md`. Initial size measurement counts currently existing files; the following required future reads have not yet been measured. Before each dependent dispatch, add these paths to its Read field, add the new foundation entries as complete current ranges (existing ranges above are base-commit locators), and rerun `python -B task-cycle/slice_size.py .runs/task-cycles/lead-project/plan.md`. Do not dispatch a too-large or unchecked slice. Every receiving agent also expands its foundation selection under WAY-150.

| Future output | Consuming slice |
|---|---|
| Final foundation entries and revised complete entry ranges in foundations/decisions.md/invariants.md/glossary.md/part_map.md | All relevant slices as their dependencies specify; every slice reruns foundation selection |
| project-level/test_plan_state_invariant.py | Slice 1, read-only |
| project-level/plan_state.py | Slice 3 |
| project-level/lead/conversation_template.md; project-level/lead/answering.md | Slice 3 |
| project-level/lead/skill/SKILL.md | Slices 4–7 |
| Full discovered source SKILL.md frontmatter inputs to discover/produce | Slices 5–7; enumerate all current source files in Read before dispatch, including the newly created lead skill |

The generator currently discovers 14 skills and 28 outputs; the new skill makes 15 and 30. The three Change lists partition all 30 paths, not directories or globs. No change to the generator, protected entry-point tests, size thresholds or root agent instructions is planned.

## Acceptance and completion checks

Use the original plan path recorded in the frozen task; do not create a reduced plan. Run `python -B project-level/plan_state.py "<original plan path from frozen task>" .runs/task-cycles/lead-project/acceptance-loop2` after preparing the disposable clone's checkout as needed. This placeholder is a source lookup, not a guessed path; root supplies the exact private argument in the executor's ignored handoff. Verify task 3 mag-w-lesie produces the composed transition to done with actual Git evidence. Through the product's actual PR route, separately establish the relation to PR #12; the script never calls that route. Preserve the source plan and original repository unchanged. Store sanitized evidence under the cycle reports, never private fixtures or source paths in tracked examples.

After all slices, run the five named part suites and the four foundation guards, read every failure/warning/unchecked result, and retain the invariant deliberate-break result, slice reviews and whole-change review. Repeat acceptance only if reader-relevant fixes invalidate its evidence. The later return step and single independent foundation assessment remain with the orchestrator. These commands are partial repository checks, not a full gate. Final source search against current foundations and approval of integration remain the pre-main route's later stages.

## Return-step verification correction

After the seven implementation slices, source comparison found the narrower Git-only property was not covered by the generic script-subprocesses invariant. The foundation author wrote project-plan-state-subprocesses/1 and corrected WAY-153 Verification at 4d705b597cb4634f1c58a056558635f63f9cd407. A distinct check author adds its check; the code author remains separate. This is task-cycle return work for an already required behavior, not an eighth product implementation slice or a new design choice. Original per-slice size reports describe the inputs measured at their dispatches. Exact evidence: reports/return-git-only-answer.md and reports/return-git-only-foundation.md.

## Assessment settlement ? current task identity

After the final code review, the one independent foundation assessment found that plan-local names cannot establish ownership of a historical cycle. Correct WAY-153/evidence invariant and necessary fingerprints first; independent check author updates positive fixtures to existing provenance and adds same-name-plan/missing/ambiguous/foreign-trace cases; separate executor repairs reader and ordinary fixtures. Both protected checks remain read-only for the executor. Rerun affected suites, real loop2 acceptance and affected code/check review, then final deliberate breaks. This is task-cycle step 11 settlement, not an eighth original slice, second assessment or reopened design. Existing identity evidence from record/task templates suffices; no new field or global namespace. The source ruling and updated spec are authoritative.
