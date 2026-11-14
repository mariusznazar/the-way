# Handoff — correction 1 for the human's remarks (task `deployment-skill-guide`)

You are the one author, resumed. Variant of `make-change`: "a correction for the human's remarks". Worktree and branch as before
(`the task's worktree`, `task/deployment-skill-guide`, head `31120e915a48edcbb3c59ad387b2c7f6ae9f8fc6`;
the code is the same as at `4e60278`, which both reviews passed; the commits after it only added and removed the record). The remote
target branch had not moved (`d40d1cb`), so nothing was merged.

The remarks bind (the human's, written by the day's advisor in the human's name), word for word in
`.runs/task-cycles/deployment-skill-guide/reports/correction-1-remarks.md`. What they ask of this correction:

1. In the guide `project-level/task/deployment_skill_guide.md`, the paragraph in part 5 (what the agent does and what the human does) on the
   automation the product already has: change "A skill says what that automation does too" to the wording "A skill names that automation too" and add
   one clause saying that the human's merge is what starts the automated deployment. Keep WAY-140 untouched and say nothing the guide
   does not already say about it.
2. Take the `[loop2: …]` marker off "60 days" (GitHub's rule for scheduled workflows), keeping the sentence otherwise as it is.
3. Do not touch anything else. The third matter of the remarks (WAY-09's list and the part-map sentence not naming the guide) is a task made
   afterwards by the orchestrator, not part of this correction; do not change WAY-09 or the part map.
Items 2 to 6 of the remarks need no code.

Do not run the product's full gate. Run, with command and exit code: `python -B elements/common/foundation_check.py`; the
`project-level` tests (`python -B -m unittest discover -s project-level -p "test_*.py"`); `python -B task-cycle/private_paths_check.py
project-level/task/deployment_skill_guide.md`; and a search of the changed text for the game's real address and the sender's mailbox
domain (taken from the loop2 files; name only that you searched and the result). Commit on the branch, do not push.
Report: `.runs/task-cycles/deployment-skill-guide/reports/author-correction-report.md`, with **Unread material**, **Searches not found
or unclear** and your own-work check. Return status, commits, one-line check result, path.
