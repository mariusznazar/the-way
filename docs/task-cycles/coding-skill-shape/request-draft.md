`maintain-coding-guidelines` kazał na wejściu przeczytać ok. 7200 słów z innych plików, w tym 3391 słów, które sesja znała już z `refine-task`. Po tej zmianie każdy krok czyta tylko to, czego potrzebuje, a główny plik skilla ma 1506 słów zamiast 3396. Czytanie do końca skilla spada o 19,3–25,0%, licząc pierwszy odczyt w `refine-task`. Skill dostał też piąty tryb: wzorzec rodzaju kodu, którego pliki produkt już ma, bez wpisu w indeksie wytycznych. Poza tym trybem żadna reguła nie zniknęła ani nie zmieniła znaczenia. Scalenie przyjmuje dwie zmiany fundamentu: WAY-216 i WAY-266, obie rozstrzygnięte w przyjętym opisie zadania.

Zadanie niezależne, ósme z jedenastu w serii przebudowy skilli. Opis przyjęty 2026-10-31, baza `foundations` `f86fd71f3cb72a9eb1620c388af44bbd1198fb4a`; do czasu tego requestu `foundations` się nie ruszyło. Sesja pracowała na samym the way, więc nie ma przypięcia procesu ani jego przesunięcia. Specyfikacji nie było, bo zadanie nie zostawiło otwartego wyboru projektowego: pytania 1–8 i trzy wiersze *Settlements to record* rozstrzygają treść, a podział na pliki to sposób wykonania. Planu nie było, bo jeden skill, jeden nowy tryb i dwie zmiany fundamentu zależą od jednej oceny i mieszczą się w pracy jednego autora.

## Co się zmieniło

- `product-guidelines/coding/SKILL.md` trzyma obraz całości, zasady wspólne dla kroków i odsyłacze. Procedury kroków i wariantów stoją w dziesięciu plikach obok: `recognize.md`, `starting_set.md`, `research.md`, `trial_run.md`, `kinds.md`, `settle.md`, `new_tools.md`, `task_document.md`, `hand_back.md`, `orchestrated_mode.md`.
- Krok 0 nie każe już czytać wszystkiego naraz. Szablon kodu jest czytany przed pierwszym krokiem, który go używa, na każdej drodze, także na „A new kind”. Szablon wytycznych czyta krok 4, a pliki krytyki pierwsza krytyka. To, co sesja przeczytała w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz.
- Krok 0 kończy się zdaniem odsyłającym sesję bez kroków 1 i 2 `refine-task` najpierw do nich, w brzmieniu ze skilla testów.
- `research.md` i `new_tools.md` są wymienione także w `SKILL.md` przy swoim kroku, z warunkiem, kiedy się je czyta.
- **Piąty tryb.** Produkt ma pliki rodzaju kodu, którego nie ma w indeksie `guidelines/coding.md`, ten plik stoi, a zadanie go nie odświeża ani nie rozszerza. Agent idzie wtedy przez `kinds.md` tylko dla tego rodzaju, bez kroku 2 i bez próbnego przebiegu, a kroki 4 i 5 rozstrzygają i sprawdzają tylko to, co dotyczy tego rodzaju. `kinds.md` nazywa tę drogę porównaniem z WAY-200, nie audytem z WAY-201.
- Kod w Pythonie, opis skilla, wejścia `the-way-*`, szablony i `product-guidelines/reading.md` się nie zmieniły.

## Ocena skilla

Pełna tabela oceny stoi w [komentarzu pod tym requestem](https://github.com/mariusznazar/the-way/pull/64#issuecomment-6544817327): 56 wierszy i 2 propozycje, każdy fragment zacytowany dosłownie z zakresem linii na `f86fd71`, z tym, kiedy jest potrzebny, czy agent rozpozna ten moment, z werdyktem i miejscem po przebudowie. Wszystkie 247 niepustych linii bazy stoi w dokładnie jednym wierszu.

Dwie propozycje nie zostały wykonane, bo zmieniają treść reguły:

- **P1, `SKILL.md:223-224`, `:269` i `:63-69` na bazie, teraz `settle.md`, `hand_back.md` i `task_document.md`, autor rekomenduje:** na drodze „A new kind” rozstrzygać i sprawdzać tylko te stałe sprawdzenia, których dotyka nowy rodzaj. Dziś agent, który tworzy pierwszy plik rodzaju w produkcie z gotowymi wytycznymi, czyta, że zadanie nie jest gotowe bez decyzji o każdym stałym sprawdzeniu, i że *To do* ma instalować każde narzędzie, choć to wszystko rozstrzygnięto przy pisaniu ogólnego pliku. Bez zmiany agent albo rozstrzyga to samo drugi raz, albo odchodzi od tekstu skilla. Po zmianie tej sprzeczności nie ma, kosztem jeszcze jednego wyjątku w krokach 4 i 5 obok tego z piątego trybu. To sprzeczność z To do 8, której cykl nie naprawia.
- **P2, `SKILL.md:108` na bazie, teraz `recognize.md`, autor nie rekomenduje:** czytać z `guidelines/` produktu tylko plik części, której dotyczy zadanie, i indeks wytycznych kodu. Bez zmiany sesja czyta całość, co kosztuje tyle słów, ile produkt ma wytycznych. Po zmianie czyta mniej, ale może pominąć regułę z pliku innej części. W przeszukanych zapisach nie ma błędu, który by ją uzasadniał.

## Liczby słów

| Droga | Przed krokiem 4: przed → po | Suma na koniec: przed → po | Suma bez pierwszego odczytu: przed → po |
|---|---:|---:|---:|
| 1. Brak kodu, człowiek bez preferencji | 14511 → 8620 (−41%) | 14511 → 11267 (−22,4%) | 11120 → 7876 (−29%) |
| 2. Brak kodu, człowiek z preferencją | 14002 → 7592 (−46%) | 14511 → 11070 (−23,7%) | 11120 → 7679 (−31%) |
| 3. Jest kod, nie ma wytycznych, bez preferencji; a także rozszerzenie | 14511 → 9064 (−38%) | 14511 → 11711 (−19,3%) | 11120 → 8320 (−25%) |
| 4. Odświeżenie | 14002 → 8036 (−43%) | 14511 → 11514 (−20,7%) | 11120 → 8123 (−27%) |
| 5. „A new kind”, gdy wytyczne już stoją | 14002 → 5300 (−62%) | 14511 → 10890 (−25,0%) | 11120 → 7499 (−33%) |
| 6. Jeden rodzaj, którego pliki już są | 14002 → 7607 (−46%) | 14511 → 11085 (−23,6%) | 11120 → 7694 (−31%) |
| 7. Tryb orkiestrowany na drodze 1 | 14511 → 8733 (−40%) | 14511 → 11380 (−21,6%) | 11120 → 7989 (−28%) |

Słowa liczone są jak `wc -w`, w stanie „przed” na `f86fd71`. Dwie pierwsze kolumny obejmują pierwszy odczyt w `refine-task` (3391 słów), a ostatnia go pomija. Plik czytany dwa razy w stanie „przed” liczy się dwa razy, pliki obok krytyki (509 słów) wchodzą tam, gdzie droga do nich dochodzi, a pliki produktu są poza liczeniem. `new_tools.md` (69 słów) dochodzi tylko wtedy, gdy nowe narzędzie zostaje pytaniem o technologię. Droga 6 w stanie „przed” nie istniała, więc liczona jest tak, jak zwykły przebieg bazy. To liczby słów w plikach, nie pomiar zachowania agenta ani tokenów. [Skład każdej drogi plik po pliku](RECORD_LINK/reports/word-counts.md).

**Wynik jest gorszy od szacunku z pytania 1.** Suma na koniec to 10 890–11 711 słów (−19,3 do −25,0%) wobec szacunku 10 600–11 300 (−22 do −27%): drogi 3, 4 i 7 są powyżej górnej granicy, o 411, 214 i 80 słów. Przed krokiem 4 jest 5300–9064 wobec 5100–8800: droga 3 jest o 264 słowa wyżej. Skill i pliki obok mają razem 4169 słów wobec 3396, czyli o 773 więcej, a nie o ok. 400. Do utrzymania dochodzi dziesięć plików. Przyrost biorą odsyłacze, zdania otwierające pliki kroków 4 i 5 oraz piąty tryb.

## Sprawdzenia

`python -B gate/run_tests.py`: kod **0** na bazie `f86fd71`, na `097123e` i na przejrzanym `088717a`, za każdym razem 615 testów w 8 katalogach, każdy katalog przeszedł. Pięć sprawdzeń pominął Windows, więc nie liczą się jako zaliczone, wszystkie z `instruction-files/test_check_instructions.py`:

- `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`, wymaga POSIX
- `test_an_absolute_link_out_of_the_repository_is_not_read`, wymaga POSIX
- `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`, wymaga POSIX
- `test_every_directory_link_is_reported_wherever_it_points`, wymaga POSIX
- `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`, brak FIFO na tej platformie

`foundation_check.py`, `check_instructions.py` (wynik taki sam jak na bazie, w tym ostrzeżenie o `_zadania\` w `AGENTS.md:21`) i `skill_entry_points.py --write` (nic nie zmienił): kod 0. Liczby słów powstały po ostatniej zmianie liczonego pliku; skrypt autora porównał z plikami 346 liczb, a skrypt recenzenta 371, bez różnic.

Autor za najsłabszy punkt uznał zachowanie reguł. Porównanie bazy z nowymi plikami zdanie po zdaniu dało 13 niedosłownych fragmentów na 157, każdy rozliczony. Recenzent powtórzył porównanie własnym skryptem, przeliczył cytaty i wszystkie drogi i przeszedł ręcznie siedem dróg od `SKILL.md` do pliku ostatniego kroku. Sprawdzenie autora nie mogło zobaczyć nowego zdania, które wyłącza stare: to pierwsza uwaga blokująca niżej. [Autor](RECORD_LINK/reports/author.md), [przegląd](RECORD_LINK/reports/review.md), [poprawka](RECORD_LINK/reports/fix.md), [przegląd poprawki](RECORD_LINK/reports/review-fix.md), [krok powrotny](RECORD_LINK/reports/return.md).

**Nie sprawdzono:**

- Żaden agent nie przeszedł po przebudowanym skillu, więc to, czy agenci sięgają po każdy odsyłacz, jest niezweryfikowane. Główną miarą zostają słowa wyżej, a porównanie niesionego tekstu czeka na następne prawdziwe użycie skilla (pytanie 6).
- Piąty tryb nie ma za sobą prawdziwego przypadku (pytanie 3).
- Recenzent przeczytał w całości wybrane decyzje dotyczące zmiany, 87 łącznie, ale 65 ze 140 wybranych po *Scope* tylko po nagłówkach; to decyzje o styleguide'zie, testach i innych elementach. Autor przeczytał w całości część listy z przekazania i doczytał w kroku powrotnym wszystkie decyzje z *Decisions in play*. Uwaga oparta na którejś z nieprzeczytanych decyzji nie zostałaby wychwycona.
- `author.md` i `fix.md` zachowują liczby o 7 słów niższe; obowiązują te z tego requestu i z `word-counts.md`.
- Zmiana nie dotyka interfejsu użytkownika, więc zrzuty ekranu nie mają zastosowania.

## Uwagi przeglądu

Przegląd dał FAIL z dwiema uwagami blokującymi, obie w tekście dopisanym przez autora, obie poprawione w `088717a`, a przegląd poprawki dał PASS:

1. Otwarcie `task_document.md` mówiło na drodze jednego rodzaju „tylko to”, więc z dokumentu zadania wypadał test każdego nowego niezmiennika i miejsca `do not copy`. Tak samo `settle.md` zostawiało otwarte, czy krytyka się odbywa.
2. *Rationale* WAY-216 zawierało powód, którego nikt nie podał, a o próbnym przebiegu był nieprawdziwy. Powód pochodzi teraz z wierszy 1 i 2 i z pytania 3.

Uwagi drobne, otwarte, słowami recenzenta, do wyboru na nowe zadania. Wszystkie dotyczą dokumentów cyklu, poza dwiema ostatnimi o fundamencie:

- **`reports/assessment.md:31`** (3): `judging.md` gives check script, table, contradictions; the assessment has contradictions before the table and numbers them so. Three rows read `SPLIT`, which is not one of its four verdicts.
- **`reports/assessment.md:81`** (4): The row of `:187-196` says "Mistake: not found in the records searched", but commits 5a00041 and f34e477 record the correction that made "the audit covers every one of them" read as it does.
- **`reports/assessment.md:29`** (5): "The paths named by the rebuilt files were checked by hand, see the author's report": the report holds no such check.
- **`reports/assessment.md:115`** (6): P1 quotes `:223-224` and only lists `:269` and `:63-69`, while saying "the lines are quoted whole"; and it is marked RECOMMENDED without saying what lets it in.
- **`reports/author.md:51`** (7): The report's table is 7 words low on every "after" figure; `word-counts.md` is right. Take the request's figures from `word-counts.md`.
- **`reports/assessment.md:47`** (A): The row still says the list costs "about 489 words"; the file now has 509.
- **`reports/fix.md:57`** (C): `SKILL.md` has 1506 words, not 1499, and the text beside the template is 4169, not 4162, so it grew by 773 words. Its table of routes is right.
- **`foundations/decisions.md:5974`** (8): "four modes of the coding-guidelines skill left as they were" holds a count and a state of the process's own skill, which author-written prose of an entry leaves out.
- **`foundations/decisions.md:5969`** (B): "Without the third sentence" holds only while the entry keeps that order, and the second reason repeats the words of the *Rejected* five lines below.

Uwagi spoza zakresu zadania: brak. Żadne sprawdzenie nie padło i nie przeszło przy powtórzeniu.

Jedno miejsce zostaje niejasne, bez uwagi blokującej: zdanie z To do 9, że przy połączeniu trybów wygrywa szerszy, nie rozstrzyga połączenia piątego trybu z „A new kind”, bo żaden nie jest szerszy. Autor puszcza oba obok siebie, a recenzent uważa to za słuszne. `SKILL.md:71` mówi wtedy „only what concerns that kind” przy dwóch rodzajach. Za tym przypadkiem nie stoi żadne prawdziwe użycie.

## Co rozstrzyga ten request

Scalenie jest przyjęciem tych zmian fundamentu. Obie pochodzą z wierszy *Settlements to record*:

- **WAY-216, zmieniona w miejscu (wiersze 1 i 2):** ani pierwszy plik rodzaju, ani porównanie plików rodzaju bez wpisu w indeksie nie czyni samo zadania rozszerzeniem według WAY-251 i nie wymaga badań stałych sprawdzeń; porównanie obejmuje tylko ten rodzaj, nie bierze próbnego przebiegu zestawu lintera i nie jest audytem z WAY-201. Decyzja dostaje relację `narrows WAY-251`, a tekst WAY-251 się nie zmienia.
- **WAY-266, zmieniona w miejscu (wiersz 3):** znika ostatnie zdanie o skillach wytycznych, które nie są związane decyzją, dopóki ich nie przebudowano, bo po tym zadaniu wszystkie trzy skille wytycznych mają zdanie z kroku 0.

Autor dopisał do WAY-216 przykłady w *Verification* oraz ścieżki niewybrane w *Rejected* i powód w *Rationale*, wszystkie ze źródeł zadania.

Żadnego nowego wpisu, wpisu rzutowanego, zmienionego testu niezmiennika, zmienionej powierzchni ani oznaczenia *Violated*. Krok powrotny porównał obie zmiany, decyzje zadania i mapę części z nowymi plikami: nic nie wymagało korekty.

Pytania: brak. Działania człowieka, na które request czeka: brak. Pozostałe wybory w ramach zmiany: 16, w [tabeli pytań i wyborów](RECORD_LINK/cycle.md#questions-and-autonomous-choices). [Czas, modele i tokeny](RECORD_LINK/stages.md).

[Pełny zapis cyklu](RECORD_LINK/cycle.md) stoi w osobnym commicie i jest od razu usuwany następnym, żeby docelowe drzewo trzymało tylko zmianę. **Proszę scalić z zachowaniem commitów, bez squash ani rebase**, bo odsyłacze prowadzą do commita zapisu. Wpisu zadania w backlogu nie zmieniono; domknięcie serii po scaleniu jest poza tym requestem.
