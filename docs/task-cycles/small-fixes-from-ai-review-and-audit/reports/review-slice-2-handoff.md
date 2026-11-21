# Handoff — reviewer of slice 2

You review slice 2 of a planned change in a task cycle of the-way, as an agent that did not make it. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report. You are read-only: you change no file of the worktree and make no commit.

- Worktree (your working directory): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. The branch's head moves with later work; the range you review is fixed by commits: base `93d3e0d76faeb272042416ddbcb25dd3a8a3b7f2`, head `8359dc25` (the full identifier is what `git rev-parse 8359dc25` prints). Compute `git diff 93d3e0d7..8359dc25` and `git log 93d3e0d7..8359dc25` yourself; the head of the worktree may be later than the head you review, and a commit after it (the repair of slice 1's new test file, which makes `agent-instructions` pass) is not in your range. Judge the range only.
- Method: `task-cycle/review/SKILL.md` (`review-change`) in the worktree, read whole. You review a slice: read what this handoff names, as the orchestrator selected it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Trust boundary: yes. The slice changes `task-cycle/gate_times.py`, which the part map names as a trust boundary: check crafted input at it, as the invariant `gate-times-refuses-impossible-entry` and the testing guidelines' *Trust boundaries* hold, and the memory the script keeps for untrusted output. Irreversible operation: no.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-slice-2-report.md`. Its first line is `PASS <sha>` or `FAIL <sha>` (the full sha of the head you reviewed), or `questions`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); write it there although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.
- Your directory for working copies: `.runs/review-slice-2/`.
- The author's report: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-2-report.md`: a set of claims to verify, not evidence. Its concern about `agent-instructions` (a failure through `process-audit/test_process_versions.py`, a file of slice 1) is known to the orchestrator and handled in a separate commit; it is no finding of this slice.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.
- What you read, besides the slice's section below (the passages of the task and the entries are named in its *Read*): the frozen task `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` lines 39, 91-96 and 111-112; the foundation entries of the slice's *Read*, each whole, at the ranges in it; the guideline files `guidelines/coding.md`, `guidelines/coding-command-runner.md` and `guidelines/testing.md`, each whole; `gate/run_tests.py` for the form of the output. Grade and scope are yours.

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


## What your report holds

Your report holds, after its first line, what the method gives: the graded findings (blocking and Minor, each with the place in the code, the reason and — for a blocking one — whether it contradicts the settlements, with the mark `Contradiction: yes` or `Contradiction: no` as the method asks), the findings outside the task's scope, the checks you ran each with its command and exit code, each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the report's first line, the checks you ran with their results, and the report's path.

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
