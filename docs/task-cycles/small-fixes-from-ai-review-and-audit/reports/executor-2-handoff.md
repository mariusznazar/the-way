# Handoff — executor of slice 2

You make slice 2 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 2's base: the head of slice 1, `93d3e0d7` (`git rev-parse HEAD` now; write down what it prints). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it for how to read the plan and the task, and what to do when the plan and the code disagree. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 2 only. You do not start slice 3.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-2-report.md`.
- Your directory for working copies: `.runs/executor-2/`.
- Answers of the cycle's step 4: trust boundary yes — this slice changes `task-cycle/gate_times.py`, which the part map names as a trust boundary, so crafted input at it is yours to keep refused (the invariant `gate-times-refuses-impossible-entry`), and a fresh agent reviews the slice; irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (the passages below are copied; open the file only where the slice's section needs it).

## Your slice, word for word from the plan

### Slice 2 — the times of the gate: the lines of a nested run are no directories

- **Goal:** `task-cycle/gate_times.py` gives, for the output of a gate run whose failing test printed the output of a nested run of `gate/run_tests.py`, the directories that run itself opened and the time of each, and for the directory in which that test failed its own time. The shape of that output, as `gate/run_tests.py` and the unittest of Python print it: the failing test prints the nested output inside its failure message, so the first nested `== <directory>` line has text before it on its line (`AssertionError: 0 != 5 : == tests/one`) and does not open a block, the later nested `== <directory>` lines stand at the start of a line, each nested directory has its own `Ran <n> test in <s>s` line, the nested output ends with the summary line `<n> tests in <m> directories; every directory passed` (or `failed: …` in place of the last words), and the enclosing directory's own `Ran` line comes after it; the run's own last line is a summary line of the same form. The script holds these rules, and the form of the record file and the exit codes do not change:
  - the last summary line of the output is the run's own, and each earlier one closes the output of a nested run;
  - where the output holds an earlier summary line and the number of lines `== <directory>` at the start of a line is greater than the `<m>` of the last summary line, the surplus lines are the nested run's: they open no block, taken from those that stand directly before an earlier summary line, last to first, each such summary line taking at most its own `<m>` of them; a run with no earlier summary line, or with no summary line at all (a gate that was killed), is read as it is today;
  - a block that holds an earlier summary line takes as its time the first `Ran` line after the last such summary line, and the `Ran` lines of the nested run give it none; every other block keeps today's rule, the first `Ran` line of its text (the two existing tests `test_block_without_a_ran_line_gives_unknown` and `test_first_ran_line_after_its_own_block_counts` pass as they stand);
  - the memory the script keeps stays bounded whatever the output holds, as the cap of 50 listed blocks, the cut of a long directory and the limit of a line keep it today, a flood of summary lines included, and the rows that count the blocks not listed stay as they are.
  The tests start from the failing ones: a run whose output has the shape above (written out by hand in the test, with the times worked out by hand), then a nested run of three directories, two nested runs in one block, a nested run in a block that is not the first, a run whose nested output is cut off before its summary line, and a run with a nested run that passes with every one of today's tests unchanged. The script keeps its place as the exemplar of the kind `command-runner`: the exit code it passes on, its `Error:` forms and its output relay do not change.
- **Change:** `task-cycle/gate_times.py` · `task-cycle/test_gate_times.py`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:39-39` *To do* point 8 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:91-96` *Context*, the lines on point 8 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:111-112` *Decisions in play*, WAY-339 and WAY-350 · `gate/run_tests.py` · `foundations/decisions.md:8607-8758` WAY-339 · `foundations/decisions.md:8759-8795` WAY-350 · `foundations/decisions.md:11279-11298` WAY-390 · `foundations/decisions.md:9763-9806` WAY-199 · `foundations/decisions.md:11143-11190` WAY-385 · `foundations/invariants.md:541-550` gate-times-refuses-impossible-entry · `foundations/invariants.md:491-500` command-runner-passes-exit-code · `foundations/invariants.md:441-470` ruff-blocking-rules, formatter-layout, function-and-file-size · `foundations/part_map.md:104-116` task-cycle · `guidelines/coding.md` · `guidelines/coding-command-runner.md` · `guidelines/testing.md`
- **Model:** same — the rule must read an output whose nested lines look like real ones, hold for untrusted output in bounded memory, and leave every passing run read as before
- **Risk:** trust boundary — `task-cycle/gate_times.py`
- **Checks:** first the new tests fail on the base (`python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` fails with the new tests only), then the same command passes with every earlier test unchanged, the tests of the invariants `command-runner-passes-exit-code` and `gate-times-refuses-impossible-entry` among them; `python -B gate/run_tests.py process-audit` passes (the invariant `audit-series-script-paths` holds the path of the script); `python -B gate/run_tests.py agent-instructions` passes.
- **Depends on:** none

## Notes of the orchestrator for this slice

- The ranges of decisions in *Read* are the current ones at the base (the foundation step moved them by a few lines from the plan's). WAY-339 and WAY-350 are read whole as the ranges say; WAY-417 (new, lines 8995-9038) does not bear on this slice.
- The planner derived the shape of the nested output in the Goal from a run it made of a failing test that prints a nested run of `gate/run_tests.py`; no real `gate_times.md` of a failed run stands in the task. Where, running the real runner on a failing test of your own (in your directory for working copies, never in the repository's tests), you find that the shape differs from the Goal, say so in your report: this is a way of making what the task settles (point 8), so make the rule hold for the shape you find and name the difference; do not return a question for it unless the rule cannot be made at all.
- Keep the exemplar's rules (WAY-199, the kind `command-runner`): the script's exit code, its `Error:` forms and its output relay do not change. A change in a script over a threshold of WAY-385 begins with a move; the size test is among the checks named.


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
