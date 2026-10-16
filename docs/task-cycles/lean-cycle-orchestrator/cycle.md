# Cycle record: lean task-cycle orchestration

- Frozen task: [task.md](task.md), approved 2026-10-16; independent task.
- Original source: `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/odchudzic_orkiestratora_cyklu.md`.
- Worktree: `C:/Storage/repos/the-way-lean-cycle-orchestrator`; branch `task/lean-cycle-orchestrator`.
- Process pin and target `foundations`: `41cfbe55c17981500490ffddd24fc1fe0ec1c6ef`; prerequisite PR #20 merged at that base.
- Completed implementation: `643bcfa8955e0abbe138dd5a0d95fec52400e433`; request-link-only commit: `88e185d`.
- Request: https://github.com/mariusznazar/the-way/pull/21. Implementation, reviews and assessment settlement complete; human decision remains at the request. No merge authorized or performed.
- Superpowers 6.4.1 verified from installed manifest. One author without a spec or plan: all five settlements already decided behavior, and the coherent change fit one agent. No discarded attempt or oversized slice.
- Actors: orchestrator, /root/author and /root/reviewer on gpt-6-astra; independent /root/assessor on gpt-6.1-sol. The same author performed foundation, implementation, return and correction; the same reviewer checked the correction.

## Sharpness at start and after the final diff

| When | Criticality and touched parts | Trust-boundary files | Reversibility | Consequent checks |
|---|---|---|---|---|
| Start | High: task-cycle has high undetected failures | None | Reversible git changes | Focused tests, available critical-flow tests, affected format guards, independent review and assessment |
| Final | Same; three files in foundation and task-cycle | None | Same | No reduction; final available verification repeated after A1 correction |

No new invariant or invariant check: these runtime coordination policies have promise level 2. A phrase-presence test would not prove that an agent obeys them. No deliberate-break stage applies. Skill names, descriptions and paths did not change; entry-point regeneration was unnecessary, and its existing tests passed.

## Events and dispatches

Exact dispatch messages are retained in [dispatch-log.json](reports/dispatch-log.json); handoffs and full reports below are the operational inputs and outputs. Stage durations, actual models and token counts are in [stages.md](stages.md). This snapshot ends before archival and final request publication; monetary cost is unavailable. The table reports input including cached input, not unique context or a measured saving.

| Stage | Actor | Inputs and method | Full output | Result and next step |
|---|---|---|---|---|
| Preflight and baseline | Orchestrator | Frozen task; pinned implement-task; repository README; selected foundation; Superpowers manifest | [Selection](reports/foundation-selection.md); baseline logs | Ready, independent; no human actions. Baseline 41 task-cycle and 98 gate tests pass. |
| Foundation | Author, turn 1 | [Handoff](reports/author-foundation-handoff.md); record-decision and whole required sources | [Report](reports/author-foundation.md) | `18602fd`: revise WAY-125/148, propagate WAY-140 reference, add WAY-157–160. Orchestrator read full evidence and actual foundation diff before provisional acceptance. |
| Implementation and wait clarification | Author, turn 2 | [Handoff](reports/author-implementation-handoff.md); test-driven-development; conventions | [Report](reports/author-implementation.md); [finding](reports/wait-mechanics-finding.md); [ruling](reports/wait-mechanics-ruling.md) | Native Claude completion notification confirmed against installed tools and official documentation. Foundation clarification `5d8a9f3` precedes dependent instruction commit `cf5f104`. 139 affected tests pass. |
| Whole-change review | Reviewer, turn 1 | [Handoff](reports/review-handoff.md); requesting-code-review; range base..cf5f104 | [Review](reports/review.md) | Full diff reviewed; no findings. Includes no-plan task coverage and foundation-before-code checks. |
| Initial completed-change verification | Orchestrator | Available README-required checks on cf5f104 | Superseded by final check outputs below | All 308 tests and three guards exit 0. Target refresh unchanged. |
| Return | Author, turn 3 | [Handoff](reports/author-return-handoff.md); WAY-11 and current foundation selection | [Report](reports/author-return.md) | No additional entries. Second whole-foundation search against current target; 432 references, zero stale fingerprints. Current verification reused. |
| Independent assessment | Assessor, one turn | elements/common/critique; only filtered tracked diff/files base..cf5f104, never task, operational handoff or reasoning | [Assessment](reports/assessment.md) | A1 requires distinguishing manual evidence from executed-command evidence. No other verified conflict. |
| Settlement | Orchestrator | Full assessment, actual clauses and whole WAY-61/83 | [Settlement](reports/assessment-settlement.md) | Apply A1; accepted behavior already allows manual methods. No human-only change of meaning. |
| Correction | Author, turn 4 | [Handoff](reports/author-fix-handoff.md) | [Report](reports/author-fix.md) | `643bcfa`: two paragraphs distinguish command fields and manual observation fields. 139 affected tests pass; return recheck finds no additional entry. |
| Affected review | Reviewer, turn 2 | [Handoff](reports/review-fix-handoff.md); cf5f104..643bcfa | [Review](reports/review-fix.md) | A1 closed; no new findings. This settles the single assessment rather than reopening it. |
| Final verification and reconciliation | Orchestrator | Final completed change at 643bcfa; refreshed origin/foundations still 41cfbe5 | [Commands, exits and summaries](reports/final-checks.json); [foundation search](reports/final-foundation-search.json) | All 308 tests pass, guards and whitespace exit 0. Full outputs retained. Final report names all unchecked results below. |
| Request preparation | Orchestrator | finishing-a-development-branch within cycle boundaries | PR #21; [publication checks](reports/publication-checks.json) | Draft opened, six approval placeholders replaced with URL only in 88e185d. Current guard has five pre-existing warnings. Backlog link added, worktree kept. |

After this snapshot the prescribed publication sequence commits this sanitized record and immediately commits its removal, pushes the pair, links the retained commit in the request, and marks the request ready. The commit history and PR state provide that publication evidence; no implementation changes belong to the pair.

## Questions and autonomous choices

| ID | Question and source | Choice and evidence | Alternative and cost if wrong | Used by |
|---|---|---|---|---|
| C1 | Repeated spaces in supplied path | Resolve the existing single-space project directory; heading and frozen content verified | Stop for typo; wrong resolution would select a different task | Preflight |
| C2 | Prerequisite ready? | PR #20 merged into foundations at recorded base | Starting earlier risks overlap | Branch creation |
| C3 | Spec or plan? | Neither: five accepted settlements, one coherent author-sized change under WAY-135/136 | Restating settled choices costs a stage; if size judgment fails, discard and plan | All author stages |
| C4 | Meaning changes authorized? | Accepted task explicitly revises coordination duties; WAY-30 applied only to these named meanings | Asking again duplicates acceptance; new unaccepted meaning would require stopping | Foundation |
| C5 | Effective wait | Blocking wait_agent up to 60 seconds because active higher-priority instructions limit blocking waits, though the live tool allows 3600000 ms; renew only after actual expiry | Tool maximum conflicts with active instructions; shorter effective limit costs more waits | All dispatches |
| C6 | How to record settlements | Four distinct new policy questions, revise WAY-125/148, mechanically propagate WAY-140; author foundation report Choices 1 | An omnibus decision couples unrelated later revisions; extra entries cost references | 18602fd |
| C7 | Which execution routes | Apply duties equally to one author and planned slices; task and WAY-136 | One-route-only text leaves inconsistent coordination; shared text must preserve stage boundaries | Foundation and skill |
| C8 | Wait renewal | Renew only after true timeout/interruption with pending work; handle input first | Repeated status calls recreate polling; never renewing strands bounded waits | WAY-157 |
| C9 | New invariant or prose test | Runtime policies remain level 2; no invariant or token-presence check; full report explains derivation | False automated assurance would mask noncompliance; limit is reliance on runtime practice and review | Foundation and verification |
| C10 | Environment entry or fixed timeout | No new empirical fact; live contract controls mechanism/limit | Fixed remembered numbers become stale; policy requires reading actual tool contract | WAY-157 |
| C11 | Claude waiting mechanism | Accept native completion notification as well as blocking wait, supported by installed tooling and official documentation; full finding and ruling retained | Blocking-only wording cannot describe background agents; notification wording must still prohibit polling | 5d8a9f3, cf5f104 |
| C12 | Repeat final checks after reconciliation? | Reuse if unchanged; rerun after A1 correction because completed change changed | Routine duplicate costs time; stale evidence after correction would be invalid | Final verification |
| C13 | Report implementation | Extend existing record template and skill, no new helper/framework | New machinery adds maintenance; prose still depends on agent compliance | cf5f104 |
| C14 | Review's declined judgments | Accept explicit limits: no measured savings or full live Claude pilot, unavailable full gate and prior debt outside scope; later cycle stages completed separately | Inventing results overstates evidence; real savings remain unmeasured | Request limits |
| C15 | Return entries | No further entry after candidate comparison and second whole-foundation search; original author's report | Duplicating existing policies adds maintenance; omission would matter if a candidate bound future work | Return |
| C16 | A1 manual evidence | Apply distinction after independent reading of assessment, actual text, WAY-61/83; full settlement linked above | Leaving unconditional command fields rejects valid manual checks or encourages invented exits; correction costs two paragraphs and affected verification | 643bcfa and affected review |

There are 16 autonomous choices; none is labeled human approval. No unresolved question or human action is left before review of the request.

## Verification and limits

Environment: Windows PowerShell, Python 3.14.3. Exact command arrays, exits and complete-output paths are retained in [foundation-checks.json](reports/foundation-checks.json), [implementation-checks.json](reports/implementation-checks.json), [fix-checks.json](reports/fix-checks.json) and [final-checks.json](reports/final-checks.json). Baseline commands are `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py gate`, both exit 0; [41-test output](reports/baseline-task-cycle.txt) and [98-test output](reports/baseline-gate.txt).

Final completed-change verification at 643bcfa: 41 task-cycle tests, 169 decision tests and 98 gate/critical-flow tests pass (308 total). Decision, invariant and part-map guards, with README-required no-main options, and `git diff --check` all exit 0. Final output files supersede the first completed-change run, rather than representing two separately retained runs. After the permitted URL-only swap, [publication checks](reports/publication-checks.json) verify exact substitution and current guard output; no behavior or binding sentence changes.

Remaining warnings: five unchanged review dates, all 2026-10-02, in WAY-03, WAY-21, WAY-52, WAY-55 and WAY-69. Six provisional request-link warnings in earlier output are resolved by 88e185d.

All 15 unchecked results remain visible in raw output and final-checks.json:

- Decisions, five no-main comparisons: existing lines/versions; template changes/version; TODO at merge; copies of shared versions; relation fingerprints at merge.
- Invariants, three no-main comparisons: identifiers/versions/corrections/violations; TODO at merge; linked fingerprints at merge.
- Part map, three no-main comparisons: known violations; identifiers; lowered computed criticality.
- Part map, four unavailable measurements: coverage for `wording-reaches-dependants`; coverage for `skills-reach-the-way-sessions`; a product command reporting promise levels; a product command reporting dependency graph.

The whole current-tree fingerprint comparison found 432 current references and no mismatch; this is not a simulated merge. The full gate does not exist yet, so no full-gate pass is claimed. No live full Claude cycle or future-cycle token/time comparison was run. Existing environment-fact probes were not run because neither their facts nor probes changed. No new invariant check required a deliberate break.

## Return and assessment

Both whole-foundation searches and scope-selection evidence remain in reports, with the second against current target 41cfbe5. Return candidates and their reasons are in [author-return.md](reports/author-return.md). The original author rechecked return implications after A1; no further foundation change was needed.

Assessment range: `41cfbe55c17981500490ffddd24fc1fe0ec1c6ef..cf5f104fb5fe1dcfb64ece84614efc5f784166cb`. Filtered files: `foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, plus tracked sources needed to interpret their binding rules. Different-model assessor received no operational materials. A1 settlement is covered by correction review through 643bcfa; the later URL-only substitution is the cycle's explicit exception to reopening assessment or review. No target reconciliation changed assessed sources.

## Request handoff

- Request: https://github.com/mariusznazar/the-way/pull/21, target foundations. Preserve commits when merging so archive links survive.
- Questions and human actions in cycle: none. Human review/merge remains outstanding.
- Backlog write: add `[url::https://github.com/mariusznazar/the-way/pull/21]` to this task's existing line in `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_tasks_active.md`; retain `[/]`. No task-source edit or vault commit.
- Process remarks: current harness's higher-priority responsiveness instruction limits each wait to 60 seconds despite the tool's larger bound. No status polling or sleeps were used to wait. Runtime compliance and savings are not established by passing repository tests.
- Archive exclusions: transient copied foundation entries, draft review template and editing scripts; git-held sources and diffs are referenced by commit rather than copied.
