# The description of a request

Read by the orchestrator of `implement-task` wherever it writes or rewrites a request's
description — step 13, a slice failed twice at step 9.4, `blocked_finding.md`, `reserved_return.md`
and `correction.md` — and by the agent leading a change to the-way that `agent-instructions/README.md`
sends here. Every request of a cycle, blocked, reserved or corrected, has this one skeleton
(WAY-286, WAY-287).

## Write, check, publish

1. Write the description into `.runs/task-cycles/<task-slug>/request.md`, beside the record.
2. Check its form, from the worktree's root — in a product, the path starts with `.the-way/`:

   ```
   python -B task-cycle/request_check.py .runs/task-cycles/<task-slug>/request.md --task <frozen task>
   ```

   `--task` is the frozen task document of the record. The script checks the headings, content or
   `none` in each section and the block's language, and judges no content (WAY-290).
3. Exit 1 lists each problem as `line <n>: <what is wrong and what to write>`. Correct the file at
   each line and run the script again, until it exits 0. Exit 2 is no error of the form: fix the
   call, or the file that could not be read.
4. Publish the file that passed, with `gh pr create --body-file` or `gh pr edit --body-file`, or the
   host's equivalent. Each later edit of the description — the record's link by its SHA, a
   correction — is checked again before it is published. Record the last run, command and exit
   code, with the number of runs, in the record's *Request handoff* (*Description*).

**An error you hold wrong.** The language measure can read a correct block, or a task document
full of quoted English names, as English, and the script itself can err. Where you hold a reported
error wrong, with evidence you can name (WAY-291):

1. Do not change the description to silence it: never write `none` into the block, and never put
   the block into English, on a language error you hold wrong.
2. Run the script once more on the final file, so that the error stands as the check's result.
3. Publish that file; the request opens, or stays, a draft. The first line reads
   `**State: draft** — the form check reports an error the cycle holds wrong`, or keeps `blocked`
   where the request is blocked for another cause.
4. Add to *For you to decide* one item: what the script reported, in plain words; why the cycle
   holds it wrong; "Merge as it stands?".
5. Name the check under *Checks*: its command, its exit code and its reported line. A failed check
   is named, never passed (WAY-160).
6. Copy the case into the record's process remarks: it is a matter of the-way's script, not of the
   product.

## The skeleton

The headings stand in this order and at this level; the script holds the same list. A section
with no content reads `none`, and never disappears. The one exception is the heading of the task's
own sections, which is omitted where the task has none (the skeleton's `## <…>` heading).

```markdown
**State: <ready|draft|blocked>** — <why, in one sentence>

## What you will see

<the whole change in plain words, what the task announced included>

### Underneath

<one or two sentences on what is under the change>

## For you to decide

<a numbered list, or none>

## Cost

<time, models and tokens, review rounds, link to the table of stages>

## How to merge

<the merge that keeps the commits, and why>

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
  (WAY-286). The **block** repeats the top part in the task document's
  language, the headings translated, directly after *How to merge*; where the task document is in
  English, the block holds only `none` after its summary (WAY-288, WAY-292).
- The **lower part** — *Technical changes* through *Course of the cycle* — holds the evidence for
  agents and for a human who checks closely. Each of its items opens with a sentence a human
  understands without the code: what it concerns, what was not checked or what can break, and how
  much that matters; the places in the code and the identifiers follow (WAY-286).

## The top part

**The state line.** The first line, no heading. `ready` for a request marked ready for review;
`blocked` for a blocked draft, whatever the cause; `draft` for a draft left so for another reason
the line names. After the dash, why, in one sentence; for `ready`, whether anything waits below.

**What you will see.** The whole change in plain words, what the task announced included: in a
product, what its user sees, with screenshots; in the-way, how the work with the process changes.
*Underneath*: one or two sentences on what is under the change.

**For you to decide.** Everything whose merge needs the human's yes, and nothing else: its `none`
means that nothing below waits for a yes (WAY-287). Each item says in plain words what the human
is asked to accept or answer, then the question — "Merge without it?", "Make a task of it?",
"Accept?". An item whose evidence stands in the lower part ends with a pointer by section and
number, such as "(Minor findings, 3)", never a file name or an identifier. The items, in this
order:

1. *What a blocked request needs to go on*, from the cause that blocked it (the variants below).
2. *Questions*: only those the foundation step allows, and a reserved choice, each with its options
   and a recommendation where one exists, from the report of the agent that returned `blocked` or
   `reserved`.
3. *Human actions*: each action the task document places in the cycle, as the document names it,
   and each effect outside the repository the cycle found that the document does not name, for the
   human to place (WAY-140); from the task's *Human actions*, the Events and the reports.
4. *Skipped steps and unrun checks*, from the record's *Verification*, Events and *Return step*: a
   stage the cycle skill requires for this change that did not run or was skipped — the return
   step, a review, the reconciliation with the target branch, a slice not made, the gate; a check
   of the final gate run that failed or did not run, save one that fails on the base too, which
   stays in *Checks*; a check the change needed that an author reports as not done — a screenshot
   unchecked (WAY-219), a missing state check or a missing own-work check (WAY-164). A check the
   skill does not call for this change is none, and a check that failed and passed again stays in
   *Checks* (WAY-261).
5. *Choices of the cycle beyond the task's content*: a choice the task document, its sources and the
   foundation do not settle, where another answer would change what the product's user sees or
   does, what the human meets when working with the process, or what the foundation binds. Look in
   the spec's *Decisions*, the answers to the task's *Questions carried to cycle* among them; in the
   rows of the questions table answered by an autonomous choice, or by a ruling that reads an item
   of the task wider or narrower than its words; in the departures from the task's wording an
   agent's report names; in a choice of how to make the change whose result the user or the human
   will see or feel, such as the look of a screen the task does not fix; and in a kept row tied to
   an entry already stated, which writes no entry (WAY-134). A row a binding source answered is
   none, and so is a choice of how to make what the task settles, unless its result shows as above;
   these are the count under **Choices**.
6. *Foundation entries the human did not see at the task document*: each with one plain sentence of
   its meaning, repeated in the block in the task document's language (WAY-114) — those the
   foundation step's and return step's reports mark `the cycle's`: entries written from the spec or
   by the return step, corrections the search of the whole foundation made, the part of a projected
   entry the code makes true. Entries written whole from rows of *Settlements to record*, and
   projected entries written whole as approved, are not here; they stand under *Foundation
   entries*.
7. *Changed invariant tests, surfaces and Violated marks*, in plain words (WAY-03, WAY-49,
   WAY-51), from the changed files read against the invariants file and the part map, and from the
   record's *Return step*.
8. *Unfixed findings the user or the human will feel* (WAY-289): read each Minor finding and each
   finding outside the task's scope, of the review of the whole change and of every later review,
   and judge from the whole record — the reports of the walk through the running product and the
   screenshots included — whether the product's user or the human working with the process will
   feel it. Restate each such finding in plain words, with "Make a task of it?". The finding stays
   in its list below, with its kind and grade; the judgment decides no fix and no block.
9. *Decisions of the task's own sections*: each item of those sections that waits on a yes, such as
   a proposal not applied.
10. *Additions to a product's logging scope*: each item the change adds to the list of what the
    product logs, in plain words — what it is and which log line carries it — with "Accept it?".
    A change that adds nothing to that list has no such item.

**Cost.** The time, the models and the tokens from `stages.md`, the number of review rounds, and
the link to the table of stages in the committed record. For a blocked request, the cost so far.

**How to merge.** A merge that keeps the commits, since the link to the record survives only then;
where the product's rules squash or rebase, that limitation named. For a blocked request, what to do
instead of merging.

## The lower part

**Technical changes.** What changed and why, by commit or by group of files.

**Checks.** The gate's command and exit code, each check that failed or did not run by name, and
for a check that failed and passed when run again the number of cycle runs in which it failed and
passed and its rerun's result (WAY-160, WAY-261); what each own-work check showed (WAY-164); the
user-interface states and the screenshot evidence, a screenshot unchecked for no settled way or the
failure of a settled one included (WAY-219); the form check's last run.

**Foundation entries.** Each foundation entry the change writes or changes, by its identifier and
one English sentence of its meaning, marked `row <n>`, `projected` or `the cycle's`; each kept row
tied to an entry already stated, with that entry (WAY-134); each invariant test the change alters
(WAY-03), each surface it alters (WAY-49) and each *Violated* mark it sets or clears (WAY-51).

**Minor findings.** The Minor findings of the review of the whole change and of every later review,
each with the reviewer's words and its place in the code, or a note that the reviewer names none
(WAY-161).

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
none; a section with no content reads `none`.

| Variant | First line | *For you to decide* | Lower part |
|---|---|---|---|
| A blocking finding remains (`blocked_finding.md`, WAY-162, WAY-163) | `**State: blocked** — a review finding remained after its one fix` | each remaining finding in plain words, with "Fix it as the finding says, or keep the code despite it?"; what has not run on that code — the return step, the reconciliation, the slices not made | **Blocking findings left**: each with its place, reason and what the fix tried; *Cost* the cost so far with the rounds; *Checks* naming what has not run |
| A slice failed twice (step 9.4) | `**State: blocked** — a slice failed with two agents` | what failed, in plain words, and what the cycle needs to go on; the stages not run — the review of the whole change, the return step, the reconciliation | **Route**: both failures with the classes tried, each slice made that no review judged |
| A reserved choice (`reserved_return.md`, WAY-269) | `**State: blocked** — the cycle met a technology choice only you make` | the choice, by what the product needs it for; the ways seen, marked as not researched, with no recommendation; what happens next: close the request, and refinement takes the choice as its note | *Technical changes* `none`; *Foundation entries* `none`; *Checks*: the checks failing on the base and each stage not run with why, the gate among them; **Route**: where it showed (stage, task item), the limb of the rule, what was searched, the discarded attempt and its report; *How to merge*: do not merge, close |
| Human actions in the cycle (WAY-140) | `**State: blocked** — waits for your actions outside the repository` | each action as the task names it; each found effect, for the human to place | as an ordinary request |
| A question from the foundation step | `**State: blocked** — needs your answer` | the question with its options and a recommendation where one exists | as an ordinary request |
| An impossible task | `**State: blocked** — <the smallest missing fact or permission>` | that fact or permission; never partial work presented as complete | **Route**: the ways tried |
| A correction (`correction.md`) | the state after the correction, with "corrected for your remarks" in the why | the items as they stand after the correction, its new choices included; a remark is no item, since it binds | *Course of the cycle*: each correction with the link to its remarks and its reset base; *Cost* across all sessions |
| A correction met a reserved choice | `**State: blocked**`, as for a reserved choice | as for a reserved choice | *Foundation entries* as in the request's previous description |
| A form error held wrong (above) | `**State: draft** — the form check reports an error the cycle holds wrong`; a request blocked for another cause stays `blocked` and gains only the item | the reported error in plain words, why the cycle holds it wrong, and "Merge as it stands?" | *Checks*: the form check's command, exit code and reported line |
| A draft for another reason | `**State: draft** — <reason>` | the reason as an item, such as "the return step was skipped on your instruction; merge without it?" | as an ordinary request |
