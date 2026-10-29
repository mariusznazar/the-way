# Handoff — review of the return step, task `rejected-from-refinement`

## Delegation

Mariusz asked this session to carry the accepted task below through the-way's task cycle to a
reviewable pull request into `foundations`; he reviews the request, not intermediate steps. You
review the return step's commit as an agent that made none of the change. Never ask Mariusz
anything; questions go to the orchestrator.

## Where and how

- Worktree (read only, from its root): `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`,
  branch `task/rejected-from-refinement`.
- Method: `task-cycle/review/SKILL.md` in the worktree. Read it whole; read a file it names only
  when the step or variant that names it comes. You review the return step's range.
- This is a change to the-way itself: `agent-instructions/README.md` governs it.
- Range: `1267e733e9d84581ce63d29d08da3744bd1bdadd..c6ee066` (one commit). The change before it,
  `d7a205c..1267e73`, passed the review of the whole change; its report is
  `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\04-review-report.md`.
- Review the range against the task and the entries the return step compares or corrects:
  WAY-134 and WAY-154 as `1267e73` left them, and WAY-29, WAY-35, WAY-113. You select your own
  further foundation reading for the parts the range touches.
- Report: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\08-return-review-report.md`;
  first line `PASS <sha>`, `FAIL <sha>` or `questions`. Return that line, the report path and a
  one-line check result. Do not run the full gate; focused checks your method calls for are yours.

## Answers of the start

- Trust boundary: no. Irreversible operation: no. Open design choice: none. Route: one author
  without a plan. Guidelines: none — the-way has no `guidelines/`.

## Inputs

- Frozen task, read whole: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\task.md`.
- Return step report: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\06-return-step-report.md`.
