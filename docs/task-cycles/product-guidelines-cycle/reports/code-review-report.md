# Independent whole-change review

Verdict: PASS for the assigned review stage. No Critical, Important or Minor finding, either in scope or outside scope. No correction round is requested. This is not approval to merge and does not replace the remaining foundation assessment, return, reconciliation or final gate.

Reviewer: `/root/code_review`, independent of the author; 2026-10-19. No subagent was used. Product files were read-only; the only file written is this report.

Worktree: `C:/Storage/repos/the-way/.runs/worktrees/product-guidelines-cycle`.
Assessed base: `f98ac2fed3ab6ecbc1701e0c5f9a694dc9d91624`.
Assessed head: `fc0c946351154a8ee5747160dad55a857522fe86`.
The current worktree HEAD matched the assigned head and its tracked working tree was clean. The review uses the pinned cycle contract at the base, not the instructions this change introduces as its own authority.

## Scope and complete diff

I read the full base-to-head diff, including the foundation commit, and the affected files in context. Counts from `git diff --numstat <base> <head>` are 10 files, 534 added and 18 removed lines:

| File | Added | Removed |
|---|---:|---:|
| `foundations/decisions.md` | 333 | 5 |
| `foundations/part_map.md` | 3 | 2 |
| `product-guidelines/coding/SKILL.md` | 5 | 2 |
| `product-guidelines/reading.md` | 77 | 0 |
| `product-guidelines/styleguide/SKILL.md` | 3 | 1 |
| `project-level/plan/skill/SKILL.md` | 12 | 0 |
| `project-level/task/skill/SKILL.md` | 31 | 0 |
| `task-cycle/plan/SKILL.md` | 11 | 5 |
| `task-cycle/record_template.md` | 7 | 0 |
| `task-cycle/skill/SKILL.md` | 52 | 3 |

All source paths and line anchors below are relative to the named worktree and refer to the assessed head unless explicitly stated otherwise. Cycle sources and reports are under `.runs/task-cycles/product-guidelines-cycle/`.

## Source and read inventory

Read whole: the handoff, frozen `task.md`, reviewed `spec.md`, `reports/foundation-report.md`, `reports/implementation-report.md`; local `AGENTS.md`, `agent-instructions/README.md`; the applicable user review playbook and its document-review delegation; Superpowers 6.4.1 requesting-code-review skill and reviewer instructions. The Obsidian rulebook was read before accessing the private review instructions. No private source content is reproduced here.

Read the complete affected skill files and record template, the shared reader, `elements/common/way_of_working.md`, `elements/common/rules.md`, the decision and part-map templates, decision examples and the full part map and glossary. Selected foundation entries were read whole, including rationale and Rejected, rather than inferred from matching lines. Truncated reads were repaired with smaller reads.

Independent foundation selection at the assessed head:

- Touched parts: `task-cycle`, `project-level`, `product-guidelines`; `instruction-files` is additionally reached by the edited WAY-212 entry. The unchanged entry-point mechanism was considered as a consumer.
- Inspected the complete current Scope fields, including wrapped values. Expected matching current decisions, all read: WAY-01, 03, 09, 10, 11, 13, 16, 21, 25, 26, 27, 28, 30, 33, 34, 36, 37, 38, 44, 45, 46, 47, 48, 51, 55, 57, 62, 63, 65, 68, 69, 82, 89, 100, 101, 102, 103, 106–140, 142–222. Each is version 1 in the current log. Their locations are their complete `### WAY-NN/1` entries in `foundations/decisions.md`; WAY-213 begins at line 7266. Comparison of this expected set with completed whole reads found no missing match.
- Expanded whole decision reading included WAY-02, 04, 05, 07, 08, 12, 14, 17, 18, 19, 20, 22, 29, 31, 35, 40, 42, 54, 56, 58, 60, 61, 71, 72, 73, 76, 81, 85, 86, 90, 95, 97, 98, 99, 104 and 141, for verification, source fidelity, relation, entry-form and adjacent workflow questions.
- Inspected current invariant Part fields throughout `foundations/invariants.md`. Read whole the 66 entries whose Part matches the four touched parts or `every`, the additional methods naming the changed decision/map files, and `decision-guard-stale-reference/1`. This includes the guideline metadata/index guards, plan form/dependency rules, entry-point contract and the unchanged obligations for foundation assessment and return records.
- Read relevant environment facts whole: `git-path-patterns`, `impossiblebench-test-modification`, `llm-self-preference`, `llm-decision-violation-detection`, `single-rule-compliance`, `agent-run-variance`. No external fact is changed or newly asserted by this task. This review does not claim to have re-probed their external sources.
- Searched all five foundation elements by behavior and alternative terms, including guideline/styleguide, exemplar, screenshot/screen/visual/appearance, checklist, plan order, first file/code, waiting, plan change, Applies to, When to read, readiness, preparatory work, finding, states and running product. Relevant expanded entries were read whole. No unresolved collision, duplicate new decision or changed glossary meaning was found. This review search does not replace the cycle's later integration search.

## Requirement, settlement and order review

Manual review actor for this section: `/root/code_review`. Method: compare every frozen To do item and settlement with the complete diff, final callers and the foundation entries; trace the concrete branch/recipient, not merely the presence of words. Result and source evidence follow. Execution command, exit code and stdout/stderr fields: not applicable to this manual assessment.

| Frozen requirement | Result and evidence |
|---|---|
| To do 1: shared selection and every operational recipient; order example for planner or no-plan author | Covered by `product-guidelines/reading.md:27`, `task-cycle/skill/SKILL.md:131`, refresh at `:140`, borrowed/fix handoffs at `:143`, and `task-cycle/plan/SKILL.md:37`. Whole-source reads and each recipient's verification are explicit. The no-plan author does not depend on a planner having run. |
| To do 2: one lookup, absent files/kinds, departures and extensions | Covered by `product-guidelines/reading.md:12`, `:34`, `:39`, `:48`, `:52`, `:56`; refinement invokes it at `project-level/task/skill/SKILL.md:89`. Prospective code/UI is classified before a diff exists. Malformed or ambiguous metadata cannot silently yield no selection. |
| To do 3: missing discipline waits, including existing products, then resume after merge | `project-level/task/skill/SKILL.md:139` and `:151` keep the explicit waiting question and require reading/settling meanings after the prerequisite merges, before acceptance. A dependency alone gives no readiness. |
| To do 4: backlog versus project-plan ownership | `project-level/task/skill/SKILL.md:145` separates independent/source-only approval and backlog creation from `plan change` / `waits for task <n>`. Task status does not overwrite the plan row's state. |
| To do 5: first kind belongs in its creating task | `project-level/task/skill/SKILL.md:158` and `product-guidelines/reading.md:56` assign exemplar, kind file and index row without a circular prerequisite. Existing unindexed files receive comparison, not a false first-file classification. |
| To do 6: project breakdown | `project-level/plan/skill/SKILL.md:73` and `:113` use the shared reading, place actual prerequisite dependencies, reuse adequate tasks and retain first-kind work in the consumer task within the approved definition. |
| To do 7: state and screenshot checks | `task-cycle/skill/SKILL.md:319` covers the no-plan author and slice executor, beside the weakest-point check. Lines 324–327 distinguish no settled route from a failed settled route; line 543 carries unchecked evidence to the request. Code inspection is not represented as rendered evidence. |
| To do 8: appearance consequence determines grading | `task-cycle/skill/SKILL.md:442` supplies generic criteria for slice, whole-change and fix reviews; reviewer grade/scope authority remains at `:451`. No finding is pregraded. |
| To do 9: examples alone do not block | The same review contract requires a named user/correctness consequence while preserving binding rules and invariant checks. `task-cycle/plan/SKILL.md:151` records the plan's use of, or departure from, the order example without turning it into a rule. |

The ten Settlements to record map in order to WAY-213 through WAY-222. I compared their full text with the task, including the separate adoption of course practices in WAY-222, scoped departures, exceptions, continuation after prerequisites, and exclusions. The spec's D1–D3 choose selection ownership, classification evidence and generic review wording; they do not invent product meanings or a new severity scale. The independent task carries no projected entries, so projected-entry realization coverage is not applicable.

History independently confirms that `c0d12611ac10fed4a7fe5b904880ea803e7644bc` contains the two foundation files and precedes dependent implementation in `fc0c946351154a8ee5747160dad55a857522fe86`. The map permits the new project-level dependency and its existing product-guidelines file assignment covers the reader. WAY-212's binding wording remains unchanged; its surrounding explanation is reconciled with cycle reading. The request-link placeholders are an expressly unfinished cycle step, not a false claim that a request already exists.

## Actual scope, sharpness and weakest check

The author's scope assessment matches the actual diff: reversible process prose in high-criticality parts, without runtime code, schema, guard, test, invariant sentence/method, new status, root instruction or skill-description changes. No declared trust boundary is modified. The relevant risks are omitted recipients, mistaken semantic classification, conflicting ownership and overstated visual evidence. Source walkthroughs and independent review address these directly; an unrelated runtime security test would not.

I evaluated the author's WAY-164 check rather than treating its reported pass as an independent result. Its enumerated routes include spec author/reviewer, planner, both no-plan variants, one/multiple slices, their reviewers, the whole-change reviewer, fixes, replacements, return and reconciliation, plus the foundation assessor as a negative case. I traced these against the actual common handoff contract and its explicit inclusion of borrowed execution methods. The filtered assessor exception at `task-cycle/skill/SKILL.md:145` preserves that separate assessment boundary.

The check is sensitive to the likely miss: a planner-only example transfer would omit no-plan authors; a contract limited to direct orchestrator dispatch would omit borrowed slice handoffs; feeding operational commentary to the assessor would fail its negative case. The 23 author scenarios separately examine selection, missing/extended/first-kind guidance, approval and plan ownership, refresh, screenshot states and grading. Their concrete source states and resulting actions support a manual semantic comparison.

Neither that check nor this review proves that live agents will comply, that classification will be correct for every product, or that any real screen renders correctly. The report accurately identifies its scenarios as hypothetical source walkthroughs. There is no fabricated agent run or screenshot result. No unresolved concern justified rerunning the author's focused checks merely to progress this review.

The new decisions' level-2 verification is reasonable for these semantic actions and assessments; existing mechanical metadata, reference, index and plan checks are retained. I did not identify a new executable product contract hidden by that classification. Because no invariant sentence, invariant method, test or guideline good/bad example is changed, reviewer-authored deliberate breaks and new good/bad executions are not applicable.

## Strengths

- Selection and gap discovery have one source, while each caller keeps its own ownership and approval rules.
- The instructions address the less direct dispatch paths and preserve full-source reading rather than passing a summary or reviewer checklist.
- Missing disciplines, extensions and first-kind work have distinct consequences, avoiding both premature readiness and a circular wait.
- Failed interface access and absent access decisions remain distinguishable, with evidence limits carried to the request.
- Reviewer independence survives the new grading criteria; examples do not silently become binding rules.

## Findings

Critical: none. Important: none. Minor: none. In-scope findings: 0. Outside-scope findings: 0. No To paste / Why item is omitted or abbreviated; there are no findings to paste.

## Declined to judge

- Actual appearance or behavior of a consuming product: no product UI is changed or run in this task.
- Live agent adherence rates and the quality of every future prospective-part classification: no behavioral experiment is provided or claimed.
- Completion of the final gate and test suites running under the orchestrator: no result from an unobserved run is called passed here. Author command ledgers remain author evidence, not reviewer executions.
- Final acceptance of the foundation, completion of the return/reconciliation steps, and replacement of request placeholders: those belong to subsequent cycle stages.
- External-source freshness of unchanged environment facts and the pre-existing overdue-review warnings: this task does not revise those facts or settle those warnings.

## Recommendations and explicit assessment

Proceed with the existing cycle's remaining checks and independent foundation assessment. Preserve the documented unchecked outcomes and manual-evidence limits in the request; complete its approval links when the request exists. No additional fix or scope expansion is recommended by this review. No unresolved question requires an answer from the orchestrator or human to close this review stage.

No executable verification suite was run by this reviewer. Inspection commands read files, the diff, current HEAD, status and history; they are source acquisition, not claimed test passes. All conclusions above are the named reviewer's manual assessment of the exact assigned range. The report stops here without product edits, commits or beginning the return step.
