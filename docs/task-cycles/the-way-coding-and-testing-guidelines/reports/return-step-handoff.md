# Handoff — the return step

The person who requested this cycle delegated intermediate choices to the orchestrator; every answer is the orchestrator's, never that person's approval. You are a fresh agent that takes the return step of a planned change.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`, head `f0482d0`. The change since the base `2d593214e4ce11676880b1f3ac3aa75884e023ab`: 39 commits (foundation entries `e1586a4`; slices 1–23; the fix of the whole-change review `be9b44d..f0482d0`). This is the-way itself.
- Method: `task-cycle/change/SKILL.md` (`make-change`) for reading, commits and the report, and **`task-cycle/skill/return_step.md`** for what the return step compares and writes — read it whole; it names `task-cycle/skill/foundation_step.md` too (read that too: the return step writes as the foundation step writes). A skill named by its name alone is the `SKILL.md` whose frontmatter `name:` is that name; you have no skill tool, read it as a file.
- Your directory for working copies: `.runs/return-step/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/return-step-report.md`, with the sections the template of the record's *Return step* gives (foundation compared with code; decisions, invariants, environment facts, glossary terms, part-map changes, projected entries and rows written or changed, each or `none`).
- Frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` (*Decisions in play*, *Settlements to record* of 34 rows, *Context*); plan: `plan.md` there; the reports of the stages are in `reports/` (the entries report `entries-report.md` has the table of identifiers). No spec. Trust boundary: yes; irreversible operation: no.
- You never run the full gate; run `python -B elements/common/foundation_check.py` (whole) and the focused checks your edits need. Commit by path, in English; if you change nothing, commit nothing and say so.

## Working copies (word for word from the orchestrator's skill)

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



## The identifiers of the entries the slice names

The plan names entries written by the foundation step by their row `E<n>`; here are the identifiers
the writer gave them (use these, not the plan's proposals):

| Entry of the plan | Kind | Identifier written | Row |
|---|---|---|---|
| E1 | decision | WAY-379 | row 1 |
| E2 | decision | WAY-380 | row 3 |
| E3 | decision | WAY-381 | row 4 |
| E4 | decision | WAY-382 | row 11 |
| E5 | decision | WAY-383 | row 12 |
| E6 | decision | WAY-384 | row 13 |
| E7 | decision | WAY-385 | row 14 |
| E8 | decision | WAY-386 | row 18 |
| E8 | decision | WAY-387 | row 18 |
| E8 | decision | WAY-388 | row 18 |
| E8 | decision | WAY-389 | row 18 |
| E8 | decision | WAY-390 | row 18 |
| E8 | decision | WAY-391 | row 18 |
| E9 | decision | WAY-392 | row 2 |
| E10 | decision | WAY-393 | row 20 |
| E11 | decision | WAY-394 | row 25 |
| E12 | decision | WAY-395 | row 26 |
| E13 | decision | WAY-396 | row 27 |
| E13 | decision | WAY-397 | row 27 |
| E13 | decision | WAY-398 | row 27 |
| E13 | decision | WAY-399 | row 27 |
| E13 | decision | WAY-400 | row 27 |
| E14 | decision | WAY-401 | row 28 |
| E15 | decision | WAY-402 | row 29 |
| E16 | change of a decision | WAY-09 | row 31 |
| E17 | withdrawal of a decision | WAY-328 | row 32 |
| E18 | change of a decision | WAY-344 | row 33 |
| E19 | change of a decision | WAY-363 | row 34 |
| E20 | change of a decision | WAY-38 | row 9 |
| E21 | change of an invariant | `script-subprocesses` | row 10 |
| E22 | invariant | `ruff-blocking-rules` | row 6 |
| E23 | invariant | `function-and-file-size` | row 15 |
| E24 | invariant | `generator-writes-only-with-write` | row 19 |
| E25 | invariant | `repository-changer-acts-only-when-told` | row 19 |
| E26 | invariant | `command-runner-passes-exit-code` | row 19 |
| E27 | invariant | `shared-module-import-runs-nothing` | row 19 |
| E28 | invariant | `readiness-check-refuses-non-utf-8` | row 30 |
| E29 | invariant | `cycle-stages-refuses-crafted-names` | row 30 |
| E30 | invariant | `cycle-measures-refuses-nested-line` | row 30 |
| E31 | invariant | `gate-times-refuses-impossible-entry` | row 30 |
| E32 | invariant | `audit-count-refuses-record-links` | row 30 |
| E33 | invariant | `check-instructions-refuses-outside-links` | row 30 |
| E34 | glossary term | `files test` | row 21 |
| E35 | glossary term | `git test` | row 22 |
| E36 | glossary term | `repository test` | row 23 |
| E37 | environment fact | `ruff-default-rules` | row 7 |
| E38 | environment fact | `ruff-required-version` | row 8 |
| E39 | part-map line | written by Slice 1 | — |
| E40 | part-map line | written by Slice 18 | — |

Deviations of the written entries from the plan that bear on you: the glossary terms are headed
`files test`, `git test` and `repository test` (not the bare `files`, `git`, `repository`); six
decisions WAY-386 to WAY-391 designate the exemplars of the six kinds (one each), and five decisions
WAY-396 to WAY-400 the exemplar of each level (one each); the entries name eleven parts with Python
code (`product-guidelines` is the eleventh).


## What the orchestrator asks you to compare (beside what `return_step.md` asks)

- Every entry the change writes, changes or withdraws (WAY-379–WAY-402, WAY-09, WAY-38, WAY-344, WAY-363, WAY-389 (narrowed by the fix), WAY-328 (withdrawn), `script-subprocesses`, the invariants of rows 6, 15, 19 and 30, the glossary terms `files test`, `git test`, `repository test`, the environment facts `ruff-default-rules`, `ruff-required-version`) against the code and files as the change leaves them, and the part map of the touched parts: the sentence of `agent-instructions` does not mention `guidelines/` (the reviewer found the same for the README: now one line each); the Scope of the decisions that name parts (a part that holds Python code is in the Scope of WAY-379/WAY-392 as they ask); the *Files* of `repository` and `agent-instructions`.
- The three script files over 1000 lines at the head (`process-audit/audit_count.py`, `task-cycle/cycle_stages.py`, and `elements/common/foundation_check.py` at 1003 lines) against what the entries of the rule of size say (the task counted two at `21ecb62`; the rationale of WAY-385 dates its count to the commit of the review of the foundation): correct a statement of the entries that is no longer true, and write nothing for the third file other than what the invariant `function-and-file-size` (`Violated: yes`) already holds.
- The Searches not found or unclear and the concerns of the reports: the order of the plan's *Choices*, the cause labels that did not match their lines (slices 19), the glossary headings, the part-map sentence, the sentences of the entries that go beyond a row (listed in `entries-report.md`), and the unread plan lines the entries agent did not read (`plan.md` slices 17–23 and *Coverage*): compare what the entries say with what those slices wrote.
- The row of `product-guidelines` in the table of parts of `guidelines/testing.md` is the orchestrator's proposal (complexity in computation); do not change it.
- Do not write an invariant for behaviour merely because no invariant covers it; write one only for a rule the task, a decision or the human sets.

## What you return

Status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), your commits (or none), a one-line check result with command and exit code, the report path, questions and concerns, **Unread material**, **Searches not found or unclear** (`none` is an answer), the working-copies line.
