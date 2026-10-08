You are reviewing one task's implementation: first whether it matches its requirements, then whether it is well-built.
This is a task-scoped gate, not a merge review — a broad whole-branch review happens separately after all tasks are
complete.

## What Was Requested

Read the task brief: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-3-brief.md`

Global constraints from the spec/design that bind this task (verbatim from the plan; file):
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`. Also binding: spec §4.1 (discovery
and generator) and §4.2 (the entry point text, character for character) in
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md`; the plan's "Review Focus"
items 1–5 are repeated in the brief's tests. Invariants `script-language`, `script-imports`, `script-subprocesses`:
Python 3.14 standard library only, `git` the only subprocess.

## What the Implementer Claims They Built

Read the implementer's report: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-3-report.md`

## Diff Under Review

**Base:** a7f42aa  **Head:** c12d4dd
**Diff file:** `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\review-a7f42aa..c12d4dd.diff`

Read the diff file once — it is your view of the change. Do not Read a changed file separately unless a hunk you must
judge is cut off, and say so. Do not re-run git commands. Do not crawl the broader codebase; inspect code outside the diff
only to evaluate a concrete risk you name — one focused check per named risk. Your review is read-only on this checkout.
Do not open `gate/test_skills_reach_the_way_sessions.py` (another author's check of this code; WAY-69).

## Deliberate break (WAY-69, WAY-08) — the one exception to read-only

After the review proper, do the brief's step 6 yourself: you wrote neither the check nor the sentence. Read only the
sentence of `skill-entry-points/1` in `foundations/invariants.md` (not the check's code), write at least four different
breaks of that sentence in the worktree, one at a time (for example: delete one `.agents/skills/the-way-*/SKILL.md`;
change one byte of one `.claude` copy; remove one sibling name from one entry point's prefix sentence; add a directory
`.claude/skills/the-way-nothing/` with a file in it; change one description's start), and after each run
`python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl` and read `.runs/gate-tests.jsonl`. For each break
report whether `test_every_skill_reaches_a_session_on_the_way` failed and `skill-entry-points/1` was recorded `fail`.
Restore after each: `git restore --source=HEAD --staged --worktree -- .claude/skills .agents/skills`, remove any directory
you added (list with `git clean -n -d -- .claude/skills .agents/skills`, delete exactly those by path). End with
`git status --short` empty and one clean gate run. A break the check does not catch is a finding against the check, for
the controller (the check is read-only here).

Also judge, as part of the entry-point text, this point the facts agent raised: the Claude Code page says "When you move
the session with /cd on v2.1.246 or later, Claude Code adds the new directory’s project skills." Does the entry point's
rule (root = the directory the session was started in) still give the right root after such a move? Report a finding only
if it does not.

## You Do Not Dispatch Subagents

Do all of this review yourself.

## Do Not Trust the Report

Treat the report as unverified claims; verify against the diff. A stated rationale never downgrades a finding.

## Tests

The implementer ran the tests (12 in `agent-instructions`, 98 in `gate`, 16 in `installation`, the part-map guard). Do not re-run the suite; run a focused
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
