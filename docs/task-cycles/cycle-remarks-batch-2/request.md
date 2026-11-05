**State: draft** — the form check reports an error the cycle holds wrong; the change is reviewed and every test passes.

## What you will see

Four small corrections to how a task cycle works, each taken from a remark that earlier cycles left in their pull requests.

1. **A task can now say that a choice gets no entry in the decision log, and that wins.** When the task or its spec states outright that a choice is not to be written into the foundation, the cycle's last step no longer overrides it: the choice stays a row in the cycle's table of questions. Without such a statement nothing changes. The cycle wrote this as a new decision that narrows two older ones, and a candidate the human cut from the list of things to record does not count as such a statement.
2. **A decision's explanation may now give a measurement.** If a choice rests on a measurement, the explanation can say what was measured and under which conditions, never as a general limit. The explanation of the rule now also says why numbers are kept out of decisions: to keep out histories and chronicles that a reader of the decision does not need, not because numbers grow old.
3. **A stage report without its list of "looked for and not found" goes back to its agent.** The same holds for the report of a finished change without the description of how its author checked their own work. "None" is an answer; a missing section is not. The check the cycle runs after a slice's executor now looks at both sections too.
4. **The reviewer hands back a fixed short answer.** The first line of the report, the counts of blocking, minor and out-of-scope findings, a one-line result of the checks and the report path. The stage that writes the spec and the stage that reviews it run no test of the product, so they return no check result; the decision on what a stage's message carries now says so.

### Underneath

Eight files of instructions and one decision log: one new decision, two decisions changed in place, the template for decisions and five cycle instructions. No code and no test changed.

## For you to decide

1. **The new pair of example sentences is laid out differently from the task.** The task asked for a second pair of "complies" and "violates" examples under the old one. The cycle appended the new examples to the old two lines instead, because it took a second pair for a form the template does not give. The reviewer showed that another decision already holds two pairs and that the form check accepts it, so the reason did not hold; the meaning is unchanged, only the layout. Merge as it stands, or make a task of laying it out as a second pair? (Minor findings, 1)
2. **The new wording leaves one question about the stage that plans slices.** The decision now asks for a check result only from a stage that runs a test or another check of the product. The stage that plans slices still says it returns one, and the only thing it checks is the size of its own plan. It is unclear whether it should return a result. You approved the new wording with the task, and the reviewer set this aside as outside it. Make a task of it? (Findings outside the task's scope, 1)
3. **Two loose passages in the explanation of the new decision.** One describes what the request template lacks today, although decisions are meant to avoid what the process's tools do or lack today; the other lists "no change" as the option "which withdraws the rule", which a reader can take the wrong way round. The rule itself is unaffected. Make a task of it, or merge without it? (Minor findings, 2 and 3)
4. **The form check reports an error that the cycle holds wrong.** The script reads the task document as English and so wants the Polish block to read `none`. The task document is in Polish; the script measures only its title, its *Need* and its *To do*, and the *To do* is mostly English wording that the task quotes from the instructions it asks to change. The cycle did not empty or translate the block to silence the script. Merge as it stands? (Checks, 6)

## Cost

About 23 minutes of working time. The orchestrator and all agents ran on one model, Claude Sonnet 5.5, using 11.9 M tokens, of which 11.4 M were input read from cache and 0.09 M output. Review rounds: the whole change was reviewed once and passed; no fix was needed. The return step made no commit, so it needed no review. The table of stages: https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/cycle-remarks-batch-2/stages.md

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: szkic** — skrypt sprawdzający układ zgłasza błąd, który cykl uważa za fałszywy; zmiana przeszła przegląd i wszystkie testy.

**Co zobaczysz**

Cztery drobne poprawki w tym, jak działa cykl zadania, każda wzięta z uwagi, którą wcześniejsze cykle zostawiły w swoich PR-ach.

1. **Zadanie może teraz powiedzieć, że wybór nie dostaje wpisu w dzienniku decyzji, i to wygrywa.** Gdy zadanie albo jego spec wprost wykluczają zapis wyboru w fundamencie, ostatni krok cyklu tego nie nadpisuje: wybór zostaje wierszem tabeli pytań w zapisie cyklu. Bez takiego wykluczenia nic się nie zmienia. Cykl zapisał to jako nową decyzję, która zawęża dwie starsze; kandydat, którego człowiek wyciął z listy rzeczy do zapisania, za wykluczenie nie liczy się.
2. **Uzasadnienie decyzji może teraz podać pomiar.** Jeśli wybór opiera się na pomiarze, uzasadnienie może powiedzieć, co zmierzono i w jakich warunkach, nigdy jako ogólną granicę. Uzasadnienie reguły mówi też teraz, po co liczby są wyłączone z decyzji: żeby nie wpuścić historii i kronik, których czytelnik decyzji nie potrzebuje — nie dlatego, że liczby się starzeją.
3. **Raport etapu bez listy „czego szukano i nie znaleziono” wraca do agenta.** To samo dotyczy raportu ukończonej zmiany bez opisu, jak autor sprawdził własną pracę. „None” jest odpowiedzią, brak sekcji nie jest. Sprawdzenie, które cykl robi po wykonawcy kawałka, obejmuje teraz też obie sekcje.
4. **Recenzent oddaje stałą, krótką odpowiedź.** Pierwsza linia raportu, liczby uwag blokujących, drobnych i poza zakresem, jednolinijkowy wynik sprawdzeń i ścieżka raportu. Etap piszący spec i etap, który go recenzuje, nie uruchamiają żadnego testu produktu, więc nie oddają wyniku sprawdzeń; decyzja o tym, co niesie wiadomość etapu, mówi to teraz wprost.

*Pod spodem:* osiem plików z instrukcjami i dziennik decyzji: jedna nowa decyzja, dwie zmienione w miejscu, szablon decyzji i pięć instrukcji cyklu. Żaden kod i żaden test się nie zmienił.

**Do Twojej decyzji**

1. **Nowa para przykładów stoi inaczej, niż chciało zadanie.** Zadanie prosiło o drugą parę przykładów „zgodne” i „naruszające” pod starą. Cykl dopisał nowe przykłady do dwóch starych linii, bo uznał drugą parę za układ, którego szablon nie podaje. Recenzent pokazał, że inna decyzja ma już dwie pary, a skrypt sprawdzający układ to przyjmuje, więc ten powód nie wytrzymał; sens jest ten sam, różni się tylko układ. Scalamy tak, jak jest, czy robimy zadanie na ułożenie jako drugiej pary? (Minor findings, 1)
2. **Nowe brzmienie zostawia pytanie o etap, który dzieli pracę na kawałki.** Decyzja prosi teraz o wynik sprawdzeń tylko od etapu, który uruchamia test albo inne sprawdzenie produktu. Etap dzielący pracę nadal mówi, że taki wynik oddaje, a sprawdza tylko rozmiar własnego planu. Nie wiadomo, czy ma go oddawać. Nowe brzmienie przyjąłeś razem z zadaniem, a recenzent uznał tę sprawę za leżącą poza nim. Robimy z tego zadanie? (Findings outside the task's scope, 1)
3. **Dwa luźne miejsca w uzasadnieniu nowej decyzji.** Jedno opisuje, czego dziś brakuje w szablonie opisu PR-a, choć decyzje mają unikać tego, co narzędzia procesu dziś robią albo czego im brak; drugie wylicza „bez zmiany” jako wariant, „który wycofuje regułę”, co czytelnik może zrozumieć na odwrót. Sama reguła na tym nie cierpi. Robimy z tego zadanie, czy scalamy bez tego? (Minor findings, 2 i 3)
4. **Skrypt sprawdzający układ zgłasza błąd, który cykl uważa za fałszywy.** Skrypt czyta dokument zadania jako angielski i dlatego chce, żeby polski blok miał tylko `none`. Dokument zadania jest po polsku; skrypt mierzy tylko jego tytuł, „Need” i „To do”, a „To do” to w większości angielskie brzmienia, które zadanie cytuje z instrukcji, jakie każe zmienić. Cykl nie opróżnił ani nie przetłumaczył bloku, żeby skrypt zamilkł. Scalamy tak, jak jest? (Checks, 6)

**Koszt**

Około 23 minut pracy. Prowadzący cykl i wszyscy agenci pracowali na jednym modelu, Claude Sonnet 5.5, i zużyli 11,9 mln tokenów, z tego 11,4 mln to wejście czytane z pamięci podręcznej, a 0,09 mln to wyjście. Rundy przeglądu: cała zmiana przejrzana raz i przeszła, bez poprawki. Krok powrotu nie zrobił żadnego commitu, więc nie wymagał przeglądu. Tabela etapów: https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/cycle-remarks-batch-2/stages.md

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The decision log gains one decision and two decisions are reworded.** `b2a52f6`: WAY-293 written at the end of the log (what prevails where a task or its spec excludes an entry); WAY-05 changed in place (binding sentence, *Rationale*, *Verification*); WAY-148 changed in place (binding sentence only). `elements/decisions/template.md` carries the same fragment as WAY-05's binding sentence.
2. **The cycle's instructions follow.** `3023f60`: `task-cycle/skill/return_step.md` and `task-cycle/record_template.md` (the exclusion prevails); `task-cycle/skill/SKILL.md` (a report without its *Searches not found or unclear* or its own-work check returns for repair, in the general rule and in the mechanical check of a slice executor's report; the parenthetical on `write-spec` agents); `task-cycle/review/SKILL.md` (what the reviewer returns); `task-cycle/spec/SKILL.md` and `task-cycle/spec/review.md` (what the designer and the reviewer of a spec return).
3. **The return step changed nothing.** It compared the three entries, the template, the touched parts and the instruction files, found nothing that no longer matched and made no commit.

## Checks

1. **The full test run passed on the base and on the tree that goes into this request.** `python -B gate/run_tests.py`: on the base `61c72fb`, exit 0, 667 tests in 8 directories; on the reviewed change `3023f60`, which is also the final tree, exit 0, 667 tests. `foundations` had not moved from the base (`git fetch`, `origin/foundations` = `61c72fb`), so no merge and no second run were needed. No check failed in any run; none failed and passed again.
2. **Two focused runs pointed at directories without tests; they are no failing tests.** The author's `python -B gate/run_tests.py elements/decisions` and `python -B gate/run_tests.py foundations` exited 1 with `no test found`, since those directories hold no tests; the gate runs every directory that holds tests.
3. **The author's own-work check showed that every sentence the task quotes stands in its place word for word.** A scratch script searched 14 quoted sentences in their target files with whitespace normalised: 14 of 14 missing on the base (exit 1), none missing on the tree (exit 0). The reviewer's own script, which kept the `complies:`/`violates:` labels, found 12 of 14 and showed that the author's script could not catch the lost labels (Minor findings, 1).
4. **The focused checks the author and the reviewer ran all exited 0.** `python -B elements/common/foundation_check.py` (`0 errors`), and `python -B gate/run_tests.py` for `task-cycle` (92 tests), `elements/common` (109), `relation-model` (12), `agent-instructions` (18) and `instruction-files` (104, 5 skipped by the tests).
5. **No user interface changed:** no states or screenshots apply.
6. **The form of this description was checked by the script.** `python -B task-cycle/request_check.py .runs/task-cycles/cycle-remarks-batch-2/request.md --task .runs/task-cycles/cycle-remarks-batch-2/task.md`: exit 1, 3 runs, last reported line `line 31: the task document is in English; the block reads `none``. The cycle holds it wrong: the task document is in Polish, and the script measures only its title, its *Need* and its *To do*, the last of which is mostly English wording quoted from the instructions the task asks to change. The block stays in Polish, the description was not changed to silence the script, and the request opens as a draft (the form check is named as failed, never passed).

## Foundation entries

Each entry this request writes or changes, with one English sentence of its meaning. No invariant test, surface or *Violated* mark changes. No kept row was tied to an entry already stated. No entry is marked `the cycle's`: all three come from rows of the task.

1. **WAY-293 (new), row 1.** Where a task or its spec explicitly excludes an entry in the foundation for a choice, that exclusion prevails over the rule that a choice binding after the merge is written into the foundation, and the choice stays a row of the cycle record's questions table, narrowing WAY-22 and WAY-18 in that area; a candidate left out of a task's settlements to record is no exclusion.
2. **WAY-05 (changed), row 2.** A decision's rationale and rejected options may give a measurement the choice rests on, with what was measured and under which conditions and never as a general bound; the ban on counts protects decisions from history and chronicle that the reader does not need.
3. **WAY-148 (changed), row 3.** A stage returns a one-line check result only where it runs a test or another check of the product, so the designer and the reviewer of a spec return no check result.

## Minor findings

1. **The new example pair is merged into the old pair instead of standing as a new pair.** M1 of the whole-change review, at `3023f60`, `foundations/decisions.md:141-146` (WAY-05 *Verification*): "To do 2, fourth bullet, asks for a new pair, `complies: …; violates: …`. The change appends the new example to the existing `complies:` line (after a `;`) and the new counter-example to the existing `violates:` line. The labels `complies:` and `violates:` therefore no longer open the task's two sentences, and the first line now lists two unrelated examples (a template field; a rationale with a measurement)." The reviewer adds that the meaning is intact, and that the author's reason does not hold, since WAY-29 already holds two pairs (`foundations/decisions.md:747-754`) and `foundation_check.py` accepts them.
2. **The new decision's rationale tells what the request template lacks today.** M2, at `3023f60`, `foundations/decisions.md:8818-8826` (WAY-293 *Rationale*): "WAY-05's binding sentence (as the same change words it) bars, in the entry author's own prose, "what the process's own tools do or lack today". The sentence describes what the request template does today and what it has no line for. The source is the task's *Context* bullet, but a *Context* bullet is not a quoted source of the entry, and the wording is the author's." The reviewer calls it small and borderline, since the sentence is also the cost of the decision.
3. **The new decision's second rejected way reads "no change, which withdraws the rule".** M3, at `3023f60`, `foundations/decisions.md:8830` (WAY-293 *Rejected*): "the task keeps two ways here, "no change" (question 1, way C) and "withdraw point 1" (critique, way c); the entry folds them into one and words it as "no change, which withdraws the rule". Read cold, it says that making no change withdraws an existing rule; what is meant is that making no change leaves the return step without the precedence." Merging the two ways is a fair reading; only the gloss misleads.
4. **Two rewrapped paragraphs are left uneven.** M4, at `3023f60`, `foundations/decisions.md:3896-3899` and `elements/decisions/template.md:57`: "WAY-148 binding sentence: a short line "in its report. The handoff names what the agent reads, as the" and `elements/decisions/template.md:57` (110 characters, the longest of the added lines; the file already holds longer ones, so no rule is broken)." Polish only; the next edit of either paragraph produces a noisier diff.

## Findings outside the task's scope

1. **The planner's return still names a check result, while WAY-148 now asks for it only where the stage runs a check "of the product".** O1 of the whole-change review, at `3023f60`, `task-cycle/plan/SKILL.md:202-203` against `foundations/decisions.md:3896`: "The planner runs the size script over its plan's slices (`task-cycle/plan/SKILL.md:184-190`), a check of the plan, not of the product. After the approved wording it is unclear whether the planner returns a result. The task limits the change to the spec stage and the wording was approved with the document (WAY-30), so I do not grade it against the change; it is a gap the wording opens, for the human who accepts decisions to settle (a word in WAY-148, or a line in `plan/SKILL.md`)." The author names the same place in its own reports.
2. **A test fixture still quotes the old first sentence of WAY-148.** Declined to judge by the reviewer, no grade: "`task-cycle/test_request_check.py:60-62` quotes the old sentence of WAY-148 in a made-up task document used as a fixture; no test compares it with the log (outside the task; harmless)."

## Course of the cycle

- **Task and sources:** "the way: poprawki z uwag cykli (ai-review S7), partia 2026-11-05", an independent task, from `zadanie_the_way_poprawki_z_uwag_cykli_2026_11_05.md` in the author's notes, `Status: ready for cycle`, answers of 2026-11-05; its citations stand at `foundations` `61c72fb`. It takes up four nightly-review cases (AIR-585, AIR-586, AIR-587, AIR-592).
- **Process pin:** none; the-way working on itself, the process root this worktree.
- **Spec:** none. The task leaves no open design choice: the *To do* items give the wording of each edit and rows 1–3 of *Settlements to record* settle the three entries.
- **Route:** one author without a plan, class `same` (Sonnet 5.5): a change of eight files that rewords approved decisions and writes one that narrows two others, where a slip would change the meaning.
- **Plan:** none.
- **Choices:** eight other choices (Q1, Q2 and Q4–Q9) in the questions table of the record's `cycle.md`; Q3 stands above as item 1 of *For you to decide*.
- **Blocking findings left:** none.
- **Record:** the cycle's record at the commit that adds it, `RECORD_SHA`: https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/cycle-remarks-batch-2 (`cycle.md` for the log, `reports/` for the handoffs and reports).
