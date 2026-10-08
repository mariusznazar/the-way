## Global Constraints

- Task worktree (the product): `C:\Storage\repos\the-way-skills-self`, branch `task/the-way-skills-in-the-way`, base `c64a6071384fb57cdb9d7e9db4560ddc43e3b355`. Every command below runs from its root.
- Process root (read-only): `C:\Storage\repos\the-way-process` at `c64a6071384fb57cdb9d7e9db4560ddc43e3b355`. Every the-way skill an agent follows is read from there (`elements/<element>/skill/SKILL.md`, `elements/common/way_of_working.md`, `elements/common/critique/SKILL.md`); never a globally installed skill (`record-*`, `update-part-map`, `refine-task`, `critique`), never the task worktree's copy of a skill, which this task edits.
- Record directory: `R=.runs/task-cycles/the-way-skills-in-the-way` (ignored by git). Check outputs go to `$R/reports/check_<task>_<name>.txt`. Each Bash call starts a fresh shell, so every command block below begins with `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && …`.
- Python: always `python -B`; scripts use the standard library of Python 3.14 only and start no program but git (invariants `script-language`, `script-imports`, `script-subprocesses`).
- Files are UTF-8 with LF (`.gitattributes`: `* text=auto eol=lf`). Edit files with the Edit or Write tool; do not write file content through Bash heredocs or `python -c` strings — the Bash tool collapses `\\` and has written a NUL byte where `\0` was meant.
- Commit by explicit paths (`git add <path> …`), never `git add -A`, `git add .` or `git commit -a`. Messages in English, the repository's style: `<type>(<part>): <Capitalised imperative>`. Identity is already local: `<author email>`.
- Two writing agents never edit the worktree at the same time; dispatches below are sequential.
- *Approved by* of every new or changed decision: `Mariusz, merge of <request link>` (the placeholder step 12 swaps). Never a date.
- Results are named as partial checks, never as a pass of the full gate (`agent-instructions/README.md`).
- Entry-point names: `the-way-<name>`; description suffix exactly ` Use this checkout's own the-way.`; directories exactly `.claude/skills/` and `.agents/skills/`.
- Generator command exactly: `python -B agent-instructions/skill_entry_points.py --write`.
- Critical flow identifier `skills-reach-the-way-sessions`; invariant `skill-entry-points/1`; decision `WAY-127/1` (provisional number; step 12 renumbers if taken); facts `claude-code-project-skills/1`, `claude-code-nested-skills/1`, `codex-repository-skills/1`, `codex-skill-paths/1`.
- Not in this plan (the orchestrator runs them, steps 11–12): the return step, the independent assessment, the request, the record commit pair, the placeholder swap, reconciliation with `origin/foundations` (099c190), the human step of point 6.
