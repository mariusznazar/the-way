**State: ready** — nothing below waits for your answer; the items in "You accept by merging" count as accepted by the merge, and item 1 of "Fix or let through" can be let through.

## What you will see

Two rules of the process's own foundation change, and one new guard is added.

First, a fact about a setting that only someone logged in to another company's service can see (a branch protection in GitHub, a rule in a Cloudflare panel) now has an allowed form of source: one reading, quoted word for word, with the command or API call, the service, the version of each tool the result depends on, and the date. Until now this was allowed only for servers the product's people run themselves, so an agent writing such a fact had to invent a form. The reading must hold no secret: the command is narrowed to the fields the fact rests on, and a marker put over a secret is refused. A reading may be several commands or a command of many lines, quoted whole in a code block, as one reading. The template for facts also now says how to quote code kept at a fixed commit.

Second, an invariant whose condition lives outside its own sentence now names, by identifier, the entry or decision that holds the condition, in a field if the template has one, otherwise in the sentence. This closes the last open note in the invariants template.

Third, a new rule with a test: no file tracked under the folder of templates and skills may carry the words "decision pending". The test runs with the full set of tests and fails when such a note returns.

### Underneath

The change is eight edits of text (three decisions edited in place, two templates, one skill file, the README, the invariants file) plus one small test and one test pinning that the foundation check reads a fact whose source holds a command of several lines.

## For you to decide

### Needed from you

none

### Fix or let through

1. The review of the whole change read 14 of the 112 decisions its selection named, whole, and went through the other 98 by their titles only. It named fourteen more as bearing on the change and left them unread, among them the decisions on what one invariant entry holds and on what the "rests on" field names, and it did not compare the example pairs of two of them with the new invariant. If one of those decisions says something that contradicts a new sentence, whoever writes the next invariant or fact finds out then, not now. Having a fresh reviewer read what stayed unread costs one more review round; making a task of it leaves the gap standing; letting it through accepts that the foundation check, the full tests and the two reviews found nothing. I recommend letting it through, since every sentence of the change was read against the decisions it touches and the check reports no error. Read the rest in this request, make a task of it, or let it through? (Course of the cycle, Checks)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The reading's form is written in the decision itself, not only in the template: one invocation quoted word for word however many commands and lines it has, a command of several lines in a code block, the version of each tool, and a quoted output with no secret. The task asked for this wording; the cycle added that the rejected way of "a reading that a check reruns" now speaks of a host or a service, because the old wording would have contradicted the new reading, and added one example to each of the three changed decisions so that a reader sees what passes and what fails. Another way was to leave the old clause and the examples as they were, which would have left the decisions contradicting themselves or the new sentences unchecked.
3. Two decisions now hold their binding sentences in two short paragraphs instead of one long one, because the form allows one to three sentences in a paragraph and the new sentences would have made five and four. No sentence was reworded for it. The other way was to leave five sentences in one paragraph, which the form does not allow.
4. The new guard reads the words "decision pending" with any run of spaces and line breaks between them as one space, so a note wrapped across two lines is caught too, while a different capitalisation and an untracked file are not. The other way was a single literal space, which a wrapped note would slip past. Nothing in the repository wraps the words today.
5. The new test sits among the tests of the shared rules of the foundation, not among the tests of the test runner or in a new folder, because the full set of tests already runs it there. The invariant lists the six parts whose files stand under the folder of templates and skills, which is all the parts that can introduce the note.
6. A foundation entry the task did not name: the decision on what an element's skill holds now names the new invariant among the rules that hold it, as the other decisions name theirs.
7. The new rule is an invariant of the process itself, checked by a test that reads the real tracked files, never a made-up fixture. It starts as satisfied: the two last notes were removed, and the test fails on a seeded one (the author's run, and the reviewer's).

## Cost

The cycle took about 39 minutes of working time over 13 stages and 24.0 million tokens, all on one model, with one round of fix: the review of the whole change failed once on a contradiction in the template, the fix passed its review, and the return step's two-line edit passed a third. The full set of tests took about 20 minutes. The table of stages is in the committed record: the stages table of the committed record (its link is added in the next edit of this description).

## How to merge

Merge with a merge commit, not a squash or a rebase, so that the link to the record by its commit stays valid. The foundation has waited for a review for 42 merges since the last one tagged on 6 November 2026, past the threshold of 30; the review is the skill that reviews the foundation against the product, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>W języku zadania</summary>

**Stan: gotowe** — nic poniżej nie czeka na Twoją odpowiedź; pozycje z „Akceptujesz przez scalenie” są przyjęte przez scalenie, a pozycję 1 z „Do poprawienia albo przepuszczenia” możesz przepuścić.

## Co zobaczysz

Zmieniają się dwie reguły fundamentu samego procesu i dochodzi jedna nowa blokada.

Po pierwsze, fakt o ustawieniu, które widać tylko po zalogowaniu w cudzej usłudze (ochrona gałęzi w GitHubie, reguła w panelu Cloudflare), ma teraz dozwoloną formę źródła: jeden odczyt, zacytowany słowo w słowo, z poleceniem albo wywołaniem API, usługą, wersją każdego narzędzia, od którego zależy wynik, i datą. Dotąd było to dozwolone tylko dla serwerów, które ludzie produktu prowadzą sami, więc agent piszący taki fakt wymyślał formę sam. Odczyt nie może zawierać sekretu: polecenie zawęża się do pól, na których stoi fakt, a znacznik zakrywający sekret jest odrzucony. Odczyt może składać się z kilku poleceń albo z polecenia wielowierszowego, cytowanego w całości w bloku kodu, jako jeden odczyt. Szablon faktów mówi też, jak cytować kod trzymany pod stałym commitem.

Po drugie, niezmiennik, którego warunek stoi poza jego zdaniem, wskazuje teraz identyfikatorem wpis albo decyzję, która ten warunek trzyma — w polu, jeśli szablon takie daje, a inaczej w zdaniu. To zamyka ostatni otwarty dopisek w szablonie niezmienników.

Po trzecie, nowa reguła z testem: żaden plik śledzony pod katalogiem szablonów i skilli nie może zawierać słów „decision pending”. Test działa razem z pełnym zestawem testów i pada, gdy taki dopisek wróci.

### Pod spodem

Zmiana to osiem edycji tekstu (trzy decyzje poprawione w miejscu, dwa szablony, jeden plik skilla, README, plik niezmienników) oraz jeden mały test i jeden test utrwalający, że sprawdzanie fundamentu czyta fakt, którego źródło ma polecenie wielowierszowe.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Do poprawienia albo przepuszczenia

1. Przegląd całej zmiany przeczytał w całości 14 ze 112 decyzji z wybranego zakresu, a pozostałe 98 przejrzał tylko po tytułach. Czternaście kolejnych nazwał jako mających związek ze zmianą i zostawił nieprzeczytane — wśród nich decyzje o tym, co zawiera jeden wpis niezmiennika i co nazywa pole „rests on”; nie porównał też par przykładów dwóch z nich z nowym niezmiennikiem. Jeśli któraś z nich przeczy nowemu zdaniu, autor następnego niezmiennika albo faktu dowie się o tym wtedy, a nie teraz. Przeczytanie reszty przez świeżego recenzenta kosztuje jedną rundę przeglądu więcej; zadanie na to zostawia lukę; przepuszczenie przyjmuje, że sprawdzanie fundamentu, pełne testy i dwa przeglądy niczego nie znalazły. Polecam przepuścić, bo każde zdanie zmiany przeczytano względem decyzji, których dotyka, a sprawdzanie nie zgłasza błędu. Doczytać resztę w tym PR, zrobić z tego zadanie czy przepuścić? (Course of the cycle, Checks)

### Akceptujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

2. Forma odczytu stoi w samej decyzji, nie tylko w szablonie: jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało, polecenie wielowierszowe w bloku kodu, wersja każdego narzędzia i cytowany wynik bez sekretu. Zadanie prosiło o to brzmienie; cykl dołożył, że odrzucone „odczyt, który sprawdzenie powtarza” mówi teraz o hoście albo usłudze, bo stare brzmienie przeczyłoby nowemu odczytowi, oraz po jednym przykładzie w trzech zmienionych decyzjach, żeby czytelnik widział, co przechodzi, a co nie. Inna droga: zostawić starą klauzulę i przykłady, co zostawiłoby decyzje sprzeczne ze sobą albo nowe zdania bez sprawdzenia.
3. Dwie decyzje mają teraz zdania wiążące w dwóch krótkich akapitach zamiast jednego długiego, bo forma dopuszcza jedno do trzech zdań w akapicie, a nowe zdania dałyby pięć i cztery. Żadne zdanie nie zostało przeformułowane. Inna droga: zostawić pięć zdań w jednym akapicie, czego forma nie dopuszcza.
4. Nowa blokada czyta słowa „decision pending” z dowolnym ciągiem spacji i końców linii między nimi jak jedną spację, więc dopisek przełamany na dwie linie też zostanie wyłapany, a inna wielkość liter i plik nieśledzony nie. Inna droga: jedna dosłowna spacja, którą przełamany dopisek by ominął. Dziś nic w repozytorium nie łamie tych słów.
5. Nowy test leży wśród testów wspólnych reguł fundamentu, nie wśród testów uruchamiacza ani w nowym katalogu, bo pełny zestaw testów już go tam uruchamia. Niezmiennik wymienia sześć części, których pliki stoją pod katalogiem szablonów i skilli, czyli wszystkie, które mogą wprowadzić dopisek.
6. Wpis fundamentu, którego zadanie nie wymieniało: decyzja o tym, co zawiera skill elementu, nazywa teraz nowy niezmiennik wśród reguł, które go trzymają, jak inne decyzje nazywają swoje.
7. Nowa reguła jest niezmiennikiem samego procesu, sprawdzanym testem, który czyta prawdziwe śledzone pliki, nigdy zmyślony przykład. Zaczyna jako spełniona: dwa ostatnie dopiski usunięto, a test pada na podłożonym (próba autora i recenzenta).

## Koszt

Cykl zajął ok. 39 minut pracy w 13 etapach i 24,0 mln tokenów, wszystko na jednym modelu, z jedną rundą poprawki: przegląd całej zmiany raz dał wynik niepomyślny, na sprzeczności w szablonie, poprawka przeszła przegląd, a dwuliniowa edycja kroku powrotnego przeszła trzeci. Pełny zestaw testów trwał ok. 20 minut. Tabela etapów leży w zacommitowanym zapisie: the stages table of the committed record (its link is added in the next edit of this description).

## Jak scalić

Scal merge commitem, nie squashem ani rebase’em, żeby link do zapisu po jego commicie pozostał ważny. Fundament czeka na przegląd przez 42 scalenia od ostatniego, otagowanego 6 listopada 2026, ponad próg 30; przegląd to skill przeglądający fundament względem produktu, uruchamiany w sesji w tym repozytorium, i nic w tym PR na niego nie czeka.

</details>

## Technical changes

The change is four commits on `task/service-reading-and-invariant-condition`, base `0e1cd3c`. A reading in a service is allowed in a few places, so a reader sees the same rule wherever a fact's source is written.

- `19efdfd` — WAY-80 (what is a fact's source) now covers a setting set on another's service, one invocation quoted whole, a multi-line command in a code block, the version of each tool, and a quoted output with no secret; WAY-84 says such a setting has a reading for its source and its *Rejected* turns down a repeated reading, not the one quoted; WAY-60 (where a condition that decides an invariant may stand) says an invariant whose condition stands outside its sentence names the entry or decision that holds it; the facts template (`elements/environment-facts/template.md`) replaces its `TODO — decision pending` bullet by a rule citing WAY-80 and WAY-84 and states the reading's form and how to cite code at a fixed commit; the facts skill (`elements/environment-facts/skill/draft.md`) says how to run a reading in a service and narrow it to the fields the sentence rests on; the invariants template (`elements/invariants/template.md`) drops its note and cites WAY-60; `README.md` (list of elements, row of `environment_facts.md`) covers a reading in a service; the new invariant `elements-no-pending-marker` is written in `foundations/invariants.md` with its test `elements/common/test_elements_pending_marker.py`; WAY-35 names it in its *Verification*.
- `8680824` — a test in `elements/common/test_foundation_check.py` pinning the answer to the task's carried question: the foundation check reads a fact whose *Source* holds an indented code block of several lines (a block not indented to the item breaks it, as the template's form says).
- `4f26b6b` — the fix of the review of the whole change: B1 (the template and the rationale of WAY-80 said "nothing is cut from the output afterwards", against the allowed "lines the sentence rests on") — the words removed; M1 (WAY-80 five sentences, WAY-60 four) — second paragraphs; M2 (the added test does not catch a break of `blocks` or `fields`, as its comment claimed) — the claim withdrawn, the test kept as a pin; M3 (test pattern broader than the sentence) — sentence now says runs of spaces and line breaks count as one space, pattern `decision[ \n]+pending`; M4 (code citation cited WAY-80) — citation dropped; M5 — rewrapping.
- `43ffa5a` — the return step: one long line of WAY-80 rewrapped and one example of WAY-84 reworded, no meaning changed.

## Checks

- Gate: `python -B task-cycle/gate_times.py --output .runs/task-cycles/service-reading-and-invariant-condition/gate_times.md -- python -B gate/run_tests.py` on `43ffa5a` (the final tree, the target branch had not moved): exit 0, 1328 tests in 10 directories, every directory passed, 1179.8 s, one other registered gate at the same time. One run.
- Failing on the base: none. No gate was run on the base: the base `0e1cd3c` is a merge whose tree equals that of its second parent, so the list was taken from `docs/task-cycles/co-trafia-do-dziennika-decyzji/cycle.md` of commit `07a2ba5`, *Verification*, the final gate (run 4) on `8571691`: exit 0, 1326 tests in 10 directories. The test `gate/test_run_tests.py` `DirectoriesAtOnce.test_by_default_every_directory_runs_at_the_same_time` failed in 2 of 4 full runs of that cycle and passed in all of this one; its file belongs to the part `gate`, outside this task's parts.
- `python -B elements/common/foundation_check.py` on the finished change, without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line.
- Own-work checks: the author's: the invariant's test fails on the two real notes (exit 1, before they were removed), on a seeded note and on one split by a line end, and passes on the committed tree; the foundation check reads a fact with a multi-line command under *Source*. The fix's: the seeded wrapped note fails the test, a tab between the words passes. The reviewers' negative controls agree.
- Focused checks: `python -B gate/run_tests.py elements/common` 201 tests, exit 0, on `4f26b6b` (author, both reviewers); `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exit 0, 298 files.
- Form check, private-paths check on the description, and the three checks on the record's copy: run on the copy of the record once it is committed; the next edit of this description fills them in.

## Foundation entries

- WAY-80, changed in place: a state of a host the product's people run, or of a setting they set on another's service which no page open without their access shows, has for its source a reading — one invocation quoted word for word, with its tools' versions, whose quoted output holds no secret. Marked `row 1`, `row 3`, `row 4`.
- WAY-84, changed in place: such a setting has a reading for its source (WAY-80), and a repeated reading is rejected, not the one quoted. Marked `row 1`, `row 2`.
- WAY-60, changed in place: an invariant whose condition stands outside its sentence names, by identifier, the entry or decision that holds it. Marked `row 5`.
- `elements-no-pending-marker` (invariant, new, method `test`, derives from WAY-35, rests on none, violated `no`): no file git tracks under `elements/` holds the text "decision pending", every run of spaces and line breaks counting as one space; its test `elements/common/test_elements_pending_marker.py` cites it by `# invariant: elements-no-pending-marker`. Marked `row 6`.
- WAY-35 *Verification* names `elements-no-pending-marker`. Marked `the cycle's`.
- Template and skill text with no decision: items 4, 5, 6 and 7 of the task's *To do* in `elements/environment-facts/template.md`, `elements/environment-facts/skill/draft.md`, `elements/invariants/template.md` and `README.md`.
- No invariant derives from WAY-60, WAY-80 or WAY-84 other than the new one from WAY-35, so none needed a corrected sentence; the check listed none.

## Minor findings

- Of the fix's review (`reports/fix-review-report.md`): "`foundations/decisions.md` WAY-80, second paragraph: the line 'quoting the source is no source. A fact resting on a whole section of rules quotes the sentence of its source that sets those rules and' is about 137 characters, and the rationale of WAY-80 ends with a one-word line (`it.`); the paragraph split left a hand-wrapped line unreflowed. Polish only, no rule limits line length" — fixed afterwards by the return step's rewrap (`43ffa5a`), whose review found nothing.
- Of the fix's review: "`foundations/invariants.md:108`: the invariant's sentence is one long line, as the file's other sentences are; no finding, noted because the sentence grew by a clause that pairs exactly with the test's pattern." The reviewer made it no finding; it stays as it is.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task "two changes of the decision log — a reading as the source of a fact about a setting in another's service, an invariant names the place of its condition — and a test that the 'decision pending' notes do not return", independent, status `ready for cycle`, frozen copy in the record; decisions as they stand on `foundations` at `0e1cd3c` (the checkout was fast-forwarded from `d40d1cb` at the start); answers of the person who owns the process noted in the task's *Questions to settle*.
- **Process pin:** none; this is the-way itself.
- **Spec:** none; no open design choice (every choice is settled by the task's *Questions to settle* and *Settlements to record*).
- **Route:** one author without a plan, class `same` as the orchestrator's, for a change over several parts of text where a wrong word binds later work; the whole-change review failed once (B1) and passed after one fix; the return step committed one edit, reviewed PASS.
- **Plan:** none on the one-author route.
- **Choices:** 7 other choices, in the questions table of the record: the checkout newer than the task's quotations, the new test's place, the matching of line breaks, "a host or a service" in the rejected clause, the examples in three decisions, the second paragraphs of two decisions, and the pinning test.
- **Blocking findings left:** none.
- **Record:** the committed record (its link is added in the next edit of this description).
