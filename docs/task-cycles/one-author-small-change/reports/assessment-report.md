# Independent foundation assessment

Assessor: gpt-6.1-sol. Author model supplied to the assessor: gpt-6-astra. One independent reader; no subagents. This report advises the orchestrator and does not approve a human settlement.

## Assessed material and boundary

Range: `dc433059ffc7f94f9aaa43588dfe94ac869fb635..10e36ef9be8194471661265edeeacf728fe8dfb9`.

Exact changed file set:

- `foundations/decisions.md`
- `task-cycle/skill/SKILL.md`
- `task-cycle/plan/SKILL.md`
- `task-cycle/record_template.md`
- `task-cycle/slice_size.py`
- `elements/decisions/template.md`
- `elements/decisions/skill/SKILL.md`
- `.claude/skills/the-way-implement-task/SKILL.md`
- `.agents/skills/the-way-implement-task/SKILL.md`
- `.claude/skills/the-way-plan-task/SKILL.md`
- `.agents/skills/the-way-plan-task/SKILL.md`

The changed decision entries are WAY-13, WAY-30, WAY-36, WAY-135 and WAY-136. The assessment covers their complete entries and the changed instruction targets, not just the added lines. The intended use is selection and execution of a ready task, before implementation and after a reviewed spec, with recovery when size or an open design choice invalidates an attempt.

Inputs were restricted to the diff, tracked instructions/code, foundation, invariant tests and relevant git history. No task, spec, plan, operational handoff, author report, chronology, session transcript, `.runs` content or `docs/task-cycles` content was read. The destination of this report was output-only. Relevant history was inspected through tracked file changes and commit metadata, without reading operational records or commit-message bodies that might contain the author's reasoning.

Governing sources include `agent-instructions/README.md`, `elements/common/critique/SKILL.md`, `elements/common/way_of_working.md`, `elements/common/rules.md`, the complete decision template/skill and their example WAY-03, and the complete part map. Foundation selection used the touched parts task-cycle, decisions and agent-instructions, complete Scope inspection including wrapped values, named decisions, linked rules, relevant invariants and the glossary. The Scope scan discovers 102 decision entries naming those parts. Initial broad outputs were truncated; bounded follow-up reads recovered the complete selected entries before this report was finalized. The selected set, all read whole, is WAY-01, 02, 03, 04, 05, 07, 09, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 57, 60, 61, 62, 63, 65, 68, 69, 71, 72, 73, 74, 82, 84, 85, 86, 89, 90, 95, 97, 98, 99, 100, 101, 102, 103, 104, 106, 113, 114, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140, 144, 147, 148, 149 and 150 (each version 1). Linked expansion additionally read WAY-08, WAY-40, WAY-56, WAY-115 and WAY-118 whole. The invariant Part inspection selected 92 entries naming these parts or every; these were read whole in bounded batches, together with the full glossary and relevant facts on independent assessment, oracle separation, test modification and git path patterns. Incoming fingerprint links to the changed decisions and wider vocabulary searches across all five foundation elements and tracked workflow sources produced no additional conflicting settlement. No source was reconstructed from a truncated result.

## Observations

### 1. Beneficiary, timing and mechanism

Sources: `foundations/decisions.md:4081`, `task-cycle/skill/SKILL.md:67`, `task-cycle/skill/SKILL.md:173`, `task-cycle/plan/SKILL.md:20`.

Checked whether the change removes work at the point where a small ready task otherwise receives a plan, and whether a spec accidentally forces planning. It does: the orchestrator chooses before implementation, repeats the judgment after spec review, and does not create a preliminary plan or run the size script to decide whether to omit the plan. The same author returns between foundation, code and return stages.

Consequence: a task fitting one author avoids the planner, plan review and repeated author handoffs, while design questions still get a spec. No concern found in this mechanism. No corrective change is requested.

This is a structural reduction in mandatory stages, not a measured reduction in time or tokens. The concrete originating case and whether this route would have acted in that case cannot be established from the permitted inputs.

### 2. Frequency, history and prediction

Sources: `foundations/decisions.md:4058`, `foundations/decisions.md:4130`; tracked history of `task-cycle/skill/SKILL.md` and the decision log.

The every-task planning rule entered in `b2e289f` on 2026-10-10 and was developed in `ea66949` and `dba4cf8`. The assessed range changes that recently introduced rule. Git history proves when instructions changed; it does not count actual cases of excess planning or successful execution. The permitted set contains no admissible operational population. Examined runtime cases: zero. No estimate of recurrence or savings is made.

Checked the removal of the old token-cost trigger as well as addition of the oversized one-author trigger. Both decisions retain review after five cycles and a check-by date; WAY-136 additionally names repeated oversized returns. This leaves a scheduled occasion to evaluate the prediction, although no quantified savings threshold remains. No contradiction or demonstrated regression follows from that removal in the permitted material. No corrective change is requested. The orchestrator should not describe the proposal as empirically proven.

### 3. Wider application and recovery cost

Sources: `foundations/decisions.md:4081`, `task-cycle/skill/SKILL.md:199`, `task-cycle/skill/SKILL.md:209`, `task-cycle/skill/SKILL.md:217`, `task-cycle/plan/SKILL.md:161`.

Checked three different recoveries: an open design choice discards the whole attempt and returns to design; an oversized one-author attempt discards the whole attempt and proceeds to planning; an oversized planned slice discards that slice and preserves earlier reviewed slices. The instructions distinguish the reports, reset points and the material that the next agent receives. A reviewed spec permits a fresh route decision rather than automatic planning.

Consequence: an optimistic size judgment costs abandoned work. Reusing a single author also increases the risk of foundation wording following the implementation's shape. These are real tradeoffs of the proposal, explicitly acknowledged by WAY-136; the proposal does not eliminate them. No unsupported fixed size threshold is introduced. No concern requiring correction found in the specified recovery. No corrective change is requested.

### 4. Independence is retained where it matters

Sources: `foundations/decisions.md:1957` (WAY-69), `foundations/decisions.md:4084`, `task-cycle/skill/SKILL.md:225`, `task-cycle/skill/SKILL.md:254`, `task-cycle/skill/SKILL.md:276`, `task-cycle/skill/SKILL.md:323`.

Checked whether one author can also write the invariant sentence or check, review its own code, or replace the independent assessment. The exception is explicit: the invariant sentence and check come from two other agents; the author pauses for these dispatches. It applies to invariants found at the return step too. The code reviewer remains different from the author, and the independent assessment retains its filtered inputs and separate model where available. Return-step check acceptance still follows WAY-149.

Consequence: one author combines ordinary foundation, code and return work but cannot combine the three invariant authorships or self-accept the finished change. No concern found in that separation. No corrective change is requested. Actual dispatch identity and clean assessor inputs in a real cycle are outside this assessment's admissible evidence.

### 5. Coverage and ordering survive removal of the plan

Sources: `task-cycle/skill/SKILL.md:233`, `task-cycle/skill/SKILL.md:276`, `task-cycle/record_template.md:42`, `foundations/decisions.md:4097`.

Checked where plan review's task coverage, accepted settlement coverage, projected entry coverage, source fidelity and foundation-before-dependent-code checks go when there is no plan. They move explicitly to the independent whole-change review, against the commits. The record template carries these checks and author identity. Shared execution, sharpness, full verification, return, assessment and request steps remain common to both routes.

Consequence: the no-plan route does not silently waive these checks. They occur later, so a coverage mistake can cost code and rework before it is found. This is a cost shift, not proof that the same mistake will be caught equally often. No missing obligation was found in the changed routing. No corrective change is requested.

### 6. Temporary rules and human authority

Sources: `foundations/decisions.md:858`, `foundations/decisions.md:1046`, `elements/decisions/template.md:119`, `elements/decisions/template.md:221`, `elements/decisions/skill/SKILL.md:32`, `task-cycle/record_template.md:73`, `task-cycle/skill/SKILL.md:249`.

Checked that removing a plan does not push temporary exclusions into the decision log or let an orchestrator approve a contradiction. WAY-36, the decision template and its skill agree that temporary rules belong to cycle choices where no plan exists. WAY-30 instead places a known required decision revision in the accepted task document and requires the decision approver before dependent code. The choice log is not authorization for an exception; the cycle's blocked-draft mechanism preserves the human boundary.

Consequence: the two destinations serve different purposes and do not conflict: temporary execution choices stay with the cycle; changed product rules remain in the foundation and require the appropriate human approval. No concern found. No corrective change is requested. Whether a particular human accepted the task's changed meaning cannot be established from the filtered inputs and is not approved here.

### 7. Form, source fidelity and duplication

Sources: `elements/decisions/template.md:93`, `foundations/decisions.md:4029`, `foundations/decisions.md:4081`, `task-cycle/slice_size.py:1`, both implement-task entry points at line 3, both plan-task entry points at line 3.

Checked the five edited entries against the decision form and compared the settlement with the skills, record and generated entry points. The changes keep existing decision numbers in place under the pre-main integration rules; WAY-13's binding wording is unchanged, while its example/rationale now fit the revised preparation. WAY-135 and WAY-136 divide spec selection and execution division. WAY-30 and WAY-36 repair consequences of having no plan instead of creating another overlapping decision. The size script changes only its explanation of when it is used, not its runtime thresholds or parser. Generated entry points describe the same route as their sources and the generator reports them current.

No contradictory or duplicated settlement was identified in those comparisons. No corrective change is requested. The private installed Superpowers source named in the existing Based on fields was outside the permitted input set; its quoted observation was not independently remeasured. Fidelity to the excluded task/spec/human conversation is also unverified, rather than inferred from fluent wording.

## Cuts and cheaper alternatives

Nothing in the changed file set is identified for a necessary cut on the evidence examined. The dependent decision/template changes have a concrete role: without them temporary rules or decision revisions still require a plan the cycle no longer writes. The generated entry-point edits keep discovery accurate. The script documentation prevents treating a planned-slice measurement as the route selector.

The cheapest competing approach is to retain the former one-slice plan and its single whole-change review. That has less route-specific instruction maintenance and gives coverage/order review before code, but preserves the planning and author-transfer work the proposal seeks to remove. Removing only the plan while keeping separate ordinary foundation and return authors would save one stage while retaining repeated context transfer; no permitted measurement establishes that this partial alternative is better. Skipping review, assessment or invariant separation would be cheaper per run but changes the required checks and is not the same effect. A conversation at the point of use would add human interruptions and does not preserve the autonomous cycle's contract. No additional artifact, routing script or numerical no-plan classifier is warranted by this assessment.

## Checks performed and limits

- `python -B gate/run_tests.py task-cycle`: exit 0; 41 tests passed.
- `python -B gate/run_tests.py gate`: exit 0; 98 tests passed.
- `python -B agent-instructions/skill_entry_points.py`: exit 0; entry points are current. An initial `--check` attempt was rejected because that option does not exist (exit 2); the documented default check was then used.
- `python -B elements/decisions/format_guard.py --base none --merge-onto none`: exit 0; 0 errors, 10 warnings, 5 unchecked. Warnings comprise five request-link placeholders and five overdue existing review dates (WAY-03, WAY-21, WAY-52, WAY-55, WAY-69). Unchecked items are log prefix/version preservation, template-change comparison, merge TODO checks, copies of shared versions, and relation fingerprint comparisons, because the specified main-branch comparison commits do not exist.

These are partial mechanical checks. They do not prove that agents follow the new path, that complete-source reading was performed in a real cycle, that the gate is complete, or that the change saves money. No tracked file was edited by the assessor. The existing ordinary slice-size tests check the unchanged measurement behavior, not agent routing.

## Assessment outcome

No actionable defect was established in the substantive checks above. Recommendation from the inspected material: apply the proposed mechanism, without claiming measured success. The required reading audit was completed within this same assessment after the initial output truncation; no reading-coverage objection remains. Human acceptance of the changed meanings remains reserved to the human; the assessor makes no settlement and no edit.
