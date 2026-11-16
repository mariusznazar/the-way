# 0. Start or resume: an existing definition

Step 0 of the skill `define-project`, whose `SKILL.md` lies beside this file, for an existing
definition.

- Read the definition whole and go on from where its status line says; a working table under
  "Projected foundation changes" means step 5 (`find_entries.md` beside this file) is under way,
  and an item of "Technology" ending `— open` that step 6 (`technology.md` beside this file) is. A
  definition whose status reads `approved` is checked first:
  `python -B <the-way>/project-level/readiness_check.py <definition>`. A finding that its
  fingerprint no longer matches means the definition changed after the
  readiness approval, and it goes
  through step 7 (`readiness_approval.md` beside this file) again.
- A definition with no `## Technology` section was written before the step that settles the
  technology. Say so, and ask whether the project is reopened, as a question of decision "How a
  skill asks" gives, the ways being: reopening settles the technology at step 6 and takes the
  definition through the readiness approval again (WAY-118); leaving it leaves the choices to the
  breakdown, and the check keeps reporting the missing section. On reopening, add `## Technology`
  reading `TODO` before "Projected foundation changes", set the status line to
  `definition — open: Technology`, and go on at step 6 (`technology.md` beside this file)
  (WAY-121).
