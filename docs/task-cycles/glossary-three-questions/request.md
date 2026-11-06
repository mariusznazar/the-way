**State: ready** — the change is reviewed and every test passes; four items below wait for your yes.

## What you will see

Three questions the glossary rules left open now have answers, and one more rule says how a reviewer's remark about a word is graded.

- **A word a product uses more narrowly than its field does** gets a glossary entry only where a reader who takes the field's meaning would misread a sentence of the product's files. Before, the rules did not say whether a narrower meaning counted at all.
- **A word of the process that also has an everyday meaning** — "sentence" in a decision log, for instance — gets a qualifier in a product's foundation only where a sentence of its files could be read in the other meaning, in either direction. Before, every bare use needed one, which in a real product meant rewriting dozens of lines that nobody misreads.
- **Two uses of a word carry two meanings** when a sentence the files already hold is true for one use and false for the other. The unfinished placeholder in the glossary template, which named a test built on definitions, is replaced by this test. A sentence made up for the occasion does not count.
- **The glossary rules bind English text.** A file in another language, such as Polish coding guidelines, keeps its words in that language's meaning, and the rules do not reach into it.
- **A reviewer's remark that a word needs a glossary entry or a qualifier is graded Minor**, so it reaches you at the merge instead of blocking the change, unless it cites a sentence a reader would misread; then it is graded like any other remark. Renaming a word that carries two meanings, and a glossary entry the change itself writes, are graded as before.

What you should notice: the dispute over one word that cost a blocking remark and an extra round of fixes in an earlier cycle has a rule to decide it, and the cycle no longer rewrites bare words in a product's log for the sake of the rule alone.

### Underneath

Five decisions of the log were rewritten in place and one new decision, the grading rule, was added. The glossary template and the reviewer's skill say the same, and three more places that repeated the old wording were brought in line.

## For you to decide

1. **One rule about what the last step of a cycle writes into the glossary was reworded, though no row of the task named it.** It said a word used "in a meaning other than the usual one" is written up. That is broader than the narrowed rule on which words take an entry, so the cycle made it point at the narrowed rule; the same phrase in two cycle files was changed the same way. Accept? (Foundation entries, 6)
2. **The reason given for refusing one older option goes a clause beyond what the task asked.** The task asked that the option "mark the domain meaning beside the bare word and report a warning" stay among the refused ones, with the reason its cost is now acceptable. The text gives that reason and adds that the option stays refused where a sentence can be read both ways. The task's words "its cost" can mean the option's cost or the new rule's; the cycle took the first. Accept? (Minor findings, 3)
3. **Two rules about the same thing now disagree for levels of tests.** The rule for naming test levels still says that a level named differently from its use in the field always gets a glossary entry, while the narrowed rule gives an entry only where a sentence would be misread. The task named neither, so the cycle left it. Make a task of it? (Findings outside the task's scope, 1)
4. **The report of the single fix after the first review has no own-work check.** The first review found two defects of form; the fix was two small edits that the reviewer's own words name, and a second review passed it. The fix's report has no section where its author names the requirement most likely unmet. The cycle did not send it back, since the method's rules for a fix ask for no such section. Merge without it?

## Cost

About 28 minutes of working time by the table of stages; the three full test runs ran in the background and are not counted. The orchestrator and every agent ran on one model, Claude Sonnet 5.5, using 23.6 M tokens, of which 22.6 M were input read from cache and 0.16 M output. Review rounds: the whole change was reviewed once (two blocking findings), fixed once, and the fix reviewed once and passed; the merge with the target branch was reviewed once and passed; the return step committed nothing, so it had no review; no spec and no plan. The table of stages: https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/glossary-three-questions/stages.md

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowy** — zmiana przeszła przegląd i wszystkie testy; cztery punkty niżej czekają na Twoje „tak”.

**Co zobaczysz**

Trzy pytania, które reguły słownika zostawiały otwarte, mają teraz odpowiedź, a jedna reguła więcej mówi, jak ocenia się uwagę recenzenta o słowie.

- **Słowo użyte w produkcie węziej niż w branży** dostaje wpis w słowniku tylko tam, gdzie czytelnik biorący znaczenie branżowe przeczytałby zdanie plików produktu błędnie. Wcześniej reguły nie mówiły, czy węższe znaczenie w ogóle się liczy.
- **Słowo procesu, które ma też zwykłe znaczenie** — na przykład „sentence” w dzienniku decyzji — dostaje dookreślenie w fundamencie produktu tylko tam, gdzie zdanie jego plików dałoby się przeczytać w drugim znaczeniu, w którąkolwiek stronę. Wcześniej dookreślenia wymagało każde gołe użycie, co w prawdziwym produkcie oznaczało przepisywanie dziesiątek wierszy, których nikt nie czyta błędnie.
- **Dwa użycia słowa niosą dwa znaczenia**, gdy zdanie, które pliki już zawierają, jest prawdziwe dla jednego użycia i fałszywe dla drugiego. Niedokończony szkic w szablonie słownika, oparty na definicjach, zastępuje ten test. Zdanie wymyślone na potrzeby sprawy się nie liczy.
- **Reguły słownika wiążą tekst angielski.** Plik w innym języku, na przykład polskie wytyczne kodowania, zachowuje słowa w znaczeniu tego języka, a reguły go nie obejmują.
- **Uwaga recenzenta, że słowo potrzebuje wpisu w słowniku albo dookreślenia, jest oceniana jako Minor**, więc trafia do Ciebie przy scaleniu, zamiast wstrzymywać zmianę — chyba że wskazuje zdanie, które czytelnik przeczytałby błędnie; wtedy jest oceniana jak każda inna. Zmiana nazwy słowa o dwóch znaczeniach i wpis słownika, który zmiana sama pisze, są oceniane jak dotąd.

Co powinieneś zauważyć: spór o jedno słowo, który w wcześniejszym cyklu kosztował uwagę blokującą i dodatkową rundę poprawek, ma regułę, która go rozstrzyga, a cykl nie przepisuje już gołych słów w dzienniku produktu wyłącznie dla samej reguły.

*Pod spodem:* pięć decyzji dziennika przepisano w miejscu i dodano jedną nową, regułę oceny. Szablon słownika i skill recenzenta mówią to samo, a trzy kolejne miejsca, które powtarzały dawne brzmienie, dopasowano.

**Do Twojej decyzji**

1. **Jedna reguła o tym, co ostatni krok cyklu zapisuje w słowniku, dostała nowe brzmienie, choć żaden wiersz zadania jej nie wymieniał.** Mówiła, że zapisuje się słowo użyte „w znaczeniu innym niż zwykłe”. To szerzej niż zawężona reguła o tym, które słowa dostają wpis, więc cykl odesłał ją do zawężonej reguły; to samo zdanie w dwóch plikach cyklu zmieniono tak samo. Akceptujesz? (Foundation entries, 6)
2. **Powód odrzucenia jednej starszej opcji wychodzi o jedną klauzulę poza to, o co prosiło zadanie.** Zadanie chciało, żeby opcja „zaznacz znaczenie domenowe obok gołego słowa i zgłoś ostrzeżenie” została wśród odrzuconych, z powodem, dla którego jej koszt jest teraz do przyjęcia. Tekst podaje ten powód i dodaje, że opcja zostaje odrzucona tam, gdzie zdanie da się przeczytać na oba sposoby. Słowa zadania „jego koszt” mogą znaczyć koszt opcji albo nowej reguły; cykl wziął pierwsze. Akceptujesz? (Minor findings, 3)
3. **Dwie reguły o tej samej sprawie nie zgadzają się teraz dla poziomów testów.** Reguła nazywania poziomów testów nadal mówi, że poziom nazwany inaczej niż w branży zawsze dostaje wpis w słowniku, a zawężona reguła daje wpis tylko tam, gdzie zdanie zostałoby źle przeczytane. Zadanie nie wymieniało żadnej z nich, więc cykl zostawił to. Robimy z tego zadanie? (Findings outside the task's scope, 1)
4. **Raport z jedynej poprawki po pierwszym przeglądzie nie ma sprawdzenia własnej pracy.** Pierwszy przegląd znalazł dwa błędy formy; poprawką były dwie małe zmiany, które nazywają słowa samego recenzenta, a drugi przegląd ją przepuścił. W raporcie poprawki nie ma sekcji, w której autor wskazuje wymaganie najbardziej narażone na niespełnienie. Cykl nie odesłał go do uzupełnienia, bo zasady metody dla poprawki takiej sekcji nie żądają. Scalić bez tego?

**Koszt**

Około 28 minut pracy według tabeli etapów; trzy pełne przebiegi testów szły w tle i nie są liczone. Prowadzący cykl i wszyscy agenci pracowali na jednym modelu, Claude Sonnet 5.5, i zużyli 23,6 mln tokenów, z czego 22,6 mln to wejście czytane z pamięci podręcznej, a 0,16 mln to wyjście. Rundy przeglądu: cała zmiana przejrzana raz (dwie uwagi blokujące), poprawiona raz, poprawka przejrzana raz i przepuszczona; uzgodnienie z gałęzią docelową przejrzane raz i przepuszczone; krok powrotu nic nie zacommitował, więc bez przeglądu; bez specyfikacji i bez planu. Tabela etapów: https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/glossary-three-questions/stages.md

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The decision log now answers the three open questions and grades remarks about words.** `24e092c` rewrote WAY-95, WAY-97, WAY-99 and WAY-104 in place, changed the phrase of WAY-11 that restated the old rule, and added a decision on grading. `049e84e` fixed two defects of form the whole-change review found: WAY-104's binding paragraph went back to three sentences, and the word "should" left the grading decision's binding sentence. The merge `826fff2` renumbered the grading decision, see item 4. The sentence test of the task's question on two meanings stands in WAY-99, which already speaks of a word carrying two meanings; the English-text limit stands there too, with WAY-95 and WAY-97 referring to it.
2. **The glossary template says the same rules in its own words.** `24e092c`: "Two glossaries" (the qualifier rule as a sentence test), "Which words take an entry" (narrower meaning; the sentence test replaces the old `TODO — decision pending` line), the English-text limit and "A changed meaning" (the search covers English text). `elements/common/way_of_working.md` and `elements/glossary/skill/decide_entry.md` restated the old rule more broadly and were brought in line.
3. **The reviewer's skill grades a remark about a word as Minor unless it cites a misread sentence.** `24e092c`: one paragraph added to section 3 of `task-cycle/review/SKILL.md` after the paragraph on departures from an entry the change writes; that paragraph is untouched. `task-cycle/record_template.md` and `task-cycle/skill/return_step.md` repeated the old phrase of WAY-11 and say what WAY-11 now says.
4. **The grading decision is WAY-297, not WAY-293.** While the task ran, the target branch merged a decision of its own numbered WAY-293 (and WAY-294 to WAY-296). The merge `826fff2` kept the target's entries byte for byte and gave this task's decision the next free number, WAY-297, and changed its one reference in `task-cycle/review/SKILL.md`. The message of `24e092c` still says WAY-293; the history was not rewritten, because the record and the reports refer to those commits.

## Checks

- Full test run on the final tree (merge `826fff2`): `python -B gate/run_tests.py`, exit 0, "714 tests in 8 directories; every directory passed"; no check failed or did not run. On the base `61c72fb`: exit 0, 667 tests, nothing failing there. On the reviewed change `049e84e`, before the merge: exit 0, 667 tests.
- Focused checks reported by the author and rerun after the merge: `python -B elements/common/foundation_check.py .` — "0 errors"; `python -B gate/run_tests.py task-cycle` — 139 tests OK, exit 0; `python -B gate/run_tests.py elements/common` — 109 tests OK, exit 0. The reviewers ran the same checks in separate worktrees of the head, exit 0.
- Own-work check of the author: the requirement most likely unmet was that the test works in both directions and only on sentences the files already hold, in each place it stands. It read each of the three places for both directions, searched the repository for the old rule's phrases, applied the new text to the task's two examples, and compared the unchanged paragraph of the grading rule byte for byte. All four held; what the text leaves open is whether "could be read" asks for a plausible reader's confusion or any logical possibility.
- Neither the fix nor the return step has an own-work check of its own (For you to decide, 4). No check was left undone: no user interface is involved, so there are no states or screenshots.
- Form check of this description: see *Course of the cycle*, Record. The process remarks check: `python -B task-cycle/remarks_check.py .runs/task-cycles/glossary-three-questions`, exit 0, "checked: 6 reports, 16 items other than none, 0 not in the process remarks"; four runs, the first of which read no report because the reports were not named `*report.md` (renamed, and entered in the process remarks).

## Foundation entries

1. **WAY-95 (row 1), rewritten in place:** A word the product uses more narrowly than its field takes a glossary entry only where a reader taking the field's meaning would read a sentence of the product's English files wrongly.
2. **WAY-97 (row 5), narrowed in place:** The search that follows a changed definition covers the English text of the files git tracks, not text in another language.
3. **WAY-99 (rows 3 and 5), rewritten in place:** Two uses of a word carry two meanings when a sentence the files hold is true in the meaning of one use and false in the meaning of the other, either way and never on a made-up sentence; the glossary rules bind English text, a file in another language keeping its words in that language's meaning.
4. **WAY-104 (row 4), rewritten in place:** A word of the glossary of the-way, or the last word of its term, takes a qualifier in a sentence of a product's foundation that could otherwise be read in the other meaning, in either direction; a bare use no sentence reads two ways stays bare.
5. **WAY-297 (row 2), new:** A reviewer grades a finding about a missing glossary entry or missing qualifier as Minor unless it cites a sentence a reader would read wrongly; the renaming of a word with two meanings is graded as before, and a glossary entry the change writes stays under the rule on departures from an entry the change writes.
6. **WAY-11 (the cycle's), one phrase changed in place:** the glossary words the last step of a cycle writes are those for which WAY-95 gives an entry, not any "meaning other than the usual one".

No invariant test, no surface and no *Violated* mark is changed.

## Minor findings

The reviewer's words are copied as written, at the reviewed head `24e092c`: the places and line numbers are those of that commit, and the reviewer calls the grading decision WAY-293, its number then; it is WAY-297 now (Technical changes, 4), and WAY-293 is a decision of the target branch.

1. **The new sentence in the reviewer's grading rules sits in the same paragraph as the rule before it and is worded a little differently from the decision it restates; no wrong grade follows.**
   Reviewer's words (M1 — the review skill's new sentence points at "the paragraph above", but it is the same paragraph, and it is vaguer than WAY-293):

   - Place: `task-cycle/review/SKILL.md:113-117`.
   - The new sentences follow the WAY-263 sentence with no blank line (`git diff` context shows
     `qualification (WAY-263).` directly followed by `+A finding that a word`), so they sit in one Markdown paragraph with
     the WAY-263 sentence; "graded as the paragraph above gives" then points at the previous block (lines 105-112 in
     the same paragraph, or the grade list above it). Also, WAY-293 says what stays Important ("a finding that a
     glossary entry the change writes or changes departs from a foundation entry"), whereas the skill says only that such
     an entry "is graded as the paragraph above gives" — no wrong grade follows, because WAY-263 grades only departures
     and other findings fall to the general grades, but the skill is a second account of WAY-293 in different words.
     Suggested: "a finding that a glossary entry the change writes or changes departs from a foundation entry stays
     Important (WAY-263)". Minor: the reader of the skill ends in WAY-263 and WAY-293 either way.

2. **Some examples in the glossary decisions show only one direction of the new test, so a reader of the examples alone would miss the other.**
   Reviewer's words (M2 — WAY-104 *Verification* examples do not match the binding text everywhere):

   - Place: `foundations/decisions.md:2262-2278` (WAY-104 *Verification*); `:2030-2037` (WAY-95 *Verification*).
   - Third `violates` item of WAY-104: "every bare "map" of a game's decisions is rewritten to a phrase though no sentence
     reads it as the part map". The binding text says where a qualifier is taken and that a bare use no sentence reads
     otherwise "keeps the meaning it has there"; it does not forbid a qualifier elsewhere, so an agent comparing a change
     that qualifies such a "map" finds no violated sentence. The `complies` list shows only the domain-use direction
     (a bare process use readable as the domain's is not shown), although the binding text and the task carry both
     directions. WAY-95's `complies` list adds a game's "map" as a case that "takes none"; that is the field's own
     meaning, not a narrower one, and shows nothing of the new rule.
   - Minor: polish of examples; the binding text is clear.

3. **The reason given for refusing the older "warning" option goes one clause beyond what the task asked (see For you to decide, 2).**
   Reviewer's words (M3 — WAY-104 *Rejected*, item "reported as a warning rather than an error": the task's reason is there, plus a tail the task does not give):

   - Place: `foundations/decisions.md:2285-2289`.
   - The task asks the variant to stay in *Rejected* "z powodem, dla którego jego koszt jest teraz do przyjęcia". The
     text gives "one word carrying two meanings in the repository is a cost now accepted where no sentence reads in the
     other meaning" — the reason, as the orchestrator read it. It then adds "but the variant stays refused where a
     sentence can be read both ways, since a mark beside the word tells the reader nothing at the use". That second
     half is the author's own reasoning, not a reason the task commands (WAY-134: nothing added that the task does not
     settle), and the author reports the instruction as ambiguous (placement choice d). If the human meant the cost of
     the new rule instead, one clause changes.
   - Minor: a clause of one item; the decision's binding text is unaffected. Worth showing the human at the merge.

4. **Two places still say "the files git tracks" without "English", so they read as if the rules reached files in any language.**
   Reviewer's words (M4 — "files git tracks" without "English" remains in the template's *Not* bullet and in WAY-94):

   - Place: `elements/glossary/template.md:85` ("each meaning the word carried in the files git tracks"),
     `foundations/decisions.md:1993` (WAY-94: "carries or carried in the files git tracks").
   - To do 3 asks the glossary template narrowed to English text; the sentence added at `template.md:69-72` says "The
     rules above bind English text", and the *Not* bullet is below it, so the bullet reads as unbounded. The author
     left WAY-94 and this bullet as outside the task's list (report, "Looked at and left alone"); the template bullet is
     in a file the task names. Minor: the meanings of a Polish file would not be recorded under the new rule anyway.

5. **Several short summaries still state the first clause of the old rule without its new limit; the files lead on to the limit, so a reader is not misled for long.**
   Reviewer's words (M5 — the first clause of WAY-95 is still restated without the narrower-meaning limit in several files):

   - Place: `elements/glossary/skill/decide_entry.md:3-5` (a file the change edits at line 10), `elements/glossary/template.md:3-5, 46-47`,
     `elements/glossary/skill/SKILL.md:3` (description), `README.md:39, :76`.
   - Each says a word "that means in the product something other than a reader ... takes it to mean" takes an entry.
     WAY-95 now says a narrower meaning takes one only where a sentence is read wrongly. In the template the limit stands
     in the next bullet, and `decide_entry.md` sends the word through "Which words take an entry" in its next steps, so
     the files lead to the limit; the description and README are summaries. By WAY-293 itself a finding of this kind
     without a read-wrongly sentence is Minor; I cite none. The author's choice not to touch the skill description (it
     would need `skill_entry_points.py --write`) is reasonable. Minor.

6. **The rule on process words says "only" in its second sentence, not in the sentence that names the qualifier, so its force must be read from both.**
   Reviewer's words (M6 — the WAY-104 binding text does not say "only" where the task does):

   - Place: `foundations/decisions.md:2251-2256`. Row 4 says the process word gets a qualifier "tylko tam, gdzie" a
     sentence could be read in the second meaning. The entry says the word "takes a qualifier in a sentence ... that
     could otherwise be read in the other meaning" and, in the next sentence, that a bare use no sentence reads
     otherwise "keeps the meaning it has there"; the "only" is carried by the second sentence and by the *Rationale*
     ("qualifying it would only add words"), not by the binding sentence that names the qualifier. Together with M2
     (third `violates`) this leaves the force of "only" to be inferred. Minor: it reads correctly once both sentences are
     read; the fix for F1 (merging sentences 1 and 2) can carry it.

## Findings outside the task's scope

1. **The rule on naming test levels still asks for a glossary entry more broadly than the narrowed rule does (see For you to decide, 3).**
   Reviewer's words (O1 — WAY-240 and the testing-guidelines files state the "something other than in the field" rule for test levels without the narrowed limit of WAY-95):

   - Place: `foundations/decisions.md:6885-6910` (WAY-240 binding sentence and *Rationale* citing WAY-95),
     `product-guidelines/testing/settle.md:8-10`, `product-guidelines/testing/template.md:110-113`.
   - WAY-240 requires a level whose name means in the product something other than in the field a glossary term and
     cites WAY-95 for it. After this change WAY-95 gives a narrower meaning an entry only where a sentence is read wrongly.
     WAY-240 is a rule of its own for test levels ("integration above all", defined by the resources a test may touch),
     not a restatement of WAY-95, so the two can be read together (a level defined by resources is read differently in
     sentences such as "integration tests may touch files"); but if they ever collide, no precedence is recorded
     (WAY-25). The task does not name it; the author reported it. A task for the human to create or decline.

## Course of the cycle

- **Task and sources:** an independent task, accepted 2026-11-05: three open questions of the glossary rules, answered by the human, and the rules that follow from them. Its sources are the task document and the foundation at `61c72fb`; the target branch moved to `2692e05` during the cycle and was merged in.
- **Process pin:** this repository is the product, so the pin is its own commit `61c72fb`; no pin was moved.
- **Spec:** none — all five questions of the task carry the human's answers and the ways not chosen, so no open design choice stood.
- **Route:** one author without a plan, on the class `same` as the orchestrator (Claude Sonnet 5.5): the change rewrites binding wording that every later review grades by, so the cheaper default was not taken. No attempt was discarded.
- **Plan:** none.
- **Choices:** 6 rows in the questions table, none of which reaches *For you to decide*; items 1 and 2 there come from the author's report. The table is in the record.
- **Blocking findings left:** none. The first review found two blocking findings, both of form — WAY-104 with four binding sentences where the template allows one to three, and the word "should" in the grading decision — both fixed in `049e84e` and passed by the review of the fix.
- **Record:** https://github.com/mariusznazar/the-way/tree/RECORD_SHA/docs/task-cycles/glossary-three-questions/cycle.md
