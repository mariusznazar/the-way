# Whole-change code review — shorten the task cycle

Code-review verdict: **PASS — no Critical, Important or Minor finding.**

Reviewed range: `d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b..19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f`.
Worktree: `C:/Storage/repos/the-way-wt/shorten-task-cycle`.
This is the one independent whole-change code review of the one-slice task, using
Superpowers 6.4.1 requesting-code-review and its code-reviewer template. This review is
not the independent foundation assessment or human acceptance.

## Strengths

- The three instruction/template files express one transfer contract. Full material stays in
  files, the short return exposes failed and unchecked work, and a ruling requires the source
  and relevant report evidence. Missing material stops dependent work rather than becoming an
  assumed pass: task-cycle/skill/SKILL.md:97, :107, :115 and :121.
- The return-step criterion narrows only newly discovered uncovered behavior. Required
  decision-derived invariants, existing invariants, accepted settlements and projected entries
  stay required: foundations/decisions.md:343 and task-cycle/skill/SKILL.md:253.
- The final-check review, deliberate break, real failure, restoration and later invalidation
  duties remain explicit after moving only return-step checks' first acceptance breaks:
  foundations/decisions.md:4600 and task-cycle/skill/SKILL.md:269.
- Useful independent slices are recommended separately from execution permission. Shared state,
  dependencies and independent review matter, and the adopted skill's sequential restriction is
  preserved: task-cycle/plan/SKILL.md:99 and task-cycle/skill/SKILL.md:171.

## Issues

### Critical — must fix

None.

### Important — should fix

None.

### Minor — nice to have

None. No new review thread or addition to an existing thread is requested. There is consequently
no finding needing a copyable comment and expanded failure explanation.

## Scope, sources and method

Read the frozen task, corrected spec and finalized plan in
`.runs/task-cycles/shorten-task-cycle/`, the foundation/executor reports, the repository's
integration guide, the review playbook and its document-review reference, and the installed
requesting-code-review skill/template. Inspected both commits and the complete five-file diff.

The documentation pass read all three affected instruction/template files in full. For the
collective foundation files, the review unit was the complete affected entry and applicable
entries/dependencies, as clarified by the requesting orchestrator. Read the changed WAY-11,
WAY-136, WAY-148, WAY-149 and renewed WAY-126/return-step-record entries, the governing
foundation entries and glossary, and compared accepted task meanings with actual resulting text.
No conclusion relies only on an author's report.

The separate technical pass inspected the existing slice parser and tests, fingerprint function,
the guards' fingerprint/none-mode behavior, actual recorded guard/test evidence and affected
references. It did not dispatch another reviewer or repeat the documentation pass as another
review round. No unchanged test suite was rerun merely to repeat its prior result.

## Documentation/source-fidelity pass

All four accepted task settlements are represented, with no extra product rule imported from
the task's game example:

| Settlement | Actual foundation and instruction result |
|---|---|
| 1 — shorter orchestrator context and file transfer | WAY-148 at foundations/decisions.md:4560; dispatch/report/return/ruling rules at task-cycle/skill/SKILL.md:97; record paths and short results at task-cycle/record_template.md:39; planner return at task-cycle/plan/SKILL.md:139. |
| 2 — product requirements and settlements determine new invariants | Revised WAY-11 at foundations/decisions.md:343; actual candidate classification and safeguards at task-cycle/skill/SKILL.md:253; evidence field at task-cycle/record_template.md:89. |
| 3 — assessment before first breaks only for return-step checks | WAY-149 at foundations/decisions.md:4600; earlier points at task-cycle/skill/SKILL.md:245; assessment, settlements, affected review and final-check break at :273 and :283; evidence at task-cycle/record_template.md:100. |
| 4 — recommend independent slices despite method restrictions | Revised WAY-136 at foundations/decisions.md:4058; plan section and rules at task-cycle/plan/SKILL.md:75 and :112; orchestrator ruling at task-cycle/skill/SKILL.md:171; record at task-cycle/record_template.md:26. |

WAY-11 and WAY-136 retain pre-main /1 versions and request-link approval placeholders, with
the intentional meaning revisions retained for renewed human acceptance. WAY-126 and
return-step-record still serve their existing duties under the narrowed criterion. The
instructions preserve whole-source reading requirements, existing dispatch boundaries, the
separation between a provisional orchestrator go-ahead and human approval, and the current
cycle's base process. No new scheduler, universal report parser, context-compaction mechanism,
parallel executor or performance guarantee enters the change.

Readability is adequate for agents using the existing task-cycle vocabulary. The report examples
are concrete, the stage ordering is explicit, and the plan recommendation is not presented as
permission. No readability observation rises to a correctness or maintainability finding.

## Nine spec cases

| Case | Result | Checked implementation and consequence |
|---|---|---|
| 1. Normal stage completion | Meets | task-cycle/skill/SKILL.md:97–128 requires full files, status/paths/commits/check result, event recording before dependent dispatch and resumption from files. The record's Events section at task-cycle/record_template.md:39 holds the paths and result. Prior conversation is not a required input. |
| 2. Failed/unchecked result or unresolved decision | Meets | task-cycle/skill/SKILL.md:115 explicitly includes failed or unchecked work and every unresolved question/concern affecting dispatch. Lines 121–128 require evidence before a ruling and repair missing/incomplete reports or stale paths/ranges. A concise success message cannot replace a missing check or conceal its result. |
| 3. Costly decision-derived invariant | Meets | task-cycle/skill/SKILL.md:261 preserves WAY-12/WAY-22 duties without a cost exception. Revised WAY-11's verification explicitly treats omission of a costly required invariant as a violation, at foundations/decisions.md:369. |
| 4. Replaceable implementation detail | Meets | task-cycle/skill/SKILL.md:255–260 classifies actual diff/log candidates, retaining a replaceable detail in ordinary tests and the change description with its reason and paths. It does not require an inventory of every function or unchanged behavior. |
| 5. Assessment changes a return-step check | Meets | task-cycle/skill/SKILL.md:270 runs the check on the product; :273–281 assesses once, settles remarks and reruns affected checks/review for changes to code, assessed entries or invariant tests. Lines 283–290 require review of the final check before a break from its final sentence, a real failure, restoration and repeated affected evidence after later changes. This includes the spec's S1 correction. |
| 6. An earlier invariant check | Meets | task-cycle/skill/SKILL.md:245–248 and :291 retain its existing break/acceptance point. The return-step exception does not move earlier checks. |
| 7. Independent slices but execution skill forbids parallel executors | Meets | task-cycle/plan/SKILL.md:112–119 still identifies useful opportunities and states the adopted restriction. task-cycle/skill/SKILL.md:171–177 records sequential execution beside the opportunity. |
| 8. Shared file, dependency or mutable state prevents independent work | Meets | task-cycle/skill/SKILL.md:172 requires the actual dependencies, shared files/state and separately judgeable review ranges; :174 rejects different files alone as proof. Existing no-concurrent-writers and same-file-dependency rules remain at :80 and task-cycle/plan/SKILL.md:110. |
| 9. A single slice covers the task | Meets | task-cycle/skill/SKILL.md:234 makes that slice's review the whole-change review; :177 and task-cycle/plan/SKILL.md:116 explicitly identify no parallel slice work. No artificial second slice or duplicate unchanged-range review is required. |

Separate authors remain at task-cycle/skill/SKILL.md:216–220 and :269. The independent assessor
still gets only permitted diff/commit files, explicitly excluding the operational handoff and
author material at :273–277. Settlement stays inside its single assessment. Reconciliation
invalidation remains at :299–304. No assessment is substituted for code review.

## Technical pass and empirical checks

A read-only inline Python probe ran with `python -B -`, importing the existing
`relation-model/fingerprint.py` and `task-cycle/slice_size.py`. Assertions completed and the
probe printed its success summaries. It made no files, index or branch changes.

### Fingerprints, dependent entries and invariants

Computed from the actual final binding text:

| Entry | Fingerprint |
|---|---|
| WAY-11 | e882a9df |
| WAY-136 | e9ca5dac |
| WAY-148 | 2a5f9057 |
| WAY-149 | 6c02ef48 |

All 12 relation targets retained or introduced by WAY-11, WAY-136, WAY-148, WAY-149 and WAY-126
match their actual current binding text. A scan of all foundation Markdown files found exactly
the two affected fingerprint-bearing dependants, both checked as actual entries:

- foundations/decisions.md:3661 — WAY-126 carries WAY-11@e882a9df.
- foundations/invariants.md:222 — return-step-record carries WAY-11@e882a9df.

WAY-136/148/149 have no fingerprint-bearing dependants there. Direct byte comparison confirms
that WAY-10, WAY-12, WAY-69 and WAY-125 are unchanged entries. The entire invariant file equals
its base blob after replacing only the old WAY-11 fingerprint; sentence, version and Method
remain unchanged. The reviewed five-file list contains no new or changed invariant test, so no
WAY-69 deliberate-break exercise is created for this review.

The no-additional-invariant resolution does not waive a derivable invariant merely because its
Method would be TODO. The new rules concern adopting cycles' semantic choices and run evidence;
a phrase/heading assertion in this repository would establish another structural constraint,
rather than these rules' compliance. The existing return-step-record obligation remains. I
found no omitted additional commit property demanded by these concrete changed entries.

The guards' actual code confirms that `--merge-onto none` skips fingerprint-value comparisons
instead of checking them: elements/decisions/format_guard.py:927 and
elements/invariants/format_guard.py:1473. The direct comparison above supplies the narrower
actual-value evidence; it does not claim to have performed a merge comparison.

### Parser and discovery compatibility

The probe parsed the actual final plan, the revised planner's Markdown template and a small
two-slice example followed by the new second-level section. Both slice fields/path sets remain
intact; section content does not become a slice's Change field. Inspection of
task-cycle/slice_size.py:106 confirms that a second-level heading resets the current slice and
field target. The actual plan still has one slice and three explicit change paths.

The actual plan measures 160619 characters, 64248 estimated tokens and `fits`. This is a rough
read-set estimate, not a measured inference-cost result. Both affected skills' frontmatter is
byte-identical to base, so no name/description/location change requires regenerated entry points.

All five worktree files equal the reviewed head's git blobs. `git diff --check d04c3fe 19c9cfe`
reported no whitespace errors. The tracked working tree remained clean.

### Existing execution evidence, warnings and unchecked results

Read the existing foundation command evidence and machine-readable records, and the executor's
complete focused-check report. These are existing partial checks, not a pass of the full gate:

| Recorded check | Existing result |
|---|---|
| Decision-element tests | 169 tests, exit 0. Machine-readable record has 17 pass verdicts for cited invariants and no failed verdict. |
| Invariant-element tests | 233 tests, exit 0. Machine-readable record has 63 pass verdicts and no failed verdict. |
| Gate/critical-flow tests | 98 tests, exit 0; also run after the instruction edit. Foundation-stage record has 59 pass verdicts and no failed verdict. |
| Task-cycle part tests | Executor records final run of 41 tests, exit 0. |
| Final instruction size check | Executor and this review's direct measure agree: one slice, three files, 160619 characters / 64248 estimated tokens, fits. |
| Decision guard in pre-main none mode | 0 errors, 9 warnings, 5 grouped unchecked messages. Its JSONL contains 6 unchecked invariant verdicts because one group covers two invariants. |
| Invariant guard in pre-main none mode | 0 errors, 0 warnings, 3 grouped unchecked messages. Its JSONL contains 9 unchecked invariant verdicts because the base-comparison group covers seven invariants. |

The nine warnings are five existing overdue-review warnings (WAY-03, WAY-21, WAY-52, WAY-55,
WAY-69, check-by 2026-10-02) and the four expected request-link placeholders (WAY-11, WAY-136,
WAY-148, WAY-149). None is a new undisclosed defect in the reviewed implementation.

None-mode work remains unchecked: original-log lines/version additions, template-triggered
decision version additions, merge TODO/approval checks, merge copies, invariant base
identifiers/versions/corrections/violated-list comparison and merge fingerprint-value comparisons.
The direct final-text fingerprint comparison above is additional evidence with its own scope.
The absence of human_verdicts.md supplies no human verdict. Existing return-step-record/1 and
related run-evidence Method TODO debt remains unimplemented and has no runnable pass.

The executor's two faulty auxiliary newline assumptions remain disclosed in its report; its
final byte-based verification succeeded without a product change to repair those probes. No
product check failure is hidden by the review. This review did not rerun the unchanged suites.

## Recommendations

No corrective product edit is requested. Continue the already required independent foundation
assessment, return step, integration-tip reconciliation/search, request-link replacement and
human review. Retain the old/new WAY-11 and WAY-136 binding text with their Polish meaning
sentences for renewed acceptance. Do not start another broad review of this unchanged range;
if a correction is needed later, scope verification to original findings and new breakage in it.

## Declined to judge

- Measured time/token or financial savings: the task expressly claims no benchmark outcome,
  and future adopting-cycle measurements are outside this implementation review.
- Implementing a parallel executor or adopting another Superpowers version: the accepted
  design retains sequential execution under 6.4.1; this change records opportunities only.
- Implementing the missing full gate and existing Method TODO run-evidence checks: they are
  existing, disclosed debt and no new implementation is part of this task.
- Completeness of later assessment, return, current-target-tip reconciliation/search, request
  creation and human renewed acceptance: these stages had not been completed at the reviewed
  head and remain orchestrator-owned; this review does not certify them as performed.

No other considered behavior was excluded on the ground that the spec was silent.

## Assessment

**Ready to proceed? Yes. No code-review fix is required.**

**Ready to merge? Not yet as an overall cycle state:** the remaining required assessment,
return/reconciliation and human acceptance still have to occur. The reviewed implementation
itself meets the task/spec/plan and has no blocking or optional finding from this whole-change
review. Source comparison, nine semantic cases, actual parser/fingerprint checks and existing
partial test evidence support that verdict; none proves future agent behavior or a cost saving.

Only this report was written by the reviewer. No product edit, index/HEAD/branch mutation,
subagent, fix, push, cleanup or next-stage dispatch was performed.
