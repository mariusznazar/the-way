# Fix report

**Status:** done

**Commit:** `d02e9adfe5ac26e0ac0e6acc8e1f25598afaacdb` (`Carry generated output action into slice goal`), on `task/generated-output-one-slice`.

## Findings fixed

1. Removed the unsupported rejection of “multiple patterns for one output directory” and its invented reason from WAY-263. Q2's rejected wording concerns one pattern across both output directories, while its two-pattern option means one pattern for each directory. This corrects the record of rejected options; it does not change the decision's binding rule.
2. Updated the planner instructions so a slice's Goal carries the full generation action: after changing an input, run the named command, handle obsolete output paths it reports, commit all output, and do not edit generated output by hand. This makes the obligations available in the copied slice section that the executor receives.

## Files and checks

- `foundations/decisions.md`: 3 insertions, 4 deletions.
- `task-cycle/plan/SKILL.md`: 4 insertions, 2 deletions.
- `python -B elements/common/foundation_check.py` — exit 0; 0 errors.
- `git diff --check` — exit 0.
- `git diff --check HEAD^ HEAD` — exit 0.
- Own-work check: compared the revised Goal instruction with the planner's run, cleanup and commit duties and confirmed all are explicitly carried into Goal; checked WAY-263's remaining rejected options against frozen task Q1–Q3 and the decision template rule. Both findings are addressed.
- No test was run: this fix changes documentation only, and the repository's prose instruction has no focused executable test. No failed run occurred during this fix.

## Reaches beyond the dispatch

- Read frozen task Q1–Q3 to distinguish the source's rejected options from the unsupported clause.
- Read `elements/decisions/template.md`'s Rejected rule to confirm derived alternatives must not be recorded as human-rejected options.
- Read the full review and the current affected passages in WAY-263 and `task-cycle/plan/SKILL.md` before editing.

## Searches not found or unclear

None.
