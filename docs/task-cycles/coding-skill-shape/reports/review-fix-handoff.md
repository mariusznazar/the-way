# Review of the fix — maintain-coding-guidelines in the WAY-256 shape

You are the reviewer of the whole change; this is the one review of the fix your findings get. Same
worktree, read-only, and same cycle directory (`<cycle>`) as your handoff
`<cycle>/reports/review-handoff.md`. The orchestrator runs the gate in this worktree beside you.

## Method

In `task-cycle/review/SKILL.md`, the review of a fix: read the file it names for that variant.

## What you review

- Fix range: `097123e..088717a`. Your findings: `<cycle>/reports/findings.md`.
- Fix report: `<cycle>/reports/fix.md`, with the handoff `<cycle>/reports/fix-handoff.md`.
- Materials changed with it: `<cycle>/reports/assessment.md` and `<cycle>/reports/word-counts.md`.

Check that each blocking finding is closed, that the fix adds no new fault, that the walk of route 6
holds by your own reading from `SKILL.md` to `hand_back.md`, and that every figure of
`word-counts.md` matches the files at the head, recomputed yourself. Your Minor findings stay as they
stand unless the fix changes them.

Do not run the whole gate; its run is the orchestrator's.

## Report

Full report: `<cycle>/reports/review-fix.md`, its first line `PASS <sha>` or `FAIL <sha>` or
`questions`, as the method gives. Return: that first line, a one-line check result naming what failed
or did not run, and the report's path.
