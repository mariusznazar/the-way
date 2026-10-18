# Implementation stage handoff — author, turn 2

Worktree and branch as in turn 1. Input commit: `49d7d2b` (your foundation step). Cycle record: `.runs/task-cycles/agent-path-technology-step/cycle.md` — read rulings C6–C10 in the questions table; they answer your turn-1 concerns and the carried question.

## Go-ahead and rulings

- Provisional orchestrator go-ahead for the foundation change under Mariusz's delegation (the human accepts the entries at the merge).
- C6: keep "settles for that behaviour". C7: a matter the foundation settles is not listed. C8: no entry for the unusable-everywhere case or for test environment vs place to run. C10: your view on the carried question is accepted — implement it.

## What this stage does

Make the code (here: process text) that WAY-121 (row 1), WAY-165 and WAY-166 call for, and nothing else:

- `project-level/definition_template.md`, section "Technology": the exception to the rule of belonging for the three matters, what each matter asks (WAY-165), and WAY-166's weighing rule, each cited. Keep the existing markers and rules; no new marker and no item every definition must hold.
- `project-level/technology/SKILL.md`: step 1 looks at the three matters as C10 says; step 0 runs that look whenever it resumes a list before approval; step 2.3 / 2.5 apply WAY-166 (an option an agent cannot use stays with the lack "agent does not check the running product this way" and the recommendation passes over it); WAY-137's tie rule stays limited to a place to run. Keep the skill's role (order of the work; rules stand in the template).
- Any other file only if it states the Technology section's rule of belonging in a way the change now contradicts — search `project-level/`, `task-cycle/`, `elements/`, `installation/` for it and report what you found, changed or left. Do not change `project-level/readiness_check.py`, `foundations/invariants.md` or any test marked `# invariant:` (To do 2; the invariant keeps its meaning). If a skill's `description` changes, run `python -B agent-instructions/skill_entry_points.py --write` and commit what it writes.
- Superpowers `test-driven-development` 6.4.1 (`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/test-driven-development/SKILL.md`, read whole) for any behaviour a test can hold; process text with no executable behaviour is checked manually — say which applies and why.
- Weakest-point check (WAY-164): name the requirement of the task (To do 1–2, rows 1–4) your work most likely does not meet, write a check that would catch it — a test, or a manual check recorded with method, actor, observed result and evidence — run it and state which requirement, which check and what it showed.
- If you meet an open design choice the task does not settle, or the change proves too large, return a report without code, as the cycle's recovery rules say. If the foundation entries turn out to need a change, stop and report it rather than editing them.

## Checks

With complete stdout+stderr under `.runs/task-cycles/agent-path-technology-step/reports/` (prefix `implementation-`) and exit codes: `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py gate`, `python -B gate/run_tests.py agent-instructions`, `python -B agent-instructions/skill_entry_points.py` (check mode, as its help gives), `git diff --check 77c8a8b..HEAD`. Name every failure, warning and `unchecked`.

## Write boundary

As in turn 1: only this worktree, line endings preserved, commit by explicit paths with an English message in the repository's style, never `.runs/`, no push, no agents.

## Output

Append to a new full report `.runs/task-cycles/agent-path-technology-step/reports/author-implementation.md`: input version; what changed and why, per file; files searched and left; TDD or manual-check reasoning; weakest-point check; choices with rejected alternatives and cost; commands, exit codes and output paths; changed files with added/removed line counts for `49d7d2b..HEAD` and for `77c8a8b..HEAD`; sharpness inputs from the actual diff (criticality, trust-boundary files, irreversible operations); unresolved concerns. Short return message as before. Stop at the committed change, before review.
