# Foundation stage handoff — invariant sentence agent

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product` (branch `task/agent-path-to-running-product`), at `596a660`.
Base of the task: `77c8a8b`.

## Authority and delegation

- Mariusz invoked the task cycle and delegated intermediate choices to the orchestrator; ask him nothing. Return questions to the orchestrator.
- You write the sentence of one invariant. Under WAY-69 the sentence, its check and the code it covers come from three different agents: you write only the sentence and its entry; another agent writes its check from your sentence and its method; the code's author writes the code. Do not read or edit the code (`project-level/readiness_check.py`) or any test to shape the sentence; write it from the decisions.

## Read first (whole)

1. The-way's `record-invariant` skill: `.claude/skills/the-way-record-invariant/SKILL.md` and every file it names (`elements/invariants/template.md`, examples, `elements/common/rules.md`, `elements/common/way_of_working.md`).
2. Decisions: WAY-121/1 (fingerprint `d0b060e5`, edited in `596a660`) and WAY-165/1 in `foundations/decisions.md`; WAY-118/1 and WAY-108/1 as context.
3. The current entry `project-technology-record/1` in `foundations/invariants.md` (around line 2021).
4. The section "What the decisions now require of `project-technology-record`" and "(d)" in `.runs/task-cycles/agent-path-to-running-product/reports/author-foundation.md` — the author's reading of the decisions, an input you weigh, not a ruling.
5. The definition template's Technology section `project-level/definition_template.md` (around lines 148–185), for the form of an item and its markers as it stands today.

## Rulings of the orchestrator already made (cycle record C6–C8)

- Each of the three items is recognized by a fixed English mark at the start of the item, before its name in the definition's language: `logs:`, `interface:`, `development data:` (C6). The template will be changed by the code author to say so.
- A second item with the same mark is not stopped (C7).
- The rule of row 5 holds wherever the readiness check runs on a definition, an approved one with its gate record included — not only "before approval" (C8; author's view (d)).

## What this stage does

- Rewrite `project-technology-record` so it states what the readiness check must reject under WAY-121 as it now stands: everything it rejects today, and a definition whose Technology list lacks the item marked as the logs, the interface or the development data — each of the three separately — whether or not the definition is approved. Keep it one invariant unless the skill's rules require a split; settle that by the skill.
- Before `main`, keep the identifier and version `/1` (edit in place; `elements/common/rules.md` "Version") unless the skill says otherwise; renew *Derives from* to `WAY-121@d0b060e5` (and add WAY-165 only if the sentence depends on it). Keep the *Method* line as the check's method unless the skill requires another.
- Search the invariants file for other invariants whose sentence the change touches (e.g. ones on the readiness gate or the definition form) and report them; change none of them unless the decisions require it — if so, report before editing.
- Do not edit `foundations/decisions.md`, tests, template, skills or code.

## Checks

Run, with complete stdout+stderr saved under `.runs/task-cycles/agent-path-to-running-product/reports/` (prefix `invariant-sentence-`) and the exit code recorded: `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` and `python -B gate/run_tests.py elements/invariants`. Recompute the fingerprint links from `foundations/invariants.md` to decisions with `relation-model/fingerprint.py` (first paragraph under the heading is the binding part) and report stale links. Name every warning and `unchecked` result.

## Write boundary

Only `foundations/invariants.md` in this worktree. Preserve line endings (byte I/O or `newline=''`). Commit by explicit path, English message in the repository's style; never stage `.runs/`. No push. Do not spawn agents. No secrets or personal data in reports.

## Output

Full report: `.runs/task-cycles/agent-path-to-running-product/reports/invariant-sentence.md` — inputs and versions; the final sentence verbatim; one sentence of its meaning **in Polish**; what changed from the old sentence and why, tied to WAY-121's wording; choices with rejected alternatives and cost if wrong; other invariants found and how they stand; commands, exit codes and output paths; changed file with added/removed lines; commit; concerns.

Return message (short): status, report path, commit, the final sentence verbatim, its *Method* line, check results, concerns.
