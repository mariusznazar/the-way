# Review-fix report

- **Status:** done
- **Fix base:** `2a46aecaf1c1afdc88eacc2d96ff15256a6274ee`
- **Commit:** `3191d42 fix: apply flaky check rule in task cycle`
- **Files changed:**
  - `foundations/decisions.md`: 1 addition, 1 removal
  - `task-cycle/record_template.md`: 8 additions, 5 removals
  - `task-cycle/skill/SKILL.md`: 4 additions, 1 removal

## Findings

1. **Fixed — cite and apply the flaky-test rule to cycle reruns.** The Verification instructions in
   `task-cycle/record_template.md` now name the product testing guidelines' *Flaky tests* rule and
   WAY-243, state that a passing rerun serves only to diagnose the flaky behavior and never makes a
   gate run pass, and apply this rule when the product guidelines have no *Flaky tests* section.
   Step 10 in `task-cycle/skill/SKILL.md` gives the same constraint where the orchestrator handles
   affected checks again. Existing retention and request-reporting requirements remain in place.
   Evidence: `rg` confirmed WAY-243, the diagnostic-only purpose, and the no-gate-pass constraint
   in both cycle files.
2. **Fixed — do not claim an unrecorded rejected option.** WAY-261's `Rejected` field in
   `foundations/decisions.md` now reads `unknown`, as the settlement source records acceptance of
   reporting both runs but no rejected alternative.

The review's Minor finding about the Request handoff's *Checks* placeholder remains unfixed, as
directed by the fix handoff; it is retained for the request. No finding was contested.

## Checks

| Command or manual check | Exit code / result |
|---|---|
| `python -B elements/common/foundation_check.py` | 0; 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0; 0 errors, one existing dead-path warning at `AGENTS.md:21`, 3 info lines |
| `git diff --check` | 0 |
| Manual weakest-point check: search both cycle files for `WAY-243`, the diagnosis-only purpose and the gate-pass constraint | Passed; the source and both constraints appear in both relevant locations |
| Manual source-fidelity check: compare WAY-261's `Rejected` field with settlement row 2 and its source | Passed; the field is `unknown`, and no alternative was added |

The full gate was not run because the handoff reserves it for the orchestrator. No tests were
written: this fix changes process instructions and a decision-log field, not executable behavior.
The instruction checker reports one existing warning for the private backlog path; no check failed.

## Additional reach

- Re-read WAY-243 whole and the task's settlement row 2 to apply each finding against its named
  source.
- Re-read WAY-134 and `elements/decisions/template.md` whole for the rule that a decision's rejected
  options must come from what the source records.
- Read `elements/common/way_of_working.md`, `elements/common/rules.md`, and the decision element's
  `read.md` and `decide_entry.md` for correcting WAY-261.
- No other foundation entries or guideline files were changed. The Minor finding was not fixed.

No failure or unchecked check remains beyond the full gate reserved to the orchestrator. No trust
boundary, irreversible operation, UI, or test behavior changed.
