---
name: implement-task
description: Use to take one ready the-way task through autonomous design, planning, implementation, testing, review and a pull or merge request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
---

# Implement one task

Drive one task from `ready for cycle` to a reviewable pull or merge request. You are the
orchestrator: invoke the installed Superpowers skills and delegate their work to fresh agents;
do not reproduce those skills here. Answer their workflow questions from the task, its stated
sources, the product's current foundation and code. Keep every answer and its evidence in the
cycle record. The person who requested this cycle has delegated intermediate choices to you;
never label your answer as that person's approval.

The cycle has one ordinary human contact: the pull or merge request. Do not pause for design,
spec, plan, implementation or review questions. Stop early only when the required outcome cannot
be implemented under the available evidence, capabilities and binding rules. A slow step, a
failed test, a reviewer finding or an ambiguous implementation method is work to resolve, not a
reason to ask the human. If a binding rule reserves a decision to a human and code cannot proceed
without it, prepare a blocked draft request with the evidence and stop; do not pretend that your
choice approved or changed the rule.

## Inputs and authority

1. Read the task document in full. Require `Status: ready for cycle`. Its `Project relation:`
   controls the sources: independent tasks need no project; plan members require the exact
   approved plan item, dependencies and assignments; source-only tasks use relevant approved
   project settlements without importing plan work. Recheck approval and current foundation
   versions before starting. If a source changed, reconcile the task against it and record the
   effect; stop only when its required outcome can no longer be established.
2. Read the product's `AGENTS.md`, process pin, foundation and relevant code. Verify that the
   pinned the-way checkout matches the product's gitlink. Follow product-specific git and test
   rules. Search the current foundation for additional applicable entries or collisions; the
   task document is a starting map, not proof that nothing else applies.
3. Verify that subagents and these installed Superpowers skills are available in this harness:
   `brainstorming`, `writing-plans`, `subagent-driven-development` or `executing-plans`,
   `test-driven-development`, `requesting-code-review`, and
   `finishing-a-development-branch`. Read each skill when its stage begins, including files it
   points to. Use the installed version; this skill does not vendor or override their methods.
   If a required capability is unavailable, first seek an equivalent installed route that
   preserves its required result and independent review; record the substitution. If none exists,
   the cycle cannot start.

## Start and record

4. Take a branch from the product's current main branch and an isolated worktree when the
   product's instructions and tools allow it. Never overwrite another worker's changes or let
   two writing agents edit the same worktree concurrently. Record
   the base commit and any failing checks already present. Keep a frozen copy of the task
   document on the task branch, with its original path and source commit or approval date.
5. Create `docs/task-cycles/<task-slug>/cycle.md` using `task-cycle/record_template.md` from the
   pinned the-way checkout. Put full agent handoffs and reports beside it in `reports/`, with
   secrets and personal data removed. Append each event before the next dependent dispatch so
   another session can resume from files and commits. Record the actor and model, inputs, skill,
   output path, result, command and exit code where relevant, time and cost when available.
   Record every question, answer, micro decision, rejected option and its cost if wrong. Link
   to the code, test, spec, plan or review finding that used the decision. Do not record hidden
   reasoning or raw secret-bearing output.

## Design and plan

6. Dispatch a fresh design agent with the frozen task, applicable source paths and the pinned
   foundation. Ask it to use Superpowers `brainstorming`. It returns questions to you and writes
   its design and spec under the product's `docs/superpowers/specs/` convention. Answer each
   question from an approved source where possible. Otherwise choose the smallest reversible
   interpretation that fulfills the task, note alternatives and the price of being wrong, and
   mark it as an autonomous choice for the request review. Do not silently expand task scope.
   Where the skill expects a human design or spec approval, give an explicitly provisional
   orchestrator go-ahead under the user's delegation; preserve the approval request for the PR.
7. Have an agent other than the designer review the spec against the frozen task and current
   foundation. Resolve missing requirements, invented behavior and contradictions before moving
   on. A spec may describe a proposed foundation change, but a decision or invariant that
   requires human approval remains proposed until the request is reviewed.
8. Dispatch a fresh planner to use Superpowers `writing-plans` on the reviewed spec. Answer its
   questions in the same way. Review the plan for full task coverage, source fidelity, dependency
   order, tests and commands that can actually run. Record a provisional go-ahead for execution.
   Keep the spec and plan as separate artifacts so later iterations can compare them with results.

## Execute, verify and review

9. Prefer Superpowers `subagent-driven-development`: fresh implementer and reviewer contexts for
   each meaningful plan task, followed by a whole-branch review. Use `executing-plans` only if
   subagent-driven execution cannot fit the plan and the reason is recorded; retain an independent
   final reviewer. Have implementers use `test-driven-development` for behavior changes. An
   implementation agent never approves its own review. Questions from any agent return to you,
   with their answers entered in the cycle record before work continues.
10. After each implementation unit, run its focused checks, review its diff and resolve findings.
    Run the product's full required gate on the completed change. For visible behavior, verify it
    in the running product as well. Use Superpowers `requesting-code-review` for a fresh final
    review, or the final review already required by the selected execution skill; do not dispatch
    a duplicate reviewer for the same range. If the foundation or an invariant test changes, run
    the the-way panel and format guards required by the current foundation. Record failed and
    unchecked results by name; never call an unrun check passed.
11. Perform the return step of WAY-11 on the real diff: identify newly learned decisions, rules,
    uncovered behavior, environment facts, terms and part-map changes; compare touched parts of
    the foundation with code. Prepare each required foundation proposal and panel record on the
    branch. Do not invent `Approved by` for a decision awaiting the human. A contradiction with a
    current decision follows WAY-30; a collision without recorded precedence follows WAY-25.
    If those rules prevent the required code, report the task as blocked in a draft request.

## Request and handoff

12. Recheck the branch against the current target branch, rerun checks affected by that update,
    and inspect the final diff. Use Superpowers `finishing-a-development-branch` for its
    verification and request preparation, then take the pull or merge request route already
    chosen by the user. Do not merge. Keep the worktree for review changes.
13. The request contains: task goal and relation, source versions, design and plan links, what
    changed and why, test and review evidence, every autonomous choice with its cost if wrong,
    foundation proposals awaiting approval, known limitations, and the exact questions on which
    human review is needed. Link the cycle record and full reports. If the task was impossible,
    mark the request `blocked`, show the smallest missing fact or authorization and the attempted
    alternatives; do not present partial work as complete.
14. Before reporting completion, confirm the record lists all dispatches, choices, rulings,
    checks, fixes and skipped stages. The request is the human's first decision point. Corrections
    from review become new record events and revisions on the same task branch.
