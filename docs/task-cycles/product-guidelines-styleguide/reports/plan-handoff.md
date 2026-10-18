# Planning-stage handoff

The user invoked `the-way-implement-task` and delegated intermediate choices to the root
orchestrator. You run step 8 of `task-cycle/skill/SKILL.md` only: the plan. Use this worktree's
`task-cycle/plan/SKILL.md` (project skill `the-way-plan-task`), read whole with what it names — not a
personal plan skill, not Superpowers `writing-plans`. Never write code, a test or a foundation
entry; never ask the human; send questions to the root by returning them.

- Worktree: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, branch
  `task/product-guidelines-styleguide`, base `96623ed7710100fe6e11a0ce3c052fc44d4af52d`
  (`foundations`); nothing committed yet.
- Read whole: the frozen task `.runs/task-cycles/product-guidelines-styleguide/task.md` (binds over
  the spec; 27 rows the human accepted), the reviewed spec `.runs/task-cycles/product-guidelines-styleguide/spec.md`,
  the review `reports/spec-review.md` with its re-review section, and the root's rulings C5–C23 in
  the questions table of `cycle.md`. The spec's review is settled: every finding addressed, R1
  confirmed by the root at `spec.md:282`.
- Select the current foundation by "Reading the foundation" (WAY-150) for the parts the spec
  touches: decisions, glossary, part-map, invariants, agent-instructions, installation,
  instruction-files, project-level, task-cycle, elements-common, relation-model, gate (critical
  flow `skills-reach-the-way-sessions`), and the new part `product-guidelines`. The designer's
  `reports/foundation-selection.md` is a map, not proof. Keep decisions as whole-entry ranges in the
  plan, not snippets.

What the plan must hold, beyond what `plan-task` requires:

- *Foundation entries* first, ordered before every slice whose code depends on them: the decisions
  G1–G26 the spec names (mapped to all 27 rows, the WAY-100 adoption decision included), the
  in-place edit of WAY-09 and the renewal of every fingerprint it moves, the glossary term
  "guidelines", the part-map part `product-guidelines` with its dependency and flow updates, and
  the-way's invariants (`guidelines-form`, `guidelines-reference-current`, the six
  `guidelines-check-*`). Invariants need three different authors for sentence, check and covered
  code (WAY-69): plan the sentence and check stages as separate foundation-stage work and say which
  code each check covers; the plan names a check but does not write it.
- Slices for the code and text: the form script and its tests (a trust boundary — WAY-48 crafted
  inputs from the spec's §10), the common template and the styleguide template, the skill
  `maintain-styleguide`, the installer's `SKILLS` and guidance and their tests, the entry points
  (`python -B agent-instructions/skill_entry_points.py --write` changes every generated entry point
  because a sibling name is added — name the generated paths so the size check does not hide them),
  README lines the spec names. Each slice independently reviewable, each with a fresh executor.
- Every slice's tests and commands must actually run in this worktree today (Python 3.14.3, Git
  Bash; `python -B gate/run_tests.py <dir>`, guards with `--base none` / `--merge-onto none`).
- Source mapping for every row of *Settlements to record* to the entry that writes it, and for every
  *To do* item to its slice.
- Your *Independence and execution* recommendation; the root records the ruling. Superpowers 6.4.1
  `subagent-driven-development` runs slices sequentially.

Baseline (all exit 0, Python 3.14.3): gate 98, decisions 169, invariants 233, glossary 204, part-map
162, environment-facts 165, relation-model 19, agent-instructions 18, installation 30,
instruction-files 104 (5 skipped), task-cycle 41, project-level 250; decision guard 0 errors, 5
pre-existing warnings; logs `reports/baseline-*`.

Write only `.runs/task-cycles/product-guidelines-styleguide/plan.md`, `plan-size.md` (the report of
`python -B task-cycle/slice_size.py .runs/task-cycles/product-guidelines-styleguide/plan.md`, run
until every slice fits, unchecked paths fixed) and `reports/plan.md` (selection, coverage, choices
with costs, size command with exit code and full output path, unresolved concerns). Return status,
paths, checks and concerns only. Dispatch no agents and start no implementation.
