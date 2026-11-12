**State: ready** — one item below asks whether to fix, make a task of, or let through a small difference in how the count treats a missing level; merging without an answer lets it through, and what you accept by merging is listed under it.

## What you will see

The register of problems that the weekly audit reads now holds, for every problem, a second grade beside its weight: how much one occurrence of that problem cost. The grade is one of five fixed levels, each dearer than the one before: `nothing` (the occurrence cost nothing: a confirmation, or a remark without effect), `steps` (a few steps of one agent in its own stage, which the agent put right itself), `stage` (a stage or a large part of it done again, or a large extra reading or check by the same agent), `round` (an extra run of an agent: a round of fixes, an extra reconciliation with the target branch, a new review, a piece of work redone) and `human` (your time: a question, a decision, a manual check, a fix after the merge). A problem gets the highest level its real cost reached; what could have happened stays the business of its weight. The template of the register has the new column and a table of the five levels with their meanings, which you may adapt, but the levels themselves you cannot change.

The counting command reads the new column and refuses a problem whose cost is none of the five levels, the same way it refuses an unknown weight. Its result gets one new section: for every matter (issue) of the register, fixed, open or dropped, it says how many of that matter's problems stand on each level of cost. The audit skill shows you this row beside each matter as material to weigh; it sets no priority and no order from it.

The command also stops now, with an error that names the missing heading, table or column and with exit code 2, when the register lacks one of them. Before, a register without a table gave exit code 1 and a result written without it.

Your own copy of the register is brought up to date in this same piece of work, at your request: it has the new column and the new table, and each of its 100 problems has a cost, proposed from the records of the six cycles they come from and decided by you in a table. The setup of the nightly session now knows the column too: its instructions and the playbook describe the cost, and the script that keeps the register's table of issues expects the new column. The count was run on your updated register with results written to a scratch folder: it ended with exit code 0 and refused no row.

The branch was brought up to date with the change that was merged to the target branch while this request was open; it merged without conflict, and the whole gate passed on the result.

### Underneath

The change is small and lies in one part of the-way, the audit of the process: the template, the counting command with its tests, the audit skill, and three foundation entries (two decisions and one glossary term) that write down the scale and where the cost shows. What was done in your notes lies outside the repository and is not part of the request's files.

## For you to decide

### Needed from you

none

### Fix or let through

1. A register whose table of weights, or the new table of cost levels, lacks a level or names one twice does not stop the count: the count writes its result, refuses the table and prints an error that names the table, not the level. This is exactly what the task asked for ("as a weights table without its four levels is treated today"). But a register without a whole table, column or heading now stops the count with exit code 2, so the two cases end differently, and the rule for scripts that read a file (a missing field stops the script with an error naming it) counts a level's name as a field too. Whoever reads the nightly result feels it only when a level disappears from one of the two tables: they will see an error and a result with no use of that table, instead of no result. Three ways are open. Fixing it here makes both tables stop the count with exit code 2; it costs one small correction with a review of the fix, and it goes against the wording of your task, so you would be choosing the rule over the task. Making a task of it costs one task and leaves the two behaviours until it is done. Letting it through costs nothing, the error is visible on the screen and in the result, and the difference stays written in the review. I recommend letting it through, since the task asked for exactly this and the error is not silent. Fix it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1.)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The cost appears in one new section of the result, with one row per matter and its fate in the row, not as five extra columns in each of the three existing tables of matters (fixed, open, dropped). The task said "for each matter, fixed, open and dropped", and one section does that without repeating the same five columns in three tables and without rewriting about a dozen checks of the existing result. The price is that the audit skill shows you two rows per matter instead of one.
3. A register that lacks a heading, a table or a column the count needs now ends the count with exit code 2, writes nothing, and prints one error naming everything missing; before, a missing table gave exit code 1 and a written result. Your task did not give the exit code. The cycle took the rule for scripts that read a file, because this change reworks how the register is read and the rule then covers the whole reading. The other way, exit code 2 only for the new column and table and the old behaviour for the old ones, would have left two behaviours in one file. If anything outside the repository reads the old exit code 1 of the count, it will see 2.
4. The cycle edited an older decision of the audit, the one that says where the audit gets the class and weight of each problem: it now says the register also holds the cost of an occurrence, and that the audit gives none itself, like class and weight. Your task named this decision as the one the change touches, and the edit is only that addition (and the question it answers, so that the question asks as much as the answer says). The other way, a new decision beside it and the old one left silent about cost, would have left the old promise "the register holds class and weight" incomplete.
5. The setup of the nightly session was changed a little beyond the "rules" the task names: besides the instructions it reads, the script that keeps the register's table of issues now expects the cost column in the table of problems (it finds the table by its header row), and its small test was changed to match. Without this, the nightly script would no longer find the table in your updated register and would stop. The other way, leaving the script alone, would have broken the nightly run on the first night.
6. In the 100 rows you decided, `human` stands only where you had to answer or do something beyond reading an item of a request; rows that the agents proposing the costs marked as weak were lowered, as you chose. That reading is now the register's practice, but the setup of the nightly session says only "the highest level the actual cost reached", so a later night may read `human` more broadly than you did here. The other way, a sentence in the nightly instructions that fixes the narrow reading, was not written because you decided only about these rows.

## Cost

About 1 hour 16 minutes of working time, 39 minutes of them without the waits for tools, and about 54.9 million tokens, all on one model family: one author, a review of the whole change, a fix of its three Minor findings with a review of the fix, a return step that corrected one printed sentence and a review of that correction; then, after you asked, six agents that proposed costs for the register's rows, one for each cycle, and the update of the branch. No review failed. The full gate ran three times, on the base, on the tree before the update of the branch, and on the tree after it, outside that count. The full table of stages stands in the record: `stages.md` in the committed record.

## How to merge

Merge with a merge commit, which keeps the commits; the link to the record survives only then. The foundation has waited for a review through 27 merges since the last tag, below the threshold of 30, so nothing is asked of you here.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — jedna pozycja niżej pyta, czy poprawić, założyć zadanie, czy przepuścić małą różnicę w tym, jak liczenie traktuje brakujący poziom; scalenie bez odpowiedzi ją przepuszcza, a to, co akceptujesz scaleniem, jest wypisane pod nią.

## Co zobaczysz

Rejestr problemów, który czyta cotygodniowy audyt, trzyma teraz przy każdym problemie drugą ocenę obok wagi: ile kosztowało jedno wystąpienie tego problemu. Ocena to jeden z pięciu stałych poziomów, każdy droższy od poprzedniego: `nothing` (wystąpienie nic nie kosztowało: potwierdzenie albo uwaga bez skutku), `steps` (kilka kroków jednego agenta w jego etapie, które agent sam naprawił), `stage` (etap albo jego spora część zrobiona jeszcze raz, albo duża dodatkowa lektura czy sprawdzenie u tego samego agenta), `round` (dodatkowe uruchomienie agenta: runda poprawek, dodatkowe uzgodnienie z gałęzią docelową, nowy przegląd, ponowiony kawałek) i `human` (czas człowieka: pytanie, decyzja, ręczne sprawdzenie, poprawka po scaleniu). Problem dostaje najwyższy poziom, do którego sięgnął jego faktyczny koszt; to, co mogło się stać, nadal mówi waga. Szablon rejestru ma nową kolumnę i tabelę pięciu poziomów z ich znaczeniami, które możesz dostosować, ale samych poziomów zmienić nie możesz.

Polecenie liczące czyta nową kolumnę i odrzuca problem, którego koszt nie jest żadnym z pięciu poziomów, tak jak odrzuca nieznaną wagę. Jego wynik dostaje jedną nową sekcję: przy każdej sprawie rejestru, poprawionej, otwartej albo porzuconej, podaje, ile jej problemów stoi na każdym poziomie kosztu. Skill audytu pokazuje Ci ten wiersz przy sprawie jako materiał do ważenia; nie ustawia z niego priorytetu ani kolejności.

Polecenie zatrzymuje się też teraz z błędem, który nazywa brakujący nagłówek, tabelę albo kolumnę, z kodem wyjścia 2, gdy rejestr któregoś z nich nie ma. Dotąd rejestr bez tabeli dawał kod wyjścia 1 i wynik zapisany bez niej.

Twoja własna kopia rejestru jest doprowadzona do porządku w tej samej robocie, na Twoją prośbę: ma nową kolumnę i nową tabelę, a każdy z jej 100 problemów ma koszt, zaproponowany z zapisów sześciu cykli, z których pochodzą, i rozstrzygnięty przez Ciebie w tabeli. Ustawienia nocnej sesji też znają kolumnę: jej instrukcje i playbook opisują koszt, a skrypt, który prowadzi tabelę spraw rejestru, oczekuje nowej kolumny. Liczenie puszczono na zaktualizowanym rejestrze z wynikami w katalogu roboczym: skończyło się kodem 0 i nie odrzuciło żadnego wiersza.

Gałąź uaktualniono o zmianę, którą scalono do gałęzi docelowej, gdy request był otwarty; scaliła się bez konfliktu, a pełna bramka przeszła na wyniku.

### Pod spodem

Zmiana jest mała i leży w jednej części the way, w audycie procesu: szablon, polecenie liczące z testami, skill audytu i trzy wpisy fundamentu (dwie decyzje i jedno hasło słownika), które zapisują skalę i miejsce, w którym widać koszt. To, co zrobiono w Twoich notatkach, leży poza repozytorium i nie należy do plików requestu.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawienia albo przepuszczenia

1. Rejestr, w którego tabeli wag albo w nowej tabeli poziomów kosztu brakuje poziomu albo któryś występuje dwa razy, nie zatrzymuje liczenia: polecenie zapisuje wynik, odrzuca tabelę i wypisuje błąd, który nazywa tabelę, a nie poziom. Dokładnie tego chciało zadanie („tak jak dziś tabelę wag bez czterech poziomów wagi”). Ale rejestr bez całej tabeli, kolumny albo nagłówka zatrzymuje teraz liczenie kodem wyjścia 2, więc te dwa przypadki kończą się różnie, a reguła dla skryptów czytających plik (brakujące pole zatrzymuje skrypt z błędem, który je nazywa) liczy za pole także nazwę poziomu. Poczuje to ten, kto czyta nocny wynik, i tylko wtedy, gdy z jednej z tych dwóch tabel zniknie poziom: zobaczy błąd i wynik bez użycia tej tabeli, zamiast braku wyniku. Są trzy drogi. Poprawka tutaj sprawia, że obie tabele zatrzymują liczenie kodem wyjścia 2; kosztuje jedną małą korektę z przeglądem poprawki i idzie wbrew brzmieniu Twojego zadania, więc wybierałbyś regułę ponad zadanie. Założenie zadania kosztuje jedno zadanie i zostawia oba zachowania do czasu jego wykonania. Przepuszczenie nic nie kosztuje, błąd jest widoczny na ekranie i w wyniku, a różnica zostaje zapisana w przeglądzie. Rekomenduję przepuszczenie, bo zadanie prosiło dokładnie o to, a błąd nie jest cichy. Poprawić w tym requeście, założyć zadanie, czy przepuścić? (Uwagi poza zakresem zadania, 1.)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Koszt pojawia się w jednej nowej sekcji wyniku, z jednym wierszem na sprawę i jej losem w wierszu, a nie jako pięć dodatkowych kolumn w każdej z trzech istniejących tabel spraw (poprawionych, otwartych, porzuconych). Zadanie mówiło „przy każdej sprawie, poprawionej, otwartej i porzuconej”, a jedna sekcja to spełnia bez powtarzania tych samych pięciu kolumn w trzech tabelach i bez przepisywania około tuzina sprawdzeń istniejącego wyniku. Cena: skill audytu pokazuje Ci dwa wiersze przy sprawie zamiast jednego.
3. Rejestr, w którym brakuje nagłówka, tabeli albo kolumny, których liczenie potrzebuje, kończy teraz liczenie kodem wyjścia 2, nic nie zapisuje i wypisuje jeden błąd z nazwami wszystkiego, czego brakuje; dotąd brakująca tabela dawała kod wyjścia 1 i zapisany wynik. Twoje zadanie nie podało kodu wyjścia. Cykl przyjął regułę dla skryptów czytających plik, bo ta zmiana przerabia sposób czytania rejestru, a reguła obejmuje wtedy cały odczyt. Druga droga, kod wyjścia 2 tylko dla nowej kolumny i tabeli, a dla starych dawne zachowanie, zostawiłaby dwa zachowania w jednym pliku. Jeśli cokolwiek poza repozytorium czyta dawny kod wyjścia 1 tego liczenia, zobaczy 2.
4. Cykl zmienił starszą decyzję audytu, tę, która mówi, skąd audyt bierze klasę i wagę każdego problemu: mówi teraz, że rejestr trzyma także koszt wystąpienia i że audyt sam go nie nadaje, tak jak klasy i wagi. Twoje zadanie wskazało tę decyzję jako tę, której zmiana dotyczy, a zmiana to tylko ten dopisek (oraz pytanie, na które decyzja odpowiada, żeby pytało o tyle, ile mówi odpowiedź). Druga droga, nowa decyzja obok i stara bez słowa o koszcie, zostawiłaby starą obietnicę „rejestr trzyma klasę i wagę” niepełną.
5. Ustawienia nocnej sesji zmieniono nieco poza „reguły”, które nazywa zadanie: oprócz instrukcji, które ona czyta, skrypt prowadzący tabelę spraw rejestru oczekuje teraz kolumny kosztu w tabeli problemów (znajduje tabelę po wierszu nagłówka), a jego mały test dopasowano. Bez tego nocny skrypt nie znalazłby tabeli w Twoim zaktualizowanym rejestrze i by się zatrzymał. Druga droga, zostawienie skryptu, zepsułaby nocny przebieg już pierwszej nocy.
6. W 100 wierszach, które rozstrzygnąłeś, `human` stoi tylko tam, gdzie musiałeś odpowiedzieć albo coś zrobić ponad przeczytanie pozycji requestu; wiersze, które agenci proponujący koszty oznaczyli jako słabe, obniżono, jak wybrałeś. Ta lektura jest teraz praktyką rejestru, ale ustawienia nocnej sesji mówią tylko „najwyższy poziom, do którego sięgnął faktyczny koszt”, więc późniejsza noc może czytać `human` szerzej niż Ty tutaj. Druga droga, zdanie w instrukcjach nocnej sesji, które utrwala wąską lekturę, nie została napisana, bo rozstrzygnąłeś tylko o tych wierszach.

## Koszt

Około 1 godziny 16 minut czasu pracy, z tego 39 minut bez czekania na narzędzia, i około 54,9 miliona tokenów, wszystko na jednej rodzinie modeli: jeden autor, przegląd całości zmiany, poprawka jego trzech uwag Minor z przeglądem poprawki, krok powrotu, który poprawił jedno wypisywane zdanie, i przegląd tej poprawki; potem, na Twoją prośbę, sześciu agentów, którzy zaproponowali koszty wierszy rejestru, po jednym na cykl, oraz uaktualnienie gałęzi. Żaden przegląd nie zakończył się odrzuceniem. Pełna bramka poszła trzy razy, na bazie, na drzewie przed uaktualnieniem gałęzi i na drzewie po nim, poza tym zliczeniem. Pełna tabela etapów jest w zapisie cyklu: `stages.md` in the committed record.

## Jak scalić

Scal commitem scalającym, który zachowuje commity; link do zapisu cyklu przeżywa tylko tak. Fundament czekał na przegląd przez 27 scaleń od ostatniego tagu, poniżej progu 30, więc nic tu od Ciebie nie jest wymagane.

</details>

## Technical changes

Commits on the task branch, then the record's pairs. Each paragraph opens with what it means for someone working with the process.

- `f5e1d45` — the register and the audit now carry the cost of an occurrence. `process-audit/problem_register.md` gets the column `Cost of an occurrence` in *Problems* (after *Weight*) and the table `## Costs of an occurrence` with the five levels; `process-audit/audit_count.py` has `COST_LEVELS`, a `cost` on each problem, a row of eight cells, refusal of a cost that is no level and of a levels table that lacks or doubles a level (as *Weights* is treated), the new result section `## Cost of an occurrence by issue`, and, for the whole reading of the register, exit code 2 with nothing written and one error naming every missing heading, table or column; `process-audit/SKILL.md` quotes the cost row beside each issue at steps 2 and 3 with the rule that it is material and never a priority, and its exit codes are updated; `process-audit/test_audit_count.py` has the tests for each (the failing run before the code was 127 of 129 failed, the passing run after was 129 OK).
- `18b4a3f` — the foundation step: WAY-345 and WAY-346 are new, the glossary term `cost of an occurrence` is new, and WAY-330 is edited in place.
- `e6d05e2` — the one fix for the three Minor findings of the review of the whole change: the template's "four tables" is now "five tables", the test of a reordered or extra column now has a reordered case, and the lines of WAY-330 that the edit had broken are rewrapped (no word changed).
- `ba2f0dc` — the return step corrected one printed sentence in `process-audit/audit_count.py`: the paragraph above *Problems by cycle* now lists the cost of an occurrence among the reasons a row is refused. No logic changed.
- `7425423` — the merge of `origin/foundations`, which moved from `55afa8e` to `54ae4cf` while the request was open (the change of the remarks check and the report names); it merged without conflict. The files it brings in lie outside this change except `foundations/decisions.md`, where the other change edits a different decision.
- Outside the repository, at your request: your copy of the register (the table of levels, the column, 100 costs), the instructions of the nightly session and its playbook (the cost is described), the script that keeps the register's table of issues (it expects the column) and its test. These files are in your notes, not in this request; they lie uncommitted in the notes' own history, for your own rhythm.
- The record of the cycle is added by one commit and removed by the next, so that the target branch never holds it; this correction repeats the pair.

## Checks

- Gate on the final tree: `python -B gate/run_tests.py`, exit 0, 1077 tests in 10 directories, every directory passed, run on the tree after the merge of the target branch (`7425423`). Earlier runs: on the base `55afa8e`, in a separate checkout, exit 0, 1066 tests; on `ba2f0dc` before the merge, exit 0, 1071 tests. No check failed or did not run.
- Focused checks of the author, the fix and the return step: `python -B gate/run_tests.py process-audit`, exit 0 (129 tests); `python -B elements/common/foundation_check.py`, exit 0 ("0 errors"), run again on the merged tree, exit 0; `python -B gate/run_tests.py elements/common` exit 0 (144) and `agent-instructions` exit 0 (18) once, by the author.
- Own-work checks: the author ran the old template (from the base) through the command with a throwaway locations file, and got exit 2 and the error naming the missing heading and column; the new template with three problem rows gave exit 0 and the section as designed. The author also switched the cost check off (the cost test failed, restored) and the fix did the same for the reordered-header case (the new case failed, restored).
- Reviews: whole change `PASS` (0 blocking, 4 Minor: 3 within the task, fixed, and 1 outside it); the fix `PASS` (0 new findings); the return step `PASS` (0 blocking, 1 Minor, not fixed). The review of the whole change read 18 of 18 selected decisions whole, 0 by title only, and named none as unread that bears on the change. It ran 16 crafted registers against the counting command (a cost that is no level, a levels table with a level missing, doubled or extra, missing heading, table or column, control and direction characters, line breaks): no unprintable character reached the result. The merge of the target branch had no fresh review: the files it brings in are outside this change, and the one shared file merged in different lines (the cycle's choice, in the record).
- The register after the update (outside the repository): `python -B process-audit/audit_count.py` with a throwaway locations file naming the updated register and a scratch results directory, exit 0, 136 cycles in 2 of 2 repositories, no refused row, the section `Cost of an occurrence by issue` listing the six issues; the nightly register script's tests: `python -B -m pytest tests/test_problem_register.py`, 5 passed; its dry run on the updated register found the table (exit 0).
- Process remarks check, on the original record: `python -B task-cycle/remarks_check.py .runs/task-cycles/problem-cost-in-register`, exit 0 on the second run of the first writing (the first run, exit 1, listed 12 items, which were then appended to the remarks) and exit 0 again after the merge of the target branch brought a new version of the script (3 runs in all).
- Form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/problem-cost-in-register/request.md --task .runs/task-cycles/problem-cost-in-register/task.md`, exit 0. Check of private paths on it: `python -B task-cycle/private_paths_check.py .runs/task-cycles/problem-cost-in-register/request.md`, exit 0. The checks on the copy of the record (private paths, images, remarks) are written in the record's *Verification* after its commit.
- Not checked: whether anything outside the repository (the wrapper of the nightly count) reads the old exit code 1 of the count; no reviewer could see it from the repository. The costs in the register rest on the records of the six cycles read by agents and decided by you; 18 of the 100 proposals were marked as unseen in the record (the cost may exist but the record does not show it) and stand as `nothing`.

## Foundation entries

- WAY-345 (row 1): the cost of an occurrence of a problem has five fixed levels, each dearer than the one before; a problem takes the highest level its cost reached; the user adapts only the meanings of the levels.
- WAY-346 (row 2): the result of the count gives, for each issue fixed, open and dropped, how many of its problems stand on each level of cost, and nothing by cycle.
- Glossary term `cost of an occurrence` (row 3): a level on the scale of five levels, different from the cost of a cycle in money (WAY-337).
- WAY-330 (the cycle's): the register holds, besides the class and weight of each problem, the cost of an occurrence, and the audit gives none of the three itself; its question, binding sentence, *Verification*, *Rationale* and *Rejected* say so.
- Rows of *Settlements to record*: row 1 → WAY-345, row 2 → WAY-346, row 3 → the glossary term. The other three candidates the task showed were not accepted. No invariant, environment fact or part-map entry was written or changed.

## Minor findings

Unfixed Minor findings within the task, with the reviewer's words.

1. Review of the return step, `process-audit/audit_count.py:2094`: "The rewrapped paragraph leaves one line 120 characters long, where the file had none above 103. […] Adding "cost of an occurrence," to line 2091 pushed the words down; the commit rewrapped lines 2091 to 2093 but left the following line 2094 as it was, so it now carries the end of the sentence from the line above plus its old tail. […] No test or gate check fails on it […] and the printed text is unchanged by wrapping, so the effect is polish only." Nobody working with the process will feel it.

## Findings outside the task's scope

1. Review of the whole change, the exit code of the row labels of the two level tables (`read_register` in `process-audit/audit_count.py`, the check that sorts the level names): "a missing or doubled level in *Weights* or *Costs of an occurrence* […] gives exit 1, a written result and the register error. The task says exactly this ("tak jak dziś tabelę wag bez czterech poziomów wagi", To do 2), and WAY-344's purpose, no quiet pass, is met: the error is on stderr and in *Unknown values*, the table is refused, nothing is read as empty […]. I do not ask for a change; the error names the table, not the level, which is the one gap against "names the field". The human may rule whether WAY-344 or the task prevails here; […] if WAY-344 prevails the fix is small (raise instead of refuse, for both tables, and two test expectations)." It stands in *Fix or let through*, 1.
2. Review of the whole change, WAY-339 and the cost levels (no code): "WAY-339 names the list of classes, the price list, the stage report and the reviewer's instructions as starting a new series, not the meaning of a cost level. Today the count compares no cost level across time, so a user who adapts a meaning starts nothing that is measured. If a later task compares the cost levels of one week with another, WAY-339 has to be revisited then." Not an item of the decisions: it asks nothing today.
3. Declined to judge by the review of the whole change: whether the old exit code 1 for a missing table had a consumer outside the repository (the nightly wrapper); the skill is the only reader inside the repository and was updated.

## Course of the cycle

- **Task and sources:** an independent task from the author's private notes, `Status: ready for cycle`, dated 2026-11-12; goal: the register and the audit carry the cost of one occurrence of a problem beside its weight. One human action placed in the cycle: the register of the author and the nightly session's setup; done in the conversation after the request opened, at the author's request, by the orchestrator and not by the code of the request. Source: the task document, frozen in the record; base `55afa8e`.
- **Process pin:** not applicable; the cycle ran on the-way's own checkout and the task moves no pin.
- **Spec:** none; no open design choice at the start: the task's three answers settle the scale, its stability and where the cost shows.
- **Route:** one author without a plan, on the same class as the orchestrator (Sonnet 5.5) rather than the cheaper default, because the change edits the counting command, a trust boundary of the part map with a 110 KB test file, and an error there shifts the audit's measures without a visible symptom; the review of the whole change by a fresh agent, one fix for its Minor findings with a review of the fix, the return step (it committed one sentence, so a fresh agent reviewed it), then the full gate. After the request opened: the update of the branch with the moved target branch, the full gate again, and the work in the author's notes described above.
- **Plan:** none.
- **Choices:** 8 other choices, in the record's questions table: `cycle.md` in the committed record.
- **Blocking findings left:** none.
- **Record:** pending the commit that adds it
