# Slice 5 implementation report

Status: DONE. Mechanical generation complete within ten-path boundary.

## Inputs and foundation selection

Source revision / BASE: 9c471a2a6dae5f2f53be882dbf888d499826cc28

Read frozen task, spec, planner ruling, generator and tests; complete part map identifies agent-instructions as the touched part because generated files belong to their generator. Refreshed selection through current Scope fields and WAY-127, WAY-150, skill-entry-points/1; read supplied source skills. No source frontmatter, foundation, generator or test was edited. Root retains reader-output encoding risk R1 outside this slice.

## Generation and verification

Ran an in-process Python script from the worktree, importing skill_entry_points through sys.path.insert(0, agent-instructions). Exact generation API:

```python
skills = g.discover(Path.cwd())
outputs = g.produce(skills)
paths = [f"{directory}/the-way-{name}/SKILL.md"
         for name in ["record-decision", "record-environment-fact",
                      "record-glossary-term", "record-invariant", "update-part-map"]
         for directory in g.ENTRY_DIRECTORIES]
for path in paths:
    (Path.cwd() / path).write_bytes(outputs[path].encode("utf-8"))
```

Inventory assertions: 15 source skills, 30 generated outputs, 10 selected output paths. Before writing, all ten existed and differed from produce bytes. After writing, every selected path equalled produce bytes and all five tool pairs were byte-identical. No hand-edited prose. TDD not applicable: existing generator output only, no new behavior or tests.

Changed paths:

- `.claude/skills/the-way-record-decision/SKILL.md` ? stale before, equal after.
- `.agents/skills/the-way-record-decision/SKILL.md` ? stale before, equal after.
- `.claude/skills/the-way-record-environment-fact/SKILL.md` ? stale before, equal after.
- `.agents/skills/the-way-record-environment-fact/SKILL.md` ? stale before, equal after.
- `.claude/skills/the-way-record-glossary-term/SKILL.md` ? stale before, equal after.
- `.agents/skills/the-way-record-glossary-term/SKILL.md` ? stale before, equal after.
- `.claude/skills/the-way-record-invariant/SKILL.md` ? stale before, equal after.
- `.agents/skills/the-way-record-invariant/SKILL.md` ? stale before, equal after.
- `.claude/skills/the-way-update-part-map/SKILL.md` ? stale before, equal after.
- `.agents/skills/the-way-update-part-map/SKILL.md` ? stale before, equal after.

Source inventory:

- `elements/common/critique/SKILL.md`
- `elements/common/skill/SKILL.md`
- `elements/decisions/skill/SKILL.md`
- `elements/environment-facts/skill/SKILL.md`
- `elements/glossary/skill/SKILL.md`
- `elements/invariants/skill/SKILL.md`
- `elements/part-map/skill/SKILL.md`
- `instruction-files/SKILL.md`
- `project-level/lead/skill/SKILL.md`
- `project-level/plan/skill/SKILL.md`
- `project-level/skill/SKILL.md`
- `project-level/task/skill/SKILL.md`
- `project-level/technology/SKILL.md`
- `task-cycle/plan/SKILL.md`
- `task-cycle/skill/SKILL.md`

## Actual command results

The two suite failures below are expected temporary incompleteness of the other two wrapper batches, not a full gate pass. All remaining paths appear in the generator dry-run output. No remaining path was written. Agent-instructions: 18 tests, 1 failure (tracked inventory lacks both lead-project wrappers). Gate: 98 tests, 1 failure (9 stale Claude sibling lists and 2 absent lead-project wrappers).

### `python -B agent-instructions/skill_entry_points.py`

Exit: 0

```text
would change .claude/skills/the-way-critique/SKILL.md
would change .agents/skills/the-way-critique/SKILL.md
would change .claude/skills/the-way-find-foundation-entries/SKILL.md
would change .agents/skills/the-way-find-foundation-entries/SKILL.md
would change .claude/skills/the-way-maintain-instruction-files/SKILL.md
would change .agents/skills/the-way-maintain-instruction-files/SKILL.md
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
would change .claude/skills/the-way-plan-task/SKILL.md
would change .agents/skills/the-way-plan-task/SKILL.md
would change .claude/skills/the-way-implement-task/SKILL.md
would change .agents/skills/the-way-implement-task/SKILL.md

```

### `python -B gate/run_tests.py agent-instructions`

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
Ran 18 tests in 5.046s

FAILED (failures=1)
```

### `python -B gate/run_tests.py gate`

Exit: 1

```text

.......................................................................................F..........
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
AssertionError: Lists differ: ['.claude/skills/the-way-critique/SKILL.md[1997 chars]ct`'] != []

First list contains 11 additional elements.
First extra element 0:
'.claude/skills/the-way-critique/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`'

Diff is 2202 characters long. Set self.maxDiff to None to see it. : a skill of the-way a session would not find under its `the-way-` name; write the entry points with `python -B agent-instructions/skill_entry_points.py --write`:
.claude/skills/the-way-critique/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-find-foundation-entries/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-maintain-instruction-files/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
project-level/lead/skill/SKILL.md: no file .claude/skills/the-way-lead-project/SKILL.md
project-level/lead/skill/SKILL.md: no file .agents/skills/the-way-lead-project/SKILL.md
.claude/skills/the-way-plan-project/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-define-project/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-refine-task/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-settle-technology/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-plan-task/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`
.claude/skills/the-way-implement-task/SKILL.md: no sentence holding the words "with the `the-way-` prefix, never an unprefixed one" names, in backticks, every skill of the-way; none names `lead-project`

----------------------------------------------------------------------
Ran 98 tests in 15.324s

FAILED (failures=1)
```

### `git diff --check`

Exit: 0

```text


```

### `git diff --stat`

Exit: 0

```text
 .agents/skills/the-way-record-decision/SKILL.md         | 2 +-
 .agents/skills/the-way-record-environment-fact/SKILL.md | 2 +-
 .agents/skills/the-way-record-glossary-term/SKILL.md    | 2 +-
 .agents/skills/the-way-record-invariant/SKILL.md        | 2 +-
 .agents/skills/the-way-update-part-map/SKILL.md         | 2 +-
 .claude/skills/the-way-record-decision/SKILL.md         | 2 +-
 .claude/skills/the-way-record-environment-fact/SKILL.md | 2 +-
 .claude/skills/the-way-record-glossary-term/SKILL.md    | 2 +-
 .claude/skills/the-way-record-invariant/SKILL.md        | 2 +-
 .claude/skills/the-way-update-part-map/SKILL.md         | 2 +-
 10 files changed, 10 insertions(+), 10 deletions(-)

```

## Self-review and choices

Diff: ten files, one added/removed sibling-list line per file, adding only lead-project in source order. All other wrapper text matches generator. git diff --check passed. Explicit byte and pair assertions passed. Full generator without --write correctly leaves twenty paths for subsequent slices. Chosen existing discover/produce filtering follows planner ruling; whole --write now would exceed the ten-path slice boundary. Cost: temporary failing complete-inventory suites until remaining batches land. No unresolved slice concern; no child agents, protected test edits, merges or pushes.

Commit: pending explicit ten-path commit; appended below after creation.

Created commit: 6b23e0b37a050d5fec45e948b047953d7a50baf8 ? chore: regenerate foundation entry skill wrappers.
