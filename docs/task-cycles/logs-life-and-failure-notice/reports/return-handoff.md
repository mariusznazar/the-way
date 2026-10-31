# Handoff — the return step

You are the one author; your first handoff, `.runs/task-cycles/logs-life-and-failure-notice/reports/author-handoff.md`, still holds: its worktree, its restriction, its commit rules and its boundaries.

Your stage: **the return step**, as you have not taken it yet. It takes none of the rows of the table in `task-cycle/change/SKILL.md`. Read `task-cycle/skill/return_step.md` whole, and `task-cycle/skill/foundation_step.md` whole, since the return step writes as the foundation step writes; read the skill of an element when you write an entry of that element.

- Head: `7f69096`, reviewed `PASS`, full gate on it passed. Range of the change: `5d66387..7f69096`.
- Compare with the files of the repository: the entries the change writes or changes (WAY-270, WAY-121, WAY-139, WAY-165), those the task names under *Decisions in play*, those your search of the foundation found (`reports/author.md`, under *Searches*), and the part map entries of `project-level` and `decisions`. Correct in the same change whatever no longer matches, and nothing else (`agent-instructions/README.md`, "Make the change").
- Check that each of the four rows of *Settlements to record* is written whole, with the human's decision "poprawmy to" as its later word: a decision silent on part of a matter opens at a task only on the human's word, WAY-267 unchanged.
- The Minor findings of the reviews are no part of this step: they go to the request. Do not fix one as a correction of the return step unless the entry and the file really say different things; then name it.
- No entry is deferred. A choice that binds after the merge and stands in no entry is what you are looking for.

Where nothing needs changing, make no commit and say so. Run `python -B elements/common/foundation_check.py .` and report its command and exit code, not through a pipe; the full gate stays mine.

Write your report to `.runs/task-cycles/logs-life-and-failure-notice/reports/return.md`: each line of the record's *Return step* (foundation compared with code; decisions written or changed; invariants; environment facts; glossary terms; part-map changes; projected entries; rows of *Settlements to record* written, each with its identifier), with **Searches not found or unclear**. Return only your status, your commits or that there are none, a one-line check result naming what failed or did not run, and the report's path.
