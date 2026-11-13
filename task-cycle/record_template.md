# Cycle record — <task title>

- Task source: <the task document and its approval date or source commit; in the working record its
  absolute path, by which the plan-state reader ties the record of a plan item to its task (WAY-153);
  the committed copy is cleaned of it and names the document by what it is, so that for a plan item
  the reader cannot anchor the copy until the plan row's *Document* links the frozen copy>
- Task relation: <independent | plan item | source only; for a plan item, the plan named by its file
  name, never by a path: the cleaning leaves this line as it is unless the check of private paths
  lists it>
- Product repository: <the repository's name or remote address, never its path on a disk>
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
- Reserved choice: <none | the choice, where it showed and the limb of the rule that takes it>
- Execution route and reason: <one author without a plan | planned slices; orchestrator's
  judgment from the task at the start, and repeated after any reviewed spec>
- Author: <agent, agent type, class and model of the one author, for its code, foundation entries
  and return step, a class other than `cheaper` with its reason; its resumptions; any replacement
  during a fix and its reason; planned executors appear in Slices>
- Plan: <none on the one-author route | number of slices and size-report verdicts>
- Discarded attempt: <time, open design choice, reserved choice or oversized one-author change,
  report, last commit and changed files including foundation entries, reset base, discard
  confirmation and next route; after an open choice, spec review and renewed judgment; after a
  reserved choice, the blocked draft request; after size, planning | none>
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
- Review rounds: <`none`, or nothing after the colon and, under this line, one entry for each fix
  round of the cycle — a fix of a review's findings and the review of that fix, a slice's round
  included — in the form below>
  - findings `reports/<file>.md`: <the findings file the fix and the review of that fix were
    given, by its path in `reports/`, opening the entry as written here; then, for a code review
    whose findings blocked — of the whole change, of the return step, of the reconciliation with
    the target branch, of a correction — its range and report, the blocking findings, the fix
    range and the review of that fix, and any blocking finding that remained after it; for the
    fix of the whole-change review's Minor findings within the task, whether it ran alone or with
    a blocking fix, its review and, where the cycle reverted it, the revert commit and the new
    finding; for a slice's round, the slice, whose row of Slices holds the rest>
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
dispatch that depends on it. In a dispatch's row the actor names the agent type the stage ran
with, `the-way-author` or `the-way-stage`, or says that it ran without its type and why.
Name handoff and report paths and input and output commits, so work
resumes from these files and commits without the conversation. Keep each complete handoff and
report, with secrets and personal data removed, in `reports/`; a short return routes the work and
names failed and unchecked checks and unresolved concerns. Repair an incomplete or missing report
before dependent work, and record corrections to stale paths or commit ranges. Record the evidence
read for a question or finding in the questions table, rather than loading every stage's full
report and sources again. This record is the cycle's only log; no method keeps one beside it.
During work this file, the frozen task, `stages.md` (step 12), `mechanism_measures.md` (step 12),
`gate_times.md` (created by the first gate run: step 2's where the pin moved, else step 4's, and
step 10's where step 4 skips its run; each later gate run appends to it), `spec.md`, `plan.md`,
`plan-size.md`, `request.md` and `reports/` live under the ignored `.runs/task-cycles/<task-slug>/`
directory. At the request, copy
that whole directory to `docs/task-cycles/<task-slug>/`, link the reports from these rows, clean
the copy and check it as `task-cycle/skill/SKILL.md` ("The record before it is committed") gives,
commit the copy and commit its removal immediately after; the request links the record by the SHA of
the commit that adds it. A correction after review repeats this pair.

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|

Include questions answered by a binding source as well as new micro decisions. A choice that binds
after the merge is written into the foundation (WAY-36), unless the task or its spec excludes the
entry, as `task-cycle/skill/return_step.md` gives; every other choice is its row here and nothing
else.

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|

Include the frozen task, `spec.md` where one was written, `plan.md` and `plan-size.md` only where
planning ran, code commits, tests and full agent reports, the report of a discarded attempt or
of a slice returned too large among them. Name commits and commit ranges instead of copying diffs
or files that git holds. A foundation entry the cycle writes lives in its commits; the report of
the agent that wrote it keeps its meaning sentences and its mark, and `request.md` takes them from
there.

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|

Record the checks already failing on the base apart from the runs after the change. Where the cycle
ran no gate on the base because step 4 of `task-cycle/skill/SKILL.md` took the list from the final
gate of the earlier cycle, the list stands there in the place of that run, with the commit and the
file of the earlier cycle's record that it was taken from, and the run of the failing tests on the
base follows it where step 4 gives that run, with its result. Where the task moved the pin, record
the gate on the commit that moved it apart as well, naming each check that fails there and is not
among those failing on the base: that is work the task carries. An executed
check is its command and exit code, with its result in one line; a report missing either returns
to its agent for repair, and a claim that tests passed does not replace them. A manual check
records its method, actor, observed result and evidence, with `not applicable` for the command and
exit code. Focused checks are not rerun merely to advance the cycle. The orchestrator runs the gate
on the tree that goes into the request and records its command, exit code and the failures it
names. Name every check that failed or did not run, with the reason; an unrun check is unchecked,
never passed. Each failing run of a check remains in the record with its command and result, even
if the check passes when run again. A check that fails in a cycle run and passes when run again
follows the product's rule on flaky tests (the testing guidelines' *Flaky tests*, WAY-243): rerunning
serves only to diagnose what makes it flaky, never to make a gate run pass. Apply this rule even when
the product has no *Flaky tests* section in its guidelines. When a check has both a failing and a
passing run during the cycle, the request lists it under *Checks* as failed, with the rerun result
and the number of cycle runs in which it failed and passed. When preparing the request, recover the
task's parts from its frozen task and changed files through the part map; if the check's file belongs
to a different part, list it beside findings outside the task's scope (WAY-261). Keep that classification
as evidence with the check, not as a separate record of selected parts. For an invariant's test the
change writes, record its failing run and its passing run as the author reports them.
For a UI change, record the author's or executor's state check and screenshot inspection: affected
components and states, method, observed result and evidence. The evidence of a screenshot is the
address of the place where it lies, never the file, which the record's copy must not hold
(WAY-316); where the foundation settles no place for screenshots, record that the screenshot was
inspected and kept nowhere (WAY-317). Carry a screenshot unchecked for no settled route, or a failed
settled route with its actual result, to the request; code inspection does not establish rendered
appearance.

## Return step

- Foundation compared with code: <the entries the change writes or changes, those the task names
  and those the search of the foundation found, and the part map of the touched parts, each
  compared with the code: what no longer matched and its correction, or none>
- Decisions written or changed: <identifiers or none>
- Invariants written or changed: <identifiers, each with the task, decision or human that sets
  its rule, or none>
- Environment facts: <sources outside the product the change rests on that the foundation did not
  hold, written as facts, or none>
- Glossary terms: <a word the change uses in a meaning for which WAY-95 gives it an entry, or a term
  used in another meaning than its entry gives, written or corrected, or none>
- Part-map changes: <identifiers or none>
- Projected entries written whole or in part: <identifiers or none>
- Rows of *Settlements to record* written: <row number and identifier for each row, or none>

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: <URL and draft/ready/blocked>
- Description: <`request.md` beside this record, written by `task-cycle/skill/request_template.md`,
  with the form check's last command and exit code and the number of its runs; in a copy committed
  before the description was written or rewritten, `written and checked after this commit`>
- Writes to the task's backlog entry: <request link and state, or none>
- Corrections after the request opened: <`none`, or the lines under this line>
  - correction <n>, remarks `reports/<file>.md`: <each pair `<source> · <kind>` of the correction
    once, joined by `, `>
- Process remarks on the-way: <`none`, or the entries under this line>
  - <stage name>, <full report path from the repository's root>: <an item of that report's
    **Searches not found or unclear** other than `none`, copied word for word>
  - <the orchestrator>: <a remark of its own about the-way, such as a listing of
    `task-cycle/remarks_check.py` the cycle holds wrong>

The corrections stand as one line for each correction after the request opened, written by the
orchestrator when the correction's record is prepared (WAY-357); the file in `reports/` holds the
human's remarks of that correction word for word, also where they came in conversation or concern
only the refreshing of the target branch. A pair is the source and the kind of a cause. The source
is read, not judged: `item <n>` is the human's answer to an item of the request's *For you to
decide*, `<n>` being the number of that item's kind in `task-cycle/skill/request_template.md`
(`item 8`, not the number the item had in that description); `remark` is a remark of the human
outside any item; `target-branch` is a correction that exists only to refresh the target branch at
the human's request. The kind is the orchestrator's judgment by one test against the documents,
`defect` where what the correction changes was required by the approved task or by the foundation,
or is a regression, as `project-level/task/template.md` gives it for a task that fixes a defect;
`not-required` where it was not required; `none`, only with `target-branch` (WAY-358). The item
stands before the process remarks, which stay the last item of the record.

The remarks stand in this form only: the item that opens with `Process remarks on the-way`, the
entries indented under it, one for each item of each stage report, repeated items kept apart, and
every line of an entry indented under the entry; not in a section or a file of their own. It is the
last item of the record, and nothing at the level of its marker follows it. The nightly review of
cycles and `task-cycle/remarks_check.py` cut the block as that item and the lines under it. Before
the record is committed, `task-cycle/skill/SKILL.md` ("The record before it is committed") has the
check run on the original and on the cleaned copy until it lists nothing.
