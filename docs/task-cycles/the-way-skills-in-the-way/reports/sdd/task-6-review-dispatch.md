You are reviewing one task's implementation: first whether it matches its requirements, then whether it is well-built.
This is a task-scoped gate, not a merge review.

## What Was Requested

Read the task brief: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-6-brief.md`. Global constraints:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`. Also binding: spec §4.6 in
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md`; `installation/install.py` is
the trust boundary of the `installation` part (`foundations/part_map.md`), and the cycle requires adversarial input checks
for a trust boundary (WAY-48) — the brief states why a literal-only change needs none new and names the existing
adversarial tests; judge that position against the diff. The invariant-like promise `installation-command` in the part
map (preview and confirmation kept, no existing file replaced) must still hold.

## What the Implementer Claims They Built

`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-6-report.md`

## Diff Under Review

**Base:** 863d458  **Head:** bb9f8ad
**Diff file:** `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\review-863d458..bb9f8ad.diff`

Read it once; do not re-run git commands; inspect outside the diff only for a named risk (one focused check each).
Read-only.

## You Do Not Dispatch Subagents

## Do Not Trust the Report

## Tests

Do not re-run the suites; a focused check only for a specific doubt.

## Part 1: Spec Compliance — Missing / Extra / Misunderstood; ⚠️ for what the diff cannot show.
## Part 2: Quality — the new wrapper sentence reads correctly with the sentences around it in `skill_wrapper` and with
the paragraphs Task 4 wrote (e.g. `elements/decisions/skill/SKILL.md` lines 13–18); the test asserts the right things.

## Output Format

### Spec Compliance
### Strengths
### Issues — Critical / Important / Minor, each with file:line
### Assessment — **Task quality:** Approved | Needs fixes; **Reasoning:** 1–2 sentences

Begin directly with the spec-compliance verdict. Return the review as your final message.
