# Designer revision report — pr-description-schema

Status: done
Spec: `docs/task-cycles/pr-description-schema/spec.md` (revised once)
Review answered: `reports/spec-review.md` (`FAIL`, four findings)

## Findings

### 1. WAY-114's new meaning drops how an entry is shown — resolved

The reviewer is right. The meaning in *Foundation entries* → WAY-114 now lists the three cases of
acceptance:

- **The readiness gate: unchanged.** The entry is shown as one sentence in the human's language with
  the entry beside it. So `elements/common/projected_mode.md:18` and
  `project-level/skill/SKILL.md:164-168` keep their anchor. The task's answer limits the change to
  the decision section ("Zmiana dotyczy tylko sekcji decyzji").
- **An accepted row:** accepted with the task document.
- **The merge:** one plain sentence of meaning in the decision section, with no identifier as row 1
  bars, repeated in the block in the human's language. The entry itself stands by its identifier,
  with its English sentence, in the full list in the lower part.

The complies example now names the gate case and "by its identifier in the lower part".

### 2. Restatements of WAY-10 and WAY-114 outside the foundation missing — resolved

The reviewer is right that WAY-33's search does not reach them. D2 gains a second table naming each
file with what it becomes:

- `task-cycle/skill/SKILL.md:204-205`;
- `elements/common/way_of_working.md:134-136`;
- `elements/glossary/template.md:48-49`;
- `elements/decisions/template.md:131`;
- `elements/common/critique/SKILL.md:20-22`.

These are named as holding as they are, the gate clause being unchanged:
`elements/common/projected_mode.md:18`, `project-level/skill/SKILL.md:164-168` and
`agent-instructions/README.md:34`. D9's last bullet, which left two of these to the foundation
search, is replaced by a pointer to that table.

Search behind the table: `grep` for "at the merge", "by merging", "WAY-114", "WAY-10)",
"WAY-10,", "WAY-10 " and "diff of the foundation" outside `.runs/`, `docs/` and `foundations/`. The
WAY-134 hits were read too; they cite WAY-134 for the refinement table and the *Rejected* rule,
which do not change, and none states acceptance at the merge. `project-level/task/template.md:197-201`
holds: "the request names the row with that entry".

### 3. On the blocked routes the record cannot hold what D3 puts in it — resolved

The reviewer is right. D3 now gives what the committed copy holds on each route:

- **Step 12, every request that opens through it:** `request.md` is written and checked before
  opening, so before the pair. The copy holds it without the SHA link, and *Description* holds the
  runs up to that commit.
- **`blocked_finding.md`, the 9.4 stop and `reserved_return.md`:** the record is committed first,
  and `request.md` is written and checked after it. The copy holds no `request.md`, and
  *Description* reads the fixed wording `written and checked after this commit`, like the reserved
  route's URL wording. The working record gets the path and runs after.
- **A correction:** the pair comes first and the rewrite after, so the copy holds the description as
  before the correction, with the same fixed wording.

D4's "Where the cycle runs it" states the same order.

### 4. No route for a form error the orchestrator holds wrong — resolved

The reviewer is right, and the second case it names, a Polish task read as English so that the
block becomes `none`, would silently defeat the task. D4 gains "An error the orchestrator holds
wrong":

1. It does not change the description to silence the error, and never writes `none` into the block
   or puts it into English on a language error it holds wrong.
2. It runs the script on the final file.
3. It publishes that file, and the request opens or stays as a draft. The first line reads
   `**State: draft** — the form check reports an error the cycle holds wrong`.
4. *For you to decide* holds the error in plain words, the cycle's reason and "merge as it stands?".
5. *Checks* names the check with its command, exit code and line (WAY-160).
6. The case is copied into the process remarks.

Where the request is blocked for another cause, it stays `blocked` and the item is added. The loop
therefore always ends.

Rejected:

- A blocked draft: the cycle needs nothing to go on.
- Correcting at any price: the correct block would be lost.
- An override flag: a switch the orchestrator sets itself.

Where else this shows:

- D7 gains the variant row.
- Step 12's "mark ready" in D2 now excepts `blocked` and `draft`.
- The row-6 decision's meaning carries the exception as a foreseen one in its binding sentences, as
  the decisions template asks. Since the row's words do not hold it, the spec marks it as a cycle
  choice beyond the task, for this task's own request.

## The reviewer's open search: a the-way change carrying a plan's position

Settled in D8 and D4:

- `--task` is the document the change carries out: the task document, or the project plan that
  holds the position. The README already says the reviewer receives "the task or the plan's
  position".
- A document with neither `### Need` nor `### To do` is measured on its whole text other than
  headings, table header rows and table separators. The plan template keeps those in English and
  its text in the definition's language (`project-level/plan/template.md:18-23`).
- So the block's language is judged on both. The script reads `not judged` only below the minimum
  of words, as for any short document.
- D4's tests gain a case for a document in a plan's form.

## What else changed

Nothing beyond what the findings and that search reach. The headings, the template's place, the
record's fields, the decision section's sources, the entries of rows 1, 2, 3 and 5, and WAY-134 and
WAY-10 stand as before.

## Checks

The four checks of the method were read again over the revised spec:

1. No placeholder, `TBD` or empty section.
2. No contradiction found. The step-12 and blocked orders now agree across D2, D3 and D4. The
   `draft` state of D4 matches D1's definition of `draft` (a draft left so for another named
   reason) and D7's row. The gate clause kept in WAY-114 matches the files D2 names as holding.
3. Still one change.
4. Two readings settled in this revision: what the committed record holds on each route; what the
   script reads for a plan.

No tests were run. A spec has none. `git status --short` in the worktree is empty: no tracked file
changed.

## Reaches beyond the handoff

- `elements/common/critique/SKILL.md:18-24`, `elements/glossary/template.md:44-50`,
  `elements/common/projected_mode.md:14-20` and `project-level/skill/SKILL.md:162-170`: the lines
  the review cites, read to settle findings 1 and 2.
- `project-level/task/template.md:180-205`: whether the task template restates acceptance at the
  merge. It does not.
- `project-level/plan/template.md:18-23`: the language of a plan's text, for the plan case of D8.
- A `grep` outside `.runs/`, `docs/` and `foundations/` for "at the merge", "by merging", "WAY-114",
  "WAY-10" and "WAY-134", for finding 2.

## Searches not found or unclear

- `task-cycle/skill/SKILL.md:193-197` says to "open the blocked draft request" for a question the
  foundation step leaves to the human, but names no route for it: step 12, or a pair-first route as
  in `blocked_finding.md`. The spec takes it as step 12, since the cycle's steps have run to that
  point. A different reading only moves that request between D3's two route groups.
