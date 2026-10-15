# Slice 4 independent review

Worktree C:/Storage/repos/the-way-wt/lead-project; user delegated implement-task through a reviewable request. Root answers intermediate questions provisionally. Read C:/Users/Mariusz/.codex/AGENTS.md, worktree AGENTS.md and agent-instructions/README.md. Before vault playbooks read C:/Storage/The Brain/The Brain/Notes/Resources/(R) Obsidian/obsidian_rulebook.md, then C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/playbook_code_review.md and its delegated review-loop file. No human questions, child agents, product/vault writes or branch/index/HEAD mutation.

Use full C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/task-reviewer-prompt.md. Brief .superpowers/sdd/plan/task-4-brief.md; report task-4-report.md beside it. Read supplied package once; focused named cross-boundary checks only, no green suite rerun. Full report .superpowers/sdd/plan/task-4-review.md has both verdicts, full anchored findings and evidence/limits. Exact base/head/package appended before dispatch.

Read full frozen task/spec and current whole selected foundation under WAY-150. Judge three-file diff independently. Concrete checks: new registry entry points at the committed lead source, product wrappers are pinned and identical for both tools, documentation matches actual inventory, meaningful ordinary tests exercise preview/apply/repeat, initialized source and preservation/mismatch refusal, with no unrelated registry or installer behavior change. Existing invariant tests are read-only; do not accept a fixture that tests an old source commit or derives its expected answer from the implementation. Protect source task/plan data. Missing/stale repository wrappers remain assigned later slices; independently distinguish that actual cause from an unexpected installer failure. Full generation must pass before final completion.

## Binding source text (verbatim from spec)

## Components and ownership

| Component | Responsibility |
|---|---|
| `project-level/lead/skill/SKILL.md` | Project orchestration, state reconciliation, round selection, dispatch, human package, final acceptance and plan/definition change routing. |
| `project-level/lead/conversation_template.md` | The one file conversation contract, actor permissions, statuses and resumption rules. |
| `project-level/lead/answering.md` | The answering-agent instructions, reached through the conversation file; this is not a second user-invoked skill. |
| `project-level/plan_state.py` | Python 3.14, standard-library state reader; starts only Git, emits proposals and evidence, never edits the plan or task documents. |
| `project-level/task/skill/SKILL.md` | Existing refinement with an orchestrated mode; manual refinement retains direct conversation and gains explicit complete-document acceptance. |
| Existing plan/definition/task-cycle skills and templates | Carry the accepted changes to dependency semantics, handover and delegated question/critique routing. |
| Entry-point generator and installer registry | Expose `the-way-lead-project` both in the-way and in newly installed product repositories. |

The skill and companion files follow this worktree or the product's pinned `.the-way`; every the-way skill handoff uses the `the-way-` prefix. The new skill's description distinguishes leading a handed-over plan from defining/breaking down a project, refining one task, and running a task cycle. No global skill or personal file is a runtime dependency.

Only one actor writes a particular conversation at a time. Different refiners write different task documents and conversations in parallel; they never change the shared plan, definition or foundation. The project orchestrator owns ordinary plan state/Document-cell updates and their change-log lines. A dispatched plan-project agent owns a structural plan edit while that edit runs; the project orchestrator pauses its own plan writes until the agent returns.


Run changed-part suites through `python -B gate/run_tests.py project-level`, `... agent-instructions`, `... installation`, `... task-cycle`, and the existing critical-flow suite `... gate`; regenerate entry points with `python -B agent-instructions/skill_entry_points.py --write` and verify them. Adding one skill changes every generated sibling list, so all generated differences belong to this task. Installer tests use a committed checkout and verify the new product wrapper and existing preservation rules. Update installer documentation to the actual skill inventory, avoiding stale numeric wrapper claims.

## Final dispatch

Base74750b340769fe1c397adaff12ece77acc8350e7; head9c471a2a6dae5f2f53be882dbf888d499826cc28; package .superpowers/sdd/plan/review-74750b3..9c471a2.diff. Standard model gpt-6.1-sol. Root read three final files/diff and full report; hashes unchanged at commit. Installation30pass; gate97/98, same incomplete repository-wrapper case. Existing product pin-move protocol intentionally unchanged.
