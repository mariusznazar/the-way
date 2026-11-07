# Findings for the fix — Minor findings of the review of the whole change

Source: `reports/04-whole-review-report.md`, `PASS 3601aba4d9277868e8291ffe190c49427bdeb4a6`. No blocking
findings. The two Minor findings below lie within the task and are not marked outside its scope; they
are fixed before the request opens (WAY-161). Reviewer's words:

### Minor

1. `foundations/decisions.md` WAY-307 *Rationale* (the last sentence of its *Rationale*, "one more file kept with the spec, which reaches the record of the cycle with the rest of its directory") and WAY-306 *Rationale* ("no automatic check finds that"). `elements/decisions/template.md` ("Where entries go" bullets on *Rationale* and *Rejected*) bars a *Rationale* the author writes from naming a file or count, or "what the process's own tools do or lack today". "One more file" is close to a count of files, "reaches the record of the cycle" tells what the copy step of the record does today, and "no automatic check finds that" tells what the checks lack today. Each fact comes from the task's *Need*/*Context* and is true, and none is a binding sentence, so the effect is a slightly looser entry; the next change to the check or the record would leave the sentence stale. Lies within the task (the entries are part of the change). Evidence: `foundations/decisions.md` WAY-307 and WAY-306 *Rationale* paragraphs, compared with the template lines quoted above. Offered fix: drop "one more file kept with the spec, which reaches ... directory" to "the cost of keeping the copy", and "and no automatic check finds that" to a statement of the risk only.

2. `task-cycle/skill/spec_review.md:6-8` and WAY-307 *Verification*. WAY-307's `complies` example says the dispatch of the review of the revision "names both" and `violates` says it leaves the reviewer to find the earlier version. The orchestrator's file `spec_review.md` (the sentence the task fixes word for word: "keep the spec as `spec-reviewed.md` beside it; ... comparing the two") does not say that the copy goes into the dispatch; that is said only in the reviewer's method, `task-cycle/spec/SKILL.md:18-20` (the dispatch carries it). An orchestrator who follows only `spec_review.md` and not the reviewer's method may still omit the path, which is the exact gap question 3 of the task wanted to close for the reviewer. Not Important: the task fixed these words and "comparing the two" implies the reviewer gets both; the reviewer's method now says what the dispatch holds. Lies within the task, but fixing it needs words beyond the task's quoted sentence, so it is the cycle's call. Evidence: `spec_review.md` text above; `foundations/decisions.md` WAY-307 *Verification*.

## The cycle's call on finding 2 (orchestrator's choice, an autonomous choice, not the reviewer's grade)

Do not change the sentence of `task-cycle/skill/spec_review.md` that the task fixes word for word, nor
the other four sentences of *To do* 1–4. Remove the mismatch where it lies in the part the change
writes freely: make WAY-307's *Verification* examples say only what the skill texts say (the reviewer
of the revision compares the revision with the spec as reviewed, and the reviewer's method has the
dispatch carry the copy's path), without claiming more about the orchestrator's file. If you hold that
this cannot be done without a word in `spec_review.md`, say so in the report and leave
`spec_review.md` unchanged.

## What to do

Resume as the one author, variant "the fix of a review's findings" (`task-cycle/change/SKILL.md`):
fix the two Minor findings, run the affected checks again (`python -B elements/common/foundation_check.py`,
`python -B gate/run_tests.py task-cycle`), commit by explicit paths with an English message, and
answer with evidence any finding you hold wrong. Write the fix report to
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\reports\06-fix-report.md`
(commands with exit codes, own-work check, **Searches not found or unclear**). Return status, commits,
one-line check result and the report path. The fix range runs from `3601aba`. Do not push; do not run
the whole gate.
