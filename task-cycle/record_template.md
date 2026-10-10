# Cycle record — <task title>

- Task source: <absolute path and approval date or source commit>
- Task relation: <independent | plan item | source only>
- Product repository: <path>
- Process pin: <commit>
- Target branch and base: <branch and commit>
- Task branch: <branch>
- Foundation route: <unchanged | entry or invariant-test change; affected entries>
- Cycle: <light | full | full after a switch from light>
- Status: running | blocked | request open | complete

## Sharpness at start and after the final diff

| When | Criticality and touched parts | Trust-boundary files | Reversibility | Consequent checks |
|---|---|---|---|---|

Unknown failure modes count as the highest criticality. Record the reason for each assessment,
then recalculate from the final diff. An irreversible operation waits for the human's decision at
the request; preparing reversible code for it does not authorize executing it.

## Cycle

- Choice at start: <light | full> — foundation: <unchanged | changed>; one agent's time to
  implement: <estimate and reason | not assessed>; files read into context: <which, and their
  size | not assessed>
- Foundation touched on the light cycle: <entry, the ruling on whether the touch is simple and
  obvious, and its reason | none>
- Switch to the full cycle: <time, why the change outgrew the light cycle, the executor's report,
  the discarded attempt's last commit and the files it changed | none>

Record the reason for each finding assessed; once one finding fails, the rest may read `not
assessed`. The last commit of a discarded attempt is a historical name, not a link to follow: the
commit is reachable only until the reflog expires. A choice or ruling of a discarded attempt keeps
its row in the questions table, with *Used by* naming the discarded attempt.

## Events

| Time | Stage | Actor and model | Skill and input | Output or report | Result and next step |
|---|---|---|---|---|---|

Append one row for every dispatch, handoff, failed attempt, rerun, review and fix. During work this
file and full sanitized prompts and reports live under the ignored `.runs/task-cycles/` directory.
After assessment, copy them to `docs/task-cycles/`, link the reports from these rows, commit the
copy and commit its removal immediately after; the request links the record by the SHA of the
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

Include the frozen task, `spec.md` and `plan.md` on the full cycle, code commits, tests and full
agent reports, the report of a discarded light-cycle attempt among them. Name
commits and commit ranges instead of copying diffs or files that git holds. A foundation entry
the cycle writes lives in its commits; the record keeps its meaning sentence for the request.

## Verification

| Command or manual check | Commit and environment | Result | Failed or unchecked details |
|---|---|---|---|

Record the baseline separately from post-change runs. A check's result is one line. An unrun
check is unchecked.

## Return step

- Decisions written or changed: <links or none after search>
- Invariants written or changed: <links or none after search>
- Behavior with no invariant: <finding or none after search>
- Environment facts and glossary terms: <links or none after search>
- Part-map changes: <links or none after search>
- Foundation compared with code in touched parts: <finding or none>
- Projected entries written whole or in part: <links or none after search>
- Rows of *Settlements to record* written: <row number and link for each row, or none>

## Independent assessment

- Assessed range and its files: <commit hashes and paths>
- Assessment: <link to the full report and its call>
- Settlement: <each remark, how it was settled, and the commit that applied it, or none>

## Request handoff

- Request URL and status: <URL and draft/ready/blocked>
- Cycle and its reasons: <as the request states them>
- What this request settles: <identifier and meaning sentence for each entry>
- What the foundation puts in front of the human at the merge: <an invariant kept at its version
  under a correction, with its old and new sentence; a part whose computed criticality fell; a
  recovered row, with the gate's report; a moved use of a changed definition; a term WAY-97 asks the
  request to name; or none>
- Questions: <only those the foundation step allows, or none>
- Choices within the request: <count and link to the questions table>
- Writes to the task's backlog entry: <request link and state, or none>
- Process remarks on the-way: <observed friction and evidence, or none>
