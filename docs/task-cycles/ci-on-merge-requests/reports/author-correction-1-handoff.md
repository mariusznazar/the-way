# Handoff: author, correction 1 (the human's remarks on the request)

## Who asks and what you may decide

The human who requested this task cycle has delegated its intermediate choices to the orchestrator, who dispatches you. Your answers to the human come only through your report. Nothing you decide is the human's approval.

## Where you work

- The task's worktree: `the worktree of the task` (branch `task/ci-on-merge-requests`, the-way itself, no `.the-way` pin). Work only there. The branch head is the merge commit `3eacbc1`, which merged the remote target branch `foundations` into the task branch; everything below stands on that head.
- Your directory for working copies: `.runs/author-correction-1/` (under the ignored `.runs/` of the worktree). No other place.
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/author-correction-1-report.md`.

## Your method and stage

- Method: `task-cycle/change/SKILL.md`, read whole. Your variant, in the words of its row: **"a correction for the human's remarks"**.
- Boundary: you make the change the remark below binds, commit it by explicit paths (`git add <file> <file>`, never `-A`, `.` or `-a`), run the affected checks, and return. You do not review, do not run the gate, do not write the request's description, and do not seek the human's approval.
- Foundation entries are written as `task-cycle/skill/foundation_step.md` gives (read it whole); for an environment fact read `elements/environment-facts/skill/SKILL.md` and the files beside it that its steps name, when the step that names one comes, and `elements/environment-facts/template.md`.

## What happened before

The request is https://github.com/mariusznazar/the-way/pull/127 (task: run the one command of tests in CI on every merge request, and signal vulnerabilities in libraries already used). The frozen task document is `.runs/task-cycles/ci-on-merge-requests/task.md`. Its change is in the range `21ecb62..351ffb1` (the last cycle commit `b344595`, then the record's pair `f891ecb` and `351ffb1`), merged into the current head `3eacbc1`. Since the first cycle, `foundations/decisions.md` of the target branch has been divided into 28 topical sections, and the merge re-applied this branch's changes to WAY-09, WAY-16, WAY-160 and WAY-206 on that log; a reviewer judges that merge separately and you do not.

The human answered the request's description. His remarks are in `.runs/task-cycles/ci-on-merge-requests/reports/correction-1-remarks.md` (the file holds the comment word for word; the three remarks stand below).

## The remark you carry out (remark 2, copied word for word)

> 2. Close it in this request. Read the branch rule now that it exists and write that reading into the decision whose *Based on* holds the open `TODO` for it (WAY-16, rows 1 and 2), the same way the three GitHub facts of this request are written (address, date read, the passage), so that no marked gap is left on the main branch.

The remark it answers (item 2 of the request's description) said: one decision, the one that says the one command also runs in CI and that its result is a required check with a bypass for the owner, rests on a setting of GitHub that nobody had read, because the branch rule did not exist; the decision is marked with an open gap (`TODO` in its *Based on*).

What binds you from the human's other remarks:

> 1. Done by Mariusz on 2026-11-15 at 11:02: the branch rule is set. A repository ruleset `foundations_tests` (id 27308872), enforcement active, targets `refs/heads/foundations`, requires the status check `tests` (source GitHub Actions, integration id 15368), does not require the branch to be up to date before merging, bypass: Repository admin role, mode always; it also restricts deletion and blocks force pushes. Read it yourself with `gh api repos/mariusznazar/the-way/rulesets/27308872` before you write it down.

This is the human's account of what he set; it is not your source. Your source is your own reading of the rule, run by you, quoted word for word, as `elements/environment-facts/template.md` gives the form of a reading.

> 3. Let both through (the two tests that fail as root, and a pull request that edits the CI file). No task.

Remark 3 changes no code and asks nothing of you: do not touch `task-cycle/test_remove_merged_worktrees.py` or the workflow `.github/workflows/tests.yml`.

## What to do

1. Read the rule with the command the human names (`gh api repos/mariusznazar/the-way/rulesets/27308872`, narrowed with `--jq` to the fields the fact rests on, as the template asks: a reading holds no secret and reads only those fields), and write it as an environment fact in `foundations/environment_facts.md` by the element's skill: the setting is one people of the product change outside the repository and no page open to a reader shows it, so by WAY-84 its source is a reading. State in the fact what the reading shows (the ruleset's name and target, that it requires the status check `tests` of GitHub Actions, and its bypass for the repository admin role, mode always), and nothing the reading does not show.
2. In WAY-16 (`foundations/decisions.md`), replace the descriptive `TODO` in *Based on* with a name of that fact, by its identifier alone, as WAY-90 gives, next to the two facts already named there (`github-required-status-checks`, `github-ruleset-bypass`). Read the rest of WAY-16 and change whatever else in it says the rule is not yet set or that no reading exists (its *Based on*, its *Rationale*, *Rejected*, *Verification*), and nothing else; do not widen the decision.
3. Search the repository, the files of this change included, for any other place that marks this gap as open — a `TODO` about the rule, a sentence that says no reading exists yet — and correct or report each. The request's description is the orchestrator's; do not edit it.
4. Check the entry's form with `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) and run the tests of the directories the change touches, one directory at a time (`python -B gate/run_tests.py <directory>`, for example `elements/common`). Never run the full gate: a full run is memory heavy, belongs to the orchestrator and waits for a signal of the day's advisor.

## Answers already settled for this cycle (step 4)

- The change of the task touches a trust boundary (the installer's block and the CI workflow). Your correction touches none of those files; a reviewer is told so all the same.
- The task holds no operation that cannot be undone; setting the branch rule was the human's, and it is done. You change no setting on GitHub: your command reads the rule only (`gh api` with GET, nothing else).
- The route is one author without a plan. There is no spec and no plan.

## Reading the foundation

Read by "Reading the foundation" in `elements/common/way_of_working.md` and by the decision index script it gives (the log is now in topical sections). At least: WAY-16, WAY-84, WAY-90, WAY-71 (descriptive `TODO` and where the main branch may hold it), WAY-82, WAY-34 and the three facts `github-required-status-checks`, `github-ruleset-bypass`, `github-dependabot-alerts` in `foundations/environment_facts.md`, with what `way_of_working.md` selects beside them for the parts you touch (`environment-facts`, `decisions`). The guideline files and part map you need are those of the parts `decisions` and `environment-facts`; the task's *Decisions in play* are in the frozen task.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## What your report holds

As `task-cycle/change/SKILL.md` gives: status, commits, checks with command and exit code, the own-work check, your reach beyond the handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), and the working copies and their removal. Keep secrets and personal data out of it.
