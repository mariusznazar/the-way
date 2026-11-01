# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/skipped-test-names`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, task branch `task/skipped-test-names`. You change no tracked file and
  make no commit. Your report: `.runs/task-cycles/skipped-test-names/reports/whole-review.md`,
  ignored by Git.

## Your method and stage

Read `task-cycle/review/SKILL.md` whole and follow it for the review of **the whole change**: read
`task-cycle/review/whole_change.md` when it names it, and each other file when the step that names
it comes. You made none of this change. You alone select your own foundation and guidelines.
Your boundary: you return your report's first line, `PASS <sha>`, `FAIL <sha>` or `questions`.

## What you review

- Range: base `2f51e6c`, head `546eb52`. One author, no plan, so this is the review of the whole
  change and no slice stands apart.
- Frozen task, read it whole: `.runs/task-cycles/skipped-test-names/task.md`. Its citations stand at
  `foundations` `2f51e6c`, the base.
- Spec and plan: none.
- Author's report: `.runs/task-cycles/skipped-test-names/reports/author.md`.
- Answers of step 4: trust boundary no; operation that cannot be undone no.

Coverage to check: every item of the task's *To do*, its *Out of scope*, and its *Questions to
settle*. The task carries no row of *Settlements to record* and no projected entry.

The-way holds no `guidelines/` directory; the task's *Questions to settle* settles that this task
does not wait for them. The gate on the change is the orchestrator's run; do not run the whole of it.
The change to `gate/run_tests.py` is checked by `python -B gate/run_tests.py gate` and by
`python -B -m unittest discover -s gate -p "test_*.py"` (`agent-instructions/README.md`).
