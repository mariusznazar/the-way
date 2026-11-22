---
title: "the way: poprawki przyczyn powtarzających się uwag agentów z zapisów cykli — przegląd 22.11, 15 spraw"
status: draft
created: 2026-11-22T11:55
updated: 2026-11-22
tags: [zadanie]
related: "a link to the project's note in the author's notes"
---

# the way: poprawki przyczyn powtarzających się uwag agentów z zapisów cykli — przegląd 22.11, 15 spraw

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/137

## Description

### Need

- Agenci, którzy prowadzą cykle zadań w the-way i loop2, zapisują po każdym cyklu, gdzie metoda the-way im nie pasowała; przegląd tych zapisów z 21–22.11 (77 cykli) dał 15 powtarzających się kłopotów.
- Kłopoty mają trzy wspólne przyczyny: reguła stoi w pliku, którego agent nie czyta w chwili działania; skrypt the-way żąda czegoś innego, niż mówi jego opis, albo zgłasza fałszywe alarmy; instrukcja milczy w sytuacji, która wraca — i agenci obchodzą to każdy po swojemu.
- Odczuwają to prowadzący, wykonawcy i recenzenci cykli: kilka zmarnowanych kroków w prawie każdym cyklu (najczęstszy kłopot trafił się w 23 cyklach).
- Odczuwa to Mariusz, gdy obejście zawiedzie: cykl loop2 stał ok. dwóch godzin na zawieszonym teście, zgubione pierwszeństwo jednej decyzji przed drugą wyszło dopiero po scaleniu, a brakujące komentarze przy testach wyłapał sam w uwagach do PR-a.
- Bez zmiany te same potknięcia wrócą w kolejnych cyklach; rzadsze, ale groźne — zawieszony test, zgubione pierwszeństwo decyzji, nowe ostrzeżenie ukryte wśród starych, kawałek planu oddany na zielono, choć sprawdzenie nie widziało nowego pliku — wyjdą dopiero, gdy ktoś je zauważy, albo wcale.

### To do

Brzmienia w cudzysłowie są przyjęte przez Mariusza słowo w słowo. Miejsca wskazuje nagłówek albo cytat; numer linii to podpowiedź według `origin/foundations` @ 2a2f4106.

1. **Przebieg w tle bez końca (AIR-705).** Agent cyklu, który czeka na polecenie puszczone w tle (WAY-255), ma górną granicę czasu: przebieg, który nie skończył się po N minutach, agent zatrzymuje i zgłasza jako niezakończony — z poleceniem i ostatnimi liniami wydruku — zamiast czekać dalej. N = 30 minut (pytanie 1). Brzmienie nieustalone — przyjęta jest zasada, nie tekst.
   - Miejsca: punkt zaczynający się od „A command that may run longer than your harness keeps its prompt cache” w `task-cycle/change/SKILL.md` (ok. :120-123) i w `task-cycle/review/SKILL.md` (ok. :113-116); zdania wiążące WAY-255, przez skill zapisu decyzji (`record-decision`).
   - Prowadzący wpisuje takie zdarzenie do zapisu cyklu, a sprawdzenie jako niewykonane: `task-cycle/skill/SKILL.md`, akapit o raporcie agenta z „a one-line check result naming what failed or did not run” (ok. :284-286).
2. **Wycofanie decyzji, która zawęża inną (AIR-697).** `elements/decisions/template.md`, sekcja „Changing a decision”, po punkcie „A decision no longer needed leaves the log in the change that ends it” (ok. :222-223), i to samo w zdaniach wiążących WAY-25 (przez skill zapisu decyzji):
   > „A decision that narrows another — named `narrows` in its *Relations*, or one whose binding sentences go against a decision it derives from in a narrower area, which is a `narrows` left unrecorded — leaves the log only with the area where it prevails carried into that other decision or into the skill or template that takes the rule, or it stays. A decision whose *Rejected* refuses the move that would withdraw it stays.”
3. **Kawałki planu zostawiające testy czerwone (AIR-708).** `task-cycle/plan/SKILL.md`, po punkcie o *Checks* zaczynającym się od „*Checks* are commands that can actually run in the product” (ok. :174-186):
   > „A slice may leave tests of the product failing that a later slice of the same plan makes pass; its *Goal* names each such test file and the slice that makes it pass, and no slice's *Checks* holds a test an earlier slice leaves failing until its owner has passed. The handoff of each later slice lists the tests the plan leaves failing at its base, with their owners, and its executor reports a listed test that fails as expected, not as a failing check of its slice; a test that fails after a slice and that no *Goal* names goes into the slice's report, and the orchestrator gives it an owner by editing the plan before the next slice is dispatched.”

   W `task-cycle/skill/SKILL.md`, w kroku „when it returns `done` or `done with concerns`, check mechanically” (ok. :464), pół zdania: „…and the failures its report names against those the plan lists”.
4. **Kawałek „za duży” tylko przez jeden ogromny plik (AIR-707).** `task-cycle/slice_size.py` — opis, kod i test:
   > „A slice too large only because one file of *Change* counts whole — one that would fit were that file counted by the ranges *Read* names of it — is reported `fits by ranges of <file>` instead of `too large`.”

   `task-cycle/plan/SKILL.md`, sekcja „4. Check the size of each slice”, przy zdaniu „Split every slice it reports `too large`” (ok. :211):
   > „A slice reported `fits by ranges of <file>` is no slice to split: its *Read* names the ranges of that file it changes, its agent changes them by search, and the review of the plan accepts it as it stands.”
5. **Szum ostrzeżeń sprawdzarki instrukcji (AIR-706).**
   1. `instruction-files/check_instructions.py`, funkcja `looks_like_path` (ok. :430): nie jest ścieżką tekst zaczynający się od `#` (adres w aplikacji, `#/konta`), tekst z cudzysłowem, `=` albo `,`, ani samo rozszerzenie (`.css`).
   2. `check_instructions.py` i lista w sekcji „What the check script settles” w `instruction-files/SKILL.md`, punkt „every path, skill and command pointed to exists;” (ok. :271):
      > „every path, skill and command pointed to exists; an absolute path outside the repository and the home directory, named in a file of the repository, names a place on another machine, such as a server the product deploys to, and is listed as not checked, not as missing;”

      W pliku podanym przez `--file` (globalny plik instrukcji użytkownika) ścieżki bezwzględne są sprawdzane jak dziś.
   3. `check_instructions.py`: ścieżka względna, której pierwszy człon stoi jako osobna linia w głównym `.gitignore`, dostaje poziom `info` (wynik uruchomienia), nie `warn`.
   4. `installation/README.md`, po akapicie kończącym się „…and to report that the one command leaves it unchecked.” (ok. :84):
      > „A warning is the change's to fix as an error is: the product keeps the script at no warning, and a change that adds one corrects the path or names it where the script does not read it.”

      Do tego jedno zdanie w `task-cycle/review/whole_change.md` (miejsca w pliku źródło nie wskazuje): ostrzeżenie tego skryptu w przebiegu na głowie zmiany to uwaga recenzenta — bez porównywania z bazą — blokująca: Important, w zakresie zadania (pytanie 3).
   5. Testy w `instruction-files/test_check_instructions.py` dla podpunktów 1–3.
6. **Świeża kopia repozytorium bez the-way i zależności (AIR-700).** `task-cycle/skill/SKILL.md`, sekcja „Working copies” (ok. :354), po pierwszym zdaniu:
   > „In a product, a worktree or checkout made to run checks gets its `.the-way` populated, and the dependencies those checks need installed as the product's own rules give, before they run; otherwise they fail for that reason.”

   Zdanie „In a product that checkout gets its dependencies installed, as the product's own rules give, and its `.the-way` populated before the checks run; otherwise they fail for that reason and not on the base.” (ok. :189-191) zamienić na odesłanie do tej sekcji.
7. **Kopia strony w archiwum bez cytowanego fragmentu (AIR-702).** `elements/environment-facts/template.md`, punkt zaczynający się od „a page without editions, with the closest archived copy that already exists” (ok. :109-113), dostaje brzmienie:
   > „a page without editions, with the closest archived copy that already exists and holds the passage, and its date — never one made for the entry, since that writes to someone else's service; where none exists, `no archived copy exists in the Internet Archive's CDX index, checked <date>`, and where those that exist do not hold it, `no archived copy in the Internet Archive's CDX index holds the passage, checked <date>` — and the place, the passage and the date read.”

   `elements/environment-facts/skill/draft.md`, po „…which misses captures that exist” (ok. :11-12):
   > „; open the copy and find the passage in it — a redirect or a page without the text holds none.”
8. **Zależność części, której chce zadanie (AIR-703).** `elements/part-map/template.md`, przed akapitem „A dependency of a part that the code holds and *Depends on* does not allow goes to the human” (ok. :113):
   > „A dependency that a settlement of the task names, or that the human allows, is written into *Depends on* by the change, its source named in the commit message, since the map holds no field for it; a settlement that asks only for a behaviour allows no dependency. The route below is for a dependency the human accepts as it stands without allowing it.”

   `elements/part-map/skill/SKILL.md`, po „…never rewrite it to fit the code (WAY-225).” (ok. :40):
   > „A dependency a settlement of the task names, or the human allows, is written into it, as the template's "Allowed dependencies" says.”

   Błąd zastany: `elements/decisions/skill/SKILL.md`, zdanie z „the entry marked as `task-cycle/skill/foundation_step.md` gives (WAY-114)” (ok. :39), podaje ścieżkę części `task-cycle`, której część `decisions` nie ma w *Depends on* (`foundations/part_map.md`). Ścieżkę usunąć, zostawiając słowa: „the entry marked as the cycle's foundation step gives (WAY-114)” (pytanie 2).
9. **Komentarz `decision:` przy teście i sprawdzenia przed `git add` (AIR-704, AIR-701, AIR-710).** `task-cycle/change/SKILL.md`, nowy punkt zaraz po punkcie „**Name the break each test catches.**” (ok. :75-78):
   > „A test whose break is code going against a sentence of a recorded decision holds that sentence, and carries the line `decision:` that `elements/decisions/template.md` gives in "Verification"; a test that only stands on the sentence — a precondition it asserts, a fixture — holds nothing of it.”

   `task-cycle/change/SKILL.md`, po „…the tests of the code you touched.” (ok. :116-117):
   > „Run them after `git add` of every file your change creates: many checks, the foundation check among them, list only the files git tracks, and a run before that passes without seeing the new file.”

   `elements/decisions/template.md`, po „The line stands at the test that holds the sentence” (ok. :276-277):
   > „; each test that holds a part of the sentences carries a line of its own, and a test that holds sentences of several decisions carries one line for each”
10. **Skrypt listy decyzji (AIR-698).** `elements/common/decision_index.py`, z testami:
    - `--decision` dopasowuje po wartości liczby: `107`, `WAY-107`, `D-7` i `D-07` trafiają w tę samą decyzję (produkt ma jeden dziennik z jednym przedrostkiem, WAY-18);
    - numer z tabeli „Withdrawn identifiers” dziennika (`foundations/decisions.md`, sekcja „## Withdrawn identifiers”, ok. :11594) nie kończy się błędem: jego następcy trafiają na listę w całości, a nad listą staje linia `<ID> is withdrawn: <powód z tabeli>; its successors are listed in full`; numer bez następcy (`none`) daje linię `<ID> is withdrawn: <powód z tabeli>; it has no successor` i kod 0, a następca sam wycofany prowadzi dalej, aż do żyjących decyzji, i linia nazywa cały łańcuch z powodami (pytanie 4);
    - pomoc skryptu (opis na początku pliku, `metavar` przełącznika `--decision`) i punkt „Add with `--decision NUMBER`” w `elements/common/way_of_working.md` (ok. :105) mówią `--decision ID`, z jednym zdaniem o obu zasadach.
11. **Pomiar bramki na Windows i licznik testów (AIR-699).**
    1. `task-cycle/gate_times.py`, przed `subprocess.Popen(command, …)` (ok. :435): pierwszy człon polecenia rozwiązuje się przez `shutil.which`, który na Windows dobiera `.cmd`/`.bat` — `npm test` z deklaracji produktu działa bez zmian. Test na poleceniu będącym plikiem `.cmd`, pomijany poza Windows.
    2. `gate/run_tests.py`, pętla liczenia linii `Ran <n> tests` (`RAN.match`, ok. :143-148): liczba testów katalogu to ostatnia linia `Ran <n> tests` jego wydruku, nie suma wszystkich. Test na wydruku z zagnieżdżonym przebiegiem.
12. **Dane próby recenzenta (AIR-711).** `task-cycle/skill/SKILL.md`, sekcja „Working copies”, zdanie z „keeps in `reports/` beside its report what the report needs” (ok. :365): „…keeps in `reports/` beside its report what the report needs**, the input and command of a probe that shows a finding among them,** and states…”. `task-cycle/review/SKILL.md`, zdanie kończące się „and the evidence: the test, check or line that shows it.” (ok. :165): „…and the evidence: the test, check or line that shows it**, or the path in `reports/` of the probe that shows it.**”
13. **Wyszukiwanie zdania w tekście łamanym na linie (AIR-712).** `task-cycle/plan/SKILL.md`, po „named with their arguments.” (ok. :174):
    > „A check that proves a sentence of prose gone or present searches its words with any whitespace between them, line breaks included — `rg -U` with `\s+` between the words, over the files `git ls-files` lists — since the text wraps where its line ends, and a search line by line passes over a sentence broken elsewhere.”

### Questions to settle

- 1. Po ilu minutach (N) agent uznaje przebieg w tle za zawieszony (punkt 1)?
  - Answer: stała 30 minut, jedna dla wszystkich produktów.
  - Not chosen:
    - wielokrotność czasu pełnych testów produktu z tabeli czasów bramki (`task-cycle/gate_times.py`) — pierwszy cykl nowego produktu tej tabeli nie ma, agent musi dostać jeszcze jeden plik, a pełne testy to zła skala dla testów jednego kawałka, które agent puszcza
    - stała 30 minut, a zlecenie może podać dłuższą granicę dla wskazanego polecenia — „Wariant c dopiszemy jednym zdaniem, gdy pojawi się pierwszy przypadek”
  - Source: doradca dnia (sesja `the-brain-33`) w imieniu Mariusza, 2026-11-22: „1 — a, stała 30 minut. Uzasadnienie: agent cyklu puszcza tylko testy swojego kawałka, w 77 cyklach nie było polecenia dłuższego niż pół godziny, a liczbę w dwóch skillach i jednej decyzji cofa jedna poprawka. Wariant c dopiszemy jednym zdaniem, gdy pojawi się pierwszy przypadek.”
- 2. Ścieżka `task-cycle/skill/foundation_step.md` w `elements/decisions/skill/SKILL.md` (punkt 8): dopisać `task-cycle` do *Depends on* części `decisions` czy usunąć ścieżkę z tekstu?
  - Answer: usunąć ścieżkę, zostawić słowa: „the entry marked as the cycle's foundation step gives (WAY-114)”.
  - Not chosen:
    - dopisać `task-cycle` do *Depends on* części `decisions` — „zależność element → wnętrze cyklu (a) nic by nie dała, a przywiązałaby element używany poza cyklem do cyklu”
  - Source: doradca dnia (sesja `the-brain-33`) w imieniu Mariusza, 2026-11-22: „2 — b, usunąć ścieżkę, zostawić słowa („the entry marked as the cycle's foundation step gives (WAY-114)”). Uzasadnienie: agent w cyklu ma ten plik w zleceniu, poza cyklem zdanie nie ma zastosowania, więc zależność element → wnętrze cyklu (a) nic by nie dała, a przywiązałaby element używany poza cyklem do cyklu. Spójne z odesłaniami po nazwie w process-audit. Cofnięcie tanie.”
- 3. Czy ostrzeżenie sprawdzarki instrukcji w przebiegu na głowie zmiany blokuje recenzję całej zmiany (punkt 5.4)?
  - Answer: blokuje — recenzent ocenia je Important, w zakresie zadania; sprzątanie prawdziwych ostrzeżeń loop2 idzie w zmianie przepięcia loop2 na nową wersję the-way.
  - Not chosen:
    - nie blokuje, uwaga trafia do dolnych list opisu PR-a — ostrzeżenia znów się zbierają, wraca szum, który leczy punkt 5, a „tak jak błąd” staje się pustym słowem
  - Source: doradca dnia (sesja `the-brain-33`) w imieniu Mariusza, 2026-11-22: „1 — a (blokuje, Important, w zakresie). Sprzątanie loop2 idzie w zmianie przepięcia: przepięcie i tak ma w zleceniu „napraw to, co zgłoszą nowe kontrole”, więc zdanie w „Out of scope” zmień na „w zmianie przepięcia loop2 na nową wersję the way”. Słaby punkt znika w praktyce: skoro przepięcie zostawia produkt na zerze, ostrzeżenie na głowie zmiany pochodzi z niej samej albo z nowej kontroli, którą wnosi następne przepięcie — to samo miejsce, które je sprząta.”
- 4. Co robi `decision_index.py --decision` dla wycofanego numeru bez żyjącego następcy (punkt 10)?
  - Answer: dla następcy `none` linia `<ID> is withdrawn: <powód>; it has no successor` i kod 0, reszta wyboru listowana; następca sam wycofany — łańcuch aż do żyjących decyzji, linia nazywa cały łańcuch z powodami.
  - Not chosen:
    - dla `none` błąd jak dziś, z powodem z tabeli w komunikacie; przy łańcuchu tylko bezpośredni następca — punkt 10 nie leczyłby większości wycofanych numerów (136 ze 179 ma następcę `none`)
  - Source: doradca dnia (sesja `the-brain-33`) w imieniu Mariusza, 2026-11-22: „2 — a (linia „it has no successor”, kod 0, łańcuch do żyjących decyzji, linia nazywa cały łańcuch z powodami).”; tabela „Withdrawn identifiers” w `foundations/decisions.md:11594` @ 2a2f4106 — 136 ze 179 wierszy ma następcę `none`, a 8 wskazuje następcę sam wycofanego (np. WAY-46 → WAY-40 → `none`)

## Context

- Źródło: dzienna sesja przeglądu warstwy AI (`/ai-review`) z 2026-11-22, sprawy z zapisów cykli; każdy punkt to przyczyna powtarzającej się uwagi agentów, nie jednorazowa łatka, i każdy przeszedł krytykę świeżego agenta i sprawdzenie w plikach.
- Pliki ruszane przez kilka punktów: `task-cycle/change/SKILL.md` — punkty 1, 9; `task-cycle/review/SKILL.md` — punkty 1, 12; `task-cycle/skill/SKILL.md` — punkty 1, 3, 6, 12; `task-cycle/plan/SKILL.md` — punkty 3, 4, 13; `elements/decisions/template.md` — punkty 2, 9.
- Punkt 1: w loop2 plik testów, który nigdy się nie kończył, trzymał wykonawcę ok. dwóch godzin.
- Punkt 1: reguła „kończ turę dopiero po końcu przebiegu” weszła 19.11 (fc88ee2c), a cykl z 15.11 biegł na ec7929d — tamten przestój miał inną przyczynę, ale dziś ryzyko jest większe.
- Punkt 1, odrzucone: kryterium „wydruk nie rośnie przez trzy odcinki” — `gate/run_tests.py` (ok. :136-141) wypisuje wynik katalogu dopiero po jego końcu, więc cisza przerywałaby zdrowe przebiegi.
- Punkt 2, odrzucone: kontrola w `foundation_check.py` po relacji `narrows` — obie zgubione decyzje (WAY-329, WAY-202) miały tylko `derives from` (sprawdzone w e6433717^), więc kontrola by ich nie złapała.
- Punkt 3, powód drugiego zdania cytatu: wykonawca puszcza też „tests of the code you touched” (`task-cycle/change/SKILL.md`), a zgłoszone czerwone sprawdzenie daje powtórkę klasą wyżej (`task-cycle/skill/SKILL.md`, ok. :475-476, WAY-229).
- Punkt 3, odrzucone: zakaz czerwonego stanu — w loop2 oznaczałby jeden kawałek na dziewięć, za duży dla agenta.
- Punkt 4, odrzucone: limit rozmiaru plików testów i podział `tests/view/account-screen.test.mjs` w loop2 — WAY-385 i decyzja loop2 D-425 świadomie wyjmują pliki testów spod limitu, a szkody z tej decyzji nikt nie wykazał.
- Punkt 5: sprawdzarka zgłasza na loop2 `main` 141 ostrzeżeń „does not exist” — 89 to ścieżki bezwzględne serwera w skillu wdrożenia, 17 to tekst, który nie jest ścieżką, 20 to foldery tworzone w trakcie działania, wpisane w `.gitignore`, 15 to reszta.
- Punkt 5, odrzucone: porównanie ostrzeżeń bazy i głowy w przeglądzie całej zmiany (leczy objaw, tylko u jednego recenzenta, wymaga dwóch dodatkowych kopii repozytorium); przepisanie ścieżek serwera w loop2 do bloków kodu (każda nowa ścieżka znów szumi).
- Punkt 6: akapit „Working copies” każde zlecenie kopiuje słowo w słowo (WAY-148), więc nowe zdanie trafi do każdego agenta.
- Punkt 6, odrzucone: zdanie tylko w metodzie recenzenta (`task-cycle/review/SKILL.md`, ok. :110) — połowa tego już obowiązuje od 4594a5a9, a recenzent to nie jedyny agent, który robi kopie.
- Punkt 7: dotychczasowa forma „no archived copy exists” zostaje, więc fakty już zapisane w loop2 nie wymagają zmiany.
- Punkt 7, odrzucone: pozycja dla Mariusza w opisie PR-a przy każdym takim fakcie — forma „kopii nie ma” z PR #155 świadomie jej nie daje.
- Punkt 8: ścieżka w skillu decyzji weszła w PR #137 (commit e9aea956).
- Punkt 8, odrzucone: zdanie definiujące, kiedy wspomnienie pliku innej części jest zależnością — odesłanie po nazwie sekcji w `process-audit/SKILL.md` (ok. :109 i :169) stałoby się wtedy niedozwoloną zależnością, odwracając świadomy odczyt cyklu #134; pytanie nie wróciło w ok. 20 cyklach od 16.11; definicja w słowniku ma być jednym zdaniem (WAY-94).
- Punkt 9, odrzucone: zdanie o miejscu linii („on the line above the test's opening”) — 1979 linii `decision:` w testach loop2 stoi na początku ciała testu; sprawdzenia widzące nieśledzone pliki (zmiana w ok. 25 skryptach, a i tak nie obejmuje narzędzi produktu).
- Punkt 10: najczęstszy kłopot przeglądu — 26 uwag w 23 cyklach.
- Punkt 10, odrzucone: same lepsze komunikaty błędu — pierwsze wywołanie dalej by padało.
- Punkt 11: błąd `cannot start 'npm'` wrócił jeszcze 20.11 (loop2, zapas-i-wskrzeszenie); odczyt zagnieżdżonego wydruku w samym `gate_times.py` naprawiono już 21.11 (8359dc25 i kolejne).
- Punkt 11: zmiana skryptu pomiaru i programu uruchamiającego testy zaczyna nową serię czasów bramki (WAY-339) — jedną, dla obu podpunktów.
- Punkt 11, odrzucone: zdanie w skillu, żeby na Windows podawać `npm.cmd`.
- Punkt 12: plik uwag dla agenta poprawki przepisuje uwagi słowami recenzenta (`task-cycle/skill/SKILL.md`, ok. :239), więc ścieżka próby dojdzie do poprawki bez osobnego zdania.
- Punkt 13, odrzucone: to samo zdanie w trzech skillach (powielenie wbrew kierunkowi WAY-256); przestanie łamać tekst na linie (odwraca konwencję całego repo przy dwóch przypadkach, które agenci sami wyłapali).
- Pełny zapis sesji, w których zadanie powstało (wygasają ~2027-02-20, pliki lokalne poza repo): sesje `95a71d05-8d1e-458f-91a2-b5e37b5f3077` (sprawy AIR-705, 697, 708, 707) i `d2092bdf-e255-4b28-9519-b46c2cd7d4bd` (pozostałe) w katalogu projektów Claude Code dla vaultu.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Zadanie zmienia trzy decyzje, przez skill zapisu decyzji (`record-decision`), i dodaje jedną nową (wiersz 4 *Settlements to record*):

- WAY-25 — dostaje zdanie o wycofaniu decyzji, która zawęża inną (punkt 2 *To do*, brzmienie tam).
- WAY-136 — dostaje zdanie o kawałku planu, który zostawia czerwone testy naprawiane przez późniejszy kawałek (punkt 3 *To do*, wiersz 3 *Settlements to record*).
- WAY-255 — dostaje górną granicę czekania: polecenie w tle, które nie skończyło się po 30 minutach, agent zatrzymuje i zgłasza jako niezakończone, z poleceniem i ostatnimi liniami wydruku (punkt 1 *To do*, pytanie 1).

Pozostałe zadanie dotyka bez zmiany: WAY-229 (punkt 3 — powtórka po czerwonym sprawdzeniu kawałka), WAY-160 (punkty 1 i 3 — sprawdzenie niewykonane nie jest zaliczone), WAY-12 (punkt 9 — linia `decision:`), WAY-148 (punkty 6 i 12 — zlecenie kopiuje akapit słowo w słowo, raporty w plikach), WAY-339 i WAY-390 (punkt 11 — nowa seria czasów bramki, wzorzec rodzaju `command-runner`), WAY-18 (punkt 10 — jeden dziennik), WAY-225 (punkt 8 — *Depends on* pisane ręcznie). Brzmienia według `origin/foundations` @ 2a2f4106:

- **WAY-25 — What settles a collision between two decisions?**

  > Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a chain, and two decisions that narrow each other are an error. A collision between two decisions with no precedence recorded is never settled silently by the agent that meets it. Where what the human accepted gives the outcome and the change may write the decision that prevails, the change records the precedence in that decision, and its request names it with the passages of what the human accepted that give the outcome, for the human to accept at the merge (WAY-114); otherwise the agent stops and asks.

- **WAY-255 — How does an agent of a task's cycle wait for a command that runs long?**

  > An agent the orchestrator dispatches waits for a command that may run longer than its harness keeps its prompt cache — a container build, a mutation run, a test suite a check names — by running it in the background and reading its output between waits each shorter than that lifetime, never in one wait past it, and ending its turn only after the command has ended and it has read its result; in Claude Code a subagent's cache lives five minutes by default, so each wait stays under about four. The one author's cache lives an hour, which the author's type sets (WAY-368), and its waits stay under about four minutes as well, since Claude Code falls back to five minutes where a subscription spends usage credits. Where the harness states no cache lifetime, the agent waits as the harness allows.

- **WAY-136 — When does a task's change need a plan, and who makes and reviews it?**

  > A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step; the same judgment follows a reviewed spec, and an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; the slices are made one after another in the plan's order, each by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split.

  > A one-author change is reviewed by an agent that did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; a change of more than one slice then gets one review of the whole change, which judges every slice that had no review of its own and names, for each blocking finding, the slice it comes from or that it comes from none, while the review of a one-author change or of a plan's only slice is the review of the whole change; and that review also checks coverage of the task, every row of its *Settlements to record* and every projected entry it carries; where the slices that have no review of their own are more than one reviewer of the whole change can compare with their sources, the orchestrator may, by its own judgment and not by a measure, dispatch reviews of groups of them in the plan's order, as for a slice with a review of its own, and it records the grouping and its reason.

- **WAY-229 — On which class of model do the executor of a slice and the one author work?**

  > The executor of a slice, and the one author of a change without a plan, work on the class of model set for them, named in general terms and never by the name of a model: by default a class cheaper than the orchestrator's, for code that carries settled matters into the product, ordinary implementation that takes decisions of its own included; the orchestrator's class, for a change across many parts; or the strongest class available, which is the strongest of the models that the session's settings allow, which the orchestrator takes from the list of allowed models (in Claude Code the setting `availableModels`; where the session has no such list, every model it offers) and never from the name of the strongest model of the family, for one that needs design — each class other than the default with one sentence of its reason. The planner sets each slice's class in the plan; the orchestrator sets the one author's when it selects that route (WAY-136), by the same measure, and records it with its reason. The one author writes its foundation entries, takes its return step and fixes its findings on its own class.

  > An executor that returns `blocked` for a fact or permission no source supplies, reports a failing check of its slice, or fails the orchestrator's mechanical check (no commit in its range, or a repair it was sent back for left undone) gets one retry: a fresh executor one class higher, from the slice's base, given the failed executor's report and what failed; and an executor of the strongest class available that fails, or a retry that fails, stops the cycle.

  > The fix of a slice's findings runs on the class of the executor whose work stands, of findings in several slices on the highest of their classes and of a planned change's finding of no slice on the orchestrator's, while the spec's designer and reviewer, the planner, the writer of the plan's foundation entries, the return step of a planned change and every other reviewer work on no class cheaper than the orchestrator's, and the review of the whole change and the review of the return step work on the strongest class available.

- **WAY-160 — How does the task-cycle orchestrator run the finished change's gate?**

  > The final gate of a task cycle is the product's gate on the tree that goes into the request, and the request gives its command and exit code, or the CI run's, and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run on the cycle's own system is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it. Where CI runs on a request whose code is finished — one open for review, or one that waits only for human actions in the cycle — the CI run on the head pushed last is the final gate, and the orchestrator runs no full gate itself at the end of the cycle or after the merge with the target branch; the run on the base of the task branch and the run after the pin of the-way moves stay the orchestrator's own, since no request stands then, and where CI runs on no request, or the request is left blocked for unfinished code, the orchestrator runs the gate itself on the tree that goes into it, save where that tree is one already run.

  > The orchestrator waits for the result of the CI run on each head it pushes to the request, a correction's included, treats a red result as a failed gate, handled as the cycle's gate gives — a fix and its review and the wait for the run on the new head, save a check outside the task's scope that passes when run again, which WAY-261 governs — and puts the result into the request's description. Where the run gives no result within 30 minutes of the push — it does not start, it stands in a queue or the host does not answer — the orchestrator runs the gate itself on the tree of that head, and the description says that CI did not answer and that the gate ran on the cycle's own system; a request the cycle leaves blocked for unfinished code is out of that wait, its description saying that the result of the CI run stands on the request's page and was not waited for. Where CI is the final gate, the cycle's record says so before it is copied, and names the request whose description gives the result, so that the next cycle takes the list of failing tests from there.

- **WAY-12 — How is a decision checked?**

  > A decision names in *Verification* the invariants derived from it, by the identifiers of their entries, where such invariants exist, and the tests that hold its sentences, by a clause that gives the parts of the sentences they hold in words and no path, no test name and no number. A test that holds a sentence of a decision carries beside it a line `decision:` that gives the number of the decision and the start of that sentence, and the decision keeps its rationale and its rejected options whole. A decision may also carry a pair of examples — a change that complies and one that violates — only for the part of its sentences that no invariant and no test checks, with which an agent compares a change with that part; the violating example is a change whose code goes against the decision while its entry stays as it is, never one that replaces the decision together with its code.

  > A decision is held when its *Verification* names an invariant, when a test holds a sentence of it by a line `decision:` that names its number, or when it carries a pair of examples. The check of the foundation reports as an error a decision that a change adds, or whose binding sentences the change alters, and that nothing holds. Any other decision that nothing holds stands in a list the check prints, and the list stops no change.

- **WAY-148 — How do task-cycle stages pass their work to the orchestrator?**

  > Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, where the stage runs a test or another check, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan; and since only the orchestrator reads `cycle.md`, the handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them, and an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it.

  > The orchestrator records the event and relevant choices before dependent dispatch and reads authoritative sources and relevant report evidence before deciding a question, settling a finding, accepting a foundation meaning or verifying disputed or incomplete evidence, while routine progression uses the short return, record, source paths and commits, without loading the material the stage agent reads and checks or its full report again, and without requiring prior conversational history; a missing or incomplete report is repaired before dependent work proceeds, check and review duties stay with their assigned owners, and the cycle record is the cycle's only log, with no method of the cycle keeping a log of its own beside it.

- **WAY-339 — When do the measures of the audit stop being comparable?**

  > A new series of the cost of cycles, the two numbers of WAY-337, starts only with a new price list or with a change of the script that measures the cost, `task-cycle/cycle_stages.py` with the module `task-cycle/stage_transcripts.py` that it imports; a new series of the count of remarks starts wherever a series of the cost starts and also with a change of the form of a stage report, of the list of classes or of the instructions of the reviewer. The measures of how a cycle's agents use context and the prompt cache and the times of the gate form series of their own: a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process, whose output gives the time of each directory; no change of the instructions of the cycle, the reviewer's and the author's included, starts one.

  > The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; and where a cycle's own change changes a tool that measures — the script that measures the cost, the script that counts the measures of context and cache use, the script that records the gate times or the test runner of the process — the audit gives the measures of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote them (the file of that tool is not read for that cycle, so no field of it is missing and no line `Error:` is given for it), and its other measures as they stand under the version it ran on. The audit shows each series as an image of all its cycles — what its kind carries, the answer Q3 and the fall standing only where two groups meet (WAY-417) — and, inside it, as a comparison before and after a change: the cycles on the versions that hold the change against those on the versions that lack it, both groups of that series, the version a cycle ran on, never its date, deciding its group; for the times of the gate both take only the runs that WAY-350 compares. That comparison is made for each fixed issue of the register of problems with a fix commit, and for no other change.

  > The measures of how a cycle's agents use the context and the prompt cache of the model — the number of model calls, the size of each call's context, the tokens written to the cache and the tokens written to it again, and, for each agent of the cycle, the bytes of the decision log and of the index of decisions that entered its context and how many times each entered it — are counted by a script of their own into a file of their own in the cycle's record, and are never columns of the stage report of the cycle's stages, the table of its tokens by model. The one exception is that this report holds, for each stage and model, the tokens written to the cache at each lifetime, as an input of the cost (WAY-337) and not as a measure of cache use: the script that measures the cost counts them, the script of the other measures counts the same tokens for its own file, and neither takes its figures from the file of the other.

- **WAY-390 — Which file is the exemplar of the kind `command-runner` in the-way's code?**

  > `task-cycle/gate_times.py` is the exemplar of the kind `command-runner` of the-way's code, and a script of the kind that wraps one command ends with that command's exit code unchanged.

- **WAY-18 — How is a product's decision log kept?**

  > A product keeps all its decisions in one log, whatever they are about. The log holds one entry for each decision in force and itself says what binds today, with no view generated from it kept in its place; the index of a selection of decisions that an agent writes on demand (WAY-150) is no such view. A link between entries is written at one end only; the one exception is a decision's invariants, which its *Verification* names while each of them names the decision in *Derives from*.

  > A log may be divided into topical sections, each a heading with one sentence of what it covers, its entries keeping their numbers; in a log so divided a new entry stands at the end of the section of its topic, or, where no section fits, in a new section at the end of the log, which the request that adds the entry names. A log without topical sections holds its entries in the order they were written, a new entry at its end.

- **WAY-225 — What in a product's foundation is derived rather than written by hand?**

  > What can be derived from what the product executes — code, configuration, infrastructure as code, runtime traces — is derived, never written by hand, and what is derived describes the state. Rules are written by hand: what is allowed and what the product promises, which the code cannot show, and a dependency of a part that the code holds and the part map does not allow is recorded as an invariant the product does not meet (WAY-51), never by rewriting the allowed dependencies of a part to fit the code.

## Settlements to record

Candidates: 6 shown, 4 accepted — 2026-11-22

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Agent cyklu, którego polecenie w tle nie skończyło się po 30 minutach, zatrzymuje je i zgłasza jako niezakończone — z poleceniem i ostatnimi liniami wydruku — zamiast czekać dalej, a prowadzący zapisuje to sprawdzenie jako niewykonane. | sentence of WAY-255 | pytanie 1 (z *Not chosen*); punkt 1 *To do* | ile minut czekać i co zrobić po przekroczeniu; bez wierszy *Rejected* WAY-255 nie dostałby odrzuconych wariantów (wielokrotność czasu bramki, granica w zleceniu, kryterium ciszy wydruku) |
| 2 | Decyzja, która zawęża inną — z `narrows` w *Relations* albo z `narrows` niezapisanym — opuszcza dziennik tylko z obszarem swojej przewagi przeniesionym do tamtej decyzji albo do skillu lub szablonu, który przejmuje regułę; inaczej zostaje, a decyzja, której *Rejected* odrzuca jej wycofanie, zostaje zawsze. | sentence of WAY-25 | punkt 2 *To do* (brzmienie przyjęte przez Mariusza); odrzucona kontrola w `foundation_check.py` po `narrows` — *Context*, punkt 2 | co wpisać w *Rejected* WAY-25: bez wiersza odrzucona kontrola po relacji `narrows` nie trafi do decyzji i ktoś zaproponuje ją ponownie |
| 3 | Kawałek planu może zostawić czerwone testy produktu, które naprawia późniejszy kawałek tego samego planu, jeśli jego *Goal* nazywa każdy taki plik testów i kawałek, który go naprawia; oczekiwanie czerwonego testu z listy nie jest czerwonym sprawdzeniem kawałka. | sentence of WAY-136 | punkt 3 *To do*; odrzucony zakaz czerwonego stanu — *Context*, punkt 3; przyjęte: doradca dnia (sesja `the-brain-33`) w imieniu Mariusza, 2026-11-22: „3 — tak (bez niego WAY-136 dalej czyta się jak zakaz, a skill mówi co innego — sprzeczność, na której zbuduje następny planista)” | cykl wpisałby regułę tylko do `task-cycle/plan/SKILL.md` i `task-cycle/skill/SKILL.md`; zakaz czerwonego stanu nie byłby nigdzie zapisany jako odrzucony, a WAY-136 („every other slice goes on after … its own checks”) dalej czytałby się jak zakaz |
| 4 | Ostrzeżenie sprawdzarki instrukcji zmiana naprawia tak jak błąd: produkt trzyma skrypt na zerze ostrzeżeń, a ostrzeżenie w przebiegu na głowie zmiany jest blokującą uwagą recenzenta (Important, w zakresie zadania), bez porównywania z bazą; decyzję trzyma najtańszy środek, który dopuszcza szablon decyzji — para przykładów, gdy wystarcza, test tylko, gdy szablon go wymaga. | decision | punkt 5.4 *To do*; odrzucone: porównanie bazy i głowy, przepisanie ścieżek serwera do bloków kodu — *Context*, punkt 5; przyjęte z warunkiem: doradca dnia (sesja `the-brain-33`) w imieniu Mariusza, 2026-11-22: „4 — tak, z warunkiem: decyzję trzyma najtańszy środek, który dopuszcza szablon decyzji (para przykładów, gdy wystarcza; test tylko, gdy szablon go wymaga). Uzasadnienie: zero ostrzeżeń to reguła wiążąca każdy produkt, a odrzucone porównanie z bazą wróciłoby bez zapisu.” | cykl wpisałby zdania tylko do `installation/README.md` i `task-cycle/review/whole_change.md`, bez decyzji, do której odsyłają; odrzucone porównanie bazy i głowy nie byłoby nigdzie zapisane |

## Out of scope

- Jednorazowe sprzątnięcie ok. 15 prawdziwych ostrzeżeń sprawdzarki w loop2 — idzie w zmianie przepięcia loop2 na nową wersję the-way (pytanie 3) — m.in. `mariusznazar/screenshots` (5×), `saved-game.js`, `frames.json`, `loop2/`, `~/.ssh/authorized_keys` w skillach `loop2-play` i `loop2-deploy`, `foundation_check.py` w `AGENTS.md:34`, `rules.test.mjs` w `guidelines/testing.md:285`; to zmiana w loop2, nie w the-way.
