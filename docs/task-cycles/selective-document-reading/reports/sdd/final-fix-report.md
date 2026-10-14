# Final review fix report

## Result

- **Status:** DONE
- **Base:** `0c266f3da8cb92204d7788c4bce9065bc2e8b92e`
- **Head:** `1de9e1aa8e91134131d2e5c6d07c0f0ebf359186`
- **Commit:** `1de9e1a docs: clarify plan check example`
- **Changed tracked file:** `foundations/decisions.md`
- **Boundary:** committed final-review fix; before scoped re-review and independent foundation assessment.

## Sources and correction

Read the complete final review, frozen task, and current WAY-151 entry, including its binding
sentences, fields, rationale and rejected options. Also read the glossary's full `format guard`
entry and *Avoid* field, the decision template's *Verification* rules, the decision skill's
relevant workflow, and the common rules and way of working. The source distinguishes an element's
entry-shape script (a format guard) from the readiness or plan checks; the glossary lists
`checker` as an avoided synonym for the former.

Changed only the WAY-151/1 Verification example phrase from `the checker receives a reduced copy`
to `a readiness or plan check receives a reduced copy`. Kept the example's normal line wrapping.
No binding sentence, meaning, version, approval placeholder, or relation changed.

## Checks

- Before correction, the focused glossary diagnostic against the review's exact base reported
  `checker` in `foundations/decisions.md` 2 times versus 1 on base: **1 error, 0 warnings,
  2 unchecked; exit 1**. The review report records the full diagnostic output.
- After correction,
  `python -B elements/glossary/format_guard.py foundations/glossary.md --base 52b9d487efeafe37c46ad2b9f10d60c13a885e63 --merge-onto none`
  reported **0 errors, 0 warnings, 2 unchecked; exit 0**. The two unchecked items are the
  no-merge-onto checks for TODO entries and terms with no use after merge.
- `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`
  reported **0 errors, 9 warnings, 5 unchecked; exit 0**. Warnings: five existing overdue reviews
  (WAY-03/21/52/55/69) and four approval URL placeholders. The five unchecked results are the
  expected no-main/no-merge comparisons.
- `python -B .runs/task-cycles/selective-document-reading/reports/verify_foundation.py` reported
  **151 relations checked, 0 control characters; exit 0**. Fingerprints remain WAY-111
  `e2fd46dc`, WAY-115 `eb7ba15c`, WAY-134 `b858b34f`, WAY-150 `3bd9e695`, and WAY-151 `739610de`.
- `git diff --check`: **exit 0**.
- No full test suite was rerun for this prose-only correction. The prior 1,265-test evidence is
  recorded at the pre-fix Head in `reports/final-verification.md`; it is not represented here as a
  post-fix result or as a full-gate pass.

## Self-review and remaining concerns

The committed diff is one localized Verification example edit in the authorized file. It uses the
review's exact settled wording and does not call the readiness or plan checks format guards. The
existing warnings and unchecked checks remain visible above. The scoped re-review and independent
foundation assessment remain for the next stage; this report does not perform or waive them.
