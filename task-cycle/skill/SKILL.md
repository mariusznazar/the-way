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
3. Require subagents and Superpowers version 6.4.1 with `brainstorming`, `writing-plans`,
   `subagent-driven-development`, `test-driven-development`, `requesting-code-review`, and
   `finishing-a-development-branch`. Verify the installed version before dispatching. Read each
   skill and its linked files when its stage begins. WAY-125 names the borrowed methods and the
   the-way adapter's stage boundaries; those boundaries govern
   handoffs and human contact. Do not silently use another version or substitute another method.
   If this version or a subagent capability is unavailable, this cycle cannot run in that harness.

## Start and record

4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. Calculate the three sharpness inputs: criticality from the touched parts
   (unknown failure modes count as highest), whether touched files are trust boundaries, and
   whether any operation cannot be undone. Use the full subagent review loop even for low
   criticality. For a trust boundary, add adversarial input checks under WAY-48. Stage but do not
   execute an irreversible operation before the human decides on it at the request. Treat a
   security-sensitive or external side effect the same way when the product's rules reserve its
   authorization to a human; prepare what can be reviewed and mark the request blocked if that
   action is necessary to finish the task. Select the task branch under the product's git rules;
   use an isolated worktree when its instructions and tools allow it. Never overwrite another
   worker's changes or let two writing agents edit the same worktree concurrently. Record the
   base commit and any failing checks already present. Keep a frozen copy of the task
   document on the task branch, with its original path and source commit or approval date.
5. Create an ignored working record at `.runs/task-cycles/<task-slug>/cycle.md` using
   `task-cycle/record_template.md` from the pinned the-way checkout. Put full agent handoffs,
   prompts, reports and ledgers beside it in `reports/`, with secrets and personal data removed.
   Append each event before the next dependent dispatch so another session can resume from the
   worktree and commits. Record the actor and model, inputs, skill, output path, result, command
   and exit code where relevant, time and cost when available.
   Record every question, answer, micro decision, rejected option and its cost if wrong. Link
   to the code, test, spec, plan or review finding that used the decision. Do not record hidden
   reasoning or raw secret-bearing output. Keep this record and its reports out of commits and
   assessment packages until the panel and independent code reviews finish.

For every dispatch, pass the user's delegation to the orchestrator, the applicable binding
sources, the agent's exact stage boundary, and the path for its full report. The agent sends
questions back to you and returns at that boundary, without invoking the next Superpowers skill
or seeking direct human approval. Answer workflow approval prompts provisionally with evidence;
only a human can approve a binding foundation entry. This adapter changes the handoff and approval
points, not the borrowed method's work within each stage.

## Design and plan

6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. Ask it to use Superpowers `brainstorming`. It
   classifies the task using that skill, then follows its architectural path because this cycle
   requires a written spec and plan for every ready task. Record the classification and this
   cycle-specific choice. The agent returns questions to you and writes its design and spec under
   the product's `docs/superpowers/specs/` convention. Its boundary is the reviewed spec: it
   returns before invoking `writing-plans`. Answer each question from an approved source where
   possible. Otherwise choose the smallest reversible
   interpretation that fulfills the task, note alternatives and the price of being wrong, and
   mark it as an autonomous choice for the request review. Do not silently expand task scope.
   Where the skill expects a human design or spec approval, give an explicitly provisional
   orchestrator go-ahead under the user's delegation; preserve the approval request for the PR.
7. Have an agent other than the designer review the spec against the frozen task and current
   foundation. Resolve missing requirements, invented behavior and contradictions before moving
   on. A spec may describe a proposed foundation change, but a decision or invariant that
   requires human approval remains proposed until the request is reviewed.
8. Dispatch a fresh planner to use Superpowers `writing-plans` on the reviewed spec. Its boundary
   is the finished plan: it returns before execution. Answer its questions in the same way. Review
   the plan for full task coverage, source fidelity, dependency order, tests and commands that can
   actually run. Record a provisional go-ahead for execution.
   Keep the spec and plan as separate artifacts so later iterations can compare them with results.

## Execute, verify and review

Before dependent implementation, run the foundation step required by WAY-01 and WAY-03 whenever
the task changes a foundation entry or an invariant test. Invoke the pinned element skills for
the affected entries, check existing approval of projected wording, search the whole foundation,
and run the applicable guards and panel. Keep unapproved wording as a proposal outside the binding
files; if the necessary change lacks the human authority required by the foundation, prepare the
blocked draft request. For invariant checks, use different agents for the sentence, check and
deliberate break under WAY-69, withhold the check and its inputs from the break author, and record
their identities and inputs for human assessment. Establish the required acceptance before the
dependent code proceeds; accepted invariant tests are read-only during implementation. If later
work needs one changed, return to this foundation step before continuing that work.

9. Use Superpowers `subagent-driven-development`: fresh implementer and reviewer contexts for
   each meaningful plan task, followed by a whole-branch review. Its boundary is the final review
   and fixes: it returns before workspace cleanup and `finishing-a-development-branch`. Copy its
   ledger and full reports into the working cycle record before allowing cleanup. Have implementers
   use `test-driven-development` for behavior changes. An implementation agent never approves its
   own review. Questions from any agent return to you,
   with their answers entered in the cycle record before work continues.
10. After each implementation unit, run its focused checks, review its diff and resolve findings.
    Recalculate the WAY-13 sharpness inputs from the completed diff; if they grew, add the
    resulting checks before review, never reduce those already run. Run the product's full
    required gate on the completed change. For visible behavior, verify it in the running
    product as well. Use Superpowers `requesting-code-review` for a fresh final review, or the
    final review already required by the selected execution skill; do not dispatch a duplicate
    reviewer for the same range. Record failed and unchecked results by name; never call an unrun
    check passed.
11. Perform the return step of WAY-11 on the real diff: identify newly learned decisions, rules,
    uncovered behavior, environment facts, terms and part-map changes; compare touched parts of
    the foundation with code. Prepare each required foundation proposal in the working record.
    Write a binding foundation change only where prior human approval authorizes its content;
    otherwise keep it proposed. Send return-step proposals to the panel as foundation changes
    even when no binding foundation file has changed (WAY-11), then carry the proposal and panel
    result to the request. Prepare a separate proposed foundation diff against a named commit,
    explicitly marked unapproved, plus the relevant code evidence; exclude the working record.
    For actual foundation or invariant-test changes, run their guards and the panel on the final
    change. Filter the assessment diff and supplied file set to code, foundation and proposed
    entries: exclude spec, plan, frozen task, chronology, reports, prompts and author reasoning,
    including those in earlier commits or later reassessments. Record the assessed range and file
    list; commit the chronology only after the panel. If a panel fix changes code, rerun affected checks
    and code review. Do not invent `Approved by` for a decision awaiting the human. A
    contradiction with a current decision follows WAY-30; a collision without recorded
    precedence follows WAY-25.
    If those rules prevent the required code, report the task as blocked in a draft request.

## Request and handoff

12. Recheck the branch against the current target branch, rerun checks affected by that update,
    and inspect the final diff. If reconciliation changes the assessed code, foundation or its
    applicable sources, invalidate the affected reviews: repeat the foundation collision search,
    affected code review and panel before proceeding. Record the final assessed commits and file
    sets so the request never presents an assessment of superseded work as current.
    Copy the sanitized working record and full reports to
    `docs/task-cycles/<task-slug>/` on the task branch, rewrite their links to the committed
    copies, and commit them after the assessed change;
    the panel record lives there under the task cycle, as `elements/common/panel.md` specifies.
    Use Superpowers `finishing-a-development-branch` for verification and request preparation,
    then take the pull or merge request route already chosen by the user, without presenting its
    integration menu. Do not merge. Keep the worktree for review changes.
13. The request contains: task goal and relation, source versions, design and plan links, what
    changed and why, test and review evidence, every autonomous choice with its cost if wrong,
    foundation proposals awaiting approval, known limitations, and the exact questions on which
    human review is needed. Link the cycle record and full reports. If the task was impossible,
    mark the request `blocked`, show the smallest missing fact or authorization and the attempted
    alternatives; do not present partial work as complete.
14. Before reporting completion, confirm the record lists all dispatches, choices, rulings,
    checks, fixes and skipped stages. The request is the human's first decision point. Corrections
    from review become new record events and revisions on the same task branch.
