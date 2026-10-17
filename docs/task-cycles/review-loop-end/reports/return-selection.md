# Foundation selection — review-loop-end, return step

Refreshed by "Reading the foundation" (WAY-150) for the real diff `e7f7c3a..78df576` (and the
return-step commit `6ed0e86`) against the current foundation.

- Target: `origin/foundations` fetched at the start of the return step = `e7f7c3a` (unchanged);
  `git diff --quiet e7f7c3a origin/foundations -- foundations/` → identical, so no foundation entry
  landed on the target since the base.
- Changed files: `foundations/decisions.md` (entries WAY-125, WAY-140, WAY-148, WAY-157 — scope
  `task-cycle` or `project-level, task-cycle` — and the new WAY-161..164, scope `task-cycle`),
  `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` (part `task-cycle`). Touched part:
  **task-cycle** (and `decisions` only as the file holding those entries, WAY-44). Unchanged from
  the foundation step's selection.
- Expected *Scope* matches: the 56 decisions listed in `foundation-selection.md` plus WAY-161,
  WAY-162, WAY-163, WAY-164 — 60, all read whole (the whole log was read in the foundation step;
  the entries changed since, WAY-125 and WAY-161..164, were re-read whole at `78df576`).
- WAY-140 (`project-level, task-cycle`) touches `project-level` only through its scope, not through
  this change's behaviour; its WAY-125 link was rechecked.
- Invariants: no entry's *Part* names `task-cycle`; none derives from WAY-125 or WAY-161..164; the
  `every` invariants read in the foundation step (return-step-record, foundation-search-record,
  foundation-change-assessment-record, foundation-change-path, merge route) still apply unchanged.
- Glossary, part map, environment facts: re-read for the candidates below (glossary terms
  `verdict`, `correction`, `result`; part `task-cycle` failure modes; facts list).
- Read vs discovered: as in `foundation-selection.md`; nothing new discovered only.
