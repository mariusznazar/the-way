FAIL a900916e8980eaf6d913e2c8bd0b6cbd212deb21

# Review of the whole change — task `deployment-skill-guide`

Range: `d40d1cb942c4fbaddb7ece1dc6d472d15cd83430..a900916e8980eaf6d913e2c8bd0b6cbd212deb21`, one commit by one
author, no plan, no slices, no spec. `git rev-parse HEAD` in the worktree is the head given. Changed files:
`project-level/task/deployment_skill_guide.md` (new, +336), `project-level/task/skill/resolve_gaps.md` (+5 -1),
`foundations/decisions.md` (WAY-139, +32 -6). Trust boundary: no. Irreversible operation: no.

Result in one line: 2 blocking findings (Important), 4 Minor within the task, 1 Minor outside the task.

## Findings

### Important (blocking, within the task)

**I1. The guide defines when a skill covers an item, against its own "it binds nothing" and WAY-139.**
Place: `project-level/task/deployment_skill_guide.md:31-33` (and, in the same vein, `:273-277`).

- What is wrong. "How to read a part" says of the questions of each part: "An answer that settles each
  question, or says in the skill that the human left it unsettled, covers the item." That is a rule for
  when an item is covered, and its measure is the guide's own questions. The same file says at `:15-17`
  that "Whether a skill covers an item is decided there [the list in WAY-139 and the check in
  `resolve_gaps.md`], not here." The two sentences contradict each other, and the first is the one a reader
  applies. The same reach shows in part 7 (`:273-277`): "A complete answer is one of two: a stated lifetime
  for each place, with what bounds it and what it misses; or the human's refusal". WAY-139 says only that a
  skill that records the refusal covers the item; WAY-165 says what the record asks; neither says that a
  lifetime "for each place, with what bounds it and what it misses" is the complete answer. (Part 8's "a
  complete answer is one of three" at `:309-311` restates WAY-270 and WAY-139 and is not part of this
  finding.)
- Why it matters. WAY-139 (its own *Verification*, `foundations/decisions.md:3918-3919`) names as a
  violation "the guide stands as a skill that a product applies as it is, or as a condition that a skill
  must meet to cover an item". A reviewer or the check, meeting a skill that answers the list but not every
  question of the guide, has a sentence in a the-way file that says it does not cover the item. Task item 6
  requires that the guide binds nothing; the explicit sentence at `:15` meets it, `:31-33` takes it back.
  Under WAY-263 a file that restates what the decision settles, broader or differently, is Important.
- Evidence. The two quotations above, read side by side; the decision's violation clause at
  `foundations/decisions.md:3918-3919`; `resolve_gaps.md:66-68` ("The guide binds nothing: the list and this
  check do").
- Fix direction. Say that the questions help to write an answer and that the list and the check decide
  coverage; drop "covers the item" from `:31-33`, and word part 7's two kinds as examples of an answer, not
  as the definition of a complete one.

**I2. A fragment cuts the qualifying clause of a sentence and so says what loop2's skill does not say.**
Place: `project-level/task/deployment_skill_guide.md:222`.

- What is wrong. The fragment reads "Every server or Cloudflare change is the human's, … The agent prepares
  the commands." The source sentence (`.claude/skills/loop2-deploy/SKILL.md:102-103` at
  `e54f23c0…`) is "Every server or Cloudflare change is the human's, except deployment started by the
  existing automation. The agent prepares the commands." The `…` marks a cut, but the cut takes the exception
  that makes the sentence true for loop2. The author's report names the cut (choice 3) and the reason: the
  exception would sit awkwardly beside WAY-140.
- Why it matters. (a) Task and WAY-139 require fidelity: "nothing the change takes from them altered". The
  cut changes the claim from "all but automated deployment" to "all". (b) The guide contradicts itself: part
  1 (`:64-66`) shows a push to `main` starting an SSH call that runs the installed deploy script, and part 5
  then says every server change is the human's. A reader who asks "what does the agent do, what does the
  human do, and what does the automation do" gets, from part 5, no third actor, though that third actor is
  the most common case of the item. (c) The reason given does not hold on its face: WAY-140
  (`foundations/decisions.md:3973-3976`) speaks of a task's effect outside the repository made through a human
  action the task names; code a human merged that an existing automation then deploys is not shown to
  contradict it, and the guide's own part 5 lead-in already states WAY-140 on its own. If the human holds
  that it does, that is a decision about WAY-140 for the human, not a cut in a quotation. The author's
  rationale does not lower the grade.
- Evidence. `git -C the local checkout of loop2 show e54f23c0ea3bd1db13d2635333417eb50412d6a0:.claude/skills/loop2-deploy/SKILL.md`
  lines 102-103; the guide lines `:64-66` and `:222`.
- Fix direction. Quote the whole sentence, mark the exception as loop2's (`[loop2: …]`) and, if the human
  wants it, say in one sentence in the guide that an automated deployment on merge is the third case a skill
  names beside the agent's reads and the human's changes.

### Minor, within the task

**M1. Unmarked loop2 parameters in fragments, against the guide's own marking rule.**
Place: `deployment_skill_guide.md:320` ("At most one message per kind in six hours and six in all in 24
hours"), `:322-324` (the scheduled check's "Every five minutes … up to six attempts 20 seconds apart"), `:281`
("not above about 100 MB"), `:145-146` ("players stay signed in"), `:315-316` ("both containers").
The guide says (`:34-38`) that loop2's own — "commands, paths, names and deployment parameters" — stands
inside `[loop2: …]`, and task item 4 and WAY-139's *Verification* (`:3909-3910`) require loop2's own parts to
be marked. The commands, paths, server and Cloudflare settings are marked throughout; these numbers and
intervals are values loop2 chose, and a reader who keeps "the shape outside the brackets" would copy them.
Effect is small (no command and no address is involved), hence Minor. Fix: put each in a marker.

**M2. Fragments join sentences from different places of the source, or reorder them, under one quotation;
a few statements about the source are not true as written.**
Place and evidence:
- `:187-191` (part 4): the guide puts "This is **script installation, one deployment and four Cloudflare
  changes**; public traffic can be unavailable…" before item "3. Restore the Origin Rule…". In
  `references/troubleshooting.md:162-170` the four items come first and "This is…" follows them.
- `:222-223` (part 5): "Treat service logs as potentially sensitive; report selected, redacted diagnosis,
  not raw logs." comes from `SKILL.md:115-116` ("Seeing deployments"), joined by `…` to `SKILL.md:102-103`.
- `:287-289` (part 7): "The file holds the game's lines for those weeks, with `accountId` values …" comes
  from `SKILL.md:279-281` ("How an agent reads it"), joined by `…` to the paragraph "How long each lives"
  (`SKILL.md:268-274`).
- `:152`: "A list of rotations ends the file" — in `references/setup_and_secrets.md` a "Sources" section follows
  the rotation list (`:615` onward). `:259`: "The table is loop2's own, from its deploy script" — `SKILL.md`
  carries the table and does not say it is copied from the script.
Why it matters: the `…` shows that something is missing but not that the pieces lie elsewhere or in another
order; a reader opening the source to see the context does not find it where the fragment implies.
No number, command or meaning is changed by these. Fix: keep the source order, name the section a spliced
sentence comes from or take it as a separate fragment, correct the two statements.

**M3. The binding sentence of WAY-139 reads as if the guide were an eighth item of the list.**
Place: `foundations/decisions.md:3868-3873`. The list is introduced by "the list of what a product's
deployment skill covers:" and runs on with semicolons to "…how a human learns of a failure; and, beside the
list, a guide to writing such a skill…". A reader reads the guide as one more thing a skill covers; "beside
the list" is the only sign it is not. The sentence at `:3873-3878` has also irregular line breaks ("When" at
the end of line 3873; line 3878 much longer than the rest) from the in-place edit. Task item 7 asks for the
guide beside the list. Fix: close the sentence of the list at "failure" and open a new one for the guide.
Minor because the *Verification* and *Rationale* of the same entry say the guide is beside the list and binds
nothing; the foundation check (`foundation_check.py`) passes.

**M4. "A preview of deployments" is read as if the list defined it.**
Place: `deployment_skill_guide.md:77-79`. WAY-139 does not define the item and nor does the task; the guide
writes "The skill of loop2 answers it in two places", which presents the author's reading (choice 1 of the
report) as the item's meaning. The reading is reasonable and part 2's questions cover the other likely
reading too (a change deployed to look at before it reaches the main line, `:83-84`), so a product with
per-branch preview environments is not left without a question. Fix: one clause saying the list does not
define it and the guide reads it as both. Minor.

### Minor, outside the task

**M5. WAY-09 and the part-map sentence of `project-level` do not name a guide.**
Place: `foundations/decisions.md:238-240` (WAY-09's list for `project-level/`) and
`foundations/part_map.md:77-83`. The author reports this as an observation. The file lies in
`project-level/`, which the invariant `repository-file-location` allows, and WAY-139 itself has Scope
`project-level`; but the part-map sentence gives refinement of a task as the part's reach, while the guide is
read by the agent that writes the skill in the cycle. The task says WAY-09 stays unchanged, so this is outside
the task; whether a word is worth adding is for the human.

## Check of the task, item by item

1. New file in `project-level/task/`, name chosen by the cycle: met (`deployment_skill_guide.md`).
2. Step `resolve_gaps.md:61-68`: item and split-off task point to the guide; the agent that writes or
   completes the skill reads it; refinement of any other task does not: met. Matches WAY-139's new sentence
   (`:3877-3878`) without restating it more broadly.
3. One part for each of the seven items and one for purpose and description: met (parts 1-8, headings follow
   the list's wording).
4. Questions and a short fragment in each part, what is loop2's marked: met in form (119 of 336 lines are
   quotation, none longer than 22 lines); marking incomplete, see M1; fidelity, see I2 and M2.
5. One commit, links with the full SHA, addresses replaced: met. Both links (`SKILL.md` and the `references/`
   tree) use `e54f23c0ea3bd1db13d2635333417eb50412d6a0`, return HTTP 200 and the repository is public. No
   fragment carries an address; the guide names the two example addresses in its own text (`:37-38`).
6. States that it binds nothing and that it is no ready skill for any kind of server: stated at `:15-19`,
   but undermined by `:31-33` (I1).
7. WAY-139 changed in place: sentence, *Verification* (one `complies`, one `violates` clause), *Rationale*,
   *Rejected* with all five ways not chosen (three under question 1, two under question 2), each with its
   cost as the task gives it; *Scope*, *Based on*, *Relations* and *Origin* unchanged. Met, except M3's
   wording and I1/I2 which concern the guide the entry describes.

Settlements to record: row 1 (the guide beside the list, loop2 first example, binds nothing, pointed to by the
check, changes WAY-139) is in the binding sentence, *Verification*, *Rationale* and *Rejected*; row 2 (fragments
of one commit with link, loop2's marked, no real addresses, example domain) is in *Verification*, *Rationale*
and *Rejected* and in the guide. Both are written whole; the meaning matches the task's rows. No second entry
and no other entry restates the old sentence "holds no skill of a product, only the list" (my own grep of
`.md` and `.py` outside `.runs/` for `holds no skill`, `deployment skill`, `WAY-139`: the other hits cite
WAY-139 as the check of the list and are unchanged in meaning).

Privacy. I searched the four loop2 files at the commit for the game's public address and for a sender
mailbox address in the author's domain (any address with `@`, and the account name in any form, case
insensitive). Result: the files hold both, in several places. I searched the whole changed text — the diff of
the range, the three files at the head, and the commit message — for the same: none found; the account name
stands only in the path of the two GitHub links, as the task allows. I also searched the loop2 files for IP
addresses: only loopback ones, which the guide does not carry.

Own-work check of the author. The requirement it names (nothing of loop2's own unmarked, each fragment a true
excerpt) is where the change is weakest, and its script check would have caught a changed word but explains
away, as artefacts or as the "adaptation", the cut clause (I2) and does not look at order or at splices
(M2). Its 11 explained differences I checked by reading: the guide's own sample wordings for part 7 and 8
are labelled as the guide's own (`:291-295`, `:333-336`), the table keeps three rows, the sentence on the
owner's private note is adapted as `:39-40` says. I found no changed command or number.

## The structure the change leaves

Sizes from `python -B task-cycle/change_file_sizes.py d40d1cb… a900916…` (exit 0): `foundations/decisions.md`
12610 to 12636 lines (+26); `project-level/task/deployment_skill_guide.md` new, 336; `project-level/task/skill/resolve_gaps.md`
87 to 91 (+4). The-way has no coding guidelines of its own for this kind of change (WAY-328), so there is no
size rule and no invariant test to run on base and head; the numbers and the diff are my material. The
guide's 336 lines are read only by the agent that writes a deployment skill (the pointer is the only thing the
step adds), so the growth costs no other refinement; no finding. WAY-139's entry grew to 105 lines, within the
shape of other long entries of the log. No code, no function, no name that stopped being true (`WAY-139` heading
still fits).

## Declined to judge

- Whether `project-level/task/` is the right place against WAY-256 (a file beside the skill that names it, here
  `project-level/task/skill/`): the task fixes the place and the guide is no fragment of a skill.
- The content and quality of loop2's own skill, and any change to it: out of scope (task *Out of scope*).
- Whether WAY-140 should admit an automated deployment of merged code as a human's act: a decision on a
  foundation entry the task does not change; raised only as the question under I2.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Head | `git rev-parse HEAD` in the worktree | 0, equals `a900916e…` |
| Foundation form | `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| Private paths and note links, the guide and `resolve_gaps.md` | `python -B task-cycle/private_paths_check.py <file>`, each of the two | 0, 0 listed each |
| Invariant `tracked-file-private-paths` | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (298 files, 0 listed) |
| Tests of the part | `python -B -m unittest discover -s project-level -p "test_*.py"` (in the background, 207 s) | 0 (275 tests, OK) |
| Sizes of changed files | `python -B task-cycle/change_file_sizes.py d40d1cb… a900916…` | 0 |
| Links of the guide | `curl -s -o /dev/null -w "%{http_code}"` on both URLs; `gh repo view mariusznazar/loop2 --json visibility` | 0; 200 and 200; PUBLIC |
| Fragment fidelity | manual: each blockquote of the guide read against `SKILL.md` (whole), `references/setup_and_secrets.md` 145-210, 325-360, 585-621 and `references/troubleshooting.md` 150-184, extracted by `git show e54f23c0…:<path>` into the scratchpad | method; result in I2, M1, M2 |
| Privacy | `grep -E` over the four loop2 files and `grep -i` over the diff, the changed files and the commit message | 0; result as above |
| Reviewed worktree unchanged | `git status --short` after the checks | empty |

Not run: the full gate (the cycle's own run). No failing-first test applies: the change is prose and no
invariant's test is new or changed. No invariant test was changed.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-07 (whole), to check the in-place edit of WAY-139; named by the task.
- Invariants `repository-file-location`, `foundation-file-kinds`, `outbound-link-reach` (whole) and the glossary
  entry `human action`, to judge the location of the guide and its links.
- `foundations/part_map.md` entry `project-level` (whole), for M5.
- `project-level/task/skill/resolve_gaps.md` lines 50-100, for I1 and the step's own wording.

## Unread material

Counts for my own selection by "Reading the foundation": the touched part is `project-level`, and WAY-139
names `project-level` alone in its Scope. The decision log has 329 decisions; 79 name `project-level` in
*Scope*. I read **12 whole** and **67 by title only**.

- Read whole: WAY-09, WAY-100, WAY-134, WAY-139, WAY-140, WAY-165, WAY-256, WAY-270, WAY-308, WAY-313,
  WAY-314, WAY-315. WAY-07 I also read whole, as a reach outside the selection (its *Scope* does not name
  `project-level`).
- By title only (67), including those whose titles I judged not to bear on the change; none of the unread
  titles pointed to a bearing, but I did not open the entries on technology choice and on the project
  definition (WAY-106 to WAY-123 apart from WAY-100, WAY-124, WAY-137, WAY-138), the plan entries (WAY-142 to
  WAY-156, WAY-230), the guideline-finding entries (WAY-214 to WAY-218, WAY-247) or WAY-127, WAY-150, WAY-267
  to WAY-269, WAY-309, WAY-328 (named in the handoff: I take from it that the-way has no guidelines of its own
  for this kind of change). WAY-267 and WAY-309 bear on the check's neighbours; I did not need them for any
  finding, but I did not read them.
- Invariants: only the three named above read whole; the others whose *Part* is `project-level` or `every`
  seen by identifier and *Part* only. Glossary: `human action` only. `elements/decisions/template.md` not
  read; the entry's form I trust to `foundation_check.py` (exit 0) and did not compare myself.
- Guidelines: none exist for the-way for this change (WAY-328); none read.
- Author's report: read whole. Frozen task: read whole.
- Loop2 at `e54f23c0…`: `SKILL.md` whole; `references/setup_and_secrets.md` lines 145-210, 325-360, 585-621
  only (the author read 100-210, 329-383, 479-621; so lines 1-144, 211-324, 361-584 are unread by me,
  though the whole file was covered by my privacy search); `references/troubleshooting.md` lines 1-40 and
  150-184 (the author read 1-40, 95-184) — lines 41-149 and 185-203 unread, whole file covered by the privacy
  search; `references/backup_and_restore.md`: no passage read, covered by the privacy search only.
  Nothing in the guide quotes the unread passages, so none of my fidelity judgments rests on them.
- WAY-140: read whole, including its *Rationale* tail the author did not read.

## Searches not found or unclear

- The meaning of "a preview of deployments" in WAY-139: no definition in the decision, the task, the
  glossary or my grep of the repository (`preview of deployments` appears only in WAY-139 and the guide).
  Unclear; see M4.
- A loop2 passage for the human's refusal of an item or for a deliberate absence of a notice: none exists, as
  the author reports; the guide's wording for both is labelled as its own and I accept that.
- A statement in WAY-09, the part map or WAY-139's scope that the guide belongs to refinement or to the cycle:
  not found; see M5.
- Whether the human accepted the exception's omission (I2) before the cut: the frozen task is silent on it;
  `task.md` gives no instruction on quoting the sentence.
- Guidelines for the-way's own prose files: none (WAY-328 covers code and tests only); I judged the
  guide against the task, the decisions named and the form of neighbouring step files.
