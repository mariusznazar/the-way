# Handoff — a correction for the human's remarks (resumed one author)

You are resumed as the one author of this cycle, for a correction after the request was reviewed by
the human. The orchestrator's delegation and answers in `reports/author-handoff.md` stand. Nothing
here is a human's approval beyond what the remarks file quotes as his words.

- Variant of `make-change`: **a correction for the human's remarks**. Read that part of
  `task-cycle/change/SKILL.md` again.
- Worktree: `the task's worktree root`, branch
  `task/backlog-line-for-plan-tasks`, head `7ca864236afac802d03ebb74d3fbe66bee1b755d` — the commits
  that add and remove the record's copy lie on top of `06144e9`, and the tree equals that of
  `06144e9`. Your commits go on top of the head. Never touch `docs/task-cycles/` (the orchestrator
  commits the record).
- The remarks, which bind: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-findings.md`
  — the human's rule for item 1 in his words and its form, the finding behind it, and five Minor
  findings (item 3) in the reviewers' words. Do all of it; nothing else. The human let items 2 and 4
  of the request through; they are not yours. You may answer, with evidence, a finding you hold
  wrong, which the reviewer then judges; the human's rule is not a finding.
- Boundaries and answers of the orchestrator:
  - The rule of item 1 stands in one place, `project-level/task_line.md`; other files point to it.
    Both halves are written there: the refiner's own line carries its identifier and its own
    dependencies where a line already stands as where it is made; and the agreement of the lines of
    the tasks it waits on and of the tasks that wait on it, each read before it is written, only a
    missing field added, no line written for a task that has none yet. The orchestrator's
    correction of dependencies when the plan changes stays.
  - The forms (identifier field, dependency field) are still the task place's rules, read through
    `task-rules`; no form of the-way's own, no private path, no note link in any tracked file.
  - Item 3's fourth finding (more binding sentences than the form allows in WAY-154 and WAY-107):
    regroup within one to three sentences without changing what binds; where a rule cannot be kept
    in three, return `questions` rather than drop it. The third (long lines): rewrap to the width of
    the neighbouring lines of the file, and say in the report the width you used.
  - Where WAY-154, WAY-329 or other entries need rewording for the rule, edit in place (WAY-07). Add
    no decision unless the rule cannot stand in WAY-154 or WAY-329.
- After the correction, take the return step again for what the correction touches: read
  `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md` whole, compare the
  entries you changed and the part map of the touched parts with the files, and correct what no
  longer matches; say in the report what you compared and what you found, or `none`. This is the
  one dispatch for both; the reviewer reads the whole range of your commits.
- Checks, each with command and exit code in the report: `python -B elements/common/foundation_check.py`,
  `python -B instruction-files/check_instructions.py .`,
  `python -B task-cycle/test_tracked_files_private_paths.py`. Not the `project-level` directory and
  not the full gate; the orchestrator runs it on the corrected tree.
- Commits: explicit paths, English messages, no `git add -A`.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/correction-report.md`
  — for each remark, made (commit and place) or contested (evidence); the return step's comparison;
  **Unread material**, **Searches not found or unclear**, your own-work check (name the requirement
  most likely unmet — the rule of item 1 across the orders in which two refiners run, for a new line
  and an existing one, for a task with and without dependencies — and run a check that would catch
  it), the checks with commands and exit codes, any reach beyond this handoff. Return status,
  commits, a one-line check result and the report path.
