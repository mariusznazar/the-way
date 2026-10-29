Sześć skilli fundamentu czytało od razu instrukcje potrzebne tylko na późniejszym kroku lub w innym wariancie. Ta zmiana przenosi procedury do plików wskazanych przy właściwym kroku, zachowując znaczenie reguł i dostęp przez bezpośredni odczyt skilla.

Obejmuje `record-decision`, `record-invariant`, `record-glossary-term`, `record-environment-fact`, `update-part-map`, `critique` oraz wspólną procedurę. Wspólne tryby projektowania wpisów i zakładania brakującego pliku są osobnymi plikami. Trzy sekcje używane przez inne części procesu zachowują nazwy i treść. `find-foundation-entries` otrzymuje wyłącznie odsyłacz potrzebny dla definicji projektu.

Zadanie niezależne, trzecie w serii. Źródło zaakceptowane 2026-10-28; baza i wersja procesu: `745a6e53ec5c8eab3e078a32a61aa6a583a61a93`. Zakres nie wymagał specyfikacji ani planu: wykonał go jeden autor, a drugi agent przejrzał całość i jedną poprawkę. Brak zmiany przypięcia procesu.

## Ocena i pomiar

Siedem pełnych tabel oceny znajduje się w komentarzach PR: 126 fragmentów z dosłownymi cytatami i zakresami linii na `745a6e5`, momentem odczytu, jego rozpoznawalnością oraz werdyktem. [Pełna ocena](./reports/assessment.md) i [pliki składające się na każdą drogę](./reports/word-counts.md) są również w zapisie cyklu.

Poniżej liczba słów rozdzielonych białymi znakami, z Markdownem i frontmatterem, w całym ukończonym przebiegu: każdy odczytany plik skilla, wspólnej procedury i plików pomocniczych liczony raz. To pomiar tekstu, nie wynik eksperymentu zachowania agenta ani tokenów niesionych w sesji.
| Complete route | Before | After | After minus before |
|---|---:|---:|---:|
| decisions / foundation entry | 2921 | 2389 | -532 |
| decisions / projected entry | 2921 | 2901 | -20 |
| decisions / first element file | 2921 | 2522 | -399 |
| invariants / foundation entry | 3143 | 2716 | -427 |
| invariants / projected entry | 3143 | 3135 | -8 |
| invariants / first element file | 3143 | 2849 | -294 |
| glossary / foundation entry | 2988 | 2520 | -468 |
| glossary / projected entry | 2988 | 2992 | +4 |
| glossary / first element file | 2988 | 2653 | -335 |
| environment-facts / foundation entry | 3028 | 2601 | -427 |
| environment-facts / projected entry | 3028 | 3056 | +28 |
| environment-facts / first element file | 3028 | 2734 | -294 |
| part-map / foundation entry | 3073 | 2573 | -500 |
| part-map / projected entry | 3073 | 2992 | -81 |
| environment-facts / withdrawal | 3028 | 2601 | -427 |
| part-map / first map | 3073 | 2775 | -298 |
| critique / critic | 766 | 616 | -150 |
| critique / author invoking and settling | 766 | 831 | +65 |

## Fixed addition, counted once per invocation

| Entry kind | Element template | Common rules | Sum to add before and after |
|---|---:|---:|---:|
| decisions: `elements/decisions/template.md` | 2046 | 747 | 2793 |
| invariants: `elements/invariants/template.md` | 2235 | 747 | 2982 |
| glossary: `elements/glossary/template.md` | 998 | 747 | 1745 |
| environment-facts: `elements/environment-facts/template.md` | 2379 | 747 | 3126 |
| part-map: `elements/part-map/template.md` | 1532 | 747 | 2279 |
| critique | 0 | 0 | 0; this skill mandates neither an element template nor common rules |

Zwykły wpis zakłada istniejący plik elementu; wariant pierwszego pliku dodaje jego osobną procedurę. Jeżeli brakuje także mapy części, dochodzi wywołanie pierwszej mapy, z plikami wspólnymi liczonymi raz. Przykłady elementów, źródła zadania i konkretne wpisy fundamentu pozostają obowiązkowe, lecz nie wchodzą do określonego zadaniem pomiaru; zależą od wywołania. Szczegóły warunków są w raporcie pomiaru.

## Propozycje pozostawione do decyzji

Istniejące akapity określające formę wpisów pozostały bez zmian w SKILL.md: przeniesienie ich do plików obok naruszyłoby kryterium zadania, a ich szablony są poza zakresem. Ocena proponuje docelowe uporządkowanie tej duplikacji w szablonach. Pozostawienie jej kosztuje dodatkowy tekst przy każdym użyciu; uporządkowanie wymaga osobnej zmiany szablonów i sprawdzenia wszystkich ich czytelników. W tej zmianie nie wykonano żadnego usunięcia ani przeredagowania zmieniającego znaczenie reguły.

## Weryfikacja

`python -B gate/run_tests.py` zakończyło się kodem **0** zarówno na bazie `745a6e5`, jak i na końcowym przejrzanym commicie `4d2f95e`: **613 przypadków w 8 zestawach, 608 zaliczonych i 5 pominiętych na Windows**. Pominięte przypadki z `instruction-files/test_check_instructions.py` nie są liczone jako zaliczone:

- `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does` — wymaga POSIX.
- `test_an_absolute_link_out_of_the_repository_is_not_read` — wymaga POSIX.
- `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on` — wymaga POSIX.
- `test_every_directory_link_is_reported_wherever_it_points` — wymaga POSIX.
- `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run` — brak FIFO na tej platformie.

Testy skupione: `python -B gate/run_tests.py agent-instructions`, kod 0, 18 testów.

Niezależny przegląd: początkowo jedna uwaga Important o niewydzielonym wariancie brakującego pliku fundamentu; poprawiona w `4d2f95e`. Ponowny przegląd: PASS. Otwarte uwagi Minor: brak. Uwagi poza zakresem: brak. [Przegląd całej zmiany](./reports/review.md), [przegląd poprawki](./reports/review-fix.md).

Autor i recenzent niezależnie sprawdzili literalne cytaty z zakresami linii, pokrycie siedmiu ocenianych plików i końcowe koszty 18 dróg użycia. Kontrola autora sprawdza również zachowanie treści, 23 odsyłacze do plików pomocniczych, trzy niezmienione sekcje zewnętrzne i warunek odczytu procedury brakującego pliku. Testy dotyczące instrukcji agentów: 18, exit 0. Sprawdzenie fundamentu, wejść skilli i instrukcji: exit 0; pozostaje wcześniejsze ostrzeżenie o prywatnym względnym odsyłaczu `_zadania` w AGENTS.md. [Wszystkie polecenia i kody wyjścia autora](./reports/author.md), [poprawki](./reports/fix.md), [weryfikacja cyklu](./cycle.md#verification).

Nie wykonano pomiaru zachowania agentów w loop2 ani pomiaru kosztu po scaleniu — zadanie umieszcza je poza tym PR. Brak zmian interfejsu użytkownika; zrzuty ekranu nie mają zastosowania.

## Co rozstrzyga ten PR

Brak nowych lub zmienionych wpisów fundamentu, zaakceptowanych wierszy ustaleń i projektowanych wpisów. Brak zmienionych testów niezmienników, powierzchni produktu lub oznaczeń Violated. Kod Pythona, szablony i wspólne reguły formy są bez zmian. Końcowe porównanie z fundamentem potwierdziło zgodność bez korekty i bez nowego commita; po uzgodnieniu z aktualną gałęzią foundations drzewo nadal odpowiada przetestowanej wersji.

Brak pytań i działań człowieka blokujących PR. Osiem roboczych wyborów opisuje [tabela cyklu](./cycle.md#questions-and-autonomous-choices); wybór drogi wykonania jest opisany osobno. [Czas, modele i tokeny](./stages.md).

[Pełny zapis cyklu](./cycle.md) jest utrwalony w osobnym commicie i od razu usunięty następnym, aby docelowe drzewo zawierało tylko zmianę. **Proszę scalić z zachowaniem commitów, bez squash/rebase**, ponieważ odsyłacze prowadzą do commita zapisu. PR nie został scalony. Wpisu zadania w backlogu nie zmieniono; domknięcie serii po scaleniu pozostaje poza zakresem.
