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

### Task 1: Foundation step (WAY-01, WAY-03; cycle skill, paragraph before step 9)

Every sub-step below is one fresh agent, dispatched by the orchestrator with the dispatch contract of the cycle skill (delegation, binding sources, stage boundary, write boundary, report returned as text). Each element agent:

- reads, at the process root, its element's `skill/SKILL.md` in full, `elements/common/way_of_working.md`, `elements/common/rules.md`, its element's `template.md` and `examples.md` (or the entries its template names), and follows them; where the skill says "Installed globally … resolve it first", it skips that: the-way is the process root `C:\Storage\repos\the-way-process`;
- treats the task worktree as the product: it reads and writes `foundations/` there, and reads the-way's glossary there (the-way is the product);
- sends every question of step 4.1 to the orchestrator, never to Mariusz; the orchestrator answers provisionally (the request carries the two questions on WAY-09 and WAY-27 for Mariusz);
- runs the whole-foundation search of `way_of_working.md` step 2 (WAY-33) for its entries and returns its findings, each as a link, a change to an entry, or a question;
- returns one sentence in Polish (the task document's language) of each entry's meaning, for the request (WAY-114);
- writes only the files named in its sub-step, and commits nothing (the orchestrator commits in 1.8).

Inputs every element agent gets: `spec.md` §1, §2, §5, §7; amendments N1–N5 (report 04); `frozen_task.md`; this sub-step. The check author of 1.7 gets none of these (see 1.7).


#### 1.6 Part-map agent — `update-part-map`

**Files:** Modify `foundations/part_map.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\part-map\skill\SKILL.md` and (spec §7):
  - **`agent-instructions`, changed**: responsibility adds the project skill entry points that make the-way's skills visible to sessions on it; *Files* add `.claude/skills/**` and `.agents/skills/**`; *Depends on* adds `project-level · task-cycle`; *Failure modes* add "a skill of the-way has no entry point, or a stale one — a session on the-way uses a personal skill of that name or none — high — detected by skill-entry-points" and "the-way's own entry point, loaded from a product's `.the-way`, is followed instead of the product's, where the agent knows neither the entry point's path nor the session's start directory (Claude Code's documentation states neither is given to the agent) — a product entry is written against the-way's own foundation — high — not detected".
  - **Critical flow `skills-reach-the-way-sessions`, new**: someone adds, renames or moves a skill of the-way, or changes its description, and a session on the-way that would not find it under its `the-way-` name is reported before the change reaches the main branch. *Criticality* high; *Parts* `agent-instructions · elements-common · decisions · invariants · glossary · part-map · environment-facts · project-level · task-cycle · gate`; *Invariant* `skill-entry-points`; *Coverage* `none`.
  - The search also answers whether `gate` needs a dependency for its new test, which reads other parts' files but imports none of their code, and returns the finding.

- [ ] **Step 2: Orchestrator check** — deferred to 1.8 (the guard needs the flow's test, which 1.7 writes).

