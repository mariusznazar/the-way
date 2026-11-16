**State: ready** — nothing waits for your answer; the items below you only accept by merging.

## What you will see

When two tasks run side by side, each gives its new decisions the next free numbers of the log it started from, so both take the same numbers, and the one that merges second finds the other's numbers already in the main branch. Until now the cycle had no rule for that moment: the agent leading the cycle invented the renumbering, and it covered the foundation and the code but not the documents of the cycle itself, so the description of the request showed the new numbers while the spec, the plan, the handoffs and the reports behind its links still showed the old ones, and you had to convert each number by hand.

After this change the cycle has the rule written down. Where the main branch already holds a number that a new decision of the task bears, the task gives way: before it merges the main branch, in a commit of its own, it renumbers all its new decisions onto the next free numbers after the highest one the main branch holds, and never changes a number of the main branch. In the same single pass it rewrites every reference to those decisions in the files of the branch and in the cycle's record as it stands before the reconciliation is noted; texts written afterwards, and your remarks quoted word for word, stay as they were. The conversion of old numbers into new ones stands in one place only, the row of the record's events that notes the reconciliation, with no note at the head of the record. The same rule holds for each merge of the main branch in a correction after your remarks on a request, which is where a second renumbering falls when the request returns after another request that adds decisions has been merged.

### Underneath

The rule is one new decision of the log with the rejected ways beside it, one new section of the cycle's skill that says how to do the pass and check it, and pointers to that section from the step that reconciles with the main branch and from both merges of a correction; the cycle's record template gains one sentence about the row that carries the conversion.

## For you to decide

### Needed from you

none

### Fix or let through

none

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

1. A choice beyond what the task says: if a request is renumbered a second time, the conversion row of the first renumbering stays as it was written, and a reader of an old number follows the rows one after the other, instead of the first row being rewritten with the second map. The reviewer showed that rewriting it in the same pass corrupts it whenever the old and new numbers overlap, which is the usual case, and that would make the old numbers unreadable again, which is the reason you gave for keeping the conversion. The other way, rewriting only the right side of the earlier row, would make the agent tell the two sides of a free-text row apart, and one slip would corrupt the only place that keeps the conversion readable. The price is that after two renumberings a reader needs to know from which row to start; the rows carry their times.

2. One decision is written by this change, and you did not see its wording at the task. It says that a task whose new decision numbers the main branch has already taken renumbers its own, before the merge, in a commit of its own, in one pass over its files and the cycle's record, and never touches the main branch's numbers; that the conversion stands only in the one row of events; and that it holds for the merges of a correction too. Its rejected ways are the ones you chose or declined at the task, and its reasons name the price: the reports of the agents differ in their numbers from what the agents wrote, nobody reviews the rewrite of the record because the record is no code, and a correction can renumber a second time. The cycle added a pair of examples to it, a change that complies and one that violates, since no test can hold a rule that agents carry out; they stand word for word under the entry in the lower part. (Foundation entries)

3. A choice about where the procedure stands and what the reviewer of the merge sees: the procedure is a section of its own in the cycle's skill that the reconciliation step and both merges of a correction point to, and the commit that renumbers lies in the range the reviewer of the merge reads, with the old-to-new map in its dispatch, so that the reviewer compares the pass with it. The record's rewrite is not code, so no reviewer checks it. (Technical changes, 1)

## Cost

Counted before this request was published: working time 0:44:11 across the orchestrator and its agents, of which 0:20:07 was waiting for tools; 25.7 million tokens (18.7 million on Sonnet 5.5, 7.0 million on Opus 5.5, which did the reviews). One review round ran a fix and a review of the fix: the review of the whole change failed once (two blocking findings and one Minor, all fixed) and the review of the fix passed; the return step changed nothing, so it needed no review. The table of stages stands in the record, linked under *Course of the cycle*.

One directory of an earlier task still stands because the cleaning script could not tell it was no longer needed; nothing in this request waits for it and you may remove it by hand. Its name, branch and reason stand in *Checks*.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing here waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — nic nie czeka na Twoją odpowiedź; pozycje poniżej tylko akceptujesz przez scalenie.

## Co zobaczysz

Gdy dwa zadania idą równolegle, każde nadaje swoim nowym decyzjom kolejne wolne numery według dziennika, z którego wystartowało, więc oba biorą te same numery, a to, które scala się jako drugie, zastaje numery tego pierwszego już w głównej gałęzi. Dotąd cykl nie miał na ten moment reguły: agent prowadzący cykl wymyślał przenumerowanie sam, a ono obejmowało fundament i kod, ale nie dokumenty samego cyklu, więc opis PR-a podawał nowe numery, a spec, plan, przekazania i raporty pod jego linkami — stare, i każdy numer trzeba było przeliczać ręcznie.

Po tej zmianie reguła jest zapisana. Gdy główna gałąź ma już numer, który nosi nowa decyzja zadania, zadanie ustępuje: przed scaleniem głównej gałęzi, osobnym commitem, przenumerowuje wszystkie swoje nowe decyzje na kolejne wolne numery po najwyższym, jaki ma główna gałąź, i nigdy nie zmienia numeru głównej gałęzi. Jednym przebiegiem przepisuje każde odwołanie do tych decyzji w plikach gałęzi i w zapisie cyklu w stanie sprzed wpisania uzgodnienia; teksty zapisane później i Twoje uwagi cytowane słowo w słowo zostają, jak są. Przeliczenie starych numerów na nowe stoi w jednym miejscu: w wierszu dziennika zdarzeń zapisu, który odnotowuje uzgodnienie, bez notki na początku zapisu. Ta sama reguła obowiązuje przy każdym scaleniu głównej gałęzi w korekcie po Twoich uwagach do PR-a — tam wypada drugie przenumerowanie, gdy PR wraca po scaleniu innego PR-a dopisującego decyzje.

### Pod spodem

Reguła to jedna nowa decyzja dziennika z odrzuconymi wariantami obok, jedna nowa sekcja skilla cyklu mówiąca, jak zrobić przebieg i jak go sprawdzić, oraz odesłania do niej z kroku uzgadniającego z główną gałęzią i z obu scaleń korekty; szablon zapisu cyklu dostaje jedno zdanie o wierszu z przeliczeniem.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

none

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

1. Wybór ponad to, co mówi zadanie: gdy PR jest przenumerowywany drugi raz, wiersz z przeliczeniem z pierwszego przenumerowania zostaje, jak był zapisany, a czytelnik starego numeru idzie po wierszach jeden po drugim, zamiast przepisywać pierwszy wiersz mapą drugiego. Recenzent pokazał, że przepisanie go w tym samym przebiegu psuje go, gdy stare i nowe numery się nakładają, a to zdarza się zwykle, i znów robiłoby stare numery nieczytelnymi, a to był Twój powód, by przeliczenie zachować. Drugi sposób, przepisanie tylko prawej strony wcześniejszego wiersza, kazałby agentowi odróżniać dwie strony wiersza w wolnym tekście, a jedna pomyłka zepsułaby jedyne miejsce, które trzyma przeliczenie czytelne. Cena: po dwóch przenumerowaniach czytelnik musi wiedzieć, od którego wiersza zacząć; wiersze mają czasy.

2. Ta zmiana zapisuje jedną decyzję, której brzmienia nie widziałeś przy zadaniu. Mówi ona, że zadanie, któremu główna gałąź zajęła numery nowych decyzji, przenumerowuje swoje przed scaleniem, osobnym commitem, jednym przebiegiem po swoich plikach i zapisie cyklu, i nigdy nie rusza numerów głównej gałęzi; że przeliczenie stoi tylko w jednym wierszu dziennika zdarzeń; i że obowiązuje także przy scaleniach korekty. Odrzucone warianty to te, które wybrałeś albo odrzuciłeś przy zadaniu, a uzasadnienie podaje cenę: raporty agentów różnią się numerami od tego, co agenci napisali, nikt nie recenzuje przepisania zapisu, bo zapis nie jest kodem, a korekta może przenumerować drugi raz. Cykl dodał do niej parę przykładów, zmianę zgodną i naruszającą, bo żaden test nie utrzyma reguły wykonywanej przez agentów; stoją słowo w słowo pod wpisem w dolnej części. (Foundation entries)

3. Wybór co do miejsca procedury i tego, co widzi recenzent scalenia: procedura jest osobną sekcją skilla cyklu, do której odsyłają krok uzgadniający i oba scalenia korekty, a commit z przenumerowaniem leży w zakresie, który czyta recenzent scalenia, z mapą starych numerów na nowe w jego poleceniu, żeby porównał przebieg z mapą. Przepisanie zapisu nie jest kodem, więc nikt go nie recenzuje. (Technical changes, 1)

## Koszt

Policzony przed opublikowaniem tego PR-a: czas pracy 0:44:11 orkiestratora i jego agentów, w tym 0:20:07 czekania na narzędzia; 25,7 mln tokenów (18,7 mln na Sonnet 5.5, 7,0 mln na Opus 5.5, który robił przeglądy). Jedna runda przeglądu miała poprawkę i przegląd poprawki: przegląd całej zmiany odpadł raz (dwie uwagi blokujące i jedna drobna, wszystkie naprawione), a przegląd poprawki przeszedł; krok powrotny niczego nie zmienił, więc nie potrzebował przeglądu. Tabela etapów stoi w zapisie, z linkiem w *Course of the cycle*.

Katalog jednego wcześniejszego zadania nadal stoi, bo skrypt czyszczący nie umiał rozpoznać, że nie jest już potrzebny; nic w tym PR-ze na niego nie czeka i możesz go usunąć ręcznie. Jego nazwa, gałąź i powód są w *Checks*.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Nic tu nie czeka na przegląd fundamentu.

</details>

## Technical changes

The change is two commits on the base `1feb483`, the author's work and the fix of the review of the whole change; the return step made no commit and the request holds the record's pair of commits besides.

1. `34db268` — the change itself. `foundations/decisions.md`: the new decision WAY-403 at the end of the section "The course of a task cycle", with its pair of examples and its rejected ways. `task-cycle/skill/SKILL.md`: step 12 begins with the fetch and, where the target branch holds a number a new decision of the task bears, the renumbering first and then the merge, with the reviewer of the merge reading the renumbering commit too; a new section "The renumbering of the task's decisions" between step 14 and "The process remarks check" holds the procedure (the map, the one pass over the files and the original of the record, the check, the commit alone before the merge, the conversion in the *Events* row). `task-cycle/skill/correction.md`: both merge paragraphs ("In the-way itself, before anything else" and "Take a link to the request") point to that section. `task-cycle/record_template.md`: one sentence on the *Events* row that gives the conversion.
2. `059b891` — the fix of the review of the whole change: step 3 of the section now checks the pass by counts (the references of each old number before, of each new number after) instead of a search for old numbers, which fails a correct pass where old and new ranges overlap; the rows of an earlier reconciliation's conversion stay as written; WAY-403 says the same in its binding paragraphs, both examples and its reasons; the example of whole-number matching in the skill uses bare numbers.

## Checks

1. The final gate is the CI run on the request's last head: the result is written here once the run ends. The cycle ran no full gate on its own system. The agents' focused checks, all exit 0 on `059b891`: `python -B gate/run_tests.py task-cycle` 534 tests OK, `product-guidelines` 14 OK, `elements/common` 257 OK (author, fix and the review of the whole change), `agent-instructions` 37 OK and `installation` 62 OK (author); `python -B elements/common/foundation_check.py` run by the orchestrator on `059b891` without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line.
2. Tests failing before the change: none. The base is a merge commit with the tree of its second parent, so no gate ran on it; the list was taken from the checks of the merged request #141, whose CI run on its last head had `tests` and `tests-windows` green, and from the cycle record of that request.
3. Own-work checks: the author's — a script applies the map once to a text with whole-number matching and compares the result with the expected one (exit 0); after the fix, the count check on an overlapping map and on a second renumbering, which fails for a missed text and for a pass done decision by decision (exit 0). The reviewer of the fix ran 20,000 random maps: every correct pass was accepted and every single missed reference was caught.
4. Not run: `ruff` is not installed where the agents worked, so no agent ran the linter's blocking rules; the CI gate runs them. The review of the whole change read 22 of the decisions of its selection whole, WAY-135 among them, and named none of the unread.
5. The target branch: `git fetch --tags origin` — `origin/foundations` is still the base `1feb483`, so no merge and no renumbering were needed. `python -B task-cycle/review_reminder.py origin/foundations`: tag `foundation-review/2026-11-15`, 14 merges, threshold 60, `reminder: no`.
6. Description checks and checks on the copy of the record: written in the edit that adds the record's link.
7. Directories of earlier tasks kept, with no absolute path: audit-answers-contradiction-after-code · task/audit-answers-contradiction-after-code · uncommitted changes, commits not on the remote, and the branch has no merge git can see on the target branch. Working copies left by agents: none.

## Foundation entries

- WAY-403 — a task branch whose new decision numbers the target branch has taken renumbers its decisions before the merge, in a commit of its own, in one pass over its files and the cycle's record, and the conversion stands only in the row of events that notes the reconciliation. Marked `the cycle's`: it carries the rows 1 and 2 of *Settlements to record* whole, and the pair of examples below is the cycle's addition. Its pair, word for word:
  - complies: the new decisions of a task branch bear the numbers 500 to 502, the target branch took 500 and 501 for its own, and the task branch gives its three the numbers 502 to 504 in a commit of its own before the merge, in the log, the tests, the comments, the skills and the original of the record, the spec, the plan, the handoffs, the reports and the process remarks among them; a remark of the human quoted in the record keeps the number it was written with; the row of the reconciliation reads 500 → 502, 501 → 503 and 502 → 504; a correction after review that meets decisions taken by another merged request renumbers the same way before its merge, gives a row of its own, 502 → 505, 503 → 506 and 504 → 507, and leaves the first row as it is;
  - violates: the task branch merges first and renumbers afterwards, or in the merge commit; the decisions of the target branch are renumbered; the numbers are replaced one decision at a time, so that 502 becomes 504 after 500 became 502; the log is renumbered and the record keeps the old numbers under a note of the conversion at its head; the human's quoted remark is rewritten; the row of the reconciliation gives no conversion; the row of an earlier reconciliation is rewritten with the map of a later one, so that it reads 500 → 505, 501 → 506 and 505 → 507; a correction merges the target branch with no renumbering where the numbers clash.
- No invariant, no test and no surface is changed, and no *Violated* mark is set or cleared; the foundation check lists no invariant for a corrected sentence.

## Minor findings

1. N-1, found by the review of the fix (`PASS 059b891`), within the task, not fixed: "after a second renumbering one number can stand on the left of both rows with two meanings. In the entry's own complying example, 502 is the first number of the third decision (row 1: 502 -> 504, then row 2: 504 -> 507) and the number the first decision bore between the two reconciliations (row 2: 502 -> 505). A reader who starts at the first row with a number written between the reconciliations goes 502 -> 504 -> 507 and lands on the wrong decision." The reviewer's note on weight: little, since the rows of *Events* carry their times and a half sentence ("starting at the first row after the number was written") would settle it. Place: `task-cycle/skill/SKILL.md:710-711` and `foundations/decisions.md:6281-6282`.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task is independent: the cycle's rule for the renumbering of a task's decisions where a parallel task took their numbers, in step 12 and at both merges of a correction, with its decision; sources: the task document, accepted 2026-11-14, and the foundation at `1feb483`. The task names WAY-306, WAY-357 and WAY-328 among its decisions in play; the log has withdrawn them since the task was accepted (their rules stand in `task-cycle/skill/correction.md` and `task-cycle/record_template.md`, and WAY-328 ended), so the change links none of them.
- **Process pin:** none; the-way itself is the process.
- **Spec:** none: the task leaves no open design choice, as its four answered questions and two settlement rows show, and the review of the whole change read WAY-135 whole and agreed.
- **Route:** one author without a plan, class `same` (Sonnet), since the change writes a decision entry whose form the foundation check holds and asks for the search of the whole foundation; the fix by the same author; the return step by the same author, with no commit.
- **Plan:** none.
- **Choices:** 8 other choices, 2 of them beyond the task's text (items 1 and 3 above); the table is in the record.
- **Blocking findings left:** none.
- **Record:** the link is added in the edit that adds the record's commit.
