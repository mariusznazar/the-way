---
name: implement-task
description: Use to take one ready the-way task through autonomous design, planning, implementation, testing, review and a pull or merge request, or to apply review corrections to its open request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
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
   controls the sources: independent tasks need no project; plan members require the exact approved
   plan item, dependencies and assignments; source-only tasks use relevant approved project
   settlements without importing plan work. Recheck approval and current foundation versions before
   starting. If a source changed, reconcile the task against it and record the effect; stop only
   when its required outcome can no longer be established.
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

The cycle writes only in the task's worktree. A preference or correction reaching beyond the
task — the-way, the user's agent instructions, another repository — goes into the request as a
proposal; the cycle changes nothing outside the product repository. The one exception: in the
task's source entry in the backlog the product names (WAY-107), the cycle may add the request link
and set the task's state.

## Start and record

4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. Calculate the three sharpness inputs: criticality from
   the touched parts (unknown failure modes count as highest), whether touched files are trust
   boundaries, and whether any operation cannot be undone. Use the full subagent review loop even
   for low criticality. For a trust boundary, add adversarial input checks under WAY-48. Stage but
   do not execute an irreversible operation before the human decides on it at the request. Treat a
   security-sensitive or external side effect the same way when the product's rules reserve its
   authorization to a human; prepare what can be reviewed and mark the request blocked if that
   action is necessary to finish the task. Create a new task branch from the current target branch,
   never reuse a branch already checked out except in a correction after review, and name it under
   the product's git rules; use an isolated worktree when its instructions and tools allow it. Never
   overwrite another worker's changes or let two writing agents edit the same worktree concurrently.
   Record the base commit and any failing checks already present. Keep a frozen copy of the task
   document in the cycle record, with its original path and source commit or approval date.
5. Create an ignored working record at `.runs/task-cycles/<task-slug>/cycle.md` using
   `task-cycle/record_template.md` from the pinned the-way checkout. Put full agent handoffs,
   prompts, reports and ledgers beside it in `reports/`, with secrets and personal data removed.
   Never copy diffs or files that git holds; name the commits instead. The one diff the record
   keeps is the manifest's diff of changes made after the panel (step 11).
   Append each event before the next dependent dispatch so another session can resume from the
   worktree and commits. Record the actor and model, inputs, skill, output path, result, command
   and exit code where relevant, time and cost when available.
   Record every question, answer, micro decision, rejected option and its cost if wrong. Link
   to the code, test, spec, plan or review finding that used the decision. Do not record hidden
   reasoning or raw secret-bearing output. Keep this record and its reports out of commits and
   assessment packages until the panel and independent code reviews finish.

For every dispatch, pass the user's delegation to the orchestrator, the applicable binding
sources, the agent's exact stage boundary, the write boundary, and the path for its full report.
The agent sends questions back to you and returns at that boundary, without invoking the next
Superpowers skill or seeking direct human approval. Answer workflow approval prompts
provisionally with evidence; only a human can approve a binding foundation entry. This adapter
changes the handoff and approval points, not the borrowed method's work within each stage.

## Design and plan

6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. Ask it to use Superpowers `brainstorming`. It
   classifies the task using that skill, then follows its architectural path because this cycle
   requires a written spec and plan for every ready task. Record the classification and this
   cycle-specific choice. The agent returns questions to you and writes its design and spec as
   `spec.md` in the working cycle record, in place of the skill's default location; the spec
   leaves with the record (step 12). Its boundary is the reviewed spec: it
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
8. Dispatch a fresh planner to use Superpowers `writing-plans` on the reviewed spec. It writes the
   plan as `plan.md` in the working cycle record, in place of the skill's default location. Its
   boundary is the finished plan: it returns before execution. Answer its questions in the same
   way. Review the plan for full task coverage, source fidelity, dependency order, tests and
   commands that can actually run. Record a provisional go-ahead for execution.
   Keep the spec and plan as separate artifacts so later iterations can compare them with results.

## Execute, verify and review

Before dependent implementation, run the foundation step required by WAY-01 and WAY-03 whenever the
task changes a foundation entry or an invariant test, or its code makes true a projected entry of
its sources (WAY-126). Invoke the pinned element skills for the affected entries and check existing
approval of projected wording. Write a projected entry the task marks whole, with *Approved by*
transcribed from the definition's gate record; a plan member writes only the entries its plan item
assigns, and one assigned to another item returns to the plan through a blocked draft request. Carry
a part of a projected entry to the request as a proposal while the code proceeds; a deferred *Review
when* goes to the request under *To decide* with a proposed value. Search the whole foundation and
run the applicable guards and panel. Keep unapproved wording as a proposal outside the binding
files; where the foundation requires a human's acceptance before the dependent code and that
authority is missing, prepare the blocked draft request. For invariant checks, use different agents
for the sentence, check and deliberate break under WAY-69, withhold the check and its inputs from
the break author, and record their identities and inputs for human assessment. Establish the
required acceptance before the dependent code proceeds; accepted invariant tests are read-only
during implementation. If later work needs one changed, return to this foundation step before
continuing that work.

9. Use Superpowers `subagent-driven-development`: fresh implementer and reviewer contexts for
   each meaningful plan task, followed by a whole-branch review. Its boundary is the final review
   and fixes: it returns before workspace cleanup and `finishing-a-development-branch`. Copy its
   ledger and full reports into the working cycle record before allowing cleanup, recording
   review ranges as commit ranges rather than copies of their diffs. Have implementers use
   `test-driven-development` for behavior changes. An implementation agent never approves its
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
11. Perform the return step of WAY-11 on the real diff and the cycle's choice log: identify newly
    learned decisions, rules, uncovered behavior, environment facts, terms and part-map changes;
    compare touched parts of the foundation with code. Every autonomous choice whose cost of being
    wrong reaches beyond this request becomes a foundation proposal when it still binds after the
    merge (WAY-36), and a question under *To decide* otherwise. Read the projected entries of the
    task's sources: one the code makes true that the foundation step did not write sends the task
    back to that step, or, for a plan member and an entry assigned to another item, back to the
    plan. For a projected invariant found this way, set aside the code it covers, have agents that
    have not seen that code write the invariant and its test, then redo the code against the
    accepted test. Propose a new entry only for a rule none of them states (WAY-126). Prepare the
    required foundation proposals in the working record as one current version: a proposed
    foundation diff against a named commit, explicitly marked unapproved, with its translation
    beside it in the task document's language for the human (WAY-114) and the commits that hold
    the relevant code evidence. Write a binding foundation change only where prior human approval
    authorizes its content; otherwise keep it proposed.
    Send return-step proposals to the panel as foundation changes even when no binding
    foundation file has changed (WAY-11), then carry the proposal and panel result to the
    request.
    For actual foundation or invariant-test changes, run their guards and the panel on the final
    change. Filter the assessment diff and supplied file set to code, foundation and proposed
    entries: exclude spec, plan, frozen task, chronology, reports, prompts and author reasoning,
    including those in earlier commits or later reassessments. Record the assessed range by commit
    hashes and its file list in the record's manifest, plus a diff only of changes made after
    the panel; commit the chronology only after the panel. If a panel fix changes code, rerun
    affected checks and code review. Do not invent `Approved by` for a decision awaiting the
    human. A contradiction with a current decision follows WAY-30; a collision without recorded
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
    copies, commit them after the assessed change and commit their removal immediately after, so
    the request's changed files show only the change and the target branch's files never hold
    the record; the panel record lives there under the task cycle, as `elements/common/panel.md`
    specifies. Link the record by the SHA of the commit that adds it, never by branch name. The
    link survives only if the request is merged with its commits kept; where the product's rules
    squash or rebase on merge, name that as a limitation in the request.
    Use Superpowers `finishing-a-development-branch` for verification and request preparation,
    then take the pull or merge request route already chosen by the user, without presenting its
    integration menu. Do not merge. Keep the worktree for review changes.
13. The request contains: task goal and relation, source versions, design and plan links, what
    changed and why, test and review evidence, a summary of the decisions the cycle took, known
    limitations, and a *To decide* section. *To decide* holds what the human settles at the request,
    each with its exact question and cost if wrong: foundation proposals awaiting approval,
    autonomous choices whose cost of being wrong reaches beyond this request, values left to the
    human, and proposals for the-way or the user's instructions. For the other choices, give their
    number and a link to the choice log. Link the cycle record and full reports by the SHA of the
    record commit. If the task was impossible, mark the request `blocked`, show the smallest missing
    fact or authorization and the attempted alternatives; do not present partial work as complete.
14. Before reporting completion, confirm the record lists all dispatches, choices, rulings,
    checks, fixes and skipped stages. The final report lists any write to the task's backlog
    entry. The request is the human's first decision point.

## Correction after review

Take a link to the request, or to a comment holding review remarks, as the input. Work on that
request's branch and in its worktree; this is the one case in which the cycle does not create a new
branch. First merge, never rebase, the current target branch, the the-way pin included, and verify
that the pinned checkout matches the product's gitlink. Treat the remarks as binding input, recorded
as new events in the working record. Repeat only the stages the remarks touch, with their reviews,
checks and return step, and then the record's pair of commits from step 12. Update the request's
description, including its record links and the choices and proposals the corrections changed.
