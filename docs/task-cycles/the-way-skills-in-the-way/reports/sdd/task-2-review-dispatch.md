You are reviewing one task's implementation: first whether it matches its requirements, then whether it is well-built.
This is a task-scoped gate, not a merge review — a broad whole-branch review happens separately after all tasks are
complete.

## What Was Requested

Read the task brief: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-2-brief.md`

Global constraints from the spec/design that bind this task (verbatim from the plan; file):
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`. Also binding: spec §4.1 (discovery
and generator) and §4.2 (the entry point text, character for character) in
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md`; the plan's "Review Focus"
items 1–5 are repeated in the brief's tests. Invariants `script-language`, `script-imports`, `script-subprocesses`:
Python 3.14 standard library only, `git` the only subprocess.

## What the Implementer Claims They Built

Read the implementer's report: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-2-report.md`

## Diff Under Review

**Base:** 47dcbe3  **Head:** a7f42aa
**Diff file:** `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\review-47dcbe3..a7f42aa.diff`

Read the diff file once — it is your view of the change. Do not Read a changed file separately unless a hunk you must
judge is cut off, and say so. Do not re-run git commands. Do not crawl the broader codebase; inspect code outside the diff
only to evaluate a concrete risk you name — one focused check per named risk. Your review is read-only on this checkout.
Do not open `gate/test_skills_reach_the_way_sessions.py` (another author's check of this code; WAY-69).

## You Do Not Dispatch Subagents

Do all of this review yourself.

## Do Not Trust the Report

Treat the report as unverified claims; verify against the diff. A stated rationale never downgrades a finding.

## Tests

The implementer ran the tests (11 in `agent-instructions`, 16 in `installation`). Do not re-run the suite; run a focused
test only for a specific doubt no run answers. Warnings or noise in reported output are findings. If the report's
evidence is missing or garbled, report that as a gap.

## Part 1: Spec Compliance

Missing / Extra / Misunderstood against the brief and spec §4.1–§4.2. Requirements you cannot verify from this diff:
report as ⚠️.

## Part 2: Code Quality

Separation of concerns, error handling, DRY, edge cases; tests verify real behaviour; file structure as the plan; one
responsibility per file. file:line evidence for every finding. Begin your final message directly with the spec-compliance
verdict; no preamble.

## Calibration

Critical / Important (this task cannot be trusted until fixed) / Minor. A plan-mandated defect is Important, labelled
plan-mandated. Acknowledge what was done well first.

## Output Format

### Spec Compliance
- ✅ Spec compliant | ❌ Issues found: […]
- ⚠️ Cannot verify from diff: […]
### Strengths
### Issues
#### Critical (Must Fix)
#### Important (Should Fix)
#### Minor (Nice to Have)
### Assessment
**Task quality:** Approved | Needs fixes
**Reasoning:** 1–2 sentences

Return the review as your final message (the harness may refuse report files from subagents).
