# Independent spec review — selective document reading

Status: review complete; no design blocker; one verification correction to settle before planning.
Boundary: task-cycle spec review, step 7. This report is advice to the orchestrator, not human approval and not the later independent foundation assessment.

## Inputs and scope

- Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`.
- Tracked source revision and HEAD: `52b9d487efeafe37c46ad2b9f10d60c13a885e63`.
- Frozen [task](../task.md), read whole; SHA256 `dff4652dc2aa1b9a2b6dae1293f4cc5a8a3013983200da4c48e02ea1f2b852d6`.
- [Spec](../spec.md), read whole; SHA256 `09eff86e9e3ab6b949bd959090ea497b1e183feb01a5ef151a9d3fcabaac770d`.
- Reviewed against the current integration route, complete part map and glossary, the applicable complete decision and invariant entries, the shared reading/writing instructions and the affected reader skills. The decisive decision entries include WAY-12/17/21/22/31/33/37/44/62/95/97/111/114/115/118/120/134/146/148. The decision template and project-plan template were read whole.
- Applied the [review playbook](<C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/playbook_code_review.md>) and its linked [document-review guidance](<C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/wzorce_petli_review_dokumentu.md>). This is one bounded review, with at most a verification of fixes to named findings if the orchestrator requests it.
- Did not read the designer's report or the root conversation. No implementation, plan, tracked-source edits, git-state mutation, commits or subagents were used.

## Blockers

None found. In particular, replacing the whole-foundation clauses of WAY-111 and WAY-115 is expressly authorized by the frozen task; their current wording is not a reason to reject that change.

## Worth correcting

### 1. Include the tests of every reader part in the verification contract

**Severity:** important verification gap; bounded correction, no architectural redesign.

**Thread:** new.

**Anchor:** [spec, line 211](../spec.md#L211).

**Paste-ready:** The reader table changes skills in part-map, invariants, glossary and environment-facts, but the verification list omits those four existing test directories. Please add their runner commands, or explicitly state that the list is illustrative and that every changed part's tests remain required; changing an invariant skill already touches the invariants part even when the invariant data file stays unchanged.

**Why I am raising this:** The verification section is the concrete source the planner uses to name runnable checks. The [integration route, line 27](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/agent-instructions/README.md#L27) requires tests for each changed part. The spec itself includes [the part-map reader](../spec.md#L114), [the invariant reader](../spec.md#L115), [the fact reader](../spec.md#L116) and [the glossary reader](../spec.md#L117). The current map assigns those paths to their corresponding parts, and each directory contains an existing test suite. A planner treating the enumerated commands as the full verification set would run project-level, task-cycle, decisions and gate, yet skip four changed parts. The conditional instruction about an invariant *file* changing does not cover an invariant *skill* change on its own.

The small correction is to include `python -B gate/run_tests.py elements/part-map`, `python -B gate/run_tests.py elements/invariants`, `python -B gate/run_tests.py elements/glossary` and `python -B gate/run_tests.py elements/environment-facts`, retaining the existing common-part unchecked result and any additional checks the final diff requires. Leaving the wording costs no edit now but leaves the verification set ambiguous; clarifying it costs one sentence or four commands and the existing test runs. I have not found a claim that these omitted tests currently fail, and I did not run them in this design review. An explicit orchestrator ruling carried into the planner's handoff can also settle this gap without another design round.

## Checks with no concern

| Check | Evidence and result |
|---|---|
| Both accepted settlements survive | [Spec, line 180](../spec.md#L180) names a new decision carrying selective foundation reading; [line 184](../spec.md#L184) names a separate decision carrying selective definition/plan reading. Neither is dropped because it changes no executable code. |
| Decisions are found before a file diff exists | [Spec, line 51](../spec.md#L51) maps proposed behavior, responsibilities, integrations, flows and surfaces to existing parts and expands uncertain ownership. [Line 57](../spec.md#L57) then inspects all current Scope fields and reads every selected decision whole. This covers project definition and task refinement as well as code changes. |
| Entries collecting several parts retain their special rule | [Spec, line 52](../spec.md#L52) preserves WAY-44: changed entries determine touched parts rather than the containing file alone. |
| Selection can expand beyond outgoing links and initial parts | [Spec, line 63](../spec.md#L63) includes the applicable links, incoming dependents, Part `every`, method-file reach and critical flows. [Line 76](../spec.md#L76) searches all five foundation elements by meaning and alternative vocabulary. It expressly preserves WAY-33/37 and readiness-search domains and timing. |
| Scope completeness is evidence, not a new gate | [Spec, line 94](../spec.md#L94) distinguishes declared/loaded entries, semantic judgment and operational comparison. The parser's actual implementation handles latest versions and wrapped Scope values. It does not itself filter repeals or detect headings whose Scope is absent; the spec's repeal and malformed/missing-data instructions therefore remain necessary when that helper is used. |
| TODO method remains visible | [Current invariant](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/invariants.md#L407) still has Method TODO. [Spec, line 104](../spec.md#L104) explicitly preserves it and rejects describing the operational comparison, fingerprint checks or Scope validation as a pass of that method or of the full gate. |
| Large-plan resumption keeps a global inventory | [Spec, line 138](../spec.md#L138) inventories all scope items, projected headings, exact questions, plan task identities/dependencies and realizing/writing assignments before selecting resumed work. Rows and items are complete units. [Line 158](../spec.md#L158) expands to every row, assignment and question reached by dependency or meaning. |
| A new breakdown still covers the entire definition | [Spec, line 156](../spec.md#L156) requires processing every scope item, projected entry and question. Selection delays context loading; it does not permit a partial breakdown to stand as the whole plan. |
| Whole-document script checks remain on originals | [Spec, line 134](../spec.md#L134) retains readiness and plan checks against original authoritative files, not reduced copies. [Line 163](../spec.md#L163) preserves all WAY-146 structural obligations and the existing interface. |
| Independent semantic judgment remains complete | [Spec, line 168](../spec.md#L168) requires one critic to read the whole plan and obtain every source unit necessary for every task, technical element, moved question and quoted answer. The author's inventory cannot limit the critic. The existing handling of findings, rerun and human handover remains. |
| Necessary foundation consequences are named | [Spec, line 187](../spec.md#L187) changes WAY-111 in place while retaining conflict presentation; [line 191](../spec.md#L191) changes only WAY-115's foundation-reading requirement; [line 194](../spec.md#L194) requires rereading WAY-134 and renewing its actual incoming WAY-115 fingerprint. Additional linked and unlinked effects remain subject to search. |
| Required whole sources and approval boundaries survive | Templates, rules and complete examples remain required. Whole project-source reads outside plan-project, the candidate table and selection, stage boundaries, human acceptance and the independent assessor's filtered package remain explicit. No other cycle reorganization is introduced. |
| Cost is proportionate to the accepted task | One shared contract avoids independently maintained local selection rules. No persistent selector/index/manifest or public command is added. The spec acknowledges the reading and completeness evidence still cost work, and does not claim measured token savings. |

## Required Scope refresh for planning and foundation work

The proposed reader files touch eight parts: `decisions`, `part-map`, `invariants`, `glossary`, `environment-facts`, `elements-common`, `project-level` and `task-cycle`. A five-part inventory omitting the three element-reader parts is not complete for this proposed change.

I independently used the existing `latest_scopes` helper against the entire current decision log in a read-only `python -B` invocation. At the source revision, the five-part set selects 117 decisions; the eight-part set selects 128. The eleven additional matches are:

| Current decision | Scope field source | Reason it joins the set |
|---|---|---|
| WAY-08/1 | [decisions, line 215](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L215) | invariants |
| WAY-56/1 | [decisions, line 1581](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L1581) | invariants |
| WAY-58/1 | [decisions, line 1660](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L1660) | invariants |
| WAY-76/1 | [decisions, line 2131](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2131) | environment-facts and invariants |
| WAY-77/1 | [decisions, line 2160](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2160) | environment-facts and invariants |
| WAY-78/1 | [decisions, line 2190](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2190) | environment-facts and invariants |
| WAY-80/1 | [decisions, line 2246](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2246) | environment-facts |
| WAY-81/1 | [decisions, line 2283](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2283) | environment-facts and invariants |
| WAY-94/1 | [decisions, line 2577](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2577) | glossary |
| WAY-96/1 | [decisions, line 2656](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2656) | glossary |
| WAY-105/1 | [decisions, line 2951](https://github.com/mariusznazar/the-way/blob/52b9d487efeafe37c46ad2b9f10d60c13a885e63/foundations/decisions.md#L2951) | invariants |

This is a required application of the spec's touched-part and refresh rules, not a contradiction in the spec: its reader table names the added files and its shared contract does not freeze the initial part set. It establishes expected Scope matches, not proof that an agent read all 128 decisions or understood them. The planner and foundation author must refresh their own complete applicable reads and record expected versus selected/read identifiers at their actual input revision. Any further file or foundation-scope expansion requires another refresh.

## Checks executed and limitations

- Read-only source inspection, full-entry extraction, global instruction/foundation searches, file/hash inspection and git status/HEAD checks completed successfully.
- The read-only current-Scope calculation using the existing helper completed with exit code 0 and the counts above. An actual added Scope entry was also inspected as an original decision entry, not a quoted task mention.
- No test suite or format guard was run: no tracked change exists at this stage. No full-gate pass, actual-read automatic check, agent walkthrough execution or measured savings is claimed.
- The concrete scenarios in the spec are verification obligations for the final instructions, not evidence that those future instructions have already worked in an agent run.
- The frozen task supplies one motivating definition-reading/compaction case and a growth concern. I did not independently measure recurrence across session transcripts; no frequency or savings percentage is established by this review.
- Tracked worktree status was clean before writing this ignored report. The report is the only file this review writes.

## Return to orchestrator

No critical finding or unresolved product/design choice prevents planning. Settle finding 1 by correcting the verification wording or carrying an explicit all-changed-parts test requirement into the planner handoff. Require the eight-part Scope refresh and final actual-read evidence; do not reuse a five-part selection as complete. After that settlement, the reviewed design can proceed to the plan-task stage under a provisional orchestrator go-ahead. This review does not grant that go-ahead and does not invoke the next stage.
