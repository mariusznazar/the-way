# Author report — request-decision-groups (the one author, whole change)

**Status:** done with concerns (the concerns are the choices and readings under "Choices" and "Problems"; none blocks).

## Commits

- `9876bfe` — code and prose: `task-cycle/request_check.py`, `task-cycle/test_request_check.py`, `task-cycle/skill/request_template.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/SKILL.md`.
- `ff77994` — foundation: `foundations/decisions.md` (WAY-287, WAY-289, WAY-290, WAY-317 edited in place; WAY-327 added).

Files (insertions/deletions over `e3825a8..HEAD`): `foundations/decisions.md` 166 changed lines, `task-cycle/request_check.py` 81, `task-cycle/skill/SKILL.md` 8, `task-cycle/skill/correction.md` 16, `task-cycle/skill/request_template.md` 318, `task-cycle/test_request_check.py` 177; total 605 insertions, 161 deletions. The worktree is clean.

## What was done, against the task's *To do*

1. Template: `## For you to decide` has three `###` groups (`Needed from you`, `Fix or let through`, `You accept by merging`), always all three, a group without items `none`, the whole section `none` alone when no group has an item, one continuous numbering. The block in the task's language stands translated, group headings among them (the template's "two parts" paragraph says so; the Polish wording is in the test fixture).
2. Criteria and kinds: kinds 1, 2, 3 in *Needed from you*; 4, 8, 9, 14 in *Fix or let through*; 5, 6, 7, 10, 11, 12, 13, 15 in *You accept by merging*. Kind numbers are the base's (checked against `e3825a8:task-cycle/skill/request_template.md` lines 170-247; 15 is the form-check error of `:54`, now a listed kind).
3. "What an item carries": the four points for an item in which the human chooses; the action item (kind 3); the item of the accepting group (what the cycle chose and why, and in one sentence why not another way; the group opens with the sentence that merging accepts). A bad item (today's example) and a good one (the loop2 #75 item 9, rewritten without product names or links) stand side by side; the good one stands in a fenced `markdown` block that a test runs through the form check.
4. "Write, check, publish": a new step 2 before the form check — the writer reads every item of the first two groups against the four points (WAY-327); later steps renumbered (nothing else refers to them by number).
5. `correction.md` and the template give what "do it in this request" runs: step or check left out (4), proposal applied (9), fresh reviewer reads what stayed unread (14); when the thing cannot be done in this request, only "make a task of it" and "let it through".
6. References by number: `correction.md` "item 8", `SKILL.md` "item 12", the template's "item 4" at kind 13 are unchanged and point at the same kinds (kinds are written `- **N.**` so that Markdown does not renumber them).
7. `request_check.py`: new `DECISIONS`, `DECISION_GROUPS`, `first_content_line`, `check_decision_groups`; docstring updated; the block is not held to the groups.
8. WAY-287 (groups with criteria, headings, `none` per group and for the whole section, continuous numbering, accepting group waits for no answer; Rationale and Rejected from the task's *Not chosen*), WAY-289 (answer "fix it in this request" also for the three kinds), WAY-290 (group headings in the list of what the script checks), WAY-327 (new; row 3).

## Foundation entries (the foundation step)

| Entry | Marked | English sentence | Polish sentence |
|---|---|---|---|
| WAY-287 | row 1, row 2 | The section for the human's decisions has three groups with their criteria, always all three, `none` for an empty group and for the whole section, continuous numbering, and the accepting group waits for no separate answer. | Sekcja decyzji człowieka ma trzy grupy z kryteriami, zawsze wszystkie trzy, `none` dla pustej grupy i dla całej sekcji, ciągłą numerację, a grupa przyjmowana scaleniem nie czeka na osobną odpowiedź. |
| WAY-327 | row 3 | An item in which the human chooses says what happens and who feels it, each way with its cost, a recommendation with a reason and a question with answers, and the writer checks it before the request opens. | Pozycja, w której człowiek wybiera, mówi co się dzieje i kto to odczuje, daje każdą drogę z ceną, rekomendację z powodem i pytanie z odpowiedziami, a piszący sprawdza to przed otwarciem PR-a. |
| WAY-289 | row 4 | The answer to fix it in this request is offered also for a skipped step or check, a proposal not applied and an incomplete reading of the review, not only for review findings. | Odpowiedź „zrobić w tym PR-ze” dotyczy też pominiętego kroku albo sprawdzenia, niewprowadzonej propozycji i niepełnej lektury recenzji, nie tylko uwag recenzji. |
| WAY-290 | row 5 | The form check holds the three group headings of the decisions section and still judges no content. | Skrypt sprawdzający formę pilnuje nagłówków trzech grup w sekcji decyzji i nadal nie ocenia treści. |
| WAY-317 | the cycle's (search of the foundation, WAY-33) | The request tells the human that no screenshot is shown, which the human accepts by merging, instead of asking a question that waits for an answer. | PR mówi człowiekowi, że zrzutu ekranu nie pokazano, co człowiek przyjmuje scaleniem, zamiast zadawać pytanie czekające na odpowiedź. |

Withdrawn numbers: none. `python -B elements/common/foundation_check.py` — exit 0, `0 errors`. No invariant written or changed; no surface, no *Violated* mark, no part map change.

## Checks

| Check | Command | Exit |
|---|---|---|
| Tests written first, failing (re-created) | `python -B <scratchpad>/failing_first/test_request_check.py > out.txt` (no pipe), run in a scratch directory outside the worktree holding the HEAD test file, the BASE `request_check.py` (`git show e3825a8:task-cycle/request_check.py`) and the HEAD `skill/request_template.md` that the test reads | 1: 74 tests, 11 failures and 1 error (the 11 failures are all in `DecisionGroupsTest`, assertions on lines and messages; the error is the skeleton test on the base's missing `DECISION_GROUPS`) |
| The same tests after the change | `python -B task-cycle/test_request_check.py` | 0 (74 tests, OK) |
| Focused: task-cycle | `python -B gate/run_tests.py task-cycle` | 0 (254 tests) |
| Focused: elements/common | `python -B gate/run_tests.py elements/common` | 0 (117 tests) |
| Focused: agent-instructions | `python -B gate/run_tests.py agent-instructions` | 0 (18 tests) |
| Focused: instruction-files | `python -B gate/run_tests.py instruction-files` | 0 (104 tests, 5 skipped) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0, `0 error, 0 warn, 3 info` |
| Private paths on each changed file | `python -B task-cycle/private_paths_check.py <file>` for the six files | 0 each |

Not run: the whole gate `python -B gate/run_tests.py` (the orchestrator's); `elements/part-map`, `installation`, `project-level`, `relation-model`, `gate` directories (not touched by the change).

`invariant: <id>` citation lines: none added. Among the invariants read, none with method `test` concerns `request_check.py` (`tracked-file-private-paths`, `derived-file-content`, `cross-part-imports` are checked by their own tests; the new code only imports the standard library, runs no program and writes no file). No invariant test was changed.

Mutations considered: order not checked, repeated heading, text before the first group, empty group (heading with only a comment), `none` in backticks or with a comment, headings in fenced code, group heading at another level or in other words, block held to the groups, missing group at each of the three places — each has a test. Tests do not repeat a constant's value (a test that only asserts the three heading strings was written and dropped by the method's rule); the group names are tied to the template by the skeleton test.

## Own-work check (WAY-164)

- Requirement most likely not met: "numbers of kinds stay and every reference by number points at the same kind" (*To do* 6), together with "the template's own example passes the check".
- Checks: (1) listed the template's kinds `- **N.**` with grep and compared their first words with `git show e3825a8` lines 170-247 and `:54`: 1 blocked request, 2 questions, 3 human actions, 4 skipped steps, 5 choices, 6 entries, 7 invariant tests, 8 unfixed findings, 9 decisions of own sections, 10 remarks listing, 11 logging scope, 12 relation line, 13 no screenshot, 14 incomplete reading, 15 form-check error — identical. References "item 8" (`correction.md`), "item 12" (`SKILL.md:563`), "item 4" (template, kind 13) unchanged and correct. (2) `test_the_templates_example_of_the_decision_section_passes_the_check` runs the template's good example through the check: passes. (3) The CLI on a file of the new shape: `python -B task-cycle/request_check.py <file> --task <polish task>` exit 0; on a file with a numbered list and no groups: exit 1 with `line 12: ... holds neither none alone nor the groups ...`.
- Showed: all hold.

## Reach beyond the dispatch

- `foundations/decisions.md` WAY-317 (read whole, lines 10232-10266) and WAY-295 (lines 9378-9397), WAY-291 (read for the statement that the form error stands in the section): found by a grep for the section's question wording after the groups were settled (WAY-33). Why: WAY-317's *complies* example said the request "asks the human whether to merge without seeing the screen", which the accepting group no longer allows; edited in place (marked `the cycle's`). WAY-295 and WAY-291 say only that the section names the case — no edit.
- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/rules.md`, `elements/common/way_of_working.md` (whole): required by the decisions skill for writing WAY-327.
- `task-cycle/skill/SKILL.md` lines 210-231, 430-465, 480-597 (read in part) and `task-cycle/skill/blocked_finding.md` (whole): to find other references to the section; one edit at `SKILL.md:507`.
- `gh pr view 75 --repo mariusznazar/loop2`: to take the good example (item 9) from its source rather than from memory.
- `instruction-files/check_instructions.py` run on the repository (not named by the handoff) to see the template and skill files are not flagged.

## Choices (with the way rejected and its cost if wrong)

1. **Kind 15 added to the template's list** (the form-check error), in *You accept by merging*, as the task's *To do* 2 puts it. Rejected: leaving it only in "An error you hold wrong" — then the kind would have no group. Cost if wrong: one list entry.
2. **Questions of the accepting-group kinds removed** ("Merge as it stands?", "Accept it?", "Merge without seeing the screen?") from kinds 10, 11, 12, 13, 15, because *To do* 3 says those items wait for no answer. Cost if wrong: the human sees statements instead of questions there; WAY-317's example had to follow (edited).
3. **"Let it through" is a third answer for kind 8** (WAY-289 said "two answers", fix or task). I read the group's name and *To do* 2 ("zrobić w tym PR-ze, zrobić z tego zadanie albo przepuścić") as applying to kind 8 too and wrote WAY-289 with three answers. Rejected: leaving kind 8 with two answers while 4, 9 and 14 have three — an inconsistent group. Cost if wrong: one phrase in WAY-289, the template (kind 8) and `correction.md` ("or to let the item through").
4. **WAY-289's title unchanged** ("Which unfixed findings...") though its content now covers things that are not findings (steps, proposals, a reading). Rejected: renaming the question (a number stands for its question; no reference quotes the title). Cost if wrong: a reviewer may flag the title as narrower than the entry.
5. **WAY-327 as a new decision** (row 3) with *Relations* `derives from WAY-287` only; it scopes to *Needed from you* and *Fix or let through* "but one that asks for an action outside the repository" (the action item has its own three-part content in the template only, as *To do* 3 gives it; no row asks for a decision on it).
6. **No change to WAY-114, WAY-286, WAY-288** (as the task says). The accepting group's kind 6 keeps WAY-114's plain sentence.
7. **Example without product names or links**: the loop2 #75 item 9 was rewritten for "a product's server" and not linked (loop2 may be private; invariant `outbound-link-reach`).
8. **Kinds written as `- **N.**` bullets**, not a numbered list, so a viewer does not renumber 4, 8, 9, 14 as 4, 5, 6, 7. Cost if wrong: a different look in the template.
9. **Script messages**: the whole section with items and no groups gives one error at the section heading (not one per missing group); text before the first group is reported at its first content line; a missing group at the next present group, or at the next `##` heading.

## Problems as observed

- WAY-287's binding sentence is one long sentence (the old list of what the section holds, plus the new groups); it keeps the 2-sentence count. Observed, not a failure of a check.
- The `Rejected` of WAY-287 for groups was taken from the task's *Not chosen*; the task's pytanie 1 answer names only the "4, 9, 14 together with 1-3" way, and pytanie 3 the other three; I wrote all four, each with its reason.

## Unread material

- `agent-instructions/README.md`: read whole. 
- Decisions read whole: WAY-114, WAY-161, WAY-286, WAY-287, WAY-288, WAY-289, WAY-290, WAY-291, WAY-292, WAY-326 (the last one, not named by the handoff, as a model of an entry). Read in part: WAY-162 (lines 4655-4709, the end of its *Rationale* and its *Rejected* not read), WAY-295 (to the end of *Verification*; *Rationale* and *Rejected* not read). Not opened as entries: WAY-150, WAY-33, WAY-36, WAY-07 (their rules were read as they are restated in `elements/common/way_of_working.md` and `agent-instructions/README.md`).
- Invariants: read whole `foundation-file-kinds`, `foundation-change-merge-route`, `return-step-record`, `derived-file-content`, `tracked-file-private-paths`, `script-language`, `script-imports`, `script-subprocesses`, `test-method-citation`, `cross-part-imports`; the rest of `foundations/invariants.md` was not read beyond lines 1-175 and 328-352 (the *Part* grep found no other with *Part* `task-cycle` besides `record-copy-image-check`, which was read).
- Part map: the `task-cycle` and `decisions` entries read whole (as lines 7-15 and 92-100).
- Glossary: headings only (none of its terms is used by the template).
- `task-cycle/skill/SKILL.md`: not read whole; read lines 210-231, 430-465, 480-598 and the grep hits of the section's wording.

## Searches not found or unclear

- The text of loop2 PR #75 is not in the task; found it with `gh pr view 75 --repo mariusznazar/loop2` (readable). The task names its item as "pozycja 9"; it sits in the PR's "Open" group.
- The handoff says "Numbers in the task's *To do* 2 refer to the numbered kinds ... lines 170-247"; kind 15 is not in that range (it is `:54`), the task says so; no gap.
- The task's *To do* 1 says the block in the task's language "stands translated"; the template does not hold the Polish headings (English template); the Polish ones live only in the test fixture. Unclear whether the template should name them; I did not add them.
- Whether `agent-instructions/README.md` ("check the description and correct it as the template gives") needs a word on the groups: judged not, it points to the template.
- A search for another file naming the questions "Merge as it stands?", "Accept it?" outside the template, `SKILL.md:507` and WAY-317: none found by grep over `*.md` and `*.py` outside `.runs` and `.git`.
