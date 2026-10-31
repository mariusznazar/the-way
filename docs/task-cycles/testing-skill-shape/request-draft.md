`maintain-testing-guidelines` kazał na wejściu przeczytać ok. 7700 słów z innych plików, w tym 2835 słów, które sesja znała już z `refine-task`. Po tej zmianie każdy krok czyta tylko to, czego potrzebuje, a główny plik skilla ma 1200 słów zamiast 3042. Czytanie do końca skilla spada o 18–22%, licząc pierwszy odczyt w `refine-task`. Żadna reguła nie zniknęła ani nie zmieniła znaczenia. Request rozszerza też WAY-256 i zapisuje dwie nowe decyzje, wszystkie trzy rozstrzygnięte w przyjętym opisie zadania.

Zadanie niezależne, piąte z jedenastu w serii przebudowy skilli. Opis przyjęty 2026-10-31, baza `foundations` `00c0a747272a9a179b7a855f256daff985ea2ee1`, a w trakcie cyklu scalone `foundations` `2dbf1e7`. Sesja pracowała na samym the way, więc nie ma przypięcia procesu ani jego przesunięcia. Specyfikacji nie było, bo zadanie nie zostawiło otwartego wyboru projektowego: pytania 1–10 i trzy wiersze *Settlements to record* rozstrzygają treść, a podział na pliki to sposób wykonania. Planu nie było, bo jeden skill, jedno zdanie w drugim skillu, jedna odpowiedź w pliku oceny i trzy wiersze fundamentu zależą od jednej oceny i mieszczą się w pracy jednego autora.

## Co się zmieniło

- `product-guidelines/testing/SKILL.md` trzyma obraz całości, zasady wspólne dla kroków i odsyłacze. Procedury kroków 1–5 i wariantów stoją w dziesięciu plikach obok: `recognize.md`, `starting_set.md`, `research.md`, `audit.md`, `new_level.md`, `settle.md`, `new_tools.md`, `task_document.md`, `hand_back.md`, `orchestrated_mode.md`.
- Krok 0 nie każe już czytać wszystkiego naraz. Szablon testów jest czytany przed pierwszym krokiem, który go używa, na każdej drodze, także na drodze „A new level” z przepisem, który już stoi. Szablon wytycznych czyta krok 4, a pliki krytyki pierwsza krytyka. To, co sesja przeczytała w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz.
- `research.md` i `new_tools.md` są wymienione także w `SKILL.md` przy swoim kroku, z warunkiem, kiedy się je czyta.
- Agent na drodze „A new level” nie czyta audytu, a agent audytu nie czyta „A new level”, gdy nowego poziomu nie ma.
- `instruction-files/kind_skill.md` dostał trzecią odpowiedź: fragment potrzebny na niektórych krokach.
- Krok 0 skilla testów i krok 0 `product-guidelines/styleguide/SKILL.md` kończą się zdaniem, które sesję bez kroków 1 i 2 `refine-task` odsyła najpierw do nich. W skillu styleguide'u to jedyna zmiana.
- Kod w Pythonie, szablony i `product-guidelines/reading.md` się nie zmieniły.

## Ocena skilla

Pełna tabela oceny stoi w [komentarzu pod tym requestem](@@ASSESSMENT_COMMENT@@): 44 wiersze, osobny wiersz o wyborze z pytania 3 i 2 propozycje, każdy fragment zacytowany dosłownie z zakresem linii na `00c0a74`, z tym, kiedy jest potrzebny, czy agent rozpozna ten moment, oraz z werdyktem. Wszystkie 227 niepustych linii bazy stoi w dokładnie jednym wierszu.

Dwie propozycje nie zostały wykonane, bo zmieniają treść reguły:

- **P1, `SKILL.md:99` na bazie, autor nie rekomenduje:** czytać z `guidelines/` produktu tylko plik części, której dotyczy zadanie, i indeks wytycznych kodu, a główny `AGENTS.md` po sekcjach. Bez zmiany sesja czyta całość, co kosztuje tyle słów, ile produkt ma wytycznych. Po zmianie czyta mniej, ale może pominąć regułę z pliku innej części. W przeszukanych zapisach nie ma błędu, który by ją uzasadniał.
- **P2, `SKILL.md:174-179` na bazie, teraz `product-guidelines/testing/new_level.md`, autor rekomenduje:** dopisać do zdania o przepisie poziomu „or, where the recipe already stands with an empty *Exemplar*, takes its exemplar with it”. Bez zmiany na drodze z gotowym przepisem zdanie „the level's recipe comes into being with it” można przeczytać tak, że przepis powstaje jeszcze raz; recenzent potwierdza, że tak się je czyta. Po zmianie zdanie jest prawdziwe na obu drogach, a koszt to kilkanaście słów i dopisany przypadek w regule, dlatego cykl sam tego nie zrobił.

## Liczby słów

| Droga | Przed krokiem 4: przed → po | Suma na koniec: przed → po | Suma bez pierwszego odczytu: przed → po |
|---|---:|---:|---:|
| 1. Pierwsze wytyczne, brak testów, człowiek bez preferencji | 14120 → 8791 (−38%) | 14120 → 11272 (−20,2%) | 11285 → 8437 (−25%) |
| 2. To samo, człowiek z preferencją | 13611 → 7728 (−43%) | 14120 → 11040 (−21,8%) | 11285 → 8205 (−27%) |
| 3. Są testy, nie ma wytycznych, bez preferencji; a także rozszerzenie | 14120 → 9021 (−36%) | 14120 → 11502 (−18,5%) | 11285 → 8667 (−23%) |
| 4. Odświeżenie | 13611 → 7958 (−42%) | 14120 → 11270 (−20,2%) | 11285 → 8435 (−25%) |
| 5. „A new level” z przepisem, który już stoi, bez kroku 2 | 13611 → 7647 (−44%) | 14120 → 10959 (−22,4%) | 11285 → 8124 (−28%) |
| 6. Tryb orkiestrowany na drodze 1 | 14120 → 8889 (−37%) | 14120 → 11370 (−19,5%) | 11285 → 8535 (−24%) |

Słowa liczone są jak `wc -w`, w stanie „przed” na `00c0a74`. Dwie pierwsze kolumny obejmują pierwszy odczyt w `refine-task` (2835 słów), a ostatnia go pomija. Plik czytany dwa razy w stanie „przed” liczy się dwa razy, pliki obok krytyki (509 słów) wchodzą tam, gdzie droga do nich dochodzi, a pliki produktu są poza liczeniem. `new_tools.md` (69 słów) dochodzi tylko wtedy, gdy nowe narzędzie zostaje pytaniem o technologię. To liczby słów w plikach, nie pomiar zachowania agenta ani tokenów. [Skład każdej drogi plik po pliku](@@RECORD@@/reports/word-counts.md).

Wobec szacunku z pytania 1 suma na koniec mieści się w 11 100–11 800 na czterech drogach, droga 2 jest o 60 słów niżej, a droga 5 o 141. Przed krokiem 4 pięć dróg mieści się w 7600–9000, a droga 3 jest o 21 słów wyżej. Skill i pliki obok mają razem 3488 słów wobec 3042, czyli o 446 więcej, a do utrzymania dochodzi dziesięć plików.

## Sprawdzenia

`python -B gate/run_tests.py`: kod **0** na bazie `00c0a74`, na przejrzanym `c17f4f8` i na scalonym `b510f40`, za każdym razem 614 testów w 8 katalogach, każdy katalog przeszedł. Pięć sprawdzeń pominął Windows, więc nie liczą się jako zaliczone, wszystkie z `instruction-files/test_check_instructions.py`:

- `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`, wymaga POSIX
- `test_an_absolute_link_out_of_the_repository_is_not_read`, wymaga POSIX
- `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`, wymaga POSIX
- `test_every_directory_link_is_reported_wherever_it_points`, wymaga POSIX
- `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`, brak FIFO na tej platformie

`foundation_check.py`, `check_instructions.py` (wynik taki sam jak na bazie, w tym ostrzeżenie o `_zadania\` w `AGENTS.md:21`) i `skill_entry_points.py --write` (nic nie zmienił): kod 0.

Autor za najsłabszy punkt uznał zachowanie reguł. Porównanie bazy z nowymi plikami zdanie po zdaniu dało 18 fragmentów niedosłownych, każdy rozliczony. Recenzent powtórzył porównanie własnym skryptem w obie strony, przeliczył cytaty i wszystkie drogi oraz dwa razy przeszedł sześć dróg ręcznie, od `SKILL.md` do pliku ostatniego kroku. Na drodze 5 nie dochodzi tylko jedna reguła: uwaga drobna 7 niżej. [Autor](@@RECORD@@/reports/author.md), [poprawka przed przeglądem](@@RECORD@@/reports/author-repair.md), [przegląd](@@RECORD@@/reports/review.md), [poprawka](@@RECORD@@/reports/fix.md), [przegląd poprawki](@@RECORD@@/reports/review-fix.md).

**Nie sprawdzono:**

- Żaden agent nie przeszedł po przebudowanym skillu, więc to, czy agenci sięgają po każdy odsyłacz, jest niezweryfikowane. Główną miarą zostają słowa wyżej, a porównanie niesionego tekstu czeka na następne prawdziwe użycie skilla (pytanie 7).
- Recenzent przeczytał w całości 40 ze 151 wybranych decyzji, a 111 tylko po nagłówkach. Autor też czytał fundament częściowo, zapisał to w raporcie i doczytał 12 decyzji cytowanych przy przeredagowanych zdaniach. Uwaga oparta na którejś z nieprzeczytanych decyzji nie zostałaby wychwycona.
- Scalenie `foundations` nie miało własnego przeglądu: wniosło tylko `task-cycle/skill/SKILL.md`, pliku spoza tej zmiany; bramka przeszła też na scalonym drzewie.
- `author.md` zachowuje liczby sprzed poprawki; obowiązują te z tego requestu.
- Zmiana nie dotyka interfejsu użytkownika, więc zrzuty ekranu nie mają zastosowania.

## Uwagi przeglądu

Przed przeglądem autor dostał jedną poprawkę od orkiestratora: wiersz 1 *Settlements to record* przeszedł z osobnego wpisu do WAY-256, a raport pokazał przeszukanie fundamentu. Przegląd dał FAIL z pięcioma uwagami blokującymi, wszystkie poprawione w `c17f4f8`, a przegląd poprawki dał PASS:

1. Liczby słów były nieaktualne na wszystkich drogach.
2. Tryb „tests at a level its cycle chooses”, którego nie ma w bazie ani w To do 3, kierował agenta audytu do `new_level.md`.
3. „Extend what exists” stało w pliku pierwszego kroku, czyli w układzie, który WAY-256 nazywa naruszeniem.
4. WAY-256 miało cztery zdania wiążące przy limicie trzech z WAY-05.
5. Wyjątek w WAY-265 nie obejmował skilla styleguide'u.

Uwagi drobne, otwarte, słowami recenzenta, do wyboru na nowe zadania:

- **`product-guidelines/testing/SKILL.md:89`** (6): The pointer names "tests with no testing guidelines yet" and "a refresh or an extension", but not a product with no tests, which is routes 1, 2 and 6. Add "before the first test" as line 133 of the base has it.
- **`product-guidelines/testing/audit.md`** (7): "A choice found in the product's tests is a proposal, never a rule" is not read on the new-level route with a product that has tests, where the base had it in step 3. Consider `settle.md`, which every route reads.
- **`foundations/decisions.md`, *Rationale* WAY-256 i WAY-265** (8): The new *Rationale* of WAY-256 and that of WAY-265 use "must"; the template keeps normative words to binding sentences.
- **`foundations/decisions.md`, WAY-265 i WAY-266** (9): "with the condition under which it is read" in WAY-265 and the last sentence of WAY-266 are not in rows 2 and 3. Name both in the request so the human reads them as additions. Stan: nazwane niżej, w „Co rozstrzyga ten request”.
- **`reports/assessment.md`, `reports/author.md`** (10): Row 187-194 says the step 4 pointer names "How to show" through `settle.md`; neither does. Row 18-22 says its added sentence is listed under "Text added"; it is not, nor is the clause added to the orchestrated pointer. Also: the assessment's sections stand in the order check, contradictions, table, where `instruction-files/judging.md:13-26` gives check, table, contradictions, and SPLIT and CHOICE are not among its four verdicts; `author.md` says "235 nonblank lines", while the base has 227 nonblank lines and the ranges also hold 8 blank ones.
- **`product-guidelines/testing/recognize.md`** (11): A task that both extends the guidelines and has a first test of a level with a standing recipe takes two modes, one saying step 2 and one saying no step 2. Consider "and no step 2 for it".

Uwagi spoza zakresu zadania: brak. Żadne sprawdzenie nie padło i nie przeszło przy powtórzeniu.

## Co rozstrzyga ten request

Scalenie jest przyjęciem tych wpisów fundamentu. Wszystkie trzy pochodzą z wierszy *Settlements to record*:

- **WAY-256, zmieniona w miejscu (wiersz 1):** fragment potrzebny na niektórych krokach skilla, nie na wszystkich, stoi według swojego rodzaju: reguła pracy zostaje w `SKILL.md`, a tekst do czytania albo zajrzenia stoi w pliku obok, który wymienia każdy z tych kroków.
- **WAY-265, nowa (wiersz 2):** w skillu przebudowywanym albo zmienianym według WAY-256 plik wariantu, do którego odsyła plik kroku, jest wymieniony także w `SKILL.md` przy tym kroku; plik kroku stojący bez zmian razem ze swoim plikiem wariantu reguła omija.
- **WAY-266, nowa (wiersz 3):** w skillu wytycznych produktu sesja, która nie przeczytała kroków 1 i 2 `refine-task`, bo otworzyła skill bezpośrednio albo wznowiła pracę w nowej rozmowie, przechodzi przez nie najpierw.

Dwa dopiski autora wychodzą poza brzmienie wierszy, zgodnie z uwagą 9: w WAY-265 „with the condition under which it is read”, a w WAY-266 ostatnie zdanie, że skille wytycznych bez zmian w tekście nie są związane, dopóki nie zostaną przebudowane. Bez drugiego skill kodu naruszałby wpis od dnia scalenia, a zadanie 8 i tak dopisze mu to zdanie.

Żadnego wpisu rzutowanego, zmienionego testu niezmiennika, zmienionej powierzchni ani oznaczenia *Violated*. Krok powrotny porównał wpisy, decyzje zadania i mapę części z nowymi plikami: nic nie wymagało korekty.

Pytania: brak. Działania człowieka, na które request czeka: brak. Pozostałe wybory w ramach zmiany: 20, w [tabeli pytań i wyborów](@@RECORD@@/cycle.md#questions-and-autonomous-choices). [Czas, modele i tokeny](@@RECORD@@/stages.md).

[Pełny zapis cyklu](@@RECORD@@/cycle.md) stoi w osobnym commicie i jest od razu usuwany następnym, żeby docelowe drzewo trzymało tylko zmianę. **Proszę scalić z zachowaniem commitów, bez squash ani rebase**, bo odsyłacze prowadzą do commita zapisu. Wpisu zadania w backlogu nie zmieniono; domknięcie serii po scaleniu jest poza tym requestem.
