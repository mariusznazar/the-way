PASS dc18abf32122d3f7466d629edbe904d0e8182cd0

# Review of the reconciliation with the target branch — task `deployment-skill-guide`

Reviewed head: `dc18abf32122d3f7466d629edbe904d0e8182cd0` (`git rev-parse HEAD` in the worktree, equal to the handoff's head). Our change on the new
base is exactly three files (`git diff --numstat 0e1cd3c dc18abf`): `foundations/decisions.md` (36+/10-),
`project-level/task/deployment_skill_guide.md` (352+), `project-level/task/skill/resolve_gaps.md` (5+/1-). The merge brought no change to
any of them beyond ours: the hunks of `git diff aa21be7 dc18abf` in `foundations/decisions.md` fall in WAY-02, 03, 05, 11, 12, 17, 19, 22, 115,
134, 167, 168, 171, 172, 241, 293 (found by locating each hunk's heading), and none in WAY-139, WAY-140, WAY-165 or WAY-270.

## Findings

### Blocking (Critical / Important)

none

### Minor

1. `foundations/decisions.md:4001` and `:4030` — the lines the change reflowed in WAY-139 are left over the width of the lines around them:
   line 4001 ("logs, on the record's life and on a failure, the check quotes the answer a decision of the foundation or an", 107 chars) in the
   binding sentences, and line 4030 ("without the check; the item that a check adds for a missing deployment skill points to the guide,", 101
   chars) in *Verification*. Cosmetic only: no rule of the template or of `foundation_check.py` sets a width (the check reports 0 errors), and
   the entry's meaning is unaffected. Evidence: `git diff 0e1cd3c dc18abf -- foundations/decisions.md`, added lines longer than 100 characters.
2. `project-level/task/skill/resolve_gaps.md:64-67` against `foundations/decisions.md` WAY-139 binding sentences — the sentence that makes the
   *To do* item and the split task name the guide stands in the paragraph on "has none or an item is missing". The three items the check
   handles apart (logs reading, record's life, failure notice; `resolve_gaps.md:71-96`) also add *To do* items that write or record an answer in
   the skill, and the bullets do not say that those items name the guide too; WAY-139's text ("that item and that task point to the guide") reads
   the same way, so the two files agree with each other. A reader could take an agent that completes the skill for one of those three items
   as not pointed to the guide, though the guide's parts 6, 7 and 8 show exactly those cases. Not caused by the merge (it stood at `aa21be7`
   and passed two reviews); task *To do* 2 says the point item and the split task name the guide, which both files do. Kept Minor: no sentence
   a reader would read wrongly was found, the guide is reachable from the first item or the split task in every flow where the skill is
   missing, and the item for a single missing list entry is covered by "an item is missing".

### Out of scope

none

## Question (a): WAY-139 against the merged decisions template and the entries the merge changed

Read whole: `elements/decisions/template.md` (merged), WAY-139 (whole, as merged), WAY-02, WAY-05, WAY-12, WAY-19, WAY-22, WAY-134. Findings of the
comparison, template rule by rule:

- Binding sentences: the first paragraph holds three sentences (The-way holds…; Beside the list it holds a guide…; When a task's outcome…),
  within "1–3". The guide is a part of the same question the heading asks (what the-way holds for the skill), so no paragraph of another
  question is needed (WAY-19, WAY-05). No `should`/`will`/capital keywords; present tense. Passes.
- Third sentence is long (it carried the check before the change and the change added a clause); that is the shape the entry had, and the
  template sets a count of sentences, not of words. Declined (below).
- Verification: no invariant and no test holds WAY-139 (no `decision: WAY-139` line anywhere in the tree: `grep -rn WAY-139`, only the guide and
  `resolve_gaps.md` cite it), so the pair of examples stays for the whole entry, as WAY-12 and the template's "Verification" allow; the
  added `complies` and `violates` examples describe code/files, not a replacement of the decision. The foundation check treats the entry as
  held (0 errors, although the binding sentences changed).
- Rationale and *Rejected*: no file name, script or count in the added prose; no history of how the decision was reached; "the one skill that exists"
  is a fact about a product's skill, not about the process's tools. *Rejected* — the rule of WAY-134 (only ways the row's source keeps, each with its
  cost or reason) — compared with the task's *Questions to settle* 1 and 2, *Not chosen*: text of the guide in the step, directory of its own,
  nothing; the whole skill copied, a frame with no fragments; each of the five appears with the reason the task gives (public address and
  mailbox, ageing; reading by every refinement and mixing with the binding rule; change of WAY-09 and the part map for no reader gain; today's
  cost zero and paid by the next product; the reader separating general from particular alone). No way derived by the writer entered.
- Where it goes (WAY-293, the new bullet): the settlement is an edit of an entry that already answers the question (question 5), and the
  instruction part stands in `resolve_gaps.md`, which names WAY-139; the entry carries a choice with real cost and rejected ways. Passes.
- Entries the merge changed that do not bear on WAY-139's form or the guide, and which I did not read whole: WAY-03, 11, 17, 115, 167, 168, 171,
  172, 241, 293 (see Unread material).

## Question (b): `resolve_gaps.md` and the guide against WAY-139 as merged

Agree. WAY-139 says: the guide binds nothing; the check of the list points to it; the item and the split task point to it; an agent reads it only
when it writes or completes a deployment skill. `resolve_gaps.md:64-67` says the same, names the guide by path (the file exists), and says the
list and the check bind. The guide's "Who reads it, when" and "It binds nothing" (lines 9-19) say the same again; its eight parts match the
seven list items plus the description part; WAY-140, WAY-165 and WAY-270, which the guide cites, are untouched by the merge and the guide's use
of them is as before. Only Minor 2 above.

## Question (c): does an entry the merge brought in contradict the guide?

No. The merge's changes are on the form of the decision log and its template, the task template's column *Kind* renamed *Goes to*, the foundation
and return steps, the request template and guidelines templates; none says anything on deployment skills, logs, secrets or failures, and the
guide cites no word of the changed entries. The guide's wording about *To do*, the human action and a split task agrees with
`project-level/task/template.md` as merged. The frozen task document still names its table's column *Kind*; it is a frozen document, not a
file of this change.

## Question (d): the foundation's own check on the merged tree

`python -B elements/common/foundation_check.py` — `0 errors`, exit 0.

## Privacy

Searched the changed text of our change (`git diff 0e1cd3c dc18abf`) for the game's public address, for the sender mailbox address in the author's
domain (both taken from loop2's files at `e54f23c0ea3bd1db13d2635333417eb50412d6a0`), and for the other host name that commit holds in its setup
reference: no match (grep exit 1). The only occurrences of the author's account name are the two links to that commit of loop2 (required by the task).

## Declined to judge

- WAY-139's *Verification* opens "an agent compares the work with the decision:" where the merged template's form reads "an agent compares a change
  with the part no invariant and no test holds:" — the wording stood before the change and the merge, outside this task.
- The very long third binding sentence of WAY-139 — it grew with the check before this task; splitting it would restructure the entry beyond the
  task's *To do* 7.
- The frozen task document's table column *Kind* against the merged template's *Goes to* — the task document is frozen and belongs to the cycle.

## Checks run

- `git rev-parse HEAD` — `dc18abf32122d3f7466d629edbe904d0e8182cd0`; `git status --short` — clean.
- `git diff --numstat 0e1cd3c dc18abf` — three files (above), exit 0.
- `git diff aa21be7 dc18abf` (hunks located by heading) — the merge touches the entries listed above, none of WAY-139/140/165/270.
- `python -B elements/common/foundation_check.py` — `0 errors`, exit 0.
- `python -B instruction-files/check_instructions.py .` — `0 error, 0 warn, 3 info`, exit 0.
- Privacy grep over `git diff 0e1cd3c dc18abf` for the address strings — no match.
- `grep -rn "WAY-139"` over the tree (outside `.runs/` and `.git/`) — no test holds a sentence of WAY-139.

Not run: the product's full gate (the orchestrator runs it); the `project-level` tests and the other test files, since nothing in the three files is
read by them (`project-level/task/` holds no test and no script reads the guide).

## Reaches beyond the dispatch

- `elements/decisions/template.md` (merged), WAY-02, WAY-05, WAY-12, WAY-19, WAY-22, WAY-134 read whole in `foundations/decisions.md`, by the handoff's
  list of the entries that bear on WAY-139's form.
- `git diff aa21be7 dc18abf` for `task-cycle/skill/foundation_step.md`, `return_step.md`, `elements/decisions/skill/SKILL.md`, `decide_entry.md`,
  `project-level/task/template.md` and `elements/common/skill/task_variant.md`, `build_table.md`: to check (c).
- `project-level/task/skill/resolve_gaps.md` lines 50-100 and the guide `project-level/task/deployment_skill_guide.md` whole; the loop2 repository
  at `the local checkout of loop2` (`git grep` at the commit) only for the privacy strings.
- `.claude/skills/the-way-refine-task/SKILL.md` and `installation/install.py` (grep), to see whether a list of files names the guide; none does.

## Unread material

- WAY-03, WAY-11, WAY-17, WAY-115, WAY-167, WAY-168, WAY-171, WAY-172, WAY-241, WAY-293: not read; I located their changed hunks and read the
  merged template and the diffs of the skills that apply them, which say what they changed for the decisions' form. They concern invariants, task end,
  relations, finding entries, and product guidelines, not WAY-139's form or the guide.
- WAY-140, WAY-165, WAY-270: not read whole; read as quoted in the task's *Decisions in play* and as cited in the guide; the merge did not touch them.
- The three `references/` files of loop2 at the pinned commit and the fragments of the guide against them: not re-verified (earlier reviews did; the
  merge does not touch the guide or the loop2 commit).
- The task document: read whole.

## Searches not found or unclear

- A test or invariant that holds any sentence of WAY-139: not found (none exists; the pair of examples holds the entry).
- A width rule for the lines of `foundations/decisions.md`: not found in the template, `rules.md` or the check.
- Whether WAY-139's "that item and that task point to the guide" covers the *To do* items of the three items handled apart: unclear (Minor 2).
