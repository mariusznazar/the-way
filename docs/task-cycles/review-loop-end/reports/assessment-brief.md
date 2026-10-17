# Independent assessment — brief given to the assessor (filtered inputs only)

Model: Fable 5.1 (author and reviewer: Opus 5.5). Method: `elements/common/critique/SKILL.md` (WAY-10).

Inputs given: a detached worktree `C:/Storage/repos/the-way-wt/review-loop-end-assess` at `6ed0e86` (no `.runs/`), the assessed range `e7f7c3a15c3f80143f9ad582ec785c993cff3779..6ed0e86`, its files `foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, and the tracked sources needed to interpret binding rules (element templates and rules, the rest of `foundations/`, the Superpowers 6.4.1 files the entries quote). Not given: the task document, handoffs, reports, cycle record, chronology, author reasoning, reviews.

Prompt (verbatim below).

---

You are the independent assessor of a change to the foundation of the-way, a repository that defines a process for agent-built software. Follow `elements/common/critique/SKILL.md` in the worktree below; read it whole first. You are the "fresh critic"; you report observations, you do not write repository files.

Worktree (read-only): `C:/Storage/repos/the-way-wt/review-loop-end-assess`, detached at `6ed0e86`. Assessed range: `e7f7c3a15c3f80143f9ad582ec785c993cff3779..6ed0e86` — run `git diff e7f7c3a..6ed0e86` there. Changed files: `foundations/decisions.md` (new decisions WAY-161..164, WAY-125 and WAY-163 edits, renewed fingerprints), `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`.

Read in full: the changed entries whole (WAY-125, WAY-161, WAY-162, WAY-163, WAY-164), the entries they relate to (follow *Relations*), `elements/decisions/template.md`, `elements/common/rules.md`, `foundations/glossary.md`, the part map's `task-cycle` part (`foundations/part_map.md`), and the whole `task-cycle/skill/SKILL.md` at `6ed0e86`. The entries quote Superpowers 6.4.1 files under `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/` — check every quotation against them (read with your file tools; do not use any Skill tool).

Check, for every changed entry and for the skill text as the implementation of those entries: purpose and the moment it acts; whether it would act in the cases it targets; error when applied too widely, and whether it moves a problem elsewhere; cheaper ways (existing rule, template, check); source fidelity of every substantive claim and quotation; contradictions with current entries anywhere in `foundations/` and between the entries and the skill; duplicated or missing settlements between the new entries; template conformance; use of glossary terms in a meaning the glossary does not give (e.g. `verdict`, `correction`). Name what of the change can be cut, or state that nothing can. Do not search session transcripts outside this worktree; say if a frequency cannot be measured from the repository.

For each observation: id (A1, A2, …), what you checked, file:line evidence, what would have to change, and how much it matters. State explicitly each check that found no concern.

Write your full report to `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/0ec12b8b-dfcb-451f-8794-0fbf50a48b21/scratchpad/assessment.md` (the only file you write). Return a short message: number of observations by weight, the cut verdict, the report path.
