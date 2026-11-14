PASS edf169933195404993b719c154fc361b4bd9fc15

# Review of the fix: task `split-only-for-gain`

Fix range `4e09369..edf1699` (one commit, `git rev-parse HEAD` = `edf169933195404993b719c154fc361b4bd9fc15`, as given); files: `foundations/decisions.md` (+25/-58 with the three others), `project-level/plan/skill/critique_plan.md`, `project-level/plan/skill/cut_tasks.md`, `project-level/plan/template.md`. Nothing under `.runs/` is in the range. Method: `task-cycle/review/SKILL.md` with `fix.md`. Counts: 0 blocking, 3 Minor in the fix diff (none blocks, WAY-162), 0 out of scope.

## Each finding of the findings file

**1. Fixed.** The plan critique's judgment of a task's size and the human's decision on a split it asks for are gone from every place that held them:
- WAY-146: the binding sentences (the "whether a task is too large" clause, the "no script judges a task's size" and "goes to the human as a question" clauses, "the plan's author never splits it for its size alone"), the *Verification* "complies" example of the account task and the "violates" clauses about the account task and the threshold, the *Rationale* sentences on size and on the signal, and the *Rejected* items on the numeric threshold (with the stale quotation of WAY-13), the script that prints counts, and the author splitting after a remark. Everything else of WAY-146 is word for word as at `4e09369` (the script's checks, the four other judgments of the critique, "A check a script can make is never left to the critique", *Relations*, the two invariants, *Origin*); I compared the two versions in `git diff 4e09369..edf1699`.
- `project-level/plan/skill/critique_plan.md` (the test and "the author hands the critic that test", the human's split question), `project-level/plan/template.md` (the clause on "too large"), `project-level/plan/skill/cut_tasks.md` (the "too large" definition, the signal, "the plan's critique judges size").
- Searched the whole repository (`grep -rn -i -E "merged before the others|size alone|its size|task's size|too large|signal to look|more open questions|clearly more"`, `.claude`, `.agents` and the slice-size texts of `task-cycle` and `process-audit`, which are about slices, set aside): no remaining wording of the critique's size test. What remains is WAY-13, WAY-372, `read_sources.md:32` and `cut_tasks.md:8` (all the new rule), WAY-136 and the slice size entries (slices of a change, correctly untouched). No test of `project-level` held a removed wording; `plan_check.py` and its tests hold no size judgment (grep).
- No collision is left with WAY-372, so no `narrows` is needed; the author wrote none, which is right (WAY-25 applies only to an unrecorded collision, and there is none now). I looked for a collision with the other decisions that bear on the plan's cut (WAY-143, WAY-156's "in-scope task split" routed to the plan-project agent, WAY-215's prerequisite task); none.

Judgement of the removal of the plan's "signal" (clearly more open questions, projected entries or In scope items than the rest of the plan), which the orchestrator ordered and which goes beyond the sentence the task names: I accept it and grade it no finding. The signal's only use, in WAY-146's *Rationale* and `cut_tasks.md`, was to point the critique to a task it might judge too large; with the judgment removed it has no consequence, and leaving it would be a dead sentence that reads as a size rule. It rests on the accepted passages the handoff gives (question 5's answer and its *Not chosen* "poza zakresem", row 6). The cost, if the human wanted it kept: one sentence to restore in WAY-146 and `cut_tasks.md`. The request should name the removal and those passages, as WAY-25 and the handoff ask; that is the orchestrator's.

**2. Fixed.** `foundations/decisions.md` WAY-372, first sentence now "A split of a task is proposed only where it makes the work better or cheaper" and ends "a split the human asks for, who sees the whole document, stands without one": the proposer is bound, the human's request is outside the rule, and the *Verification* "complies" example ("a split the human asks for is made") agrees.

**3. Fixed.** The binding sentence now reads "the parts change different repositories (WAY-140)" and *Relations* is `derives from WAY-13 · derives from WAY-140 · derives from WAY-143`; the *Rationale* no longer says what the cycle writes ("parts in different repositories are not one change"). I judge the choice of *Relations* over *Based on* right: the template gives *Based on* to sources outside the product (environment facts, cited sources) and *Relations* to a decision the entry serves, and WAY-140 is a decision of this log; no fact entry or source is invented. WAY-140 states that an effect outside the product's repository is made only by a human; it does not say in so many words "the cycle writes only in one repository", so the reason leans on it rather than quoting it, which is enough for a pointer. The skill files still say "since the cycle writes only in the product's repository" (`project-level/plan/skill/cut_tasks.md:7-8`, `read_sources.md`): an instruction file may carry the reason beside the entry, so no finding.

**4.** Asks for the wording of the request; the files need no change, as the author reports. Not mine to judge here.

**5. Fixed.** WAY-13's *Rationale* now ends "...size tells nothing worth deciding on, and a split for size alone has no reason of its own (WAY-372)": a pointer, no duplicated reasoning. WAY-13's *Verification* clause added earlier stays and agrees.

## New findings in the fix diff

All Minor, none blocks (WAY-162), all within the task's files.

- **`project-level/plan/skill/critique_plan.md:19`, 126 columns.** The fix joined two lines ("...goes back to the human. If an independent critic cannot run, say so and wait;") without rewrapping the paragraph; the file was within 100 columns at `4e09369`. No rule of the-way fixes a width, so only polish.
- **`foundations/decisions.md` WAY-372 *Rationale*, around "one change. Naming the reason makes the proposal checkable, which a" / "bare "better" is not,"**: the edit left one short line in the middle of the paragraph. Polish.
- **`foundations/decisions.md` WAY-146 *Verification* "complies" now has a single example, and WAY-146's binding sentence names four judgments of the critique with no pair on the "whether a quoted answer settles its question" judgment.** That was already so at `4e09369` (the lost example only covered size); no change needed.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Foundation | `python -B elements/common/foundation_check.py` (worktree root) | 0 | `0 errors` |
| Tests of the part the fix touches | `python -B gate/run_tests.py project-level` (run in the background, 206 s) | 0 | 275 tests, OK |
| Removed wordings | `grep -rn -i -E "merged before the others\|size alone\|its size\|task's size\|too large\|signal to look\|more open questions\|clearly more" --include=*.md --include=*.py . --exclude-dir=.git --exclude-dir=.runs` | 0 (hits read) | no remaining wording of the critique's size test (see finding 1) |
| Line width | `awk 'length($0)>100'` over the three plan files | n/a | `critique_plan.md:19` 126 (new, Minor); `template.md` lines 83, 127-141 are long table or list lines already over 100 at the base |

A first run of `gate/run_tests.py project-level` that I started in the foreground with a 110-second `timeout` was killed at the limit; its dots included one `F` before the kill. I could not read what failed. The complete re-run, alone, passed all 275 tests, so I treat the `F` as an effect of the kill or of a time-sensitive test under load and report it as unverified, not as a failure of the fix. Not run: `gate/run_tests.py` on `agent-instructions`, `instruction-files`, `elements/common` (the author ran them; the fix touches no file of those parts) and the whole gate (the orchestrator's).

## Reaches beyond the dispatch

- `git show`/`git diff 4e09369..edf1699` for all four files; `foundations/decisions.md` WAY-146, WAY-372, WAY-13 read again whole at the head; WAY-140, WAY-143, WAY-156, WAY-215 read in the first review.
- `project-level/plan_check.py` and `project-level/test_plan_check.py`: grep for "size", "threshold": no hit, to confirm no test held a removed wording.

## Unread material

This is a review of a fix, so the dispatch gives the findings file and the fix report, both read whole, plus the author's earlier report of gaps, which concerns the author's reading, not mine. My own selection of the foundation was made in the whole-change review (131 decisions naming `decisions` or `project-level` in *Scope*: 12 read whole, 4 in part, the rest by title; invariants and part map read whole; see `whole-change-review-report.md`). For this fix I read whole: WAY-146, WAY-372, WAY-13, and re-read the two edited skill files and the template passage. Not re-read: WAY-114, WAY-113, WAY-33, WAY-19, WAY-142, WAY-144, WAY-147, WAY-214, WAY-218 (named unread in the first report; the fix touches none of what they hold). `elements/decisions/examples.md` and `elements/common/rules.md`: not read; guidelines: none exist.

## Searches not found or unclear

- A rule fixing a line width for the-way's instruction files: not found (as in the first review).
- What the `F` of the killed first run of `project-level` tests was: not determined; the full re-run passed.
- The author's report says the fix put the reason of different repositories on `derives from WAY-140`; I found it in the diff as such. Nothing missing.
