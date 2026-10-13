# Design report — shorten-task-cycle

## Result and boundary

- Actor: design agent `/root/design`, inherited model and reasoning settings.
- Worktree: `C:/Storage/repos/the-way-wt/shorten-task-cycle`.
- Base read: `d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b`.
- Input handoff: `reports/design-handoff.md`, relative to this cycle.
- Output: [spec.md](../spec.md).
- Result: corrected written spec returned after independent review; its one finding applied. The
  orchestrator owns the already-dispatched scoped confirmation and written-spec go-ahead. No
  implementation, plan, foundation edit or commit.
- Open design questions: none after the provisional rulings recorded below.
- Time, token use and cost: unavailable to this agent; the cycle's stage report can supply them.

This report records findings and decisions, not hidden reasoning. The process to execute this
cycle remains the process at its base commit; the proposed changes do not authorize this cycle to
skip or reorder its own checks.

## Method and shared understanding

Used installed Superpowers 6.4.1 `skills/brainstorming/SKILL.md`, read in full, under the-way's
design-stage adapter. Classified the task as **architectural** because it alters stage interfaces
and the ordering of return-step verification. The adapter requires the architectural path and
redirects the written spec to the ignored cycle directory; it prohibits a commit, planning or
invoking the next skill at this stage. No visual question arose, so no visual companion was
offered. No web research was needed: the frozen task, local checkout and installed skill provide
the sources.

Reflected the intent to the orchestrator: reduce repeated orchestrator context and work on new
invariant checks, preserving full evidence, mandatory checks and a separate review for each slice.
The orchestrator confirmed this as provisional delegation, not human approval. The design promises
an instruction change that makes these choices concrete, not a specified measured saving.

## Inputs read

Repository/process sources:

- `AGENTS.md`, `agent-instructions/README.md`, `.agents/skills/the-way-implement-task/SKILL.md`.
- `task-cycle/skill/SKILL.md` in full, `task-cycle/plan/SKILL.md` in full and
  `task-cycle/record_template.md` in full.
- Frozen `task.md`, including all four accepted settlements, questions and exclusions.
- `foundations/part_map.md` and `foundations/glossary.md` in full; the violated-invariant list.
- `task-cycle/slice_size.py` through its parser, measuring/reporting functions and CLI start, to
  check whether another second-level plan section affects the existing parser.
- Recent git history and base identity.

Applicable decisions read as complete entries: WAY-01, WAY-03, WAY-05, WAY-07, WAY-08, WAY-09,
WAY-10, WAY-11, WAY-12, WAY-13, WAY-14, WAY-16 through WAY-22, WAY-25 through WAY-28,
WAY-30 through WAY-38, WAY-44 through WAY-49, WAY-51 through WAY-55, WAY-57, WAY-62, WAY-63,
WAY-65, WAY-68, WAY-69, WAY-74, WAY-82, WAY-83, WAY-89, WAY-100 through WAY-107,
WAY-114 through WAY-117, WAY-124 through WAY-126, WAY-134 through WAY-136, WAY-140, WAY-144
and WAY-147. The report does not claim to have read all other decision entries. Entry-writing
agents must read the full rules applicable to the entries they actually write.

Read whole invariant entries whose *Part* is `every`, plus the direct WAY-10/WAY-11/WAY-12
dependents returned by the search. Particularly relevant: `foundation-change-assessment-record/1`,
`return-step-record/1`, `invariant-test-break/1`, `foundation-change-path/1`,
`foundation-search-record/1`, `level-one-decision-invariants/1`,
`verification-invariant-derivation/1`, `decision-verification-level/1`,
`invariant-citation-target/1`, `link-fingerprint-value/1`, `skill-entry-points/1` and
`instruction-file-imports/1`. Read the whole `context-file-effect/1` fact after finding it; it
concerns repository context files and is not taken as a measurement of this proposed contract.

Installed external sources read:

- `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/brainstorming/SKILL.md`
  in full.
- Relevant sections of that installation's `subagent-driven-development/SKILL.md`, lines 231–282
  and 315–330: it already uses task-brief/report files and short returns, supplies reviewer
  packages by path and forbids multiple parallel implementation subagents. This was reference
  reading, not invocation of its execution stage; the execution agent must read its full method
  and linked files when that stage begins.

## Whole-foundation collision search

Search covered all files under `foundations/`, not only overlapping scopes. Initial command:

```text
rg -n -i 'task-cycle|return step|deliberate break|assess|orchestrat|handoff|dispatch|agent report|context|parallel|side by side|slice|code behavio|uncovered behavio|ordinary test|invariant.*behavio|test.*invariant' foundations
```

Follow-up searches used `WAY-(11|125|136)@`, the affected invariant identifiers, and headings to
read complete entries. Read the glossary and part map whole to catch effects outside keyword
matches. Findings and disposition:

| Finding | Effect on design |
|---|---|
| WAY-11 broadly requires uncovered behavior to enter the foundation | Revise its meaning explicitly from accepted settlement 2, including verification examples. Do not call this editorial. |
| WAY-126 and `return-step-record/1` carry WAY-11's fingerprint | Recheck whole entries and renew the link with the foundation change; their current meanings can remain. |
| WAY-12 and WAY-22 require decision-derived invariants | The new criterion cannot waive those checks or convert them to ordinary tests. |
| WAY-10 permits one assessment including its settlements | Keep one independent assessment; moving return-step breaks after it needs no amendment to this rule. |
| WAY-08, WAY-69 and `invariant-test-break/1` require a failing break and separate authors | Preserve all of them after reordering; passing the product check or assessment alone does not accept a check. |
| WAY-125 adopts version 6.4.1 and reserves human decisions | Keep that version and its sequential execution. The file contract supplements the adapter without replacing a borrowed method. |
| WAY-136 lacks the requested recommendation of independent slices | Revise it from settlement 4; preserve one executor/reviewer per slice and the final review. |
| WAY-144 derives possible side-by-side project tasks from dependencies | Applies to project plans. No project-plan change; the task-slice plan uses a short derived explanation, not a peer field per slice. |
| WAY-134 carries accepted settlements and narrows WAY-114 | Preserve all four meanings; do not turn them into optional design choices. |
| WAY-07, WAY-30 and pre-main README govern revisions | Prepare in-place edits on the task branch, preserve versions and request renewed human acceptance of the changed meanings. Further unapproved collisions require a blocked draft. |
| WAY-33 and WAY-31 require searches and dependent renewal | This design search is evidence for the stage, not a substitute for entry-writing and pre-integration searches. |
| WAY-36 distinguishes lasting rules from task choices | Permanent handoff, criterion, order and recommendation meanings belong in decisions; this cycle's provisional rulings stay in its record. |
| WAY-52, WAY-128-related context findings and `context-file-effect/1` concern always-loaded/generated guidance | Do not expand into generated overviews, global instructions or a performance research task. |
| WAY-27 prohibits private reasoning links in committed material | Foundation entries must carry their reasoning without linking to the private task note. The frozen source stays in the sanitized cycle record. |
| Part map already claims `task-cycle/**` | No new part or surface follows from the chosen existing-file instruction changes. |
| `foundations/violated_invariants.md` lists only `surface-promise-level/1` | No new violation, quarantine or waiver is proposed. |

The direct identifier in this checkout is `return-step-record/1`; the handoff's name
`task-return-record` does not name an entry. No invariant is derived from WAY-125 or WAY-136 by
the searched fingerprint links at this base. A precise search `rg -n '^\s*# invariant:' task-cycle`
returned none; the same expression against `gate/test_skills_reach_the_way_sessions.py` returned
the real `skill-entry-points/1` citation at line 212 as a positive control. The ordinary
`task-cycle` tests are not reported as invariant tests merely because the record template mentions
the word `invariant`.

## Approaches and costs

1. **Selected: descriptive contract in existing files.** Hand off full files, return status/paths,
   keep complete reports, read relevant evidence before decisions. Lowest additional maintenance;
   reuses Superpowers' existing file-based behavior. Cost if wrong: a short return can conceal
   evidence unless report completeness and source reading are enforced by the orchestrator and
   reviewer. No automatic proof or fixed saving is claimed.
2. **Rejected: separate universal templates plus validator.** Could detect omitted structural
   fields, but would add code and duplicate stage-specific borrowed report contracts. It still
   could not show whether the contents justify a decision. No evidence establishes a need for it.

Leaving current instructions unchanged avoids editing costs but fails the accepted direction:
the full messages may continue accumulating, replaceable details may gain invariants, and
assessment corrections may repeat return-step deliberate breaks.

## Questions and provisional rulings

| ID | Material/question | Orchestrator answer | Evidence and rejected way | Cost if wrong / used by |
|---|---|---|---|---|
| D1 | Architectural path and reflected task intent | Confirmed provisionally, not human approval | Frozen four settlements and adapter step 6; bounded/no-spec path rejected because interface/order choices remain | Design may be heavier than a bounded edit; spec enables independent source review |
| D2 | Existing-file contract or new validator/templates? | First option approved provisionally | Full inputs/reports in files; short return must include status, paths, commits/check result and all unresolved concerns affecting next dispatch | Manual completeness remains; spec §1 |
| D3 | Return-step invariant criterion | Approved; no compulsory catalogue of every function | Accepted settlement 2, WAY-12 preserved; broad freezing of details rejected | Wrong classification could miss a product rule; diff/log candidates require source-backed explanation; spec §2 |
| D4 | Assess before breaking only return-step checks | Approved; settle remarks, rerun changed checks, break final check; no second assessment | Accepted settlement 3, WAY-10/08/69; shifting earlier breaks rejected | Superseded evidence could be reused unless ranges/final checks are explicit; spec §3 |
| D5 | Recommend independent slices while SDD stays sequential | Approved provisionally | Accepted settlement 4, WAY-136, installed SDD restriction; suppressing recommendation or silently parallelizing rejected | Recommendation alone does not produce parallel speedup; execution ruling explains restriction; spec §4 |
| D6 | Authority for revising WAY-11/136 | Root confirmed accepted rows authorize direction; keep pre-main versions and show meanings in PR | WAY-134 narrows WAY-114; accepted task quotes current decision and changed meanings; README requires renewed acceptance | An additional meaning or collision is not approved; stop through blocked draft if found; spec decision-revisions section |

Approval messages were sent to the orchestrator, never the human. The first approval allowed the
contract design; the second expressly approved the three remaining sections and writing the full
spec. Neither is recorded as human acceptance of a foundation entry. The orchestrator requested
that the designer finalize without adding research beyond the four settlements; no new question
was introduced afterwards.

## Proposed implementation surface and entry allocation

- `task-cycle/skill/SKILL.md`: file handoff/short-return contract, source reading on decisions,
  return-step criterion and order, execution ruling that preserves the adopted skill restriction.
- `task-cycle/plan/SKILL.md`: independent cut recommendation plus one concise `Independence and
  execution` section, retaining current slice fields and dependency order.
- `task-cycle/record_template.md`: extend existing places for evidence/paths, return classifications
  and execution ruling instead of a new parallel ledger.
- Foundation: new decision for settlement 1, edit WAY-11 for settlement 2, new decision for
  settlement 3, edit WAY-136 for settlement 4; entry writers assign final wording/numbers using
  their skills. Recheck dependent entries, especially WAY-126 and `return-step-record/1`.

No scheduler, new parser, compaction controller, new telemetry, project-plan change, external
action or edit to another product is proposed. The spec's allocation avoids a duplicate decision
answering WAY-11 or WAY-136. It does not predetermine that no derived invariant is needed: writers
must preserve WAY-12 and WAY-22 and arrange separate authors if a new checkable invariant follows.

## Self-review and verification

Self-reviewed the spec for task coverage, all four settlements, explicit earlier-check preservation,
independent-assessor input restrictions, no executable parallel override, source fidelity, scope and
ambiguity. The short coordination contract keeps the duties to inspect diffs and run checks; it
does not authorize the orchestrator to ignore required evidence. The new plan section does not
change the headings/fields `slice_size.py` parses; this is based on its parser, not a guessed
compatibility claim. No changes to that parser are proposed.

Checked the written spec for `TODO`, `TBD` and `PLACEHOLDER`: none. Checked control characters
other than tab/CR/LF: zero. `git status --short` remained empty because the only new files are
ignored cycle artifacts; this is not proof that the artifacts do not exist. No product tests were
run by the designer because this stage wrote no product source. Root reported baseline results
of 41 task-cycle tests and 98 gate tests passing; this report attributes them to root and does not
claim an independent rerun.

Two exploratory checks were corrected before drawing a conclusion: a positive-control command
initially named a nonexistent gate test file, and a NUL-containing ripgrep expression was rejected
without text mode. The precise real-file positive control and direct character scan above supply
the final evidence. A broad `gate` citation search was too large and is not used to count tests.

The spec supplies concrete review cases and the existing part/critical-flow test commands. Final
foundation guards, semantic source comparison, independent assessment and code review remain for
their respective stages. The guards are partial checks; no full-gate pass or realized performance
improvement is claimed here.

## Handoff

Independent review: [spec-review.md](spec-review.md). Its single finding S1 identified that the
numbered sequence explicitly reran code review only for a code-changing settlement. The current
process also requires it when assessed foundation entries or invariant tests change. This was an
unintended loss of an existing obligation, not another design choice.

Applied S1 to spec §3, items 3–4: the trigger now explicitly includes code, assessed foundation
entries and invariant tests; the reviewer reviews the final return-step check before writing and
running its break, using the affected review already required rather than adding a duplicate
whole-change review. Leaving the original wording risked accepting a changed check without its
review; the correction preserves the existing affected review and keeps the first acceptance break
after assessment. No task meaning, foundation rule or other spec section changed.

Requested one scoped confirmation of the corrected sequence from the same independent reviewer.
The orchestrator triggered that follow-up and explicitly released the designer from waiting for
another turn; it retains the scoped result in the cycle. The written-spec provisional go-ahead
remains a separate recorded gate from approval to write it. The designer stops before planning,
implementation or foundation writes.
