FAIL 2a46aecaf1c1afdc88eacc2d96ff15256a6274ee

# Whole-change review

Range: `d115159c554752601749efa8270ae76fbe02f4df..2a46aecaf1c1afdc88eacc2d96ff15256a6274ee`.
One-author change; no plan or slices. Counts: 2 blocking Important findings, 1 Minor, 0 out of scope. No Critical findings.

## Important — blocking

### 1. Carry the flaky-test rule into the cycle, including its source

**Anchor:** `task-cycle/record_template.md:125` (new thread; within the task; no slice).

**Ready to paste:** The new paragraph retains failures, but it does not connect their handling to the product's *Flaky tests* rule or name WAY-243 as its source, as To do 1 and answer 4 require. Add that connection and make the diagnostic-only purpose of a rerun apply even when the product has no such guidelines section; preserving a failed result in a report is not the whole rule about why a rerun is allowed.

**Why this is a finding:** This task arose because the cycle did not invoke the existing flaky-test rule. Its settled answer 4 expressly requires the cycle text to name WAY-243 beside the product's *Flaky tests* section. The changed paragraph instead introduces a reporting rule and cites WAY-260 alone. That decision derives from WAY-243, but its binding text only controls retained evidence and request contents; it does not state that rerunning serves diagnosis only and cannot make a gate run pass. The existing step 10 at `task-cycle/skill/SKILL.md:309` also has no such constraint: it calls for affected checks again after a failure. A product without a *Flaky tests* section can therefore follow the new cycle wording, rerun merely to obtain a green gate, and still preserve the earlier failure and counts in the request. That meets the added reporting text but misses the distinct behavior the task expressly imports. Put the source and the rule at the point of handling the failed-then-passed check, retaining the reporting requirements already present. This does not require the cycle to fix or diagnose every unrelated defect before opening a request.

**Evidence:** Frozen task *To do* 1, *Questions to settle* 4 and settlement row 1; WAY-243 in full; `product-guidelines/testing/template.md:219`–222; comparison with the complete Verification paragraph and skill step 10. A search of both cycle files for `WAY-243|Flaky tests` finds neither, while the positive-control search finds the new WAY-260 references and rerun wording.

### 2. Do not invent the rejected option of settlement row 2

**Anchor:** `foundations/decisions.md:7458` (new thread; within the task; no slice).

**Ready to paste:** WAY-261 records “reporting only the successful rerun” as a rejected option, but settlement row 2's source records only acceptance of reporting both runs. Use `unknown` for its *Rejected* value unless a source actually records that alternative as one considered and not chosen.

**Why this is a finding:** The field tells later agents what the human weighed and rejected, not what the opposite of a decision would be. Row 2 points to To do 4 and the acceptance “ok, niech będą obie”; it contains no rejected alternative. “Only the successful run” appears in the row's separate column describing what the cycle would otherwise guess. WAY-134 explicitly prohibits deriving rejected options from that column. The new entry turns exactly that possible guess into a historical human choice. A future change proposing shorter evidence would then have to justify revisiting an option the supplied source never says was weighed. `unknown` preserves the accepted binding rule while avoiding that false source claim. This is a source-fidelity defect in a required foundation settlement, not a wording preference.

**Evidence:** Complete frozen task settlement row 2 and its To do 4 source; WAY-134's binding rule and violating example; `elements/decisions/template.md`, the *Rejected* rule; new WAY-261. No outside source was supplied that establishes the rejection.

## Minor

### 3. Put the requested counts in the Request handoff's Checks field

**Anchor:** `task-cycle/record_template.md:169` (new thread; within the task; no slice).

**Ready to paste:** Could the *Checks* placeholder also name the rerun result and failure/pass counts? To do 3 explicitly names this field, but it still asks only for the gate command, exit code and failed or unrun checks, while the neighboring review-findings placeholder now asks for counts.

**Why this is a finding:** The request is assembled from *Request handoff*, so this placeholder is the immediate prompt for its evidence. For a check inside the task's parts that fails six times and passes once, filling the placeholder literally gives its name and results without the requested frequency. The earlier Verification paragraph and step 13 do require counts, so the overall instructions already supply the substantive rule; this is a Minor consistency and discoverability gap rather than an independently missing reporting behavior. Adding the same evidence to this placeholder closes the task's specifically named template surface.

## Declined to judge

None.

## Coverage and scenario checks

- To do 1: retaining every failed run with command and result is implemented. Direct application and attribution of the existing flaky-test rule is incomplete (finding 1).
- To do 2: both step 13 and *Review findings listed* add outside-part failed-then-passed checks, file paths, rerun results and counts. The human remains the one choosing new tasks; review findings are not reclassified by the orchestrator.
- To do 3: Verification and step 13 require both inside-part and outside-part checks in *Checks*, with rerun results and counts. Only outside-part checks additionally join the out-of-scope item. The *Checks* placeholder itself remains unchanged (finding 3).
- To do 4 and settlement row 2: the author/executor report explicitly gives both runs as command and exit code; existing “each check you ran” still covers more than two runs. WAY-261 carries that accepted meaning, with the source defect in its *Rejected* value (finding 2).
- Settlement row 1: WAY-260 carries retained failures, counts, the additional outside-part listing and application in all products. Its link to WAY-243 does not substitute for the task's required operational invocation of that rule (finding 1).
- Manual trace: a check in `task-cycle/**` failing twice and passing once stays in the record and *Checks* with 2 failures/1 pass, and does not enter the outside-part item. The corresponding check in `gate/**` also enters that item, because the part map assigns it to `gate` while this task's changed instructions and foundation-entry scopes belong to `task-cycle`.
- Manual trace: repeated failures from multiple author reports are not overwritten; every failing run stays, every check run already has command/exit-code evidence, and the request counts failures and passes rather than retaining only the last verdict.
- Classification can be performed from the frozen task, changed paths and part-map rules when preparing the request. Recording the check path and the classification evidence does not require a maintained foundation-reading selection list. The author's weakest-point check addresses the right risk and gives a valid small example; it does not catch either blocking finding.
- No code, test, invariant test, trust boundary, irreversible operation or user interface changes. No guideline files selected: the frozen task explicitly settles the empty reading for this Markdown-only change. Foundation review invariants are unchanged; no private source link is introduced into tracked files.

## Executed checks

All commands ran in `C:/Storage/repos/the-way/.runs/worktrees/retain-failed-checks`.

| Command or method | Exit code / result |
|---|---|
| `git rev-parse HEAD` | 0; matches the dispatched head |
| `git log --oneline d115159c554752601749efa8270ae76fbe02f4df..2a46aecaf1c1afdc88eacc2d96ff15256a6274ee` | 0; one commit, `2a46aec` |
| `git diff d115159c554752601749efa8270ae76fbe02f4df..2a46aecaf1c1afdc88eacc2d96ff15256a6274ee` | 0; all four changed files reviewed |
| `git rev-parse --show-superproject-working-tree` and `git ls-files --stage -- ':/.the-way'` | 0; neither product condition holds |
| `python -B elements/common/foundation_check.py` | 0; 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0; 0 errors, one existing `dead-path` warning at `AGENTS.md:21` for the private backlog path |
| `git diff --check d115159c554752601749efa8270ae76fbe02f4df..2a46aecaf1c1afdc88eacc2d96ff15256a6274ee` | 0 |
| `git status --short` | 0; clean before writing this ignored report |
| Manual task-to-diff and settlement-to-source comparison | Findings 1–3 above |
| Manual inside/outside-part and repeated-failure traces | Reporting and classification work as described above; the diagnostic-only rerun constraint remains absent from the cycle text |

The full gate was not run: the method and handoff reserve it to the orchestrator. No behavioral agent experiment was run; the scenario checks above are instruction traces, not measured agent compliance. Mechanical checks cannot establish source fidelity or compliance with the imported flaky-test meaning.

## Reads beyond the handoff and own selection

The required own foundation reading used the part map's assignment rules, complete decision entries scoped to `task-cycle`, the decisions named by the frozen task, reached invariants naming `every`, and the glossary. The methods and repository guide were read as directed; the task's settled empty guidelines reading applies.

Additional targeted reads beyond that selection:

- `elements/decisions/template.md` whole, to verify the form and source requirements of both new decisions.
- `product-guidelines/testing/template.md`, the *Flaky tests* passage, to compare the accepted source rule with the cycle wording; this is an unchanged process template, not a selected product guideline.
- WAY-04, WAY-05, WAY-19, WAY-29, WAY-41, WAY-53, WAY-129 and WAY-225 whole, following the reached invariant links and checking decision form, numbering and source fidelity.
- Relevant surrounding passages of `task-cycle/change/SKILL.md`, `task-cycle/record_template.md` and `task-cycle/skill/SKILL.md`, to trace report collection, gate handling and request assembly beyond individual diff hunks.
- The user-required code-review playbook, script rules and search rules, for review reporting, safe commands and validation of negative search results.

No cycle record was read. No tracked file, index or branch was changed.
