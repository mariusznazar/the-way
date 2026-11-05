# Handoff — the fix of the whole-change review's findings

You are the one author of this change, resumed for a fix. The review of the whole change returned
`FAIL 5b685df`: its report is `docs/task-cycles/pr-description-schema/reports/whole-review.md`, and
the one blocking finding, I-1, stands in the reviewer's words in
`docs/task-cycles/pr-description-schema/reports/whole-review-findings.md`.

Follow `task-cycle/change/SKILL.md` in its variant **"the fix of a review's findings"**, reading
`task-cycle/change/fix.md` as it gives. The same worktree, branch and rules as your first handoff
(`reports/author-handoff.md`): commit on `task/pr-description-schema`, never push, nothing under
`.runs/` committed, no full gate run, no commit while one of your test runs is going. Where you
write or change a foundation entry, do it through the element's skill, as
`task-cycle/skill/foundation_step.md` gives, the mark `the cycle's` and its two sentences of meaning
included. Fix only I-1; the Minor findings M-1 to M-4 are not yours to fix. Where you hold the
finding wrong, answer it with evidence instead.

Run the affected checks again (`python -B gate/run_tests.py task-cycle`,
`python -B elements/common/foundation_check.py .`, and any other directory your fix touches), each
with its command and exit code.

Write your report to `docs/task-cycles/pr-description-schema/reports/fix.md` as `fix.md` gives it,
with the meaning sentence in Polish of each entry written or changed, your checks, reaches and
**Searches not found or unclear**, or `none`. Return your status, your commits, a one-line check
result and the report's path.
