# Author report — the whole change as the one author

**Status:** done with concerns (the concerns are two places where the task's words and the files differ,
listed under "Problems observed")

## Commits and files

- `6727b67` on `task/cycle-after-foundation-review` (base `739c813`): "Settle the cycle's removal of
  directories against WAY-13, the red gate on a flaky test and the answers to a request's items".
  The worktree is clean.
- Files changed (5 files, 111 added, 57 removed lines):
  - `foundations/decisions.md`: 127 lines changed (WAY-13, WAY-375, WAY-376, WAY-261, WAY-289)
  - `task-cycle/skill/SKILL.md`: 22 lines changed (step 10 paragraph, first paragraph of "Working
    copies"; part of that count is a rewrap of the lines after the added sentence)
  - `task-cycle/skill/correction.md`: 5 lines
  - `task-cycle/skill/request_template.md`: 7 lines
  - `agent-instructions/README.md`: 7 lines
- Not changed, as the handoff says: WAY-243, the testing template, the glossary, the part map, the
  invariants, `task-cycle/remove_merged_worktrees.py`.

## Checks (command, exit code)

| Command | Exit | Note |
|---|---|---|
| `python -B elements/common/foundation_check.py` (full, no `--skip-test-citations`) | 0 | `0 errors`; no `listed:` line |
| `python -B gate/run_tests.py elements/common` | 0 | 235 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 483 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B gate/run_tests.py process-audit` | 0 | OK |
| `python -B task-cycle/private_paths_check.py <file>` for each of the 5 changed files | 0 each | `0 listed` |

The four directory runs and the foundation check ran twice: once on the uncommitted change and once on
commit `6727b67` (between them only the word "will" left a Verification line and a binding sentence).
Both runs passed; the figures above are of the second. `installation` was not run: no file it checks
changed. `python -B agent-instructions/skill_entry_points.py` was not run: no description of a skill
changed. The whole gate was not run, as instructed.

No invariant was changed and no test was written or changed. No test could be made to fail first: the
change is prose in decisions and skills, which `make-change` section 2 leaves without a test, and every
test that cites a sentence of WAY-375 and WAY-376 (`task-cycle/test_remove_merged_worktrees.py`, lines
232-477) keeps its quoted sentence start unchanged (the foundation check, which compares the quotations,
passes).

## Own-work check (WAY-164)

- Requirement most likely unmet: that no entry or instruction still says what the change removes — that
  the human sees the ignored-file list before the cycle removes (item 2), that the first clearing is a
  human act (item 1), that loose base copies stay for hand clearing (item 3) — and that the wording a
  test quotes still stands.
- Check: `git grep -n -i "first clearing|before the removal|hand clearing|sees before|loose copies"`
  over the tracked files. It shows hits only in the *Rejected* of WAY-375 and WAY-376, where the ways
  not chosen are named, and one old, unrelated *Rejected* item of WAY-375 ("only directories below the
  repository's own directory ... for hand clearing"). The foundation check and the `task-cycle` tests,
  which read the quoted sentences by lines `decision:`, pass.
- A second check on forbidden words: the lines I added to `decisions.md`, searched for *will*,
  *should*, *must*, *shall*. It found "will" in a binding sentence and in a Verification line of
  WAY-261; both are reworded to "fixes" (the template bans "will" in binding sentences), and the second
  hit is a rewrapped old line of WAY-289.

## The foundation entries (step "foundation step", `task-cycle/skill/foundation_step.md`)

Each entry: meaning in English, meaning in Polish (the task document's language), mark.

1. **WAY-375**, binding sentences, *Relations*, *Rationale*, *Rejected* (edited in place) — marks: row 1,
   row 2, row 4.
   - EN: The first clearing of directories that gathered before the script is no longer named as the
     human's act; a copy of a base that the script does not assign to a task stays for the human; and
     WAY-375 narrows WAY-13 in the area of removing a cycle's own directories whose branches are merged,
     while WAY-13 keeps every other operation that cannot be undone.
   - PL: Pierwsze sprzątanie zaległych katalogów przestaje być nazwane czynnością człowieka; kopia
     bazowa, której skrypt nie przypisze do zadania, zostaje człowiekowi; WAY-375 zawęża WAY-13 w obszarze
     usuwania własnych, scalonych katalogów cyklu, a WAY-13 zachowuje zasięg wobec każdej innej
     nieodwracalnej czynności.
   - Row 1: the clause removed from the second paragraph, and in *Rejected* the way not chosen (keeping
     the clause) added from the row's source. Row 4: the third sentence of the first paragraph now says
     the copy stays; *Rationale* names the reason (a copy removed for a name that matches no branch
     could belong to a running cycle); the contradicting *Rejected* item is removed and the way not
     chosen by the row's source (removing a clean copy with no branch found) is added. Row 2: `narrows
     WAY-13` in *Relations*, a closing sentence of the second paragraph that states the area, one
     sentence of *Rationale* for why WAY-13 yields, and the way not chosen (narrowing WAY-13's sentence)
     in *Rejected*.
   - Precedence between two decisions (WAY-25), for the request: the passages of what the human accepted
     that give the outcome, quoted from the frozen task:
     - *Questions to settle*, P18, Answer: "(b) — WAY-375 zapisuje w *Relations* `narrows WAY-13`, a jej
       zdanie wiążące nazywa obszar: usuwanie własnych, scalonych katalogów cyklu; WAY-13 zachowuje
       zasięg wobec każdej innej nieodwracalnej czynności."
     - *To do* 4: "Zapisać w WAY-375 `narrows WAY-13` w *Relations* i w zdaniu wiążącym obszar, w którym
       WAY-375 przeważa: usuwanie własnych, scalonych katalogów cyklu."
     - *Settlements to record*, row 2.
2. **WAY-376**, binding sentences, *Rationale*, *Rejected* (edited in place) — mark: row 3.
   - EN: The list of ignored paths in a directory serves a dry run that a human starts alone (the script
     without `--apply`); the cycle's own run with `--apply` waits for no one to read it, and the cycle's
     start step is unchanged.
   - PL: Lista ścieżek ignorowanych służy przebiegowi na sucho (skrypt bez `--apply`), który człowiek
     uruchamia sam; przebieg cyklu z `--apply` nie czeka na jej przeczytanie, a krok startu cyklu się nie
     zmienia.
   - *Rejected* gets the two ways of the row's source (list into the record and request; stopping the
     cycle where the list is not empty).
3. **WAY-261**, a second paragraph of binding sentences, *Verification* pair, *Rationale*, *Rejected*
   (edited in place) — marks: row 5 (the sentence) and row 6 (where the rule stands: the skill and
   WAY-261, WAY-243 and the template untouched).
   - EN: The red result of the first run of the gate on the final tree stays the gate's result, also
     where the failing check is one outside the task's scope that passes when run again; the cycle does
     not stop, and the request names that check and the task that fixes it, or proposes the task.
   - PL: Czerwony wynik pierwszego przebiegu bramki na końcowym drzewie zostaje wynikiem bramki, także
     gdy padł losowo padający test spoza zakresu zmiany; cykl się nie zatrzymuje, a prośba nazywa ten
     test i zadanie, które go naprawi, albo je proponuje.
   - *Rejected* gets the two ways of the rows' sources (disabling the test with a cause under WAY-233;
     the rule also in WAY-243 and the testing template).
4. **WAY-13**, *Verification*, violating example only (binding sentence unchanged) — mark: `the cycle's`
   (carried by *To do* 5, which no row of *Settlements to record* holds).
   - EN: The example of a violation names its subject: "an agent treats a large task as a reason to
     split it ...".
   - PL: Przykład naruszenia ma podmiot: „an agent treats a large task as a reason to split it …”.
5. **WAY-289**, binding sentences and *Rationale* (edited in place) — mark: `the cycle's` (carried by
   *To do* 8, which no row holds).
   - EN: The answer "do it in this request" is offered also for something an entry stands on that the
     foundation does not hold yet, and runs the writing of the missing fact, decision or source.
   - PL: Odpowiedź „zrób to w tej prośbie” dotyczy też rzeczy, na której stoi wpis, a której fundament
     jeszcze nie zawiera, i uruchamia dopisanie brakującego faktu, decyzji albo źródła.

Skill and instruction files written by the task's rows and items (no entry written for them):
`task-cycle/skill/SKILL.md` step 10 (row 6; item 6) and the "Working copies" paragraph (item 11);
`agent-instructions/README.md` ("Integrate into `foundations`", row 7; item 7);
`task-cycle/skill/correction.md` (item 8, the list of kinds);
`task-cycle/skill/request_template.md` (item 9, the example of kind 17; item 10, the row "A correction",
whose last clause carries item 8's kind 16 as well).

## Choices (with the way rejected and its cost if wrong)

1. **WAY-261: the new sentence is a second paragraph, not a fourth sentence.** The first paragraph
   already holds three sentences, the template's limit. Rejected: a fourth sentence in the first
   paragraph (breaks the template's 1-3). Cost if wrong: a reviewer who reads the second paragraph as
   no "part of another question" asks to move it; the move is mechanical.
2. **WAY-375: the base-copy rule is folded into the first paragraph's last sentence**, as "a copy of a
   base that the script does not assign to a task — one named for no task, or for a branch it does not
   find — among them". It keeps the quoted start of the test (`A directory of a cycle that the script
   does not remove stays`) intact. The two cases (named for no task; branch not found) are the two the
   script keeps (`task-cycle/remove_merged_worktrees.py`, `inspect_state`). Rejected: a separate
   sentence (the paragraph would hold four). Cost if wrong: a long sentence to rewrite.
3. **WAY-375: the narrowing sentence names the area as "removing a cycle's own directories whose
   branches are merged"**, the task's "usuwanie własnych, scalonych katalogów cyklu". Rejected: naming
   the script (binding sentences may name it, but the area is wider than one script).
4. **WAY-376: "waits for no one to read the list"** is how the binding sentence says that the cycle's
   removal does not show the list. Rejected: "shows it to no one" (the script prints the list and the
   orchestrator sees it; only the human's reading before the removal is dropped).
5. **Item 10, the row "A correction":** the state line's why names the cause by the sources of item 17's
   pairs: "corrected for your remarks" only for `remark`, "corrected for your answer to an item" for
   `item <n>`, "refreshed from the target branch at your request" for `target-branch`, each in its words
   when there are two. The phrases are mine; the task fixes only the first and says "to, co ją
   uruchomiło". Rejected: one fixed phrase per source in the check script (the task does not touch
   `request_check.py`). Cost if wrong: a reviewer wants other words; no script reads them.
6. **Item 6 in the skill:** the sentence is added to the paragraph of step 10 as the task says, with a
   reference to WAY-261; no change to `request_template.md` for it (the task lists none). Where the
   request names the test and the task: the existing *Findings outside the task's scope* and kind 4
   already carry a check that failed and passed again; see "Problems observed" 3.
7. **WAY-261 *Rejected* and WAY-375 *Rejected* take the ways of the rows' sources**, each with the cost
   the source gives; the writer's own derivations stay out (WAY-134).
8. **The `.runs/` directory of this agent holds no copy at return.** I made test logs in
   `.runs/author/` and removed them (the figures are in the table above).

No change of section 4 of the skill (plan versus code) applies; there is no plan. No file over the
threshold of a rule of size was grown (this repository holds no guidelines; WAY-365 does not apply).

## Reaches beyond the handoff

- `task-cycle/remove_merged_worktrees.py`, the docstring and the two functions `inspect_state` and
  `describe_owner` (read only), to word item 3 as the script behaves: which base copies it keeps and
  why. Reason: the task says "kopia bazowa, której skrypt nie przypisze do zadania" without naming the
  cases.
- `task-cycle/change/ui_check.md` (read whole, not changed), for item 11: the paragraph it ends with
  says where a screenshot shown to the human goes.
- `task-cycle/test_remove_merged_worktrees.py`, the `decision:` lines (grep), to keep the quoted
  sentences true.
- `foundations/decisions.md` WAY-373 (read whole, not changed), see "Problems observed" 2.
- `elements/decisions/skill/read.md` and `decide_entry.md`: the skill file names them for step 1 and 2.

## Problems observed

1. **The task misplaces the list of WAY-289.** *Decisions in play* and *To do* 8 say the list "An answer
   to do it in this request, to an item of *Fix or let through* other than item 8, ..." is in WAY-289. That
   paragraph is in `task-cycle/skill/correction.md` (line 75 before the change); WAY-289's binding sentence
   holds a shorter list: "a step or a check the cycle skipped, a proposal of the task's own sections not
   applied and an incomplete reading of the review of the whole change". I changed both places: the
   correction file's list (as item 8 says) and WAY-289's sentence and *Rationale*. Evidence: `grep -n
   "other than item 8" foundations/decisions.md` finds no such text.
2. **WAY-373 names "a screenshot" as a working copy kept in the agent's directory, with no exception.** *To
   do* 11 adds the exception to the paragraph of the skill only, which copies WAY-373's sentence. A
   screenshot shown to the human is no working copy made "to check something" in the sense of the
   second sentence, so I read the two as compatible and did not touch WAY-373 (the task changes none),
   but a reviewer may see a collision. Guess, not verified: no test compares the two texts.
3. **Item 6 stands on a part the request template does not give.** The skill and WAY-261 say that the
   request "names that test and the task that fixes it, or proposes one". The template has no kind for
   it: a flaky test that failed once and passed lies under *Checks* and, where its file is outside the
   task's parts, under *Findings outside the task's scope* "for the human to choose which become new
   tasks"; kind 4 excludes a check that failed and passed again. The orchestrator can do what the sentence
   says in *Findings outside the task's scope*, so I added nothing to the template; whether a request
   item is wanted is for the reviewer or the human.
4. `ui_check.md` says both "keep none" and "move it ... where none is settled into your directory"; not
   in the task, left as it is.
5. I rewrapped only the lines I touched and the paragraph tails that my change moved, so the diff of
   `SKILL.md` and `decisions.md` holds some rewrapped lines; no line I added is over 100 characters,
   except the table row below. The row "A correction" of the variants table of `request_template.md` was
   a single long line before and is longer now (a table row cannot be wrapped).

## Unread material

none. (Every file the handoff names was read whole; the invariants file whole; the glossary whole; the
decisions WAY-13, WAY-25, WAY-375, WAY-376, WAY-261, WAY-243, WAY-289 and WAY-373 whole. WAY-140,
WAY-153, WAY-300, WAY-233 and WAY-148 were not opened whole: the change needed none of their text, only
the names the entries I edited already carry. Of the part map and the decision log, the rest was not
read.)

## Searches not found or unclear

- The list "An answer to do it in this request, to an item of *Fix or let through* other than item 8,
  ..." that the task's *Decisions in play* (WAY-289) and *To do* 8 place in WAY-289: not in WAY-289; it is
  in `task-cycle/skill/correction.md`. I read WAY-289's own list as the one meant (problem 1).
- The *Verification* of WAY-376 holds the words the task calls "zdanie wiążące i *Rationale*, akapit, który
  zaczyna się od 'the files a repository ignores'": the paragraph is the *Rationale* alone; found, no
  trouble.
- The foundation check lists no invariant for the rewritten sentences (`listed:` lines absent), so the
  question the handoff raises about invariants that read `test` has no finding.

## Working copies

None remain. I made no worktree and no clone. The only files I made in `.runs/author/` were four test
logs; each was removed (`find .runs/author -mindepth 1 -delete`), and the directory stands empty.
