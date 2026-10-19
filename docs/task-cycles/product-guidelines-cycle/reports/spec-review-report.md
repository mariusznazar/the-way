# Independent spec review

Verdict: **pass**. No required corrections, blocking findings or Minor findings. No unresolved question for the orchestrator. The spec answers the frozen task without changing its accepted meanings; implementation and its verification remain future work.

Reviewer: independent agent `/root/spec_review`. Scope: task-cycle step 7, review of `.runs/task-cycles/product-guidelines-cycle/spec.md` against the complete frozen `task.md`, current foundation and affected procedures. Worktree: `C:/Storage/repos/the-way/.runs/worktrees/product-guidelines-cycle`; foundation revision: `f98ac2fed3ab6ecbc1701e0c5f9a694dc9d91624`. All locations below are relative to that worktree; `spec.md` and `task.md` mean the files in this cycle. No implementation, spec edit, commit or next-stage work was performed.

## Foundation selection and reading

I independently selected the starting parts `product-guidelines`, `task-cycle` and `project-level`, then added `instruction-files` because guideline pointers must survive and `agent-instructions` because changed skill descriptions require regenerated entry points. I read the complete part map before selecting entries. I read each selected decision and invariant whole, including rationale, examples, sources and outgoing relations; the designer's report was evidence of provisional rulings, not a replacement for the foundation.

The scope inventory scanned all 198 decision entries and all 222 invariant entries. It selected 143 decisions and 68 invariants; I read all 143 and 68. The complete selected IDs and locations are retained in [decision inventory](spec-review-decisions.md.stdout.txt) and [invariant inventory](spec-review-invariants.md.stdout.txt). Thus there is no selected-but-unread entry. These counts concern this revision's entries, not keyword occurrences.

Link and subject expansion added 31 whole decisions: WAY-02, 04, 05, 07, 08, 12, 14, 17, 18, 19, 20, 22, 29, 31, 35, 40, 41, 49, 52, 53, 54, 56, 60, 64, 71, 72, 85, 86, 95, 97 and 104. The critical flow also added `decision-guard-stale-reference/1` at `foundations/invariants.md:6`. Total whole-entry reading: 174 decisions and 69 invariants. I also read the complete glossary, environment-facts file and violated-invariants register. The full part map supplied dependencies, critical flows and surfaces. Semantic searches for guidelines, styleguide, exemplar and screenshot were used to cross-check the selection; they did not replace whole-entry reading. No relevant unresolved foundation conflict was found.

Affected interface sources read: the complete task refinement and project-plan skills and their templates; task-cycle skill and record template; task planning skill; shared guidelines template; both discipline skills and templates. These establish the existing status vocabulary, ownership and write boundaries, creation/adoption routes, author/reviewer split, independent assessment inputs and report contract.

## Frozen task coverage

Each row below is a manual source comparison by `/root/spec_review`: read the complete requirement, trace its meaning into the spec and test it against the applicable workflow contract. Command/exit/output fields are not applicable to these manual checks. All outcomes are pass with no concern.

| Frozen requirement | Spec evidence and observed result |
|---|---|
| To do 1, `task.md:26` | `spec.md:18`, `spec.md:39`, `spec.md:41`: every applicable guideline file, kind condition and all named operational recipients are covered. Recipients read whole sources; no review checklist substitutes for them. The order example reaches both planner and no-plan author and remains an example. |
| To do 2, `task.md:27` | `spec.md:15`–`spec.md:23`: one shared discovery procedure serves all callers. A missing discipline file, omitted part, missing kind row, scoped departure and the task writing its own guidelines remain different cases. |
| To do 3, `task.md:28` | `spec.md:27`, `spec.md:31`: the absent file blocks readiness in both new and existing products; the question waits for the prerequisite merge. Resumption reads the new guidelines and settles meanings before complete-document acceptance. |
| To do 4, `task.md:29` | `spec.md:29`: independent/source-only tasks propose backlog work for human approval; plan members return the specified `plan change` or `waits for task <n>`. No refiner writes another owner's plan. |
| To do 5, `task.md:30` | `spec.md:20`, `spec.md:33`: genuinely first-kind work includes exemplar designation, kind file and index in the first-file task. It does not create a circular prerequisite. General guidelines and their exceptions remain explicit. |
| To do 6, `task.md:31` | `spec.md:35`: breakdown uses the same lookup, places prerequisite tasks before consumers with dependencies, reuses adequate tasks and assigns first-kind work to its first-file task. Approved-definition boundaries remain intact. |
| To do 7, `task.md:32` | `spec.md:49`, `spec.md:51`: no-plan author and slice executor check product-required states in addition to WAY-164 and inspect a screenshot by the settled route. With no settled route, code inspection and an unchecked screenshot are recorded in report and request. A failing settled route retains its actual failure. |
| To do 8, `task.md:33` | `spec.md:53`–`spec.md:58`: appearance severity follows the concrete consequence for the user. The spec makes neither every visual issue Minor nor every visual issue blocking. |
| To do 9, `task.md:34` | `spec.md:56`–`spec.md:58`: an example-only departure does not establish a blocking finding; a named user or code-correctness consequence does. Binding rules retain their force and the reviewer owns the grade and scope. |

## Accepted settlements and questions

The explicit foundation instruction at `spec.md:62` covers all ten rows in `task.md:137`–`task.md:146`. I compared each row's full meaning, not only its number. Rows 1–9 are also embodied in the corresponding behavior above: selection/all recipients (1), unified lookup (2), absence/wait/resumption/extension (3), first kind (4), scoped departure (5), breakdown ordering (6), UI evidence (7), visual severity (8), and example-only differences (9). No row is dropped or weakened.

Row 10 is separately handled at `spec.md:62`: explicit cycle adoption identifies what is taken and excluded, preserves source attribution and prohibits copying private lesson material. Existing WAY-175's styleguide adoption is explicitly insufficient. No private lesson quotation is needed in tracked output. No concern.

All three carried questions at `task.md:84` are answered:

- Selection ownership and refresh: `spec.md:21`, `spec.md:39`–`spec.md:45` put the initial selection with the orchestrator, require recipient verification/expansion and refresh later handoffs when scope or sources change. The filtered foundation-assessment handoff stays separate.
- Classification before a diff exists: `spec.md:17`–`spec.md:20` use required behavior, responsibilities and map/file evidence; prospective parts and uncertainty remain explicit. No invented flags, inferred exemptions or fabricated file assignments are introduced. Existing discipline skills retain ownership of establishing parts and guidelines.
- Review criteria without pregrading findings: `spec.md:53`–`spec.md:58` express generic criteria while retaining the reviewer's exclusive grade/scope authority under WAY-161/162. The orchestrator cannot use these criteria to discard a finding.

D1–D3 are identified as provisionally approved design choices, not human approval of new product meanings (`spec.md:3`, `spec.md:64`). Their meanings fit the task and existing approval boundaries. No unanswered design choice remains.

## Distinctions, boundaries and interfaces

Manual adversarial reading checked the cases most likely to collapse into the wrong route. Evidence and observed outcomes:

- **Missing versus extending:** `spec.md:20`, `spec.md:31` block an absent required discipline file, but keep omitted-part coverage, extension and correction in the current task, even for substantial extension. The guideline-writing task is exempt from waiting for its own output. No concern.
- **First versus existing unindexed kind:** `spec.md:20`, `spec.md:33` preserve WAY-200's different exemplar processes. Existing files require comparison through the coding-guidelines process, not an invented claim that the next file is the first or permission for an unrelated audit. No concern.
- **Departure scope:** `spec.md:19` applies only the product decision's express scope; it cannot waive guidelines for another affected part. No concern.
- **Task versus plan state:** `spec.md:29` keeps `waiting for human` in the task document distinct from the owning plan's state and its question-specific waiting rule, consistent with `project-level/task/skill/SKILL.md:16` and the existing templates. No new state or readiness bypass is introduced. No concern.
- **Actual UI evidence:** `spec.md:49`–`spec.md:51` derive required states from adopted product guidelines. Unavailable route and failed settled route remain separate, and code reading is not reported as a rendered appearance check. No screenshot comparison or route-selection blocker is invented. No concern.
- **No-plan route:** `spec.md:39`, `spec.md:41`, `spec.md:49` explicitly cover its author. Nothing requires a plan merely because a spec exists; this fits the cycle's renewed execution choice. No concern.
- **Foundation before implementation:** `spec.md:60`–`spec.md:74` sends all settlements to the existing foundation step, retains independent assessment, avoids allocating decision IDs early, and preserves source/fingerprint obligations. It identifies directly obsolete prose to reconcile while keeping instruction pointers. No concern.
- **Scope exclusions:** `spec.md:11`, `spec.md:51`, `spec.md:62`, `spec.md:74` preserve the frozen exclusions at `task.md:148`: screenshot comparison, loop2 guideline implementation and interface technology choice outside the project-definition route. The shared procedure is prose; no unnecessary schema, runtime change or root-instruction rewrite is required. No concern.

The final implementation must demonstrate that every actual dispatch route calls the shared contract. This is a verification obligation already explicit at `spec.md:84`, not a defect in the spec or a reason to claim that behavior has already been tested.

## Checks and evidence

The inventory commands were executed against this worktree and both exited 0. Exact commands, exit codes and complete stdout/stderr paths are retained in [check ledger](spec-review-checks.json); the underlying temporary reading helper is [spec_review_read.py](spec_review_read.py). Complete outputs are the two inventories linked above and their corresponding `spec-review-decisions.md.stderr.txt` and `spec-review-invariants.md.stderr.txt` files (both empty). The inventory confirms the complete scope population and selected counts; it does not prove semantic correctness. The manual comparisons in this report supply that assessment.

No product tests, guard or required implementation gate were run by this reviewer. They are **unchecked at this spec-review stage**, not failed or passed. The spec claims no implementation result and requires final-file checks plus the repository gate at `spec.md:82`–`spec.md:84`. A manual walk through final instructions and its scenario evidence also remain implementation-stage work. No baseline rerun or duplicate test was needed to review this design.

Required changes: **none**. Remaining questions: **none**. Review ends here.
