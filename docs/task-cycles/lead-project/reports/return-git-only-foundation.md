# Return-step foundation correction — Git-only reader

Status: ready for root's ruling and independent check dispatch. Source HEAD before this correction: ea9a23e93958aa3e579d1846177b1d32c1d739e4. Written files: foundations/decisions.md and foundations/invariants.md only, plus ignored reports/contract. No source, code, test or existing invariant sentence changed; no child agent, review or deliberate break was launched. Root accepted the completeness finding provisionally under the delegated task cycle; human approval remains the reviewed merge.

## Meaning and source

New project-plan-state-subprocesses/1: „Każdy program uruchamiany jako podproces przez czytnik stanu planu jest Gitem.” WAY-153 Verification now names this invariant at level 1, keeping human application of proposals and resolution of PR outcomes at level 2. Frozen task item 5 and accepted settlement 2 already require Git-only execution; WAY-12 and WAY-22 require its commit-falsifiable part as a derived invariant. This closes a verification gap, not a new behavioral choice. The preceding source-grounded judgment is reports/return-git-only-answer.md.

Full new entry:

```markdown
## project-plan-state-subprocesses/1

Every subprocess the plan-state reader starts runs Git.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@33b10f25
- **Part:** project-level
- **Correction:** none
```

The exact shared Method follows the root's adjustment and WAY-61: one command can record verdicts for multiple invariants. Its record name is output storage, not another property of the invariant. A second record name for the same directory would duplicate the run without extending coverage. The sentence concerns subprocesses the reader itself starts, not Git's own helper/transport subprocesses. Its Part is project-level, which owns the reader; no outside fact supplies a condition, so Rests on reads none. No global restriction changes and no existing evidence sentence is extended with a second property. The check author receives only reports/subprocess-check-contract.md, which contains the sentence, current identifier/version, exact Method and Part/derivation, allowed check path and observable boundary without this rationale or the ordinary-test mechanism.

Complete revised Verification field:

```markdown
- **Verification:** level 1 — invariants: project-plan-state-evidence ·
  project-plan-state-subprocesses. Level 2 for applying proposals and resolving PR outcomes —
  an agent compares the evidence and leading session with the decision:
  - complies: the project orchestrator applies supported transitions with a reason and evidence
    in the plan's log, resolves an unchecked PR outcome through the product's chosen PR tool,
    and shows a closed-unmerged PR to the human without automatic correction;
  - violates: the project orchestrator treats an unchecked observation as completion without
    resolving it, silently normalizes a conflicting trace, or guesses the PR outcome when the
    product's PR tool is absent instead of asking the human.
```

WAY-153's complete binding paragraph, rationale, rejected options and all other fields retain their existing text. Recomputed binding fingerprint remains `33b10f25`; the existing project-plan-state-evidence link and the new subprocess link both use it. No incoming fingerprint changes are triggered by changing Verification alone. Version stays /1 before main. The source task's Git-only restriction remains exactly the same.

## Refreshed context and whole-foundation search

Behaviorally touched part: project-level. Complete current Scope inspection returns 40 decisions: WAY-09, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 126, 127, 134, 137, 138, 139, 140, 142, 143, 144, 145, 146, 147, 150, 151, 152, 153, 154, 155 and 156. These are contained in the full entries already read and recorded by this foundation author. `git diff 7b070c1 HEAD --` all five foundation files is empty: those retained entries and the whole map/glossary/facts have not changed since that reading. This correction freshly read the complete WAY-12, 22, 38, 153, script-subprocesses/1 and project-plan-state-evidence/1 and the two focused handoffs. The existing pinned element skills/common rules/templates remain the ones already read. Inspection of Scope is current, includes wrapped fields and finds no missing field or new applicable decision. The additional invariant is the only new entry this correction adds.

Exact whole-foundation query before writing:

```text
rg -n -i 'git.only|subprocess|starts a program|starts.*git|product.declared|plan.state.reader|state.reader|WAY-153@|project-plan-state-subprocesses' foundations/decisions.md foundations/invariants.md foundations/glossary.md foundations/environment_facts.md foundations/part_map.md
```

It searches all five elements rather than only Scope matches. Positive controls are WAY-153's Git-only sentence and the script-subprocesses sentence. Findings and assessed consequences:

- WAY-38 and script-subprocesses/1 permit Git or a product-declared command. The new property is stricter for this reader and consistent with that allowance; no collision or narrowing relation is needed because requiring only an allowed subset does not contradict the broader allowance. Keep both whole existing entries unchanged.
- WAY-153 contains the narrower accepted policy but assigns its execution boundary to level 2. Revise its Verification to name the new derived invariant; its binding fingerprint is unchanged.
- project-plan-state-evidence/1 is the sole existing incoming WAY-153 fingerprint link. Its evidence/nonmutating-output sentence says nothing about executable identity and remains unchanged. The new invariant provides the separate coverage instead of modifying or reciting the existing one.
- The project-level map's state-reader failure mode concerns unsupported progress, not executable identity. The existing responsibility and project-level/** pattern already own the reader and the planned independent check; no map ownership, severity, dependency, surface or detection promise changes with this narrower invariant. The existing state-evidence detection remains accurate for its named failure.
- Environment-fact hits are incidental “starts” wording in Claude Code/Codex loading facts. Read in their complete existing entries, they supply no condition for subprocess identity and require no links or change. The glossary contains no conflicting meaning or a definition of subprocess; the sentence uses its ordinary technical meaning.
- No existing identifier duplicates project-plan-state-subprocesses. The explicit follow-up identifier search over map, environment facts and glossary returns no match, while the broader query found the known current entries as positive controls. No unlinked conflicting rule or additional required dependent entry was found.

This is the additional initial WAY-33 search for the return-step entry against current task HEAD. It does not claim the final search against the then-current integration tip or independent assessment has happened; those remain the root's later work.

## Cost and verification

Leaving the narrower rule only in a decision and ordinary tests would allow a future product-declared non-Git executable to satisfy the broader foundation invariant while breaking this reader's accepted rule. Adding the separate invariant costs an independent check and deliberate-break acceptance. Sharing Method avoids duplicate whole-directory runs; keeping the sentences separate preserves independent meanings and avoids changing the established evidence check.

Actual checks:

- Decision format guard, `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`: exit 0, 0 errors, 14 warnings, 5 unchecked. Full output: reports/return-git-only-guard-decisions.txt. Nine warnings are existing request-link placeholders; five are existing overdue reviews WAY-03, 21, 52, 55 and 69. The five unchecked lines all derive from none options: base log preservation/version growth, base template versioning, merge TODO, repeated versions and relation fingerprints. None is silently cleared.
- Invariant format guard, `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`: exit 0, 0 errors, 0 warnings, 3 unchecked. Full output: reports/return-git-only-guard-invariants.txt. The three none-option unchecked lines cover base identifiers/versions/corrections/violations, merge TODO and merge link fingerprints. No human_verdicts.md exists; no human verdict was given.
- `python -B gate/run_tests.py gate`: exit 0, 98 tests passed.
- Shared Method, `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`: exit 0, 227 existing tests passed. The produced record contains project-plan-state-evidence/1 verdicts (positive control), but exact search for project-plan-state-subprocesses returns no match. The new property is therefore not yet checked; it has no invariant verdict and is not claimed pass. The method's aggregate success does not supply the missing verdict.
- `git diff --check`: exit 0. The inspected diff contains one new invariant entry and the one Verification-field replacement only. Existing invariant checks and every existing invariant sentence are untouched.

These are partial repository checks, not a full-gate pass. New check implementation, final code review, independent assessment and later return-step deliberate-break acceptance remain pending. The source-grounded R2 finding is addressed at the sentence/entry boundary; root still routes the three separate authors and the remaining acceptance work. No unresolved source choice or additional foundation finding blocks independent check dispatch.
