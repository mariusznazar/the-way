FAIL 938d6ee95381594374ca7dd1fb405ca2a961e63d

# Review of the fix of correction 1 — agent-test-bypass

Range `637d7787..938d6ee9`, one commit (`938d6ee9`, "Fix the review of correction 1: a row that
adopts an outside practice enters accepted, and a question shows the left-out parts as ways"), two
files: `elements/common/skill/task_variant.md`, `project-level/task/skill/find_settlements.md`
(11 added, 9 removed). `git rev-parse HEAD` is `938d6ee95381594374ca7dd1fb405ca2a961e63d`, the head
given. Reviewed as `task-cycle/review/fix.md` gives: the findings file
`reports/fix-findings-correction.md` bounds the review, and the fix diff is inspected for what the
fix itself broke.

Counts: 1 blocking (a new Important finding in the fix diff, which counts as one that remains),
0 Minor, 0 out of scope. Finding 1 of the findings file: fixed in `task_variant.md`; the new
wording in `find_settlements.md` drops a qualification (finding A).

## The findings of the findings file

**1. (Important) The refinement step made a row that repeats the human's choice wait for the human's
acceptance when it adopts an outside practice — fixed, with a new defect in one of the two copies
(finding A).**

Evidence:

- No copy of the step now makes such a row wait. `task_variant.md:33-39` builds the row
  "`accepted`, as any such row is". `find_settlements.md:29-32` says it "enters `accepted`". A search
  of the repository outside `.runs/` for "`waiting`", "row waits", "enters accepted", "built
  `accepted`", "starts `accepted`" and "already `accepted`" found no other place that makes such a
  row wait. The places that state the state — `build_table.md:17-21`, `task_variant.md:40-42`,
  `find_settlements.md:21-25`, `project-level/task/template.md:208-209`, WAY-134
  `foundations/decisions.md:5283-5285`, `:5331`, `:5344-5346`, `:5360` — all say a row repeating a
  choice between ways shown enters accepted. The decisions template and WAY-100 name no state.
- The question stays: "Where the source keeps none, the question of 'How a skill asks' … shows the
  parts the practice leaves out as ways before the table closes" (`task_variant.md:36-38`). The
  same holds in `find_settlements.md:31-32`.
- The parts the human turns down go into the row's *Source*: "go into the row's *Source*, with the
  cost or the reason, as step 4 gives for a question against a choice, so that the decision's
  *Rejected* takes them (WAY-134)" (`task_variant.md:38-39`). The same holds in
  `find_settlements.md:32`.
- WAY-409 and WAY-410 still comply: `git diff --stat 637d7787..938d6ee9 -- foundations/` is empty,
  so neither entry changed, and the rule they comply with (WAY-134's second paragraph) is
  unchanged.

In `task_variant.md` the defect no longer exists. In `find_settlements.md` the fix replaced it with
finding A.

## What the fix itself broke

### Important — within the correction

**A. `find_settlements.md` says every row that adopts an outside practice enters `accepted` as the
human's choice, dropping the qualification that the row repeats a choice the human made between ways
shown.**

Place: `project-level/task/skill/find_settlements.md:29-30`: "A row that adopts a practice from
outside the product (WAY-100) enters `accepted` as the human's choice, like any row that repeats
one, and carries among the ways its source keeps the parts of the practice the human turned down".

What is wrong. The sentence's subject is every row that adopts an outside practice. "Like any row
that repeats one" compares the row with repeating rows; it does not limit the sentence to them. Its
twin in `task_variant.md:33-35` keeps the qualification: "A candidate that adopts a practice from
outside the product (WAY-100) and repeats a choice the human made between ways shown is built
`accepted`". WAY-134 keeps that only rows repeating the human's choice enter accepted, and that "the
human cuts only the rows the agent derived" (`foundations/decisions.md:5360-5361`); its *complies*
says "the rows the agent derived from the material wait for the human" (`:5332`). `build_table.md:15-16`
says "A candidate from the material is a proposal: it enters only on the human's word".

A row the refiner derives from the material that adopts an outside practice — say, from a *To do*
item that names a practice of a source, with no question settling it — would by `find_settlements.md`
enter accepted, marked as the human's choice, though the human never chose it. The cycle then writes
a binding decision from a row the human never accepted. Preventing that is the core of WAY-134.
`find_settlements.md` is what `refine-task` reads at that step, so it is a copy a refiner acts on,
not a side note.

Why it matters. Two copies of one step now give different states for a derived row, and the
unqualified one lets a settlement bind without the human's acceptance.

What would fix it: in `find_settlements.md:29`, add the qualification `task_variant.md` carries —
"A row that adopts a practice from outside the product (WAY-100) and repeats a choice the human made
between ways shown enters `accepted` as the human's choice, like any such row, …".

Grade: Important by WAY-263 — a file of the change restates WAY-134, an entry the change itself
changes, without a qualification. By `fix.md`, a new Important finding in the fix diff counts as one
that remains.

Contradiction: yes — WAY-134 (its first binding paragraph, rows the human accepts, and its
*complies* "the rows the agent derived from the material wait for the human").

## Declined to judge

- Whether a row the agent derived that adopts an outside practice must also get the question that
  shows the left-out parts. WAY-134's second paragraph ties the showing to "the question that settles
  it", which a derived row does not have. Neither the findings file nor the fix reaches this, and
  `task_variant.md` now speaks only of the repeating row.
- Minor finding 2 of the review of correction 1 (the wording "the parts the practice leaves out") —
  not part of this fix, as the findings file says; it goes to the request's list.

## Checks

- `git rev-parse HEAD` — exit 0, `938d6ee95381594374ca7dd1fb405ca2a961e63d`.
- `git log 637d7787..938d6ee9 --stat` and `git diff 637d7787..938d6ee9` — exit 0; one commit, two
  files.
- `git diff --stat 637d7787..938d6ee9 -- foundations/` — exit 0, empty (WAY-409, WAY-410, WAY-100
  and WAY-134 unchanged by the fix).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, 270 tests, OK.
- `python -B gate/run_tests.py project-level` — exit 0, 279 tests, OK.
- Manual: a search of the repository outside `.runs/` for every statement of the state a row is
  built in (patterns above); the two changed passages read against WAY-134, `build_table.md` and the
  task template.
- Not run: the full gate (not the reviewer's). `reports/author-correction-check.py` was not run: its
  assertions test for "waiting" and "accepted", and finding A lies in a missing qualifier, which no
  assertion reads.

## Reaches beyond the dispatch

None beyond the files the handoff names. WAY-134 was read at the head in the review of correction 1
and is unchanged by this range.

## Working copies

None made. `.runs/review-correction-fix/` was never
created; nothing remains.

## Unread material

- `reports/author-correction-check.py`: not read (see Checks).
- `elements/common/skill/definition_variant.md`: only the search hit (line 27); it is the definition
  variant, which the correction does not touch.

## Searches not found or unclear

none
