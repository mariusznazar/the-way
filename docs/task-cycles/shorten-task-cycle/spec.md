# Design — shorten the task cycle

## Intent and authority

The task changes the process that a future `implement-task` cycle follows. It reduces repeated
material in the orchestrator's context and work on invariant checks that protect changeable
implementation details. It preserves the evidence, checks and independent readers needed to bring
one ready task to a reviewable request.

The frozen task is [task.md](task.md). It is independent, ready for its cycle and has no human
actions. Its four accepted *Settlements to record* authorize the four meanings below. The
orchestrator provisionally approved this design under the task owner's delegation; that approval
is not human acceptance of the entries or the request. This cycle still runs under the process
from its base commit, `d04c3fe`; the changes below govern cycles that adopt the resulting pin.

Success is a clear, usable instruction change with all four settlements represented. No particular
time or token reduction is promised. The task's recorded measurements explain the need; they are
not a benchmark or a money-cost estimate.

## Chosen approach

Extend the existing cycle skill and record template with a small file-based handoff and return
contract. Keep the existing task record, plan, borrowed methods and checks. Do not add a runtime
scheduler, report parser, universal report schema, telemetry or custom context compaction.

A second approach would add separate handoff/report templates and a structural validator. It could
detect missing fields, but would add code and another contract beside the borrowed skills without
proving that a report is complete or correct. The chosen approach costs manual review of the
required evidence and may need revision if short returns repeatedly omit decisions. Keeping the
current wording would avoid that edit but would leave full reports and handoffs free to accumulate
in the orchestrator's context, and would not fulfill the task.

## 1. Handoffs, reports and the orchestrator's reads

The full dispatch instructions live in a file under the working cycle's `reports/` directory. The
dispatch message names that file and gives only the routing information needed to start its stage.
The file carries the existing dispatch contract: delegation, worktree, authoritative inputs,
applicable sources, stage and write boundaries, expected output/report paths and any relevant
ruling. Requirements and exact values stay in their authoritative files rather than being copied
into multiple prompts. Name files and relevant entries or ranges so an agent can find what it must
read. A requirement to read a source whole remains a requirement to read it whole.

An agent writes its complete, sanitized report to the named file. It follows its stage's report
requirements, including those of the borrowed skill. Where applicable, it records input versions,
result and boundary reached, changed files and commit ranges, questions and choices with evidence,
rejected alternatives and their costs, check commands and exit codes, failures, unchecked work and
unresolved concerns. This is not a new mandatory catalogue for matters irrelevant to that stage.
Git-held source files and diffs are referenced by path and commit rather than copied into the
permanent cycle record. Keep the borrowed method's transient review packages where its method
requires them; retain the review report and assessed commit range, not another archived diff.

The agent's return message contains its stage status, artifact/report paths, commits where any
exist, a short check result and every unresolved question or concern that affects the next dispatch.
A blocking question includes the concrete decision needed and points to the complete evidence. A
short return never replaces the report and must not conceal failed or unchecked work.

The orchestrator records the event and relevant choices before dependent dispatch. It reads the
source and the relevant report material before deciding a question, settling a finding, accepting a
foundation meaning or verifying disputed or incomplete evidence. Routine progression does not
require loading every full report into its context. Existing duties to read inputs, inspect diffs,
run checks and review the finished change remain. Where a source requires a whole entry or file,
selective reading does not override it. On resumption, the record, source paths and commits provide
the state; an agent's previous conversational history is not an input requirement.

A missing or incomplete report is repaired before dependent work proceeds. Resolve stale paths or
mismatched commit ranges against the actual worktree and record the correction. Do not treat an
agent's summary as proof of a missing check. The independent foundation assessor receives only its
allowed commit/diff and files, never the operational handoff packet, task chronicle, author reports,
spec, plan or author reasoning (WAY-10). File-based transfer must not widen that assessor's inputs.

Use the same contract for design, planning, foundation work, implementation, reviews and the return
step where their existing stage boundaries permit it. Reuse file-based briefs and returns already
required by Superpowers 6.4.1 rather than creating a second brief for the same work.

## 2. What the return step writes as an invariant

The return step still searches the real diff and choice log, compares the touched foundation with
the product and checks the task's accepted settlements and applicable projected entries. The
criterion for a newly discovered behavior is:

> Would changing this behavior in a later task violate a requirement or a settled rule of the
> product? If yes, preserve it with an invariant. If no, it is an implementation detail that may
> remain in ordinary tests and the description of the change.

An invariant required by an existing decision remains required (WAY-12, WAY-22). The criterion
cannot waive it, remove an existing invariant or omit an accepted settlement or a projected entry
that the task must write (WAY-126, WAY-134). No decision changes merely because a check is costly.
The task's example that every move ends on an adjacent tile remains a product rule; this task does
not edit that other product or import its game rules into the-way's foundation.

The return report identifies the behavior and foundation candidates actually found in the diff or
log, with the requirement or settlement supporting an invariant, or the reason a candidate remains
an implementation detail. It is not a compulsory inventory of every function or of every unchanged
behavior. A detail left out of the foundation remains visible in the applicable ordinary test and
change description; it is not a deferred foundation proposal. Existing obligations to record new
decisions, environment facts, glossary terms and part-map changes remain.

## 3. Assessment before breaks of return-step checks

Only invariant checks added in the return step change position. The resulting order is:

1. Write the return-step foundation entries and checks with the existing separate authors. Run the
   checks on the product and record their actual results.
2. Run the single independent assessment of the change's foundation entries and invariant tests,
   using the existing filtered input contract.
3. Settle every remark. If a settlement changes code, assessed foundation entries or invariant
   tests, rerun the affected checks and the affected code review. A settlement is part of the one
   assessment and does not request a second one (WAY-10).
4. Have the code reviewer, who did not write the check, review the final return-step check, then
   write the deliberate break from the final invariant sentence and run the check on it. Use the
   affected review already required in item 3 where it covers that check; do not add another
   whole-change review of an unchanged range. Record the required failure under WAY-08 and WAY-69
   before accepting the check.

A new check is not accepted merely because it passes on the product or because its assessment is
finished. A break that the check does not detect is a finding to resolve, not a passing result.
Remove or restore the deliberate break before the final clean verification. If a later correction
changes the final check or the behavior its break covers, repeat the affected verification; do not
present evidence for a superseded check as current. The existing reconciliation and review
invalidation rules remain.

Checks written before the return step retain their current acceptance and deliberate-break points.
Changes to the sentence, invariant test and covered code still use three different agents; the
code reviewer writes the break. The change does not replace the code review with the independent
foundation assessment or add a second whole-change review.

## 4. Independent slices and possible parallel work

`plan-task` recommends slices that a reviewer can judge separately and identifies possible parallel
work independently of the chosen execution skill. It keeps a dependency-ordered plan, one goal per
slice and the current `Change`, `Read`, `Checks` and `Depends on` fields. Avoid manufacturing slices
for their own sake or dividing inseparable changes merely to claim parallel work.

Add one short `Independence and execution` section to the plan. Derive its opportunities from the
slice dependencies and write sets, rather than adding a list of peers to every slice. Name the
independent slices and why they can be worked on separately, or say that no such opportunity exists.
The planner recommends a useful cut even when the currently adopted method must execute it
sequentially. A one-slice plan says there is no parallel slice work; it does not add a second slice.

Before execution, the orchestrator records whether the recommendation can be used: dependencies,
shared files or mutable worktree/test state, whether each review can assess its own range, and the
selected skill's restrictions. File separation alone is not proof of independence. Every slice
retains its own executor and independent review, and a multi-slice change retains its final review
(WAY-136). No two writing agents edit the same worktree concurrently.

With adopted Superpowers 6.4.1 `subagent-driven-development`, execution remains sequential because
that skill forbids parallel implementation subagents. Record that restriction beside the
recommendation; do not suppress the recommendation or silently override the skill. This task does
not adopt another method, change the Superpowers version or implement a parallel executor. The
project-plan rule in WAY-144 governs project tasks, not the slices of one task, and is unchanged.

## Foundation and affected files

The implementation needs the foundation route and the entry-writing skills before dependent work.
The intended allocation is:

| Accepted settlement | Entry to write or change | Meaning |
|---|---|---|
| 1 | A new decision on the cycle's handoff/report contract | Full material lives in files; short messages route work, while the orchestrator reads the evidence needed for decisions. |
| 2 | Edit WAY-11/1 in place | The return step preserves product requirements and settlements as invariants, while changeable implementation details stay outside the foundation; WAY-12 still applies. |
| 3 | A new decision on the order of return-step check acceptance | The independent assessment and its settlements precede deliberate breaks of checks added in the return step; earlier checks keep their position. |
| 4 | Edit WAY-136/1 in place | Plans recommend independent slices and show possible parallel work, with execution constraints and the orchestrator's assessment kept explicit. |

The entry writers choose final wording and numbers through their skills. Do not create an extra
version before `main` or a second decision answering WAY-11's or WAY-136's existing question. Update
WAY-11's verification examples. Recheck and renew its fingerprint in WAY-126 and
`return-step-record/1`; the latter's sentence and version remain unchanged if only its link changes.
Search all foundation files for other affected links and unlinked effects before accepting the
entries and again against the integration tip. No binding change to WAY-10, WAY-12, WAY-69 or
WAY-125 is needed for the selected design.

The process instructions change in `task-cycle/skill/SKILL.md`, `task-cycle/plan/SKILL.md` and
`task-cycle/record_template.md`. The record needs places for the handoff/report paths, the concise
coordination result, relevant return-step classifications, the assessment/break evidence and the
orchestrator's execution ruling; extend existing sections instead of adding a second ledger. The
existing glob `task-cycle/**` already assigns these files to their part. Existing parsers read
slice headings and `Change`/`Read`; a separate second-level plan section need not change their
syntax. No new script is part of the design.

## Decision revisions and human review

WAY-11 currently asks for uncovered code behavior to enter the foundation broadly. The new
criterion is an intentional narrowing authorized by the task's accepted second settlement, not an
editorial correction. WAY-136 gains an intentional recommendation authorized by the fourth
settlement. Preserve their current pre-`main` version numbers and show their full old and new
binding text and Polish meaning sentences for renewed acceptance at the request/merge.

The task already quotes the decisions and explicitly settles the changed meanings. Together with
WAY-134's narrowing of WAY-114 and the repository's pre-`main` integration route, that permits
preparing the entries and the instructions on the task branch; the orchestrator cannot accept
them as the human. No newly discovered contradiction remains to authorize this chosen scope.
If a writer or reviewer finds that implementing a settlement requires a further change of meaning,
cannot preserve its accepted meaning, or collides with an unamended decision, follow WAY-30 and
WAY-25: report the exact conflict and prepare a blocked draft rather than inventing precedence or
silently changing the settlement. Human acceptance of this request remains necessary.

## Verification and limits

Review the resulting instructions against concrete cases:

| Case | Required result |
|---|---|
| An agent finishes normally | Short return points to a complete report; the record can resume the next stage from files and commits. |
| A report has a failed or unchecked check, or an unresolved decision | The short return exposes it; the orchestrator reads its evidence before a dependent ruling. |
| A required decision-derived invariant is costly | The new criterion does not waive the invariant or its checks. |
| A discovered behavior is a replaceable implementation detail | The return record explains the classification; no new foundation invariant is invented for it. |
| Assessment changes a return-step check | Final checks run after settlement; its first acceptance break is written for the final version after assessment. |
| An invariant check was written earlier in the cycle | Its current break/acceptance point is preserved. |
| Two useful slices are independent but the skill forbids parallel executors | The plan states the opportunity; the execution record states sequential execution and the restriction. |
| Slices share a file, dependency or mutable state that prevents independent work | The orchestrator rejects parallel execution and records why. |
| A single slice covers the task | One slice, one whole-change review, no invented parallel work. |

Use the existing part tests and critical-flow tests: `python -B gate/run_tests.py task-cycle` and
`python -B gate/run_tests.py gate`. Run the decision and invariant format guards with the pre-`main`
`none` options their CLIs provide, including dependent fingerprint checks, and any other element
guard for an entry actually changed. Regenerate entry points if a skill's name, location or
description changes. Preserve failures, warnings and unchecked results in the review evidence;
these are partial checks, not the full product gate.

The foundation skills must derive any additional checkable invariant demanded by a decision and
keep WAY-69's separate authors; this spec does not waive that obligation. Tests that only match a
sentence's wording cannot establish that agents follow it. Evaluate semantic instruction changes
with the source comparisons and cases above, and keep the existing checks rather than claiming a
new automatic proof of agent behavior. Existing cycle-stage reporting can later show actual costs;
its implementation and new measurements are outside this task.

## Stage boundary

This is a design spec, not the task's implementation plan. It contains no product code, test bodies
or foundation entries. The next actor is an independent spec reviewer appointed by the
orchestrator. After review corrections, the designer returns before planning or implementation.
