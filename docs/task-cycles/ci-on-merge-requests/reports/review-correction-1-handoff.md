# Handoff: review of correction 1 (the human's remarks on the request)

## Who asks and what you may decide

The human who requested this task cycle has delegated its intermediate choices to the orchestrator, who dispatches you. You are an agent that did not make the change. You are read-only on the repository: you write only your report and your own working copy. You do not seek the human's approval and you do not run the product's full gate (memory heavy, the orchestrator's alone); run the tests of single directories one at a time (`python -B gate/run_tests.py <directory>`).

## Method and stage

- Method: `task-cycle/review/SKILL.md`, read whole; a file it names only when the step that names it comes.
- Stage: the review of a correction after the human's remarks, in place of a findings file the remarks bind (`task-cycle/skill/correction.md`).
- Task's worktree: `the worktree of the task`, branch `task/ci-on-merge-requests`, the-way itself (no `.the-way` pin). Make your own clone or worktree of the commit you review in `.runs/review-correction-1/` (directly under the ignored `.runs/` of that worktree) and read there.
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/review-correction-1-report.md`, first line `PASS <sha>` or `FAIL <sha>`.

## The range to review

`3eacbc1..7d00a48`: one commit, `7d00a48` "Record the reading of the branch rule of foundations and name it in WAY-16", by the author of the correction. It changes two files: `foundations/environment_facts.md` (a new entry `foundations-branch-ruleset`) and `foundations/decisions.md` (the *Based on* of WAY-16). `3eacbc1` is the merge of the target branch into the task branch; a separate reviewer judges that merge and you do not. The author's report is `.runs/task-cycles/ci-on-merge-requests/reports/author-correction-1-report.md`.

## What the correction had to do (the remarks it binds)

The frozen task is `.runs/task-cycles/ci-on-merge-requests/task.md` (the change: the one command of tests runs in CI on every merge request; the result is a required check with a bypass for the owner). The human's remarks are in `.runs/task-cycles/ci-on-merge-requests/reports/correction-1-remarks.md`. The one that binds code, word for word:

> 2. Close it in this request. Read the branch rule now that it exists and write that reading into the decision whose *Based on* holds the open `TODO` for it (WAY-16, rows 1 and 2), the same way the three GitHub facts of this request are written (address, date read, the passage), so that no marked gap is left on the main branch.

His remark 1 states what he set (the ruleset `foundations_tests`, id 27308872, targeting `refs/heads/foundations`, requiring the status check `tests` of GitHub Actions, no up-to-date requirement, bypass for the Repository admin role, mode always) and tells the agent to read it himself with `gh api repos/mariusznazar/the-way/rulesets/27308872`. His remark 3 lets two findings outside the task through with no task and binds nothing in code.

## What to judge

1. That the correction does what remark 2 asks and nothing else: the *Based on* of WAY-16 has no open `TODO` left, names the fact by its identifier alone as WAY-90 gives, and no other part of WAY-16 or of any other entry changed (compare with `3eacbc1`).
2. That the new fact is written as `elements/environment-facts/template.md` and WAY-84, WAY-90 and WAY-82 give for a setting changed outside the repository, whose source is a reading: the form of the source (the command, the tool and its version, the output word for word, the run date), that the output quoted is what the command prints for these fields, that it holds no secret, that the sentence says only what the quoted output shows (the author chose not to say "GitHub Actions" or "Repository admin role" because the output shows only the numbers 15368 and 5; judge whether the sentence and WAY-16 rest soundly on that), and that the identifier names what the fact is about.
3. Whether the reading can be repeated by you: run the two read-only commands of the entry (`gh api ...` with `GET` only; change no setting on GitHub) and compare the output with the quoted one; where the live rule has changed since 2026-11-15, say so.
4. The foundation check on the corrected tree, `python -B elements/common/foundation_check.py` without `--skip-test-citations`, and `python -B gate/run_tests.py elements/common`.
5. That no marked gap of this reading stays anywhere in tracked files (search the tree of your clone for a `TODO` about the rule or a sentence saying that no such rule or reading exists yet).

## Answers settled for this cycle (step 4)

The change of the task touches a trust boundary (the installer's block and the CI workflow); this correction touches neither file, and you are told so all the same. The task holds no operation that cannot be undone; the correction reads the rule and changes no setting.

## The author's gap, carried to you

The author's report names as unread the section "Reading the foundation" of `elements/common/way_of_working.md` (the author read WAY-16, WAY-84, WAY-90, WAY-71, WAY-82, WAY-34 and the element's template and skill instead). Select your own foundation by the parts the correction touches (`decisions`, `environment-facts`) as that section gives, and judge whether anything it selects bears on the entry.

## What to give back

First line, findings with grades and places (the reviewer alone grades and scopes), the checks you ran with command and exit code, your **Unread material** (or `none`), **Searches not found or unclear** (or `none`), and your working copies and their removal. Keep secrets and personal data out.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
