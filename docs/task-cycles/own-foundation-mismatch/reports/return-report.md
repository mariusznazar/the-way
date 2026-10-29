# Return-step report

**Status:** done

**Commit range:** `76cbe0ea4e766eb9561052355e370d6424c1d32f..876482ee4545749f7e3daa8e8c3a3c607f1682fc`. No new commit; the return step found no correction to make.

**Entries compared and corrected:** I compared the foundation selection from the author handoff, the task's named decisions WAY-01, WAY-11, WAY-161 and WAY-162, the whole-change review criteria WAY-220 and WAY-221, the entries found by the foundation search, the new WAY-263, and the task-cycle and decisions parts of `foundations/part_map.md` with the two changed files. WAY-263 is assigned to `task-cycle`, derives from the existing WAY-161, and is reflected at the Grade step in `task-cycle/review/SKILL.md`. The decision log remains assigned to `decisions`; its entry scopes the rule to `task-cycle`, which the map allows to depend on `decisions`. The two files agree on direct departures and changed restatements, include entries the change writes or changes, and preserve WAY-161's general blocking rule. No entry or part-map item needs correction.

**Settlement 1:** Recorded as the new decision WAY-263, deriving from WAY-161; WAY-161 remains unchanged. Znaczenie: Recenzent ocenia jako Important uwagę, że zmiana przeczy wpisowi fundamentu, który sama zapisuje lub zmienia — przez kod sprzeczny z wpisem albo przez powtórzenie wpisu z szerszą treścią lub bez jego zastrzeżenia.

**Checks:**

- `python -B elements/common/foundation_check.py` — exit code 0, 0 errors, as recorded in the author report on this head.
- `git diff --check` — exit code 0 in the author stage; no files changed in the return step.
- `python -B gate/run_tests.py` — exit code 0, 613 tests in 8 directories, with five Windows platform skips, as reported by the orchestrator for this head.
- Manual return comparison — the commit diff, the selected foundation entries and the part map agree; no environment fact, glossary term, missed settlement, projected entry or invariant is needed. No invariant was added for prose that has no program behaviour to test.
- No checks were rerun during this return step; the author-focused check and full gate evidence already apply to the unchanged head.

**Reaches:** Read `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md` for this return. The foundation selection remains as named in the author handoff, with WAY-263 and the previously reported search findings WAY-07, WAY-35, WAY-64, WAY-135, WAY-145, WAY-148, WAY-169 and WAY-171; each was compared whole. The relevant entries WAY-01, WAY-11, WAY-161, WAY-162, WAY-220 and WAY-221 were also compared with the diff. The project part map was read whole to check the files' assignments and dependency.

**Searches not found or unclear:** None during the return step. The author-stage search, recorded in `author-report.md`, found no prior WAY-263 or existing decision that already states this grading rule.
