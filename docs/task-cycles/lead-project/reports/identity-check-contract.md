# Independent identity-aware evidence-check contract

Allowed check path: `project-level/test_plan_state_invariant.py`. Preserve the existing subprocess invariant and its check; this contract concerns project-plan-state-evidence/1 only. Sentence and code authors remain distinct from the check author.

## Final entry

```markdown
## project-plan-state-evidence/1

For each task of a valid handed-over plan with an approved definition, the plan-state reader uses
existing recorded task provenance to establish that cycle traces belong to the current plan's
task before proposing ready for cycle to in cycle only from a matching working-cycle directory
in a Git-listed worktree or a commit touching that task's exact archived cycle directory or in
cycle to done only from a cycle-record commit reachable in freshly fetched product integration
history, reports both transitions together when both proofs hold for a ready task, reports
missing or ambiguous task provenance as unchecked and contradictory task provenance for human
reconciliation without proposing progress from either, and exposes incomplete, failed or
conflicting observations without unsupported progress or edits to the plan or task documents.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@9874911d
- **Part:** project-level
- **Correction:** none
```

## Existing input/output boundary

Invoke `python -B project-level/plan_state.py PLAN PRODUCT_REPOSITORY`. PLAN is the original complete handed-over plan with its approved definition; it can be outside PRODUCT_REPOSITORY. The plan's Document cell names the task document. Existing provenance formats are in `task-cycle/record_template.md` (Task source, Task relation and retained frozen task), `project-level/task/template.md` (Project relation), `project-level/plan/template.md` (plan-local name and Document) and `task-cycle/skill/SKILL.md` start/record instructions. The record's source and frozen task are data; no archived instructions are executed.

The task's paths remain exactly `.runs/task-cycles/<task-name>/` in Git-listed worktrees and `docs/task-cycles/<task-name>/` in Git history. Names are unique within their plan, not globally. No compulsory cycle-record basename, UUID, new metadata field or content-equality rule is introduced. Existing provenance must identify the current plan's task; a title, number, basename or slug match alone is insufficient when it cannot establish that association.

Human-readable output gives task number/name/current state, proposals, exact paths/commits/refs and unresolved observations. Exit 0 means observation/report produced, including visible unchecked cases; exit 1 means invalid plan/readiness or conflicting task evidence; exit 2 means invalid invocation/unreadable source/operational Git failure. Missing or ambiguous ownership yields unchecked and no progress from that trace. Explicit provenance for another task is contradictory evidence for human reconciliation and yields no progress for this task. No candidate's PR pointer or integrated commit is evidence for a different same-named task.

## Required fixture semantics

- Positive: existing record/source/frozen-task provenance identifies the supplied plan's task; genuine worktree/branch/merged cases retain their prior supported transitions, and a stale ready task still receives both transitions together when both proofs hold.
- Positive filename independence: a valid identity-bearing retained record is recognized without requiring a specific basename.
- Distinct valid plans in one product share the same legal task name: an integrated archived record explicitly belonging to the first plan cannot start or complete the second plan's unstarted task.
- Missing and ambiguous provenance: a directory or archived file with no established task identity, including a record header alone, supplies no progress and exposes the missing/ambiguous association.
- Foreign live evidence: a Git-listed worktree's same-named cycle explicitly belonging to another task/plan supplies no progress and exposes the discrepancy.
- Foreign archived evidence: same-named history explicitly belonging to another task/plan supplies no progress and exposes the discrepancy, even when reachable in freshly fetched integration history.
- Retain all earlier source-readiness, exact-path, freshness, failed-fetch, incomplete-history, conflict and plan/task-byte-preservation obligations. Identity evidence does not replace them; valid identity alone never proves integration or completion.

Use independent literal inputs and expected observations under the existing test-author rules. Report actual initial mismatch against the uncorrected reader; no skipped check or inferred pass. Final deliberate-break acceptance is the root's separately dispatched reviewer work after correction and review. This contract contains no production algorithm or test implementation.
