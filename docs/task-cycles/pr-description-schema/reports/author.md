# Author report — pr-description-schema

**Status:** done with concerns (one concern, under *Problems observed*: WAY-274)

Worktree `C:/Storage/repos/the-way/.runs/worktrees/pr-description-schema`, branch
`task/pr-description-schema`, base `f45ca40`. Variant: the whole change as the one author, foundation
step included.

## Commits

| Commit | What and why |
|---|---|
| `609a92f` | docs: foundation entries. Six new decisions WAY-286 to WAY-291 (rows 1, 2, 3, 5, 6 and the D10 exception); WAY-114, WAY-134 and WAY-10 changed in place (row 4); search corrections to WAY-161, WAY-33, WAY-126 and WAY-97; the restatements of WAY-10 and WAY-114 in `elements/common/way_of_working.md`, `elements/glossary/template.md`, `elements/decisions/template.md` and `elements/common/critique/SKILL.md` (spec D2, second table). |
| `d1d57db` | feat: `task-cycle/skill/request_template.md` (skeleton of D1, the section rules and sources of D2 and D5, the variants of D7, the command and correction loop of D4, the route for an error held wrong of D4 and D10), `task-cycle/request_check.py` and `task-cycle/test_request_check.py` (D4). |
| `5b685df` | docs: pointers. `task-cycle/skill/SKILL.md` (`:196`, `:204-206`, the 9.4 stop, `:351-353`, steps 12 and 13), `task-cycle/record_template.md` (*Request handoff* per D3, `request.md` in the directory list, the *Artifacts* sentence), `correction.md`, `foundation_step.md`, `reserved_return.md`, `blocked_finding.md`, `agent-instructions/README.md` (D8). One wording fix to the template is in this commit too (the top part bars "identifiers of entries", as row 1 says, not of commits or findings as well). |

Files changed, `git diff --numstat f45ca40..HEAD` (added / removed):

```
17   8  agent-instructions/README.md
2    2  elements/common/critique/SKILL.md
3    2  elements/common/way_of_working.md
3    1  elements/decisions/template.md
3    2  elements/glossary/template.md
250  29 foundations/decisions.md
8    26 task-cycle/record_template.md
486  0  task-cycle/request_check.py
27   55 task-cycle/skill/SKILL.md
3    2  task-cycle/skill/blocked_finding.md
4    2  task-cycle/skill/correction.md
7    5  task-cycle/skill/foundation_step.md
254  0  task-cycle/skill/request_template.md
12   22 task-cycle/skill/reserved_return.md
671  0  task-cycle/test_request_check.py
```

## Foundation entries

Mark as `foundation_step.md` now gives it: `row <n>`, `projected` or `the cycle's`. English meaning
first, then Polish for the request's decision section and its block.

| Entry | Mark | English meaning | Polish meaning |
|---|---|---|---|
| WAY-286 (new) | row 1 | A cycle's request description follows one template: a plain-word top part (state, what you will see with what is underneath, your decisions, cost, how to merge) and a lower part in fixed order (technical changes, checks, entries, Minor findings, findings outside the scope, the task's own sections, course of the cycle), each lower-part item opening with a sentence a human understands, and an empty section reading `none`. | Opis PR-a z cyklu ma jeden szablon: na górze zwykłymi słowami stan, co zobaczysz (i co pod spodem), twoje decyzje, koszt i sposób scalenia, niżej w stałej kolejności archiwum, którego każda pozycja zaczyna się zdaniem zrozumiałym bez kodu; pusta sekcja ma `none`. |
| WAY-287 (new) | row 2 | The section for the human's decisions holds everything whose merge needs the human's yes, and its `none` says nothing else waits; a blocked request keeps the same skeleton, what the cycle needs standing in that section. | Sekcja decyzji zbiera wszystko, co przy merge wymaga twojego „tak”, a jej `none` znaczy, że nic więcej nie czeka; PR zablokowany ma ten sam szkielet, a w sekcji decyzji stoi to, czego cykl potrzebuje. |
| WAY-288 (new) | row 3 | The description is in English, and its top part stands a second time, in the task document's language, in a collapsed block. | Opis PR-a jest po angielsku, a jego górna część stoi drugi raz w języku dokumentu zadania, w zwiniętym bloku. |
| WAY-114 (changed) | row 4 | The human accepts an entry's meaning at the readiness gate for a projected entry, with the task document for an entry written whole from an accepted row, and at the merge for every other entry, which the decision section gives as one plain sentence repeated in the block, the full list standing in the lower part. | Wpis rzutowany akceptujesz przy bramce gotowości, wpis z zaakceptowanego wiersza zadania przy dokumencie zadania, a każdy inny przy merge — jego zdanie znaczenia stoi w sekcji decyzji i w zwiniętym bloku, a pełna lista wpisów w archiwum. |
| WAY-134 (changed) | row 4 | An entry written from a kept row has the meaning the human accepted with the row; the merge does not ask again, and the review reads the entry against the row. | Wpis napisany z zaakceptowanego wiersza ma znaczenie, które przyjąłeś przy dokumencie zadania; merge nie pyta o niego drugi raz, a przegląd porównuje wpis z wierszem. |
| WAY-10 (changed) | row 4 | The human reads the request's decision section and accepts the change by merging, while the reviewer reads the whole diff. | Przy merge czytasz sekcję decyzji i akceptujesz zmianę, scalając PR; cały diff czyta recenzent. |
| WAY-289 (new) | row 5 | The orchestrator judges each Minor and out-of-scope finding by whether the user or the human working with the process will feel it, and restates such findings in the decision section as "make a task of it?"; every finding stays in its list with the reviewer's words, kind and grade unchanged. | Prowadzący cykl ocenia każdą drobną uwagę i uwagę spoza zakresu, czy odczuje ją użytkownik albo człowiek pracujący procesem, i takie przepisuje do sekcji decyzji jako „robimy z tego zadanie?”; wszystkie zostają w archiwum ze słowami recenzenta. |
| WAY-290 (new) | row 6 | Before a request opens, the cycle runs the-way's script that checks the description's form and corrects the description until the script reports no error; the script judges no content. | Przed otwarciem PR-a cykl uruchamia skrypt sprawdzający formę opisu i poprawia opis, dopóki skrypt zgłasza błędy; skrypt nie ocenia treści. |
| WAY-291 (new) | the cycle's | Where the orchestrator holds a form error wrong, with evidence, it does not silence it — never empties the block or puts it into English — and the request opens or stays a draft naming the error and the reason in the decision section and the check as failed. | Gdy prowadzący cykl uważa błąd zgłoszony przez skrypt za fałszywy i ma na to dowód, nie usuwa go na siłę — nie czyści bloku ani nie przepisuje go po angielsku — tylko otwiera PR jako szkic i pyta cię w sekcji decyzji, czy scalić mimo tego. |
| WAY-161 (rationale) | the cycle's | Its rationale now says a listed finding stays within the human's reach and one the user or the human will feel is put before the human (WAY-289). | Uzasadnienie WAY-161 mówi teraz, że uwaga z listy jest w zasięgu człowieka, a ta, którą ktoś odczuje, trafia do sekcji decyzji. |
| WAY-33 (rationale) | the cycle's | Its rationale now says the human sees in the request each entry not accepted with the task document, not every entry. | Uzasadnienie WAY-33 mówi teraz, że w PR-ze widzisz wpisy, których nie przyjąłeś przy dokumencie zadania, a nie wszystkie. |
| WAY-126 (verification) | the cycle's | Its examples put the meaning of the part of a projected entry into the request's decision section. | Przykłady WAY-126 kierują zdanie znaczenia części wpisu rzutowanego do sekcji decyzji. |
| WAY-97 (rationale) | the cycle's | Its rationale now says the review sees a changed glossary definition and its rewritten uses in one diff, and the human sees the changed meaning in the request. | Uzasadnienie WAY-97 mówi teraz, że zmienioną definicję i przepisane zdania widzi w diffie recenzent, a ty widzisz zmienione znaczenie w PR-ze. |

The `the cycle's` entries are those the request's *For you to decide* puts before the human (D5
item 6). Rows 1–6 are not listed there; they stand in *Foundation entries*.

### Each kept row and its entry

- Row 1 → WAY-286. Row 2 → WAY-287. Row 3 → WAY-288. Row 4 → WAY-114, WAY-134, WAY-10 (changed in
  place). Row 5 → WAY-289. Row 6 → WAY-290 (written whole, no exception; D10 A).
- No row was tied to an entry already stated: the search found none stating a row.

### The search of the whole foundation (WAY-33, spec D9)

`grep` over `foundations/*.md` for "at the merge", "by merging", "in its request", "in the request",
"the request lists", "request names/gives/states/shows", "diff of the foundation", "human who
merges", "human merging", and each hit's entry read whole. Corrected: WAY-161, WAY-33, WAY-126 (D9
named them) and WAY-97 (not named by D9: its rationale had the human seeing the diff at the merge).
WAY-134's `narrows WAY-114` kept: WAY-134 still sends a question to the human (a blocked draft
where a row's meaning cannot hold) beyond WAY-114's limit on questions. Hold unchanged: WAY-03,
WAY-13, WAY-14, WAY-49, WAY-51, WAY-65, WAY-95, WAY-99, WAY-127, WAY-130, WAY-140, WAY-160,
WAY-162, WAY-163, WAY-164, WAY-172, WAY-219, WAY-227, WAY-242, WAY-261, WAY-268, WAY-269. One
finding not corrected: WAY-274, below. Invariants, glossary, environment facts and part map: no hit
needing change; the new files fall under `task-cycle/**`; no surface, trust boundary, invariant
test or *Violated* mark changes.

## Choices under *Left to the maker*

- **Function words, threshold, minimum.** About 110 English function words, leaving out `a`, `i`,
  `to`, `on`, `no`, `do`, `by`, `we`, `my`, `me`, `was`, `same`, `most`, `mine` (common Polish words).
  `ENGLISH_THRESHOLD = 0.2`, `MINIMUM_WORDS = 20`. Measured: the test prose, English 0.46 and Polish
  (with an English quote of WAY-114 and code names) 0.07; the frozen task of this cycle 0.007; every
  task document under `C:\Storage\The Brain\The Brain\Notes\Projects\*\_zadania\` that holds *Need*
  or *To do* (57 judged), at most 0.14; the English top parts of the-way #66, #68, #69, #70 0.37–0.41
  and their Polish blocks 0.0 and 0.002 (read with `gh pr view`). Rejected: 0.25, which narrows the
  Polish margin less than it costs terse English. Cost if wrong: a Polish task quoting much English
  between 0.14 and 0.2 still passes; above 0.2 it reads English and the route of WAY-291 opens a
  draft instead of losing the block.
- **Lines.** The script splits lines on `\n`, `\r\n` and `\r` only, not `str.splitlines`, so line
  numbers match an editor's.
- **A `<details>` left open** ends before the next `##` heading of the template, so one missing
  `</details>` gives one error, not a heading missing for every section after it. Rejected: running
  it to the end of the file (every later section reported missing).
- **The block's `none`** may stand in backticks. **The state line** takes the em dash only.
- **A wrong argument** gives `Error:` on stderr with exit 2, through an `ArgumentParser` whose
  `error()` raises, rather than argparse's usage text and exit 2.
- **`request.md` in *Artifacts*.** Named in the record template's list of what lives under the
  record's directory, and the *Artifacts* sentence says the foundation step's report keeps the
  meaning sentences and their marks, and `request.md` takes them from there.
- **The record's *Description* field.** One field that holds both D3 cases: the path with the last
  run and the number of runs, or `written and checked after this commit` in a copy committed before
  the description was written or rewritten.
- **Relations of new entries.** WAY-286 and WAY-287 derive from WAY-227; WAY-288 and WAY-290 derive
  from WAY-286 (WAY-290 also from WAY-288); WAY-289 derives from WAY-161 and WAY-287; WAY-291
  narrows WAY-290. Scope of all six: `task-cycle, agent-instructions`, since the README route uses
  them; WAY-114 gains `task-cycle`.
- **WAY-288's binding sentence** stays with the row: it does not say the block reads `none` for an
  English task. That rule stands in the template only (spec D1 item 6), so it is a choice beyond the
  task's content for the orchestrator to weigh for *For you to decide*.
- **Step 12's order.** Gate, stages, step 13's description and check, open the draft from it, URL
  into the record, record pair and push, the SHA link into the description, check, edit, mark ready
  unless the first line reads `blocked` or `draft`.
- **`reserved_return.md`, "What the request states"** keeps only the pointer to the template's
  variant and the rule that a remark is no correction (D2: none of its own list).

## Own-work check (WAY-164)

- **Requirement most likely not met:** the nightly digest outside the repository keeps cutting the
  "Process remarks" block out of the rebuilt *Request handoff* (spec D3, task *Context*). No test of
  the-way covers it.
- **Check:** a scratch script,
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\7a4fe94e-3148-4011-bad6-7d83342c594a\scratchpad\digest_check.py`,
  imports `cycle_remarks_digest.py` from its own directory (read-only; nothing outside the
  repository changed) and runs `extract_remark_blocks` on a record built from the new
  `task-cycle/record_template.md`, its *Request handoff* filled with a URL, a *Description*, the
  backlog line and a *Process remarks* item with a lead-in list of two remarks.
- **What it showed:** `python -B ...\digest_check.py task-cycle/record_template.md ...` exit 0: one
  block, both remarks inside it, neither the *Description* nor the backlog line leaking into it.
  Positive control: the same run with the item renamed `Remarks on the-way`
  (`...\digest_check_negative.py`), exit 0, zero blocks. The check holds.
- Second check, of To do 1: `grep` for "What this request settles", "step 13 names", "step 13 gives
  under", "request's lists (step 13)" and `*Questions*` over `task-cycle`, `agent-instructions`,
  `elements`, `project-level`, `installation` and `README.md` finds only the template's own item 2.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest task-cycle/test_request_check.py` (stub module, before the code) | 1 | failing run of the tests written first: 49 ran, 41 failures, 1 error (template missing); 7 that assert "no problem" passed on the stub |
| `python -B -m unittest task-cycle/test_request_check.py` (script written, template not yet) | 1 | 49 ran, 1 error: the template-agreement test, template missing |
| `python -B -m unittest task-cycle/test_request_check.py` (template written) | 0 | 49 OK |
| same, after the plan and task fixtures were made English on their whole text and the argument test added | 0 | 50 OK |
| mutation: `task_text` returning the whole document, then `python -B -m unittest task-cycle/test_request_check.py` | 1 | 34 failures; code restored from a copy, rerun exit 0 |
| `python -B elements/common/foundation_check.py .` after the new decisions | 0 | 0 errors |
| `python -B elements/common/foundation_check.py .` after the changed and corrected decisions | 0 | 0 errors (run after each edit, all exit 0) |
| `python -B gate/run_tests.py task-cycle` (new test file added to git) | 0 | 92 tests OK |
| `python -B gate/run_tests.py task-cycle` (after the pointers) | 0 | OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | OK |
| `python -B gate/run_tests.py elements` | 1 | `no test found in elements`: the wrong directory, the tests stand in `elements/common` |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 268 tests OK |
| `python -B gate/run_tests.py task-cycle` (after the last template edit, before the third commit) | 0 | OK |
| `python -B elements/common/foundation_check.py .` (final head `5b685df`) | 0 | 0 errors |
| digest check and its negative control (own-work check) | 0 / 0 | see above |

Not run: the full gate (the orchestrator's, WAY-160); `installation`, `instruction-files`, `gate`,
`relation-model` tests (no file of theirs changed); `agent-instructions/skill_entry_points.py
--write` (no skill added, renamed or moved, and no `description` changed). No invariant's test
written or changed.

## Reaches beyond the handoff

- WAY-126, WAY-95, WAY-97, WAY-99, WAY-172, WAY-242, WAY-274, and the hits in WAY-13, WAY-65,
  WAY-73, WAY-127, WAY-130, WAY-281 in `foundations/decisions.md` — the search of the whole
  foundation (WAY-33, D9).
- `project-level/plan/template.md` — the *Goal* column and *Open questions* form for the plan case
  of the language measure (D4 unit 3, D10 B).
- `project-level/plan_state.py` `display` — the printable filter D4 names.
- `elements/common/rules.md`, `elements/decisions/examples.md` (WAY-03) — step 1 of the decisions
  skill.
- `agent-instructions/test_instruction_files.py` head — to confirm `agent-instructions/README.md`
  is a repository instruction file (no `@` written).
- Real task documents under `C:\Storage\The Brain\The Brain\Notes\Projects\*\_zadania\` and the
  bodies of the-way #66, #68, #69, #70 (`gh pr view`) — read only, to place the threshold; nothing
  of them copied into the repository.

## Problems observed

- **WAY-274 (concern).** Its binding sentence says an agent adds an item to a product's logging
  scope "in the change that brings it, and the human sees it at the merge". Under the changed WAY-10
  the human reads the request's section for the human's decisions, and neither WAY-287 nor the
  template's list of that section names an addition to a product's guidelines. WAY-274 still holds
  word for word, since the item stands in the diff, but the sight it relies on is weaker. I did not
  correct it: it would add to the decision section's list beyond row 2 or change WAY-274's meaning.
  Recommended: name it in the request as a finding of the search for the human, or add "an addition
  a decision has the human see at the merge" to the template's item 5 in a later task.
- The spec's D4 *Tests* line "a plan's form is measured on its whole text" was superseded by D10 B.
  The test follows D10: a Polish plan whose whole text reads English by the measure (0.21) reads
  `not English` on its *Goal* cells and questions.
- The handoff's example `python -B gate/run_tests.py elements` finds no test (exit 1). The tests
  are in `elements/common`.

## Searches not found or unclear

- The handoff names `python -B gate/run_tests.py elements` as a focused check. That directory holds
  no test (`no test found in elements`, exit 1). Its tests stand in `elements/common`.
- Whether WAY-274's "the human sees it at the merge" was meant to reach the request's decision
  section. Unclear; see *Problems observed*.
