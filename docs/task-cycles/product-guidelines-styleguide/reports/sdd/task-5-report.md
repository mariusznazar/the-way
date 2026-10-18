# Task 5 report - Entry points, first batch

Commit: fbf008b `chore(agent-instructions): regenerate five skills' entry points with the maintain-styleguide sibling`
Written in process from `produce(discover(ROOT))` (script: .runs/task-cycles/product-guidelines-styleguide/reports/slice-5-write.py); no `--write`, no hand edits.

## Checks (outputs under .runs/task-cycles/product-guidelines-styleguide/reports/)
- write script: exit 0, "written 10" - slice-5-write.txt
- `python -B agent-instructions/skill_entry_points.py`: exit 0, exactly 20 `would change` lines (record-decision, record-environment-fact, record-glossary-term, record-invariant, update-part-map, maintain-instruction-files, plan-project, refine-task, settle-technology, plan-task; both tools) - slice-5-generator.txt
- `python -B gate/run_tests.py agent-instructions`: exit 1, 18 tests, 1 failure (tracked entry points != generator) - slice-5-ai-tests.txt (expected red, recorded)
- `python -B gate/run_tests.py gate`: exit 1, 98 tests, 1 failure (test_every_skill_reaches_a_session_on_the_way) - slice-5-gate-tests.txt (expected red, recorded)
- `cmp` of each .claude/.agents pair: all 5 identical.
- Neither failure output mentions any of the five regenerated skills (0 hits).

## Files changed (10, each +1 -1; only the sibling-list line gains `maintain-styleguide`)
.claude/skills/ and .agents/skills/ the-way-{critique,define-project,find-foundation-entries,implement-task,lead-project}/SKILL.md

## Sharpness inputs
Parts touched: agent-instructions entry points only (generated). No trust-boundary files, nothing irreversible, no foundations/ edits, no CRLF.

## Weakest-point check (WAY-164)
Requirement most likely unmet: "exactly as the generator produces them" / ten paths only. Check: generator dry run lists none of the ten among the 20 stale, the 20 are exactly slices 6-7's set, pairs byte-identical, git status showed only the ten paths modified. Result: met.

## Concerns
None.
