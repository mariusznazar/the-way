PASS cdbde3d23ef92f3e5e844ea1217ac40c469942bd

# Review of the fix — task `walkthrough-in-running-product`

Range `940893de..cdbde3d2`, one commit, `cdbde3d2` ("Fix the findings of the review of the walk
through the running product"); `git rev-parse HEAD` gives `cdbde3d23ef92f3e5e844ea1217ac40c469942bd`,
the head given. Bounded by `reports/fix-findings.md` (I1-I6 blocking, M1-M6 Minor within the task),
as `task-cycle/review/fix.md` gives. Files of the fix: `foundations/decisions.md`,
`task-cycle/change/SKILL.md`, `task-cycle/change/walkthrough.md`,
`task-cycle/skill/request_template.md` (96 insertions, 77 deletions).

Counts: 0 blocking; every finding of the file fixed; 4 new Minor findings in the fix diff; 0 outside
the task's scope.

## The findings

| Finding | State | Evidence on `cdbde3d2` |
|---|---|---|
| I1 | fixed | `task-cycle/change/walkthrough.md:48` — the column "By what" names only ways of the running product ("a reading of the data the running product holds"); `:50-51` adds that a reading of the code fills no row and a case only the code could check stays unchecked with that reason. |
| I2 | fixed | `task-cycle/skill/request_template.md:497-498` — *Checks* no longer lists the walk's cases; the top part (`:185-187`) keeps them in the reports. No other sentence of the template puts the cases into the description. |
| I3 | fixed | See "I3 against WAY-25, WAY-287 and *To do* 5" below. |
| I4 | fixed | `walkthrough.md:20-22` — "A skill of the product may hold the steps of operation and cites the decision, so search the product's skills for the identifier of each of those decisions and read each skill found": the direction WAY-121 gives. |
| I5 | fixed | WAY-406 *Rejected* (`foundations/decisions.md:6829`) ends at "the cleanup, which WAY-373 gives."; the two course items the task put outside its scope are gone; what stays is the task's own list ("Zostaje przy VOX") and the *Not chosen* of its questions. |
| I6 | fixed | WAY-407 *Scope* reads `task-cycle, project-level` (`decisions.md:6839`), as WAY-238 does for its parallel rule on refinement. |
| M1 | fixed | WAY-406: first paragraph of three sentences answering who walks and for which changes, then a paragraph on the move to a stage of its own (one sentence) and one on the case of no settled way (two sentences); WAY-319's added sentence stands in a paragraph of its own (`decisions.md:4880-4883`). |
| M2 | fixed | WAY-406 *Rationale*: "a team of the human who owns this process"; the opening sentence no longer tells what the cycle lacked before. |
| M3 | fixed | `task-cycle/change/SKILL.md:155-157` — the bullet opens "as the one author or the executor of a slice" and says "(the fix and a correction report no walk)". |
| M4 | fixed | WAY-121 *violates* re-flowed; the short line is gone (one line is now longer than the log's width, new Minor N4). |
| M5 | fixed | `walkthrough.md:73` — "(WAY-406; WAY-13 for what cannot be undone)". |
| M6 | fixed | WAY-407 and WAY-408 binding sentences name "the author of a change or the executor of a slice"; the rest of their text speaks of "the author or the executor" or "the agent". The heading of WAY-408 still says "the author" (new Minor N3). |

### I3 against WAY-25, WAY-287 and *To do* 5

- **WAY-25.** The collision between WAY-408's unconditional sentence and WAY-289's judgment of what is
  felt now has its precedence recorded in the decision that prevails: WAY-408 *Relations* read
  `derives from WAY-239 · narrows WAY-289` (`decisions.md:6877`), and its binding sentence states the
  area: "in this area this decision prevails over WAY-289, under which the cycle puts before the human
  only what it judges will be felt". WAY-289's *Relations* (`derives from WAY-161 · derives from
  WAY-287`) name no relation to WAY-408, so the two do not narrow each other, and nothing follows along
  a chain. What the human accepted gives the outcome: *To do* 5 ("błąd spoza zakresu zadania znaleziony
  przy przejściu trafia do sekcji dla decyzji człowieka jako sprawa do rozstrzygnięcia (zrobić z niego
  zadanie czy puścić)") and row 5 ("błąd poza zakresem zadania zgłasza do PR-a jako sprawę dla
  człowieka") send every such error to the human, with no judgment of what is felt. WAY-25 then asks
  the request to name the precedence with those passages; the fix report gives them for the request,
  which is the orchestrator's to write — to be checked there, not in this diff.
- **WAY-287.** WAY-408 now names the group: "under *Fix or let through*", which WAY-287's second
  paragraph requires of a decision that adds a kind of item. The template carries the item inside kind
  8 (`request_template.md:260-264`), which stands in that group, and lists it, so "the template of a
  request's description lists every kind" holds; no new number was needed, and `correction.md`'s
  handling of item 8 still reaches it.
- **The loss the finding named.** Kind 8 now restates each such error "with no judgment of what is
  felt", and the lower part's *Findings outside the task's scope* (`request_template.md:533-536`) lists
  each with the author's words and where it showed, so the error has a place in the description
  whatever the orchestrator judges. The single question "Make a task of it?", with merging as letting
  it through, matches the task's "(zrobić z niego zadanie czy puścić)" and the group's rule for an item
  that carries only that question.
- WAY-408's *violates* gains "or leaves it out because the cycle judges it will not be felt", which
  the template now forbids; its *Rationale* gives the reason for the precedence.

## New findings in the fix diff

All Minor; none blocks (`task-cycle/review/fix.md`, WAY-162).

- **N1.** `task-cycle/skill/request_template.md:250` — kind 8 keeps its title "*Unfixed findings the
  user or the human will feel*" while it now also holds the walk's errors "with no judgment of what is
  felt". A reader who goes by the titles of the kinds expects only felt items there; the sentence below
  says otherwise, so the item is not lost.
- **N2.** `request_template.md:261-262` and `:534-535` — the template speaks of the error "its author
  reported" and "an author's walk", while WAY-408 now has the executor of a slice report such errors
  too. An orchestrator of a planned change could read the item as covering only a one-author change;
  "the author or the executor of a slice" would match WAY-408.
- **N3.** `foundations/decisions.md:6862` — WAY-408's heading still asks "What does the author do with
  a case of the walk that fell wrong?" while its sentences bind the executor of a slice as well.
- **N4.** `foundations/decisions.md:3887`, `:6787`, `:6847`, `:6856` — re-flowed lines run past the
  log's width of about 100 characters (108, 121, 116, 115), and `:6801` ("regression. From the") is
  left short; cosmetic.

## Declined to judge

- Whether the request of this cycle quotes the passages of *To do* 5 and row 5 beside WAY-408, as
  WAY-25 asks: the request is not written yet; it is the orchestrator's.

## Checks

| Command (from the worktree root) | Exit |
|---|---|
| `git rev-parse HEAD` | 0 (`cdbde3d2…`, the head given) |
| `git log --oneline 940893de..HEAD`, `git diff --stat` and `git diff 940893de..cdbde3d2` | 0 |
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`; it reports two decisions that narrow each other as an error, so the new `narrows WAY-289` passes it) |
| `python -B task-cycle/private_paths_check.py <file>` for each of the 4 files of the fix | 0 each (`0 listed`) |
| `python -B gate/run_tests.py task-cycle` | 0 (534 tests, OK, 2 skipped) |
| manual: `grep` of `Relations` lines for WAY-408 and WAY-289 | WAY-408 `narrows WAY-289`; WAY-289 names no relation to WAY-408 |
| manual: line lengths of the added lines of the fix diff | four lines over 101 characters (N4) |

Not run: the full gate (the cycle's); the tests of `project-level`, `elements/common` and
`agent-instructions` — the fix changes no file of those parts, and they passed on `940893de` in the
review of the whole change.

## Reaches beyond the dispatch

- `task-cycle/review/fix.md`, whole, as section 1 of `review-change` gives for the review of a fix.
- WAY-25, WAY-287 and WAY-289, read whole in the review of the whole change of this cycle, reread
  for I3 in the passages of their binding sentences and *Relations*; WAY-238 *Scope* for I6.

## Working copies

- `.runs/review-fix/` in the task's worktree held the output of the foundation check and of the
  `task-cycle` tests. Removed before returning (`rm -rf .runs/review-fix`); nothing is kept in
  `reports/`. No git worktree or clone was made, and `git status --short` of the reviewed worktree was
  empty.

## Unread material

- `task-cycle/skill/correction.md`: not read; the fix report's claim that its handling of item 8
  reaches the walk's errors was not checked, since the fix adds no kind number and kind 8 is unchanged
  as a number.
- The rest of the selection of the review of the whole change was not reread; the fix diff touches
  only the entries named above.

## Searches not found or unclear

none
