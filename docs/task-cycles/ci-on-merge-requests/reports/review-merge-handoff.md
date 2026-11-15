# Handoff: review of the merge of the target branch into the task branch (correction 1)

## Who asks and what you may decide

The human who requested this task cycle has delegated its intermediate choices to the orchestrator, who dispatches you. You are an agent that did not make the change. You are read-only on the repository: you write only your report and your own working copy. You do not seek the human's approval, and you do not run the product's full gate (a full run is memory heavy and the orchestrator's alone; run the tests of single directories one at a time, `python -B gate/run_tests.py <directory>`).

## Method and stage

- Method: `task-cycle/review/SKILL.md`, read whole by you; a file it names, one beside it included, only when the step that names it comes.
- Stage: the review of the reconciliation with the target branch, in a correction after the human's remarks on the request (`task-cycle/skill/correction.md`).
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/review-merge-report.md` in the task's worktree `the worktree of the task`; its first line is `PASS <sha>` or `FAIL <sha>` (the sha of the merge commit you reviewed), as your method gives.
- Your directory for working copies: `.runs/review-merge/` (directly under the ignored `.runs/` of that worktree).

## The range to review

The task branch `task/ci-on-merge-requests` and the remote target branch `foundations` of the-way itself (no `.the-way` pin). The merge commit is `3eacbc1` (message "Merge origin/foundations into task/ci-on-merge-requests"):

- first parent `351ffb1` (the task branch: the last commit of the first cycle, which removes the copy of the record from the tree; the change is in `21ecb62..b344595`),
- second parent `7f5c5a5` (the target branch `foundations`, 44 commits after the old base `21ecb62`).

The range is that merge: what it brought from `7f5c5a5` and how its two conflicts were resolved. Review the merge commit, not the worktree: while you read, another agent (the author of the correction) edits the working tree of the worktree, so do not read files from it. Make your own clone or worktree of the commit `3eacbc1` in `.runs/review-merge/` and read there; read git objects with `git show 3eacbc1:<path>`.

The merge had two conflicts, both resolved by hand: `foundations/decisions.md` and `agent-instructions/README.md`.

- `foundations/decisions.md`: the target divided the decision log into 28 topical sections between the base and `7f5c5a5` (commit `104e126`, entries' numbers and texts unchanged). The task branch had changed four entries of the old log: WAY-09 (the list of what the repository holds and the sentence of its *Verification*, which name the CI configuration under `.github/workflows/`), WAY-16 (the one command of tests runs in CI; its *Scope*, *Based on*, *Relations*, *Verification*, *Rationale*, *Rejected*), WAY-160 (the wait for the CI result on the request, corrections included) and WAY-206 (the signal for a vulnerability in a held dependency, the Dependabot alerts). The resolution took the target's log whole and re-applied those four entries' changes on it by hand, with a rewrap to 100 columns where the text was edited. The old task-branch version of the log is `git show 351ffb1:foundations/decisions.md`; the new target's is `git show 7f5c5a5:foundations/decisions.md`.
- `agent-instructions/README.md`: the task branch added a paragraph on waiting for the CI run on the request's last head (WAY-160); the target added a paragraph on the answer "fix it in this request" to an item of *Fix or let through*. The resolution keeps both, the target's after the task branch's.

The rest of the merge merged without a conflict (`foundations/part_map.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md`, `README.md` and others).

## The question

Do the two sides still hold together? A merge can bring in a rule or code that the change goes against, or that meets the change at a seam neither side shows alone. Judge, for the range above:

1. The four re-applied entries: each of the task branch's changes to WAY-09, WAY-16, WAY-160 and WAY-206 is in the merged log, in the right entry, with its words unchanged except for rewrapping, and nothing else of the target's text of those entries or of any other entry was lost or changed. The target's own script that compares the entries of two copies of a log (`elements/common/compare_log_entries.py`; read its docstring for its use) is made for this comparison: use it between the target's log and the merged one, and between the task branch's log and the merged one, and read what it lists against the above.
2. The task-cycle skill and its beside files as they stand merged (`task-cycle/skill/SKILL.md` steps 12 and 13, `correction.md`, `request_template.md`, `record_template.md`): the paragraph of the task branch (the wait for the CI run on the request's last head, written into *Checks* and the record's *Verification*) next to what the target changed in the same files (for instance the reading of the backlog for the review's line before the reminder, the cycle's removal of directories of finished tasks, the answers to the items of *Fix or let through*): do they say one consistent thing, with no step now contradicting another, no item number of the request template that another file cites wrongly?
3. The part map as merged (`foundations/part_map.md`): the line the task branch added (`.github/workflows/**` to `agent-instructions`) against what the target changed in the map (a dependency of a part, the comparison named in the map).
4. The foundation check on the merged tree, as the gate runs it: `python -B elements/common/foundation_check.py` in your working copy, and the tests of `elements/common`, `installation`, `agent-instructions`, `instruction-files` and `task-cycle`, one directory at a time.
5. The foundation entries the merge brought in that bear on the parts the change touches (`decisions`, `environment-facts`, `installation`, `agent-instructions`, `task-cycle`, `product-guidelines`, `instruction-files`, `repository`). Entries known to come with the merge: WAY-18 (the log's topical sections), WAY-150 (the reading by an index of the selected decisions), WAY-21, WAY-24, WAY-300 (the review reminder), WAY-287 and WAY-339 (the request's items and the measures), WAY-375 (the cycle's removal of working directories), WAY-373 and WAY-316 (the record's copy and screenshots). Select further ones by the decision index script of `elements/common/way_of_working.md` ("Reading the foundation"), by the parts above, and read the ones that bear on the change whole.

The task branch's change is trust-boundary relevant (the installer's block and a CI workflow that takes in content of a pull request, which the first cycle's reviews checked); the merge changes none of those two files, which you may confirm with `git diff 351ffb1 3eacbc1 -- installation/install.py .github/workflows/tests.yml`.

## What to give back

Your report, by your method: its first line, the findings with grades and their places, the checks you ran with command and exit code, your **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), and **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), and your working copies with their removal. Keep secrets and personal data out of it.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
