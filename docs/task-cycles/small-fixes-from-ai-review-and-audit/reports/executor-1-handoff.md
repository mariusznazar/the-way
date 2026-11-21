# Handoff — executor of slice 1

You make slice 1 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 1's base: `a946862b557fc3bd1b3e04976a2bcf66054a1ace` (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it for how to read the plan and the task. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 1 only. You do not start slice 2.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-1-report.md`.
- Your directory for working copies: `.runs/executor-1/`.
- Answers of the cycle's step 4: trust boundary yes for the change as a whole (not for this slice, whose risk is `none`); irreversible operation no.
- Frozen task (not to open unless the slice's section needs it): `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`. This slice's reason, in the task's words (point 4 and 5 of *To do* change the tests that this slice moves; this slice is the move alone): the later slices change the tests of the versions of the audit, and the file `process-audit/test_audit_count.py` is too large (5729 lines) for a slice to read whole beside the code it changes.

## Your slice, word for word from the plan

### Slice 1 — move the tests of the versions into a file of their own

- **Goal:** the helper `process_record`, the class `ProcessVersions`, the helper `gate_run` and the class `MeasureVersions`, which stand today between the lines 4230 and 5711 of `process-audit/test_audit_count.py`, stand in the new file `process-audit/test_process_versions.py`, which takes from `process-audit/test_audit_count.py` the fixtures and helpers they use (imported from it, so that no fixture is written twice and no test class of `process-audit/test_audit_count.py` is collected twice). No test changes its assertions, none is added or removed, and the number of tests that `process-audit/` runs is the same before and after. Nothing of the audit's code changes, and no behaviour changes.
- **Change:** `process-audit/test_audit_count.py` · `process-audit/test_process_versions.py`
- **Read:** `guidelines/coding.md` · `guidelines/testing.md` · `foundations/part_map.md:128-143` process-audit
- **Model:** cheaper
- **Risk:** none
- **Checks:** before the move, `python -B -m unittest discover -s process-audit -p "test_*.py"` and note the line `Ran <n> tests`; after it, the same command prints the same `<n>` and `OK`; `python -B gate/run_tests.py agent-instructions` passes (the linter, the formatter and the size tests of the invariants `ruff-blocking-rules`, `formatter-layout` and `function-and-file-size`).
- **Depends on:** none

## Notes of the orchestrator for this slice

- Current ranges: the line numbers of the plan's Goal are those of `process-audit/test_audit_count.py` at the base `268b2b07`; no commit since touched that file, so they hold at `a946862b`. Find the helper and the classes by name before you cut.
- Move the text byte for byte (a script that reads and writes bytes, or with `newline=''`, keeps line endings; check `git ls-files --eol process-audit/test_audit_count.py`). A moved test keeps its name and its text; only the imports it needs change. After the move run the formatter and the linter through the size/format tests named in *Checks* and fix only what they report in the files you changed.
- The new file imports the fixtures it uses from `process-audit/test_audit_count.py`; where the unittest discovery would collect a class imported from a test module a second time, import the module, not the class names, or give the importing a form that collects nothing twice; the count `Ran <n> tests` before and after must be equal. The test file keeps the head description every test file of the directory has, if any does.
- Write the first count down before you change anything; it is the failing-first record of a move that changes no behaviour: report the counts as the checks.
- The files of the foundation of the-way name `process-audit/test_audit_count.py` in places (the guidelines' *Where in code*, the exemplar of the e2e recipe `process-audit/test_audit_count.py`, the test `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share`): that test stays in `process-audit/test_audit_count.py`, since it is not in the range you move; check that it does, and report it if it is among the tests you moved.

## What you return and keep (WAY-148, WAY-164, WAY-260)

- Make the slice from its section above and the *Read* it names; do not open the plan. Where the plan and the code disagree, `slice.md` says what to do.
- Write the failing test first where the slice changes behaviour, and keep the failing run's command and exit code for your report. A check you report carries its command and its exit code; run only the focused checks the slice's *Checks* names, never the product's gate (`python -B gate/run_tests.py` with no directory), which the orchestrator or CI runs.
- Commit your work on the task branch, by path (`git add <path> <path>`, never `git add -A`, `git add .` or `git commit -a`), with commit messages in English; leave the worktree clean. Name your commits in the report. Do not push.
- Your report holds: the status (`done`, `done with concerns`, `questions`, `returned` or `blocked`, as the method gives), your commits, each check with its command and exit code, the own-work check the method asks for (the weakest point of your work, how you tested it, what it showed), each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the status, your commits, a one-line check result naming what failed or did not run, and the report's path.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.
- The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), so write it at the path above although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.

## Working copies (word for word from the process of the cycle)

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
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.
