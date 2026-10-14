# Request-boundary verification

Request: https://github.com/mariusznazar/the-way/pull/18, created as draft against foundations.
Final reviewed/settled source is `c744b15f4a48d5525e42022a5e364997e2fe1f43`.
After that commit, the only product edit replaces four literal `<request link>` values in
decision approval fields with this request URL. Bytes outside those values are preserved.
No assessed binding sentence, relation, Scope or instruction changes at this boundary.

`request-checks.py` captured the following independent commands in UTF-8 with explicit exit
codes in `request-verification.json`; root read their actual outputs. One additional direct
no-base decision-guard run confirmed the captured 0/5/5 result when the first console read did
not display the output; it was an output-evidence check, not a broader test run.

| Check | Actual result | Full evidence |
|---|---|---|
| Decision format guard, `--base none --merge-onto none` | exit0; 0 errors, 5 warnings, 5 unchecked groups | [output](request-decision-guard.txt), [verdicts](request-decision-guard.jsonl) |
| Glossary Avoid-growth diagnostic, real base52b9d48 and `--merge-onto none` | exit0; 0 errors/warnings, 2 unchecked | [output](request-glossary-diagnostic.txt) |
| Direct existing-parser binding fingerprint check | exit0; all151 current relations match; unchanged five affected fingerprints; zero controls | [output](request-relations.txt), [method](verify_foundation.py) |
| `git diff --check 52b9d48` | exit0, no output | [output](request-diff.txt) |
| Control scan, all14 changed Markdown paths | zero forbidden controls | [structured results](request-verification.json) |
| Final available suites at stable0c266f3 | 1265 tests pass; common0/exit1 unchecked | [full outputs/records](final-verification.md) |
| Critical-flow and changed-common runners after assessment correctionc744b15 | gate98 pass; common0/exit1 NO TESTS RAN unchecked | [fix report](assessment-fix.md), [gate output](assessment-fix-gate.txt), [common output](assessment-fix-elements-common.txt) |
| Map guard on unchanged map/guard inputs | 0 errors/warnings, 7 unchecked | [existing full output](final-part-map-guard.txt), [verdicts](final-map-guard.jsonl) |

The map and executable test/guard source have not changed since the corresponding runs. The
later changes are the readiness/plan example phrase, one shared instruction citation/obsolete
marker and four request URLs. No executable source or invariant check changed, so no unrelated
suite repetition or new deliberate break is claimed. Both source corrections were scoped-reviewed.

## Preserved warnings and unchecked work

- Existing overdue reviews: WAY-03, WAY-21, WAY-52, WAY-55, WAY-69. Four placeholder warnings
  disappeared after the URL substitution; dates of unrelated decisions were not edited.
- Decision no-base/no-merge checks: existing lines/version increments; template-change decision;
  TODO at merge; equal copies of versions; carried relation fingerprints. Direct verification
  supplements only the last; none of the unavailable comparisons is called passed.
- Map: coverage files absent for wording-reaches-dependants and skills-reach-the-way-sessions;
  no command reports promise-level policy/change paths or the part-dependency graph; no-base
  comparisons of known violations, identifiers and lowered criticality remain unchecked.
- Glossary diagnostic: TODO entries and terms unused after merge require a merge target and
  remain unchecked. Using the actual base to detect word growth does not create a main branch.
- Common has no executable tests. Source walkthroughs/reviews do not execute future agents.
  Actual read/comprehension completeness, unlinked semantic discovery, real-project context
  savings and the full gate remain unverified. Existing Method TODOs are unchanged.

No open review finding, unresolved foundation meaning or human action blocks ready status.
The cycle record's history-only publication and ready transition follow these checks.
