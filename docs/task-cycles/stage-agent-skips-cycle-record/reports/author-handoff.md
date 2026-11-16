# Handoff — the one author of the change

Stage: the whole change as the one author. Boundary: you make the change and its foundation entries, commit them on the task branch and return before any review; you take no return step now (you will be resumed for it) and you run no full gate (no handoff tells an agent to run the product's gate).

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Never label an answer as that person's approval. Where you need an answer, put your question in your report and return `questions`.

## Where you work

- Worktree (your working directory): `the root of the task's worktree`, branch `task/stage-agent-skips-cycle-record`, base `3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898` (target branch `foundations`). Work only there.
- Your directory for working copies: `.runs/author/` of the worktree.
- Your report path: `.runs/task-cycles/stage-agent-skips-cycle-record/reports/author-report.md`

## Method

Read `task-cycle/change/SKILL.md` whole, variant "the whole change as the one author". Read a file it names, one beside it included, only when the step or variant that names the file comes. The foundation step is `task-cycle/skill/foundation_step.md`: read it when you write the decision entry, and the `SKILL.md` of the element (`elements/decisions/`, at the path `foundation_step.md` gives) when you write that entry.

The cycle record directory `.runs/task-cycles/stage-agent-skips-cycle-record/` holds the cycle's log (`cycle.md`) and the files of other agents. Only the files this handoff names are yours to read there: `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read unless this handoff names them. The files this handoff names there are this handoff and the frozen task.

## Task and answers of step 4

- The frozen task: `.runs/task-cycles/stage-agent-skips-cycle-record/task.md` — read it whole. It is `ready for cycle`, `Project relation: independent`.
- Trust boundary: no. Irreversible operation: no. Open design choice: none — the task's *Questions to settle* are answered: 1 a, 2 b, 3 a. Reserved choice: none. Route: one author without a plan.
- Checks failing on the base: none.

## What to make

The task's *To do* gives two items: the sentence in `task-cycle/skill/SKILL.md` on the list of what every handoff carries (the sentence that opens "The handoff gives the user's delegation" and ends "and the report path."), and the change of WAY-148 in `foundations/decisions.md` as the task's *Decisions in play* gives it. The task's *Settlements to record* row 1 is the settlement the foundation step writes; it is the decision's change, not a new decision.

Words you take word for word from the task: the sentence for the skill is "It tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them."

Foundation to read, by identifier, in `foundations/decisions.md` (find the entry by its heading, read whole the range from its heading to the next heading): WAY-148 (the entry you change, with its *Rejected*), WAY-150, WAY-10, WAY-368, WAY-370 (the entries the task's *Decisions in play* names; WAY-368 and WAY-370 are named to be kept as they are). Selected parts: `task-cycle` and `decisions` of `foundations/part_map.md`. Read the glossary entries of the terms you use. Read `guidelines/coding.md` whole only if you change code, and `guidelines/testing.md` whole only if you write or change a test; the change is expected to be text only. `task-cycle/test_request_check.py` quotes WAY-148 at its line 61; check whether any test cites WAY-148 by `decision:` and whether `python -B elements/common/foundation_check.py` passes after your change.

After the entry is settled, search the foundation once for the entries the change touches and correct them in the same change (WAY-33).

## Checks you run

The focused checks of the directories the change touches and the foundation check (`python -B elements/common/foundation_check.py`, without `--skip-test-citations`). Give each with its command and exit code in the report, with the own-work check `make-change` asks for.

## Working copies (word for word)

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
all the same and names in the report the remainder, with its full path and the reason it stayed.

## Your return

Write the full report to your report path as `make-change` gives it, with **Unread material** and **Searches not found or unclear** (each `none` or the items), the own-work check and the working copies line. Return the status, your commits, a one-line check result naming what failed or did not run, and the report's path. Commit by path (`git add <file> …`), never `git add -A`; commit messages in English.
