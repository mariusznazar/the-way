**State: ready** — one item below asks whether to make a task of a rule that two older decisions pull the other way; merging without an answer lets it through, and what you accept by merging is listed under it.

## What you will see

The-way gets one new rule for its own scripts. A script that reads a file written by an agent or by you now has to check that the file holds each field the script needs, and when one is missing or has another name, it has to stop with an error that names the field. It must not guess, and it must not take a missing field for an empty value. A field is anything the script looks for data by: a section heading, a row label, a table column or a JSON key.

The rule covers every script that a change adds. In a script that a change changes, it covers the whole reading of each file whose way of reading the change reworks: all fields of that file, but no other file and no other part of the script. A script that exists to check the form of a file keeps listing a missing field it checks as a finding; every other script stops with a message that names the file and the field. Each covered reading of a file gets one test that gives the file without one field and checks that the failure names that field; the review of the change answers for the other fields. The rule says nothing about the scripts that exist today, and reviewing them stays outside this request.

The rule stands as a decision of its own beside the one that releases the-way from the general coding and testing guidelines of a product. It is not an exception written into that decision, and not a rule about every tracked script on every commit. Its reach names all parts of the map of the-way, and a change that adds a part to the map adds it there too.

### Underneath

Only the decision log changed: one new entry, no script, test or skill. The idea comes from the example in the course lesson, where a script that checked its fields stopped with "Missing issues.due" after the source renamed `due` to `due_date`, and the script that did not check read the missing field as "no due date" and gave a wrong report for two days.

## For you to decide

### Needed from you

none

### Fix or let through

1. The new rule says a script must stop with an error when a field is missing. While this change was being made, the target branch gained the decisions of the weekly audit of the process, and three of them make an absence a normal, defined result: a cycle whose record names no version counts as "no version", the share of fix rounds is "unknown" where the records cannot tie a round, and a missing `repository` entry in your locations file falls back to the checkout that runs the count. Two older promises in the map of parts, that the private-paths check and the reader of a plan's state keep their exit codes, can clash with the new rule in the same way. Nothing is wrong today, because the rule binds only a script that a change adds or reworks and no script changes here. The trouble shows at the first change that reworks how the audit script reads those files: the agent will meet two instructions pointing opposite ways and must break one of them, either the audit's "no version" result or the new rule. Three ways are open. Fixing it in this request adds an exception to the new rule, such as "except a field that a decision of the-way lets be absent and says what the script does then"; it costs a correction with a review, and it changes the meaning of an approved decision beyond what you settled in the task, so you would choose here which absences count as allowed. Making a task of it costs one task, and the refinement settles the wording; until then the tension stands and shows at the first change to those scripts. Letting it through costs nothing today and is the same as the task without the task: whoever meets it first has to find it again. I recommend making a task, since the wording of the exception decides which missing fields are legitimate, which is yours to settle, and no script is at risk until one changes. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1 and 2.)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The reach of the new decision names 17 parts, not the 16 your task counted. While the change was made, the target branch added a part for the audit of the process to the map, and your own rule in the task is that the reach names every part of the map and that a new part is added to it. The cycle added that part. The other way, leaving it at 16, would have broken that rule on the day of the merge. For the same reason the entry has the next free number after the audit's decisions, not the one it was first written under.
3. The cycle wrote three things in the new decision that none of your four settled rows carries, and you see them first now. First, a pair of examples that an agent compares a change against, written from your own case (the renamed `due` key) and from the rows: what complies, such as a new script that stops with a message naming the file and the key, and what violates, such as a script that reads the absent key as "no due date". Second, a link marking the decision as descending from the one that keeps the scripts to the standard library, because your task calls it a rule of the same family and the quiet pass that decision forbids is the very reason for this one; the other choice, no link, would have hidden the family. Third, a closing sentence of the reasoning saying that tests of a script's behaviour stand without an invariant, because the older decision says tests live only with invariants and concerns how a decision is checked. The older decision itself is unchanged, and still reads, in its letter, as if it forbade the test this rule requires; narrowing its wording is a separate change.

## Cost

About 28 minutes of working time, 15 of them without the waits for tools, and about 17.7 million tokens, all on one model family: one author, a review of the whole change, a fix of two of its four Minor findings (the other two stand in the lower part) with a review of the fix, a review of the merge with the target branch, and a return step that had nothing to correct. No review failed. The full table of stages stands in the record: `stages.md` in the committed record.

## How to merge

Merge with a merge commit, which keeps the commits; the link to the record survives only then. The foundation has waited for a review through 24 merges since the last tag, below the threshold of 30, so nothing is asked of you here.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — jedna pozycja niżej pyta, czy założyć zadanie na regułę, z którą dwie starsze decyzje się rozchodzą; scalenie bez odpowiedzi przepuszcza ją, a to, co akceptujesz scaleniem, jest wypisane pod nią.

## Co zobaczysz

The way dostaje jedną nową regułę dla własnych skryptów. Skrypt, który czyta plik pisany przez agenta albo przez Ciebie, musi teraz sprawdzić, czy plik ma każde pole, którego skrypt potrzebuje, a gdy którego brakuje albo stoi pod inną nazwą, ma się zakończyć błędem z nazwą tego pola. Nie wolno mu zgadywać ani brać braku pola za wartość pustą. Polem jest każda rzecz, po której skrypt szuka danych: nagłówek sekcji, etykieta wiersza, kolumna tabeli albo klucz JSON.

Reguła obejmuje każdy skrypt, który zmiana dodaje. W skrypcie, który zmiana zmienia, obejmuje cały odczyt każdego pliku, którego sposób czytania zmiana przerabia: wszystkie pola tego pliku, ale nie inne pliki i nie inne części skryptu. Skrypt, który istnieje po to, by sprawdzać formę pliku, nadal wypisuje brakujące pole, którego obecność sprawdza, jako ustalenie; każdy inny skrypt kończy się komunikatem z nazwą pliku i pola. Każdy objęty odczyt pliku dostaje jeden test, który podaje plik bez jednego pola i sprawdza, że błąd podaje nazwę tego pola; za pozostałe pola odpowiada przegląd zmiany. Reguła nie mówi nic o skryptach, które istnieją dziś, a ich przegląd zostaje poza tym requestem.

Reguła stoi jako osobna decyzja obok tej, która zwalnia the way z ogólnych wytycznych kodowania i testów produktu. Nie jest wyjątkiem dopisanym do tamtej decyzji ani regułą o każdym śledzonym skrypcie na każdym commicie. Jej zakres wymienia wszystkie części mapy the way, a zmiana, która dodaje część do mapy, dopisuje ją też tam.

### Pod spodem

Zmienił się tylko dziennik decyzji: jeden nowy wpis, żadnego skryptu, testu ani skilla. Pomysł pochodzi z przykładu z lekcji kursu, gdzie skrypt sprawdzający swoje pola zatrzymał się z błędem „Missing issues.due”, gdy źródło zmieniło `due` na `due_date`, a skrypt niesprawdzający wziął brak pola za „brak terminu” i przez dwa dni dawał zły raport.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawienia albo przepuszczenia

1. Nowa reguła mówi, że skrypt ma się zatrzymać z błędem, gdy brakuje pola. W trakcie tej zmiany gałąź docelowa dostała decyzje tygodniowego audytu procesu, a trzy z nich czynią brak pola normalnym, określonym wynikiem: cykl, którego zapis nie podaje wersji, liczy się jako „bez wersji”; udział rund poprawek jest „nieznany”, gdy zapisy nie pozwalają powiązać rundy; brakujący wpis `repository` w Twoim pliku lokalizacji wraca do checkoutu, który liczy. Dwie starsze obietnice w mapie części, że kontrola prywatnych ścieżek i czytnik stanu planu zachowują swoje kody wyjścia, mogą kolidować z nową regułą tak samo. Dziś nic nie jest zepsute, bo reguła obejmuje tylko skrypt, który zmiana dodaje albo przerabia, a żaden skrypt się tu nie zmienia. Kłopot ujawni się przy pierwszej zmianie, która przerobi odczyt tych plików w skrypcie audytu: agent trafi na dwie instrukcje idące w przeciwne strony i będzie musiał złamać jedną z nich — albo wynik audytu „bez wersji”, albo nową regułę. Są trzy drogi. Poprawka w tym requeście dopisuje do nowej reguły wyjątek, np. „z wyjątkiem pola, które decyzja the way pozwala pominąć i mówi, co skrypt wtedy robi”; kosztuje korektę z przeglądem i zmienia znaczenie zatwierdzonej decyzji ponad to, co rozstrzygnąłeś w zadaniu, więc tu wybierałbyś, które braki są dozwolone. Założenie zadania kosztuje jedno zadanie, a doprecyzowanie ustala brzmienie; do tego czasu napięcie stoi i pokaże się przy pierwszej zmianie tych skryptów. Przepuszczenie nic dziś nie kosztuje i jest tym samym co zadanie bez zadania: kto trafi pierwszy, musi to znaleźć od nowa. Rekomenduję założyć zadanie, bo brzmienie wyjątku rozstrzyga, które brakujące pola są uprawnione, a to należy do Ciebie, i żaden skrypt nie jest zagrożony, dopóki któryś się nie zmieni. Poprawić w tym requeście, założyć zadanie, czy przepuścić? (Uwagi poza zakresem zadania, 1 i 2.)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Zakres nowej decyzji wymienia 17 części, nie 16, jak policzyło Twoje zadanie. W trakcie zmiany gałąź docelowa dodała do mapy część dla audytu procesu, a Twoja reguła z zadania mówi, że zakres wymienia każdą część mapy i że nowa część się do niego dopisuje. Cykl dopisał tę część. Druga droga, zostawienie 16, złamałaby tę regułę w dniu scalenia. Z tego samego powodu wpis ma kolejny wolny numer po decyzjach audytu, a nie ten, pod którym został napisany najpierw.
3. Cykl zapisał w nowej decyzji trzy rzeczy, których nie niesie żaden z Twoich czterech rozstrzygniętych wierszy, i widzisz je dopiero teraz. Po pierwsze, parę przykładów, z którymi agent porównuje zmianę, napisaną z Twojego przypadku (zmieniony klucz `due`) i z wierszy: co spełnia regułę, np. nowy skrypt kończący się komunikatem z nazwą pliku i klucza, a co ją łamie, np. skrypt czytający brakujący klucz jako „brak terminu”. Po drugie, powiązanie oznaczające, że decyzja wywodzi się z tej, która ogranicza skrypty do biblioteki standardowej, bo Twoje zadanie nazywa to regułą z tej samej rodziny, a ciche przepuszczenie, które tamta decyzja zakazuje, jest właśnie powodem tej; druga droga, brak powiązania, ukryłaby rodzinę. Po trzecie, zamykające zdanie uzasadnienia, że testy zachowania skryptu stoją bez niezmiennika, bo starsza decyzja mówi, że testy żyją tylko przy niezmiennikach, a dotyczy sprawdzania decyzji. Sama starsza decyzja jest bez zmian i dosłownie nadal brzmi tak, jakby zakazywała testu, którego ta reguła wymaga; zawężenie jej brzmienia to osobna zmiana.

## Koszt

Około 28 minut czasu pracy, z tego 15 bez czekania na narzędzia, i około 17,7 miliona tokenów, wszystko na jednej rodzinie modeli: jeden autor, przegląd całości zmiany, poprawka dwóch z jej czterech uwag Minor (pozostałe dwie stoją w dolnej części) z przeglądem poprawki, przegląd scalenia z gałęzią docelową i krok powrotu, który nie miał czego poprawiać. Żaden przegląd nie zakończył się odrzuceniem. Pełna tabela etapów jest w zapisie cyklu: `stages.md` in the committed record.

## Jak scalić

Scal commitem scalającym, który zachowuje commity; link do zapisu cyklu przeżywa tylko tak. Fundament czekał na przegląd przez 24 scalenia od ostatniego tagu, poniżej progu 30, więc nic tu od Ciebie nie jest wymagane.

</details>

## Technical changes

The change is one commit, a fix commit and a merge, then the record's pair. Each paragraph opens with what it means for someone working with the process.

- `4905a56` — the rule is written down as a decision of the-way's log: a script that reads a file checks the fields it needs and fails with the field's name. The entry is `WAY-344` in `foundations/decisions.md` (written as WAY-330 and renumbered by the merge); its *Scope* names every part of the map, its *Relations* line derives it from WAY-38, and its *Rejected* keeps the ways the task left unchosen with their costs.
- `5922ffc` — the one fix for the four Minor findings of the review of the whole change: the *Verification* "violates" example now carries the qualification of the binding sentence, and the *Rejected* clause on a new exit code no longer states what the skills know today. The other two findings were left, as their reviewer suggested; they stand below.
- `c32cfe1` — the merge of `origin/foundations`, which had moved from `e9a0f92` to `3bcad13` while the cycle ran. Both sides had appended entries after WAY-329 in `foundations/decisions.md`; the target's entries WAY-330…WAY-343 (the audit of the process) stay as they were, and this entry takes the next number, WAY-344. Because the target added the part `process-audit` to the part map, the entry's *Scope* gained it; the *Scope* equals the 17 parts of `foundations/part_map.md` as sets.
- The record of the cycle is added by one commit and removed by the next, so that the target branch never holds it.

## Checks

- Gate on the final tree `c32cfe1`: `python -B gate/run_tests.py`, exit 0, 1066 tests in 10 directories, every directory passed. Before the merge, on the reviewed tree `5922ffc`: exit 0, 919 tests in 9 directories. On the base `e9a0f92`, in a separate checkout: exit 0, 919 tests in 9 directories. No check failed or did not run.
- `python -B elements/common/foundation_check.py`: exit 0, "0 errors", run by the author after the entry, after the fix, after the merge (by the orchestrator) and by each reviewer.
- Own-work check of the author: a one-off run that compared the entry's *Scope* with the parts of `foundations/part_map.md` as sets (16 at the time, equal), searched the binding sentences for *should*, *will* and RFC 2119 capitals, and for carriage returns; exit 0. The orchestrator ran the same comparison after the merge: 17 and 17, equal. They are reading and a script of the moment, not tests; the change writes no test and no invariant.
- Reviews: whole change `PASS` (0 blocking, 4 Minor within the task, 2 outside); the fix of the Minor findings `PASS`; the reconciliation with the target branch `PASS` (0 blocking, 1 Minor, outside the task). The return step committed nothing, so it had no review. The review of the whole change read 40 decisions whole and 248 by title only, and named none as unread that bears on the change.
- Process remarks check, on the original record: `python -B task-cycle/remarks_check.py .runs/task-cycles/scripts-fail-on-missing-fields`, exit 0 on the second run (the first run, exit 1, listed 5 items, which were then appended to the remarks).
- Form check of this description, check of private paths on it, and the checks on the copy of the record: pending the last runs.
- Not checked: whether the part map's promise that two surfaces keep their exit codes still holds under a later script that gives exit code 2 for a missing field; no script changes here.

## Foundation entries

- WAY-344 (rows 1, 2, 3, 4; the cycle's for the *Verification* examples, the relation to WAY-38 and the last sentence of the *Rationale*): a script of the-way that reads a file an agent or a human writes checks the fields it needs and ends with an error naming a missing or renamed field, never guessing or reading the absence as an empty value; the rule binds a script a change adds and, in a changed script, the whole reading of each file whose way of reading the change reworks; a missing field gives exit code 2 with file and field, except in a script that checks the form of a file, where it is a finding with exit code 1; each covered reading has one test that gives the file without one field; the *Scope* names every part of the map and a new part is added to it.
- Rows of *Settlements to record*: row 1 → WAY-344 (form and reach), row 2 → WAY-344 (the test), row 3 → WAY-344 (exit codes), row 4 → WAY-344 (what a field is). No invariant, environment fact, glossary term or part-map entry was written or changed.

## Minor findings

Unfixed Minor findings within the task, with the reviewers' words.

1. Review of the whole change, `foundations/decisions.md`, last sentence of the *Rationale* of WAY-344: "it states, in prose, how an agent is to read WAY-12 against the test this entry requires; WAY-05 puts what a decision forces on later work in a binding sentence or a field, never in prose, and WAY-12 itself still says "tests live only with invariants" with no relation to this entry. […] Suggested: keep the sentence, name it in the request's section for the human's decisions as the cycle's wording, and leave a narrowing of WAY-12's wording to a separate change." It stands in *You accept by merging*, 3.
2. Review of the whole change, the relation and the pair of examples: "the writer's own additions (the relation `derives from WAY-38`, the pair of examples, the WAY-12 sentence) are not carried by any row. […] WAY-32 defines `derives from` as "a higher decision this one serves", which is a stronger claim than "same family", though the *Rationale* does rely on WAY-38's quiet-pass sentence, so the relation is defensible. […] Suggested: that naming; no change to the entry." It stands in *You accept by merging*, 3.
3. Review of the fix, the clause on a new exit code in *Rejected* of WAY-344: "The tail that went with it — "and until then each orchestrator would read an unknown code its own way, in exchange for a signal that exit code 2 already gives" — is the other half of the cost the task keeps beside this *Not chosen* way […]. What is left ("would have to be extended") is a true but weaker cost, and the reason that exit code 2 already gives the signal no longer stands in the entry. […] Suggested, for a later pass if the human wants the task's wording whole: restore "until then each orchestrator would read an unknown code its own way, in exchange for a signal that exit code 2 already gives" after "extended"; it states no present fact about the skills." (new Minor within the task, found by the review of the fix).

## Findings outside the task's scope

1. Review of the whole change: "The part map's surfaces `tracked-private-paths-command`, `project-plan-state-command` and `foundation-check-command` (`foundations/part_map.md:197-217`) promise to keep "its exit codes". A later change that gives one of those scripts exit code 2 for a missing field changes what the surface promises; WAY-49 governs that, and WAY-330 states nothing about existing scripts." It stands in *Fix or let through*, 1.
2. Review of the reconciliation with the target branch: "WAY-344 has no clause for a field that a decision of the audit lets be absent (`foundations/decisions.md:11307`, the sentence "ends the script with an error that names it, never guessing and never reading the absence as an empty value", with WAY-343 at `:11281`, WAY-337 at `:11112`, WAY-342 at `:11247`). […] a later change that reworks the audit script's reading of the locations file or of a cycle record would be bound by WAY-344 to exit 2 at that field, and WAY-344's *Verification* "violates" list […] would read as forbidding what WAY-343 and WAY-342 require. […] Resolution is not mine: adding a clause such as "except a field that a decision of the-way lets be absent and says what the script does then" changes the meaning of an approved decision beyond what the task settles (WAY-114), so it goes to the human, or is left for the first change that reworks the audit script. Not blocking." It stands in *Fix or let through*, 1.
3. Review of the whole change: "A word: "field" in WAY-330 (a thing a script looks for data by in a file) and "field" of an entry (*Scope*, *Based on*; WAY-71, invariant `map-reference-target`) are two uses in one foundation, and the glossary holds no entry for it. WAY-330 defines its use in its own binding sentence, and I found no sentence a reader would read wrongly for lack of an entry (WAY-297), so Minor and not in the task's reach."
4. Declined to judge by the review of the whole change, from the author's report: `task-cycle/remarks_check.py` lists nothing and exits 0 when a record has no `reports/` directory; an existing script, outside the task, not verified by any reviewer.

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes, `Status: ready for cycle`, settlements accepted 2026-11-11; goal: the-way's scripts check the fields they read and fail with the field's name. No human action. Source: the task document, frozen in the record; base `e9a0f92`.
- **Process pin:** not applicable; the cycle ran on the-way's own checkout and the task moves no pin.
- **Spec:** none; no open design choice at the start: the four settlements settle the decision's form, reach, check and exit codes.
- **Route:** one author without a plan, on the same class as the orchestrator (Sonnet 5.5), because the entry binds the later scripts of every part and a wrong *Scope* or *Relations* would pass the form check unseen; the review of the whole change by a fresh agent, one fix for its Minor findings with a review of the fix, the return step (no commit, so no review), then the merge with the moved target branch and its review.
- **Plan:** none.
- **Choices:** 4 other choices, in the record's questions table: `cycle.md` in the committed record.
- **Blocking findings left:** none.
- **Record:** pending the commit that adds it
