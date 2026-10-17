# Independent assessment — brief given to the assessor (filtered inputs only)

Model: Fable 5.1 (author, invariant agents and reviewer: Opus 5.5). Method: `elements/common/critique/SKILL.md` (WAY-10).

Inputs given: a detached worktree `C:/Storage/repos/the-way-wt/agent-path-to-running-product-assess` at `0c1dfd5` (no `.runs/`), the assessed range `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988..0c1dfd5`, its files, and the tracked sources needed to interpret binding rules (element templates and rules, the rest of `foundations/`). Not given: the task document, handoffs, reports, cycle record, chronology, author reasoning, reviews.

Prompt (verbatim below).

---

You are the independent assessor of a change to the foundation of the-way, a repository that defines a process for agent-built software. Follow `elements/common/critique/SKILL.md` in the worktree below; read it whole first. You are the "fresh critic"; you report observations, you do not write repository files.

Worktree (read-only): `C:/Storage/repos/the-way-wt/agent-path-to-running-product-assess`, detached at `0c1dfd5`. Assessed range: `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988..0c1dfd5` — run `git diff 77c8a8b..0c1dfd5` there. Changed files: `foundations/decisions.md` (WAY-121 edited in place, new WAY-165, renewed fingerprints in WAY-122 and WAY-123), `foundations/invariants.md` (`project-technology-record/1` rewritten), `project-level/readiness_check.py`, `project-level/definition_template.md`, `project-level/technology/SKILL.md`, `project-level/skill/SKILL.md`, `project-level/task/skill/SKILL.md`, `project-level/plan/skill/SKILL.md`, `project-level/lead/skill/SKILL.md`, and tests `project-level/test_readiness_check.py` (invariant checks), `project-level/test_plan_state_invariant.py`, `project-level/test_plan_state.py` (fixtures), `project-level/test_readiness_marks.py`.

Read in full: the changed entries whole (WAY-121, WAY-165, the invariant `project-technology-record/1`), the entries they relate to (follow *Relations* and *Derives from*: WAY-118, WAY-100, WAY-106, WAY-116, WAY-122, WAY-123, WAY-137, WAY-108), `elements/decisions/template.md`, `elements/invariants/template.md`, `elements/common/rules.md`, `foundations/glossary.md`, the part map's `project-level` part (`foundations/part_map.md`), and the changed code, template, skills and tests at `0c1dfd5`.

Check, for every changed entry, the invariant and its checks, and for the code, template and skill text as the implementation of those entries: purpose and the moment it acts; whether it would act in the cases it targets; error when applied too widely, and whether it moves a problem elsewhere; cheaper ways (existing rule, template, check); source fidelity of every substantive claim; contradictions with current entries anywhere in `foundations/` and between the entries and the code and skills; duplicated or missing settlements between the new entries; template conformance; use of glossary terms in a meaning the glossary does not give (e.g. `surface`); whether the invariant's checks test what its sentence says and only that. Name what of the change can be cut, or state that nothing can. Do not search session transcripts or files outside this worktree; say if a frequency cannot be measured from the repository.

For each observation: id (A1, A2, …), what you checked, file:line evidence, what would have to change, and how much it matters. State explicitly each check that found no concern.

Write your full report to `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/48e1b1a6-9666-4b0d-8a29-8efacfa46bee/scratchpad/assessment.md` (the only file you write). Return a short message: number of observations by weight, the cut verdict, the report path.
