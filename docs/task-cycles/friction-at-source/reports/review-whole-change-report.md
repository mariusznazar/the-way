PASS e51d835

# Review of the whole change `friction-at-source`, range `6814c6f..e51d835`

Head confirmed: `git rev-parse HEAD` printed `e51d8350cf70dc81a0523b2a92b03b518c18f61c`. Three commits (`ffeadc7`, `32f9904`, `e51d835`), 10 files,
184 insertions and 23 deletions. The reviewed worktree was left clean (`git status --short` empty after all my runs).

Counts: 0 blocking, 7 Minor (all within the task), 0 out of scope.

## Against the task

*To do*:

1. Steps for the human in the item for an unrun check. Met: WAY-327 gains the fifth part in its binding sentence, its Verification pair, its
   Rationale and its Rejected. `task-cycle/skill/request_template.md` gains it in step 2 of "Write, check, publish", in kind 4, in "What an item
   carries" and in a second example. The three answers are unchanged, and the skeleton (WAY-286) and the form check (WAY-290) are not touched.
2. Place to change in a file pointed at by a heading or a quotation, the line only a hint, the *Source* under a question left as it is. Met in
   `project-level/task/template.md` (last paragraph), `project-level/task/skill/draft.md` and `project-level/task/skill/final_review.md`, with
   WAY-353 as the entry.
3. The review of the foundation lists decisions that describe a transitional state, asks the human at each, and proposes the task where none
   exists. Met in `foundation-review/weak_points.md`, `proposals.md`, `with_the_human.md` and `SKILL.md` steps 2 and 6, with WAY-354 as the entry.

*Settlements to record*:

- Row 1 -> WAY-353. Meaning kept. *Rejected* matches the *Not chosen* of question 2: the script that catches about 15 of 80 rows, and no rule.
- Row 2 -> WAY-354. Meaning kept. *Rejected* matches the three ways of question 3: the field, the question at refinement, no rule. The entry has no
  field for the task.
- Row 3 -> WAY-327, edited in place. *Rejected* gained both ways of question 4's *Not chosen*, each with its cost.
- Row 4 -> the glossary term `transitional state`, the row's meaning word for word in English.

*Out of scope*: question 1 (the script that writes the proof) and question 5 (counting by cause) are not touched. The skeleton, the form script and
WAY-286, WAY-289 and WAY-290 are not edited. Nothing was added that nobody asked for, except the clause in `final_review.md` and the second example
in the request template. Both are in the task's reach: the first is a gate check for row 1, the second a worked example for row 3.

*Decisions in play*: WAY-327, 286, 287, 289, 290, 24, 302, 305, 36, 37, 01 were read whole and none is contradicted. WAY-354 sits beside WAY-24
(the entry carries no field) and WAY-302 (the proposal becomes a task on the human's yes). WAY-36 is respected: a rule that ends with its own change
is excluded in `weak_points.md`. WAY-01 is respected: no field, no roadmap.

## Findings

### Critical

none

### Important

none

### Minor (all within the task; none blocks)

1. **`foundation-review/SKILL.md:60-61` and `:81` do not mention the new kind of item.** Step 4 reads "the proposals about the foundation, the groups of
   remarks, and the data file". Step 7 reads "The review is done when the human has decided on every proposal and every group". Steps 2 and 6 were
   updated. WAY-354 requires that the human is asked at each such decision, and `with_the_human.md` step 2 does that. But the condition for marking the
   review done, which decides whether a tag is placed, does not name these decisions. Where the human names an existing task, `proposals.md` says "nothing
   is proposed", so the item is not a "proposal" in step 7's words, and the review could in the letter be marked done without asking. Evidence: the two
   quoted lines and `proposals.md:20-29`. Why it is Minor and not Important under WAY-263: step 6 does require asking at each, so the files do not do
   what the entry forbids, they only leave the end condition loose.
2. **WAY-354's *Rationale* (`foundations/decisions.md:11763-11765`) carries a rule in prose: "the review does not search".** The binding sentence
   says only that the review asks the human. WAY-05 (and `elements/decisions/template.md`) says that what a decision forces on later work stands in a
   binding sentence or a field, never in prose. `foundation-review/weak_points.md` (end of the new section) repeats it as an instruction: "The review
   does not look for the task". Fix: say it in the binding sentence, or drop it from the files.
3. **"as before" in the binding sentence of WAY-327** (`foundations/decisions.md:10839`), in its Verification ("the same three answers as before") and
   in `task-cycle/skill/request_template.md:337`. An entry describes the decision as it stands now, never the change (WAY-07, WAY-19). "As before"
   points at the earlier wording. A reader of the entry alone cannot tell what "before" was. Fix: state the remark as a standing rule, "the human who
   checks by hand writes a remark after the check". (After the repair reading below: WAY-297's binding sentence says "graded as before" and WAY-07
   says "as before it", so the phrase has precedent in the log. The finding stays Minor, graded on the point that the entry is read alone, not on
   WAY-07 or WAY-19 as a breach.)
4. **WAY-353's *Verification* names as a violation something its binding sentence does not forbid** (`foundations/decisions.md:11719-11721`: "a script
   is run before the cycle starts to check that every file, line and entry a task document names still exists"). The binding sentence says only how a
   place is pointed at and what the *Source* keeps. The script is a rejected way, and its place is *Rejected*. As a "violates" example it makes a later
   comparing agent fail a change that adds such a check although no sentence forbids it. Fix: drop that clause, or put the prohibition in the sentence if
   it is meant to bind.
5. **Concern (a), judged: the steps rule meets WAY-286 in its letter, with a gap** (`task-cycle/skill/request_template.md:332-338`). The rule says: no file
   name and no identifier in a step; where the way to the place is a file, the step describes the place; the item ends with its pointer to the lower
   part. That keeps WAY-286's top-part rule. But a check by hand often needs a command or a file the human must name. The rule does not say whether a
   step may carry a command, and the author reported this as unresolved (author report, choice 3). The example (`:378-391`) also ends the item with the
   steps and not with a pointer, so the reader of the rule cannot see where the pointer goes. In the same example, "If you want to look first, and write
   a remark with what you saw:" reads as an optional fourth way, while WAY-327's *violates* names "adds a fourth answer for them". The sentence is a
   invitation and not an answer, but it is close. Fix by wording: put the pointer after the steps in the example, state the command case in one
   sentence, and rephrase the invitation.
6. **Concern (b), judged: WAY-354's *Rationale* cites WAY-329 for more than WAY-329 says** (`foundations/decisions.md:11764-11765`: "an identifier of a
   task that an entry could name exists only for a task of a project plan (WAY-329)"). WAY-329 derives the identifier of a plan task's line and says
   nothing about tasks outside a plan. The sentence is an inference. It is faithful to the task document, whose *Context* makes the same attribution,
   and the author named it a reading. Fix: write it as the reason without the citation, or cite WAY-329 as "only plan tasks have an identifier derived
   by a decision".
7. **Form of two files.** `project-level/task/skill/final_review.md:10-13` re-wrapped lines unevenly: one line is 123 characters in a file that wraps near
   100. `project-level/task/skill/draft.md` repeats the rule of the template in its own words, so the rule now stands in three files (concern (c)).
   `final_review.md` carries it as a gate check, and `draft.md` and `template.md` as the writing rule. Judged: acceptable, because the task asks for the
   template and the skill, and each of the three says it once. The risk is drift in a later edit. No fix needed beyond the wrap.

Concerns (d) and (e): (d) the glossary entry `transitional state` is justified. Its meaning is narrower than the field's, and a reader taking "temporary
state" would read WAY-354 as covering ordinary "until" rules and states that end with their own change. `git grep -i transitional` shows no other use
of the word, so there is no second meaning to rename (WAY-99). The form matches the template (one sentence, `Not: none`). (e) Three commits: I checked each
one on a copy outside the worktree (below), and `foundation_check.py` gives `0 errors` on all three. The author's remark that the check passes only on the
last commit is wrong but harmless.

## Declined to judge

- The form script's silence about the fifth part: by design (WAY-290: the script judges no content), and the task leaves it unchanged. Out of scope.
- The task document's own pointers by line number (its *Context*): the rule applies from this change onward, and the document is frozen. Out of scope.
- Whether WAY-353's *Rationale* figures from the register of problems belong in *Based on*: the register lies in private notes (WAY-320), and WAY-05 lets
  a measurement with its conditions stand in prose. Set aside as not a finding.
- The 40 of 80 stale references that stood in orders to agents and plans, which WAY-353 does not reach: the task limited the rule to the task document.
  Out of scope.

## Checks run

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (head) | 0, `0 errors` |
| `python -B gate/run_tests.py task-cycle` | 0, 365 tests OK |
| `python -B gate/run_tests.py project-level > <scratchpad>\pl_run.txt 2>&1; echo "exit $?"` (run again, no pipe) | 0, 275 tests OK. (The first run went through `tail` and its exit code was lost; this one replaces it.) |
| `python -B agent-instructions/skill_entry_points.py` (no argument; reads, writes nothing, `git status --short` empty after) | 0, `entry points are current` |
| `python -B <scratchpad>\ownwork.py .` (the author's own-work check, read first; it only imports the test module and writes nothing) | 0, `problems: []` |
| `python -B elements/common/foundation_check.py` on a `git archive` copy of `ffeadc7` and of `32f9904` in the scratchpad, each in a fresh `git init` | 0, `0 errors`, for both |

Not run: the whole gate (the orchestrator runs it), `foundation-review/` has no tests, `agent-instructions` and the other parts' tests (no file of
theirs changed). Whether `foundation-review/SKILL.md`'s front matter changed: it did not (`git diff` of it is empty), so the entry points stay current.
The checks tell this change apart from a broken one on the points they cover. The new example item passes the form check, and the skeleton test
passes. They do not judge the content of the fifth part or the review's new step.

## Reach beyond the dispatch

- `foundations/decisions.md` WAY-05, 95, 124, 134, 263, 300, 304, 329, 320, read whole: to judge the entries against the template, the glossary rule, the
  readiness rule and the grading rule. Reached by their Scope or by an identifier in the change.
- `foundations/invariants.md`, the 27 invariants whose *Part* names `every`, `task-cycle`, `project-level`, `decisions` or `glossary`, read whole in the
  repair of this report (the selection of the coordinator's message; no `foundation-review` or `glossary`-only invariant exists).
- `elements/decisions/template.md` and `elements/glossary/template.md`: read whole, for the form of entries.
- `elements/common/way_of_working.md` lines 1-150: "Reading the foundation" and "How a skill asks".
- `task-cycle/review/whole_change.md`: read whole.
- `git grep -i "four parts|WAY-327|these four"` and `git grep -i transitional`: to find other files that restate the entries.
- `foundations/part_map.md`: only the headings and the `foundation-review` part were read (assignment of the touched files).

## Repair reading (after the coordinator's message): ten decisions and the invariants

I read whole WAY-07, 19, 33, 35, 99, 297, 114, 150, 303, 161, and the 27 invariants of the selection (`foundation-file-kinds`,
`foundation-change-merge-route`, `repository-file-location`, `element-directory-contents`, `return-step-record`, `derived-file-content`,
`ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`, `skill-rule-source`, `script-language`, `script-imports`,
`script-subprocesses`, `map-reference-target`, `test-method-citation`, `project-definition-form`, `project-readiness-gate`,
`project-technology-record`, `project-plan-form`, `project-plan-check`, `skill-entry-points`, `instruction-file-imports`,
`project-plan-state-evidence`, `project-plan-state-subprocesses`, `cross-part-imports`, `record-copy-image-check`, `record-copy-image-files`).

Result: no finding is changed in grade, and no new finding appears.

- Finding 3 loses part of its basis: WAY-297's binding sentence says "graded as before" and WAY-07 says "as before it", so "as before" in a binding
  sentence has precedent. It stays Minor on the reading-alone point only (noted under the finding).
- WAY-33: the author's search is the one the author report gives (WAY-33 section); the change brings no entry that waits for something it does not
  fix. No finding.
- WAY-35 and `skill-rule-source` bind the skills of the five elements. `foundation-review` and `project-level/task/skill` are no element skill, so
  the rule of WAY-353 standing in `template.md`, `draft.md` and `final_review.md` and the review's rules standing in its own files break neither.
  The three-places point stays a drift risk in finding 7 and no more.
- WAY-99 and WAY-297: the glossary entry `transitional state` is the only meaning of the word in the tracked English files; a finding about a missing
  entry or qualifier would be Minor by WAY-297 anyway, and I raise none. WAY-263's reading of the entries the change writes is the one I used.
- WAY-114: the entries come from accepted rows, so the human accepted their meaning with the task document; the review read each against its row,
  as WAY-114 expects. No finding.
- WAY-150: confirms the screening I did (titles of all 207, whole reads for the ones that bear). The ten decisions are now read whole and the
  counts are updated below.
- WAY-161: the Minor findings 1 to 7 lie within the task and none is marked outside it, so by WAY-161 the cycle fixes them before the request opens.
- WAY-303: concerns the unfixed remarks of merged requests, not the change. No bearing.
- Invariants: `skill-entry-points` holds (no skill description changed; `skill_entry_points.py` with no argument exits 0, `entry points are current`).
  `tracked-file-private-paths` holds (the `task-cycle` run passed its test). `outbound-link-reach` holds: the added lines hold no link. 
  `instruction-file-imports` holds: the added lines hold no `@` (a `grep '@'` of the added lines of the diff returned nothing). 
  `map-reference-target` and `test-method-citation` are checked by `foundation_check.py` and the test runs, which passed.
  `foundation-change-merge-route` and `return-step-record` concern the merge and the return step, which the orchestrator runs after this review.
  The others concern scripts, imports, the plan check and the plan state, none of which the change touches. No finding.

## Unread material

Counts: of 207 decisions that name a touched part in their *Scope* (`task-cycle` 122, `decisions` 81, `glossary` 43, `project-level` 77,
`foundation-review` 13, with overlaps), I read **32 whole** and **175 by title only**. Whole: WAY-01, 05, 07, 19, 24, 33, 35, 36, 37, 95, 99, 114, 124,
134, 150, 161, 263, 286, 287, 289, 290, 297, 300, 302, 303, 304, 305, 320, 327, 329, and the new WAY-353 and WAY-354. All 207 titles were run through.

By title only, none whose title points to a bearing on the change is left unopened by my judgment of the titles. Left by title are the decisions of the
parts that the change does not reach in their subject (scripts, the audit, technology choices, guidelines, the plan of a project, screenshots,
the cycle's private paths and the like). A decision with an unremarkable title that bears on the change can pass unopened, as WAY-150 says of its price.

Not read: `foundations/environment_facts.md` (no entry of it is touched); `foundations/invariants.md` read for the 27 invariants of the selection
and the 6 others (`fingerprint-definition`, `generated-overview`, `gate-exit-code`, `python-version-declared`, `root-claude-md-import`,
`installation-claude-guidance`) by title only; the part map beyond its headings and the `foundation-review` part; no guideline file (the-way has none).
`project-level/task/skill/` read only in `draft.md` and `final_review.md`, through the diff; `project-level/task/template.md` and
`task-cycle/skill/request_template.md` were read in the parts the diff touches and in the passages the form rules point at (request template lines
200-400), not whole.

## Searches not found or unclear

- The handoff names `python -B agent-instructions/skill_entry_points.py --check`? It does not: the handoff names only the three focused checks. The
  author's report says its own handoff named `--check`, which does not exist. Nothing for me to do.
- Which step of `foundation-review/SKILL.md` ends the review is unclear for a transitional-state decision where the human names a task (finding 1).
- Where a step for a check by hand may name a command: not settled by WAY-286, WAY-327 or the template (finding 5).
- No path to a data file of this review in a repository, so I could not check how a "task exists" answer is recorded beyond `proposals.md:55-60`.
