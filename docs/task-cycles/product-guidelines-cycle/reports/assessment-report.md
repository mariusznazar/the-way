# Independent foundation assessment

Assessed base: `f98ac2fed3ab6ecbc1701e0c5f9a694dc9d91624`.
Assessed head: `fc0c946351154a8ee5747160dad55a857522fe86`.
Repository: `C:/Storage/repos/the-way/.runs/worktrees/product-guidelines-cycle`.

## Result and boundaries

No actionable defect was established in the assessed change. This is an independent assessment of the permitted tracked sources, not approval of the change or a settlement of its meaning. The orchestrator settles observations; the human accepts the request.

The complete changed-file set is:

- `foundations/decisions.md`
- `foundations/part_map.md`
- `product-guidelines/coding/SKILL.md`
- `product-guidelines/reading.md`
- `product-guidelines/styleguide/SKILL.md`
- `project-level/plan/skill/SKILL.md`
- `project-level/task/skill/SKILL.md`
- `task-cycle/plan/SKILL.md`
- `task-cycle/record_template.md`
- `task-cycle/skill/SKILL.md`

I inspected the full substantive diff, the whole changed decision entries (WAY-212 through WAY-222), the changed workflow files, the shared guidelines template, the complete part map, the common foundation-reading procedure, relevant existing decisions and invariant entries, and tracked history identifying the origins of the existing timing and review rules. Large combined tool outputs were truncated; the changed material was subsequently read separately. This was not a full line-by-line reading of every unchanged entry of the decision log, nor an exhaustive semantic audit of all unchanged foundation material. Conclusions below concern the examined change and its relevant contracts.

No task, spec, implementation plan, operational handoff, existing author report, session transcript, private note or private lesson was used. Only assessment-generated execution outputs were read under the working reports directory. No code or tracked source was edited, and no child agent was started.

## Observations

### A1. Shared discovery has a defined owner and does not silently waive uncertain coverage — no concern found

Evidence: `product-guidelines/reading.md`, especially “Find the affected work”, “Select and read”, and “Distinguish the gaps”; WAY-213, WAY-214, WAY-217 and WAY-218 in `foundations/decisions.md`; the new calls in step 1 of task refinement and project breakdown.

Checked: how announced behavior is classified before a diff exists, how the complete part map is used, how headers and the complete kind index are inspected, and how malformed metadata, missing indexed files and uncertain conditions are handled. The algorithm explicitly expands reading and exposes questions rather than treating uncertainty as no applicable guidelines. General coding guidance remains applicable when no kind matches. An existing general file whose coverage omits a code part is extended rather than mistakenly treated as absent.

Consequence: later stages receive both the selected paths and unresolved findings. Scoped departures require an actual current product decision; absence alone authorizes no exemption. This agrees with WAY-167, WAY-171, WAY-173, WAY-193 and WAY-208 rather than making an outside template directly bind product code.

Required change: none established.

### A2. Prerequisite timing preserves the two different creation cases and existing plan ownership — no concern found

Evidence: WAY-215 and WAY-216; `project-level/task/skill/SKILL.md` steps 3 and 6; `project-level/plan/skill/SKILL.md` step 2; `product-guidelines/reading.md` gap routing. Existing authority: WAY-172, WAY-184, WAY-199, WAY-200 and WAY-209.

Checked: missing general guidelines versus extension of existing guidance; genuinely first instances versus existing unindexed code; independent/source-only versus plan-member tasks; readiness after the prerequisite merges; and a guidelines-writing task's exemption from waiting for its own output.

Consequence: missing discipline guidelines become a real refinement question instead of an apparently executable task item. A dependency alone does not answer it. First-kind work stays with the first file, avoiding a prerequisite whose exemplar cannot yet exist. Existing files require comparison rather than being bypassed by calling the next file the first. The refiner does not acquire authority to edit the project plan or invent a plan state.

Required change: none established. The broader policy does delay existing-product fixes when guidelines are absent; WAY-215 states that cost explicitly and permits a product-approved scoped departure. That cost is a deliberate policy consequence in the permitted sources, not a defect I can establish from observed frequency.

### A3. Whole-source delivery reaches the people making decisions, while assessment isolation remains explicit — no concern found

Evidence: WAY-213; `task-cycle/skill/SKILL.md` “Start and record” and the added handoff/refresh paragraphs; `task-cycle/plan/SKILL.md` steps 1, 3 and 5; `task-cycle/record_template.md` “Product guidelines”.

Checked: recipients include spec author/reviewer, planner, no-plan author, slice executor and code reviewers, including fix handoffs; each verifies the selection and reads the selected files whole. Refresh is required after scope/source changes and against actual changes on author return and reconciliation. The independent assessor explicitly receives only the existing filtered sources, not the operational selection explanation or a checklist.

Consequence: the new selection does not replace mandatory source reading or the independent assessor's judgment with the orchestrator's summary. Existing instruction pointers continue to serve sessions outside the cycle. Recording uses existing reports rather than introducing a second maintained catalogue.

Required change: none established.

### A4. The order-of-work example and review criteria do not acquire unintended binding force — no concern found

Evidence: WAY-181, WAY-198 and WAY-199; new WAY-220 and WAY-221; `task-cycle/skill/SKILL.md` “The end of a code review”; `task-cycle/plan/SKILL.md` reading and return requirements.

Checked: whether departing from an example can alone reject a plan or block a change; whether appearance findings are preclassified; and whether the orchestrator gains authority to change reviewer grades or discard findings.

Consequence: the planner/author must either use or explain departing from an example, but the order is expressly not mandatory. An example alone does not justify a blocking finding; a reviewer must identify the user/correctness consequence. Binding rules retain their force. Severity and scope remain with the reviewer under WAY-161. This adds criteria, not a second severity scale or an exception to reviewer ownership.

Required change: none established.

### A5. UI evidence distinguishes rendered observations from source inspection — no concern found

Evidence: WAY-219 and WAY-222; `task-cycle/skill/SKILL.md` step 9 and request contents; `task-cycle/record_template.md` Verification; existing styleguide skill audit instructions and WAY-165.

Checked: authors' component/state inspection, use of the foundation-settled route, no-route fallback, treatment of a failed settled route, screenshot evidence, and propagation to the request.

Consequence: the new check is additional to the weakest-point check. It cannot relabel a code inspection as rendered evidence, hide a failed route behind a no-route explanation, or require adopting a new interface tool during execution. Reference-image comparison and product technology selection are explicitly outside the adoption. The permitted sources do not support claiming that every possible rendered fault will be caught, and the wording does not make that claim.

Required change: none established.

### A6. Foundation/implementation correspondence and part ownership — no concern found within inspected material

Evidence: WAY-213 through WAY-222, the implementation locations above, and `foundations/part_map.md` entries `project-level`, `task-cycle` and `product-guidelines`.

Checked: whether the new reading procedure has an owning part, whether the added project-level dependency is allowed by the map, and whether each new decision has an operational counterpart or records an explicit adoption boundary. The changed WAY-212 rationale describes the remaining purpose of instruction pointers once the cycle delivers guidelines. Its approval placeholder agrees with the cycle's treatment of an entry it changes; the existing approval URL is not being presented as approval of the new wording.

Consequence: no new sixth foundation element, duplicate maintained index, or separate approval owner is introduced. No invariant sentence or test is changed in this range. Mechanical guards remain partial evidence, as the repository instructions require.

Required change: none established.

## What can be cut; cost and cheaper alternatives

Nothing in the assessed change is demonstrably safe to cut on the permitted evidence. The central algorithm avoids maintaining unrelated discovery implementations for refinement, breakdown and execution. Caller-specific text supplies timing, ownership, dispatch and return boundaries that the central algorithm cannot supply alone. The cycle-record additions use an existing artifact; they do not establish another maintained format.

Leaving instruction pointers as the only mechanism is cheaper in reading/reporting overhead, but supplies no explicit cycle handoff or refresh contract and does not expose missing guidelines during breakdown/refinement. Sending only excerpts or a checklist reduces context cost but loses the whole-file context that the new policy expressly protects. Leaving the state/screenshot check solely to review reduces author work but moves discovery later. The proposed route costs repeated selection verification, whole applicable-file reads, prerequisite waiting and extra UI evidence. There is no permitted empirical record establishing the size of those costs or the frequency of the failure they address.

WAY-222 overlaps operationally with the three decisions it references, but supplies an explicit boundary on an outside-practice adoption under WAY-100. Cutting it would remove that declared boundary, rather than merely delete another copy of executable instructions.

## Executed checks and retained evidence

Each numbered execution has `assessment-<n>-command.json`, `assessment-<n>-stdout.txt` and `assessment-<n>-stderr.txt` beside this report. The JSON contains the exact argument vector and actual exit code; both output streams are complete. No tracked source body or diff is archived in them.

| n | Exact command | Actual exit | Observed result |
|---|---|---|---|
| 0 | `python -B gate/run_tests.py gate` | 0 | 98 tests, OK; complete runner output is in stderr |
| 1 | `python -B elements/decisions/format_guard.py --help` | 0 | Argument discovery only; not a validation pass |
| 2 | `python -B elements/part-map/format_guard.py --help` | 0 | Argument discovery only; not a validation pass |
| 3 | `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 16 warnings, 5 unchecked |
| 4 | `python -B elements/part-map/format_guard.py --base none` | 0 | 0 errors, 0 warnings, 7 unchecked |

The decision warnings name five overdue check-by dates (WAY-03, WAY-21, WAY-52, WAY-55 and WAY-69) and eleven request-link approval placeholders (WAY-212 through WAY-222). These are reported, not called errors or silently cleared. The guard does not check base/merge comparisons, merge copies, merge-time TODO rejection or relation fingerprint values when their comparison commits are `none`.

The part-map unchecked work includes the two critical flows' part lists without coverage files, promise-level declarations without a reporting command, the absence of a dependency-graph command, and base-relative violation-list, identifier and criticality comparisons. Neither command is evidence that the complete gate exists or has passed.

## Evidence limits and unverified facts

- No behavioral-frequency estimate is supplied. Session/run records and task chronicles were excluded by the dispatch; no such records were searched. The number of true cases, recurrence after earlier rules and dated behavioral examples are unverified.
- The private lesson behind WAY-222 was excluded. Fidelity to that lesson and human acceptance of the intended adoption cannot be independently established here. I checked only the public tracked adoption wording against its implementation and existing authority; no outside claim was filled from memory.
- History identifies the introduction of the existing styleguide timing rule at `5fde846`, coding timing rule at `b03c5da` and final-review ownership rule at `0761d6d`. Those tracked origins establish earlier rules, not whether agents followed them or problems recurred afterwards.
- No live product, rendered screen, actual task refinement or operational guideline handoff was exercised. Their behavior is unverified; this assessment checks the written process contracts.
- I did not run every part's test suite or independently verify every current relation fingerprint. No claim of a full gate pass, complete foundation collision search, or full unchanged-log semantic audit is made.
- Current acceptance of changed meanings, completion of overdue reviews and replacement of request placeholders remain outside what this filtered assessment proves.

Actionable observations requiring a source/code change: none established.
