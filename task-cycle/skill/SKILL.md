---
name: implement-task
description: Use to take one ready the-way task to a reviewable pull or merge request — through a spec where the task leaves an open design choice, one author without a plan where the change fits one agent or a plan of slices made one after another, review by agents that did not make the change and the product's full tests — or to apply corrections for the human's remarks to its open request. Requires subagents. The human reviews the request, not intermediate steps.
---

# Implement one task

Drive one task from `ready for cycle` to a reviewable pull or merge request. You are the
orchestrator: you dispatch each stage to an agent of its own, keep the cycle record, and run the
loop of slices and the end of each code review yourself. The agents use the-way's methods of their
stages — `write-spec`, `plan-task`, `make-change` and `review-change` (WAY-125). Answer their
questions from the task, its sources, the product's current foundation and code, and keep every
answer and its evidence in the record. The person who requested this cycle has delegated
intermediate choices to you; never label your answer as that person's approval.

The cycle has one ordinary human contact: the request. Do not pause for design, spec, plan,
implementation or review questions. Stop early only when the required outcome cannot be made under
the available evidence, capabilities and binding rules, when a blocking finding survives the one
fix a code review allows ("The end of a code review"), or when a slice's executor fails after its
one retry (step 9). A slow step, a failed test or an unclear way to make the change is work to
resolve, within that one retry for a slice, not a reason to ask the human. Where a binding rule
reserves a decision to a human and the code cannot proceed without it, open a blocked draft request
with the evidence and stop.

## Inputs and authority

1. Read the task document in full. Require `Status: ready for cycle` and every human action its
   *Human actions* places before the cycle done (WAY-124); those it places in the cycle step 4
   takes up. Its `Project relation:` sets the sources: an independent task needs no project; a plan
   member requires its approved plan item, dependencies and assignments; a source-only task uses
   the approved project settlements it names without taking plan work. Its *Decisions in play*
   names the decisions it touches, and its *Settlements to record* what its refinement settled for
   the foundation (WAY-134). If a source changed since the task was accepted, reconcile the task
   against it and record the effect; stop only when the required outcome can no longer be
   established.
   Before a plan member's cycle starts, read `task-cycle/skill/plan_member.md` and follow it.
2. Read the product's `AGENTS.md`, verify that the pinned the-way checkout matches the product's
   gitlink, and follow the product's git and test rules. Where the task moves the pin to a commit
   it names, move it now, before anything else of the cycle (WAY-34): create the task branch and
   record its base and the checks failing on it as step 4 gives, clone the-way at that commit into
   the worktree's ignored `.runs/`, run the installer from that clone as `installation/README.md`
   gives, and commit the gitlink with everything the installer rewrote, and the removal
   `installation/README.md` asks for, as the task branch's first commit; then delete the clone. No
   author makes that commit and no slice holds it. Then read this skill again from the worktree's
   `.the-way` and go on under the new pin: every later reading, dispatch and script of the cycle
   comes from it. The skills of the-way read `.the-way` from the directory their agent works in,
   so each handoff has the agent work from the worktree's root and names its stage's method by its
   path in the worktree's `.the-way`. Run the product's gate on that commit as step 10 gives; a
   check that fails there and passed on the base is work the task carries, made under the new
   pin: step 4's judgment counts those checks, and steps 8 and 9 hand them on with the task and
   check their coverage as they check its items. Every reset of the task branch to its base stops
   at that commit. The review of the whole change checks that commit: it holds only the gitlink, at
   the commit the task names, and what the installer owns: the `the-way-*` entry points in
   `.claude/skills/` and `.agents/skills/`, in `AGENTS.md` the block between its markers, and the
   removal of `.claude/rules/the-way.md` where an older pin installed it.
   Read the foundation by "Reading the foundation" in `elements/common/way_of_working.md`, and the
   product's guidelines by `product-guidelines/reading.md`, for the parts the task's required
   behaviour changes: you select from them what each agent reads (WAY-150, WAY-213), and they serve
   the judgments of step 4. A finding of the guidelines' reading takes the route the procedure
   names.
3. Require a harness that can dispatch subagents, and the methods of the stages in the pinned
   the-way, each a project skill with the `the-way-` prefix: `write-spec`, `plan-task`,
   `make-change` and `review-change`. Each stage agent reads the `SKILL.md` of its stage's method
   whole, and a file the method names, one beside that `SKILL.md` included, only when the step or
   variant that names the file comes; you read this skill and no method you do not conduct. Without
   subagents this cycle cannot run in that harness.

The cycle writes only in the task's worktree and changes nothing outside the product repository;
reading outside it stays with the agent (WAY-140). A remark about the-way, the user's agent
instructions or another repository goes into the record's process remarks, never into the request.
The one exception is the cycle's own account of its request: in the task's entry in the backlog the
product names (WAY-107), the cycle may add the request link and set the task's state.

## Start and record

4. Answer two questions about the change the task requires, recorded under *Two questions at
   start* (WAY-13):
   - Does it touch a trust boundary — files the part map names as one, which take in data from the
     network, keys, the deployment or files from outside (WAY-48)? Then every code review of the
     cycle is told so, and checks crafted input at that boundary.
   - Does it hold an operation that cannot be undone? Then the cycle prepares it and never performs
     it, every code review checks that the change only prepares it, and the human performs it after
     deciding at the request. Treat a security-sensitive action the same way where the product's
     rules reserve its authorization to a human; where it is needed to finish the task, the request
     opens blocked.

   A yes adds the reviews aimed at that risk, those of the slices the plan marks with it included;
   neither answer removes anything: every change, whatever its size, gets the product's tests and a
   review by an agent that did not make it. Only a human sets a task to return knowledge instead of
   a change.
   In the same reading, settle whether the task leaves an open design choice (WAY-135). A row of
   *Settlements to record* or a projected entry the task carries settles its entry, an invariant's
   included; an entry that follows from the change with no way left open, such as a part-map line
   for a file the change adds, is no choice. Where one stands, the cycle writes a spec (step 6).
   Otherwise judge from the task document, and from the checks the move of the pin broke where step
   2 moved it, whether one agent can hold the change (WAY-136): if so, select one author without a
   plan and set its class of model by the measure a planner uses for a slice (WAY-229) — `cheaper`
   than yours by default, ordinary implementation that takes decisions of its own included; `same`
   as yours for a change across many parts; the `strongest` available for one that needs design —
   recording a class other than `cheaper` with its reason under *Author*; if it needs division,
   select planning (step 8). Record the finding, the route and their reasons; write no preliminary
   plan and run no slice-size script to judge.
   An effect outside the product repository is made only by a human, through a human action
   (WAY-140): for those the task document places in the cycle, prepare what the repository allows
   and list them in the request, which opens as a blocked draft; an effect the cycle finds that the
   document does not name joins that list for the human to place, and opens the request the same
   way.
   Create a task branch from the current target branch under the product's git rules, in an
   isolated worktree where its instructions and tools allow; only a correction after review reuses
   a branch. Never overwrite another worker's changes or let two writing agents edit one worktree at
   once. Record the base commit and the checks already failing on it, and keep a frozen copy of the
   task document with its original path and its approval date or source commit. Where step 2 moved
   the pin, the branch, its base and those checks already stand.
5. Name the task `<task-slug>`: for a task of a project plan, its name in the plan (WAY-147); for
   any other, the name the cycle gives it. Create the ignored record
   `.runs/task-cycles/<task-slug>/cycle.md` from `task-cycle/record_template.md` of the pinned
   the-way and fill it as its sections give; it is the cycle's only log (WAY-148). Keep each full
   handoff and report beside it in `reports/`, with secrets and personal data removed; never copy
   diffs or files git holds — name the commits. Append each event before the dispatch that depends
   on it, so that another session can resume from the record, the worktree and the commits. Record
   every question, answer and choice with the option rejected, its cost if wrong and what used it;
   no hidden reasoning and no output bearing secrets. The record stays out of commits until step 12.

Write each dispatch's full handoff to a file in `reports/`; the message names that file and only
what routing needs (WAY-148). The handoff gives the user's delegation, the worktree, the method of
the stage by the path of its `SKILL.md` in the pinned the-way, the stage and its boundary, the paths
and commits of the frozen task and of the spec and plan where they exist, the answers of step 4,
and the report path. The agent reads that `SKILL.md` whole, and a file it names, one beside it
included, only when the step or variant that names the file comes (WAY-125); no handoff tells it to
read at the start every file its method names. Where that `SKILL.md` opens with a table of
variants, the handoff names the agent's variant in the words of its row: under `make-change`,
"the whole change as the one author", for the one author;
"a slice, or the retry of a slice", for a slice's executor and its retry;
"the fix of a review's findings", for a fix;
"a correction for the human's remarks", for a correction.
The agent of the plan's *Foundation entries* and a fresh agent of the return step take none of its
rows, and their handoff names their stage instead. For the foundation step, the handoff names
`task-cycle/skill/foundation_step.md`, and for the return step `task-cycle/skill/return_step.md`
with it, since the return step writes as the foundation step writes, each by its path in the
pinned the-way; the agent reads each whole, and the skill of an element when it writes an entry of
that element. For a review, it gives the range to review and the author's report. For a fix, it
gives the findings file, which you write from the review's blocking findings in the reviewer's
words; the fix's range runs from the reviewed head, and the review of the fix also gets the fix
report. No handoff tells an agent to run the product's gate; its run is
yours (step 10, WAY-160).

You decide what each agent reads, and its handoff names it (WAY-150, WAY-213): the foundation
entries by identifier — those of the task's *Decisions in play*, and the decisions, invariants and
linked entries of the parts the agent's work touches, selected by "Reading the foundation"; the
guideline files of those parts, each whole; and the passages of the task, its sources, the spec
and the plan it needs.
The designer and the reviewer of the spec, the planner, the one author and the reviewer of the whole
change read the whole frozen task, since each works on the whole. What a slice's executor and the
reviewer of a slice get stands in `task-cycle/skill/planning.md`, which step 8 names. Requirements
and values stay in their own files: copy a section of the plan, spec or task into the handoff word
for word, never restated in other words, and name its file as its address (WAY-148). The reviewer
of the whole change selects its own foundation and guidelines, by the parts of the change, and an
agent writing a foundation entry reads as the element's skill gives. You alone read `cycle.md`: an
answer or choice that binds an agent goes into its handoff or the message that resumes it.

Wait for an agent through the harness's completion notification or one blocking wait at the
longest duration its live tool contract and active instructions permit. In Codex, use
`collaboration.wait_agent` where exposed, or the harness's equivalent. In Claude Code, a foreground
`Agent` call blocks where the current mode allows it; a background or resumed agent reports by
completion notification, so yield the turn when only that result remains and resume on it, without
claiming the cycle complete. Renew a bounded wait only after an actual timeout or interruption
leaves work pending, handling a returned question first. Do not list agents, poll their status or
sleep between checks. Record the mechanism and any limit.

Each agent writes its full report to its report path as its method gives it and returns its status,
its commits, a one-line check result naming what failed or did not run, and the report's path; its
questions and concerns, and each reach beyond its handoff, stand in the report (WAY-148). In every
report read its checks and the reaches it names; read the rest of it where the status is other than
`done`. A reach shows where your selection fell short: add what it found to the handoffs that
follow. Under `make-change` the status is `done`, `done with concerns`, `questions`, `returned` or
`blocked`; under `plan-task` it is `done`, `done with concerns`, `questions` or `returned`; under
`review-change` it is the report's first line, `PASS <sha>`, `FAIL <sha>` or `questions`; under
`write-spec` the designer returns `questions` or `done` and its reviewer `PASS` or `FAIL`. A check a
report says it ran carries its command and exit code; a report missing either returns to its agent
for repair before dependent work, and a claim that tests passed does not repair it (WAY-159). An
agent that returns `questions` gets your answers as step 6 answers the designer's — from an approved
source, otherwise the smallest reversible reading that fulfils the task, recorded as an autonomous
choice — and is resumed, with no mechanical check and no review until it returns its work. `blocked`
is for a missing fact or permission, and for a question the foundation step leaves to the human:
supply the fact or permission where a source gives it and resume the agent; for a slice's executor
that no source can help, step 9 gives one retry and then its stop; otherwise open the blocked draft
request, holding the question under *Questions* or showing the missing fact or permission as step 13
gives for an impossible task.

Advance on the short return, the record, the paths and the commits; do not load a stage agent's
sources, full report or diff again merely to go on (WAY-148). Read the sources and the relevant
report before you answer a question or verify disputed or incomplete evidence, and correct a stale
path or commit range against the worktree, recording the correction. An agent sends its questions to
you and returns at its boundary, never starting the next stage or seeking human approval. Each
go-ahead you give a stage is provisional, never the human's approval; the human accepts the
foundation entries the cycle writes by merging the request (WAY-114).

## Design and execution choice

Only an open design choice calls for a spec (WAY-135). A change one agent can hold is made by one
author without a plan, also when it writes foundation entries or follows a reviewed spec; a change
needing division gets a plan (WAY-136). Both routes reach the same outcome through the same
reviews, tests, return step and request.

6. Where step 4 found an open design choice, or an agent returned one (below), dispatch a fresh
   designer with `write-spec`, the frozen task, the choice and, after a discarded attempt, that
   attempt's report. It writes `spec.md` in the record's directory. While it returns `questions`,
   answer each from an approved source where one answers it; otherwise choose the smallest
   reversible reading that fulfils the task, note the ways and the price of being wrong, record it
   as an autonomous choice and resume the designer. Never widen the task. It returns `done` with
   the spec, before any plan or code.
7. When the designer returns `done` with the spec, read `task-cycle/skill/spec_review.md` and
   follow it: the spec's review by a fresh agent, and the route judged again after it.
8. Only on the planning route, read `task-cycle/skill/planning.md` and follow it: the planner's
   dispatch, the review of its plan, and what each slice's handoff carries.

An agent that meets an open design choice while it makes the change or a fix returns `returned`
with a report and no code: the choice, where it shows, the ways open and what it found (WAY-135). A
choice of how to make what the task and the foundation settle is none; the agent makes it and names
it, and you enter it in the questions table. Check that the report holds no code and keep it.
Record the attempt's last commit — a historical name, not a link to follow — and the files it
changed, then discard the attempt, its foundation entries included, by resetting the task branch to
the recorded base — to the commit that moved the pin where step 2 moved it. Record the discard
with its reason and continue at step 6; after the spec's review, step 7 chooses the route again.

A one-author change that proves too large returns `returned` with where the size lies. Keep the
report, record the attempt's last commit and files, discard the whole attempt and its foundation
entries by resetting the branch to its base — to the commit that moved the pin where step 2 moved
it — and dispatch the planner at step 8 with the frozen task, any reviewed spec and the report
(WAY-136). Record it as a return for size.

A slice that proves too large for its executor returns the same way. Record its last commit and
files, reset the branch to the slice's base and have the planner split that slice; the slices
already made stay. Record it under *Slices returned too large*.

## Execute, verify and review

The foundation step writes the entries the task carries, as `task-cycle/skill/foundation_step.md`
gives: its agent — the one author with its code, or on the planned route the agent of the plan's
*Foundation entries* — reads that file, which its handoff names. Read it yourself when an agent
returns `blocked` with a question for the human, and at step 7 for a finding that the spec
contradicts a decision.

9. Make the change and have it reviewed.
   - **One author.** Dispatch a fresh author with `make-change`, on the class of model you set
     for it (step 4) and the harness's model closest to it, as sub-step 2 of the planned route
     gives for a slice, recorded under *Author* — with the frozen task, any reviewed spec and the
     checks the move of the pin carried (step 2). It does the foundation step with its
     code and returns before review; where the change touches a user interface, it reads the
     styleguide's example of the order of work as an example (WAY-213). Keep it for the fix and
     the return step, on its class (WAY-229); where the harness cannot resume it, a fresh author
     of the same class on the same branch takes its place, recorded under *Author*.
   - **Plan.** Where the plan lists *Foundation entries*, write slice 1's base first, then dispatch
     a fresh agent with `make-change` for those entries, recorded in the row `Foundation entries`
     of *Slices*; slice 1's range starts at that base, so whichever review judges slice 1 covers
     the entries. Then make the slices one after another, in the plan's order. For each slice:
     1. write its base, from `git rev-parse HEAD`, in its row of *Slices* before you dispatch it;
     2. dispatch a fresh executor with `make-change`, on the class of model the slice's *Model*
        sets (WAY-229) — `cheaper` than yours, `same` as yours or the `strongest` available, on
        the harness's model closest to it, recorded in the slice's row; where yours is the
        strongest, `same` and `strongest` are one class; where the harness cannot choose a model,
        dispatch as it allows and record that the class was not applied — with the slice's
        section of the plan copied word for word and what its *Read* names, as the handoff
        paragraph above and `task-cycle/skill/planning.md` give;
     3. when it returns `done` or `done with concerns`, check mechanically: a clean worktree, a
        non-empty range from the base to its head, the changed files against the slice's *Change*
        and, for slice 1, the plan's *Foundation entries*, and each check of the report with its
        command and exit code. Uncommitted work returns to the executor to commit, and a check
        without its command or exit code returns the report for repair (WAY-159); any other
        mismatch goes as information to the review that judges the slice and does not return it.
        The mechanical check fails where the range holds no commit, or where a repair the
        executor was sent back for is left undone;
     4. an executor that returns `blocked` for a fact or permission no source supplies, reports a
        failing check of its slice, or fails the mechanical check gets one retry (WAY-229): record
        its last commit, reset the branch to the slice's base and dispatch a fresh executor one
        class higher — `cheaper` to `same`, `same` to `strongest` — with the failed executor's
        report and what failed. The retry goes through sub-steps 3 and 5 as any executor does.
        An executor of the strongest class that fails, or a retry that fails, stops the cycle:
        record its last commit and reset the branch to the slice's base, run the gate on the
        change as step 10 gives, run `task-cycle/cycle_stages.py` and commit the record and its
        removal as step 12 gives, and open the request as a draft marked `blocked`, linking the
        record by the SHA of the commit that adds it and giving what step 13 names for a blocked
        request, that names both failures with the classes tried, each slice made so far that no
        review judged, and the review of the whole change, the return step and the reconciliation
        with the target branch as not run;
     5. where the slice's *Risk* names a trust boundary or an operation that cannot be undone,
        dispatch a fresh reviewer with `review-change` on that range and the slice's number, with
        the executor's selection; for slice 1 the handoff names the plan's *Foundation entries* as
        part of the range and gives the report of the agent that wrote them beside the
        executor's. A `FAIL` gets one fix and one review of the fix, as "The end of a code review"
        gives; keep its Minor and out-of-scope findings in its row for the review of the whole
        change. Every other slice goes on after its mechanical check, and the review of the whole
        change judges it (WAY-136).

     A plan of one slice skips the review of the slice: the review of the whole change is its one.

   Then the review of the whole change: a fresh reviewer that made none of it, on no class cheaper
   than yours (WAY-229), with `review-change`, on the range from the task's base to the head, with
   the frozen task, any spec and plan, each slice's range and whether it had a review of its own,
   the report of each executor whose slice had none with any mismatch its mechanical check passed
   on, the report of the agent that wrote the plan's *Foundation entries* where slice 1 had no
   review of its own, and the Minor and out-of-scope findings of the slice reviews (WAY-164); where
   the task moved the pin, it is told of that commit and given the checks the move carried. It
   selects its own foundation and guidelines, judges every slice that had no review of its own, and
   names for each blocking finding the slice it comes from, or that it comes from none (WAY-136).
   For progression use the changed files with their line counts and the review's first line
   (WAY-158); read the evidence only when a question about a finding needs it, never to change a
   reviewer's grade or scope.
10. Run the product's gate yourself on the reviewed change (WAY-160), and record its command, exit
    code and the failures it names under *Verification*, with each check that failed or did not
    run by name; an unrun check is unchecked, never passed. The authors' focused checks are not
    rerun merely to go on (WAY-159); a change, a failure or disputed evidence calls for the affected
    checks again, by the agent that owns them. A check that fails in a cycle run and passes when run
    again follows the product's rule on flaky tests (the testing guidelines' *Flaky tests*,
    WAY-243): rerunning serves only to diagnose what makes it flaky, never to make a gate run pass.
    Apply this rule even when the product has no *Flaky tests* section in its guidelines.
11. Take the return step: the author resumes for it, on its class (WAY-229), or on the planned route
    a fresh agent with `make-change` takes it, on no class cheaper than yours. What it compares and
    writes stands in `task-cycle/skill/return_step.md`, which its handoff names. Where the
    return step commits anything, a fresh reviewer on no class cheaper than yours (WAY-229) reviews
    its range with `review-change`, against the task and the entries the return step writes or
    corrects. Record the result under *Return step*.

## The end of a code review

Every code review of the cycle — of a slice, of the whole change, of the return step, of the
reconciliation with the target branch and of a correction — is made by an agent that did not make
the change, with `review-change`, which holds its grades, its criteria for appearance and for
guideline examples (WAY-220, WAY-221), and what blocks. The reviewer alone grades and scopes: the
handoff names no finding wrong, Minor or outside the scope, though it may carry the author's
evidence on a contested finding, and you move no finding from one kind to another (WAY-161).

A review whose first line is `PASS` sends the change on without a fix. A Minor finding and a
finding the reviewer marks outside the task's scope are not fixed; outside the slice reviews, each
goes to the request's lists (step 13) with the reviewer's words and its place in the code, or a
note that the reviewer names none.

A `FAIL` gets one fix and one review of that fix (WAY-162); you never overrule a blocking finding or
skip its fix. The author or executor whose work the findings concern fixes them with `make-change`,
given the findings file, runs the affected checks again and answers with evidence a finding it holds
wrong; where the harness cannot resume it, or the findings concern several slices, a fresh agent on
the same branch, given the task and the findings, fixes them. The fix of a slice's findings runs on
the class of the executor whose work stands, of findings in several slices on the highest of their
classes, of a planned change's finding of no slice on yours, and of the one author's findings on the
one author's class (WAY-229). The same reviewer, or a fresh one given its report where it cannot be
resumed, reviews the fix range once. A new Critical or Important finding in the fix counts as one
that remains.

When a blocking finding remains after the review of its fix — in any of these reviews, a slice's
included — read `task-cycle/skill/blocked_finding.md` and follow it.

## Request and handoff

12. A request that a remaining blocking finding blocks follows "The end of a code review" instead.
    Otherwise merge the current target branch into the task branch; where that changes the reviewed
    code, have a fresh reviewer review the merge with `review-change`, and have the agents that own
    the affected checks run them. Where the final tree differs from the one step 10 checked, run the
    gate again on it as step 10 gives. Open the request as a draft by the pull or merge request
    route the user already chose. Then record how long each stage took, which models did it and how
    many tokens it used: run `task-cycle/cycle_stages.py` of the pinned the-way with `--output
    .runs/task-cycles/<task-slug>/stages.md`, naming every session of this cycle's orchestrator, a
    correction's included, by its transcript path or id; Claude Code holds the current session's id
    in `CLAUDE_CODE_SESSION_ID` and Codex in `CODEX_SESSION_ID`. Copy the whole record directory to
    `docs/task-cycles/<task-slug>/` on the task branch, rewrite its links to the committed copies,
    commit it, commit its removal immediately after and push, so that the request's changed files
    show only the change and the target branch never holds the record. Never force-push: a rejected
    push is investigated. Link the record in the request's description by the SHA of the commit that
    adds it, never by branch name, and ask for a merge that keeps its commits, since the link
    survives only then; where the product's rules squash or rebase, name that limitation. Mark the
    request ready for review, except one the cycle marks `blocked`, one waiting for human actions in
    the cycle included, which stays a draft. Do not merge. Keep the worktree for corrections.
13. The request states, as the record's *Request handoff* gives it: the task's goal and relation and
    the source revisions it used; the process pin, and where the task moved it, from and to which
    commit, with the gate on that commit; whether a spec was written and why, with its link; the
    route and its reason, and after a discarded attempt its reason and the agent's report; the
    plan's link and slices where one was written; what changed and why. *Checks*: the gate's
    command and exit code, each check that failed or did not run by name, and for a check that
    failed and passed when rerun the number of cycle runs in which it failed and passed, its rerun
    result, and (when its file belongs to a part outside the task's parts recovered from its frozen
    task and changed files through the part map) its listing with its file path beside findings
    outside the task's scope (WAY-260); what each own-work
    check showed (WAY-164), and the user-interface states and screenshot evidence, a screenshot
    unchecked for no settled way or the failure of a settled one included (WAY-219). The Minor findings of
    the review of the whole change and of every later review in one item, and the findings their
    reviewers marked outside the task's scope in another, for the human to choose which become new
    tasks and to create them; that item also names the file paths of checks outside the task's parts
    that failed in a cycle run and passed again, with their rerun results and failure/pass counts
    (WAY-260). Recover the task's parts from its frozen task and changed files through the part map
    when preparing the request, and keep that classification as evidence with the check, not as a
    separate record of the selected parts.
    *What this request settles*: each foundation entry the
    change writes or changes, by its identifier and one sentence of its meaning in the task
    document's language, the projected entries and those written from rows of *Settlements to
    record* apart from new ones, and each kept row tied to an entry already stated, with that entry
    (WAY-134); beside them, each invariant test the change alters (WAY-03), each surface it alters
    (WAY-49) and each *Violated* mark it sets or clears (WAY-51). *Questions*: only those the
    foundation step allows, each with its options and a recommendation where one exists, or a line
    that there are none. The number of other choices with a link to the questions table, and the
    record's link by SHA. The human actions the request waits for, each as the task document names
    it, with each effect outside the repository the cycle found that the document does not name, for
    the human to place (WAY-140). A request a remaining blocking finding blocks is marked `blocked`
    and lists each such finding with its place in the code and its reason, what the fix tried, the
    time, models and tokens of the cycle so far from `stages.md` with the number of review rounds,
    and what has not run on that code (WAY-162, WAY-163). If the task proved impossible, mark the
    request `blocked` and show the smallest missing fact or authorization and the ways tried; never
    present partial work as complete.
14. Before reporting completion, confirm that the record lists every dispatch, choice, check, fix,
    review round and skipped stage. The final report names any write to the task's backlog entry.
    The request is the human's first decision point.

## Correction after review

When your input is a link to a request, or to a comment holding the human's remarks, read
`task-cycle/skill/correction.md` and follow it.
