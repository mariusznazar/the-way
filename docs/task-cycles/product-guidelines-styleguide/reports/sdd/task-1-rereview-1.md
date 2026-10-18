### Finding Verdicts
- **I1: two rules of writing cite decisions that do not set them (code in backticks; no emphasis words)** — ADDRESSED. Both items are gone from `## Rules of writing` (diff, `product-guidelines/template.md` old lines 26-36 removed). The content now sits in `## Note: a file of guidelines read as an instruction file` (new lines 43-58), placed between `## Rules of writing` and `## The invariants of guidelines`. The note says it is no rule of the template and cites no decision as setting it. It cites `instruction-files/check_instructions.py` and `instruction-files/principles.md` as the sources. Content checked against the sources: `check_instructions.py:533-537` warns when more than one line carries emphasis, and `principles.md:171` says emphasis goes on one rule per file at most. The dead-path and at-import behaviour matches the previous text and the positive control in the fix report. The note's own wording is also narrower than before: it no longer claims a rule, only what the two files do.

### New Breakage in the Fix Diff
None. The fenced skeletons and required headings are untouched. The note carries no decision citation and no capitalised emphasis words. The fix report shows the covering checks and their output: `check_instructions.py` run with `0 error, 0 warn, 2 info`, `git diff --cached --check` clean, and the weakest-point script with the forms still following the fixtures. Minor, not blocking: the note says "`AGENTS.md` or `CLAUDE.md`" where the old text and WAY-192 name only `AGENTS.md`. This is accurate for "repository instruction file" per the glossary, and it is not a rule.

### Out-of-Scope Observations
- The generalisation to every discipline, which the original review raised, is now stated as a fact about the scripts rather than as a rule, so it no longer needs a decision.
- Report concerns 2-4 (file-name pattern `<discipline>-<part>.md` absent from WAY-167, package-name examples, the form-check interface) stand and are unchanged by this fix.

### Verdict
**Fix round:** All findings addressed, no new Critical/Important breakage
