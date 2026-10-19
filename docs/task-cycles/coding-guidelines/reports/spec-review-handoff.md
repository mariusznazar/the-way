# Spec review handoff — coding guidelines (step 7 of the task cycle)

## Delegation

Mariusz asked for the-way's task cycle to take this task to a pull request and delegated
intermediate choices to the orchestrator. You are the spec reviewer of step 7; you did not write the
spec. You never ask Mariusz anything; questions go back to the orchestrator in your report.

## Worktree and boundaries

- Worktree `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc` at `235b0b4`. **Read
  only**: edit no tracked file, do not commit, do not edit `spec.md`.
- Write only your full report: `docs/task-cycles/coding-guidelines/reports/spec-review.md`.

## Inputs (read whole)

1. Frozen task: `docs/task-cycles/coding-guidelines/task-frozen.md` (Polish,
   binding: *To do*, answers to questions 1–18, *Settlements to record* rows 1–25, *Out of scope*).
2. Spec: `docs/task-cycles/coding-guidelines/spec.md`.
3. Orchestrator rulings on the spec's proposals: `.../reports/design-rulings.md` (C1–C9) and the
   three points passed to you at its end.
4. The designer's report, for evidence only: `.../reports/design.md`.
5. The current foundation of the-way at `235b0b4`, selected by "Reading the foundation" in
   `elements/common/way_of_working.md` for the parts the spec touches; read whole every entry you
   rely on. Code and templates: `product-guidelines/**`, `installation/install.py`,
   `task-cycle/skill/SKILL.md`, `agent-instructions/skill_entry_points.py`, `gate/run_tests.py`.
6. Research of the task (read-only vault copy):
   `/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/brain-main/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_kodowania/`.

## What to judge

- Task compliance: every *To do* item and every one of the 25 rows is carried with its meaning
  (no narrowing, no widening); every answer of questions 1–18 respected; nothing out of scope
  brought in. Missing requirements, invented behaviour, contradictions.
- Foundation coherence: contradictions with current decisions and invariants (WAY-04, 08, 16, 22,
  30, 31, 38, 44, 48, 51, 60–63, 68, 69, 86, 95–99, 100, 114, 122, 127–129, 133, 139, 167–192 and
  any other you find), correct relations and renewal of dependents for the in-place edits,
  glossary words, invariants and their derivation, the three points the rulings pass to you.
- Whether the rulings C1–C9 fit the task and foundation.
- Whether a plan could be written from the spec: files, tests, commands that can actually run.

Grade each finding Critical, Important or Minor, with the place in the spec (`spec.md:line`) and
the evidence (task line or entry identifier). Return a short message: verdict on task compliance
and on coherence, counts by grade, and any question that needs an orchestrator ruling.
