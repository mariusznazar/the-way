# Handoff — reviewer of the return step's commits (`review-change`: the return step's commits)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's approval. You review as an agent that
made none of this change; grade and scope are yours. Your questions go to the orchestrator.

## What you review

- Worktree (read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Method: `task-cycle/review/SKILL.md` sections 1–4 (the return step's commits are reviewed as section 2 gives, against the task and the foundation entries the
  return step writes or corrects); not `fix.md`, not `whole_change.md`.
- Range: `51cae12..b36014a` (compute the diff yourself with `git diff 51cae12..b36014a` and `git log 51cae12..b36014a`; confirm `git rev-parse HEAD` is `b36014a`).
  The commit changes `foundations/decisions.md` only.
- Report path: `docs/task-cycles/weekly-process-audit/reports\review_return_report.md`.
- The return step agent's report (a set of claims to verify): `.runs/task-cycles/weekly-process-audit/reports/return_step_report.md`; its handoff, with what it was to do:
  `.runs/task-cycles/weekly-process-audit/reports/return_step_handoff.md`; the rules it followed: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`.

## Selection

- The frozen task, whole: `.runs/task-cycles/weekly-process-audit/task.md`; the plan: `.runs/task-cycles/weekly-process-audit/plan.md` (its decisions are numbered two lower than the
  log now: the audit's decisions are WAY-329…WAY-340; the plan's "row n" = WAY-(328+n)).
- The decisions the commit writes or changes, each whole in `foundations/decisions.md` by identifier: WAY-332 (the examples of what the count refuses and what the
  session adds), WAY-336 (the rewording of "stage report"), WAY-337 (the working time without the wait for tools; a call that starts, messages or waits for a subagent is
  the subagent's work; its Scope gains `task-cycle`), and the two new ones WAY-341 (which locations-file entries the audit reads) and WAY-342 (the version of the-way of
  a cycle of its own history). Also WAY-330 (what the part's own scope may name), WAY-328 and WAY-48, WAY-73 (when an environment fact stands), WAY-95, WAY-97 and WAY-99
  (which words take a glossary entry), WAY-36 and WAY-134 (a choice that binds after the merge; the entries a row carries), and the glossary and part map as they stand.
- The code each corrected or new entry is compared with: `process-audit/audit_count.py` (docstring, the entries it reads, the version given to a cycle of its own history),
  `process-audit/SKILL.md`, `process-audit/problem_register.md`, `task-cycle/cycle_stages.py` (docstring).

## What to judge

- Does each corrected or new entry say what the code does, and nothing broader or narrower than the task and the human settled (WAY-263: an entry that restates a settlement
  differently, more broadly or without a qualification, is Important)? The two new entries are marked `the cycle's` (they come from no row of the task): do they bind a
  choice that binds later users and was not settled, and are they written without inventing a rule?
- The choices the return step left in the cycle record and wrote no decision for (the command's options, the conservative series rule, the reading of the *Plan* item):
  is that right by WAY-36?
- The decision not to write environment facts and glossary entries: is that right by WAY-73, WAY-95, WAY-97, WAY-99? (The words "issue" and "series" are used in the
  audit's decisions in a meaning of their own.)
- The code mismatches the return step reported and did not change (the citation of WAY-338 in `cycle_stages.py`; "stage report" meaning `stages.md` in `audit_count.py`;
  the open issue's count of cycles in which the problem "stands" against the task's "came back"): grade each as a finding of this review (Minor unless a sentence the
  files hold would be read wrongly) and say whether it lies within the task.
- The foundation check (`python -B elements/common/foundation_check.py`) must report 0 errors; run it, and any focused check you need.

## Report

Write the full report to the report path, first line `PASS <head sha>` or `FAIL <head sha>`. Include the findings by grade, each with its place, reasoning and evidence;
**Declined to judge**; each check you ran as command and exit code; each reach beyond the dispatch; **Unread material**; **Searches not found or unclear**. Return only the first
line, the counts of blocking, Minor and out-of-scope findings, a one-line check result and the report path.
