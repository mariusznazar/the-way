FAIL 4e09369fa5d4d61e4ff423c07d51e119d8bc73ba

# Review of the whole change: task `split-only-for-gain`

Range `0b77f5a2e1e37d04cd58888dd1d761f8e0329bd4..4e09369` (one commit; `git rev-parse HEAD` = `4e09369fa5d4d61e4ff423c07d51e119d8bc73ba`, as given). Counts: 1 blocking, 4 Minor within the task, 0 out of scope.

Changed files (my own `python -B task-cycle/change_file_sizes.py` run; the diff's own count is +81/-17):

| File | Before | After | Change |
|---|---|---|---|
| `foundations/decisions.md` | 12827 | 12882 | +55 (diff: +60/-5) |
| `project-level/plan/skill/cut_tasks.md` | 26 | 30 | +4 |
| `project-level/task/skill/orchestrated_mode.md` | 75 | 75 | +0 (1 line replaced) |
| `project-level/task/skill/read_sources.md` | 36 | 41 | +5 |
| `project-level/task/skill/resolve_gaps.md` | 87 | 87 | +0 (5 lines replaced) |

Nothing under `.runs/` is in the range (`git diff --stat -- .runs` empty).

## Findings

### Blocking

**1. Important — the change leaves the plan's critique splitting tasks for a "too large" test that WAY-372 and the task's question 5 rule out, and the paragraph it edits in `cut_tasks.md` contradicts itself. Within the task (item 7, row 6). Spans: the one commit; no plan or slices exist.**

Places:
- `project-level/plan/skill/cut_tasks.md:3-14` (the edited paragraph): line 8 now says "A task's size alone is no reason to cut it (WAY-372)"; lines 9-10 keep "A task is too large when its goal joins two or more effects, each of which can be checked alone in the running product and merged before the others", which now has no consequence in this file; lines 12-14 keep "the plan's critique judges size, and the human settles any split it asks for before the plan is handed over (WAY-146)".
- `foundations/decisions.md` WAY-146 (binding sentences, *Verification* "complies" example of the account task marked too large and sent to the human with its split, *Rejected* "where size is only a signal (WAY-13)"), left untouched.
- `project-level/plan/skill/critique_plan.md:16-22` and `project-level/plan/template.md:188`, left untouched.
- `foundations/decisions.md` WAY-372, second paragraph and *Verification* "violates" ("a split is proposed with no reason named; a plan's author cuts a task for its size alone"), and WAY-13 ("outside preparing and making the change it decides nothing").

What is wrong. After the change, one set of files tells the plan's critique to judge a task too large by the test "two or more effects, each checkable alone and merged before the others" and to put the split to the human, while the entry the change writes says a plan cuts tasks only by WAY-143 and the three reasons, that anyone who proposes a split names one of the three, and that size alone is no reason. The critique's test is not one of the three reasons. Its content, an independent effect that can "be merged before the others", is the reason the task's question 2 lists under *Not chosen* ("część ryzykowna obok niezależnej ... podział daje tylko to, że część niezależna scali się bez czekania, czyli 'szybciej'"), and WAY-372's own *Rejected* repeats it. So the critique's split question meets WAY-372's "violates" example "a split is proposed with no reason named", and WAY-146's *Rejected* quotes WAY-13 for a sentence ("where size is only a signal") that WAY-13 no longer holds. No precedence is recorded (no `narrows`), so WAY-25 applies: the collision is not settled, and the agent that met it may only record a precedence where what the human accepted gives the outcome, or stop and ask.

Why it matters. A plan's critique will go on putting split questions to the human for tasks that the task document, as accepted, says are not split for their size. That is the same cost the task exists to remove (a whole turn spent turning down a split, or a whole extra cycle for an accepted one), now moved to the plan. A reader who follows `cut_tasks.md` gets a definition of "too large" and no instruction that uses it, and a rule in the same paragraph that the critique judges size.

Judgement of the orchestrator's reading. It fulfils the letter of item 7: the sentence it names was replaced, and WAY-146, `critique_plan.md`, `template.md` and the plan checks were left alone, which WAY-30 and WAY-114 ask for when a change goes beyond what the accepted task carries (WAY-146 is not in the task's *Decisions in play*). It does not fulfil row 6 and question 5, whose answer is "tak ... zadania tnie się według WAY-143 i powodów z pytania 2". The author's own report (status `done with concerns`) names the collision correctly; the author's two readings (a fourth reason in WAY-372, or removal of the test from WAY-146, `critique_plan.md` and `template.md`) are the two ways open. Neither is mine to choose: the first changes row 2 (the task's question 2 lists exactly three reasons), the second changes WAY-146's meaning beyond the task.

What to do (a recommendation, for the orchestrator to put to the human as a question of decision):
- (a) Remove the "too large" test from WAY-146 (binding sentence, the "complies" example, *Rejected*), `critique_plan.md`, `plan/template.md` and `cut_tasks.md`, keeping the signal of open questions only if the human wants it. Cost: a change to WAY-146 beyond the task, so the human must approve it; the plan then has no critique of size, which is what questions 1 to 3 and 5 say the human wants. Cost of leaving as is: the contradiction above, which every plan critique meets.
- (b) Keep the test and name it a fourth reason in WAY-372. Cost: it reopens question 2, whose answer lists three reasons and rejects the reason this test is made of; it brings back the "ready sooner" argument question 1 refuses.
- (c) Leave both, and record in WAY-372 `narrows WAY-146` with the area where it prevails (WAY-25), the request quoting the passages of question 5 and row 6 that give the outcome. Cost: the critique's wording stays in four files with a precedence note, and WAY-146's *Verification* example still shows a split that WAY-372 forbids; the stale quotation of WAY-13 stays.
My recommendation is (a), put to the human, because (b) contradicts the accepted task and (c) keeps two files saying what the entry now forbids.

Evidence: `git show 4e09369:project-level/plan/skill/cut_tasks.md` lines 3-14; `grep -n -i -E "too large|size alone" foundations/decisions.md project-level/plan/skill/critique_plan.md project-level/plan/template.md` (hits at WAY-146 lines 4355-4359, 4368-4376, 4394; `critique_plan.md:16-22`; `template.md:188`).

### Minor (all within the task)

**2. `foundations/decisions.md` WAY-372, first sentence of the first paragraph: "A task is split only where the split makes the work better or cheaper" is stronger than row 1 and sits against the entry's own third sentence.** Row 1 says a split "ma sens", makes sense, when the work is better or cheaper; row 2 limits what the agent proposes. "A task is split only where" binds every split, the human's own included, while the same paragraph says the human "may ask for a split" for a task of any size. A reader comparing a change with the entry can read a split the human asks for, which is no better or cheaper, as a violation. A small fix: bind the proposer ("A split is proposed only where ...") and keep the human's request outside it.

**3. `foundations/decisions.md` WAY-372 *Rationale*, "work in several repositories cannot be one task while the cycle writes only in one", and the binding sentence's "since the cycle writes only in the product's repository".** The template asks *Rationale* to name no "what the process's own tools do or lack today" (`elements/decisions/template.md`, bullet on *Rationale* and *Rejected*), and the entry's *Based on* is `none`, so reason 2 rests on a fact of the cycle that no decision of this log or fact entry holds (it stands in `task-cycle/skill/SKILL.md:76` and, in part, in WAY-140). The sentence is taken from the task's question 2, so it is faithful to the source; the form departs from the template and a change to the cycle would silently strand the reason. Minor by WAY-364 (the content agrees with the files).

**4. Rows 4 and 5 are rightly handled, but the author's report ties them to WAY-139 as "already stated", which is too strong; name them in the request as lines of a skill.** WAY-139's binding sentence says "the task gains an item of its To do for that work or the human splits that work into a task of its own"; it does not say the refinement offers no split (row 4), nor that the questions on the record's life and on a failure come before the human splits the work off (row 5). WAY-139's own "complies" example, "a task that sets up the product's first deployment finds no deployment skill, and the human splits writing one into a task of its own", shows no question before the split. The result is still right: under WAY-134 "a rule of how an agent works that only one skill holds ... goes to that skill", and the where-it-goes questions of the decisions template send both rows there; both lines are in `project-level/task/skill/resolve_gaps.md:62-64` and `:85-87`. The tie to WAY-139 is only for the human's own split. In the request, name rows 4 and 5 as written into `resolve_gaps.md`, and WAY-139 as the entry they stand beside, not as the entry that states them. No second entry is needed.

**5. `foundations/decisions.md` WAY-13 *Rationale*, new sentence "a split for size alone adds a whole cycle, with its review, its tests and its request, and gives no better or cheaper result".** It states, in the entry on the weight of a task's process, the reasoning WAY-372 holds for a different question, and it is a general claim where WAY-372 allows three reasons for a split. It is true as written (for size alone) and the *Verification* clause added to WAY-13 is fine; the duplicate is one more place to change when WAY-372 changes. Minor, optional; a pointer ("see WAY-372") would do.

## Task coverage

- Item 1 (reasons only, three, named at proposal): met. `project-level/task/skill/read_sources.md:28-34` lists the three reasons and "name that reason (WAY-372)". The orchestrator's point 1b stands: the paragraph already left a size alone as a signal for the human, and the author applied items 1 and 2 to it as it stood; the result matches the item.
- Item 2 (nothing said of a split for size alone): met, `read_sources.md:32-34` ("no mention, no question, no recommendation").
- Item 3 (WAY-13): met. The clause "otherwise serves only as a signal to split it" is gone; "outside preparing and making the change it decides nothing" is in its place (`foundations/decisions.md` WAY-13 binding sentence).
- Item 4 (no offer of the split; the item goes to *To do*): met, `resolve_gaps.md:62-64`.
- Item 5 ("ask before offering the split" becomes asking before the human splits): met, `resolve_gaps.md:85-87`.
- Item 6 ("deployment-work splits" gone): met, `orchestrated_mode.md:15`.
- Item 7 (the sentence replaced): the letter is met; the outcome is not (finding 1).

Settlement rows (against the entries the change writes):
- Row 1: WAY-372 first sentence (finding 2 on its strength).
- Row 2: WAY-372 first paragraph, the three reasons in the task's words; the *Rejected* list holds all three ways not chosen of question 2.
- Row 3: WAY-13 (size decides nothing outside preparing and making) and WAY-372 (silence). The sentence "the human, who sees the whole document, may ask for a split" is in no row's text, but it is the second half of question 3's own *Answer* ("Mariusz widzi cały dokument przy akceptacji i może sam poprosić o podział"), which row 3 cites as its source. I judge it faithful, not invented; the only issue is its fit with sentence 1 (finding 2).
- Row 4: skill line in `resolve_gaps.md` (finding 4 on the tie).
- Row 5: skill line in `resolve_gaps.md`.
- Row 6: the sentence of `cut_tasks.md` and WAY-372's second paragraph (finding 1).

## Source fidelity

Compared WAY-372's *Rejected* with the *Not chosen* of questions 1, 2, 3 and 5: every way kept there stands with its cost (two of question 1, three of question 2, two of question 3, two of question 5), and the writer derived none (WAY-134). Rows 4 and 5's *Not chosen* (questions 4 and 6) are not in WAY-372, correctly, as it does not carry those rows. Nothing in the diff is taken from outside the task other than the author's choices named in its report (one entry for four rows, the human's request sentence, the plan's reasons stated in full in `cut_tasks.md`). The task's text and the entry's text agree on the three reasons, on "time does not count", and on the silence for size alone.

Form of WAY-372 against `elements/decisions/template.md`: the number is the next free one (WAY-372, no withdrawn number holds it; withdrawn list ends at WAY-224); it stands at the end of the log before "Withdrawn identifiers"; two binding paragraphs of 3 and 1 sentences, each of one to three; no *should*/*will*/capitalized keywords; *Scope* `project-level`, *Based on* `none`, *Relations* `derives from WAY-13 · derives from WAY-143`, *Origin* `none`; *Verification* a pair of examples that name the behaviour the task asks for. Departures: findings 2 and 3 only. The binding paragraph's limit: reason 3 ("a later step of the refinement offers a separate task") is held today only by "Missing discipline guidelines" (`project-level/task/skill/guideline_findings.md:10-24`, WAY-215), which is consistent.

## Foundation read against the change (WAY-150)

Parts touched: `decisions` (`foundations/decisions.md`), `project-level` (four skill files), and `task-cycle` for WAY-13 (the edited entry's own scope). Selection by "Reading the foundation": 330 entries in the log; 131 name `decisions` or `project-level` in *Scope* (5 558 lines), found by a script of my own (`the reviewer's scratch directory/sel.py`, output `...\scratchpad\sel.txt`).

Invariants: `foundations/invariants.md` read whole (376 lines, all entries; the *Part* `every`, `decisions` and `project-level` ones in particular). None states or contradicts rows 1 to 6; `project-plan-form` and `project-plan-check` derive from WAY-143 and WAY-146 and check form and structure, never size. Glossary: grep of headings and the `slice` entry; no term the change uses in another meaning. Part map read whole.

## Declined to judge

- Whether the plan's critique should keep a signal of "clearly more open questions, projected entries or In scope items" (kept by the author in `cut_tasks.md`): it is WAY-146's, outside the task; a part of the decision in finding 1.
- `project-level/task/skill/resolve_gaps.md:77` ("or the human splits it off"): it names the human's own split, matches WAY-139, offers nothing; left as the author left it.
- Whether the reason "a step of the refinement offers a separate task" is useful to a plan's author in `cut_tasks.md`: it follows row 6 ("the reasons of row 2") and the author's choice 4; not a defect.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Foundation | `python -B elements/common/foundation_check.py` (worktree root) | 0 | `0 errors` |
| File sizes | `python -B task-cycle/change_file_sizes.py 0b77f5a2e1e37d04cd58888dd1d761f8e0329bd4 4e09369` | 0 | table above |
| Removed wordings | `grep -rn -i -E "split|too large|large task|oversiz|size alone|its size|task's size|task of its own"` over `task-cycle project-level product-guidelines installation foundation-review process-audit elements README.md agent-instructions/README.md` (tests and agent types excluded) | 0 (hits read) | no instruction file offers a split for size; the only survivors are the plan's critique (finding 1), WAY-139's human split, slices (WAY-136) and unrelated uses |
| Line length | `awk 'length($0)>100'` over the four skill files | n/a | `read_sources.md:35` 106 columns, `resolve_gaps.md:82` 102 (that line is not in the diff); no rule of the-way fixes a width; the old paragraph of `read_sources.md` was 402 columns on one line, so no finding |
| Structure of code | the test of the invariant named by the rule of size | not run | no code changed; the-way's product guidelines hold no rule of size that reaches these files; finding of structure would be Minor (WAY-363); none made |

Not run: the author's gate commands (`gate/run_tests.py` on `agent-instructions`, `instruction-files`, `elements/common`, `project-level`), which the orchestrator runs; the full gate. Nothing failed.

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md`: WAY-25, WAY-30 (whole), to grade finding 1 by the rules of collision and of a change beyond the task's meaning.
- `foundations/decisions.md`: WAY-136 (passage), WAY-154 (opening paragraph), WAY-124 (whole), WAY-247 (whole), WAY-215 (whole), WAY-140 (whole), and passages at the audit entry that mentions "the human splits the work after the audit of code stopped" and WAY-165's rationale ("a task of its own"): search hits of `split`, `task of its own` and `too large`, to see whether any states or contradicts rows 1 to 6.
- `task-cycle/skill/SKILL.md:76`, `project-level/task/skill/guideline_findings.md:10-24`, `project-level/plan/skill/critique_plan.md`, `project-level/plan/template.md:188` (the lines found), `project-level/lead/skill/route_changes.md:7` and `project-level/task/skill/project_plan_task.md:10` (hit lines; a plan change's routing, compatible).
- `the author's own rules file for writing scripts` for my own script (the review's method does not name it).

## Unread material

Decisions of my selection: 131 (`decisions` or `project-level` in *Scope*). Read whole: 12 of them (WAY-25, WAY-30, WAY-124, WAY-134, WAY-139, WAY-140, WAY-143, WAY-146, WAY-156, WAY-215, WAY-247, WAY-372), plus WAY-13 whole (outside the selection by *Scope*, but the entry the change edits). Read in part: WAY-136, WAY-154, WAY-165 and the audit entry (passages found by search). Skimmed by title only: the remaining 117, from the list in `sel.txt` (title, scope, size and the words I searched for in each; the search hits are in the section above).

Decisions that bear on the change and stayed unread: WAY-114 (what a human accepts of an entry; read through WAY-30's and the template's quotation of it), WAY-113, WAY-33 and WAY-19 (read through the template and `way_of_working.md`, not as entries), WAY-144 and WAY-147 (tasks of a plan side by side, naming), WAY-142 (what the breakdown writes), WAY-214 and WAY-218 (missing guidelines in refinement and in the breakdown). None of them has a hit on `split`, `too large`, `size` of a task, `oversiz` or `task of its own`, which is what I searched for.

Read whole: `task-cycle/review/SKILL.md`, `whole_change.md`, the handoff, the task document, the author's report, `elements/decisions/template.md`, `elements/common/way_of_working.md`, `foundations/part_map.md`, `foundations/invariants.md`, the four changed skill files (the passages the diff reaches, with their neighbours; `cut_tasks.md` whole). Not read: `elements/decisions/examples.md` (six lines, names WAY-03; not needed to judge the form, which I took from the template); `elements/common/rules.md` (the entry's rules of form the template points to; the *Rationale* and binding-sentence rules I used are the template's own); `guidelines/` (the-way has none); guideline files: none, no `guidelines/` directory.

## Searches not found or unclear

- A rule fixing a line width of the-way's instruction files: not found (grep of `agent-instructions/README.md`, `instruction-files/*.md`, `product-guidelines/*.md` for "100 col", "columns", "line length", "wrap").
- A decision or fact entry that holds "the cycle writes only in the product's repository" as a rule with its own number: not found; it stands in `task-cycle/skill/SKILL.md:76` and is partly in WAY-140 (finding 3).
- The handoff said the author's reading of `read_sources.md`'s paragraph differs from the task's description; the file at the base matches the handoff (it already said "you name as a signal and leave the split to the human"). Clear.
- The handoff's "handoff answer 4" and "handoff answer 1" (the author's handoff, with the orchestrator's orders to leave WAY-139 and WAY-146 untouched) are not among the files I was given; I judged the author's report as it states them.
