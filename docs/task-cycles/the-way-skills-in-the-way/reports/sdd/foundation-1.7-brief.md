#### 1.7 Check author — the flow test (WAY-69)

**Files:** Create `gate/test_skills_reach_the_way_sessions.py` only.

- [ ] **Step 1: Dispatch a fresh agent** that wrote neither the sentence nor any code it covers, and that receives only:
  - the entry `skill-entry-points/1` as 1.5 wrote it (sentence, method, links), and the flow entry `skills-reach-the-way-sessions` as 1.6 wrote it;
  - the "Test" section of `C:\Storage\repos\the-way-process\elements\invariants\template.md` and WAY-69's binding sentences;
  - the docstring of `gate/run_tests.py` (citation form) and `gate/test_wording_reaches_dependants.py` as the form of a flow test;
  - this brief: a file `gate/test_skills_reach_the_way_sessions.py` with the line `# flow: skills-reach-the-way-sessions` at the top; `ROOT` the repository the file lies in; it imports nothing from `agent-instructions/` and nothing that computes entry points; it finds the population the sentence names with its own `git ls-files -z --cached --others --exclude-standard -- ':(glob)**/SKILL.md'` run in the root it checks, and reads each skill's name and description from its `SKILL.md`; every value it expects is written out in the test, taken from the sentence; text is compared with runs of whitespace collapsed to one space; a function `problems(root) -> list[str]` returns one line per property of the sentence that fails, naming the file; `test_every_skill_reaches_a_session_on_the_way` holds `# invariant: skill-entry-points/1` alone on its line inside the method, asserts `problems(ROOT) == []` with a failure message that names `python -B agent-instructions/skill_entry_points.py --write`, and, as a positive control, asserts that discovery found `elements/decisions/skill/SKILL.md` and `task-cycle/skill/SKILL.md`; `test_problems_reports_a_skill_the_session_does_not_see` cites nothing and, on a temporary `git init` repository with no commit, shows that `problems()` reports a skill with no entry points, a skill with only the `.claude` one, two copies that differ in bytes, and an orphan `the-way-*` directory.
  - It never receives `spec.md` §4.1–§4.3, this plan's Tasks 2–3, or any generator code. Its questions go to the orchestrator, who answers from the sentence only; a question the sentence cannot answer returns to 1.5.

- [ ] **Step 2: Run it (expected red until Task 3)**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > $R/reports/check_1_7_gate.txt 2>&1; echo $?; grep -E "^(FAIL|ERROR|Ran|OK|FAILED)" $R/reports/check_1_7_gate.txt
```
Expected: exit 1; the 96 baseline tests pass; the control test passes; `test_every_skill_reaches_a_session_on_the_way` FAILS with problems naming missing entry points and the generator command (no entry points exist yet); in `.runs/gate-tests.jsonl` a `fail` line for `skill-entry-points/1`. An ERROR (import, syntax) or a passing citing test is a defect of 1.7.

