# Handoff — the one author — decisions-log-after-foundation-review

## Delegation

The human who requested this cycle delegated every intermediate choice to the orchestrator; you ask
no human. Your answers come from the frozen task, its sources, the foundation and the code. Your
go-ahead is provisional, never the human's approval.

## What you make

Your variant of `make-change`: **the whole change as the one author**. You make the whole change of
the frozen task, with its foundation entries (the foundation step), and return before any review.
No plan and no spec exist: the route is one author without a plan, and the cycle found no open
design choice. The cycle's orchestrator runs the product's full gate, the return step and the
reviews; you run no full gate and take no return step now.

- Worktree (work from its root): `the task's worktree`, branch `task/decisions-log-after-foundation-review`, base commit `0dae56b` (merge of PR #134). Work only there. Do not switch branches, do not push, do not touch `.runs/task-cycles/`.
- Method: `task-cycle/change/SKILL.md` in that worktree. Read it whole; read a file it names only when the step that names it comes.
- Foundation step: `task-cycle/skill/foundation_step.md`, read whole. Each entry is written by following the `SKILL.md` of its element (`elements/decisions/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`, `elements/environment-facts/skill/SKILL.md`, …), which selects the reading it needs. You have no skill tool: read each as a file.
- The repository's own rule for work on the-way as the top-level repository: `agent-instructions/README.md`, read whole before you start. Its "Make the change" search of the whole foundation (WAY-33) is yours once an entry is settled; the return step compares afterwards and is not yours now.
- Frozen task, read whole: `.runs/task-cycles/decisions-log-after-foundation-review/task.md` in the worktree (235 lines; accepted by the human 2026-11-15, status `ready for cycle`). *To do* 1–19 and *Settlements to record* rows 1–11 are your change.
- Report path: `.runs/task-cycles/decisions-log-after-foundation-review/reports/author-report.md`.
- Your directory for working copies: `.runs/author/` directly under `.runs/` of the worktree.

## Answers of step 4 of the cycle

- Touches a trust boundary: no.
- Holds an operation that cannot be undone: no.
- Open design choice: none. Reserved choice: none. Route: one author without a plan; your class is `same` as the orchestrator's.

## What to read (selected by the orchestrator)

- The frozen task whole, and from it every entry of *Decisions in play* **whole** in `foundations/decisions.md`, under its heading `### WAY-NN` with *Rationale* and *Rejected*: WAY-229, 27, 320, 287, 35, 241, 44, 162 (the ones the task changes); WAY-05, 09, 52, 173, 372 (the ones it sets against the change); WAY-10, 90, 121, 124, 126, 140, 147, 161, 206, 216, 237, 243, 255, 313, 328, 330, 339, 360, 363, 365 (the ones it changes in *Rationale*, *Rejected*, *Based on*, *Verification* or line breaks only); and, to check them against the new text, WAY-85, 127, 129, 132, 141, 308, 316, 350, 71, 25, 36, 114, 134, 135, 136.
- The invariants the task changes or sets in play, whole in `foundations/invariants.md`: `repository-file-location`, `elements-no-pending-marker`, `generated-overview`, `installation-claude-guidance`, `tracked-file-private-paths`, and any invariant that cites a decision you change.
- The environment facts the task changes, whole in `foundations/environment_facts.md`: `openai-model-states`, `claude-code-imports`, `anthropic-model-states`, `claude-code-project-skills`, `claude-code-subagent-cache-ttl`, `claude-code-subagent-cache-ttl-credits`, and the prompt-caching facts WAY-255 already cites.
- `foundations/part_map.md`: the entries of the parts you touch, and the entry "External context" (item 19.20 changes its sentence on the script of the gate; note that the task gives item 19.23, WAY-44, and leaves out the part-map items P6 and P26, which another task carries).
- Files named by *To do*: `agent-instructions/README.md`, `elements/common/test_elements_pending_marker.py`, `product-guidelines/testing/template.md`, `product-guidelines/styleguide/starting_rules.md`, `project-level/plan/skill/cut_tasks.md`, `project-level/task/skill/` (the refinement files item 18 names), `product-guidelines/audit_end.md`, `product-guidelines/coding/hand_back.md`, `instruction-files/tool_loading.md`, `task-cycle/skill/SKILL.md`.
- Guidelines of the product: the-way has no `guidelines/` of its own for code or tests (WAY-328's transitional departure), so no guideline file applies.
- Every file you change, whole, before you change it — for `foundations/decisions.md` that means the entry whole; the file is large, do not read it whole.

The line numbers in the task refer to commit `21ecb62`; the base is `0dae56b`. Find each place by the quoted text, not by the number. Where a quoted text does not stand at the base as the task says, name it in your report and do not guess.

## Boundaries and cautions

- The change is texts of the foundation and of method files; no code except a comment of `elements/common/test_elements_pending_marker.py` (item 9) and anything a test legitimately needs. Item 9 renames the invariant `elements-no-pending-marker` to `elements-pending-marker` in the invariant's heading, in the *Verification* of WAY-35 and in the test's comment; search the whole repository (`git grep`) for every other use of the old identifier, including tests that cite it by a `decision:` or invariant line, and fix each in the same change. A change to a sentence of an invariant that `foundation_check.py` lists as reading `test` may require the citing test files to change in the same change: run `python -B elements/common/foundation_check.py` before you return, and the focused tests of every directory you changed (`python -B gate/run_tests.py <directory>`).
- Binding sentences only where the task gives them; never invent an extra decision. The wording of a binding sentence is yours (WAY-134), its meaning the task's. Keep WAY-05's limits: one to three binding sentences per paragraph.
- Item 1 (WAY-229): "the strongest class available" gets one meaning in the whole entry; no model name and no name of a tool setting in the text; the cut-off of Fable is a setting of the cycle's session and never a sentence of the-way. Change `task-cycle/skill/SKILL.md` where the task says (the review of the whole change and step 11), nowhere else in that file; check with `git grep` the other places that state the review's class (for instance in `task-cycle/review/`, `task-cycle/skill/request_template.md`, `agent-instructions/README.md`, the agent-type definitions in `task-cycle/agent-types/`) and correct what contradicts the new rule in the same change — and if a change to the definition of an agent type or to a skill description results, run the scripts the repository's `AGENTS.md` names (`python -B agent-instructions/skill_entry_points.py --write`, `python -B agent-instructions/agent_type_copies.py --write`) and commit what they write.
- Items 11, 12, 15, 19.21 and 19.22 rest on pages of the web: read the page now (the address is in the item or in the existing fact), copy the fragments word for word, and write the date of reading as 2026-11-15. A fact's text is never written from memory. If a page cannot be read, say so in **Searches not found or unclear** and leave the fact unchanged rather than guess; for a fact whose source quote is "today's" text, that is a `blocked` question.
- Item 15 and the facts for WAY-255: new facts are written by `elements/environment-facts/skill/SKILL.md`; the price of caching in a decision is not yours to rewrite.
- Concurrent tasks change texts you also change (WAY-121 `Rationale`, the sections for the human's decisions in the request template). The orchestrator reconciles the order at the merge; you change only what this task's items name.
- Items 19.x "przewinąć" mean rewrapping lines to the width the entry's neighbouring lines use; no change of wording unless the item gives one.
- Commits: English messages, in the style of `git log`, several commits each holding a group of items (for instance: the review class WAY-229, WAY-10 and the skill; places and limits WAY-27, WAY-320, WAY-241 and the template; WAY-287 and the invariants; the facts; the rest by item). Add files by path, never `git add -A`, `git add .` or `git commit -a`. Do not commit `.runs/`. The commit author address comes from the repository's configuration; do not change it. Do not push.
- Do not run `python -B gate/run_tests.py` without a directory (that is the orchestrator's run); run the focused tests of the directories you change.
- Private data: the frozen task quotes the author's private note locations; the repository's files never hold an absolute path or a note link (WAY-320). Write none.

## Working copies (word for word from `task-cycle/skill/SKILL.md`)

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

## Return

Write your full report to the report path above as `make-change` gives it (status, commits, checks
with command and exit code, the own-work check, **Unread material**, **Searches not found or
unclear**, reaches beyond this handoff, working copies, and for each foundation entry one sentence
of its meaning in English and one in Polish, marked `row <n>`, `projected` or `the cycle's`). Return
the status, the commits, a one-line check result and the report's path.
