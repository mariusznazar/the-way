---
title: "the way: skrypty po przeglądzie fundamentu — brakujące pole, kontrole tekstów i ich testy, liczenie audytu"
status: draft
created: 2026-11-15
updated: 2026-11-15
tags: [zadanie]
related: "a link to the project's note"
---

# the way: skrypty po przeglądzie fundamentu — brakujące pole, kontrole tekstów i ich testy, liczenie audytu

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/10 · https://github.com/mariusznazar/the-way/pull/25 · https://github.com/mariusznazar/the-way/pull/42 · https://github.com/mariusznazar/the-way/pull/77 · https://github.com/mariusznazar/the-way/pull/83 · https://github.com/mariusznazar/the-way/pull/95 · https://github.com/mariusznazar/the-way/pull/97 · https://github.com/mariusznazar/the-way/pull/104 · https://github.com/mariusznazar/the-way/pull/105 · https://github.com/mariusznazar/the-way/pull/112 · https://github.com/mariusznazar/the-way/pull/120

## Description

### Need

- Przegląd fundamentu the way z 2026-11-14 (sprawdzony commit `21ecb62`) znalazł skrypty the way, które dają złą albo pustą odpowiedź, przepuszczają to, czego reguła zabrania, albo zabraniają tego, na co reguła pozwala; Mariusz zdecydował, że idą jednym zadaniem.
- P16 (WAY-344, uwagi #103-1, #104-1, #112): trzy skrypty czytają brakujące pole inaczej, niż każe WAY-344 — następny agent dostaje dwa przeciwne polecenia, a kto czyta nocny wynik audytu, dostaje błąd z nazwą tabeli zamiast poziomu.
- G1 (6 uwag z próśb: #100-3, #100-5, #106-16, #106-2, #106-13, #106-10, i jedna pozycja z lektury fundamentu): liczenie audytu i skrypty etapów i miar cyklu dają w trzech miejscach złą albo pustą odpowiedź (wyciąg stosu zamiast tabeli etapów na Windows, `unknown` przy większości wersji procesu, cykl liczony pod złą wersją), w dwóch nikt nie sprawdził ich na prawdziwych danych, a cennik audytu nie wycenia godzinnej pamięci podręcznej autora, którą wybrała WAY-368.
- G3 (9 uwag z próśb: #97-1, #120-16, #77-4, #86-7, #105-1, #83-4, #95-7, #95-9, #87-9): kontrola formy fundamentu, test importów między częściami, kontrola ścieżek prywatnych i skrypt uwag procesowych cyklu przepuszczają coś, czego reguła zabrania, albo zabraniają czegoś, na co reguła pozwala; dwa testy instalatora dają fałszywie czerwoną bramkę, gdy ktoś zrobi commit w trakcie pełnego przebiegu.
- Każda pozycja ma w pliku danych przeglądu (zob. *Context*) słowa recenzenta, miejsce, stan na sprawdzonym commicie i decyzję Mariusza.

### To do

1. P16, #104-1 — gdy tabeli *Weights* albo *Costs of an occurrence* rejestru problemów brakuje któregoś poziomu, liczenie audytu dalej zapisuje wynik, wartości zależne od tabeli daje jako `unknown` i kończy się kodem 1, a jego linia `Error:` nazywa brakujący poziom, nie tylko tabelę (`process-audit/audit_count.py`, zdania „the table `Weights` must name the four levels, each once” i „the table `{COSTS_TITLE}` must name the five levels, each once”, ok. l. 1977 i 1983); WAY-344 dostaje wyjątek dla poziomów tych dwóch tabel, a test daje tabelę bez jednego poziomu i sprawdza, że błąd go nazywa.
2. P16, #112 — `agent-instructions/agent_type_copies.py` przy definicji typu agenta bez linii `name:` albo `description:` kończy się kodem 2 z komunikatem, który nazywa plik i brakujące pole; inne jego błędy zostają przy kodzie 1, a opis kodów wyjścia („Exit code: 0 on success; 1 with `Error: <message>` on stderr otherwise”, ok. l. 22) mówi o obu; test daje definicję bez jednego z tych pól i sprawdza kod i nazwę pola.
3. P16, #103-1 — WAY-344 dostaje wąski wyjątek: brak wpisu `repository` pod `the-way` w pliku lokalizacji nie jest brakującym polem, liczenie audytu bierze wtedy checkout, w którym samo leży, jak dziś (`process-audit/audit_count.py`, funkcja `the_way_checkout`, ok. l. 513; opis modułu „where that entry is missing, the checkout this script lies in”, ok. l. 26).
4. G1, #100-3 — `task-cycle/cycle_stages.py` na Windows daje tabelę etapów, a nie wyciąg stosu, gdy sesja orkiestratora Codexa nie ma własnej tury (funkcja `read_codex_session`, linia `since = min((start for start, _ in orchestrator.turns), default=datetime.fromtimestamp(0))`, ok. l. 468).
5. G1, #100-5 — liczenie audytu (`process-audit/audit_count.py`, opis modułu od „The process versions (WAY-339)”, ok. l. 95, i kod grupowania wersji w serie) prowadzi dwa rodzaje serii: serię kosztu dzieli tylko nowy cennik i zmiana skryptu, który koszt mierzy (`task-cycle/cycle_stages.py`); serię liczby uwag dzieli też zmiana formy raportu etapu, listy klas rejestru i instrukcji recenzenta; wynik audytu porównuje koszt wewnątrz serii kosztu, a liczbę uwag wewnątrz serii liczby uwag; WAY-339 dostaje to zdanie w miejscu (WAY-07), z *Verification* i *Rationale*, w którym stoi cena: wzrostu kosztu po zmianie instrukcji recenzenta nie da się oddzielić od wzrostu kosztu procesu.
6. G1, #100-5 i #113-1 — zmiana `task-cycle/agent-types/the-way-stage.md`, którego treść dostaje recenzent jako swoją instrukcję, dzieli serię liczby uwag jak zmiana instrukcji recenzenta (lista podziału w opisie modułu `process-audit/audit_count.py`, akapit „the tree of the-way under `task-cycle/change`, …”, ok. l. 104).
7. G1, pozycja z lektury fundamentu — koszt cyklu w audycie wycenia zapisy do pamięci podręcznej na 5 minut i na godzinę każdy po jego własnej cenie, a nie jako zwykłe wejście; cennik (`process-audit/price_list.md`) dostaje kolumnę *Cache write (1 hour)* z ceną odczytaną przez cykl ze strony cennika Anthropic, nową datę listy i opis użycia kolumn bez zdania „Cache writes (*Cache write (5 minutes)*) are not priced: …”.
8. G1, #106-16 — w cyklu, którego zmiana zmienia narzędzie pomiaru (`task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py` albo `gate/run_tests.py`), liczenie audytu daje pomiary tego narzędzia jako `unknown` z powodem, że cykl zmienił narzędzie, które je zapisało; pozostałe miary cyklu liczy jak dziś, pod wersją, na której biegł.
9. G1, #106-10 — komentarz przy `MEASURES_FILE` w `process-audit/audit_count.py` („A copy holding neither is an earlier form.”, ok. l. 381) mówi to samo co opis modułu („A copy that holds neither is of an earlier cycle or of one whose script failed”, ok. l. 181).
10. G1, #106-13 — lista *Unknown values* wyniku audytu podaje wartości rejestru, których liczenie nie ustaliło, jedną linią na parę pola i powodu, z liczbą takich wartości i kilkoma pierwszymi przykładami; pełna lista zostaje w rejestrze (dziś limit `MAX_LISTED` i linia „more values the register leaves unknown are not listed here”, `process-audit/audit_count.py`, ok. l. 2283).
11. G1, #106-2 i #106-13 — cykl uruchamia `task-cycle/cycle_measures.py` na zapisach sesji prawdziwego cyklu prowadzonego w Codexie i `process-audit/audit_count.py` na prawdziwym rejestrze problemów, a opis prośby podaje, co dały: czy miary sesji Codexa i zagnieżdżonego pomocnika Claude Code są pełne, i ile linii ma *Unknown values* po *To do* 10; miarę złą albo pustą naprawia w tym cyklu. Oba przebiegi piszą tylko do katalogu tymczasowego cyklu: skrypt miar z `--output` tam, a liczenie audytu z `--locations` wskazującym kopię pliku lokalizacji, w której `audit_results` wskazuje ten katalog; ścieżki nie trafiają do zapisu ani opisu prośby (WAY-320).
12. G3, #97-1 — kontrola fundamentu (`elements/common/foundation_check.py`, funkcja `todo_item`, ok. l. 298) wypisuje gołe `TODO` także wtedy, gdy stoi po przecinku albo po złamaniu linii zamiast po ` · `, a przy `TODO` z opisem po przecinku jej błąd mówi, że pozycje pola łączy ` · `, zamiast „is no identifier of a fact”.
13. G3, #120-16 — linia `# decision: WAY-03 "A change whose check lists such an invariant"` w `elements/common/test_foundation_check.py` (ok. l. 1452) cytuje zdanie WAY-03, które test sprawdza, albo znika.
14. G3, #77-4 — test `elements/part-map/test_cross_part_imports.py` nie pada na `compile` dane tekstem pliku innej części, którego nic nie uruchamia; `exec` i `eval` dalej padają (krotka `BUILTINS = ("exec", "eval", "compile", "__import__")`, ok. l. 81, i gałąź „Code given to `exec`, `eval` or `compile`”, ok. l. 406).
15. G3, #86-7 — test pada, gdy plik skilla w `product-guidelines/` albo w `project-level/` wskazuje plik the way, którego nie ma, albo krok czy nagłówek pliku, którego w nim nie ma; ścieżki plików produktu, które skille nazywają, test odróżnia i przepuszcza.
16. G3, #105-1 — `task-cycle/remarks_check.py` czyta pozycje pod etykietą `**Searches not found or unclear:**` także wtedy, gdy etykieta stoi w linii tuż pod punktem listy poprzedniej sekcji (układ szablonu raportu planu, `task-cycle/plan/SKILL.md`, ok. l. 216), a opis skryptu (akapit „a bold label `**Searches not found or unclear**`”, ok. l. 19) nazywa ten przypadek.
17. G3, #83-4 — `task-cycle/private_paths_check.py` wypisuje ścieżkę Windows w formie adresu, `a drive path in address form`; `https://host/C:/x` dalej nie jest wypisywane, jak przypina `task-cycle/test_private_paths_check.py` (ok. l. 66).
18. G3, #95-7 — `task-cycle/tracked_private_paths_check.py` szuka linków do notatek w plikach `.md`, `.markdown`, `.mdx` i `.mdc` (dziś `MARKDOWN_SUFFIX = ".md"`, ok. l. 42), a jego opis i opis polecenia w `installation/README.md` mówią to samo.
19. G3, #95-9 — `installation/README.md` (zdanie „a tracked file is not UTF-8 text”, ok. l. 127) mówi, że plik zaczynający się znacznikiem kolejności bajtów UTF-16 jest czytany.
20. G3, #87-9 — `installation/test_styleguide_installation.py` i `installation/test_testing_guidelines_installation.py` instalują z klonu, jak cztery pozostałe testy instalacji wytycznych, więc commit zrobiony w checkoucie the-way w trakcie pełnego przebiegu ich nie wywraca (linia `self.commit = self.git("rev-parse", "HEAD", cwd=SOURCE)`, ok. l. 37 i 32).

### Questions to settle

- 1. P16 (WAY-344). Przy każdym z trzech przypadków — tabela rejestru bez poziomu (#104-1), generator kopii typów agentów (#112), wpis `repository` w pliku lokalizacji (#103-1): kod do reguły WAY-344 czy wyjątek zapisany w WAY-344?
  - Answer: 1.1 — wynik zostaje, błąd nazywa brakujący poziom, WAY-344 dostaje wyjątek dla poziomów tabel *Weights* i *Costs of an occurrence*; 1.2 — kod do reguły: kod 2 przy brakującym `name:` albo `description:`, inne błędy przy kodzie 1; 1.3 — wąski wyjątek w WAY-344 dla wpisu `repository` pod `the-way`: jego brak znaczy checkout, w którym leży skrypt.
  - Not chosen:
    - 1.1 a) kod 2 z nazwą poziomu i bez wyniku — jedna literówka w poziomie zostawia sesję audytu bez wyniku, dopóki rejestr nie zostanie poprawiony.
    - 1.2 b) wyjątek w WAY-344 dla generatorów dzielących kody wyjścia z `skill_entry_points.py` — lista wyjątków rośnie o przypadek bez innego uzasadnienia niż wygoda, a następny skrypt może go skopiować.
    - 1.3 a) kod 2 — kto nie ma wpisu, rano nie dostaje wyniku audytu, a zamierzony powrót do własnego checkoutu znika.
    - 1.3 c) wyjątek ogólny dla pola, którego brak opis skryptu dopuszcza z wartością domyślną — furtka, przez którą następny autor może uznać dowolne pole za opcjonalne.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1.1 b, 1.2 a, 1.3 b — za rekomendacjami (1.1: ten sam powód co istniejący wyjątek liczenia audytu; 1.2: kilka linii, bez rosnącej listy wyjątków; 1.3: wąski wyjątek zamiast furtki)”.
- 2. G1, #100-5. Reguła serii kosztu: zostaje ostrożna (dzieli przy każdej zmianie plików metod etapów) czy dzieli tylko przy zmianie, która rusza formę raportu etapu, listę klas albo instrukcje recenzenta — i jak to rozpoznać?
  - Answer: c — zmiana WAY-339: serię kosztu dzieli tylko nowy cennik i zmiana skryptu mierzącego koszt; instrukcje recenzenta, lista klas i forma raportu dzielą tylko serię liczby uwag; *Rationale* nazywa cenę: nie da się oddzielić „recenzent znalazł więcej” od „proces zdrożał”.
  - Not chosen:
    - a) reguła bez zmian, tylko `the-way-stage.md` dopisany do listy podziału — audyt dalej odpowiada `unknown` przy większości wersji.
    - b) zawężenie skryptu do WAY-339 przez wyjęcie form raportów etapów do osobnych plików — odpada najwyżej 14 z 34 podziałów w 134 scaleniach, za przebudowę czterech plików metod.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „2 c — zmiana WAY-339: serię kosztu dzieli tylko nowy cennik i zmiana skryptu mierzącego koszt; instrukcje recenzenta, lista klas i forma raportu dzielą tylko serię liczby uwag. Powód: tylko to sprawia, że audyt odpowiada na pytanie o koszt; ten sam argument WAY-339 już stosuje do kontekstu i czasów bramki. W Rationale nazwij cenę (nie da się oddzielić „recenzent znalazł więcej” od „proces zdrożał”).” Liczby podziałów: scalenia pierwszego rodzica gałęzi `foundations` do `21ecb62`, pliki listy podziału z `process-audit/audit_count.py` i `task-cycle/agent-types/the-way-stage.md`.
- 3. G1, pozycja z lektury fundamentu. Kolumna zapisu na godzinę w cenniku i rozdzielenie zapisów w skrypcie etapów czy zdanie w cenniku, że godzinnych zapisów audyt nie wycenia?
  - Answer: a — wycenić zapisy dokładnie: zapisy na 5 minut i na godzinę rozdzielone, kolumna zapisu na godzinę w cenniku, liczenie wycenia oba; cenę zapisu na godzinę cykl czyta ze strony cennika Anthropic, nie z pamięci.
  - Not chosen:
    - b) zdanie w cenniku, że zapisów na godzinę audyt nie wycenia osobno — tekst przestaje udawać, ale liczba zostaje zła.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „3 a — wycenić zapisy dokładnie; przerwa w serii kosztu i tak przychodzi z tym zadaniem. Cenę zapisu na godzinę cykl czyta ze strony cennika Anthropic, nie z pamięci.”
- 4. G1, #106-16. Pod którą wersją procesu liczyć miary cyklu, który sam zmienia narzędzie pomiaru?
  - Answer: b — pomiary narzędzia, które cykl sam zmienia, dają `unknown` z powodem; reszta miar cyklu jak dziś.
  - Not chosen:
    - a) pomiary tego narzędzia w nowej serii, reszta pod wersją, na której cykl biegł — jeden cykl w dwóch wersjach, grupowanie i testy liczenia się komplikują.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „4 b — pomiar narzędzia, które cykl sam zmienia, daje unknown z powodem; prosto i uczciwie.”
- 5. G1, #106-13. Co czytający audyt ma zobaczyć w *Unknown values* zamiast kilkuset linii niewiadomych rejestru?
  - Answer: a — jedna linia na parę „pole i powód”, z liczbą wartości i kilkoma przykładami; pełna lista zostaje w rejestrze.
  - Not chosen:
    - b) niższy limit, np. 50 linii, z dopiskiem „N more” — pierwsze 50 linii w przypadkowym porządku, częsty powód zasłania rzadki, nie widać, ile jakich.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „5 a — jedna linia na parę „pole i powód”, z liczbą i kilkoma przykładami; to jest ucięcie zalewu, o które prosił, bez gubienia powodów.”
- 6. G1, #106-2 i #106-13. Czy cykl ma uruchomić skrypt miar na prawdziwej sesji Codexa i liczenie audytu na prawdziwym rejestrze?
  - Answer: tak — cykl uruchamia oba na prawdziwych danych, pisząc tylko do swojego katalogu tymczasowego (skrypt miar przez `--output`, liczenie audytu przez kopię pliku lokalizacji podaną w `--locations`), i podaje wynik w opisie prośby; złą albo pustą miarę naprawia w tym cyklu.
  - Not chosen:
    - zostawić obie uwagi poza zadaniem — zostają nierozstrzygnięte, a cykl na Codexie może dawać w audycie złe albo puste miary, o których nikt nie wie.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „przy pytaniu 6 i kolejnych idź za rekomendacją, gdy nie zmienia zatwierdzonej decyzji ani niczego na komputerze Mariusza — wtedy pytaj”; rekomendacja: uruchomić, bo przebiegi tylko czytają, a wynik idzie do katalogu tymczasowego. Na dysku są zapisy sesji Codexa, które nazywają the way i `implement-task` (78 plików pod `~/.codex/sessions/2026`, stan 2026-11-15).
- 7. G3, #86-7. Które skille obejmuje test martwych wskazań na pliki i kroki?
  - Answer: skille w `product-guidelines/` i `project-level/` — części, których dotyczyły uwagi #86-7, #87-5, #89-10 i #90-3.
  - Not chosen:
    - wszystkie skille the way — więcej ścieżek produktu do odróżnienia i więcej fałszywych trafień, bez uwagi, która by tego wymagała.
    - zostawić uwagę — prozę czyta recenzja, ale martwe wskazanie wychodzi dopiero w sesji, która za nim pójdzie.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15 (jak przy pytaniu 6: za rekomendacją).
- 8. G3, #95-7. Co jest „plikiem Markdown” w zdaniu WAY-320 i niezmiennika `tracked-file-private-paths`: tylko `.md` czy też `.markdown`, `.mdx` i `.mdc`?
  - Answer: plik `.md`, `.markdown`, `.mdx` albo `.mdc` (reguły Cursora to Markdown z nagłówkiem); zdanie WAY-320 i niezmiennika zostaje bez zmian.
  - Not chosen:
    - tylko `.md` — publiczny produkt z regułami Cursora może opublikować w nich link do prywatnej notatki, a jego test przejdzie.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15 (jak przy pytaniu 6: za rekomendacją). Ani the way, ani loop2 nie śledzą dziś takich plików (plik danych przeglądu, G3, #95-7), więc nowe czytanie nie wywraca dziś testu żadnego produktu.
- 9. Kolejność cyklu tego zadania i zadania „the way: drobne poprawki po PR-ach #117–#121”, które zmienia ten sam plik `elements/common/foundation_check.py` i to samo zdanie WAY-344.
  - Answer: bez zależności; cykl, który scala się drugi, odświeża gałąź i godzi oba zdania WAY-344 i obie zmiany `foundation_check.py`.
  - Not chosen:
    - jedno zadanie czeka na drugie — dzień albo więcej przestoju za konflikt w kilku liniach jednego zdania i jednej funkcji.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15 (jak przy pytaniu 6: za rekomendacją).

## Context

- Plik danych przeglądu: `a rule or note file of the author's, outside the repository` — sekcja „Fundament” → „Propozycje”, P16, i „Grupy uwag”, G1 i G3.
- Sprawdzony commit przeglądu: `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (gałąź `foundations`); numery linii w pliku danych odnoszą się do niego, ale część z nich odbiega o kilka linii od pliku — miejsce wyznacza cytat.
- Przypadek #120-2 (kontrola fundamentu pomija niezmiennik, któremu w bazie brakowało pola) niesie zadanie „the way: drobne poprawki po PR-ach #117–#121” (*To do* 8–9, wybór „4 a”: linia `listed:` i zdanie w WAY-344); to zadanie zmienia też `elements/common/foundation_check.py`.
- `task-cycle/cycle_measures.py` zmienia też zadanie „the way: jak agent czyta dziennik decyzji” (*To do* 8), którego cykl ruszył 2026-11-14.
- Funkcję `read_contradiction` w `process-audit/audit_count.py` przepisuje zadanie „the way: audyt procesu ma odpowiadać, czy sprzeczność … wyszła dopiero po napisaniu kodu” — uwaga #100-6 jest notatką do tamtego zadania, nie tutaj.
- *Defect introduced by*: #10 — `default=datetime.fromtimestamp(0)` (#100-3); #25 i #42 — testy instalatora czytające żywy `HEAD` (#87-9); #77 — `compile` w teście importów (#77-4); #83 — wyłączenie litery dysku po ukośniku (#83-4); #95 — `MARKDOWN_SUFFIX = ".md"` (#95-7) i zdanie README (#95-9); #97 — `todo_item` (#97-1); #104 — tabela *Costs of an occurrence* odrzucana z błędem tabeli, gdy WAY-344 już stała (#104-1); #105 — `opens_paragraph` (#105-1); #112 — kod 1 nowego generatora wbrew WAY-344 (#112); #120 — linia `decision:` (#120-16).
- Bez defektu: #103-1 (WAY-344 wiąże powrót do checkoutu dopiero przy przeróbce tego czytania), #100-5, #106-16, #106-2, #106-13, #106-10, cennik i #86-7 — reguły napisane świadomie, niesprawdzone przypadki albo brakujący test; tabela *Weights* przyszła z #100, scalonej przed #103, która wprowadziła WAY-344.
- Zapisy sesji Claude Code podają zapis do pamięci podręcznej rozdzielony na 5 minut i godzinę (`ephemeral_5m_input_tokens`, `ephemeral_1h_input_tokens`); `task-cycle/cycle_stages.py` sumuje dziś `cache_creation_input_tokens` do *Input* (ok. l. 576).
- WAY-339 mówi, że tokeny zapisane do pamięci podręcznej jako miara użycia pamięci „are never columns of the stage report” i liczy je osobny skrypt (`task-cycle/cycle_measures.py`); którędy liczenie audytu dostaje zapisy rozdzielone po modelu i czasie życia do wyceny w *To do* 7, wybiera cykl.
- Cennik audytu (`process-audit/price_list.md`) ma kolumnę *Cache write (5 minutes)* i zdanie „Cache writes (*Cache write (5 minutes)*) are not priced: `task-cycle/cycle_stages.py` folds them into *Input*, so they are priced there as input, an approximation”.
- Lista *Unknown values* ma dziś limit 500 wartości rejestru i linię „more values the register leaves unknown are not listed here” (`process-audit/audit_count.py`, `MAX_LISTED`, ok. l. 2283); na szablonie rejestru wynik ma po #106 ok. 830 linii.
- WAY-343 (na której wersji the-way biegł cykl samej the-way) jest wycofana; jej reguła stoi w opisie modułu `process-audit/audit_count.py` (pozycja *Process pin*, ok. l. 49–54).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-03 — Who may change an invariant test, and when?: „A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request, so that the agent reviewing the change and the human merging it see it.” Dotyczy *To do* 13 (linia `decision:`) i 14 (test niezmiennika `cross-part-imports`).
- WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?: „the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports […] that the record's process remarks do not hold word for word”. Dotyczy *To do* 16.
- WAY-309 — How does the cycle find the private paths and notes in what it publishes?: „the orchestrator runs the-way's script that lists, with the file and the line of each, every absolute path (a drive letter, a home directory) and every note link written `[[...]]` […] no letter for the start of a drive when a backslash stands before it.” Dotyczy *To do* 17.
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name?: „No file the repository tracks holds an absolute path, or a note link in a Markdown file, other than the files that the invariant `tracked-file-private-paths` names”. Dotyczy *To do* 18.
- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?: „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under the shared reading of product guidelines: in each part named in *Scope*, neither is missing”. Zadanie nie czeka na wytyczne.
- WAY-337 — How is the cost of a cycle measured?: „its cost at constant prices, computed from a price list of models that carries a date”. Dotyczy *To do* 7.
- WAY-339 — When do the measures of the audit stop being comparable?: „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures, except for the measures of how a cycle's agents use context and the prompt cache and the times of the gate: a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process”. Dotyczy *To do* 5–8. Zadanie zmienia decyzję w miejscu (WAY-07), jak wybrano w pytaniu 2: serię kosztu zaczyna tylko nowy cennik i zmiana skryptu, który koszt mierzy; zmiana formy raportu etapu, listy klas i instrukcji recenzenta zaczyna tylko nową serię liczby uwag; *Rejected* dostaje warianty a i b pytania 2.
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?: „where a field is missing or stands under another name the script ends with an error that names it […] a missing field ends the script with exit code 2 and a message that names the file and the field, except that a script whose purpose is to check the form of a file reports a missing field whose presence it checks as a finding of its list, with exit code 1, and except that the command that counts the audit, in a file of a cycle's record that it reads from git history, gives the values that need a missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field”. Dotyczy *To do* 1–3. Zadanie zmienia decyzję w miejscu (WAY-07), jak wybrano w pytaniu 1: dwa nowe wyjątki — tabela *Weights* albo *Costs of an occurrence* rejestru bez któregoś poziomu daje zapisany wynik, `unknown` przy wartościach zależnych od tabeli, kod 1 i linię `Error:` z nazwą poziomu; brak wpisu `repository` pod `the-way` w pliku lokalizacji nie jest brakującym polem, a liczenie bierze wtedy checkout, w którym leży — z *Verification* i *Rationale* do nich.
- WAY-368 — Which agents run the stages of a task cycle in Claude Code?: „only the type of the one author has the prompt cache lifetime that WAY-255 gives that agent.” Dotyczy *To do* 7.

## Settlements to record

Candidates: 13 shown, 8 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy tabeli *Weights* albo *Costs of an occurrence* rejestru brakuje poziomu, wynik zostaje zapisany, a błąd nazywa brakujący poziom. | sentence of WAY-344 | pytanie 1 (1.1, jego *Not chosen*) | kod 2 bez wyniku, jak przy brakującym nagłówku rejestru |
| 2 | Brak wpisu `repository` pod `the-way` w pliku lokalizacji nie jest brakującym polem: liczenie bierze checkout, w którym leży. | sentence of WAY-344 | pytanie 1 (1.3, jego *Not chosen*) | kod 2 przy następnej przeróbce czytania pliku lokalizacji albo wyjątek ogólny dla pól z wartością domyślną |
| 3 | Serię kosztu dzieli tylko nowy cennik i zmiana skryptu mierzącego koszt; instrukcje recenzenta, lista klas i forma raportu dzielą tylko serię liczby uwag; nie da się oddzielić „recenzent znalazł więcej” od „proces zdrożał”. | sentence of WAY-339 | pytanie 2 (jego *Not chosen*) | jedna seria dla kosztu i uwag, dzielona przy każdej zmianie instrukcji recenzenta |
| 4 | Pomiar narzędzia, które cykl sam zmienia, daje `unknown` z powodem. | sentence of WAY-339 | pytanie 4 (jego *Not chosen*) | liczenie takiego pomiaru w nowej serii albo w starej, jak dziś |
| 5 | Zapisy do pamięci podręcznej na 5 minut i na godzinę są wyceniane każdy po swojej cenie, a cennik ma kolumnę zapisu na godzinę. | data or code: `process-audit/price_list.md` i liczenie kosztu w `process-audit/audit_count.py` | pytanie 3 (jego *Not chosen*) | dopisanie do cennika tylko zdania o przybliżeniu |
| 6 | *Unknown values* podaje niewiadome rejestru jedną linią na parę „pole i powód”, z liczbą i kilkoma przykładami. | data or code: opis wyniku i kod *Unknown values* w `process-audit/audit_count.py` | pytanie 5 (jego *Not chosen*) | niższy limit linii z dopiskiem „N more” |
| 7 | Test martwych wskazań obejmuje skille w `product-guidelines/` i `project-level/`. | data or code: test martwych wskazań (*To do* 15) | pytanie 7 (jego *Not chosen*) | test wszystkich skilli the way |
| 8 | Plik Markdown to plik `.md`, `.markdown`, `.mdx` albo `.mdc`. | glossary term | pytanie 8 (jego *Not chosen*) | tylko `.md`, jak dziś w `tracked_private_paths_check.py` |

## Out of scope

- Uwaga #100-6 (fałszywe „tak” przy zaprzeczeniach w *Discarded attempt*) — notatka do zadania o sprzeczności po kodzie.
- Uwaga #120-2 (niezmiennik bez pola w bazie) — niesie ją zadanie „the way: drobne poprawki po PR-ach #117–#121”.
