# Spec — Opis PR-a z cyklu the way ma stały schemat: na górze to, co Mariusz rozstrzyga, niżej archiwum

- Task: `docs/task-cycles/pr-description-schema/task.md` (frozen 2026-11-05, citations at
  `foundations` `f45ca40`)
- Open choice: the English headings of the request template, in fixed order and level (the task's
  *Questions carried to cycle*); where the template stands and how the cycle's files point to it;
  what the record's *Request handoff* keeps; the form check script (path, interface, what it judges,
  where the cycle runs it); what fills the section for the human's decisions and from where; the
  form of the foundation entries rows 1–6 enter as; the blocked, reserved and corrected variants;
  the-way's own requests.

## Intent

A request a task cycle opens gets one description shape. The top part is written for the human in
plain words: the state, what changes, everything that waits for the human's yes, the cost and how to
merge. It is repeated in the task document's language in a collapsed block. Below it, the lower part
holds the evidence for agents and for a human who checks closely, in a fixed order. One template
replaces the lists that step 13 of the cycle skill, the record template and five other files keep
today. A script checks the form before the request opens, so a missing or misplaced section is
caught before the human reads it. The foundation records the new shape, and WAY-114, WAY-134 and
WAY-10 change so that the merge accepts only what the human has not already accepted with the
task document.

"Top part" and "lower part" are this spec's names, used in the template and the entries in place of
the task's "archiwum". "Archive" is avoided because `project-level/plan_state.py` already uses it
for the committed record directory, and because it would be a word with a meaning of its own in the
the-way (a glossary candidate). Neither name is a heading.

## Goals and non-goals

Goals:

- One template file holds the request description's skeleton, what each section holds and where the
  orchestrator takes it from. Every other file that lists request content points to it (To do 1).
- The top part and lower part as To do 2–6 give them, with the headings settled below.
- The section for the human's decisions is filled from named places in the record and the reports,
  so that its `none` means nothing else waits (To do 3, 7, rows 2, 5).
- A form check script with tests that the gate runs. The cycle runs it and corrects the description
  until it reports no error (To do 9, row 6).
- Foundation entries for rows 1–6. WAY-114, WAY-134 and WAY-10 change as To do 8 gives them.
- The nightly digest keeps getting the "Process remarks" block from the record.

Non-goals:

- Where screenshots and other test artifacts live, and the weekly review of the lower parts'
  findings (task *Out of scope*).
- Judging content by script. The script does not check that the decision section is complete or
  true, that the top part uses plain words and no file names or identifiers, that the block says
  what the English top part says, which non-English language the block is in, the first-sentence
  form of lower-part items, or the content of the task's own sections. To do 9 lists three checks;
  the script does those three, plus the state line, which is the top part's first item.
- A mark in the questions table for "beyond the task". The orchestrator selects such rows when it
  writes the request (Decision 5). This leaves *Questions and autonomous choices* in
  `task-cycle/record_template.md` untouched. The collective task changes that section (task
  *Context*).
- A second agent comparing the description with the record (rejected in the task).
- Any change to the review skill, the grades or the kinds of findings.
- A declared language field in the task document template.

## Constraints

- The task's To do 1–9, its answers and rows 1–6 bind. *Checks* stays as a heading (WAY-261).
- WAY-256: a template that several steps consult stands in a file beside the skill, and each step
  that uses it names it. The request template is no rule of an element's entries, so WAY-35 places
  it nowhere else.
- WAY-161: the request lists the Minor findings in one item and the findings outside the task's
  scope in another, each with the reviewer's words and its place in the code. The orchestrator moves
  no finding from one kind to another.
- WAY-162, WAY-163: a blocked request lists each remaining blocking finding with its place and
  reason, what the fix tried, the time, models and tokens so far with the number of review rounds,
  and what has not run on that code.
- WAY-269: a request a reserved choice blocks names the choice, says what did not run and why, and
  settles nothing. In the reserved path, the request opens on the commit that adds the record.
- WAY-03, WAY-49, WAY-51, WAY-140, WAY-160, WAY-164, WAY-219, WAY-261: the request names, lists or
  gives the items these decisions require. Each still holds once its item stands in the top part,
  the lower part or both (Decision 9).
- WAY-227: the request is the human's first point of review. The orchestrator's choices are
  provisional and never recorded as the human's approval.
- The decisions template (`elements/decisions/template.md`): one to three binding sentences. A new
  rule beside an existing decision is a new question (WAY-19). A decision written from a row takes
  as *Rejected* only the ways not chosen that the row's source keeps, otherwise `unknown`.
- Invariants `script-language`, `script-imports` and `script-subprocesses`: Python, standard library
  only, no program started. The house style of `task-cycle/cycle_stages.py` and
  `task-cycle/slice_size.py`: a module docstring that is the usage text, `main(argv) -> int`,
  argparse, `Error: <message>` on stderr, stdout reconfigured to UTF-8.
- `gate/run_tests.py` runs every directory that holds a `test_*.py` file git tracks.
  `task-cycle/` already holds tracked tests, so a new test file there runs once it is in the tree.
- `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py` reads
  `docs/task-cycles/<slug>/cycle.md`. In `extract_remark_blocks`, a block is a heading, a list item
  or a paragraph whose text starts with "process remark", "process improvements", "other process
  remarks" or "searches not found" (case ignored). A list item followed by a blank line and items
  at its level runs to the next heading. The record keeps such a block.
- `project-level/test_plan_state_invariant.py:186` and
  `project-level/test_plan_state_subprocesses_invariant.py:109-111` hold `## Request handoff` and
  `- Request URL and status:` in fixture data. `project-level/plan_state.py` finds a request by any
  pull or merge request link in the committed record (`record_pointers`), not by the heading. So the
  committed record has to hold the request URL. That is why step 12 opens the request before it
  commits the record.
- Trust boundary: none. The design changes no file the part map names as one, and the new script is
  no boundary (Decision 4). Operation that cannot be undone: none.
- The collective task (AIR-592 and its siblings) changes `task-cycle/skill/SKILL.md` near `:188` and
  `:287-289`, and the *Questions and autonomous choices* section of `task-cycle/record_template.md`.
  Its cycle goes first. This design changes `SKILL.md` steps 9.4, 12 and 13 and lines `:196` and
  `:353`, and in `record_template.md` only *Request handoff* and one sentence of *Artifacts*.

## Decisions

### D1 — The template's headings, order and level

The settled headings, in this order. They are the open choice the task carried to the cycle, so they
are named here word for word. `##` marks a section and `###` a subsection.

**Top part**

1. The first line of the description, no heading: `**State: <ready|draft|blocked>** — <why>`. The
   three words are fixed: `ready` for a request marked ready for review, `blocked` for a blocked
   draft (any cause), and `draft` for a draft left so for another named reason, such as a step
   skipped on the human's instruction. The text after the dash says why in one sentence. For
   `ready`, that is whether anything waits below.
2. `## What you will see`: the whole change in plain words, what the task announced included (row 1,
   the condition of the WAY-114 answer). In a product, what its user sees, with screenshots; in the
   the-way, how the work with the process changes.
   - `### Underneath`: one or two sentences on what is under the change.
3. `## For you to decide`: Decision 5 gives its content. A numbered list, or `none`.
4. `## Cost`: time, models and tokens from `stages.md`, the number of review rounds and the link to
   the table of stages. For a blocked request, these are the cost so far.
5. `## How to merge`: the merge that keeps the commits and why, a host rule that squashes or
   rebases named as a limitation, or for a blocked request what to do instead of merging.
6. The block: a `<details>` element whose `<summary>` and content are in the task document's
   language. It repeats items 1–5 in that language, with the headings translated by the writer.
   It stands directly after the content of `## How to merge`, before the lower part. Where the task
   document is in English, the block holds only `none` after its summary.

**Lower part**, in this order:

7. `## Technical changes`
8. `## Checks`
9. `## Foundation entries`
10. `## Minor findings`
11. `## Findings outside the task's scope`
12. The task's own sections, each `## <its own heading>`, zero or more, in this slot only.
13. `## Course of the cycle`: a list whose items open with fixed bold labels, in this order:
    **Task and sources**, **Process pin**, **Spec**, **Route**, **Plan**, **Choices**,
    **Blocking findings left**, **Record**. The script does not check the labels.

Each item of the lower part opens with a sentence a human understands without the code: what it
concerns, what was not checked or what can break, and how much that matters. The places in the code
and the identifiers follow (To do 5). A section, subsection or block with no content reads `none`
(To do 6). The template states this; the script checks only content-or-`none`.

Why these words: "For you to decide" avoids "decision", which in the the-way names an entry of the
decision log. "Foundation entries" replaces *What this request settles*, which a human can read as
"what this request decides". "Findings outside the task's scope" keeps WAY-161's and WAY-261's
words.

*Rejected:*
- The block at the very end of the description, the literal reading of the task's "pod nim". The
  human would reach it only past the whole lower part.
- `### Underneath` as a bold label instead of a heading. The script could not check it the same way
  as the other sections.
- Each *Course of the cycle* item as its own heading. Eight more headings in the part only agents
  read.
- Keeping *What this request settles*.

Cost if wrong: renaming a heading costs one edit of the template, the script's constants and the
tests. Requests already merged keep the old words.

### D2 — Where the template stands and what each file keeps

The template is `task-cycle/skill/request_template.md`, a file beside the cycle skill (WAY-256). It
is text several steps consult (step 9.4's stop, steps 12–13, `blocked_finding.md`,
`reserved_return.md`, `correction.md`), so it is neither inline in `SKILL.md` nor in an element's
template. It holds:

- the skeleton of D1;
- for each section, what it holds and where the orchestrator takes it from (D5 for the decision
  section; for the others, what step 13 lists today, moved there);
- the rule for lower-part items;
- the variants of D7;
- the command of D4 and the correction loop.

`task-cycle/record_template.md` stays at `task-cycle/` (WAY-256 leaves an unchanged fragment
alone).

For each file:

| File | Keeps | Moves into the template | Points to instead |
|---|---|---|---|
| `task-cycle/skill/SKILL.md:390-425` (step 13) | One instruction: write the description into `.runs/task-cycles/<task-slug>/request.md` from the template, check it with the script and correct it until it passes, then publish it from that file. Recover the task's parts through the part map as WAY-261 gives, kept as a rule of the step. | Every list of what the request states, its *Checks*, its findings lists, *What this request settles*, *Questions*, human actions, blocked and impossible cases | the template |
| `SKILL.md` step 12 (`:376-389`) | Reconciliation, gate, and the record's commit pair. Order: run `cycle_stages.py` before the request opens, so *Cost* is real at opening; then step 13's check; open the draft from the file; write the URL into the record; copy, commit the pair and push; put the record's SHA link into *Course of the cycle*; check again; edit; mark ready unless the first line reads `blocked` or `draft` (D4, D7). | "Link the record in the request's description by the SHA…" and "ask for a merge that keeps its commits" become content of *Course of the cycle* and *How to merge* | template sections |
| `SKILL.md:300-303` (9.4 stop) | The stop and its order | "giving what step 13 names for a blocked request" | the template's variant for a slice failed twice |
| `SKILL.md:196` | The route to a blocked request | "under *Questions*… as step 13 gives for an impossible task" | *For you to decide*, as the template gives |
| `SKILL.md:353` | The rule that Minor and out-of-scope findings are not fixed | "goes to the request's lists (step 13)" | the lower part's lists the template gives |
| `task-cycle/record_template.md:163-191` | See D3 | — | — |
| `task-cycle/record_template.md:110-111` (*Artifacts*) | — | "the record keeps its meaning sentence for the request" becomes: the foundation step's report keeps the meaning sentences, and `request.md` uses them | — |
| `task-cycle/skill/correction.md:31` | The correction route | "its record link, its lists of findings and *What this request settles*" | rewrite `request.md` by the template for the corrected state, check, edit (D7) |
| `task-cycle/skill/foundation_step.md:15` | The tie of a row to an entry already stated | "*What this request settles*" | *Foundation entries*, and the tie in *For you to decide* as a choice beyond the task (D5) |
| `foundation_step.md:17` | — | "keeps for the request one sentence of each entry's meaning in the task document's language" becomes: keeps for each entry one sentence of its meaning in English and in the task document's language, and marks it `row <n>`, `projected` or `the cycle's` | — |
| `foundation_step.md:27` | The blocked return | "as step 13… gives under *Questions*" | *For you to decide* by the template |
| `task-cycle/skill/reserved_return.md:63-78` ("What the request states") | Nothing of its own list | All its items, as the template's reserved variant (D7) | the template |
| `reserved_return.md:51-61` (order) | The order (commit adding the record, push, open, removal), with the description written and checked after the push and before opening | — | — |
| `reserved_return.md:86-92` (after a correction) | The reset and the record pair | "its *What this request settles* unchanged" | the template's reserved variant after a correction |
| `task-cycle/skill/blocked_finding.md:12` | The run order (gate, stages, pair, then open) | "give what step 13 names for it" | the template's variant for a remaining blocking finding; check before opening |
| `agent-instructions/README.md:66-74` | D8 | — | — |

The search (`grep` for "request states", "request lists", "names in its request", "in the
request", "step 13", "*Questions*", "What this request settles", "Request handoff" over the tree
outside `.runs/`) found no other file of `task-cycle/` that lists request content. The following
mention the request and stay as they are: `return_step.md:15-16`, `change/SKILL.md:88`,
`review/SKILL.md:12,38,91`, `review/fix.md:4,9`, `SKILL.md:110`. These files outside `task-cycle/`
say a change "names in its request" an item and hold once the lower part names it:
`elements/invariants/skill/write.md:9`, `elements/invariants/template.md:77,163,182`,
`elements/part-map/template.md:110`, `project-level/task/template.md:201`,
`installation/README.md:111` and `README.md:52,74`.

The search of the whole foundation (WAY-33) does not reach files outside `foundations/`. So every
file outside it that restates WAY-10's or WAY-114's acceptance at the merge is named here, with
what it becomes under row 4. These come from a `grep` for "at the merge", "by merging", "WAY-114",
"WAY-10)" and "diff of the foundation" outside `.runs/`, `docs/` and `foundations/`:

| File | Says today | Becomes |
|---|---|---|
| `task-cycle/skill/SKILL.md:204-205` | "the human accepts the foundation entries the cycle writes by merging the request (WAY-114)" | the human accepts, by merging, the entries not accepted with the task document or at the gate, which the request puts before the human (WAY-114) |
| `elements/common/way_of_working.md:134-136` | "The human accepts the meaning at the merge, or at the readiness gate for a projected entry (WAY-114)" | adds the third case: an entry written whole from an accepted row, with the task document |
| `elements/glossary/template.md:48-49` | "The human accepting the change at the merge accepts the meaning of each entry (WAY-114)" | the same three cases, a term written from an accepted row being accepted with the task document |
| `elements/decisions/template.md:131` | "A human accepts the changed meaning by merging the request that carries the change (WAY-14)" | by merging, unless the change was written from an accepted row, whose meaning the human accepted with the task document (WAY-114). Line 68-70's "the human's acceptance of the task document being its approval" already says so for a technology row |
| `elements/common/critique/SKILL.md:20-22` | the diff of the foundation "the review of the change by an agent that did not make it reads it, and the human reads it at the merge (WAY-10)" | the review reads it, and the human reads the request's section for the human's decisions at the merge (WAY-10) |

These hold as they are, since WAY-114's gate clause is unchanged:
- `elements/common/projected_mode.md:18`;
- `project-level/skill/SKILL.md:164-168`;
- `agent-instructions/README.md:34`, about questions before the merge.

*Rejected:*
- `task-cycle/request_template.md`, beside `record_template.md`. Symmetry with an older file
  against WAY-256's "beside the skill".
- The template inside `SKILL.md`. Text only some steps consult, carried through all of them
  (WAY-256).

Cost if wrong: a moved file and its pointers, one commit.

### D3 — The record's *Request handoff*

The heading `## Request handoff` stays. The test fixtures need nothing, and `plan_state.py` keeps
finding the URL. The section keeps these fields, in this order:

- *Request URL and status*: unchanged, the reserved wording `blocked draft, opened on this commit`
  included.
- *Description*: the path `request.md` beside the record, and the form check's last command and exit
  code with the number of its runs. This field is new.
- *Writes to the task's backlog entry*: unchanged.
- *Process remarks on the-way*: unchanged, as the last list item of the section, word for word as
  today. The digest's list-item rule takes it and its lead-in list to the end of the section.

These fields go, since `request.md` holds their content: *Cycle and its reasons*, *Process pin*,
*What this request settles*, *What the foundation puts in front of the human…*, *Checks*, *Human
actions…*, *Questions*, *Review findings listed*, *Blocked by review* and *Choices within the
request*.

`request.md` lives in `.runs/task-cycles/<task-slug>/`. What the committed copy holds depends on the
route:

- **Step 12: every request that opens through it.** This includes a blocked draft that waits for
  human actions or for an answer, since those finish the cycle's steps before opening. `request.md` is written
  and checked before the request opens, which is before the record pair. So the copy commits it as
  it stood then, before the SHA link. *Description* in the copy holds the runs of the check up to
  that commit. The working record gets the later runs.
- **The routes that commit the record first: `blocked_finding.md`, the 9.4 stop and
  `reserved_return.md`.** The record's
  commit comes before the description, since the description links that commit by its SHA. On these
  routes `request.md` is written and checked only after the commit that adds the record. The
  committed copy therefore holds no `request.md`, and its *Description* reads `written and checked
  after this commit`. That reading is a fixed wording, like *Request URL and status*'s
  `blocked draft, opened on this commit`. The working record in the kept worktree then gets the
  path and the runs.

A correction repeats the record pair, then rewrites `request.md` to link the new commit
(`correction.md`). Its copy therefore holds the description as it stood before the correction, and
its *Description* reads `written and checked after this commit`, as on the routes that commit the record first. What the human or a later reader needs of a blocked request stands in the request itself
and, for its trail, in the record's *Request URL and status* and the Events.

*Rejected:*
- A heading `## Process remarks on the-way` of its own. The digest would take it as well, but
  WAY-260 and `SKILL.md:70-72` name the item, and the move buys nothing.
- Keeping the fields beside `request.md`. Two copies of one content.

Cost if wrong: the digest stops getting remarks. The test of D4 does not catch that, and the
nightly session sees an empty digest. Keeping the item's text unchanged avoids it.

### D4 — The form check script

**Path and part.** `task-cycle/request_check.py`, part `task-cycle`. Tests in
`task-cycle/test_request_check.py`. Standard library only. It starts no program and writes no file.
It is no trust boundary and no surface:
- It reads two text files of the cycle and runs nothing from them, like `cycle_stages.py` and
  `slice_size.py`. Any input text it prints passes through a printable filter, as
  `plan_state.display` does.
- The-way's own skill at the same pin runs it, and no one outside a product relies on its command
  (WAY-49). The surfaces at the end of `foundations/part_map.md` gain nothing.

**Command.** `python -B task-cycle/request_check.py DESCRIPTION --task TASK`. In a product, the path
starts with `.the-way/`.
- DESCRIPTION is the description file, `.runs/task-cycles/<task-slug>/request.md`.
- TASK is the frozen task document of the record, or, for a the-way change, the task document or the
  project plan the change carries out (D8).

**Units.**
1. *Sections*. Splits the description into the state line, the `##` sections with their content, the
   `### Underneath` subsection and the block. Lines inside fenced code and inside any `<details>`
   element are never headings. Only ATX headings count.
2. *Block finder*. The block is the one `<details>` element whose opening line comes after
   `## How to merge` and before `## Technical changes`. Its content is the text after its
   `</summary>` up to the matching `</details>`, nesting counted.
3. *Language measure*. For a text, the share of its words that are English function words. The list
   holds no word that is also a common Polish word (`a`, `i`, `to`, `on`, `no`, `do` among those
   left out). The text is measured without code spans, fenced code, URLs, link targets and HTML
   tags. A text is English when the share reaches a threshold. It is not judged when it holds
   fewer words than a minimum.
   - For TASK, the measured text is the title line and the content of `### Need` and `### To do`.
     The task template writes those in the human's language and keeps the headings and markers in
     English. A TASK with neither heading, such as a project plan whose position a the-way change
     carries out (D8), is measured on the *Goal* cells of its `## Tasks` table and the question text
     of each item of its `## Open questions` (the text before its first ` — `), and on nothing else:
     the plan template keeps its headings, header lines, column headings, states and markers in
     English, whatever the definition's language (`project-level/plan/template.md:22-23`). D10.
   - For the block, it is the block's content.
4. *Report*. Each problem on stdout as `line <n>: <what is wrong and what to write>`, then one
   summary line. Problems are reported in the order of the file.

**Errors** (each reported, exit 1):
- the first non-blank line is not `**State: ready|draft|blocked** — <text>`;
- a required `##` heading missing, repeated or out of order;
- `### Underneath` missing from `## What you will see`;
- a `##` heading that is not in D1 and stands anywhere but the slot of the task's own sections;
- a section, `### Underneath` or the block with no content. Content is any non-blank line that is
  not only an HTML comment, `none` included;
- no block in its place, more than one, or one not closed;
- where TASK is English: the block holds anything but `none`;
- where TASK is not English: the block reads `none`, or its text is English.

**Not judged.** Everything in the second non-goal. Where TASK or the block is below the minimum of
words, the language is not judged. The summary line says so, and no error follows from it.

**Exit codes and output.** 0 when the form holds, with the summary line naming the sections found
and the language reading (`task: English|not English|not judged`). 1 with the problems listed. 2
with `Error: <message>` on stderr when an argument is wrong or a file cannot be read as UTF-8.

**Agreement with the template.** The script keeps the headings of D1 as constants. A test reads the
first fenced `markdown` block of `task-cycle/skill/request_template.md` and requires its headings,
in order and level, to equal those constants. The placeholder heading `## <…>` marks the slot of
the task's own sections. A change to one without the other fails the gate.

**Tests** (`task-cycle/test_request_check.py`, `unittest`, fixtures written for the test as inline
text, no copy of private notes):
- a whole valid description with a Polish block and a Polish task passes;
- an English task with a `none` block passes;
- the task's own sections in their slot pass;
- one failing case for each error above, with the line number reported;
- headings inside fenced code and inside the block are ignored;
- a second `<details>` in the lower part is not the block;
- a short task text gives `not judged` and exit 0;
- a document with neither `### Need` nor `### To do`, a plan's form, is measured on its whole text;
- an unreadable file gives exit 2;
- English prose and Polish prose of realistic length, the Polish holding English quotes and
  backticked names as task documents do, fall on the right side of the threshold with a margin;
- the agreement test.

**Where the cycle runs it.**
- Step 13, before the request opens, and again before each later edit of the description is
  published (step 12's SHA link).
- `blocked_finding.md` and the 9.4 stop: `request.md` is written after the record pair, then
  checked, before opening. The committed copy holds no `request.md` (D3).
- `reserved_return.md`: `request.md` is written after pushing the commit that adds the record, then
  checked, before opening; the copy holds no `request.md` (D3). In "After a correction", it is
  checked before the request returns to draft.
- `correction.md`, after `request.md` is rewritten and before the edit.

**How the cycle corrects.** The orchestrator edits `request.md` at each reported line it agrees with
and runs the script again, until exit 0: each error names what to write. It publishes a file that
passed, through `gh pr create --body-file` or `gh pr edit --body-file` or the host's equivalent,
except in the case below. Exit 2 is no form error: the orchestrator fixes the call, or, where the
file cannot be read, the file. The last run goes into *Description* of the record (D3).

**An error the orchestrator holds wrong.** A reported error can be wrong. The language measure can
read a correct Polish block, or a Polish task document full of quoted English names, as English,
and an error of the script itself is possible. Where the orchestrator holds a reported error wrong,
with evidence it can name, it handles it this way:

1. It does not change the description to silence the error. Above all, it never writes `none` into
   the block, and never puts the block into English, on a language error it holds wrong.
2. It runs the script once more on the final file, so the error stands as the check's actual result.
3. It publishes that file, and the request opens, or stays, as a draft. The first line reads
   `**State: draft** — the form check reports an error the cycle holds wrong`.
4. *For you to decide* holds one item: what the script reported, in plain words; why the cycle holds
   it wrong; "merge as it stands?".
5. *Checks* names the check, its command, its exit code and its reported line (WAY-160: a check that
   failed is named, never passed).
6. The orchestrator copies the case into the record's process remarks, since it is a matter of the
   the-way's script, not of the product.

The loop thus always ends: in exit 0, or in a draft that names the failed check. The request never
opens with a description the script passed only because a correct block was removed.

The `draft` state, not `blocked`, fits this case. The cycle needs nothing to go on, and the human's
yes to the description is all that waits.

*Ways weighed for the language:*
- (a) Function-word lists for a closed set of languages. Fails every language outside the set.
- (b) Letter-trigram profiles that compare the block with the task document and with the English
  top part. Language-agnostic, but it needs tuned distances, and a task document quoting English
  decisions blurs the profile.
- (c) A language tag the orchestrator writes on the block. It checks nothing about the language.
- (d) The English function-word share only. Chosen: the description is English by rule, so English
  is the one language the script must know. It catches the observed failures: a missing block, an
  untranslated block, a translated block for an English task.

*Rejected:*
- The script reading the headings from the template at runtime. One source, but the prose file
  becomes a runtime format, and the agreement test gives the same protection.
- `--language` given by the orchestrator. Mechanical on the task's side costs one more argument.

Cost if wrong: a block in a wrong non-English language passes, a case not seen so far. A threshold
too tight reports a correct block. The prose tests with a margin guard against that, and where it
still happens, the route of an error held wrong opens a draft that names it instead of losing the
block.

*Rejected for an error held wrong:*
- Opening the request as a blocked draft. The cycle needs nothing to go on, so `blocked` would
  misstate the state.
- Correcting until exit 0 at any price. A correct Polish block would be replaced by `none` or by
  English, and the human would lose the block the task exists to give, with nothing saying so.
- An override flag on the script. A switch that silences the check, which the orchestrator would
  set itself.

### D5 — What fills *For you to decide*, and from where

Each item states in plain words what the human is asked to accept or answer, then the question,
such as "Merge without it?", "Make a task of it?" or "Accept?". An item that has its evidence in the
lower part ends with a pointer by section and number, such as "(Minor findings, 3)". A pointer is
neither a file name nor an entry identifier.

Items, in this order:

1. **What a blocked request needs** to go on (D7). From the cause that blocked it.
2. **Questions** the foundation step allows, and a reserved choice. From the agent report that
   returned `blocked` or `reserved`.
3. **Human actions**: each action the task places in the cycle, and each effect outside the
   repository the cycle found that the document does not name (WAY-140). From *Human actions* of
   the frozen task, and from the Events and reports.
4. **Skipped steps and unrun checks.** From *Verification*, the Events and *Return step* of the
   record:
   - a stage the cycle skill requires for this change that did not run or was skipped, such as the
     return step, a review, the reconciliation with the target branch, a slice not made or the gate;
   - a check of the final gate run that failed or did not run, apart from one that also fails on
     the base, which stays in *Checks*;
   - a check the change needed that an author reports as not done: a screenshot unchecked
     (WAY-219), a missing state check or a missing own-work check (WAY-164).

   A check the skill does not call for this change is none. A check that failed and passed again
   stays in *Checks* (WAY-261).
5. **Choices of the cycle beyond the task's content.** A choice is one when the task document, its
   sources and the foundation do not settle it, and another answer would change what the product's
   user sees or does, what the human meets when working with the process, or what the foundation
   binds. Sources:
   - the spec's *Decisions*, the answers to the task's *Questions carried to cycle* included;
   - rows of the questions table answered by an autonomous choice (the smallest reversible reading)
     or by a ruling that reads an item of the task wider or narrower than its words;
   - departures from the task's wording an agent names in its report;
   - a choice of how to make the change whose result the user or the human will see or feel, such
     as the look of a screen the task does not fix;
   - a kept row tied to an entry already stated, so that it writes no entry (WAY-134).

   A row a binding source answered is none. A choice of how to make what the task settles is none
   either (`SKILL.md:234-237`), unless its result shows as above. The rest are the count in
   *Course of the cycle* → **Choices**.
6. **Foundation entries the human did not see at the task document**, each with one plain sentence
   of meaning, repeated in the block in the task's language. From the foundation step's and return
   step's reports, by the mark of D2 (`the cycle's`):
   - entries written from the spec or by the return step;
   - corrections the search of the whole foundation made;
   - the part of a projected entry (WAY-126).

   Excluded: entries written whole from rows of *Settlements to record*, and projected entries
   written whole as approved (row 4).
7. **Changed invariant tests, surfaces and *Violated* marks** (WAY-03, WAY-49, WAY-51), in plain
   words. From the changed files, read against the invariants file and the part map, and from the
   record's *Return step*.
8. **Unfixed findings the user or the human will feel** (row 5). The orchestrator reads each Minor
   finding and each finding outside the task's scope, of the review of the whole change and every
   later review. It judges, from the whole record, reports of the walk through the running product
   and screenshots included, whether the product's user or the human working with the process will
   feel it. It restates each such finding in plain words as "Make a task of it?".
9. **Decisions of the task's own sections**: each item of those sections that waits on a yes, such
   as a proposal not applied.

Row 5 and WAY-161:
- The finding stays in its lower-part list with the reviewer's words and its place in the code.
  It keeps its kind and grade.
- The judgment decides no fix and no block, and removes nothing from a list.
- So "moves no finding from one of these kinds to another" holds. WAY-161 warns about an
  orchestrator moving an inconvenient finding out of the way of a blocked request. That cannot
  happen here, since the judgment only adds a line before the human, and a finding judged "not
  felt" stays where WAY-161 puts it.
- The new decision of row 5 says this in its rationale.

Empty: `none`, and then nothing below waits for a yes. A lower-part item whose decision stands here
is no breach, since its yes is asked above.

*Rejected:* a column "beyond the task" in the questions table, filled when each row is recorded.
More reliable, but it changes the section the collective task changes and the recording rule of
step 5. Selecting at the end can miss a row, and the weekly review is the backstop.

Cost if wrong: a choice the human would have questioned passes unseen, as today.

### D6 — The foundation entries' form

New decisions, at the next free numbers (WAY-286 onwards at the base), one per row: rows 1, 2, 3, 5
and 6. Each answers a question no entry answers. Row 4 changes WAY-114, WAY-134 and WAY-10 in place.
"Foundation entries" below gives each meaning, for the foundation step to word. The meanings are
given sentence by sentence, as the handoff asks, but as meanings: `design.md` keeps the wording for
the foundation step, and WAY-114 keeps it the agent's.

Merging rows was weighed and rejected:
- Rows 1 and 2 in one entry: more than three binding sentences.
- Row 5 as a fourth sentence of WAY-161: past the limit, and a new rule beside an existing
  decision is a new question (WAY-19).
- Separate entries also keep each *Rejected* tied to its row's source.

Cost if wrong: renumbering before the merge only.

### D7 — The variants on one skeleton

Every variant keeps every heading of D1. Sections with no content read `none`.

| Variant | First line | *For you to decide* | Lower part |
|---|---|---|---|
| Remaining blocking finding (`blocked_finding.md`, WAY-162/163) | `**State: blocked** — a review finding remained after its one fix` | each remaining finding in plain words, with "fix it as the finding says, or keep the code despite it?"; what has not run on that code (return step, reconciliation, slices not made) | **Blocking findings left**: each with its place, reason and what the fix tried; *Cost* the cost so far with the rounds; *Checks* naming what has not run |
| Slice failed twice (9.4) | `**State: blocked** — a slice failed with two agents` | what failed, in plain words, and what the cycle needs to go on; the stages not run | *Course* **Route**: both failures with the classes tried, the slices made with no review |
| Reserved choice (`reserved_return.md`, WAY-269) | `**State: blocked** — the cycle met a technology choice only you make` | the choice by what the product needs it for; the ways seen, marked as not researched, with no recommendation; what happens next: close the request, and refinement takes the choice as its note | *Technical changes* `none`; *Foundation entries* `none`; *Checks*: base checks and each stage not run with why, the gate included; *Course* **Route**: where it showed (stage, task item), the limb of the rule and what was searched, the discarded attempt and its report; *How to merge*: do not merge, close |
| Human actions in the cycle (WAY-140) | `**State: blocked** — waits for your actions outside the repository` | each action as the task names it; each found effect for the human to place | as an ordinary request |
| Question from the foundation step | `**State: blocked** — needs your answer` | the question with options and a recommendation where one exists | as an ordinary request |
| Impossible task | `**State: blocked** — <the smallest missing fact or permission>` | that fact or permission | *Course* **Route**: the ways tried |
| Correction (`correction.md`) | the state after the correction, with "corrected for your remarks" in the why | the items as they stand after the correction, the correction's new choices included; a remark is no item, since it binds | *Course*: each correction with its remarks' link and reset base; *Cost* across all sessions |
| Correction met a reserved choice | `**State: blocked**`, as for a reserved choice | as for a reserved choice | *Foundation entries* unchanged from the request's previous description |
| Form check error held wrong (D4) | `**State: draft** — the form check reports an error the cycle holds wrong`. Where the request is blocked for another cause, it stays `blocked` and only the item is added | the reported error in plain words, why the cycle holds it wrong, and "merge as it stands?" | *Checks*: the form check's command, exit code and reported line |
| Draft for another reason | `**State: draft** — <reason>` | the reason as an item, such as "the return step was skipped on your instruction; merge without it?" | as an ordinary request |

### D8 — The-way's own requests

`agent-instructions/README.md`, "Integrate into `foundations`":
- Its five bullets go.
- The section says that the description follows `task-cycle/skill/request_template.md`.
- *Cost* reads `none` and *Course of the cycle* holds **Task and sources** only, the other labels
  reading `none`, where no cycle ran.
- The agent leading the work makes row 5's judgment.
- `request_check.py` runs on every such request before it opens and before each edit, as the route
  of an error held wrong in D4 allows. Its `--task` is the document the change carries out: the
  task document, or, for a change that carries out a plan's position, the project plan that holds
  that position. The README already says the reviewer receives "the task or the plan's position".
  - A task document is measured on its title, *Need* and *To do*.
  - A plan, having neither heading, is measured on its whole text other than headings (D4, unit 3),
    so the block's language is judged in both cases. Below the minimum of words it reads
    `not judged`, as for any short document.
- "Mariusz merges the request; the merge is the acceptance of the change and of every entry it
  alters" becomes: the merge accepts the change and each entry he did not see at the task document,
  those standing in *For you to decide* (row 4).
- `README.md:64`: "the other remarks go into the request" points to the lower part's lists.

Cost if wrong: one more template than the README route needs, at about two `none` sections.

### D9 — Entries that say what the request names

For the search of the whole foundation (WAY-33): look for every entry whose binding sentences,
*Verification*, *Rationale* or *Rejected* say that the request lists, names, states, gives or shows
an item, that the human reads or sees something in the request or at the merge, or that the human
accepts a meaning at the merge. Judge each by whether it holds once its item stands in the top part,
the lower part or both.

Hold, with no change: WAY-03, WAY-49 and WAY-51 (named in *Foundation entries* and in *For you to
decide*); WAY-140, WAY-160, WAY-162, WAY-163, WAY-164, WAY-219, WAY-261, WAY-269, WAY-130, WAY-172,
WAY-227, WAY-242 and WAY-268.

To check in the search:
- WAY-161's rationale "one listed in the request with the reviewer's words stays in front of the
  human who merges". It is now true only of the felt findings. Correct it, naming the new row-5
  decision.
- WAY-33's rationale "the human who sees every entry it alters in its request". It becomes: who sees
  each entry not accepted at the task document.
- WAY-126's complies example "lists its meaning in the request". It goes to *For you to decide*.
- WAY-134's *Relations* `narrows WAY-114`: does it still narrow, once WAY-114 states the row
  acceptance itself?

The files outside the foundation that restate WAY-10 or WAY-114 are not left to this search. D2's
second table names each of them with what it becomes.

### D10 — Settled by the orchestrator after the spec's review

The review of the revision (`reports/spec-review-2.md`) left two findings; the orchestrator settled
them as step 6 settles a question (`task-cycle/skill/spec_review.md`).

- **A — the exception and row 6.** Row 6 is written whole, as the row says it: the cycle corrects
  the description while the script reports errors. The exception for an error the orchestrator
  holds wrong (D4, "An error the orchestrator holds wrong") is a decision of its own, written from
  this spec, answering its own question and narrowing the row-6 decision; as an entry the cycle
  wrote, it stands in *For you to decide* under D5 item 6, where the human accepts or rejects it at
  the merge. Not chosen: the exception inside the row-6 entry (it changes the row's meaning, against
  WAY-134); asking the human before the change (a blocked draft for a choice the request already puts
  before the human). Cost if wrong: one decision to withdraw at the merge, and D4's route with it.
- **B — the plan case.** For a TASK with neither `### Need` nor `### To do`, the measure reads only
  the *Goal* cells of `## Tasks` and the question text of `## Open questions` (D4 unit 3), since the
  plan template keeps every other line's markers and states in English. Not chosen: all text but
  headings and table header rows (English states, markers and the change log push a Polish plan to
  English); stripping named columns and lines (a longer list to keep in step with the template).
  Cost if wrong: a plan with short *Goal* cells is `not judged` and its block's language goes
  unchecked, which the measure's minimum already allows.

## Foundation entries

Meanings, sentence by sentence. The foundation step words them.

**New decision, row 1.** What form does the description of a task cycle's request take?
- It follows one template with headings in a fixed order and level. The top part is for the human,
  in plain words with no file names or entry identifiers: the state in the first sentence; what the
  human will see, the whole change, what the task announced included, with a word on what is
  underneath; the human's decisions; the cost; and how to merge.
- The lower part, in a fixed order, holds the technical changes, the checks, the full list of
  foundation entries, the Minor findings, the findings outside the task's scope, the task's own
  sections under their own headings, and the course of the cycle. Each of its items opens with a
  sentence a human understands without the code, before the places in the code and the identifiers.
- A section with no content reads `none`.
- *Rejected:* `unknown`. The row's sources keep no way not chosen for the layout.
- Scope: task-cycle, agent-instructions.

**New decision, row 2.** What does a request put before the human for a decision?
- Its section for the human's decisions holds everything whose merge needs the human's yes: the
  cycle's choices beyond the task's content, skipped steps and unrun checks, unfixed findings the
  user or the human working with the process will feel, the decisions of the task's own sections,
  in a blocked request what the cycle needs to go on, the human actions, the changed invariant
  tests, surfaces and *Violated* marks, and the foundation entries the human did not see at the
  task document. Its `none` means nothing else waits.
- A blocked request has the same skeleton, with `blocked` in its first sentence and what the cycle
  needs in plain words in that section, while each remaining finding with its place in the code
  stands in the lower part.
- *Rejected:* `unknown`.
- Relations: derives from WAY-227.

**New decision, row 3.** In what language is a request's description written?
- English, with its top part repeated in the task document's language in a collapsed block.
- *Rejected*, from the row's source:
  - all in English, as before: a long English text the human reads line by line, so not at all;
  - the top part in Polish and the lower part in English: a public request opens in Polish;
  - a Polish report in the human's notes: the cycle writes nothing outside the repository, and
    the human would look in two places.

**New decision, row 5.** Which unfixed findings does a request put before the human for a decision?
- Writing the request, the orchestrator judges each Minor finding and each finding outside the
  task's scope, from the whole cycle record, reports of the walk through the running product and
  screenshots included, by whether the product's user or the human working with the process will
  feel it.
- It restates each such finding in plain words in the section for the human's decisions, as a
  question whether it becomes a task. Every finding stays in its list in the lower part with the
  reviewer's words and its place in the code.
- The judgment changes no finding's kind or grade, and no fix or block (WAY-161).
- *Rejected*, from the row's sources:
  - every finding in the lower part only: findings a player would feel are lost unseen, since
    neither the human nor the nightly review reads them;
  - the nightly review of the AI layer extended to review findings: that review would start
    carrying product bugs, and the clean-ups would flood its ledger;
  - the reviewer who reports the finding judging it: it looks with fresh eyes but reads code and
    task and does not run the product.
- Relations: derives from WAY-161.
- Its rationale answers WAY-161's warning (D5).

**New decision, row 6.** How is the form of a request's description checked?
- Before the request opens, the cycle runs the-way's script that checks the description's form —
  the order of its headings, content or `none` in every section, and the collapsed block in the task
  document's language — and corrects the description until the script reports no error.
- The script judges no content.
- The exception for an error the orchestrator holds wrong is not in this entry: it stands in the
  decision below (D10).
- *Rejected*, from the row's source:
  - the template alone: an agent can lose or move a section, unseen until reading;
  - the script and a second agent comparing the description with the record: one more agent
    call each cycle, before it is known whether decisions slip into the lower part at all.

**New decision, from this spec, not from a row (D10).** What does the cycle do with a form error
it holds wrong?
- Where the orchestrator holds an error of the form check wrong, with its evidence, it does not
  correct it away — it never empties the block or puts it into English — and the request opens as a
  draft that names the error and the cycle's reason in the section for the human's decisions and
  under *Checks*.
- *Rejected:* correcting the description until the script passes in every case — a measure that
  misreads a correct block would end with the block lost or the request never opening; asking the
  human through a blocked draft before writing — a round for a case the draft already puts before
  the human.
- Relations: narrows the row-6 decision.
- As an entry the cycle writes beyond a row, it stands in the section for the human's decisions of
  this task's own request (D5 item 6), with one sentence of its meaning.

**WAY-114, changed in place (row 4).**
- The human accepts the meaning of a foundation entry, while its wording is the agent's. Where and
  how the human accepts it depends on the entry:
  - a projected entry, at the readiness gate, shown as one sentence in the human's language with
    the entry beside it. This is unchanged from today, so `elements/common/projected_mode.md:18`
    and `project-level/skill/SKILL.md:164-168` keep their anchor;
  - an entry written whole from an accepted row of the task's *Settlements to record*, with the
    task document, where the row is the human's own sentence;
  - every other entry, at the merge of the change that holds it. There, the request's section for
    the human's decisions gives one plain sentence of its meaning, with no identifier, as row 1
    bars identifiers from the top part, and repeats that sentence in the human's language in the
    collapsed block. The entry itself stands, by its identifier with its English meaning sentence,
    in the full list of entries in the lower part.

  The change touches only what the merge shows and accepts. The gate clause stays as it is, since
  the task's answer limits the change to the decision section ("Zmiana dotyczy tylko sekcji
  decyzji").
- Unchanged: before that, a question goes to the human only where the agent has no recommendation or
  the entry would change the meaning of an approved decision; a translation never enters the
  foundation.
- *Verification*:
  - complies: the readiness gate shows each projected entry's meaning sentence in Polish with the
    entry beside it; the request's section for the human's decisions gives a plain sentence of the
    meaning of each entry the cycle wrote with no row or projected entry carrying it — from the
    spec, a correction the search of the foundation made, the part of a projected entry —
    repeated in the task's language in the block, while every entry, those from rows and projected
    ones included, stands by its identifier in English in the lower part; the human reads that
    section and merges;
  - violates: an agent asks the human to confirm a choice it already recommends; a translation is
    written into the foundation; an entry changes the meaning of an approved decision without a
    question; an entry written from the spec stands only in the lower part; the section for the
    human's decisions lists the entries written from accepted rows.
- *Rationale*: the human judges what an entry settles, and the wording rarely changes that. A row is
  the human's own settlement, accepted with the task document, and a projected entry is wording the
  gate approved. Asking again at the merge buries the entries the human has not seen among those
  already accepted, and a list the human does not read accepts nothing. The price: an entry whose
  wording drifts from its row reaches the merge unseen by the human, and the review of the whole
  change reads it against the row (WAY-134, WAY-10).
- *Rejected*: the two options it holds today stay. Added from row 4's source:
  - WAY-114 left as it was: the full list with Polish sentences at the top, 39 items in loop2 #55,
    a wall of text the human does not read;
  - the full list in the lower part and nothing at the top: entries the cycle adds enter without
    the human's knowledge;
  - at the top also an entry from a row whose wording the cycle wrote, when it differs from the
    human's sentence by more than words: the human kept the variant without it at the control
    question.
- Scope gains task-cycle.

**WAY-134, changed in place (row 4).**
- Its third binding sentence: "and otherwise the human accepts the entry's meaning at the merge
  (WAY-114)" becomes "and otherwise the entry's meaning is the one the human accepted with the row
  in the task document (WAY-114)". Unchanged: the tie of a row to an entry already stated, named in
  the request.
- *Verification*'s complies "names it in the request" becomes "lists it in the request's lower
  part".
- *Rationale*: "and the human judges the meaning at the merge" becomes "the human judged the meaning
  when accepting the row, and the merge does not ask again, while the review of the whole change
  reads the entry against the row".
- *Rejected* unchanged: the row's source keeps no way not chosen for WAY-134.

**WAY-10, changed in place (row 4).**
- Binding sentence: "a human reads the diff of the foundation and accepts the change by merging its
  request" becomes "a human reads the request's section for the human's decisions and accepts the
  change by merging the request".
- *Verification*'s complies: "and the human, reading what that section puts before the human, the
  reworded decision in plain words among it, merges it with no other assessment". The violates
  examples are unchanged.
- *Rationale*: "which the tests and the human reading the diff of the foundation at the merge also
  meet" becomes "which the tests and the review of the whole change also meet". Add that the human
  reads the section that holds what the human has not accepted, while the reviewer reads the whole
  diff.
- *Rejected* unchanged.

Invariant tests, surfaces, *Violated* marks, glossary, environment facts and the part map: none
change. No new term: "For you to decide", "top part" and "lower part" read in their plain meaning.

## Left to the maker

- The English function-word list, the threshold and the minimum word count, chosen so that the prose
  tests of D4 hold with a margin.
- The exact wording of the template's guidance, of each pointer sentence in the changed files, and
  of the new step-12 order within D2's sequence.
- The names of the script's functions and the wording of its messages, each saying what to write.
- Whether `request.md` in the committed record copy gets a sentence in *Artifacts*.
- The foundation step words every entry above, numbers the new ones and runs the search of D9.
