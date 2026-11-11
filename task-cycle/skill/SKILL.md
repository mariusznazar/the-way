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
   path in the worktree's `.the-way`. Run the product's gate on that commit as step 10 gives, at
   once; a check that fails there and passed on the base is work the task carries, made under the
   new pin: step 4's judgment counts those checks, and steps 8 and 9 hand them on with the task and
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

The cycle writes only in the task's worktree and changes nothing outside the product repository,
except the fast-forward of the checkout in step 4 and the account of the request named below;
reading outside it stays with the agent (WAY-140). A remark about the-way, the user's agent
instructions or another repository goes into the record's process remarks, never into the request.
For each stage report, copy every item under **Searches not found or unclear** that is not `none` word for word into
those remarks, with the stage name and full report path; keep repeated items separate (WAY-260).
The remarks stand in the one form `task-cycle/record_template.md` gives (WAY-296), and before every
commit that adds the record, "The record before it is committed" below compares them with the
reports (WAY-294) and cleans and checks the copy it commits (WAY-308, WAY-309, WAY-316).
The account of its request is the cycle's own: in the task's entry in the backlog the product names
(WAY-107), found as `project-level/backlog_place.md` gives, the cycle may add the request link and
set the task's state.

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
   for a file the change adds, is no choice. Judge first whether such a choice is a reserved choice,
   as "Design and execution choice" gives: then no spec is written, no route is judged, and once
   this step and step 5 have set up the branch and the record, `task-cycle/skill/reserved_return.md`
   takes over. Where any other open design choice stands, the cycle writes a spec (step 6).
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
   In the-way itself, first bring the checkout the session works in up to the remote target branch,
   the one change the cycle makes to a checkout outside the task's worktree: fetch, and where it stands behind,
   fast-forward it when it is on that branch with a clean tree and no local commits, then start
   again from the entry point that started the cycle; where it cannot fast-forward, stop and say
   so.
   Create a task branch from the current target branch under the product's git rules, in an
   isolated worktree where its instructions and tools allow; only a correction after review reuses
   a branch. Never overwrite another worker's changes or let two writing agents edit one worktree at
   once. Record the base commit and the checks already failing on it. Run those checks on the base
   alone: finish them before anything changes a tracked file of the worktree, or run them in a
   separate checkout of the base commit under the worktree's ignored `.runs/`, deleted when they
   end. In a product that checkout gets its dependencies installed, as the product's own rules give,
   and its `.the-way` populated before the checks run; otherwise they fail for that reason and not on
   the base. Keep a frozen copy of the task document with its original path and its approval date or
   source commit. Where step 2 moved the pin, the branch, its base and those checks already stand.
5. Name the task `<task-slug>`: for a task of a project plan, its name in the plan (WAY-147); for
   any other, the name the cycle gives it. Create the ignored record
   `.runs/task-cycles/<task-slug>/cycle.md` in the task's worktree from
   `task-cycle/record_template.md` of the pinned the-way and fill it as its sections give; it is
   the cycle's only log (WAY-148). Keep each full handoff and report beside it in `reports/`, with
   secrets and personal data removed; never copy diffs or files git holds — name the commits.
   Append each event before the dispatch that depends on it, so that another session can resume
   from the record, the worktree and the commits. Record every question, answer and choice with the
   option rejected, its cost if wrong and what used it; no hidden reasoning and no output bearing
   secrets. The record stays out of commits until step 12.

Write each dispatch's full handoff to a file in `reports/` whose name holds `handoff`; the message
names that file and only what routing needs (WAY-148). The handoff gives the user's delegation, the worktree, the method of
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
gives the findings file, which you write in the reviewer's words from the review's blocking
findings and, after them, the Minor findings of the review of the whole change within the task
("The end of a code review"); the fix's range runs from the reviewed head, and the review of the
fix also gets the fix report. The message that dispatches or resumes the agent of a fix, and the
one of the review of that fix, names the findings file by its path in `reports/`, as
`reports/<file>.md`, besides the handoff that names it, and no other message does: the audit of
the process ties a turn to its fix round by that path (WAY-336). No handoff tells an agent to run
the product's gate; its run is yours (step 10, WAY-160).

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
its commits, a one-line check result naming what failed or did not run (an agent of `write-spec`
runs no test or other check and returns no check result), and the report's path; its
questions and concerns, each reach beyond its handoff, its **Unread material** — what its handoff
names, or for the reviewer of the whole change its own selection, that stayed unread or was read in
part, or `none` — and **Searches not found or unclear** — each thing looked for and not found or
unclear, or `none` — stand in the report (WAY-148, WAY-260, WAY-325, WAY-326). In every report read
its checks, reaches, unread material and searches; read the rest of it where the status is other
than `done`. A reach shows where your selection fell short: add what it found to the handoffs that
follow. Where a report says that something its handoff names stayed unread or was read in part,
decide before you act on its status: resume the agent to read it, carry the gap into the handoff of
the next agent able to judge it, or record an autonomous choice saying why it bears on nothing the
agent judged. A decision the reviewer of the whole change read by title as WAY-150 gives is no gap.
Under `make-change` the status is `done`, `done with concerns`, `questions`, `returned`, `reserved`
or `blocked`; under `plan-task` it is `done`, `done with concerns`, `questions`, `returned` or
`reserved`; under `review-change` it is the report's first line, `PASS <sha>`, `FAIL <sha>` or
`questions`; under `write-spec` the designer returns `questions`, `done` or `reserved` and its
reviewer `PASS` or `FAIL`. A check a report says it ran carries its
command and exit code; a report missing either returns to its agent for repair before dependent
work, and a claim that tests passed does not repair it (WAY-159). A report that lacks its **Unread
material** (WAY-326) or its **Searches not found or unclear** (WAY-260), save one returning
`questions`, or a `make-change` report of `done` or `done with concerns` without its own-work check
(WAY-164), returns to its agent for repair the same way (WAY-148); `none` is an answer, a missing
section is not. An agent that returns `questions` gets your answers as step 6 answers the
designer's — from an approved source, otherwise, except for a reserved choice, the smallest
reversible reading that fulfils the task, recorded as an autonomous choice — and is resumed, with
no mechanical check and no review until it returns its work. `blocked` is for a missing fact or
permission, and for a question the foundation step leaves to the human: supply the fact or
permission where a source gives it and resume the agent; for a slice's executor that no source can
help, step 9 gives one retry and then its stop; otherwise open the blocked draft request, the
question or the missing fact or permission in its section for the human's decisions, as step 13
gives.

Advance on the short return, the record, the paths and the commits; do not load a stage agent's
sources, full report or diff again merely to go on (WAY-148). Read the sources and the relevant
report before you answer a question or verify disputed or incomplete evidence, and correct a stale
path or commit range against the worktree, recording the correction. An agent sends its questions to
you and returns at its boundary, never starting the next stage or seeking human approval. Each
go-ahead you give a stage is provisional, never the human's approval; by merging the request, the
human accepts the foundation entries the cycle writes that were not accepted with the task document
or at the readiness gate, which the request puts before the human (WAY-114).

## Design and execution choice

Only an open design choice calls for a spec (WAY-135). A change one agent can hold is made by one
author without a plan, also when it writes foundation entries or follows a reviewed spec; a change
needing division gets a plan (WAY-136). Both routes reach the same outcome through the same
reviews, tests, return step and request.

No stage of the cycle settles a reserved choice, you included (WAY-268), and no spec is written for
one (WAY-135). Where an agent returns `reserved`, or where the task at step 4, an agent's question
or a report of `returned` needs a language, a framework, a library, a store of data, a way of
logging in or a place to run that the task, the spec and the foundation do not settle, read
`task-cycle/skill/reserved_return.md`, which checks the choice against
`project-level/technology/reserved_choices.md` of the pinned the-way, and follow it before you
answer or go on.

6. Where step 4 found an open design choice, or an agent returned one (below), dispatch a fresh
   designer with `write-spec`, the frozen task, the choice and, after a discarded attempt, that
   attempt's report. It writes `spec.md` in the record's directory. While it returns `questions`,
   answer each from an approved source where one answers it; otherwise, except for a reserved
   choice, choose the smallest reversible reading that fulfils the task, note the ways and the price
   of being wrong, record it as an autonomous choice and resume the designer. Never widen the task.
   It returns `done` with the spec, before any plan or code.
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
        (each path pattern there covers every changed file it matches)
        and, for slice 1, the plan's *Foundation entries*, and each check of the report with its
        command and exit code, its **Unread material**, its **Searches not found or unclear** and
        its own-work check. Uncommitted work returns to the executor to commit, and a check without
        its command or exit code, or a report missing one of these sections, returns the report for
        repair (WAY-148, WAY-159, WAY-164, WAY-260, WAY-326); any other mismatch goes as
        information to the review that judges the slice and does not return it.
        The mechanical check fails where the range holds no commit, or where a repair the
        executor was sent back for is left undone;
     4. an executor that returns `blocked` for a fact or permission no source supplies, reports a
        failing check of its slice, or fails the mechanical check gets one retry (WAY-229): record
        its last commit, reset the branch to the slice's base and dispatch a fresh executor one
        class higher — `cheaper` to `same`, `same` to `strongest` — with the failed executor's
        report and what failed. The retry goes through sub-steps 3 and 5 as any executor does.
        An executor of the strongest class that fails, or a retry that fails, stops the cycle:
        record its last commit and reset the branch to the slice's base, run the gate on the
        change as step 10 gives (at once, since no return step runs), run
        `task-cycle/cycle_stages.py`, prepare the record's copy as
        "The record before it is committed" gives and commit it and its removal as step 12 gives,
        then write the description by
        `task-cycle/skill/request_template.md` as step 13 gives, in its variant for a slice failed
        twice, linking the record by the SHA of the commit that adds it, and open the request from
        it as a draft marked `blocked`;
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
   reviewer's grade or scope. The Minor findings of this review within the task are fixed before
   step 10, as "The end of a code review" gives (WAY-161).
10. Run the product's gate yourself on the reviewed change (WAY-160), the fix for its Minor findings
    included, or the code a revert of that fix leaves, and record its command, exit
    code and the failures it names under *Verification*, with each check that failed or did not
    run by name; an unrun check is unchecked, never passed. Start it once step 11's return step and
    any review of it are done, on the tree they leave: the return step needs no result of the gate,
    so one run covers both. Where the gate then fails and its fix changes code, the return step
    compares that fix's range too. The authors' focused checks are not rerun merely to go on
    (WAY-159); a change, a failure or disputed evidence calls for the affected
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

A review whose first line is `PASS` sends the change on without a fix, save for the Minor findings
of the review of the whole change (below). A finding the reviewer marks outside the task's scope is
not fixed, whatever its grade, and a Minor finding of a slice review, of the return step, of the
reconciliation with the target branch or of a correction is not fixed either; outside the slice
reviews, each goes to its list in the lower part of the request's description (step 13) with the
reviewer's words and its place in the code, or a note that the reviewer names none.

The review of the whole change differs in its Minor findings (WAY-161). Each that its report lists
and the reviewer has not marked outside the task's scope is fixed before the request opens; a Minor
finding of a slice review that the report does not list is not, and stays in the request's list. Cut
these Minor findings from the report in the reviewer's words, and write them into the findings file
after the blocking findings, if any.

A `FAIL` gets one fix and one review of that fix (WAY-162); you never overrule a blocking finding or
skip its fix. The author or executor whose work the findings concern fixes them with `make-change`,
given the findings file, runs the affected checks again and answers with evidence a finding it holds
wrong; where the harness cannot resume it, or the findings concern several slices, a fresh agent on
the same branch, given the task and the findings, fixes them. The fix of a slice's findings runs on
the class of the executor whose work stands, of findings in several slices on the highest of their
classes, of a planned change's finding of no slice on yours, and of the one author's findings on the
one author's class (WAY-229). A Minor finding names no slice, so it changes neither the agent nor
the class that the blocking findings set. The same reviewer, or a fresh one given its report where
it cannot be resumed, reviews the fix range once. A new Critical or Important finding in the fix
counts as one that remains; a Minor finding that remains after the fix, or that the review of the
fix finds new, does not block, and goes to the request's list.

A `PASS` of the review of the whole change that lists Minor findings within the task gets one fix
for them alone and one review of that fix (WAY-161, WAY-162). The one author, resumed, fixes them
on its class, as it would fix a blocking finding; on the planned route a fresh agent with
`make-change` fixes them on yours, since they name no slice. The same reviewer, or a fresh one given
its report, reviews the fix range once, as above. Only a new Critical or Important finding in the
fix fails that review. When it does, revert the fix's commits, in a revert commit on the branch so
that they stay in history, and run no third round: the code is then the code the review of the
whole change accepted, and the request opens on it, not blocked, with no review of the revert
itself. The Minor findings the fix tried and the new finding stand in the request's list of Minor
findings, the new finding marked with its grade and as found by the review of the reverted fix, with
the reviewer's words and its place in the code; step 13 judges it like any unfixed finding
(WAY-289). Where the fix passes its review, the Minor findings it fixed are no longer unfixed, and
those it left, or that its review found, go to the list.

When a blocking finding remains after the review of its fix — in any of these reviews, a slice's
included — read `task-cycle/skill/blocked_finding.md` and follow it.

## Request and handoff

12. A request that a remaining blocking finding blocks follows "The end of a code review" instead.
    Otherwise merge the remote target branch into the task branch; where that changes the reviewed
    code, have a fresh reviewer review the merge with `review-change`, with a dispatch that asks
    whether the two sides still hold together and names the foundation entries the merge brought in
    that bear on the parts the change touches (WAY-150), and have the agents that own the affected
    checks run them. Where the final tree differs from the one step 10 checked, run the
    gate again on it as step 10 gives. Record how long each stage took, which models did it and how
    many tokens it used: run `task-cycle/cycle_stages.py` of the pinned the-way with `--output
    .runs/task-cycles/<task-slug>/stages.md`, naming every session of this cycle's orchestrator, a
    correction's included, by its transcript path or id; Claude Code holds the current session's id
    in `CLAUDE_CODE_SESSION_ID` and Codex in `CODEX_SESSION_ID`. Run the process remarks check on
    the record as "The process remarks check" gives, before the description is written, so that a
    listing you hold wrong reaches the description. Write and check the description by
    `task-cycle/skill/request_template.md` as step 13 gives, and open the request from it as a draft by the pull or merge request route the
    user already chose. Write its URL into the record, then take "The record before it is
    committed" below: it copies the whole record directory to `docs/task-cycles/<task-slug>/` on
    the task branch and cleans and checks the copy. Commit it, commit its removal immediately after
    and push, so that the request's changed files show only the change and the target branch never
    holds the record. Never force-push: a rejected push is investigated. Put the link to the
    record, by the SHA of the commit that adds it, never by branch name, into the description, and
    in the same edit fill in under *Checks* the runs of the three checks on the copy; check it again
    by the template's checks, which include the check of private paths, and edit the request with
    it. Mark the
    request ready for review unless the description's first line reads `blocked` or `draft`; a
    request waiting for human actions in the cycle stays a draft marked `blocked`. Do not merge.
    Keep the worktree for corrections.
13. Before you write the description, count the merges since the last review of the foundation: in
    the worktree's root (in a product, the path starts with `.the-way/`), after a fetch, run
    `python -B task-cycle/review_reminder.py origin/<target branch>`. When its last line reads
    `reminder: yes`, the description's *How to merge* carries the reminder as
    `task-cycle/skill/request_template.md` gives; it blocks nothing, and every request the cycle
    writes or rewrites gets it while the count stands (WAY-300). Record the output under
    *Verification*.
    Write the request's description into `.runs/task-cycles/<task-slug>/request.md` by
    `task-cycle/skill/request_template.md` of the pinned the-way, which holds its sections, where each
    takes its content from and the variants of a blocked, reserved or corrected request; check its
    form with `task-cycle/request_check.py` and its text for private paths with
    `task-cycle/private_paths_check.py`, and correct it until both checks pass, as the template
    gives, and publish it from that file (WAY-286, WAY-290, WAY-309). Recover the task's parts from its
    frozen task and changed files through the part map when preparing the request, and keep that
    classification as evidence with the check, not as a separate record of the selected parts
    (WAY-261). Never present partial work as complete.
14. Before reporting completion, confirm that the record lists every dispatch, choice, check, fix,
    review round and skipped stage. The final report names any write to the task's backlog entry.
    The request is the human's first decision point.

## The process remarks check

Before every commit that adds the record, "The record before it is committed" below has this check
run twice: on the original in `.runs/`, and again on the cleaned copy. Run, from the worktree's root
(in a product, the path starts with `.the-way/`), the-way's script (WAY-294):

```
python -B task-cycle/remarks_check.py .runs/task-cycles/<task-slug>
```

The copy is given in the place of the original, `docs/task-cycles/<task-slug>`, and is read the
same way.

It reads the **Searches not found or unclear** section of every report in the record's `reports/`,
a file whose name holds neither `handoff` nor `findings`, in either of the forms the reports give
it, and lists each item other than `none` that the record's process remarks do not hold word for
word, with the path of its report. It only lists, and it
judges no content. On the original, exit 1 lists each item as `<report path>: <item>`:

1. Append each listed item to the process remarks word for word, as an entry in the form
   `task-cycle/record_template.md` gives, with the stage name from the Events and the full report
   path; never in other words, never with the item left out for being trivial, and with a repeated
   item as an entry of its own for each report that gives it.
2. Run the script again, and go on until it exits 0 and lists nothing.
3. Record the last run, its command and exit code, with the number of runs, under *Verification*.

Exit 2 is no listing: fix the call, or the file that could not be read.

**A listing you hold wrong.** Where you hold a listed line to be an error of the script, with
evidence you can name — the line is text of the report that is no item, say — the script is not
changed in this cycle and the archive is not held back (WAY-295):

1. Do not append the listed line as an item of its stage.
2. Enter the case in the process remarks as an entry of your own: the script, the line it listed,
   and why you hold it wrong. It is a matter of the-way's script, not of the product.
3. Commit the record as usual. In the request's description, the group *You accept by merging* of
   *For you to decide* gets one item naming what the script listed, in plain words, and why the
   cycle holds it wrong, and *Checks* names the check with its command, its exit code and its
   listed line, as `task-cycle/skill/request_template.md` gives.

## The record before it is committed

The record's copy stays in the repository's history, and the repository may be read by anyone.
Before every commit that adds the record to `docs/task-cycles/<task-slug>/` — step 12, its
repetition in a correction (`correction.md`), the stop of a slice failed twice at step 9 sub-step 4
and the blocked requests of `blocked_finding.md` and `reserved_return.md` — the copy is cleaned of
what only its author may see and checked, in every repository, public or private (WAY-308, WAY-309),
and checked for image files, which no copy holds (WAY-316). The original in `.runs/` is never
cleaned; each commit adds a fresh copy of it, cleaned again. The steps stand in this order, run from
the worktree's root (in a product, the path starts with `.the-way/`):

1. Run the process remarks check on the original, as "The process remarks check" gives, until it
   lists nothing. It runs on the original first, because the original holds the words the reports
   gave: each item reaches the remarks once, before any word is changed, and the cleaning below
   meets it in both places.
2. Copy the whole record directory to `docs/task-cycles/<task-slug>/` on the task branch and
   rewrite its links to the committed copies.
3. Clean the copy by one rewriting, applied to every text file of it — `cycle.md`, the handoffs
   and reports, the copy of the task document, `stages.md`, `request.md` — so that a text standing
   in two files is replaced by the same words in both. An item of a report and the same item in
   the process remarks must still read the same, word for word:
   - an absolute path to a place inside the repository, such as the worktree, becomes the path
     from the repository's root; an absolute path to a place outside it becomes a description of
     what the place is, since no relative path reaches it;
   - the path and the title of a private note become a description of what the note is, such as
     "the task's note in the author's backlog", not a new name for the note;
   - the lines `Task relation:` of `cycle.md` and `Project relation:` of the copy of the task
     document stay as they are unless the check of step 4 lists them, because the plan-state
     reader ties the record to the plan's task by them (WAY-153). Their form names the plan by its
     file name, so neither is expected to hold a path. A line the check lists is cleaned like any
     other, and the reader may then report a conflict with exit 1 for this task, which the human
     sees in the request (step 4);
   - the line `Task source:` is cleaned like any other. For a plan item this costs the reader part
     of its proof until the plan row's *Document* links the frozen copy: it cannot anchor the
     copy, reports it `unchecked` and proposes no move to `done` from it. An independent task is
     not touched.
4. Run the-way's check of private paths on the copy:

   ```
   python -B task-cycle/private_paths_check.py docs/task-cycles/<task-slug>
   ```

   It reads every file below the directory and lists, by pattern, each absolute path (a drive
   letter, a home directory) and each note link written in double square brackets, as
   `<file>:<line>: <kind>: <text>`; it holds no list of private words, judges nothing else and
   rewrites nothing. Exit 1: correct each listed place in the copy by step 3, with the same words
   wherever the text stands, and run the check again until it exits 0. A path is replaced whole,
   to the end of the phrase that names it, not only up to the part the check prints: a path with
   a space in it is printed to the space. A listed text that is neither kind, such as a code
   sample, is written so that the pattern does not list it. No listing is left in place, a
   `Task relation:` or `Project relation:` line included; where such a line had to be cleaned, the
   request tells the human, as item 12 of *For you to decide* in
   `task-cycle/skill/request_template.md` gives. Exit 2 is no listing: fix the call, or the file
   that could not be read. The last line counts the files not read: a text file among them, such
   as one a shell saved in an encoding other than UTF-8 or UTF-16, is read by hand or saved as
   UTF-8 and checked again; a file that is no text needs no reading by this check, and an image
   file is the business of step 5.
5. Run the-way's check of image files on the copy (WAY-316):

   ```
   python -B task-cycle/image_files_check.py docs/task-cycles/<task-slug>
   ```

   It lists, as `<file>: image file`, each file below the directory whose name ends in an image
   extension, and judges nothing else; it never opens a file, so it does not see an image saved
   under another name or written into a text, and a screenshot is not kept in the record in any
   form (`change/ui_check.md`). Exit 1: delete each listed file from the copy only, since the
   original in `.runs/` is never changed, rewrite every mention of it in the copy, by step 3's one
   rewriting, as words that say what the screenshot showed and where it lies, and run the check
   again until it exits 0. Exit 2 is no listing: fix the call.
6. Run the process remarks check on the cleaned copy. It lists nothing when step 3 was one
   rewriting. An item it lists has different words in a report and in the remarks of the copy:
   make the two read the same in the copy, and append no second entry for it, since step 1 has
   the remarks hold it already (WAY-309 gives this run its place beside WAY-294). After any
   correction of the copy, run the checks of steps 4 and 5 and this check again until all three
   exit 0.
7. Record the last run of each of the three checks on the copy, its command and exit code, with the
   number of runs, under *Verification* of the original record; the description names them under
   *Checks*.

Then commit the copy. Commit messages are not checked (WAY-308).

## Correction after review

When your input is a link to a request, or to a comment holding the human's remarks, read
`task-cycle/skill/correction.md` and follow it.
