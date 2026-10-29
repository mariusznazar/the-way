# Cycle record — <task title>

- Task source: <absolute path and approval date or source commit>
- Task relation: <independent | plan item | source only>
- Product repository: <path>
- Process pin: `<commit>`, or `<commit> at start; moved to <commit> by the task branch's first
  commit <sha>`
- Target branch and base: <branch and commit>
- Task branch: <branch>
- Status: running | blocked | request open | complete

## Two questions at start

- Trust boundary: <no | yes — the boundary the part map names (network, keys, deployment, files
  from outside), the files of it the change touches, and the review aimed at that risk>
- Irreversible operation: <no | yes — the operation, what the change prepares for it, the review
  aimed at that risk, and the human who performs it after deciding at the request>

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: <none — the entries and ways weighed and why each is settled |
  the choice, where it shows and the ways open>
- Execution route and reason: <one author without a plan | planned slices; orchestrator's
  judgment from the task at the start, and repeated after any reviewed spec>
- Author: <agent, class and model of the one author, for its code, foundation entries and return
  step, a class other than `cheaper` with its reason; its resumptions; any replacement during a fix
  and its reason; planned executors appear in Slices>
- Plan: <none on the one-author route | number of slices and size-report verdicts>
- Discarded attempt: <time, open design choice or oversized one-author change, report, last
  commit and changed files including foundation entries, reset base, discard confirmation and
  next route; after an open choice, spec review and renewed judgment; after size, planning | none>
- Slices returned too large: <for each, the slice, its agent's report, its last commit and files,
  reset commit, earlier completed/reviewed slices retained, and slices it was split into | none>
- Agent waiting: <native completion notification or blocking tool; live-contract limit and any
  smaller active-instruction limit; actual timeout/interruption if waiting had to resume>
- Whole-change review: <reviewer other than the author, by `review-change`; range by base and head
  commits, the report's first line and its path, changed files with added and removed line counts;
  coverage of every task item, settlement row and carried projected entry, and source fidelity;
  on the planned route, also the plan review's evidence, and for each blocking finding the slice
  it comes from, with that slice's class, or none — a gap of the plan, or the plan's *Foundation
  entries* with their writer's class>
- Review rounds: <for each code review whose findings blocked — of the whole change, of the
  return step, of the reconciliation with the target branch, of a correction — its range and
  report, the blocking findings, the fix range and the review of that fix; any blocking finding
  that remained after it; a slice's rounds stand in its row of Slices; or none>
- Weakest-point checks: <for the author and each executor: the requirement named, the check, what
  it showed and the report that states it>

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Only on the planned route, one row per slice, made in the plan's order. Where the plan lists
foundation entries, a row `Foundation entries` comes first, with its agent and head; it shares
slice 1's base, written before that agent is dispatched, so whichever review judges slice 1 covers
the entries. Write each base before the slice's executor is dispatched. The class is the one the
plan's *Model* sets, and *Risk* the plan's mark, which decides whether the slice gets a review of
its own. The mechanical check is the orchestrator's after the executor returns: what it compared and
any mismatch it passed to the review that judges the slice; a retry one class higher names the
failed executor's last commit, the failure and the retry's class (WAY-229). A slice without a review
of its own reads `judged by the whole-change review` in the last column.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|

Append one row for every dispatch, handoff, failed attempt, rerun, review and fix before the
dispatch that depends on it. Name handoff and report paths and input and output commits, so work
resumes from these files and commits without the conversation. Keep each complete handoff and
report, with secrets and personal data removed, in `reports/`; a short return routes the work and
names failed and unchecked checks and unresolved concerns. Repair an incomplete or missing report
before dependent work, and record corrections to stale paths or commit ranges. Record the evidence
read for a question or finding in the questions table, rather than loading every stage's full
report and sources again. This record is the cycle's only log; no method keeps one beside it.
During work this file, the frozen task, `stages.md`, `spec.md`, `plan.md`, `plan-size.md` and
`reports/` live under the ignored `.runs/task-cycles/<task-slug>/` directory. At the request, copy
that whole directory to `docs/task-cycles/<task-slug>/`, link the reports from these rows, commit
the copy and commit its removal immediately after; the request links the record by the SHA of the
commit that adds it. A correction after review repeats this pair.

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|

Include questions answered by a binding source as well as new micro decisions. A choice that binds
after the merge is written into the foundation (WAY-36); every other choice is its row here and
nothing else.

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|

Include the frozen task, `spec.md` where one was written, `plan.md` and `plan-size.md` only where
planning ran, code commits, tests and full agent reports, the report of a discarded attempt or
of a slice returned too large among them. Name commits and commit ranges instead of copying diffs
or files that git holds. A foundation entry the cycle writes lives in its commits; the record
keeps its meaning sentence for the request.

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|

Record the checks already failing on the base apart from the runs after the change. Where the task
moved the pin, record the gate on the commit that moved it apart as well, naming each check that
fails there and passed on the base: that is work the task carries. An executed
check is its command and exit code, with its result in one line; a report missing either returns
to its agent for repair, and a claim that tests passed does not replace them. A manual check
records its method, actor, observed result and evidence, with `not applicable` for the command and
exit code. Focused checks are not rerun merely to advance the cycle. The orchestrator runs the gate
on the tree that goes into the request and records its command, exit code and the failures it
names. Name every check that failed or did not run, with the reason; an unrun check is unchecked,
never passed. For an invariant's test the change writes, record its failing run and its passing
run as the author reports them.
For a UI change, record the author's or executor's state check and screenshot inspection: affected
components and states, method, observed result and evidence. Carry a screenshot unchecked for no
settled route, or a failed settled route with its actual result, to the request; code inspection
does not establish rendered appearance.

## Return step

- Foundation compared with code: <the entries the change writes or changes, those the task names
  and those the search of the foundation found, and the part map of the touched parts, each
  compared with the code: what no longer matched and its correction, or none>
- Decisions written or changed: <identifiers or none>
- Invariants written or changed: <identifiers, each with the task, decision or human that sets
  its rule, or none>
- Environment facts: <sources outside the product the change rests on that the foundation did not
  hold, written as facts, or none>
- Glossary terms: <a word the change uses in a meaning other than the usual one, or a term used in
  another meaning than its entry gives, written or corrected, or none>
- Part-map changes: <identifiers or none>
- Projected entries written whole or in part: <identifiers or none>
- Rows of *Settlements to record* written: <row number and identifier for each row, or none>

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: <URL and draft/ready/blocked>
- Cycle and its reasons: <as the request states them>
- Process pin: <the pin, or where the task moved it, from and to which commit and the gate on the
  commit that moved it>
- What this request settles: <identifier and meaning sentence for each entry, and each kept row
  tied to an entry already stated, with that entry (WAY-134)>
- What the foundation puts in front of the human at the merge: <each invariant test the change
  alters (WAY-03), each surface it alters (WAY-49) and each *Violated* mark it sets or clears
  (WAY-51), or none>
- Checks: <the gate's command and exit code, and each check that failed or did not run, named,
  or none>
- Human actions the request waits for: <each action the task document places in the cycle, and
  each effect outside the repository the cycle found that the document does not name, or none>
- Questions: <only those the cycle allows to reach the human, or none>
- Review findings listed: <unfixed Minor findings and findings the reviewer marked outside the
  task's scope, from the review of the whole change and every later code review, each with the
  reviewer's words and its place in the code or a note that none is named, or none>
- Blocked by review: <each blocking finding left after the review of its fix with its place and
  reason, what the fix tried, the cycle's time, models and tokens from `stages.md` with the number
  of review rounds, and the reconciliation and return step not run on that code, or none>
- Choices within the request: <count and link to the questions table>
- Writes to the task's backlog entry: <request link and state, or none>
- Process remarks on the-way: <each item from a stage report other than `none`, copied word for
  word, with the stage name and full report path; keep repeated items separate, or none>
