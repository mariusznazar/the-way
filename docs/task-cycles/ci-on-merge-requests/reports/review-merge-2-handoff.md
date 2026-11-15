# Handoff: review of the second merge of the target branch (correction 2)

## Who asks and what you may decide

The human who requested this task cycle has delegated its intermediate choices to the orchestrator, who dispatches you. You are an agent that did not make the change, and you are fresh: no earlier review of this request was yours. You are read-only on the repository: you write only your report and your own working copy. You do not seek the human's approval and you do not run the product's full gate (memory heavy, the orchestrator's alone, and it waits for a signal of the day's advisor); run the tests of single directories one at a time (`python -B gate/run_tests.py <directory>`).

## Method and stage

- Method: `task-cycle/review/SKILL.md`, read whole by you from your own clone of the commit you review; a file it names, one beside it included, only when the step that names it comes.
- Stage: the review of the reconciliation with the target branch, in a correction after the human's answer (`task-cycle/skill/correction.md`).
- Task's worktree: `the worktree of the task`, branch `task/ci-on-merge-requests`, the-way itself (no `.the-way` pin). Make your own clone or worktree of the commit in `.runs/review-merge-2/` (directly under the ignored `.runs/` of that worktree) and read there; read git objects with `git show <commit>:<path>`.
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/review-merge-2-report.md`, first line `PASS <sha>` or `FAIL <sha>` (the sha of the merge commit).

## The range

The merge commit `cde07dd` ("Merge remote-tracking branch 'origin/foundations' into task/ci-on-merge-requests"): first parent `2e83447` (the task branch, after correction 2), second parent `9cbc6b2` (the target branch `foundations`, 39 commits after the earlier merge `7f5c5a5`, the last of them the merged request 132). It had no conflict. The merge base is `7f5c5a5`, the target branch of the first merge, which another reviewer judged earlier (`FAIL`, finding 1 fixed and accepted, finding 2 resolved by correction 2, `PASS 2e83447`).

What the target brought in (46 files, +3606 −689): changes to the measures and stage scripts of the cycle and their tests, the audit count of the process, the checks of private paths and of the remarks, a new test of dead pointers in skills (`product-guidelines/test_skill_references.py`), a new glossary term (Markdown file), and rewrites of WAY-321, WAY-339 and WAY-344 (the entries of the decision log that differ between `7f5c5a5` and `9cbc6b2`, by `elements/common/compare_log_entries.py`; none of them is among the four entries this task changed: WAY-09, WAY-16, WAY-160, WAY-206).

The four files that both sides changed since the merge base, auto-merged: `foundations/decisions.md`, `foundations/part_map.md`, `installation/README.md`, `task-cycle/skill/SKILL.md`.

## The question

Do the two sides still hold together? A merge can bring in a rule or code that the change goes against, or that meets the change at a seam neither side shows alone. Judge, for the range above:

1. The four files that both sides changed: that each task-branch change is in the merged file with its words unchanged, nothing of the target's lost, and no seam: in `task-cycle/skill/SKILL.md` the paragraph of the task branch (the wait for the CI run on the request's last head and its exception for a flaky check outside the task's scope, in step 12) next to what the target changed in the same file (12 lines); in `foundations/part_map.md` the lines of the task branch (`.github/workflows/**` for `agent-instructions`, `instruction-files` in the *Depends on* of `installation`) next to the target's; in `installation/README.md` the task's section on the CI file next to the target's change; in `foundations/decisions.md` the four entries of the task branch (compare the entries of the log with `elements/common/compare_log_entries.py`, as the earlier review did, against the target's log and the task branch's).
2. Whether any new rule or new check of the target meets the task's change: in particular the checks of private paths and of the remarks, the new test of dead pointers in skills, the tracking of Markdown suffixes, the new glossary term and WAY-321, WAY-339 and WAY-344, against the task's files (`.github/workflows/tests.yml`, the installer's block and README, the skill and the templates of the cycle, the foundation entries of the task). Select your own foundation by "Reading the foundation" of `elements/common/way_of_working.md` and the decision index script, for the parts the change touches (`decisions`, `environment-facts`, `installation`, `agent-instructions`, `task-cycle`, `product-guidelines`, `instruction-files`, `repository`, `invariants`, `part-map`), and read whole the entries the merge brought in that bear on the change.
3. The checks on the merged tree, as the gate runs them, one directory at a time: `python -B elements/common/foundation_check.py` without `--skip-test-citations`, and `python -B gate/run_tests.py` for `elements/common`, `installation`, `agent-instructions`, `instruction-files`, `task-cycle`, `product-guidelines`, `elements/part-map`.

The change of the task is trust-boundary relevant (the installer's block and a CI workflow that takes in content of a pull request); the merge changes none of those two files, which `git diff 2e83447 cde07dd -- installation/install.py .github/workflows/tests.yml` confirms (it should print nothing). Your Minor findings stay unfixed by design; the Minor findings of earlier reviews (two further reaches no *Depends on* allows; three edited lines over 100 characters; the three Minor findings on the new fact) stand in the request's list and are not yours to re-judge.

## What to give back

Your report: its first line, findings with grades and places (the reviewer alone grades and scopes), the checks you ran with command and exit code, your **Unread material** (or `none`), **Searches not found or unclear** (or `none`), and your working copies with their removal. No secrets or personal data.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
