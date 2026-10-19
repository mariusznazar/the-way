### Slice 5 — The task cycle: the reviewer runs the test cases

- **Goal:** `task-cycle/skill/SKILL.md` holds, at the code reviewer's deliberate break in step 10
  and at step 11's for return-step checks, the one sentence of spec §7 (C8, C18, C19): for an
  invariant a rule of the product's guidelines names with test cases, whose sentence the change adds
  or alters or one of whose cases it rewrites, the reviewer also runs the check in a scratch
  worktree of the commit with that invariant's good file and with its bad file in place, records
  that it passes and fails there — relatively for a listed invariant, strictly for its per-file
  companion — and does not accept the check otherwise; the bad file is a case beside the break,
  never the break; cases are applied only in the scratch worktree. Nothing else changes; the
  frontmatter stays as it is.
- **Change:** `task-cycle/skill/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `product-guidelines/template.md` · `foundations/decisions.md:203-232`
  `foundations/decisions.md:1440-1474` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:3665-3725` · `foundations/decisions.md:4723-4763`
  `foundations/decisions.md:5510-5578` · `foundations/decisions.md:6352-6386`
  `foundations/decisions.md:6674-6713` · `foundations/decisions.md:6974-7015`
  `foundations/invariants.md:136-144` · `foundations/invariants.md:1107-1115`
  `foundations/invariants.md:2243-2251`
- **Checks:** process prose; no test asserts it. `git diff --stat` shows this file alone, its
  frontmatter untouched; `python -B agent-instructions/skill_entry_points.py` prints
  `entry points are current` (no description changed); `python -B gate/run_tests.py task-cycle`
  and `python -B gate/run_tests.py gate` pass. Manual, in the report: the sentence in step 10 and
  in step 11, each element of spec §7 present, no review against guidelines added (Q5).
- **Depends on:** Slice 1 · F1a (WAY-168, WAY-197) · F1b (WAY-205) · F3
  (`gate-guidelines-example-evidence`)

