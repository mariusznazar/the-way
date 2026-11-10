# Handoff 05 — the return step

You are the one author of this change, resumed for the return step. The delegation, the worktree,
the branch and the rules of `01-author-handoff.md` stand. This is neither a fix nor a new
implementation: the variant is the return step, and its method is
`task-cycle/skill/return_step.md` together with `task-cycle/skill/foundation_step.md` (read both
whole), by the path in this worktree. Use the skills of the elements you write
(`the-way-update-part-map` for the part map; the skill of any other element only if the step requires
it).

## State

- Head: `578a8bd` (your fix of the Minor findings), on `287a027`, on base `73b51db`.
- The review of the whole change: `PASS 287a027...`, report `reports/02-whole-change-review-report.md`;
  the review of the fix: `PASS 578a8bd`, report `reports/04-fix-review-report.md`. Both Minor lists
  are the cycle's: the one new Minor finding of the review of the fix (`installation/README.md:119`:
  a UTF-16 file with a byte-order mark is read, so the README's "not UTF-8 text" over-promises
  exit 2) is **not yours to fix**; it goes to the request's list.
- The orchestrator runs the whole gate on `578a8bd` in a separate checkout; do not run it.

## What you do

1. Compare with the code, as `return_step.md` gives: the entries you wrote or changed (WAY-320,
   WAY-323, WAY-324, the invariant `tracked-file-private-paths`), the entries the task names (WAY-309,
   WAY-16, WAY-321, WAY-34) and the part map of the touched parts (`task-cycle`, `installation`,
   `gate`), each with the code, and correct what no longer matches.
2. The part-map surface for the new command is yours to write, and the orchestrator has chosen to
   write it (record Q4): a surface entry through `the-way-update-part-map` for
   `task-cycle/tracked_private_paths_check.py` — the command a product relies on for its name, its
   argument and its exit codes, `Relied on by` a product pinned to a commit of the-way, in the form of
   `test-runner-command` and `installation-command`. Follow that skill's reading and its checks. Your
   own draft of this entry is in your report 01 (concern 1); the skill decides the final form.
3. A choice that binds after the merge (WAY-36) not yet in a decision, an environment fact, a
   glossary term (WAY-95), or a projected entry the foundation step missed: write it, or say it is
   none. No entry is deferred; an entry you do not write is neither proposed nor listed for later.
4. Run the focused checks of what you change: `python -B elements/common/foundation_check.py`
   (without `--skip-test-citations`, since the test already exists), and the tests of the directory of
   any file you change (`python -B gate/run_tests.py <directory>`).
5. Commit your work by path; if you change nothing, say so and commit nothing.

## Report

Write `.runs/task-cycles/private-path-patterns-in-code/reports/05-return-step-report.md`, holding
what the return step compares and writes by `return_step.md`, in the form of the record's *Return
step* section: foundation compared with code, decisions, invariants, environment facts, glossary
terms, part-map changes, projected entries and rows of *Settlements to record* written (each by
identifier, or `none`), each check with its command and exit code, the reaches beyond this handoff
and **Searches not found or unclear** (`none` is an answer). Return your status, your commits, a
one-line check result and the report's path.
