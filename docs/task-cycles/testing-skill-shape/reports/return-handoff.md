# Return step — maintain-testing-guidelines in the WAY-256 shape

Same worktree, branch and rules as `reports/author-handoff.md`. Stage: the return step of the task's
cycle, on your class. Head: `c17f4f8`, reviewed `PASS c17f4f8`; the orchestrator's gate on it exited
0.

Read `task-cycle/skill/return_step.md` whole and `task-cycle/skill/foundation_step.md` whole, each
in this worktree, and follow them; read the skill of an element only if you write an entry of it.
The return step of this repository is also what `agent-instructions/README.md`, "Make the change",
gives.

Compare with the files at the head: the entries the change writes or changes (WAY-256, WAY-265,
WAY-266), each decision of the task's *Decisions in play*, each entry the search of your repair
found, and the part-map entries `product-guidelines`, `instruction-files` and `decisions`. The
search of the foundation is not made a second time.

Correct in the same change whatever no longer matches, in a new commit, by `git add <paths>`; if
nothing needs it, commit nothing. A finding you cannot settle by correcting an entry returns as a
question. Minor findings of the reviews are not part of this step.

Do not run the whole gate. Report: `.runs/task-cycles/testing-skill-shape/reports/return.md`, with
what you compared, what no longer matched and its correction, or none; decisions, invariants,
environment facts, glossary terms and part-map changes written or none; the rows of *Settlements to
record* with the identifier of each; each check's command and exit code; reaches; concerns; and
**Searches not found or unclear**. Return: your status, your commits or none, a one-line check result
naming what failed or did not run, and the report's path.
