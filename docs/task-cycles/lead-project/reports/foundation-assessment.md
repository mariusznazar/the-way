# Independent foundation assessment

Assessed commit: `84cdc87cc12ce43526cb24a61640e39cf00e950a`.
Base: `db77ba549cb9ece7d3e62bf29e1256973f62deab`.
Assessment follows `elements/common/critique/SKILL.md` (WAY-10). This report supplies observations, not the author's verdict.

## Inputs and limits

I inspected the exact file manifest and filtered diff supplied in `assessment-input-files.json` and `assessment-input.diff`, then concentrated on the changed foundation entries, their executable lead/refinement contracts, the state reader and both new invariant-test modules at HEAD (verified equal to the assessed commit). I read the complete part map, shared rules/workflow, relevant element-template material and the complete lead skill, answerer, conversation template, task skill/template and reader. Large combined tool outputs were truncated; targeted reads recovered the specific entries and code on which the observations below rely. This is not a claim that every changed installation file or every selected Scope entry received an exhaustive full-file review.

No operational handoff, frozen task, spec, plan, chronology, transcript, prior report or author's defense was read. Product skill instructions and their templates were treated as executable behavior. Installation README was excluded. Consequently I cannot establish fidelity of WAY-152–156 or the amendments to the human's task settlements, nor the approval of any particular meaning. Their pending `<request link>` approval fields remain pending integration evidence, not evidence of approval already given.

I inspected source history without commit messages: the earlier WAY-134 text at `3286b67` (2026-10-10), the earlier plan/dependency rules at `97b7212` (2026-10-11), and history locating the readiness rule at `1e06f70` (2026-10-05). Existing rules already required candidate acceptance and plan dependency ordering. They did not spell out the new complete-document acceptance and orchestrated ownership boundaries in the same terms. Actual recurrence after those rules cannot be measured: the permitted input excludes run/session records. Examined behavioral sessions: zero; no dated incident count is asserted. Test fixtures are synthetic cases, not observed incidents.

Authorship separation and acceptance deliberate-break evidence under WAY-69/WAY-149 are unavailable under this filtered-input contract. I make no claim that those requirements have been fulfilled.

## Observation 1: a plan-local task name is insufficient evidence of this plan's cycle

**Checked:** correspondence between task identity in the foundation and the new rule authorizing automatic progress proposals.

**Evidence:** `foundations/decisions.md:4553` (WAY-147) guarantees uniqueness only among tasks of one plan; `project-level/plan/template.md:82` explicitly says “unique in the plan.” WAY-153 (`foundations/decisions.md:4770`) and `project-plan-state-evidence/1` (`foundations/invariants.md:2105`) treat a matching cycle trace as evidence for the task. The implementation at `project-level/plan_state.py:164–192` constructs working/archive paths from `task.name` alone and searches all reachable archive history; it never matches a record to the current plan or task document. The black-box positive fixture at `project-level/test_plan_state_invariant.py:248` uses a record containing only `# Cycle record` and expects both progress transitions. The conversation contract already recognizes the same ambiguity: `project-level/lead/conversation_template.md`, opening paragraph, forbids overwriting a same-named task of another plan.

**Consequence:** two otherwise valid plans in one product can both name a task `report-download`. An old integrated record for the first plan then supplies both progress proposals for the second plan's still-unstarted task. This is a collision between the existing identity guarantee and the new evidence rule, not merely an untested spelling variant. The positive tests establish that no plan identity is required by the current implementation.

**What would change:** settle the identity boundary explicitly. One route is product-wide, persistent task-name uniqueness, with a check and a treatment of existing names. Another is evidence that binds a record to the plan/task identity, with ambiguity reported unchecked. Add a black-box case containing two plans with the same legal plan-local name and require no unsupported progress for the second. Leaving the rule as it stands avoids migration work but can hide unstarted work as delivered. Stronger identity costs either naming/migration constraints or record metadata and verification. No choice between those routes is made here.

## Observation 2: remote default is assumed to be product integration

**Checked:** whether “establishes the product's integration ref without guessing” is backed by a declared source of that identity.

**Evidence:** WAY-153 at `foundations/decisions.md:4777` states that promise. `project-level/plan_state.py:86–108` requires `origin/HEAD`, verifies that it agrees with the remote HEAD, and uses that branch as integration. The test at `project-level/test_plan_state_invariant.py:342` specifically accepts origin despite another remote. The new lead instructions do not require confirming that the product's integration route is its origin default before applying proposals.

**Consequence:** the reader proves which branch origin advertises as default; that does not itself establish which branch a product integrates work into. In a product that integrates into another branch, a valid integrated task can remain unchecked, or a record on the default branch can be treated as completion under the wrong route. This is a contract/source gap; no actual affected product or incident frequency was supplied.

**What would change:** either bind and expose origin-default-as-integration as the supported contract and have the caller validate that precondition, or consume an explicit integration route and report unresolved routes as unchecked. Leaving the implementation unchanged is cheap for products using the conventional route but does not justify the unconditional foundation promise. Explicit route support adds configuration and checks; a documented precondition is smaller but excludes other products.

## Independent checks with no additional concern

- **Who benefits and when:** the human leading an already handed-over plan gets a single conversation for question deduplication, explicit approval and progress maintenance. The instructions act before readiness writes and at session resumption; final acceptance is recorded before status updates. The task-cycle addition checks dependencies again at cycle start, so early refinement does not imply early implementation. These boundaries agree across WAY-124, WAY-134, WAY-144 and WAY-152–156 in the inspected material.
- **Over-application:** complete-document acceptance now applies to manual tasks with no new candidate settlements too. This adds a human turn to small tasks, but the rule explicitly separates acceptance of candidates from acceptance of the task actually implemented. No internal contradiction was found. Whether this extra turn was authorized by the source task remains unavailable.
- **Ownership and recovery:** the inspected contracts serialize shared files, keep body edits with refiners and final Status changes with the project orchestrator, require exact-document identity on interrupted acceptance, and preserve source answers before deleting conversations. No additional conflict was found among these contracts.
- **Invariant-test oracle:** the evidence tests use real disposable Git repositories and literal expected proposal strings; they do not call the reader to compute expected output. The subprocess tests observe actual Python process-start audit events, with a real fetched ref change as a positive control. Sharing literal fixture inputs does not share the product's oracle. Git's descendants are explicitly outside the audit hook's observation; the invariant says processes the reader starts, so that limitation is not itself a mismatch.
- **Form and ownership:** the new glossary term denotes the specific project-facing actor without embedding its procedure. The part-map responsibility, trust-boundary path and pinned command surface match the added reader. The two new invariants distinguish evidence behavior from permitted subprocesses. I found no reason to split every transition into its own invariant; they form one progress-evidence contract.

## What can be cut, and what it costs

The unrelated line reflow around WAY-09 (`foundations/decisions.md:236–263`) can be cut while retaining the words that add plan leading and its evidence reader. That reduces review churn without changing behavior.

I cannot justify cutting a substantive new role, the independent quotation check, whole-document approval, or the separate subprocess invariant from the permitted evidence. Each protects a different boundary. There is repeated ownership text across the lead skill, task skill and conversation template, but those are separate actor entry points; deleting it without proving that every actor reads the authoritative contract would trade reading cost for a missing instruction. No behavior-frequency evidence is available to decide that trade.

## Verification performed

Command run at the assessed checkout:

`python -B -m unittest discover -s project-level -p 'test_plan_state*invariant.py'`

Result: **20 tests passed**, 31.636 seconds. This is a direct run of the two new invariant suites, not a full gate or an acceptance deliberate break. No product files were edited. No foundation format-guard or full critical-flow result is asserted here.

## Addendum: completeness of the selected foundation inputs

This clarification concerns only the original assessed commit, `84cdc87cc12ce43526cb24a61640e39cf00e950a`; it is not an assessment of later settlement edits.

The foundation entries actually used for the judgments above are WAY-09, WAY-10, WAY-56, WAY-69, WAY-124, WAY-134, WAY-144, WAY-147, WAY-149, WAY-150 and WAY-152–156; the glossary entry `project orchestrator`; both new `project-plan-state-*` invariants; and the part-map entries (the map was read whole). Their whole-entry reading is now complete, including fields, rationale and Rejected where present. The initial combined output did not safely establish whole-entry reading for WAY-09, WAY-10, WAY-124 and WAY-134; a short targeted WAY-56 read also ended before its final Rejected sentence, and the recovered WAY-152 body lacked its heading. I completed those inputs from the original commit with `git show`, not from the subsequently changed working tree. No entry in this actually used set remains truncated or missing.

For the historical comparison, I also completed the entire earlier WAY-144 entry at `97b7212`; the earlier WAY-134 entry at `3286b67` had already been read whole. `1e06f70` was only an entry-introduction locator, not a claim to have read that historical readiness entry whole.

The remaining limitation is unchanged: this does not establish an exhaustive WAY-150 Scope-selection reconciliation or reading of every incoming/linked foundation dependency and required template example across all touched parts. It establishes whole reading of the entries actually used for this report's judgments. Excluded source fidelity, behavioral recurrence, authorship separation, deliberate-break verification and full-gate coverage remain unavailable as stated above. No finding is widened by this addendum.
