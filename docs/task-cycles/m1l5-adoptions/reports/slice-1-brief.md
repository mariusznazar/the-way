### Slice 1 — technology step carries the tie-breaker and the "what will this break" tests

- **Goal:** the Technology section's rules in `definition_template.md` state WAY-137 and WAY-138
  beside the WAY-123 bullet; `settle-technology` step 5 forms each recommendation, applies the
  tie-breaker of WAY-137 to a place to run, has one fresh agent per wave run the three tests on
  every recommended option of a choice settled in this project (never a `held by` choice), passes
  the table's contradiction critique the risks marked as hypotheses rather than claimed
  differences, and shows the risks beside the recommended option; step 6 says that choosing an
  option takes its risks; step 7 hands the accepted risks to `record-decision` with the lacks of the
  chosen option, marked as hypotheses; `record-decision`'s projected mode says in which field the
  lacks and the accepted risks of a chosen option stand (*Rationale*, a risk marked as a
  hypothesis, never in *Based on*).
- **Change:** `project-level/definition_template.md` · `project-level/technology/SKILL.md` ·
  `elements/decisions/skill/SKILL.md`
- **Read:** `foundations/decisions.md:2769-2794` · `foundations/decisions.md:3158-3193` ·
  `foundations/decisions.md:3371-3537` · `elements/decisions/template.md` ·
  `elements/common/way_of_working.md:1-60` · `elements/common/critique/SKILL.md`, and the entries
  WAY-137 and WAY-138 the foundation step appends at the end of the decision log
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B gate/run_tests.py
  elements/decisions` · `python -B gate/run_tests.py gate` · `python -B
  agent-instructions/skill_entry_points.py` (entry points still current: no description changes);
  no script's behaviour changes, so no test is written first
- **Depends on:** WAY-137 · WAY-138

