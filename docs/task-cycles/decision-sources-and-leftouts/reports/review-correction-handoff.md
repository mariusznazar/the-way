# Handoff — the review of correction 1 and the unread reading, `review-change`

You are a fresh reviewer: you did not make this change and did not write either of the earlier reviews of it. The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval. You are read-only for the repository. You do two things, in one report.

## Where you work

- Worktree: the worktree of the task, branch `task/decision-sources-and-leftouts`. Work from that directory.
- Method: `task-cycle/review/SKILL.md` of that worktree, read whole; a file it names only when the step or variant that names it comes. Variant: **a later change to an open request** (a correction), the remarks in place of a findings file.
- Range of the correction: `b679864..d48638a` (one commit, `foundations/decisions.md`, 42 added, 14 removed lines). The whole change from the base `aba5ee92a0734c2e775cc69662af669bf6455795` to `d48638a` is the context. The commits `7705860` and `b679864` above `01ab269` only add and remove the cycle's record and hold no code.
- Directory for working copies: `.runs/review-correction/` (directly under the ignored `.runs/` of the worktree). The first paragraph of "Working copies" of the cycle skill, word for word:

> An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
> clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
> directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
> in the system's temporary directory, in the scratch directory of a session or in the main checkout
> of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
> itself under its session's directory is moved into the agent's directory and the original removed,
> except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
> says, to the place the product's foundation settles for screenshots, and into the agent's directory
> only where no such place is settled. The files that a product's own tools and tests make by
> themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
> each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
> `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
> the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
> all the same and names in the report the remainder, with its full path and the reason it stayed.

- Report: `.runs/task-cycles/decision-sources-and-leftouts/reports/review-correction-report.md`, first line `PASS <sha>` or `FAIL <sha>` as the method gives; with the checks (command and exit code), **Unread material** and **Searches not found or unclear** (each `none` or the items), and, for each finding, its grade, scope and place.

## What the correction is, and what binds

The remarks of the human, word for word: `reports/correction-1-remarks.md` (in `.runs/task-cycles/decision-sources-and-leftouts/`). They bind, and you read them whole. Item 1 had the author fix three decisions the earlier review found outside the task's scope — WAY-145, WAY-139 and WAY-165 — by the same rule as the 25 entries (the source the practice was in fact taken from; leftovers in *Rejected*, a reason only where the entry, the source or the author's map gives one; leave an entry as it was if no taking can be traced). The author's report: `reports/author-correction-report.md`, whole; it gives for each of the three where the author searched, what it found and in which place, and its judgment that each adopts. The frozen task: `.runs/task-cycles/decision-sources-and-leftouts/task.md`; the reports of the earlier reviews: `reports/review-whole-report.md` and `reports/review-fix-report.md` (for the context of finding O1 and N1).

## Part A — review the correction (item 1)

Grade and scope by the method. Test at least:

1. **Source fidelity.** For each of the three decisions, compare every element the entry now says the practice has, takes, or leaves out with the source the author names: the course skill `10x-roadmap` (the author read it from a local archive of the author's course trials; you may read the same: `git show` of the tag `archive/10x-m2l1`, the skill file `.claude/skills/10x-roadmap/SKILL.md`, in the author's local repository of course trials found beside the author's other repositories — if you cannot find it, say so in **Searches not found or unclear**), the author's map of the course package and the lesson notes of m1l5 and m3l5 in the author's vault `the author's vault\` (reading only). A leftover that the practice does not in fact have, or a reason the trace does not hold, is the fault the first review found in WAY-142 (I1): look for exactly that.
2. **What the remarks allow.** *Rejected* reasons only from the entry, the source or the map; `derives from WAY-100` where the entry adopts; the closed lessons said to be closed; no private path or note link in the diff; no binding sentence changed anywhere against the base (compare the text before `- **Scope:**` of every decision at the base and at the head; only WAY-100's may differ).
3. **WAY-139's history.** The author's report says the second round of the log (commit `cfd275c`, row F3 (c) of its foundation report) removed `derives from WAY-100` from WAY-139 because "the entry no longer claims to adopt a practice from outside", that the frozen task's *Out of scope* lists WAY-139 as evidence-only, and that the author followed the human's remark, which names it, against both. Judge from the trace whether the fix is true to the source and whether either earlier statement shows a reason that the fix now contradicts without saying so.
4. **Consistency.** The new items of WAY-145, 139 and 165 against WAY-142, 270, 143–147 and 121 (the author says WAY-142 and WAY-145 both list the parked list and the blocked state as left out and do not contradict). WAY-270's *Rationale* says two questions bind "by this decision, by WAY-165 and by WAY-139, and nowhere else": check that the three entries still agree with it. Run `python -B elements/common/foundation_check.py`. Do **not** run the full gate (`python -B gate/run_tests.py` with no directory).

The Minor finding N1 of the review of the fix (WAY-142, the parked list's reason) is known and out of this correction: do not report it again.

## Part B — read what stayed unread (item 2 of the remarks)

The human asked that the reviewer of this round read, and compare, what the review of the whole change left unread (its **Unread material**, `reports/review-whole-report.md`):

1. **WAY-256, read whole** (it is a decision the change touched, in a sentence on the lessons not being open; the earlier reviewer read it only up to line 3440 of the log and not its *Rationale* in the rest, nor its *Rejected*). Open it by its heading `### WAY-256` in `foundations/decisions.md` and read every field. Say whether the change's addition agrees with it.
2. **The lesson notes of the two lessons m2l4 and m3l5**, in the author's vault (the notes of the course, files whose names begin `09-research-i-implementacja` for m2l4 and `16-debugowanie-z-ai` for m3l5; search the vault for them): read them whole, and compare with them **the leftovers and the reasons now written** in the decisions that rest on them — WAY-268 (m2l4), WAY-270 and WAY-273 (m3l5), and WAY-139 and WAY-165 where they take from m3l5 — and with the map's rows that carry them. Report each leftover or reason that the lesson note contradicts or does not hold, as a finding with its grade; report that none was found if none.

Report Part B in its own section of the report, naming what you read whole and what you read in part. Findings of Part B are graded and scoped like any finding: a wrong reason or leftover within the task's changed entries is within the task.

## Limits

You change no file of the repository. Nothing of the vault reaches the report as an absolute path or a note link: describe a note by what it is. Return with the short return the method gives: first line, checks, report path, blocking findings, Minor findings, findings outside the scope, **Unread material**, **Searches not found or unclear**.
