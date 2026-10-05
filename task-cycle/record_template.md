# Cycle record — <task title>

- Task source: <absolute path and approval date or source commit>
- Task relation: <independent | plan item | source only>
- Product repository: <path>
- Process pin: <commit>
- Target branch and base: <branch and commit>
- Task branch: <branch>
- Foundation route: <unchanged | entry or invariant-test change; affected entries and prior approval>
- Status: running | blocked | request open | complete

## Sharpness at start and after the final diff

| When | Criticality and touched parts | Trust-boundary files | Reversibility | Consequent checks |
|---|---|---|---|---|

Unknown failure modes count as the highest criticality. Record the reason for each assessment,
then recalculate from the final diff. An irreversible operation waits for the human's decision at
the request; preparing reversible code for it does not authorize executing it.

## Events

| Time | Stage | Actor and model | Skill and input | Output or report | Result and next step |
|---|---|---|---|---|---|

Append one row for every dispatch, handoff, failed attempt, rerun, review and fix. During work this
file and full sanitized prompts and reports live under the ignored `.runs/task-cycles/` directory.
After assessment, copy them to `docs/task-cycles/`, link the reports from these rows, commit the
copy and commit its removal immediately after; the request links the record by the SHA of the
commit that adds it. A correction after review repeats this pair.

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Reaches beyond the request | Used by | Review status |
|---|---|---|---|---|---|---|---|---|

Include questions that were answered by a binding source as well as new micro decisions. Mark
choices requiring a human foundation decision as proposed, never approved. A choice whose cost of
being wrong reaches beyond the request becomes a proposed foundation entry.

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|

Include the frozen task, `spec.md`, `plan.md`, code commits, tests and full agent reports. Name
commits and commit ranges instead of copying diffs or files that git holds. A foundation proposal
has one current version and one wording in the task document's language for the human; the
manifest records the assessed range by commit hashes, plus a diff only of changes made after the
panel.

## Verification

| Command or manual check | Commit and environment | Result | Failed or unchecked details |
|---|---|---|---|

Record the baseline separately from post-change runs. A check's result is one line. An unrun
check is unchecked.

## Return step

- New decisions or changed decisions proposed: <links or none after search>
- New invariants or changes proposed: <links or none after search>
- Behavior with no invariant: <finding or none after search>
- Environment facts and glossary terms: <links or none after search>
- Part-map changes: <links or none after search>
- Panel and foundation comparison: <reports or not applicable>

## Panel

- Assessed commit or range and its files: <commit or range and paths>
- Independent assessments: <links to full reports>
- Settlement, first order: <link to full report and concise call>
- Settlement, swapped order: <link to full report and concise call>
- Fixes and re-assessment: <links or none>

## Request handoff

- Request URL and status: <URL and draft/ready/blocked>
- Proposed foundation entries from choices: <IDs from the questions table, or none>
- Choices within the request: <count and link to the questions table>
- Writes to the task's backlog entry: <request link and state, or none>
- Remaining limitations: <list or none>
- Process improvements to consider next time: <observed friction and evidence, or none>
