# Findings for the fix — review of the whole change, `PASS 79c9bfb95e772cb21810a78fc42607f99d726da0`

Source: `reports/review-whole-report.md`, in the reviewer's words. Reviewed range
`4758840fbaf9562db960965c706d8681c3d23a43..79c9bfb95e772cb21810a78fc42607f99d726da0`.

## Blocking findings

none (Contradiction with the settlements: none, no blocking finding).

## Minor findings within the task (fixed in this round, WAY-161)

1. **`process-audit/SKILL.md:124` and `process-audit/audit_count.py:25-26` (module docstring) — "every
   key that holds a key `repository`".** Within the task (To do 9). The rename makes both levels of
   the locations file "key", and this sentence now says "key" for both in one breath. Elsewhere the
   change tells the two apart: `project-level/backlog_place.md:25-31` and `process-audit/SKILL.md:106`
   say "repository key" for the outer level, and the new error message at
   `process-audit/audit_count.py:628` says "no repository named in the locations file holds a key
   `repository`". The sentence is still true, but it reads worse than the rest. Suggested wording:
   "every repository key that holds a key `repository`". Nothing breaks if it stays.

2. **Lines not rewrapped after the rename (about 70 added lines over 104 characters in Markdown and
   Python outside the glossary and the skill descriptions).** Within the task. Examples:
   `foundations/decisions.md:201` (WAY-118), `foundations/decisions.md:3805` (WAY-145 *Verification*),
   `project-level/definition_template.md:338` and `:340`, `project-level/lead/skill/definition_change.md:3`
   and `:14`, `project-level/plan/skill/delegated_mode.md:22`, `project-level/readiness_check.py:290`,
   `project-level/test_plan_check.py:334`. The files around them wrap at about 100 columns. No reader
   reads them wrongly and the linter does not object; the only cost is a larger diff for whoever
   rewraps them later.

3. **No permanent test pins the refusal of the old heading and the old status.** Within the task
   (To do 3 and 4; *Questions to settle* 1, whose way not chosen was "the scripts accept both
   headings"). `project-level/test_readiness_check.py` refuses headings and statuses outside the form
   only through general cases (`test_a_section_outside_the_template_is_reported`,
   `test_a_status_off_its_forms_is_reported`, line 166). A later change that adds `Gate record` to
   `SECTIONS` as an alias, or `ready for gate` to `STATUS`, would pass the suite. My one-off check
   (below) shows the head refuses both today. One case each, "`## Gate record` is reported as no
   section of the template" and "`Status: ready for gate` is reported", would hold the human's choice
   in place. Coverage that would be nice, not a defect.
