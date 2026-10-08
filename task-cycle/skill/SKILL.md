---
name: implement-task
description: Use to take one ready the-way task to a reviewable pull or merge request — through autonomous design, planning, implementation, testing and review, or, for a small task that leaves the foundation unchanged, through one agent's implementation, the same checks and one review — or to apply review corrections to its open request. Requires subagents and the Superpowers skills named by this process. The human reviews the request, not intermediate steps.
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

The cycle writes only in the task's worktree and changes nothing outside the product repository. A
remark about the-way, the user's agent instructions or another repository goes into the cycle
record's process remarks, never into the request. The one exception: in the task's source entry in
the backlog the product names (WAY-107), the cycle may add the request link and set the task's
state.

## Start and record

4. Determine and record whether the task changes the foundation (WAY-13), which selects its
   foundation route before implementation. In the same analysis, choose the light or the full
   cycle as "Light cycle" below gives it, and record the choice with the reason for each finding
   you assessed; once one finding fails, the rest may be recorded as not assessed. Calculate the
   three sharpness inputs: criticality from the touched parts (unknown failure modes count as
   highest), whether touched files are trust boundaries, and whether any operation cannot be
   undone. On the full cycle, use the full subagent review loop even for low criticality. For a
   trust boundary, add adversarial input checks under WAY-48. Stage but
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
   Never copy diffs or files that git holds; name the commits instead.
   Append each event before the next dependent dispatch so another session can resume from the
   worktree and commits. Record the actor and model, inputs, skill, output path, result, command
   and exit code where relevant, time and cost when available.
   Record every question, answer, micro decision, rejected option and its cost if wrong. Link
   to the code, test, spec, plan or review finding that used the decision. Do not record hidden
   reasoning or raw secret-bearing output. Keep this record and its reports out of commits and
   assessment packages until the independent assessment and the code reviews finish.

For every dispatch, pass the user's delegation to the orchestrator, the applicable binding
sources, the agent's exact stage boundary, the write boundary, and the path for its full report.
The agent sends questions back to you and returns at that boundary, without invoking the next
Superpowers skill or seeking direct human approval. Answer workflow approval prompts
provisionally with evidence; a human accepts the foundation entries the cycle writes when merging
the request (WAY-114). This adapter changes the handoff and approval points, not the borrowed
method's work within each stage, except that the code review also writes the deliberate break of
an invariant's check (WAY-69).

## Light cycle

A task takes the light cycle when the analysis of step 4 finds all three: the task leaves the
foundation unchanged, so the foundation step below would not run for it; one agent can implement
it in about ten minutes; and its implementation needs neither very large files nor very many files
read into context. Every other task takes the full cycle — steps 6 to 9 — exactly as written. The
two cycles differ in how a change is prepared and made, never in the outcome the task has to reach
or the checks run on the finished change (WAY-13, WAY-125); both run inside the foundation route
of step 4. On the light cycle:

- Dispatch one fresh executor with the frozen task, the applicable source paths, the pinned
  foundation and the dispatch contract above. It makes the whole change from the task, without a
  spec or a plan, using Superpowers `test-driven-development` for behavior changes, and commits it.
  Its boundary is the committed change with its focused checks run; it returns before any review.
  It also returns, with its work committed, when the change touches the foundation and when the
  change outgrows a finding of step 4.
- When the change touches the foundation, rule on the touch and record the ruling. The touch is
  simple and obvious when the entry's change follows from the task's required outcome with no
  choice the task leaves open, changes the meaning of no approved decision, contradicts no current
  entry, and writes or changes no invariant or invariant test. On that ruling, record the
  foundation route as changed; the executor then writes the entry through its element's skill, as
  the foundation step below gives an entry the cycle writes, before it continues the code that
  depends on it, and the entry joins the one independent assessment of step 11. Any other touch
  switches the task to the full cycle.
- When the change is made, run step 10 in full. The whole change is its one implementation unit,
  and one Superpowers `requesting-code-review` of the whole change, with the frozen task as its
  requirements, is both that unit's review and the final review: the executor fixes its findings,
  the affected checks run again, and the same reviewer reviews the fix range once. Then continue
  with steps 11 to 14 as written. Where the harness cannot resume the executor after a ruling or
  for fixes, a fresh executor on the same branch, given the task and the ruling or the findings,
  continues in its place.

Switch to the full cycle when the executor, or you from its work, find while the change is being
made or its review findings fixed that it outgrows a finding of step 4 or touches the foundation in
a way that is not simple and obvious. The executor returns a report without code and without a
diff: why the change grew, which files and obstacles it found, and what proved not obvious. Check
that the report holds no code, keep it in `reports/`, and record the attempt's last commit, as a
historical name rather than a link to follow, and the names of the files it changed. Then discard
the attempt, its foundation entries included, by resetting the task branch to the recorded base
commit, record the switch with its reason, and continue at step 6, whose fresh design agent
receives the executor's report beside the frozen task.

## Design and plan

6. Dispatch a fresh design agent with the frozen task, applicable source paths, the pinned
   foundation and the dispatch contract above. After a switch from the light cycle, also give it
   the executor's report, as the findings of a discarded attempt. Ask it to use Superpowers
   `brainstorming`. It classifies the task using that skill, then follows its architectural path
   because the full cycle requires a written spec and plan for every task it runs. Record the
   classification and this
   cycle-specific choice. The agent returns questions to you and writes its design and spec as
   `spec.md` in the working cycle record, in place of the skill's default location; the spec
   leaves with the record (step 12). Its boundary is the reviewed spec: it
   returns before invoking `writing-plans`. Answer each question from an approved source where
   possible. Otherwise choose the smallest reversible
   interpretation that fulfills the task, note alternatives and the price of being wrong, and
   record it as an autonomous choice. Do not silently expand task scope.
   Where the skill expects a human design or spec approval, give an explicitly provisional
   orchestrator go-ahead under the user's delegation; preserve the approval request for the PR.
7. Have an agent other than the designer review the spec against the frozen task and current
   foundation. Resolve missing requirements, invented behavior and contradictions before moving
   on. A spec may name the foundation entries the task will write; the foundation step or the return
   step writes them.
8. Dispatch a fresh planner to use Superpowers `writing-plans` on the reviewed spec. It writes the
   plan as `plan.md` in the working cycle record, in place of the skill's default location. Its
   boundary is the finished plan: it returns before execution. Answer its questions in the same
   way. Review the plan for full task coverage, source fidelity, dependency order, tests and
   commands that can actually run. Record a provisional go-ahead for execution.
   Keep the spec and plan as separate artifacts so iterations can compare them with results.

## Execute, verify and review

Before dependent implementation, run the foundation step required by WAY-01 and WAY-03 whenever the
task changes a foundation entry or an invariant test, or its plan item assigns, or its code makes
true, a projected entry of its sources (WAY-126). Invoke the pinned element skills for the affected
entries and write each entry into `foundations/` on the task branch without waiting for the human;
keep, for the request, one sentence of its meaning in the task document's language (WAY-114). Write
a projected entry the task marks or its plan item assigns whole, with *Approved by* transcribed from
the definition's gate record; write a part of a projected entry, and every other new or changed
decision, with *Approved by* `<approver>, merge of <request link>` (WAY-14) — never a date, which
only the human's merge sets. A plan member writes only the entries its plan item assigns; one
assigned to another item returns to the plan through a blocked draft request. Set every *Review
when* yourself. Ask the human before the request only where you have no recommendation or an entry
would change the meaning of an approved decision, through a blocked draft request holding the
question. Search the whole foundation and run the applicable guards. An invariant's sentence, its
check and the code it covers come from three different agents (WAY-69): give the check's author the
sentence and its method, never the code's reasoning. Invariant tests written in this step are
read-only during implementation; if later work needs one changed, return to this foundation step
before continuing that work.

9. On the full cycle, use Superpowers `subagent-driven-development`: fresh implementer and
   reviewer contexts for each meaningful plan task, followed by a whole-branch review. Its
   boundary is the final review
   and fixes: it returns before workspace cleanup and `finishing-a-development-branch`. Copy its
   ledger and full reports into the working cycle record before allowing cleanup, recording
   review ranges as commit ranges rather than copies of their diffs. Have implementers use
   `test-driven-development` for behavior changes. An implementation agent never approves its
   own review. Questions from any agent return to you,
   with their answers entered in the cycle record before work continues.
10. After each implementation unit, run its focused checks, review its diff and resolve findings.
    Recalculate the WAY-13 sharpness inputs from the completed diff; if they grew, add the
    resulting checks before review, never reduce those already run. Run the product's full
    required gate on the completed change. The review of a change holding an invariant check writes
    the deliberate break from the invariant's sentence, runs the check on it and reports whether it
    fails (WAY-69, WAY-08). For visible behavior, verify it in the running
    product as well. Use Superpowers `requesting-code-review` for a fresh final review, or the
    final review already required by the selected execution skill; do not dispatch a duplicate
    reviewer for the same range. Record failed and unchecked results by name; never call an unrun
    check passed.
11. Perform the return step of WAY-11 on the real diff and the cycle's choice log: identify newly
    learned decisions, rules, uncovered behavior, environment facts, terms and part-map changes;
    compare touched parts of the foundation with code. Write every one that binds after the merge
    (WAY-36) into the foundation as the foundation step writes; every other choice stays one line in
    the choice table. Nothing is deferred: what this request does not write is neither proposed nor
    listed for later. Read the projected entries of the task's sources: write one the code makes
    true that the foundation step missed (WAY-126) — for an invariant, its check comes from an agent
    that did not write the code it covers and runs on that code; an entry assigned to another plan
    item returns to the plan. A check the return step writes then goes to a code reviewer that did
    not write it, which writes its deliberate break from the sentence, runs the check on it and
    reports whether it fails (WAY-69, WAY-08). Write a new entry only for a rule none of them
    states. Then have the
    change's foundation entries and invariant tests assessed once, following
    `elements/common/critique/SKILL.md` (WAY-10): one agent on a model other than the author's where
    available, given the diff and the files of the assessed commit filtered to code, foundation and
    invariant tests — never spec, plan, frozen task, chronology, reports, prompts or author
    reasoning. Settle each remark yourself and record how; a remark reaches the human only as the
    foundation step allows a question. If a settlement changes code, rerun the affected checks and
    code review. A settlement that changes the assessed foundation entries or invariant tests does
    not reopen the independent assessment: rerun the affected checks and the code review, whose
    reviewer writes the deliberate break again. A remark that cannot be settled without changing
    the meaning the task requires goes to the human as the foundation step allows a question.
    Record the assessed range by commit hashes and its file list. A contradiction with
    a current decision follows WAY-30; a collision without recorded precedence follows WAY-25. If
    those rules prevent the required code, report the task as blocked in a draft request.

## Request and handoff

12. Recheck the branch against the current target branch, rerun checks affected by that update,
    and inspect the final diff. If reconciliation changes the assessed code, foundation or its
    applicable sources, invalidate the affected reviews: repeat the foundation collision search,
    affected code review and independent assessment before proceeding. Record the final assessed
    commits and file sets so the request never presents an assessment of superseded work as
    current. Run the verification, then open the request as a draft by the pull or merge request
    route already chosen by the user, without presenting the integration menu of Superpowers
    `finishing-a-development-branch`. Replace `<request link>` in the *Approved by* of the entries
    this cycle wrote with the request's URL, commit and push; this is a placeholder swap that
    changes no other text, so it reopens neither the independent assessment nor the code reviews.
    Then copy the sanitized working record and full reports to `docs/task-cycles/<task-slug>/` on
    the task branch, rewrite their links to the committed copies, commit them, commit their removal
    immediately after, and push, so the request's changed files show only the change and the target
    branch's files never hold the record; the assessment record lives there under `reports/`. Then
    update the request's description with links to the record by the SHA of the commit that adds it,
    never by branch name. Ask in the request for a merge that keeps its commits, since the link
    survives only then; where the product's rules squash or rebase on merge, name that as a
    limitation in the request. Then mark the request ready for review, except a request the cycle
    marks `blocked`, which stays a draft. Do not merge. Keep the worktree for review changes.
13. The request contains: task goal and relation, source versions, the cycle taken and its
    reasons — after a switch, its reason and a link to the executor's report — design and plan
    links on the full cycle, what changed and why, test and review evidence with every check that
    did not run named, and *What
    this request settles*: each foundation entry the change writes or changes, as its identifier and
    one sentence of its meaning in the task document's language, projected entries apart from new
    ones. Beside them, what the foundation puts in front of the human at the merge: an invariant
    kept at its version under a correction, with its old and new sentence (WAY-57); a part whose
    computed criticality fell (WAY-46); a recovered row, with the gate's report (WAY-58); a moved
    use of a changed definition and a term WAY-97 asks the request to name. Under *Questions*, only
    the questions the foundation step allows, each with its options and a recommendation where one
    exists; where there are none, say so. Give the number of other choices and a link to the choice
    log. Link the cycle record and full reports by the SHA of the
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
checks and return step, and the independent assessment only where the correction changes the
foundation or an invariant test, and then the record's pair of commits from step 12. A decision
written in a correction takes the existing request's URL directly in its *Approved by*. Update the
request's description, including its record links and *What this request settles*.
