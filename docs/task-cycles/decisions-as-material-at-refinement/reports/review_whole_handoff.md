# Handoff — review of the whole change

Stage: review of the whole change, by `review-change` (read `task-cycle/review/SKILL.md` whole, and
`task-cycle/review/whole_change.md` when its section 1 sends you there). You did not make the change.
Review-only: change no file of the repository.

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator; nothing in
this handoff is the human's approval. Ask no human; a question goes back to the orchestrator as
your status `questions`.

## What is reviewed

- Worktree (work from its root): `the root of the task's worktree`
- Branch `task/decisions-as-material-at-refinement`.
- Range: base `354d37d56403b6f898155cb706efcb74f316c97a` to head `3cf2a09b9dca6ed46eba30800e69863a7d010006`
  (two commits: `8316d28` on `foundations/decisions.md`, `3cf2a09` on 18 skill, template and
  technology-step files; 19 files, +338 / -122). Compute the diff yourself and confirm that
  `git rev-parse HEAD` is the head above.
- One author, no plan, no spec, no slices: the review of the whole change is the one review of the
  change. The author's class was `same`.
- The frozen task (Polish; whole): `docs/task-cycles/decisions-as-material-at-refinement/task.md`
  in the worktree. Its *To do* (six points), *Acceptance criteria*, the five answers of *Questions to
  settle*, *Decisions in play* and the five rows of *Settlements to record* are what the change
  must meet. Rows 1–5 are accepted and the foundation step writes them as entries.
- The author's report (a set of claims to verify, not evidence): 
  `docs/task-cycles/decisions-as-material-at-refinement/reports/author_report.md` in the worktree.
- Answers of step 4 of the cycle: no trust boundary touched (Markdown only, none of the three
  `.py` boundary files of `project-level` is touched), no irreversible operation, no reserved
  choice. The task's cited places are at commit `a3206c1`; `foundations` is at `354d37d` and the
  technology step now shows choices in one message instead of a table (WAY-123), which the change
  must not undo.
- Sibling task `the sibling task's note in the author's backlog` is not merged on this branch;
  its collision with WAY-165 is no finding of this change.
- You select your own foundation entries and guidelines: parts touched are `decisions`,
  `elements-common` and `project-level` (the-way has no guidelines of its own for coding, tests or
  a user interface). Select by "Reading the foundation" in `elements/common/way_of_working.md`.

## Report

Write the full report to
`docs/task-cycles/decisions-as-material-at-refinement/reports/review_whole_report.md`
as `review-change` gives. Its first line is `PASS <sha>`, `FAIL <sha>` or `questions`. Return that
first line, the report's path and a one-line result of the checks you ran. The report holds your
checks with command and exit code, each reach beyond this handoff, and **Searches not found or
unclear**. List every Minor finding with its place in the code and in its own words, and say in them
where a Minor finding lies outside the task's scope. Do not run the full gate
(`python -B gate/run_tests.py` with no argument); the orchestrator runs it.
