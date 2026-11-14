# Handoff — revision of the spec (the one revision the review allows)

Stage: you revise `spec.md` once after a `FAIL` of its review. The method, worktree, delegation and boundary are those of `reports/designer-handoff.md`; you write no code and no commit. The spec as reviewed is kept beside it as `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec-reviewed.md`. The reviewer's report, with the four findings in full: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/spec-reviewer-report.md` (read it whole).

## The orchestrator's rulings (autonomous choices, never the human's approval)

1. Finding 1 (the line for an unknown base breaks `installation/test_install.py::test_empty_foundations_have_valid_form`): settle as the reviewer's way (a). The `listed:` line for an unknown base is written only where the working tree's `foundations/decisions.md` holds at least one decision. Say in the spec that the installation tests are among the tests the change must leave passing as they stand, naming that one, and add a test of the script for a repository with no commit and an empty log that reads no such line.
2. Finding 2 (the pair of examples written at the foundation step and trimmed later has no file): settle as the reviewer's first way. Put the two halves where the reviewer says — one bullet in `elements/decisions/skill/SKILL.md` step 3 (a decision whose test a later slice writes carries a pair for now, since the run after writing reports a changed decision with nothing holding it) and one clause in `task-cycle/skill/return_step.md` (it removes from the pair the part a test then holds and names that test by the clause `tests:`) — and list both in the spec's file lists (D6, D3/D5 as fits) so the planner sees them. Keep the open alternative (the switch also skips the error, WAY-321 changed) in the line for the human as it stands.
3. Finding 3 (row 8's "rationale and rejected options stay whole" is missing from WAY-12): add it to the spec's line for WAY-12, as the reviewer says.
4. Finding 4 (a file missing at the base): settle as the first reading: a file the base lacks makes the base unknown for that file — no decision counts as changed, no invariant is listed from it, and the unknown-base line is written under the rule of ruling 1. One sentence in D1; the tests of D9 get a case for it.

## Also

Take into the spec, as the reviewer's notes bear on the build: name WAY-241, WAY-237, WAY-235 and WAY-268 under "Other decisions of the log the change reaches" with the way each is met; add the test of D9 for an invariant with no *Method* at the base or now; and say that WAY-12's and its attached paragraph's text calls what the script compares "binding sentences" where the glossary's "binding part" would read differently, or settle the one word the glossary and the script share. Do not widen the task.

## Report

Rewrite `reports/designer-report.md` as the method gives it, with a section naming each finding and where the revision settles it, and the sections **Unread material** and **Searches not found or unclear**. Write the revised spec to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md`. Return `done`, `questions` or `reserved`, a one-line result and the report path.
