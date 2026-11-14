# Fix report: task `split-only-for-gain`

**Status:** `done`

Reviewed head `4e09369`; the fix is one commit on `task/split-only-for-gain`:

- `edf1699` — "Remove the plan critique's judgment of a task's size and bind WAY-372 to the proposer of a split".

| File | Change |
|---|---|
| `foundations/decisions.md` | WAY-146 edited in place (size judgment removed); WAY-372 (proposer bound, WAY-140 added to *Relations*, *Rationale* cleaned); WAY-13 *Rationale* sentence replaced by a pointer to WAY-372 |
| `project-level/plan/skill/critique_plan.md` | the critique no longer judges a task too large; the paragraph on the split the critique asks for is gone |
| `project-level/plan/template.md` | the passage on the plan's critique no longer names the "too large" judgment |
| `project-level/plan/skill/cut_tasks.md` | the paragraph ends with WAY-143, the reasons and "a task's size alone is no reason to cut it (WAY-372)" |

(`git diff --shortstat 4e09369 HEAD`: 4 files changed, 25 insertions, 58 deletions.)

## Finding 1 (blocking): fixed as the orchestrator's choice Q3, the reviewer's way (a)

Removed from every place that held it:

- **WAY-146**: from the binding sentences, the clause "and whether a task is too large, which it is when its goal joins two or more effects ... merged before the others", the clause "no script judges a task's size; a task the critique finds too large goes to the human as a question, with its split and the choice to keep the task, and the plan's author never splits it for its size alone"; from *Verification* "complies" the game-plan account task marked too large and the task not marked, and from "violates" "the author splits the account task for its size alone, or the critique passes it without a word on its size" and "a script counts a task's questions against a threshold"; from *Rationale* the two sentences on size and on the signal of open questions; from *Rejected* the numeric threshold for a task's size (which quoted WAY-13 for "where size is only a signal"), the script that prints each task's counts, and the author splitting a task after the critique's remark. What WAY-146 keeps is word for word: the script's checks, the critique's other four judgments, "a check a script can make is never left to the critique", the other *Verification* items, the roadmap sentence of the *Rationale* and the three other *Rejected* ways. One grammatical join was made ("and whether a quoted answer settles its question").
- **`project-level/plan/skill/critique_plan.md`**: the judgment "whether each task is too large by the test in `cut_tasks.md`" with the author handing the critic that test, and the sentence putting the critique's split to the human.
- **`project-level/plan/template.md`**: the judgment from the passage on the plan's critique.
- **`project-level/plan/skill/cut_tasks.md`**: the definition of "too large", the signal of "clearly more open questions, projected entries or In scope items", and the sentence that the critique judges size and the human settles its split.

**Removed on the orchestrator's order and to be put before the human by the request:** the signal "a task that gathers clearly more open questions, projected entries or In scope items than the rest of the plan is only a signal to look at it" is gone, from `cut_tasks.md` (the paragraph) and from WAY-146's *Rationale*, because once a split for size is ruled out the signal has no consequence. The task's accepted text names the sentence "A large task is split" only; this signal is a removal beyond the words the task names.

**Search of the repository for the carrying words** (`too large`, `size alone`, `its size`, `merged before the others`, `only a signal`, `signal to look`, `no number decides`, `checked alone`, and `task` near `large|big|size`), over all files outside `.git` and `.runs`: no hit about a task's size remains. Hits left, each not about a task's size and not touched: the slices of a change (WAY-136, WAY-371, `task-cycle/plan/too_large.md`, `slice_size.py` and their tests, `task-cycle/skill/SKILL.md`, `record_template.md`, `process-audit/audit_count.py`), the review of a change's size in `product-guidelines`, and WAY-372's own *Rejected* ("a request to merge too large for a sensible review"). No script or test of `project-level` holds a removed wording (`plan_check.py` and its tests judge no size); so no test changed. The generated skill entry points (`.claude/skills`, `.agents/skills`) hold only descriptions, which no edit touched.

**Precedence (item 3):** after the removal no entry collides with WAY-372 (searched as above: WAY-136 and WAY-371 divide a change into slices; WAY-139 and WAY-156 are compatible), so no `narrows` was written.

## Minor findings

- **2 (fixed):** WAY-372's first sentence now reads "A split of a task is proposed only where it makes the work better or cheaper; time does not count, so that a part is ready sooner is no reason", and its last sentence ends "a split the human asks for, who sees the whole document, stands without one", so the rule binds the proposer and the human's own request stays outside it.
- **3 (fixed):** the binding sentence reads "the parts change different repositories (WAY-140)", the *Rationale* reads "parts in different repositories are not one change", and WAY-372's *Relations* gain `derives from WAY-140`, which holds that an effect outside the product's repository is made only by a human. I did not use *Based on* for it: the decisions' template gives *Based on* only sources outside the product (an environment fact or a quoted source), and a decision of the log goes in *Relations*; *Based on* stays `none`. The skills (`read_sources.md`, `cut_tasks.md`) keep "since the cycle writes only in the product's repository" as instruction text; the finding concerns the entry. A judgment, flagged: if the request's reader wants a quoted source in *Based on*, none exists in the foundation for the sentence.
- **4 (no change in the files):** the finding asks for the wording of the request: rows 4 and 5 are to be named there as lines written into `resolve_gaps.md:62-64` and `:85-87`, with WAY-139 as the entry they stand beside, not the entry that states them. No file needed a change for it; my earlier report's wording "already stated by WAY-139" is too strong, and the request should not repeat it.
- **5 (fixed):** WAY-13's *Rationale* now reads "Beyond preparing and making the change size tells nothing worth deciding on, and a split for size alone has no reason of its own (WAY-372)."

## Foundation entries changed (meaning in English and Polish, with mark)

1. **WAY-146** (edited in place) — mark: `the cycle's` (it carries the accepted answer to question 5 and row 6 of the task, and it changes the meaning of WAY-146 beyond the task's *Decisions in play*; the request puts it before the human, with the passages the orchestrator names: question 5's answer and *Not chosen*, row 6, and question 2's *Not chosen* on the part that "scali się bez czekania").
   - EN: before a project plan is handed over, a script checks its form and structure and the independent critique judges only whether an end is checkable, whether an element enters early, whether a question stands where the definition puts it and whether a quoted answer settles it; no judgment of a task's size is made, and no check a script can make goes to the critique.
   - PL: przed przekazaniem planu projektu skrypt sprawdza jego formę i strukturę, a niezależna krytyka ocenia tylko, czy koniec zadania da się sprawdzić, czy element techniczny wchodzi wcześnie, czy pytanie stoi tam, gdzie je stawia definicja, i czy zacytowana odpowiedź je rozstrzyga; rozmiaru zadania nikt nie ocenia, a to, co może sprawdzić skrypt, nie idzie do krytyki.
2. **WAY-372** (edited in place after the first commit) — marks as before: `row 1`, `row 2`, `row 6`, and the silence half of `row 3`.
   - EN: a split of a task is proposed only where it makes the work better or cheaper, with one of three named reasons (a part that cannot start or finish without something outside the refinement, parts in different repositories, a split a later step of the refinement offers); an agent says nothing of a split for size alone, a split the human asks for stands without a reason, and a project plan cuts its tasks by WAY-143 and these reasons.
   - PL: podział zadania proponuje się tylko wtedy, gdy daje lepszy albo tańszy wynik, i z jednym z trzech nazwanych powodów (część nie może ruszyć albo się skończyć bez czegoś spoza doprecyzowania, części zmieniają różne repozytoria, późniejszy krok doprecyzowania proponuje podział); przy samym rozmiarze agent nic nie mówi o podziale, podział, o który prosi człowiek, nie wymaga powodu, a plan projektu tnie zadania według WAY-143 i tych powodów.
3. **WAY-13** (edited in place) — mark: `row 3`.
   - EN: a task's size may lighten how its change is prepared and made, and outside that it decides nothing; a split for size alone has no reason of its own (WAY-372).
   - PL: rozmiar zadania może odciążyć przygotowanie i wykonanie zmiany, a poza nimi niczego nie rozstrzyga; sam rozmiar nie jest powodem podziału (WAY-372).

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (after the final edit of `decisions.md`) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped by the tests themselves |
| `python -B gate/run_tests.py elements/common` | 0 | 201 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 275 tests OK |

`agent-instructions` and `instruction-files` ran before the commit on the same file content as the commit's (the later edits were rewraps in `template.md` and `critique_plan.md` only, followed by `foundation_check.py` and the two long runs, which ran on `edf1699`). Not run: the whole gate, and any directory beyond these (no test elsewhere holds a removed wording; the search above found none).

## Own-work check

- Requirement the fix most likely does not meet: every place that holds the critique's size judgment or the human's decision on a split it asks for is gone, and nothing else that is not about a task's size was removed.
- Check: the search above (`grep -rn -i -E "too large|merged before the others|critique judges size|signal to look" project-level foundations/decisions.md`, filtered for slices) and the reading of WAY-146 whole after the edit (`awk '/^### WAY-146 /{f=1} /^### WAY-147 /{f=0} f' foundations/decisions.md`); `foundation_check.py` exit 0.
- Showed: three remaining hits, all about slices (WAY-136 line 3867, WAY-371 line 12744) or WAY-372's own *Rejected* (line 12805); the rewritten WAY-146 reads whole and keeps the critique's four other judgments; no test of `project-level` held a removed wording.

## Reaches beyond the handoff

- `grep` over the whole worktree for the words above, and a read of WAY-140 whole (for the reason of different repositories) and of `task-cycle/skill/SKILL.md:70-80`. Why: finding 3 asks to rest reason 2 on an entry the log holds.
- A read of `project-level/plan/template.md:175-190` and the lines of WAY-146 to its end, and of `foundations/decisions.md` near WAY-151 (lines 4585-4600), to see whether another entry depends on the removed judgment: it derives from WAY-146 for the critique's reading of the plan, not for size; no change.

## Unread material

- The whole-change review's report `reports/whole-change-review-report.md` (the handoff names it; the findings file quotes its lines 19-53, which I read): not read.
- The same decisions of the `project-level` and `task-cycle` scopes as in my first report remain unread (see that report); I added WAY-140 and WAY-146 (read whole) to those read.

## Searches not found or unclear

- No script or test holds the removed "too large" wording of the plan critique; the invariants `project-plan-form` and `project-plan-check` were not opened, and `plan_check.py` contains no word of the removed judgment (grep over `project-level/*.py`).
- Unclear: whether the request should treat WAY-146 as an entry "written whole from an accepted row" (accepted with the task document, WAY-114) or as `the cycle's` (put before the human at the merge). The accepted task names WAY-146 in none of its sections, so I marked it `the cycle's`; the orchestrator's choice Q3 supplies the passages that give the outcome (WAY-25).

## Choices

1. Removed the plan's signal of "clearly more open questions, projected entries or In scope items" with the rest, as the handoff orders (named above).
2. Kept WAY-146's *Rejected* ways "the author checking its own plan", "checks of a plan's form across several copies" and "an agent checking what a script decides" word for word; removed the three ways that concern a task's size. Rejected: leaving the script-prints-counts way (it exists only to judge size). Cost if wrong: a way the human once refused is lost from the log; low.
3. Used *Relations* `derives from WAY-140` and left *Based on* `none` for finding 3 (reason above). Rejected: a quotation from `task-cycle/skill/SKILL.md` in *Based on*, since it is a file of the product, not a source outside it.
4. No precedence recorded: nothing collides after the removal.

## Questions

None.
