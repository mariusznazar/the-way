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


#### 1.2 Watch author — four watches

**Files:** Create `probes/<id>/test_<id_with_underscores>.py` for the four identifiers.

- [ ] **Step 1: Dispatch a fresh agent** (not the facts agent; facts skill, "After step 4.4") with only: the four entries as written in 1.1, their *Method*, `probes/fact_probes.py`, and `probes/claude-code-path-rules/test_claude_code_path_rules.py` as the form. Each file: module docstring as in the model (the docs are published without versions, so the watch reads the passages at the address, never the archived copy; no probe of behaviour, since a run of the tool takes credentials and a model), a class `<CamelCaseId>Watch(fact_probes.FactCheck)` with `def test_the_passages_stand(self):` whose body holds `# fact: <id>/1` and `self.watch_passages(IDENTIFIER)`. Whether WAY-08's deliberate break binds a fact's method stays the template's open question; the agent settles neither answer.

- [ ] **Step 2: Run each watch**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && for id in claude-code-project-skills claude-code-nested-skills codex-repository-skills codex-skill-paths; do python -B gate/run_tests.py probes/$id --record .runs/fact-$id.jsonl > $R/reports/check_1_2_watch_$id.txt 2>&1; echo "$id $?"; done
```
Expected: each `0` (1 test, OK). A skip ("no verdict: …") is a result to record, not a pass; a failure means a passage does not stand — back to 1.1.

