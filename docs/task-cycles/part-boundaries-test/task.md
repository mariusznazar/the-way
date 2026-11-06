---
title: "the way: produkt pilnuje dozwolonych zależności między częściami niezmiennikiem z testem"
status: draft
created: 2026-11-06T00:10
updated: 2026-11-06
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: produkt pilnuje dozwolonych zależności między częściami niezmiennikiem z testem

Status: ready for cycle
Project relation: independent

## Description

### Need

- Mapa części produktu zapisuje przy każdej części, od których części wolno jej zależeć (*Depends on*), ale żaden mechanizm the way nie sprawdza, czy kod się tego trzyma.
- Dziś porównuje to tylko agent w kroku zwrotnym cyklu zadania (WAY-11), czyli w kroku na końcu cyklu, w którym agent zestawia mapę części dotkniętych części z kodem; import zza granicy musi zauważyć sam.
- W loop2 (stan `18fca47`, skan importów 2026-11-06) test symulacji `tests/sim/encounters.test.mjs:18-19` importuje dwa pliki widoku, choć mapa daje symulacji `Depends on: none`; import wszedł 2026-10-29 z PR-em #38 i przeszedł przez 18 kolejnych scaleń bez uwagi kroku zwrotnego i przeglądu; 11 z nich zmieniało pliki symulacji, a 4 (#39, #40, #42, #52) sam ten plik testu.
- Kod gry w `src/` loop2 trzyma się mapy; naruszenia stoją w testach.
- Szablon mapy części nie mówi, do której części należy plik pomocniczy wspólny dla testów kilku części: w loop2 30 testów niezmienników symulacji i widoku importuje `tests/invariants/loop2_invariant_support.py`, który mapa daje części `build-tools`, więc według mapy to 30 naruszeń.
- Odczuwa to agent kroku zwrotnego i przeglądu, a przez niego Mariusz, gdy części produktu zaczną się splatać; przeniesienie cyklu zadania na tańsze modele jest bez mechanicznej bramki ryzykowniejsze.

### To do

1. Sekcja „Allowed dependencies” szablonu mapy części (`elements/part-map/template.md:84`) mówi, że każdy produkt, którego części importują kod z innych części, ma jeden niezmiennik z testem w swoim zestawie testów (wiersz 1 *Settlements to record*): kiedy go zakłada, że import z testu do części pomocników testów jest dozwolony i że import objęty niezmiennikiem „część X nie zależy od Y” oznaczonym jako naruszony go nie łamie. Akapit `elements/part-map/template.md:90-94` o zapisywaniu zaakceptowanej zależności zostaje i odsyła do tej reguły.
2. Sekcja „Assigning files” szablonu mapy części mówi, że pliki obsługujące testy kilku części tworzą osobną część, którą zdanie części tak opisuje, bez nowego pola we wpisie (wiersz 2).
3. The way dostaje test niezmiennika z wiersza 3, który czyta importy Pythona, także te przez dopisanie katalogu do `sys.path`, a wpis niezmiennika staje się przykładem w `elements/invariants/examples.md`.

### Acceptance criteria

- Test z pozycji 3 przechodzi na dzisiejszym kodzie the way, w którym jedyna znana zależność między częściami przez import (`project-level` → `relation-model`) jest dozwolona.

### Questions to settle

- Gdzie mieszka sprawdzenie, że części importują tylko z części dozwolonych w mapie?
  - Answer: B. W produkcie, jako jeden niezmiennik z testem, który czyta mapę części i importy we własnych językach produktu; the way zapisuje w szablonie mapy części, że produkt tak pilnuje dozwolonych zależności. Test w loop2 robi osobne zadanie loop2, po scaleniu tego.
  - Not chosen:
    - A. Ogólny skrypt the way, który czyta wynik polecenia zadeklarowanego przez produkt (graf importów) — kontrakt polecenia, który the way utrzymuje wobec każdego produktu, projektowany przy jednym konsumencie; do zamknięcia dwie dziury z 2026-09-18 (puste wyjście nieodróżnialne od braku zależności, polecenie podane napisem działa inaczej na Windowsie i Linuksie); największa praca z trzech.
    - C. Zostawić jak jest — granicy pilnuje agent kroku zwrotnego; dziś nic nie kosztuje, ale naruszenie w teście symulacji loop2 zostaje, a następne przejdą tak samo.
  - Source: Mariusz, 2026-11-06: „no to chyba B faktycznie”, na pytanie, który wariant (A, B czy C); podział na zadanie the way i zadanie loop2 — Mariusz, 2026-11-06: „no w tej sesji refinujemy zadanie the way, a zadanie dla loop dodajemy, żeby nie uciekło”.
- Czy niezmiennik granic jest obowiązkiem każdego produktu, którego części importują kod z innych części, czy zaleceniem szablonu?
  - Answer: a) Obowiązek. Każdy produkt, którego części importują kod z innych części, ma ten niezmiennik i test; zakłada je, gdy w mapie pojawia się druga część z takim kodem, a produkt już działający — osobnym zadaniem, jak loop2. To nowa reguła wiążąca produkty, więc wchodzi decyzją w dzienniku the way.
  - Not chosen:
    - b) Zalecenie szablonu, o którego zastosowaniu decyduje człowiek przy produkcie — najmniejsza zmiana, ale nic go nie wymusza, więc w następnym produkcie agent najpewniej go pominie i wraca sytuacja z loop2 (naruszenie przez 18 scaleń).
    - c) Szablon bez zmian, sam test w loop2 — koszt jak b), bez śladu w szablonie.
  - Source: Mariusz, 2026-11-06: „a”, na pytanie: obowiązek (a), zalecenie (b) czy bez zmiany szablonu (c).
- Jak szablon mapy części traktuje plik pomocniczy wspólny dla testów kilku części?
  - Answer: a) Pliki, które obsługują testy kilku części, tworzą osobną część; testy każdej części mogą z niej importować, kod, który testem nie jest — nie. Wchodzi to dopiskiem w WAY-44, na który Mariusz się zgodził tą odpowiedzią. Jak test produktu rozpoznaje plik testu, rozstrzyga cykl zadania produktu.
  - Not chosen:
    - b) Pomocnik zostaje w swojej części, a części, których testy go używają, dopisują ją do *Depends on* — zero zmian w the way, ale dopisek pozwala importować tę część także kodowi, który testem nie jest; reguła luzuje się dla całej części, żeby przepuścić testy.
    - c) Importów z testów nie sprawdzać — najprostszy test, ale znika jedyne prawdziwe znalezisko (test symulacji loop2 sięgający do widoku).
  - Source: Mariusz, 2026-11-06: „a”, na pytanie „a, b czy c? Jeśli a, to czy zgadzasz się na dopisek w WAY-44?”, przy wariancie a opisanym jako zmiana zatwierdzonej decyzji, na którą odpowiedź byłaby zgodą. Na pytanie, czy wybór zostaje wobec *Rejected* WAY-44 („tests as a part of their own — a test change stops counting against what it tests”), z oceną, że pomocnik w `build-tools` ma tę słabość już dziś, a pomocnik niczego nie testuje — Mariusz, 2026-11-06: „ok”. Miejsca: `C:\Storage\repos\loop2\foundations\part_map.md` (`tests/invariants/loop2_invariant_support.py` w części `build-tools`, `simulation` z `Depends on: none`) @ `18fca47`; WAY-44 w `foundations/decisions.md:1070` @ `3177e10`.
- Czy the way pisze taki niezmiennik i test dla siebie?
  - Answer: a) Tak, w tym zadaniu: the way dostaje niezmiennik granic i test na importy Pythona, także te przez dopisanie katalogu do `sys.path`; wpis i test służą produktom za przykład.
  - Not chosen:
    - b) Osobnym zadaniem the way — to zadanie zostaje bez kodu, ale do scalenia tamtego the way łamie własną regułę, a produkty nie mają przykładu.
    - c) Decyzja zwalniająca the way z obowiązku (jedna dozwolona zależność przez import, pozostałe zależności biegną przez teksty skilli) — proces nie stosuje własnej reguły, a przykład trzeba brać skądinąd.
  - Source: Mariusz, 2026-11-06: „a”, na pytanie „a, b czy c?” (pytanie o pisanie przez the way niezmiennika i testu dla siebie). Miejsca: `project-level/readiness_check.py:45` (`sys.path.insert(0, os.path.join(HERE, "..", "relation-model"))`), `elements/invariants/examples.md` — stan `foundations` @ `3177e10`.
- Jak jeden niezmiennik granic na produkt współistnieje z zależnością, którą człowiek zaakceptował, choć mapa jej nie dopuszcza, skoro szablon zapisuje taką zależność jako osobny niezmiennik „część X nie zależy od Y” oznaczony jako naruszony, a WAY-51 każe oznaczyć jako naruszony każdy niezmiennik, którego produkt dziś nie spełnia?
  - Answer: a) Zdanie wspólnego niezmiennika dopuszcza import z części, od której niezmiennik „część X nie zależy od Y”, oznaczony jako naruszony, mówi, że część X dziś zależy. Każda zaakceptowana zależność stoi dalej jako osobny niezmiennik ze swoim testem jako spodziewaną porażką, a wspólny niezmiennik przechodzi i pilnuje reszty. Decyzja z wiersza 1 mówi wprost, dlaczego to nie jest lista znanych naruszeń: każda para jest pełnym wpisem fundamentu, który zaakceptował człowiek, a nie spisem obok wpisów.
  - Not chosen:
    - b) Jeden niezmiennik na każdą część z kodem — zaakceptowana zależność wyłącza bramkę dla całej swojej części; w loop2 od razu dla symulacji, a wpisów jest kilka zamiast jednego.
    - c) Jak dziś stanowi WAY-51 — jedna zaakceptowana zależność oznacza wspólny niezmiennik jako naruszony i wyłącza bramkę w całym produkcie, dopóki ktoś jej nie poprawi.
  - Source: Mariusz, 2026-11-06: „tak jak rekomendujesz”, na pytanie „Pytanie 6: a, b czy c?”, przy wariancie a, którego słabość nazwano: test czyta plik niezmienników i recenzent może wziąć to za zakazaną listę naruszeń. Miejsca: `elements/part-map/template.md:90-94`, WAY-51 (`foundations/decisions.md:1184`), WAY-40 *Verification* — stan `foundations` @ `3177e10`.
- Jak mapa części wskazuje część pomocników testów?
  - Answer: Bez nowego pola we wpisie części: zdanie części mówi, czym ona jest, a test produktu wskazuje ją po identyfikatorze.
  - Not chosen:
    - Nowe pole albo znacznik we wpisie części — zmienia formę mapy we wszystkich produktach, choć dziś nic tego nie wymaga; przydałoby się dopiero ogólnemu skryptowi the way (wariant A).
  - Source: Mariusz, 2026-11-06: „tak jak rekomendujesz”, na pytanie „Pytanie 7: zgadzasz się bez nowego pola?”. Miejsce: forma wpisu części, `elements/part-map/template.md:38-47` @ `3177e10`.
- Czy to zadanie czeka na własne wytyczne kodowania i testów the way, skoro pisze kod i test w the way, w którym nie ma katalogu `guidelines/`, a WAY-215 trzyma takie zadanie w doprecyzowaniu do scalenia osobnego zadania o wytycznych?
  - Answer: Nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a rozjazd reguły z praktyką zostaje w zadaniu [[wlasne_wytyczne_the_way]].
  - Not chosen:
    - Czekać na zadanie o wytycznych — to zadanie i czekające na nie zadanie loop2 stoją za zadaniem bez wybranego kierunku, a naruszenie w teście symulacji loop2 zostaje do tego czasu.
  - Source: Mariusz, 2026-11-06: „nie czeka”. Miejsca: WAY-215 w `foundations/decisions.md` @ `3177e10`; to samo rozstrzygnięcie przy [[zadanie_the_way_logowanie_w_sekcji_decyzji]] (Mariusz, 2026-11-05: „tak jak dotychczas”).

## Context

- Obecna reguła szablonu (`elements/part-map/template.md:86-94` @ `3177e10`): „*Depends on* names the parts this part may depend on, not those its code reaches for today: the map holds the rule, and the code shows the state (WAY-225). The return step of a change compares the two for the parts the change touches (WAY-11). A dependency the code holds that *Depends on* does not allow goes to the human. Where the human accepts it as it stands, it is written as an invariant — "the part `<part>` does not depend on `<part>`" — that reads `Violated: yes`, its test standing as an expected failure until the code meets it […]; *Depends on* is never rewritten to fit what the code reaches for today (WAY-225, WAY-51). The map holds no list of such dependencies.”
- We wrześniu, przy budowie mapy części, sprawdzenie zaprojektowano jako skrypt the way czytający graf importów z polecenia produktu, z osobną listą znanych naruszeń (ustalenia R5 i R6 w `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\budowa_mapy_czesci.md:130`).
- 2026-09-18 odłożono je do chwili, gdy pierwszy produkt spoza the way przypnie commit albo gdy w the way pojawi się zależność między częściami, której mapa nie dopuszcza (wpis w tej samej notatce, linia 312).
- Listę znanych naruszeń zastąpiły od tego czasu WAY-40, WAY-51 i WAY-225.
- Inspiracją jest repozytorium gon-stack (https://github.com/polubis/gon-stack), w którym tanie modele pracują za bramką mechanicznych sprawdzeń uruchamianych przed commitem (przegląd Mariusza z 2026-11-05, zapisany w pierwszej wersji tej notatki).
- Istniejący wzór testu granicy jednej części: `C:\Storage\repos\loop2\tests\invariants\test_simulation_isolation.py` (niezmiennik simulation-isolation); czyta tylko `src/browser/sim/`, więc nie widzi importu w `tests/sim/`.
- Jednorazowy skan importów z 2026-11-06 przypisuje pliki do części przez `git check-attr`, jak `elements/common/foundation_check.py`, i czyta importy TypeScriptu, JavaScriptu i Pythona oraz odwołania w HTML i CSS: `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\af8f51b4-24bb-448e-a3bc-656f1857231a\scratchpad\boundary_scan.py` (plik tymczasowy, poza repo).
- W the way ten sam skan nie znalazł żadnego importu między częściami; jedyny znany (`project-level/readiness_check.py` sięga do `relation-model/` przez `sys.path`) skan przeoczył, a zależności między częściami the way biegną głównie przez odwołania w tekstach skilli i szablonów, nie przez importy.
- Notatka powiązanego zadania loop2: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Loop\_zadania\zadanie_loop2_test_granic_czesci.md`.
- Przykład z the way pokazuje tylko importy Pythona; trudniejszych przypadków loop2 (ścieżki `../../dist/...` wskazujące na pliki z `src/`, odróżnianie pliku testu od pomocnika) nie pokazuje.
- Test the way, który przypisuje pliki do części przez import `elements/common/foundation_check.py`, sam podlega niezmiennikowi: w części o wąskim *Depends on* (np. `gate`, `Depends on: none`) złamałby go.

## Questions carried to cycle

- Czy uruchomienie skryptu innej części (`runpy.run_path`, nowy proces) liczy się jako import w rozumieniu niezmiennika z wiersza 3; dziś robią to `relation-model/test_fingerprint.py:108` i `project-level/test_plan_state_subprocesses_invariant.py:82`, oba w obrębie własnej części.

## Human actions

none

## Decisions in play

- WAY-225: „What can be derived from what the product executes — code, configuration, infrastructure as code, runtime traces — is derived, never written by hand, and what is derived describes the state. Rules are written by hand: what is allowed and what the product promises, which the code cannot show, and a dependency the code holds that the part map does not allow is recorded as an invariant the product does not meet (WAY-51), never by rewriting the allowed dependencies to fit the code.”
- WAY-51: „On the main branch an invariant the product does not meet today stays whole and is marked violated at its entry; an invariant is marked violated only by a change of the foundation that a human accepts, never by a step of implementation. A change that sets or clears the mark names it in its request; the test of a marked invariant stands in the product's suite marked as an expected failure in the product's test tool, and the change in which it starts to pass removes that marking and the mark of the invariant. […]”
- WAY-40: „The part map holds two kinds of entry: a part and a surface. An allowed dependency and a trust boundary are fields of the part they belong to, so neither is an entry of its own, and a critical flow has no entry (WAY-45). […]” — w *Verification* jako naruszenie: „the map holds […] a list of known violations of its allowed dependencies”.
- WAY-44: „Every file git tracks belongs to exactly one part of the map, by path patterns that git itself matches […]. Tests belong to the part they test and generated files to the part of their generator; the files that serve the whole repository — the lockfile and the build configuration — are a part of their own, and the files that only direct whoever carries out its tasks […] are another. […]”
- WAY-38: „Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.” — w *Rejected*: „the scripts parsing other languages themselves — tools that tried gave it up (cargo-semver-checks)”.
- WAY-11: „A task ends with its return step before its branch is merged: an agent compares with the code the foundation entries the change writes or changes, those its task names and those the search of the foundation found, and the part map of the parts the task touched, and corrects in the same change whatever no longer matches. […]”
- WAY-28: „When the process enters a product that already exists, the existing state is its starting point and needs no justification, and the rules apply to changes from then on. The part map comes first; the invariants of the critical flows, each naming in *Part* the parts its flow runs through, are then recovered from what the product does — an agent lists what a part does, and a human chooses which of it the product must keep — and the other invariants come through the return step of tasks. Decisions are recovered only when a task touches the parts they govern.”
- WAY-62: „An invariant entry names the parts of the part map where a change can make its sentence false, or `every` where a change to any part can. A change, against the commit its branch left the main branch from, reaches an invariant that names `every` or a part the change touches, or that a test the change alters cites, whatever parts a file collecting entries gives that change (WAY-44), and the agent making the change reads every invariant it reaches. The entry names no critical flow or surface.”
- WAY-65: „A test cites, at the test that checks it, each invariant it checks as `invariant: <identifier>`. A file is an invariant test of a change when it cites an invariant on the commit the branch left the main branch from or on the commit being checked.”
- WAY-215: „Unless a departure under WAY-217 applies, a task changing a user interface with no styleguide, writing code in a product with no general coding guidelines or writing or changing a test in a product with no testing guidelines, whether or not the product already has screens, code or tests, stays in refinement as `waiting for human` with a *Questions to settle* question awaiting the merge of a separate guidelines task […]” — to zadanie od tego odchodzi decyzją Mariusza pod *Questions to settle*, a request nazywa to odejście.
- WAY-16: „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”

## Settlements to record

Candidates: 5 shown, 3 accepted — 2026-11-06

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Każdy produkt, którego części importują kod z innych części, ma jeden niezmiennik z testem w swoim zestawie testów — plik części importuje tylko pliki części, które *Depends on* tej części dopuszcza, części pomocników testów, gdy jest testem, i części, od której niezmiennik „część X nie zależy od Y” oznaczony jako naruszony mówi, że część X dziś zależy — zakładany, gdy w mapie pojawia się druga część z takim kodem, a w produkcie już działającym osobnym zadaniem; taki oznaczony niezmiennik jest pełnym wpisem zaakceptowanym przez człowieka, a nie listą znanych naruszeń. | decision | odpowiedzi na pytania 1 (B), 2 (a) i o współistnieniu z zaakceptowaną zależnością (a) pod *Questions to settle*, z ich *Not chosen* | czy obowiązek wchodzi samym zdaniem szablonu, czy decyzją; kiedy produkt ma założyć niezmiennik; co robi wspólny niezmiennik, gdy człowiek zaakceptuje zależność spoza mapy; które warianty trafiają do *Rejected* (skrypt the way, zalecenie, brak zmiany, niezmiennik na część, bramka wyłączona w całości) |
| 2 | Pliki, które obsługują testy kilku części, tworzą osobną część, którą zdanie części tak opisuje, bez nowego pola we wpisie; testy każdej części mogą z niej importować, a kod, który testem nie jest — nie; wchodzi dopiskiem w WAY-44. | decision | odpowiedzi na pytanie 3 (a), z jej *Not chosen* i pytaniem kontrolnym wobec *Rejected* WAY-44, oraz na pytanie o wskazanie części pomocników testów pod *Questions to settle* | czy import z testu do takiej części jest zależnością, którą trzeba wpisać w *Depends on* |
| 3 | W the way żaden plik części nie importuje pliku części, której *Depends on* tej części nie dopuszcza, z wyjątkiem importu z testu do części pomocników testów i importu objętego niezmiennikiem „część X nie zależy od Y” oznaczonym jako naruszony. | invariant | odpowiedzi na pytanie 4 (a) i o współistnieniu z zaakceptowaną zależnością (a) pod *Questions to settle* | zdanie niezmiennika i czy obejmuje importy przez dopisanie katalogu do `sys.path` |

## Out of scope

- Niezmiennik i test granic w loop2 oraz rozstrzygnięcie jego obecnych naruszeń — robi je zadanie [[zadanie_loop2_test_granic_czesci]].
