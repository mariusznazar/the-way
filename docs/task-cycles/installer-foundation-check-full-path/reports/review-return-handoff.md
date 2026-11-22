# Handoff — the review of the return step's commits, `review-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

## Where you work

- The worktree: `the task's worktree` (branch `task/installer-foundation-check-full-path`); the-way is this worktree, no product. Your directory for working copies: `.runs/review-return/` (directly under `.runs/`).
- Your report: `.runs/task-cycles/installer-foundation-check-full-path/reports/review-return-report.md`, first line `PASS <sha>` or `FAIL <sha>` (the file is the input of the cycle's scripts; the rule against a subagent writing a file whose name starts with `report` does not apply to it; if refused, return the report whole as your answer).
- `cycle.md` and the other files of the record directory are not yours to read, save what this handoff names.

## Your stage

Review the commits of the return step with `review-change`: read `task-cycle/review/SKILL.md` whole and follow it; the return step's commits are reviewed as its section 2 gives, against the task and the entries the return step writes or corrects. You are read-only; no full gate.

- Range: base `674c93feda110b00fab3327546a41ca26ac5e860` to head `325af473` (confirm `git rev-parse HEAD` is the full SHA that begins `325af473`); one commit, which changes `installation/README.md` alone.
- The frozen task: `.runs/task-cycles/installer-foundation-check-full-path/task.md`; read the passages you need.
- The return step's report: `.runs/task-cycles/installer-foundation-check-full-path/reports/author-return-report.md` (claims to verify). Check its comparison of the entries and the code, and whether the README change is true to the test it names and the rest of that section.
- The invariant `installation-agents-md-warnings` (`foundations/invariants.md`) and WAY-418 (`foundations/decisions.md`), with the test `InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning` in `installation/test_install.py`, are what the return step compared; they were reviewed at `674c93fe` and are not under review again, but a mismatch the return step missed is a finding. One Minor finding of the review of the fix is known and goes to the request's list: the invariant's sentence says "no warning", its test also refuses an error.
- The trust boundary: the task touches `installation/install.py` (a literal only); this range changes none of the code.
- Grade and scope are yours. Run the checks the method gives (`python -B elements/common/foundation_check.py`, the instruction check on the head) and the test the README names.

## Working copies

Remove your copies, state where each stood and that it was removed; the first paragraph of "Working copies" in `task-cycle/skill/SKILL.md` is the rule: a directory of your own directly under `.runs/`, never the system's temporary directory, removed by its path written out in full before you return.

## What to return

The report with its first line, findings graded and scoped by you, each check with its command and exit code, **Unread material** and **Searches not found or unclear** (`none` where there is none), and the line on working copies. Return the status, the first line, one line on the checks and the report's path.
