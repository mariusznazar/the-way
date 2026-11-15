# Handoff — the fix of the findings of the review of the whole change

The person who requested this cycle delegated intermediate choices to the orchestrator; every answer below is the orchestrator's, never that person's approval. You are a fresh agent that fixes the findings of the review of the whole change: four blocking and twelve Minor findings within the task. You change only what the findings need.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`, head `be9b44d`. This is the-way itself. Nobody else writes in the worktree while you do.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant **"the fix of a review's findings"**; read it whole and `task-cycle/change/fix.md` where it names it. A skill named by its name alone is the `SKILL.md` whose frontmatter `name:` is that name; you have no skill tool, read it as a file.
- Findings file: `reports/whole-change-findings.md` (in `.runs/task-cycles/the-way-coding-and-testing-guidelines/`; the reviewer's words; its full report is `reports/review-whole-report.md`). Frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`; plan: `plan.md` there (its *Choices* bind you). The reports of the executors are in `reports/` beside.
- Your directory for working copies: `.runs/fix-whole/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/fix-whole-report.md`.
- Trust boundary: yes (`task-cycle/cycle_stages.py` is among the files you edit for M-2 and M-3); irreversible operation: no. You never run the full gate (`python -B gate/run_tests.py` with no directory); run the affected checks, and for I-1 the tests of every directory you touch together with `elements/part-map` (`python -B gate/run_tests.py elements/part-map`).
- Commit by path (`git add <path>…`), messages in English; you may commit in several commits. The range of your fix starts at `be9b44d`.
- `check_instructions.py` takes the root first: `python -B instruction-files/check_instructions.py . --file <file>`. `<ruff>` is `.runs/quality-venv/Scripts/ruff.exe` under the main checkout `<main checkout>`.

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


## The orchestrator's directions (autonomous choices Q12–Q15; answer with evidence if you hold a finding wrong)

- **I-1:** make both tests pass the check of `cross-part-imports`, keeping their meaning; show `python -B gate/run_tests.py elements/part-map` exit 0 and the tests of the touched directories.
- **I-2:** close the race by the executor's own suggestion (`timed_module` writes an event when its process ends and `a` waits for that event, or the driver releases `a` after `b`'s report is printed); show the test stable over 40 runs in a row (command and count).
- **I-3:** change the sentence of the invariant `shared-module-import-runs-nothing` in `foundations/invariants.md` and the line of `guidelines/coding-shared-module.md` to "with its input open and empty"; no change of the test. The invariant is the cycle's own entry; change it in place.
- **I-4 (Q12):** take the first way the reviewer lists: narrow the sentence of the invariant `repository-changer-acts-only-when-told` so that it excepts a report that the human names with `--report` ("…change no tracked file and no working directory other than a report file the human names with `--report`"), and rewrite the guideline `guidelines/coding-repository-changer.md` accordingly: the paragraph that says the script breaks the invariant goes; the status of `elements/common/migrate_foundation.py` returns to `copy` as the plan allocated it (the reviewer's reproduction shows it overwrites a tracked path only when the human names that path). Keep the narrowing to the sentence and its *Rationale/Relations* where they restate it; check with `python -B elements/common/foundation_check.py` (the citations now stand) and keep the cited test as it is. Name this change in your report: the human accepts it at the request.
- **M-5 (Q13):** state the exemption of `guidelines/coding.md` without the false reason: the rule reaches a script whose use is the command line; a module that only has a fixed `if __name__ == "__main__":` block is excepted in words that are true of `relation-model/fingerprint.py`. Keep it one sentence.
- **M-7 (Q14):** add the withdrawn-part message to the findings the test of the foundation keeps, when the withdrawn word names a part of the part map's *Withdrawn identifiers* — if that cannot be done with a message the script gives, say in a comment of the test why it is left out and keep the README sentence of M-8 true; do not change `elements/common/foundation_check.py`.
- **M-11 (Q15):** make the text true, not the code: the header of `agent-instructions/skill_entry_points.py` and `guidelines/coding-generator.md` say a missing *line* ends with exit 2 and an empty value ends with exit 1.
- **M-3:** a JSON line that is no object ends with exit 2 and the message naming the rollout and the line, as the Claude Code half does; add the count `10**15-1` test.
- **M-10:** add a check that every tracked `.py` file lies under one of the directories of the tuple (in each of the two tests or one shared helper in `agent-instructions/`), failing and naming the file otherwise.
- **M-12:** the two sentences keep to what the author is to do and tell no state.
- Findings O-1 and O-3 (outside the task) are not yours.

For each fix: the failing run before and the passing run after, with command and exit code, where the finding is about behaviour; the affected checks again; `python -B elements/common/foundation_check.py` exit 0 at the end (the whole check, citations included).

## What you return

Status, your commits, a one-line check result, the report path, questions and concerns, **Unread material**, **Searches not found or unclear** (`none` is an answer), the working-copies line, and a table: finding → commit → check (command, exit code).
