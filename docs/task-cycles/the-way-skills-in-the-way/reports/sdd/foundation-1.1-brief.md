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


#### 1.1 Facts agent — `record-environment-fact`

**Files:** Modify `foundations/environment_facts.md` only.

- [ ] **Step 1: Dispatch** with the skill `C:\Storage\repos\the-way-process\elements\environment-facts\skill\SKILL.md` and these entries (spec §7, WAY-76 one fact per entry; the agent may split an entry where WAY-76 asks and reports the new identifiers):
  - `claude-code-project-skills/1` — Claude Code loads project skills from `.claude/skills/` in the directory where it starts and in each parent up to the repository root, only up to the worktree root in a linked git worktree, and from v2.1.277 the main checkout's project skills when the worktree checkout has none at its root.
  - `claude-code-nested-skills/1` — Claude Code loads a nested `.claude/skills/` the first time it reads or edits a file in that subdirectory, keeps both skills when a nested skill's directory name matches another skill's name, and lists the directory-qualified variants with an instruction to invoke the one whose directory holds the files it is working on.
  - `codex-repository-skills/1` — Codex scans `.agents/skills` in every directory from its current working directory up to the repository root.
  - `codex-skill-paths/1` — Codex's initial list of skills includes each skill's file path.
  - Shape after `claude-code-path-rules/1`: *Holds for* "<tool>, whose documentation <site> publishes for its current release without versions"; *Source* `<address> (archived: <copy>, <date>) § <place> — "<passage>"; read <date>`; *Method* `python -B gate/run_tests.py probes/<id> --record .runs/fact-<id>.jsonl`.
  - Passages, as the planner read them on 2026-10-08 through `probes/fact_probes.py` (`page_runs`), each standing in one run of text. They hold the typographic apostrophe U+2019 (’), not `'`; a passage copied with `'` fails its watch:
    - https://code.claude.com/docs/en/skills: "Claude Code loads project skills from .claude/skills/ in the directory where you start it and in every parent directory up to the repository root" (start of a longer run; copy the sentence as the page ends it); "In a session running in a linked git worktree, Claude Code searches parent directories only up to the worktree root."; "On Claude Code v2.1.277 or later, when the worktree checkout has no .claude/skills directory at its root, Claude Code loads the main checkout’s project skills instead."; "They load the first time Claude reads or edits a file in that subdirectory and stay available for the rest of the session."; "When a nested skill’s directory name matches another skill’s name, both stay available."; "Claude Code also lists the directory-qualified variants for Claude, with an instruction to invoke the one whose directory holds the files it’s working on, so the nested skill still applies to work in apps/web/."
    - https://developers.openai.com/codex/skills (redirects to https://learn.chatgpt.com/docs/build-skills; archived http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills): "For repositories, Codex scans .agents/skills in every directory from your current working directory up to the repository root."; "In Codex, the initial list also includes each skill’s file path."
  - The agent re-reads each passage itself (skill step 4, mechanical check) and looks for the archived copy of the Claude Code page through the Wayback CDX index (skill step 3); where none is found, the entry says so as the template allows. Which of the two Codex addresses *Source* cites is its choice; the watch reads that address, so it must answer 200 with the passage.
  - Return to the orchestrator before writing if a passage does not stand word for word: `codex-skill-paths` carries the first product check in Codex (spec §4.2), so a changed passage changes the design.

- [ ] **Step 2: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none > $R/reports/check_1_1_guard_facts.txt 2>&1; echo $?; tail -3 $R/reports/check_1_1_guard_facts.txt; python -B -I .runs/stale_refs.py claude-code-project-skills claude-code-nested-skills codex-repository-skills codex-skill-paths
```
(`R=.runs/task-cycles/the-way-skills-in-the-way`.) Expected: exit 0, `0 error(s)`; warnings, if any, only for a new fact nothing names yet (WAY-73; the check of facts nothing names after the merge is unchecked with `--merge-onto none`, and 1.3 names all four); four fingerprints printed (none `NOT FOUND`); keep them for 1.3.

