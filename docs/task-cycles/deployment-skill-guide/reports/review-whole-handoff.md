# Handoff — review of the whole change (task `deployment-skill-guide`)

You did not make this change. Review it as `review-change`: read `task-cycle/review/SKILL.md` whole in the
worktree and follow it; its variant is the whole change. Read-only: you change no file of the repository.

Worktree (work from its root): `the task's worktree`.
Range: base `d40d1cb942c4fbaddb7ece1dc6d472d15cd83430` to head `a900916` (one commit, by the one author, no
plan, no slices, no spec). Changed files: `project-level/task/deployment_skill_guide.md` (+336),
`project-level/task/skill/resolve_gaps.md` (+5 -1), `foundations/decisions.md` (WAY-139, +32 -6).

Frozen task (read whole): `.runs/task-cycles/deployment-skill-guide/task.md`. Check every *To do* item 1-7,
both rows of *Settlements to record*, and source fidelity of the fragments against the loop2 files at the one
commit `e54f23c0ea3bd1db13d2635333417eb50412d6a0` (a checkout is at `the local checkout of loop2`; read with
`git -C the local checkout of loop2 show e54f23c0ea3bd1db13d2635333417eb50412d6a0:<path>`; do not change loop2).
Source fidelity includes the privacy requirement: no real public address of the game and no sender mailbox
address in the author's domain anywhere in the changed text, found by your own search of those loop2 files for
such strings and of the changed files for them; name in the report only that you searched and the result.
The author's report: `.runs/task-cycles/deployment-skill-guide/reports/author-report.md`. Its "Unread material"
says the author read loop2's `references/` files only in part and the tail of WAY-140's *Rationale* not at all;
read the loop2 passages and the part of WAY-140 you need for your judgments yourself, and say in your report what
you left unread.

The orchestrator's answers of step 4: trust boundary no; irreversible operation no. You select your own
foundation reading by the parts of the change (`project-level` is the touched part; `foundations/decisions.md`
is a file collecting entries about several parts, so the parts WAY-139 names) per "Reading the foundation" in
`elements/common/way_of_working.md`, and state in your report how many decisions you read whole and how many by
title only. The-way has no coding or testing guidelines of its own for this kind of change (WAY-328).

The orchestrator has no view on the author's remarks "Problems as observed" (WAY-09 does not name a guide among
what `project-level/` holds; length of 336 lines against "do not copy the whole skill") and on the author's
choices 1 and 3 in the report; judge them like any other point, and grade and scope each yourself.

The report: write it to `.runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md` in the form
the method gives, its first line `PASS <sha>` or `FAIL <sha>` with the head's full SHA, with the checks you ran
and their command and exit code, **Unread material** and **Searches not found or unclear**. Return the first
line, the path and the questions if any.
