# Slice 6 implementation report

Status: DONE. Boundary: exact ten generated wrappers committed; no review dispatch, merge or push.

## Inputs and authority

Worktree: C:/Storage/repos/the-way-wt/lead-project
Branch: task/lead-project
Actual BASE and source revision: 6b23e0b37a050d5fec45e948b047953d7a50baf8.
Borrowed brief: .superpowers/sdd/plan/task-6-brief.md, including actual dispatch and planner-routing ruling.
Read frozen task, full spec, planner routing, generator and tests, complete part map, all fifteen source skills, WAY-127 and WAY-152 through WAY-156. Scope inventory of the current decision log selected agent-instructions matches WAY-09, WAY-16, WAY-27, WAY-44, WAY-120, WAY-127 through WAY-133; each selected entry was read whole. These wrappers are owned by agent-instructions, not the source skill's part. WAY-150 selection was refreshed against this source revision. No foundation meaning changes.

Read global/worktree instructions, pre-main integration guide, Superpowers 6.4.1 implementer-prompt template, Obsidian rulebook, skill conventions and code-review playbook. No global or vault writes.

## Implementation and evidence

Imported agent-instructions/skill_entry_points.py in a Python -B stdin invocation using sys.path.insert(0, 'agent-instructions'); called discover(Path.cwd()), then produce(skills). Asserted 15 discovered source skills and 30 outputs. Built exact ten-path set from the five names critique, find-foundation-entries, maintain-instruction-files, implement-task and plan-task and ENTRY_DIRECTORIES. For each named path wrote only produced[path].encode('utf-8') with Path.write_bytes. No source skills, generator, tests or foundation edited.

Before: all ten existing named outputs differed from produce.
After: all ten matched produce byte for byte; all five Claude/Codex pairs were byte-identical.
Captured all twenty other output paths before writing and asserted their content/existence unchanged after writing.
Machine evidence: .superpowers/sdd/plan/task-6-generation.json (ignored).

Changed paths:
- .claude/skills/the-way-critique/SKILL.md
- .agents/skills/the-way-critique/SKILL.md
- .claude/skills/the-way-find-foundation-entries/SKILL.md
- .agents/skills/the-way-find-foundation-entries/SKILL.md
- .claude/skills/the-way-maintain-instruction-files/SKILL.md
- .agents/skills/the-way-maintain-instruction-files/SKILL.md
- .claude/skills/the-way-implement-task/SKILL.md
- .agents/skills/the-way-implement-task/SKILL.md
- .claude/skills/the-way-plan-task/SKILL.md
- .agents/skills/the-way-plan-task/SKILL.md

## Commands and actual output

Generation invocation exited 0:
15 sources; 30 outputs; 10 stale before; 10 equal after; 5 identical pairs; 20 other outputs untouched

### python -B agent-instructions/skill_entry_points.py

Exit: 0

```text
would create .claude/skills/the-way-lead-project/SKILL.md
would create .agents/skills/the-way-lead-project/SKILL.md
would change .claude/skills/the-way-plan-project/SKILL.md
would change .agents/skills/the-way-plan-project/SKILL.md
would change .claude/skills/the-way-define-project/SKILL.md
would change .agents/skills/the-way-define-project/SKILL.md
would change .claude/skills/the-way-refine-task/SKILL.md
would change .agents/skills/the-way-refine-task/SKILL.md
would change .claude/skills/the-way-settle-technology/SKILL.md
would change .agents/skills/the-way-settle-technology/SKILL.md
```

### python -B gate/run_tests.py agent-instructions

Exit: 1

```text
..............F...
======================================================================
FAIL: test_the_tracked_entry_points_are_what_the_generator_produces (test_skill_entry_points.TrackedEntryPoints.test_the_tracked_entry_points_are_what_the_generator_produces)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Storage\repos\the-way-wt\lead-project\agent-instructions\test_skill_entry_points.py", line 256, in test_the_tracked_entry_points_are_what_the_generator_produces
    self.assertEqual(tracked, sorted(produced),
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     "run python -B agent-instructions/skill_entry_points.py --write and "
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     "commit what it writes")
                     ^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: ['.ag[218 chars]-way-maintain-instruction-files/SKILL.md', '.a[1180 chars].md'] != ['.ag[218 chars]-way-lead-project/SKILL.md', '.agents/skills/t[1276 chars].md']

First differing element 4:
'.agents/skills/the-way-maintain-instruction-files/SKILL.md'
'.agents/skills/the-way-lead-project/SKILL.md'

Second list contains 2 additional elements.
First extra element 28:
'.claude/skills/the-way-settle-technology/SKILL.md'

Diff is 1640 characters long. Set self.maxDiff to None to see it. : run python -B agent-instructions/skill_entry_points.py --write and commit what it writes

----------------------------------------------------------------------
Ran 18 tests in 6.223s

FAILED (failures=1)
```

### python -B gate/run_tests.py gate (initial chunk)

Exit: running

```text
..................................................```

### gate continuation

Exit: running

```text
.....................................F..```

### gate final continuation

Exit: 1

```text
........
======================================================================
FAIL: test_every_skill_reaches_a_session_on_the_way (test_skills_reach_the_way_sessions.SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Storage\repos\the-way-wt\lead-project\gate\test_skills_reach_the_way_sessions.py", line 217, in test_every_skill_reaches_a_session_on_the_way
    self.assertEqual(found, [], "a skill of the-way a session would not find under its "
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     "`the-way-` name; write the entry points with `" + GENERATOR + "`:\n"
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     + "\n".join(found))
                     ^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: ['project-level/lead/skill/SKILL.md: no fi[957 chars]ct`'] != []

First list contains 6 additional elements.
First extra element 0:
'project-level/lead/skill/SKILL.md: no file .claude/skills/the-way-lead-project/SKILL.md'

Diff is 1087 characters long. Set self.maxDiff to None to see it. : a skill of the-way a session would not find under its `the-way-` name; write the entry points with `python -B agent-instructions/skill_entry_points.py --write`:
project-level/lead/skill/SKILL.md: no file .claude/skills/the-way-lead-project/SKILL.md
project-level/lead/skill/SKILL.md: no file .agents/skills/the-way-lead-project/SKILL.md
.claude/skills/the-way-plan-project/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-define-project/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-refine-task/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-settle-technology/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`

----------------------------------------------------------------------
Ran 98 tests in 19.989s

FAILED (failures=1)
```

## Results, choices and concerns

Generator preview exit 0 lists exactly ten remaining paths: two missing lead-project wrappers and eight stale project wrappers for plan-project, define-project, refine-task and settle-technology. Those paths belong to Slice 7 and were not written.
Agent-instructions: 18 tests, 1 expected failure, TrackedEntryPoints.test_the_tracked_entry_points_are_what_the_generator_produces, because the two new lead-project wrappers are not tracked yet.
Gate: 98 tests, 1 expected failure, SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way, with six explicit findings: two missing lead-project wrappers and four Claude project-wrapper sibling inventories missing lead-project. The paired Codex project wrappers are also stale per generator preview. No unrelated failures.
These are partial checks, not a full gate pass. TDD is not applicable: this is mechanical output regeneration under the explicit brief, with no new behavior or new tests.

Choice: use existing discover/produce API and exact path filter. Rejected whole --write in this slice because it would write the other ten paths outside scope and exceed the ten-file slice boundary. Cost: expected temporary incomplete-wrapper suite failures until Slice 7.
Self-review: git diff --stat shows exactly ten files, ten insertions and ten deletions; inspected generated change and byte assertions establish each difference is the added lead-project sibling. git diff --check exited 0, no output. No findings.
Root riskR1 reader output encoding is outside this write scope and remains assigned final review/fix.
Commit: 0a1846b6d5f6b92806082bc9d22e66ff896a1e31 — chore: regenerate shared and task-cycle skill wrappers. Commit command exited 0; exactly ten files, ten insertions and ten deletions. Post-commit git status --short exited 0 with no output.
