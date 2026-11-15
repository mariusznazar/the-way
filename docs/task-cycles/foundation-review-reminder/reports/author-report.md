# Author report — foundation-review-reminder

**Status:** done (with two additions of mine that the orchestrator should see, under *Choices* 6 and 7).

## Commits (task branch `task/foundation-review-reminder`, base `ff88ca3`)

1. `f96ddd2` — Raise the review reminder's threshold to 60 merges and end the count with exit 2 where git fails to list or describe the review tags: `task-cycle/review_reminder.py`, `task-cycle/test_review_reminder.py`.
2. `c0ba78b` — Make the cycle read the backlog for the review's line before it writes the reminder, and let the foundation review group the log's entries that are no decisions: `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`, `README.md`, `foundation-review/SKILL.md`, `weak_points.md`, `proposals.md`, `with_the_human.md`.
3. `b7ec371` — Rewrite WAY-24 and WAY-300 for the review's line in the backlog and a threshold that stands in the reminder script: `foundations/decisions.md`.

Diff against base: 10 files, +252 / -73 (`git diff --numstat ff88ca3 HEAD`): `README.md` +2/-1, `foundation-review/SKILL.md` +15/-7, `proposals.md` +18/-0, `weak_points.md` +29/-1, `with_the_human.md` +11/-2, `foundations/decisions.md` +68/-29, `task-cycle/review_reminder.py` +31/-12, `task-cycle/skill/SKILL.md` +14/-5, `request_template.md` +17/-7, `test_review_reminder.py` +47/-9.

## Checks (command, exit code)

| Check | Command | Exit |
|---|---|---|
| Failing run of the tests written first (against the old code) | `python -B task-cycle/test_review_reminder.py` | 1 — 3 failures, each for the expected reason: `test_a_git_that_cannot_list_the_review_tags_is_an_error` and `test_a_git_that_cannot_describe_a_tag_that_exists_is_an_error` got exit 0 where 2 was asserted; `test_the_reminder_starts_at_sixty_merges_and_not_at_fifty_nine` saw `threshold: 30` and `reminder: yes` at 59 merges |
| Passing run after the code | `python -B task-cycle/test_review_reminder.py` | 0 — 11 tests OK |
| Foundation entries | `python -B elements/common/foundation_check.py` | 0 — `0 errors` |
| Directory of the change | `python -B gate/run_tests.py task-cycle` | 0 — 480 tests OK (includes `test_request_check.py`, `test_tracked_files_private_paths.py`) |
| Shared elements | `python -B gate/run_tests.py elements/common` | 0 — 232 tests OK |
| Own-work check, real history | `python -B task-cycle/review_reminder.py ff88ca3` | 0 — `tag: foundation-review/2026-11-15`, `merges: 1`, `threshold: 60`, `reminder: no`; the same tag and count come from `git describe` and `git rev-list` run by hand |
| Error path, real git | `python -B task-cycle/review_reminder.py nonexistent` | 2 — `Error: 'nonexistent' names no commit in .` |

Not run: the full gate (`python -B gate/run_tests.py` without a directory), as the handoff says; `python -B agent-instructions/skill_entry_points.py --write`, since no `description:` line of any skill changed; `request_check.py` itself, since it reads a request, not the template (its tests passed in the task-cycle run).

## Own-work check (WAY-164)

- **Requirement most likely unmet:** point 4 — the script ends with exit 2 for an error of git, *and* still reads a real absence of tags as "none", whatever language git's messages are in; and point 1 — the sentence's two forms plus the unreadable backlog, spread across step 13, the request template and WAY-300 without one contradicting another.
- **Check:** (a) the tests above, where a stub replaces only the one git command that must fail and answers in Polish, so no English message can save the code; the real-git "no tag" test (`test_without_a_tag_every_merge_since_the_start_of_history_counts`) keeps passing through the new path. (b) The script on the real history (table above) agrees with `git describe` and `git rev-list` by hand. (c) I read the three texts for the same three conditions (no line / line stands / backlog unreadable) and the same rule below the threshold ("says nothing about a review").
- **Showed:** all pass. One thing I could not make fail for real: I tried to find a real corruption of a repository that makes `git describe` fail where `git tag --list --merged` works. A missing side commit, a ref to a missing object and a corrupt tag object all give git's own verdict "no tag" (describe exit 128 *and* the list empty with exit 0), so for those the new code agrees with git. The two error tests therefore use a stub of one git command, which is the only way I found to give the code a failing describe with tags present.

## Mutation in my head

- `if not listed.stdout.strip(): return None` turned into `return None` always → the two-tag tests fail. Describe failure read as no tag → `test_a_git_that_cannot_describe...` fails. List failure read as no tag → `test_a_git_that_cannot_list...` fails. Threshold 59 or 61 → the boundary test fails. Unprotected: the *wording* of the comment at `THRESHOLD`, and the case "list gives a tag, describe gives empty output with exit 0" (cannot happen with git; no test).

## Foundation entries (WAY-134: one sentence in English and one in Polish, marked)

- **row 1** — WAY-300, second paragraph of its binding sentences. EN: from the threshold on, the orchestrator reads the product's backlog for an open line whose name holds `review-foundation` and the repository's name; with no such line or an unreadable backlog the sentence asks the human to add the task of the review, otherwise it points to the line without urging, and the cycle adds or changes no line. PL: od progu cykl czyta backlog produktu i szuka otwartej linii z `review-foundation` i nazwą repozytorium w nazwie; gdy jej nie ma albo backlogu nie da się przeczytać, zdanie prosi człowieka o dodanie zadania przeglądu, gdy stoi — wskazuje ją i nie ponagla, a cykl linii nie zakłada ani nie zmienia.
- **row 2** — WAY-24, binding sentences 2–3. EN: the review stays a run of the skill `review-foundation` in a session with a human; a task of the product's backlog may stand for it, and a human adds it, never a cycle. PL: przegląd zostaje przebiegiem skilla `review-foundation` w sesji z człowiekiem; zadanie w backlogu produktu może go oznaczać, ale zakłada je człowiek, nigdy cykl.
- **row 3** — not an entry of the log; written in its place by the rule of the place (skill files of `foundation-review/`: `SKILL.md`, `weak_points.md`, `proposals.md`, `with_the_human.md`). EN: at every run the review finds all the log's entries that are no decisions by the questions "Where it goes", groups them by the place they go to with a count, and the human decides which whole groups go into a backlog task this time, the rest waiting. PL: przegląd przy każdym przebiegu znajduje wszystkie wpisy dziennika, które decyzjami nie są, według pytań „Where it goes”, układa je w grupy według miejsca z liczbą wpisów, a człowiek decyduje, które całe grupy idą do zadania tym razem, reszta czeka.
- **row 4** — not an entry; written in code: `THRESHOLD = 60` in `task-cycle/review_reminder.py` with its comment and the boundary test. EN: the threshold is 60 merges, held by a test at 59 and 60, with the reason (rhythm and accepted price) at the value. PL: próg to 60 scaleń, trzymany testem na 59 i 60, z powodem (rytm i przyjęta cena) przy wartości.
- **row 5** — WAY-300, first paragraph. EN: the sentence says "from the threshold of the reminder script on" and keeps the rule that the threshold is one number for every product, which no product sets. PL: zdanie mówi „od progu skryptu przypomnienia” i trzyma regułę, że próg to jedna liczba dla każdego produktu, której produkt nie ustala sam.
- **projected:** none. **the cycle's:** none (the entries above carry the rows whole; the other edits are text of skills and templates).

Point 5 of *To do* was also written in WAY-300: the *Verification* example now says the reminder ends *How to merge* (was "opens its request"); the *Rationale* lost the sentence about the history of the first product, the rhythm for 30 and the weak point "repeats … also while the human puts it off on purpose"; *Rejected* lost "50 merges". Step 13 now says that below the threshold the description says nothing about a review, and that a fetch must bring the tags.

## Choices (with the way rejected and its cost if wrong)

1. **No tag versus a git error (point 4).** `git tag --list --merged BRANCH 'foundation-review/*'` first: exit 0 and empty = no tag; non-zero = error; non-empty list then `git describe`, whose failure is an error too. Rejected: reading the message of `git describe` ("No names found", "No tags can describe") — git translates its messages, so the code would break on a Polish locale; and checking only `describe`'s exit code against a second command run on failure (same result, one more call when a tag is absent). Cost if wrong: if `--merged` ever differed from describe's reachability a tag could be listed that describe does not give, which now ends in exit 2 instead of a silent count from the start — a visible failure, not a wrong count.
2. **Test with a stub of one git command** (`run_with_failing_git`), real git for everything else. Rejected: a real corruption (none made describe fail while the list worked, see own-work check) and a fake `git` executable on `PATH` (Windows shim problems).
3. **Restart test uses `mock.patch.object(review_reminder, "THRESHOLD", 3)`** so it builds 6 merges and not 61. Rejected: building 61 merges (about 3 git calls each, nearly doubling a 7-second test file). The boundary test uses the real value, 59 and 60.
4. **Comment at `THRESHOLD`:** rhythm "every 2 to 10 weeks in the-way, 3 to 15 in a product" and the price. Reckoning mismatch: the task says "od 2,5 do 10 tygodni w the way"; 60 / 26 merges a week = 2.3, so I wrote "2 to 10". Everything else of the task's rhythm (3 to 15, about 10 days) matches 60 / 21 = 2.9, 60 / 4 = 15, 60 / (49 / 8 days).
5. **WAY-300 relations:** added `derives from WAY-107 · derives from WAY-140` (the reading of the backlog and the ban on writing there), beside WAY-24. Rejected: leaving the two as references in the sentence only. Cost if wrong: an over-linked entry; WAY-161 does the same for WAY-140.
6. **Addition not in the task: step 13 on exit code 2** — "where the script ends with exit code 2, record its message under *Verification* and write no reminder, since the count is unknown". The task makes git errors exit 2 but says nothing of what the cycle does with it. Rejected: leaving it unsaid (an orchestrator would invent a reaction), and writing the "add the task" form on an unknown count (it would claim a number that is not known). Cost if wrong: a failed count shows only in *Verification*; the orchestrator may prefer to stop the cycle.
7. **Addition not in the task: `foundation-review/SKILL.md` step 7** tells the review to say to the human that an open line of this review is to be marked done by the task place's rules. Reason: an open line left behind makes the next reminder "point and not urge" for ever. Rejected: leaving it to the setup of the human's daily advisor (out of scope of the-way, so the gap would stay in the-way). Cost if wrong: one sentence to delete.
8. **WAY-24 *Rejected* kept** "the review set as a task of the backlog, run by a cycle that ends in a request of corrections" and "a ready task of the review copied into the backlog"; both still describe ways not taken (a cycle runs the review; a ready task for a cycle). Only the *violates* example "set as a task of the backlog with a date" and the binding words "and no task of the product's backlog" went. Cost if wrong: the first rejected way reads partly against the new binding sentence; the human can read it as I did, "run by a cycle" being the rejected part.
9. **`elements/decisions/template.md` unchanged:** its five questions "Where it goes" are the review's instrument as they stand, read for an entry of the log as for a settlement; `weak_points.md` points at them and does not copy them.
10. **Size rule (WAY-365):** `review_reminder.py` is 121 lines, `decisions.md` is a log of entries (no function); no part of the change stands over a threshold and the product's coding guidelines are not read for the-way (WAY-328). No move.

## Reaches beyond the handoff

- `Grep` of `reminder|THRESHOLD|30 merges|WAY-300` over the repository, and of `reminder|review tag|review-foundation…` over `foundations/` — the search of the whole foundation (WAY-33) after settling the entries; it found nothing further than the files listed. WAY-24's other references (lines about facts and dates, "no date in an entry") name only its first sentence and stay true.
- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/way_of_working.md`, `elements/common/rules.md`, `elements/decisions/examples.md` — named by `SKILL.md` of the element, read whole.
- `project-level/backlog_place.md` and `project-level/task_line.md` (searched for "identifier"): to word step 13 and the rejected identifier way without WAY-329, which is withdrawn.
- `task-cycle/request_check.py` (search for "template", "How to merge"): confirms the check reads the request, not the template text.
- `a file of the author's agent instructions`, `git.md`, `knowledge_artifacts.md` — the user's rules a hook and the instructions pointed me to; no content of them enters a file.
- A failed first working-copy command ran three read-only git commands in `the main checkout of the repository` (the main checkout) because the directory of the copy did not yet exist; it wrote nothing there (`git status` clean).

## Unread material

Read in part, after a read of a fixed length that ended before the entry's end (the tail of each is *Rejected* or *Verification* prose):

- WAY-161 (`foundations/decisions.md`): read to the middle of *Rejected* (the sentence that begins "the small findings joining a fix only where one runs anyway"); its last lines unread.
- WAY-150: read to the middle of *Verification* (the *violates* list, "in a log with topical sections the decisions outside the work's sections…"); the rest of that list unread.
- WAY-344: read to the middle of *Verification* (the *complies* example on the audit's measures); the rest, about 70 lines, unread. The change adds no script that reads a file written by an agent, so the rule does not bind it.
- WAY-107: read through *Rationale* up to "…and the place can change"; the last lines of it unread.

`foundations/invariants.md`: read the eight named entries whole and no other. `foundations/part_map.md`: the entries `decisions`, `task-cycle` and `foundation-review` whole, and the list of headings. Everything else the handoff names was read whole.

## Searches not found or unclear

- The repository name that the line's name must hold: the task says "nazwa repozytorium" and the template of the sentence gives no source. I wrote "as the `## Backlog` section of the root `AGENTS.md` names the product" (in the-way that is `the-way`). Unclear whether a product whose directory name differs from that should use the directory name; the orchestrator may answer.
- `project-level/backlog_place.md` says what open means nowhere (the task says "reguły miejsca zadań"); step 13 therefore refers to the rules of the task place and to WAY-107, as the task does.

## Working copies

`.runs/author/exp` (a scratch repository for the experiments on git's behaviour) and the two output files of the focused gate runs: removed. `.runs/author/` stands empty.

## Questions to the orchestrator

None blocking. Recommend a look at choices 6 and 7 (additions beyond the task).
