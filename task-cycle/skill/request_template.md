# The description of a request

Read by the orchestrator of `implement-task` wherever it writes or rewrites a request's
description — step 13, a slice failed twice at step 9.4, `blocked_finding.md`, `reserved_return.md`
and `correction.md` — and by the agent leading a change to the-way that `agent-instructions/README.md`
sends here. Every request of a cycle, blocked, reserved or corrected, has this one skeleton
(WAY-286, WAY-287).

## Write, check, publish

1. Write the description into `.runs/task-cycles/<task-slug>/request.md`, beside the record.
2. Before the form check, read each item of *Needed from you* and of *Fix or let through* against
   the four parts "What an item carries" gives for an item in which the human chooses, and write
   what is missing (WAY-327). The script cannot do this, since it judges no content.
3. Check its form, from the worktree's root — in a product, the path starts with `.the-way/`:

   ```
   python -B task-cycle/request_check.py .runs/task-cycles/<task-slug>/request.md --task <frozen task>
   ```

   `--task` is the frozen task document of the record. The script checks the headings, the three
   groups of *For you to decide*, content or `none` in each section and the block's language, and
   judges no content (WAY-290).
4. Exit 1 lists each problem as `line <n>: <what is wrong and what to write>`. Correct the file at
   each line and run the form check again, until it exits 0. Exit 2 is no error of the form: fix
   the call, or the file that could not be read.
5. Check the same file for private paths (WAY-308, WAY-309):

   ```
   python -B task-cycle/private_paths_check.py .runs/task-cycles/<task-slug>/request.md
   ```

   It lists, as `<file>:<line>: <kind>: <text>`, each absolute path (a drive letter, a home
   directory) and each note link written in double square brackets, the block in the task
   document's language included, and judges nothing else. Exit 1: replace each listed place by the
   path from the repository's root, or by a description of what the note or the place is, the whole
   path to the end of the phrase that names it (a path with a space in it is printed to the
   space), and run both checks again, until both exit 0. Exit 2 is no listing: fix the call, or the
   file that could not be read. Commit messages are not checked.
6. Publish the file that passed, with `gh pr create --body-file` or `gh pr edit --body-file`, or the
   host's equivalent. Each later edit of the description — the record's link by its SHA, a
   correction — is checked again by both checks before it is published. The edit that adds the
   record's link also fills in *Checks* with the runs of the three checks on the copy of the record,
   which did not exist when the description was first written. Record the last run of
   each, command and exit code, with the number of runs, in the record's *Request handoff*
   (*Description*).

**An error you hold wrong.** The language measure can read a correct block, or a task document
full of quoted English names, as English, and the script itself can err. Where you hold a reported
error wrong, with evidence you can name (WAY-291):

1. Do not change the description to silence it: never write `none` into the block, and never put
   the block into English, on a language error you hold wrong.
2. Run the script once more on the final file, so that the error stands as the check's result.
3. Publish that file; the request opens, or stays, a draft. The first line reads
   `**State: draft** — the form check reports an error the cycle holds wrong`, or keeps `blocked`
   where the request is blocked for another cause.
4. Add to *You accept by merging* one item of kind 15: what the script reported, in plain words,
   and why the cycle holds it wrong.
5. Name the check under *Checks*: its command, its exit code and its reported line. A failed check
   is named, never passed (WAY-160).
6. Copy the case into the record's process remarks: it is a matter of the-way's script, not of the
   product.

## The skeleton

The headings stand in this order and at this level; the script holds the same list. A section
with no content reads `none`, and never disappears. The one exception is the heading of the task's
own sections, which is omitted where the task has none (the skeleton's `## <…>` heading). The
three group headings stand in *For you to decide* in every request, each with its items or `none`;
only where no group has an item does the section read `none` alone, with no group heading.

```markdown
**State: <ready|draft|blocked>** — <why, in one sentence>

## What you will see

<the whole change in plain words, what the task announced included>

### Underneath

<one or two sentences on what is under the change>

## For you to decide

### Needed from you

<numbered items, or none>

### Fix or let through

<numbered items, or none>

### You accept by merging

<the sentence that merging accepts these items, then numbered items, or none>

## Cost

<time, models and tokens, review rounds, link to the table of stages>

## How to merge

<the merge that keeps the commits, and why; the reminder of a review of the foundation where the count asks for it>

<details>
<summary><"In your language", in the task document's language></summary>

<the state line and the four sections above in the task document's language, their headings
translated; none where the task document is in English>

</details>

## Technical changes

<…>

## Checks

<…>

## Foundation entries

<…>

## Minor findings

<…>

## Findings outside the task's scope

<…>

## <…>

<each of the task's own sections under its own heading, here and only here. Where the task has no
sections of its own, omit this heading altogether: it is not written with `none`>

## Course of the cycle

- **Task and sources:** <…>
- **Process pin:** <…>
- **Spec:** <…>
- **Route:** <…>
- **Plan:** <…>
- **Choices:** <…>
- **Blocking findings left:** <…>
- **Record:** <…>
```

## The two parts and the language

- The whole description is in English. Its **top part** — the state line through *How to merge* —
  is written for the human in plain words, with no file names and no identifiers of entries
  (WAY-286). The **block** repeats the top part in the task document's language, the headings
  translated, the three group headings of *For you to decide* among them, directly after *How to
  merge*; where the task document is in English, the block holds only `none` after its summary
  (WAY-288, WAY-292).
- The **lower part** — *Technical changes* through *Course of the cycle* — holds the evidence for
  agents and for a human who checks closely. Each of its items opens with a sentence a human
  understands without the code: what it concerns, what was not checked or what can break, and how
  much that matters; the places in the code and the identifiers follow (WAY-286).

## The top part

**The state line.** The first line, no heading. `ready` for a request marked ready for review;
`blocked` for a blocked draft, whatever the cause; `draft` for a draft left so for another reason
the line names. After the dash, why, in one sentence; for `ready`, whether any item of *Needed from
you* or *Fix or let through* below waits for the human's answer; what the human only accepts by
merging waits for nothing.

**What you will see.** The whole change in plain words, what the task announced included: in a
product, what its user sees; in the-way, how the work with the process changes. Where the change
alters what a screen shows, the screenshots that the author or the reviewer shows the human stand
here as images, each from the place the product's foundation settles for screenshots, which the
reports name; no file of the repository or of the record's copy is linked as an image (WAY-316).
Where the foundation settles no such place, no screenshot is shown, and *For you to decide* says so
(WAY-317). Of the artifacts of the check only screenshots reach the description: describe motion in
words, and leave logs and outputs in the reports (WAY-318). *Underneath*: one or two sentences on
what is under the change.

**For you to decide.** Everything whose merge needs the human's yes, and nothing else, in three
groups under headings of their own (WAY-287). The three groups stand in every request, in this
order, and a group with no item reads `none`; where no group has an item, the section reads `none`
alone, with no group heading, and that `none` means that nothing below waits for a yes. The items
are numbered in one run from 1 through the three groups, and the numbering does not start again in
a group. Each item says in plain words what the human is asked to accept or answer; an item whose
evidence stands in the lower part ends with a pointer by section and number, such as "(Minor
findings, 3)", never a file name or an identifier. The groups:

- **`### Needed from you`.** Without the human's answer or action the request cannot go on.
- **`### Fix or let through`.** Something the cycle did not do, or did not fix, and that can still
  be done in this request. The human answers: do it in this request, make a task of it, or let it
  through. What "do it in this request" runs for each kind of item stands under that kind below
  and in `correction.md`. Where the thing cannot be done in this request, and for whatever a
  correction left unfixed or undone, the item carries only the question "Make a task of it?"; the
  human who makes no task lets it through by merging (WAY-289).
- **`### You accept by merging`.** What the cycle did within its authority. The merge is the
  human's agreement, and no item waits for a separate answer. Where the group holds an item, it
  opens with one sentence saying that merging accepts these items and that the human says which
  one does not suit; a group with no item reads `none` alone, without that sentence.

**The kinds of items.** Each kind has a number, and other files name a kind by that number, such as
"item 8 of the template". The number of a kind is not the number of an item in a description, which
runs from 1 in the description. A kind stands in the group below, and the items of a group come in
the order of their kinds.

*Needed from you*

- **1.** *What a blocked request needs to go on*, from the cause that blocked it (the variants
  below), and the stages the cycle did not run because it stopped there — the return step, the
  reconciliation, the slices not made, the review of the whole change. They stand here, since they
  cannot be run until the human decides, and kind 4 does not list them again.
- **2.** *Questions*: only those the foundation step allows, which
  `task-cycle/skill/foundation_step.md` says, and a reserved choice, each with its options and a
  recommendation where one exists, from the report of the agent that returned `blocked` or
  `reserved`.
- **3.** *Human actions*: each action the task document places in the cycle, as the document names
  it, and each effect outside the repository the cycle found that the document does not name, for
  the human to place (WAY-140); from the task's *Human actions*, the Events and the reports. The
  item says what to do, why the request needs it and what happens without it.

*Fix or let through*

- **4.** *Skipped steps and unrun checks*, from the record's *Verification*, Events and *Return
  step*: a stage the cycle skill requires for this change that did not run or was skipped — the
  return step, a review, the reconciliation with the target branch, a slice not made, the gate; a
  check of the final gate run that failed or did not run, save one that fails on the base too, which
  stays in *Checks*; a check the change needed that an author reports as not done — a screenshot
  unchecked (WAY-219), a missing state check or a missing own-work check (WAY-164). A check the
  skill does not call for this change is none, and a check that failed and passed again stays in
  *Checks* (WAY-261). The stages a blocked request did not run because it stopped are kind 1's, not
  these. The answer "do it in this request" runs the step or the check that was left out.
- **8.** *Unfixed findings the user or the human will feel* (WAY-289): read each Minor finding that
  no fix made and each finding outside the task's scope, of the review of the whole change and of
  every later review, and each Minor finding and new serious finding of a reverted fix, and judge
  from the whole record — the reports of the walk through the running product and the screenshots
  included — whether the product's user or the human working with the process will feel it. Restate
  each such finding in plain words, with the question whether to fix it in this request, make a task
  of it or let it through; one answer may cover the whole list. The answer to fix it runs a
  correction with one fix and one review of that fix (`correction.md`). In the description after
  that correction, a finding it left unfixed carries only "Make a task of it?", or stays in the
  lower part, as anything else a correction left undone does. The finding stays in its list below,
  with its kind and grade; the judgment decides no fix and no block.
- **9.** *Decisions of the task's own sections*: each item of those sections that waits on a yes,
  such as a proposal not applied. The answer "do it in this request" applies the proposal.
- **14.** *An incomplete reading by the review of the whole change* (WAY-326, WAY-287), from the
  **Unread material** of that review's report and of its fix review's, and from the record: where
  the reviewer did not run through the rest of its selection by title, or itself named a decision
  concerning the change as unread, and the gap was not closed on the way, by the reviewer or a fresh
  one reading what stayed unread: in plain words how much of what it selected it read whole, such as
  "The review of the whole change read 40 of 151 selected decisions whole". The answer "do it in
  this request" has a fresh reviewer read what stayed unread. A reviewer that read whole the
  decisions concerning the change, ran through the rest by title and named none unread gives no
  item, since that reading is the practice (WAY-150).
- **16.** *Something an entry stands on that the foundation does not hold yet* (WAY-71, WAY-287),
  from the invariants file and the decision log of the tree after the change: each descriptive
  `TODO` — `TODO — <the fact, with its source>` in an invariant's *Rests on*,
  `TODO — <the decision, and where it is expected>` in an invariant's *Derives from*,
  `TODO — <what is missing, with its source>` in a decision's *Based on* — that stands there; the
  change writes it, keeps it or does not remove it. A `TODO` that closes a value after known entries
  (`<fact> · TODO — …`) is the same gap: one item, naming what is missing alone, not the known
  entries. One item for each gap, in plain words: the rule the invariant states or the question the
  decision answers, and what is missing. The answer "do it in this request" has the missing fact,
  decision or source written in this request; "make a task of it" leaves the gap standing; letting it
  through accepts it on the main branch. A request therefore carries one such item for as long as an
  old gap stands.

*You accept by merging*

- **5.** *Choices of the cycle beyond the task's content*: a choice the task document, its sources
  and the foundation do not settle, where another answer would change what the product's user sees
  or does, what the human meets when working with the process, or what the foundation binds. Look in
  the spec's *Decisions*, the answers to the task's *Questions carried to cycle* among them; in the
  rows of the questions table answered by an autonomous choice, or by a ruling that reads an item of
  the task wider or narrower than its words; in the departures from the task's wording an agent's
  report names; in a choice of how to make the change whose result the user or the human will see or
  feel, such as the look of a screen the task does not fix; and in a kept row tied to an entry
  already stated, which writes no entry (WAY-134). A row a binding source answered is none, and so
  is a choice of how to make what the task settles, unless its result shows as above; these are the
  count under **Choices**.
- **6.** *Foundation entries the human did not see at the task document*: each with one plain
  sentence of its meaning, repeated in the block in the task document's language (WAY-114) — those
  the foundation step's and return step's reports mark `the cycle's`: entries written from the spec
  or by the return step, corrections the search of the whole foundation made, the part of a
  projected entry the code makes true, and a precedence between two decisions the cycle recorded,
  which gives beside its sentence the passages of what the human accepted that give the outcome,
  quoted from the report of the step that wrote it (WAY-25). Entries written whole from rows of
  *Settlements to record*, and projected entries written whole as approved, are not here; they stand
  under *Foundation entries*.
- **7.** *Changed invariant tests, surfaces and Violated marks*, in plain words (WAY-03, WAY-49,
  WAY-51), from the changed files read against the invariants file and the part map, and from the
  record's *Return step*.
- **10.** *A listing of the remarks check held wrong*, where the cycle holds an item the check
  listed to be an error of the script (WAY-295): in plain words what the script listed and why the
  cycle holds it wrong. The script is not changed in the cycle, and the archive is written; the case
  also stands in the record's process remarks, as `SKILL.md` ("The process remarks check") gives.
- **11.** *Additions to a product's logging scope*: the author finds them in the diff of the change
  to the product's logging-scope rule (WAY-274); each item the change adds to the list of what the
  product logs, in plain words — what it is and which log line carries it. A change that adds
  nothing to that list has no such item.
- **12.** *A relation line the cleaning rewrote* (`SKILL.md`, "The record before it is committed",
  WAY-308), where the check of private paths listed the `Task relation:` line of the record or the
  `Project relation:` line of the task copy and the cycle cleaned it: in plain words which of the
  two lines it was, never its text, and that the reader of a project plan's state may now report a
  conflict for this task.
- **13.** *No screenshot of a changed screen* (WAY-317), where the change alters what a screen
  shows, the author inspected a screenshot, and the product's foundation settles no place for
  screenshots, so the request shows none: in plain words that the screen was looked at and is not
  shown, and that the product has settled no place for screenshots. A screenshot left unchecked for
  want of a settled way to the running product stands in item 4 and takes no item here.
- **15.** *A form error held wrong* ("An error you hold wrong", above): in plain words what the
  script reported and why the cycle holds it wrong.
- **17.** *The cause of a correction* (WAY-287, WAY-356), in the description after a correction: one
  sentence, from the pairs `source · kind` of the correction's line in the record, that says in
  plain words what started the correction — your remarks, your answer to an item of this request,
  or only the refreshing of the target branch — and whether the cycle judged that the task or the
  foundation required what the correction changed, or did not, so that you see that judgment at
  the merge. For `target-branch · none` the cycle judged nothing, and the sentence says so, such as
  "This correction only refreshed the branch from the target branch at your request; nothing else
  changed, and the cycle made no judgment of whether the task required anything." Where a correction
  has two sources, the one sentence carries each pair once, such as "This correction answered your
  remark about a defect the task required, and it refreshed the branch from the target branch at
  your request, which the cycle judged nothing about."

**What an item carries.**

- An item in which the human chooses — each item of *Needed from you* and of *Fix or let through*
  but one that asks for an action outside the repository — has four parts, and the agent that
  writes the description checks every such item against them and fills what is missing before it
  checks the form (WAY-327):
  1. what happens, concretely: who will feel it — the product's user or the person working with the
     process — when and in what situation; with no name of a step of the process and no number of
     an entry, and a name that cannot be avoided followed, at its first mention, by one sentence on
     what it is;
  2. each way open, one by one: what happens once it is chosen, what it costs — time, a round of
     correction with its review, the risk that stays — and where it can show up later;
  3. the recommendation, with its reason in one sentence;
  4. the question, with the answers to choose from.
- An item of *Needed from you* that asks for an action outside the repository (kind 3) says what to
  do, why the request needs it and what happens without it.
- An item of *You accept by merging* says what the cycle chose or wrote and why, in plain words,
  and where it had another way, in one sentence why it did not take it.

A bad item and a good one. The bad item leaves the human to ask what happened, who will feel it,
what each answer costs and what the writer would do:

> 1. The return step was skipped on your instruction; merge without it?

The good item, with its group around it, for a change to the restore instruction of a product's
server:

```markdown
## For you to decide

### Needed from you

none

### Fix or let through

1. Some parts of the new restore instruction were never tried: the way back after a failed check,
   a second attempt after a failed one, and the use of the old encryption key. If one of them is
   wrong, whoever restores the server finds out on the day of a real failure, not before. Trying
   them now costs another session on the test server and a round of review; merging now costs
   nothing today, and the instruction marks each untried part in its own text. I recommend letting
   it through, since the common path was tried from the first step to the last. Try them in this
   request, make a task of a separate trial, or let it through?

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The instruction takes the newest backup by the time of its file, not by the backup log: on a new
   server the log is gone, and that is when someone restores. The price is fetching up to seven
   backups instead of one.
```

**Cost.** The time, the models and the tokens from `stages.md`, the number of review rounds, and
the link to the table of stages in the committed record. For a blocked request, the cost so far.

**How to merge.** A merge that keeps the commits, since the link to the record survives only then;
where the product's rules squash or rebase, that limitation named. For a blocked request, what to do
instead of merging.

Where the count of `SKILL.md` step 13 reads `reminder: yes`, *How to merge* ends with the reminder
(WAY-300): in plain words, that the foundation has waited for a review through the number of merges
the script gives since the tag of the last review, or since the start of the history where the
script gives no tag; that the review is the skill `the-way-review-foundation`, started in a session
in this repository; and that nothing in this request waits for it. The reminder is no item of *For
you to decide*, as it asks for no yes to the merge, and it repeats in the block like the rest of
*How to merge*. Where the count reads `reminder: no`, nothing is written.

## The lower part

**Technical changes.** What changed and why, by commit or by group of files; the fix for Minor
findings among them, and where the cycle reverted it, its commits and the revert commit (WAY-162).

**Checks.** The gate's command and exit code, each check that failed or did not run by name, and
for a check that failed and passed when run again the number of cycle runs in which it failed and
passed and its rerun's result (WAY-160, WAY-261); what each own-work check showed (WAY-164); the
user-interface states and the screenshot evidence, a screenshot unchecked for no settled way or the
failure of a settled one included (WAY-219); the form check's last run; the check of private
paths' last run on the description and its last run on the copy of the record, each with its
command and exit code (WAY-309); the image check's last run on the copy of the record, with its
command and exit code (WAY-316); the remarks check's last run on the original and on the copy,
and where it listed an item the cycle holds wrong, its command, exit code and listed line
(WAY-295).

**Foundation entries.** Each foundation entry the change writes or changes, by its identifier and
one English sentence of its meaning, marked `row <n>`, `projected` or `the cycle's`; each kept row
tied to an entry already stated, with that entry (WAY-134); each invariant test the change alters
(WAY-03), each surface it alters (WAY-49) and each *Violated* mark it sets or clears (WAY-51).

**Minor findings.** The Minor findings that no fix made — those of the review of the whole change
that its fix left or did not take in, those of every later review, and those a reverted fix tried —
each with the reviewer's words and its place in the code, or a note that the reviewer names none
(WAY-161). Beside them, the new Critical or Important finding of a reverted fix, marked with its
grade and as found by the review of the reverted fix, with the reviewer's words and its place in
the code (WAY-162).

**Findings outside the task's scope.** The findings the reviewers marked outside the task's scope,
each the same way, for the human to choose which become new tasks and to create them (WAY-161);
beside them, each check whose file belongs to a part outside the task's parts that failed in a cycle
run and passed again, with its file path, its rerun's result and its counts (WAY-261).

**The task's own sections.** Each section the task document keeps of its own, under its own heading,
here; what in it waits on a yes also stands in *For you to decide*.

**Course of the cycle.** The labels, in this order:

- **Task and sources:** the task's goal and relation, the source revisions it used.
- **Process pin:** the pin, or where the task moved it, from and to which commit, with the gate on
  that commit.
- **Spec:** whether a spec was written and why, with its link.
- **Route:** the route and its reason; after a discarded attempt, its reason and the agent's report.
- **Plan:** the plan's link and its slices, where one was written.
- **Choices:** the number of the cycle's other choices, with the link to the questions table.
- **Blocking findings left:** each blocking finding left after the review of its fix, with its
  place in the code, its reason and what the fix tried (WAY-162).
- **Record:** the link to the record by the SHA of the commit that adds it.

## The variants

Every variant keeps every heading, save the heading of the task's own sections where the task has
none; a section with no content reads `none`, and a group of *For you to decide* with no item
reads `none` under its heading.

| Variant | First line | *For you to decide* | Lower part |
|---|---|---|---|
| A blocking finding remains (`blocked_finding.md`, WAY-162, WAY-163) | `**State: blocked** — a review finding remained after its one fix` | in *Needed from you*, each remaining finding in plain words, with "Fix it as the finding says, or keep the code despite it?"; what has not run on that code — the return step, the reconciliation, the slices not made | **Blocking findings left**: each with its place, reason and what the fix tried; *Cost* the cost so far with the rounds; *Checks* naming what has not run |
| A slice failed twice (step 9.4) | `**State: blocked** — a slice failed with two agents` | in *Needed from you*, what failed, in plain words, and what the cycle needs to go on; the stages not run — the review of the whole change, the return step, the reconciliation | **Route**: both failures with the classes tried, each slice made that no review judged |
| A reserved choice (`reserved_return.md`, WAY-269) | `**State: blocked** — the cycle met a technology choice only you make` | in *Needed from you*, the choice, by what the product needs it for; the ways seen, marked as not researched, with no recommendation; what happens next: close the request, and refinement takes the choice as its note | *Technical changes* `none`; *Foundation entries* `none`; *Checks*: the checks failing on the base and each stage not run with why, the gate among them; **Route**: where it showed (stage, task item), the limb of the rule, what was searched, the discarded attempt and its report; *How to merge*: do not merge, close |
| Human actions in the cycle (WAY-140) | `**State: blocked** — waits for your actions outside the repository` | in *Needed from you*, each action as the task names it; each found effect, for the human to place | as an ordinary request |
| A question from the foundation step | `**State: blocked** — needs your answer` | in *Needed from you*, the question with its options and a recommendation where one exists | as an ordinary request |
| An impossible task | `**State: blocked** — <the smallest missing fact or permission>` | in *Needed from you*, that fact or permission; never partial work presented as complete | **Route**: the ways tried |
| A correction (`correction.md`) | the state after the correction, with "corrected for your remarks" in the why | the items as they stand after the correction, each in its group, its new choices included, and the pairs of the correction as item 17 in *You accept by merging*; a remark is no item, since it binds; what a correction left unfixed or undone, whether it ran on an answer to item 8, 4, 9 or 14, carries only "Make a task of it?" | *Course of the cycle*: each correction with the link to its remarks and its reset base; *Cost* across all sessions |
| A correction met a reserved choice | `**State: blocked**`, as for a reserved choice | as for a reserved choice | *Foundation entries* as in the request's previous description |
| A form error held wrong (above) | `**State: draft** — the form check reports an error the cycle holds wrong`; a request blocked for another cause stays `blocked` and gains only the item | in *You accept by merging*, item 15: the reported error in plain words and why the cycle holds it wrong | *Checks*: the form check's command, exit code and reported line |
| A remarks listing held wrong (`SKILL.md`, "The process remarks check", WAY-295) | unchanged: the state the request has for its other causes | in *You accept by merging*, the listing as item 10 | *Checks*: the remarks check's command, exit code and listed line |
| A draft for another reason | `**State: draft** — <reason>` | the reason as an item of the group it belongs to, such as a skipped step (item 4) in *Fix or let through*, written as "What an item carries" gives | as an ordinary request |
