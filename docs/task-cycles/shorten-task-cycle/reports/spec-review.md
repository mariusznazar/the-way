# Independent spec review — shorten-task-cycle

Verdict: **changes requested before planning**. The design represents all four accepted
settlements and needs no additional human decision of meaning for its chosen approach. One local
correction is required to preserve the existing review obligation after assessment settlements.

## Reviewed material and boundary

- Worktree: `C:/Storage/repos/the-way-wt/shorten-task-cycle`.
- Repository HEAD: `d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b`.
- Spec: `.runs/task-cycles/shorten-task-cycle/spec.md`, read in full, SHA256
  `D3395531CE495BDA842DBEA02E9191F4C1FE41C4CFEAA97721AFB2596992C560`.
- Frozen task: `.runs/task-cycles/shorten-task-cycle/task.md`, read in full.
- Current process: `agent-instructions/README.md`, `task-cycle/skill/SKILL.md`,
  `task-cycle/plan/SKILL.md`, `task-cycle/record_template.md` and the relevant parser in
  `task-cycle/slice_size.py`.
- Foundation: the part map and glossary; relevant decisions WAY-01, WAY-03, WAY-07, WAY-08,
  WAY-10, WAY-11, WAY-12, WAY-13, WAY-14, WAY-22, WAY-25, WAY-30, WAY-31, WAY-33, WAY-36,
  WAY-69, WAY-114, WAY-120, WAY-125, WAY-126, WAY-134, WAY-135, WAY-136 and WAY-144;
  the existing assessment and return-step record invariants and decision-verification entries.
- Borrowed method: installed Superpowers 6.4.1 `subagent-driven-development/SKILL.md`, including
  its file briefs/reports, sequential-execution prohibition and task-review requirements.

This is the independent stage-7 spec review, not WAY-10's foundation assessment and not a code
review. No repository source, spec or foundation file was changed. No tests were run: this review
compares the proposed process and its sources; the implementation checks remain future work.

## Required correction

### 1. Preserve code review when assessment changes an invariant test or foundation entry

**Anchor:** `.runs/task-cycles/shorten-task-cycle/spec.md:106`.

**New thread — required before planning.**

**Text for the designer:** The proposed sequence only explicitly reruns code review when a
settlement changes code. Keep the current requirement to rerun the affected code review when a
settlement changes assessed foundation entries or invariant tests as well, and make clear that
the reviewer reviews the final return-step check before producing its acceptance break. Moving
the break after assessment does not authorize replacing that review with the break alone.

**Why this is a finding:** The task authorizes moving deliberate breaks of return-step checks,
while preserving earlier breaks; it does not authorize dropping another check
(`task.md:29`, `task.md:40`). The current process explicitly distinguishes a change of code from
a change of the assessed foundation entries or invariant tests and requires affected checks and
code review in both cases (`task-cycle/skill/SKILL.md:233`,
`task-cycle/skill/SKILL.md:235`). The spec's complete proposed sequence says:

> 3. Settle every remark. Rerun checks affected by the settlement and the code review where it changes
>    code. A settlement is part of the one assessment and does not request a second one (WAY-10).
> 4. Have the code reviewer, who did not write the check, write the deliberate break from the final
>    invariant sentence and run the final return-step check on it. Record the required failure under
>    WAY-08 and WAY-69 before accepting the check.

For example, the product code can remain at commit A while an assessment settlement changes an
invariant sentence and its check from version B to version C. Following this numbered sequence
literally allows running C and asking a reviewer only to write its deliberate break, with no
explicit review of the B-to-C changes. A break failing is necessary acceptance evidence, but is
not an independent review of the final check, its assumptions and its agreement with the final
sentence. The generic preservation statements at `spec.md:61` and `spec.md:121` leave the more
specific sequence ambiguous at the point an executor uses it.

**Suggested correction:** Replace item 3 with wording that retains the current trigger:

> Settle every remark. If a settlement changes code, assessed foundation entries or invariant
> tests, rerun the affected checks and the affected code review. A settlement is part of the one
> assessment and does not request a second one (WAY-10).

Make item 4 explicitly have that independent code reviewer review the final return-step check and
then write and run the deliberate break. This can use the affected review already required; it
does not require another whole-change review of an unchanged range.

**Cost of either path:** Leaving the sequence as written risks accepting a changed check without
its required final review. The correction adds only the existing affected review after an actual
change; it preserves the task's saving by performing the first acceptance break after settlement.
It requires no new foundation meaning or renewed human question.

## Coverage and source fidelity

| Accepted direction | Finding |
|---|---|
| 1 — shorten orchestrator context and transfer work through files | Covered by `spec.md:35` through `spec.md:73`. Full reports remain available, short returns expose failures and unresolved concerns, and evidence is read before rulings. Whole-source reading duties and WAY-10's filtered assessor inputs are preserved. No mandatory report parser, telemetry or custom compaction is introduced. |
| 2 — preserve product rules as invariants, keep replaceable details in ordinary tests | Covered by `spec.md:77` through `spec.md:96`. The later-task violation test matches the accepted answer. Existing decision-derived invariants, accepted rows and projected entries cannot be waived. The adjacent-tile example remains a rule of its own product, without introducing that game rule into the-way. |
| 3 — assessment before breaks only for return-step checks | Covered by `spec.md:100` through `spec.md:122`, subject to finding 1. The scope excludes earlier checks, keeps the three authors and reviewer-written break, and requires real failure evidence for the final check. One assessment and its settlements remain one assessment. |
| 4 — recommend independent slices regardless of the current tool restriction | Covered by `spec.md:126` through `spec.md:147`. Useful independent cuts and potential parallel work appear in the plan. The orchestrator considers files, dependencies, mutable state and review ranges. Current Superpowers 6.4.1 implementation stays sequential, with separate slice authors/reviews and the final review retained. |

The file contract, the extra plan section and reuse of existing record sections are implementation
choices within the accepted meanings. They do not require another settlement. The two proposed
new decisions record accepted rows 1 and 3; edits to WAY-11 and WAY-136 record accepted rows 2 and
4 without creating duplicate answers to their existing questions. Current pre-`main` versioning,
dependent fingerprint renewal, whole-foundation searches and renewed acceptance at the request
are explicitly retained (`spec.md:161`, `spec.md:179`). No additional collision requiring a human
choice was established in this review. The report does not itself authorize the final entry
wording; the entry writers must still search and check their concrete entries.

## Feasibility and cost

- The existing record already has events, artifacts, choices, verification, return and assessment
  sections. Extending them is sufficient for the proposed evidence; a second ledger is unnecessary.
- `slice_size.py:119` ends a slice at another heading. A separate second-level plan section does
  not alter `Change` or `Read` parsing. No parser change follows from the proposed section.
- Superpowers already transfers briefs and reports through files. Reusing those artifacts keeps
  the proposed contract feasible without changing its adopted version or adding an executor.
- The beneficiary is the orchestrator coordinating later stages, and the check authors/reviewers
  after a return-step assessment. The proposal acts at the places identified in the frozen task.
- The task provides two prior cycle cases for context cost and one return-step case for repeated
  breaks. This review did not independently remeasure the archived sessions. It makes no frequency,
  time-saving, token-saving or monetary-cost claim beyond the frozen task's stated evidence.
- Selective report reading can hide an omitted concern, and classification can mislabel a product
  rule as an implementation detail. The spec explicitly preserves complete reports, evidence
  review for decisions, failure visibility and decision-derived invariants. These controls address
  the task's risks without a new schema or proof of agent compliance.
- Keeping the current process costs no edit but leaves all four accepted changes undelivered.
  The proposed instruction/template edit is the cheaper supported route than a report validator
  or new runtime scheduler. Its remaining cost is manual semantic review, correctly acknowledged
  by the spec rather than presented as an automatic guarantee.

## Handoff

Resolve finding 1 in the spec before planning. The correction restores an existing obligation;
it does not require new human acceptance beyond the request/merge already required for the task's
four settlements. No other requirement gap, invented product behavior or execution blocker was
established. No further stage was invoked.

## Scoped confirmation of S1

Final verdict: **pass after correction**. S1 is resolved; no finding from this review remains open.

Reviewed only the correction in `spec.md:106` through `spec.md:113`, its surrounding acceptance
sequence, and the designer's S1 settlement in `reports/design.md`. Corrected spec SHA256:
`0A1B0C6B9E99D5F24A1F47890DDDE0CB10946CB6664E8FCC2F1BE933C5B7C9C1`.

- Item 3 now explicitly requires affected checks and affected code review when a settlement changes
  code, assessed foundation entries or invariant tests. The B-to-C scenario in finding 1 can no
  longer omit the affected review merely because the product code stays unchanged.
- Item 4 explicitly requires review of the final return-step check before the reviewer writes and
  runs its acceptance break. It reuses the affected review when that review covers the check;
  it does not introduce a duplicate whole-change review of an unchanged range.
- The single assessment, reviewer separation, actual failure evidence and unchanged position of
  earlier checks remain intact. The fix restores the existing obligation and adds no new decision
  of meaning for the human.

This was a scoped confirmation of the one finding, not a second general spec review. No tests,
source edits, foundation writes or later stages were performed.
