# Report 02 — the one author of the whole change

**Status:** done with concerns (the concerns are in "Concerns" below; none blocks review).

## Commits (branch `task/cycle-remarks-batch-3`, base `3177e10`)

- `0b81978` docs: a cycle on the-way starts from the remote target branch, fast-forwarded first (WAY-298) — To do 1: `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`; the new decision WAY-298 and, in the same file, the WAY-291 *Verification* example (To do 4) in `foundations/decisions.md`.
- `f13c800` docs: foundation entries a change writes skip the set critique; the nightly review is named without its private script — To do 2 (`elements/common/way_of_working.md`) and To do 3 (`task-cycle/record_template.md`, `task-cycle/remarks_check.py`).
- `7841f00` fix: the language check does not count quoted text or block quotes — To do 4 (`task-cycle/request_check.py`, `task-cycle/test_request_check.py`).

Files changed (added/removed lines, `git diff --stat` before committing): `elements/common/way_of_working.md` 3/1, `foundations/decisions.md` 57/4, `task-cycle/record_template.md` 2/3, `task-cycle/remarks_check.py` 6/6, `task-cycle/request_check.py` 20/11, `task-cycle/skill/SKILL.md` 14/6, `task-cycle/skill/correction.md` 10/4, `task-cycle/test_request_check.py` 62/0. Line endings: all LF (`git ls-files --eol`), kept.

## Checks (command, exit code)

- Test first, failing run: `python -B task-cycle/test_request_check.py` -> exit 1 (two new tests failed on their assertions: `test_a_block_wholly_in_quotation_marks_is_not_judged` got `English`, `test_quoted_text_and_quoted_lines_are_not_counted` got share 0.362; the third new test, the unpaired mark, passed from the start because the old code cut no quotes — it guards the new code). Fixture arithmetic of that third test corrected by hand (33 words, 9 function words) before the implementation.
- Same command after the implementation: exit 0 (55 tests OK).
- Mutations tried, each made the file's tests fail (exit 1), then restored (`cmp` against a backup, tests exit 0): block-quote stripping removed; the straight-quote alternative removed; the „…” match allowed to cross lines. A first version of the unpaired-mark test let the cross-line mutant pass (exit 0); I added a closing ” on a later line of its fixture and the mutant then fails (exit 1).
- `python -B gate/run_tests.py task-cycle` -> exit 0 (142 tests).
- `python -B gate/run_tests.py elements/common` -> exit 0 (109 tests).
- `python -B gate/run_tests.py agent-instructions` -> exit 0 (18 tests).
- `python -B gate/run_tests.py relation-model` -> exit 0 (12 tests).
- `python -B gate/run_tests.py instruction-files` -> exit 0 (104 tests, 5 skipped as before).
- `python -B elements/common/foundation_check.py` (from the worktree root) -> exit 0, `0 errors`.
- Not run: the product's full gate (`python -B gate/run_tests.py` without argument) — the orchestrator's run (handoff, WAY-160). The skill entry points script was not run: no skill description changed.

## Own-work check (WAY-164)

- Requirement most likely not met: "the language check does not count quoted text" must make the real motivating case — a Polish task with English quotations — read `not English`, without cutting more than the quotes.
- Check: ran `english_share(task_text(...))` on this cycle's frozen task (a Polish task with English quoted decisions inside *To do* and *Need*). Result with the change: share 0.021 on 336 words, `not English`. With the quote and block-quote patterns disabled in the same process: share 0.175 on 559 words. So the quotes carried most of the English words, and what remains is Polish text. The three new tests and the mutations above cover the unpaired mark, the block quote and the straight quote.

## Foundation entry written (WAY-134, row 1) and meaning sentences

- **WAY-298** — How does a cycle on the-way itself start from the current rules? (`foundations/decisions.md`, end of the log; the next free number, no entry and no withdrawn number held it). Scope `task-cycle`; Relations `derives from WAY-127`; *Origin* `none`. Mark: **row 1**.
  - Meaning, English: In the-way itself the cycle fetches and fast-forwards the checkout the session works in before it creates the task branch, restarts from the entry point, and stops when it cannot fast-forward; a correction does the same, merging the remote target branch into the request's worktree, and its merge takes the remote branch in a product as well.
  - Meaning, Polish: Na samym the-way cykl, zanim założy gałąź zadania, pobiera zmiany i przewija do przodu kopię, w której pracuje sesja, po czym zaczyna od nowa od punktu wejścia; gdy przewinąć się nie da, staje. Korekta robi to samo, a w worktree requestu scala do niego zdalną gałąź docelową; jej scalenie gałęzi docelowej bierze gałąź zdalną także w produktach.
  - *Rejected* holds, with the cost beside each: the two ways of question 1 (reading the skill from the base commit; a `git pull` habit or session hook outside the-way), the way of question 2 (reading the skill again, without the entry point) and the three of question 3 (new cycle only; fast-forward in the correction on the target branch only; "remote target branch" only in the sentence for the-way itself), as the task gives them. I left out the counts and the commit hash the task's *Not chosen* quotes ("15 times", `8e5115a`), since *Rejected* of a written entry names no count; the cost is that the "often changed" fact is stated without the number. Question 4 (guidelines) is no way of this decision and is not in it.
- The other two entry changes are edits in place, not entries: the WAY-291 *Verification* example (`complies: the script reads a correct Polish block full of English names outside quotes as English, ...`, re-wrapped) and the sentence in `elements/common/way_of_working.md` (WAY-10, WAY-114).
- Search of the foundation (WAY-33): searched `current target branch`, `remote target branch`, `target branch`, `fast-forward`, `fetch`, `cycle_remarks_digest` and `task's worktree` over `foundations/*.md` and the repository's md/py files. No entry states the settlement of row 1 already, and none collides with it: WAY-127 (reading from the checkout the session works in) is the entry WAY-298 derives from; WAY-140 concerns effects outside the repository, and the fast-forward is inside it. No glossary entry or part-map change was found to need an edit (no file added, no term new).

## Choices and adaptations

- **Correction restart condition.** `correction.md` says "In both cases, where something came in, start again from the entry point". The task says to start again "in both cases"; read plainly, that restarts the correction even when nothing came in, and the restarted correction would read the same paragraph again. Rejected: the unconditional wording (a loop in the letter of the text). Cost if wrong: the human wanted the restart unconditional; one phrase to delete. The step 4 sentence is copied exactly and is conditional by its own structure (restart after the fast-forward).
- **`correction.md` structure.** The new paragraph stands first and the old "Before anything else, read the field *Reserved choice*" paragraph begins "Then read the field *Reserved choice*"; its text is otherwise unchanged except for the line wrap.
- **WAY-298's second sentence** names the correction's merge of the remote target branch "in a product as well", because the task's answer to question 3 and row 1 make `correction.md`'s change cover products.
- **Line numbers**: all quoted line numbers matched the base file, except that the To do 1 step-5 sentence is at lines 125-126 as the task says and the WAY-291 *Verification* sentence is at `foundations/decisions.md:8810` as the task says; no correction needed.

## Concerns (not blocking)

- `task-cycle/skill/SKILL.md` still says at the sentence after step 3 "The cycle writes only in the task's worktree and changes nothing outside the product repository" (line 68). The task treats the new clause "the one change the cycle makes outside the task's worktree" as removing the contradiction and does not change line 68, so I left it; a reader of line 68 alone still meets "only". If the reviewer holds that a contradiction, the fix is one clause in line 68 (out of the four To do items).
- Step 12 of the same skill still says "merge the current target branch into the task branch" while the correction now merges the remote target branch. The task changes only `correction.md:20`; I did not touch step 12.
- In a correction in the request's worktree of the-way itself, the new first paragraph merges the remote target branch and the existing "First merge, never rebase, the remote target branch" sentence merges it again: the second merge is a no-op. Left as the task gives it.
- The correction paragraph says "step 4 of `implement-task`" for the fast-forward; the skill's name is `implement-task` in its front matter and `the-way-implement-task` as a project skill. The skill's own text uses `implement-task` elsewhere, so I followed that.

## Reaches beyond the dispatch

- `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md` (named in the user's global instructions, read after a first script of mine garbled non-ASCII text from a heredoc); I then edited all non-ASCII text with the Edit tool and restored `task-cycle/test_request_check.py` from git once before redoing it. Nothing of that stayed in a commit.
- Searches over `foundations/*.md` and the repository's files for the identifiers named above (WAY-33 search), and `sed` reads of WAY-10, 25, 27, 30, 34, 114, 120, 127, 134, 140, 290, 291, 292, 296 as the handoff named, plus WAY-293 to WAY-297 only in passing (the neighbours of the new entry).
- A scratch file `C:\Storage\repos\scratch_t1.txt` I wrote by a wrong relative path was deleted at once; outputs of the checks are in the session scratchpad.

## Searches not found or unclear

- `elements/decisions/examples.md` names WAY-03 as the form example; the task's *Rejected* source holds the ways with their costs in the form "way — cost", while the log's other entries use `;`-joined "way — cost" items; I followed the log's form. Nothing was missing.
- The handoff's wording "the corrected example of WAY-291" is at `foundations/decisions.md:8810`; the `Verification` line there had its text re-wrapped by me because the replacement made the line longer than the file's 100 characters; unclear whether the task wanted the wrap kept as the original.
- Nothing else looked for was missing; the handoff, the task and the method named every file I needed.
