# Task 7 report

Status: done. File changed: `instruction-files/principles.md` only.

## Checks
- Decision citations `(WAY-1[23]x`: 13 lines (needs 12).
- Stale text grep (`for one occurrence`, `skill/`, `Read on 20`, `Measured:`, `<version>`): none, `stale text 1`.
- Fact lines: 11 (agent-run-variance, claude-code-agents-md, claude-code-imports, claude-code-path-rules, claude-code-project-skills, codex-agents-md, codex-repository-skills, context-file-effect, cursor-agents-md, instruction-density-accuracy, single-rule-compliance).
- No `.runs`, `checker` or machine path in the file.

## Changes beyond the brief
1. §7 "When to add a rule": the replacement sentence is followed by the WAY-130 exception (a rule that carries a recorded decision or a step of an activity in the file that leads it needs no repeated mistake).
2. §7 "Every rule added against a mistake names that mistake (WAY-130)" replaces "Every rule has a named mistake that it removes", so it no longer contradicts the exception.
3. §7 "When to remove a rule": the last bullet is now scoped to rules added for a mistake, split into removal (mistake can no longer be named) and removal test (mistake named but may no longer happen), and says a decision- or step-carrying rule goes with that decision or step. The first bullet gained "(a rule added for a mistake)".
4. Sources, studies, to match the abstracts read:
   - `2605.10039v1`: written from the fact (no detectable contrast from the four structural variables; about 5.6% lower odds per additional function), with no compliance percentage.
   - `2606.15828`: version read on its abstract page is v5. The abstract does NOT state "91 of 100"; it gives six smells (four named), a catalogue from grey literature and mining, 100 popular repositories, Lint Leakage 62%. The entry says only that.
   - `2511.12884v2`: abstract says files grow by frequent small additions; "deletions negligible" dropped (it is from WAY-130's html section 4.2.3, not the abstract).

## arXiv versions read
2606.15828 abstract page: latest v5 (written as v5); 2511.12884v2 abstract read.

## Concerns
- The brief's "91 of 100" is unsupported by the abstract; removed. Check whether another source holds it before reinstating.
- WebFetch summarises rather than quotes, so the abstract wording was verified by summary.

## Fix round 1
Before/after (principles.md):
- §6 Statically bullet: "A verdict to add, reword or move a rule rests on a mistake found more than once in records of the work, or on a stated cost" -> "A verdict to add or reword a rule rests on a mistake found more than once in records of the work, or on a decision or step it carries; a verdict to keep, move or remove one may rest on a stated cost" (controller ruling, WAY-130).
- single-rule-compliance study: "... compliance with a single trivial rule, and ... about 5.6% lower odds of compliance" -> "... after multiple-testing correction, and ... about 5.6% lower odds of compliance per step, though not as a constant effect".
- 2511.12884v2: "instruction files grow by frequent small additions" -> "instruction files evolve through frequent small additions".
- 2602.11988v3: "raise the cost of a task by over 20%" -> "raise inference cost by over 20%".
- 2602.07150v3: "differ by several percentage points" -> "differ by 2.2 to 6.0 percentage points in a single run's score".
- §6 In operation: "a move into enforcement (a hook, CI, a check of the output)" -> "a move into enforcement (CI or a check of the output; a hook only against slips)".
- Rewrapped to about 100 columns: the "Loaded is not yet carried out" bullet, the opening of §3, the `@path` pitfall, the first removal bullet. No wording change.
Checks rerun: 13 decision citations, stale text 1, 11 fact lines, no non-table line over 100 columns.
