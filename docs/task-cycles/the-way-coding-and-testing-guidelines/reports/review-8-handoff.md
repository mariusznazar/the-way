# Handoff — reviewer of slice 8

The person who requested this cycle delegated intermediate choices to the orchestrator; nothing here
is that person's approval. You review one slice of the plan as an agent that did not make it.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. You change nothing in it.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant **a planned slice**; read it whole and a file it names only when the step or variant that names it comes. A skill named by its name alone is the `SKILL.md` whose frontmatter `name:` is that name; read it as a file (you have no skill tool).
- Range to review: `8ef214d..6cf3fa9` (`git diff 8ef214d 6cf3fa9`); read the full diff.
- The executor's report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/executor-8-report.md` (the executor's own claims are material, not evidence; rerun a check you rely on).
- Frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`; plan: `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` (its *Choices* and the orchestrator's additions at its end bind the change too).
- Trust boundary: **yes where the slice's *Risk* names one** — then check crafted input at that file and that the change only does what the slice says. Irreversible operation: no.
- Your directory for working copies: `.runs/review-8/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/review-8-report.md`; its first line is `PASS <sha>` or `FAIL <sha>` with the head you reviewed.
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

### Slice 8 — The tests of the audit count: fixed time, a repository built in a temporary directory, git without the user's configuration, no unused names, and the refusal invariant of a link

- **Goal:** in `process-audit/test_audit_count.py` — (a) cause 4, the places of this file: the two
  runs of the test `test_the_same_input_gives_the_same_bytes_in_both_files` are given `--today` with
  one fixed day, and the limit of wall time of the helper `run_count` and of the tests that pass it
  60 seconds no longer makes a test red on a slow machine where the limit is no oracle of the test
  (a limit that is the test's oracle, as in a test that a long line does not stall the count,
  stays and is named in the report); (b) cause 6: the test
  `test_the_way_without_a_repository_entry_is_this_checkout` runs on a repository built in a temporary
  directory that holds a copy of `process-audit/audit_count.py` (the script reads the checkout it
  lies in), not on this checkout; (c) cause 7, the place of this file: git runs with the user's
  global and system configuration shut out, `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM` set as
  `project-level/test_plan_state_invariant.py` sets them, in the constant `GIT_ENV` and in the
  environment `run_count` gives the script; (d) cause 26: every unpacked name that is never read,
  in every place the linter reports in this file as RUF059 (13 at the task's commit, 14 at the
  base), is replaced by `_` or used, and the test whose name's reason the script rejects checks
  that reason; (e) the test `test_a_symbolic_link_leaving_the_record_is_not_followed` carries
  `# invariant: <identifier of E32>` and is shown failing once with the refusal broken for a moment,
  undone. The report names each place of the linter it leaves in the file (F541 at the base). The
  code it writes breaks no rule of `ruff.toml`.
- **Change:** `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:41-44` To do (items 15 to 18)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:46-46` To do (item 20)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:92-97` Questions to settle (answer 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:161-168` Questions to settle (answers 17 and 18)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:253-259` Context (cause 4)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:267-279` Context (causes 6 and 7)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:391-397` Context (cause 26)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E32 · E11 · E12
  · `foundations/decisions.md:2496-2525` WAY-48
  · `foundations/decisions.md:9145-9200` WAY-235
  · `foundations/decisions.md:1750-1779` WAY-08
  · `foundations/decisions.md:2823-2968` WAY-344
  · `foundations/decisions.md:9522-9552` WAY-243
  · `foundations/invariants.md:166-175` test-method-citation
  · `foundations/part_map.md:124-134` process-audit
  · `process-audit/audit_count.py:1-60` the description
  · `process-audit/audit_count.py:325-345` the checkout the script lies in
  · `process-audit/audit_count.py:3240-3310` the arguments
  · `project-level/test_plan_state_invariant.py:195-205` the environment of git of a test of the level git
- **Model:** same — four causes and a boundary citation in one file of 4195 lines
- **Risk:** trust boundary — `process-audit/audit_count.py` (the slice adds the citation of the invariant of its refusal; the script is not changed)
- **Checks:** `python -B process-audit/test_audit_count.py` exits 0 (the whole file; it is this
  slice's one file, not the gate); the cited test shown failing with the refusal of links broken for
  a moment, undone (`git diff -- process-audit/audit_count.py` empty); `<ruff> check --config
  ruff.toml --no-cache --ignore-noqa process-audit/test_audit_count.py` reports no RUF059 and nothing
  on a line the slice wrote; `python -B elements/common/foundation_check.py --skip-test-citations`
  exits 0
- **Depends on:** Foundation entries E32 · Slice 1


## The orchestrator's additions to this slice's *Read*

Whole, from `foundations/invariants.md` where the slice adds or edits a Python file: `script-language`,
`script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`; where it adds
files at the root or under `guidelines/`: `repository-file-location`, `ci-checking-commands`,
`tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target`, `derived-file-content`
(and `python-version-declared` for slice 1); for slice 23 also `instruction-file-imports` and
`root-claude-md-import`. The whole of the end of `plan.md` ("Orchestrator's additions") applies.


## What you return

The report's first line, graded findings as the method gives (every finding with `file:line`, a failure scenario and its grade; Minor and outside-the-task findings marked as the method gives), the checks you ran with command and exit code, **Unread material** and **Searches not found or unclear** (`none` is an answer), the working-copies line, and a short return to the orchestrator: status, the report path, the changed files with line counts, one-line check result.
