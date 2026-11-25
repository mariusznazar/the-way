---
title: "the way: drobne poprawki z przeglądu warstwy AI, zbierane od 24.11 — opis prośby o scalenie poprawiany fragmentem i powiązanie niezmiennika z decyzją, z której wynika"
status: draft
created: 2026-11-24T00:00
updated: 2026-11-25
tags: [zadanie]
related: "the project note in the author's notes"
---

# the way: drobne poprawki z przeglądu warstwy AI, zbierane od 24.11 — opis prośby o scalenie poprawiany fragmentem i powiązanie niezmiennika z decyzją, z której wynika

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/117 · https://github.com/mariusznazar/the-way/pull/136

## Description

### Need

- Zadanie zbiorcze: każdy punkt *To do* to jedna sprawa przyjęta w dziennym przeglądzie warstwy AI (`/ai-review`), z jej numerem jako źródłem; wdrażamy je jednym cyklem zamiast wielu.
- AIR-720: agent prowadzący cykl zadania pisze opis prośby o scalenie, potem dopisuje do niego SHA zapisu cyklu i wyniki sprawdzeń, zwykle skryptem albo `sed -i`, a przy kolejnej poprawce przepisuje cały plik od nowa.
- Narzędzie zapisu odmawia, bo plik zmienił się poza nim, więc agent czyta go ponownie i pisze wszystko drugi raz — do 44 tys. znaków za każdym razem.
- Płaci za to Mariusz: każde ponowne przepisanie idzie z limitu, z którego pracuje; działo się to w kilkudziesięciu sesjach w dwa tygodnie, głównie w cyklach loop2.
- Bez zmiany opisy dalej powstają poprawnie, tracone są tylko tokeny i minuta–dwie na każde wystąpienie.
- AIR-718: każda decyzja the-way ma wymieniać w *Verification* niezmienniki, które z niej wynikają (WAY-12), żeby ten, kto ją zmienia, wiedział, co jeszcze ruszy; gdy cykl dopisuje nowy niezmiennik do istniejącej decyzji, nikt nie dopisuje go do decyzji i żaden skrypt tego nie sprawdza.
- W samym the-way brakuje już 15 takich powiązań; lukę łapią ręcznie recenzenci, kosztem rundy poprawek, albo nie łapie nikt, a Mariusz, zmieniając decyzję, nie widzi reguły i testu, które na niej stoją.

### To do

Miejsca wskazuje nagłówek albo cytat; numer linii to podpowiedź według `origin/foundations` @ `07aa55df`.

1. **Opis prośby o scalenie poprawiany fragmentem (AIR-720).** `task-cycle/skill/request_template.md`, punkt 6 („Publish the file that passed…”, ok. :45-51), na jego końcu, po zdaniu kończącym się „…in the record's *Request handoff* (*Description*).” (pytanie 4) — dopisek, przyjęty przez Mariusza słowo w słowo:
   > „Make each later edit as an edit of the part that changes, not a rewrite of the whole file. Where a script or a command has changed `request.md` since your harness last read it, read the file again before you edit it — your harness can refuse a write to a file changed outside it.”
2. **Krok 4.4 skilla niezmienników (AIR-718).** `elements/invariants/skill/write.md`, punkt zaczynający się od „Step 4.4:” (ok. :5-6):
   - jest: „Step 4.4: what follows from this entry is a decision whose level 1 verification gains, loses or renames it, through `record-decision`.”
   - będzie: „Step 4.4: each decision the entry's *Derives from* names gains the entry's identifier in its *Verification*, after `invariants:` (WAY-12) — or loses or renames it where the entry is withdrawn or renamed — through `record-decision`.”
3. **Kontrola powiązania w skrypcie (AIR-718).** `elements/common/foundation_check.py`: niezmiennik, którego *Derives from* wymienia decyzję, a *Verification* tej decyzji go nie wymienia, jest błędem, gdy zmiana dodaje albo zmienia którykolwiek z dwóch wpisów — niezmiennik albo decyzję, w dowolnym miejscu wpisu (pytanie 2); poza tym jest linią `listed:`, która niczego nie zatrzymuje (jak decyzja niczym nietrzymana z WAY-12). Komunikat błędu podaje, który identyfikator niezmiennika dopisać do *Verification* której decyzji, po `invariants:`. Opis skryptu (docstring) dostaje ten punkt; testy obu przypadków w `elements/common/test_foundation_check.py`.
4. **15 brakujących powiązań (AIR-718).** W tej samej zmianie *Verification* decyzji dostaje po `invariants:` identyfikatory niezmienników, które ją wymieniają w *Derives from*:
   - WAY-48: `audit-count-refuses-record-links`, `check-instructions-refuses-outside-links`, `cycle-measures-refuses-nested-line`, `cycle-stages-refuses-crafted-names`, `gate-times-refuses-impossible-entry`, `installation-paths-through-links`, `readiness-check-refuses-non-utf-8`;
   - WAY-235: te same siedem;
   - WAY-368: `installation-paths-through-links`.
5. **Drugie zdanie z „level 1 verification” (AIR-718, pytanie 3).** `elements/invariants/skill/decide_entry.md`, punkt zaczynający się od „The search of the foundation also looks for a decision whose level 1 verification calls for this rule” (ok. :19-21): początek zdania dostaje brzmienie „The search of the foundation also looks for each decision this rule derives from, which its *Derives from* names, and an entry it names whose binding part has changed, …”; reszta zdania bez zmian.

### Acceptance criteria

- `python -B elements/common/foundation_check.py` uruchomione na the-way po zmianie nie podaje żadnego brakującego powiązania niezmiennika z decyzją — ani jako błędu, ani jako linii `listed:`.

### Questions to settle

- 1\. Czy dopisanie samego powiązania niezmiennika do *Verification* istniejącej decyzji wymaga zgody człowieka przed kodem, tak jak zmiana decyzji, której potrzebuje zadanie (WAY-30)?
  - Answer: nie — Mariusz przyjmuje takie powiązanie przy scaleniu, razem z listą wpisów prośby (WAY-114); WAY-30 dostaje nowy akapit, który mówi to wprost (wiersz 1 *Settlements to record*).
  - Not chosen:
    - zgoda przy scaleniu bez zmiany tekstu — zostawia rozbieżność, na której cykle stają albo rozstrzygają każdy po swojemu;
    - zgoda przed kodem, jak przy każdej zmianie decyzji — cykl bez planu staje przy każdej nowej regule z istniejącej decyzji, dla jednej mechanicznej linii.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „pytanie 1 — a. Wpis w Verification nie zmienia tego, czego decyzja wymaga, Mariusz widzi go przy scaleniu na liście wpisów prośby, a b zostawia rozbieżność, na której cykle stają albo rozstrzygają każdy po swojemu (the way: lepiej i szybciej, nic gorzej). Wycofanie tanie.”; tekst pytania: WAY-30, `foundations/decisions.md:1275` @ `07aa55df` — „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made”; `elements/decisions/template.md:215-218` @ `07aa55df` — „A change to a decision edits its entry in place: the binding sentences, the fields, *Rationale* and *Rejected* describe the decision as it then stands” oraz „A human accepts the changed meaning by merging the request that carries the change (WAY-14)”; recenzent cyklu `installer-foundation-check-full-path` (PR #158) odczytał, że zgody nie wymaga („my reading is no”).
- 2\. Kiedy brak powiązania jest błędem: „zmiana dodaje albo zmienia którąkolwiek ze stron powiązania” (punkt 3 *To do*) — czy stroną jest pole, które niesie powiązanie (*Derives from* niezmiennika, *Verification* decyzji), czy cały wpis niezmiennika albo decyzji?
  - Answer: cały wpis — każda zmiana niezmiennika albo decyzji, nie tylko pola z powiązaniem, i każdy wpis dodany w zmianie; komunikat błędu podaje, który identyfikator dopisać do *Verification* której decyzji, żeby domknięcie przy okazji było mechaniczne.
  - Not chosen:
    - stroną jest pole z powiązaniem — zostawia lukę właśnie tam, gdzie ktoś zmienia decyzję i powinien widzieć, co na niej stoi.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „pytanie 2 — b, strona to cały wpis. Cel sprawy to widzieć przy zmianie, co stoi na decyzji, a a zostawia lukę właśnie tam; dopisanie kilku linii to mały koszt, a przyczyna znika u źródła razem ze skutkami (zasada: przyczyna i objaw). Dopilnuj w punkcie 3, żeby komunikat błędu podawał dokładnie, którą linię gdzie dopisać — wtedy domknięcie przy okazji jest mechaniczne.”; tekst pytania: punkt 3 *To do*, brzmienie z notatki zadania z 24.11.
- 3\. Czy zadanie zmienia też zdanie z „level 1 verification” w `elements/invariants/skill/decide_entry.md`, które Context podaje jako źródło błędnego odczytania kroku 4.4?
  - Answer: tak — punkt 5 *To do*.
  - Not chosen:
    - zostawić zdanie — zostaje ostatni egzemplarz martwego słownictwa, które wprowadziło autora w błąd, i błąd wróci.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „1: to ta sama przyczyna, którą zadanie usuwa — ostatni egzemplarz martwego słownictwa, które wprowadziło w błąd; zostawiony wróci (przyczyna i skutki razem); zakaz dopisywania punktów chroni przed rozrostem zakresu, nie przed domknięciem tej samej sprawy.”; tekst: `elements/invariants/skill/decide_entry.md:19-21` @ `07aa55df`; WAY-12 *Rejected*, `foundations/decisions.md:817-819` @ `07aa55df` — „a level of verification named in every decision”.
- 4\. Gdzie w punkcie 6 `request_template.md` staje dopisek z punktu 1 *To do*?
  - Answer: na końcu punktu 6, po „(*Description*).”; brzmienie bez zmian.
  - Not chosen:
    - po zdaniu kończącym się „…which did not exist when the description was first written.” (miejsce z notatki z 24.11) — rozdziela „Record the last run of each” od „the three checks”, do których odnosi się „each”.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-25: „2: brzmienie bez zmian, inne miejsce usuwa dwuznaczność za darmo.”; tekst: `task-cycle/skill/request_template.md:45-51` @ `07aa55df`.

## Context

- Źródła spraw: AIR-720 i AIR-718 z dziennego przeglądu warstwy AI z 24.11; zadanie jest otwartą listą — kolejne drobne poprawki the-way z `/ai-review` dopisuje się tu jako następne punkty, dopóki Mariusz nie uzna listy za zamkniętą.
- AIR-720: błąd narzędzia Write „File has been modified since read, either by the user or by a linter” na `request.md` wystąpił w 28 sesjach Claude Code między 6.11 a 21.11 (pomiar przeglądu z 24.11; nocny skan wzorców podał 32 sesje z 17 nocy).
- W każdym sprawdzonym przypadku między odczytem a zapisem stało polecenie powłoki zmieniające `request.md` — skrypt Pythona z podmianą tekstu albo `sed -i` — zwykle po to, by wpisać SHA commitu dodającego zapis cyklu.
- W sesji loop2 `01bcd8a7-d745-4cdb-bed0-63bd0d8858f8` odrzucony zapis miał 43 608 znaków, a ponowny 43 615 (transkrypt, linie 7034 i 7054).
- Ani `task-cycle/skill/SKILL.md` (krok 12), ani `request_template.md` nie mówią, czym edytować opis; żaden skrypt the-way nie zapisuje `request.md` — `task-cycle/request_check.py` i `task-cycle/private_paths_check.py` tylko go czytają.
- AIR-720, sprawdzone i odrzucone przy przyjmowaniu brzmienia: zakaz edycji skryptem (zderzyłby się z ewentualnym skryptem the-way wpisującym SHA i nie usuwa głównego kosztu, czyli przepisywania całości); „na pliku przeczytanym tuż przed edycją” (popycha do pełnego odczytu 20–40 KB przed każdą edycją, a narzędziu wystarcza dowolny odczyt po zmianie z zewnątrz); powód jako pewnik „is refused” (to zachowanie Claude Code, a the-way obsługuje różne narzędzia, stąd „can refuse”).
- AIR-720, sonda po wdrożeniu: zero błędów „File has been modified since read” na `request.md` w kolejnych oknach nocnego skanu wzorców.
- AIR-718, skąd: cykl `installer-foundation-check-full-path` (PR #158; `the-way@b92b77a:docs/task-cycles/installer-foundation-check-full-path/cycle.md`, linie 51–57 i 108–117; raport `reports/review-whole-report.md:21-49`) — autor zostawił WAY-418 bez nowego niezmiennika `installation-agents-md-warnings`, czytając krok 4.4 przez zdanie z `elements/invariants/skill/decide_entry.md` („a decision whose level 1 verification calls for this rule”, ok. :19-21); lukę złapał przegląd całej zmiany (uwaga Important), poprawka kosztowała rundę.
- 15 brakujących powiązań weszło w commitach `474df779` (14.11, PR #117) i `e1586a41` (15.11, PR #136) i przeszło przegląd; WAY-12 stoi od 21.10, krok 4.4 od 29.10 — sam tekst reguły nie zadziałał, stąd kontrola w skrypcie. Liczba 15 sprawdzona ponownie 25.11 na `07aa55df`.
- W loop2 przegląd zmierzył 2 takie luki (D-13 bez `tracked-file-private-names`, D-22 bez `instrument-game-agreement`); po podbiciu the-way w loop2 kontrola pokaże je jako linie `listed:`.
- AIR-718, sprawdzone i odrzucone: sam punkt 2, bez kontroli w skrypcie — sam tekst reguły już nie zadziałał.
- Dziś *Verification* WAY-48, WAY-235 i WAY-368 ma tylko parę przykładów (`complies:` / `violates:`); WAY-12 dopuszcza parę „only for the part of its sentences that no invariant and no test checks”, a wzór pola z niezmiennikami i parą stoi np. przy decyzji z `invariants: foundation-change-merge-route. For the rest, an agent compares the…` (`foundations/decisions.md`, ok. :439).
- `elements/common/foundation_check.py` ma dziś 1115 linii przy progu 1200 z WAY-385; nowa kontrola stoi obok `check_held` (ok. :742), która sprawdza tylko, czy decyzję cokolwiek trzyma.
- Uwaga z przeglądu, niesprawdzona: `elements/common/test_foundation_check.py` ma wiele przykładów niezmiennika z *Derives from* bez powiązania zwrotnego — część testów może wymagać uzupełnienia przykładów.
- To, co zgłasza `foundation_check.py`, opisują też: akapit „The form of the foundation” w `agent-instructions/README.md` (ok. :13-23), wiersz *Verification* tabeli „who reads it” w `elements/decisions/template.md` (ok. :130) i wiersz *Derives from* takiej tabeli w `elements/invariants/template.md` (ok. :179).
- Akapity WAY-12 (drugi) i WAY-30 mają już po trzy zdania, górną granicę z WAY-05, więc zdania z wierszy 1 i 2 *Settlements to record* stają jako nowe akapity.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-12** — How is a decision checked? (`foundations/decisions.md`, ok. :766) — zadanie dodaje zdanie z wiersza 2 *Settlements to record* (odpowiedź na pytanie 2):
  > A decision names in *Verification* the invariants derived from it, by the identifiers of their entries, where such invariants exist, and the tests that hold its sentences, by a clause that gives the parts of the sentences they hold in words and no path, no test name and no number. A test that holds a sentence of a decision carries beside it a line `decision:` that gives the number of the decision and the start of that sentence, and the decision keeps its rationale and its rejected options whole. A decision may also carry a pair of examples — a change that complies and one that violates — only for the part of its sentences that no invariant and no test checks, with which an agent compares a change with that part; the violating example is a change whose code goes against the decision while its entry stays as it is, never one that replaces the decision together with its code.
  >
  > A decision is held when its *Verification* names an invariant, when a test holds a sentence of it by a line `decision:` that names its number, or when it carries a pair of examples. The check of the foundation reports as an error a decision that a change adds, or whose binding sentences the change alters, and that nothing holds. Any other decision that nothing holds stands in a list the check prints, and the list stops no change.
- **WAY-18** — How is a product's decision log kept? (ok. :824), pierwszy akapit:
  > A product keeps all its decisions in one log, whatever they are about. The log holds one entry for each decision in force and itself says what binds today, with no view generated from it kept in its place; the index of a selection of decisions that an agent writes on demand (WAY-150) is no such view. A link between entries is written at one end only; the one exception is a decision's invariants, which its *Verification* names while each of them names the decision in *Derives from*.
- **WAY-30** — What happens when a change contradicts a decision? (ok. :1273) — zadanie dodaje akapit z wiersza 1 *Settlements to record* (odpowiedź na pytanie 1):
  > A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made; that approval, including a change carried by a row of *Settlements to record*, answers the question WAY-114 requires, so the agent writing the entry asks only about a meaning beyond what the approved plan or task document carries, and in this area this decision prevails over WAY-114. When a contradiction shows only during implementation, the agent stops, quotes the decision by its number, and either brings the change into line, drops the change, or proposes on the task branch an edit of the decision, a new wording or a narrowing, and the code that needs it waits for that human. An exception written in advance into a decision's binding sentences is not a contradiction, and no exception lives only in a task document, plan or cycle record.
- **WAY-114** — What does a human accept of an entry, and when? (ok. :1312), fragment:
  > A human accepts the meaning of a foundation entry while its wording is the agent's: […] and that of every other entry at the merge of the change that holds it […]. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.
- **WAY-48** — How is a trust boundary recorded? (ok. :2616) — zadanie zmienia tylko *Verification* (punkt 4 *To do*):
  > A trust boundary is recorded at the part that holds it, as a pattern of the code files which take in what the product does not control — data from the network, keys, the deployment, files that come from outside the product, such as one on the user's disk — and never at a script that only checks the product's own files. An exchange with the external context records its direction and marks what comes in as untrusted. A change that touches the files of a boundary is checked for crafted input, and its review is aimed at that risk.
- **WAY-235** — How do a product's tests keep its trust boundaries? (ok. :10461) — zadanie zmienia tylko *Verification* (punkt 4 *To do*):
  > The template of the testing discipline requires, and the skill `maintain-testing-guidelines` proposes, for each trust boundary of the product's part map at least one invariant that the boundary refuses crafted input or unauthorised access, checked by a permanent test that checks the refusal directly, takes the expected refusal from the product's decisions on permissions and is seen failing once; a boundary that does not refuse today has that invariant marked violated as WAY-51 gives it, and a boundary that is only the configuration of someone else's service stays with the review of WAY-48. For authorization, the rule of the product's testing guidelines holds a table of who, which resource and which action with the expected result, each row naming the decision on permissions it comes from. In the area of trust boundaries this decision prevails over WAY-168: the *Invariant* of the rule on trust boundaries names the refusal invariant of each boundary, although its test checks the product's behaviour rather than a convention of the product's code.
- **WAY-368** — Which agents run the stages of a task cycle in Claude Code? (ok. :3618) — zadanie zmienia tylko *Verification* (punkt 4 *To do*):
  > In Claude Code, a task cycle dispatches the one author of a change without a plan as an agent of the type `the-way-author` and every other stage agent as an agent of the type `the-way-stage`, two types of the-way's own that give their agent every tool of the session except the skill tool. Each type has a body of its own saying what it is, and only the type of the one author has the prompt cache lifetime that WAY-255 gives that agent. A stage agent reaches each method, and each skill a method names, as a file by its path, never by calling a skill; the installer writes the definitions of the pinned commit into a product, replacing and deleting only its own files, and the copies a session on the-way itself loads are generated from them and tracked.
  >
  > The agent types of a task cycle start with the instruction files that Claude Code loads into an agent of the session, the user's and the product's; no definition of a type sets the field that starts an agent without them.
- **WAY-385** — How large may a function and a file of a script of the-way be? (ok. :11222), fragment:
  > A function of a script of the-way has at most 110 lines, counted with the functions nested in it, and a file of a script has at most 1200 lines, in each part that WAY-379 names, both counted on the code as the formatter of WAY-382 leaves it; a test file stands outside the rule, and no function and no file is kept whole over a threshold as an exception.

## Settlements to record

Candidates: 4 shown, 2 accepted — 2026-11-25

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Dopisanie, usunięcie albo zmiana nazwy niezmiennika w *Verification* decyzji, bez zmiany jej zdań wiążących, nie wymaga zgody przed kodem — Mariusz przyjmuje je przy scaleniu, razem z listą wpisów prośby. | sentence of WAY-30 | pytanie 1 (*Not chosen* tam) | czy przy nowym niezmienniku z istniejącej decyzji zatrzymać cykl z pytaniem do człowieka, czy wpisać sprawę do *Needed from you* prośby |
| 2 | Sprawdzenie fundamentu zgłasza jako błąd niezmiennik, którego *Derives from* wymienia decyzję, a jej *Verification* go nie wymienia, gdy zmiana dodaje albo zmienia którykolwiek z tych dwóch wpisów, i podaje w błędzie, który identyfikator dopisać do której decyzji; każdą inną taką lukę tylko wypisuje. | sentence of WAY-12 | pytanie 2 (*Not chosen* tam) | czy zapisać nową kontrolę tylko w opisie skryptu, bez zdania w WAY-12 obok kontroli decyzji niczym nietrzymanej, i czy błąd ma wskazywać, co dopisać |

## Out of scope

- Skrypt the-way, który sam wpisuje do `request.md` link do zapisu przez SHA i wyniki trzech sprawdzeń — najmocniejszy środek na AIR-720, ale wymaga decyzji o stałych polach w szablonie; odłożony na wypadek, gdyby błąd wrócił po dopisku z punktu 1.
- Dwie luki powiązań w loop2 (D-13, D-22) — to inne repozytorium; zadanie zmienia tylko the-way.
