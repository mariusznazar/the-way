PASS 44c1d9924ea5832b0ce8dfb825814c30e063c6e6

# Review of the whole change: oversized-plan-tasks

Range `5a24ac97277fa1c04fbb967da5c6a2854d17cb8f..44c1d99` (`0ed5ad7`, `44c1d99`); `git rev-parse HEAD` is `44c1d9924ea5832b0ce8dfb825814c30e063c6e6`, as dispatched. One author, no plan, no slices. Nothing in the worktree was changed by this review.

Result: 0 blocking, 3 Minor within the task, 1 Minor outside the task.

## Changed files (from `python -B task-cycle/change_file_sizes.py <base> 44c1d99`, exit 0)

| File | Before | After | Change |
|---|---|---|---|
| `foundations/decisions.md` (entry WAY-146 only, lines 4177-4234) | 12589 | 12610 | +21 |
| `project-level/plan/skill/critique_plan.md` | 20 | 23 | +3 |
| `project-level/plan/skill/cut_tasks.md` | 21 | 26 | +5 |
| `project-level/plan/template.md` | 188 | 190 | +2 |

Total +31 lines. All four files are prose; no function, no code and no test changed, so there is no growth of a function and no code left without a user. The-way has no rule of size (WAY-328, WAY-363), so the structure check is the numbers above and the diff only. No name stopped being true: the headings and file names are unchanged.

## Against the task (frozen `task.md`)

- To do 1 (`cut_tasks.md` first bullet): met. The text carries the two-or-more-effects test, each checkable alone in the running product and mergeable before the others, and the signal (more open questions, projected entries or In scope items than the rest of the plan) with "no number decides it". It matches the task's wording; nothing is widened.
- To do 2 (`critique_plan.md`, "Ask it to judge" sentence): met. The critic is also asked whether each task is too large "by the test in `cut_tasks.md` beside this skill". The pointer is as the task gives it ("according to the criterion of point 1"); see Minor 3.
- To do 3 (`critique_plan.md`, "Verify each observation" bullet): met. The bullet says a split asked for because of size goes to the human as a question before the plan is handed over, with the split and the choice to keep the task, and the author alone does not make it.
- To do 4 (WAY-146 edited in place, WAY-07): met. The binding sentences are still three. They add the size judgment to the critique's list and say the human settles a size split. Verification holds one complies and one violates example in words, with no pointer to a private note (WAY-27; the example names no plan, game or note). *Rejected* holds the two ways not chosen under question 2 (threshold, counts printout), each with its reason as the source keeps it, and the third item discussed below. The entry has no version, no new number.
- Acceptance criterion: the test and the Verification example separate the two cases. The account goal (accounts, login, blocking, address confirmation, password reset, mail) joins several effects, each checkable alone and mergeable first, so it is marked; "a blocked player loses the session and cannot log in" is one effect (blocking), so it is not marked. The Verification example says exactly this in the entry's own words.
- Settlements row 1 (test of the goal, signal only, no numeric threshold in a script; changes WAY-146): written in the binding sentence, Rationale and Rejected. Row 2 (the human settles a size split, with the choice to keep; the author never splits for size alone; changes WAY-146): written in the binding sentence, Verification and Rejected, `cut_tasks.md` and `critique_plan.md`. Both rows are written by editing WAY-146; no entry is added. That fits the rows' "changes WAY-146".
- Out of scope: `plan_check.py` untouched, no measurement made. Confirmed by the diff.

## The author's choices and the orchestrator's rulings, judged

1. Template clause in `project-level/plan/template.md` (file the task does not name). I judge it right. The paragraph "What the check decides, and what the critique judges" restates WAY-146's list of what the critique judges and cites WAY-146 three times; after the edit of WAY-146 it would have gone on stating a list the decision no longer gives, which WAY-263 grades Important for a change that writes the entry. The clause is the decision's size test in its own words, adds nothing else (no threshold, no rule of who splits) and leaves the second sentence intact. It is not widening: the task's Out of scope names only the measurement and `plan_check.py`. I searched for other echoes of the list (`grep` for "answer settles", "settles its question", "too large", "WAY-146" outside `foundations/decisions.md`): the other hits are `critique_plan.md` (changed), `plan_check.py:45-47` (see Minor 4, out of scope), and unrelated senses of "too large" (slices).
2. Third item in *Rejected* (author splits after the critique's remark). I judge it right and required: the template says the *Rejected* of a decision written from a row of *Settlements to record* holds the ways not chosen that the row's source keeps (WAY-134), and the source of row 2 is question 3, whose *Not chosen* is exactly this way, with the cost beside it ("may split too finely; each needless split is a whole cycle the human sees only in the handed-over plan"). To do 4 names only the two ways under question 2, so the third item goes beyond its letter but not beyond the task as a whole (it is the not-chosen way of row 2). The text follows the source and adds no way the writer derived.
3. Change of the cut-tasks bullet ("A large task is split" to "A task too large is split ... The author never splits a task for its size alone"). Needed: the old sentence told the plan's author to split a large task, which contradicts question 3 and the new binding sentence. The rewrite keeps WAY-13's "its size chooses nothing else" and adds the pointer to WAY-146. Its remaining weakness is Minor 2.

## Against the foundation

- WAY-146 (changed): the binding sentence, `cut_tasks.md`, `critique_plan.md` and the template say the same test and the same routing. The binding sentence is stated no more broadly than its sources: "no script judges a task's size" follows from rejecting both the threshold and the printout of counts (question 2). No restatement with a different or broader meaning found (WAY-263).
- Collisions checked: WAY-13 (size "serves only as a signal to split it"): consistent, the change adds who judges and who decides. WAY-120 (author verifies each observation and gives a verdict): consistent, the author still verifies and gives a verdict, the correction goes to the human, as that bullet already does for a changed human answer. WAY-143, 145 (a question that arises only in the breakdown goes to the human before handover): consistent. WAY-151 (critic reads the whole plan): consistent. WAY-156 (after handover an in-scope task split is delegated to a plan-project agent): a different moment from WAY-146, which governs before handover; no collision, listed in Declined to judge.
- Invariants `project-plan-form` and `project-plan-check` (both test, both derive from WAY-146): neither judges size, so no invariant test changes. No changed invariant test.
- Template of the entry (`elements/decisions/template.md`): *Rationale* and *Rejected* name no file and no count of the foundation; the changed text keeps to that, except the point in Minor 1.

## Findings

### Critical, Important

none

### Minor (within the task)

1. `foundations/decisions.md:4226` (*Rejected*, the threshold item): "the account task after its split still held more than a third of the questions" states a measurement of the product's own plan (a plan the reader of this repository cannot open). The decision template says such a measurement stands in *Rationale* or *Rejected* with what was measured and under which conditions, and says in the prose that it is the product's own and that its record is not open to a reader of the repository. The sentence carries neither; it is read as a fact about a case without a source. This departs from the form of its template while the content agrees with the task (WAY-364), so Minor. A reader is not led to a wrong reading by it (the point of the item, that a threshold fitted to one case would stop a task that is right to stand, stays clear). Suggested fix: add a clause that this is the measurement of the-way's author on one plan of a product and that its record is not open to a reader of this repository, or state the item without the case figure.
2. `project-level/plan/skill/cut_tasks.md:4-5`: "A task too large is split, and its size chooses nothing else (WAY-13)." reads as an unqualified rule addressed to the author doing the cut; the qualification that the human settles the split and may keep the task comes two sentences later (line 8-10) and in WAY-146. Read alone, the first sentence still tells the author to split. This restates WAY-146 without its qualification in the sentence itself (WAY-263), but the next sentences qualify it in the same bullet, so a reader reading the bullet is not misled; Minor. Suggested wording: "A task too large is put to the human to split, ...".
3. `project-level/plan/skill/critique_plan.md:16-17`: the critic is asked to judge size "by the test in `cut_tasks.md` beside this skill", while the other items of the list are given in the sentence itself. The critic is a fresh agent that gets its prompt from the author; the other four items travel in the sentence the author reads, the size test only through another file. If the author passes the sentence on without the test, the critic has no criterion. The task asks for the criterion from point 1, so the pointer is faithful; it is a fragility, not a defect of the requirement. Suggested fix: say that the author hands the critic the test (its text) with the request.

### Minor (outside the task)

4. `project-level/plan_check.py:45-47` (docstring, "The check judges nothing the plan's critique judges: whether a goal is checkable..., where a technical element enters, whether a moved question has its reason in the change log, or whether an answer settles its question"): the list of what the critique judges omits the size of a task, which the critique now judges. The docstring stays true (the script does not judge size), only incomplete. The task puts `plan_check.py` out of scope and the orchestrator ruled to leave it; so it is outside the task and not blocking. Whoever next touches that file may add it.

## Declined to judge

- WAY-156 (after handover, an in-scope task split is delegated to a plan-project agent and logged): whether a split after handover, for size alone, needs the same routing to the human. The change governs the plan before it is handed over (WAY-146); a decision about leading a plan after handover is another question. Outside the task.
- The measurement of the 12.11.2026 note (size of the task document against the problems of a cycle): the task's own Out of scope.
- Whether WAY-146 should gain a *Relations* link to WAY-13: the author left it (the field's two types do not fit); no rule requires it. Not judged as a defect.

## Checks run

| Check | Command | Result |
|---|---|---|
| File sizes of the range | `python -B task-cycle/change_file_sizes.py 5a24ac97277fa1c04fbb967da5c6a2854d17cb8f 44c1d99` | exit 0 |
| Foundation check | `python -B elements/common/foundation_check.py` | exit 0, "0 errors" |
| Plan tests | `python -B -m unittest discover -s project-level -p "test_*.py"` | exit 0, 275 tests OK (380 s) |
| Diff and log | `git diff <base>..44c1d99`, `git log <base>..44c1d99` | read whole (4 files, 46 insertions, 15 deletions) |
| Echoes of the changed wording | `grep -rn` for "answer settles", "settles its question", "large task", "too large", "WAY-146" over `*.md` and `*.py` outside `.runs` and outside the WAY-146 entry | read; one stale echo found (Minor 4), the template one was edited in the change |
| Structure test of a rule of size | not run: the-way has no rule of size (WAY-328, WAY-363) | not applicable |
| `project-level/plan_check.py` on a plan | not run: no plan in the change and the script is untouched | not run |
| The product's gate `gate/run_tests.py` | not run: the orchestrator's | not run |

The `project-level` tests and the foundation check do not read the prose of `cut_tasks.md` or `critique_plan.md`; the tests therefore protect the change only against breaking the checked form, and the content was checked by reading. The acceptance criterion has no test; it is judged by reading, which is what the task's design intends (criterion for agents, no script).

## Reaches beyond the dispatch (section 1)

- `elements/common/way_of_working.md`: whole, for "Reading the foundation".
- `elements/decisions/template.md`: whole, to compare the entry's form and the rule for *Rejected* of a decision written from a row (WAY-134, WAY-364).
- `foundations/invariants.md` lines 225-270 (`project-plan-form`, `project-plan-check`, `skill-entry-points`): to see whether an invariant judges size.
- `project-level/plan/template.md` lines 165-190 and `project-level/plan_check.py` lines 30-55: to find echoes of WAY-146's list.
- `project-level/definition_template.md:92-102` and `foundations/decisions.md` (WAY-146 references at lines 4177, 4426, 4430, 6991, 7016): echoes of WAY-146; none restates the critique's list.

## Unread material

Counts of the decisions of my selection (parts touched: `project-level`, and `decisions` for the edited log): the search of *Scope* for `project-level` gave 79 entries. I read whole 13 of them: WAY-120, 142, 143, 144, 145, 146, 147, 151, 152, 156, and WAY-13, 07, 27 (outside the `project-level` scope but named by the task's *Decisions in play* or by the change's sentences). I went through by title only the remaining 66 (including WAY-308, of which I read the binding sentence and Verification and not its *Rationale* and *Rejected*, to confirm that the Verification example names no private path or note). Each decision bearing on the change was read whole; no decision whose title points to a bearing on the change stayed unread, except as follows:

- WAY-106 (what the project level writes before tasks exist, 23 lines) and WAY-230 (side by side tasks): read by title; I judged them not to concern size or the critique. WAY-134 (settlements and *Rejected*): I took its rule from the decision template's own paragraph, not the entry.
- Decisions whose *Scope* names `decisions` (the part of the edited file; e.g. WAY-05, WAY-19, WAY-29, WAY-35): not read; the template and `rules.md` carry what they give. `elements/common/rules.md`, `elements/decisions/examples.md`, `elements/decisions/skill/*`: not read; not needed for judging an in-place edit of an entry. The-way's glossary: not read.
- `foundations/part_map.md`: only the `project-level` lines (74-91) read, to confirm that the touched files are not a trust boundary (the boundary files are `readiness_check.py`, `plan_check.py`, `plan_state.py`); not the whole entry. `product-guidelines/reading.md` not read: the-way holds no coding or testing guidelines (WAY-328) and no guideline file applies to prose of a skill.
- WAY-13, WAY-07, WAY-27: read whole.

## Searches not found or unclear

- Not found: a rule in the-way's coding guidelines of size, or guidelines for the-way's own code (none, WAY-328).
- Unclear: whether the critic of the plan receives `cut_tasks.md` or only the author's prompt (Minor 3); `critique_plan.md` does not say how the criterion reaches it.
- The handoff said the part map's boundary files of `project-level` are untouched: confirmed by the diff (none of the three scripts changed).
