### Task 3: Generated entry points and their derived equality

**Files:**
- Create: 22 files `.claude/skills/the-way-<name>/SKILL.md`, `.agents/skills/the-way-<name>/SKILL.md` (by the generator)
- Modify: `agent-instructions/test_skill_entry_points.py` (add `TrackedEntryPoints` before `if __name__`)

**Interfaces:**
- Consumes: `generator.discover`, `generator.produce`, `generator.orphans`, `ROOT` from Task 2.
- Produces: the tracked entry points that `gate/test_skills_reach_the_way_sessions.py` and `foundations/part_map.md`'s patterns need.

- [ ] **Step 1: Write the failing test** — insert into `agent-instructions/test_skill_entry_points.py`, before `if __name__ == "__main__":`:

```python
class TrackedEntryPoints(unittest.TestCase):
    def test_the_tracked_entry_points_are_what_the_generator_produces(self) -> None:
        skills = generator.discover(ROOT)
        produced = generator.produce(skills)
        listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--", ".claude/skills",
                                 ".agents/skills"], check=True, capture_output=True).stdout
        tracked = sorted(path for path in listed.decode("utf-8").split("\0") if path)
        self.assertEqual(tracked, sorted(produced),
                         "run python -B agent-instructions/skill_entry_points.py --write and "
                         "commit what it writes")
        for path, text in produced.items():
            self.assertEqual((ROOT / path).read_bytes(), text.encode("utf-8"), path)
        self.assertEqual(generator.orphans(ROOT, skills), [])
```

This is the derived-file equality of WAY-53 for these files. It cites no invariant: citing `derived-file-content/1` would make it an invariant check, which the code's author may not write (WAY-69).

- [ ] **Step 2: Run it to see it fail**

Run: `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions`
Expected: exit 1, `FAIL: test_the_tracked_entry_points_are_what_the_generator_produces`, `AssertionError: Lists differ: [] != ['.agents/skills/the-way-critique/SKILL.md…` (the planner saw exactly this in a scratch copy).

- [ ] **Step 3: Generate and stage the entry points**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B agent-instructions/skill_entry_points.py --write | tee $R/reports/check_3_generate.txt | wc -l && python -B agent-instructions/skill_entry_points.py && git add .claude/skills .agents/skills agent-instructions/test_skill_entry_points.py && git ls-files .claude/skills .agents/skills | wc -l && for d in .claude/skills/the-way-*; do cmp "$d/SKILL.md" ".agents/skills/$(basename $d)/SKILL.md" || echo "DIFFER $d"; done
```
Expected: `22`; then `entry points are current`; `22` tracked; no `DIFFER` line.

- [ ] **Step 4: Run the checks the entry points turn green**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions > $R/reports/check_3_tests_agent_instructions.txt 2>&1; echo "agent-instructions $?"; \
python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > $R/reports/check_3_gate.txt 2>&1; echo "gate $?"; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none > $R/reports/check_3_guard_part_map.txt 2>&1; echo "part-map $?"; tail -1 $R/reports/check_3_guard_part_map.txt; \
python -B gate/run_tests.py installation > $R/reports/check_3_tests_installation.txt 2>&1; echo "installation $?"
```
Expected: agent-instructions `0` (12 tests); gate `0` (the 96 baseline tests and the two flow tests, `skill-entry-points/1` recorded `pass`); part-map `0`, `0 error(s), 0 warning(s)` (both patterns now reach files, every entry point claimed once); installation `0` (16 tests; the planner ran them with the entry points committed in a scratch copy).

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "feat(agent-instructions): Add the entry points that give sessions on the-way its own skills" -- .claude/skills .agents/skills agent-instructions/test_skill_entry_points.py && git status --short
```
Expected: empty status.

- [ ] **Step 6: Deliberate break (for this task's reviewer, WAY-69, WAY-08)**

The reviewer of Task 3's code — who wrote neither the check nor the sentence — reads only the sentence of `skill-entry-points/1` in `foundations/invariants.md`, writes at least one break of it in the worktree (for example: delete one `.agents/skills/the-way-*/SKILL.md`; change one byte of a `.claude` copy; remove one sibling name from one entry point; add an empty directory `.claude/skills/the-way-nothing/` with a file in it), runs `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`, and reports for each break whether `test_every_skill_reaches_a_session_on_the_way` failed and `skill-entry-points/1` was recorded `fail`. Then it restores: `git restore --source=HEAD --staged --worktree -- .claude/skills .agents/skills` and removes any directory it added (`git clean -n -d -- .claude/skills .agents/skills` to list, then deletes those listed by path); `git status --short` is empty. A break that does not fail the check is a finding against the check; it goes to the orchestrator, which returns it to the foundation step (the check is read-only here).

---

