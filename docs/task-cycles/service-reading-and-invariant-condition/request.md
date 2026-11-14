**State: ready** — corrected for your remarks; the one item of "Fix or let through" asks only whether to make a task of a finding, and the merge lets it through.

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

1. Two rules the change touches now say different things about where an identifier goes. One says an invariant whose condition stands outside its sentence names the decision that holds it in the sentence itself, where its form has no field for it; the other, older, says an invariant's links stand beside its sentence, not inside it. They can be read as agreeing, since a decision of the pinned process is no entry of the product's own log, so naming it is no link, but no sentence says so. A writer or a reviewer who reads the older rule first may reject the form the new rule gives. Fixing it in this request costs one more fix and one more review round, and it would edit an older decision beyond what the task asked; making a task of it leaves the two sentences as they are until someone settles the reading in one clause; letting it through accepts that a writer hesitates once. I recommend making a task, since the clause may belong in either decision and that choice is yours. Make a task of it? (Minor findings, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The reading's form is written in the decision itself, not only in the template: one invocation quoted word for word however many commands and lines it has, a command of several lines in a code block, the version of each tool, and a quoted output with no secret. The task asked for this wording; the cycle added that the rejected way of "a reading that a check reruns" now speaks of a host or a service, because the old wording would have contradicted the new reading, and added one example to each of the three changed decisions so that a reader sees what passes and what fails. Another way was to leave the old clause and the examples as they were, which would have left the decisions contradicting themselves or the new sentences unchecked.
3. Two decisions now hold their binding sentences in two short paragraphs instead of one long one, because the form allows one to three sentences in a paragraph and the new sentences would have made five and four. No sentence was reworded for it. The other way was to leave five sentences in one paragraph, which the form does not allow.
4. The new guard reads the words "decision pending" with any run of spaces and line breaks between them as one space, so a note wrapped across two lines is caught too, while a different capitalisation and an untracked file are not. The other way was a single literal space, which a wrapped note would slip past. Nothing in the repository wraps the words today.
5. The new test sits among the tests of the shared rules of the foundation, not among the tests of the test runner or in a new folder, because the full set of tests already runs it there. The invariant lists the six parts whose files stand under the folder of templates and skills, which is all the parts that can introduce the note.
6. A foundation entry the task did not name: the decision on what an element's skill holds now names the new invariant among the rules that hold it, as the other decisions name theirs.
7. The new rule is an invariant of the process itself, checked by a test that reads the real tracked files, never a made-up fixture. It starts as satisfied: the two last notes were removed, and the test fails on a seeded one (the author's run, and the reviewer's).
8. This correction answered your remark on the item about the decisions the first review left unread, which the cycle judged the task and the foundation did not require. A fresh reviewer read all fourteen of them whole and compared the example pairs of two of them with the new invariant; it found nothing that blocks, so no code changed.

## Cost

The cycle took about 52 minutes of working time and 32.6 million tokens across the first run and the correction, all on one model, with one round of fix: the review of the whole change failed once on a contradiction in the template, the fix passed its review, the return step's two-line edit passed a third, and the fresh review of the correction passed. The full set of tests took about 20 minutes and was not rerun, since the correction changed no code. The table of stages, across the correction, is in the committed record: https://github.com/mariusznazar/the-way/blob/e071faceda5d64dd2a498e2099d53fba57e59a57/docs/task-cycles/service-reading-and-invariant-condition/stages.md.

## How to merge

Merge with a merge commit, not a squash or a rebase, so that the link to the record by its commit stays valid. The foundation has waited for a review for 42 merges since the last one tagged on 6 November 2026, past the threshold of 30; the review is the skill that reviews the foundation against the product, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>W języku zadania</summary>

**Stan: gotowe** — poprawione po Twoich uwagach; jedyna pozycja z „Do poprawienia albo przepuszczenia” pyta tylko, czy zrobić zadanie ze znaleziska, a scalenie je przepuszcza.

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

1. Dwie reguły, których dotyka zmiana, mówią teraz różnie o tym, gdzie stoi identyfikator. Jedna mówi, że niezmiennik, którego warunek stoi poza jego zdaniem, wskazuje decyzję, która go trzyma, w samym zdaniu, gdy forma nie ma na to pola; druga, starsza, mówi, że powiązania niezmiennika stoją obok jego zdania, nie w nim. Da się je czytać zgodnie, bo decyzja z przypiętego procesu nie jest wpisem dziennika samego produktu, więc jej wskazanie nie jest powiązaniem, ale żadne zdanie tego nie mówi. Autor albo recenzent, który przeczyta najpierw starszą regułę, może odrzucić formę, jaką daje nowa. Poprawka w tym PR kosztuje jedną rundę poprawki i przeglądu więcej i zmieniłaby starszą decyzję ponad to, o co prosiło zadanie; zadanie zostawia oba zdania, jak są, dopóki ktoś nie rozstrzygnie czytania jedną klauzulą; przepuszczenie przyjmuje, że autor raz się zawaha. Polecam zadanie, bo klauzula może należeć do którejś z dwóch decyzji, a ten wybór jest Twój. Zrobić z tego zadanie? (Minor findings, 1)

### Akceptujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

2. Forma odczytu stoi w samej decyzji, nie tylko w szablonie: jedno wywołanie cytowane słowo w słowo, ile by poleceń i linii nie miało, polecenie wielowierszowe w bloku kodu, wersja każdego narzędzia i cytowany wynik bez sekretu. Zadanie prosiło o to brzmienie; cykl dołożył, że odrzucone „odczyt, który sprawdzenie powtarza” mówi teraz o hoście albo usłudze, bo stare brzmienie przeczyłoby nowemu odczytowi, oraz po jednym przykładzie w trzech zmienionych decyzjach, żeby czytelnik widział, co przechodzi, a co nie. Inna droga: zostawić starą klauzulę i przykłady, co zostawiłoby decyzje sprzeczne ze sobą albo nowe zdania bez sprawdzenia.
3. Dwie decyzje mają teraz zdania wiążące w dwóch krótkich akapitach zamiast jednego długiego, bo forma dopuszcza jedno do trzech zdań w akapicie, a nowe zdania dałyby pięć i cztery. Żadne zdanie nie zostało przeformułowane. Inna droga: zostawić pięć zdań w jednym akapicie, czego forma nie dopuszcza.
4. Nowa blokada czyta słowa „decision pending” z dowolnym ciągiem spacji i końców linii między nimi jak jedną spację, więc dopisek przełamany na dwie linie też zostanie wyłapany, a inna wielkość liter i plik nieśledzony nie. Inna droga: jedna dosłowna spacja, którą przełamany dopisek by ominął. Dziś nic w repozytorium nie łamie tych słów.
5. Nowy test leży wśród testów wspólnych reguł fundamentu, nie wśród testów uruchamiacza ani w nowym katalogu, bo pełny zestaw testów już go tam uruchamia. Niezmiennik wymienia sześć części, których pliki stoją pod katalogiem szablonów i skilli, czyli wszystkie, które mogą wprowadzić dopisek.
6. Wpis fundamentu, którego zadanie nie wymieniało: decyzja o tym, co zawiera skill elementu, nazywa teraz nowy niezmiennik wśród reguł, które go trzymają, jak inne decyzje nazywają swoje.
7. Nowa reguła jest niezmiennikiem samego procesu, sprawdzanym testem, który czyta prawdziwe śledzone pliki, nigdy zmyślony przykład. Zaczyna jako spełniona: dwa ostatnie dopiski usunięto, a test pada na podłożonym (próba autora i recenzenta).
8. Ta korekta odpowiedziała na Twoją uwagę do pozycji o decyzjach, które pierwszy przegląd zostawił nieprzeczytane; cykl uznał, że zadanie ani fundament tego nie wymagały. Świeży recenzent przeczytał wszystkie czternaście w całości i porównał pary przykładów dwóch z nich z nowym niezmiennikiem; nie znalazł niczego blokującego, więc kod się nie zmienił.

## Koszt

Cykl zajął ok. 52 minuty pracy i 32,6 mln tokenów w pierwszym przebiegu i w korekcie, wszystko na jednym modelu, z jedną rundą poprawki: przegląd całej zmiany raz dał wynik niepomyślny, na sprzeczności w szablonie, poprawka przeszła przegląd, dwuliniowa edycja kroku powrotnego przeszła trzeci, a świeży przegląd korekty też przeszedł. Pełny zestaw testów trwał ok. 20 minut i nie był powtarzany, bo korekta nie zmieniła kodu. Tabela etapów, z korektą, leży w zacommitowanym zapisie: https://github.com/mariusznazar/the-way/blob/e071faceda5d64dd2a498e2099d53fba57e59a57/docs/task-cycles/service-reading-and-invariant-condition/stages.md.

## Jak scalić

Scal merge commitem, nie squashem ani rebase’em, żeby link do zapisu po jego commicie pozostał ważny. Fundament czeka na przegląd przez 42 scalenia od ostatniego, otagowanego 6 listopada 2026, ponad próg 30; przegląd to skill przeglądający fundament względem produktu, uruchamiany w sesji w tym repozytorium, i nic w tym PR na niego nie czeka.

</details>

## Technical changes

The change is four commits on `task/service-reading-and-invariant-condition`, base `0e1cd3c`. A reading in a service is allowed in a few places, so a reader sees the same rule wherever a fact's source is written.

- `19efdfd` — WAY-80 (what is a fact's source) now covers a setting set on another's service, one invocation quoted whole, a multi-line command in a code block, the version of each tool, and a quoted output with no secret; WAY-84 says such a setting has a reading for its source and its *Rejected* turns down a repeated reading, not the one quoted; WAY-60 (where a condition that decides an invariant may stand) says an invariant whose condition stands outside its sentence names the entry or decision that holds it; the facts template (`elements/environment-facts/template.md`) replaces its `TODO — decision pending` bullet by a rule citing WAY-80 and WAY-84 and states the reading's form and how to cite code at a fixed commit; the facts skill (`elements/environment-facts/skill/draft.md`) says how to run a reading in a service and narrow it to the fields the sentence rests on; the invariants template (`elements/invariants/template.md`) drops its note and cites WAY-60; `README.md` (list of elements, row of `environment_facts.md`) covers a reading in a service; the new invariant `elements-no-pending-marker` is written in `foundations/invariants.md` with its test `elements/common/test_elements_pending_marker.py`; WAY-35 names it in its *Verification*.
- `8680824` — a test in `elements/common/test_foundation_check.py` pinning the answer to the task's carried question: the foundation check reads a fact whose *Source* holds an indented code block of several lines (a block not indented to the item breaks it, as the template's form says).
- `4f26b6b` — the fix of the review of the whole change: B1 (the template and the rationale of WAY-80 said "nothing is cut from the output afterwards", against the allowed "lines the sentence rests on") — the words removed; M1 (WAY-80 five sentences, WAY-60 four) — second paragraphs; M2 (the added test does not catch a break of `blocks` or `fields`, as its comment claimed) — the claim withdrawn, the test kept as a pin; M3 (test pattern broader than the sentence) — sentence now says runs of spaces and line breaks count as one space, pattern `decision[ \n]+pending`; M4 (code citation cited WAY-80) — citation dropped; M5 — rewrapping.
- `43ffa5a` — the return step: one long line of WAY-80 rewrapped and one example of WAY-84 reworded, no meaning changed.

- Correction 1 changed no code: a fresh reviewer read the fourteen decisions the first review left unread, whole, and compared the example pairs of two of them with the new invariant (`reports/correction-1-review-report.md`, `PASS 43ffa5a`); the branch holds only the record's copy added and removed again after the change.

## Checks

- Correction 1: no gate was run on the corrected tree, since the correction changed no code (`git diff 43ffa5a HEAD` is empty) and the gate below stands for the same tree; the correction review ran `python -B elements/common/foundation_check.py` (exit 0, `0 errors`), `python -B -m unittest elements/common/test_elements_pending_marker.py` (exit 0) and `git diff --check 0e1cd3c..43ffa5a` (exit 0).
- Gate: `python -B task-cycle/gate_times.py --output .runs/task-cycles/service-reading-and-invariant-condition/gate_times.md -- python -B gate/run_tests.py` on `43ffa5a` (the final tree, the target branch had not moved): exit 0, 1328 tests in 10 directories, every directory passed, 1179.8 s, one other registered gate at the same time. One run.
- Failing on the base: none. No gate was run on the base: the base `0e1cd3c` is a merge whose tree equals that of its second parent, so the list was taken from `docs/task-cycles/co-trafia-do-dziennika-decyzji/cycle.md` of commit `07a2ba5`, *Verification*, the final gate (run 4) on `8571691`: exit 0, 1326 tests in 10 directories. The test `gate/test_run_tests.py` `DirectoriesAtOnce.test_by_default_every_directory_runs_at_the_same_time` failed in 2 of 4 full runs of that cycle and passed in all of this one; its file belongs to the part `gate`, outside this task's parts.
- `python -B elements/common/foundation_check.py` on the finished change, without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line.
- Own-work checks: the author's: the invariant's test fails on the two real notes (exit 1, before they were removed), on a seeded note and on one split by a line end, and passes on the committed tree; the foundation check reads a fact with a multi-line command under *Source*. The fix's: the seeded wrapped note fails the test, a tab between the words passes. The reviewers' negative controls agree.
- Focused checks: `python -B gate/run_tests.py elements/common` 201 tests, exit 0, on `4f26b6b` (author, both reviewers); `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exit 0, 298 files.
- Form check, private-paths check on the description, and the three checks on the record's copy: on the copy of the record at `e071fac`, 2 runs each, last run exit 0: `python -B task-cycle/remarks_check.py docs/task-cycles/service-reading-and-invariant-condition` (6 reports, 7 items, 0 not in the process remarks; the original's run: 1 listing of 7 items, then 0); `python -B task-cycle/private_paths_check.py docs/task-cycles/service-reading-and-invariant-condition` (20 files, 0 listed; the first run listed 7 files, cleaned by the rewriting); `python -B task-cycle/image_files_check.py docs/task-cycles/service-reading-and-invariant-condition` (20 files, 0 listed). Form check on this description: `python -B task-cycle/request_check.py .runs/task-cycles/service-reading-and-invariant-condition/request.md --task .runs/task-cycles/service-reading-and-invariant-condition/task.md` exit 0, and the private-paths check on it exit 0, each 2 runs.

## Foundation entries

- WAY-80, changed in place: a state of a host the product's people run, or of a setting they set on another's service which no page open without their access shows, has for its source a reading — one invocation quoted word for word, with its tools' versions, whose quoted output holds no secret. Marked `row 1`, `row 3`, `row 4`.
- WAY-84, changed in place: such a setting has a reading for its source (WAY-80), and a repeated reading is rejected, not the one quoted. Marked `row 1`, `row 2`.
- WAY-60, changed in place: an invariant whose condition stands outside its sentence names, by identifier, the entry or decision that holds it. Marked `row 5`.
- `elements-no-pending-marker` (invariant, new, method `test`, derives from WAY-35, rests on none, violated `no`): no file git tracks under `elements/` holds the text "decision pending", every run of spaces and line breaks counting as one space; its test `elements/common/test_elements_pending_marker.py` cites it by `# invariant: elements-no-pending-marker`. Marked `row 6`.
- WAY-35 *Verification* names `elements-no-pending-marker`. Marked `the cycle's`.
- Template and skill text with no decision: items 4, 5, 6 and 7 of the task's *To do* in `elements/environment-facts/template.md`, `elements/environment-facts/skill/draft.md`, `elements/invariants/template.md` and `README.md`.
- No invariant derives from WAY-60, WAY-80 or WAY-84 other than the new one from WAY-35, so none needed a corrected sentence; the check listed none.

## Minor findings

- Of the review of correction 1 (`reports/correction-1-review-report.md`), not fixed since a correction's Minor findings are not: M1 — WAY-60 and the invariants template now tell a writer to put an identifier in the sentence, while WAY-56 and the template line that cites it say the links stand beside the sentence, not inside it, and nothing says the two do not collide. Places: `foundations/decisions.md` WAY-60, first paragraph, last sentence ("…names by identifier the entry or the decision that holds the condition, in a field where the template gives one and otherwise in its sentence"), and its *Verification* complies example ("names that decision's number in its sentence, its template giving no field for it"); `elements/invariants/template.md:81-83` ("…and otherwise in the sentence (WAY-60)"). Against: WAY-56 binding paragraph ("The method of checking and the links that WAY-08 and WAY-17 require stand beside that sentence, not inside it") and `elements/invariants/template.md:74-78` ("The method and the links stand beside it, not inside it (WAY-56)"), five lines above the new text. WAY-60 itself carries `derives from WAY-56`. What is wrong: the new sentence is the one case in which an identifier of a decision stands in the sentence, which is the binding part (WAY-56). A reader who takes "the links" of WAY-56 as any naming of an entry reads WAY-60 as breaking WAY-56; a reader who takes it as the two fields (the template's *Links* section, `elements/invariants/template.md:107-118`) reads them as agreeing. The files do not say which, and WAY-25 says a collision between two decisions with no precedence recorded is not settled silently. The harmonising reading exists and is what I take: a decision of the pinned the-way is no decision entry of the product's log (WAY-58), so naming it in the sentence is no link that WAY-17 requires; and the foundation already does this (`foundations/invariants.md` `tracked-file-private-paths`, "as WAY-309 and WAY-323 name them"). Way out: a clause in WAY-60 and in the template line 81-83 that the identifier so placed is no link of WAY-17 (a decision of the pinned the-way is no entry of the product's log, WAY-58); or a clause in WAY-56 that it speaks of the links of WAY-17.
- Of the same review: M2 — The identifier `elements-no-pending-marker` names what the sentence demands, where the invariants template says an identifier names what the sentence constrains, never what it demands. Place: `foundations/invariants.md`, heading `## elements-no-pending-marker`, with its citation at `elements/common/test_elements_pending_marker.py:27`, its listing in WAY-35's *Verification*, and the module's name; template rule at `elements/invariants/template.md:18-20` ("The identifier names what the sentence constrains, never what it demands, so that a reworded sentence leaves it true"). WAY-64 gives the identifier's form as words; this is a template rule, not WAY-64's. What is wrong: the "no" in the identifier is the demand. The neighbours constrain a thing (`tracked-file-private-paths`, `outbound-link-reach`, `script-imports`). `elements-pending-marker` would name what is constrained.
- Of the fix's review (`reports/fix-review-report.md`): "`foundations/decisions.md` WAY-80, second paragraph: the line 'quoting the source is no source. A fact resting on a whole section of rules quotes the sentence of its source that sets those rules and' is about 137 characters, and the rationale of WAY-80 ends with a one-word line (`it.`); the paragraph split left a hand-wrapped line unreflowed. Polish only, no rule limits line length" — fixed afterwards by the return step's rewrap (`43ffa5a`), whose review found nothing.
- Of the fix's review: "`foundations/invariants.md:108`: the invariant's sentence is one long line, as the file's other sentences are; no finding, noted because the sentence grew by a clause that pairs exactly with the test's pattern." The reviewer made it no finding; it stays as it is.

## Findings outside the task's scope

- Of the review of correction 1: O1 — The invariant `elements-no-pending-marker` derives from WAY-35, whose binding sentence says nothing about a pending marker. Place: `foundations/invariants.md` (`Derives from: WAY-35`), WAY-35 `foundations/decisions.md` (binding paragraph; *Verification* now naming the invariant). WAY-35 says every rule of an element's entries stands in the template or once in the part the elements share; a pending marker in a template is a rule that does not yet stand there, which is a reading, not a sentence of the decision. WAY-22 asks an invariant to be derived from the decision whose choice it keeps, and WAY-17 asks the link to be written; the nearer decisions are WAY-37 (entries that wait for something) and WAY-71 (where `TODO` may stand), and neither holds the rule either. This lies outside the task: the human settled it ("wyprowadzony z WAY-35", question on the test and the invariant, answer a), so I record it for the human and do not ask the cycle to change it. If the human wants the chain readable, one sentence in WAY-35 that a template or a skill carries no note that a rule is pending would close it.

## Course of the cycle

- **Task and sources:** the task "two changes of the decision log — a reading as the source of a fact about a setting in another's service, an invariant names the place of its condition — and a test that the 'decision pending' notes do not return", independent, status `ready for cycle`, frozen copy in the record; decisions as they stand on `foundations` at `0e1cd3c` (the checkout was fast-forwarded from `d40d1cb` at the start); answers of the person who owns the process noted in the task's *Questions to settle*.
- **Process pin:** none; this is the-way itself.
- **Spec:** none; no open design choice (every choice is settled by the task's *Questions to settle* and *Settlements to record*).
- **Route:** one author without a plan, class `same` as the orchestrator's, for a change over several parts of text where a wrong word binds later work; the whole-change review failed once (B1) and passed after one fix; the return step committed one edit, reviewed PASS.
- **Plan:** none on the one-author route.
- **Choices:** 7 other choices, in the questions table of the record: the checkout newer than the task's quotations, the new test's place, the matching of line breaks, "a host or a service" in the rejected clause, the examples in three decisions, the second paragraphs of two decisions, and the pinning test.
- **Blocking findings left:** none.
- **Corrections:** correction 1, remarks `reports/correction-1-remarks.md` (item 14 of the first description), no reset: the branch was not touched; a fresh review passed.
- **Record:** https://github.com/mariusznazar/the-way/blob/e071faceda5d64dd2a498e2099d53fba57e59a57/docs/task-cycles/service-reading-and-invariant-condition/cycle.md.
