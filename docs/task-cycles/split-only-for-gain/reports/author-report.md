# Author report: task `split-only-for-gain`

**Status:** `done with concerns` (one collision with a current decision that the task does not carry; see "The collision" below, for the request to put before the human).

## Commits and files

One commit on `task/split-only-for-gain`, base `0b77f5a2e1e37d04cd58888dd1d761f8e0329bd4`:

- `4e09369` — "Split a task only for a reason that makes the work better or cheaper, and say nothing of a split for size alone".

| File | Added / removed |
|---|---|
| `foundations/decisions.md` | +60 / -5 (WAY-13 edited in place; WAY-372 added at the end of the log) |
| `project-level/task/skill/read_sources.md` | +8 / -3 |
| `project-level/task/skill/resolve_gaps.md` | +5 / -5 |
| `project-level/task/skill/orchestrated_mode.md` | +1 / -1 |
| `project-level/plan/skill/cut_tasks.md` | +7 / -3 |

Total: 5 files, 81 insertions, 17 deletions. Nothing under `.runs/` is committed or touched except this report.

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (run after WAY-372 and the WAY-13 edit; run again inside the loop below) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped (the tests' own skips: "needs the real path of a link, as on POSIX") |
| `python -B gate/run_tests.py elements/common` | 0 | 201 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 275 tests OK |
| `grep -rn -i -E "offer the human to split\|deployment-work split\|ask before offering\|signal to split\|large task is split\|name as a signal\|offering the split" . --exclude-dir=.git --exclude-dir=.runs` | 1 (no match) | none of the removed wordings stands anywhere in the repository |

Not run: the whole gate (the orchestrator runs it, handoff answer 6). The five checks ran in one loop from the worktree root; the loop's last member (`project-level`) ran in the background past the harness's foreground limit and completed with exit 0.

No test was written: the change is prose of instruction files and entries of the decision log, which the method's section 2 gives no test ("prose for people gets no test"); no invariant derives from WAY-13 or WAY-372, and no test cites either by a line `decision:`. No invariant test was changed.

## Own-work check (section 3)

- Requirement most likely not met: every wording of the old rule (a size signal, an offer to split deployment work, "ask before offering the split", "A large task is split") has gone from every file, not only the four the task names, and each new limb stands where the task puts it.
- Check: the grep above over the whole worktree, exit 1 with no output; plus `grep -c "different repositories"` on `read_sources.md` and `cut_tasks.md` (1 and 1), and `grep -rn "WAY-372"` (the decision's heading, `read_sources.md:32`, `cut_tasks.md:8`).
- Showed: no leftover of the removed wordings; the third reason and the silence on size are in `read_sources.md`; the plan's cut carries the rule of row 6. One wording that remains and is not mine: `project-level/plan/template.md:188` and `project-level/plan/skill/critique_plan.md:16-22` still carry the plan critique's test "too large" and the human's decision on a split it asks for (left as ordered; see the collision).

## Foundation entries

Each entry with its mark; one sentence of meaning in English, one in Polish.

1. **WAY-372** (new, "When is a task split into several tasks?") — marks: `row 1`, `row 2`, `row 6`, and the half of `row 3` that says the agent is silent on a task's size (the other half of row 3 is WAY-13 below).
   - EN: a task is split only where the split makes the work better or cheaper (time does not count), the proposer names one of three reasons — a part that cannot start or finish without something outside the refinement, parts in different repositories, or a split a later step of the refinement offers — an agent says nothing of a split for a task's size alone, the human may ask for one, and a project plan cuts its tasks by WAY-143 and these reasons, never by size alone.
   - PL: zadanie dzieli się tylko wtedy, gdy podział daje lepszy albo tańszy wynik (czas się nie liczy), a kto proponuje podział, nazywa jeden z trzech powodów — część nie może ruszyć albo się skończyć bez czegoś spoza doprecyzowania, części zmieniają różne repozytoria albo późniejszy krok doprecyzowania sam proponuje osobne zadanie; przy samym rozmiarze zadania agent nic nie mówi o podziale, człowiek może sam o niego poprosić, a plan projektu tnie zadania według WAY-143 i tych powodów, nigdy z samego rozmiaru.
2. **WAY-13** (edited in place) — mark: `row 3`.
   - EN: a task's size may lighten how its change is prepared and made, and outside preparing and making the change it decides nothing, so it is no signal to split the task.
   - PL: rozmiar zadania może odciążyć przygotowanie i wykonanie zmiany, a poza nimi niczego nie rozstrzyga, więc nie jest sygnałem do podziału zadania.
3. **Rows 4 and 5 — tied to WAY-139, no entry written.** Mark: `row 4`, `row 5` (no new entry carries them).
   - EN (row 4): the step on the deployment skill adds the missing work to the *To do* and offers no split, and the human may split it off, as WAY-139 already says ("or the human splits that work into a task of its own").
   - PL (wiersz 4): krok o umiejętności wdrożenia dodaje brakującą pracę do *To do* i nie proponuje jej wydzielenia, a człowiek może ją wydzielić sam, jak WAY-139 już mówi.
   - EN (row 5): where the product has no deployment skill at all, the agent asks the questions on the record's life and on a failure before the human splits the work off, so the split task carries the answer or the refusal.
   - PL (wiersz 5): gdy produkt nie ma umiejętności wdrożenia wcale, agent zadaje pytania o czas życia zapisu logów i o awarie, zanim człowiek sam wydzieli tę pracę, więc wydzielone zadanie niesie odpowiedź albo odmowę.
   - Row 5's ordering ("before the human splits it off") stands in `resolve_gaps.md` only; WAY-139 states that the check asks those questions whenever nothing answers the item, with no condition on a split, and WAY-139's *Verification* and *Rationale* name the human's split as an allowed outcome. I judged that the settlement is already stated by WAY-139 (WAY-33, WAY-134) and wrote no second entry. If the request's reviewer reads the ordering as an unstated half, the cost is one more sentence in WAY-139; I did not edit WAY-139 (handoff answer 4).

Rows 1, 2 and 6 as one entry: the decisions' template allows it because rows 1, 2 and 6 answer one question (what justifies a split); *Rejected* holds the ways not chosen that the sources of questions 1, 2, 3 and 5 keep, each with its cost, none derived by me.

The search of the whole foundation (WAY-33) was one grep of `foundations/decisions.md`, `invariants.md`, `glossary.md`, `part_map.md` and `environment_facts.md` for `split`, `too large`, `size alone`, `its size`, `large task`, `oversiz`, `task of its own` and the like, then each hit's entry read: WAY-13, WAY-136, WAY-139, WAY-143, WAY-146 whole; WAY-154, WAY-156, WAY-161, WAY-218, WAY-302 and WAY-371 at the passage found. Findings: WAY-139 states rows 4 and 5 (tied above); WAY-136 and WAY-371 concern the slices of a change, not tasks, and need no change; WAY-156's "in-scope task split" is the project orchestrator's routing of a plan change, compatible; the one collision is WAY-146 (below). No glossary word was found used in another meaning, and nothing the change brings is awaited by a template, the part map or a script.

## The collision (for the request to put before the human)

WAY-146 and the plan's critique still hold the test "a task is too large when its goal joins two or more effects that can each be checked alone in the running product and merged before the others", and the human decides on any split the critique asks for. After this change two statements stand together:

- WAY-13 and WAY-372: a task's size decides nothing outside preparing and making the change, and a project plan cuts its tasks by WAY-143 and the three reasons, never by size alone.
- WAY-146 (binding sentences, *Verification* "complies" example of the game plan whose account task is marked too large, and *Rejected* "where size is only a signal (WAY-13)") and `project-level/plan/skill/critique_plan.md:16-22`, `project-level/plan/template.md:188`: the critique judges whether a task is too large by that test and the split goes to the human as a question.

Where it stands in the files I edited: `project-level/plan/skill/cut_tasks.md` now says a task's size alone is no reason to cut it (my sentence, per handoff answer 1), and the next sentence, kept as ordered, still says "A task is too large when its goal joins two or more effects, each of which can be checked alone in the running product and merged before the others", followed by the kept sentences on the signal of open questions and on the author never splitting for size alone. The definition of "too large" therefore stands in that file with no consequence of its own left in the same paragraph; the consequence stands in `critique_plan.md` and WAY-146. A reading under which the two stand together exists (the test names two independent effects, not a size), and then WAY-146's critique is a fourth reason to cut that WAY-372 does not list; the other reading is that the critique's test is size by another name and should go. The human has to choose between: keep the test and name it as a fourth reason in WAY-372 (a change of meaning of row 2, which the task does not carry), or remove the test from WAY-146, `critique_plan.md` and `plan/template.md` (a change of meaning of WAY-146 beyond what the task carries, WAY-30, WAY-114). Left as it is, the plan critique goes on asking the human about splits that WAY-372 says size alone does not justify, and WAY-146's *Rejected* quotes WAY-13 for "where size is only a signal", which WAY-13 no longer says. I recorded no precedence (no `narrows`), as the orchestrator ordered, and edited neither WAY-146 nor `critique_plan.md` nor `template.md`.

## Reaches beyond the dispatch (section 1)

- The decision log's `grep` for the words of the split (the WAY-33 search above), over all five foundation files, and the reads of WAY-136, WAY-154 (passage), WAY-156, WAY-161 (passage), WAY-218 (passage) it found. Why: the search of the whole foundation is the foundation step's own; WAY-136 and WAY-371 had to be judged as not about tasks.
- `grep -rn -i "split|too large|large task"` over `project-level`, `elements`, `product-guidelines`, `installation`, `foundation-review`, `process-audit`, `agent-instructions/README.md`, `README.md`, to find any other file carrying the old rule; found `project-level/lead/skill/route_changes.md:7` and `project-level/task/skill/project_plan_task.md:10` (a plan change's routing, compatible, not edited) and the two plan files named in the collision.
- `elements/decisions/template.md`, `skill/SKILL.md`, `read.md`, `decide_entry.md`, `examples.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`: read whole, as the foundation step and the decisions' skill name them.
- A script (Python, in a heredoc) that counted the decisions whose *Scope* names `project-level` or `task-cycle` (180 entries, 7 648 lines), to decide what to read (see Unread material).
- Withdrawn numbers of the log, to take the next free number: WAY-372 (highest entry WAY-371; highest withdrawn WAY-224).

## Unread material

- The decisions whose *Scope* names `project-level` or `task-cycle`, which the handoff asks to read whole: 180 entries of 7 648 lines. I did not read them all; reading them whole would have filled the context of a change of four small files. Read whole: WAY-13, WAY-30, WAY-33, WAY-136, WAY-139, WAY-143, WAY-146 (to the end of its *Rejected*), WAY-156. Read in part: WAY-113 whole; WAY-114 and WAY-134 to the middle of their *Rationale*; WAY-150 to its *Verification*; WAY-154, WAY-161, WAY-218, WAY-302, WAY-371 at the passage a search found. The other decisions of those scopes are unread. The risk: a decision of those scopes that states or contradicts rows 1 to 6 without using any word of my search (`split`, `too large`, `size alone`, `its size`, `large task`, `oversiz`, `task of its own`) would be missed.
- The invariants whose *Part* names `project-level`, `task-cycle` or `every`: not read; searched `invariants.md` for the same words and for `split`, no hit. `project-plan-check` and `project-plan-form` (named by WAY-143 and WAY-146) were not opened; no test or script of `project-level` contains the removed wordings (the grep above).
- `elements/decisions/examples.md` names WAY-03; not read (I wrote the entry from the template and from WAY-136, WAY-139, WAY-146, WAY-371 as neighbours).
- Files of the task I did not read for their own sake: `project-level/plan/template.md` (only line 188 and its neighbours by grep, as the handoff asks "the passage on the plan's critique"); `project-level/task/skill/project_plan_task.md` and `project-level/lead/skill/route_changes.md` (the hit lines only).
- Read whole: the handoff, `task-cycle/change/SKILL.md`, `task-cycle/skill/foundation_step.md`, the frozen task document, `foundations/glossary.md`, `foundations/part_map.md`, the four files edited, `critique_plan.md`.

## Searches not found or unclear

- The orchestrator's handoff says the commits `0ed5ad7` and `4e3c4cf` changed `cut_tasks.md`; both are ancestors of the base, and the wording found matches the handoff word for word. Nothing missing.
- Row 6's source (question 5 of the task) says the plan's cut loses "A large task is split". That sentence no longer stands in `cut_tasks.md`; what stood was "A task too large is put to the human to split, and its size chooses nothing else (WAY-13)", which I replaced as ordered. Unclear: the task's item 7 and its Question 5 assume the plan has no other split rule; WAY-146 and the critique's test contradict that (see the collision).
- The task's item 4 says the sentence "offer the human to split it into a task of its own" stands "around line 63" and item 5's point "around line 85": both found at lines 63 and 85. The paragraph of `read_sources.md` is at line 28, as the task says.
- `foundation_check.py` has no check on a decision's *Rejected* or on the wording "WAY-13" in another entry; so the stale reference in WAY-146's *Rejected* is not reported by it.

## Choices (with the way rejected and its cost if wrong)

1. **One new decision (WAY-372) for rows 1, 2, 6 and the silence half of row 3**, WAY-13 edited for the other half of row 3. Rejected: two or three separate decisions (reasons / size / plan's cut) — they answer one question ("what justifies a split"), WAY-19 asks one entry for one question; and putting the agent's silence into WAY-13 — it would give WAY-13 a second question (how an agent behaves at refinement) that can change on its own. Cost if wrong: a later change to the plan's cut cannot be edited without touching the entry of the refinement's reasons; low.
2. **Rows 4 and 5 tied to WAY-139, no entry.** Rejected: a decision for row 5's ordering — it is an instruction for one skill (`resolve_gaps.md`) with no choice of real cost, so the-way's log question 1 sends it to the skill; and a sentence in WAY-139 (handoff answer 4 says it stays). Cost if wrong: the ordering "before the human splits it off" is held by one skill file with no entry or test; a later edit of that skill could drop it unnoticed.
3. **Item 7's reasons stated in `cut_tasks.md` in full (three reasons, in plain words), not by a reference to the refinement.** Rejected: "the reasons of the refinement's one-task check" with no list — the plan's author does not read `read_sources.md` and cannot name a reason it does not see. Cost if wrong: the list is in two skill files and one decision; a change of a reason has three places to edit (WAY-372 names it).
4. **The reason "a later step of the refinement offers a separate task" is kept in `cut_tasks.md`** though a plan's author may find it hard to apply; row 6 says "the reasons of row 2", all three. Rejected: dropping it from the plan's cut — it would give the plan's cut a shorter list than row 2 with no row saying so.
5. **Sentence added to `read_sources.md`: "the human sees the whole document and may ask for a split".** It stands in the settlement's source (question 3, "Mariusz widzi cały dokument przy akceptacji i może sam poprosić o podział") and not in the rows' text; I wrote it into both the skill and WAY-372's binding sentences. Rejected: leaving it out of the entry — then the silence on size could be read as forbidding the human's own request. Cost if wrong: one sentence to delete from two places.
6. **WAY-13's *Verification* "violates" gained one clause** ("a large task is treated as a reason to split it, or to lighten its checks, because of its size") and its *Rationale* one sentence, to keep both true to the new wording, as the handoff asks. Rejected: leaving *Verification* untouched — its "violates" examples would not have covered the new limb.
7. **`resolve_gaps.md` line 77 ("or the human splits it off") left as it stands**: it names the human's own split, matches WAY-139 and offers nothing.
8. **No file was moved or extracted** (WAY-365 does not apply: the-way's product guidelines hold no rule of size; no code changed).

## Problems as observed

- WAY-146's *Rejected* reads "... each false alarm forces a split, a whole cycle, or a mechanism of exceptions, where size is only a signal (WAY-13)". WAY-13 no longer says size is a signal; the reference is stale after this change (observed by reading line ~4390 of `foundations/decisions.md` against the new WAY-13; `foundation_check.py` does not report it). I did not edit WAY-146.
- `project-level/plan/skill/cut_tasks.md` before my edit already held one line over 100 columns (the old line 5); I rewrapped the paragraph I edited, so the new lines are within 100 columns. No test or check reported a length.
- The `PreToolUse` hook of the harness stopped two of my shell calls once each (rules file shown once per session) and I repeated them; no effect on the change.

## Questions

None for the author's own work; the collision above is the one matter for the human, put by the request.
