`maintain-styleguide` kazał na wejściu przeczytać ok. 9000 słów, w tym pliki, które sesja znała już z `refine-task`. Po tej zmianie każdy krok czyta tylko to, czego potrzebuje, a główny plik skilla ma 906 słów zamiast 2830. Żadna reguła nie zniknęła ani nie zmieniła znaczenia. Zmiana poprawia też jedno zdanie w pliku, którym cykl ocenia skille, bo dawało sprzeczne odpowiedzi.

Zadanie niezależne, czwarte z jedenastu w serii przebudowy skilli. Opis przyjęty 2026-10-30, baza `foundations` `525cde1dd53c474f56ea0ece289cb60e868aa90d`. Sesja pracowała na samym the way, więc nie ma przypięcia procesu ani jego przesunięcia. Specyfikacji nie było, bo zadanie nie zostawiło otwartego wyboru projektowego: podział na pliki to sposób wykonania tego, co zadanie rozstrzygnęło. Planu nie było, bo jeden skill i jedno zdanie w drugiej części mieszczą się w pracy jednego autora.

## Co się zmieniło

- `product-guidelines/styleguide/SKILL.md` trzyma obraz całości, zasady wspólne dla kroków i odsyłacze. Procedury kroków 1–5 i wariantów stoją w dziesięciu plikach obok: `recognize.md`, `starting_rules.md`, `research.md`, `audit.md`, `settle.md`, `new_tools.md`, `staged_cleaning.md`, `task_document.md`, `hand_back.md`, `orchestrated_mode.md`.
- Krok 0 nie każe już czytać wszystkiego naraz. Szablon styleguide'u jest czytany na kroku 2, szablon wytycznych na kroku 4, a pliki krytyki przy pierwszej krytyce. To, co sesja przeczytała w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz.
- `instruction-files/kind_skill.md:8-14` mówi teraz to samo co WAY-256: w `SKILL.md` zostaje to, czego potrzebuje każdy krok, a fragment jednego kroku idzie do pliku obok także wtedy, gdy dochodzi do niego każde użycie skilla.
- Kod w Pythonie, szablony i pozostałe pliki z kroku 0 się nie zmieniły.

## Ocena skilla

Pełna tabela oceny stoi w [komentarzu pod tym requestem](@@ASSESSMENT_COMMENT@@): 50 wierszy i 2 propozycje, każdy fragment zacytowany dosłownie z zakresem linii na `525cde1`, z tym, kiedy jest potrzebny, czy agent rozpozna ten moment, oraz z werdyktem. Wszystkie 205 niepustych linii bazy stoi w dokładnie jednym wierszu.

Dwie propozycje nie zostały wykonane, bo zmieniają treść reguły. Autor ich nie rekomenduje: w przeszukanych zapisach nie ma błędu, który by je uzasadniał.

- **P1, `SKILL.md:92`:** czytać z `guidelines/` produktu tylko plik części, której dotyczy zadanie, i indeks wytycznych kodu. Bez zmiany sesja czyta wszystkie pliki pod `guidelines/`, co kosztuje tyle słów, ile produkt ma wytycznych. Po zmianie czyta mniej, ale może pominąć regułę z pliku innej części.
- **P2, `SKILL.md:190-197`:** proponować decyzję o przyjęciu WCAG tylko wtedy, gdy dziennik produktu jej nie ma. Bez zmiany odświeżenie styleguide'u proponuje ją po raz kolejny, co jest zbędną rozmową. Po zmianie warunek wychodzi poza brzmienie WAY-191, więc wymagałby zmiany tej decyzji.

## Liczby słów

| Droga | Przed krokiem 4: przed → po | Suma na koniec: przed → po | Suma bez pierwszych odczytów: przed → po |
|---|---:|---:|---:|
| 1. Pierwszy styleguide, bez ekranów, człowiek bez preferencji | 12678 → 7290 (−42%) | 12678 → 9672 (−24%) | 9843 → 6837 |
| 2. To samo, człowiek z preferencją | 12169 → 6248 (−49%) | 12678 → 9461 (−25%) | 9843 → 6626 |
| 3. Pierwszy styleguide, są ekrany (liczone bez preferencji: badania i audyt) | 12678 → 7527 (−41%) | 12678 → 9909 (−22%) | 9843 → 7074 |
| 4. Odświeżenie bez zmienionych ekranów | 12169 → 6248 (−49%) | 12678 → 9461 (−25%) | 9843 → 6626 |
| 5. Rozszerzenie ze zmienionymi ekranami | 12678 → 7527 (−41%) | 12678 → 9909 (−22%) | 9843 → 7074 |
| 6. Tryb orkiestrowany na drodze 1 | 12678 → 7394 (−42%) | 12678 → 9776 (−23%) | 9843 → 6941 |
| 7. Produkt bez interfejsu, koniec na kroku 1 | 12169 → 4086 (−66%) | 12169 → 4086 (−66%) | 9334 → 1251 |

Liczone są słowa rozdzielone białymi znakami, razem z Markdownem i nagłówkiem pliku. Plik czytany dwa razy w stanie „przed” liczy się dwa razy, więc liczby obejmują też pierwszy odczyt w `refine-task` czterech rzeczy, które krok 0 kazał czytać ponownie (2835 słów). Ostatnia kolumna pomija ten pierwszy odczyt. Poza liczeniem zostają pliki produktu i inne pliki `refine-task`, jednakowe w obu stanach. To liczby słów w plikach, nie pomiar zachowania agenta ani tokenów. [Skład każdej drogi plik po pliku](@@RECORD@@/reports/word-counts.md).

Różnice wobec szacunków z zadania:

- Stan „przed” to 9334 słowa wobec ok. 8850. Różnica to 492 słowa sekcji „Reading the foundation”, czytanej dwa razy, której szacunek nie liczył; po odjęciu wychodzi 8842.
- Stan „po” to 6626 słów wobec ok. 5900, czyli 726 więcej. Zadanie nie podaje składu tej liczby. Recenzent wyprowadza ją jako ok. 8270 minus ok. 2350 i wtedy różnica to 509 słów plików obok krytyki, których szacunek nie liczył, oraz ok. 217 słów odsyłaczy i nagłówków. To jego wniosek z liczb zadania, nie zapis z zadania.
- `SKILL.md` ma 906 słów wobec ok. 600. Nadwyżka to tabela „Where the skill works” i reguły obowiązujące na kilku krokach. Na sumę nie wpływa, bo na drogach pełnych te słowa i tak byłyby czytane.

## Sprawdzenia

`python -B gate/run_tests.py`: kod **0** na bazie `525cde1` i na przejrzanym `d32f76d`, 614 testów w 8 katalogach, każdy katalog przeszedł. Pięć sprawdzeń pominął Windows, więc nie liczą się jako zaliczone, wszystkie z `instruction-files/test_check_instructions.py`:

- `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`, wymaga POSIX
- `test_an_absolute_link_out_of_the_repository_is_not_read`, wymaga POSIX
- `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`, wymaga POSIX
- `test_every_directory_link_is_reported_wherever_it_points`, wymaga POSIX
- `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`, brak FIFO na tej platformie

`foundation_check.py`, `check_instructions.py` (wynik taki sam jak na bazie, w tym ostrzeżenie o `_zadania\` w `AGENTS.md:21`) i `skill_entry_points.py --write` (nic nie zmienił): kod 0.

Autor za najsłabszy punkt uznał zachowanie reguł. Porównanie bazy z nowymi plikami zdanie po zdaniu dało 15 fragmentów niedosłownych, każdy rozliczony jako odsyłacz albo przeredagowanie bez zmiany znaczenia. Recenzent powtórzył porównanie własnym skryptem, przeliczył cytaty i wszystkie drogi oraz przeszedł siedem dróg przez nowe pliki jak agent czytający `SKILL.md` po ścieżce: każda reguła dociera tam, gdzie jest potrzebna. [Autor](@@RECORD@@/reports/author.md), [poprawka](@@RECORD@@/reports/fix.md), [przegląd](@@RECORD@@/reports/review.md), [przegląd poprawki](@@RECORD@@/reports/review-fix.md).

**Nie sprawdzono:** żaden agent nie przeszedł po przebudowanym skillu, więc to, czy agenci sięgają po każdy odsyłacz, pozostaje niezweryfikowane. Pomiar niesionego tekstu po scaleniu jest poza tym requestem. Autor nie przeczytał w całości 20 decyzji z listy zlecenia; przeczytał je recenzent, poza końcówką WAY-134, i żadna nie jest naruszona. Zmiana nie dotyka interfejsu użytkownika, więc zrzuty ekranu nie mają zastosowania.

## Uwagi przeglądu

Pierwszy przegląd dał FAIL z dwiema uwagami blokującymi: liczby słów pomijały sekcję czytaną dwa razy, a `recognize.md` kazał czytać drugi raz wytyczne przeczytane już przez `refine-task`. Obie poprawione w `d32f76d`; przegląd poprawki dał PASS.

Uwagi drobne, otwarte, słowami recenzenta, do wyboru na nowe zadania:

- **`instruction-files/kind_skill.md:8-14`:** The two answers are now "every step needs it" and "only one step or one variant needs it", so a fragment that two or three steps need fits neither. Tasks 5 to 11 judge by this file and will meet that case. Should it be settled now?
- **`product-guidelines/styleguide/starting_rules.md:10`, `settle.md:4`, `settle.md:38`:** `research.md`, `new_tools.md` and `staged_cleaning.md` are reached through a file beside the skill, while `instruction-files/SKILL.md:174` says a step points one level deep. The assessment table does not mention this; only the author's report does.
- **`product-guidelines/styleguide/staged_cleaning.md:3-5`, `settle.md:37-38`:** The file holds one sentence, and the pointer to it takes 21 of those 54 words. Is that two instructions, as the row says, or the one instruction WAY-256 keeps where its pointer would stand?
- **`product-guidelines/styleguide/SKILL.md:65-69`, `recognize.md:11`:** A session that opens this skill directly, as its description allows, is told that the task template, "How a skill asks" and the foundation are "not read again" although it never read them. Nothing sends it to `refine-task` first.
- **`reports/assessment.md:53`, `:61`, `:84`, `:31`:** Three rows name no ground, and contradictions stand before the table rather than after it.
- **`reports/word-counts.md:8`; `reports/author.md:110`, `:76`:** Two matters of the counts' account, neither changing a difference between before and after: `word-counts.md:8` departs from the rule as written and needs the orchestrator's confirmation, and the reason `author.md:110` gives for missing 5900 is wrong and should not go into the request. Stan: wyłączenie potwierdzone jako reguła cyklu, a błędne uzasadnienie wycofane w `fix.md`.
- **`reports/fix.md:36`:** The base `SKILL.md` has 232 lines, not 233. `assessment.md:3` has it right.
- **`reports/fix.md:35`, `:51`; `task.md:43`, `:45`:** The task gives about 8270 words on the route with no research and no audit, and about 2350 words already read; their difference is about 5900. Stan: uwzględnione wyżej, w różnicach wobec szacunków.

Uwagi spoza zakresu zadania: brak.

## Co rozstrzyga ten request

Żadnego nowego ani zmienionego wpisu fundamentu, żadnego wiersza *Settlements to record*, żadnego wpisu rzutowanego. Żadnego zmienionego testu niezmiennika, żadnej zmienionej powierzchni, żadnego oznaczenia *Violated*. Krok powrotny porównał decyzje zadania i mapę części z nowymi plikami: nic nie wymagało korekty.

Pytania: brak. Działania człowieka, na które request czeka: brak. Pozostałe wybory w ramach zmiany: 16, w [tabeli pytań i wyborów](@@RECORD@@/cycle.md#questions-and-autonomous-choices). [Czas, modele i tokeny](@@RECORD@@/stages.md).

[Pełny zapis cyklu](@@RECORD@@/cycle.md) stoi w osobnym commicie i jest od razu usuwany następnym, żeby docelowe drzewo trzymało tylko zmianę. **Proszę scalić z zachowaniem commitów, bez squash ani rebase**, bo odsyłacze prowadzą do commita zapisu. Wpisu zadania w backlogu nie zmieniono; domknięcie serii po scaleniu jest poza tym requestem.
