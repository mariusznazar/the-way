# Settlement of the independent assessment (`reports/assessment.md`, read whole for each remark)

Assessed range `235b0b4..28b42a2`, 51 files (`reports/assessment/assessed-files.txt`). Call: apply,
with corrections; nothing has to be cut. Settled by the orchestrator (step 11):

| Remark | Settlement | By |
|---|---|---|
| I1 WAY-203's first sentence reads as one guidelines rule per linter rule (`decisions.md:6882`) | accepted: reword so it says the blocking rules stand in the adopting decision under the one linter rule, keeping row 7's meaning; renew WAY-204's relation | foundation author B (wrote WAY-203) |
| I2 styleguide template and skill never mention test cases, now required of every discipline (WAY-168, C1) | accepted: `product-guidelines/styleguide/template.md` and `product-guidelines/styleguide/SKILL.md` point to "Test cases of a rule" of the common template and say which of the styleguide's required rules take the relative reading for an invariant on the violated list (C19); no rule restated | executor S1 (wrote the common template's rule) |
| I3 two clauses with no invariant test: a test case left open to the end (`invariants.md:2233`); a Kinds row whose *File* names a tracked file not of the form `guidelines/coding-<kind>.md` (`:2213`) | accepted: one invariant test each; if the open-to-end clause cannot be isolated (F4's reason), record it as unchecked with the reason | check author D |
| M1 sentences say less than the check reports | kept; listed in the request (pre-existing pattern, `guidelines-check-code-path/1`) | — |
| M2 *Avoid* words occur nowhere outside the glossary | kept: *Avoid* lists the words a writer would reach for, not words present (glossary skill's choice) | — |
| M3 WAY-212 restates WAY-167's table; M4 WAY-201 could join WAY-200 | kept: rows 1, 15, 3 and 22 are separate settlements, each written whole as its own entry (WAY-134, C20) | — |
| M5 NAMES entry and the dedicated installation test overlap | kept: NAMES is the invariant test (C24), the dedicated test is spec §6.6's ordinary test | — |
| M6 styleguide fixture's cases could not decide `background-pair` | kept; listed in the request | — |

After these, the affected checks rerun and one affected code review covers `5a00041..HEAD` (the
return step `355a240`, C39 `f34e477`, C40 `28b42a2` and these settlements), with the deliberate
breaks of the edited `guidelines-check-kind-index/1` and of every invariant test added here; it
ends as "The end of a code review" gives.
