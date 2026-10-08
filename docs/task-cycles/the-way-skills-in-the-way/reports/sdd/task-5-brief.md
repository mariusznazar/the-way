### Task 5: `AGENTS.md` and `README.md`
> Controller note: amendment R12 (spec §10) applied to this brief — "the session was started in" → "the session works in", "the session's start directory" → "the session's working directory".

**Files:**
- Modify: `AGENTS.md` (append two sections)
- Modify: `README.md` ("What else is here", `agent-instructions/` bullet; "Using the skills", whole section)

**Interfaces:** Consumes the generator command (Task 2) and the entry-point directories (Task 3).

- [ ] **Step 1: `AGENTS.md`** — keep the existing paragraph; append, after one blank line (spec §4.5):

```markdown
## Skills

A session on this repository finds each skill of the-way as the project skill `the-way-<name>`,
in `.claude/skills/` for Claude Code and `.agents/skills/` for Codex, and each reads its skill and
the files it names from the checkout or worktree the session works in. Use only these: a
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

A Claude Code or Codex session working in a checkout or worktree of the-way finds each of them as
the project skill `the-way-<name>`: `.claude/skills/` holds the entry points Claude Code reads and
`.agents/skills/` the identical ones Codex reads, and each entry point reads its skill from the
checkout or worktree the session works in. They are generated; after adding, renaming or
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

