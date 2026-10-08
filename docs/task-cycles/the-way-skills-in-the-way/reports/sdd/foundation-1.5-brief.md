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


#### 1.5 Invariants agent (sentence author) — `record-invariant`

**Files:** Modify `foundations/invariants.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\invariants\skill\SKILL.md` and:
  - **Fingerprint renewal** (WAY-31, N2): `repository-file-location`, `element-directory-contents`, `relation-model-directory-contents`, `invariant-example-target`, `map-example-target`, `glossary-example-target` carry `WAY-09@<new fingerprint>` in *Derives from*; each sentence is rechecked against WAY-09's new binding part and keeps its wording (spec §5.1); versions stay `/1` (the sentence, which the fingerprint covers, is unchanged).
  - **`outbound-link-reach/1`, edited in place (N3)**: sentence "No file git tracks contains a link into a repository that a reader not signed in to its host cannot open, or into a private note collection other than to the place of tasks that the `## Backlog` section of the root `AGENTS.md` names." (or a narrower equivalent the agent reports); *Derives from* `WAY-27@<new fingerprint>`; *Method* stays `TODO`. Version stays `/1`: WAY-57 compares with the commit the branch left the main branch from, and the-way has no main branch, so the comparison is unchecked with `--base none`; the request names the old and new sentence. The orchestrator's proposal for the request: a raise once `main` exists is not owed, because the entry is edited in place before `main` (`agent-instructions/README.md`).
  - **`skill-entry-points/1`, new (N5)**: one sentence, worded by this agent, that states every property its check will assert, because the check's author receives the sentence and the method only. It must state, for every `SKILL.md` that git tracks — or that stands untracked and not ignored — outside `.claude/` and `.agents/`, with `<name>` the name its frontmatter gives:
    1. a file `.claude/skills/the-way-<name>/SKILL.md` and a byte-identical `.agents/skills/the-way-<name>/SKILL.md` exist;
    2. their frontmatter names `the-way-<name>` and gives a description that starts with the skill's own description;
    3. their text names the skill's path, `--show-superproject-working-tree`, `git ls-files --stage -- ':/.the-way'` and `git rev-parse --show-toplevel`, holds the sentence "If the skill tells you to resolve a link to find the-way, skip that", and names, in backticks, the name of every such skill together with the words "with the `the-way-` prefix, never an unprefixed one";
    4. every directory `the-way-*` in `.claude/skills/` or `.agents/skills/` is the directory of such a skill.
    The literal strings in item 3 are the ones the generator writes (spec §4.2); they stand in the sentence so that the check's expected values come from the sentence (WAY-69). *Method* `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`; *Rests on* `none` (WAY-73: the four facts are reasons of WAY-127, not conditions of the sentence); *Derives from* `WAY-127@<fingerprint>` (N4); *Part* `every`; *Correction* `none`. The agent weighs the sentence against WAY-56's complying and violating pair and reports the result; splitting into two invariants is allowed only if the agent reports which one the flow names.
  - After step 4.4 the agent returns the instruction for the check (skill: "the entry, its method, and the checks citing an identifier this change retires or a version it raises" — none here) to the orchestrator.

- [ ] **Step 2: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none > $R/reports/check_1_5_guard_invariants.txt 2>&1; echo $?; grep -v "^unchecked" $R/reports/check_1_5_guard_invariants.txt; python -B -I .runs/stale_refs.py > $R/reports/check_1_5_stale_refs.txt; echo $?; tail -1 $R/reports/check_1_5_stale_refs.txt; python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none 2>&1 | tail -1
```
Expected: invariants guard exit 0, `0 error(s), 0 warning(s)` and the three baseline `unchecked` lines (among them "the fingerprints the links of the entries carry — --merge-onto none"); comparison exit 0, `references checked 378, stale 0` (372 at the base, plus WAY-127's four *Based on* facts and one relation, plus `skill-entry-points`' one *Derives from*; more only if 1.1 split a fact — then 372 plus every new `@` reference, and always `stale 0`); decisions guard `0 error(s)` (level-one-decision-invariants now holds for WAY-127).

