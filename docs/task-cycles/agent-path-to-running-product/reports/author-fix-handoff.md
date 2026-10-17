# Review fix handoff — author, turn 3

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product`, at `c657b2b`.
Review: `.runs/task-cycles/agent-path-to-running-product/reports/review.md` (range `77c8a8b..c657b2b`, verdict "With fixes").

## What to fix

The review leaves one blocking finding — **Important 1** (`project-level/skill/SKILL.md:68-74`: `define-project` still offers to "leave" a definition with no `## Technology` section, which WAY-121 and row 5 now rule out, and the stated cost is wrong). Read its full text in `review.md` ("Important (Should Fix)") and fix it. This is the one fix the review allows ("The end of a code review", WAY-162).

Do not fix the Minor findings or act on the *Declined to judge* lines: under the task-cycle skill they are not fixed and go to the request's lists. If you hold Important 1 wrong, do not change the code for it; answer it with evidence in your fix report instead.

Rules as before: no `foundations/**` and no test marked `# invariant:` (read-only; if the fix needs one changed, stop and report). TDD where the fix changes behaviour; a skill text change gets a manual check recorded with method, actor, observed result and evidence.

## Checks

Rerun the affected checks, outputs under `reports/` with prefix `fix-`, exit codes recorded: `python -B gate/run_tests.py project-level --record .runs/project-level-tests.jsonl`, `python -B gate/run_tests.py gate`, `python -B agent-instructions/skill_entry_points.py` (check mode), `git diff --check 77c8a8b..HEAD`. Rerun your weakest-point check if the fix touches what it covers.

## Write boundary and output

As in turn 2. Append a section "Fix (turn 3)" to `reports/author-implementation.md`: what changed and why, any finding answered with evidence, commands, exit codes, output paths, changed files with added/removed lines for `c657b2b..HEAD`, sharpness inputs if changed. Return a short message: status, commit, checks, concerns.
