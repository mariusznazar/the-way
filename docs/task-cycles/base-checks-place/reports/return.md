# Return step - base-checks-place

Status: done. Commits: none. Written: none.

Compared with the code (task-cycle/skill/SKILL.md step 4, head b9b93af):
- WAY-140: the new sentence puts the separate base checkout under the worktree's ignored `.runs/`, so the cycle still writes only in the task's worktree (line 68 unchanged); no effect outside the repository. Matches.
- WAY-160: the sentence concerns the base-commit measurement, not the finished change's gate; the orchestrator's gate run on the request tree is untouched. Matches.
- WAY-256: the sentence is one instruction of step 4 and stays in SKILL.md, not in a file beside the skill. Matches.
- Part map `task-cycle` (files task-cycle/**, dependencies, trust boundary none): change stays inside the part; no entry change needed.
- Task carries no settlement row or projected entry; record_template.md not edited.

Searches not found or unclear: none.
