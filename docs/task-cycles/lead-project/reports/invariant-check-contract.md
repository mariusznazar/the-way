# Independent invariant-check contract

Author boundary: the receiving agent wrote neither the sentence below nor the reader it checks. Write only project-level/test_plan_state_invariant.py. Do not change foundation wording, reader code or existing invariant tests. No implementation rationale or pseudocode is included in this contract. No prior check cites this new identifier, and no identifier/version is retired.

## Entry, in full

```markdown
## project-plan-state-evidence/1

For each task of a valid handed-over plan with an approved definition, the plan-state reader
proposes ready for cycle to in cycle only from a matching working-cycle directory in a Git-listed
worktree or a commit touching that task's exact archived cycle directory, proposes in cycle to
done only from a cycle-record commit reachable in freshly fetched product integration history,
reports both transitions together when both proofs hold for a ready task, and exposes incomplete,
failed or conflicting observations without unsupported progress or edits to the plan or task
documents.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@33b10f25
- **Part:** project-level
- **Correction:** none
```

## Public observation boundary

Run `python -B <the-way-checkout>/project-level/plan_state.py PLAN PRODUCT_REPOSITORY`, where PLAN is an original complete handed-over plan (including a path outside the product repository) and PRODUCT_REPOSITORY is the explicitly supplied Git repository. Temporary controlled repositories and literal complete approved definition/plan inputs are suitable. The script is a reader: Git metadata can change through fetch, but plan and task-document bytes do not change.

Human-readable output is the interface; no JSON schema is promised. It names each task's number, stable name, current state, proposed transitions, exact task-cycle path/commit/ref evidence and each unresolved observation. Completion evidence identifies the freshly fetched product integration ref and commit. The archive path is exactly docs/task-cycles/<task-name>/; the working path is exactly .runs/task-cycles/<task-name>/ in a worktree Git lists. A neighbouring slug, a branch name or message text alone is no evidence. A stale ready task with both proofs reports ready for cycle → in cycle and in cycle → done in one report.

Exit 0 means a report was produced, including visible unchecked cases; exit 1 means invalid plan/readiness findings or inconsistent evidence; exit 2 means invocation/unreadable-input/operational Git failure. Invalid or draft plan, unreadable or unapproved definition gives no state proposals. Failed fetch never yields done, even if local cycle evidence was observed. Missing/ambiguous integration ref, unavailable worktree, insufficient/shallow history or outcomes Git cannot establish expose the reason rather than unsupported progress. A closed-unmerged PR is handled by the skill/human, not by this CLI; no PR host executable belongs in the reader.

The invariant's command runs the complete project-level test directory and records per-entry verdicts at .runs/project-plan-state-evidence.jsonl; it does not accept a filename instead of that directory. Cite `# invariant: project-plan-state-evidence/1` at each smallest check that records its own verdict. Inputs and expected observations are independent literals wherever production code would otherwise compute them; do not read expected answers from production or from the invariant wording at run time. Positive evidence and conservative/error cases both matter: worktree trace, branch-only record, freshly fetched reachable record, both transitions, deleted merged branch, nondefault integration name, missing/ambiguous remote information, fetch failure, shallow history, missing worktree, conflicting states, exact slug separation and path handling. Check preserved plan/document bytes as part of the reader's proposal contract. Cases beyond the invariant's one evidence rule belong to the implementation's ordinary tests and are not given this invariant's verdict merely because they are useful.

Run the method and record the actual initial failure while plan_state.py is absent; do not skip it or manufacture a reader stub. The future code reviewer, who did not write this check, supplies its deliberate break from the sentence and records the required failure before final acceptance. The command/exit/interface statements above are observables, not instructions on how to implement the reader.

## Observable row convention

Each task has a header `task <n> <slug>: <current state>` and zero or more proposal lines `propose <n> <slug>: <from state> -> <to state>`. A proposal is only a line beginning with that exact propose prefix, without indentation or bullets. State values are the plan's literal English values; the separator is ASCII ` -> `.

Evidence rows use `evidence <n> <slug>: <details>`, unresolved task observations `unchecked <n> <slug>: <reason>`, and inconsistent task observations `conflict <n> <slug>: <reason>`. Global observations can use `unchecked: <reason>` and failures `error: <reason>`. Global header lines are `repository: <absolute path>` and, when established, `integration: <ref> <commit>`. Details/reasons are human-readable and not otherwise frozen; facts such as exact paths, refs and commit IDs must be present as the existing contract requires. An unavailable integration has no fabricated ref/commit.

The integration header renders the fully-qualified remote-tracking ref (`refs/remotes/<remote>/<branch>`); path evidence may use either native or forward separators where both identify the same path on the platform.

## Integration-source clarification

A working branch's upstream is not a declaration of the product integration branch. The installed product guidance already declares `origin/HEAD`: installation/install.py product_guidance(), lines158-166, says `git symbolic-ref --short refs/remotes/origin/HEAD` names it as `origin/<branch>` and otherwise asks the human. Use that existing origin route, confirmed through Git; another configured remote with a different default does not by itself make a valid origin route ambiguous. No main/master fallback or inference from the checked-out/upstream branch.

For the ambiguous case, origin metadata that cannot establish one valid default route remains unchecked. Do not commit a negative expectation that rejects origin merely because another remote exists; instead exercise the presence of another remote as a positive no-false-ambiguity case, preserving origin's completion evidence. A missing/invalid origin default remains the existing negative case. No configuration or new CLI override is added in this task. This is source-grounded observability clarification, not a code algorithm handed to the check author.
