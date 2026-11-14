# Handoff — correction 1 for the human's remarks (the stale citations)

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator; the human's remarks on the open request bind the correction. You have no human to ask: return `questions` or `blocked` to the orchestrator. Never label an answer as the human's approval.

## Worktree, branch and range

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`, head `306a122959b3d2e72d76ad3a2d01a2bd1655f9b4` (confirm with `git rev-parse HEAD`); the tree is the reviewed and gated tree, the record's copy is removed from it. Your range starts at that head. You are the only agent writing in this worktree now (a reviewer reads it at the same time and writes nothing).
- Commits: messages in English, imperative, short; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files. Never push. Leave the worktree clean.

## Method and stage

You made the fix of the review's Minor findings earlier in this cycle and are resumed for this correction. Make it with `task-cycle/change/SKILL.md` (`make-change`), the variant "a correction for the human's remarks"; read `task-cycle/change/fix.md` if the method names it for this variant. Stage: this one correction and nothing else.

## The remarks that bind

The human's remarks, word for word: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/correction-1-remarks.md` (read it whole). They give three answers: the first item's first part is let through (no change); the first item's second part is fixed in this request; the second item asks a fresh reviewer to read the 24 unread decisions (a reviewer does that at the same time as you, read-only; do not read or judge those decisions yourself, and do nothing for that item); items 3–9 are accepted (no change).

## What to do

Fix the two places that cite WAY-168 for a sentence it no longer says: the *Rationale* of WAY-241 in `foundations/decisions.md` ("A field binds only where a decision of the product carries it (WAY-168)") and `product-guidelines/testing/template.md:229` ("a field naming no decision stands as an example (WAY-241, WAY-168)"). The remarks say "cite WAY-173 or drop the citation, as m1 settles", where m1 is the finding quoted in the request's *Minor findings* and in `reports/return-review-report.md` (read that finding whole). Rule of the orchestrator: cite WAY-173 (the decision under which a product adopts the recipes of the-way's testing template) where the sentence is what WAY-173 says; otherwise drop the citation; use the same choice in both places, and state in your report which you took and why. Read WAY-241, WAY-173 and WAY-168 whole (as they now stand) before you write. Editing the *Rationale* of WAY-241 changes no binding sentence, so no decision becomes "changed" for the check of the foundation; change no binding sentence, no *Verification* and no other word of those two places. Search the repository (`foundations/`, `elements/`, `product-guidelines/`, `task-cycle/`) once for any other place that cites WAY-168 for "a rule that names no decision is an example", and correct such a place in the same way; report each place you find and each you leave, with why.

## Checks

Run, each with command and exit code in your report: `python -B elements/common/foundation_check.py` (exit 0, `0 errors`), `python -B gate/run_tests.py elements/common` and `python -B gate/run_tests.py product-guidelines` if that directory holds tests (the command reports it where it holds none). The gate with no directory is the orchestrator's alone.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/correction-1-report.md` (this cycle's handoff overrides any general instruction not to write report files): status, commits, each place changed or left with the reason, each check with command and exit code, the own-work check, questions and concerns, **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Stop every background process you started before you return. Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
