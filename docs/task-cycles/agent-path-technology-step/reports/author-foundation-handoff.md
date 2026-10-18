# Foundation stage handoff — author, turn 1

Worktree: `C:/Storage/repos/the-way-wt/agent-path-technology-step` (branch `task/agent-path-technology-step`).
Base: `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` (= `origin/foundations`).
Cycle record: `.runs/task-cycles/agent-path-technology-step/cycle.md` (ignored; read it for route and choices C1–C5).

## Authority and delegation

- Task: `.runs/task-cycles/agent-path-technology-step/task.md` — frozen copy of the accepted task document (Polish). Read it whole. Its rows 1–4 of *Settlements to record* and the answers to questions 1–8 are the human's settled meanings; where an answer says it is superseded in part by answers 7 and 8, the later answer binds (nothing is mandatory in every definition, the readiness gate checks nothing new, no approved definition returns).
- Mariusz invoked `implement-task` and delegated every intermediate choice to the orchestrator; do not ask him anything. You return questions to the orchestrator.
- The task cites `foundations` `77c8a8b`, equal to the base.
- A first version of this task was implemented in PR #23 (branch `task/agent-path-to-running-product`), closed unmerged after review because it made the three items mandatory with gate marks. Nothing carries over from it: do not read or copy that branch. Its WAY-165 does not exist on the base.
- Route: one author without spec or plan (WAY-136). You are that author: the foundation step now, the code later (turn 2), the return step after review. No other agent writes in this worktree while you work.

## Read first (whole)

1. `AGENTS.md`, `agent-instructions/README.md`.
2. `task-cycle/skill/SKILL.md` — the paragraph "Before dependent implementation, run the foundation step …" (rules for writing entries, rows of *Settlements to record*, *Approved by*).
3. The-way's `record-decision` skill: `.claude/skills/the-way-record-decision/SKILL.md` and every file it names (templates, `elements/common/rules.md`, `elements/common/way_of_working.md`, examples). Use other element skills (`the-way-record-glossary-term`, `the-way-update-part-map`, …) only if your search shows an entry of their kind is needed; read theirs whole then.
4. The files the change will later touch, for knowing what the decisions must make possible: `project-level/definition_template.md` (section "Technology"), `project-level/technology/SKILL.md`; and, to confirm they need not change, `project-level/readiness_check.py`, invariant `project-technology-record/1` in `foundations/invariants.md`.

## What this stage does

- Select and read the foundation by "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150); write the selection (revision, touched parts, expected *Scope* matches, selected identifiers with source lines, read vs discovered) to `.runs/task-cycles/agent-path-technology-step/reports/foundation-selection.md`. Touched parts at least `project-level`; the task's *Decisions in play* names WAY-121, WAY-122, WAY-123, WAY-137, WAY-138, WAY-139, WAY-140, WAY-143, WAY-100, WAY-106, WAY-04 and invariant `project-technology-record`; glossary term `surface` has a narrow meaning the interface matter must not use (task's Context).
- Search the whole foundation (all five elements) for unlinked effects (WAY-33), with alternative vocabulary (log, logging, observability, running product, interface, UI, browser, terminal, API call, seed, fixture, test data, development data, test environment, staging, agent works with, tie, place to run, belongs on the list …). Record domain, terms and findings.
- Write each row 1–4 whole, as a decision (WAY-134): wording yours, meaning the row's. Before `main`, edit an existing decision in place (README). Row 1 is the named exception to WAY-121's rule of belonging (task answer 8), so WAY-121 is its expected home; settle by your search where rows 2–4 belong — in WAY-121, in a new decision, or (row 4) beside WAY-137, whose tie rule for a place to run stays. Keep each decision to what one question settles (WAY-122 rejects binding independent choices together; respect the element's rules on binding sentences). Update every fingerprint and dependent entry a changed binding part affects (WAY-31): WAY-122, WAY-123 and invariant `project-technology-record/1` derive from WAY-121 — for the invariant renew only its relation link (choice C5); its sentence and checks stay. Name what is adopted from the lesson "Towards Autonomous Product Development", where and why (WAY-100); the task's Context names the source and what is not adopted (the hard limit without production database and root).
- Carried question: where in `settle-technology` the check of the three matters stands, and how the step resumes a definition whose list arose before this change. Give your view in this report as far as the entries' wording depends on it; the skill text itself is turn 2.
- *Approved by* of every new or changed decision: `Mariusz, merge of <request link>` (placeholder, swapped later). Set every *Review when* yourself.
- If a row cannot hold — it collides with a current entry, the code shows an exception the row does not allow, or it needs a value neither the row nor your work gives — stop and report it; never write a row with another meaning.
- Do not edit non-foundation files in this stage (template and skill come in turn 2).
- If you meet an open design choice the task does not settle, or the change proves too large for one author, return a report without code or diff, as the cycle's recovery rules say.

## Checks

Run, with complete stdout+stderr saved under `.runs/task-cycles/agent-path-technology-step/reports/` and the exit code recorded for each: `python -B gate/run_tests.py elements/decisions`, `python -B gate/run_tests.py elements/invariants`, `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py gate` (critical flows), and the format guards of changed foundation files with `--base none` and, where available, `--merge-onto none` (README). Count fingerprint links and confirm none stale. Name every warning and `unchecked` result.

## Write boundary

Only inside this worktree. Never the original checkout `C:/Storage/repos/the-way`, the vault, or another repository. Preserve line endings (byte I/O or `newline=''`). Commit by explicit paths (`git add <file> …`), English message in the repository's style (see `git log`); never stage `.runs/`. No push, no PR. Do not spawn agents. Strip secrets and personal data from reports.

## Output

Full sanitized report: `.runs/task-cycles/agent-path-technology-step/reports/author-foundation.md` — input versions; selection summary; search domain, terms and findings; for every entry written or changed: identifier, which row(s) it carries, one sentence of its meaning **in Polish**; placement of rows 2–4 with the ways weighed; your view on the carried question; choices with rejected alternatives and cost if wrong; commands, exit codes and output paths; changed files with added/removed line counts for the commit range; sharpness inputs from your actual diff (criticality of touched parts, trust-boundary files, irreversible operations); unresolved concerns.

Return message (short): status, report path, commits, check result incl. failures/unchecked, concerns affecting the next dispatch. Stop at the committed foundation change; the orchestrator gives the go-ahead for the code.
