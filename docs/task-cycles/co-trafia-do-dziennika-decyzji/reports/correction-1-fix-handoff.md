# Handoff — the fix of the blocking findings of the review of the unread decisions (correction 1)

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator; the human's remarks on the open request bind the correction (`reports/correction-1-remarks.md`: the human asked that a fresh reviewer read the 24 unread decisions in this request and that the correction fix what that reading finds). You have no human to ask: return `questions` or `blocked` to the orchestrator. Never label an answer as the human's approval.

## Worktree, branch and range

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The reviewed head: `306a122959b3d2e72d76ad3a2d01a2bd1655f9b4`; the first part of this correction (the two citations of WAY-241) is your commit `7a5fea4`; your range for this fix starts at that commit (`7a5fea4..HEAD`). You are the only agent writing in this worktree now.
- Commits: messages in English, imperative, short; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files. Never push. Leave the worktree clean.

## Method and stage

You are resumed. Make this fix with `task-cycle/change/SKILL.md` (`make-change`), the variant "the fix of a review's findings", with `task-cycle/change/fix.md` where the method names it. Stage: this one fix, nothing else.

## The findings

The findings file, cut word for word from the reviewer's report: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/unread-review-findings.md` (read it whole); the full report is `reports/unread-review-report.md` (read around a finding only where it needs it). It holds two blocking findings, both Important and within the task: I1 and I2. The reviewer's Minor findings (m1–m5) and the finding outside the scope (o1) are not part of this fix: do not touch them.

## Rulings of the orchestrator for the choices the findings leave

- I1: settle as the reviewer says — in `README.md` and `agent-instructions/README.md` write "each decision that a change adds or whose binding sentences it alters" and "each invariant that reads `test` whose sentence a change rewords while no file citing it changes" (the two qualifications the entries and the script's docstring carry), in the same plain words as the file's neighbouring text; change no other word of those lines.
- I2: widen, the reviewer's first way (it is the task's own wording: row 9 and *To do* 6 say a change of a test that carries a line `decision:` is named in the request as a change of an invariant test is). Widen the two places that name only the changed line — kind 7 of `task-cycle/skill/request_template.md` and the lower part *Foundation entries* of the same file — and the *Verification* clause of WAY-03 in `foundations/decisions.md` — to name each test that carries a line `decision:` and that the change adds, drops or alters, whether it alters the test or only its line. WAY-03's binding sentences stay as they are (no human acceptance needed); a *Verification* clause is no binding sentence, so no decision becomes "changed" for the check of the foundation, and WAY-03 stays held by its pair of examples and its test lines. Keep every heading, group name and kind number of the request template.

## Checks

Run, each with command and exit code in your report: `python -B elements/common/foundation_check.py` (exit 0, `0 errors`), `python -B gate/run_tests.py elements/common`, `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py agent-instructions`. The gate with no directory is the orchestrator's alone.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/correction-1-fix-report.md` (this cycle's handoff overrides any general instruction not to write report files): status, commits, for each finding what you did or why you hold it wrong (with evidence), each check with command and exit code, the own-work check, questions and concerns, **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Stop every background process you started before you return. Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
