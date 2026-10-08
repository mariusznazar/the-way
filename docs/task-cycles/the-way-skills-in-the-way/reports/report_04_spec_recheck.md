# Report 04 — spec reviewer, re-check (saved by the orchestrator from the returned text)

All 11 earlier findings resolved (11 partly: N1). R2/R3 routes fit WAY-25, WAY-30 (`decisions.md:822-824`: "An
exception written in advance into a decision's binding sentences is not a contradiction") and the cycle skill
(`SKILL.md:124-126`, `172-174`). Six `WAY-09@b829b86a` references (`invariants.md:152-202`), no others. Codex
sentence verbatim: "In Codex, the initial list also includes each skill's file path." (text run 767).

New findings:
- N1 should fix — §4.7 PowerShell does not parse in Windows PowerShell 5.1 (`ParseInput`:
  InvalidVariableReferenceWithDrive at lines 4 and 6, `"$n: …"`). Fix: `"${n}: …"` or `-f`.
- N2 should fix — §8 says the decision guard reports stale fingerprints of WAY-09/WAY-27; the references are in
  invariants' *Derives from*, checked by the invariants guard, whose `check_fingerprints` runs only with
  `--merge-onto` (`elements/invariants/format_guard.py:24-29, 100-101`); with `none` it is unchecked. Fix: name the
  invariants guard, state unchecked, compute new fingerprints with `relation-model/fingerprint.py` and compare by
  hand as a partial check, or list as unchecked.
- N3 minor — `outbound-link-reach` edit cites WAY-07 (decisions); invariants are versioned by WAY-57
  (`decisions.md:1563-1569`), no main branch → stays `/1`, comparison unchecked with `--base none`. Exception too
  wide and ambiguous. Proposed: "No file git tracks contains a link into a repository that a reader not signed in
  to its host cannot open, or into a private note collection other than to the place of tasks that the
  `## Backlog` section of the root `AGENTS.md` names."
- N4 minor — WAY-127 relations/Based on need fingerprints (`derives from WAY-44@2f2b6227`, `<fact>@<fingerprint>`).
- N5 minor — `skill-entry-points/1` sentence states less than the test checks (product checks, root rule, skip
  line, prefix rule): extend the sentence or move those assertions out of the citing test.

No other contradictions (§4.2, §4.4, §6, §7 failure mode agree; facts match §2; WAY-27 has one dependant,
`invariants.md:473`).

Verdict: approved after fixes; N1, N2 in spec or carried into the plan; N3–N5 in the foundation step.
