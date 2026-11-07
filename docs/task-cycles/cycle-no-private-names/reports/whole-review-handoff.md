# Handoff — review of the whole change

You review the whole change of a the-way task cycle (`implement-task`) as an agent that did not make
it. You are read-only: change no file of the worktree, commit nothing.

## What is reviewed

- Worktree: `.`, branch
  `task/cycle-no-private-names`.
- Range: base `ad44b842d62cf1e4b4119779ad63d4048f5866af` (`ad44b84`) to head `b6d93e8` (three
  commits: `c8fe9f6`, `4643660`, `b6d93e8`). Compute the diff yourself with
  `git diff ad44b84..b6d93e8`; confirm `git rev-parse HEAD` is `b6d93e8...`.
- Your method: `task-cycle/review/SKILL.md` in this worktree, whole; it names
  `task-cycle/review/whole_change.md`, which you read and follow. Variant: the review of the whole
  change. You select your own foundation and guidelines by the parts of the change (WAY-150).
- Frozen task, whole: `.runs/task-cycles/cycle-no-private-names/task.md`. Route: one author without
  a plan, no spec, no plan. No slice reviews exist: you judge the whole change.
- The author's report (claims to verify, not evidence):
  `.runs/task-cycles/cycle-no-private-names/reports/author-report.md`.
- Your report: write it to `.runs/task-cycles/cycle-no-private-names/reports/whole-review-report.md` as
  your method gives it (first line `PASS <sha>` or `FAIL <sha>`), and return the first line, the
  report path and the files changed with line counts. Include **Searches not found or unclear**
  (`none` is an answer) and the coverage of every task item (*To do* 1 and 2, the acceptance
  criterion, settlement rows 1 and 2, questions 1–5, *Questions carried to cycle*).

## What the orchestrator tells you

- Trust boundary: no (part map: `task-cycle` has none). Irreversible operation: no.
- Product guidelines: none exist (task, question 4); judge the script and its test against the
  existing scripts of `task-cycle/` (`remarks_check.py`, `request_check.py` and their tests).
- Orchestrator ruling Q1: `remarks_check.py` runs as today on the original record; the cleaning is
  one rewriting applied to every text file of the copy; then the new script and `remarks_check.py`
  run on the cleaned copy.
- Author's concern, ruled as an autonomous choice (Q2): `Task source:` of the record template. The
  working record in `.runs/` keeps an absolute path (the plan-state reader,
  `project-level/plan_state.py`, anchors a plan item's record to its task by it when it reads a
  working cycle directory); the committed, cleaned copy describes the document instead. Check the
  code path of `plan_state.py` for the committed copy of an **independent** task and of a **plan
  item** after this rule, and say whether the rule breaks the invariant
  `project-plan-state-evidence` (WAY-153). The author read the code and ran no fixture; you may run
  the reader's tests (`python -B gate/run_tests.py project-level`) and a small check of your own
  in a scratch directory outside the repository.
- The handoff for the author named `elements/decisions/SKILL.md`; the file is
  `elements/decisions/skill/SKILL.md` (an error of the orchestrator's, not the author's).
- The full gate is the orchestrator's; do not run `python -B gate/run_tests.py` without a
  directory. Focused runs are yours to choose; give each command and exit code.
- Weak points the orchestrator asks you to check first: (1) false positives and misses of the
  patterns in `task-cycle/private_paths_check.py` on real text (run it on the tracked text of the
  repository and on the frozen task, and try a few forms the author did not: a bare drive root, a lower-case
  drive letter, a Windows long-path prefix with a drive, a Windows path inside a Markdown link, a path in a table cell, a note link with an alias and an embedded image); (2) the rules in `task-cycle/skill/SKILL.md` ("The record before it is
  committed") — whether the sequence can be followed as written, whether each commit that adds the
  record (copy for a request, correction, blocked request of every cause) is covered, and whether
  `correction.md`, `blocked_finding.md`, `reserved_return.md` and `request_template.md` agree with
  it; (3) WAY-308 and WAY-309 against the entry templates and `foundation_check.py`, their
  *Rejected* material against the task's *Not chosen* options, their *Scope*, and whether a
  decision that already stands (WAY-27, WAY-153, WAY-288, WAY-294, WAY-295, WAY-296) is contradicted
  or left saying what no longer holds.
- Grade and scope are yours; this handoff calls no finding wrong, Minor or out of scope.
