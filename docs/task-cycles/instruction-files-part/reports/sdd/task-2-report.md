# Task 2 report: entry points of maintain-instruction-files

Status: DONE
Commit: 588e0a3 feat(agent-instructions): Add the entry points of maintain-instruction-files
Branch: task/instruction-files-part (base of this task: d87d74f)

## Step 1: RED (before generating)

Command:
```
python -B gate/run_tests.py gate | grep -E "^(FAIL|ERROR):|^Ran"
python -B gate/run_tests.py agent-instructions | grep -E "^(FAIL|ERROR):|^Ran"
python -B agent-instructions/skill_entry_points.py | awk '{print $1, $2}' | sort | uniq -c
```
Output:
```
FAIL: test_every_skill_reaches_a_session_on_the_way (test_skills_reach_the_way_sessions.SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way)
Ran 98 tests in 16.342s
FAIL: test_the_tracked_entry_points_are_what_the_generator_produces (test_skill_entry_points.TrackedEntryPoints.test_the_tracked_entry_points_are_what_the_generator_produces)
Ran 18 tests in 4.169s
     22 would change
      2 would create
```
Matches the brief: the two known FAILs, and the dry run reports 22 changes and 2 creations. Nothing was written by the dry run; `git status` was clean before and after.

## Step 2: generate and stage

Command:
```
python -B agent-instructions/skill_entry_points.py --write > .runs/task-cycles/instruction-files-part/reports/check_2_generate.txt; echo "generate $?"
grep -c "^created" <report>; grep -c "^changed" <report>
python -B agent-instructions/skill_entry_points.py && git add .claude/skills .agents/skills && git status --short | awk '{print $1}' | sort | uniq -c
cmp .claude/skills/the-way-maintain-instruction-files/SKILL.md .agents/skills/the-way-maintain-instruction-files/SKILL.md && echo identical
```
Output:
```
generate 0
2
22
entry points are current
      2 A
     22 M
identical
```
Matches the brief's expected output exactly.

## Step 3: GREEN

Command and output:
```
python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl > .../check_2_tests_agent_instructions.txt 2>&1; echo "agent-instructions $?"
  -> agent-instructions 0
  -> tail -1: OK
python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl > .../check_2_gate.txt 2>&1; echo "gate $?"
  -> gate 0
  -> tail -1: OK
grep -c '"fail"' .runs/gate-tests.jsonl
  -> 0
python -B elements/part-map/format_guard.py foundations/part_map.md --base none | tail -1
  -> 0 error(s), 0 warning(s), 7 unchecked
```
Matches the brief's expected results (agent-instructions OK; gate OK; 0 fail lines; part map 0 errors, 0 warnings, 7 unchecked). The gate ran 98 tests, as expected.

## Step 4: commit

Command: `git commit -m "feat(agent-instructions): Add the entry points of maintain-instruction-files" -m "Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" -- .claude/skills .agents/skills`

Result: commit 588e0a3, 24 files changed (2 created, 22 modified), 52 insertions, 22 deletions. `git status --short` is empty afterwards.

## Files changed

Created:
- `.claude/skills/the-way-maintain-instruction-files/SKILL.md`
- `.agents/skills/the-way-maintain-instruction-files/SKILL.md` (byte-identical to the Claude copy)

Modified (generator output, one line each: the sentence naming the skills gains `maintain-instruction-files`):
- the 22 other entry points under `.claude/skills/the-way-*/SKILL.md` and `.agents/skills/the-way-*/SKILL.md`

No file under `foundations/` and no `agent-instructions/test_instruction_files.py` was touched. No code was written by hand.

## Concerns

None blocking. Note that the gate and agent-instructions checks are partial checks in the sense of `agent-instructions/README.md`; a green result here is not a pass of the full gate.
