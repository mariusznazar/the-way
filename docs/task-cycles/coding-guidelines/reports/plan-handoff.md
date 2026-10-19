# Planning handoff — coding guidelines (step 8 of the task cycle)

## Delegation

Mariusz asked for the-way's task cycle to take this task to a pull request and delegated
intermediate choices to the orchestrator. You are the planner of step 8. You never ask Mariusz
anything; questions go back to the orchestrator in your report.

## Worktree and boundaries

- Worktree `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc` at `235b0b4`. **Read
  only for tracked files; write no code, no foundation entry, no commit.**
- You write: `docs/task-cycles/coding-guidelines/plan.md`,
  `docs/task-cycles/coding-guidelines/plan-size.md` (the report of
  `python3 -B task-cycle/slice_size.py` as `task-cycle/plan/SKILL.md` gives it; record its command
  and exit code), and your full report `docs/task-cycles/coding-guidelines/reports/plan.md`.

## Skill

the-way's `plan-task`: read whole `/home/user/the-way/task-cycle/plan/SKILL.md` and the files it
names, from this checkout. Your boundary is the finished plan with its size report; return before
any slice is made.

## Authoritative inputs (read whole)

1. Frozen task: `docs/task-cycles/coding-guidelines/task-frozen.md` (binding).
2. Reviewed spec: `docs/task-cycles/coding-guidelines/spec.md` (settled; the spec review ended
   after the fix of C18–C21, confirmed by the orchestrator).
3. Rulings C1–C21: `docs/task-cycles/coding-guidelines/reports/design-rulings.md` — they are
   applied in the spec; read them where the spec cites them.
4. Evidence only: `reports/design.md`, `reports/spec-review.md`.
5. The-way at `235b0b4`: `agent-instructions/README.md` (integration route, checks to run with
   `--base none` / `--merge-onto none`), `foundations/part_map.md`, the foundation by "Reading the
   foundation" for the parts the plan touches, and the code the slices change.
6. For structure only, the previous cycle on this frame planned foundation stages then slices:
   `git show cf27d79:docs/task-cycles/product-guidelines-styleguide/plan.md` (binds nothing).

## Requirements the plan must meet (the orchestrator reviews against these)

- Full coverage of every *To do* item and every one of the 25 rows of *Settlements to record*
  (each written whole as its entry, WAY-134), plus the entries the spec adds (new invariants of
  the-way, WAY-167/WAY-168 in-place edits with their dependents renewed under WAY-31, part-map
  failure modes, the task-cycle sentence).
- Foundation entries in *Foundation entries*, ordered before the slices whose code depends on them.
- Three different authors for each new or changed invariant's sentence, its check and the code it
  covers (WAY-69); the invariant tests are an assessed change (WAY-10).
- No code in the plan; tests and commands that can actually run here (Python 3.13.16; the repo
  declares 3.14 — record it); run_tests per changed part, `gate` critical flows, element guards with
  `--base none` and `--merge-onto none`, `skill_entry_points.py --write` and its check.
- Crafted-input checks for both trust boundaries (`product-guidelines/form_check.py`,
  `installation/install.py`, WAY-48).
- A size report in which every slice fits; an *Independence and execution* recommendation.
- Public sources quoted in WAY-195 re-read from the public source by the writing agent (spec §8.3).

Return a short message: status, paths, slices and size verdicts, choices for the orchestrator,
questions.
