**State: ready** — nothing waits for your answer; the full tests are green on the final tree.

## What you will see

The work with the process changes in one respect, all of it instructions and one new decision; no product code changes.

- When an agent refines a task, it now looks for one particular kind of trap: a word in the task document, or in the sentences the task's required result rests on (the decisions of the foundation the document quotes and the sentences of the approved project definition), that can be read two ways, where the two readings would make the product behave differently. If no approved source and no glossary entry settles which reading holds, the agent shows you a short example from the task's scope — "under reading A this happens, under reading B that" — and asks which reading holds. Your answer goes under the task's *Questions to settle*, like any other answer of the refinement.
- The check is bounded so that it does not invent cases. A case counts only where a sentence that really stands in the document or in such a source allows both readings and the two readings give a different result you could observe inside the task's scope. A reading no sentence allows, or a scenario outside the task, raises no question. The check has no duty to find anything and no number of cases to show; where it finds nothing, the agent says nothing about it.
- A meaning you settle that a reader who knows the product's field would not give the word goes on to the task's list of what its refinement settles, as a candidate for the glossary, as it does today; the check itself changes no glossary. A word that the glossary already settles raises no question. An ambiguity inside the approved project definition goes back to the definition and its readiness check only where settling it would change the definition.

### Underneath

One new paragraph in the step of the refinement that resolves the gaps, one line in the list of that step, and one new decision that adopts the practice from a lesson of an outside course on planning with an agent (probing the terms a request leaves undefined with the smallest case in which two readings differ), names where it applies and why. The trial of a list of decisions with their sources marked, which aims at a wider class of the same problem, is a separate task and is not part of this one.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. The new decision cites the outside course in its reasoning in words and quotes no passage of it. The repository holds no passage of the lesson, and your task gave only a paraphrase, so the author followed the two earlier decisions that adopt a lesson of the same course: the course is named in the reasoning, and the line that lists what the decision rests on stays empty. I did not write a placeholder to be filled later, since nothing in the repository could fill it. If you want a quoted passage there, it needs the text of the lesson from you.

## Cost

About 28 minutes of working time in the stages, plus 11 minutes for the full test run, and about 16 million tokens, all on one model family; one fix round (the review of the whole change failed once, because the new decision and the new instruction said different things about an ambiguity inside the approved project definition; the fix passed its review). Table of stages: the committed record, `stages.md`.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation has waited for a review through 46 merges since the last review, tagged 2026-11-06; the review is the skill `the-way-review-foundation`, started in a session in this repository; nothing in this request waits for it.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — nic nie czeka na Twoją odpowiedź; pełne testy są zielone na końcowym drzewie.

## Co zobaczysz

Praca z procesem zmienia się w jednym miejscu; wszystko to instrukcje i jedna nowa decyzja, kod produktu się nie zmienia.

- Gdy agent doprecyzowuje zadanie, szuka teraz jednej konkretnej pułapki: słowa w dokumencie zadania albo w zdaniach, na których stoi wymagany wynik zadania (przytoczone decyzje fundamentu i zdania zatwierdzonej definicji projektu), które da się rozumieć na dwa sposoby, gdy te dwa odczyty sprawiłyby, że produkt zachowa się inaczej. Jeśli żadne zatwierdzone źródło ani wpis słownika nie rozstrzyga, który odczyt obowiązuje, agent pokazuje Ci krótki przykład z zakresu zadania — „przy odczycie A dzieje się to, przy odczycie B tamto" — i pyta, który odczyt obowiązuje. Twoja odpowiedź trafia pod *Questions to settle* zadania, jak każda inna odpowiedź doprecyzowania.
- Sprawdzenie ma granicę, która chroni przed wymyślaniem przypadków. Przypadek liczy się tylko wtedy, gdy zdanie, które naprawdę stoi w dokumencie albo w takim źródle, dopuszcza oba odczyty i oba dają różny wynik, który dałoby się zaobserwować w zakresie zadania. Odczyt, którego żadne zdanie nie dopuszcza, i scenariusz spoza zadania nie rodzą pytania. Sprawdzenie nie ma obowiązku niczego znaleźć ani liczby przypadków do pokazania; gdy nic nie znajdzie, agent nic o nim nie mówi.
- Znaczenie, które rozstrzygniesz, a którego czytelnik znający dziedzinę produktu by słowu nie nadał, idzie dalej na listę tego, co doprecyzowanie zadania ustala, jako kandydat do słownika, tak jak dziś; samo sprawdzenie nie zmienia żadnego słownika. Słowo, które słownik już rozstrzyga, nie rodzi pytania. Niejasność wewnątrz zatwierdzonej definicji projektu wraca do definicji i jej kontroli gotowości tylko tam, gdzie jej rozstrzygnięcie zmieniłoby definicję.

### Pod spodem

Jeden nowy akapit w kroku doprecyzowania, który zamyka luki, jedna linijka na liście tego kroku i jedna nowa decyzja, która przejmuje praktykę z lekcji zewnętrznego kursu o planowaniu z agentem (sondowanie terminów, których prośba nie definiuje, najmniejszym przypadkiem, w którym dwa odczyty dają różny wynik), nazywa, gdzie obowiązuje, i dlaczego. Próba spisu decyzji z oznaczeniem źródła, która celuje w szerszą klasę tego samego problemu, jest osobnym zadaniem i nie wchodzi w to.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

none

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

1. Nowa decyzja przywołuje zewnętrzny kurs w uzasadnieniu własnymi słowami i nie cytuje żadnego fragmentu. Repozytorium nie zawiera fragmentu lekcji, a zadanie podało tylko parafrazę, więc autor poszedł za dwiema wcześniejszymi decyzjami, które przejmują lekcje tego samego kursu: kurs jest nazwany w uzasadnieniu, a wiersz o tym, na czym decyzja stoi, zostaje pusty. Nie wpisałem miejsca na uzupełnienie później, bo nic w repozytorium nie mogłoby go uzupełnić. Jeśli chcesz tam cytowanego fragmentu, potrzebny jest tekst lekcji od Ciebie.

## Koszt

Około 28 minut pracy w etapach, plus 11 minut pełnego przebiegu testów, i około 16 milionów tokenów, wszystko na jednej rodzinie modeli; jedna runda poprawek (przegląd całej zmiany raz dał wynik negatywny, bo nowa decyzja i nowa instrukcja mówiły różnie o niejasności wewnątrz zatwierdzonej definicji projektu; poprawka przeszła swój przegląd). Tabela etapów: zapis cyklu w repozytorium, `stages.md`.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Fundament czeka na przegląd przez 46 scaleń od ostatniego przeglądu, oznaczonego 2026-11-06; przegląd to umiejętność `the-way-review-foundation`, uruchamiana w sesji w tym repozytorium; nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

The change adds the check of a word read two ways to the refinement of a task and the decision that adopts it. It touches the instruction files of the refinement and the decision log; no script, test or generated file changes.

- `9c66ee1` — adds WAY-374 ("Does the refinement of a task ask about a word its sources leave readable in two ways?", *Scope* `project-level`, derives from WAY-100); adds three paragraphs to `project-level/task/skill/resolve_gaps.md` (what is searched and what settles a word; what counts as a case, the example and the question; the glossary candidate, the approved definition and the absence of any duty to find); adds the check to the list of section 3 of `project-level/task/skill/SKILL.md`.
- `187bbde` — the fix of the review of the whole change: brings the decision and the skill to one condition for an ambiguity of the approved definition (it goes back to the definition and its gate only where settling it changes the definition; finding I-1), re-wraps the lines the change left over 100 characters in the skill and in the entry (M-1, M-2), says "after the model of" for the WAY-99 reference (M-3), adds that WAY-95 judges the glossary candidate (M-4), names the section "How a skill asks" and splits the long paragraph into three (M-5).
- The return step changed nothing: no commit, so no review of it. `project-level/task/skill/orchestrated_mode.md`, the template of a task, the glossary, WAY-95 and the skill's description are not changed.

## Checks

1. The gate, `python -B task-cycle/gate_times.py --output .runs/task-cycles/resolve-gaps-two-meanings/gate_times.md -- python -B gate/run_tests.py`, on `187bbde`, the final tree (`origin/foundations` had not moved, so no merge): exit 0; 1328 tests in 10 directories, 657.8 s, every directory passed, no other gate of the-way at the same time. The list of tests failing before the change was taken from the final gate of the merged branch of the previous cycle (`docs/task-cycles/agent-work-copies-in-task-directory/cycle.md` in commit `b7f4c3f`): none failing, 1328 tests; the base is a merge whose tree equals that of its second parent, so no gate ran on the base.
2. `python -B elements/common/foundation_check.py` on `187bbde`, without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line. Focused runs of the author and the reviewers: `gate/run_tests.py` for `project-level` (275 tests), `elements/common` (201), `instruction-files` (104, 5 skipped by the tests), `agent-instructions` (25) and `task-cycle` (394), each exit 0; `python -B instruction-files/check_instructions.py .`, exit 0, `0 error, 0 warn, 3 info`.
3. Own-work checks: the author's, `grep` of the diff for the words of the trial of a list, of private notes and of counts of the register (`D8|trial|loop2|mapa|usprawnien|register|\.md\]\]`), exit 1 (no match, as wanted), and a reading of each way not chosen of the entry against the task's questions; the fix's, a reading of `git diff 9c66ee1 HEAD`: only the findings' changes. What they cannot show: whether an agent given the check asks the right questions and stays silent otherwise; the next refinements show that, in the register of problems of the audit.
4. Not run: no review of the return step (it made no commit); no run of the generator of skill entry points (no skill's description changed); no test was written, since the change is instruction text and one decision, and no test cites the sentences changed.
5. Working copies: each agent reported where its copy stood — the reviewer's worktree of the head, twice, removed, and a temporary test-output file of the author, removed; the author made none for the return step — and no remainder was named.
6. The form check, `python -B task-cycle/request_check.py .runs/task-cycles/resolve-gaps-two-meanings/request.md --task .runs/task-cycles/resolve-gaps-two-meanings/task.md`, and the check of private paths on this description, `python -B task-cycle/private_paths_check.py .runs/task-cycles/resolve-gaps-two-meanings/request.md`: written and checked after the record's commit. The remarks check on the original, `python -B task-cycle/remarks_check.py .runs/task-cycles/resolve-gaps-two-meanings`: exit 1 listing 6 items, then exit 0 after they were appended to the process remarks, 2 runs. The remarks check, the check of private paths and the check of image files on the copy of the record: filled in when the record's link is added.

## Foundation entries

1. WAY-374 (`row 1`) — at its step that resolves the gaps, the refinement of a task asks the human which reading holds where a word of the task document or of the sentences its result rests on allows two readings that give different observable results inside the task's scope and no approved source settles it, and says nothing where it finds no such word.

No invariant, its test or its surface changes and no *Violated* mark is set; the foundation check lists nothing.

## Minor findings

Minor finding that no fix made, from the review of the fix of the whole change (`PASS 187bbde67c221a847f53e693d4c75d94f51a3e3a`), in the reviewer's words:

1. `project-level/task/skill/resolve_gaps.md`, the end of the third paragraph of the check: "lines of the check hold one remaining sentence "The check owes no finding and no number of cases; where it finds none, say nothing of it" at the end of the paragraph about the glossary and the definition, now separated from the paragraph that states what counts; a reader finds it, but it fits the second paragraph better. Cosmetic."

The five Minor findings of the review of the whole change (a line left at 142 characters in the skill, five over-long lines in the entry, "sets" where the entry only follows a model, the missing mention that the glossary candidate is judged by the rule of glossary entries, the section "How a skill asks" not named) were fixed in `187bbde` and the review of the fix found them fixed.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the refinement of a task asks about a word its sources leave readable in two ways before the agent chooses alone; independent task, no project; sources: the task document (settlement row 1 accepted 2026-11-14, answers of the five questions given through the advisor of the day) and the foundation at `f4af75d`.
- **Process pin:** this checkout of the-way is the repository changed; base `f4af75d` of `foundations`; no pin moved; the gate on the final tree is in Checks, 1.
- **Spec:** none; no open design choice at the start (*Questions carried to cycle* reads `none`).
- **Route:** one author without a plan, class `same` (the entry's wording and the check's boundary are the whole product), a fix and a review of the fix after one `FAIL`, the return step found nothing; the review of the whole change read 17 of the 81 decisions whose scope names the refined part whole, and two more the task names, and ran through 64 by title, naming none of them as bearing on the change; the one file of the step it did not read, the one that finds what a refinement settles, the reviewer of the fix read whole.
- **Plan:** none.
- **Choices:** 5 entries in the questions table of the record: the route, the class of the author, the form of the citation of the course (item 1 above), and two on unread material of reports that the cycle judged bore on nothing it judged or closed in the review of the fix.
- **Blocking findings left:** none.
- **Record:** written after the record's commit.
