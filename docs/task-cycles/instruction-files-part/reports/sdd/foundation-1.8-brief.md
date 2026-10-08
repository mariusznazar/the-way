#### 1.8 Check author — the two invariant checks (WAY-69)

**Files:** Create `agent-instructions/test_instruction_files.py` only.

- [ ] **Step 1: Dispatch a fresh agent** that wrote neither the sentences nor any code they cover, and that receives only:
  - the entries `instruction-file-imports/1` and `root-claude-md-import/1` as 1.6 wrote them (sentence, method, links), and the glossary entry of every term their sentences use (`foundations/glossary.md`);
  - the "Test" section of `C:\Storage\repos\the-way-process\elements\invariants\template.md` and WAY-69's binding sentences;
  - the docstring of `gate/run_tests.py` (citation form) and `gate/test_skills_reach_the_way_sessions.py` as the form of a test that finds its population with its own call to git and holds its expected values as literals;
  - this brief: the file `agent-instructions/test_instruction_files.py`, part `agent-instructions`, run by the method `python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl`, its docstring naming that command (WAY-16); `ROOT` the repository the file lies in; it imports nothing from `instruction-files/` and nothing from `agent-instructions/skill_entry_points.py` — were it to use the check script, a change to that script would move both sides (WAY-69); it finds the files of each sentence with its own `git ls-files` run in the root it checks, and the Markdown files the root files name with its own pattern; every value it expects is written out in the test, taken from the sentence; one test per invariant, each holding `# invariant: <identifier>/1` alone on its line inside the method body, asserting a `problems(root) -> list[str]` of that invariant empty with a message naming each file and line; a positive control in each citing test that the population it found includes the root `AGENTS.md` and `CLAUDE.md` and `agent-instructions/README.md`; and tests citing nothing that, on temporary `git init` repositories, show each `problems()` reporting every kind of violation its sentence names and passing what the sentence allows (code spans, fenced blocks, an address such as `a@example.com`, an untracked file, a named file git does not track).
  - It never receives `spec.md`, this plan's Tasks 2–9, the check script or the generator. Its questions go to the orchestrator, who answers from the sentences only; a question the sentences cannot answer returns to 1.6.
- [ ] **Step 2: Run it**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl > $R/reports/check_1_8_tests_agent_instructions.txt 2>&1; echo "agent-instructions $?"; grep -E "^(FAIL|ERROR):|^Ran" $R/reports/check_1_8_tests_agent_instructions.txt; grep -E "instruction-file-imports|root-claude-md-import" .runs/agent-instructions-tests.jsonl
```
Expected: exit 1 with exactly the one known FAIL `test_the_tracked_entry_points_are_what_the_generator_produces` (red until Task 2); the record holds `"verdict": "pass"` lines for `instruction-file-imports/1` and `root-claude-md-import/1` and no `fail` for either. The planner checked on 252152a that the only `@` import in the population (`AGENTS.md`, `CLAUDE.md`, `agent-instructions/README.md`) is the first line of `CLAUDE.md`. An ERROR (import, syntax) or a failing invariant test is a defect of 1.8 or a finding against 1.6, returned to the orchestrator. From the commit of 1.9 the file is read-only for every later task (WAY-03).

