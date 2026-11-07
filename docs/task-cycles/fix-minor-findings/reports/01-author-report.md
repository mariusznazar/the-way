# Report 01 — the one author, the whole change

**Status:** done

**Commits** (base `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6`, head `820f963`):

- `8eafea5` docs: WAY-161, WAY-162 and WAY-289 ... (decisions; WAY-297 follows)
- `820f963` docs: the cycle fixes the Minor findings of the whole-change review ... (cycle documents)

**Files changed** (added / removed lines, base to head):

| File | + | - |
|---|---|---|
| `foundations/decisions.md` | 132 | 67 |
| `task-cycle/skill/SKILL.md` | 39 | 12 |
| `task-cycle/skill/request_template.md` | 17 | 9 |
| `task-cycle/skill/correction.md` | 7 | 0 |
| `task-cycle/change/fix.md` | 10 | 4 |
| `task-cycle/review/fix.md` | 12 | 7 |
| `task-cycle/review/whole_change.md` | 4 | 1 |
| `task-cycle/record_template.md` | 3 | 1 |

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (run after each edit round and after the
  commits).
- `python -B gate/run_tests.py task-cycle` — exit 0, 142 tests OK (covers `test_request_check.py`, which quotes
  WAY-162, and `request_check.py`, whose headings I did not change).
- `python -B gate/run_tests.py agent-instructions` — exit 0, 18 tests OK.
- Not run: the full gate (`gate/run_tests.py` without a directory) — the orchestrator's run, by the handoff.
- No test written or changed: the change is prose, and the method says prose gets no test. No invariant test
  involved, so no failing run to report.

## Entries written (foundation step)

All three were edited in place; the identifiers are kept. The wording is mine; the meaning is the row's. The
*Rejected* of each holds the ways the task's *Questions to settle* keeps under *Not chosen*, beside the
rejected ways the entry held before that stay true.

- **WAY-161** — `row 1`.
  EN: The review of the whole change has its Minor findings within the task fixed before the request opens, in
  the fix that runs for the blocking findings or in one fix of their own; findings outside the task's scope are
  not fixed, and the Minor findings that no fix made go to the request's list.
  PL: Uwagi Minor z przeglądu całej zmiany, które leżą w zakresie zadania, cykl poprawia przed otwarciem PR-a —
  w poprawce po uwadze blokującej albo w jednej poprawce tylko dla nich; uwag spoza zakresu nie poprawia, a
  uwagi Minor, których żadna poprawka nie zrobiła, trafiają do listy w PR-ze.
  *Rejected* added: A (question in the request, no fix by the cycle), C (fix only where one runs anyway), D
  (rule left as it was).
- **WAY-162** — `row 2`.
  EN: When the review of a fix made for Minor findings alone finds a new Critical or Important finding in it,
  the cycle reverts the fix's commits with a revert commit and opens the request, not blocked, on the code the
  review of the whole change accepted, with the Minor findings and the new finding in the request's lists; no
  third round; a fix that ran for a blocking finding ends as before.
  PL: Gdy przegląd poprawki zrobionej tylko dla uwag Minor znajdzie w niej nową uwagę Critical albo Important,
  cykl cofa commity tej poprawki commitem cofającym i otwiera PR (niezablokowany) na kodzie przyjętym przez
  przegląd całej zmiany, a uwagi Minor i nowa uwaga trafiają do list w PR-ze; trzeciej rundy nie ma, a
  poprawka uruchomiona po uwadze blokującej kończy się jak dotąd.
  *Rejected* added: a (blocked request), c (keep the accepted part of the fix).
- **WAY-289** — `row 3`.
  EN: Each unfixed finding the user or the human will feel (a Minor finding no fix made, one outside the task's
  scope, the new serious finding of a reverted fix) is put in the human's section as one question with two
  answers, "fix it in this request" or "make a task of it", where one answer may cover the whole list; "fix
  it" runs one correction with one fix and one review, and what it leaves unfixed carries only the question of
  a task or stays below.
  PL: Każdą niepoprawioną uwagę, którą ktoś odczuje (Minor, której żadna poprawka nie zrobiła; spoza zakresu;
  nową poważną uwagę wycofanej poprawki), PR stawia jednym pytaniem o dwóch odpowiedziach — „poprawić w tym
  PR-ze" albo „zrobić zadanie" — na które jedna odpowiedź może objąć całą listę; „poprawić" uruchamia jedną
  korektę z jedną poprawką i jednym przeglądem, a to, czego nie poprawiła, dostaje już tylko pytanie o zadanie
  albo zostaje w dolnej części.
  *Rejected* added: a (question as it was), c (the same question for findings nobody will feel).
- **WAY-297** — `the cycle's` (a consequence edit, no row carries it). See "Choices" below.
  EN: A Minor finding about a missing glossary entry or qualifier goes to the fix for Minor findings (where the
  author may contest it) or to the request's list, instead of staying in front of the human at the merge.
  PL: Uwaga Minor o brakującym haśle słownika albo kwalifikatorze trafia do poprawki uwag Minor (autor może ją
  zakwestionować) albo na listę w PR-ze, a nie „zostaje przed człowiekiem przy scalaniu".

## Choices given by the orchestrator (recorded as given)

- Q1: `correction.md` got its own paragraph (an answer to item 8 asking for the fix makes the findings it names,
  or the listed ones if it names none, the remarks the correction binds; its review ends as every review does;
  what it leaves goes only with the question of a task or stays below). The "A correction" row of the variants
  table in `request_template.md` says the same.
- Q2: the Minor-only fix is made by the one author, resumed, on its class; on the planned route by a fresh agent
  with `make-change` on the orchestrator's class. Put into "The end of a code review" in `SKILL.md`. Its review
  is by the whole-change reviewer, resumed or fresh given its report.
- Q3: the fix takes in only the Minor findings that the whole-change report lists and has not marked outside
  the task's scope (WAY-161, `SKILL.md`).
- Q4: a reverted fix's new Critical or Important finding stands in the request's *Minor findings* list beside
  the Minor findings the fix tried, marked with its grade and as found by the review of the reverted fix;
  WAY-289 judges it. No new heading; `request_check.py` unchanged.

## Other changes

- `task-cycle/skill/SKILL.md`: handoff paragraph (the findings file now holds in-scope Minor findings after the
  blocking ones); step 9 (one sentence after the whole-change review); step 10 (gate runs on the code with the
  fix, or on the code a revert leaves); "The end of a code review" (three paragraphs: the Minor findings of the
  whole-change review; the `FAIL` paragraph with the Minor findings joining it and a remaining Minor finding
  not blocking; the new `PASS` paragraph for the Minor-only fix, its review and the revert).
- `task-cycle/skill/request_template.md`: item 8 of *For you to decide* (the two-answer question and the
  one-correction end), *Technical changes* (the fix and the revert named), *Minor findings* (only unfixed
  Minor findings, plus the new serious finding of a reverted fix), the correction variant row.
- `task-cycle/change/fix.md`: the findings file holds in-scope Minor findings after the blocking ones; keep a
  Minor fix as small as the finding asks; a Minor finding may be contested.
- `task-cycle/review/fix.md`: the same for the reviewer; a remaining or new Minor finding blocks nothing; in a
  Minor-only fix only a new Critical or Important fails the review.
- `task-cycle/review/whole_change.md`: the reviewer lists each Minor finding with its place and says in its
  words where one lies outside the task, so that the cycle can cut the findings file from the report.
- `task-cycle/record_template.md`: *Review rounds* also records the fix for Minor findings, its review and the
  revert commit and the new finding.

## Own-work check

- Requirement most likely unmet: item 2 of *To do* (a reverted Minor-only fix — revert commit, not blocked,
  request opens on the accepted code, Minor findings and the new finding in the request's lists, no third
  round) and the one-correction end of item 3, because each spans four files (decision, `SKILL.md`,
  `request_template.md`, `correction.md`) that must say the same.
- Check: read the final text of "The end of a code review", the *Minor findings* paragraph, item 8 and the
  correction paragraph against the three rows and their *Not chosen*; then a search of `foundations/`,
  `task-cycle/`, `elements/`, `project-level/`, `agent-instructions/`, `installation/`,
  `product-guidelines/` for "Minor", "unfixed", "not fixed", "without a fix", "not yours to fix", "Make a task of
  it" (command: `grep -rn -i -E "not fixed|without a fix|never fixed|unfixed|not yours to fix|Make a task of it"`
  and `Grep Minor` over the worktree, excluding `.runs/` and `docs/task-cycles/`).
- Showed: every remaining hit is either new text or still true (list below). Lines the search found and I
  corrected: WAY-161, WAY-162, WAY-289, WAY-297, `change/fix.md`, `review/fix.md`, `skill/SKILL.md`,
  `request_template.md`, `record_template.md`. Lines left because still true: WAY-220/221/204 (grade, style
  never blocks), WAY-263 (Important), WAY-287 (the list of what the human's section holds), WAY-163 (blocked
  request only), WAY-229, WAY-136, WAY-148, WAY-135, `review/SKILL.md` (grade and report form),
  `request_template.md` line 143 (the generic example "Make a task of it?").

## Reaches beyond the dispatch

- Read whole before editing: every file listed above, plus `task-cycle/record_template.md`,
  `task-cycle/skill/blocked_finding.md`, `agent-instructions/README.md`, `task-cycle/review/SKILL.md`.
- Selective reads: `foundations/part_map.md` (the `task-cycle` entry, no change needed), `foundations/decisions.md`
  passages of WAY-03 (example), WAY-204, WAY-220, WAY-221, WAY-263 (line 7695 range), WAY-286, WAY-297,
  `task-cycle/test_request_check.py` lines 40-100; `foundations/invariants.md` and `glossary.md` searched for
  "finding" and "revert": no hit.
- Why: the handoff asked for a search of the whole foundation (WAY-33) and a check of lines my edits make untrue.

## Searches not found or unclear

- `task-cycle/review/whole_change.md` already tells the whole-change reviewer to grade every Minor finding of the
  slice reviews "as a finding of this review", so the case in Q3 ("a slice-review Minor finding that the
  whole-change reviewer does not repeat stays unfixed") arises only when the reviewer omits one. I kept Q3 as
  given; the text reads fine, but the case is rare in practice.
- The handoff names `agent-instructions/README.md` as a file that may need a change; no line of it became untrue
  (see "Left alone").
- The task's *Decisions in play* quote WAY-161's *Rationale* ("A minor finding fixed in a round of its own spends
  that round on polish"); that sentence is now replaced, so the quotation in the frozen task is of an older
  wording. Nothing to fix; noted for whoever reads the task against the entry.

## Choices (way rejected, cost if wrong)

1. **WAY-297 edited (the cycle's).** Its Rationale said a Minor glossary finding "stays in front of the human at the
   merge", and its *Rejected* said a collision shown on a sentence "is never repaired in the cycle". Both became
   untrue with row 1. I changed the sentences minimally: the finding goes to the fix for Minor findings (author
   may contest) or to the list; the *Rejected* reason is now that such a fix is given up whole when it draws a
   new serious finding. Rejected: leaving WAY-297 as it was (two false lines in the foundation); making Minor
   glossary findings an exception to row 1 (a change of row 1's meaning, which is the human's). Cost if wrong:
   the human may prefer glossary findings never to be fixed by the cycle; that is one more row to the request's
   *For you to decide* item 6 ("foundation entries the human did not see"), which the orchestrator should
   include since this edit is `the cycle's`.
2. **The Minor-only fix may be contested, not only made.** `change/fix.md` lets the fixer mark a Minor finding as
   contested with evidence, and the finding then goes to the list. Row 1 says the cycle fixes "all" in-scope
   Minor findings; a fixer that holds a finding wrong needs a way out (the existing text for blocking findings
   already allowed it). Rejected: no contest (the fixer would be forced to make a change it holds wrong).
   Cost if wrong: a few Minor findings stay in the list that the human wanted fixed.
3. **"Fix" run by the cycle's own commit, not by the orchestrator.** The revert is done by the orchestrator
   (like the resets the skill already gives it), in one revert commit. Rejected: the author reverting (the
   author is the agent whose work is given up). Cost if wrong: none for the result, only who runs a git command.
4. **The Minor findings of a correction's review are not fixed** (they go to the list), as the task's list of
   "what the cycle did not fix" says (Minor of reviews after the whole-change review). Rejected: a Minor fix in
   corrections too (a loop; it would break "one correction ends it").
5. **The Technical changes paragraph names the Minor fix.** Fixed Minor findings do not appear in the Minor list;
   to keep them visible I put the fix (and a revert) under *Technical changes*. Rejected: a new heading
   (`request_check.py` is not to change).
6. **WAY-289 binding sentence widened** to "each unfixed finding" so the new serious finding of a reverted fix is
   covered (Q4), though the title already said "unfixed findings".
7. **WAY-229 and WAY-136 not edited.** WAY-229 already gives the one author "fixes its findings on its own
   class" and a planned change's finding of no slice the orchestrator's class, which covers the Minor-only fix.
   Rejected: adding "Minor" there (a restatement that can drift, WAY-263). Cost if wrong: a reader may want it
   explicit; one sentence.

## Left alone

- `agent-instructions/README.md` (lines 59-65, the hand-made change before `main`): it says the author makes one
  fix for the blocking remarks and "the other remarks go into the lists". It describes the route without a task
  cycle, which the task does not change; with the cycle's rule the line would be wrong only if hand-made changes
  were also to fix Minor remarks, a decision the task does not make. Cost if wrong: hand-made changes keep
  listing Minor remarks as today.
- WAY-163, WAY-287 (the human's section `none` still means nothing waits for a yes), WAY-229, WAY-136, WAY-148,
  WAY-135: read, no line untrue.
- `task-cycle/request_check.py` and the test files: headings unchanged; `test_request_check.py` quotes a
  sentence of WAY-162 that I did not change.
- `task-cycle/skill/blocked_finding.md`, `reserved_return.md`, `planning.md`: no text on Minor fixes.
- The part map: no file added, no change.

## Problems observed

None.
