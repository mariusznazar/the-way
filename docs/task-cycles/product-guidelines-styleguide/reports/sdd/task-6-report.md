# Task 6 report - Entry points, second batch

Commit: see `git log -1` on branch task/product-guidelines-styleguide, message "chore(agent-instructions): regenerate five more skills' entry points with the maintain-styleguide sibling".
Written in process from `produce(discover(ROOT))` (script: .runs/task-cycles/product-guidelines-styleguide/reports/slice-6-write.py, slice 5's script with the five names changed); no `--write`, no hand edits.

## Checks (outputs under .runs/task-cycles/product-guidelines-styleguide/reports/)
- write script: exit 0, "written 10" - slice-6-write.txt
- `python -B agent-instructions/skill_entry_points.py`: exit 0, exactly 10 `would change` lines (record-glossary-term, record-invariant, update-part-map, refine-task, settle-technology; both tools) = slice 7's set - slice-6-generator.txt
- `python -B gate/run_tests.py agent-instructions`: exit 1, 18 tests, 1 failure (tracked entry points != generator; names record-glossary-term) - slice-6-ai-tests.txt (expected red, recorded)
- `python -B gate/run_tests.py gate`: exit 1, 98 tests, 1 failure - slice-6-gate-tests.txt (expected red, recorded)
- `cmp` of each .claude/.agents pair: all 5 identical.
- `git diff --check` on the commit: exit 0. Files are i/lf.

## Files changed (10, each +1 -1; only the sibling-list line gains `maintain-styleguide`)
.claude/skills/ and .agents/skills/ the-way-{maintain-instruction-files,plan-project,plan-task,record-decision,record-environment-fact}/SKILL.md

## Sharpness inputs
Parts touched: agent-instructions entry points only (generated). No trust-boundary files, nothing irreversible, no foundations/ edits.

## Weakest-point check (WAY-164)
Requirement most likely unmet: "exactly as the generator produces them", ten paths only. Check: generator dry run no longer lists any of my ten and lists exactly the 10 remaining paths of slice 7; pairs byte-identical; git status before commit showed only the ten paths modified; none of my five skills is a failing path in the two red test outputs (the one "plan-project" text hit is inside the failure message about record-glossary-term's sibling list). Result: met.

## Concerns
None.
