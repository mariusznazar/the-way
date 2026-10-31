---
title: "the way: krok technologii pyta też, jak długo żyją logi produktu i skąd człowiek dowiaduje się o awarii"
status: draft
created: 2026-10-29T23:48
updated: 2026-10-31
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: krok technologii pyta też, jak długo żyją logi produktu i skąd człowiek dowiaduje się o awarii

Status: ready for cycle
Project relation: independent

## Description

### Need

- Krok technologii the way (skill `settle-technology`, który przed zatwierdzeniem projektu ustala jego technologie) pyta o logi działającego produktu tylko o to, dokąd trafia zapis i jak agent go czyta (`project-level/definition_template.md:176`, WAY-165).
- Nie pyta, jak długo zapis żyje ani skąd człowiek dowiaduje się o awarii.
- Mariusz zgłasza, że w `loop2` odpowiedź brzmi „konsola kontenera, agent czyta ją przez serwer MCP `mikrus`” — formalnie kompletna, a jednak log ginie przy każdym wdrożeniu, bo kontener jest stawiany od nowa, a o awarii Mariusz „dowiaduje się sam”.
- Odbiorcą jest Mariusz, który o awarii produktu dowiaduje się od graczy albo przypadkiem, i agent diagnozujący błąd, który po wdrożeniu nie ma już czego czytać.
- Bez zmiany każdy produkt prowadzony the way dostanie log, który wystarcza do sprawdzenia zmiany tuż po wdrożeniu, ale nie do diagnozy awarii sprzed wdrożenia.
- W `loop2` dziś to nie przeszkadza, bo jedynym graczem jest Mariusz; zacznie przy pierwszych obcych graczach.

### To do

1. Pytanie o logi w kroku technologii — dziś „gdzie trafia zapis tego, co działający produkt robi, i jak agent go czyta” — obejmuje też to, jak długo zapis żyje, także między wdrożeniami.
2. Krok technologii sprawdza, jak człowiek dowiaduje się o awarii, jako osobną pozycję listy wyborów, poza sprawami drogi agenta do działającego produktu (pytanie 1): narzędzie do śledzenia błędów (na przykład Sentry, które samo zbiera wyjątki z produkcji i pokazuje je jako listę), alert albo świadomy brak na początek; brak narzędzia jest pełnoprawną opcją.
3. Przy definicji projektu pozycja awarii trafia na listę, gdy fundament nie ma o niej decyzji, a projekt uruchamia produkt poza maszyną, na której produkt powstaje (pytania 2 i 5).
4. Lista skilla wdrożeniowego z WAY-139 dostaje dwa punkty: jak długo żyją logi, także między wdrożeniami, i skąd człowiek dowiaduje się o awarii; gdy zadanie wdraża produkt albo zmienia, jak lub gdzie działa, a skill tego nie mówi, doprecyzowanie pyta człowieka, czy uruchomić przy tym zadaniu krok technologii z dopiskiem o tych sprawach, a skill dostaje odpowiedź (pytanie 5); gdy człowiek odmówi, zadanie zapisuje w skillu wdrożeniowym, że świadomie nie rozstrzyga tych spraw, i pytanie nie wraca (pytanie 6).
5. Krok rozstrzyga obie sprawy swoim zwykłym mechanizmem, jak każdy inny wybór technologii: świeży agent na wybór, opcje oparte na stronie dokumentacji z wersją, konsekwencje (koszt, utrzymanie, zmiana później) i rekomendacja najprostszej i najtańszej opcji (WAY-122, WAY-123); „świadomy brak” zawsze wchodzi do porównania pozycji awarii, choć nie ma strony dokumentacji, a tekst kroku nie nazywa żadnego narzędzia, bo opcje nie biorą się ze stałej listy: „never from a fixed list of stacks, not even as a hint” (`project-level/technology/research.md:18-19`).
6. Definicja projektu nie ma obowiązkowej pozycji awarii, bramka gotowości jej nie sprawdza, a definicja już zatwierdzona nie wraca z jej powodu do kroku technologii.

### Questions to settle

- Pytanie 1: czy to, skąd człowiek dowiaduje się o awarii, jest częścią pozycji logów, czy osobną pozycją listy wyborów, i czy należy do spraw drogi agenta do działającego produktu?
  - Answer: osobną pozycją poza tą rodziną — zmiana narzędzia do śledzenia błędów nie otwiera decyzji o logach, WAY-166 tej pozycji nie dotyczy, a to, czy agent czyta wybrane narzędzie, jest zwykłą konsekwencją do zważenia; the way dostaje na to nową decyzję i osobne zdanie o tym, kiedy krok tę sprawę sprawdza.
  - Not chosen:
    - część pozycji logów — jedna pozycja mniej, ale zmiana narzędzia otwiera całą decyzję o logach, co WAY-121 już odrzuciło („it binds independent choices together, and a later change to one reopens them all”), i potrzebny jest wyjątek od WAY-166
    - czwarta sprawa w rodzinie drogi agenta — działa istniejący mechanizm i kryterium wejścia na listę, ale WAY-166 ominęłoby panel, który czyta tylko człowiek, więc wyjątek i tak jest potrzebny, a definicja ze słownika przestaje pasować, bo sprawa nie mówi o sprawdzaniu zachowania przez agenta
  - Source: Mariusz, 2026-10-31: „C” — na drogę C przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: jedna pozycja więcej do rozstrzygnięcia w pierwszym projekcie produktu, a alert budowany na logach może przyjść osobną tabelą, dopiero po rozstrzygnięciu logów; WAY-166, `foundations/decisions.md:4467`, WAY-121 *Rejected*, `foundations/decisions.md:2694-2695`, `foundations/glossary.md:9`, `foundations` `f86fd71`.
- Pytanie 2: kiedy sprawa awarii trafia na listę wyborów — przy tym samym kryterium co droga agenta (projekt wnosi zachowanie, które użytkownik zobaczy w działającym produkcie, a fundament nie ma decyzji), czy przy innym, na przykład pierwszy użytkownik spoza zespołu?
  - Answer: przy własnym kryterium — pozycja trafia na listę, gdy fundament nie ma o niej decyzji, a projekt uruchamia produkt poza maszyną, na której produkt powstaje, albo krok uruchomiony przy dokumencie zadania wybiera takie miejsce uruchomienia; pierwsze wdrożenie wymaga miejsca uruchomienia, a ten wybór zawsze przechodzi przez krok, jeśli nic go nie rozstrzyga, więc pytanie pada i przy projekcie, i przy zadaniu; produkt z już rozstrzygniętym miejscem uruchomienia i zatwierdzoną definicją otwiera tę sprawę dopiskiem; retencja jest częścią pytania o logi i idzie za ich kryterium.
  - Not chosen:
    - to samo kryterium co droga agenta — pyta też przy produktach tylko lokalnych i nie działa przy zadaniu, które stawia produkt na serwerze
    - tylko przy definicji, gdy projekt uruchamia produkt poza maszyną, na której powstaje — pierwsze wdrożenie zadaniem przechodzi bez pytania, chyba że człowiek sam je dopisze
    - pierwszy użytkownik spoza zespołu — definicja nie zapisuje takiego momentu, a produkt może dostać obcych użytkowników bez nowego projektu, więc krok nie rusza i człowiek dowiaduje się o awarii od nich
    - bez nowego kryterium, zwykła reguła WAY-121 — „świadomy brak” niczego nie dokłada, więc pytanie nie pada, dopóki ktoś sam nie pomyśli o narzędziu
  - Source: Mariusz, 2026-10-31: „C2” — na drogę przedstawioną w rozmowie doprecyzowania, ze wskazanym kosztem: zadanie o serwerze dostaje jedną pozycję więcej, trzeba zmienić WAY-267 i `project-level/technology/task_run.md`, a odpowiedź „tylko to, o czym mówi dopisek” dostaje jeden wyjątek; wcześniej Mariusz, 2026-10-31: „niezależnie od tego, czy robimy to projektem, czy robimy to zadaniem, jeżeli dojdziemy, rozmawiamy o czymś, co ma związek ze stackiem produktu, to powinniśmy użyć tego skilla”; `project-level/definition_template.md:167`, `project-level/technology/reserved_choices.md:30`, `foundations` `f86fd71`.
  - Zastąpione w części odpowiedzią na pytanie 5: własne kryterium zostaje przy definicji projektu, a przy zadaniu pytanie pada przez listę skilla wdrożeniowego.
- Pytanie 3: jak brzmi granica kroku technologii, skoro „tylko to, co da się zmienić bez dotykania kodu aplikacji” nie obejmuje narzędzia wymienionego w To do 2 — Sentry dla Node.js instaluje się pakietem i uruchamia wywołaniem `Sentry.init()` w pliku projektu (https://docs.sentry.io/platforms/javascript/guides/node/, przeczytane 2026-10-31)?
  - Answer: granica według pytania, na które odpowiada — krok rozstrzyga, czym i dokąd: jakie narzędzie, gdzie trafia zapis, jak długo żyje, jak człowiek dowiaduje się o awarii; wytyczne kodu rozstrzygają, co i w jakiej postaci kod zapisuje; ile kodu wymaga podpięcie narzędzia, pokazuje tabela jako koszt zmiany później.
  - Not chosen:
    - granica zostaje dosłownie, „tylko to, co da się zmienić bez dotykania kodu aplikacji” — prosty test, ale narzędzia wymagające pakietu w kodzie wypadają z kroku, wbrew `project-level/technology/reserved_choices.md:30`, gdzie narzędzie do śledzenia błędów jest wyborem zastrzeżonym dla człowieka
  - Source: Mariusz, 2026-10-31: „B” — na drogę B przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: granica przestaje być prostym testem, a przypadki graniczne rozstrzyga osąd agenta; to samo zdanie poprawiono tego dnia w zadaniu o zawartości logów; `foundations` `f86fd71`.
- Pytanie 4: czy krok uruchomiony przy zadaniu, które wybiera miejsce uruchomienia poza maszyną, na której produkt powstaje, pyta też o logi, razem z tym, jak długo żyje zapis, skoro odpowiedź na pytanie 2 obejmuje tylko pozycję awarii?
  - Answer: tak — krok przy takim zadaniu stawia na liście także sprawę logów, razem z tym, jak długo żyje zapis, o ile fundament jeszcze tego nie mówi; interfejsu i danych deweloperskich ta zmiana nie dotyka.
  - Not chosen:
    - przy takim zadaniu tylko pozycja awarii — zadanie rośnie o jedną pozycję, ale produkt wdrażany zadaniem nie dostaje pytania o trwałość logów, dopóki człowiek sam go nie dopisze, więc zadanie naprawia to tylko przy definicji projektu
  - Source: Mariusz, 2026-10-31: „B” — na drogę B przedstawioną w rozmowie doprecyzowania, ze wskazanym kosztem: zadanie o serwerze rośnie o dwie pozycje przy pierwszym wdrożeniu produktu, a przykład naruszenia w WAY-267 trzeba zmienić; `project-level/technology/task_run.md:39-40`, `foundations/decisions.md:7685-7686`, `foundations` `f86fd71`.
  - Zastąpione odpowiedzią na pytanie 5: krok przy zadaniu nie dokłada sam logów, a pytanie o nie pada przez listę skilla wdrożeniowego.
- Pytanie 5 (rewizja po krytyce dokumentu): jak pytać o czas życia logów i o awarię przy zadaniu, które wdraża produkt, skoro dokładanie ich do kroku wybierającego miejsce uruchomienia każe agentowi otwierać decyzję, nie działa w `loop2` i wymaga pozycji czekających na wybór miejsca?
  - Answer: przez listę skilla wdrożeniowego — lista WAY-139 dostaje dwa punkty: jak długo żyją logi i skąd człowiek dowiaduje się o awarii; gdy zadanie wdraża produkt albo zmienia, jak lub gdzie działa, a skill tego nie mówi, doprecyzowanie pyta człowieka, czy uruchomić krok technologii z dopiskiem o tych sprawach; człowiek rozstrzyga je w tabeli, a skill dostaje odpowiedź; WAY-267 zostaje bez zmian; przy definicji projektu działa kryterium z To do 3.
  - Not chosen:
    - dokładanie logów i pozycji awarii do kroku przy zadaniu, które wybiera miejsce uruchomienia — pytanie pada w samym kroku, bez dodatkowego przystanku, ale WAY-267 dostaje wyjątek, trzeba dopisać reguły na otwieranie decyzji przez agenta i na czekanie na wybór miejsca, a `loop2` dalej wymaga dopisku człowieka
  - Source: Mariusz, 2026-10-31: „No dobrze, niech będzie B.” — na drogę B przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: zadanie wdrożeniowe dostaje jedno pytanie więcej, produkt bez skilla wdrożeniowego najpierw musi go mieć, pytanie pada dopiero przy takim zadaniu, nie przy zwykłej zmianie kodu, a odpowiedź żyje w decyzji i w skillu; WAY-139, `foundations/decisions.md:3501-3504`, WAY-121 *Rejected*, `foundations/decisions.md:2697-2699`, `project-level/technology/task_run.md:49-51`, `foundations` `f86fd71`.
- Pytanie 6: co dzieje się, gdy człowiek odmówi uruchomienia kroku przy zadaniu wdrożeniowym, skoro WAY-139 każe uzupełnić brakujący punkt skilla?
  - Answer: zadanie zapisuje w skillu wdrożeniowym, że człowiek świadomie nie rozstrzyga tych spraw, i pytanie nie wraca, dopóki człowiek sam go nie otworzy.
  - Not chosen:
    - pytanie przy każdym kolejnym wdrożeniu — jedno pytanie za każdym razem i wyjątek od WAY-139
  - Source: Mariusz, 2026-10-31: „przejmuje wszystko zgodnie z rekomendacją” — na propozycję przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: jedno „nie” zamyka sprawę, dopóki człowiek sam jej nie otworzy.

## Context

- To, co kod zapisuje i w jakiej postaci — błąd razem z przyczyną, identyfikatory łączące zdarzenia jednego przepływu — należy do wytycznych kodu, czyli do zadania [[zadanie_ustalic_co_produkt_zapisuje_w_logach_zeby_dalo_sie]]; granicę ustalił Mariusz 17.10, potwierdził 29.10.2026, a jej brzmienie niesie odpowiedź na pytanie 3.
- Osobny skill do researchu observability odpadł, bo krok ma już mechanizm researchu, a osobny skill by go powielał i rozjeżdżał się z nim przy każdej zmianie (decyzja Mariusza, 29.10.2026, lekcja 10xDEVS m3l5).
- Produkt z zatwierdzoną definicją projektu — jak `loop2` — otwiera ten wybór krokiem technologii uruchomionym przy dokumencie zadania (WAY-267, `project-level/technology/task_run.md`); tej ścieżki dostarczyło zadanie [[zadanie_wybor_technologii_ktorej_projekt_nie_ustalil_wraca]], scalone w PR https://github.com/mariusznazar/the-way/pull/63.
- Pierwszy przypadek użycia: `loop2` w kroku 4 lekcji m3l5.
- Skąd wzięło się obecne pytanie o logi, dlaczego niezależnych wyborów nie łączy się w jeden i kiedy taka sprawa trafia na listę wyborów: [[krok_technologii_droga_agenta_do_produktu]], pytania 1, 3, 5 i 8.
- Obecne brzmienie pytania o logi stoi w `project-level/definition_template.md:176-183` (WAY-165), a spojrzenie kroku na logi, interfejs i dane deweloperskie w `project-level/technology/running_product.md`.
- Warunek zachowania widocznego dla użytkownika w `project-level/technology/SKILL.md:48-49` i `project-level/technology/list.md:11` oraz słowa „these matters” w `project-level/technology/start.md:16-17` mówią dziś tylko o drodze agenta, a sprawdzenie skilla wdrożeniowego stoi w `project-level/task/skill/resolve_gaps.md:50-54`.
- Decyzja produktu o logach, która nie mówi, jak długo zapis żyje, po tej zmianie nie rozstrzyga sprawy logów, bo spojrzenie kroku czyta sprawę tak, jak podaje ją szablon: „reading what the matter asks as the template gives it (WAY-165): where one stands, the matter is not listed” (`project-level/technology/running_product.md:11-12`, `foundations` `f86fd71`); następna definicja projektu stawia więc logi na liście, a definicja już zatwierdzona nie wraca: „A definition the gate has approved does not come back to this step for these matters.” (`project-level/technology/start.md:16-17`, `foundations` `f86fd71`).
- The-way nie ma własnego katalogu `guidelines/`; zadanie zmienia tekst skilli i wpisy fundamentu, a pracę nad samym the-way prowadzi `agent-instructions/README.md`.
- Agent tego zadania, w doprecyzowaniu i w cyklu, nie zagląda do `C:\Storage\repos\loop2-10x`, do gałęzi `10x/m3l5`, do tagu `archive/10x-m3l5` w repo `loop2` ani do mapy m3l5: leży tam raport audytu z kursu o logach `loop2`, a krok 4 lekcji m3l5 sprawdza, czy proces the way dojdzie do tych ustaleń sam, więc zmiana w the way, która je zna, unieważnia ten pomiar.
- Po scaleniu sesja, która dostanie link do requestu, przestawia nośnik wierszy 4, 7 i 8 w sekcji „m3l5” pliku `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Przejście 10xDEVS\mapa_pakietu_10x.md` na numer wpisu WAY-xx.

## Questions carried to cycle

- Gdzie w plikach kroku stoi spojrzenie na pozycję awarii, skoro `project-level/technology/running_product.md` opisuje drogę agenta do działającego produktu, i jak krok wznawia definicję, której lista powstała przed tą zmianą, także gdy pozycja logów stoi już na niej jako `held by` albo `projected` i nie jest „brakująca” w sensie `project-level/technology/start.md:13-15`.

## Human actions

none

## Decisions in play

Wybór: decyzje z *Scope* `project-level` według „Reading the foundation”, wyszukanie słów „log”, „retention”, „error track”, „alert”, „running product” w plikach fundamentu i w `project-level/`, wpisy, do których te decyzje prowadzą, oraz niezmiennik `project-technology-record`, na `foundations` `f86fd71`.

- WAY-121 — „A choice belongs on the list when settling it later could change how the work is cut into tasks, or when it adds something the product has to run, pay for or back up”; „As an exception to that rule, where the project brings behaviour a user sees in the running product, the step looks at three matters of an agent's way to the running product — its logs, its interface and its development data”. Pozycja awarii dostaje własne kryterium obok tego wyjątku (pytania 1 i 2); *Rejected* odrzuca „the logs, the interface and the development data as one choice — it binds independent choices together, and a later change to one reopens them all”, co niesie odpowiedź na pytanie 1.
- WAY-122 — „The options of each technology choice a project or a task needs come from research of that choice”. Obowiązuje obie sprawy bez zmian (To do 5); narzędzie, przeciw któremu pisze się kod, jest ważone jak biblioteka.
- WAY-123 — „shows the options of each choice by their consequences for the product — what it costs, where it runs, what keeping it running takes and what changing it later costs”. Tu pokazuje się koszt podpięcia narzędzia w kodzie (pytanie 3).
- WAY-138 — „tests the option it recommends for each choice it settles”. Obejmuje obie sprawy, także odpowiedź „świadomy brak”, gdy jest rekomendowana.
- WAY-139 — „The-way holds no skill of a product, only the list of what a product's deployment skill covers: a preview of deployments; where the secrets lie and how they are rotated; rollback, with its number of steps and what happens to the data; what the agent does and what the human does; and how to read the logs.” Zmienia się: lista dostaje dwa punkty (pytanie 5); *Rejected* w WAY-121 odrzuca te sprawy na tej liście z powodu, który tu nie działa: „only a task that deploys the product checks that list, so a product run on a local machine alone would leave an agent with no way to it”.
- WAY-140 — „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human”. Dotyczy zadań produktu, które budują wybraną odpowiedź, na przykład konta w usłudze śledzenia błędów, nie tego zadania.
- WAY-143 — „A technical element enters the plan with the first task that uses it, or with a preparatory task that task depends on.” Bez zmian: narzędzie do śledzenia błędów wchodzi z pierwszym zadaniem, które z niego korzysta.
- WAY-165 — „the logs ask where the record of what the running product does goes and how an agent reads it”; *Rejected*: „what the product logs and in what form, in the same decision — that rule acts where code is written and reviewed, in the task cycle, not where a project settles its technology”. Pytanie o logi zostaje poszerzone o to, jak długo żyje zapis (To do 1), a przykład zgodny, „an agent reading the output of the server's container”, i uzasadnienie, które mówi tylko o sprawdzaniu zmiany, muszą mówić też o czasie życia zapisu i diagnozie po wdrożeniu; *Rejected* zgadza się z odpowiedzią na pytanie 3.
- WAY-166 — „In a choice of an agent's way to the running product, whether an agent can use an option is a consequence for the product”. Obowiązuje logi razem z czasem życia zapisu; pozycji awarii nie obowiązuje (pytanie 1).
- WAY-219 — „Where the foundation settles no such way, they inspect the states in code and mark the screenshot unchecked”. Bez zmian: pozycja awarii nie jest drogą agenta.
- WAY-267 — „looks at the matters of an agent's way to the running product only where the note touches them”; przykład naruszenia „a run adds the logs, the interface or the development data to its list though the note does not touch them”; *Rejected*: „the note and the matters of an agent's way to the running product together, where a task brings something a user sees — a task about something else can gain up to three further choices”. Bez zmian (pytanie 5): dopisek uruchomiony za zgodą człowieka dotyka tych spraw, a przypadek „the human asks for a run while the task is refined” stoi już w `project-level/task/skill/resolve_gaps.md:31`.
- WAY-268 — „A technology choice whose later settling could change how the work is cut into tasks, or that adds something the product has to run, pay for or back up, and that no decision of the foundation, no approved definition the task carries and no accepted answer of its task document settles, is a reserved choice”. Bez zmian; narzędzie do śledzenia błędów jest przykładem wyboru zastrzeżonego (`project-level/technology/reserved_choices.md:30`).
- WAY-100 — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” Nowa decyzja nazywa, co przejmuje z lekcji 10xDEVS m3l5.
- WAY-106 — „The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries.” Bez zmian.
- `project-technology-record` — „Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>` nor a question a heading of a projected decision holds.” Bez zmiany znaczenia.

## Settlements to record

Candidates: 5 shown, 4 accepted — 2026-10-31

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Pytanie o logi w kroku technologii obejmuje też to, jak długo zapis żyje, także między wdrożeniami. | decision | To do 1 | czy decyzja o logach może nie mówić, czy zapis przeżywa wdrożenie |
| 2 | Krok technologii sprawdza, jak człowiek dowiaduje się o awarii, jako osobną pozycję listy poza drogą agenta do działającego produktu: narzędzie do śledzenia błędów, alert albo świadomy brak na początek, a brak narzędzia jest pełnoprawną opcją; to, czy agent czyta wybrane narzędzie, jest zwykłą konsekwencją do zważenia, a nie brakiem z WAY-166; sprawę bada zwykły mechanizm kroku, bo osobny skill do researchu observability by go powielał i rozjeżdżał się z nim przy każdej zmianie; to przejęcie z lekcji 10xDEVS m3l5: pytania o to, jak długo żyje zapis i skąd człowiek dowiaduje się o awarii, bo log wystarczający do sprawdzenia zmiany tuż po wdrożeniu nie wystarcza do diagnozy awarii sprzed wdrożenia. | decision | odpowiedź na pytanie 1; To do 2; Context, wiersz o osobnym skillu; Need | czy dopisać sprawę do pozycji logów, czy rekomendacja ma omijać panel, który czyta tylko człowiek, i czy pisać osobny skill |
| 3 | Przy definicji projektu pozycja awarii trafia na listę, gdy fundament nie ma o niej decyzji, a projekt uruchamia produkt poza maszyną, na której produkt powstaje; definicja nie ma obowiązkowej pozycji awarii, bramka gotowości jej nie sprawdza, a definicja już zatwierdzona nie wraca z jej powodu do kroku technologii. | decision | odpowiedzi na pytania 2 i 5; To do 6 | czy pytać przy każdym projekcie z zachowaniem widocznym dla użytkownika, czy dopiero przy pierwszym obcym użytkowniku, i czy dołożyć warunek do bramki gotowości |
| 4 | Lista skilla wdrożeniowego z WAY-139 obejmuje też to, jak długo żyją logi, także między wdrożeniami, i skąd człowiek dowiaduje się o awarii; gdy zadanie wdraża produkt albo zmienia, jak lub gdzie działa, a skill tego nie mówi, doprecyzowanie pyta człowieka, czy uruchomić krok technologii z dopiskiem o tych sprawach, a skill dostaje odpowiedź; gdy człowiek odmówi, zadanie zapisuje w skillu, że świadomie nie rozstrzyga tych spraw, i pytanie nie wraca. | decision | odpowiedzi na pytania 5 i 6 | czy dopisać brakujący punkt skilla samemu, bez wyboru człowieka, czy dokładać te sprawy do kroku przy zadaniu, i co zrobić po odmowie |

## Out of scope

- To, co kod zapisuje i w jakiej postaci — zadanie [[zadanie_ustalic_co_produkt_zapisuje_w_logach_zeby_dalo_sie]].
- Przestawienie przypięcia the way w `loop2` i sam wybór logów i awarii w `loop2` — krok 4 lekcji 10xDEVS m3l5.
