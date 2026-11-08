---
title: "the way: artefakty testów"
status: draft
created: 2026-10-31T18:40
updated: 2026-11-08
tags: [zadanie]
related: "the project note in the author's notes"
---

## Po co to

- **Jak jest dziś:** szablon opisu PR-a każe pokazać ekran „with screenshots”, a skill `loop2-play` każe nie zostawiać w repozytorium żadnego zrzutu. Agenci rozstrzygają to po swojemu: z sześciu PR-ów loop2 ze zmianą ekranu (#62–#67) trzy osadzają obrazki, które trafiają przez to na stałe do historii repo, a trzy nie pokazują żadnego.
- **Kto to odczuwa:** Ty przy akceptacji, bo czy zobaczysz ekran, zależy od tego, którą instrukcję agent posłuchał. Agenci też: zostawiona otwarta przeglądarka blokuje następnego. W Claude Code, w sesjach loop2 i the-way, to 13 błędów zajętego profilu w 9 plikach rozmów z 20–31.10.
- **Co jeśli nic:** zrzuty dalej albo przepadają, albo puchną w historii produktu (w loop2 od 1.10 to ok. 29 MB z ok. 51 MB całej historii), a każdy nowy produkt zaczyna od zera.

# the way: artefakty sprawdzenia zmiany docierają do opisu PR-a spoza historii repo produktu

Status: ready for cycle
Project relation: independent

## Description

### Need

- Przy zmianie ekranu autor ogląda zrzut działającego produktu (WAY-219), a szablon opisu PR-a każe pokazać człowiekowi, co zobaczy jego użytkownik, „with screenshots” (`task-cycle/skill/request_template.md:153-154`).
- Nic w the-way nie mówi, gdzie te zrzuty leżą i jak trafiają do opisu PR-a.
- W loop2 (`origin/main` @ 72287c2) skill produktu mówi: „Nothing of it stays in the repository: no Playwright test, no frame, no snapshot. Its evidence goes into the report or the request.” (`.claude/skills/loop2-play/SKILL.md:12`).
- Skutek w loop2: PR-y #63, #66 i #67 osadzają obrazki linkiem do pliku w zapisie cyklu w konkretnym commicie, więc obrazki zostają na stałe w historii repo produktu; PR-y #62, #64 i #65 piszą, że zrzuty zrobiono, ale ich nie dołączono.
- Odbiorcą jest Mariusz przy akceptacji PR-a: ma widzieć ekran w opisie PR-a, bez uruchamiania produktu.

### To do

1. Przy zmianie ekranu zrzuty, które autor albo recenzent pokazuje człowiekowi, są osadzone w opisie PR-a jako obrazki (pytanie 1).
2. Żaden plik zrzutu nie trafia do historii repozytorium produktu, także w kopii zapisu cyklu dodawanej commitem przy PR-ze (pytanie 1).
3. Miejsce, w którym leżą zrzuty, ustala fundament produktu; the-way nie wskazuje konkretnego miejsca (pytanie 1).
4. Gdy fundament produktu nie ustala miejsca na zrzuty, agent nie pokazuje zrzutu w PR-ze, a opis PR-a podaje człowiekowi do decyzji, że zrzutu nie ma i dlaczego; cykl się nie zatrzymuje (pytanie 4).
5. Z artefaktów sprawdzenia do opisu PR-a trafiają tylko zrzuty ekranu; ślady tekstowe zostają w raportach zapisu cyklu (pytanie 5).
6. Droga agenta do działającego produktu, którą ustala fundament produktu, pozwala dwóm cyklom w osobnych worktree sprawdzać naraz bez wspólnej przeglądarki, a agent zamyka przeglądarkę, którą otworzył (pytanie 6).
7. Krok technologii przy definiowaniu projektu (WAY-121) ustala miejsce na zrzuty jako czwartą sprawę drogi agenta do działającego produktu, obok logów, interfejsu i danych (pytanie 4).
8. Przed każdym commitem, który dodaje kopię zapisu cyklu, skrypt the-way sprawdza, że kopia nie zawiera żadnego pliku obrazu, tak jak dziś sprawdza ją pod kątem ścieżek prywatnych (*Settlements to record*, wiersz 7).

### Questions to settle

1. Gdzie leżą zrzuty ze sprawdzenia zmiany i jak trafiają do Mariusza?
   - Answer: poza repozytorium produktu, w miejscu, które ustala produkt; opis PR-a osadza je jako obrazki. the-way ustala regułę, produkt — miejsce.
   - Not chosen:
     - zrzuty w zapisie cyklu w repo produktu, osadzane linkiem do commita (jak w #67) — Mariusz: „nie no nie możemy tych plików zapisywać kurcze w repozytorium...”
     - nic nie zostaje, agent opisuje ekran słowami (jak w #64, #65) — przy akceptacji nadal nie widać ekranu, czyli zostaje problem, od którego wyszło zadanie
     - załączniki wydania GitHuba w repo produktu — w prywatnym repo obrazek może się nie wyświetlić (niesprawdzone), bałagan na liście wydań
     - zewnętrzny magazyn plików, np. Cloudflare R2 — nowe narzędzie, klucze i ręczna akcja człowieka, wybór technologii do osobnego ustalenia
     - zrzuty tylko na dysku człowieka, w ignorowanym `.runs/` — opis PR-a nie może linkować do pliku lokalnego
   - Source: Mariusz, 2026-11-08: „nie no nie możemy tych plików zapisywać kurcze w repozytorium... tylko nie wiem gdzie w takim razie to robić”; propozycja podziału „reguła w the-way, miejsce w produkcie” przyjęta tego samego dnia.
2. Czy zrzuty są trwałym dowodem, czy dowodem na czas akceptacji?
   - Answer: dowodem na czas akceptacji; miejsce na zrzuty wolno po dłuższym czasie wyczyścić, a obrazki w starych PR-ach przestaną się wtedy wyświetlać.
   - Not chosen:
     - miejsca na zrzuty się nie czyści, a gdy urośnie, temat wraca — Mariusz: „jeśli za pół roku coś w wyglądzie się będzie psuło to po jakiego grzyba mam sięgać do widoków sprzed pół roku?”
   - Source: Mariusz, 2026-11-08: „kiedyś jak bedę chciał usunąć stare obrazki, to się je usunie po prostu i przestaną się wyświetlać w PR'ach do których już nikt nie będzie miał potrzeby wracać”; „no zakładam, że jak będę to chciał zrobić, to zrobię to po dłuższym czasie”.
3. Gdzie leżą zrzuty loop2?
   - Answer: w osobnym publicznym repozytorium na dowody, z katalogiem na każdy cykl; opis PR-a osadza obrazek linkiem do pliku w commicie tego repo, jak w #67.
   - Not chosen:
     - osobne prywatne repo — obrazek w publicznym PR-ze loop2 widziałby tylko Mariusz, innym czytelnikom pokazałby się jako zepsuta ikonka, a mechanizm wymagał próby; prywatność niczego nie chroni, bo loop2 i jego PR-y są publiczne
   - Source: Mariusz, 2026-11-08: „osobne repo dla loop2 chyba byłoby spoko”, „widzę obrazki” (o PR #67), „niech będzie publiczne”.
4. Co dzieje się przy zmianie ekranu, gdy fundament produktu nie ustala miejsca na zrzuty?
   - Answer: agent ogląda zrzut sam, nie pokazuje go w PR-ze, a w części opisu PR-a z decyzjami człowieka podaje, że zrzutu nie ma, bo produkt nie ustalił miejsca; cykl się nie zatrzymuje. Do tego krok technologii (WAY-121) przy projekcie z zachowaniem widocznym w działającym produkcie ustala miejsce na zrzuty jako czwartą sprawę drogi agenta do działającego produktu, obok logów, interfejsu i danych.
   - Not chosen:
     - tylko zachowanie przy braku miejsca, bez zmiany kroku technologii — produkt dowiaduje się o braku miejsca dopiero przy pierwszym PR-ze ze zmianą ekranu
     - brak miejsca zatrzymuje cykl — blokada pojawia się po zrobieniu zmiany; to samo odrzuciło WAY-219 dla drogi do produktu
   - Source: Mariusz, 2026-11-08: „B” (na pytanie o drogi A, B, C).
5. Czy poza zrzutami powstają inne artefakty sprawdzenia — klatki ruchu, logi, wyniki sprawdzeń ręcznych — i czy obowiązuje je ta sama reguła?
   - Answer: do opisu PR-a trafiają tylko zrzuty ekranu; ruch agent opisuje słowami, a płynność sprawdza człowiek. Ślady tekstowe — logi, wyniki poleceń, obserwacje — zostają w raportach zapisu cyklu, jak dziś.
   - Not chosen:
     - przy zmianie ruchu także krótkie nagranie z klatek w opisie PR-a — plik kilka MB, narzędzie do składania klatek do ustalenia, a nagranie z kilku klatek na sekundę może pokazać płynność, której gra nie ma
   - Source: Mariusz, 2026-11-08: „A” (na pytanie „czy do opisu PR-a mają trafiać tylko zrzuty ekranu, czy przy zmianach ruchu chcesz też nagranie?”).
6. Jak dwa cykle biegnące naraz dzielą przeglądarkę?
   - Answer: the-way stawia warunek drodze agenta do działającego produktu, którą ustala fundament produktu: dwa cykle w osobnych worktree sprawdzają naraz bez wspólnej przeglądarki, a agent zamyka przeglądarkę, którą otworzył.
   - Not chosen:
     - the-way nic nie mówi, sprawa zostaje przy produkcie — każdy produkt odkrywa konflikt sam, po błędach; produkt z Playwright MCP jako główną drogą wraca do zajętego profilu
   - Source: Mariusz, 2026-11-08: „B” (na pytanie „czy the-way ma stawiać ten warunek drodze do działającego produktu (B), czy zostawiamy to produktom (A)?”).
7. Co z dwoma zadaniami, które czekały na tę rozmowę: „Dać agentom the way metodę testowania w działającym produkcie” i „Pokazać na przykładzie loop2, jak przygotować instrukcję wdrażania kolejnego produktu” — przepisać, włączyć tu czy zamknąć?
   - Answer: oba zostają osobnymi zadaniami i przestają czekać. „Metoda testowania w działającym produkcie” zachowuje zakres i niski priorytet; jej opis dostaje zdanie, że to, co zostaje po sprawdzeniu i gdzie leży, ustala to zadanie. „Instrukcja wdrażania na przykładzie loop2” zachowuje zakres bez zmian — zależność dotyczyła drogi agenta do działającego produktu, którą loop2 zapisało w skillu `loop2-play`.
   - Not chosen:
     - zostawić oba z oznaczeniem „czeka” — wiszą, choć nie mają już na co czekać
   - Source: Mariusz, 2026-11-08: „akceptuję” (tabela trzech decyzji o spisie zadań, wiersze 2 i 3).
8. Czy zmiana w loop2 (decyzja o repo na dowody, poprawka zdania w `loop2-play`) idzie osobnym zadaniem loop2?
   - Answer: tak — osobne zadanie loop2, które czeka na scalenie tego zadania: publiczne repo na dowody, decyzja w fundamencie loop2, zdanie „nothing stays in the repository” w `loop2-play` zamienione na wskazanie repo na dowody, a przy drodze zapasowej przez Playwright MCP dopisek, że wolno z niej korzystać tylko z sesji wystartowanej w worktree cyklu. Założenie repo na GitHubie robi Mariusz.
   - Not chosen:
     - nic nie zakładać — reguła the-way wejdzie, a loop2 nie będzie miało miejsca na zrzuty, więc jego PR-y będą pisać, że zrzutu nie ma
   - Source: Mariusz, 2026-11-08: „akceptuję” (tabela trzech decyzji o spisie zadań, wiersz 1).
9. Czy zadanie czeka na własne wytyczne kodowania i testów the-way, skoro cykl zmienia skrypt i jego testy (punkt 8 z „To do”) w repozytorium bez `guidelines/`?
   - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the-way, a brak własnych wytycznych zostaje w osobnym zadaniu o wytycznych the-way. Słaby punkt przyjęty z tą drogą: warunek w skrypcie i jego test powstają bez wytycznych kodowania i testów, jak dotychczasowe skrypty the-way.
   - Not chosen:
     - czekać na zadanie o wytycznych — tamto zadanie nie ma jeszcze wybranego kierunku, a do jego scalenia zrzuty dalej trafiałyby do historii produktu albo przepadały
   - Source: Mariusz, 2026-11-08: „nie czeka”; ta sama odpowiedź w zadaniu „cykl zadania nie publikuje prywatnych nazw”, pytanie 4.

## Context

- Źródło zadania: sprawa AIR-555 z przeglądu warstwy AI, 2026-10-31, rozszerzona uwagą Mariusza o wytycznych testowania i artefaktach.
- Stan, na którym zadanie stoi: the-way `foundations` @ 57795e4, loop2 `origin/main` @ 72287c2.
- Zadanie o stałym schemacie opisu PR-a jest zamknięte (the-way PR #71, 2026-11-05); wyznaczyło miejsce zrzutów w górnej części opisu.
- loop2 ma już drogę agenta do działającej gry: lokalny start jednym poleceniem, Playwright CLI i stan gry budowany funkcjami symulacji (decyzje loop2 D-254, D-255; skill `loop2-play`).
- loop2 i the-way są publiczne (`gh repo view`, 2026-11-08).
- Link do pliku w konkretnym commicie z dopiskiem `?raw=true` wyświetla się w opisie PR-a jako obrazek (loop2 PR #67, potwierdzone przez Mariusza 2026-11-08).
- Usunięcie pliku kolejnym commitem nie zmienia obrazka osadzonego linkiem do starego commita; żeby obrazki zniknęły, trzeba skasować albo przepisać historię repo z dowodami.
- W historii loop2 384 pliki PNG zajmują ok. 29 MB z ok. 51 MB całego repo (pomiar `git rev-list --objects --all` i `git count-objects`, 2026-11-08); git nie ściska zrzutów różnicowo, a usunięcie pliku nie zwalnia miejsca.
- Limity GitHuba: plik powyżej 100 MiB jest blokowany, repo „ideally less than 1 GB, and less than 5 GB is strongly recommended” (docs.github.com, „About large files on GitHub”, czytane 2026-11-08).
- Playwright CLI 0.1.22 trzyma profil przeglądarki w pamięci, a sesję domyślną rozdziela według repozytorium: w dwóch worktree tego samego repo każdy ma własną przeglądarkę, a w dwóch katalogach poza gitem drugie `open` przejmuje przeglądarkę pierwszego bez komunikatu (próba w katalogach tymczasowych, 2026-11-08).
- 13 błędów zajętego profilu z 20–31.10 pochodzi z sesji sprzed przejścia loop2 na Playwright CLI (D-254, 2026-11-02).
- Playwright MCP trzyma trwały profil przeglądarki dla katalogu, z którego wystartowała sesja agenta, więc dwie sesje z tego samego katalogu się blokują (sprawa AIR-454, zadanie „Dwie sesje z przeglądarką w tym samym katalogu bez zamykania jednej” w notatkach autora o Claude Code); to zadanie dotyczy konfiguracji narzędzia na komputerze autora i zostaje osobne.
- Zamykanie przeglądarki po sprawdzeniu opisuje dziś tylko skill `loop2-play` („End the check”: `playwright-cli close`); zdania o zamykaniu przeglądarki nie ma w żadnym commicie the-way.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-219 — What does an author check before a user-interface change reaches review?: „Before review, the author of a one-author change and the executor of a slice changing a user interface check the affected components' states required by the product's applicable styleguide, beside the check of WAY-164, and inspect a screenshot through the agent's way to the running product that its foundation settles. Where the foundation settles no such way, they inspect the states in code and mark the screenshot unchecked for that reason in their report and the request; a settled way that fails keeps its actual failed or unperformed check rather than that reason. The report records what was checked, how, what was observed and the screenshot evidence where obtained, without treating a code inspection as evidence of rendered appearance.”
- WAY-286 — What form does the description of a request a task cycle opens take?: „…first a top part written for the human in plain words, with no file names and no identifiers of entries, that gives the request's state in its first sentence, then what the human will see once the change is in — the whole change, what the task announced included — …”
- WAY-308 — How does a task cycle keep the paths and the notes of its human out of what it publishes?: „A task cycle commits its record and publishes the description of its request only cleaned, in every repository, public or private …” — kopia zapisu cyklu jest commitowana do repo produktu, więc punkt 2 z „To do” dotyczy jej wprost.
- WAY-121 — Where does a project settle the technology it needs?: „… the step looks at three matters of an agent's way to the running product — its logs, its interface and its development data — and lists as a choice of its own each matter that no decision of the foundation settles for that behaviour …” — zadanie dokłada czwartą sprawę: miejsce na zrzuty (pytanie 4).

## Settlements to record

Candidates: 10 shown, 7 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zrzuty ze sprawdzenia zmiany ekranu trafiają do opisu PR-a jako obrazki i nigdy do historii repozytorium produktu, także w kopii zapisu cyklu; miejsce, w którym leżą, ustala fundament produktu. | decision | pytanie 1; pytanie przeciw odpowiedzi, Mariusz 2026-11-08: „wiersz 1 zostaje z «nigdy»”. Not chosen: próg rozmiaru zamiast „nigdy” — trzeba ustalić liczbę, skrypt musiałby mierzyć pliki, a historia i tak rośnie, tylko wolniej | czy zrzuty kłaść w `reports/` zapisu cyklu i osadzać linkiem do commita, jak w loop2 #67, czy ich nie dołączać, jak w #64 |
| 2 | Zrzuty są dowodem na czas akceptacji; produkt może po dłuższym czasie wyczyścić miejsce na nie, a stare PR-y tracą wtedy obrazki. | decision | pytanie 2 | czy wymagać od produktu miejsca trwałego, które nie może być czyszczone, skoro zapis cyklu zostaje w historii na zawsze |
| 3 | Gdy fundament produktu nie ustala miejsca na zrzuty, agent nie pokazuje zrzutu, opis PR-a podaje człowiekowi do decyzji, że zrzutu nie ma i dlaczego, a cykl się nie zatrzymuje. | decision | pytanie 4 | czy zatrzymać cykl, wrzucić zrzut do zapisu cyklu mimo reguły, czy tylko wspomnieć o braku w *Checks* |
| 4 | Krok technologii przy projekcie z zachowaniem widocznym w działającym produkcie ustala miejsce na zrzuty jako czwartą sprawę drogi agenta do działającego produktu, obok logów, interfejsu i danych. | decision | pytanie 4 | czy zmieniać WAY-121, czy zostawić miejsce na zrzuty do ustalenia przy pierwszym PR-ze; koliduje z dzisiejszym brzmieniem WAY-121 („three matters”), które ta zmiana poprawia |
| 5 | Do opisu PR-a trafiają z artefaktów sprawdzenia tylko zrzuty ekranu; ruch agent opisuje słowami, a ślady tekstowe zostają w raportach zapisu cyklu. | decision | pytanie 5 | czy dołączać nagrania ruchu złożone z klatek albo logi do opisu PR-a |
| 6 | Droga agenta do działającego produktu, którą ustala fundament produktu, pozwala dwóm cyklom w osobnych worktree sprawdzać naraz bez wspólnej przeglądarki, a agent zamyka przeglądarkę, którą otworzył. | decision | pytanie 6 | czy dopisać tylko zdanie o zamykaniu przeglądarki w `task-cycle/change/ui_check.md`, czy stawiać warunek samej drodze |
| 7 | Kopia zapisu cyklu dodawana commitem do repozytorium produktu nie zawiera żadnego pliku obrazu; sprawdza to skrypt, jak ścieżki prywatne. | invariant | propozycja z materiału, przyjęta: Mariusz 2026-11-08, „tak, przyjmuję 1–7” | czy pilnować reguły z wiersza 1 skryptem i testem, czy tylko zdaniem w skillu i przeglądem |

## Out of scope

- Ustalenie miejsca na zrzuty w loop2 i poprawka skilla `loop2-play` — zmiana w repo loop2 (pytanie 8).
