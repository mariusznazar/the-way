# Whole-change review — one-author-small-change

## Inputs and boundary

- Base: `dc433059ffc7f94f9aaa43588dfe94ac869fb635`.
- Reviewed head: `10e36ef9be8194471661265edeeacf728fe8dfb9`.
- Foundation commit: `7513de82cb144f36e01b12eb8ef02970a382c2d9`.
- Worktree: `C:/Storage/repos/the-way-wt/one-author-small-change`.
- Requirements: the complete frozen [task](../task.md) and [plan](../plan.md), with the [review handoff](reviewer-handoff.md).
- Method: installed Superpowers 6.4.1 requesting-code-review and its complete code-reviewer template, the code-review playbook and linked document-review guidance. This is the single review of the only slice and the whole change. No subagents, fixes, tracked edits, index edits, branch operations, PR creation or merge were performed.

The review covered all eleven changed files and their surrounding instructions, including the unchanged cycle handoff, approval, verification, return, assessment and request steps. Code and documentation were inspected separately: the sole Python change changes the module description; the actual workflow change is in the instructions and foundation entries.

The implementation is cohesive: both routes use the existing shared stages, the planner remains available for changes needing division, and the author does not gain authority to approve foundation changes or review its own work. Detailed strengths are recorded below, after issue categories as required by the review playbook.

## Critical issues

None.

## Important issues

None.

## Minor issues

None. No stylistic alternatives are presented as defects.

There are no issue threads to open or additions to existing threads. The warnings and remaining cycle duties below are explicit limitations, not hidden findings or claims of completion.

## Strengths

1. **One common cycle with a clear execution choice.** [task-cycle/skill/SKILL.md:69](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L69) selects the route from the task; [line 175](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L175) repeats that judgment after a reviewed spec. Neither requires a preliminary plan. Foundation work, verification, assessment and request preparation remain shared.
2. **The author boundary preserves independence.** [task-cycle/skill/SKILL.md:225](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L225) keeps the same author for foundation, code and return work; [line 255](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L255) pauses that author for different invariant-sentence and check authors. The reviewer remains independent, with the existing deliberate-break order preserved.
3. **Failure recovery distinguishes different causes.** [task-cycle/skill/SKILL.md:198](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L198) sends an open design choice through discard and spec, [line 209](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L209) discards an oversized one-author attempt including its entries, and [line 217](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L217) retains completed reviewed slices when only a later planned slice is oversized.
4. **The record and public skill descriptions agree with the workflow.** [task-cycle/record_template.md:21](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/record_template.md#L21) records route, author identity, invariant authors, discard evidence and coverage review. The four generated entry points match their sources; the generator independently reports them current.

## Requirements and scenario results

These are semantic walks through the final instructions, not observed runs of the new route.

| Requirement or scenario | Result and evidence |
|---|---|
| To do 1; settlement 1: one author without a plan, including foundation and return work | Met. Step 4 selects from the task; the common execution introduction preserves the author's identity across foundation, code and return; step 11 resumes that author. See [skill:69](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L69), [skill:225](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L225), [skill:300](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L300), and [WAY-136:4081](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/foundations/decisions.md#L4081). |
| To do 2; settlement 1: separate invariant sentence, check and code authors | Met. The orchestrator pauses the author and dispatches two others, including for an invariant found in the return step; the record captures all three identities. Earlier check acceptance remains in step 10, return-step check acceptance follows assessment settlements in step 11. See [skill:255](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L255), [skill:293](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L293), [skill:335](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L335). |
| To do 3; settlement 2: oversized author returns no code and the whole attempt is discarded | Met. The report excludes code and diff; the task branch resets to its recorded base, including all foundation entries written for that attempt. The planner receives the task, reviewed spec if any, and report, without abandoned code or entries. See [skill:209](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L209), [planner:159](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/plan/SKILL.md#L159). |
| To do 4 and 7; settlement 3: sizing after a reviewed spec | Met for both outcomes. A settled spec that still fits one author proceeds without a plan, including when it spans several parts; a spec that grows the work beyond that judgment proceeds to a fresh plan. An earlier plan no longer binds. See [skill:172](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L172), [planner:156](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/plan/SKILL.md#L156), [WAY-135:4031](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/foundations/decisions.md#L4031). |
| To do 5; settlement 4: review inherits coverage and chronology checks | Met. The independent whole-change review expressly checks every task item, every settlement row, every carried projected entry, source fidelity and entries before dependent code against commits. A plan's only slice still gets only one whole-change review. See [skill:276](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L276), [record:41](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/record_template.md#L41). |
| To do 6; settlement 1: gate, return and independent assessment retained | Met. Step 10 retains sharpness recalculation, required gate and failed/unchecked reporting; step 11 retains source and uncovered-behavior checks, filtered independent assessment, settlement, and final check acceptance. Only the return-step author changes on the new route. See [skill:288](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L288), [skill:300](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L300). |
| To do 8; settlement 5: review conditions contain no token thresholds | Met. WAY-135 retains five cycles, late-found contradiction and 2026-11-30. WAY-136 retains five cycles, oversized one-author returns in two cycles out of three, more than one oversized planned slice in three, and 2026-11-30. See [WAY-135:4058](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/foundations/decisions.md#L4058), [WAY-136:4130](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/foundations/decisions.md#L4130). |
| To do 9: cycle, planner, record and sizing description agree | Met. The planner is conditional, artifacts are optional where planning never ran, request contents name the chosen route, and sizing measures an existing plan. The four entry-point descriptions were regenerated and independently checked. See [planner:19](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/plan/SKILL.md#L19), [record:80](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/record_template.md#L80), [skill:374](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L374), [slice_size.py:1](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/slice_size.py#L1). |
| Scenario 1: small settled task with foundation entries, no spec | Pass as written. Step 4 selects one author, foundation entries precede dependent code, the author returns between stages, an independent reviewer checks the whole change, and the same author performs the return step. |
| Scenario 2: no-plan task writing an invariant | Pass as written. Sentence, check and covered code have distinct authors; the check author receives the sentence and method without the code's reasoning; implementation cannot edit the invariant test without returning to the foundation step. Deliberate-break ownership and timing remain intact. |
| Scenario 3: small and oversized post-spec change | Pass as written. Step 7 repeats the same sizing judgment and permits either route. A spec does not itself force planning. |
| Scenario 4: oversized whole attempt | Pass as written. No partial foundation or code survives the reset. The cycle retains the report and discard evidence, and planning divides the change anew. |
| Scenario 5: open design choice found during execution or review correction | Pass as written. The report/discard/fresh-spec route is retained; after review the route is selected again. Correction instructions explicitly require a reset base for that correction, rather than silently assuming the original task base. See [skill:398](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L398). |
| Scenario 6: oversized planned slice | Pass as written. Reset is to that slice's starting commit and preserves earlier completed reviewed slices. The planner splits only the oversized slice and checks the new sizes. |
| Scenario 7: coverage, projected entries and chronology | Pass as written and for this diff. All nine task items and five accepted settlements are covered above; this task carries no projected entry. Foundation commit 7513de8 changes only the decision log; implementation commit 10e36ef follows it and changes the other ten files. The instruction coverage review also protects future tasks carrying projected entries. |
| Scenario 8: blocked human action and human-reserved contradiction authority | Pass as written. Existing external-action and irreversible-action restrictions, human decision authority, and blocked draft requests remain. WAY-30 adds a task-document carrier for known no-plan revisions while retaining approval by the decision's approver before dependent code and the stop for a newly discovered contradiction. See [skill:82](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L82), [skill:249](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/task-cycle/skill/SKILL.md#L249), [WAY-30:857](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/foundations/decisions.md#L857). |

The carrier updates are narrow. WAY-36 and both decision-template references keep temporary rules out of the foundation and give them the cycle's choices table when no plan exists. The projected-mode exclusion still belongs to a project definition. WAY-13 changes its example, rationale and approval carrier; its binding sentences remain exactly unchanged. No excluded orchestrator optimization, separate lightweight task process, stack-selection task or partial-cycle feature was introduced.

## Foundation selection and compatibility

The foundation revision is the reviewed head. The complete part map assigns the changed instructions to `task-cycle`, the decision template and skill to `decisions`, and generated entry points to `agent-instructions`; changed log entries also govern `task-cycle` and `decisions`. No changed file is a declared trust-boundary file. All touched parts have high criticality; no check was reduced on size grounds.

Inspection of every current Scope field, including wrapped values, produced 102 matches. The matches read were WAY-01, 02, 03, 04, 05, 07, 09, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 57, 60, 61, 62, 63, 65, 68, 69, 71, 72, 73, 74, 82, 84, 85, 86, 89, 90, 95, 97, 98, 99, 100, 101, 102, 103, 104, 106, 113, 114, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140, 144, 147, 148, 149 and 150, in [the decision log](https://github.com/mariusznazar/the-way/blob/aed12a81d7246dcef902e1920cb6f43de27970a1/foundations/decisions.md). Relevant linked rules, invariant entries selected by Part/every/method/critical-flow, the glossary, and relevant supporting fact entries were also read. No expected Scope match remains merely discovered and unread.

Searches across all five elements used author/one agent, planning/planner/plan, slice, spec, foundation and return steps, discard, temporary rule and contradiction vocabulary, plus explicit identifiers and incoming fingerprints. Search hits were distinguished from operative requirements: project-level plans and installer plans concern different work. The existing glossary definition of slice remains a piece set apart by a plan; the new one-author route does not call its change a slice. The environment-fact search did not reveal a new premise the changed entries needed to record.

A separate assertion found no incoming fingerprint references to WAY-30, WAY-36, WAY-135 or WAY-136 in foundation files. The positive control, WAY-13 references, remains present, and a byte-derived comparison of normalized binding text confirmed WAY-13's binding part unchanged. Only WAY-13, WAY-30, WAY-36, WAY-135 and WAY-136 differ in the log. Thus this diff does not leave an old incoming fingerprint requiring renewal. No invariant or invariant-check file changes in the reviewed range.

The change does not alter executable sizing logic, numeric limits, CLI arguments, exit codes or record parsing. An AST comparison of the base and head sizing modules with their first docstring expressions removed is equal. Repository searches found no consumer of the old `Spec and plan` record heading and no surviving unconditional task-plan instruction in the cycle, planner, entry points or request contents. No data migration or new runtime dependency is required.

## Verification performed by this reviewer

All commands below ran in the named worktree at the reviewed head. Tests were independent reruns, not inferred from the supplied final-checks summary.

| Command/check | Result |
|---|---|
| `python -B gate/run_tests.py task-cycle` | Exit 0; 41 tests pass. |
| `python -B gate/run_tests.py agent-instructions` | Exit 0; 18 tests pass. |
| `python -B gate/run_tests.py elements/decisions` | Exit 0; 169 tests pass. |
| `python -B gate/run_tests.py gate` | Exit 0; 98 tests pass, including the existing critical-flow tests. |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --today 2026-10-16` | Exit 0; 0 errors, 10 warnings, 5 unchecked. |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | Exit 0; 0 errors, 0 warnings, 3 unchecked. |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | Exit 0; 0 errors, 0 warnings, 7 unchecked. |
| `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | Exit 0; 0 errors, 0 warnings, 3 unchecked. |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | Exit 0; 0 errors, 0 warnings, 5 unchecked. |
| `python -B agent-instructions/skill_entry_points.py` | Exit 0; entry points are current. Read-only check; no `--write` run in review. |
| `git diff --check dc433059ffc7f94f9aaa43588dfe94ac869fb635 10e36ef9be8194471661265edeeacf728fe8dfb9` | Exit 0; no whitespace errors. |
| Base/head AST and foundation comparisons using standard-library Python plus `git show` | Exit 0; executable sizing AST unchanged, WAY-13 binding unchanged, precisely five expected log entries changed, no incoming references to the other four changed decisions. |
| `git diff --stat`, full diff, per-commit file lists and `git log`/`git show` | Eleven files, 227 insertions and 139 deletions; foundation-only commit precedes implementation. |
| `git status --short` and `git rev-parse HEAD` after checks | No tracked changes; head remains `10e36ef9be8194471661265edeeacf728fe8dfb9`. |

Total: 326 tests pass. The supplied [final-checks.json](final-checks.json) agrees with the independent reruns.

Warnings and unchecked work:

- Five pre-existing overdue review dates: WAY-03, WAY-21, WAY-52, WAY-55 and WAY-69, each 2026-10-02.
- Five pending `merge of <request link>` approval placeholders: WAY-13, WAY-30, WAY-36, WAY-135 and WAY-136. The cycle's existing request step replaces them once the PR exists; the head reviewed here does not yet have that URL.
- Nineteen unchecked guard results arise from the intentionally absent main/base/merge-onto comparison: decisions 5, invariants 3, part map 3, environment facts 3, glossary 5. They cover main-branch history and versions, template/log change coupling, merge TODO checks, merge copy and fingerprint comparisons, known violations and identifier/criticality comparisons, fact dependencies, and glossary changes/uses.
- Four additional part-map checks are unchecked individually: parts covered by `wording-reaches-dependants` (no coverage file); parts covered by `skills-reach-the-way-sessions` (no coverage file); promise-level declarations (no reporting command); dependency graph and new/stale dependency violations (no reporting command).
- No human-verdict file exists; the guards give no human verdict. This is an informational note, not a fabricated pass.
- The full gate does not exist for this pre-main repository. These tests and guards are partial verification only.
- No real one-author cycle pilot, compliance measurement, token-cost comparison or runtime-savings measurement ran. No new test mirrors instruction wording. No deliberate-break exercise is needed for this range because it changes no invariant check.
- The later return step, filtered WAY-10 assessment, final integration-tip reconciliation and search, PR placeholder replacement, and human merge decision are outside this review's execution boundary. This report does not claim those cycle stages have completed.

## Recommendations

Continue to the remaining cycle stages. Preserve the explicit warnings and unchecked work in the request. Replace the five URL placeholders through the established request step. Use the planned future pilot to observe whether the route is followed and whether it reduces cost; the present review establishes consistency of the instructions, not those empirical outcomes.

## Declined to judge

- Whether this change actually reduces time or tokens in live task cycles: no pilot or comparable run exists at this head, and measurement is explicitly excluded from the present claim.
- Whether the complete gate would pass: that program is not yet available; the actual partial checks are reported above.
- Whether excluded orchestrator-context optimization or a separate lightweight product-task process would be better: these are explicit task exclusions and are not introduced by the diff.
- Whether to approve the final merge: this review gives technical readiness; the remaining independent assessment and human decision retain their separate authority.

## Verdict

**READY — no code-review changes required.** The reviewed range satisfies the frozen task and plan, including all eight semantic scenarios, with unchanged executable sizing behavior and 326 passing tests. It is ready to continue through the remaining cycle stages and eventual human review; no unresolved defect was found. This verdict is not a full-gate pass, pilot result or merge approval.
