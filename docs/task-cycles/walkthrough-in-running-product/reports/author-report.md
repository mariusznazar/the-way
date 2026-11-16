# Author report — task `walkthrough-in-running-product`

**Status:** done

## Commits and files

One commit, `940893de` ("Add the walk through the running product to the author's own-work check"), on `task/walkthrough-in-running-product`, base `9cffc9ba`.

| File | Added / removed |
|---|---|
| `task-cycle/change/walkthrough.md` (new) | 105 / 0 |
| `foundations/decisions.md` | 190 / 10 |
| `task-cycle/skill/request_template.md` | 14 / 5 |
| `task-cycle/change/SKILL.md` | 9 / 0 |
| `task-cycle/review/SKILL.md` | 4 / 0 |
| `elements/decisions/template.md` | 5 / 1 |
| `project-level/technology/research.md` | 4 / 1 |
| `foundations/glossary.md` | 1 / 1 |

No script, no skill description and no boundary file (`task-cycle/cycle_stages.py`, `installation/install.py`, ...) is touched; the trust-boundary answer of the handoff holds.

## Checks

| Command (from the worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B agent-instructions/skill_entry_points.py` (no `--write`; no description changed) | 0 (`entry points are current`) |
| `python -B gate/run_tests.py task-cycle` | 0 (534 tests, OK, 2 skipped) |
| `python -B gate/run_tests.py project-level` | 0 (279 tests, OK) |
| `python -B gate/run_tests.py elements/common` | 0 (257 tests, OK) |
| `python -B gate/run_tests.py agent-instructions` | 0 (37 tests, OK, 2 expected failures) |
| `python -B task-cycle/private_paths_check.py <file>` for each of the 8 changed files | 0 for each |

`task-cycle/request_check.py` on a drafted description was not run: the change to `request_template.md` is prose inside existing items (no heading, group or kind added), and `task-cycle/test_request_check.py` runs inside the `task-cycle` directory run above. The gate as a whole was not run (the orchestrator's).

No check failed and none was rerun. Not run: the full gate (the orchestrator's) and `task-cycle/request_check.py` on a draft.

## The foundation step — entries written

Marking: `row <n>`, `projected` or `the cycle's`. Each of the three new decisions is `the cycle's` for one reason only: its *Verification* is a pair of examples that I added (the rows give none), and no test of this change can hold a sentence of a text that instructs agents. The pairs stand word for word in the log, entries WAY-406, WAY-407 and WAY-408, under *Verification*; the request quotes them under each entry. WAY-121 and WAY-319 each carry one added item in an existing pair; their meaning is the row's.

| Entry | Marked | One sentence (English) | One sentence (Polish) |
|---|---|---|---|
| WAY-406 (new, section "The work of a cycle's agents") | rows 1, 2, 3; `the cycle's` for the pair | The author of a change, and the executor of each slice that alters behaviour a user sees, walks through the running product what the tests do not cover, after the code and before the review; the walk is required for every such change, is "not performed" with its reason where the foundation settles no way to the product without stopping the cycle, the fix of a review's findings does not repeat it, and a stage of its own comes only if the audit shows an error the author let through; the practices of `test-run` and the courses bind only through this decision. | Autor zmiany, a przy planie wykonawca każdej części zmieniającej zachowanie widoczne dla użytkownika, sprawdza w działającym produkcie to, czego nie obejmują testy, po kodzie i przed recenzją; przejście jest obowiązkowe przy każdej takiej zmianie, a gdy fundament nie ustala drogi do produktu, jest niewykonane z tym powodem i cykl się nie zatrzymuje; poprawka po recenzji go nie powtarza, osobny etap pojawi się dopiero, gdy audyt pokaże błąd przepuszczony przez autora; praktyki `test-run` i kursów wiążą tylko przez tę decyzję. |
| WAY-407 (new) | row 4; `the cycle's` for the pair | No one approves the cases of the walk before it is made and the cycle does not stop for them; the author draws them from the requirements of the task and the human sees in the request what was not checked; the refinement of a task writes no list of inputs to try. | Nikt nie zatwierdza przypadków przejścia przed jego wykonaniem i cykl się nie zatrzymuje; autor układa je według wymagań zadania, a człowiek widzi w PR-ze, czego nie sprawdzono; doprecyzowanie zadania nie zapisuje listy wejść do wypróbowania. |
| WAY-408 (new) | row 5; `the cycle's` for the pair | The author corrects a case that fell wrong before the review, with a test at the lowest level that catches the error, and reports an error outside the task's scope, which the request puts before the human to make a task of or let through. | Autor poprawia przypadek, który wypadł źle, przed recenzją z testem na najniższym poziomie, który ten błąd łapie, a błąd poza zakresem zadania zgłasza, i PR stawia go człowiekowi do zrobienia z niego zadania albo puszczenia. |
| WAY-121 (new paragraph; *Rationale*, *Rejected*, one item each in *complies* and *violates*) | row 9; `the cycle's` for the two added pair items | The answer to a matter of an agent's way to the running product is a decision of the product though it tells an agent how to work, and a skill of the product may hold the steps of operation and cites that decision. | Odpowiedź na sprawę drogi agenta do działającego produktu jest decyzją produktu, choć mówi agentowi, jak pracować, a skill produktu może trzymać kroki obsługi i powołuje się na tę decyzję. |
| WAY-319 (second sentence; *Rationale*, *Rejected*, one item each in *complies* and *violates*) | row 11; `the cycle's` for the two added pair items | The condition reaches a product through the step that settles technology, which says for each option of the interface whether two cycles can check at once without a shared browser, and an option that cannot stays in the comparison with that lack. | Warunek dociera do produktu przez krok technologii, który przy każdej opcji interfejsu podaje, czy dwa cykle mogą sprawdzać naraz bez wspólnej przeglądarki, a opcja, która nie może, zostaje w porównaniu z tym brakiem. |
| `elements/decisions/template.md`, "Where it goes", question 1 | row 9 (the same sentence in the template) | Question 1 sends an answer on a matter of an agent's way to the running product to the log, not to a skill, and says that a skill of the product may hold the steps and cites the decision. | Pytanie 1 kieruje odpowiedź na sprawę drogi agenta do działającego produktu do logu, nie do skilla, a skill produktu może trzymać kroki i powołuje się na decyzję. |
| glossary "agent's way to the running product" | row 10 | The way is also the means by which the agent shows the human what it saw. | Droga to także środek, którym agent pokazuje człowiekowi, co zobaczył. |

Rows 6, 7 and 8 stand in `task-cycle/change/walkthrough.md` (no entry written, by the row's *Goes to*): row 6 in section 4 (order by conditions and the building of state, with the reason in one sentence), row 7 in sections 5 and 6 (block of costly and irreversible effects, where checked, verdict from a reading of the state, name of the missing tool, limitation and evidence from the layer checked, the whole screen read), row 8 in sections 1 to 6 (preparation, shared code, scope, plan with "by what" and the "side observation" row, widening only on a hard signal, verdict per case with the layer, "what I did not check", comparison of two measurements). The wording of what was left at VOX stands in *Rejected* of WAY-406 and is carried from the task's answer under the question on `test-run`.

Question 11 of the *To do* (WAY-319 sentence) is in the log as the second sentence of WAY-319, as the row says.

## Pointers and pieces (To do 2 to 5, 8)

- `task-cycle/change/SKILL.md` section 3: a new point naming the readers (the one author and the executor of a slice; the fix reads nothing of it); section 6: a bullet for the report's content, or "alters no such behaviour" with one sentence why.
- `task-cycle/review/SKILL.md`, "The author's own-work check": a bullet that reads the report of the walk (the judgment of alter / not alter, cases from the requirements, a reason for each unchecked case).
- `task-cycle/skill/request_template.md`: kind 4 (the walk not performed or a case unchecked, with its reason; the screenshot unchecked and the walk not performed for the one cause stand as one item), kind 8 (an error outside the scope the author reported, with "Make a task of it?"), kind 13 (pointer that the walk joins kind 4), the paragraph of the top part on artifacts (cases and verdicts stay in the reports), and *Checks* (cases with their verdicts). `task-cycle/change/ui_check.md` is unchanged.
- `project-level/technology/research.md`, point 3: for a choice of the interface, each option says whether two cycles in separate worktrees can check at once without a shared browser; an option that cannot stays with the lack.

## Choices of how to make what the task settles (for the orchestrator's record)

1. **Name of the method file:** `task-cycle/change/walkthrough.md` (the recommended name). Rejected: `test_run.md` (names a source not open to a reader); `walk.md` (reads as the verb).
2. **Split of rows 1 to 5 into three decisions, WAY-406 to WAY-408**, placed at the end of the section "The work of a cycle's agents" (its sentence covers what an agent checks of its own work and reports). Reason (WAY-19): the question of who walks and for which changes, the question of who approves the cases and the question of what happens to a case that fell wrong can change on their own. Rejected: one decision with three paragraphs (WAY-407 and WAY-408 would then change WAY-406 each time); four decisions with the adoption as one (WAY-100 and the decisions template forbid "what do we take from X" as a question). Cost if wrong: renumbering by the cycle, three entries in place of one in the request.
3. **Adoption (WAY-100) stands in the *Rationale* of WAY-406**, which describes what was seen in `test-run` and in the two courses and says the sources are not open to a reader (WAY-27). It names no path and no title of a note; it names `test-run` and "two courses" only. What was left out stands in the *Rejected* of WAY-406: the answer under the question on `test-run` ("Zostaje przy VOX ...") and the course items taken out ("limit jednoczesnych instancji", "pole 'jak to sprawdzić'") are carried from the task's text as the row's source keeps them; a strict reading of WAY-134 could count the first of these as "a way the writer derives"; I judged it the source's own list.
4. **Pairs of examples** for the three new decisions (a decision that nothing holds is an error of the check), written by me, therefore `the cycle's`; for WAY-121 and WAY-319 I added one item to each side of the existing pair, for the new sentence, which no invariant or test holds (the pair there is optional).
5. **The wording of the lack** of an option of the interface in `research.md`: "two task cycles cannot check the running product at once this way", on the model of the lack that WAY-166 gives.
6. **Request template, kind 8:** the error outside the scope reported by the author carries only "Make a task of it?" (the task: "zrobić z niego zadanie czy puścić"), where a reviewer's finding outside the scope keeps the three answers kind 8 already gives.
7. **Method file addresses the author as "you"** like `ui_check.md`; it carries the reason of the order of cases in one sentence (WAY-293).

## Own-work check (WAY-164)

- **Requirement most likely not met:** that the committed files hold no path or title of a private note, and that the decisions' *Rationale* and *Rejected* follow the form of the template (WAY-05: no file, script or count; WAY-27), since the sources of the method are private notes and a team repository.
- **Check:** `python -B task-cycle/private_paths_check.py <file>` for each of the 8 changed files (exit 0 for each), a `git grep` of the new text for `vox`, the course names as titles and drive paths (only the two existing decisions name the courses; WAY-406 names "two courses" and `test-run` alone), and `python -B elements/common/foundation_check.py` (exit 0).
- **Showed:** no private path or title; WAY-406 *Rationale* names the skill `test-run`, which is a name of an outside practice, not a file of this repository, and I read WAY-164's own naming of Limen as the precedent; that is my reading, and the reviewer may hold it otherwise.

Second requirement attacked: "the fix of a review's findings reads nothing of the walk". Check: `change/SKILL.md` section 1 (read whole) gives the fix row `fix.md` for its reading, and `git grep -n -i "ui_check\|walkthrough" task-cycle/change/fix.md` finds nothing (`fix.md` was not read whole and is unchanged); section 3's new point names the readers as the one author and the executor of a slice. It showed that the fix's own reading never reaches `walkthrough.md`, except where the fix's agent applies section 3 whole, which its point now excludes in words.

## Reaches beyond the dispatch

- `foundations/decisions.md`: read the *Rejected* of WAY-121 whole, and the sections' headings of the log to place the new entries, to follow `way_of_working.md`.
- `elements/decisions/skill/read.md` and `decide_entry.md` (named by the skill I was told to follow).
- `task-cycle/skill/SKILL.md` lines 284 to 340 (the orchestrator's check of reports, the working copies paragraph): to see whether a report of `make-change` is checked for its parts; it is checked for the own-work check only (line 298), and the task names no change there.
- `project-level/definition_template.md` lines 158 to 250, `project-level/technology/settle.md` line 34 and `running_product.md`: to see whether the WAY-166 rule stands in more files than `research.md`.
- `task-cycle/review/whole_change.md` lines 15 to 25: for the reading of the executors' own-work check.
- The two private notes of the courses, for the lines the task names (D21 and U4); only the passages on the method were read.

## Unread material

- `foundations/decisions.md` beyond the entries named and the headings of the sections: not read whole (the index of the orchestrator covers 60 entries in full; I opened whole WAY-100, WAY-121, WAY-164, WAY-319, WAY-373 and the entries I wrote; the others of the handoff list I read as the index gives them: WAY-165, WAY-227, WAY-238, WAY-239, WAY-13, WAY-140, WAY-287, WAY-316, WAY-166, WAY-125, WAY-256, WAY-293).
- `foundations/part_map.md`: read the entries of `decisions`, `glossary`, `project-level`, `task-cycle`; not the rest.
- `foundations/invariants.md`: the entries whose *Part* names a touched part or `every`: read as first lines only (identifier and first sentence), not whole.
- `guidelines/coding.md` and `guidelines/testing.md`: not read; no code or test was changed.
- `vox-ai-tools/skills/test-run/SKILL.md`: read whole; its `references/mechanika.md` not read.
- `elements/glossary/examples.md`, `elements/decisions/examples.md`: the latter read (names WAY-03); not the entries it names.

## Searches not found or unclear

- The handoff names "the paragraph beginning 'Where a change alters what a screen shows'" in `request_template.md`; no paragraph begins so (the words stand in WAY-316 and, in other form, in the top part's "What you will see" and kind 13). I took it for the paragraph of "What you will see" ending in "leave logs and outputs in the reports" and for kind 13.
- The task cites WAY-140 for "no pauses in the middle of the cycle" (*Questions to settle*, plan approval); WAY-140 in the log is about effects outside the repository, and carries no such rule. I did not cite WAY-140 in WAY-407; WAY-227 carries the reason.
- The task says, in *Context*, that the rule on textual traces stands in the paragraph beginning "Where a change alters what a screen shows" of the request template; the matching sentence is "Of the artifacts of the check only screenshots reach the description ...".
- The orchestrator's check of reports (`task-cycle/skill/SKILL.md` line 298) returns a `make-change` report without its own-work check, but names no check for the walk; the task does not ask for one. Not changed.
- `project-level/definition_template.md` (the Technology section, line 241) carries the WAY-166 rule as `research.md` does, but the task names only `research.md` for the WAY-319 condition; I changed `research.md` alone. The template's section is read by the research agent too, so the condition reaches it through `research.md` only.

## Working copies

Stood in `.runs/author/` of the worktree: the output of the foundation check and of the test runs. They are ignored by git and hold nothing that the report needs; I removed the directory `.runs/author/` after the last check, so nothing of it remains; the results above are recorded as command and exit code.

## Problems observed

None beyond the above.
