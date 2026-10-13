# Plan — shorten the task cycle

- Task: `.runs/task-cycles/shorten-task-cycle/task.md`
- Spec: `.runs/task-cycles/shorten-task-cycle/spec.md`
- Base: `d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b`

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| F1 — new decision on the cycle's handoff/report contract; the entry writer assigns its identifier | decision | Accepted settlement row 1; spec section 1 and Foundation and affected files | Slice 1: dispatch, report, coordination and resumption instructions and record fields |
| F2 — edit WAY-11/1 in place, including its verification examples | decision | Accepted settlement row 2; spec section 2 | F5 and F6; Slice 1: return-step classification and evidence |
| F3 — new decision on acceptance order for checks added in the return step; the entry writer assigns its identifier | decision | Accepted settlement row 3; corrected spec section 3 | Slice 1: assessment, settlement, final review and deliberate-break order |
| F4 — edit WAY-136/1 in place | decision | Accepted settlement row 4; spec section 4 | Slice 1: planning recommendation and the orchestrator's execution ruling |
| F5 — recheck WAY-126/1 against the changed WAY-11 and renew its relation fingerprint | decision dependency renewal | Spec Foundation and affected files; WAY-31 | Slice 1: projected-entry obligations remain in force |
| F6 — recheck return-step-record/1 against WAY-11 and renew its Derives from fingerprint; retain its sentence and version if only the link changes | invariant dependency renewal; existing Method remains TODO | Spec Foundation and affected files; WAY-31 | Slice 1: the existing return record remains required; this renewal creates no test |
| F7 — any further invariant actually derived from the concrete F1–F4 sentences under WAY-12 and WAY-22; finalize each identifier, Method and any check path before Slice 1 | completed derivation prerequisite; no new check | Spec Verification and limits; root's planning ruling recorded in reports/planner.md | Slice 1; no additional sentence/check author is needed; existing return-step-record Method TODO remains |

Write F1–F4 through this worktree's `the-way-record-decision`, and F6 and any F7 entry through
`the-way-record-invariant`. Their element skills' whole-file reading duties apply to the entry
writers; the targeted reads below do not override them. No project definition or assigned
projected entry applies to this independent task.

Before dependent implementation, complete the whole-foundation search, recheck every affected
linked entry, and resolve any further effects it finds. Known foundation write paths are
`foundations/decisions.md` and `foundations/invariants.md`. Do not change WAY-10, WAY-12, WAY-69 or
WAY-125, or create a new version of an existing pre-main entry, merely to implement this task.
The existing `task-cycle/**` part assignment covers the three changed instruction files; no
part-map entry is presently needed.

The foundation stage fixes F1/F3's final identifiers and makes the F7 finding explicit: either
list every resulting entry, method and check, or record why none can be derived. An unknown
method alone does not justify omitting a derivable invariant. Do not invent a prose-matching
test as proof that an agent follows instructions. If a resulting check needs writing, complete
that foundation work with the current cycle's authorship, review and acceptance rules before
Slice 1; this cycle does not adopt its proposed return-step order early.

Before Slice 1 dispatch, update this plan with those final identifiers, methods and check paths,
refresh all affected Read ranges against the finished foundation, add the new entries' exact
ranges, and rerun the size check. If a new entry requires a
design choice beyond the accepted rows and spec, return to the orchestrator rather than silently
expand the task. Keep the full old/new binding text and Polish meaning sentences of WAY-11 and
WAY-136 for renewed human acceptance at the request; a provisional ruling is not that acceptance.

Foundation verification uses the actual final entries and these existing commands:

- `python -B gate/run_tests.py elements/decisions`
- `python -B gate/run_tests.py elements/invariants`
- `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --record .runs/task-cycles/shorten-task-cycle/reports/foundation-decisions.jsonl`
- `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none --record .runs/task-cycles/shorten-task-cycle/reports/foundation-invariants.jsonl`

The pre-main none options leave merge comparisons, including fingerprint-value comparisons,
unchecked. Separately compute the changed decisions' fingerprints with the existing
`relation-model/fingerprint.py` from their exact final binding text and compare all affected
references, including F5/F6. Record that comparison rather than report the none-mode guards as
having checked it. Preserve every warning, failure and unchecked result, including any TODO
method. Search the whole foundation again against the current integration tip before integration
and retain both search records and the independent foundation assessment for the request.

Foundation resolution at `dba4cf81769446484d68b6260424260f7f1da85e`: F1 is WAY-148/1; F3 is WAY-149/1; F7 is complete with no new invariant, method or check. All decision Read ranges below were recomputed from the final foundation; the existing invariant sentence, version and Method remain unchanged.

## Slices

### Slice 1 — make the cycle and its record follow the four settlements

- **Goal:** Future cycles have one consistent file-based transfer contract, the accepted boundary for new return-step invariants, the corrected acceptance order for return-step checks, and an explicit distinction between independent-slice recommendations and execution restrictions.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/plan/SKILL.md` · `task-cycle/record_template.md`
- **Read:** `.runs/task-cycles/shorten-task-cycle/task.md` · `.runs/task-cycles/shorten-task-cycle/spec.md` ·
  `agent-instructions/README.md` · `foundations/glossary.md` ·
  `foundations/part_map.md:131-165` · `foundations/part_map.md:180-214` ·
  · ·
  · ·
  · ·
  · ·
  · ·
  `foundations/decisions.md:6-37` ·
  `foundations/decisions.md:176-202` ·
  `foundations/decisions.md:203-233` ·
  `foundations/decisions.md:305-342` ·
  `foundations/decisions.md:343-383` ·
  `foundations/decisions.md:384-413` ·
  `foundations/decisions.md:414-458` ·
  `foundations/decisions.md:459-479` ·
  `foundations/decisions.md:708-736` ·
  `foundations/decisions.md:857-887` ·
  `foundations/decisions.md:888-922` ·
  `foundations/decisions.md:923-948` ·
  `foundations/decisions.md:949-979` ·
  `foundations/decisions.md:1043-1069` ·
  `foundations/decisions.md:1259-1284` ·
  `foundations/decisions.md:1955-1990` ·
  `foundations/decisions.md:3598-3642` ·
  `foundations/decisions.md:3643-3689` ·
  `foundations/decisions.md:3962-4009` ·
  `foundations/decisions.md:4010-4057` ·
  `foundations/decisions.md:4058-4114` ·
  `foundations/decisions.md:4560-4599` ·
  `foundations/decisions.md:4600-4640` ·
  `foundations/invariants.md:206-255` · `task-cycle/slice_size.py` · `task-cycle/test_slice_size.py`
- **Checks:** Before editing, compare the current instructions and record with all nine cases in spec Verification and limits and record the unmet cases. After editing, repeat that semantic comparison, including the corrected assessment-settlement review trigger and review of the final check before its break. Run `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py gate`, and `python -B task-cycle/slice_size.py .runs/task-cycles/shorten-task-cycle/plan.md`. Confirm that the new second-level Independence and execution section leaves the existing slice/Change/Read parser syntax valid. Preserve stage report requirements, mandatory whole-source reads, WAY-10's filtered assessor inputs, earlier check acceptance points, review invalidation, separate authors, and one whole-change review for one slice. These are instruction changes assessed by source comparison and concrete cases, not a new executable agent-behavior claim.
- **Depends on:** F1 · F2 · F3 · F4 · F5 · F6 · F7 resolution and any resulting entries/checks

The executor extends existing record sections for transfer paths and short coordination results,
return classifications, assessment/break evidence and the execution ruling. Keep one record;
reuse the borrowed method's briefs/reports. The planner skill gains the specified independent-work
recommendation section without changing its parsed fields. The orchestrator skill explains when
to read report evidence, how to repair incomplete reports and how to record its execution ruling.
No new scheduler, validator, telemetry, additional compaction or script is part of this slice.
Keep skill names, paths and descriptions unchanged; if implementation actually needs a change
to one, report it and run the repository's entry-point regeneration and tests before dispatching
completion.

This is one slice: its independent review is the whole-change code review. It still receives the
current cycle's independent foundation assessment and return step. The semantic changes apply to
future adopters of the resulting commit; the current cycle continues under its base process.

## Independence and execution

There is no useful parallel slice work in this plan. The cycle instructions and record share
the handoff and return-step contract; the planner's recommendation and the orchestrator's ruling
share the plan/record interface. Splitting these three files would create dependent, partially
specified interfaces or repeated edits to the same cycle and record files. One reviewer can judge
their consistency together, and the combined read/change set fits one executor.

The foundation writers run before the instruction executor and use distinct authors where an
invariant needs them. No two writing agents edit this worktree concurrently. Adopted Superpowers
6.4.1 also forbids parallel implementation subagents; the orchestrator records that restriction
and the absence of useful independent slices. This planning-stage explanation does not adopt the
new instructions during the current run or create an extra slice to claim parallel work.

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome: a shorter-context, less repetitive cycle that preserves product requirements and review evidence | F1–F7 resolution; Slice 1; spec cases and current required checks, with no unmeasured saving claim |
| To do 1 and accepted settlement row 1: shorten the orchestrator's context and transfer work through files | F1; Slice 1 transfer, short-return, evidence-reading, repair and resumption contract; existing record sections |
| To do 2 and accepted settlement row 2: classify new return-step behaviors by whether later change violates a product requirement or settlement | F2, F5, F6; Slice 1 return instructions and classification evidence; F7 derivation cannot waive decision-required invariants |
| Preserve the answered adjacent-tile movement rule as a product invariant | Slice 1 preserves the requirement-based criterion; no change to the other product or import of its rule |
| To do 3 and accepted settlement row 3: independent assessment and settlements precede first acceptance breaks only for return-step checks | F3; Slice 1 corrected sequence, affected checks/review after settlements, final-check review and break evidence; earlier breaks keep their position |
| To do 4 and accepted settlement row 4: recommend useful independent slices and possible parallel work regardless of the adopted execution skill | F4; Slice 1 planner recommendation plus orchestrator ruling and record evidence; this plan's Independence and execution section |
| The orchestrator assesses dependencies, shared files/state, independent review and the chosen skill's restrictions | F4; Slice 1 execution ruling; one slice and sequential current execution |
| Carried question: how to limit context and transfer work through files | F1; Slice 1 follows spec section 1 without a new schema or runtime |
| Carried question: how to implement the recommendation despite the current skill's prohibition | F4; Slice 1 follows spec section 4, retains each slice's own executor/review and the final-review rule |
| Keep mandatory decision-derived invariants, accepted rows and projected-entry duties | F2, F5, F6, F7 resolution; Slice 1 safeguards and concrete cases |
| Preserve review obligations after assessment settlements, separate authors and real failure evidence | F3, F7 resolution; Slice 1; corrected S1 in spec sections 3 and Verification and limits |
| Pre-main route, linked and unlinked foundation effects, renewed acceptance and partial-check disclosure | F1–F7 resolution; foundation checks/searches; current cycle assessment and request, before integration |
| Out of scope: plan-project large-document reads and extra context compaction | Slice 1 stays in the three named task-cycle files and introduces neither change |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| One cohesive instruction/template slice after the foundation stage | Split by settlement or by file | A single reviewer must hold the combined contract; if it proves too large, discard and replan that slice. Splitting now adds reviews and either shared-file dependencies or incomplete interfaces without useful parallelism. |
| Reuse existing record sections and borrowed-method briefs/reports | Add a second ledger, generic report schema or validator | Manual semantic review can miss an omission; the concrete cases and report-repair rule remain necessary. Extra machinery adds maintenance without establishing completeness or agent compliance. |
| Freeze concrete derived-invariant IDs, methods and checks at the foundation boundary before dispatch, then refresh plan ranges/size | Invent speculative invariant sentences or tests before the entry writers choose concrete binding text | Dispatch must wait for that explicit resolution and the final size report. Premature tests could enforce wording rather than the accepted meaning or violate the separate-author rule. |
| Keep skill descriptions and entry-point locations unchanged | Change discovery text as part of instruction editing | If a description change proves necessary, the write scope and checks must expand to generated entry points. Keeping unrelated discovery text avoids that cost now. |
| Run existing tests and compare instructions against the nine spec cases | Add brittle tests that only search for required phrases | Semantic review cannot prove future agent behavior; phrase tests would add maintenance while claiming no stronger proof. Actual cycle cost measurement remains outside this task. |
