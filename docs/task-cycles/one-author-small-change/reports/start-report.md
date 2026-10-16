# Start and baseline

Actor: root orchestrator, inherited GPT-6 family. Date: 2026-10-16.
Repository and process base: dc433059ffc7f94f9aaa43588dfe94ac869fb635. Target foundations, equal to freshly fetched origin/foundations; clean initial checkout. Isolated worktree branch task/one-author-small-change created with --no-track. No mismatched upstream.

Frozen task ../task.md is independent, ready for cycle, with five accepted settlements and no human actions. The named decision meanings are intentionally revised by that accepted task. Existing process requires a plan for this cycle; the changed process is the deliverable. No spec: no open design choice remains in the task. Touched semantic parts: task-cycle and generated agent-instructions, high criticality. No trust boundary or irreversible action.

## Foundation reading

Read complete part map and shared reading method. Inspected every current Scope, including wrapped continuation lines, from the complete decision log. All versions are /1, no repeal found. Expected Scope matches and entries read whole: WAY-01,03,09,10,11,13,16,21,25,26,27,28,30,33,34,36,37,38,44,45,46,47,48,51,55,57,62,63,65,68,69,82,89,100,101,102,103,106,120,124,125,126,127,128,129,130,131,132,133,134,135,136,140,144,147,148,149,150. Extra whole entries for relevant approval, verification and incoming-link rules: WAY-07,12,14,17,22,31,35,114. Read entire glossary and current invariant Part fields; read whole entries naming every, task-cycle or agent-instructions. Scope matches equal read selection. Part-map critical flows and their invariants are included. Source locations are headings in foundations/decisions.md, foundations/invariants.md and foundations/glossary.md at the base commit; planner report supplies line ranges.

Search across foundation for WAY-30/36/135/136 incoming fingerprints, plan/every task/one-slice/no-plan/spec wording finds no incoming fingerprints for the changed binding entries. Finds WAY-13 nonbinding explanation, WAY-30 known-decision-change carrier, WAY-36 temporary-rule carrier. The foundation author must perform and record complete WAY-33 semantic search across all five elements before writing, and repeat before request.

## Rulings

1. Revise WAY-13 examples/rationale only to describe no-plan route. Keeping stale examples misleads later cycles; updating them leaves the same binding safeguards.
2. WAY-30's known-revision approval is carried by the accepted task on a no-plan route, by the plan when present; human approval and stopping on an unexpected contradiction remain. The accepted no-plan foundation-change settlement entails this carrier update. Requiring a plan here would silently exclude the intended foundation changes.
3. WAY-36's temporary rules may live in the cycle choice record without a plan. Existing record already carries temporary choices; permanent rules still go in the foundation. Preserving an exclusive plan carrier would create a compulsory plan by another rule.

## Baseline checks

Python 3.14.3. Commands run in isolated worktree, before tracked edits:
- python -B gate/run_tests.py task-cycle: exit 0, 41 tests, OK; baseline-task-cycle.txt.
- python -B gate/run_tests.py gate: 98 tests, OK; baseline-gate.txt.
- python -B gate/run_tests.py agent-instructions: 18 tests, OK; baseline-agent-instructions.txt.
- python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --today 2026-10-16 --record .runs/task-cycles/one-author-small-change/reports/baseline-decisions.jsonl: exit 0, zero errors; five pre-existing overdue reviews WAY-03,21,52,55,69 (2026-10-02); five comparison checks unchecked because no main.
- python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none --record .runs/task-cycles/one-author-small-change/reports/baseline-invariants.jsonl: exit 0, zero errors/warnings, three no-main checks unchecked; no human_verdicts.md.
- python -B elements/part-map/format_guard.py foundations/part_map.md --base none --record .runs/task-cycles/one-author-small-change/reports/baseline-part-map.jsonl: exit 0, zero errors/warnings; three no-main checks unchecked; both critical-flow part lists unchecked (no coverage), promise change paths unchecked (no command), dependency graph and violations comparison unchecked (no command).

These are partial checks, not the full gate, which does not exist. The new no-plan route has not run in a real task pilot; runtime cost improvement remains unmeasured by this change.
