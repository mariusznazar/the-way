# Handoff — reviewer of the spec of the task `scripts-after-foundation-review`

You review a spec in a task cycle of the-way (`implement-task`) as an agent that did not write it.
The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing
here is the human's approval. Ask no human; questions go to the orchestrator.

- Worktree (work from its root): `the root of the task's worktree`, base `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The-way is the checkout you work in.
- Method, read whole: `task-cycle/spec/SKILL.md` (`write-spec`); variant: the reviewer of a spec. Read `review.md` beside it when its step comes. You have no skill tool.
- Spec to review: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/spec-review-report.md`; its first line is `PASS` or `FAIL`.
- The designer's report, for what it found unclear: `.runs/task-cycles/scripts-after-foundation-review/reports/designer-report.md`. Its four readings that carry weight, which you judge: (1) WAY-344's "a change that reworks how a script reads a file" includes adding one field, so the whole Claude Code transcript reading of `task-cycle/cycle_stages.py` comes under WAY-344; (2) one write column present without the other is a missing field (exit 1 with `Error:`, the cost `unknown`); (3) the audit requires both write columns in every table of the price list (OpenAI's gets `—`), and a table without them ends with exit 2; (4) a Warning, not an error, where the two lifetimes do not add up to `cache_creation_input_tokens`.
- What the spec has to settle (and nothing more): the route by which the audit count receives, for each stage row and model, the cache writes of each lifetime; the foundation sentences the route makes untrue and their new wording; what the route requires of each script. Settled by the task and not for you to reopen: the two exceptions of WAY-344, the two kinds of series, the unknown measure of a tool the cycle changes, the new price-list column.
- Trust boundary: yes (`process-audit/audit_count.py`, `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`).
- Check in particular: whether any foundation entry besides WAY-339 and WAY-344 is made untrue by the route (the designer searched `foundations/` for cache write, stage report, `cycle_stages`, `cycle_measures`, price list and "never columns"); whether the route breaks what the audit reads today of `stages.md` (read the detailed section code in `process-audit/audit_count.py`, about lines 920–1044 and 1255–1316, and the Claude Code reading in `task-cycle/cycle_stages.py`, about lines 500–630); whether D4's "whole reading under WAY-344" asks what the decision asks and no more; whether the spec asks for anything the task excludes.
- Directory for your working copies: `.runs/spec-review/`.

## What you read (named by the orchestrator, WAY-150)

`foundations/decisions.md`, each whole (heading `### WAY-nnn`): WAY-337, WAY-339, WAY-344, WAY-330, WAY-350, WAY-38, WAY-07, WAY-135. `foundations/invariants.md`: `audit-series-script-paths`, `script-language`, `script-imports`, `script-subprocesses`. `foundations/part_map.md`: entries `task-cycle` and `process-audit`. `foundations/glossary.md` whole.

## Working copies

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
