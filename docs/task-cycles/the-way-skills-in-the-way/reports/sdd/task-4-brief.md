### Task 4: Where the-way lies, in each skill (points 2, 3)
> Controller note: amendment R12 (spec §10) applied to this brief — "the session was started in" → "the session works in", "the session's start directory" → "the session's working directory".

**Files:** Modify the nine paragraphs and one sentence below. Nothing else in these files changes. Replace each paragraph whole with the Edit tool (old text = the paragraph at the lines named, read from the file).

**Interfaces:** Consumes the names `the-way-<name>` (Task 3). Produces the paragraphs Task 6's installer sentence points to ("where it says where the-way lies").

- [ ] **Step 1: Five element skills** — the paragraph at lines 13–17 that begins "This skill lives in `elements/<element>/skill/` of the-way. Installed globally" becomes, per file:

`elements/decisions/skill/SKILL.md`:
```markdown
This skill lives in `elements/decisions/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/decisions/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what a decision adds to each.
```

`elements/environment-facts/skill/SKILL.md`:
```markdown
This skill lives in `elements/environment-facts/skill/` of the-way. In the-way itself, the-way is
the checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/environment-facts/` there, and each the-way skill named below is
the project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what an environment fact adds to each.
```

`elements/glossary/skill/SKILL.md`:
```markdown
This skill lives in `elements/glossary/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/glossary/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what a glossary entry adds to each.
```

`elements/invariants/skill/SKILL.md`:
```markdown
This skill lives in `elements/invariants/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/invariants/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what an invariant adds to each.
```

`elements/part-map/skill/SKILL.md`:
```markdown
This skill lives in `elements/part-map/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
element's directory is `elements/part-map/` there, and each the-way skill named below is the
project skill of that name with the `the-way-` prefix. Follow the steps of
`elements/common/way_of_working.md` there; below is what the part map adds to each.
```

- [ ] **Step 2: `elements/common/skill/SKILL.md`, lines 16–20** (begins "This skill lives in `elements/common/skill/` of the-way. Installed globally"):
```markdown
This skill lives in `elements/common/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`.
`elements/common/` is there, and each skill named below is the project skill of that name with the
`the-way-` prefix.
```

- [ ] **Step 3: `project-level/skill/SKILL.md`, lines 16–20, and `project-level/technology/SKILL.md`, lines 18–22**:

`project-level/skill/SKILL.md`:
```markdown
This skill lives in `project-level/skill/` of the-way. In the-way itself, the-way is the checkout
or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The project
level's directory, `project-level/`, is there, and each skill named below is the project skill of
that name with the `the-way-` prefix.
```

`project-level/technology/SKILL.md`:
```markdown
This skill lives in `project-level/technology/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
project level's directory, `project-level/`, is there, and each skill named below is the project
skill of that name with the `the-way-` prefix.
```

- [ ] **Step 4: `project-level/task/skill/SKILL.md`, lines 12–14** (begins "This skill lives in `project-level/task/skill/` of the-way. When installed globally"):
```markdown
This skill lives in `project-level/task/skill/` of the-way. In the-way itself, read it in the
checkout or worktree the session works in; in a product, at the pinned `.the-way` commit.
Another the-way skill named here is the project skill with the `the-way-` prefix.
```

- [ ] **Step 5: `elements/common/way_of_working.md`, lines 9–10** ("Paths under `elements/` below are those of the-way at the commit the product pins, which the skill reaches by resolving its own directory (WAY-34).") becomes:
```markdown
Paths under `elements/` below are those of the-way at the commit the product pins (WAY-34); in
the-way itself, those of the checkout or worktree the session works in.
```
`elements/common/critique/SKILL.md` and `task-cycle/skill/SKILL.md` are not changed (spec §4.3).

- [ ] **Step 6: Check**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git grep -n -i -e "installed globally" -e "realpath <base>" -e "Get-Item <base>" -e "resolving its own directory" -- '*.md'; echo "grep $?"; \
git grep -l "the session works in" -- 'elements/*SKILL.md' 'project-level/*SKILL.md' elements/common/way_of_working.md | wc -l; \
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

