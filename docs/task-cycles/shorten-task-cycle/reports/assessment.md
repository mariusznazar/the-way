# Independent assessment — shorten-task-cycle

Assessed range: d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b..19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f.

Assessed files:
- foundations/decisions.md
- foundations/invariants.md
- task-cycle/skill/SKILL.md
- task-cycle/plan/SKILL.md
- task-cycle/record_template.md

This is the one WAY-10 assessment, not approval. The orchestrator settles these observations. HEAD matched the assessed head and the tracked working tree was clean when inspected. No assessed file, index, branch or HEAD was changed. The only write is this report.

## Result and observation to settle

No material correctness concern found in the assessed change. One optional reduction:

### A1 — Low: cut the repeated fixed-version execution answer from the record placeholder

Anchor: task-cycle/record_template.md:26, especially line 28.

The new field already asks for the plan recommendation, orchestrator ruling, dependencies, mutable state, separate review and skill restrictions. Its final clause additionally supplies the answer: “with Superpowers 6.4.1 subagent-driven-development, sequential execution despite any opportunity”. That restriction is already executable guidance at task-cycle/skill/SKILL.md:174 and task-cycle/plan/SKILL.md:115, and is verified directly against the installed method at subagent-driven-development/SKILL.md:282.

What can be cut: the final fixed-version clause of this placeholder, retaining the requirement to record the actual restriction and ruling. The field could end after “separate review and skill restrictions>”.

Keeping it costs very little today and helps a reader filling the template without revisiting the skill; it also maintains a third copy of the version-specific answer and encourages copying boilerplate. Cutting it reduces that duplication without changing the mandatory sequential execution in either skill; the cost is that the template reader must obtain the actual restriction from the prescribed execution skill. This is optional wording economy, not a reason to delay the change.

No substantive safeguard or whole feature should be cut on the evidence available. In particular, retaining evidence reads for rulings, the assessor input filter, mandatory whole-source reads, decision-derived invariants, and the final deliberate break is necessary to preserve the surrounding rules.

## Purpose, operating cost and excessive scope

1. **File handoffs — no concern found.** WAY-148 (foundations/decisions.md:4560) acts at each dispatch and return, benefiting the orchestrator's subsequent context and a resumed session. The implementation at task-cycle/skill/SKILL.md:97 distinguishes routine progression from decisions needing report evidence. It retains failures, unchecked work and unresolved concerns in the short return, requires incomplete reports to be repaired, and preserves borrowed review packages. It does not authorize replacing mandatory reads with summaries. Leaving the old rule alone still preserves reports but does not require short routing messages throughout the cycle; applying this rule adds file I/O and reporting discipline while reducing repeated conversational payload. Its actual net token or time saving is unmeasured. The cheaper existing mechanism is the borrowed method's own brief/report, which the change explicitly reuses rather than duplicating.

2. **Invariant classification — no concern found.** WAY-11 (foundations/decisions.md:344) and task-cycle/skill/SKILL.md:253 ask whether a later change would violate a requirement or settled product rule. This serves future maintainers at the return step: replaceable details need not become permanent foundation rules. Overbroad application could excuse a required invariant; the text explicitly preserves WAY-12/WAY-22, accepted settlements, projected entries and existing invariants. The record asks for actual candidates and their evidence, not an inventory of functions. Leaving the former broad wording preserves ambiguity over replaceable details; the change adds a small classification cost while avoiding permanent entries and their independent authorship/review costs. Ordinary tests here cover replaceable implementation details, not decision verification: WAY-12 still governs the latter. No contradiction found with the whole WAY-12, WAY-22, WAY-126 or WAY-134 entries.

3. **Independent slicing and execution — no concern found beyond A1.** WAY-136 (foundations/decisions.md:4058), the planner section at task-cycle/plan/SKILL.md:112 and the orchestrator ruling at task-cycle/skill/SKILL.md:171 distinguish useful work division from permission to execute concurrently. The installed Superpowers 6.4.1 method explicitly forbids parallel implementation agents. The new instructions preserve that restriction and the existing ban on concurrent writers in one worktree. The cost is a short extra plan section and ruling even when execution must be sequential; its value is explicit separability and review boundaries, not immediate parallel speedup. Keeping only dependencies would be cheaper but would not explicitly expose the recommendation or distinguish it from the method's restriction. One-slice and inseparable work receive explicit limits, preventing a requirement to manufacture slices. The parser at task-cycle/slice_size.py:106 ends a slice at another heading, so the new second-level section is compatible with its existing parsing.

4. **Return-step deliberate break — no concern found.** WAY-149 (foundations/decisions.md:4600) and task-cycle/skill/SKILL.md:270 move only the first acceptance break of a newly added return-step check after assessment settlement. Product execution remains before assessment; the final check still receives review by a reviewer who did not write it, and its break is derived from the final invariant sentence. The change preserves three authors, earlier checks' acceptance points, the single assessment, reruns after relevant changes, restoration and clean verification. Leaving the former ordering can repeat a break when settlement changes the check; the proposed order avoids that avoidable first run but still costs the final review and actual failing break. Reusing an affected review is the cheapest compatible route and is explicit. A passing product check or finished assessment cannot substitute for the break.

## Source consistency and complete-entry checks

Read the actual diff and the complete final task-cycle skill, planning skill and record template. In the collecting foundation files, read the complete affected entries WAY-11, WAY-126, WAY-136, WAY-148, WAY-149 and return-step-record; also read applicable complete entries WAY-01, WAY-03, WAY-04, WAY-08, WAY-10, WAY-12, WAY-13, WAY-22, WAY-36, WAY-65, WAY-69, WAY-114, WAY-125 and WAY-134, and the applicable invariant/method/assessment entries and glossary definitions.

- No mismatch found between the changed decisions and their operational instructions or record fields.
- WAY-11's two dependent references found by the foundation/source search use the new fingerprint e882a9df: WAY-126 and return-step-record. The latter's binding sentence is unchanged, appropriately: it requires a committed return-step record, while classification remains an agent comparison.
- WAY-148 expressly protects the independent assessor's filtered inputs; the skill and record repeat that boundary. No operational handoff or author report was read in this assessment.
- The installed Superpowers method supplies file briefs/reports and expressly forbids parallel implementers. The change's claims on these points match that source.
- The new decisions retain decision form, scope, relations, verification examples and pending merge approval. No human approval is inferred from their placeholder.
- Fidelity to the task's human settlements is not checked: the task, spec and plan are excluded assessor inputs. This report does not certify that those private sources authorize every meaning change.

## History and frequency limits

Inspected git history using hash/date-only log output and source diffs with commit messages suppressed. The return-step decision wording is present from 046eb2a (2026-09-27); the operational handoff rule was added in 2f8450b (2026-10-05); the explicit return-step check review/break before assessment was added in 6c31b31 (2026-10-06); the plan skill was added in b2e289f (2026-10-10). The assessed changes to these rules are therefore changes to existing, in several cases recent, mechanisms. Their history alone does not establish that the problem recurred after adoption.

Runtime frequency cannot be measured under this assessment's input filter. Session transcripts, cycle reports and chronological records were explicitly excluded, so none were searched or read. Number of runtime cases examined: zero; recurrence and savings are unknown, not zero. Installed method text contains behavioral claims, but these are source statements, not measured cases from this assessment. No new monitoring layer is proposed merely to fill that evidence gap.

## Verification limits

This was a read-only source assessment. No runtime test, format guard or full gate was run, and no test pass is claimed. Existing output reports were not read. Source consistency and the parser observation above are inspection findings; the orchestrator retains responsibility for the applicable checks and for settling A1.
