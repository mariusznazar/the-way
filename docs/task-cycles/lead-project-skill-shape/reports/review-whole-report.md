PASS 038a3301e8ca3eee1969b2b94576f0328109e436

# Review of the whole change — task `lead-project-skill-shape`

Range `57795e4..038a330` (commits `e98f46b`, `b9e19f7`, `038a330`); `git rev-parse HEAD` in the worktree is
`038a3301e8ca3eee1969b2b94576f0328109e436`, the head given. One-author change without a plan and without a
spec: this review judges all of it. Trust boundary: no. Irreversible operation: no. I made no change and no
commit (`git status --short` is empty).

Summary: the change carries every item of *To do* 1–7, every acceptance criterion and the accepted row 1. The
moved text is word-for-word equal to the base except at the places the author lists as rewords; every number I
recomputed agrees; no rule disappears or changes meaning. No blocking finding. Six Minor findings, all inside
the task's scope, none out of scope.

## Findings

Blocking (Critical / Important): none.

### Minor 1 — `foundations/decisions.md:7646–7647` and `:7685–7687` (WAY-256 *Rationale* and *Rejected*): the "five to fifteen percent more words" figure is an estimate of a layout nobody built, stated without what was measured

Within the task. The *Rationale* says "estimated from the files of one skill, that shape reads five to fifteen
percent more words in a typical session than keeping its steps in `SKILL.md`", and *Rejected* repeats "an
estimated five to fifteen percent more words read in a typical session". WAY-05 lets a rationale hold "a
measurement the choice rests on ... with what was measured and under which conditions". The figure is the
task's own estimate for the full shape of `lead-project` (task question 3, "pełny kształt ... +5 do +15%");
the full shape was not built, so nothing was measured, and the entry names neither the skill nor what was
counted (files of the skill, words). "Typical session" is a condition, so this is not the case WAY-05's
*violates* example gives (a bound with no conditions); the entry is not wrong, only thin. The author's report
(choice 7) already says the reviewer may want it out.

Evidence: WAY-05 text; the author's measured result for the chosen shape (skill text -3.8% to -21.1% on the six
roads, files together +277 words) does not test the unbuilt shape. A reading that stays within WAY-05: say it is
an estimate made before the rebuild, from the word counts of the files of `lead-project`, or drop the figure
from one of the two places. Not blocking: the figure comes from row 1's source and is labelled "estimated".

### Minor 2 — `project-level/lead/skill/SKILL.md:176–181` (step 5 pointer): the road "recovery of a pending gate or recheck in step 0" does not say whether `route_changes.md` is read

Within the task. The first sentence sends to `route_changes.md` "from a refiner's result `plan change` or from
a changed definition in step 0"; the second sends to `definition_change.md` for a change of the definition, its
gate or the plan recheck, "a gate or recheck found pending in step 0 included". A pending gate found at the
start is not obviously "a changed definition", so the first sentence may or may not apply. In the base the agent
read the whole of step 5 on this road. What `route_changes.md` bullet 1 holds that the recheck also needs: "Stop
your shared-plan writes until it returns ... Human questions and required critique requests return through the
file, for you to dispatch/present and record. Read its result and rerun the whole-plan check before resuming
state updates or affected refinement" (the recheck of `definition_change.md` bullet 3 dispatches the same kind
of `plan-project` agent). `definition_change.md` bullet 3 keeps "serialized shared-plan ownership", "readiness
writes blocked" and "logged corrections", and step 1 (`SKILL.md:73–75`) keeps "Run `plan_check.py` after plan
changes", so what can be lost is narrow: the rule that questions and critique requests of that agent come back
through the file, and the explicit rerun of the whole-plan check before resuming. Fix: either word the first
sentence to include the pending gate or recheck of step 0, or repeat nothing and let the second sentence say
"read `route_changes.md` too". Evidence: reading of the stub against base lines 190–219 (`git show a3206c1:project-level/lead/skill/SKILL.md`).

### Minor 3 — `project-level/lead/skill/definition_change.md:23`: "this route" has no antecedent in the new file

Within the task. The moved sentence "A check passing the old fingerprint or approval alone does not complete this
route" stood under the step heading "Route plan and definition changes"; the new file's heading is "Change of
the definition and its gate", and `route_changes.md` (the other half of that old heading) is a separate file.
The reading is easy (the route of the definition change), but the criterion asks for each demonstrative of a
moved sentence to be read alone and the author's own-work check (section 9 of the report) lists "its", "it",
"either mismatch", "the file" and "Left in place", not "this route". Meaning is not lost. Fix: "does not complete
this change" or "does not complete the recheck".

### Minor 4 — `foundations/decisions.md:7601, 7659, 7662, 7688, 7691, 7692, 7696`: the "reflow" commit left seven lines of the WAY-256 entry over 100 columns

Within the task. `038a330` is described as a reflow of the rationale and rejected ways; a word-level diff of
`e98f46b` against `038a330` (`git diff -w --word-diff=porcelain`) shows only line breaks moved, as claimed, but
`awk 'length($0)>101'` still finds seven long lines in the entry (103, 102, 119, 102, 103, 109, 123 characters);
the rest of the entry and the log wrap at 100. Cosmetic: noisy diff for the next editor.

### Minor 5 — the request's word-count columns "with the step-0 files" mix two bases

Within the task (acceptance criterion on the numbers). The "before" column uses 9833 (7253 of the side files at
`a3206c1` plus 2580), the "after" column 7255 of side files at the head, because `conversation_template.md`
grew by two words between `a3206c1` and `57795e4`. So "-96 (-1.0%)" on road 1 is the real -98 of the skill text
plus the two words of an unrelated merge. The author's report discloses it (section 5, last list). The request
should say so beside the table or give the side files at one commit in both columns; the skill-text columns are
exact and unaffected.

### Minor 6 — `project-level/lead/skill/technology_run.md:3`, `task_return.md:3–4`: two opening lines are given "no exclusion" or an exclusion that is the pointer itself

Within the task. The criterion asks the author to name what each new sentence excludes. For `technology_run.md`
the report says "nothing but orientation"; for `task_return.md` it says the line excludes "the transitions that
step 1 supports from evidence", which the condition of the same line ("when the human has said that the blocked
request of a task is closed") does. Both sentences are harmless (they restate the condition of the pointer in
`SKILL.md` and add no road; I compared them with the pointers: same conditions), so this is a matter of the
request giving the honest entry for each: "restates the pointer's condition, adds none".

## Per-item coverage (To do 1–7, acceptance criteria, accepted row 1)

| Requirement | Carried? | Shown at |
|---|---|---|
| To do 1: WAY-256 changed in place by row 1; sentences contradicting row 1 gone; *Rationale* and *Rejected* from the source; old rule's repeats changed | Yes | `foundations/decisions.md:7592–7700`; `:3033–3040` (WAY-125), `:3145–3149` (WAY-127); `instruction-files/kind_skill.md:8–21`. My own search (see *Searches*) found no remaining place that states the old rule as binding |
| To do 2: `lead-project` judged, records searched before the table | Yes (as a report: section 2 and 3 of the author's report, 8 uses, table of 55 rows); the judging itself is not in the diff, the diff is its product | author report; records themselves not re-searched by me |
| To do 3: steps 0–4 stay; step 5 and three variants go to files; `SKILL.md` names each file at its step with the condition (WAY-265); headings 0–5 and numbers 3.1–3.6 stay | Yes | `SKILL.md:62–65` (return), `:103–105` (technology, 3.1), `:119–121` (3.3), `:176–181` (step 5); headings and 3.1–3.6 unchanged in the diff |
| To do 4: nothing outside `project-level/lead/skill/` and point 1 | Yes | `git diff --stat 57795e4..038a330` lists only the seven files; `answering.md`, `conversation_template.md`, other skills, Python, `description` (SKILL.md lines 1–4) unchanged |
| To do 5: table of assessment, verbatim, line ranges on `a3206c1`, when/recognised/verdict/place | Yes, author report section 3, 55 rows | I verified 40 quoted fragments against `a3206c1` (all found, 38 inside the line range they cite; row 46's range is right, my check cut it) and the 15 other rows (proposals, rewords) against the head text |
| To do 6: word counts on the six roads | Yes | recomputed below, all agree |
| To do 7: `remove`/`reword` that change a rule's content | None exist | report section 4; my word diff (below) finds no content change |
| Criterion: no rule disappears or changes meaning | Met | word diff of the base `SKILL.md` against the five head files: 22 differences, listed below |
| Criterion: reworded conditions compared with base; no road added or lost; each new sentence's exclusion named | Met except Minors 2 and 6 | below |
| Criterion: pointer conditions for the listed roads | Met (Minor 2 on one road) | below |
| Criterion: moved sentences read alone; references from remaining steps still land | Met (Minor 3) | below |
| Criterion: outside readers land under the same heading | Met | below |
| Criterion: WAY-256 within three binding sentences; rationale from the source; rejected from the ways not chosen | Met (Minor 1 on the estimate) | below |
| Criterion: manual walk of roads 1, 4, 6 and the rows compared with the places | Done | below |
| Criterion: `description` and Python unchanged; entry points unchanged | Met | `git diff` of lines 1–4 empty; `python -B gate/run_tests.py agent-instructions` exit 0 |
| Criterion: word counts after the last change; disagreements reported | Met | below |
| Accepted row 1 | Carried | the entry's wording matches row 1: a step stays in `SKILL.md` until records a person can open show part of the uses pass it by, also with no record; variants and such steps go beside; the third sentence unchanged (compared word for word with `a3206c1`: unchanged apart from line breaks) |

## Rule preservation

Method: the base `SKILL.md` (`57795e4`, which differs from `a3206c1` for this file by the two lines the handoff
names) was compared word by word (`difflib.SequenceMatcher` over the words) with the concatenation of the five
head files. The 22 differences are: the five-word pointer in step 0; the step-1 pointer replacing the moved
row-return text; the standalone `Never run git fetch --prune` bullet (the same words, now outside the variant
bullet, the leading "- " only); the 3.1 pointer replacing the moved dispatch sentence; the 3.3 pointer replacing
the moved sentence; the step-5 stub; the opening lines of the four files; and the five rewords the report lists
(`after item 3`, `the reader (plan_state.py) ... as SKILL.md step 1 gives for a conflicting trace`, `in the round
package of 3.3 once`, `(3.6 of SKILL.md)`, `, by definition_change.md`, `from its step 0`). Everything else in
the moved text is equal word for word. No `remove` and no content-changing `reword`.

Reworded conditions against base, by road:

- Task return, step 1 at the start and step 1 repeated after a merge: pointer is "Each time you reach this
  step, at the session start or after a merge in the middle of it, read `task_return.md` ... when the human has
  said so". The base rule stood in step 1 and applied when the human said it; same road, stated by reaching the
  step. A road is not added. One possible reading gap is listed under *Searches unclear*.
- `settle-technology` run, first and every later turn, also after resuming: 3.1 pointer says "in any turn of a
  round, one resumed from the conversation files included"; the condition is a refiner's *Child-work request*
  for the run, as in the base. 3.3 pointer: "A run of the step that settles technology in the conversations
  enters the package as `technology_run.md` gives; read it unless 3.1 did" matches the base condition (a run
  held in the conversations) and adds the standard "unless an earlier step did".
- Step 5, `plan change` after 3.6 and a changed definition in step 0: the stub names both ("from a refiner's
  result `plan change` or from a changed definition in step 0"). The paragraph after 3.6 still says
  "`plan change` reaches step 5"; step 0 still says "A changed definition follows step 5 below". Both land on
  the heading `## 5.`, which stays.
- Definition change, step 5 and the recovery of an open gate in step 0: step 5 stub names it; step 0 gains
  "Step 5 gives that recovery". The base had no pointer from the recovery sentence at all. See Minor 2 for the
  one open point.
- Excluded roads checked: a plan change without a definition change reads only `route_changes.md`; the stub's
  second sentence is limited to the definition, its gate and the recheck; a run of `settle-technology` in a
  round never reads the other files.

## Manual walk (roads 1, 4 and 6 of question 5)

Road 1, steps 0–5 with definition change and gate. Read: `SKILL.md` whole (2036 words): step 0 (the pointer
"A changed definition follows step 5 below", the five-word pointer on recovery), step 1 including the unused
return pointer (53 words), step 2, step 3 including the two technology pointers (33 and 22 words), the
paragraph after 3.6 ("`plan change` reaches step 5"), step 4 ("step 5's definition gate" lands on step 5), step
5 stub. The stub sends to `route_changes.md` (176 words), whose bullet 2 ends "changing the definition does, by
`definition_change.md`", and to `definition_change.md` (270). Stays from the lead's point of view: everything of
steps 0–4 unchanged, the fetch-prune rule, the closure bullet. Drops out: `task_return.md` (246) and
`technology_run.md` (129). Total 2482, base 2580. Every sentence of base steps 0–5 is present on this road.

Road 4, return of a task, then steps 0–5 with a plan change. Read: `SKILL.md` to step 1; the bullet at lines
62–65 sends, when the human has said the blocked request is closed, to `task_return.md` (246): transition,
the four removals in order with `after item 3`, the consequences of a trace left in place, failure handled "as
`SKILL.md` step 1 gives for a conflicting trace" (lines 68–72, present). The standing `Never run git fetch
--prune` bullet (lines 66–67) is read on the way. Then steps 2–4 as before; the `plan change` result reaches
the stub, which sends to `route_changes.md` (176). Drops out: `definition_change.md`, `technology_run.md`. Total
2458. The moved text reads without help: no "above", "below" or "step N" of the base is left in the file that
does not name `SKILL.md` or item 3.

Road 6, a critic or refiner told "`SKILL.md` (definition-change route and what it blocks)". Read: the heading
`## 5. Route plan and definition changes` (unchanged, so the order still lands); the stub; `route_changes.md`
(its bullet 2 holds the rule that changing the definition needs a gate) and `definition_change.md` (edit,
critique and gate, recheck, "Keep readiness writes blocked"). What it blocks stands in three places: step 4's
first bullet ("No task becomes ready during step 5's definition gate or pending plan recheck", unchanged),
step 0's "before permitting any readiness writes" and `definition_change.md` bullet 3. The reader loses a
direct hop: two files after the heading instead of one section (the report says so). A critic that opened the
whole file reads 2036 + 176 + 270 against 2580. Nothing the order names is unreachable.

Each row of the assessment table against the place: all 55 rows checked. The 40 quoted fragments of the base
are literal (checked by a script: the quote normalised for whitespace and list markers is a substring of the
base file, and, for rows with a range, of the lines of that range). The five pointer proposals (rows 10, 19,
28, 34, 51) and the four opening lines (rows 52–55) equal the text at the head. Rows 14, 17, 27, 31, 44–49
(the moved ones) stand in the file the row names, in the order the row gives (`task_return.md` first
paragraph and list, then last paragraph; `technology_run.md` two paragraphs; `route_changes.md` two bullets;
`definition_change.md` three bullets). Rewords 15, 18, 32, 33, 46, 50 stand as the table words them. Rows
keep/stay (all others) stand at the same text in `SKILL.md`. Row 22 (closure bullet) stays in `SKILL.md` as
the row says (see *Declined to judge*). No row disagrees with the head.

## The edit of WAY-256

- Binding sentences: three. Sentence 1 is rewritten to "only one variant ... or only one step that some uses of
  the skill pass by"; sentence 2 adds "every step until records of sessions a person can open, those of Claude
  Code and Codex, show that part of the uses since the step stood in the skill pass it by — also where no
  record exists"; sentence 3 is unchanged (line breaks only). WAY-05 (one to three) holds.
- The sentences that contradicted row 1 are gone: "the measure is the instructions in play, not the words" now
  reads "over the uses of the skill"; "with each step's guidance in a file beside it" now reads "the guidance
  of each variant and of each step some uses pass by". The *Rejected* sentence "every fragment one step or
  variant needs moved out, one instruction included" is kept and still true (it is about one-instruction
  fragments). I agree with the author that it does not contradict row 1.
- *Rationale* takes the reason from the source (a step every use comes to is in play wherever it stands; a file
  adds a pointer and a sentence and spares nothing), the no-record reasoning of question 11 and the two weak
  points named in the questions. *Rejected* holds the ways not chosen from questions 3 and 11: a file for every
  step; an exception named for one skill; no change to the decision; the old rule for a skill with no records;
  a threshold of recorded uses. The two layout-only ways (question 3's second item, question 4's second item)
  are left out on purpose; that is right, they concern one skill's layout.
- Nothing else of the decision moved: scope, based-on, relations, origin are unchanged; the *Verification*
  examples gain one *complies* and two *violates* items, all within row 1.
- The estimate: Minor 1.
- WAY-33 search: I searched the repository (`grep -rnE` over `*.md` and `*.py`, outside `.runs`) for the old
  rule's words (`one step or variant`, `only one step`, `every use of the skill comes`, `also where every use`,
  `file beside the skill for every`, `WAY-256`, `beside the skill`, `file beside`, `kind_skill`). The places
  that remain are the edited ones, the *Rejected* sentence on one-instruction fragments (true as it stands),
  `instruction-files/SKILL.md:13` and `:144` (state the criterion at the level of kinds of files and of
  instructions in play; neither contradicts row 1), the layout descriptions of `product-guidelines/*/SKILL.md`
  (descriptions of those skills' files, not the rule), WAY-265 and WAY-258 (read: none restates the old rule).
  Nothing found that still repeats the old rule as binding.

## Limits

`git diff --name-only 57795e4..038a330` lists exactly: `foundations/decisions.md`,
`instruction-files/kind_skill.md`, and the five files of `project-level/lead/skill/`. Lines 1–4 of `SKILL.md`
unchanged; no Python file; `answering.md`, `conversation_template.md`, other skills unchanged. The edit of
`kind_skill.md` is named by the task (`:9`, `:13–14`, `:20`); WAY-125 and WAY-127 rationales are named too.

## Word counts (recomputed; `LC_ALL=C wc -w`; before `git show a3206c1:<path> | wc -w`; after the head files)

| Number in the report | My value |
|---|---|
| `SKILL.md` before 2580; after 2036 | 2580; 2036 |
| `route_changes.md` 176, `definition_change.md` 270, `task_return.md` 246, `technology_run.md` 129; sum 2857, +277 | same; 2857; +277 |
| `:61–77` 240; `:113–118` 67; `:189–219` 399 (with the heading); `:190–219` 392 | 240; 67; 399; 392 |
| `:190–196` 84 + `:197–201` 67 = 151; `:202–219` 241 | 84 + 67 = 151; 241 |
| fetch-prune rule 29 (base lines 73–74) | 29 (30 at the head only because `wc -w` counts the leading "- ") |
| pointers 166 (5 + 53 + 33 + 22 + 53) | 5, 53, 33, 22, 53 = 166 |
| side files before 7253: 1855, 2213, 1419, 775, 204, 496, 291; after 7255 (conversation template 1421) | same, every file |
| roads 1–6 skill text: 2482, 2212, 2036, 2458, 2341, 2482 | same, each sum recomputed |
| roads with side files: before 9833, after 9737, 9467, 9291, 9713, 9596 | same |
| percentages -3.8, -14.3, -21.1, -4.7, -9.3 and -1.0, -3.7, -5.5, -1.2, -2.4 | same to one decimal |
| the task's estimates per road contain the measured numbers | yes, all six |

No number disagrees. The only remark is Minor 5.

## Readers outside the skill

- `project-level/plan/template.md:102` ("only as `lead-project` gives"): lands on `SKILL.md` step 1, which says a
  task whose blocked request the human closed returns to refinement and sends to `task_return.md`; it loses one
  file read (the row move and the order of the removals are one hop away). Lands.
- `project-level/plan/skill/hand_over.md:16`: names the skill only; nothing lost.
- `project-level/plan/skill/delegated_mode.md:3–4`, `project-level/plan/skill/SKILL.md:25`,
  `project-level/skill/delegated_mode.md:4–7`, `project-level/skill/SKILL.md:28`: name the skill as the one that
  dispatches; do not read it; nothing lost.
- Three `orchestrated_mode.md` of the guidelines skills, `product-guidelines/coding/SKILL.md:88`,
  `testing/SKILL.md:79`: name the skill only; nothing lost.
- A critic or refiner told "`SKILL.md` (definition-change route and what it blocks)": road 6 above; loses one hop.
- `installation/install.py:33`, `installation/test_lead_installation.py`, the entry points
  `.claude/skills/the-way-lead-project/SKILL.md` and `.agents/...`: still map to `SKILL.md`; the entry point tells
  the session to read a file the skill names when its step comes (WAY-259, WAY-127); nothing lost.
- No decision or template names a step number of this skill; grep of `foundations/` and `project-level/` finds
  none that the rebuild breaks.

## Declined to judge

- `SKILL.md:76–78` (the closing of a finished project): a variant no use reached; the task fixes the three
  variants that move and the author flags it as a candidate for the follow-up task. Outside the task.
- Whether the judgement of the 55 rows is the best one for each fragment (e.g. the keep of `Never run git fetch
  --prune`): a call within the task; I read it as sound (the harm does not depend on the variant) and did not
  grade it.
- The list of Codex files in the task's *Context* (37) against the author's 31: outside the diff; the author
  reports it.
- The reworked earlier skills of the series (the follow-up task of question 9): outside the task.

## Checks I ran

| Command (from the worktree root) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git status --short` | 0 | head `038a3301...`; clean |
| `git diff --stat 57795e4..038a330`; `git diff --name-only a3206c1 57795e4` | 0 | seven files in scope; the base drift is as the handoff says |
| `git diff -w --word-diff=porcelain e98f46b 038a330 -- foundations/decisions.md` | 0 | no word change (line breaks only) |
| word diff of base `SKILL.md` against the five head files (Python, `-B -I`, scratchpad) | 0 | 22 differences, all accounted for above |
| script: each quoted fragment of the 55 rows against `a3206c1` | 0 | 40 quotes found; proposals match the head |
| `LC_ALL=C wc -w` over the files above (before via `git show a3206c1:<path>`) | 0 | every number agrees |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn (`_zadania\` of `AGENTS.md`, not from this change), 3 info |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK (skipped=5) |
| `python -B gate/run_tests.py project-level` | 0 | OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |

Not run: `python -B gate/run_tests.py installation` (about three minutes; the change touches neither
`installation/` nor an entry point, and the author reports exit 0); the whole gate (the orchestrator's). Records of sessions
(Claude Code in `loop2`, Codex) not re-searched by me: the judgement rests on the author's search, which agrees
with the task's *Context* (steps 0–4 in 8 of 8, step 5 with a plan change in 7, definition change in 4, no
return of a task, no technology run).

## Reach beyond the dispatch

Selective reads of the foundation by search (WAY-150): WAY-05, WAY-33, WAY-256 (whole), WAY-265 (whole), WAY-269
(whole), the *Rationale* passages of WAY-125 and WAY-127, the `lead` lines of `foundations/part_map.md`
(grep) and the invariant on entry points (grep); `instruction-files/kind_skill.md`, `judging.md` lines 1–30,
`SKILL.md` lines 5–20 and 135–160 of `instruction-files`; the entry point
`.claude/skills/the-way-lead-project/SKILL.md`; `project-level/plan/template.md:88–108`. I did not read whole every
decision of the `project-level` part; I read what the change cites or restates.

## Searches not found or unclear

- Unclear: the step-1 pointer ("Each time you reach this step ... read `task_return.md` ... when the human has
  said so") ties the reading to reaching step 1. If the human says a request is closed in the middle of a round
  (after step 1 was passed) and no merge follows, the text does not say to go back to step 1. The base had the
  same rule inside step 1 only, and the criterion prescribes this form, so I count no road as lost; no record
  contains a return, so how an agent reads the pointer is untested.
- Not found: any decision or record that sets what "part of the uses" means as a threshold (one use of eight?);
  row 1 and WAY-256 leave it open, as the task does.
- Not found: a remaining place that states the old rule as binding (WAY-33 search above).
- Not reproduced: the Codex file count of 37 (the author finds 31); I did not repeat the search.
- The Rationale's estimate against WAY-05 is Minor 1; I did not find a decision that settles whether an estimate
  counts as a "measurement the choice rests on".
