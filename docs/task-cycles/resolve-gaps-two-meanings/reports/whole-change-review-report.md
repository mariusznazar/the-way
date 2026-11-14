FAIL 9c66ee1179d0a84f41dec2c6c19d1d87de36d7dd

# Review of the whole change: task `resolve-gaps-two-meanings`

Range `f4af75d..9c66ee1`, one commit (`git log` shows only `9c66ee1`); `git rev-parse HEAD` of the reviewed
worktree is `9c66ee1179d0a84f41dec2c6c19d1d87de36d7dd`, the head given. Reviewer did not make the change; no
subagent used.

Changed files (python -B task-cycle/change_file_sizes.py f4af75d 9c66ee1, exit 0):

| File | Before | After | Change |
|---|---|---|---|
| `foundations/decisions.md` | 12925 | 12989 | +64 |
| `project-level/task/skill/SKILL.md` | 62 | 62 | +0 (2 lines out, 2 in) |
| `project-level/task/skill/resolve_gaps.md` | 91 | 108 | +17 |

Structure of the code left: the-way has no `guidelines/coding.md` and so no rule of size and no test of
it; the numbers above and the diff are the material. No function; no file crossed a threshold that exists;
no code without a user; no name that stopped being true. No finding of structure.

## Findings

### Critical

none

### Important (blocking; within the task; the change is one commit, no plan, so no slice)

**I-1. The new entry and the new text of the skill tell a different thing about an ambiguity of the approved
project definition (WAY-263).**

- Place: `foundations/decisions.md:12895-12896` (WAY-374, second paragraph: "an ambiguity in the approved
  project definition goes back to the definition and its readiness gate (WAY-118)") against
  `project-level/task/skill/resolve_gaps.md:24-25` ("Where the word stands in the approved project definition
  and the answer would change it, the paragraph below on that definition applies").
- What is wrong: the binding sentence of the entry sends every ambiguity of the definition back to the
  definition and its gate, without a condition. The skill sends it there only where the human's answer would
  change the definition, and that is what the paragraph it points to says (`resolve_gaps.md:40-41`: "If the
  answer changes the approved project definition or a projected decision of it, route that change"). The
  entry's sentence is the broader one, and WAY-118, which it cites, makes a pass through the gate follow a
  change ("A change to those sections after approval goes through the gate again"), not an ambiguity. The task
  Q1 answer says "jak dziś daje krok „Resolve the gaps”", i.e. the conditional form; the entry dropped the
  condition while the skill kept it.
- Why it matters: WAY-263 grades a change whose files restate an entry it writes differently, more broadly or
  without a qualification, as Important. An agent comparing the skill with the entry finds a departure; an
  agent following the entry alone may stop and send a task back to the definition for a word it would have
  asked about and settled under *Questions to settle* with the definition's text untouched, which is the cost
  WAY-118 does not impose. It also leaves open whether the word of the definition is asked about at all.
- Evidence: the two quoted passages above; WAY-118 read whole at `foundations/decisions.md:3017-3051`.
- Fix proposed: bring one side to the other in the same words, most simply the entry: "an ambiguity in the
  approved project definition whose resolution changes the definition goes back to the definition and its
  readiness gate (WAY-118)", leaving the skill as it stands.

### Minor (within the task)

- **M-1.** `project-level/task/skill/SKILL.md:42-43` — the inserted words left line 43 at 142 characters
  (the rest of the file wraps at about 100) because the paragraph was not re-wrapped. Re-wrap the paragraph.
- **M-2.** `foundations/decisions.md:12880`, `12883`, `12884`, `12936`, `12939`
  (lines of 102-112 characters among neighbours wrapped at 100): the new entry is not wrapped as the entries
  around it are. Polish only.
- **M-3.** `foundations/decisions.md:12926` (*Rationale*): "the standard WAY-99 sets for a word of the
  foundation". WAY-99's standard is that a sentence the files hold is true in one meaning and false in the
  other; the entry's standard is that a sentence allows both readings and the readings give different
  observable results in the task's scope. They are alike in kind (a sentence standing in the files, none made
  up), not the same standard. The words "after the model of" would say what the task's *Context* says ("bierze
  wzór z testu WAY-99").
- **M-4.** `foundations/decisions.md:12894-12895` and `project-level/task/skill/resolve_gaps.md:21-23` — the
  candidate-for-the-glossary sentence says "a meaning ... a reader who knows the product's field would not
  give the word". WAY-95 adds a qualification for a narrower meaning (an entry only where a reader of the field
  would read a sentence wrongly). The route is a candidate that WAY-95 then judges at the table of settlements
  (WAY-134), and the wording is the task's own (Q4), so nothing is lost, but one clause "(WAY-95 judges it
  there)" would remove the question. Graded Minor because the sentence names WAY-95 and says "candidate".
- **M-5.** `project-level/task/skill/resolve_gaps.md:10-25` — the new paragraph is one block of eight sentences;
  To do 3 asks for the question "według „How a skill asks”" and the paragraph says only "as a question of
  decision" without naming the section (the entry names WAY-113). A reader of the skill alone finds the way
  through "question of decision", which the shared file defines; naming it would match the task word for word.

### Out of scope

none

## Check against the task

- To do 1 — met: `resolve_gaps.md:10-14` searches the task document and "the sentences of the sources its
  required result rests on — the foundation decisions it quotes and the sentences of the approved project
  definition" for a word allowing different required behaviours that no approved definition, entry of the
  foundation (glossary entry named), or answer of the human settles (Q1, Q4).
- To do 2 — met: `resolve_gaps.md:16-18`, "A case counts only where a sentence standing in the document or in
  such a source allows both readings and the readings give different, observable results inside the task's
  scope; a reading no sentence allows and a scenario outside the scope count for nothing". Same sentence in
  WAY-374 paragraph 2. This is the guard of answer 2; the wording invites no invented case: it requires a
  standing sentence, an observable difference and the scope, and states "no duty and no number".
- To do 3 — met: example "under reading A this happens, under reading B that", asked as a question of
  decision, answer under *Questions to settle* "as above" (the first paragraph of the file gives the ways not
  chosen with the answer, WAY-134). See M-5 for the one naming difference.
- To do 4 — met: `resolve_gaps.md:23-24`, "The check owes no finding and no number of cases; where it finds
  none, say nothing of it" (Q3; way not chosen, "one sentence it found no word", is in the entry's *Rejected*
  and the entry's "violates" list).
- To do 5 — met: `SKILL.md:42-43` lists "the check for a word that can be read two ways" beside questions and
  choices. `description` unchanged, so no entry-point regeneration is owed.
- Q1 to Q4 answers and ways not chosen: each of the five ways not chosen of Q1-Q4 stands in the entry's
  *Rejected* with its cost; none is invented (WAY-134: only the ways of the row's source). The way of Q5
  (wait for the trial, run it now) is left out as it belongs to another question and to the out-of-scope item.
  Q2's wording "the principle alone" matches. Q4's "glossary of the-way for words of the process, the
  product's glossary for words of the product" is in `resolve_gaps.md:14-16`; "nothing changes in the
  glossary" is `resolve_gaps.md:22-23` ("this step edits no glossary").
- Out of scope — kept: no trial of a list (card D8), no private note, no count from the register in the
  diff (grep of the diff for `D8`, `trial`, `loop2`, `mapa`, `usprawnien`: no hit; and the invariant
  `tracked-file-private-paths` is held by the 394 tests of `task-cycle`, which passed).
- Row 1 of *Settlements to record*: written whole as WAY-374 (kind decision, *Scope* project-level, *Relations*
  `derives from WAY-100`, *Based on* none, *Origin* none). The row says the practice is taken from the course,
  what is adopted, where (the refinement of a task) and under which bounds; the entry's *Rationale* names the
  course and says it binds the refinement and nowhere else, as WAY-100 requires. All bounds of the row are in
  the binding sentences: the extent of the check, the sentence standing in the source, the silence when
  nothing is found. Fidelity: apart from I-1, nothing taken from the sources is altered or invented.
- *Decisions in play* of the task (WAY-100, 113, 95, 99, 118): each keeps its meaning — the change edits none
  of them (the diff touches the log only by an appended entry; `git diff` shows no line removed). WAY-374
  contradicts none: WAY-100 (it is the adoption it asks for), WAY-113 (it asks in text as a question of
  decision, naming it), WAY-95 (it adds no entry to the glossary and routes a candidate), WAY-99 (it takes only
  its habit of judging by a sentence the files hold; see M-3), WAY-118 (see I-1). Also read and found
  consistent: WAY-134 (the candidate goes to the table; the *Rejected* of the new entry holds only the ways of
  the row's source), WAY-154/155 (in orchestrated refinement the question goes through the conversation file;
  the answering agent answers only from a quotation, so a word settled by a source is not asked), WAY-313 to
  315 (no step in the new text asks leave to open a decision), WAY-124 (the document is ready only when every
  known question blocking the outcome is answered; the new question is one such), WAY-372 (no mention of a
  split), WAY-256 (the paragraph stays in the step's file; the pointer stays in `SKILL.md`), WAY-308/309 (no
  absolute path or note link in the diff).
- Invariants (all 376 lines read whole): those with *Part* `every` or `project-level` that the change
  reaches are `foundation-file-kinds`, `repository-file-location`, `outbound-link-reach`,
  `tracked-file-private-paths`, `skill-entry-points`, `test-method-citation`, `derived-file-content`; none is
  contradicted. No invariant test is changed by the change.

## Checks run

| Check | Where | Result |
|---|---|---|
| `git rev-parse HEAD`, `git log f4af75d..9c66ee1 --oneline`, `git diff f4af75d..9c66ee1` | reviewed worktree | head confirmed; one commit |
| `python -B task-cycle/change_file_sizes.py f4af75d 9c66ee1` | reviewed worktree | exit 0 |
| `python -B elements/common/foundation_check.py` | reviewed worktree | exit 0, `0 errors` |
| `python -B instruction-files/check_instructions.py .` | reviewed worktree | exit 0, `0 error, 0 warn, 3 info` |
| `python -B gate/run_tests.py project-level` | worktree of the head in `.runs/review-whole/head` | exit 0, 275 tests OK |
| `python -B gate/run_tests.py task-cycle` | same worktree | exit 0, 394 tests OK (holds `tracked-file-private-paths`) |
| awk for lines over 100 characters in the two skill files, and of added lines of the diff of `decisions.md` | reviewed worktree | M-1, M-2 |

Not run: `gate/run_tests.py elements/common`, `instruction-files` and `agent-instructions` (the author's report
claims them OK; the change touches no code and the `foundation_check` and `check_instructions` runs above
cover the files this change alters; unverified by me); the whole gate (the cycle's own run).

## Declined to judge

- The sentence of the course (lesson m2l2) quoted in the entry's *Rationale*: its source is the task's *Context*
  and a private note outside the repository; I cannot open either and judged only that the entry names the
  practice, not that the course says it so. The author states the same as a search not found.
- Whether the pair of examples under *Verification* of WAY-374 is the best possible: the template makes the
  pair optional and the example is within the form; not graded further.

## Reaches beyond the dispatch

- `elements/decisions/template.md` read whole, to compare the form of WAY-374 with the template, and
  `foundations/decisions.md:12790-12878` (WAY-372, WAY-373) as the nearest entries of the present form.
- `grep -n "10xDEVS\|course" foundations/decisions.md`, to see how earlier entries cite the course in
  *Rationale* with *Based on* `none` (lines 8261, 8842, 8956, 9238 and others); it settles that I-1 is the only
  departure and *Based on* `none` follows the practice.
- `grep -rn "resolve_gaps\|Resolve the gaps"` over `*.md` and `*.py` outside `.runs/` and the log, to find
  other places that list what the step does: `deployment_skill_guide.md`, `carry_foundation.md`,
  `project_plan_task.md`, `technology/task_run.md` refer to the file or to its WAY-118 paragraph only; none
  needs a change.
- `foundations/decisions.md` WAY-308/309 (private paths) and WAY-124 (readiness), read whole for the
  checks above.

## Unread material

Counts for the selection: parts touched: `project-level` (files `project-level/task/skill/*` and the entries
that the new text of `foundations/decisions.md` names as *Scope*: `project-level`). The decisions whose *Scope*
names `project-level`, by a script over the `- **Scope:**` lines: 81 (of 332 entries counted by heading, the new
entry among them).

- Decisions of the selection read whole: 17 — WAY-100, 113, 114, 118, 124, 134, 150, 154, 155, 256, 308, 309,
  313, 314, 315, 372, 374.
- Decisions of the selection run through by title only: 64 (the other 64 of the 81 titles, which I listed from
  the script's output and ran through once). None of them has a title that points to a bearing on the change,
  in my reading; those I considered most near and did not open are WAY-111 (what the project level reads in the
  foundation), WAY-115, WAY-120 (critique of a proposal), WAY-140, WAY-153, WAY-214 to 218 (guidelines found
  missing at refinement), WAY-353 (how a task points to a place in a file), WAY-265 (file of a variant named by a
  step), and WAY-373, which stands outside the selection and was read whole as a neighbour.
- Outside the selection by *Scope*, read whole: WAY-95 and WAY-99 (named by the task's *Decisions in play*;
  their *Scope* is glossary and others, not project-level). Total read whole: 19; by title only: 64.
- Not made: the decisions whose *Scope* names `decisions` alone or `task-cycle` alone and not `project-level`;
  `foundations/decisions.md` is a file collecting entries about several parts, and WAY-44 assigns it to the
  parts the new entry names (project-level). WAY-33 and WAY-44 were not read whole (their use was by the title).
- Foundation read whole: `foundations/invariants.md` (376 lines), `foundations/glossary.md` (191 lines),
  `foundations/part_map.md` (read whole, in two reads, lines 1-200 and 200-267), `elements/common/way_of_working.md`, `elements/decisions/template.md`.
- Guideline files: none (the-way has no `guidelines/` directory; `product-guidelines/reading.md` not read for
  that reason).
- Not read whole: `project-level/task/skill/draft.md`, `carry_foundation.md`, `find_settlements.md`,
  `orchestrated_mode.md`, `project_plan_task.md`, `final_review.md` and `project-level/task/template.md` (the
  step 5 reference "which step 5 finds" I confirmed from the heading `## 5. Find what the refinement settles`
  and its sentence in `SKILL.md:58-60`, not from `find_settlements.md`); the author's report was read whole as
  claims, not as evidence.

## Searches not found or unclear

- A passage of lesson m2l2 of the 10xDEVS course: not found in the repository (as in the author's report); the
  entry names the practice in words, as WAY-273 and WAY-280 do. Unclear whether the course's step probes terms
  of the request only or also of sources it rests on; the entry says what the-way takes, not what the course has.
- "How a skill asks" named in To do 3: it is a section heading of `elements/common/way_of_working.md`; the skill
  file does not name it (M-5).

## Working copies

One worktree of the head `9c66ee1` at `.runs/review-whole/head`
(for the two test runs), plus a list-of-scopes file `.runs/review-whole/scope.txt` in the same directory.
Removed with `git worktree remove --force` and `git worktree prune`; the directory `.runs/review-whole/` was
removed; `git worktree list` no longer shows it. No remainder. The reviewed worktree, its index and branch were
not changed (`git status --short` empty after the review).
