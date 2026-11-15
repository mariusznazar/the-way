# Handoff — reviewer of slice 2

The person who requested this cycle delegated intermediate choices to the orchestrator; nothing here
is that person's approval. You review one slice of the plan as an agent that did not make it.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. You change nothing in it.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant **a planned slice**; read it whole and a file it names only when the step or variant that names it comes. A skill named by its name alone is the `SKILL.md` whose frontmatter `name:` is that name; read it as a file (you have no skill tool).
- Range to review: `162bff8..d113238` (`git diff 162bff8 d113238`); read the full diff.
- The executor's report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/executor-2-report.md` (the executor's own claims are material, not evidence; rerun a check you rely on).
- Frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`; plan: `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` (its *Choices* and the orchestrator's additions at its end bind the change too).
- Trust boundary: **yes where the slice's *Risk* names one** — then check crafted input at that file and that the change only does what the slice says. Irreversible operation: no.
- Your directory for working copies: `.runs/review-2/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/review-2-report.md`; its first line is `PASS <sha>` or `FAIL <sha>` with the head you reviewed.
- You never run the product's gate (`python -B gate/run_tests.py` with no directory); run the focused checks you need.
- `<ruff>` means `.runs/quality-venv/Scripts/ruff.exe` under the main checkout `<main checkout>` (the parent of the directory `git rev-parse --git-common-dir` prints).

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

### Slice 2 — The sections of a definition written out in the readiness test, and the refusal invariant of `readiness_check.py`

- **Goal:** in `project-level/test_readiness_check.py` the list of the sections of a definition is
  written out in the test with its source in a comment (the headings of the form in
  `project-level/definition_template.md`), no longer taken from `readiness_check.SECTIONS`, so that a
  section dropped from the code's tuple no longer vanishes from the test data (cause 1; every place
  of the file that takes `readiness_check.SECTIONS` for an input or an expectation). The test
  `test_a_file_that_is_not_utf_8_exits_two` carries the line `# invariant: <identifier of E28>`
  (item 8). Both changes are shown to fail once: the sections test fails when a section is removed
  from the tuple for a moment, and the cited test fails when the refusal of a file that is not UTF-8
  is broken for a moment (item 9, WAY-08); each break is undone. The code it writes breaks no rule
  of `ruff.toml`.
- **Change:** `project-level/test_readiness_check.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:38-38` To do (item 12)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:232-238` Context (cause 1)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E28 · E11
  · `foundations/decisions.md:2496-2525` WAY-48
  · `foundations/decisions.md:9145-9200` WAY-235
  · `foundations/decisions.md:1750-1779` WAY-08
  · `foundations/decisions.md:9019-9058` WAY-232
  · `foundations/decisions.md:9059-9100` WAY-233
  · `foundations/invariants.md:166-175` test-method-citation
  · `foundations/part_map.md:80-99` project-level
  · `project-level/readiness_check.py:1-52` the description and the tuple of sections
  · `project-level/definition_template.md:39-75` the form of a definition
- **Model:** cheaper
- **Risk:** trust boundary — `project-level/readiness_check.py` (the slice adds the citation of the invariant of its refusal; the file itself is not changed)
- **Checks:** `python -B project-level/test_readiness_check.py` exits 0; the section test shown failing
  with `SECTIONS` changed for a moment and the cited test shown failing with the refusal broken for a
  moment, each with the command and its exit code, the changes undone (`git diff -- project-level/readiness_check.py`
  empty); `<ruff> check --config ruff.toml --no-cache --ignore-noqa project-level/test_readiness_check.py`
  reports nothing on a line the slice wrote; `python -B elements/common/foundation_check.py
  --skip-test-citations` exits 0
- **Depends on:** Foundation entries E28 · Slice 1


## The orchestrator's additions to this slice's *Read*

Whole, from `foundations/invariants.md` where the slice adds or edits a Python file: `script-language`,
`script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`; where it adds
files at the root or under `guidelines/`: `repository-file-location`, `ci-checking-commands`,
`tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target`, `derived-file-content`
(and `python-version-declared` for slice 1); for slice 23 also `instruction-file-imports` and
`root-claude-md-import`. The whole of the end of `plan.md` ("Orchestrator's additions") applies.


## What you return

The report's first line, graded findings as the method gives (every finding with `file:line`, a failure scenario and its grade; Minor and outside-the-task findings marked as the method gives), the checks you ran with command and exit code, **Unread material** and **Searches not found or unclear** (`none` is an answer), the working-copies line, and a short return to the orchestrator: status, the report path, the changed files with line counts, one-line check result.
