# Handoff — planner

You are the planner of one task's change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root` (task branch `task/small-fixes-from-ai-review-and-audit`, base `268b2b074691a331ed8db136343b4060bdd44539`). Start from its root.
- Method of your stage: `task-cycle/plan/SKILL.md` (`plan-task`) in that worktree. Read it whole; read a file it names (`too_large.md` and the like) only when the step that names it comes. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: write the plan and its size report, then return before any slice is made. Plan: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan.md`; size report: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan-size.md`. No code, no test, no foundation entry.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/planner-report.md`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), so write it there although its name could look like a report of the kind Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.
- Your directory for working copies: `.runs/planner/` (under the worktree's ignored `.runs/`).
- `cycle.md` and the other files of the cycle's record directory (other agents' handoffs, reports and findings) are not yours to read, unless this handoff names them. The files named below are yours.
- Spec: none. No reviewed spec exists: step 4 of the cycle found no open design choice.
- Frozen task, whole: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`. It carries nine points in *To do*; read all of it, its *Context* and *Decisions in play* included.

## Answers of the cycle's step 4

- Trust boundary: yes. The part map names `task-cycle/gate_times.py` (part `task-cycle`) and `process-audit/audit_count.py` (part `process-audit`) as trust boundaries; points 4, 5 and 8 of the task change them. A slice that changes either carries `Risk: trust boundary — <which>` and gets a review of its own. `process-audit/record_items.py`, `problem_register.py`, `record_reading.py` and `audit_shared.py` are trust boundaries of `process-audit` too: a slice that changes one of them is marked the same way.
- Irreversible operation: no.
- Open design choice: none found. Where the single place of point 9 stands is, in the orchestrator's judgment, a way of making what the task settles (WAY-256 with WAY-35 give the kind of place; `elements/common/way_of_working.md` is out of scope, so a file beside it or another file the skills can read is the way). If reading the code shows you a choice that is open in the sense of section 2 of your method, write no plan and return it, as the method says. Nothing in the task is a reserved choice.
- Pin: nothing moved; the-way itself.

## What you read (the orchestrator's selection, WAY-150, WAY-213)

Parts the change touches: `task-cycle`, `process-audit`, `environment-facts` (`elements/environment-facts/template.md`), `elements-common`, `project-level`, `product-guidelines`, `foundation-review` (the 15 skill files of point 9 stand in `elements/*`, `foundation-review`, `product-guidelines/*` and `project-level/*`), `agent-instructions` and `gate` (the invariant `skill-entry-points` and its test, `gate/test_skills_reach_the_way_sessions.py`, which point 9 may touch).

- The part map, whole: `foundations/part_map.md`. The glossary, whole: `foundations/glossary.md`.
- The index of the decisions this selection gives, written by `elements/common/decision_index.py` into the worktree: `.runs/index.md` (decisions listed in full and by heading). Read it. Open whole, each as the range from its heading to the next heading in `foundations/decisions.md`: WAY-11, WAY-33, WAY-35, WAY-84, WAY-127, WAY-160, WAY-256, WAY-330, WAY-337, WAY-339, WAY-344, WAY-350, WAY-385, WAY-404, WAY-405 and WAY-416. Of WAY-84, WAY-11, WAY-33, WAY-339 and WAY-350 the task's *Decisions in play* quotes the sentence the change touches. Read WAY-365 and WAY-361 (named by your method's rule of size) as well.
- Invariants (each whole, in `foundations/invariants.md`): `skill-entry-points`, `skill-rule-source`, `gate-times-refuses-impossible-entry`, `audit-count-refuses-record-links`, `audit-series-script-paths`, `return-step-record`, `function-and-file-size`, `formatter-layout`, `ruff-blocking-rules`.
- Guidelines (each whole): `guidelines/coding.md`, `guidelines/coding-measuring-report.md`, `guidelines/coding-check.md`, `guidelines/coding-command-runner.md`, `guidelines/coding-shared-module.md`, `guidelines/testing.md`.
- Code and tests, as far as you need them to cut slices and to name each slice's files and reading: `process-audit/audit_count.py`, `process-audit/version_analysis.py`, `process-audit/audit_report.py`, `process-audit/audit_shared.py`, `process-audit/SKILL.md`, the tests in `process-audit/`, `task-cycle/gate_times.py` with `task-cycle/test_gate_times.py`, the three files of points 1–3, and the 15 skill files of point 9 (`grep` the files git tracks for the paragraph "where the-way lies" that the-way#154 rewrote; the list stands in that request's *Technical changes* and in WAY-127's *Verification*).
- The rule of size (WAY-385, WAY-365, WAY-361): several of the files point 4–5 touches may stand over a threshold. Read the thresholds in WAY-385 and find the sizes by running the size test on the base in a worktree of your own under `.runs/planner/`, as your method's rule gives, and plan a slice that moves a part out first where a later slice adds to a file or a function over its threshold.

## Questions to answer in the plan

Settle, as ways of making and under *Choices*: where the single place of point 9's paragraph stands, and how the skills read it from there; whether WAY-127's *Verification* and the invariant `skill-entry-points` or its test need a change because of that move (the task says the foundation's rule for a shared way of working is WAY-256 with WAY-35; a change to a decision's binding sentence beyond what the task settles is not yours to plan: name it in your report as a question instead); which slices change a decision or an invariant sentence, and whether the foundation entries of the plan's *Foundation entries* are needed (the task's *Settlements to record* names three rows: 1 and 2 go to a sentence of WAY-339, 3 to a decision). The one session of point 9 that checks an agent follows the hand-over is a check made once by the cycle, not a permanent test (the testing guidelines' *Not tested on purpose*): the plan names it as a check of a slice or of the whole change, whichever fits, without making it a slice that writes a test.

## Working copies (word for word from the process of the cycle)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

## Return

Return the status, the plan's path, a one-line check result and the report's path, as your method gives. Your report holds its **Unread material** and **Searches not found or unclear** sections, as the method requires.
