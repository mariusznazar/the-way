**State: draft** — waiting for the CI run on the last head, which is the final gate; two items below wait for your answer

## What you will see

Twelve saved decisions of the process stood over the length limit that the check of the foundation now enforces: a paragraph of at most three sentences and 300 words, and at most 600 words for all binding sentences of one decision. After this request none of them is over it, so the check stops listing them and stops halting a change that touches one of them for another reason. Ten decisions are only cut into two or three paragraphs, at the places the task named, with every word kept except one pointer ("first paragraph" became "second paragraph" where it now points to the second one). The long rule about what a script does when a file lacks a field is split into two decisions: the general rule stays where it was, and everything about the command that counts the audit moves to a new decision of its own, in the section about the process audit. The long first sentence of the decision about what a request puts before you is cut into two sentences. Four small fixes ride along: the numbering rule names a part of a question the same way as the rule for writing an entry; the scope of one coding-example decision lists the same parts as its guideline file; one sentence in the guide for work on the process says "these two reports alone"; and in the template of a decision the words about the 600-word limit stand on their own line after the paragraphs.

### Underneath

Only words, line breaks and the numbers in comments and test quotation lines change; no script, test assertion or command behaves differently.

## For you to decide

### Needed from you

none

### Fix or let through

1. The template agents follow when they change a saved decision still describes the numbering rule's "part of a question" in the old words, while the numbering rule now says it the way the rule for writing an entry does: a part of another question, or a part of the entry's own question. Nobody is misled about what to do, since the template's next lines still send the reader to the right section, but an agent that reads only the template meets two names for one thing, and the next person who edits a decision with the template open will see it. Fixing it in this request costs one small change and a round of review; undoing it, nothing. Making a task of it leaves the old words until someone takes the task; undoing it, nothing. Letting it through accepts the two names for now; undoing it, one later line. I recommend making a task of it, since the rules of the template belong to the earlier request about the length check, which this task keeps out. Its weak point: such a task is tiny and may stay on the list for a long time. Fix it in this request, make a task of it, or let it through?
   (Findings outside the task's scope, 1)
2. The review of the whole change opened 8 of the 38 decisions it selected whole. It read the index of its whole selection, but for the ten decisions that were only cut into paragraphs it read their rules and not their reasoning or rejected ways, and for three decisions the task names as unchanged it read only their rules. It judged this safe because it read the whole diff, which shows only blank lines and line breaks there, and because its own word-for-word comparison and the author's found no other change in those decisions. If that is wrong, a changed word in a reasoning of those decisions would go unseen until someone reads it. Having a fresh reviewer read what stayed unread costs one more review round; undoing it, nothing. Making a task of it leaves the gap standing; undoing it, nothing. Letting it through accepts it; undoing it, a later correction if a word turns out changed. I recommend letting it through, since the comparison by script covers the rules of every changed decision and, for the fix, every word of the log. Its weak point: the comparison and the diff were read by the reviewer and the author, not by a third pair of eyes. Read it in this request, make a task of it, or let it through?
   (Checks, 7)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The new decision about the command that counts the audit opens with one sentence saying that it prevails over the general rule in the cases its sentences give, and that in every other case the general rule binds that command; the general rule ends its second sentence with the matching pointer to the new decision. The task asked for the area where the new decision prevails and for the number in the general rule, but not for the words. I did not leave the area unwritten or put it only in the field that links decisions, because a reader of the general rule alone then could not tell where the exception lives. No test holds this one sentence, since a test cannot tell "prevails" from "does not prevail" apart from the cases themselves; the other sentences of the new decision are held by 21 test lines.
4. Two sentences of the general rule's reasoning had to be cut in two to divide it between the two decisions, and the cuts add a few words so that each part reads as a sentence: "Exit code 2 says the file was not read, apart from the count of the audit," opens the part that moved, and "The price:" opens a clause that moved. The task asked each part to keep its wording; no other cut keeps both parts as full sentences. The new decision's reasoning also opens with one sentence, taken from your answer on why this decision grows with every change to the command, and its rejected ways got the two ways you answered against.
5. In the template of a decision, the words "all the binding sentences together at most 600 words" stand on their own line in parentheses after the paragraphs, not in a line in angle brackets. Every angle-bracket line of that template is a paragraph, so an angle-bracket line would have read as a paragraph. Moving the words outside the code block instead would have separated them from the entry form.
6. Tests of the audit command that quoted a sentence of the general rule now quote the matching sentence of the new decision: 21 quotation lines in the audit's test files, and several comments in the audit's code, point to the new decision; six quotation lines at tests of transcripts and generators stay with the general rule. No test was added, dropped or changed in what it asserts, and the check of the foundation, run without skipping test citations, lists nothing.

## Cost

The cycle ran 31 minutes of working time (22 without waiting for tools), 33.1 million tokens in all — 24.9 million on Sonnet 5.5 (orchestrator and author) and 8.2 million on Opus 5.5 (the two reviews) — in one round of review and one fix, and a return step that changed nothing. The table of stages is in the record of the cycle (Course of the cycle, Record).

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then; the repository's merges already work this way.

<details>
<summary>W Twoim języku</summary>

**Stan: wersja robocza** — czeka na przebieg CI na ostatnim commicie, który jest bramką końcową; dwie pozycje niżej czekają na Twoją odpowiedź

## Co zobaczysz

Dwanaście zapisanych decyzji procesu stało ponad limit długości, który pilnuje teraz sprawdzenie fundamentu: akapit najwyżej trzy zdania i 300 słów, a wszystkie zdania wiążące jednej decyzji najwyżej 600 słów. Po tym requeście żadna z nich nie jest ponad limitem, więc sprawdzenie przestaje je wypisywać i przestaje zatrzymywać zmianę, która rusza jedną z nich z innego powodu. Dziesięć decyzji jest tylko pociętych na dwa albo trzy akapity w miejscach, które podało zadanie, i zachowuje wszystkie słowa poza jednym wskazaniem („pierwszy akapit” zmieniło się w „drugi akapit” tam, gdzie reguła stoi teraz w drugim). Długa reguła o tym, co robi skrypt, gdy w pliku brakuje pola, dzieli się na dwie decyzje: reguła ogólna zostaje, a wszystko o komendzie liczącej audyt przechodzi do nowej decyzji w sekcji o audycie procesu. Długie pierwsze zdanie decyzji o tym, co request stawia przed Tobą do rozstrzygnięcia, jest rozcięte na dwa. Przy okazji cztery drobne poprawki: reguła numerowania nazywa część pytania tak samo jak reguła pisania wpisu; zakres jednej decyzji o wzorcowym kodzie wymienia te same części co jej plik wytycznych; jedno zdanie w przewodniku pracy nad procesem mówi „te dwa raporty”; a w szablonie decyzji słowa o limicie 600 słów stoją w osobnej linii po akapitach.

### Pod spodem

Zmieniają się tylko słowa, podziały linii i numery w komentarzach oraz w liniach cytujących w testach; żaden skrypt, żadne sprawdzenie w teście ani żadna komenda nie działa inaczej.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Napraw albo przepuść

1. Szablon, według którego agenci zmieniają zapisaną decyzję, nadal opisuje „część pytania” z reguły numerowania starymi słowami, a sama reguła numerowania mówi teraz tak jak reguła pisania wpisu: część innego pytania albo część własnego pytania wpisu. Nikt nie zostaje wprowadzony w błąd co do tego, co robić, bo dalsze linie szablonu kierują do właściwej sekcji, ale agent, który czyta tylko szablon, trafia na dwie nazwy jednej rzeczy, a następna osoba zmieniająca decyzję z otwartym szablonem to zobaczy. Poprawka w tym requeście kosztuje jedną małą zmianę i turę recenzji; cofnięcie nic. Zrobienie z tego zadania zostawia stare słowa, aż ktoś weźmie zadanie; cofnięcie nic. Przepuszczenie akceptuje na razie dwie nazwy; cofnięcie to jedna późniejsza linia. Rekomenduję zrobić z tego zadanie, bo reguły szablonu należą do wcześniejszego requestu o sprawdzaniu długości, który to zadanie wyłącza. Słaby punkt: takie zadanie jest drobne i może długo leżeć na liście. Poprawić w tym requeście, zrobić z tego zadanie czy przepuścić?
   (Ustalenia poza zakresem zadania, 1)
2. Recenzja całej zmiany otworzyła w całości 8 z 38 wybranych przez siebie decyzji. Przeczytała indeks całego swojego wyboru, ale przy dziesięciu decyzjach, które tylko pocięto na akapity, przeczytała ich reguły, a nie uzasadnienia ani odrzucone warianty, a przy trzech decyzjach, które zadanie wymienia jako niezmieniane, tylko ich reguły. Uznała to za bezpieczne, bo przeczytała cały diff, który pokazuje tam tylko puste linie i łamanie linii, a jej własne porównanie słowo w słowo i porównanie autora nie znalazły żadnej innej zmiany w tych decyzjach. Jeśli to błąd, zmienione słowo w uzasadnieniu którejś z nich zostanie niezauważone, aż ktoś je przeczyta. Przeczytanie tego, co zostało nieprzeczytane, przez świeżego recenzenta kosztuje jeszcze jedną turę recenzji; cofnięcie nic. Zrobienie z tego zadania zostawia lukę; cofnięcie nic. Przepuszczenie to akceptuje; cofnięcie to późniejsza korekta, jeśli okaże się, że jakieś słowo się zmieniło. Rekomenduję przepuścić, bo porównanie skryptem obejmuje reguły każdej zmienionej decyzji, a przy poprawce każde słowo dziennika. Słaby punkt: porównanie i diff czytali recenzent i autor, a nie trzecia para oczu. Przeczytać w tym requeście, zrobić z tego zadanie czy przepuścić?
   (Sprawdzenia, 7)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

3. Nowa decyzja o komendzie liczącej audyt otwiera się jednym zdaniem, że ma pierwszeństwo przed regułą ogólną w przypadkach, które podają jej zdania, a w każdym innym przypadku tę komendę wiąże reguła ogólna; reguła ogólna kończy swoje drugie zdanie odpowiednim wskazaniem na nową decyzję. Zadanie prosiło o obszar, w którym nowa decyzja ma pierwszeństwo, i o numer w regule ogólnej, ale nie o same słowa. Nie zostawiłem obszaru niezapisanego ani nie wpisałem go tylko do pola łączącego decyzje, bo czytelnik samej reguły ogólnej nie wiedziałby wtedy, gdzie stoi wyjątek. Żaden test nie trzyma tego jednego zdania, bo test nie odróżni „ma pierwszeństwo” od „nie ma”, poza samymi przypadkami; pozostałe zdania nowej decyzji trzyma 21 linii testów.
4. Dwa zdania uzasadnienia reguły ogólnej trzeba było rozciąć na dwie części, żeby podzielić je między dwie decyzje, a cięcia dodają kilka słów, żeby każda część czytała się jak zdanie: „Exit code 2 says the file was not read, apart from the count of the audit,” otwiera część, która przeszła, a „The price:” otwiera klauzulę, która przeszła. Zadanie chciało, żeby każda część zachowała brzmienie; żadne inne cięcie nie zostawia obu części jako pełnych zdań. Uzasadnienie nowej decyzji otwiera też jedno zdanie, wzięte z Twojej odpowiedzi o tym, dlaczego ta decyzja rośnie z każdą zmianą komendy, a jej odrzucone warianty dostały dwa warianty, przeciw którym odpowiedziałeś.
5. W szablonie decyzji słowa „all the binding sentences together at most 600 words” stoją w osobnej linii w nawiasie po akapitach, a nie w linii w nawiasach ostrych. Każda linia w nawiasach ostrych tego szablonu jest akapitem, więc linia w nawiasach ostrych czytałaby się jak akapit. Wyniesienie słów poza blok kodu oddzieliłoby je od wzoru wpisu.
6. Testy komendy liczącej audyt, które cytowały zdanie reguły ogólnej, cytują teraz odpowiadające zdanie nowej decyzji: 21 linii cytujących w plikach testów audytu i kilka komentarzy w kodzie audytu wskazuje nową decyzję; sześć linii cytujących przy testach transkryptów i generatorów zostaje przy regule ogólnej. Żaden test nie został dodany, usunięty ani zmieniony w tym, co sprawdza, a sprawdzenie fundamentu uruchomione bez pomijania cytowań testów niczego nie wypisuje.

## Koszt

Cykl zajął 31 minut czasu pracy (22 bez czekania na narzędzia), 33,1 mln tokenów — 24,9 mln na Sonnet 5.5 (orkiestrator i autor) i 8,2 mln na Opus 5.5 (dwie recenzje) — w jednej rundzie recenzji i jednej poprawce, a krok zwrotny niczego nie zmienił. Tabela etapów jest w zapisie cyklu (Przebieg cyklu, Zapis).

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu przetrwa tylko wtedy; scalenia w tym repozytorium już tak działają.

</details>

## Technical changes

- `2f31b30f` — `agent-instructions/README.md` (the words "for these two reports alone") and `elements/decisions/template.md` (the limit of 600 words on its own line in parentheses after the blocks of paragraphs; the angle-bracket form would have read as a paragraph).
- `ef8aa061` — `foundations/decisions.md`: a blank line before the sentence the task's table names in each of WAY-256, 148, 339, 289, 150, 405, 136, 154, 139 and 134 (WAY-154 gets two); WAY-150's pointer "first paragraph" → "second paragraph"; WAY-287's first sentence cut at "— in three groups, headed" into two; WAY-19's name for a part of a question; WAY-391's *Scope*; WAY-344 divided into WAY-344 and the new WAY-416, which stands at the end of the section "Process audit" (*Scope* `process-audit, task-cycle`, *Relations* `narrows WAY-344`); the `decision:` lines of `process-audit/test_audit_count.py` and the comments of `process-audit/audit_count.py`, `process-audit/record_reading.py`, `process-audit/problem_register.py` and `process-audit/SKILL.md` that concern a moved sentence now name WAY-416. No script, test assertion or command changed in what it does; no Python file changed its line count.
- `644cbe51` — the fix of the review's Minor finding within the task: the raw lines of the ten split entries and of WAY-287 rewrapped to 100 columns around the new paragraph breaks, no word changed.

## Checks

- **Final gate:** the CI run on this request's last head; it stands here once it ends. The cycle ran no full gate on its own system, since CI runs on a request into `foundations`.
- **Failing before the change:** none, taken from the merged request https://github.com/mariusznazar/the-way/pull/152, whose CI run on its last head (https://github.com/mariusznazar/the-way/actions/runs/44736608254) passed in both checks; the base `bafe3904` is a merge commit with the tree of its second parent, so no gate ran on the base.
- **The check of the foundation** (`python -B elements/common/foundation_check.py`, no switch): exit 0, `0 errors`, no `listed:` line, on the head `644cbe51`, by the author, the reviewer and the orchestrator; on the base it listed thirteen lines of length.
- **Focused runs** (`python -B gate/run_tests.py <directory>`, exit 0): `process-audit` (277 tests), `agent-instructions`, `elements/common` by the author and the reviewer, `task-cycle` by the author, at `ef8aa061`; no test directory was run on `644cbe51`, which changes line breaks of the log alone.
- **Own-work check:** the author named its weakest point (that every reference to WAY-344 that concerns a moved sentence now names WAY-416, which is a judgement over about ninety references, and the word-for-word comparison) and checked it by a search of the whole repository before and after, each remaining reference read in context, and two comparison scripts, exit 0 each: the ten entries equal the base except one word, and nothing of WAY-344's *Rationale*, *Rejected* or *Verification* dropped or stands in both; the reviewer repeated the comparison with its own script, exit 0.
- **Not run:** `ruff check` and `ruff format --check` (ruff is not installed in the agents' environment; the changed Python lines are comments, a docstring and `decision:` lines, and no Python file changed its line count); the size test of the invariants, since no function or file grew; a walk through a running product, since the change is texts of a decision log, comments and test quotation lines, with no screen or command.
- **Reviews:** whole change `PASS ef8aa061` (0 blocking, 3 Minor: 1 within the task, fixed; 2 outside it), by a reviewer on Opus 5.5 as you asked; the fix `PASS 644cbe51`, 0 new findings; the return step committed nothing, so no review of it ran. The reviewer read 8 of 38 listed decisions whole and ran through all 139 headings.
- **Review of the foundation:** 26 merges since the tag `foundation-review/2026-11-15`, threshold 60: no reminder.
- **Form check** of this description: `python -B task-cycle/request_check.py .runs/task-cycles/shorten-decisions-over-length-limit/request.md --task .runs/task-cycles/shorten-decisions-over-length-limit/task.md` and **check of private paths** on it: `python -B task-cycle/private_paths_check.py .runs/task-cycles/shorten-decisions-over-length-limit/request.md`; their last runs stand here once the description is final.
- **Working copies left:** none. **Directories of earlier tasks kept:** none.

## Foundation entries

Each entry marked `row 1` was written whole from the task's row of *Settlements to record*; the others are the entries the task changes.

- **WAY-416** (`row 1`, new, end of the section "Process audit", *Scope* `process-audit, task-cycle`, *Relations* `narrows WAY-344`): the command that counts the audit, where a file it reads lacks a field, writes its result, gives the values that need the field as unknown, ends with exit code 1 and a line `Error:`, and reads earlier forms of the files as such, where WAY-344 gives exit code 2 for other scripts; in the cases its sentences give it prevails over WAY-344.
- **WAY-344** (changed): the general rule of a missing field stays; the second sentence ends with a pointer to WAY-416.
- **WAY-287** (changed): the first sentence is cut in two at "— in three groups, headed".
- **WAY-19** (changed): the name of a part of a question.
- **WAY-391** (changed): *Scope* `relation-model, process-audit, task-cycle, elements-common`.
- **WAY-256, 148, 339, 289, 150, 405, 136, 154, 139, 134** (changed): a blank line before the sentence the task's table names; WAY-150 also "second paragraph" in place of "first paragraph".

The binding sentences, old and new, in full:

**WAY-344 — before the change** (What does a script of the-way do when a file it reads lacks a field it needs?)

>
> A script of the-way that reads a file an agent or a human writes checks that the file holds each
> field the script needs — a field being any named thing the script looks for data by in the file: a
> section heading, a row label, a table column or a JSON key — and where a field is missing or stands
> under another name the script ends with an error that names it, never guessing and never reading the
> absence as an empty value. The rule binds a script that a change adds and, in a script that a change
> changes, the whole reading of each file whose way of reading the change reworks — every field of that
> file, no other file and no other part of the script — and a missing field ends the script with exit
> code 2 and a message that names the file and the field, except that a script whose purpose is to
> check the form of a file reports a missing field whose presence it checks as a finding of its list,
> with exit code 1, and except that the command that counts the audit, in a file of a cycle's record
> that it reads from git history, gives the values that need a missing field as unknown, writes its
> result and ends with exit code 1 and a line `Error:` that names the file and the field — a field
> that an earlier form of the file never had being no missing field where the command reads the file
> as that form, which it does for a stage report that has no heading of its detailed section and holds
> a table of tokens by model, for one that has neither of its two time lines, and for one whose
> detailed section has no column *Files named*, and which gives the values that need that field as
> unknown, with no line `Error:` and no change of the exit code; a file of a tool that the cycle's own
> change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives
> no line `Error:`. Where a script whose purpose is to check the form of a file reads a copy of the
> file from the commit the branch left the main branch from, a field it needs for a comparison and
> finds missing from that copy is listed by a line `listed:` that names the entry and the field, with
> no error and no change of the exit code. Each reading of a file that the rule covers has one test that gives the file
> without one of the fields it needs and asserts the failure that names that field, the review of the
> change answering for the other fields; the *Scope* names every part of the-way's part map, and a
> change that adds a part to the part map adds it to this *Scope*. The command that counts the audit,
> where a table of weights or a table of the costs of an occurrence in the register of problems lacks
> one of its levels, writes its result, gives the values that depend on the table as unknown and ends
> with exit code 1 and a line `Error:` that names the missing level. Where a stage report has neither
> of the two columns of the cache writes in its detailed section, that command reads the report as an
> earlier form too, with no line `Error:`, giving the cost with the writes standing inside *Input* and
> priced as input, an approximation, and no value unknown for the missing columns, while a stage
> report that has one of the two columns and not the other has a missing field, with the line
> `Error:`. Where the command that counts the audit reads a cycle's record that lacks a line or an
> item it reads of it — the line `Process pin` or `Target branch and base`, or the item `Process
> remarks on the-way`, `Discarded attempt`, `Review rounds`, `Plan` or `Slices returned too large` — the
> record is of an earlier form and no field is missing: the command gives the values that need it as
> unknown, with a reason that names the line or the item, no line `Error:` and no change of the exit
> code. Where the locations file has no key `repository` under `the-way`, no field is missing and
> that command takes the checkout in which its script lies.

**WAY-416 — before the change:** the entry did not exist.

**WAY-287 — before the change** (What does a request put before the human for a decision?)

>
> The section of a request's description for the human's decisions holds everything whose merge needs
> the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks
> not run, the incomplete reading of the review of the whole change where its reviewer did not read
> the index of its whole selection or itself named a decision concerning the change as unread, and the
> gap was not closed on the way by that reviewer, or a fresh one, reading what stayed
> unread, the unfixed findings the product's user or the human working with the process will feel, the
> decisions of the task's own sections, in a blocked request what the cycle needs to go on, the human
> actions, the changed invariant tests, surfaces and *Violated* marks, the additions a change makes to
> a product's logging scope, a listing of the remarks check that the cycle holds wrong (WAY-295), an
> error of the form check that the cycle holds wrong, the pairs that give the cause of a
> correction after the request opened, each descriptive `TODO` in an
> invariant's *Rests on* or *Derives from* or in a decision's *Based on* or *Relations* that stands on
> the main branch after the change (WAY-71), and the foundation entries the human did not see at the task document — in
> three groups, headed *Needed from you*, *Fix or let through* and *You accept by merging*, in this
> order: what the request cannot go on without, an answer or an action of the human; what the cycle did
> not do or did not fix and can still be done in this request, which the human has done there, makes a
> task of or lets through; and what the cycle did within its authority, which the human accepts by
> merging and which waits for no separate answer. Every group stands, reading `none` where it holds no
> item, the items are numbered in one run through the three groups, and the section reads `none` alone
> where no group holds an item, which says that nothing else in the request waits for the human's yes.
> A blocked request keeps the same skeleton, with `blocked` in its first sentence and what the cycle
> needs, in plain words, and the stages it did not run because it stopped, under *Needed from you*,
> while each remaining finding stands with its place in the code in the lower part.
>
> Another decision may add a kind of item to one of the three groups, naming the group, and the
> template of a request's description lists every kind.

**WAY-19 — before the change** (How are decisions numbered?)

>
> A number stands for the question a decision answers, carries the product's prefix and is given
> in the order entries are written; a new question gets the next free number, a question independent
> of every existing entry included, while a part of the question an existing entry answers is a
> sentence of that entry where it cannot change without changing that entry. A new answer to a
> question the log holds rewrites that question's entry. When a new decision answers a question that
> an older one answered in passing, the sentence moves to the new decision, and the older one loses it
> in the same change.

**WAY-344 — after the change** (What does a script of the-way do when a file it reads lacks a field it needs?)

>
> A script of the-way that reads a file an agent or a human writes checks that the file holds each
> field the script needs — a field being any named thing the script looks for data by in the file: a
> section heading, a row label, a table column or a JSON key — and where a field is missing or stands
> under another name the script ends with an error that names it, never guessing and never reading the
> absence as an empty value. The rule binds a script that a change adds and, in a script that a change
> changes, the whole reading of each file whose way of reading the change reworks — every field of
> that file, no other file and no other part of the script — and a missing field ends the script with
> exit code 2 and a message that names the file and the field, except that a script whose purpose is
> to check the form of a file reports a missing field whose presence it checks as a finding of its
> list, with exit code 1, and except that the command that counts the audit is bound by WAY-416 in the
> cases that decision gives, where it prevails over this decision.
>
> Where a script whose purpose is to check the form of a file reads a copy of the file from the commit
> the branch left the main branch from, a field it needs for a comparison and finds missing from that
> copy is listed by a line `listed:` that names the entry and the field, with no error and no change
> of the exit code. Each reading of a file that the rule covers has one test that gives the file
> without one of the fields it needs and asserts the failure that names that field, the review of the
> change answering for the other fields; the *Scope* names every part of the-way's part map, and a
> change that adds a part to the part map adds it to this *Scope*.

**WAY-416 — after the change** (What does the command that counts the audit do when a file it reads lacks a field it needs?)

>
> For the command that counts the audit this decision prevails over WAY-344 in the cases that its
> sentences give, and in every other case WAY-344 binds that command. The command that counts the
> audit, in a file of a cycle's record that it reads from git history, gives the values that need a
> missing field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names
> the file and the field — a field that an earlier form of the file never had being no missing field
> where the command reads the file as that form, which it does for a stage report that has no heading
> of its detailed section and holds a table of tokens by model, for one that has neither of its two
> time lines, and for one whose detailed section has no column *Files named*, and which gives the
> values that need that field as unknown, with no line `Error:` and no change of the exit code; a file
> of a tool that the cycle's own change changed is not read for that cycle (WAY-339), so none of its
> fields is missing and it gives no line `Error:`. The command that counts the audit, where a table of
> weights or a table of the costs of an occurrence in the register of problems lacks one of its
> levels, writes its result, gives the values that depend on the table as unknown and ends with exit
> code 1 and a line `Error:` that names the missing level.
>
> Where a stage report has neither of the two columns of the cache writes in its detailed section,
> that command reads the report as an earlier form too, with no line `Error:`, giving the cost with
> the writes standing inside *Input* and priced as input, an approximation, and no value unknown for
> the missing columns, while a stage report that has one of the two columns and not the other has a
> missing field, with the line `Error:`. Where the command that counts the audit reads a cycle's
> record that lacks a line or an item it reads of it — the line `Process pin` or `Target branch and
> base`, or the item `Process remarks on the-way`, `Discarded attempt`, `Review rounds`, `Plan` or
> `Slices returned too large` — the record is of an earlier form and no field is missing: the command
> gives the values that need it as unknown, with a reason that names the line or the item, no line
> `Error:` and no change of the exit code. Where the locations file has no key `repository` under
> `the-way`, no field is missing and that command takes the checkout in which its script lies.

**WAY-287 — after the change** (What does a request put before the human for a decision?)

>
> The section of a request's description for the human's decisions holds everything whose merge needs
> the human's yes — the cycle's choices beyond the task's content, the steps skipped and the checks
> not run, the incomplete reading of the review of the whole change where its reviewer did not read
> the index of its whole selection or itself named a decision concerning the change as unread, and the
> gap was not closed on the way by that reviewer, or a fresh one, reading what stayed unread, the
> unfixed findings the product's user or the human working with the process will feel, the decisions
> of the task's own sections, in a blocked request what the cycle needs to go on, the human actions,
> the changed invariant tests, surfaces and *Violated* marks, the additions a change makes to a
> product's logging scope, a listing of the remarks check that the cycle holds wrong (WAY-295), an
> error of the form check that the cycle holds wrong, the pairs that give the cause of a correction
> after the request opened, each descriptive `TODO` in an invariant's *Rests on* or *Derives from* or
> in a decision's *Based on* or *Relations* that stands on the main branch after the change (WAY-71),
> and the foundation entries the human did not see at the task document.
>
> The section stands in three groups, headed *Needed from you*, *Fix or let through* and *You accept
> by merging*, in this order: what the request cannot go on without, an answer or an action of the
> human; what the cycle did not do or did not fix and can still be done in this request, which the
> human has done there, makes a task of or lets through; and what the cycle did within its authority,
> which the human accepts by merging and which waits for no separate answer. Every group stands,
> reading `none` where it holds no item, the items are numbered in one run through the three groups,
> and the section reads `none` alone where no group holds an item, which says that nothing else in the
> request waits for the human's yes. A blocked request keeps the same skeleton, with `blocked` in its
> first sentence and what the cycle needs, in plain words, and the stages it did not run because it
> stopped, under *Needed from you*, while each remaining finding stands with its place in the code in
> the lower part.
>
> Another decision may add a kind of item to one of the three groups, naming the group, and the
> template of a request's description lists every kind.

**WAY-19 — after the change** (How are decisions numbered?)

>
> A number stands for the question a decision answers, carries the product's prefix and is given
> in the order entries are written; a new question gets the next free number, a question independent
> of every existing entry included, while a part of another question that an existing entry
> answers, or a part of its own question that it sets apart, is a sentence of that entry where it
> cannot change without changing that entry. A new answer to a
> question the log holds rewrites that question's entry. When a new decision answers a question that
> an older one answered in passing, the sentence moves to the new decision, and the older one loses it
> in the same change.

Where WAY-344's *Verification*, *Rationale* and *Rejected* went, with the sentence each concerns:

Verification (the clause `tests:`), nine clauses of the base, in order:

| # | Clause (start) | Went to | Sentence it concerns |
|---|---|---|---|
| 1 | "that a field missing from a Claude Code transcript … or from the definition of an agent type … exit code 2 … and that each such reading has a test that gives the file without a field" | WAY-344 | second sentence (the rule, exit code 2) and the sentence "Each reading of a file that the rule covers has one test" |
| 2 | "that the command that counts the audit, at a field missing in the file of the measures, the file of the gate times or a stage report, … exit code 1 and a line `Error:`" | WAY-416 | the former rest of WAY-344's second sentence |
| 3 | "that it reads a stage report of an earlier form, one with no heading … or with neither column of the cache writes …" | WAY-416 | the former rest of the second sentence (earlier forms) and the sentence "Where a stage report has neither of the two columns of the cache writes" |
| 4 | "that it reads a report that has one time line or one of the two cache write columns and not the other as a missing field" | WAY-416 | the same two sentences |
| 5 | "that it reads a cycle's record that lacks the line `Process pin` or `Target branch and base` or an item it reads of it …" | WAY-416 | "Where the command that counts the audit reads a cycle's record that lacks a line or an item" |
| 6 | "that a table of weights or of the costs of an occurrence which lacks a level gives the result, unknown values and the line `Error:`" | WAY-416 | "The command that counts the audit, where a table of weights …" |
| 7 | "that a locations file with no key `repository` under `the-way` gives the checkout in which the script lies and no line `Error:`" | WAY-416 | "Where the locations file has no key `repository` under `the-way`" |
| 8 | "that the check of the foundation lists an invariant whose sentence the change reworded and whose copy at the commit the branch left lacks its *Method* or its *Part* …" | WAY-344 | "Where a script whose purpose is to check the form of a file reads a copy of the file …" |
| 9 | "that the file of a tool the cycle's own change changed is not read" | WAY-416 | the former rest of the second sentence ("a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339)") |

The pair of examples (*complies* four, *violates* six) stays whole in WAY-344, the violating example "a script that is neither a check of form nor the count of the audit lists an absent field as an item with exit code 1" included, as the settlement says; WAY-416 has no pair. The clauses 1 and 8 got "and" before the last one in WAY-344; the clauses of WAY-416 keep their words.

Rationale, thirteen sentences of the base, in order:

| # | Sentence (start) | Went to | Sentence it concerns |
|---|---|---|---|
| 1 | "a script that reads a file an agent writes meets a changed format as an absent field …" | WAY-344 | the first sentence |
| 2 | "The coding guidelines of the-way point to this rule …" | WAY-344 | the first sentence |
| 3 | "An error naming the field lets the author … exit code 2 says the file was not read, apart from a listing of findings … and apart from the count of the audit, whose file in the history of git …" | **cut at the clause boundary before ", and apart from the count of the audit"**: first part WAY-344 (the second sentence, exit code 2 and the check-of-form exception), second part WAY-416 (the former rest of the second sentence) | both |
| 4 | "A field that an earlier form of a file never had is no loss of the file …" | WAY-416 | the former rest of the second sentence |
| 5 | "The record of a cycle is such a file …" | WAY-416 | "Where the command that counts the audit reads a cycle's record …" |
| 6 | "The rule covers the whole reading of a file a change reworks …" | WAY-344 | the second sentence and the test per reading |
| 7 | "The price: a change that reworks the reading of a file pays …; a stage report that has lost its two time lines …, where the rule alone would give an error; an existing script that no change touches stays as it is …; and the review alone answers …" | **cut at the clause boundaries**: "The price: … every field of that file; an existing script … gives up." stays in WAY-344; "a stage report that has lost … would give an error" goes to WAY-416 | the clause of the stage report concerns the former rest of the second sentence; the others concern the rule |
| 8 | "Tests of a script's behaviour stand without an invariant, since WAY-12 …" | WAY-344 | the *Verification* of the rule |
| 9 | "A table of the register of problems that lacks one of its levels …" | WAY-416 | "The command that counts the audit, where a table of weights …" |
| 10 | "The key `repository` under `the-way` is the one key …" | WAY-416 | "Where the locations file has no key `repository` under `the-way`" |
| 11 | "The exception is written for that key alone …" | WAY-416 | the same |
| 12 | "A stage report with neither column of the cache writes was written before the columns existed …" | WAY-416 | "Where a stage report has neither of the two columns of the cache writes" |
| 13 | "A copy of a file at the commit the branch left is a file no change can mend …" | WAY-344 | "Where a script whose purpose is to check the form of a file reads a copy …" |

Words the two cuts add so that each part reads as a sentence: in WAY-416 the head "Exit code 2 says the file was not read, apart from the count of the audit," (the first part in WAY-344 keeps "exit code 2 says the file was not read, apart from a listing of findings, which a caller carries out as findings.") and the head "The price:" before the clause of the stage report; the full stop and the "and" at the cuts differ. A script of my own compared the multisets of words (see below): nothing of the base *Rationale* is dropped; the additions are those two heads, the full stops, and the writer's sentence (b) above.

Rejected, sixteen ways of the base, in order:

| # | Way (start) | Went to | Sentence it concerns |
|---|---|---|---|
| 1 | "the rule as a sentence of WAY-379" | WAY-344 | the first sentence |
| 2 | "the rule as a decision with an invariant whose *Part* is `every`" | WAY-344 | the first sentence |
| 3 | "the whole script as what a changed script brings under the rule" | WAY-344 | the second sentence |
| 4 | "only the readings of fields that the change adds or reworks" | WAY-344 | the second sentence |
| 5 | "review alone with the test left to the choice of the cycle" | WAY-344 | "Each reading … has one test" |
| 6 | "review and a test for every field" | WAY-344 | "Each reading … has one test" |
| 7 | "exit code 1 always, a missing field as an item of the list" | WAY-344 | the second sentence (exit code 2, the check of form) |
| 8 | "a new exit code, such as 3" | WAY-344 | the second sentence |
| 9 | "exit code 2 with no result for the count of the audit" | WAY-416 | the former rest of the second sentence |
| 10 | "the exception for the stage report alone, the file of measures and the file of gate times keeping exit code 2" | WAY-416 | the former rest of the second sentence |
| 11 | "for a table of the register of problems that lacks a level, exit code 2 with the level named and no result" | WAY-416 | "The command that counts the audit, where a table of weights …" |
| 12 | "for the key `repository` under `the-way`, exit code 2" | WAY-416 | "Where the locations file has no key `repository` …" |
| 13 | "for the same key, a general exception for a field whose absence the description of a script allows with a default" | WAY-416 | the same |
| 14 | "for a generator of copies that shares its exit codes with another script, an exception written into this decision" | WAY-344 | the second sentence (its list of exceptions) |
| 15 | "for a field missing from the copy at the commit the branch left, an exception that leaves the invariant out with no word" | WAY-344 | "Where a script whose purpose is to check the form of a file reads a copy …" |
| 16 | "the same case left as the cycle that wrote the check left it, with no sentence" | WAY-344 | the same |

WAY-416's *Rejected* adds, after the five moved ways, the two ways of the question "Co zrobić z WAY-344": the cases kept in WAY-344 and divided into paragraphs only; a decision for each case of the command that counts the audit.

## Minor findings

Minor 3 of the review of the whole change (the raw lines of the new paragraph breaks) was fixed in `644cbe51`; the review of the fix found no new finding, so nothing stays here.

## Findings outside the task's scope

1. `elements/decisions/template.md:210-213` — the template's "Changing a decision" still states WAY-19 with the old name of the part: "A part of the question an existing entry answers is a sentence of that entry, in a paragraph of its own as "Binding sentences" gives, where it cannot change without changing that entry … (WAY-19)". After this change WAY-19 names the two kinds: "a part of another question that an existing entry answers, or a part of its own question that it sets apart". The template points to "Binding sentences", which tells the two kinds apart, so a reader is not misled about what to do. (The reviewer's words, shortened to the quoted lines; the author observed the same.)
2. `process-audit/test_audit_count.py:2036` — the docstring of `StagesForms` cites "the settlement 6 of the task", the task document of an earlier cycle, which no reader of the repository can open; the change only replaced `WAY-344` with `WAY-416` on that line, and the citation was already there at the base.

## Course of the cycle

- **Task and sources:** the task "the way: skrócić 12 zapisanych decyzji, które stoją ponad nowy limit długości" (independent), frozen from its note in the author's backlog; it rests on the merged request #152, which brought the length check.
- **Process pin:** none (the-way is the top-level repository); the gate on the base was not run: the base is a merge commit with the tree of its second parent, and the list of failing tests (none) is taken from #152.
- **Spec:** none: the task settles every choice that bears on the change.
- **Route:** one author without a plan; one author (`the-way-author`, Sonnet 5.5, class `same`) made the whole change, the foundation entry and the return step; the reviews ran on Opus 5.5.
- **Plan:** none.
- **Choices:** 6 choices of the cycle, in the record's table of questions and choices.
- **Blocking findings left:** none.
- **Record:** the link to the record by the SHA of the commit that adds its copy follows in the next edit of this description; the commit does not exist yet
