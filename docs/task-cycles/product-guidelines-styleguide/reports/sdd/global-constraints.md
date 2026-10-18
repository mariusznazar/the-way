# Global constraints for every slice of this plan

- Worktree `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, branch
  `task/product-guidelines-styleguide`. The frozen task
  `.runs/task-cycles/product-guidelines-styleguide/task.md` binds over the reviewed spec
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`; the spec binds where it settles more;
  the plan is its argument. The root orchestrator's rulings are rows C5–C28 of the questions table in
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md`.
- The foundation is written (`96623ed..8ea4679`): decisions WAY-167–WAY-192, the term "guidelines",
  part `product-guidelines`, eight invariants `foundations/invariants.md:2133-2212`. No slice edits
  `foundations/`. A slice that needs an entry changed stops and reports.
- `product-guidelines/test_form_check_invariants.py` is an invariant test written by another agent:
  read-only (WAY-03). Its assertions (exit codes, line numbers, message fragments) are the contract
  (C28.2). A slice that needs it changed stops and reports.
- Scripts run on the declared Python with the standard library only, and install nothing (WAY-38).
  `product-guidelines/form_check.py` is a trust boundary (WAY-48): it reads a product's files as
  untrusted input (spec §5.4).
- Every behaviour change goes test first (Superpowers 6.4.1 `test-driven-development`, read from
  `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/test-driven-development/SKILL.md`).
- Code, identifiers, comments, commit messages in English; commits by explicit paths only
  (`git add <file>`), never `-A`/`.`; messages in the repository's style (`feat(product-guidelines): …`).
- Before returning, the executor names the requirement of its slice, read against the task, that
  its work most likely does not meet, writes a check that would catch it (a test, or a manual check
  with method, actor, observed result and evidence), runs it and states which requirement, which
  check and what it showed (WAY-164).
- The report records every check command with its exit code and the path of its complete output,
  saved under `.runs/task-cycles/product-guidelines-styleguide/reports/slice-<N>-<name>.txt`; the
  changed-file list with added and removed lines for the slice's commit range; and the sharpness
  inputs from the actual diff (parts touched, trust-boundary files, anything irreversible).
- Expected red states are recorded, never suppressed: F4 reference tests until slice 3; gate and
  agent-instructions tests on 30 stale entry points from slice 4 to slice 7; the part-map guard's
  three errors until slices 1–2 add the files.
