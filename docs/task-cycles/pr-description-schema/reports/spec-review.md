FAIL

# Spec review — pr-description-schema

Reviewed: `docs/task-cycles/pr-description-schema/spec.md` against the frozen task
(`docs/task-cycles/pr-description-schema/task.md`, To do 1–9, its answers, rows 1–6, *Out of scope*),
the designer's handoff, and the foundation entries the review handoff names, each read whole.

The spec settles every choice the designer's handoff named, and most of it holds against the task:
the headings and their order match To do 2 and 5, the block's place follows the human's approved
summary (transcript MSG 22, item 6: "Punkty 1–5 jeszcze raz po polsku, w zwiniętym bloku", then the
archive below), the *Rejected* of rows 3, 4, 5 and 6 carry exactly the ways not chosen the rows'
sources keep, row 5's judgment is kept apart from WAY-161's kinds, and the record keeps the
"Process remarks" item where `extract_remark_blocks` cuts it. Four findings remain.

## Findings

### 1. The new meaning of WAY-114 drops how an entry is shown, at the readiness gate as well as at the merge

Spec `spec.md:580-586` gives WAY-114's first sentence as "The human accepts the meaning of a
foundation entry, while its wording is the agent's", then the three points of acceptance, then
"There, the request's section for the human's decisions shows that entry with one sentence of its
meaning, repeated in the human's language in its collapsed block". Today's WAY-114
(`foundations/decisions.md:2452-2453`) says the meaning is "shown as one sentence in the human's
language with the entry beside it".

- At the readiness gate, that clause is what `elements/common/projected_mode.md:18` ("The readiness
  gate shows each projected entry's meaning sentence with the entry beside it and approves the
  meaning (WAY-114)") and `project-level/skill/SKILL.md:164-168` cite WAY-114 for. The spec's
  meaning removes it for the gate, though the task's answer says the change concerns the decision
  section only ("Zmiana dotyczy tylko sekcji decyzji") — a change the task does not ask for.
- At the merge, "shows that entry" leaves open whether the decision section shows the entry itself.
  Row 1 and To do 2 forbid entry identifiers in the top part, and D5 (`spec.md:362-365`) points by
  section and number. A foundation step that keeps today's "with the entry beside it" for the merge
  writes a WAY-114 that contradicts the new row-1 decision; one that drops it everywhere breaks the
  gate's anchor above.

The builder has to guess the binding sentence of an approved decision. The spec should say, as a
meaning: at the gate, unchanged (sentence in the human's language with the entry beside it); at
the merge, the plain sentence in the decision section and in the block, with the entry itself in
the lower part's full list.

### 2. Restatements of WAY-10 and WAY-114 outside the foundation are missing from the lists of files to change

D2 (`spec.md:206-215`) claims a search of the tree outside `.runs/` and lists the files that hold or
change with request wording; D9 (`spec.md:491-511`) names `elements/common/way_of_working.md:134`
and `elements/decisions/template.md:131`. The search of the whole foundation (WAY-33) covers only
the foundation, so files outside it change only if the spec names them. Not named:

- `elements/common/critique/SKILL.md:20-22`: "the review of the change by an agent that did not
  make it reads it, and the human reads it at the merge (WAY-10)" — "it" is the diff of the
  foundation. Under the new WAY-10 (`spec.md:628-631`) the human reads the decision section, not the
  diff, so this line would cite WAY-10 for what WAY-10 no longer says.
- `elements/glossary/template.md:48-49`: "The human accepting the change at the merge accepts the
  meaning of each entry (WAY-114)" — false under row 4 for a glossary term written from an
  accepted row.
- `task-cycle/skill/SKILL.md:204-205`: "the human accepts the foundation entries the cycle writes
  by merging the request (WAY-114)" — the same, in the cycle skill this change already edits.
- With finding 1, `elements/common/projected_mode.md:18` and `project-level/skill/SKILL.md:168`,
  if WAY-114's gate clause moves.

A builder following D2 and D9 as written leaves these contradicting the changed entries.

### 3. On the blocked routes, the record cannot hold what D3 puts in it

D3 (`spec.md:232-233`, `243-244`) gives the record's *Request handoff* a new field, *Description*:
"the path `request.md` beside the record, and the form check's last command and exit code with the
number of its runs", and says step 12's copy commits `request.md` with the record. D4
(`spec.md:330-332`) runs the check on the blocked routes after the record pair is committed:
"`blocked_finding.md` and the 9.4 stop, after the record pair and before opening", and on the
reserved route "after pushing the commit that adds the record and before opening". On these three
routes the committed record exists before the check has run, and before `request.md` is final,
since the description links the record by the SHA of the commit that adds it.

The builder has to guess what the committed record's *Description* holds on these routes, and
whether `request.md` is written before the pair (with the SHA link missing) or left out of the
committed copy. The record is the trail WAY-269's rationale leans on when a host drops a closed
request's commits, so the answer belongs in the spec: for example, the field reads that the check
runs after this commit, and `request.md` is not part of the committed copy on the blocked routes.

### 4. No route for a form error the orchestrator holds wrong

D4 (`spec.md:335-339`) has the orchestrator correct `request.md` "until exit 0, with no round
limit", and publish "only a file that passed". Its own *Cost if wrong* (`spec.md:356-358`) names
the case it leaves without a route: "A threshold too tight reports a correct block, which the
orchestrator cannot correct away." Two outcomes follow, and neither is settled:

- the block is Polish and is read as English: the loop has no end and the request never opens;
- a Polish task document is read as English (title, *Need* and *To do* full of quoted English
  names, as the-way's tasks are): the error says the block must hold `none`, the orchestrator
  writes `none` as told, the script passes, and the human loses the Polish block the task exists to
  give, with nothing in the request saying so.

The builder writing the template's correction loop has to choose what the orchestrator does when it
holds the script's reading wrong — for example, open the request as a blocked draft naming the
failed check under *Checks* and in *For you to decide*, as an unrun or failed check is treated
(WAY-160) — and that choice changes what the human sees. The spec should settle it.

## Reaches beyond the handoff

- `foundations/decisions.md`: WAY-33 and WAY-126 whole, to judge D9's search criterion and the
  projected-part case of D5 item 6; a grep of the log for every reference to WAY-10, WAY-114 and
  WAY-134, to see whether D9's criterion reaches them.
- `foundations/invariants.md`: `return-step-record`, `outbound-link-reach`, `script-language`,
  `script-imports`, `script-subprocesses`, for the script and the committed `request.md`.
- `project-level/plan_state.py:146-158`, `230-262`, `340-385` (`record_pointers`, `provenance`):
  whether a new `request.md` in the committed record directory would add pointers or provenance
  conflicts. It does not: only files with *Task source* / *Task relation* fields are records.
- `project-level/task/template.md` headings, for D4's language measure of `### Need` and
  `### To do`.
- `elements/common/projected_mode.md:14-20`, `project-level/skill/SKILL.md:164-170`,
  `elements/glossary/template.md:44-50`, `elements/common/critique/SKILL.md:18-24`,
  `elements/common/way_of_working.md:125-140`, `README.md:20-26`, `README.md:48-76`,
  `installation/README.md:105-112`, `elements/invariants/skill/write.md:5-12`,
  `task-cycle/skill/return_step.md:12-18`, `task-cycle/skill/SKILL.md:180-240`: found by greps for
  "at the merge", "by merging", "WAY-114", "WAY-10)", "step 13", "*Questions*", "Request handoff"
  and the record's field names, outside `.runs/`, to check D2's and D9's lists (findings 1 and 2).
- `task-cycle/cycle_stages.py:1-30`: the house style D4 cites.
- The designer's dump of the refinement transcript,
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\7a4fe94e-3148-4011-bad6-7d83342c594a\scratchpad\transcript.txt`,
  MSG 19–25 only: to check the block's place D1 chose against the summary the human approved.
- `git log` and `git status` in the worktree, to confirm the base `f45ca40` and a clean tree.

## Searches not found or unclear

- Whether every change of the-way under the `agent-instructions/README.md` route has a task
  document to give the script as `--task` (D8): the README says the reviewer receives "the task or
  the plan's position the change carries out". Given a plan's position, D4's measure reads no
  `### Need` or `### To do` and returns `not judged`, so the block's language goes unchecked; the
  spec does not say whether that is intended.
- How a request is "marked `blocked`" on the host today (title, label or body) is settled nowhere
  in `task-cycle/`; D1 makes the first line the mark. Not a finding, since the task asks only for
  the state in the first sentence.
- The example requests (`gh pr view` of the-way #66, #69, #70 and loop2 #52, #55) were not read;
  the transcript passages and the task's *Need* sufficed for this review.
