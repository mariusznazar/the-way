**State: ready** — the change is reviewed and every test passes; ten items below wait for your yes.

## What you will see

Every pull request a task cycle opens, and every pull request to the-way itself, will look the same.
Its first sentence says whether it is ready, a draft or blocked, and why. Next comes what changes, in
plain words. Then one section, *For you to decide*, holds everything whose merge needs your yes: the
choices the cycle made beyond the task, steps it skipped and checks it did not run, review remarks
you or a user would feel, and the decision-log entries you did not see while the task was refined.
When that section reads `none`, nothing else waits for you. Then the cost of the cycle and how to
merge. The same top part follows once more in Polish, in a collapsed block. Below it stands an
archive for agents and for a closer look. It always has the same sections in the same order, and
every item opens with a sentence you can follow without reading the code.

You are no longer asked at the merge about the entries you accepted while the task was refined.
A script checks the shape of the description before the request opens, and the cycle fixes what it
reports. Where the cycle thinks the script is wrong, the request opens as a draft and asks you.

### Underneath

A single template for the description, which the cycle and the-way's own pull requests both read.
A script with its tests, run by the full test run. Six new decisions and three changed ones on what
a request shows and what you accept at the merge.

## For you to decide

1. **The cycle does not hide a form error it thinks is wrong.** When the shape-checking script reports
   an error the cycle holds false, the cycle leaves the description as it is. It never empties or
   translates the Polish block to make the error go away. The request opens as a draft and asks you
   whether to merge anyway. The cycle added this rule, which no row of the task holds. Accept?
   (Foundation entries, 9)
2. **A task written in English gets no Polish block.** Where the task document is in English, the
   collapsed block holds only `none`, since the top part is already in that language. The cycle
   added this rule; the task's row says only "in the task's language". Accept? (Foundation
   entries, 10)
3. **The process now relies on GitHub keeping the block collapsed.** The cycle recorded this fact
   from GitHub's documentation, so that a later change on GitHub's side shows which decision it
   breaks. Accept? (Foundation entries, 11)
4. **Four explanations in the decision log were brought in line with the new rule on what you accept
   at the merge.** They concern the reasons and examples of older decisions, not what those
   decisions require. Accept? (Foundation entries, 12–15)
5. **The headings are in English and are fixed:** *What you will see* with *Underneath*, *For you to
   decide*, *Cost*, *How to merge*; the Polish block is titled "W Twoim języku". The task left the
   wording to the cycle. Accept?
6. **The Polish block stands right after *How to merge*, not at the very end of the description.**
   It is the part you read, so it sits where you stop reading. The task's sentence can be read
   either way. Accept?
7. **Which of the cycle's own choices reach this section.** Only a choice where another answer would
   change what a user of the product sees or does, what you meet when you work with the process, or
   what the decision log binds. The rest are only counted in the archive, with a link to the full
   table. Accept?
8. **How the script tells English from Polish.** It counts common English words that are not also
   Polish words. A text where they make up a fifth or more of the words, and which has at least 20
   words, counts as English. On 57 task documents in your notes the share was at most 0.14, and on
   the English parts of recent pull requests 0.37–0.41. A Polish task full of quoted English names
   could cross the line. Then the request opens as a draft and asks you (item 1). Accept?
9. **Additions to a product's logging rules may now pass without your noticing.** A decision says
   you see such an addition at the merge, but this section does not list it, and you now read only
   this section. Make a task of it? (Minor findings, 3)
10. **Two small gaps in the script you could run into.** A description saved by PowerShell with an
    invisible mark at its start fails with a puzzling error on its first line, which can turn a
    ready request into a draft for no reason. And a placeholder heading copied from the template
    passes the check, so you could see a section titled `<…>`. Make a task of them? (Minor findings,
    1 and 2)

## Cost

About 1 h 35 min of working time. All agents and the orchestrator ran on one model, Claude Opus 5.5,
using 74.8 M tokens, of which 72.2 M were input read from cache and 0.39 M output. Review rounds:
the spec was reviewed twice (one revision); the whole change was reviewed, fixed once and reviewed
again; the return step was reviewed once. The table of stages: see *Record* under *Course of the
cycle*, file `stages.md`.

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this
branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowy** — zmiana przeszła przegląd i wszystkie testy; dziesięć punktów niżej czeka na Twoje „tak”.

**Co zobaczysz**

Każdy PR z cyklu zadania i każdy PR do samego the way będzie wyglądał tak samo. Pierwsze zdanie
mówi, czy jest gotowy, czy to szkic, czy jest zablokowany, i dlaczego. Potem zwykłymi słowami, co się
zmienia. Dalej jedna sekcja, „Do Twojej decyzji”, zbiera wszystko, co przy scaleniu wymaga Twojego
„tak”: wybory cyklu wykraczające poza zadanie, pominięte kroki i niewykonane sprawdzenia, uwagi
z przeglądu, które odczujesz Ty albo użytkownik, oraz wpisy w dzienniku decyzji, których nie
widziałeś przy doprecyzowaniu zadania. Gdy ta sekcja mówi `none`, nic więcej na Ciebie nie czeka.
Potem koszt cyklu i sposób scalenia. Ta sama górna część stoi jeszcze raz po polsku, w zwiniętym
bloku — tym tutaj. Pod nim leży archiwum dla agentów i do dokładniejszego sprawdzenia: zawsze te
same sekcje w tej samej kolejności, a każda pozycja zaczyna się zdaniem zrozumiałym bez czytania kodu.

Przy scaleniu cykl nie pyta Cię już o wpisy, które zaakceptowałeś przy doprecyzowaniu zadania.
Przed otwarciem PR-a skrypt sprawdza układ opisu, a cykl poprawia to, co skrypt zgłosi. Gdy cykl
uważa, że skrypt się myli, PR otwiera się jako szkic i pyta Ciebie.

*Pod spodem:* jeden szablon opisu, z którego korzysta cykl i PR-y samego the way; skrypt z testami
uruchamianymi przez pełny przebieg testów; sześć nowych i trzy zmienione decyzje o tym, co pokazuje
PR i co akceptujesz przy scaleniu.

**Do Twojej decyzji**

1. **Cykl nie ukrywa błędu formy, który uważa za fałszywy.** Gdy skrypt sprawdzający układ zgłasza
   błąd, który cykl ma za fałszywy, opis zostaje bez zmian. Cykl nigdy nie czyści ani nie tłumaczy
   polskiego bloku, żeby błąd zniknął. PR otwiera się jako szkic i pyta Cię, czy scalić mimo to.
   Tę regułę dodał cykl, żaden wiersz zadania jej nie zawiera. Akceptujesz? (Foundation entries, 9)
2. **Zadanie napisane po angielsku nie dostaje polskiego bloku.** Gdy dokument zadania jest po
   angielsku, zwinięty blok ma tylko `none`, bo górna część jest już w tym języku. Tę regułę dodał
   cykl; wiersz zadania mówi tylko „w języku dokumentu zadania”. Akceptujesz? (Foundation entries, 10)
3. **Proces opiera się teraz na tym, że GitHub zwija ten blok.** Cykl zapisał ten fakt
   z dokumentacji GitHuba, żeby przy zmianie po stronie GitHuba było widać, którą decyzję to psuje.
   Akceptujesz? (Foundation entries, 11)
4. **Cztery wyjaśnienia w dzienniku decyzji dopasowano do nowej zasady o tym, co akceptujesz przy
   scaleniu.** Dotyczą uzasadnień i przykładów starszych decyzji, nie tego, czego te decyzje
   wymagają. Akceptujesz? (Foundation entries, 12–15)
5. **Nagłówki są po angielsku i stałe:** *What you will see* z *Underneath*, *For you to decide*,
   *Cost*, *How to merge*; polski blok ma tytuł „W Twoim języku”. Zadanie zostawiło brzmienie
   cyklowi. Akceptujesz?
6. **Polski blok stoi zaraz po *How to merge*, a nie na samym końcu opisu.** To część, którą
   czytasz, więc stoi tam, gdzie kończysz czytać. Zdanie zadania da się odczytać na oba sposoby.
   Akceptujesz?
7. **Które własne wybory cyklu trafiają do tej sekcji.** Tylko taki, przy którym inna odpowiedź
   zmieniłaby to, co widzi albo robi użytkownik produktu, to, z czym spotykasz się, pracując
   procesem, albo to, co wiąże dziennik decyzji. Resztę archiwum tylko liczy, z linkiem do pełnej
   tabeli. Akceptujesz?
8. **Jak skrypt odróżnia angielski od polskiego.** Liczy częste angielskie słowa, które nie są
   zarazem słowami polskimi. Tekst, w którym stanowią co najmniej jedną piątą słów, a słów jest co
   najmniej 20, uchodzi za angielski. W 57 dokumentach zadań z Twoich notatek ten udział wynosił
   najwyżej 0,14, a w angielskich częściach ostatnich PR-ów 0,37–0,41. Polskie zadanie pełne
   cytowanych angielskich nazw mogłoby przekroczyć próg — wtedy PR otwiera się jako szkic i pyta
   Cię (punkt 1). Akceptujesz?
9. **Dopisanie czegoś do reguł logowania produktu może teraz przejść niezauważone.** Jedna
   z decyzji mówi, że takie dopisanie widzisz przy scaleniu, ale ta sekcja go nie wymienia, a Ty
   czytasz teraz tylko ją. Robimy z tego zadanie? (Minor findings, 3)
10. **Dwie małe luki w skrypcie, na które możesz trafić.** Opis zapisany przez PowerShella
    z niewidocznym znakiem na początku dostaje niezrozumiały błąd w pierwszej linii, co może bez
    powodu zrobić z gotowego PR-a szkic. A nagłówek-wypełniacz skopiowany z szablonu przechodzi
    sprawdzenie, więc mógłbyś zobaczyć sekcję zatytułowaną `<…>`. Robimy z tego zadanie? (Minor
    findings, 1 i 2)

**Koszt**

Około 1 h 35 min pracy. Wszyscy agenci i prowadzący cykl pracowali na jednym modelu, Claude Opus 5.5,
i zużyli 74,8 mln tokenów, z tego 72,2 mln to wejście czytane z pamięci podręcznej, a 0,39 mln to
wyjście. Rundy przeglądu: spec przejrzany dwa razy (jedna poprawka); cała zmiana przejrzana,
poprawiona raz i przejrzana ponownie; krok powrotu przejrzany raz. Tabela etapów: zob. *Record*
w *Course of the cycle*, plik `stages.md`.

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej
gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The decision log gains the rules of the new description and of what the human accepts at the
   merge.** `609a92f`: WAY-286 to WAY-291 written; WAY-114, WAY-134 and WAY-10 changed in place;
   WAY-161, WAY-33, WAY-126 and WAY-97 corrected by the search of the whole foundation; the
   restatements in `elements/common/critique/SKILL.md`, `elements/common/way_of_working.md`,
   `elements/decisions/template.md` and `elements/glossary/template.md` follow.
2. **One template and a script that checks a description against it.** `d1d57db`:
   `task-cycle/skill/request_template.md`, `task-cycle/request_check.py`,
   `task-cycle/test_request_check.py`.
3. **The cycle's steps and the-way's own route point to the template instead of keeping their own
   lists.** `5b685df`: `task-cycle/skill/SKILL.md` steps 12 and 13, `task-cycle/record_template.md`
   (*Request handoff* reduced to the URL, the description's check and the process remarks),
   `task-cycle/skill/correction.md`, `foundation_step.md`, `reserved_return.md`, `blocked_finding.md`,
   `agent-instructions/README.md` ("Integrate into `foundations`").
4. **A task in English gets `none` in its block, written as a decision of its own.** `4327974`, the
   fix of the whole-change review's one blocking finding: WAY-292; the template and the script's
   docstring cite it.
5. **The return step's three corrections.** `e6f24b0`: environment fact `github-collapsed-section`,
   named in WAY-288's *Based on*; WAY-292 narrowed to where the check reads the task as English; the
   9.4 stop, step 12 and `blocked_finding.md` name the template.

## Checks

1. **The full test run passed on the base and on every later tree that went into this request.**
   `python -B gate/run_tests.py`: on the base `f45ca40`, exit 0, 617 tests in 8 directories; on the
   reviewed change `5b685df`, exit 0, 667 tests; on the fixed change `4327974`, exit 0, 667 tests;
   on the final tree `e6f24b0`, exit 0, 667 tests. `foundations` had not moved from the base, so no merge was needed. No check failed in any run; none failed and passed again.
2. **One focused run pointed at a directory without tests; it is no failing test.** The author's
   `python -B gate/run_tests.py elements` exited 1 with `no test found in elements`, as the handoff
   named the wrong directory; `python -B gate/run_tests.py elements/common` exited 0, 109 tests.
3. **The author's own-work check showed that the nightly digest still finds the process remarks of
   a record built from the new template.** A scratch run of `extract_remark_blocks` from
   `cycle_remarks_digest.py` on a filled record from `task-cycle/record_template.md`, exit 0: one
   block, both remarks in it; with the item renamed, exit 0 and zero blocks. The reviewer of the
   whole change repeated it with the same result.
4. **No user interface changed:** no states or screenshots apply.
5. **The form of this description was checked by the script it adds.** `python -B task-cycle/request_check.py docs/task-cycles/pr-description-schema/request.md --task docs/task-cycles/pr-description-schema/task.md`, exit 0 on every run before each publication; it read the task and the block as not English.

## Foundation entries

Each entry this request writes or changes, with one English sentence of its meaning. No invariant
test, surface or *Violated* mark changes. No kept row was tied to an entry already stated.

1. **WAY-286 (new), row 1.** A cycle's request description follows one template: a plain-word top
   part (state, what you will see with what is underneath, your decisions, cost, how to merge) and
   a lower part in a fixed order, each item opening with a sentence a human understands; an empty
   section reads `none`.
2. **WAY-287 (new), row 2.** The section for the human's decisions holds everything whose merge needs
   the human's yes, and its `none` says nothing else waits; a blocked request keeps the same
   skeleton, with what the cycle needs in that section.
3. **WAY-288 (new), row 3.** The description is in English, and its top part stands a second time,
   in the task document's language, in a collapsed block.
4. **WAY-114 (changed), row 4.** The human accepts a projected entry at the readiness gate, an entry
   written whole from an accepted row with the task document, and every other entry at the merge,
   where the decision section gives it as one plain sentence repeated in the block.
5. **WAY-134 (changed), row 4.** An entry written from a kept row has the meaning the human accepted
   with the row; the merge does not ask again, and the review reads the entry against the row.
6. **WAY-10 (changed), row 4.** The human reads the request's decision section and accepts the change
   by merging, while the reviewer reads the whole diff.
7. **WAY-289 (new), row 5.** The orchestrator judges each Minor and out-of-scope finding by whether
   a user or the human working with the process will feel it, and restates those in the decision
   section; every finding stays in its list with the reviewer's words, kind and grade.
8. **WAY-290 (new), row 6.** Before a request opens, the cycle runs the script that checks the
   description's form and corrects the description until it reports no error; the script judges no
   content.
9. **WAY-291 (new), the cycle's.** Where the orchestrator holds a form error wrong, with evidence, it
   does not silence it, and the request opens or stays a draft naming the error in the decision
   section and the check as failed.
10. **WAY-292 (new), the cycle's.** Where the task document is in English, the block reads `none`,
    and the form check holds it to that wherever it reads the task document as English.
11. **`github-collapsed-section` (new environment fact), the cycle's.** GitHub keeps the Markdown
    inside a `<details>` block collapsed until the reader expands it; WAY-288 rests on it.
12. **WAY-161 (rationale corrected), the cycle's.** A listed finding stays within the human's reach,
    and one a user or the human will feel is put in the decision section.
13. **WAY-33 (rationale corrected), the cycle's.** The human sees in the request each entry not
    accepted with the task document, not every entry.
14. **WAY-126 (verification corrected), the cycle's.** Its examples put the meaning of the part of a
    projected entry into the request's decision section.
15. **WAY-97 (rationale corrected), the cycle's.** The review sees a changed glossary definition and
    its rewritten uses in one diff, and the human sees the changed meaning in the request.

## Minor findings

1. **A description saved with an invisible byte-order mark fails with a confusing error.** M-1 of the
   whole-change review, at `5b685df`, `task-cycle/request_check.py:460-464` and `:318-326`: "A
   description saved with a UTF-8 byte-order mark fails the state-line check with a message that
   points at a line that looks correct."
2. **A placeholder heading left from the template passes the check.** M-2, at `5b685df`,
   `task-cycle/skill/request_template.md:101-104`, `task-cycle/request_check.py:363-364`: "The
   skeleton's placeholder heading passes when left in a description."
3. **An addition to a product's logging rules is no longer shown where the human reads.** M-3, at
   `5b685df`, `foundations/decisions.md:8120-8121` (WAY-274): "WAY-274 counts on the human seeing an
   addition to a product's logging scope at the merge. Under the changed WAY-10 and the new WAY-287,
   the human reads only the decision section, and the template does not put such an addition
   there."
4. **The return step is not told to mark the entries it writes, which the description needs.** M-4,
   at `5b685df`, `task-cycle/skill/request_template.md:173-177`,
   `task-cycle/skill/foundation_step.md:17-20`, `task-cycle/skill/return_step.md:8`: "The template
   reads marks and meaning sentences from the return step's report, but the return step's own file
   does not ask for them."
5. **One new decision said more than the script does; the return step has since narrowed it.** M-5
   of the review of the fix, at `4327974`, `foundations/decisions.md:8763-8765`,
   `task-cycle/request_check.py:269-273`, `:433-440`: "WAY-292 says the form check holds the block to
   `none` for any English task document, but the script does so only when it can judge the task's
   language."
6. **The check described under that decision still reads as it did before the narrowing.** m-1 of the
   review of the return step, at `e6f24b0`, `foundations/decisions.md:8772-8773`: "WAY-292's
   *Verification* still says what the binding sentence no longer says."
7. **One step still points to the template only through another step.** m-2, at `e6f24b0`,
   `task-cycle/skill/SKILL.md:193-197`: "One more place writes the description \"as step 13 gives\"
   without naming the template."
8. **One line of the cycle skill is longer than its neighbours.** m-3, at `e6f24b0`,
   `task-cycle/skill/SKILL.md:381`: "Step 12's corrected line runs to 139 characters."

## Findings outside the task's scope

1. **A record committed before its request opens cannot point the plan's state reader to that
   request.** Declined to judge by the whole-change reviewer, no place named beyond the files: "The
   record-first routes (`blocked_finding.md`, the 9.4 stop) commit a record whose *Request URL* holds
   no link yet, so `project-level/plan_state.py` cannot find such a request from the committed
   record. Outside the task: the order was the same before this change, and only
   `reserved_return.md` has a fixed wording for it."
2. **The collapsed block's fact covers GitHub only.** Declined to judge by the reviewer of the return
   step: "Whether WAY-288 needs a fact for a host other than GitHub (a merge request on GitLab)".
3. **The new fact's place in its file follows no rule.** Declined to judge by the reviewer of the
   return step: "The new fact's place in the file, before `github-closed-pull-request-branch` rather
   than after it — no rule of `elements/environment-facts/template.md` or `elements/common/rules.md`
   I found orders the entries."
4. **The Polish sentences of this description were not reviewed by an agent.** Declined to judge by
   the reviewer of the return step: "The Polish meanings in the return step's table and the request's
   *For you to decide* item 6 — the request's description is not in this range."
5. **The foundation check lets a mistyped fact name pass in one case.** Declined to judge by the
   reviewer of the return step: "`foundation_check.py` takes an uppercase word in *Based on*
   (`github-collapsed-sectionX`) for a quoted source and reports nothing (seen in my positive
   control) — the script is not in this range and fact identifiers are lowercase."

## Course of the cycle

- **Task and sources:** "Opis PR-a z cyklu the way ma stały schemat", an independent task, from
  `zadanie_the_way_staly_schemat_pr.md` in the author's notes, `Status: ready for cycle`, copied
  2026-11-05; its citations stand at `foundations` `f45ca40`. Its *Context* placed the cycle of
  AIR-592 before this one; that cycle had not run, and Mariusz chose to start this one now.
- **Process pin:** none; the-way working on itself, the process root this worktree.
- **Spec:** written, for the English headings the task left open and the choices no row settled
  (template's place, the record's section, the script, what fills the decision section, the form of
  the entries, the variants, the-way's own route). Reviewed `FAIL`, revised once, reviewed `FAIL`
  again with two findings the orchestrator settled (spec D10). `spec.md` in the record.
- **Route:** one author without a plan, class `same`: one template, one script and the files that
  point to it bind one another word for word.
- **Plan:** none.
- **Choices:** five other choices (Q1–Q3, Q6, Q7) in the questions table of the record's `cycle.md`; Q4, Q5 and Q8 stand above as items 6, 1 and 9 of *For you to decide*.
- **Blocking findings left:** none.
- **Record:** RECORD_LINK
