# Author report — task `project-closure-step`

**Status:** done with concerns (see "Choices": a case the task leaves open and a collision with WAY-154
whose precedence I recorded).

Worktree `the task's worktree`, branch `task/project-closure-step`, base
`cb5feab98c697354ae79a8f559b950fbf10d0030`. Author address of the commits checked with
`git log --format='%h %ae'`: the private address, as the user's git configuration gives for the
repository's account.

## Commits

| Commit | What |
|---|---|
| `6fa4bef8` | `plan_check.py` and `plan_state.py` with their tests: the closed state of the `Status:` line |
| `f7ddbadd` | the closing step (`project-level/lead/skill/closure.md`), the lead skill, the plan template, `existing_plan.md`, regenerated entry points |
| `029bc875` | the foundation entries: WAY-142 edited, WAY-411 to WAY-415, `project-plan-check`, the part map |
| `a90023e6` | the scripts the lead skill and the closing file name written by their paths (a dead-pointer finding of the test of `product-guidelines`) |
| `95d42e9a` | fix of the review, tests: no Git read for a closed plan, the first `Status:` line decides, the comment, the reader's help text |
| `836be8a0` | fix of the review: `SKILL.md`, `closure.md`, the plan template, `task_line.md`, regenerated entry points |
| `d4cfe710` | fix of the review: WAY-414, WAY-415, WAY-411 to WAY-413 (word "dropped"), the part map |
| `ee85f143` | `closure.md` section 2: the two cases of the orchestrator's answer on which projected entries go with a withdrawn task |

## Files changed (added / removed lines, `git diff --numstat cb5feab9..HEAD`)

| File | Added | Removed |
|---|---|---|
| `project-level/plan_check.py` | 66 | 11 |
| `project-level/plan_state.py` | 15 | 9 |
| `project-level/test_plan_check.py` | 85 | 0 |
| `project-level/test_plan_state.py` | 42 | 0 |
| `project-level/lead/skill/closure.md` (new) | 133 | 0 |
| `project-level/lead/skill/SKILL.md` | 16 | 11 |
| `project-level/plan/template.md` | 14 | 2 |
| `project-level/plan/skill/existing_plan.md` | 3 | 3 |
| `.claude/skills/the-way-lead-project/SKILL.md` (generated) | 1 | 1 |
| `.agents/skills/the-way-lead-project/SKILL.md` (generated) | 1 | 1 |
| `foundations/decisions.md` | 167 | 5 |
| `foundations/invariants.md` | 5 | 3 |
| `foundations/part_map.md` | 2 | 1 |

13 files, 550 insertions, 47 deletions in all.

## What was made

- `project-level/plan_check.py`: `STATUS` reads `closed YYYY-MM-DD`; the date of a `closed` line must be a
  calendar date; a second `Status:` line is a `form` finding; new `closed_date(preamble)` and
  `check_closed(tasks)`; in a plan whose first `Status:` line reads `closed …` each row that is none of
  `done`, `done — goal delivered in task <n>` and `dropped — approved by human`, and each row whose goal is
  delivered in a task that is `dropped — approved by human`, is a finding of the new condition `closed`,
  reported at the row. The docstring lists the new condition and form.
- `project-level/plan_state.py`: `sources` returns the closing date as a fourth value; a plan whose single
  `Status:` line reads `closed YYYY-MM-DD` and that passes the plan check prints
  `closed: the plan was closed on <date>; its tasks stand in final states` and exits 0 with no Git
  observation; every other plan keeps its earlier findings, the handed-over finding included. The docstring
  gives the new exit-0 case.
- `project-level/lead/skill/closure.md` (new): section 1 the condition of start; 2 what the closing item and the
  moves are made of (counts, scope not delivered, what goes with a withdrawn task, the search of the foundation
  at a commit); 3 the three places; 4 what travels; 5 the closing item (form); 6 the preview and the
  acceptance; 7 writing, in order, and the checks; 8 what the closing leaves as it is (the definition).
- `project-level/lead/skill/SKILL.md`: the `description` and the opening no longer exclude the closing; step 0
  stops on a closed plan; step 1's last bullet names `closure.md` with its condition (WAY-256, WAY-265) in
  place of the old stop.
- `project-level/plan/template.md`: the header bullet gives `closed YYYY-MM-DD`, "stands once", the closing step;
  the states passage gives what a closed plan holds; the Change log passage names the closing item; "What the
  check decides" gives the check of a closed plan.
- `project-level/plan/skill/existing_plan.md`: "a plan handed over, or closed, changes only as its change log
  records".
- Foundation: see "Foundation entries".

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Failing run of the new tests before the code (the two scripts restored to the base, the tests of the change in place) | `python -B gate/run_tests.py project-level` | 1 (16 failing subtests in 9 tests: the new `Closed` tests of `test_plan_check.py` and the three new tests of `test_plan_state.py`; log `reports/project-level-before.log`) |
| Same tests with the code | `python -B gate/run_tests.py project-level` | 0 (log `reports/after-project-level.log`) |
| Tests of the directory of the generated entry points and of the sizes, formatter and linter invariants | `python -B gate/run_tests.py agent-instructions` | 0 (52 tests, rerun after the last commit's entry-point check) |
| Dead pointers of the skills | `python -B gate/run_tests.py product-guidelines` | first run 1 (three bare script names in the lead skill and the closing file), after commit `a90023e6` 0 |
| Tracked private paths | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 |
| Foundation check, whole (no `--skip-test-citations`) | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Foundation tests | `python -B -m unittest discover -s elements/common -p "test_foundation_check.py"` | 0 (206 tests) |
| Entry points current | `python -B agent-instructions/skill_entry_points.py --write` then rerun | 0, `entry points are current` |
| Formatter and linter on the changed scripts | `ruff format --check`, `ruff check` on `project-level/*.py` (Ruff of the main checkout's `.runs/quality-venv`, not run as a gate command; the gate's `agent-instructions` run holds the standing tests of the same rules) | 0, 0 |

After the change of choice 6 (commit `ee85f143`, `closure.md` only): `python -B gate/run_tests.py project-level` exit 0
(log `reports/after-project-level-correction.log`), `python -B gate/run_tests.py product-guidelines` exit 0,
`python -B elements/common/foundation_check.py` exit 0, `python -B agent-instructions/skill_entry_points.py --write`
reported `entry points are current`.

Not run: the whole gate (`python -B gate/run_tests.py`), by the handoff; `task-cycle`, `installation`,
`instruction-files`, `process-audit` as directories (no file of them changed; the two tests that read the
whole tracked tree and the foundation were run apart as above).

The invariant tests I wrote that cite `project-plan-check` and `project-plan-form` are the tests of class
`Closed` and the closed-status tests of class `Header` in `project-level/test_plan_check.py`. Each was seen
failing once in the before run above (the code of the base, with the tests of the change) and passing with the code.

## Own-work check (section 3 of `make-change`; trust boundary: yes)

Requirement most likely not met: *a closed plan with a row in another state, or a `done — goal delivered in task
<n>` row pointing at a dropped task, is reported, and a status line a crafted file can bend is never read as
closed by the reader that skips Git.* The check is the tests of the two files above plus a set of crafted inputs I
ran through `plan_check.check` in a working script (removed, below):

| Crafted input | Result |
|---|---|
| `Status: closed 2026-11-19`, every row final | no finding (also with CRLF line endings) |
| the same, the first row `in cycle` | one finding `closed` at that row |
| the same, the first row dropped and the second `done — goal delivered in task 1` | one finding `closed` at the second row |
| `done — goal delivered in task 9` (not held) or in the task itself, in a closed plan | `form` only, no second finding |
| the same pointing at a dropped task in a plan `handed over` | no finding (the check is for closed plans only) |
| `Status: closed 2026-13-45`, `closed 2026-02-30` | `form` (no calendar date) |
| `closed` written with Arabic-Indic digits, `Status:closed 2026-11-19`, `Status: Closed …`, `closed 2026-11-19 early`, `closed` alone | `form` |
| `Status: closed 2026-11-19` twice, or `closed` then `handed over` and the reverse | `form` at the second line |
| `Status: closed 2026-11-19` with trailing spaces and a tab, a closed plan with a row `in cycle` | still a closed plan: the one `closed` finding |
| a state off the list (`blocked`) in a closed plan | `form` and `closed` |

Through `plan_state.py` (git test, the real script as a process): a closed plan with every row done exits 0 and
says it is closed (also with trailing spaces after the date); a closed plan with a row `ready for cycle`,
`in cycle` or `to refine` exits 1 with `fail: closed`; a closed line off its form, a doubled one and a lower-case
variant exit 1; a draft or handed-over plan keeps its earlier findings. What I did not try: a closed plan whose
second `Status:` line stands below the first section (it is no header line; the plan check's rule about sections
decides it), and a very large plan.

One characteristic I left and name: `str.rstrip()` strips a no-break space as well, so
`Status: closed 2026-11-19` followed by a no-break space reads as closed. The handed-over line has always read so;
I did not change it.

Mutations in my head that a test catches: `check_closed` skipping the dropped-target branch (test of the delivered
row), skipping rows in `to refine` or `waiting for human` (test over four states), applying to all plans (test
`..._in_a_plan_not_closed_are_no_finding`), `closed_date` reading the second line, or not stripping trailing
spaces (second-line test, trailing-spaces test), `plan_state` printing closed for a plan with a finding (the
closed-with-a-row-in-another-state test), `plan_state` reading Git for a closed plan (not asserted: the
output of a closed plan is asserted for the closed line and the absence of proposals only).

## Walk through the running product

The change alters what two commands print and exit with, and a skill's step. The foundation of the-way settles no
agent's way to a running product for the-way itself, so the walk of `walkthrough.md` is not performed. In its
place I ran the two commands as a user does: `plan_check.py` on a closed plan whose every row is final (output
`plan: nothing found`, exit 0) and on the same plan with the first row dropped and the second delivered in it
(one `fail: closed` line for the second row, `plan: 1 finding(s)`, exit 1); `plan_state.py` is exercised as a
process, against real temporary Git repositories, by the new tests. The wording of a skill is tested by no
test (testing guidelines, "Not tested on purpose").

## Foundation entries (the foundation step; one sentence in English and one in Polish for each)

| Entry | Marker | Meaning, English | Znaczenie, po polsku |
|---|---|---|---|
| WAY-411 — Where does the closing of a project stand in the process? | row 1, with a pair added (see `the cycle's` below) | The closing of a project is a step of the skill that leads the plan, in a file beside it that the skill names, not a skill of its own. | Zamknięcie projektu jest krokiem skilla prowadzącego plan, opisanym w pliku obok niego, który skill wskazuje, a nie osobnym skillem. |
| WAY-412 — Where can a task withdrawn from a project go when the project is closed? | row 2, with a pair added | The human picks, for each withdrawn task, the next project's note, a task of its own or dropped for good with a reason, and the closing itself writes the move with the goal, the plan's questions and the entry the task did not write. | Człowiek wybiera dla każdego zadania wycofanego notatkę następnego projektu, samodzielne zadanie albo porzucenie z powodem, a zamknięcie samo zapisuje przeniesienie z celem, pytaniami planu i wpisem, którego zadanie nie zapisało. |
| WAY-413 — When does the closing of a project write anything? | row 3, with a pair added | The closing first shows the human the closing item, the `Status:` change and the full text of each move, and writes only after the human accepts it. | Zamknięcie najpierw pokazuje człowiekowi wpis zamknięcia, zmianę `Status:` i pełny tekst każdego przeniesienia i zapisuje dopiero po jego akceptacji. |
| `project-plan-check` (invariant, extended) | row 4 | The plan check rejects a closed plan with a task in a state other than done, delivered by another task or dropped, or with a goal delivered by a dropped task. | Kontrola planu zgłasza plan zamknięty, w którym zadanie stoi w innym stanie niż zrobione, dostarczone w innym zadaniu albo wycofane, albo w którym cel dostarcza zadanie wycofane. |
| WAY-414 — How does the closing of a project learn whether the entry a withdrawn task was to write is in the foundation? | row 5, with a pair added | The closing searches the foundation at a named commit by the entry's question and writes "absent" or the entry found, partial included, and puts a doubtful hit to the human in the preview. | Zamknięcie szuka wpisu w fundamencie na wskazanym commicie po pytaniu wpisu i pisze „brak” albo znaleziony wpis, także częściowy, a niepewne trafienie stawia człowiekowi w podglądzie. |
| WAY-415 — What does a withdrawn task become when the closing of a project makes it a task of its own? | row 6, with a pair and a paragraph of precedence added | A withdrawn task made a task of its own gets a `refining` document in the full template layout with `source only`, and the closing neither doubles its existing line nor a section already standing in the next project's note. | Zadanie wycofane, które staje się samodzielnym zadaniem, dostaje dokument `refining` w pełnym układzie szablonu z `source only`, a zamknięcie nie dubluje ani jego istniejącej linii, ani sekcji już stojącej w notatce następnego projektu. |
| WAY-142 (edited in place: first sentence, *Verification* names `project-plan-check`, *Rationale* and *Rejected* each one sentence longer) | the cycle's | The `Status:` line of a plan also says that the plan was closed once each task is done, delivered in another task or dropped. | Linia `Status:` planu mówi też, że plan został zamknięty, gdy każde zadanie jest zrobione, dostarczone w innym albo wycofane. |
| Part map, part `project-level` (description names the closing of a project) | the cycle's | The part `project-level` also answers for the closing of a project. | Część `project-level` odpowiada też za zamknięcie projektu. |

Where they stand: WAY-411 to WAY-415 at the end of the section `## Project plan` of `foundations/decisions.md`
(next free numbers: the greatest number on the base was 410, withdrawn ones counted). `*Rejected*` of each
decision from a row is the ways the row's source question keeps under *Not chosen* (rows 1, 2, 3, 5, 6); the
invariant has none. Each decision has `Based on: none`, `Origin: none`.

**`the cycle's` parts to put before the human (WAY-114).** The pairs of examples I added, which the check of the
foundation requires for a decision that no invariant and no test holds, word for word (the closing item was
"closing entry" in no committed text; I use "closing item" for the item of the plan's change log, so that it is no
"entry" of the foundation):

- WAY-411 — complies: the skill that leads the plan names, at the step that reconciles progress, the file that
  describes the closing and says when it is read, and that file holds the whole closing; violates: the closing is
  given a skill of its own, with an entry point and a description, while it only reads the plan, writes an item of
  its log and moves the tasks the human withdrew.
- WAY-412 — complies: a task withdrawn from the project goes, by the human's choice, into a section of the note of
  the next project that already stands, with its goal, its questions of the plan and the entry it was to write, and
  the closing item says where it went; another goes to a task of its own; a third is dropped for good with the
  human's reason in the closing item; violates: the closing writes in the plan only where a task went and leaves
  the move of its questions and its entry to the human; the closing makes a new file for the next project while a
  note of it already stands; a withdrawn task is left in the log with no place.
- WAY-413 — complies: the closing shows the closing item, the new `Status:` line and the full text of a section for
  the note of the next project and of a task document, the human accepts them, and only then does the closing write;
  violates: the closing writes a section into the note of the next project as soon as the human has named the note;
  the closing shows the closing item and not the text of the moves.
- WAY-414 — complies: the closing finds at the commit it names a decision whose heading holds the question of a
  withdrawn task's entry, written by another task for part of the entry, names it and says it is partial; for an
  entry it finds nowhere it writes that the entry is absent at that commit; violates: the closing writes that an
  entry is absent because the task that was to write it was withdrawn, without a search; the closing takes a
  decision whose sentence resembles the entry's for the entry and writes nothing for the human to see.
- WAY-415 — complies: the closing makes for a withdrawn task a document in the state `refining` with the full
  layout of the template and `Project relation: source only: <the definition>`, leaves the line the task already
  has, and completes the section about it that the note of the next project holds; violates: the closing makes the
  document `Project relation: independent`; the closing adds a second line for a task that has one, or a second
  section for a task whose section the note of the next project already holds; the closing rewrites the body of a
  document a refiner has taken up.

**Precedence recorded (WAY-25).** WAY-415 `narrows WAY-154` and its second paragraph states the area: where the
project orchestrator writes the body of the first document of a withdrawn task and the line the task lacks, WAY-415
prevails; from the first refinement on, WAY-154 governs. WAY-154 gives the body of a task document to a refiner and
`project-level/task_line.md` gives the making of a line to a refiner. The passages of what the human accepted that
give the outcome (the task's *To do* 3, second bullet, and *Questions to settle*, the question on how a withdrawn
task becomes a task of its own): "w miejscu zadań zamknięcie zakłada dokument zadania w stanie `refining`, w pełnym
układzie `project-level/task/template.md`, z `Project relation: source only: <definicja>`; istniejąca linia zadania
zostaje, a zamknięcie zmienia w niej tylko to, na co pozwalają reguły miejsca zadań, nową linię według
`project-level/task_line.md` zakłada tylko wtedy, gdy zadanie żadnej nie ma", and the answer "Pełny układ szablonu
zadania i `Project relation: source only: <definicja>`; istniejąca linia zadania zostaje […], nowa linia tylko, gdy
zadanie żadnej nie ma." The paragraph is an addition to row 6, so WAY-415 is `the cycle's` and puts the paragraph
before the human.

**WAY-33 search** (the whole foundation once): found WAY-154 (above); WAY-140 (a task's effect outside the
repository is a human's): the closing is no task cycle, writes only after the human accepts the text, so I wrote no
precedence and name it here; WAY-153, WAY-269 (what the lead skill does at a session start and on the human's word):
unchanged, the closing is added beside; WAY-146's title says "before a project plan is handed over" while the
closed-plan check runs after it: I left WAY-146 as the task did not name it. No glossary term is needed. The
return step is the same compare, made in this change: WAY-142, WAY-411 to WAY-415, `project-plan-check`,
`project-plan-form` (its sentence reads the closed form through the template; unchanged), the part map and the
files named above.

## Each reach beyond the dispatch

- `project-level/plan/skill/existing_plan.md` (+`closed` in one clause): the plan skill's treatment of an existing
  plan reaches a closed plan the new state makes; changed because it would otherwise leave a closed plan outside
  "changes only as its change log records".
- Decisions WAY-107, WAY-124, WAY-153, WAY-154, WAY-269, WAY-114, WAY-320, WAY-308/309 (the last four by index
  heading, then the passages found by a search for "lead-project" and "project orchestrator") read whole: to see
  whether the closing collides with them. Found WAY-154 only.
- `elements/decisions/skill/*.md`, `elements/invariants/skill/*.md`, `elements/part-map/skill/*.md` (the skills of
  the elements I wrote entries by), their templates and `elements/common/rules.md`, `way_of_working.md`: as
  `foundation_step.md` gives.
- `project-level/definition_template.md` (section "Projected foundation changes", headings by kind): to word the
  search of the foundation by heading in `closure.md`.
- `project-level/readiness_check.py` (`items`, `NESTED_ITEM`): to check that a closing item with nested lines still
  reads as one dated item of the change log.
- `task-cycle/change/walkthrough.md`: to decide the walk.

## Choices (the way rejected, and its cost if wrong)

1. **The closing step is `project-level/lead/skill/closure.md`.** Rejected: a section of `SKILL.md` (WAY-256: a step
   that only some uses reach stands in a file); a name `close_project.md`. Cost if wrong: a rename.
2. **The new condition of the plan check is named `closed`.** Rejected: `form` (the check would not separate the
   state of rows from the form of the file), `order`. Cost: a rename and the tests.
3. **`plan_state.py` on a closed plan: exit 0, one line, no Git observation.** Rejected: observing Git as for a
   handed-over plan (a closed plan has nothing to propose and the skill stops), and exit 1 with a finding (the task
   asks for a plain statement, not an error). Cost if wrong: a closed plan whose done task has a conflicting trace
   in Git is not shown; the closing itself reads the integration commit before it closes.
4. **A second `Status:` line is a finding of `form` in `plan_check.py`.** The task does not say it; I added it so that
   a closed marker and a handed-over marker never stand together, and so that the check and the reader agree (the
   reader accepted only one line, the check the first). Rejected: leaving `plan_check.py` to read the first line
   alone, which would let a closed plan with a second line pass the check while the reader refused it. Cost: a plan
   that has two `Status:` lines, which no template form gives, fails the check where before it passed.
5. **"closing item", not "closing entry", for the item the closing adds to the plan's change log.** The task and the
   handoff say "entry". Rejected: "entry", which the glossary gives for the text of the foundation. Cost: a reader
   who knows the word of the task meets another; one rename.
6. **Which projected entries go with a withdrawn task (closure.md, section 2).** First written as the task's words
   read literally; changed after the orchestrator's answer (an autonomous choice of the cycle, not the human's
   approval): an entry goes with a withdrawn task in case (a), its `Written by` cell names a withdrawn task (it goes
   with that task, even where a finished task also realizes it, the WAY-126 partial case, which the search of the
   foundation then reports partial or absent), or case (b), every task of its `Realized by` cell is withdrawn and
   `Written by` names no withdrawn task (it goes with the withdrawn tasks of `Realized by`). Rejected: my literal
   reading, which let an entry a withdrawn task was to write fall out with no task. Cost if wrong: one more line
   in a closing item. Note: the plan check requires the writing task to be among the realizing ones, so case (b)
   never adds an entry beyond case (a); I wrote it as given. WAY-412 and the pairs of examples do not restate the
   rule and are unchanged.
7. **The closing starts by telling the human that every row is final and goes on to read; it writes nothing before
   the acceptance of the preview.** The task says the closing "starts only when" every row is final and does not say
   whether the human first says go. Rejected: waiting for the human's word before reading (one more turn, and the
   preview is the human's act anyway). Cost if wrong: the human sees a preview they did not ask for.
8. **The foundation is searched at the commit of `integration: <ref> <commit>`, printed by `plan_state.py` in the same
   session, and by `git`, not in the working tree.** The task says "na wskazanym commicie". Rejected: the working
   tree, the head of a branch the agent names. Cost: where the line is absent the human is asked for the commit.
9. **A task document the plan's `Document` cell already links for a withdrawn task is left as it is and a new
   document is made beside it.** The task is silent; I stayed with "no change to what exists" and named it
   (see "Searches"). Cost if wrong: two documents for one task.
10. **The closing item's form (head line plus four nested items).** The task gives its content, not its form. Rejected:
    one long line; a table. Cost: the form changes, nothing else reads it.
11. **The regular expression of the new status** reads `closed ` and a date of ASCII digits in the same alternation as
    `handed over`; the date is then checked with `datetime.date.fromisoformat` as before. Rejected: a separate
    pattern for the closed line. Cost: none.
12. **WAY-415 `narrows` WAY-154**, recorded, not asked (see "Precedence recorded").
13. **No move out first (WAY-365).** No function or file this change adds to stands over its threshold: `plan_check.py`
    went from 986 to 1041 lines (threshold 1200), `plan_state.py` from 703 to 709, the longest function I touched is
    `read_tasks` (not changed) and `sources`/`check` stay under 40 lines; the size test of the invariant
    `function-and-file-size` passed in the `agent-instructions` run. Rejected: a move out of `plan_check.py` for its
    own sake.

## Problems as observed

- Choice 6 was a literal reading that left a projected entry realized by a finished task and written by a withdrawn
  one with no task. Corrected as the orchestrator answered; see choice 6.
- The console prints `—` in a `fail:` line as a replacement character on this machine (code page); it does so for
  every finding of the script before my change as well.
- The first run of `product-guidelines` failed on three bare script names in the lead skill and the closing file
  (a pointer to `plan_check.py` must name its path); fixed in `a90023e6`, rerun green.
- Both `project-level` runs, the before and the after, took about 140 seconds.

## Unread material

none. (The handoff's decisions WAY-142, 145, 146, 118, 153, 107, 143, 147, 230, 126, 134, 140, 256, 265, 344, 385,
379, 380, 382 and the invariants it names that I changed or went near — `project-plan-form`, `project-plan-check`,
`project-plan-state-evidence`, `project-plan-state-subprocesses`, `project-readiness-check`, `skill-entry-points`,
`foundation-change-merge-route`, `return-step-record`, `script-language`, `script-imports`, `script-subprocesses` —
were read whole, each decision with its *Rejected*; `ruff-blocking-rules`, `formatter-layout` and
`function-and-file-size` were read by their decisions WAY-380, WAY-382 and WAY-385 and held by the `agent-instructions`
run. The index of the decisions by the part `project-level` was written and read by heading, and the decisions
that bear on the work were opened whole as listed above.)

## Searches not found or unclear

- Where a withdrawn task already has a task document (the plan's `Document` cell links one, with `Status:
  dropped — approved by human`): the task settles the line (stays) and the section (completed), not the document.
  I left it as it is (choice 9) and did not search further.
- Whether the closing "starts" on its own or on the human's word: not stated (choice 7).
- The word "entry" of the task for the closing's item in the change log: the glossary gives "entry" a meaning of its
  own (choice 5).
- `task-cycle/skill/plan_member.md` and `project-level/task/skill/project_plan_task.md` name the plan's check and
  states; neither reads the `Status:` line, so I changed neither. `installation/README.md` names the lead skill by
  name only. `process-audit` and `agent-instructions` hold no reader of the plan's `Status:` line (searched for
  `handed over`, `Status:`, `plan_check`, `plan_state`, `closure`, `lead-project`).
- No find-by-name tool outside the repository was needed; the task's notes of `loop2` were not read, as the handoff
  says.

## Working copies

Made: `.runs/author/` in the worktree (copies of the two scripts for the before run, a script of crafted inputs, a
plan and a definition for the command-line run, the index of decisions, a draft of the new decisions, the logs).
Removed: the directory `.runs/author/` was deleted whole and made again empty before I returned. Kept in `reports/`
beside this report: `project-level-before.log`, `after-project-level.log`, `after-agent-instructions.log`,
`after-product-guidelines.log`. No worktree or clone was made. No remainder.


# Fix of the review of the whole change (head reviewed `ee85f143`; commits `95d42e9a`, `836be8a0`, `d4cfe710`)

Variant: the fix of a review's findings. Findings file: `reports/review-whole-fix-findings.md`, read whole. Fixed:
I1 to I5 and Minor 1 to 9; Minor 10 is not mine.

| Finding | What I did |
|---|---|
| I1 | The last bullet of step 1 of `SKILL.md` now tells the human which row holds the closing, by number and name, and in which state (or in which dropped task); `closure.md` section 1 keeps the same sentence. |
| I2 (orchestrator's choice) | A row `done — goal delivered in task <n>` whose task n is dropped holds the closing as a row in another state does, before any preview and reconciled with the human; `SKILL.md` step 1 and `closure.md` section 1 say so. |
| I3 | `closure.md` section 2 compares the text of what the search finds with the projected change; a new result: an entry stands under the identifier or term without the change (written so, with the part missing); a hit that cannot be told to hold the change goes to the human. WAY-414's pair of examples carries the case. |
| I4 | WAY-414's binding sentence names the key for each kind and the comparison (passage below); `closure.md` says the same. |
| I5 (orchestrator's choice) | Place 2 and sections 4 and 6 of `closure.md`: where the plan's `Document` cell links a task document, the preview shows it (path, `Status:`, `Project relation:`) and asks which stands; a new document carries a reference to the old one under *Context*, and the new place (note section or document) refers to the old document; the existing line links a new document only where the rules of the task place allow and the preview shows it. WAY-415's pair says so; its violating example "rewrites the body of a document a refiner has taken up" stays and a second violating example is added. |
| Minor 1 | (a) the closed-plan reader test asserts no `repository:` line; (b) new test `Closed.test_the_first_status_line_decides_whether_the_plan_is_closed` (a row in cycle under a first `closed` line and a second `handed over` line reports `closed` and `form`; the reverse order reports `form` only); (c) the comment is corrected; (d) correction of this report: the tests that were seen failing on the base code are those that name a `closed` plan passing or its rows (the 16 failing subtests of the before run); `Header.test_a_closed_date_that_is_no_calendar_date_is_reported` and the reader test `test_a_closed_line_off_its_form_or_doubled_is_no_closed_plan` assert refusals the base code gave by refusing every `closed` line, so they pass on the base code and are held by mutation, not by a failing run. The reader's help text is now "original handed-over or closed project plan". Mutants run and caught: `closed_date` reading the last line (1 failure in `test_plan_check`), `return 0` removed after the `closed:` line (failures of the closed-plan reader test); both restored before the commit. |
| Minor 2 | The second case is removed from `closure.md`; only "`Written by` names a dropped task" stays. |
| Minor 3 (smaller way) | `task_line.md` names the closing as a reader and as a maker of a line; the line of a `source only` task that leaves the plan carries no identifier derived from the plan and no dependencies (the smaller of the two ways). |
| Minor 4 | WAY-415's second paragraph no longer says WAY-154 governs the refinement: it prevails "for the first body only; once a refiner has taken the document up, its body is the refiner's". |
| Minor 5 (smaller way) | The form of the closing item: four nested items always standing, the last three reading `none` where nothing is to list; the labels and `project closed` are markers kept in English, the rest in the language of the plan; the last label reads `projected entries a dropped task was to write`. |
| Minor 6 | The template now says "A closed plan holds only rows `done`, `done — goal delivered in task <n>` and `dropped — approved by human`, and no row delivered in a task of the last state". |
| Minor 7 | `closure.md` section 3 says the moves are written only after the acceptance of section 6. |
| Minor 8 (smaller way) | One word: "dropped" (the state's own word in WAY-142, the invariant and the template), in the skill's description, the part map, `closure.md` and WAY-411 to WAY-415; the third place is now "given up for good", so the two do not collide. The other way, "withdrawn" everywhere, would have rewritten the state's name in older entries. |
| Minor 9 | The template cites the check of a closed plan to WAY-142 and WAY-146. |

**Case the request puts before the human (I5).** The task does not settle a dropped task that already has a task
document linked from the plan's `Document` cell. The closing shows that document in the preview and asks which
document stands; where a new one is made it refers to the old one, and the note section or new document refers
to the old document, which holds the answers given while the task was refined. WAY-415's pair of examples says it.

**Added passage of WAY-414 (an addition to row 5, so the entry stays `the cycle's`), word for word:**

"The closing searches the product's foundation, at a commit it names, for the projected entry of a dropped task,
by the question the heading of a decision holds or by the identifier or term of any other entry, which the plan
keeps word for word, and compares the text of what it finds with the projected change. It writes that the entry is
absent from the foundation at that commit, or the entry it found, a part of it included, that another task wrote
(WAY-126), or that an entry stands under that identifier or term without the change. A hit the closing cannot tell
to be the same entry, or to hold the change, is put to the human as a question in the preview, before anything is
written."

(Row 5 gave the search by the question and the two results "absent" and "found, partial included"; the key for
the other four kinds, the comparison and the third result are the addition.) The pair of examples of WAY-414
gained a case for a change to a current decision that stands without the change, and a violating example of an
entry written as found without comparing; WAY-415's pair gained the existing-document case and one violating
example. Both pairs stay `the cycle's` parts; the earlier pairs of this report otherwise stand as written.

## Checks of the fix (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Plan check tests | `python -B -m unittest test_plan_check` (in `project-level`) | 0 (134 tests) |
| Directory | `python -B gate/run_tests.py project-level` | 0 (log `reports/after-project-level-fix.log`) |
| Dead pointers | `python -B gate/run_tests.py product-guidelines` | 0 |
| Entry points, sizes, formatter, linter | `python -B gate/run_tests.py agent-instructions` | 0 |
| Foundation | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Entry points | `python -B agent-instructions/skill_entry_points.py --write` | 0, `entry points are current` after the description changed once and was regenerated |
| Formatter and linter on `project-level/*.py` | `ruff format`, `ruff check` (Ruff of the main checkout's environment) | 0, 0 |

## Reaches, working copies, unread, searches (this fix)

- Reaches beyond the handoff: none beyond `reports/review-whole-report.md`, which I did not need to read; the
  findings file gave each place. I read `project-level/definition_template.md` lines for the heading kinds again
  (I3, I4) only through the findings' own quotation.
- Working copies: `.runs/author/` (backups of the two scripts for the mutants, the run log); removed whole and made
  again empty; the log of the run kept as `reports/after-project-level-fix.log`. No remainder.
- **Unread material:** `reports/review-whole-report.md` (named for context; the findings file was enough), and the
  definition template's passage on the headings by kind, which I took from the findings' quotation of lines 328 to 332.
- **Searches not found or unclear:** whether the human, on a row delivered in a dropped task, settles it by changing
  the row or by naming the task that delivered the goal: `closure.md` says it is reconciled with the human, as the
  plan template gives, and no more. The earlier entries of this report ("withdrawn" in choice and table text) keep
  the word of the time they were written; the committed files say "dropped".
