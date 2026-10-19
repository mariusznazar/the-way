# Product guidelines in refinement, planning and the task cycle

Status: design complete; D1-D3 provisionally approved by the cycle orchestrator under the user's delegation; awaiting independent spec review. This is not human approval of new product meanings.

Task: `task.md` beside this file. Source foundation: `f98ac2fed3ab6ecbc1701e0c5f9a694dc9d91624`. Design evidence and rulings: `reports/design-report.md`.

## Outcome and boundaries

Agents refining, breaking down, designing, making and reviewing a change read the product guidelines that apply to it. One shared procedure finds those files and recognizes missing discipline guidelines before refinement becomes ready. It also recognizes a first kind of code whose exemplar and kind guidelines belong in the task that creates its first file. UI authors record their state check and screenshot inspection before review; reviewers judge visual consequences without turning examples into binding rules.

This change implements the frozen task's nine To do items and ten accepted settlements. It neither writes loop2's guidelines, introduces screenshot comparison, nor selects a product's interface technology outside the existing project-definition route. It adds no selection schema, flags in the part map, generated review checklist or new task/plan status.

## Shared reading procedure

Add a prose procedure at `product-guidelines/reading.md`. Refinement, project breakdown, the cycle and task planning call this procedure rather than maintaining separate discipline-specific discovery algorithms. Its inputs are the proposed change or approved project scope, the current product foundation and repository, and any previous selection with its reasons. Its result is the affected parts with evidence, the selected guideline paths with reasons, and named uncertainties or missing-guideline findings, recorded in each workflow's existing document/report mechanism.

1. Read the complete part map. Associate the required behavior and responsibilities with its parts, files, critical flows and surfaces; inspect existing files as evidence of what the product has. Determine whether the change affects a user interface, writes code, and introduces or changes a kind of code. A backend's admin UI is a UI; helper scripts are code. Names and file extensions alone do not settle either classification. Future code and UI are classified from the required outcome, even where no diff or files exist. A prospective part stays explicitly unresolved until its identity is settled through the workflow's existing questions. Map additions follow existing rules and known facts, never invented file assignments.
2. Inspect every product guideline file's header and the complete kind index in `guidelines/coding.md`, when present. Select every guideline whose `Applies to` includes an affected part. For a `coding-<kind>.md` file, also require the condition in its coding index row's `When to read` to match the proposed change. Inspect the selected files' reading conditions and read selected files whole. General coding guidelines remain relevant when the kind index has no matching row; a missing row does not imply no coding guidelines apply.
3. Check current product decisions for a departure from a discipline's guidelines for an affected part. Apply only the scope that decision expressly covers. Missing, malformed or contradictory metadata, including an indexed file that is absent, is a named finding to resolve, never an empty match. Ambiguous classification first expands reading; an unresolved identity or condition becomes an explicit question in the owning workflow. The procedure does not invent an exemption or silently call an existing file absent.
4. Recognize missing files and missing kind coverage separately. Absence of the styleguide for an affected interface and absence of `guidelines/coding.md` for code work are missing-discipline findings unless a scoped departure applies or the task itself writes the missing guidelines. An existing `coding.md` that omits an affected code part is an extension of that file in the current task; read it as the source to extend. A missing kind row for a genuinely first file is first-kind work in that task. Existing unindexed files invoke the distinction already made by WAY-200: an exemplar comes from comparison by the coding-guidelines skill. Record that discrepancy and route the needed work through the owning workflow; this does not authorize an unrelated audit or pretend the next file is the first.
5. Refresh the selection when scope or sources change and against actual affected parts on return and reconciliation, before dependent work is dispatched. Reuse a selection only while its source and scope still support it. Record additions, changed reasons and unresolved findings in the existing record. Do not store a second catalogue of guideline contents.

Selection discovers the discipline files by their shared form. The response to a missing file follows the discipline's existing creation timing, with the concrete styleguide, general-code and first-kind cases below. A future discipline therefore adds no second discovery mechanism.

## Refinement and project breakdown

`project-level/task/skill/SKILL.md` invokes the shared reading during grounding, before deciding readiness, and again when later clarification changes scope. A task that needs missing discipline guidelines retains a named `Questions to settle` question awaiting the separate guidelines task's merge and a task-document status of `waiting for human`. This applies even to a product that already has screens or code. Continue all refinement independent of that answer. The guidelines-writing task is exempt from waiting for the file it creates.

For an independent task or one using a project only as source, the refiner proposes the separate prerequisite and adds it to the product backlog after human approval, following the existing document/backlog conventions. For a member of a plan, the refiner respects its write boundary: return `plan change` if the plan lacks the prerequisite, or `waits for task <n>` if it exists. The project orchestrator owns the plan and its rows. A task document's `waiting for human` is distinct from the plan row: existing question-specific wait rules may leave that row `to refine`; do not add or reinterpret plan states.

After the prerequisite is merged, resume refinement, read the new guidelines, settle the meanings this task needs through WAY-172 and obtain the existing complete-document acceptance before `ready for cycle`. Merely adding a dependency does not make the task ready. An extension or correction of existing guidelines remains in this task, including a substantial extension; changed meanings and exemplar changes keep their existing approval routes under WAY-172/199. A human can choose to separate the extension.

A task creating the first file of an unindexed kind receives explicit To do work to designate that file as exemplar and write the kind's guidelines/index entry through the existing coding-guidelines process. It does not wait for a separate task that would need the file this task creates. The general coding file must already exist unless this task itself writes it or a valid departure applies.

`project-level/plan/skill/SKILL.md` performs the same reading while breaking down the approved definition. It places each missing-discipline guidelines task before its consumers, with actual dependency links and the preparatory-task rules of WAY-143. It assigns first-kind work to the task creating that kind's first file. It reuses an adequate existing task rather than creating duplicates. It keeps the existing definition/plan write boundary and question routing; it does not silently enlarge an approved definition. Refinement remains a second check, including for tasks outside a plan.

## Cycle, planning and handoffs

The cycle orchestrator owns the initial selection and records the affected parts, selected paths and reasons in the cycle record. Its file handoff carries these to the spec author and reviewer, planner, no-plan author, slice executor and reviewers. Each recipient reads selected files whole, checks that selection against the scope it is actually judging or making, and expands or reports a discrepancy before relying on it. The recipient's report returns changed selection/reasons so the orchestrator refreshes dependent handoffs. Whole-source reading is not replaced by quoted excerpts or a list of checks.

`task-cycle/plan/SKILL.md` calls the same procedure and verifies the selection against the whole task it divides. Both planner and no-plan author receive the styleguide's order-of-work example with the styleguide, explicitly as an example: they may follow it or explain why another order fits. It is not a mandatory slice order and cannot itself justify rejecting a plan.

The cycle refreshes after spec/planning changes and author returns and at reconciliation, using actual changed files and affected parts. A late finding uses the cycle's existing pause/re-refinement or foundation-meaning path as appropriate; it does not silently waive the earlier requirement or add a new status. Product instruction-file pointers to guidelines remain: they serve sessions outside the cycle too.

The independent foundation assessor retains its filtered input contract. No operational cycle record, selection explanation or checklist is added to its handoff; relevant repository guidelines are available through its existing permitted source reading. This preserves assessment independence while keeping applicable source material available.

## UI author evidence and code review

Before review, the no-plan author and each executor changing a UI check the affected components' states required by the applicable product styleguide, including any applicable adopted exception or departure. This is additional to the existing weakest-point check under WAY-164. The requirement comes from the product's guideline, not an unadopted template forced directly onto the product.

Use the agent's route to the running product settled in its foundation to inspect a screenshot. Record the affected UI/states, method, observed result and screenshot evidence path in the stage report. Preserve the existing complete evidence requirements for commands and checks. When the foundation settles no route, inspect states in code and mark the screenshot unchecked for that specific reason in both the stage report and the request. Code inspection does not establish rendered focus or other appearance. If a settled route fails, record the actual failed or unperformed check and evidence through the existing result contract; do not label it the no-route case. This task requires no baseline image or image-comparison test and introduces no new route-selection blocker.

Reviewer instructions carry two generic criteria, never a preclassified finding:

- Judge the severity of an appearance finding by the concrete effect the user sees, within the existing Critical/Important/Minor scale. A visual issue is not automatically Minor and is not automatically blocking.
- Departure from a guideline example or the script-unchecked part of an exemplar alone cannot justify a blocking finding. Name the user-visible or code-correctness consequence that warrants it. A bound rule and its checks retain their existing force.

The reviewer alone sets each finding's grade and scope under WAY-161/162. The orchestrator cannot downgrade or discard a finding by invoking these criteria. Existing external-style sources and examples do not become binding product rules through the handoff.

## Foundation and implementation scope

The foundation step records all ten accepted settlement rows from `task.md`, preserving their substance and sources. The entries must cover: shared cycle selection and all recipients (1); one refinement lookup (2); missing-discipline wait, backlog ownership, existing products, resumption and extensions (3); first-kind work (4); scoped departures (5); breakdown ordering (6); UI evidence/fallback (7); consequence-based visual severity (8); example-only differences (9); and the explicit adoption of private course practices for the cycle (10). The last entry names what is taken and where, and leaves screenshot comparison, loop2 implementation and out-of-definition technology selection outside this change. Describe the private source without quotations or copied lesson material, as WAY-27/100 require. WAY-175's styleguide-only adoption does not substitute for this cycle adoption.

D1's selection ownership/refresh and D2's evidence-based classification refine these settlements through the provisionally approved design. Preserve human-reserved product-meaning decisions and the existing independent foundation assessment. Use exact current identifiers and fingerprints in the foundation step; this spec allocates no new decision numbers and writes no entries early.

Expected implementation files:

- New `product-guidelines/reading.md` owns the shared procedure.
- `project-level/task/skill/SKILL.md` and `project-level/plan/skill/SKILL.md` integrate lookup and workflow-specific responses.
- `task-cycle/skill/SKILL.md` and `task-cycle/plan/SKILL.md` integrate dispatch, recipient reading, refresh, UI evidence and reviewer criteria; adapt `task-cycle/record_template.md` only where needed to make the required evidence discoverable in existing sections, not a second registry.
- `product-guidelines/styleguide/SKILL.md` and `product-guidelines/coding/SKILL.md` lose the obsolete claim that refinement/the cycle do not change for them and point to the shared reader where relevant. They keep ownership of creating/adopting guidelines.
- `foundations/decisions.md` receives the accepted rules; `foundations/part_map.md` gains the `project-level` dependency on `product-guidelines` and updates the latter's responsibility for shared reading. Reconcile any directly affected rationale, including WAY-212's obsolete temporal explanation, under the existing editorial rules; its instruction-pointer rule remains.

The guideline templates/form checker, root instruction files, installation path, task/plan data schemas and runtime scripts need no behavioral change from this design. If implementation changes a skill description, name or location, regenerate and commit its project entry points through the existing command. File-scope changes that prove necessary return with their reason, not as assumed permission for unrelated cleanup.

## Verification and remaining risk

The principal new behavior is agent judgment and routing. Verify it by independent source review and a manual scenario walk through the actual final instructions, with source locations and observed outcomes recorded. Do not pretend exact-phrase tests establish semantic classification or reviewer judgment.

Required cases: existing guidelines for multiple affected parts; a matching and nonmatching code-kind condition; a coding file omitting a new code part; missing discipline files in both a new and existing product; a scoped departure; a guidelines-writing task; a first unindexed kind; existing unindexed files; uncertain/malformed metadata; a planned prerequisite present and absent; resumption after its merge; scope expansion after the first handoff; screenshot success, absent route and failed settled route; an appearance finding with a concrete consequence and an example-only difference. For each, verify the recipient, action and recorded reason, including plan/task status distinction and independent grade ownership.

Run the repository checks appropriate to the final changed files: decision/part-map integrity and fingerprints, task-cycle/project-level/product-guidelines checks, and the required gate. Use baseline evidence rather than duplicate a completed baseline without a change. Generated skill entry points are checked if applicable. Any added or changed invariant method follows its existing deliberate-break obligations; this design does not require a new mechanical test for prose-only judgment. Evidence of unperformed checks remains explicit in reports and the request.

Residual risks: prospective part/kind classification is semantic and can be wrong; recipient verification and scope refresh reduce but do not eliminate it. A missing interface route leaves rendered behavior unchecked, explicitly visible to the human. Whole guidelines add context cost; selecting by affected parts and kind conditions bounds it without losing sources. Independent review must check that every dispatch route actually invokes the contract, including the no-plan route.

No unresolved design question remains after D1-D3 rulings. Independent spec review and the orchestrator's next-stage decision remain pending. No implementation or test result is claimed by this spec.
