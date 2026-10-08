### Task 2: Entry points of the new skill (task point 8)

**Files:**
- Create: `.claude/skills/the-way-maintain-instruction-files/SKILL.md`, `.agents/skills/the-way-maintain-instruction-files/SKILL.md` (by the generator)
- Modify: the 22 other entry points under `.claude/skills/the-way-*/` and `.agents/skills/the-way-*/` (their sentence naming every skill gains `maintain-instruction-files`; by the generator)

**Interfaces:**
- Consumes: `instruction-files/SKILL.md` (Task 0; its frontmatter `name: maintain-instruction-files` and its one-line description, which no later task changes); the flow's *Parts* (1.7).
- Produces: the tracked entry points the gate's flow test and `agent-instructions/test_skill_entry_points.py` ask for.

- [ ] **Step 1: See the failing tests**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py gate 2>&1 | grep -E "^(FAIL|ERROR):|^Ran"; python -B gate/run_tests.py agent-instructions 2>&1 | grep -E "^(FAIL|ERROR):|^Ran"; python -B agent-instructions/skill_entry_points.py | awk '{print $1, $2}' | sort | uniq -c
```
Expected: the two known FAILs; the dry run prints `22 would change` and `2 would create` and writes nothing.

- [ ] **Step 2: Generate, and stage what the generator wrote**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B agent-instructions/skill_entry_points.py --write > $R/reports/check_2_generate.txt; echo "generate $?"; grep -c "^created" $R/reports/check_2_generate.txt; grep -c "^changed" $R/reports/check_2_generate.txt; python -B agent-instructions/skill_entry_points.py && git add .claude/skills .agents/skills && git status --short | awk '{print $1}' | sort | uniq -c && cmp .claude/skills/the-way-maintain-instruction-files/SKILL.md .agents/skills/the-way-maintain-instruction-files/SKILL.md && echo identical
```
Expected (planner, on a clone): `generate 0`, `2`, `22`, `entry points are current`, `2 A` and `22 M`, `identical`.

- [ ] **Step 3: Run the checks the entry points turn green**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl > $R/reports/check_2_tests_agent_instructions.txt 2>&1; echo "agent-instructions $?"; tail -1 $R/reports/check_2_tests_agent_instructions.txt; \
python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > $R/reports/check_2_gate.txt 2>&1; echo "gate $?"; tail -1 $R/reports/check_2_gate.txt; grep -c '"fail"' .runs/gate-tests.jsonl; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none 2>&1 | tail -1
```
Expected (planner, on a clone): agent-instructions `0`, `OK`; gate `0`, `OK` (98 tests), `0` fail lines; part map `0 error(s), 0 warning(s), 7 unchecked`.

- [ ] **Step 4: Commit**

```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && S="Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" && git commit -m "feat(agent-instructions): Add the entry points of maintain-instruction-files" -m "$S" -- .claude/skills .agents/skills && git status --short
```
Expected: empty status. From here `gate` and `agent-instructions` are green; a red result in either is a defect of the task that produced it.

---

