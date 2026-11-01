`plan-project` był jednym plikiem o 2344 słowach, więc agent w wąskiej turze niósł też tekst kroków, których nie wykonywał. Po tej zmianie główny plik ma 623 słowa, a procedury kroków i wariantów stoją w jedenastu plikach obok. Tura zlecona, która czyta tylko swoje kroki, czyta 1986 słów zamiast 2344; nowe rozbicie czyta o 63–239 słów więcej, a tura czytająca wszystko 3047, czyli o 703 więcej. Poza dwoma punktami ustalonymi w zadaniu żadna reguła nie zniknęła ani nie zmieniła znaczenia: zdanie w `lead-project` wskazuje nowy plik, a sesja na istniejącym planie przechodzi przez krok 1, zanim pójdzie dalej. Scalenie nie zmienia fundamentu.

Zadanie niezależne, szóste z jedenastu w serii przebudowy skilli. Opis przyjęty 2026-11-01, baza `foundations` `2f51e6c31f5911ac8a0292a80a4f599bd4bd0092`; do czasu tego requestu `foundations` się nie ruszyło. Sesja pracowała na samym the way, więc nie ma przypięcia procesu ani jego przesunięcia. Specyfikacji nie było, bo zadanie nie zostawiło otwartego wyboru projektowego: pytania 1–7 rozstrzygają treść, a nazwy i podział plików to sposób wykonania. Planu nie było, bo jeden skill i jedno zdanie obok zależą od jednej oceny i mieszczą się w pracy jednego autora.

## Co się zmieniło

- `project-level/plan/skill/SKILL.md` trzyma obraz całości, zasady wspólne dla kroków i odsyłacze. Kroki zachowują numery od 0 do 7, a nagłówek „Delegated work while leading a plan” zostaje.
- Obok stoi jedenaście plików: `delegated_mode.md`, `existing_plan.md`, `read.md`, `reading_definition_and_plan.md`, `cut_tasks.md`, `guideline_tasks.md`, `assign_entries.md`, `place_questions.md`, `write_and_check.md`, `critique_plan.md`, `hand_over.md`.
- Sekcja „Reading the definition and plan” stoi w pliku obok, wymienionym przez kroki 0 i 1. Jej zdania o nadrzędności oryginałów i sprawdzeniach na całych plikach zostały w `SKILL.md`, razem ze zdaniem, że nowe rozbicie obejmuje każdy punkt zakresu.
- `guideline_tasks.md` jest wymieniony w `SKILL.md` przy kroku 2, z warunkiem obejmującym brakujące wytyczne, pierwszy plik rodzaju, istniejący rodzaj bez wpisu w indeksie, pierwszy test poziomu i rozszerzenie wytycznych.
- Pliki kroków 5–7 zaczynają się od zastrzeżenia dla tury zleconej: agent nie pyta człowieka sam, nie uruchamia krytyki sam i nie pokazuje człowiekowi planu sam.
- `project-level/lead/skill/SKILL.md:30–31` wskazuje `reading_definition_and_plan.md` zamiast sekcji `SKILL.md`; to jedyna zmiana w tym skillu.
- Kod w Pythonie, opis skilla, wejścia `the-way-*` i `project-level/plan/template.md` się nie zmieniły.

Jeden wybór cyklu warto zobaczyć przed scaleniem. Pytanie 3 mówi, że sesja na istniejącym planie „czyta” plik kroku 1. Autor najpierw policzył to jako samo przeczytanie, a przegląd pokazał, że wtedy agent zmienia plan bez fundamentu w głowie, czyli dostaje wariant odrzucony w tym pytaniu. Cykl uznał więc, że sesja wykonuje krok 1, i `existing_plan.md` mówi to wprost: „goes through”. Dosłowna baza wysyłała wznowiony szkic od razu do pierwszego niedokończonego kroku, ale według zadania `readiness_check.py` uruchomiono w każdej z 14 sesji, a do `foundations/` produktu sięgnięto w 11. Gdyby zostawić samo przeczytanie, drogi 3 i 6 byłyby tańsze na papierze, a agent albo robiłby krok 1 wbrew opisowi, albo szedł bez fundamentu. Przy obecnym brzmieniu te drogi na pewno niosą 1774 słowa kroku 1 (`read.md` 141, sekcja „Reading the foundation” 492, `product-guidelines/reading.md` 1141).

## Ocena skilla

Pełna tabela oceny stoi w [komentarzu pod tym requestem](ASSESSMENT_LINK): 34 wiersze i 6 propozycji, każdy fragment zacytowany dosłownie z zakresem linii na `2f51e6c`, z tym, kiedy jest potrzebny, czy agent rozpozna ten moment, z werdyktem i miejscem po przebudowie. Wszystkie 179 niepustych linii bazy stoi w dokładnie jednym wierszu.

Sześć propozycji nie zostało wykonanych. Przy każdej: co będzie, gdy zostanie, i co kosztuje zmiana. Propozycje 2–5 to powtórzenia między skillem a `project-level/plan/template.md`. Lista powtórzeń nie jest pełna, zob. uwagę 5 niżej.

1. **`SKILL.md:11–12` na bazie, „The decisions that set its rules are cited below.”:** usunąć zdanie. Zostaje: 9 słów przy każdym użyciu. Po zmianie czytelnik nie dowie się przed krokami, że nawiasy to decyzje.
2. **`SKILL.md:144–149` na bazie, teraz `assign_entries.md`, format wpisu „side by side”, powtórzony w `template.md:162–168`:** usunąć format ze skilla i wskazać szablon. Zostaje: dwa miejsca do utrzymania w zgodzie. Po zmianie instrukcja traci wzór w chwili przypisywania, a agent, który przejrzał szablon pobieżnie, zapisze wpis źle i zgłosi to `plan_check.py`.
3. **`SKILL.md:184–188` na bazie, teraz `critique_plan.md`, lista tego, co ocenia krytyka, powtórzona w `template.md:184–188`:** usunąć listę ze zlecenia kroku 6 i wskazać sekcję szablonu. Zostaje: powtórzenie i ryzyko rozjazdu. Po zmianie, gdy autor zapomni o tej sekcji, krytyk oceni mniej, niż wymaga WAY-146.
4. **`SKILL.md:110–114` i `:128–134` na bazie, teraz `cut_tasks.md`, reguły cięcia powtórzone w kolumnach szablonu:** usunąć je z `cut_tasks.md`. Zostaje: powtórzenie. Po zmianie cięcie traci reguły w chwili cięcia i opiera się na tym, że agent zastosuje komórkę tabeli.
5. **`SKILL.md:160–163` na bazie, „stands with — definition: none”, powtórzone w `template.md:146–147`, teraz w `place_questions.md` i `write_and_check.md`:** zostawić regułę tylko w szablonie. Zostają trzy miejsca. Po zmianie oznaczenie zmienia się w jednym miejscu, kosztem odsyłacza przy dwóch krokach.
6. **Warunek odsyłacza w `SKILL.md`, krok 0:** przenieść „by the human or in a dispatched turn by its conversation file” do `delegated_mode.md` jako piąty punkt. Zostaje: warunek w `SKILL.md`, który recenzent potwierdził jako niezmieniający wyboru dróg. Po zmianie dochodzi nowe zdanie w pliku, którego zadanie każe nie zmieniać (pytanie 1).

## Liczby słów

| Droga | Tekst skilla: przed → po | Suma z plikami obok: przed → po |
|---|---:|---:|
| 1. Nowe rozbicie, odczyt wytycznych nic nie znalazł | 2344 → 2407 (+2,7%) | 6897 → 6960 (+0,9%) |
| 2. Nowe rozbicie z `guideline_tasks.md` | 2344 → 2583 (+10,2%) | 6897 → 7136 (+3,5%) |
| 3. Wznowienie szkicu od kroku 5 | 2344 → 1949 (−16,9%) | 6897 → 6502 (−5,7%) |
| 4. Korekta człowieka do oddanego planu, np. podział zadania | 2344 → 2429 (+3,6%) | 6897 → 6982 (+1,2%) |
| 5a. Wąska tura zlecona, agent czyta swoje kroki | 2344 → 1986 (−15,3%) | 7485 → 7127 (−4,8%) |
| 5b. Wąska tura zlecona, agent czyta wszystko | 2344 → 3047 (+30,0%) | 7485 → 8188 (+9,4%) |
| 6. Tura samego oddania planu | 2344 → 1730 (−26,2%) | 7485 → 6871 (−8,2%) |
| 7. Ponowne sprawdzenie po bramce definicji | 2344 → 2871 (+22,5%) | 7485 → 8012 (+7,0%) |

Słowa liczone są jak `wc -w`, w stanie „przed” na `2f51e6c`. Suma dolicza `project-level/plan/template.md`, sekcje `elements/common/way_of_working.md`, `project-level/lead/conversation_template.md`, `product-guidelines/reading.md` i pliki krytyki tam, gdzie droga do nich dochodzi. Definicja, plan i pliki produktu są poza liczeniem. To liczby słów w plikach, nie pomiar zachowania agenta ani tokenów. [Skład każdej drogi plik po pliku](RECORD_LINK/reports/word-counts.md).

Na drogach 3 i 6 oba stany liczą krok 1 jako wykonany, jak robiły zapisane sesje. Przy dosłownym odczycie bazy, która wysyłała te drogi obok kroku 1, stan „przed” to 5264 i 5852 słowa, a suma rośnie o 23,5% i 17,4%. Sprawdzenie jest tu słabsze, niż to wygląda: zapisane sesje uruchamiały `readiness_check.py` i sięgały do fundamentu, ale żadna nie sięgnęła do `guidelines/` produktu, więc 1141 słów `reading.md` w stanie „przed” to wymaganie tekstu, nie zachowanie sesji.

**Wobec szacunków z zadania:** nowe rozbicie 2407–2583 mieści się w 2300–2900; tura 5a, 1986, w poprawionych 1800–2000; tura czytająca wszystko 3047 i ponowne sprawdzenie 2871 w 2800–3250; 703 słowa dopłaty w 450–900. Poza zakresem −15 do +25% z niewybranej odpowiedzi w pytaniu 4 są droga 6 (−26,2%) i 5b (+30,0%). `read.md` ma 141 słów wobec szacowanych ok. 170. Dwanaście plików skilla ma razem 3047 słów, o 703 więcej niż dawny jeden plik. Do utrzymania dochodzi jedenaście plików i tekst powtórzony celowo: lista pytań w `write_and_check.md`, ustalenie `plan_check.py` o dwóch zadaniach w trzech plikach i zastrzeżenie na początku kroków 5–7.

## Sprawdzenia

`python -B gate/run_tests.py`: kod **0** na bazie `2f51e6c`, na `db3845c` i na przejrzanym `1fa823e`, za każdym razem 615 testów w 8 katalogach, każdy katalog przeszedł. Pięć sprawdzeń pominął Windows, więc nie liczą się jako zaliczone, wszystkie z `instruction-files/test_check_instructions.py`:

- `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`, wymaga POSIX
- `test_an_absolute_link_out_of_the_repository_is_not_read`, wymaga POSIX
- `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`, wymaga POSIX
- `test_every_directory_link_is_reported_wherever_it_points`, wymaga POSIX
- `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`, brak FIFO na tej platformie

`foundation_check.py`, `check_instructions.py` (wynik taki sam jak na bazie, w tym ostrzeżenie o `_zadania\` w `AGENTS.md:21`) i `skill_entry_points.py --write` (nic nie zmienił): kod 0. Liczby słów powstały po ostatniej zmianie liczonego pliku; skrypt autora porównał z plikami 279 liczb, bez różnic.

Autor za najsłabszy punkt uznał zachowanie reguł. Porównanie zdanie po zdaniu dało 3 niedosłowne fragmenty bazy, wszystkie to przeredagowane odsyłacze, każdy rozliczony. Recenzent powtórzył to własnym skryptem (144 fragmenty bazy, te same 3 niedosłowne, 36 nowych), przeczytał ręcznie każdy nowy fragment pod kątem tego, co wyłącza, przeliczył cytaty, wiersze oceny, wszystkie liczby dróg i przeszedł ręcznie drogi 2, 3, 4, 5 i 7. [Autor](RECORD_LINK/reports/author.md), [przegląd](RECORD_LINK/reports/review.md), [poprawka](RECORD_LINK/reports/fix.md), [przegląd poprawki](RECORD_LINK/reports/review-fix.md), [krok powrotny](RECORD_LINK/reports/return.md).

**Nie sprawdzono:**

- Żaden agent nie przeszedł po przebudowanym skillu, więc to, czy czyta swoje kroki, czy wszystko, i czy sięga po każdy odsyłacz, jest niezweryfikowane. Główną miarą zostają słowa wyżej, a porównanie niesionego tekstu czeka na następne prawdziwe użycie skilla w `loop2` (pytanie 5).
- `verify_counts.py` nie porównuje z plikami liczb z sekcji o dosłownym odczycie bazy ani z akapitu o szacunkach. Recenzent przeliczył je własnym skryptem i się zgadzają, ale nie spełnia tego sam skrypt autora, o co prosi ostatnie kryterium akceptacji.
- Autor przeczytał w całości część decyzji z przekazania, a resztę doczytał dopiero w kroku powrotnym; wszystkie decyzje z *Decisions in play* porównał wtedy z plikami. Recenzent przeczytał w całości 70 decyzji, w tym każdą z *Scope* `project-level`; pozostałe 167 nie.
- `author.md` zachowuje część liczb sprzed poprawki; obowiązują te z tego requestu i `word-counts.md`, a tabela zastąpionych liczb stoi w `fix.md`.
- Zmiana nie dotyka interfejsu użytkownika, więc zrzuty ekranu nie mają zastosowania.

## Uwagi przeglądu

Przegląd dał FAIL z jedną uwagą blokującą, poprawioną w `1fa823e`, a przegląd poprawki dał PASS. Uwaga dotyczyła zdania opisanego wyżej: ocena i liczby przypisywały mu dwa różne skutki, a drogi 3 i 6 stały na odczycie odrzuconym w pytaniu 3.

Uwagi drobne, otwarte, słowami recenzenta, do wyboru na nowe zadania:

- **`project-level/plan/skill/critique_plan.md:3-5`** (2): In a dispatched turn, "goes back to the human" at step 6 stands with no qualifier; the opener speaks only of running the critique. Add that clause to the opener, and step 6 to the row.
- **`project-level/plan/skill/reading_definition_and_plan.md:3-4`** (3): A reader who comes from `lead-project` has another `SKILL.md` in mind. Write "the `SKILL.md` beside this file".
- **`project-level/plan/skill/SKILL.md:42-43`** (4): "When an existing plan is named, read ..." selects all that the listed wording selects, and also a plan named by a skill or a document that sends the session here. The listed sources add nothing.
- **`reports/assessment.md:63`, `:65`, `:16`, `:14`, `:24`** (5): The list says the repetitions with the template "are 2-5"; there are more. Proposal 1 is labelled reword and proposes a removal. The proposals stand in no rows of their own. Niewymienione powtórzenia i dwa błędne zdania wylicza [przegląd](RECORD_LINK/reports/review.md).
- **`reports/assessment.md:30`** (6): The row says "cost: 185 words of the file"; `existing_plan.md` now has 187 words, and the fix's table of replaced figures does not list it.
- **`reports/word-counts.md:9`** (7): The rule cites 14 of 14 readiness checks and 11 of 14 foundation reads for counting step 1 in the state "before", but `product-guidelines/reading.md` is counted there too, and no recorded session reached the product's `guidelines/`. Say so. Ta sama uwaga: `word-counts.md:9`, `:148` i `:335` mylą „above” i „below”, a `tools/verify_counts.py` nie porównuje nowej sekcji.

Uwagi spoza zakresu zadania, słowami recenzenta, bez wskazania miejsca poza podanym:

- Whether a narrow turn will read only its own steps or everything: the task settles it in question 1 and measures it at the first real use (question 5).
- Whether the repetitions with the template should go: To do 9 makes them the human's, as proposals.
- **`project-level/plan/skill/SKILL.md:12`, `:17`:** "each skill named below" and "cited below", which now reach text standing in files beside the skill for a session without the entry point: the sentences stand unchanged, and the skills of the series rebuilt earlier keep the same words (`product-guidelines/testing/SKILL.md:21`), so it is a wording for the series, beyond this task.
- Whether "goes through" needs an entry of its own in the foundation: the task's question 3 says the pointer gets no row of *Settlements to record*, and the stronger verb is the return step's to weigh.
- Whether `author.md`'s route notes should be edited rather than replaced by the table in `fix.md`: the fix's handoff asks for the table, and the request's form is the orchestrator's.

Żadne sprawdzenie nie padło i nie przeszło przy powtórzeniu.

## Co rozstrzyga ten request

Żadnego wpisu fundamentu, wpisu rzutowanego, zmienionego testu niezmiennika, zmienionej powierzchni ani oznaczenia *Violated*. Krok powrotny porównał decyzje zadania, wpisy znalezione w fundamencie i mapę części z nowymi plikami: nic nie wymagało korekty, więc nie ma commita. Reguła o kroku 1 stoi w skillu i opiera się na odpowiedzi na pytanie 3, która odsyłaczowi nie daje wiersza *Settlements to record*.

Pytania: brak. Działania człowieka, na które request czeka: brak. Pozostałe wybory w ramach zmiany: CHOICES_COUNT, w [tabeli pytań i wyborów](RECORD_LINK/cycle.md#questions-and-autonomous-choices). [Czas, modele i tokeny](RECORD_LINK/stages.md).

[Pełny zapis cyklu](RECORD_LINK/cycle.md) stoi w osobnym commicie i jest od razu usuwany następnym, żeby docelowe drzewo trzymało tylko zmianę. **Proszę scalić z zachowaniem commitów, bez squash ani rebase**, bo odsyłacze prowadzą do commita zapisu. Wpisu zadania w backlogu nie zmieniono; domknięcie serii po scaleniu jest poza tym requestem.
