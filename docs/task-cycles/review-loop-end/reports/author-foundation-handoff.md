# Foundation stage handoff — author, turn 1

Worktree: `C:/Storage/repos/the-way-wt/review-loop-end` (branch `task/review-loop-end`).
Base: `e7f7c3a15c3f80143f9ad582ec785c993cff3779` (= `origin/foundations`).
Cycle record: `.runs/task-cycles/review-loop-end/cycle.md` (ignored; read it for route and choices C1–C4).

## Authority and delegation

- Task: `.runs/task-cycles/review-loop-end/task.md` — frozen copy of the accepted task document. Read it whole. Its rows 1–7 of *Settlements to record* and the answers to questions 1–9 are the human's settled meanings. Mariusz invoked `implement-task` and delegated every intermediate choice to the orchestrator; do not ask him anything. You return questions to the orchestrator.
- Route: one author without spec or plan (WAY-136). You are that author: you do the foundation step now, the code later (turn 2) and the return step (turn 3). No other agent writes in this worktree while you work.

## Read first (whole)

1. `AGENTS.md`, `agent-instructions/README.md`.
2. `task-cycle/skill/SKILL.md` (whole) — the cycle this task changes; the foundation step is the section "Before dependent implementation, run the foundation step …".
3. The-way's `record-decision` skill: `.claude/skills/the-way-record-decision/SKILL.md` and every file it names (templates, `elements/common/rules.md`, `elements/common/way_of_working.md`, examples). Use other element skills (`the-way-record-glossary-term`, `the-way-record-invariant`, …) only if your search shows an entry of their kind is needed; read theirs whole then.
4. Superpowers 6.4.1, read from `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/` (NOT through the Skill tool, which loads 7.0.0; WAY-125 forbids another version): `requesting-code-review/SKILL.md` and `requesting-code-review/code-reviewer.md`, `subagent-driven-development/SKILL.md` and its `re-review-prompt.md` — the task's rows depart from named steps there, and the entries must quote them correctly.

## What this stage does

- Select and read the foundation by "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150); write the selection (revision, touched parts, expected *Scope* matches, selected identifiers with source lines, read vs discovered) to `.runs/task-cycles/review-loop-end/reports/foundation-selection.md`. Touched parts at least `task-cycle`; the task names WAY-125, WAY-136, WAY-11, WAY-10, WAY-148, WAY-13, WAY-69, WAY-101, WAY-140, WAY-134; glossary terms `verdict` and `correction` have narrow meanings (task's Context) — check them and any word your entries use.
- Search the whole foundation (all five elements) for unlinked effects (WAY-33), with alternative vocabulary (re-review, fix range, second review, blocked, Minor, Important, non-blocking, scope, weakest, deliberate break, final review, fix wave …). Record domain, terms and findings.
- Write each row 1–7 whole, as a decision (WAY-134): wording yours, meaning the row's. Settle the carried question "new decisions or an addition to an existing one" from the search; before `main`, edit an existing decision in place (README). Where an accepted row departs from a step of a method WAY-125 adopts (the task's *Decisions in play* names four such departures), WAY-125 must stop contradicting it — edit it in place and keep its other meaning. Update every fingerprint and dependent entry a changed binding part affects (WAY-31).
- *Approved by* of every new or changed decision: `Mariusz, merge of <request link>` (placeholder, swapped later). Set every *Review when* yourself.
- Do not use the glossary's narrow `verdict` / `correction` for the reviewer's call or the fix (task Context).
- If a row cannot hold — it collides with a current entry, the code shows an exception the row does not allow, or it needs a value neither the row nor your work gives — stop and report it; never write a row with another meaning.
- Invariants: these are runtime coordination rules (promise level 2 expected). If you conclude an invariant is needed, report that need before writing a sentence or a check — they need separate authors (WAY-69). No level-1 check that merely asserts prose.
- Do not edit `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` or other non-foundation files in this stage.
- If you meet an open design choice the task does not settle, or the change proves too large for one author, return a report without code or diff, as the cycle's recovery rules say.

## Checks

Run, with complete stdout+stderr saved under `.runs/task-cycles/review-loop-end/reports/` and the exit code recorded for each: tests of changed parts (`python -B gate/run_tests.py <dir>`, e.g. `elements/decisions`), `python -B gate/run_tests.py gate` (critical flows), and the format guards of changed foundation files with `--base none` and, where available, `--merge-onto none` (README). Name every warning and `unchecked` result.

## Write boundary

Only inside this worktree. Never the original checkout `C:/Storage/repos/the-way`, the vault, or another repository. Preserve line endings (byte I/O or `newline=''`). Commit by explicit paths (`git add <file> …`), English message in the repository's style; never stage `.runs/`. No push, no PR. Do not spawn agents. Strip secrets and personal data from reports.

## Output

Full sanitized report: `.runs/task-cycles/review-loop-end/reports/author-foundation.md` — input versions; selection summary; search domain, terms and findings; for every entry written or changed: identifier, which row(s) it carries, one sentence of its meaning **in Polish**; settlement of the carried questions you touched; choices with rejected alternatives and cost if wrong; commands, exit codes and output paths; changed files with added/removed line counts for the commit range; sharpness inputs from your actual diff (criticality of touched parts, trust-boundary files, irreversible operations); unresolved concerns.

Return message (short): status, report path, commits, check result incl. failures/unchecked, concerns affecting the next dispatch. Stop at the committed foundation change; the orchestrator gives the go-ahead for the code.
