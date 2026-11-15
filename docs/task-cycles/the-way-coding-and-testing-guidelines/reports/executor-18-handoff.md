# Handoff — executor of slice 18

The person who requested this cycle delegated intermediate choices to the orchestrator; every
answer here is the orchestrator's, never that person's approval. You make slice 18 of the plan.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. Base of
  your slice: `f16616c0aea695c7416d81efd5a0822540385efc`. This is the-way itself; no `.the-way`, no pin. Nobody else writes in the worktree while you do.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant **"a slice, or the retry of a slice"**.
  Read it whole; read a file it names only when the step or variant that names it comes. Foundation
  entries are already written (commit `e1586a4`); a decision, an invariant or a glossary term you
  need is read in `foundations/`. Methods the plan names by a skill's name alone are the `SKILL.md`
  whose frontmatter `name:` is that name; you have no skill tool, read it as a file.
- Your directory for working copies: `.runs/executor-18/`.
- Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/executor-18-report.md`.
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

### Slice 18 — The guidelines of the kinds `check` and `shared-module`, and the directory `guidelines/` in the part map

- **Goal:** the files `guidelines/coding-check.md` and `guidelines/coding-shared-module.md` stand in
  the form `product-guidelines/coding/template.md` gives a file of a kind (the form of
  `product-guidelines/template.md` with `## Files of this kind`), written from the settlements, E8
  and E27, never from memory: *Applies to* the parts the kind's files lie in; *When to read*
  before adding or changing a file of the kind; the table of the files of the kind with their
  statuses by the allocation of the task's Context (`task-cycle/tracked_private_paths_check.py` is
  the exemplar of `check`, with E8 in its *Decision* cell; a file whose places of `do not copy` are
  all corrected at the base or in this task is `copy`; `task-cycle/request_check.py` stays `do not
  copy`; `relation-model/fingerprint.py` is the exemplar of `shared-module`); for `shared-module`,
  the rule of E27 with that invariant and the rest of the exemplar as an example; for `check`, whose
  answer 13 gives no rule that a test checks, `## Rules` holds `none — <identifier of E8>` and the
  rest of the exemplar stands as an example (WAY-198). *Where in code* names the directories the files
  lie in. No value is copied from code or a decision. Through `update-part-map`, the part
  `agent-instructions` of `foundations/part_map.md` lists `guidelines/**` (E40), written with the
  first file this slice adds. A script of the repository added after the audit of the task (such as
  `elements/common/compare_log_entries.py` and `elements/common/decision_index.py`) takes no row, as
  the template says.
- **Change:** `guidelines/coding-check.md` · `guidelines/coding-shared-module.md` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:28-28` To do (item 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:130-147` Questions to settle (answers 12 and 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:218-224` Context (the allocation of the scripts to kinds)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:531-532` Settlements to record (rows 18 and 19)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:544-544` Settlements to record (row 31)
  · E8 · E27 · E16 · E40
  · `foundations/decisions.md:7837-7910` WAY-167
  · `foundations/decisions.md:7911-7971` WAY-168
  · `foundations/decisions.md:7972-8007` WAY-173
  · `foundations/decisions.md:8107-8163` WAY-312
  · `foundations/decisions.md:8517-8548` WAY-198
  · `foundations/decisions.md:8549-8584` WAY-199
  · `product-guidelines/template.md` · `product-guidelines/coding/template.md` · `product-guidelines/reading.md`
  · `task-cycle/tracked_private_paths_check.py` · `relation-model/fingerprint.py`
  · `elements/part-map/skill/SKILL.md` · `elements/part-map/template.md` · `elements/common/rules.md`
  · `foundations/invariants.md:86-95` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0 (every reference of the two files
  names an entry, every path pattern of the map matches a tracked file); `git ls-files guidelines`
  lists the two files; no path of the main checkout or of the user's disk, no link to a note, stands
  in either file (`python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`)
- **Depends on:** Slice 1 · Slice 15 · Foundation entries E8 · E16 · E27

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
