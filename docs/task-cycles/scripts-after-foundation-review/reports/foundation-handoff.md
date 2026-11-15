# Handoff — the agent of the plan's *Foundation entries*, task `scripts-after-foundation-review`

You write the foundation entries of a task cycle of the-way (`implement-task`) before any slice is
made. The person who requested the cycle has delegated intermediate choices to the orchestrator;
nothing here is the human's approval. Ask no human: a question you cannot settle by the files below
returns with the status `questions` or `blocked`, as `task-cycle/skill/foundation_step.md` gives.

## Where and what you make

- Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`, base `7f5c5a56f67d9ff40554240594ca0bde59773cb3` (target `foundations`). The-way is the checkout you work in; it is no product's `.the-way`.
- Method of your stage: `task-cycle/change/SKILL.md` (`make-change`) — you take none of the rows of its table of variants; your stage is the foundation step, and your handoff is this file. Read the `SKILL.md` whole and `task-cycle/skill/foundation_step.md` whole; each file either names, only when its step comes. You have no skill tool: a skill a file names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file. The skill of each element is `elements/decisions/skill/SKILL.md` for a decision and `elements/glossary/skill/SKILL.md` for a glossary term; each selects what you read for the entry you write (the templates, `elements/common/rules.md`, `elements/common/way_of_working.md`). The checks of the form: `python -B elements/common/foundation_check.py --skip-test-citations` from the worktree's root, as `way_of_working.md` step 4.3 gives; run it after each entry and at the end. You run no other check and never the gate (WAY-160).
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec (read the passages named below; its D3 binds the wording of two entries): `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md`, its section *Foundation entries* is your list.
- Answers of step 4: trust boundary yes (code of other slices; none of your files); irreversible operation none.
- Your commits: one commit for each entry (or one for all if they touch one file in one change), on the task branch, each message in English. Do not commit anything under `.runs/`. Add files by path, never `git add -A`.
- Report: `.runs/task-cycles/scripts-after-foundation-review/reports/foundation-report.md`, in the form `make-change` gives for a report of the foundation step: status; commits; for each entry one sentence of its meaning in English and one in Polish (the language of the task document), marked `row <n>`, `projected` or `the cycle's`; the checks with command and exit code; **Unread material**; **Searches not found or unclear** (each item or `none`); the working copies line. Your own-work check as `make-change` section 5 gives it.
- Directory for your working copies: `.runs/foundation/`.

## The entries you write (the plan's table, copied)

| Entry | Kind | From |
|---|---|---|
| WAY-339 | decision, rewritten in place (WAY-07), with its *Verification*, *Rationale* and *Rejected*: the task's rows 3 and 4 (two kinds of series; the measure of a tool the cycle changes, `unknown`) and, as the spec's D3 words it, the tokens written to the cache by lifetime as columns of the stage report only as an input of the cost, the cache-use measures staying in the file of the measures, `task-cycle/cycle_stages.py` the script that measures the cost and records the columns, the *violates* and *complies* lines, the price of the columns in *Rationale*, ways A and B of D1 in *Rejected* | rows 3 and 4 of *Settlements to record*; spec D3; *Decisions in play*; questions 2 and 4 |
| WAY-344 | decision, rewritten in place (WAY-07), with its *Verification* and *Rationale*: the tables *Weights* and *Costs of an occurrence* without a level; the missing entry `repository` under `the-way`; and, as the spec's D3 words it, the earlier form of `stages.md` without the two columns of the cache writes (read with no `Error:`, its cost given as the approximation, no value made `unknown` by the missing columns) and one of the two columns alone as a missing field | rows 1 and 2 of *Settlements to record*; spec D3; question 1 |
| WAY-337 | decision, unchanged (read only): the spec's D3 finds none of its sentences made untrue | spec D3 |
| glossary: the term for a Markdown file (`.md`, `.markdown`, `.mdx`, `.mdc`) | glossary entry, new, written in plain words as row 8 says; your search of the whole foundation (WAY-33) corrects the other uses of "Markdown file" that mean `.md` alone and you report a correction that would change the meaning of an approved decision | row 8 of *Settlements to record*; question 8 |

Rows 5, 6 and 7 of *Settlements to record* go to code, data and a test: you write nothing for them.

## What you read (named by the orchestrator, WAY-150)

- From the frozen task, the passages the rows carry word for word: *Settlements to record* rows 1–4 and 8 (`task.md:143-146`, `task.md:150`), the answers of *Questions to settle* 1, 2, 4 and 8 with their *Not chosen* and their sources (`task.md:51-58`, `task.md:59-64`, `task.md:70-74`, `task.md:91-95`), the *Decisions in play* entries WAY-339, WAY-344 and WAY-320 (`task.md:127-135`), *Context* (`task.md:104-115`).
- From the spec: D1's ways A and B (`spec.md:100-130`), D1's price of the route (`spec.md:132-135`), **D3 whole** (`spec.md:180-248`). The spec's D3 binds the wording of the two decisions for the cache columns; where it differs from the task's row, the task binds.
- Foundation entries, each whole (`foundations/decisions.md`, heading `### WAY-nnn`): WAY-339, WAY-344, WAY-337, WAY-320, WAY-324, WAY-07, WAY-33, WAY-95, WAY-97, WAY-99, WAY-35, WAY-150 and WAY-30. Invariants whose sentence names a Markdown file or the tracked check: `tracked-file-private-paths`, `test-method-citation`. `foundations/glossary.md` and `foundations/part_map.md`: whole (short).
- You read the code that makes a sentence true only as far as the entry needs it: `task-cycle/tracked_private_paths_check.py` (the module description) for the glossary term; `process-audit/audit_count.py` (the module description, lines about 1–330) for the list of the earlier forms of `stages.md` and for *Weights*/*Costs of an occurrence* in WAY-344.

## Limits

- You write entries only; no code, no test, no `description:` of a skill. The wording of every sentence is yours (WAY-134); its meaning is the row's and the spec's.
- WAY-339 and WAY-344 are rewritten in place (WAY-07): the entry carries only its current wording; no history of attempts or dates of events in it: the entry describes the current state, not the way to it.
- A decision's *Rejected* takes the ways the sources keep: the task's *Not chosen* of the questions and ways A and B of the spec's D1; `unknown` or `none considered` only where the sources give none.
- Another task (“the way: small fixes after the requests #117 to #121”) changes the same sentence of WAY-344 and the file `elements/common/foundation_check.py`; do not wait for it. The cycle that merges second reconciles; where you can write your sentence so that the two edits stay apart, do.
- Return `blocked` with the question for a human only in the cases `foundation_step.md` names.

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
