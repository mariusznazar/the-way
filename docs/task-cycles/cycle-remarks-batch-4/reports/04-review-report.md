FAIL 0d59ce9e4b4e5cd76029c405b878f94cb33df56f

# Review of the whole change, cycle `cycle-remarks-batch-4`

Range `e3825a82386a61930a86f8517fc0c5f422fc2833..0d59ce9e4b4e5cd76029c405b878f94cb33df56f`
(`git rev-parse HEAD` = the head given). Commits `3effb9b`, `77ecd4a`, `0d59ce9`. Route: one author, no
slices, no spec, no earlier review. Diff and log computed with `git diff e3825a8..HEAD` and
`git log e3825a8..HEAD`.

Verdict in short: all seven To do items and all seven answered questions are met, and the quoted
sentences are copied word for word (rewrapped only). One blocking finding: the request template
(item 15) and the three foundation texts it rests on (WAY-71, `rules.md`, WAY-287) say different things
about which `TODO`s reach the human. Six Minor findings (M-6 is new in the amendment below).

**Amendment (second pass).** The first version of this report read 3 decisions whole and screened none
by title. On the coordinator's request I made the screening: the 173 decisions whose *Scope* names
`decisions`, `task-cycle`, `elements-common` or `invariants` (a script over `foundations/decisions.md`,
including *Scope* lines that continue on the next line, found 173 of 284) had their titles run through,
and 64 were read whole. The invariants file and the glossary were read whole too. Result: the
Important finding I-1 and the grades of M-1 to M-5 stand (the readings of WAY-263, WAY-25, WAY-21 and
WAY-30 support them); one Minor finding is added (M-6, from WAY-05). Nothing else changed in the
findings. The sections *Unread material*, *Reaches beyond the dispatch* and *Searches not found or
unclear* are rewritten below.

## Findings

### Important

**I-1. The scope of "a change that leaves one there" is stated wide in three places and narrow in the
request template that carries it out (WAY-263).**
Places:
- `task-cycle/skill/request_template.md:249-253` (item 15) gives an item only for a `TODO` "that the
  change writes, or keeps in an entry it edits", and says "A `TODO` in an entry the change does not
  touch is not the change's and gives no item".
- `foundations/decisions.md:1681-1682` (WAY-71): "a change that leaves one there puts it before the
  human"; `elements/common/rules.md:20-22`: the same; `foundations/decisions.md:9077-9078` (WAY-287
  binding sentence): "each descriptive `TODO` in an invariant's *Rests on* that the change leaves on
  the main branch"; `foundations/decisions.md:9114-9116` (WAY-287 rationale): "A descriptive `TODO`
  left in an invariant's *Rests on* ... stands here".
- The task's To do 7 reads "każde opisowe `TODO` w *Rests on*, które zmiana zostawia na gałęzi
  głównej".

What is wrong: the three entries the change writes say that every descriptive `TODO` the merge leaves
on the main branch is put before the human; the template, which is the only place that tells the cycle
what to do, narrows that to the entries the change edits. A reader of WAY-287 (the reviewer of a later
request, or the cycle comparing a request with the decision) will count an old `TODO` in an untouched
entry as missing from the request; a reader of the template will not put it there. WAY-263 grades a
file that "restates [an entry] differently, including more broadly or without a qualification"
Important. The author named this as the weakest point of the work and asked for a ruling.

My answer to the author's question: the narrow reading is workable, and the reason the author gives
(every request would repeat the same old gap) is sound. But then the decisions and `rules.md` have
to say the narrow thing, because they are what a later agent is compared with. The task's sentence is
ambiguous ("zostawia" can mean written or kept in an edited entry, or merely not removed), and the
task's own Out of scope line about loop2's bare `TODO` (it is reported by the script after the pin and
described by "that update in loop2") fits the narrow reading, since that update edits the entry.

Evidence: the five quotations above; nothing in WAY-71, `rules.md` or WAY-287 carries the qualification
"in an entry the change edits".

Fix: either add the qualification to the WAY-71 binding sentence, `rules.md:20-22` and the WAY-287
binding sentence and rationale (the task's sentence of To do 6 is then changed, which is a decision of
the human, not of the cycle), or widen item 15 to every `TODO` on the tree after the change. The first
changes the wording the task gives for WAY-71 and `rules.md`; the second is the task's literal wording
and costs one item per request for as long as an old gap stands. Scope: within the task. Slice: none
(one author, no plan).

### Minor

**M-1. `task-cycle/skill/SKILL.md:48`, the pin-move run, still says "Run the product's gate on that
commit as step 10 gives" while step 10 now says to start the gate after the return step.** The author
changed the same phrase in sub-step 9.4 (`SKILL.md:326`) and in `blocked_finding.md:8` ("at once"), and
left this one, calling it "a run on a commit, not on the finished change". The result of this run is
handed to steps 4, 8 and 9 (same paragraph), so it must not wait for step 11; a literal reader of
"as step 10 gives" is told to wait. Add "at once" here too (WAY-33). Within the task (it is a
consequence of To do 2).

**M-2. `task-cycle/skill/SKILL.md:326` is a 131-character line in a file wrapped at 100, and the added
clause makes the sentence a chain of commas:** "change as step 10 gives, at once, since no return step
runs, run `task-cycle/cycle_stages.py`, prepare ...". The reader can take "since no return step runs,
run" as one clause. Rewrap and set the clause off (a dash or parentheses). Also `SKILL.md:362` ends a
line after "The authors' focused checks are not", a short line left by inserting the task's two
sentences (cosmetic). Within the task.

**M-3. A bare `TODO` inside a list in *Rests on* still passes
(`elements/common/foundation_check.py:102-103`, `:397-409`).** `TODO_VALUE` matches only a value that
begins with `TODO` followed by a blank, a backtick or the end. I ran `foundation_check.py` on a scratch
copy of the foundation with these values in an invariant's *Rests on* (exit 1 for the copy's other
errors, none about this field): `git-state · TODO` gives only "names no fact" for `git-state`, no
bare-`TODO` error; `TODO,` gives no error at all; `TODO — x · TODO` gives no error; `TODO—the fact` and
`TODO: the fact` give "is no identifier of a fact" (an error, but not the hint the task asks for).
The task's answer to question 6 says the bare `TODO` in *Rests on* "jest błędem"; To do 5 words it as
a value that begins with `TODO`, which the check meets. So this is polish: either say in the
docstring that only a value that begins with `TODO` is read, or report a bare `TODO` item anywhere in
the field. Also note the check accepts a description without the dash (`TODO the store`) though the
rule (WAY-71, `rules.md:20-21`) states the form with it; the author reported this (*Choices* 5). Within
the task.

**M-4. WAY-71's own *Verification* contradicts its binding sentence
(`foundations/decisions.md:1690-1692`):** "complies: ... a decision whose source is silent on what it
rests on reads `Based on: TODO — <what is missing>`", while the binding sentence (rewritten by this
change at `:1680-1682`) lets the main branch hold `TODO` only in an invariant's *Rests on*. The
contradiction was already at the base commit (the author reported it); the change rewrites the entry
and does not repair it, and `DECISION_WORDS` in `foundation_check.py` still lets *Based on* read
`TODO`. Partly beyond the task: the example is not in the task's list, and whether *Based on* may read
`TODO` is a decision for the human. Within the entry the change rewrites, though, so it is listed.

**M-5. WAY-71 now governs what a request shows the human, but its *Scope* does not name
`task-cycle` or `agent-instructions` (`foundations/decisions.md:1685`), and WAY-287's *Verification*
(`:9082-9100`) has no example of the new item.** A cycle that selects decisions by *Scope* "task-cycle"
(the method of `way_of_working.md`, "Reading the foundation", step 2) for a change to the request
template will not find WAY-71. Adding the part, or a *Relations* link from WAY-287 to WAY-71, is a
change to approved decisions; it is not in the task. Mostly outside the task; the *Verification*
example of WAY-287 is within it.

**M-6 (new in the amendment). WAY-160 states in its rationale prose a rule that binds later work, which
WAY-05 says stands in a binding sentence or a field (`foundations/decisions.md:4582-4583`).** The added
rationale says: "The price is that a failure of the gate comes after the return step, so the fix of
that failure sends the return step back to its range." The rule itself ("Where the gate then fails and
its fix changes code, the return step compares that fix's range too") lives in
`task-cycle/skill/SKILL.md:361-362` (the task's To do 2 gives it there), but neither WAY-160's
binding sentence nor its *Verification* (`:4565-4568`) carries it, so a reviewer comparing a cycle with
WAY-160 has nothing to check it against, and a later edit of step 10 could drop it without
contradicting an entry (WAY-05: "what a decision forces on later work stands in a binding sentence or
a field, never in prose"). The rationale sentence is the author's, not the task's (the task changes
only the *complies* example and *Rejected*). Fix: say the rule in the *complies* line (for example,
"and where the gate fails and its fix changes code, compares that fix's range in the return step too")
or leave the sentence as a plain statement of the price without "sends ... back". Within the task.

### Out of scope

none beyond the part of M-4 and M-5 named there.

## Task, item by item

1. `elements/decisions/template.md:210-218` — the sentence is replaced word for word. Met.
2. `task-cycle/skill/SKILL.md:359-362` — inserted after step 10's first sentence, word for word. Met.
   Steps 10 and 11 keep their numbers (Out of scope kept).
3. WAY-160 *Verification* — "complies" replaced word for word (`foundations/decisions.md:4565-4568`).
   *Rejected* has the added clause as the task quotes it. The rationale addition ("the return step ...
   needs no result of the gate", "the price is ...") is the cycle's and says what step 10 now does.
   Met.
4. `task-cycle/remarks_check.py:16-18` (docstring, word for word), `:63-64` and `:126-130`
   (`SECTION_NUMBER`, applied once after the emphasis marks are removed); `test_remarks_check.py` has the
   case `## 12. Searches not found or unclear` and more. Met. A mutation of the number handling fails
   the tests (see Checks).
5. `foundation_check.py:397-409` (`check_rests_on`), docstring `:39-43`; tests
   `test_foundation_check.py:599-634`: the descriptive form with a comma, over two lines, the bare
   forms with the exact message and line, `TODOs`, `none`. Met, with M-3.
6. WAY-71 and `elements/common/rules.md:20-22` carry the task's sentence word for word. Rationale and
   *Rejected* as the task's *Decisions in play* quote. Met, with I-1 and M-4.
7. `request_template.md:249-253`, item 15 in *For you to decide*, matching the task's "wybór cyklu".
   Met with the narrowing of I-1.

Questions to settle: 1 and 2 (no task document in *Origin* wherever the tasks are kept) — the template
sentence is the answer. 3 (the gate once after the return step and its review, a second time only
after a merge that changed the tree) — SKILL.md step 10 and WAY-160. 4 (the script lists no reports
without a section) — nothing added; correct. 5 and 6 — `check_rests_on`. 7 — item 15. 8 (no hold on
WAY-215) — the change proceeded; correct.

Out of scope of the task: the change touches neither loop2's old *Origin* entries, nor loop2's bare
`TODO`, nor the numbering of steps 10 and 11. Kept.

## Files the handoff named as outside the task's list

- `task-cycle/skill/blocked_finding.md:8-10` ("at once, since no return step runs on this code") —
  justified: without it, the blocked-cycle run, which WAY-163 says goes with no return step, would be
  told by step 10 to wait for one. No finding. Same for `SKILL.md:326` (sub-step 9.4) but see M-1, M-2.
- WAY-287 (`foundations/decisions.md:9077-9078`, `:9114-9116`) — justified in kind: WAY-287 says its
  `none` means that nothing else in the request waits for the human's yes, so item 15 without it
  would contradict it (WAY-33, WAY-37). The edit adds a kind of item for the human beyond what the
  task's *Decisions in play* lists, so it goes to the human as the cycle's entry at the merge; the
  wording of the edit is the subject of I-1. After reading WAY-30, WAY-14, WAY-114 and WAY-227 whole:
  the edit is a proposal on the task branch that binds only when Mariusz merges (WAY-14), which is what
  WAY-30 allows for a contradiction found during implementation, provided the request shows it to him
  (WAY-114: the cycle's entry, item 6 of the request's section for the human's decisions). No finding;
  the orchestrator should check that the request does so.
- `elements/invariants/template.md:122-125` — justified: the old sentence "a link the author knows is
  missing reads `TODO` rather than `none`" would license the bare word; the new one gives the form for
  *Rests on* and says the script reports the bare word. No finding. (The same bullet still lets
  *Derives from* read `TODO`, which line 45 of the same template gives as `TODO — <the decision, and
  where it is expected>`; that is unchanged and not this change's.)

## Tests

The new tests fail for the right reason. I ran mutations of the head in scratch copies (see Checks):
removing the number handling, loosening the blank after the number, and widening the number pattern
fail `test_remarks_check`; removing the bare-`TODO` branch, reading every value as a list, and
dropping the word boundary of `TODO_VALUE` fail `test_foundation_check`. No test asserts a value it
computes itself. No invariant test is changed (`git diff --stat` has no `foundations/invariants.md`).

## Own-work check of the author

The requirement named as most likely unmet (a quoted sentence copied exactly) is the right one for
items 1, 2, 3, 4 and 6, and I checked it again against the diff: all six agree with the task apart
from line wrapping. The check would not catch I-1, which is a disagreement between the author's text
and the foundation, not between the text and the task; the author named that gap under "Weakest point".

## Declined to judge

- Whether `Based on` may read `TODO` on the main branch (the example in WAY-71 *Verification*, the
  `DECISION_WORDS` table of `foundation_check.py`): a decision for the human, beyond the task (M-4).
- Whether `Derives from: TODO — ...` of the invariants template (line 45) agrees with WAY-71's "only in
  *Rests on*": already at the base, beyond the task.
- Whether the three commits are well divided (the author gave the reason: one file, three entries):
  not a matter of the code.
- Whether the edits to WAY-160 and WAY-71 were made through `record-decision` as the task asks: the
  report cannot show it; I judged the text, not the route.

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `0d59ce9e4b4e5cd76029c405b878f94cb33df56f` |
| `git status --short` (reviewed worktree) | 0 | clean |
| `python -B gate/run_tests.py task-cycle` (reviewed worktree) | 0 | 238 tests, OK |
| `python -B gate/run_tests.py elements/common` (reviewed worktree) | 0 | 122 tests, OK |
| `python -B -I foundation_check.py . --skip-test-citations` on a scratch copy of `foundations/` (own git repo, other files missing, so 27 unrelated errors) with six values of an invariant's *Rests on* | 1 (the copy's other errors) | `TODO` gives the new error at `foundations/invariants.md:41`; `TODO — x · TODO` and `TODO,` give none; `git-state · TODO`, `TODO—the fact` and `TODO: the fact` give "names no fact" / "is no identifier of a fact" (M-3) |
| `python -B -I mut.py` (scratchpad `a scratch file in the agent session's scratch directory`): six mutations of copies of `task-cycle/` and `elements/common/`, each run with `python -B -m unittest test_remarks_check` or `test_foundation_check` | 1 for each of the six | every mutation fails the tests (2, 1, 22, 5, 10 and 2 failures) |
| `python -B -I scope.py <worktree> scope.txt` (scratchpad `...\rv\scope.py`): lists the decisions whose *Scope* names `decisions`, `task-cycle`, `elements-common` or `invariants` | 0 | 173 of 284 (amendment) |
| Manual (amendment): `git diff e3825a8..HEAD` filtered to added lines, searched for absolute paths, `@` imports and links | n/a | none found (invariants `tracked-file-private-paths`, `outbound-link-reach`, `instruction-file-imports` not departed from) |
| Manual: the six quoted sentences of the task compared with the diff by reading | n/a | agree apart from wrapping |
| Manual: grep of the repository for `step 10`, `after the return step`, `Origin`, `TODO`, `Searches not found or unclear` to find places that disagree with the changed texts | n/a | found `SKILL.md:48` (M-1), WAY-71 *Verification* (M-4); the rest agree |

Not run: the full gate (the orchestrator's), `agent-instructions/skill_entry_points.py` (no skill name or
description changed: the diff touches no frontmatter), `installation` and `instruction-files`
directories (the author reports them passing; I did not repeat them).

## Reaches beyond the dispatch

- `agent-instructions/README.md` (named by the repository's `AGENTS.md`, and by the handoff): read
  to learn the integration route and the gate sentence; no finding.
- `foundations/decisions.md` WAY-160, WAY-71, WAY-287: each read whole (they are the entries the
  change writes). The decisions of the screening are listed under **Unread material**.
- A script over `foundations/decisions.md` that lists the entries whose *Scope* names `decisions`,
  `task-cycle`, `elements-common` or `invariants` with their titles and line ranges, to run the
  screening (scratchpad `a scratch file in the agent session's scratch directory`,
  its output `...\rv\scope.txt`).
- `task-cycle/record_template.md:120-160`, `task-cycle/skill/correction.md:30-45`,
  `task-cycle/skill/SKILL.md:44-52, 160-170, 340-500`, `elements/invariants/template.md:40-56, 118-130`,
  `elements/invariants/skill/SKILL.md:55-62`, `elements/environment-facts/skill/decide_entry.md:1-8`:
  read to find places that say something about the gate order, `TODO` or the heading form (WAY-33
  search by hand).
- `the user's global rule on writing scripts` (the global rule before writing a script), for the
  mutation script.

## Unread material

Counts for the selection of section 1 of the method (amended): the decisions whose *Scope* names
`decisions`, `task-cycle`, `elements-common` or `invariants` number **173** of the log's 284
(*Scope* lines that continue on the next line included). **64 read whole, 109 by title only.** I ran
through all 173 titles (list from the script named under *Reaches*), opened every one whose title
points to a bearing on the change, and read whole those that concern its topic.

Read whole (64):
- the entries the change writes: WAY-160, WAY-71, WAY-287;
- the gate order and the cycle's checks: WAY-159, WAY-163, WAY-164, WAY-148, WAY-150, WAY-306;
- `TODO`, *Rests on* and the form of entries: WAY-17, WAY-58, WAY-60, WAY-61, WAY-64, WAY-73, WAY-82,
  WAY-05, WAY-07, WAY-12, WAY-21, WAY-35, WAY-36;
- *Origin* and what an entry may point to: WAY-27, WAY-29, WAY-308;
- the author's search and the entries that wait: WAY-33, WAY-37, WAY-02;
- changing a decision, who accepts it, collisions: WAY-01, WAY-10, WAY-14, WAY-22, WAY-24, WAY-25,
  WAY-30, WAY-114, WAY-227, WAY-293;
- the return step and projected or settled entries: WAY-11, WAY-28, WAY-34, WAY-117, WAY-126, WAY-134;
- findings and grading: WAY-161, WAY-162, WAY-263, WAY-297;
- the request and its checks: WAY-286, WAY-288, WAY-289, WAY-290, WAY-291, WAY-292;
- the remarks check and unread material: WAY-260, WAY-294, WAY-295, WAY-296, WAY-298, WAY-300, WAY-307,
  WAY-325, WAY-326;
- WAY-299 (read for the part-map and invariants files; no bearing).

Run through by title only (109): every other entry of the 173. The ones I judged to have no bearing
include the decisions on parts that the change does not touch (the part map, the glossary, project
level, technology choices, guidelines and styleguide, the environment facts' entries), on the log's
numbering and withdrawals (WAY-18, WAY-19, WAY-32), on the weight and methods of the cycle (WAY-13,
WAY-125, WAY-135, WAY-136, WAY-229), on private paths (WAY-309, WAY-323, WAY-324), on screenshots
(WAY-316, WAY-317, WAY-318), on the flaky-check reports (WAY-261, WAY-262), and on who reads the full diff (WAY-158). Decisions with a title that could point to a bearing
and that I did not open: WAY-13 (the weight of a task's process), WAY-124 (when a task is ready),
WAY-125 (the autonomous cycle's methods) and WAY-309 (how the cycle finds private paths and notes);
I judged none of them to bear on a change to a template sentence, a step order, a heading pattern and
a field check, and the price of that judgment is the one WAY-150 names: a decision with a title that
looks unrelated can pass unopened.

The decisions the task lists and the coordinator named, WAY-17, WAY-27, WAY-29, WAY-33, WAY-37, WAY-159,
WAY-163, WAY-263, WAY-290, WAY-294, WAY-295, WAY-296, WAY-298 and WAY-300, are all in the list read
whole. None of them led to a finding except as follows: WAY-263, WAY-25, WAY-30 and WAY-114 ground I-1
and the note on WAY-287; WAY-05 gave M-6; WAY-21 supports M-5; WAY-27 and WAY-33/37 support the
template sentence and the other changes. WAY-295, WAY-296, WAY-298 and WAY-300 are not touched by the
change.

Foundation other than decisions: `foundations/invariants.md` read whole (356 lines); invariants that
bear on the change: `foundation-file-kinds`, `return-step-record`, `outbound-link-reach`,
`tracked-file-private-paths` (no absolute path or note link in the added lines: grep over the diff found
none), `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`,
`skill-entry-points` (no frontmatter changed) and `record-copy-image-check`; none is departed from.
Part-map entries `decisions`, `invariants`, `elements-common`, `task-cycle`: read whole. Glossary
(`foundations/glossary.md`): read whole; no term is used in a meaning other than its entry gives.
Guidelines: the-way has no `guidelines/` directory; none read. `product-guidelines/template.md`: not
read (the change writes no product guidelines). `project-level/technology/reserved_choices.md`: not
read; the change settles no language, framework, library, store, login or place to run.

Not read whole: the 109 decisions run through by title above (their titles only); WAY-80 and the
decisions whose *Scope* names none of the four parts (outside the selection); the bodies of
`elements/decisions/examples.md` and `elements/common/projected_mode.md`.

## Searches not found or unclear

- Guidelines of the-way for the touched parts: none exist (no `guidelines/` directory), as the handoff
  says.
- Any test, invariant or script that checks the *wording* of `request_template.md` against WAY-287 or
  against the list of items in *For you to decide*: not found; so nothing guards the disagreement of
  I-1.
- Whether the task means by "które zmiana zostawia na gałęzi głównej" every `TODO` on the tree after
  the merge or only those in entries the change edits: unclear in the task; the author took the
  narrow reading and said so (*Choices* 1). See I-1.
- Whether the rule in WAY-71 about the form `TODO — <the fact, with its source>` is meant to bind the
  script (the check accepts `TODO the store` with no dash): unclear; the task words the script's
  rule as "a value that begins with `TODO`" (M-3).
- The route by which the edits to WAY-160 and WAY-71 were made (`record-decision`): not shown in the
  author's report; I could not check it.
- (Amendment) A decision of the log that says where a rule that binds later work stands when the rule
  is also a step of a skill (WAY-160's fix-of-a-failed-gate rule is in `SKILL.md` and in rationale
  prose only): WAY-05 says binding sentence or field, WAY-36 and WAY-35 say what stays out of the log
  or a skill; none says whether a step order of the skill needs an entry of its own. Unclear; I took
  WAY-05 as the rule (M-6).
- (Amendment) An entry of the log that says whether the cycle may edit a decision the task does not
  list when a new item contradicts it: WAY-30 (propose on the task branch, the human accepts by
  merging, WAY-14) is the nearest; it does not say whether the request must name the edit apart from
  the cycle's other entries. Unclear; I took item 6 of the request's section for the human's decisions
  (WAY-114) as the place.
