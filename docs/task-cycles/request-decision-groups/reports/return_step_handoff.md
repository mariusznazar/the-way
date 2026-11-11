# Handoff — the return step (step 11), the one author resumed

Stage: the return step of the task cycle. Do not start another stage; no human approval is sought.

- Worktree: `the repository's root (the task's worktree)`, branch `task/request-decision-groups`, head `9d4bdcde27179325126d1431e6cb825df3290754` (reviewed PASS; the orchestrator's gate on it: `python -B gate/run_tests.py` exit 0, 883 tests in 9 directories).
- Read `task-cycle/skill/return_step.md` whole and follow it (it also names which skill writes which element; read the skill of an element when you write an entry of it).
- Frozen task: `docs/task-cycles/request-decision-groups/task_frozen.md`. Entries the change wrote or changed: WAY-287, WAY-289, WAY-290, WAY-317 (edited), WAY-327 (new). Compare them, the entries the task names (WAY-286, WAY-288, WAY-114) and those the search of the foundation found with the files of the repository (the template, `request_check.py`, `correction.md`, `SKILL.md`), and the part map entries `task-cycle` and `decisions`; correct in the same change whatever no longer matches. If nothing needs changing, commit nothing and say so.
- Your report goes to: `docs/task-cycles/request-decision-groups/reports/return_step_report.md`. It states, for the record's *Return step*: foundation compared with code (what no longer matched and its correction, or none); decisions written or changed; invariants written or changed; environment facts; glossary terms; part-map changes; projected entries; rows of *Settlements to record* written (row number and identifier for each of rows 1–5). Include **Unread material**, **Searches not found or unclear**, every check with its command and exit code.
- Commit only by explicit paths, English messages, no push. Do not run the whole gate.
