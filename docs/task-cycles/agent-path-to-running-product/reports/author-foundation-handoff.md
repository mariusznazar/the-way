# Foundation stage handoff — author, turn 1

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product` (branch `task/agent-path-to-running-product`).
Base: `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` (= `origin/foundations`).
Cycle record: `.runs/task-cycles/agent-path-to-running-product/cycle.md` (ignored; read it for route and choices C1–C5).

## Authority and delegation

- Task: `.runs/task-cycles/agent-path-to-running-product/task.md` — frozen copy of the accepted task document (Polish). Read it whole. Its rows 1–6 of *Settlements to record* and the answers to questions 1–6 are the human's settled meanings. Mariusz invoked `implement-task` and delegated every intermediate choice to the orchestrator; do not ask him anything. You return questions to the orchestrator.
- The task cites `foundations` `e7f7c3a`; the base is `77c8a8b`. Between them only WAY-125, WAY-161..164, fingerprint renewals in WAY-140/148/157 and `task-cycle` files changed; the decisions the task cites are unchanged, their line numbers shifted (WAY-137 by about 9 lines).
- Route: one author without spec or plan (WAY-136). You are that author: the foundation step now, the code later (turn 2), the return step after review. No other agent writes in this worktree while you work.

## Read first (whole)

1. `AGENTS.md`, `agent-instructions/README.md`.
2. `task-cycle/skill/SKILL.md` — the paragraph "Before dependent implementation, run the foundation step …" (the rules for writing entries, rows of *Settlements to record*, *Approved by*, invariants by three agents).
3. The-way's `record-decision` skill: `.claude/skills/the-way-record-decision/SKILL.md` and every file it names (templates, `elements/common/rules.md`, `elements/common/way_of_working.md`, examples). Use other element skills (`the-way-record-glossary-term`, `the-way-update-part-map`, …) only if your search shows an entry of their kind is needed; read theirs whole then. Do NOT use `the-way-record-invariant` in this turn (see Invariants below).
4. The files the change will later touch, for knowing what the decisions must make possible: `project-level/definition_template.md` (section "Technology"), `project-level/technology/SKILL.md`, `project-level/readiness_check.py`, `project-level/skill/SKILL.md` (gate), `project-level/task/skill/SKILL.md` (around lines 75–85), invariant `project-technology-record/1` in `foundations/invariants.md`.

## What this stage does

- Select and read the foundation by "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150); write the selection (revision, touched parts, expected *Scope* matches, selected identifiers with source lines, read vs discovered) to `.runs/task-cycles/agent-path-to-running-product/reports/foundation-selection.md`. Touched parts at least `project-level`; the task names WAY-121, WAY-122, WAY-123, WAY-137, WAY-138, WAY-118, WAY-139, WAY-140, WAY-143, WAY-100, WAY-04, invariant `project-technology-record`; glossary term `surface` has a narrow meaning the interface item must not use (task's Context).
- Search the whole foundation (all five elements) for unlinked effects (WAY-33), with alternative vocabulary (log, logging, observability, running product, interface, UI, browser, terminal, API call, seed, fixture, test data, development data, test environment, staging, agent works with, tie, place to run …). Record domain, terms and findings.
- Write each row 1–6 whole, as a decision (WAY-134): wording yours, meaning the row's. Before `main`, edit an existing decision in place (README) — WAY-121 is the expected home of rows 1–4 per the task's answer to question 2; settle by your search whether rows 5 and 6 belong in WAY-121, in another existing decision (row 6 against WAY-137 is a carried question) or in a new one. Update every fingerprint and dependent entry a changed binding part affects (WAY-31): WAY-122, WAY-123 and the invariant derive from WAY-121@740c254e. Name what is adopted from the lesson "Towards Autonomous Product Development", where and why (WAY-100).
- Carried question (a): how the readiness script recognizes the three items, given each item names its choice in the definition's language and only its marker is English (`project-level/definition_template.md:167-169`). The entry and template wording must make the three items mechanically recognizable without changing row 1's meaning. Settle it, record the ways weighed and their cost in your report; it is your wording of row 1 (and of the template later), not a new meaning.
- *Approved by* of every new or changed decision: `Mariusz, merge of <request link>` (placeholder, swapped later). Set every *Review when* yourself.
- If a row cannot hold — it collides with a current entry, the code shows an exception the row does not allow, or it needs a value neither the row nor your work gives — stop and report it; never write a row with another meaning.
- Invariants: `project-technology-record/1` must change (To do 2, rows 4 and 5). Its sentence and its check come from two other agents (WAY-69), dispatched by the orchestrator after this turn. Do not edit `foundations/invariants.md` or any test marked `# invariant:`. Instead, in your report, name what the decisions now require of that invariant (in terms of the decisions, not of code), including your view on carried question (d): whether the invariant covers the run of the readiness script on an already approved definition (row 5).
- Do not edit non-foundation files in this stage (template, skills, script come in turn 2).
- If you meet an open design choice the task does not settle, or the change proves too large for one author, return a report without code or diff, as the cycle's recovery rules say.

## Checks

Run, with complete stdout+stderr saved under `.runs/task-cycles/agent-path-to-running-product/reports/` and the exit code recorded for each: `python -B gate/run_tests.py elements/decisions`, `python -B gate/run_tests.py gate` (critical flows), and the format guards of changed foundation files with `--base none` and, where available, `--merge-onto none` (README). Count fingerprint links and confirm none stale. Name every warning and `unchecked` result.

## Write boundary

Only inside this worktree. Never the original checkout `C:/Storage/repos/the-way`, the vault, or another repository. Preserve line endings (byte I/O or `newline=''`). Commit by explicit paths (`git add <file> …`), English message in the repository's style; never stage `.runs/`. No push, no PR. Do not spawn agents. Strip secrets and personal data from reports.

## Output

Full sanitized report: `.runs/task-cycles/agent-path-to-running-product/reports/author-foundation.md` — input versions; selection summary; search domain, terms and findings; for every entry written or changed: identifier, which row(s) it carries, one sentence of its meaning **in Polish**; settlement of the carried questions (a), (b) and your view on (c), (d); what the invariant must now require; choices with rejected alternatives and cost if wrong; commands, exit codes and output paths; changed files with added/removed line counts for the commit range; sharpness inputs from your actual diff (criticality of touched parts, trust-boundary files, irreversible operations); unresolved concerns.

Return message (short): status, report path, commits, check result incl. failures/unchecked, concerns affecting the next dispatch. Stop at the committed foundation change; the orchestrator dispatches the invariant agents and then gives the go-ahead for the code.
