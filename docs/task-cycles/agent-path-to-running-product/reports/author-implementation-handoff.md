# Implementation stage handoff — author, turn 2

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product` (branch `task/agent-path-to-running-product`), at `8720107`.
Inputs: your foundation commit `596a660`; invariant sentence `4c251dc` (sentence agent, [invariant-sentence.md](invariant-sentence.md)); invariant checks and fixtures `8720107` (check agent, [invariant-check.md](invariant-check.md)).
Cycle record: `.runs/task-cycles/agent-path-to-running-product/cycle.md` — read rulings C6–C11 (and C12 below).

## Authority

Same as turn 1: the frozen task `.runs/task-cycles/agent-path-to-running-product/task.md`, its To do 1–3 and rows 1–6; WAY-121@d0b060e5, WAY-165; the invariant `project-technology-record/1` as now written. The orchestrator gave a provisional go-ahead on the foundation. Ask the human nothing.

## Read first

1. Superpowers 6.4.1 `test-driven-development`, read from `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/test-driven-development/SKILL.md` and the files it links (NOT through the Skill tool, which loads 7.0.0; WAY-125).
2. The invariant sentence in `foundations/invariants.md` (`project-technology-record/1`) and the new checks in `project-level/test_readiness_check.py` (class `TechnologyMarks` and `Command.test_a_definition_lacking_a_mark_exits_one_approved_or_not`). These tests and every test marked `# invariant:` are **read-only** for you (WAY-03, WAY-69). If one of them seems wrong, stop and report — do not edit it; the orchestrator returns it to the foundation step.

## What this stage does

Make the code so the invariant's checks pass and the task's To do 1–2 hold, by TDD for behaviour changes (ordinary tests you write are yours):

- `project-level/readiness_check.py`: reject a definition lacking any of the three marked items, in both modes (before approval and on an approved definition with its gate record). Treat the input as untrusted (trust boundary, WAY-48).
- `project-level/definition_template.md`: the Technology section states the three mandatory items, their English marks at the start of the item (`logs:`, `interface:`, `development data:` — C6), that each is answered also where the product lacks the thing, and the example list shows them; cite WAY-121/WAY-165 like the other rules there.
- `project-level/technology/SKILL.md` (`settle-technology`): the list always holds the three; what each asks (WAY-165); an agent's use of an option weighed as a consequence in them (WAY-165, against WAY-137); resuming a definition that lacks one of the three (carried question (c) — your view in turn 1 is accepted: step 0 adds the missing items as open, step 2 settles them; for an approved definition the route back through the gate).
- `project-level/skill/SKILL.md` (`define-project`): the gate and the route of an approved definition the readiness check now stops for a missing item, back to the technology step and through the gate again (WAY-118, WAY-121).
- `project-level/task/skill/SKILL.md` (`refine-task`, around line 79) and any other skill that runs the readiness check on an approved definition (`plan-project`, `lead-project`, plan-state reader texts): say what happens when that run finds a missing item — the definition returns to the technology step and the gate before the refinement goes on (row 5, To do 3's effect).
- Concerns of the check agent you settle: (1) the template test runs the check on the template's Technology example — the template must carry the three items; (2) the uncited test `Technology.test_a_section_still_reading_todo_is_one_gap_and_no_g…` expects a section reading `TODO` to give one finding — settle how the mark rule treats a `TODO` section (ruling C12 below) and keep that test meaningful.
- Run `python -B agent-instructions/skill_entry_points.py --write` only if you change a skill's description (AGENTS.md); commit what it writes.
- Do not edit `foundations/**` in this turn. If the code shows that a foundation entry must change, stop and report.

Ruling C12: a Technology section reading `TODO` is one gap (the step has not run); the mark rule adds no finding to it unless the invariant's checks require otherwise. If a read-only check contradicts this, report it instead of working around it.

## Weakest-point check (WAY-164)

Before returning, name the requirement of the task (To do 1–3, rows 1–6) your work most likely does not meet, write a check that would catch it — a test, or a manual check recorded with method, actor, observed result and evidence — run it, and state which requirement, which check and what it showed.

## Checks

Save complete stdout+stderr under `.runs/task-cycles/agent-path-to-running-product/reports/` (prefix `implementation-`), with exit codes: `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`; `python -B gate/run_tests.py gate`; `python -B gate/run_tests.py agent-instructions` (skill entry points); `python -B agent-instructions/skill_entry_points.py` check mode if it has one; `git diff --check 77c8a8b..HEAD`. Name every warning, failure and `unchecked` result.

## Write boundary

Only inside this worktree; no `foundations/**`, no test marked `# invariant:`. Preserve line endings (byte I/O or `newline=''`). Commit by explicit paths, English message in the repository's style; never stage `.runs/`. No push. Do not spawn agents. No secrets or personal data in reports.

## Output

Append to your report a new file `.runs/task-cycles/agent-path-to-running-product/reports/author-implementation.md`: inputs; what changed and why per file; TDD evidence (red then green, with output paths); settlement of the check agent's concerns 1–2 and of carried question (c); the weakest-point check; choices with rejected alternatives and cost if wrong; commands, exit codes, output paths; changed-file list with added/removed lines for `8720107..HEAD`; sharpness inputs from your actual diff (criticality, trust-boundary files touched, irreversible operations); unresolved concerns.

Return message (short): status, report path, commits, check results incl. failures/unchecked, weakest-point result, concerns. Stop at the committed change; review comes next.
