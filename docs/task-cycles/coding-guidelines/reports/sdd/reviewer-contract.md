# Task reviewer contract — coding guidelines slices (SDD 6.4.1 task review, task cycle step 9)

Follow the Superpowers 6.4.1 task-reviewer template, read whole from
`/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/superpowers-6.4.1/skills/subagent-driven-development/task-reviewer-prompt.md`
(the prompt inside its fenced block is your instruction; the dispatch gives its placeholders).
You did not write this slice. Read-only on the checkout `/home/user/the-way`; never use the
Artifact tool or any publishing tool. Never ask Mariusz anything.

Cycle additions:
- Authority: frozen task `docs/task-cycles/coding-guidelines/task-frozen.md` over the reviewed spec
  `docs/task-cycles/coding-guidelines/spec.md` over the plan; later rulings in `cycle.md`'s
  questions table (C22–) and in `reports/sdd/progress.md` (`Ruling:` lines).
- Check the executor's weakest-point finding (WAY-164) and its sharpness inputs from the actual
  diff (parts touched, trust-boundary files: `product-guidelines/form_check.py`,
  `installation/install.py`); for a trust boundary, check the crafted-input tests (WAY-48).
- Where the slice covers code an invariant checks (the brief names it), write the **deliberate
  break** from the invariant's sentence in `foundations/invariants.md` (you did not write the check):
  in a scratch worktree (`git worktree add <scratchpad>/review-<sha> <sha>`), break the covered code
  so the sentence is false, run `python3 -B gate/run_tests.py product-guidelines` (or the
  directory named), record that a test citing the invariant fails (command, exit code, output path),
  then remove the scratch worktree. An undetected break is a finding.
- Grade each finding Critical, Important or Minor; mark a finding outside the task's scope as such.
- Write your full report to the path the dispatch names; return the report's verdict lines.
