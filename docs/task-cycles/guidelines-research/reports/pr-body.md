Research działa spójnie w wytycznych kodowania, styleguide'a i testów: uruchamia się przy pierwszych wytycznych bez preferencji oraz przy każdej rozbudowie. Odświeżenie dotychczasowego zakresu pomija research. Nowe narzędzie dostaje porównanie skutków dla produktu, rekomendację i jej słaby punkt; preferencja człowieka zachowuje pierwszeństwo.

## Zakres i źródło

Niezależne zadanie „research i rekomendacja narzędzia spójne w trzech skillach wytycznych”, zaakceptowane 2026-10-25, na podstawie `foundations` `2895e0e7860ec1f48ddc7dacd15ef6b26e731c5c`. Zamrożony dokument zadania znajduje się w zapisie cyklu wskazanym poniżej. Nie stwierdzono zmiany źródeł wymagającej uzgodnienia zadania.

Bez osobnego specu i planu: zadanie rozstrzyga wybory projektowe, a zmianę wykonał jeden autor. Poprawione są również dalsze kroki zakładające istnienie raportu researchu. Pierwszy styleguide przy istniejących ekranach przechodzi ścieżkę preferencji/researchu oraz dotychczasowy audyt, zgodnie ze wspólną regułą punktu 1 zadania.

## Co ten PR rozstrzyga

Wpisy wynikające z czterech przyjętych ustaleń zadania:

| Entry | Meaning for the request |
|---|---|
| WAY-185 | Wybór nowej biblioteki komponentów lub sposobu stylowania pozostaje pytaniem zadania dla człowieka, ale dostaje skutki dla produktu, rekomendację i jej słaby punkt; preferencja człowieka ma pierwszeństwo, a bez niej przy remisie wygrywa wariant najprostszy i najtańszy. |
| WAY-186 | Styleguide korzysta z preferencji, przy pierwszych wytycznych bez preferencji i przy każdej rozbudowie robi research, przy odświeżeniu go pomija i nie zastępuje narzędzia preferowanego przez człowieka; istniejące ekrany zachowują audyt obok tej ścieżki. |
| WAY-210 | Nowy linter, formater lub audyt zależności dostaje rekomendację przez skutki dla produktu i słaby punkt zamiast domyślnego wyboru narzędzia najczęściej używanego; preferencja człowieka pozostaje pierwsza, a przy remisie bez preferencji wygrywa wariant najprostszy i najtańszy. |
| WAY-211 | Wytyczne kodowania robią research przy pierwszym zestawie bez preferencji i przy każdej rozbudowie, nie przy odświeżeniu, a wskazane przez człowieka narzędzie pozostaje propozycją. |
| WAY-248 | Nowe narzędzie testów lub biblioteka testów własności pozostaje wyborem człowieka w zadaniu i dostaje skutki dla produktu, rekomendację oraz jej słaby punkt, z pierwszeństwem preferencji i wyborem najprostszego, najtańszego wariantu przy remisie bez preferencji. |
| WAY-249 | Wytyczne testów robią research przy pierwszym zestawie bez preferencji i przy każdej rozbudowie, pomijają go przy odświeżeniu i nie wypierają narzędzia preferowanego przez człowieka. |
| WAY-251 | Odświeżenie aktualizuje albo koryguje przyjęte wytyczne w dotychczasowym zakresie, także przy nowej wersji narzędzia, a rozbudowa obejmuje coś nowego i bada, czy użyć tego, co produkt już ma, czy czegoś innego, zachowując preferencję człowieka. |

Mapowanie ustaleń zadania: 1 → WAY-186/211/249; 2 → WAY-251; 3 → WAY-185/210/248; 4 → WAY-186/211/249 i pierwszeństwo preferencji w WAY-185/210/248. Nie pominięto żadnego ustalenia. WAY-251 jest nowym wpisem dla ustalenia 2; nie ma dodatkowych nowych reguł spoza zadania.

Nie zmieniono niezmienników, ich testów, publicznych interfejsów ani oznaczeń `Violated`. Nazwy, opisy i ścieżki skilli pozostają bez zmian; punkty wejścia nie wymagały regeneracji.

## Sprawdzenie

- `python -B gate/run_tests.py` — exit 0 na `a6453b7`: 605 testów w 8 katalogach, pięć pominiętych z powodu platformy Windows.
- `python -B elements/common/foundation_check.py` — końcowo exit 0, zero błędów. Pośredni przebieg zwrócił exit 1: pięć etykiet `Rejected` połączono z poprzednim akapitem; autor poprawił formatowanie i ponowił kontrolę z wynikiem 0.
- `python -B agent-instructions/skill_entry_points.py` — exit 0, punkty wejścia aktualne.
- `git diff --check` — exit 0; niezależny reviewer sprawdził również cały zakres commitów.
- Niezależny przegląd całej zmiany: **PASS** dla `a6453b7ba019c6f2c54a503fb62adb4a1ffc84e5`, bez uwag.

Pominięte testy w `instruction-files/test_check_instructions.py`: cztery wymagają POSIX (`test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`, `test_an_absolute_link_out_of_the_repository_is_not_read`, `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`, `test_every_directory_link_is_reported_wherever_it_points`), a `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run` wymaga `os.mkfifo`.

Autor przeszedł ręcznie siedem scenariuszy: pierwsze wytyczne z preferencją i bez niej, odświeżenie bez preferencji, nowa wersja narzędzia w dotychczasowym zakresie, rozbudowa z preferowanym narzędziem, nowy wybór ze skutkami oraz remis. Nie znalazł obowiązkowego odwołania do nieistniejącego raportu researchu ani ścieżki wypierającej preferowane narzędzie. Reviewer niezależnie sprawdził te ścieżki.

Nie uruchomiono rzeczywistych sesji refinementu trzema zmienionymi skillami; przejście scenariuszy jest sprawdzeniem instrukcji. Pełnej bramki na bazowym commicie nie uruchomiono; bramka końcowej zmiany przeszła. Nie dodano testów utrwalających brzmienie tekstu. Kontrole uruchomionego produktu i zrzutów UI nie dotyczą tej zmiany.

## Uwagi i przekazanie

- Uwagi Minor: brak.
- Uwagi poza zakresem zadania: brak.
- Pytania do rozstrzygnięcia: brak.
- Działania człowieka poza repozytorium: brak.
- Pozostałe wybory cyklu: 7, opisane z alternatywami i kosztami w tabeli pytań zapisu cyklu.
- Kontrola zgodności dokumentów po zmianie: zgodna; wszystkie cztery ustalenia mają wpisy, mapa części pozostaje aktualna, bez dodatkowej zmiany.

Zapis cyklu w tym commicie: [cycle.md](../cycle.md). Opis PR-a wskazuje ten zapis przez SHA commita dodającego.

Proszę scalić z zachowaniem commitów (merge commit, bez squash/rebase), żeby odnośnik do zapisu cyklu pozostał osiągalny. Zapis ma osobny commit dodający i bezpośrednio następny usuwający; końcowy diff PR-a zawiera tylko zmianę produktu. PR nie został scalony automatycznie.
