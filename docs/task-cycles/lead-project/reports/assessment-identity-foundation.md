# Foundation correction within assessment settlement — identity

Status: committed-stage material ready for root's ruling and independent check correction. Base HEAD before correction: 84cdc87cc12ce43526cb24a61640e39cf00e950a. Branch/worktree: task/lead-project at C:/Storage/repos/the-way-wt/lead-project. Final correction commit is returned separately; it contains only foundations/decisions.md and foundations/invariants.md. No code, check, workflow, map, unrelated reflow or additional assessment was changed or launched. This is settlement of observation 1 of the one independent assessment, not a second assessment or human approval of a new meaning.

## Old/new meaning and fidelity

Meaning for the request: „Czytnik przypisuje ślad cyklu do konkretnego zadania bieżącego planu na podstawie już zapisanego pochodzenia zadania; ta sama nazwa nie wystarcza, a brak, niejednoznaczność lub sprzeczność nie daje postępu.”

Before correction, WAY-153 and the evidence invariant said matching trace/that task's archive without explicitly establishing which plan's task owned it. The reader/check contract accepted an ordinary archived file by path alone, despite WAY-147 only guaranteeing name uniqueness within one plan. The revised text makes the existing referent explicit using already recorded task provenance; it keeps the original names, trace paths, filename independence, two composed transitions, fresh integration evidence, Git-only policy and document preservation. No global uniqueness, required filename, UUID, new metadata field or body-content equality was added.

Frozen task item 5 speaks of this task's cycle traces and requires conflicting traces to reach the human; accepted row 2 repeats that boundary. WAY-147 retains plan-local identity. Existing Task source and Task relation in task-cycle/record_template.md, frozen source instruction in task-cycle/skill/SKILL.md:92–93, Project relation in project-level/task/template.md and the plan's Document cell supply the evidence already required by the process. The source-grounded ruling and root's two-plan reproduction are reports/assessment-identity-source-ruling.md and reports/assessment-identity-reproduction.txt. Root's inspection of the real acceptance archive found Task source and Task relation already present; that provenance must still be verified against the original plan/document in the later corrected acceptance run, rather than replacing the original PR #12 criterion.

This replaces the reversible part of C13 that treated any retained ordinary file at the same slug as sufficient identity. C13's rejection of a compulsory basename remains. Missing or ambiguous ownership is unchecked/no progress from that trace; explicit provenance belonging elsewhere is human reconciliation/no progress. Supported local evidence can still prove start while completion evidence remains unresolved; the text does not turn every incomplete fetch/observation into a prohibition on an independently supported start. The task's post-merge no-re-refinement rule is preserved: identity association is not a semantic reevaluation of already accepted task scope.

Both entries retain /1 under the pre-main route. Correction remains none: this is not a claim that old expected test values can be retained under an invariant Correction declaration. Required positive/negative check inputs change, so the protected check is handed back to its independent author through the foundation stage. Approved by retains the prescribed request placeholder for the later real URL swap.

## Current selection and whole-foundation search

Touched part remains project-level. Refreshed complete current Scope inspection returns 40 matching entries, including wrapped fields, with no missing Scope or new match:

WAY-09, WAY-106, WAY-107, WAY-108, WAY-109, WAY-110, WAY-111, WAY-112, WAY-113, WAY-114, WAY-115, WAY-116, WAY-117, WAY-118, WAY-119, WAY-120, WAY-121, WAY-122, WAY-123, WAY-124, WAY-126, WAY-127, WAY-134, WAY-137, WAY-138, WAY-139, WAY-140, WAY-142, WAY-143, WAY-144, WAY-145, WAY-146, WAY-147, WAY-150, WAY-151, WAY-152, WAY-153, WAY-154, WAY-155, WAY-156.

The original foundation author has read these complete entries, full current part map/glossary/facts, relevant invariant Part entries and the pinned skills/common rules/templates. The current changed sources were read again: complete frozen task, WAY-147/153, evidence invariant, record/task/plan templates, reader and the source ruling/assessment observation. This correction selects source identity, authority and evidence rules; it does not silently expand scope to a different naming policy.

Exact whole-foundation initial query before writing:

```text
rg -n -i 'task.provenance|task.source|project.relation|task.identity|plan.local|unique in.*plan|WAY-153@|plan.state.reader|state.reader' foundations/decisions.md foundations/invariants.md foundations/glossary.md foundations/environment_facts.md foundations/part_map.md
```

Expanded exact query to recover names/record concepts and verify current effects:

```text
rg -n -i 'task.provenance|task.source|project.relation|task.identity|plan.local|no other task|cycle names its record|unique.*plan|WAY-153@|project-plan-state-evidence|plan.state.reader|state.reader' foundations/decisions.md foundations/invariants.md foundations/glossary.md foundations/environment_facts.md foundations/part_map.md
rg -n 'WAY-153@|project-plan-state-evidence' foundations
```

An intervening generic source/record search produced truncated broad output; it was not treated as a negative result or as complete evidence. The narrowed expanded query above was rerun and read without truncation. Positive controls are WAY-147's cycle-name sentence, WAY-153's reader and the evidence invariant/map detection.

Whole-entry findings and disposition:

- WAY-147: only plan-local name uniqueness; retain its entire entry and fingerprint. The correction identifies a current plan's task without renaming it or extending its uniqueness scope.
- WAY-153: revise only the binding paragraph to state identity and conservative unknown/contradictory provenance. Verification, rationale, rejected options, relations and approval marker remain unchanged.
- Existing incoming WAY-153 links: exactly project-plan-state-evidence/1 and project-plan-state-subprocesses/1. The evidence sentence gains the identity condition. The subprocess sentence still constrains only programs started by the reader and remains byte-identical; review against the full amended decision confirms that identity does not change its Git-only meaning. Renew both relation fingerprints.
- Map project-level failure mode already says the reader can propose progress without required cycle evidence or after an incomplete observation and names project-plan-state-evidence. Identity is part of required evidence, so that detection remains correct. Its responsibility, trust-boundary ownership and CLI surface's evidence/unchecked-output promise also already cover the correction. No map edit is needed, and no new argument, promise level or record format is introduced.
- No glossary or environment-fact entry defines task provenance/identity or imposes an alternative matching policy. Recorded provenance uses the existing process source fields and ordinary meaning; no new technical term or outside fact is needed. No additional decision fingerprint reference or unlinked conflicting rule was found.
- Existing no-write, Git-only, complete-original-source checks, human reconciliation and archive/task-name contracts remain applicable. The correction is not a new permission to execute record content or read arbitrary instruction paths.

This is the additional WAY-33 initial search for the assessment settlement. Root still owns the later final search against the then-current integration tip and the settlement record of the one assessment. Neither is falsely claimed here.

## Fingerprints and exact wording

WAY-153 binding fingerprint: `33b10f25` → `9874911d`. Both incoming invariant links now carry `9874911d`. Evidence invariant sentence fingerprints: `955ef508` → `d7b8cc0b`. Subprocess invariant sentence and its current citation/version do not change. No dependent decision relation to WAY-153 exists in the current foundation. Only the evidence sentence and both incoming links change in invariants.md.

Old WAY-153 binding paragraph:

```markdown
At each leading session's start a Git-only state reader proposes, with exact evidence, ready for
cycle to in cycle from a matching working cycle directory in a Git-listed worktree or a commit
touching the task's exact archived cycle directory, and in cycle to done from a cycle-record
commit reachable in the product's freshly fetched integration history, composing both
transitions when the plan is still ready for cycle. The reader changes no plan or task document,
establishes the product's integration ref without guessing, and exposes absent or incomplete
evidence, operational failures and conflicting traces without inferring completion. The project
orchestrator applies supported transitions with a reason and evidence in the plan's log,
resolves outcomes Git cannot establish through the product's chosen PR tool or asks the human
when that tool is absent, and brings a closed-unmerged PR or a trace conflicting with the plan
to the human without automatically correcting the plan.
```

Complete current WAY-153:

```markdown
### WAY-153/1 — What evidence supports a task state in a project plan?

At each leading session's start a Git-only state reader uses existing recorded task provenance
to establish that cycle traces belong to the current plan's task and proposes, with exact
evidence, ready for cycle to in cycle from such a matching working cycle directory in a
Git-listed worktree or a commit touching that task's exact archived cycle directory, and in
cycle to done from such a cycle-record commit reachable in the product's freshly fetched
integration history, composing both transitions when the plan is still ready for cycle. The
reader changes no plan or task document, establishes the product's integration ref without
guessing, and exposes absent or incomplete evidence, operational failures and conflicting traces
without unsupported progress; missing or ambiguous task provenance is unchecked and contradictory
task provenance goes to human reconciliation, with neither supplying progress. The project
orchestrator applies supported transitions with a reason and evidence in the plan's log,
resolves outcomes Git cannot establish through the product's chosen PR tool or asks the human
when that tool is absent, and brings a closed-unmerged PR or a trace conflicting with the plan
to the human without automatically correcting the plan.

- **Change:** new decision
- **Scope:** project-level
- **Based on:** none
- **Relations:** derives from WAY-38@6e10c3fd · derives from WAY-142@e53cd0ac · derives from
  WAY-147@8cfe543f
- **Verification:** level 1 — invariants: project-plan-state-evidence ·
  project-plan-state-subprocesses. Level 2 for applying proposals and resolving PR outcomes —
  an agent compares the evidence and leading session with the decision:
  - complies: the project orchestrator applies supported transitions with a reason and evidence
    in the plan's log, resolves an unchecked PR outcome through the product's chosen PR tool,
    and shows a closed-unmerged PR to the human without automatic correction;
  - violates: the project orchestrator treats an unchecked observation as completion without
    resolving it, silently normalizes a conflicting trace, or guesses the PR outcome when the
    product's PR tool is absent instead of asking the human.
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, merge of <request link>

*Rationale:* evidence-backed progress prevents a stale plan from hiding delivered work without letting
an uncertain observation claim delivery. Separating observation from the plan write keeps the
human-facing judgment visible; unresolved host outcomes cost a lookup or a question.
*Rejected:* a state reader that also queries the PR host — it couples observation to a host-specific
executable; inferring completion from a local trace — unfinished or abandoned work looks delivered;
automatically normalizing conflicts — a plausible state hides the discrepancy the human needs.
```

Old evidence sentence:

```markdown
For each task of a valid handed-over plan with an approved definition, the plan-state reader
proposes ready for cycle to in cycle only from a matching working-cycle directory in a Git-listed
worktree or a commit touching that task's exact archived cycle directory, proposes in cycle to
done only from a cycle-record commit reachable in freshly fetched product integration history,
reports both transitions together when both proofs hold for a ready task, and exposes incomplete,
failed or conflicting observations without unsupported progress or edits to the plan or task
documents.
```

Complete current evidence entry:

```markdown
## project-plan-state-evidence/1

For each task of a valid handed-over plan with an approved definition, the plan-state reader uses
existing recorded task provenance to establish that cycle traces belong to the current plan's
task before proposing ready for cycle to in cycle only from a matching working-cycle directory
in a Git-listed worktree or a commit touching that task's exact archived cycle directory or in
cycle to done only from a cycle-record commit reachable in freshly fetched product integration
history, reports both transitions together when both proofs hold for a ready task, reports
missing or ambiguous task provenance as unchecked and contradictory task provenance for human
reconciliation without proposing progress from either, and exposes incomplete, failed or
conflicting observations without unsupported progress or edits to the plan or task documents.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@9874911d
- **Part:** project-level
- **Correction:** none
```

## Checks and pending stage boundary

- Decision guard: `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`, exit 0, 0 errors, 14 warnings, 5 unchecked. Full output: reports/assessment-identity-guard-decisions.txt. Warnings are the nine pending request-link placeholders and five pre-existing overdue reviews WAY-03, 21, 52, 55 and 69. Five none-option unchecked results concern base log/version preservation, base template versioning and merge TODO/version copies/relation fingerprints; none is cleared or misreported.
- Invariant guard: `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`, exit 0, 0 errors, 0 warnings, 3 unchecked. Full output: reports/assessment-identity-guard-invariants.txt. Three none-option unchecked results concern base identifiers/versions/corrections/violations, merge TODO and merge fingerprints. No human_verdicts.md exists, so no human verdict is asserted.
- `git diff --check`: exit 0. Inspected diff: only the WAY-153 binding paragraph, evidence sentence and two WAY-153 fingerprints. No part-map clarification was necessary and no unrelated changes were staged.
- No broad test suite was repeated at this boundary, as authorized in the focused handoff. Current code and protected positive fixtures predate the revised identity condition; no pass of the revised invariant is claimed. Independent check correction and actual initial mismatch, reader correction, affected review and clean verification are subsequent work.

Isolated observable handoff: reports/identity-check-contract.md. It carries the final entry/Method, existing input/output boundary, source-format paths and positive/negative fixture semantics, without the production algorithm or this report's defense. It retains previous freshness/readiness/conflict/document-preservation obligations, filename-independent positive provenance and distinct-plan/missing/ambiguous/foreign-live/foreign-archive cases.

Cost of leaving the gap is unsupported done for an unstarted same-named task. Cost of correction is existing-provenance association and independent evidence-check changes plus the required reruns; product-wide renaming or new metadata would add migration cost and is not authorized. No irreducible human-reserved choice or unresolved source question was found. Root owns later code/check author dispatch, the one-assessment settlement record, affected review and both final deliberate breaks. Stop at the committed foundation boundary.
