# Focused return-step answer — Git-only reader

Verdict: a narrower derived invariant is required. The current foundation does not protect this reader's Git-only restriction with an applicable invariant, although its ordinary test demonstrates that the restriction is mechanically checkable. My earlier classification of that restriction as level 2 was incorrect under WAY-12 and WAY-22. This is completeness of the existing accepted rule, not a new choice or permission to relax it.

Reviewed revision: ea9a23e93958aa3e579d1846177b1d32c1d739e4, confirmed by `git rev-parse HEAD`. Read the complete question handoff, WAY-12, WAY-22, WAY-38, WAY-153, script-subprocesses/1 and project-plan-state-evidence/1, and inspected the reader's subprocess boundary and ordinary test. This report is the only file written; no foundation, code, check, source or commit changed and no child agent was started.

## Source evidence and boundary

1. Frozen task `.runs/task-cycles/lead-project/task.md:32` says “skrypt uruchamia tylko gita”; accepted settlement 2 at line 132 repeats “skrypt odczytu stanu używa tylko gita”. WAY-153's first binding sentence, `foundations/decisions.md:4772`, consequently calls it a “Git-only state reader”. The restriction is already accepted.
2. WAY-12, complete entry beginning `foundations/decisions.md:384`, requires derived invariants when one can be stated today; its violating example specifically rejects leaving a lint-enforceable rule at level 2. WAY-22, complete entry beginning line 645, says “what of it a commit can make false is written as an invariant derived from it”. A reader revision starting a non-Git executable makes this restriction false on that commit. No uncertain agent-conduct measurement is needed to state that property.
3. WAY-38 permits Git and product-declared commands. Its `script-subprocesses/1` derivative at `foundations/invariants.md:567` says: “No script git tracks starts a program other than git or a command the product declares in its repository.” Its Method is `TODO`. Thus it is both broader than the reader rule and currently without a runnable check; adding a product-declared non-Git command to the reader could satisfy this invariant while violating the task and WAY-153. Changing the global invariant would wrongly remove the allowance other scripts retain.
4. `project-plan-state-evidence/1`, complete entry at `foundations/invariants.md:2105`, constrains evidence, composed transitions, conservative observations and document preservation. It names no program restriction. Its Method runs the project-level directory. That command running ordinary tests does not silently extend the invariant's sentence or assign a verdict for a second property: checks cite the property they establish, and this sentence can stay true while a non-Git subprocess is added without changing its output.
5. The actual implementation at `project-level/plan_state.py:44` passes `git` as the first argument of `subprocess.run`. The ordinary test `project-level/test_plan_state.py:332`, read in full, observes subprocess calls and asserts their first executable is `git` at line 339. This establishes a concrete available observation boundary, not proof that every future execution path is covered. Its lack of an invariant citation means it is ordinary-test coverage, not the missing foundation invariant. A separately authored invariant check can enforce the narrower property without using that author's test as its own expected answer.

Search of `foundations/invariants.md` and `foundations/decisions.md` for `subprocess|Git-only|other than git|starts a program|only git` found the broad invariant and WAY-38/WAY-153, with no narrower existing invariant. The query also hit the explicit frozen-task authority. The positive controls were the actual script-subprocesses sentence and WAY-153 Git-only wording. No broader rule or the evidence invariant supplies the omitted restriction by implication.

## Smallest compliant correction, proposed only

Add one separate invariant. Extending the evidence sentence would combine two independently changeable properties and unnecessarily change its existing check contract. The new invariant's exact proposed sentence is:

> Every subprocess the plan-state reader starts runs Git.

The sentence concerns programs started by the reader itself, the same subprocess boundary used by script-subprocesses; it does not assert that Git itself starts no transport, helper or other program. It introduces no extra shell, timeout or process-tree restriction beyond the accepted Git-only policy.

Full proposed entry:

```markdown
## project-plan-state-subprocesses/1

Every subprocess the plan-state reader starts runs Git.

- **Method:** `python -B gate/run_tests.py project-level --record .runs/project-plan-state-subprocesses.jsonl`
- **Rests on:** none
- **Derives from:** WAY-153@33b10f25
- **Part:** project-level
- **Correction:** none
```

The subject and scope are the reader owned by project-level, rather than all scripts. The sentence is about the program's behavior, so controlled calls/repositories are an appropriate method; it is not a sentence about an actual private product's completion. No new outside fact is assumed. The directory method already exists; a separately authored check still has to cite this identifier and produce its own verdict, and the method passing without that verdict is not a pass for the new invariant.

Replace the complete Verification field of WAY-153 with:

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

This leaves WAY-153's binding wording and fingerprint `33b10f25` unchanged, as well as the existing evidence invariant and its check. WAY-38 and script-subprocesses remain unchanged. The independently authored new check, subsequent code review and deliberate-break acceptance are still required under WAY-69 and the return-step ordering of WAY-149; existing ordinary tests do not replace them. The root can use this sentence as the sentence author's contribution while dispatching the check to another agent, keeping the code author separate. No check implementation or mutation is proposed in this report.

## Costs and limits

Leaving the gap allows a later reader to start a product-declared non-Git executable while satisfying the broad foundation invariant; the narrower task rule would remain protected only by ordinary tests and semantic review. Correcting it adds one small invariant entry, independently authored check and its deliberate-break acceptance, followed by the affected guards and review. That cost is required by the existing decision-verification rule and preserves the global command allowance for other scripts.

No tests or guards were run for this focused read-only judgment; no run is claimed as proof of the proposed invariant. This report does not perform the return-step foundation search, final independent assessment or deliberate break. Pending source choice: none. Recommendation: add the separate invariant and revise Verification exactly as above through the remaining return-step foundation/check route.
