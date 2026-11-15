# Handoff — executor of slice 22

The person who requested this cycle delegated intermediate choices to the orchestrator; every
answer here is the orchestrator's, never that person's approval. You make slice 22 of the plan.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. Base of
  your slice: `6fd60efda6773fb942509ebd4243ce2e76470e51`. This is the-way itself; no `.the-way`, no pin. Nobody else writes in the worktree while you do.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant **"a slice, or the retry of a slice"**.
  Read it whole; read a file it names only when the step or variant that names it comes. Foundation
  entries are already written (commit `e1586a4`); a decision, an invariant or a glossary term you
  need is read in `foundations/`. Methods the plan names by a skill's name alone are the `SKILL.md`
  whose frontmatter `name:` is that name; you have no skill tool, read it as a file.
- Your directory for working copies: `.runs/executor-22/`.
- Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/executor-22-report.md`.
- Answers of step 4: trust boundary **no** for this slice (see its *Risk*; where it names a file of a boundary, check crafted input at that file); irreversible operation: no.
- You never run the product's gate (`python -B gate/run_tests.py` without a directory, WAY-160); run the focused checks the slice's *Checks* names. A focused run of one directory is `python -B gate/run_tests.py <directory>`.
- Commit by path (`git add <path>…`, never `-A`/`.`/`-a`), messages in English like the repository's history.
- `<ruff>` means `.runs/quality-venv/Scripts/ruff.exe` under the main checkout `<main checkout>` (the parent of the directory `git rev-parse --git-common-dir` prints); ruff 0.17.1 is installed there by a human action done before the cycle. Slice 1 creates `ruff.toml`.
- The frozen task is `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`; the *Read* line ranges below refer to it (copy at the base). The plan is `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md`; its *Choices* and the orchestrator's additions at its end bind you too.

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

## The slice (copied word for word from `plan.md`; line ranges of decisions and invariants refreshed to the worktree as it stands)

### Slice 22 — The testing guidelines `guidelines/testing.md`

- **Goal:** `guidelines/testing.md` stands in the form of `product-guidelines/testing/template.md`,
  written from the settlements and the entries, never from memory: *Applies to* every part the
  tests check or that holds test files; `## When to read` before writing or changing a test;
  `## Levels` with the table of the five levels (E10 in each *Decision* cell, E34–E36 named as the
  glossary terms of the three levels the glossary defines) and the table of parts with the sentence
  for each (the ten parts of answer 15; the table's row for `product-guidelines` follows the answer
  the orchestrator gives to the question of the plan's report, and a row whose answer is missing is
  left as a question, never filled); `## Rules` in the template's order, each required rule with its
  decisions and *Invariant* `none` but `### Trust boundaries`, which names the refusal invariant of
  each of the nine boundaries (E28–E33 and the three standing, `project-plan-form`,
  `project-plan-state-evidence` and `installation-paths-through-links`) and holds the table of
  authorization with its header and no row (the-way has no users or permissions); `### Where the
  expected value comes from` naming E11; `### Mutation testing` reading `none — <identifier of E15>`;
  `### AI in tests` with no decision of a tool (the-way's tests use no AI tool); `## Recipes` with one
  recipe per level, the fields in the template's order, the *Command* `python -B gate/run_tests.py
  <directory>`, the *Time limit* `none — <identifier of E12>`, the *Exemplar* of each level the test of
  answer 18 with E13; `## Not tested on purpose` naming E14; `## Examples`; `## Where in code`. No
  value is copied from code or a decision, no text names WAY-328 (E17), and every reference names an
  entry the foundation holds.
- **Change:** `guidelines/testing.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:29-29` To do (item 3)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:63-65` Questions to settle (preferences about tests)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:148-181` Questions to settle (answers 14 to 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:203-207` Questions to settle (answer 26)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:514-515` Settlements to record (rows 1 and 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:533-543` Settlements to record (rows 20 to 30)
  · E9 · E10 · E11 · E12 · E13 · E14 · E15 · E17 · E28 · E29 · E30 · E31 · E32 · E33 · E34 · E35 · E36
  · `foundations/decisions.md:8982-9018` WAY-231
  · `foundations/decisions.md:9145-9200` WAY-235
  · `foundations/decisions.md:9253-9301` WAY-237
  · `foundations/decisions.md:9380-9424` WAY-240
  · `foundations/decisions.md:9425-9472` WAY-241
  · `foundations/decisions.md:9473-9521` WAY-242
  · `foundations/decisions.md:9578-9620` WAY-252
  · `foundations/decisions.md:9621-9656` WAY-253
  · `foundations/decisions.md:9657-9688` WAY-254
  · `foundations/decisions.md:7837-7910` WAY-167
  · `foundations/decisions.md:7911-7971` WAY-168
  · `foundations/decisions.md:7972-8007` WAY-173
  · `foundations/decisions.md:8107-8163` WAY-312
  · `foundations/invariants.md:238-251` project-plan-form
  · `foundations/invariants.md:311-320` installation-paths-through-links and project-plan-state-evidence
  · `foundations/part_map.md:1-283` the part map of the-way
  · `product-guidelines/template.md` · `product-guidelines/testing/template.md` · `product-guidelines/reading.md`
  · `foundations/invariants.md:86-95` tracked-file-private-paths
- **Model:** same — a file of many rules and five recipes, written without a change of the settlements
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0 (every decision, invariant and
  part it names is an entry); `python -B task-cycle/tracked_private_paths_check.py
  tracked-file-private-paths` exits 0; `python -B instruction-files/check_instructions.py
  guidelines/testing.md` gives no finding the file's form causes; each path in *Where in code* and
  *Exemplar* is a path `git ls-files` lists, and each exemplar test named exists
- **Depends on:** Slice 2 · Slice 4 · Slice 5 · Slice 6 · Slice 8 · Slice 11 · Foundation entries E9–E15 · E17 · E28–E36

## The orchestrator's additions to this slice's *Read*

Whole, from `foundations/invariants.md` where the slice adds or edits a Python file: `script-language`,
`script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`; where it adds
files at the root or under `guidelines/`: `repository-file-location`, `ci-checking-commands`,
`tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target`, `derived-file-content`
(and `python-version-declared` for slice 1); for slice 23 also `instruction-file-imports` and
`root-claude-md-import`. The whole of the end of `plan.md` ("Orchestrator's additions") applies.

## What you return

Status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your
commits, a one-line check result naming what failed or did not run, the report path, questions and
concerns, **Unread material** (what this handoff names that stayed unread or was read in part, or
`none`) and **Searches not found or unclear** (`none` is an answer) and the own-work check with the
commands and exit codes of each check; a report missing a section or a command or exit code is
returned to you for repair. A reach beyond the handoff (a part whose guidelines or decisions you read
yourself) is named in the report. The slice's weakest point and the check you made of it go in the
report as `make-change` gives.

## The orchestrator's answers that bind this slice

- The table of parts of `guidelines/testing.md` has a row for `product-guidelines` (the eleventh part with Python, autonomous choice Q2): write it with the complexity in **computation** (the test parses the text of skills and checks references against files), and mark it in your report as the orchestrator's proposal that the human confirms at the request; do not leave the row empty and do not invent a source for it.
- The glossary terms written by the foundation step are headed `files test`, `git test` and `repository test`; name the levels in the guidelines with those words.
- Check `guidelines/testing.md` with `python -B instruction-files/check_instructions.py . --file guidelines/testing.md` (the script's first argument is the root).
