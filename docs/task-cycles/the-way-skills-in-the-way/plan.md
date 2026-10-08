# the-way's Skills in Sessions on the-way — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A Claude Code or Codex session started in a checkout or worktree of the-way sees every skill of the-way as the project skill `the-way-<name>`, reading the skill and the files it names from that same checkout or worktree, with a gate test that reports a skill the session would not see.

**Architecture:** A standard-library script `agent-instructions/skill_entry_points.py` generates two byte-identical tracked entry points per `SKILL.md` (`.claude/skills/the-way-<name>/SKILL.md`, `.agents/skills/the-way-<name>/SKILL.md`). A critical-flow test in `gate/`, written by an agent that never sees the generator, checks them on every change. The foundation step first writes the decision (WAY-127), its invariant (`skill-entry-points/1`), four environment facts with watches, the part-map changes and the edits of WAY-09 and WAY-27; then the skills' "where the-way lies" paragraphs, `AGENTS.md`, `README.md` and one installer sentence follow.

**Tech Stack:** Python 3.14 standard library, `unittest` through `gate/run_tests.py`, git 2.55 (Windows), Git Bash or Windows PowerShell 5.1.

**Spec:** `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md`, with the binding amendments N1–N5 of `reports/report_04_spec_recheck.md` (carried below). Frozen task: `frozen_task.md` beside the spec. Run brief: `reports/run_brief.md`.

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

## Review Focus

1. A skill whose frontmatter is not plain one-line YAML — a folded `description: >`, a byte-order mark before `---`, CRLF line ends — must stop the generator with a message naming the file, or be read correctly (CRLF), never produce an entry point with a broken or empty description. Pinned in Task 2 (`FrontmatterErrors`, `test_a_non_ascii_path_and_crlf_frontmatter_are_read`).
2. A skill added but not yet staged, a skill under `.claude/`/`.agents/` or an ignored directory such as `.runs/`, and a tracked `SKILL.md` deleted on disk: only the first counts as a skill. Pinned in Task 2 (`Discovery`).
3. A skill renamed or removed leaves an orphan `the-way-*` directory: the generator lists it with the `git rm -r` command and deletes nothing; the gate test reports it. Pinned in Task 2 (`test_an_orphan_directory_is_listed_and_kept`) and in the check brief of Task 1.7.
4. The generator run from another directory — a product's root, a subdirectory, a shell that moved by `cd` — writes only into the repository the script lies in. Pinned by the design (`ROOT` from `__file__`) and Task 2's tests, which pass `root=` explicitly.
5. A path with a space or non-ASCII letters (`git ls-files -z` hands raw UTF-8): read, sorted and named in the text unchanged. Pinned in Task 2 (`test_siblings_follow_the_order_of_paths_with_or_before_the_last`, `test_a_non_ascii_path_and_crlf_frontmatter_are_read`).

## File structure

| File | Part | Responsibility | Task |
|---|---|---|---|
| `foundations/environment_facts.md` (modify) | environment-facts | four new facts | 1.1 |
| `probes/claude-code-project-skills/test_claude_code_project_skills.py` (create) | environment-facts | watch | 1.2 |
| `probes/claude-code-nested-skills/test_claude_code_nested_skills.py` (create) | environment-facts | watch | 1.2 |
| `probes/codex-repository-skills/test_codex_repository_skills.py` (create) | environment-facts | watch | 1.2 |
| `probes/codex-skill-paths/test_codex_skill_paths.py` (create) | environment-facts | watch | 1.2 |
| `foundations/decisions.md` (modify) | decisions | WAY-09 edit, WAY-27 edit, WAY-127 new | 1.3 |
| `foundations/invariants.md` (modify) | invariants | six fingerprint renewals, `outbound-link-reach` edit, `skill-entry-points/1` new | 1.5 |
| `foundations/part_map.md` (modify) | part-map | `agent-instructions` changed, flow `skills-reach-the-way-sessions` new | 1.6 |
| `gate/test_skills_reach_the_way_sessions.py` (create) | gate | the flow test citing `skill-entry-points/1` | 1.7 |
| `agent-instructions/skill_entry_points.py` (create) | agent-instructions | the generator | 2 |
| `agent-instructions/test_skill_entry_points.py` (create) | agent-instructions | the generator's tests | 2, 3 |
| `.claude/skills/the-way-<name>/SKILL.md`, `.agents/skills/the-way-<name>/SKILL.md` (create, 22) | agent-instructions | generated entry points | 3 |
| nine `SKILL.md` files, `elements/common/way_of_working.md` (modify) | element parts, elements-common, project-level | where the-way lies | 4 |
| `AGENTS.md`, `README.md` (modify) | agent-instructions; left out on purpose | `## Skills`, `## Backlog`; "Using the skills" | 5 |
| `installation/install.py`, `installation/test_install.py` (modify) | installation | wrapper sentence and its test | 6 |
| `.runs/stale_refs.py` (create, ignored, not committed) | — | read-only fingerprint comparison (N2, N4) | 0 |

Dependency order: Task 0 → Task 1 (1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7 → 1.8) → Task 2 → Task 3 → Task 4 → Task 5 → Task 6 → Task 7. Tasks 4 and 5 depend only on Task 1 and Task 2's command name; they stay after Task 3 so that the gate is green before prose changes. Task 6 follows Task 4 because its sentence points to the paragraphs Task 4 writes.

---

### Task 0: Pre-flight (orchestrator)

**Files:**
- Create: `.runs/stale_refs.py` (ignored; a copy of the read-only script below)

- [ ] **Step 1: Check both roots and the worktree**

Run (Git Bash):
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git status --short && git rev-parse HEAD && git branch --show-current && git -C /c/Storage/repos/the-way-process rev-parse HEAD && git -C /c/Storage/repos/the-way-process status --short
```
Expected: no status lines; `c64a6071384fb57cdb9d7e9db4560ddc43e3b355` twice; `task/the-way-skills-in-the-way`.

- [ ] **Step 2: Write `.runs/stale_refs.py` with the Write tool**

```python
"""Read-only partial check: every `<WAY-n|fact>@<fingerprint>` in foundations/decisions.md and
foundations/invariants.md against the fingerprint the guards' parsers and relation-model give now.
Usage, from the root of the-way: python -B -I .runs/stale_refs.py [NAME ...]
NAME (WAY-127, claude-code-project-skills, skill-entry-points) prints that entry's current
fingerprint instead of comparing."""
import importlib.util, os, re, sys
root = os.getcwd()
for sub in ("relation-model", "elements/common"):
    sys.path.insert(0, os.path.join(root, sub))
from fingerprint import fingerprint


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(root, rel))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(rel):
    with open(os.path.join(root, rel), encoding="utf-8") as handle:
        return handle.read()


decisions_guard = load("decisions_guard", "elements/decisions/format_guard.py")
facts_guard = load("facts_guard", "elements/environment-facts/format_guard.py")
invariants_guard = load("invariants_guard", "elements/invariants/format_guard.py")
current = {}
for entry in decisions_guard.parse_log(read("foundations/decisions.md"), "WAY"):
    if getattr(entry, "kind", "version") == "version" and getattr(entry, "binding", None) is not None:
        key = "WAY-%02d" % entry.number
        if key not in current or current[key][0] < entry.version:
            current[key] = (entry.version, fingerprint(entry.binding))
current = {key: value[1] for key, value in current.items()}
parsed = facts_guard.parse_file(read("foundations/environment_facts.md"), facts_guard.read_rules())
for entry in (parsed[0] if isinstance(parsed, tuple) else parsed):
    if getattr(entry, "identifier", None) and getattr(entry, "sentence", None):
        current[entry.identifier] = facts_guard.entry_fingerprint(entry)
parsed = invariants_guard.parse_file(read("foundations/invariants.md"), invariants_guard.read_rules())
invariants = {getattr(entry, "identifier", None): fingerprint(entry.sentence)
              for entry in (parsed[0] if isinstance(parsed, tuple) else parsed)
              if getattr(entry, "identifier", None) and getattr(entry, "sentence", None)}
if len(sys.argv) > 1:
    for name in sys.argv[1:]:
        print("%s %s" % (name, current.get(name) or invariants.get(name) or "NOT FOUND"))
    sys.exit(0)
stale = checked = 0
for rel in ("foundations/decisions.md", "foundations/invariants.md"):
    for number, line in enumerate(read(rel).splitlines(), 1):
        for found in re.finditer(r"\b(WAY-\d+|[a-z0-9]+(?:-[a-z0-9]+)+)@([0-9a-f]{8})\b", line):
            name, carried = found.group(1), found.group(2)
            now = current.get(name)
            checked += 1
            if now != carried:
                stale += 1
                print("STALE %s:%d %s@%s now %s" % (rel, number, name, carried, now or "NOT FOUND"))
print("references checked %d, stale %d" % (checked, stale))
sys.exit(1 if stale else 0)
```

- [ ] **Step 3: Run it at the base, with its known values**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B -I .runs/stale_refs.py; python -B -I .runs/stale_refs.py WAY-09 WAY-27 WAY-44 claude-code-path-rules
```
Expected (verified by the planner on c64a607): `references checked 372, stale 0`, exit 0; then `WAY-09 b829b86a`, `WAY-27 770078ba`, `WAY-44 2f2b6227`, `claude-code-path-rules ac99f128` (the last equals the reference at `foundations/decisions.md:1428`, so the fact fingerprint matches the guard's). The planner also ran it on a copy with one word of WAY-09 changed: it printed six `STALE foundations/invariants.md:152…202 WAY-09@b829b86a` lines and exited 1, so it detects a stale reference.

Nothing to commit.

---

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

#### 1.2 Watch author — four watches

**Files:** Create `probes/<id>/test_<id_with_underscores>.py` for the four identifiers.

- [ ] **Step 1: Dispatch a fresh agent** (not the facts agent; facts skill, "After step 4.4") with only: the four entries as written in 1.1, their *Method*, `probes/fact_probes.py`, and `probes/claude-code-path-rules/test_claude_code_path_rules.py` as the form. Each file: module docstring as in the model (the docs are published without versions, so the watch reads the passages at the address, never the archived copy; no probe of behaviour, since a run of the tool takes credentials and a model), a class `<CamelCaseId>Watch(fact_probes.FactCheck)` with `def test_the_passages_stand(self):` whose body holds `# fact: <id>/1` and `self.watch_passages(IDENTIFIER)`. Whether WAY-08's deliberate break binds a fact's method stays the template's open question; the agent settles neither answer.

- [ ] **Step 2: Run each watch**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && for id in claude-code-project-skills claude-code-nested-skills codex-repository-skills codex-skill-paths; do python -B gate/run_tests.py probes/$id --record .runs/fact-$id.jsonl > $R/reports/check_1_2_watch_$id.txt 2>&1; echo "$id $?"; done
```
Expected: each `0` (1 test, OK). A skip ("no verdict: …") is a result to record, not a pass; a failure means a passage does not stand — back to 1.1.

#### 1.3 Decisions agent — `record-decision`

**Files:** Modify `foundations/decisions.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\decisions\skill\SKILL.md` and:
  - **WAY-09/1, edit in place [change of meaning — question 1 of the request].** In the first binding sentence, "the root agent instruction files, which the map gives to `agent-instructions` (WAY-44)" becomes "the root agent instruction files and the project skill entry points under `.claude/skills/` and `.agents/skills/`, which the map gives to `agent-instructions` (WAY-44)" (spec §5.1). *Verification* gains a "complies" example for the entry points standing at the root as files of `agent-instructions`. *Approved by* `Mariusz, merge of <request link>`. *Review when* stays `none`. The search also answers whether the sentence on what `agent-instructions/` holds ("the instructions for agents working on this repository, led to from the root agent instruction files") admits the generator and its test there, and returns a finding either way.
  - **WAY-27/1, edit in place [change of meaning — question 2 of the request].** The binding sentence gains the exception: "Nothing in this repository points to a source outside it that its readers cannot reach, except the place of its tasks that the `## Backlog` section of its root `AGENTS.md` names: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to." (spec §5.2). *Rationale* gains the clause: a backlog place is where work is kept, not reasoning an entry rests on, and WAY-107 sends an agent there. *Verification* gains a "complies" example: the-way's root `AGENTS.md` names, in `## Backlog`, the private note where its tasks are kept. *Approved by* `Mariusz, merge of <request link>` (it was `Mariusz, 2026-09-16`). *Review when* stays `none`.
  - **WAY-127/1, new decision** — question: how does a session working on the-way itself reach the-way's skills? Content (spec §7, §3): a session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`; an entry point reads its skill and the files it names from the checkout or worktree the session was started in, stops itself in a product, and hands another the-way skill on under the `the-way-` prefix; no global link reaches a skill of the-way and the-way is not installed in itself. One to three binding sentences (template). *Change* new decision. *Scope* `agent-instructions, elements-common, project-level, task-cycle, decisions, invariants, glossary, part-map, environment-facts, installation`. *Based on* the four facts of 1.1 as `<id>@<fingerprint>` joined by ` · ` (fingerprints from 1.1 step 2; N4). *Relations* `derives from WAY-44@2f2b6227` (N4). *Verification* `level 1 — invariants: skill-entry-points. Level 2 for the paragraphs of the skills that say where the-way lies` with a complies and a violates example. *Review when* `none` (the tools' behaviour it rests on is watched through the four facts; no waited-for state). *Origin* `none`. *Approved by* `Mariusz, merge of <request link>`. *Rationale*; *Rejected*: B (installer mode without a pin — its files would belong to `installation`, outside `installation/`; its trust boundary grows), C (untracked per-checkout files — a fresh worktree or cloud session has none), D (global or per-worktree links, git symlinks — read another branch; need `core.symlinks` and rights on Windows), unprefixed names (a personal skill wins over a project one in Claude Code). Number 127 is provisional against other open branches.
  - Entries the search must read whole besides those the skill leads to: WAY-07, WAY-14, WAY-22, WAY-25, WAY-30, WAY-31, WAY-33, WAY-34, WAY-38, WAY-44, WAY-45, WAY-52, WAY-53, WAY-55, WAY-57, WAY-69, WAY-73, WAY-76, WAY-90, WAY-97, WAY-101, WAY-107, WAY-125, WAY-126. It also states whether "entry point" (already in WAY-09's *Verification*: "root entry points") uses the glossary term `entry` in another meaning (WAY-97); provisional answer: no — a fixed compound of the field, not a use of `entry` — unless the search shows otherwise, in which case it returns the finding to the orchestrator before writing (a glossary change goes through `C:\Storage\repos\the-way-process\elements\glossary\skill\SKILL.md` in a further dispatch, and a carrier may not hold the word `entry`).

- [ ] **Step 2: Orchestrator check — guard and the positive control of the fingerprint comparison**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none > $R/reports/check_1_3_guard_decisions.txt 2>&1; echo $?; grep -v "^unchecked" $R/reports/check_1_3_guard_decisions.txt; python -B -I .runs/stale_refs.py > $R/reports/check_1_3_stale_refs.txt; echo $?; cat $R/reports/check_1_3_stale_refs.txt; python -B -I .runs/stale_refs.py WAY-09 WAY-27 WAY-127
```
Expected: guard exit 0, `0 error(s)`; warnings: the five baseline overdue reviews (WAY-03, WAY-21, WAY-52, WAY-55, WAY-69) and the merge-placeholder warning for WAY-09, WAY-27 and WAY-127, nothing else. The comparison (`references checked 377` without a split fact) exits 1 with exactly seven `STALE` lines: six `foundations/invariants.md:152…202 WAY-09@b829b86a` and one `foundations/invariants.md:473 WAY-27@770078ba` — the references 1.5 renews; any other line is a defect of 1.3. The last command prints three fingerprints, none `NOT FOUND`, and WAY-09/WAY-27 differ from `b829b86a`/`770078ba`.

#### 1.4 Orchestrator — answers before the invariants agent

- [ ] **Step 1:** Record in `cycle.md` the questions 1.1–1.3 returned and the provisional answers, the WAY-33 findings and how each was settled, and the Polish meaning sentences. If the decisions agent found that "entry point" collides with `entry`, dispatch the glossary agent now and rerun the glossary guard (1.8 step 1) before 1.5.

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

#### 1.6 Part-map agent — `update-part-map`

**Files:** Modify `foundations/part_map.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\part-map\skill\SKILL.md` and (spec §7):
  - **`agent-instructions`, changed**: responsibility adds the project skill entry points that make the-way's skills visible to sessions on it; *Files* add `.claude/skills/**` and `.agents/skills/**`; *Depends on* adds `project-level · task-cycle`; *Failure modes* add "a skill of the-way has no entry point, or a stale one — a session on the-way uses a personal skill of that name or none — high — detected by skill-entry-points" and "the-way's own entry point, loaded from a product's `.the-way`, is followed instead of the product's, where the agent knows neither the entry point's path nor the session's start directory (Claude Code's documentation states neither is given to the agent) — a product entry is written against the-way's own foundation — high — not detected".
  - **Critical flow `skills-reach-the-way-sessions`, new**: someone adds, renames or moves a skill of the-way, or changes its description, and a session on the-way that would not find it under its `the-way-` name is reported before the change reaches the main branch. *Criticality* high; *Parts* `agent-instructions · elements-common · decisions · invariants · glossary · part-map · environment-facts · project-level · task-cycle · gate`; *Invariant* `skill-entry-points`; *Coverage* `none`.
  - The search also answers whether `gate` needs a dependency for its new test, which reads other parts' files but imports none of their code, and returns the finding.

- [ ] **Step 2: Orchestrator check** — deferred to 1.8 (the guard needs the flow's test, which 1.7 writes).

#### 1.7 Check author — the flow test (WAY-69)

**Files:** Create `gate/test_skills_reach_the_way_sessions.py` only.

- [ ] **Step 1: Dispatch a fresh agent** that wrote neither the sentence nor any code it covers, and that receives only:
  - the entry `skill-entry-points/1` as 1.5 wrote it (sentence, method, links), and the flow entry `skills-reach-the-way-sessions` as 1.6 wrote it;
  - the "Test" section of `C:\Storage\repos\the-way-process\elements\invariants\template.md` and WAY-69's binding sentences;
  - the docstring of `gate/run_tests.py` (citation form) and `gate/test_wording_reaches_dependants.py` as the form of a flow test;
  - this brief: a file `gate/test_skills_reach_the_way_sessions.py` with the line `# flow: skills-reach-the-way-sessions` at the top; `ROOT` the repository the file lies in; it imports nothing from `agent-instructions/` and nothing that computes entry points; it finds the population the sentence names with its own `git ls-files -z --cached --others --exclude-standard -- ':(glob)**/SKILL.md'` run in the root it checks, and reads each skill's name and description from its `SKILL.md`; every value it expects is written out in the test, taken from the sentence; text is compared with runs of whitespace collapsed to one space; a function `problems(root) -> list[str]` returns one line per property of the sentence that fails, naming the file; `test_every_skill_reaches_a_session_on_the_way` holds `# invariant: skill-entry-points/1` alone on its line inside the method, asserts `problems(ROOT) == []` with a failure message that names `python -B agent-instructions/skill_entry_points.py --write`, and, as a positive control, asserts that discovery found `elements/decisions/skill/SKILL.md` and `task-cycle/skill/SKILL.md`; `test_problems_reports_a_skill_the_session_does_not_see` cites nothing and, on a temporary `git init` repository with no commit, shows that `problems()` reports a skill with no entry points, a skill with only the `.claude` one, two copies that differ in bytes, and an orphan `the-way-*` directory.
  - It never receives `spec.md` §4.1–§4.3, this plan's Tasks 2–3, or any generator code. Its questions go to the orchestrator, who answers from the sentence only; a question the sentence cannot answer returns to 1.5.

- [ ] **Step 2: Run it (expected red until Task 3)**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > $R/reports/check_1_7_gate.txt 2>&1; echo $?; grep -E "^(FAIL|ERROR|Ran|OK|FAILED)" $R/reports/check_1_7_gate.txt
```
Expected: exit 1; the 96 baseline tests pass; the control test passes; `test_every_skill_reaches_a_session_on_the_way` FAILS with problems naming missing entry points and the generator command (no entry points exist yet); in `.runs/gate-tests.jsonl` a `fail` line for `skill-entry-points/1`. An ERROR (import, syntax) or a passing citing test is a defect of 1.7.

#### 1.8 Foundation checks, search record, commits

- [ ] **Step 1: Run every guard of the changed foundation files and the element tests**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git add foundations/decisions.md foundations/invariants.md foundations/part_map.md foundations/environment_facts.md gate/test_skills_reach_the_way_sessions.py probes/claude-code-project-skills probes/claude-code-nested-skills probes/codex-repository-skills probes/codex-skill-paths && \
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none > $R/reports/check_1_8_guard_decisions.txt 2>&1; echo "decisions $?"; \
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none > $R/reports/check_1_8_guard_invariants.txt 2>&1; echo "invariants $?"; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none > $R/reports/check_1_8_guard_part_map.txt 2>&1; echo "part-map $?"; \
python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none > $R/reports/check_1_8_guard_facts.txt 2>&1; echo "facts $?"; \
python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none > $R/reports/check_1_8_guard_glossary.txt 2>&1; echo "glossary $?"; \
python -B -I .runs/stale_refs.py > $R/reports/check_1_8_stale_refs.txt; echo "stale $?"; \
for d in elements/decisions elements/invariants elements/part-map elements/environment-facts elements/glossary; do python -B gate/run_tests.py $d > $R/reports/check_1_8_tests_$(basename $d).txt 2>&1; echo "$d $?"; done
```
(The guards read the flow's test from git's index, so the files are staged first.) Expected:
- decisions `0`: `0 error(s)`, warnings as in 1.3 step 2;
- invariants `0`: `0 error(s), 0 warning(s)`;
- part-map `1`: exactly two errors, `pattern `.claude/skills/**` of `agent-instructions` matches no file git tracks` and the same for `.agents/skills/**` (the planner reproduced both on a copy) — accepted until Task 3, recorded as such; any other error is a defect of 1.6;
- facts `0`: `0 error(s), 0 warning(s)` (every new fact is named by WAY-127's *Based on*);
- glossary `0`: `0 error(s)`;
- stale `0`: `stale 0`;
- each element test directory `0`.

- [ ] **Step 2: Record** in `cycle.md`: the WAY-33 searches of 1.1, 1.3, 1.5, 1.6 (and glossary if run) with how each finding was settled, the Polish meaning sentence of each entry, the partial checks above and what they leave unchecked (Task 7, "Unchecked").

- [ ] **Step 3: Commit in three commits**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "feat(foundations): Reach the-way's skills in sessions on the-way through generated project skill entry points" -- foundations/decisions.md foundations/invariants.md foundations/part_map.md foundations/environment_facts.md && \
git commit -m "test(environment-facts): Watch how Claude Code and Codex find project skills" -- probes/claude-code-project-skills probes/claude-code-nested-skills probes/codex-repository-skills probes/codex-skill-paths && \
git commit -m "test(gate): Report a skill a session on the-way would not see" -- gate/test_skills_reach_the_way_sessions.py && git status --short && git log --oneline -3
```
Expected: three commits; empty status. From here `gate/test_skills_reach_the_way_sessions.py` is read-only for every later task (WAY-03); a task that needs it changed stops and returns to the foundation step.

---

### Task 2: Generator and its tests (`agent-instructions`)

**Files:**
- Create: `agent-instructions/skill_entry_points.py`
- Create: `agent-instructions/test_skill_entry_points.py`

**Interfaces:**
- Consumes: nothing from earlier tasks (it does not read the gate's test, and the gate's test does not import it).
- Produces: `ROOT: Path`; `ENTRY_DIRECTORIES = (".claude/skills", ".agents/skills")`; `PREFIX = "the-way-"`; `class GeneratorError(Exception)`; `@dataclass(frozen=True) class Skill(path: str, name: str, description: str)`; `discover(root: Path) -> list[Skill]` (sorted by path); `sibling_names(skills: list[Skill]) -> str`; `entry_point_text(skill: Skill, skills: list[Skill]) -> str`; `produce(skills: list[Skill]) -> dict[str, str]` (path from root → text); `orphans(root: Path, skills: list[Skill]) -> list[str]`; `main(argv: list[str] | None = None, root: Path = ROOT) -> int`. Output lines: `would create|would change <path>`, `created|changed <path>`, `orphan <dir>: no skill produces it; remove it with git rm -r -- <dir>`, `entry points are current`; errors `Error: <message>` on stderr, exit 1.

The planner ran this code and these tests in a scratch copy of the repository (11 tests OK; the generator produced 22 files, byte-identical pairs, and a rerun printed `entry points are current`).

- [ ] **Step 1: Write the failing tests** — create `agent-instructions/test_skill_entry_points.py`:

```python
"""Tests of the generator of the project skill entry points (WAY-127).

The expected texts are written out on purpose: a test that built them with the generator's own
functions would pass whatever those functions produce.

Run from the root of the-way: python -B gate/run_tests.py agent-instructions
"""

from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import skill_entry_points as generator  # noqa: E402

CRITIQUE = ("---\nname: critique\ndescription: Use when a proposal needs a second reader.\n---\n\n"
            "# Critique\n")
DECISION = ("---\nname: record-decision\ndescription: Use when a decision has to be written.\n"
            "---\n\n# Record a decision\n")

# The entry point of `record-decision` beside `critique`, written out in full.
DECISION_ENTRY = (
    "---\n"
    "name: the-way-record-decision\n"
    "description: Use when a decision has to be written. Use this checkout's own the-way.\n"
    "---\n"
    "\n"
    "# the-way-record-decision\n"
    "\n"
    "This entry point serves a session that works on the-way itself. Stop following it, and use "
    "the product's own project skill `the-way-record-decision`, if either check shows a "
    "product:\n"
    "\n"
    "- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` "
    "prints a path: this file lies in a product's `.the-way` submodule;\n"
    "- `git ls-files --stage -- ':/.the-way'`, run in the directory the session was started in, "
    "prints a line: the session works in a product that pins the-way.\n"
    "\n"
    "The process root is the checkout or worktree the session was started in: the directory "
    "`git rev-parse --show-toplevel` prints when run in the session's start directory, not in the "
    "shell's current directory, which moves. Read `elements/decisions/skill/SKILL.md` there in "
    "full and follow it, and read the files it names under the same root, never a copy in "
    "another checkout or worktree. If the skill tells you to resolve a link to find the-way, skip "
    "that: the root is the one above. Do not substitute a global skill.\n"
    "\n"
    "Where this skill or a file it reads names another the-way skill — `critique` or "
    "`record-decision` — use this repository's project skill of the same name with the "
    "`the-way-` prefix, never an unprefixed one.\n")


class Repository:
    """A temporary git repository with no commit; untracked files count as skills."""

    def __init__(self, test: unittest.TestCase) -> None:
        directory = tempfile.TemporaryDirectory(prefix="the-way-entry-points-")
        test.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def run(self, *arguments: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = generator.main(list(arguments), root=self.root)
        return code, out.getvalue(), err.getvalue()

    def files(self) -> dict[str, bytes]:
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*")
                if path.is_file() and ".git" not in path.relative_to(self.root).parts}


class EntryPointText(unittest.TestCase):
    def test_text_is_the_written_out_form(self) -> None:
        skills = [generator.Skill("elements/common/critique/SKILL.md", "critique",
                                  "Use when a proposal needs a second reader."),
                  generator.Skill("elements/decisions/skill/SKILL.md", "record-decision",
                                  "Use when a decision has to be written.")]
        self.assertEqual(generator.entry_point_text(skills[1], skills), DECISION_ENTRY)

    def test_one_skill_names_itself_alone(self) -> None:
        skill = generator.Skill("a/SKILL.md", "alpha", "Use for alpha.")
        self.assertIn("another the-way skill — `alpha` — use", generator.entry_point_text(
            skill, [skill]))

    def test_siblings_follow_the_order_of_paths_with_or_before_the_last(self) -> None:
        repository = Repository(self)
        repository.write("zeta/SKILL.md", "---\nname: alpha\ndescription: Use for alpha.\n---\n")
        repository.write("beta/SKILL.md", "---\nname: zulu\ndescription: Use for zulu.\n---\n")
        repository.write("dir with space/SKILL.md",
                         "---\nname: mike\ndescription: Use for mike.\n---\n")
        skills = generator.discover(repository.root)
        self.assertEqual([skill.path for skill in skills],
                         ["beta/SKILL.md", "dir with space/SKILL.md", "zeta/SKILL.md"])
        self.assertEqual(generator.sibling_names(skills), "`zulu`, `mike` or `alpha`")


class Discovery(unittest.TestCase):
    def test_skills_under_the_entry_directories_and_ignored_ones_are_not_skills(self) -> None:
        repository = Repository(self)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        repository.write(".claude/skills/own/SKILL.md", CRITIQUE)
        repository.write(".agents/skills/own/SKILL.md", CRITIQUE)
        repository.write(".gitignore", ".runs/\n")
        repository.write(".runs/copy/SKILL.md", CRITIQUE)
        self.assertEqual([skill.path for skill in generator.discover(repository.root)],
                         ["elements/decisions/skill/SKILL.md"])

    def test_a_tracked_skill_deleted_on_disk_is_not_a_skill(self) -> None:
        repository = Repository(self)
        repository.write("gone/SKILL.md", CRITIQUE)
        subprocess.run(["git", "-C", str(repository.root), "add", "gone/SKILL.md"], check=True,
                       capture_output=True)
        (repository.root / "gone" / "SKILL.md").unlink()
        self.assertEqual(generator.discover(repository.root), [])

    def test_a_non_ascii_path_and_crlf_frontmatter_are_read(self) -> None:
        repository = Repository(self)
        repository.write("zażółć/SKILL.md",
                         "---\r\nname: alpha\r\ndescription: Use for alpha.\r\n---\r\n")
        self.assertEqual(generator.discover(repository.root),
                         [generator.Skill("zażółć/SKILL.md", "alpha", "Use for alpha.")])


class FrontmatterErrors(unittest.TestCase):
    CASES = (
        ("no frontmatter", "# A skill\n",
         "Error: a/SKILL.md: no frontmatter between the first two '---' lines\n"),
        ("unclosed frontmatter", "---\nname: alpha\ndescription: Use for alpha.\n",
         "Error: a/SKILL.md: no frontmatter between the first two '---' lines\n"),
        ("byte order mark", "\ufeff---\nname: alpha\ndescription: Use for alpha.\n---\n",
         "Error: a/SKILL.md: no frontmatter between the first two '---' lines\n"),
        ("no name", "---\ndescription: Use for alpha.\n---\n",
         "Error: a/SKILL.md: frontmatter has no 'name:' with a value\n"),
        ("empty name", "---\nname:\ndescription: Use for alpha.\n---\n",
         "Error: a/SKILL.md: frontmatter has no 'name:' with a value\n"),
        ("no description", "---\nname: alpha\n---\n",
         "Error: a/SKILL.md: frontmatter has no 'description:' with a value\n"),
        ("folded description", "---\nname: alpha\ndescription: >\n  Use for alpha.\n---\n",
         "Error: a/SKILL.md: description is not on one line\n"),
        ("name off the form", "---\nname: Record_Decision\ndescription: Use for it.\n---\n",
         "Error: a/SKILL.md: name 'Record_Decision' is not lowercase words joined by hyphens\n"),
        ("name with the prefix", "---\nname: the-way-alpha\ndescription: Use for it.\n---\n",
         "Error: a/SKILL.md: name 'the-way-alpha' already starts with 'the-way-'\n"),
    )

    def test_each_error_stops_with_its_message_and_writes_nothing(self) -> None:
        for label, text, message in self.CASES:
            with self.subTest(label):
                repository = Repository(self)
                repository.write("a/SKILL.md", text)
                repository.write("b/SKILL.md", DECISION)
                before = repository.files()
                self.assertEqual(repository.run("--write"), (1, "", message))
                self.assertEqual(repository.files(), before)

    def test_a_name_two_skills_hold_stops_and_writes_nothing(self) -> None:
        repository = Repository(self)
        repository.write("a/SKILL.md", DECISION)
        repository.write("b/SKILL.md", DECISION)
        before = repository.files()
        self.assertEqual(repository.run("--write"), (
            1, "", "Error: name 'record-decision' is held by both a/SKILL.md and b/SKILL.md\n"))
        self.assertEqual(repository.files(), before)


class Writing(unittest.TestCase):
    def test_write_creates_both_copies_and_a_rerun_finds_them_current(self) -> None:
        repository = Repository(self)
        repository.write("elements/common/critique/SKILL.md", CRITIQUE)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        sources = repository.files()
        code, out, err = repository.run("--write")
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out, "created .claude/skills/the-way-critique/SKILL.md\n"
                              "created .agents/skills/the-way-critique/SKILL.md\n"
                              "created .claude/skills/the-way-record-decision/SKILL.md\n"
                              "created .agents/skills/the-way-record-decision/SKILL.md\n")
        written = {path: data for path, data in repository.files().items() if path not in sources}
        self.assertEqual(set(written), {".claude/skills/the-way-critique/SKILL.md",
                                        ".agents/skills/the-way-critique/SKILL.md",
                                        ".claude/skills/the-way-record-decision/SKILL.md",
                                        ".agents/skills/the-way-record-decision/SKILL.md"})
        self.assertEqual(written[".claude/skills/the-way-record-decision/SKILL.md"],
                         DECISION_ENTRY.encode("utf-8"))
        self.assertEqual(written[".agents/skills/the-way-record-decision/SKILL.md"],
                         DECISION_ENTRY.encode("utf-8"))
        self.assertEqual(written[".claude/skills/the-way-critique/SKILL.md"],
                         written[".agents/skills/the-way-critique/SKILL.md"])
        self.assertEqual(repository.run("--write"), (0, "entry points are current\n", ""))

    def test_without_write_it_lists_the_plan_and_writes_nothing(self) -> None:
        repository = Repository(self)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        repository.write(".claude/skills/the-way-record-decision/SKILL.md", "stale\n")
        before = repository.files()
        self.assertEqual(repository.run(), (
            0, "would change .claude/skills/the-way-record-decision/SKILL.md\n"
               "would create .agents/skills/the-way-record-decision/SKILL.md\n", ""))
        self.assertEqual(repository.files(), before)

    def test_an_orphan_directory_is_listed_and_kept(self) -> None:
        repository = Repository(self)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        repository.run("--write")
        repository.write(".agents/skills/the-way-renamed/SKILL.md", "old\n")
        repository.write(".claude/skills/someone-elses/SKILL.md", "theirs\n")
        self.assertEqual(repository.run("--write"), (
            0, "orphan .agents/skills/the-way-renamed: no skill produces it; remove it with "
               "git rm -r -- .agents/skills/the-way-renamed\n", ""))
        self.assertEqual((repository.root / ".agents/skills/the-way-renamed/SKILL.md").read_bytes(),
                         b"old\n")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to see them fail**

Run: `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions`
Expected: exit 1, `ImportError: Failed to import test module: test_skill_entry_points` caused by `ModuleNotFoundError: No module named 'skill_entry_points'`.

- [ ] **Step 3: Write the generator** — create `agent-instructions/skill_entry_points.py`:

```python
"""Generator of the project skill entry points through which a session working on the-way itself
reaches the-way's own skills (WAY-127).

Usage, from the root of the-way:

    python -B agent-instructions/skill_entry_points.py [--write]

A skill of the-way is a file `SKILL.md` that `git ls-files --cached --others --exclude-standard`
lists in this repository outside `.claude/` and `.agents/`, and that exists on disk. From its
frontmatter the generator takes `name:` and `description:`, each on one line, and produces
`.claude/skills/the-way-<name>/SKILL.md` for Claude Code and a byte-identical
`.agents/skills/the-way-<name>/SKILL.md` for Codex. The repository is the one this script lies in,
whatever the current directory, so a run from a product's `.the-way` writes nothing into the
product.

Without --write the generator prints what it would create or change and writes nothing; with
--write it writes those files, UTF-8 with LF line ends. Either way it prints each directory
`the-way-*` under `.claude/skills/` or `.agents/skills/` that no skill produces, for the author to
remove with `git rm -r`; it deletes nothing. A malformed frontmatter, a name two skills hold, or a
failed git call stops the run before anything is written.

Exit code: 0 on success; 1 with `Error: <message>` on stderr otherwise.

Standard library only; the only program started is git.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRY_DIRECTORIES = (".claude/skills", ".agents/skills")
PREFIX = "the-way-"
SUFFIX = " Use this checkout's own the-way."
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
BLOCK_SCALAR = re.compile(r"[|>][-+0-9]*")
FIELD = re.compile(r"(name|description):(.*)")


class GeneratorError(Exception):
    """A skill or the repository keeps the entry points from being produced."""


@dataclass(frozen=True)
class Skill:
    path: str          # from the repository root, with `/`, e.g. "task-cycle/skill/SKILL.md"
    name: str          # e.g. "implement-task"
    description: str   # the frontmatter's one-line description, as written


def git(root: Path, *arguments: str) -> bytes:
    try:
        completed = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True,
                                   check=False)
    except OSError as error:
        raise GeneratorError(f"git cannot run: {error}") from error
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", "replace").strip()
        raise GeneratorError(f"git {' '.join(arguments)} failed: {message}")
    return completed.stdout


def skill_paths(root: Path) -> list[str]:
    """Every skill's path, sorted, as git lists it: tracked or untracked and not ignored, outside
    `.claude/` and `.agents/`, and present on disk."""
    listed = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--",
                 ":(glob)**/SKILL.md")
    paths = set()
    for raw in listed.split(b"\0"):
        if not raw:
            continue
        try:
            path = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise GeneratorError(f"a path git lists is not UTF-8: {raw!r}") from error
        if path.startswith((".claude/", ".agents/")):
            continue
        if (root / path).is_file():
            paths.add(path)
    return sorted(paths)


def frontmatter(path: str, text: str) -> dict[str, str]:
    """The first `name:` and `description:` between the file's first two `---` lines."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise GeneratorError(f"{path}: no frontmatter between the first two '---' lines")
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if end is None:
        raise GeneratorError(f"{path}: no frontmatter between the first two '---' lines")
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        found = FIELD.fullmatch(line)
        if found and found.group(1) not in fields:
            fields[found.group(1)] = found.group(2).strip()
    return fields


def read_skill(root: Path, path: str) -> Skill:
    try:
        text = (root / path).read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise GeneratorError(f"{path}: not UTF-8") from error
    fields = frontmatter(path, text)
    for field in ("name", "description"):
        value = fields.get(field, "")
        if not value:
            raise GeneratorError(f"{path}: frontmatter has no '{field}:' with a value")
        if BLOCK_SCALAR.fullmatch(value):
            raise GeneratorError(f"{path}: {field} is not on one line")
    name = fields["name"]
    if not NAME.fullmatch(name):
        raise GeneratorError(f"{path}: name '{name}' is not lowercase words joined by hyphens")
    if name.startswith(PREFIX):
        raise GeneratorError(f"{path}: name '{name}' already starts with '{PREFIX}'")
    return Skill(path, name, fields["description"])


def discover(root: Path) -> list[Skill]:
    """Every skill of the repository at `root`, sorted by path."""
    skills: list[Skill] = []
    holders: dict[str, str] = {}
    for path in skill_paths(root):
        skill = read_skill(root, path)
        if skill.name in holders:
            raise GeneratorError(f"name '{skill.name}' is held by both {holders[skill.name]} and "
                                 f"{path}")
        holders[skill.name] = path
        skills.append(skill)
    return skills


def sibling_names(skills: list[Skill]) -> str:
    """The backticked names of all skills in their order, joined with `, ` and ` or `."""
    names = [f"`{skill.name}`" for skill in skills]
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " or " + names[-1]


def entry_point_text(skill: Skill, skills: list[Skill]) -> str:
    """The text of both entry points of `skill`; each paragraph and list item is one line."""
    name = PREFIX + skill.name
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {skill.description}{SUFFIX}\n"
        "---\n"
        "\n"
        f"# {name}\n"
        "\n"
        "This entry point serves a session that works on the-way itself. Stop following it, and "
        f"use the product's own project skill `{name}`, if either check shows a product:\n"
        "\n"
        "- `git -C <the directory that holds this file> rev-parse "
        "--show-superproject-working-tree` prints a path: this file lies in a product's "
        "`.the-way` submodule;\n"
        "- `git ls-files --stage -- ':/.the-way'`, run in the directory the session was started "
        "in, prints a line: the session works in a product that pins the-way.\n"
        "\n"
        "The process root is the checkout or worktree the session was started in: the directory "
        "`git rev-parse --show-toplevel` prints when run in the session's start directory, not in "
        "the shell's current directory, which moves. "
        f"Read `{skill.path}` there in full and follow it, and read the files it names under the "
        "same root, never a copy in another checkout or worktree. If the skill tells you to "
        "resolve a link to find the-way, skip that: the root is the one above. Do not substitute "
        "a global skill.\n"
        "\n"
        "Where this skill or a file it reads names another the-way skill — "
        f"{sibling_names(skills)} — use this repository's project skill of the same name with the "
        "`the-way-` prefix, never an unprefixed one.\n")


def produce(skills: list[Skill]) -> dict[str, str]:
    """Path from the repository root -> text, two entry points per skill, in skill order."""
    produced: dict[str, str] = {}
    for skill in skills:
        text = entry_point_text(skill, skills)
        for directory in ENTRY_DIRECTORIES:
            produced[f"{directory}/{PREFIX}{skill.name}/SKILL.md"] = text
    return produced


def orphans(root: Path, skills: list[Skill]) -> list[str]:
    """Every directory `the-way-*` under either skills directory that no skill produces."""
    names = {PREFIX + skill.name for skill in skills}
    found = []
    for directory in ENTRY_DIRECTORIES:
        base = root / directory
        if not base.is_dir():
            continue
        for child in sorted(base.iterdir(), key=lambda entry: entry.name):
            if child.is_dir() and child.name.startswith(PREFIX) and child.name not in names:
                found.append(f"{directory}/{child.name}")
    return found


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the project skill entry points of the-way's own skills.")
    parser.add_argument("--write", action="store_true",
                        help="write the entry points; without it, print what would change")
    arguments = parser.parse_args(argv)
    try:
        skills = discover(root)
        changes = []
        for relative, text in produce(skills).items():
            target = root / relative
            data = text.encode("utf-8")
            if not target.is_file():
                changes.append(("create", relative, target, data))
            elif target.read_bytes() != data:
                changes.append(("change", relative, target, data))
        left = orphans(root, skills)
        for kind, relative, target, data in changes:
            if arguments.write:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                print(f"{kind}d {relative}")
            else:
                print(f"would {kind} {relative}")
        for directory in left:
            print(f"orphan {directory}: no skill produces it; remove it with "
                  f"git rm -r -- {directory}")
        if not changes and not left:
            print("entry points are current")
        return 0
    except (GeneratorError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

The text of each paragraph is one line (no hard wraps), so no literal phrase of the entry point is split by a line break.

- [ ] **Step 4: Run the tests to see them pass, and a dry run on the repository**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions > $R/reports/check_2_tests_agent_instructions.txt 2>&1; echo $?; tail -3 $R/reports/check_2_tests_agent_instructions.txt; python -B agent-instructions/skill_entry_points.py | head -3; git status --short
```
Expected: exit 0, `Ran 11 tests`, `OK`; the dry run prints `would create .claude/skills/the-way-critique/SKILL.md` first (22 `would create` lines in all); status shows only the two new files (`??`): the dry run wrote nothing.

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git add agent-instructions/skill_entry_points.py agent-instructions/test_skill_entry_points.py && git commit -m "feat(agent-instructions): Generate the project skill entry points of the-way's skills"
```

---

### Task 3: Generated entry points and their derived equality

**Files:**
- Create: 22 files `.claude/skills/the-way-<name>/SKILL.md`, `.agents/skills/the-way-<name>/SKILL.md` (by the generator)
- Modify: `agent-instructions/test_skill_entry_points.py` (add `TrackedEntryPoints` before `if __name__`)

**Interfaces:**
- Consumes: `generator.discover`, `generator.produce`, `generator.orphans`, `ROOT` from Task 2.
- Produces: the tracked entry points that `gate/test_skills_reach_the_way_sessions.py` and `foundations/part_map.md`'s patterns need.

- [ ] **Step 1: Write the failing test** — insert into `agent-instructions/test_skill_entry_points.py`, before `if __name__ == "__main__":`:

```python
class TrackedEntryPoints(unittest.TestCase):
    def test_the_tracked_entry_points_are_what_the_generator_produces(self) -> None:
        skills = generator.discover(ROOT)
        produced = generator.produce(skills)
        listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--", ".claude/skills",
                                 ".agents/skills"], check=True, capture_output=True).stdout
        tracked = sorted(path for path in listed.decode("utf-8").split("\0") if path)
        self.assertEqual(tracked, sorted(produced),
                         "run python -B agent-instructions/skill_entry_points.py --write and "
                         "commit what it writes")
        for path, text in produced.items():
            self.assertEqual((ROOT / path).read_bytes(), text.encode("utf-8"), path)
        self.assertEqual(generator.orphans(ROOT, skills), [])
```

This is the derived-file equality of WAY-53 for these files. It cites no invariant: citing `derived-file-content/1` would make it an invariant check, which the code's author may not write (WAY-69).

- [ ] **Step 2: Run it to see it fail**

Run: `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions`
Expected: exit 1, `FAIL: test_the_tracked_entry_points_are_what_the_generator_produces`, `AssertionError: Lists differ: [] != ['.agents/skills/the-way-critique/SKILL.md…` (the planner saw exactly this in a scratch copy).

- [ ] **Step 3: Generate and stage the entry points**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B agent-instructions/skill_entry_points.py --write | tee $R/reports/check_3_generate.txt | wc -l && python -B agent-instructions/skill_entry_points.py && git add .claude/skills .agents/skills agent-instructions/test_skill_entry_points.py && git ls-files .claude/skills .agents/skills | wc -l && for d in .claude/skills/the-way-*; do cmp "$d/SKILL.md" ".agents/skills/$(basename $d)/SKILL.md" || echo "DIFFER $d"; done
```
Expected: `22`; then `entry points are current`; `22` tracked; no `DIFFER` line.

- [ ] **Step 4: Run the checks the entry points turn green**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions > $R/reports/check_3_tests_agent_instructions.txt 2>&1; echo "agent-instructions $?"; \
python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > $R/reports/check_3_gate.txt 2>&1; echo "gate $?"; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none > $R/reports/check_3_guard_part_map.txt 2>&1; echo "part-map $?"; tail -1 $R/reports/check_3_guard_part_map.txt; \
python -B gate/run_tests.py installation > $R/reports/check_3_tests_installation.txt 2>&1; echo "installation $?"
```
Expected: agent-instructions `0` (12 tests); gate `0` (the 96 baseline tests and the two flow tests, `skill-entry-points/1` recorded `pass`); part-map `0`, `0 error(s), 0 warning(s)` (both patterns now reach files, every entry point claimed once); installation `0` (16 tests; the planner ran them with the entry points committed in a scratch copy).

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "feat(agent-instructions): Add the entry points that give sessions on the-way its own skills" -- .claude/skills .agents/skills agent-instructions/test_skill_entry_points.py && git status --short
```
Expected: empty status.

- [ ] **Step 6: Deliberate break (for this task's reviewer, WAY-69, WAY-08)**

The reviewer of Task 3's code — who wrote neither the check nor the sentence — reads only the sentence of `skill-entry-points/1` in `foundations/invariants.md`, writes at least one break of it in the worktree (for example: delete one `.agents/skills/the-way-*/SKILL.md`; change one byte of a `.claude` copy; remove one sibling name from one entry point; add an empty directory `.claude/skills/the-way-nothing/` with a file in it), runs `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`, and reports for each break whether `test_every_skill_reaches_a_session_on_the_way` failed and `skill-entry-points/1` was recorded `fail`. Then it restores: `git restore --source=HEAD --staged --worktree -- .claude/skills .agents/skills` and removes any directory it added (`git clean -n -d -- .claude/skills .agents/skills` to list, then deletes those listed by path); `git status --short` is empty. A break that does not fail the check is a finding against the check; it goes to the orchestrator, which returns it to the foundation step (the check is read-only here).

---

### Task 4: Where the-way lies, in each skill (points 2, 3)

**Files:** Modify the nine paragraphs and one sentence below. Nothing else in these files changes. Replace each paragraph whole with the Edit tool (old text = the paragraph at the lines named, read from the file).

**Interfaces:** Consumes the names `the-way-<name>` (Task 3). Produces the paragraphs Task 6's installer sentence points to ("where it says where the-way lies").

- [ ] **Step 1: Five element skills** — the paragraph at lines 13–17 that begins "This skill lives in `elements/<element>/skill/` of the-way. Installed globally" becomes, per file:

`elements/decisions/skill/SKILL.md`:
```markdown
This skill lives in `elements/decisions/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/decisions/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what a decision adds to each.
```

`elements/environment-facts/skill/SKILL.md`:
```markdown
This skill lives in `elements/environment-facts/skill/` of the-way. In the-way itself, the-way is
the checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/environment-facts/` there, and each the-way skill named below is
the project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what an environment fact adds to each.
```

`elements/glossary/skill/SKILL.md`:
```markdown
This skill lives in `elements/glossary/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/glossary/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what a glossary entry adds to each.
```

`elements/invariants/skill/SKILL.md`:
```markdown
This skill lives in `elements/invariants/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/invariants/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what an invariant adds to each.
```

`elements/part-map/skill/SKILL.md`:
```markdown
This skill lives in `elements/part-map/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/part-map/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what the part map adds to each.
```

- [ ] **Step 2: `elements/common/skill/SKILL.md`, lines 16–20** (begins "This skill lives in `elements/common/skill/` of the-way. Installed globally"):
```markdown
This skill lives in `elements/common/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`.
`elements/common/` is there, and each skill named below is the project skill of that name with the
`the-way-` prefix.
```

- [ ] **Step 3: `project-level/skill/SKILL.md`, lines 16–20, and `project-level/technology/SKILL.md`, lines 18–22**:

`project-level/skill/SKILL.md`:
```markdown
This skill lives in `project-level/skill/` of the-way. In the-way itself, the-way is the checkout
or worktree the session was started in, the directory `git rev-parse --show-toplevel` prints in
the session's start directory; in a product, it is the product's pinned `.the-way`. The project
level's directory, `project-level/`, is there, and each skill named below is the project skill of
that name with the `the-way-` prefix.
```

`project-level/technology/SKILL.md`:
```markdown
This skill lives in `project-level/technology/` of the-way. In the-way itself, the-way is the
checkout or worktree the session was started in, the directory `git rev-parse --show-toplevel`
prints in the session's start directory; in a product, it is the product's pinned `.the-way`. The
project level's directory, `project-level/`, is there, and each skill named below is the project
skill of that name with the `the-way-` prefix.
```

- [ ] **Step 4: `project-level/task/skill/SKILL.md`, lines 12–14** (begins "This skill lives in `project-level/task/skill/` of the-way. When installed globally"):
```markdown
This skill lives in `project-level/task/skill/` of the-way. In the-way itself, read it in the
checkout or worktree the session was started in; in a product, at the pinned `.the-way` commit.
Another the-way skill named here is the project skill with the `the-way-` prefix.
```

- [ ] **Step 5: `elements/common/way_of_working.md`, lines 9–10** ("Paths under `elements/` below are those of the-way at the commit the product pins, which the skill reaches by resolving its own directory (WAY-34).") becomes:
```markdown
Paths under `elements/` below are those of the-way at the commit the product pins (WAY-34); in
the-way itself, those of the checkout or worktree the session was started in.
```
`elements/common/critique/SKILL.md` and `task-cycle/skill/SKILL.md` are not changed (spec §4.3).

- [ ] **Step 6: Check**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git grep -n -i -e "installed globally" -e "realpath <base>" -e "Get-Item <base>" -e "resolving its own directory" -- '*.md'; echo "grep $?"; \
git grep -l "the session was started in" -- 'elements/*SKILL.md' 'project-level/*SKILL.md' elements/common/way_of_working.md | wc -l; \
git grep -c "elements/common/way_of_working.md" -- 'elements/*/skill/SKILL.md'; \
python -B agent-instructions/skill_entry_points.py; \
for d in gate agent-instructions installation project-level elements/decisions elements/invariants elements/part-map elements/environment-facts elements/glossary; do python -B gate/run_tests.py $d > $R/reports/check_4_tests_$(echo $d | tr / _).txt 2>&1; echo "$d $?"; done; \
python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none > $R/reports/check_4_guard_glossary.txt 2>&1; echo "glossary $?"; tail -1 $R/reports/check_4_guard_glossary.txt
```
Expected: the first `git grep` prints nothing and `grep 1`; `10` files; each element skill still names `elements/common/way_of_working.md` (invariant `skill-rule-source`, level 2); `entry points are current` (no description changed); every test directory `0` (the installer tests read the committed `SKILL.md`, unchanged until the commit); glossary `0`, `0 error(s)`.

- [ ] **Step 7: Commit (two commits by part)**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "feat(elements): Read the-way from the session's own checkout in the-way and from .the-way in a product" -- elements/decisions/skill/SKILL.md elements/environment-facts/skill/SKILL.md elements/glossary/skill/SKILL.md elements/invariants/skill/SKILL.md elements/part-map/skill/SKILL.md elements/common/skill/SKILL.md elements/common/way_of_working.md && \
git commit -m "feat(project-level): Read the-way from the session's own checkout in the-way and from .the-way in a product" -- project-level/skill/SKILL.md project-level/technology/SKILL.md project-level/task/skill/SKILL.md && git status --short
```

---

### Task 5: `AGENTS.md` and `README.md`

**Files:**
- Modify: `AGENTS.md` (append two sections)
- Modify: `README.md` ("What else is here", `agent-instructions/` bullet; "Using the skills", whole section)

**Interfaces:** Consumes the generator command (Task 2) and the entry-point directories (Task 3).

- [ ] **Step 1: `AGENTS.md`** — keep the existing paragraph; append, after one blank line (spec §4.5):

```markdown
## Skills

A session on this repository finds each skill of the-way as the project skill `the-way-<name>`,
in `.claude/skills/` for Claude Code and `.agents/skills/` for Codex, and each reads its skill and
the files it names from the checkout or worktree the session was started in. Use only these: a
personal skill of the same name without the prefix — `refine-task`, `critique` or another — is not
the-way's. A change that adds, renames or moves a skill, or changes its description, runs
`python -B agent-instructions/skill_entry_points.py --write` and commits what it writes; the gate's
tests report a skill a session would not see.

## Backlog

- Tasks: `<private notes>/Notes\Projects\(P) Proces pracy nad produktem\_tasks_active.md`.
  A task's description is a document in the `_zadania\` folder beside it, linked from the task's
  line. Both are in the author's private notes; an agent that cannot open them asks the human.
```

- [ ] **Step 2: `README.md`, "What else is here"** — the bullet beginning "- `agent-instructions/`, with `AGENTS.md` and `CLAUDE.md` at the root" becomes:
```markdown
- `agent-instructions/`, with `AGENTS.md` and `CLAUDE.md` at the root and the skill entry points in
  `.claude/skills/` and `.agents/skills/` — instructions for agents working on the-way itself, and
  the script that generates those entry points.
```

- [ ] **Step 3: `README.md`, "Using the skills"** — everything from `## Using the skills` to the end of the file (the junction command included) becomes:
````markdown
## Using the skills

Each element's `skill/` directory, `elements/common/skill/` and `elements/common/critique/`, the
project level's skill directories and `task-cycle/skill/` hold one skill, named in its `SKILL.md`.

A Claude Code or Codex session started in a checkout or worktree of the-way finds each of them as
the project skill `the-way-<name>`: `.claude/skills/` holds the entry points Claude Code reads and
`.agents/skills/` the identical ones Codex reads, and each entry point reads its skill from the
checkout or worktree the session was started in. They are generated; after adding, renaming or
moving a skill, or changing its description, run:

```bash
python -B agent-instructions/skill_entry_points.py --write
```

and commit what it writes. A product gets the same skills, pointing to its pinned `.the-way`, from
the installer; see `installation/README.md`.
````

- [ ] **Step 4: Check**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && grep -n "^## " AGENTS.md; grep -c "New-Item -ItemType Junction" README.md; \
python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > $R/reports/check_5_gate.txt 2>&1; echo "gate $?"; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none 2>&1 | tail -1
```
Expected: `AGENTS.md` lists `# Working in the-way`, `## Skills`, `## Backlog`; `0` junction lines; gate `0`; part map `0 error(s)`. The vault path in `## Backlog` is what `outbound-link-reach/1`'s edited sentence (1.5) admits; its *Method* is `TODO`, so no command checks it (named under Task 7, "Unchecked").

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "docs(agent-instructions): Name the-way's project skills and its backlog in AGENTS.md and README" -- AGENTS.md README.md
```

---

### Task 6: Installer sentence and its test (`installation`, trust boundary)

**Files:**
- Modify: `installation/install.py:128` (one string literal in `skill_wrapper`)
- Test: `installation/test_install.py` (new method before `test_guidance_names_no_commit_and_covers_the_product_rules`)

**Interfaces:** Consumes Task 4's paragraphs (the wrapper now sends the agent to "where it says where the-way lies"). `install.skill_wrapper(path: str, name: str, commit: str) -> str` keeps its signature.

- [ ] **Step 1: Write the failing test** — insert into class `InstallTest`, before `def test_guidance_names_no_commit_and_covers_the_product_rules`:

```python
    def test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies(self) -> None:
        for path, name in NAMES:
            with self.subTest(name):
                text = install.skill_wrapper(path, name, self.commit)
                self.assertIn("Where it says where the-way lies, the product's case applies: "
                              "here the process root is `.the-way`.", text)
                self.assertNotIn("global install", text)
                self.assertIn("Do not substitute a global skill.", text)
```

- [ ] **Step 2: Run it to see it fail**

Run: `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py installation`
Expected: exit 1, `FAIL: test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies` (11 subtests) with `AssertionError: "Where it says where the-way lies…" not found`.

- [ ] **Step 3: Change the sentence** — in `installation/install.py`, line 128, replace the literal
`"Its paragraph about resolving a global skill link applies only to a global install; "`
with
`"Where it says where the-way lies, the product's case applies: "`.
Line 129 (`f"here the process root is `{SUBMODULE}`. Do not substitute a global skill.\n\n"`) stays.

- [ ] **Step 4: Run the installer's tests**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py installation > $R/reports/check_6_tests_installation.txt 2>&1; echo $?; tail -3 $R/reports/check_6_tests_installation.txt
```
Expected: exit 0, `Ran 17 tests`, `OK` (the planner ran this change and test in a scratch copy: OK). WAY-48: the change replaces a string literal of generated text and adds no input, path, argument or subprocess; the installer's existing adversarial tests run in this suite (`test_rejects_agents_file_with_other_or_broken_block_before_writing`, `test_rejects_agents_or_ignore_file_that_is_no_regular_utf8_file`, `test_rejects_conflicting_integration_file_before_writing`, `test_rejects_an_ignored_submodule_path_before_writing`, `test_warns_before_writing_paths_git_ignores`, `test_warns_where_codex_would_miss_the_block`, `test_preview_apply_rerun_and_preserve_foundation`, `test_declined_apply_writes_nothing`).

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "fix(installation): Point a product's skill wrapper to the product case of where the-way lies" -- installation/install.py installation/test_install.py
```

For the request (step 12, `pinned` change path): "Moving the pin rewrites the eleven wrappers' sentence on the process root; `.the-way` now carries the-way's own `.claude/skills/` and `.agents/skills/`, which Claude Code may list as `.the-way:the-way-<name>` and which stop themselves in a product."

---

### Task 7: Partial checks of the completed change, and the final review

- [ ] **Step 1: Run every check of the changed parts on the final commit**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git status --short; git log --oneline c64a607..HEAD; \
for d in gate agent-instructions installation project-level elements/decisions elements/invariants elements/part-map elements/environment-facts elements/glossary; do python -B gate/run_tests.py $d > $R/reports/check_7_tests_$(echo $d | tr / _).txt 2>&1; echo "$d $?"; done; \
for id in claude-code-project-skills claude-code-nested-skills codex-repository-skills codex-skill-paths; do python -B gate/run_tests.py probes/$id --record .runs/fact-$id.jsonl > $R/reports/check_7_watch_$id.txt 2>&1; echo "probes/$id $?"; done; \
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none > $R/reports/check_7_guard_decisions.txt 2>&1; echo "decisions $?"; \
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none > $R/reports/check_7_guard_invariants.txt 2>&1; echo "invariants $?"; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none > $R/reports/check_7_guard_part_map.txt 2>&1; echo "part-map $?"; \
python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none > $R/reports/check_7_guard_facts.txt 2>&1; echo "facts $?"; \
python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none > $R/reports/check_7_guard_glossary.txt 2>&1; echo "glossary $?"; \
python -B -I .runs/stale_refs.py > $R/reports/check_7_stale_refs.txt; echo "stale $?"; \
python -B agent-instructions/skill_entry_points.py; \
git ls-files .claude/skills .agents/skills | wc -l; git ls-files docs .gitmodules .the-way | wc -l; \
git grep -n -i -e "installed globally" -e "realpath <base>" -- '*.md'; echo "global-mode grep $?"
```
Expected: clean status; nine commits since c64a607; every test directory `0`; each watch `0` (a skip is recorded as no verdict); decisions `0` with the warnings of 1.3 step 2; invariants, part-map, facts, glossary `0` with `0 error(s)`; `stale 0`; `entry points are current`; `22`; `0`; no global-mode line and `global-mode grep 1`.

- [ ] **Step 2: Recalculate the sharpness inputs** (cycle step 10) from `git diff --stat c64a607..HEAD`: touched parts (foundations entries of decisions, invariants, part-map, environment-facts; gate; agent-instructions; elements-common; the five element parts; project-level; installation; repository files: none), trust boundary `installation/install.py` (string literal), nothing irreversible in the repository. Add checks if they grew; never drop any run above.

- [ ] **Step 3: Final review** — the whole-branch review of `subagent-driven-development` over `c64a607..HEAD` (no duplicate `requesting-code-review` dispatch for the same range). Its reviewer gets the spec, this plan and the diff; it confirms, among the rest, that `gate/test_skills_reach_the_way_sessions.py` is unchanged since its commit in 1.8 (`git log --oneline -- gate/test_skills_reach_the_way_sessions.py` shows one commit).

- [ ] **Step 4: Record** in `cycle.md` every result above by name, and the list "Unchecked" below.

**Unchecked (name these in the record and the request; none is a pass):**
- Every guard check that needs `--base` or `--merge-onto` (each guard prints its list): among them invariant versions and corrections (so `outbound-link-reach` staying `/1` under WAY-57 is unchecked), the fingerprints relations and links carry (covered only by the partial comparison `.runs/stale_refs.py`, N2/N4), the count of *Avoid* words, `TODO` in entries, the identifiers of the map, facts nothing names after the merge.
- Invariants whose *Method* is `TODO`: `outbound-link-reach` (the vault path in `AGENTS.md`), `repository-file-location` (the 22 entry points' place), `script-language`, `script-imports`, `script-subprocesses` (the generator), `derived-file-content` (covered in substance by the generator's own equality test, which cites nothing).
- Whether Claude Code and Codex actually list and follow the entry points: no session of either tool is run; only the human step after the merge (points 1–2 of the text below) observes it. The failure mode "the-way's own entry point followed inside a product where the agent knows neither path nor start directory" stays not detected.
- The level-2 verifications (WAY-09, WAY-27, WAY-127 paragraphs, `skill-rule-source`): left to the independent assessment and the code review.
- The watches depend on the network; a page that cannot be read gives no verdict. Whether WAY-08's deliberate break binds a fact's method stays open (environment-facts template).
- The dependency graph between parts (no command reports it), and the full gate, which does not exist.
- Reconciliation with `origin/foundations` 099c190 (PR #6, #7) and the sibling branch `task/instruction-files` (a twelfth skill: whichever merges second runs `--write`): step 12.

---

## For the request: the human step of point 6 (spec §4.7 with N1)

The planner parsed this script with the Windows PowerShell 5.1 parser (5.1.26100.9444): 0 errors. It was not run.

After `foundations` with this change is checked out in `C:\Storage\repos\the-way`:

1. Open a new Claude Code session there and check that `/the-way-record-decision` is listed.
2. Open a new Codex session there and check that its skill selector lists `the-way-record-decision`.
3. Then, in Windows PowerShell:

```powershell
$names = 'record-decision','record-invariant','record-glossary-term','record-environment-fact','update-part-map'
foreach ($n in $names) {
  $p = Join-Path $HOME ".claude\skills\$n"
  if (-not (Test-Path -LiteralPath $p)) { "${n}: not present, nothing to remove"; continue }
  $i = Get-Item -LiteralPath $p
  if ($i.LinkType -ne 'Junction') { "${n}: not a junction ($($i.LinkType)); left in place"; continue }
  cmd /c rmdir "$p"
}
foreach ($n in $names) { "{0}: {1}" -f $n, (Test-Path -LiteralPath (Join-Path $HOME ".claude\skills\$n")) }
Test-Path 'C:\Storage\repos\the-way\elements\decisions\skill\SKILL.md'
```

`rmdir` without `/s` removes the junction, never its target; `Remove-Item` is avoided because in Windows PowerShell 5.1 it can descend into a junction's target. Expected: five `False`, then `True`. `C:\Users\Mariusz\.agents\skills` is a link to the same directory, so Codex loses the same five. `refine-task` and `critique` (vox-ai-tools) are not the-way's and stay.

## Choices this plan makes (provisional, under the orchestrator)

| # | Choice | Alternative | Price if wrong |
|---|---|---|---|
| P1 | N5: the invariant's sentence states every property the check asserts, literals included | trim the check to what a short sentence states | a long sentence the assessment may judge against WAY-56; a shorter check would not report a stale prefix sentence |
| P2 | The plan gives properties, not wording, for the invariant's sentence, and gives the check author nothing of the generator | planner drafts the sentence | the planner, who wrote the generator's code here, would also be the sentence's author (WAY-69) |
| P3 | Watches written by a fresh agent after the facts agent (facts skill, "After step 4.4") | the facts agent writes them | one agent writes a fact and its check |
| P4 | WAY-127 *Review when* `none` | a state such as "Claude Code documents that the agent is told the skill file's path · check by: <date>" | a missed review if that state comes; the watches still catch a change of the cited passages |
| P5 | Generator root = the repository the script lies in, not the current directory | `git rev-parse --show-toplevel` of the current directory | none known; the other way could write into a product |
| P6 | Each paragraph of an entry point is one line | hard-wrapped like the spec's block | none; a wrapped text could split a phrase the check looks for |
| P7 | Folded or literal YAML values and a BOM stop the generator | accept them | a skill written so needs one-line frontmatter |
| P8 | Foundation step commits with two known reds (part-map pattern reach, the flow test) until Task 3 | land the map patterns with the entry points | none; WAY-01 orders the foundation first, and the reds are recorded |
| P9 | Fingerprint values checked by `.runs/stale_refs.py`, using the guards' parsers and `relation-model/fingerprint.py` | by hand only | a defect in the script; it agreed with the decisions guard's own reference values at the base and caught a planted change |
| P10 | `README.md` "Using the skills" also names `elements/common/skill/` and `elements/common/critique/` | keep the old first sentence | none |
| P11 | "entry point" is not a second meaning of the glossary term `entry`, unless 1.3's search finds otherwise | a glossary change now | a glossary change in the correction; a carrier cannot hold the word `entry` |
