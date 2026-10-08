# Task 4 report

Status: DONE

## Changes
Nine paragraphs and one sentence replaced whole, text verbatim from the brief (amendment R12 included):
- elements/decisions, environment-facts, glossary, invariants, part-map: skill/SKILL.md paragraph
- elements/common/skill/SKILL.md
- project-level/skill/SKILL.md, project-level/technology/SKILL.md, project-level/task/skill/SKILL.md
- elements/common/way_of_working.md: one sentence

## Checks
- git grep for old wording: nothing, `grep 1`
- files containing "the session works in": 10
- each element skill still names elements/common/way_of_working.md (common 2, others 3)
- skill_entry_points.py: entry points are current
- tests: gate, agent-instructions, installation, project-level, decisions, invariants, part-map, environment-facts, glossary all 0
- glossary format guard: 0, "0 error(s), 0 warning(s), 5 unchecked"
Outputs in .runs/task-cycles/the-way-skills-in-the-way/reports/check_4_*.txt

## Commits
- 4816161 feat(elements): Read the-way from the session's own checkout in the-way and from .the-way in a product
- dd25a36 feat(project-level): Read the-way from the session's own checkout in the-way and from .the-way in a product

## Self-review
10 files changed, nothing else; no added line over 100 columns; status clean after commits.

## Concerns
None.
