---
title: Rozdzielić w the way dwa znaczenia słowa „gate”, żeby agent nie mylił akceptacji definicji z uruchomieniem testów
status: draft
created: 2026-10-25T16:00
updated: 2026-11-15
tags: [zadanie]
related: "the project note of the process of working on a product"
---

## Po co to

- **Jak jest dziś:** W the way słowo „gate” znaczy dwie rzeczy: polecenie, które uruchamia wszystkie testy produktu, oraz moment, w którym człowiek zatwierdza definicję projektu. Do tego słowo „projected entry” (wpis projektowany) niesie obowiązki w regułach, a słownik go nie wyjaśnia — a jego wpis „entry” mówi, że wpis leży w pliku fundamentu, choć wpis projektowany stoi w definicji projektu.
- **Kto to odczuwa:** Agent prowadzący definicję albo plan projektu w produkcie (dziś loop2), który czyta „the gate” bez kontekstu; Mariusz, gdy taki agent pominie zatwierdzenie albo zgłosi je w złym miejscu, i gdy na zatwierdzeniu definicji akceptuje znaczenie wpisów projektowanych.
- **Co jeśli nic:** Na razie nic — w źródłach nie ma przypadku, w którym agent pomylił te znaczenia; the way dalej łamie własną regułę, że słowo w dwóch znaczeniach dostaje jedno przemianowane.

# Rozdzielić w the way dwa znaczenia słowa „gate” i dopisać do słownika „projected entry”

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/commit/7aba681309ba179282d13bc4bf367e87919f486e

## Description

### Need

- Słownik the way definiuje „gate” jako jedno polecenie, które uruchamia wszystkie testy produktu, a część projektowa używa tego samego słowa dla zatwierdzenia definicji projektu przez człowieka („readiness gate”, „Gate record”, gołe „the gate”).
- Agent prowadzący definicję albo plan projektu w produkcie może przeczytać „the gate” w złym znaczeniu: uruchomić testy zamiast poprosić o zatwierdzenie definicji albo odwrotnie.
- Reguła WAY-99 każe w takim przypadku przemianować jedno ze znaczeń; Mariusz wybrał przemianowanie znaczenia projektowego.
- Reguły the way mówią o „projected entry” w zdaniach wiążących wielu decyzji, a słownik tego słowa nie wyjaśnia; jego wpis „entry” zawęża wpis do tekstu trzymanego przez plik fundamentu, choć wpis projektowany stoi w definicji projektu.
- Słownik definiuje „entry” jako tekst, który plik fundamentu trzyma o jednej rzeczy, a repozytorium mówi „entry” także o kluczu pliku lokalizacji (`~/.the-way/locations.json`) i o linii zadania w backlogu; zdanie „Where the file or the entry is missing” z `AGENTS.md` jest fałszywe w znaczeniu słownika.
- Słownik definiuje „read off” jako wartość, którą daje narzędzie z produktu albo maszyny, a krok badania technologii używa tego słowa dla właściwości wyczytanej z dokumentacji; agent znający słownik może uznać taką właściwość za odczytaną narzędziem, czyli pewniejszą, niż jest.

### To do

1. Wpis „gate” w słowniku (`foundations/glossary.md`, nagłówek `## gate`) zostaje przy znaczeniu polecenia testów, a jego pole *Not* wskazuje nową nazwę znaczenia projektowego, „readiness approval”.
2. Każde użycie słowa „gate” w znaczeniu zatwierdzenia definicji projektu w angielskim tekście plików śledzonych przez git repozytorium the-way dostaje nową nazwę: „readiness gate” → „readiness approval”, „gate record” / „Gate record” → „approval record” / „Approval record”, a gołe „the gate”, „its gate”, „definition gate” i podobne w tym znaczeniu — wyrażenie z nowej nazwy; dotyczy to także nazw plików (np. `project-level/skill/readiness_gate.md`), nagłówków sekcji skilli, opisów skilli i komunikatów skryptów. Po zmianie „gate” w the way znaczy już tylko polecenie testów albo część `gate` i jej katalog.
3. Szablon definicji projektu (`project-level/definition_template.md`) ma sekcję `## Approval record` w miejsce `## Gate record`, a skrypty `project-level/readiness_check.py` i `project-level/plan_check.py` szukają sekcji zatwierdzenia pod nową nazwą; ich testy sprawdzają nową nazwę.
4. Status definicji gotowej do zatwierdzenia ma wartość `awaiting approval` w miejsce `ready for gate` — w szablonie definicji, w skryptach, które czytają linię `Status:`, i w ich testach (pytanie 4).
5. Niezmiennik `project-readiness-gate` (`foundations/invariants.md`, nagłówek `## project-readiness-gate`) ma identyfikator `project-readiness-check`, a każde miejsce, które go cytuje, w tym linie `invariant:` testów, cytuje nowy (pytanie 5).
6. Opis prośby o scalenie mówi, że produkt, który przesuwa przypiętą wersję the-way za tę zmianę, zmienia w swoich zatwierdzonych definicjach nagłówek `## Gate record` na `## Approval record` (pytanie 1), a w sekcji `## Backlog` swojego głównego `AGENTS.md` „the entry `tasks` under …” i podobne na „the key …” (pytanie 7).
7. Słownik the way dostaje jeden wpis „projected entry”, dopisany skillem `record-glossary-term`: brzmienie, w sekcji „Projected foundation changes” definicji projektu, wpisu albo zmiany wpisu, które fundament produktu ma przyjąć, gdy kod zadania uczyni je prawdziwym; definicja wymienia rodzaje (decyzja, niezmiennik, termin, fakt o środowisku, zmiana mapy części), a wpis „entry” zostaje bez zmian (pytania 2 i 6).
8. Zdania, w których „read off” znaczy wyczytanie czegoś z dokumentu, a nie wartość podaną przez narzędzie z produktu albo maszyny — wśród nich `project-level/technology/research.md`, krok „Weigh” („read off its documentation and its public record of use the properties”), ok. linii 27 — mówią to innymi słowami; wpis „read off” w słowniku zostaje bez zmian (pytanie 3).
9. Każde użycie „entry” / „entries” w znaczeniu klucza pliku lokalizacji w angielskim tekście plików śledzonych przez git the-way mówi „key” / „keys” — np. „the entry `tasks` under `the-way`” → „the key `tasks` under `the-way`”, „an entry of the locations file” → „a key of the locations file”, nagłówek „## Resolve an entry of the locations file” w `project-level/backlog_place.md`; wśród miejsc: `AGENTS.md` (sekcja `## Backlog`), `project-level/backlog_place.md`, `process-audit/SKILL.md`, docstringi i komunikaty `process-audit/audit_count.py`, decyzje WAY-27, WAY-107, WAY-320 (zdanie wiążące i *Verification*, które dziś podaje „the entry `tasks` under `the-way`” jako przykład zgodności), WAY-330 i cytowane pytanie WAY-342 w WAY-376. Nazwy w kodzie (`entry_path`, `REGISTER_ENTRY`) i wartości kluczy w samym pliku zostają (pytanie 7).
10. Każde użycie „backlog entry” w znaczeniu linii zadania mówi „the task's line in the backlog” albo podobne wyrażenie ze słowem „line” — WAY-140 („the task's state in the backlog entry the product names”), `task-cycle/record_template.md` („Writes to the task's backlog entry”), `task-cycle/skill/SKILL.md` i tekst testu `project-level/test_plan_state.py`, który ten wiersz zapisu kopiuje (pytanie 7). Po zmianach 9 i 10 „entry” w the way znaczy tylko wpis fundamentu, a hasło „entry” w słowniku zostaje bez zmian, z *Not*: none.
11. Punkty wejścia skilli (`.claude/skills/`, `.agents/skills/`) są przegenerowane poleceniem `python -B agent-instructions/skill_entry_points.py --write`, bo zmieniają się opisy skilli `define-project`, `plan-project` i `settle-technology`.

### Questions to settle

- Które znaczenie „gate” zmienia nazwę i na jaką?
  - Answer: znaczenie projektowe: „readiness gate” → „readiness approval”, „gate record” → „approval record” (w tym nagłówek `## Gate record` w definicjach), identyfikator niezmiennika `project-readiness-gate` → nowa nazwa; „gate” zostaje przy poleceniu testów.
  - Not chosen:
    - przemianowanie znaczenia testowego i inne warianty przeglądu fundamentu (sprawa C9) — nie zapisane: przegląd z wariantami odbył się w sesji Claude Code, której zapis się nie zachował.
  - Source: linia zadania w backlogu the-way (wpis `tasks` pod `the-way`), Mariusz, 2026-10-22: „the way: przemianować projektowe znaczenie „gate” — „readiness gate” → „readiness approval”, „gate record” → „approval record” (…, nagłówek czytany przez `readiness_check.py` i `plan_check.py`, identyfikator `project-readiness-gate`, migracja zatwierdzonych definicji w produktach; WAY-99, Mariusz 2026-10-22)”
- 1. Co z zatwierdzonymi definicjami w produktach, które mają nagłówek `## Gate record`?
  - Answer: nagłówek zmienia produkt przy przesunięciu przypiętej wersji the-way; opis prośby o scalenie tego zadania mówi, że produkt, który przesuwa wersję, zmienia w zatwierdzonych definicjach `## Gate record` na `## Approval record`, a w backlogu loop2 stoi zadanie na tę zmianę, czekające na to zadanie.
  - Not chosen:
    - skrypty the-way przyjmują oba nagłówki — stara nazwa zostaje w kodzie the-way w usuwanym znaczeniu, wbrew WAY-99, i trzeba późniejszego zadania, które ją usunie;
    - nic poza kodem the-way — nigdzie nie ma śladu, że produkt musi zmienić nagłówek; po przesunięciu wersji skrypt zgłosi brak sekcji, a agent może wziąć to za powód do ponownego zatwierdzania definicji.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a”
- 2. Przez jaki rodzaj nadrzędny słownik definiuje „projected entry”?
  - Answer: „entry” zostaje bez zmian, a „projected entry” to brzmienie przyszłego wpisu: „A projected entry is the wording, under a project definition's Projected foundation changes, of an entry, or of a change to one, that the product's foundation is to hold once a task's code makes it true.” (propozycja brzmienia; cykl wybiera brzmienie, zachowując znaczenie).
  - Not chosen:
    - poszerzyć „entry” tak, żeby obejmowało też tekst w definicji projektu — „entry” / „entries” stoi w 2304 miejscach, reguła zmiany znaczenia każe w tej samej zmianie przejrzeć każde, a zdania w rodzaju „sprawdzanie fundamentu sprawdza każdy wpis” przestałyby być prawdziwe dla wpisów projektowanych.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 a”
- 3. Czy zadanie obejmuje także „read off” (uwaga theway#059-8 z przeglądu fundamentu)?
  - Answer: tak; zdania, w których „read off” znaczy wyczytanie z dokumentu, mówią to innymi słowami, a wpis w słowniku zostaje.
  - Not chosen:
    - osobne zadanie — pełny cykl dla około pięciu zdań;
    - zostawić — uwaga zostaje otwarta, a agent znający słownik może uznać właściwość wyczytaną z dokumentacji za odczytaną narzędziem; przegląd ocenił skutek jako mały, bo agent badawczy nie dostaje słownika.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 a”
- 4. Na jaką wartość zmienia się status definicji `ready for gate`?
  - Answer: `awaiting approval`.
  - Not chosen:
    - `ready for readiness approval` — wierna nowej nazwie, ale z powtórzonym „ready”;
    - zostawić `ready for gate` — „gate” zostaje w znaczeniu projektowym, zmiana niepełna wobec WAY-99.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4 a”
- 5. Jaki identyfikator dostaje niezmiennik `project-readiness-gate`?
  - Answer: `project-readiness-check` — nazywa skrypt sprawdzający definicję przed zatwierdzeniem, o którym mówi niezmiennik.
  - Not chosen:
    - `project-readiness-approval` — powtarza nową nazwę, ale sugeruje, że niezmiennik mówi o samym zatwierdzeniu.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „5 a”
- 6. Czy słownik dostaje wpis tylko dla „projected entry”, czy także dla „projected decision”, „projected invariant” i pozostałych?
  - Answer: jeden wpis „projected entry”; definicja wymienia rodzaje, a „projected decision” czyta się jako wpis projektowany, który jest decyzją.
  - Not chosen:
    - osobne wpisy dla każdego rodzaju — cztery albo pięć wpisów mówiących to samo, do utrzymywania w zgodzie;
    - wpis dla samego przymiotnika „projected” — „projected mode” (tryb skilli) znaczy co innego niż „projected entry”, więc jedna definicja przymiotnika nie pasowałaby do wszystkich użyć.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „6 a”
- 7. Którą drogą idzie słowo „entry”, które repozytorium używa w trzech znaczeniach: wpis fundamentu (hasło słownika), klucz pliku lokalizacji i linia zadania w backlogu (propozycja P24 przeglądu fundamentu 2026-11-14)?
  - Answer: przemianować dwa znaczenia poboczne — klucz pliku lokalizacji na „key” („the key `tasks` under `the-way`”, jak już pisze `process-audit/audit_count.py:20` „under the key `the-way`”), linię backlogu na „the task's line in the backlog”; „entry” zostaje przy wpisie fundamentu, a *Not* hasła „entry” zostaje `none`, bo szablon słownika wpisuje w *Not* tylko znaczenia, których nie da czytelnik znający branżę, a klucz JSON i linia listy są znaczeniami branżowymi.
  - Not chosen:
    - (b) zostawić i zapisać osąd, że czytelnik tych znaczeń nie pomyli — wprost wbrew WAY-99, bo zdanie `AGENTS.md` spełnia jej test; obrona wymagałaby uznania wpisu fundamentu za znaczenie branżowe, a wtedy słowo nie powinno mieć hasła (WAY-95); każdy przegląd fundamentu znajdzie rozbieżność od nowa;
    - (a) ze słowem „location” dla klucza pliku lokalizacji (propozycja P24) — nie wybrane, wybrano „key”;
    - (a) z oboma znaczeniami wpisanymi w *Not* hasła „entry” (propozycja P24) — szablon słownika nie wpisuje w *Not* znaczeń branżowych.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 a, słowo „key” (klucz w pliku lokalizacji) i „the task's line in the backlog”; Not hasła „entry” zostaje none.”

## Context

- Słowo „gate” w znaczeniu projektowym w plikach śledzonych przez git the-way (2026-11-14, `f4af75d`): „readiness gate” 61 linii, „gate record” 46, `project-readiness-gate` 8, `ready for gate` 12, `readiness_gate` 3; do tego gołe „the gate” / „its gate” / „definition gate” w znaczeniu projektowym, nieliczone osobno — m.in. w `foundations/decisions.md` (WAY-117, WAY-118, WAY-126, WAY-156), `project-level/lead/skill/`, `project-level/plan/skill/`, `project-level/technology/`.
- Odcisk definicji liczy się z tekstu od `## Goal` do nagłówka sekcji zatwierdzenia, bez samego nagłówka (`project-level/readiness_check.py`, docstring funkcji liczącej odcisk, ok. linii 268), więc zmiana nagłówka nie zmienia odcisku zatwierdzonej definicji.
- Wartość `ready for approval` jest już zajęta: to wynik tury doprecyzowania w prowadzeniu projektu (`project-level/lead/conversation_template.md`, tabela wyników tury, ok. linii 132; `project-level/task/template.md`: „`ready for approval` is a conversation turn result, never a value of `Status:`”).
- Zatwierdzone definicje z `## Gate record` w produktach: dwie definicje loop2 w notatkach Mariusza poza repozytoriami (`definicja_mvp_loop2.md`, `definicja_mvp2_loop2.md` w folderze projektu Loop); loop2 przypina the-way na `55afa8e` (2026-11-11), którego skrypty szukają `## Gate record`.
- Przegląd fundamentu z 2026-11-07 skierował do tego zadania dwie niezałatane uwagi z próśb o scalenie: theway#059-9 („the skill says "readiness gate" and "the gate has approved", while the glossary defines "the gate" as the command that runs all tests”) i theway#059-8 = theway#066-10 („The glossary defines "read off" as what a tool gives from the product or the machine as they stand, while here an agent reads a property from documentation”, `project-level/technology/research.md`, krok „Weigh”).
- Reguła o przemianowaniu słowa w dwóch znaczeniach stała już w szablonie słownika (`elements/glossary/template.md` w `dc29549`), gdy „readiness gate” i „projected entry” weszły do the-way scaleniem `7aba681` („Merge task/way-project into foundations”), bez prośby o scalenie.
- Linia włączonego zadania (przegląd focusowy, 2026-11-06) wymienia zdania wiążące decyzji WAY-106, 116–118, 124, 126, 134 i 142–146 jako miejsca, w których „projected entry” niesie obowiązki.
- Fraza „projected entry” / „projected entries” występuje 132 razy w plikach śledzonych przez git (bez kopii punktów wejścia skilli), „projected decision” 38, „projected invariant” 4, „projected term” 2, „projected mode” 27.
- Szablon słownika podaje „castle gate” jako przykład kwalifikatora dla „gate” w znaczeniu polecenia testów (`elements/glossary/template.md`, sekcja „Two glossaries”); ten przykład zostaje prawdziwy po zmianie.
- Przegląd fundamentu 2026-11-14 (P24 i P25, bez uwag z próśb; do włączenia w doprecyzowaniu):
  - P25: zadanie niesie sprawę dwóch znaczeń „gate” w całości — potwierdzone.
  - P24: słowo „entry” ma w repozytorium trzy znaczenia — wpis fundamentu, wpis pliku lokalizacji (`~/.the-way/locations.json`, od WAY-320, `973ee64`) i linia backlogu; Mariusz zdecydował, że sprawa idzie tym zadaniem, a drogę rozstrzyga pytanie 7.
- Użycia „entry” w znaczeniu klucza pliku lokalizacji (2026-11-15, `21ecb62`, bez kopii punktów wejścia skilli i zapisów cykli): ok. 30 linii w 10 plikach — `AGENTS.md`, `foundations/decisions.md`, `foundations/part_map.md`, `process-audit/SKILL.md`, `process-audit/audit_count.py`, `project-level/backlog_place.md`, `project-level/definition_template.md`, `project-level/task/skill/orchestrated_mode.md`, `project-level/task/skill/read_sources.md`, `task-cycle/skill/foundation_step.md`; „backlog entry” — 4 linie.
- Zadanie „the way: dziennik decyzji po przeglądzie fundamentu 2026-11-14” (`zadanie_the_way_dziennik_decyzji_po_przegladzie_fundamentu.md` w tym samym folderze `_zadania`, *To do* 3, doprecyzowanie w toku) zmienia WAY-27 i WAY-320 sformułowaniem „entry of the locations file”; cykl, który scali się drugi, uzgadnia to słowo z „key”.
- `AGENTS.md` loop2 mówi w sekcji `## Backlog` „the entry `projects` / `tasks` / `task-rules` under `loop2`” (3 linie); zmienia je loop2 przy przesunięciu przypiętej wersji the-way.
- Plik danych przeglądu fundamentu 2026-11-14: `a data file of the foundation review of 2026-11-14 in the author's private notes`, sekcja „Fundament” → „Propozycje”, P24 i P25.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-99** — „Two uses of a word in the English text of the files git tracks carry two meanings when a sentence those files hold is true in the meaning of one use and false in the meaning of the other, whichever of the two the sentence uses, and a sentence made up for the test does not count; where one of the two meanings is a meaning a reader who knows the product's field would not give the word, one of the two is renamed, and the glossary entry of the word names in *Not* each such meaning it no longer carries, with the term, identifier, closed-list value or quoted word — holding neither the term nor its forms — that carries it now. A meaning whose word a human has not yet chosen reads `TODO` in *Not*, which a task branch may hold and the main branch never does. A file of a product in another language uses its words in the meaning they have in that language, and the rules of the glossary do not reach it.”
- **WAY-95** — „A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean; a word the product uses more narrowly than the field takes an entry only where a reader who takes the field's meaning would read a sentence of the product's English files wrongly. An agent that meets such a word in its work — writing an entry, searching the foundation, in a task's return step — writes its entry, no sweep of every binding sentence looks for candidates, and a human accepts the meaning (WAY-114).”
- **WAY-97** — „A sentence relies on a glossary term by using its word. A glossary entry is edited in place, its meaning included, and the author of a change to a definition searches, in the same change, the English text of every file git tracks for the word and rewrites each use whose meaning the new definition moves; a text in another language is not searched (WAY-99).”
- **WAY-34** — „A product uses the-way at a commit pinned in its own repository: its templates, skills and scripts, and the decisions of the-way that bind its work, all come from that commit. A newer version of the process enters a product only in one commit of the product that moves the pin, made when a task of the product needs a change of the process, as the first commit of that task's branch, under which the task's whole cycle works, or in a step of its own that takes several changes of the-way at once.”
- **WAY-118** — „The readiness gate blocks a definition with a missing section, unresolved content, an open question without its place of resolution, an unfinished candidate search, or an unsettled human-given part of a projected entry: (…) the gate record then names the approver and the fingerprint of the definition's sections from Goal through Projected foundation changes, and no projected entry carries a field of approval. A change to those sections after approval goes through the gate again before breakdown relies on it.” — zmiana: „readiness gate”, „the gate”, „gate record” w tym zdaniu dostają nowe nazwy, znaczenie bez zmian.
- **WAY-114**, **WAY-117**, **WAY-126** i inne decyzje, których zdania wiążące, uzasadnienie albo *Rejected* trzymają „readiness gate”, „gate record”, `project-readiness-gate` albo gołe „the gate” w znaczeniu zatwierdzenia definicji — np. WAY-114: „the meaning of a projected entry at the readiness gate”, WAY-126: „whole, in the wording the readiness gate approved, (…) with no record of approval copied from the gate” — zmiana: te słowa dostają nowe nazwy, znaczenie żadnej decyzji się nie zmienia; pełna lista wychodzi z wyszukania słowa w cyklu (WAY-97).
- **WAY-320** — „A user's places on their own disk that lie outside every repository, such as the place of a product's tasks and the place of its projects, are kept in one file, `~/.the-way/locations.json`, found at that place for every user and through no environment variable: a JSON object whose keys are repository names, each holding entries by name, such as `tasks`, `projects` and `task-rules`, whose values are paths on the user's disk. (…) a file that points to such a place names its entry in the locations file.”; *Verification*: „a file the repository tracks says "the entry `tasks` under `the-way`" where it means a place on the user's disk” — zmiana (pytanie 7): „entries by name” → klucze, „names its entry” → nazywa swój klucz, przykład zgodności „the key `tasks` under `the-way`”; znaczenie bez zmian.
- **WAY-107** — „a place on the user's disk outside every repository standing there as an entry of the locations file of WAY-320, never as a path (…) the section names, beside the place of the tasks, the entry `task-rules` of the locations file under the product's name, whose value is the path of those rules, and where that entry or the file it names is missing, the agent asks the human once and offers to add the entry” — zmiana (pytanie 7): „entry” w tym znaczeniu → „key”; znaczenie bez zmian.
- **WAY-140** — „the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task” — zmiana (pytanie 7): „backlog entry” → linia zadania w backlogu; znaczenie bez zmian.
- **WAY-330** — „the audit reads the register that an entry of the user's locations file names” — zmiana (pytanie 7): „entry” → „key”; znaczenie bez zmian.
- **WAY-27** — *Verification*: „the-way's root `AGENTS.md` names, in `## Backlog`, the entries of the locations file where the place of its tasks and the rules of that place are kept”; zdanie wiążące: „Named by an entry of the locations file, it adds no path to a public source” — zmiana (pytanie 7): „entry” / „entries” w tym znaczeniu → „key” / „keys”; znaczenie bez zmian; WAY-27 i WAY-320 zmienia też zadanie „the way: dziennik decyzji po przeglądzie fundamentu 2026-11-14” (zob. *Context*).

## Settlements to record

Candidates: 6 shown, 6 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | „gate” w the way znaczy tylko polecenie testów; zatwierdzenie definicji projektu przez człowieka nazywa się „readiness approval”, a sekcja, w której się je zapisuje, „approval record”. | glossary term | *Questions to settle*: „Które znaczenie „gate” zmienia nazwę i na jaką?” (wybór człowieka) | które znaczenie przemianować i na jakie słowo, i co wpisać w *Not* hasła „gate” |
| 2 | „projected entry” to brzmienie, w sekcji „Projected foundation changes” definicji projektu, wpisu albo zmiany wpisu, które fundament ma przyjąć, gdy kod zadania uczyni je prawdziwym; jeden wpis obejmuje wszystkie rodzaje, a „entry” zostaje bez zmian. | glossary term | *Questions to settle*: pytania 2 i 6 (wybór człowieka) | przez jaki rodzaj nadrzędny zdefiniować termin, czy poszerzyć „entry” i czy pisać osobne wpisy dla „projected decision” i pozostałych |
| 3 | Status definicji gotowej do zatwierdzenia to `awaiting approval`. | data or code: `project-level/definition_template.md` i `project-level/readiness_check.py` | *Questions to settle*: pytanie 4 (wybór człowieka) | nową wartość statusu, z ryzykiem wzięcia zajętego już `ready for approval` |
| 4 | Niezmiennik `project-readiness-gate` nosi identyfikator `project-readiness-check`. | invariant | *Questions to settle*: pytanie 5 (wybór człowieka) | nowy identyfikator niezmiennika |
| 5 | Nazwa w pliku lokalizacji, pod którą stoi ścieżka, to „key” („the key `tasks` under `the-way`”), nie „entry”. | sentence of WAY-320 | *Questions to settle*: pytanie 7 (wybór człowieka) | słowo dla klucza pliku lokalizacji, z ryzykiem zostawienia „entry” w zdaniu wiążącym i w *Verification* WAY-320 albo wzięcia „location” |
| 6 | Zapis zadania w backlogu to linia zadania („the task's line in the backlog”), nie „backlog entry”. | sentence of WAY-140 | *Questions to settle*: pytanie 7 (wybór człowieka) | czy przemianować „backlog entry” i na jakie słowo |

## Out of scope

- Teksty po polsku — notatki Mariusza, polskie pliki produktów; reguły słownika ich nie obejmują (WAY-99).
- Pliki repozytorium loop2, w tym jego kopie punktów wejścia skilli, zapisy `.runs/` i sekcja `## Backlog` jego `AGENTS.md`, oraz nagłówki dwóch zatwierdzonych definicji loop2; zmienia je loop2 przy przesunięciu przypiętej wersji the-way, osobnym zadaniem w backlogu loop2.