# Blocking findings


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
