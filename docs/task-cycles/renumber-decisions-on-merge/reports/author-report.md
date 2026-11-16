# Author report — renumber-decisions-on-merge

**Status:** done

## Commits

- `34db2685` — Renumber a task's decisions before the merge of the target branch where it took their
  numbers (WAY-403). Base `1feb483cbb5a6538a475d6e42629441ba563d7f8`.

## Files changed (added / removed lines)

- `foundations/decisions.md` — +64 / -0: new entry WAY-403, at the end of the section "The course of a
  task cycle", before "The work of a cycle's agents".
- `task-cycle/skill/SKILL.md` — +39 / -2: step 12 of "Request and handoff" (the paragraph that begins
  "Otherwise merge the remote target branch") and the new section "The renumbering of the task's
  decisions" (after step 14, before "The process remarks check").
- `task-cycle/skill/correction.md` — +9 / -5: the paragraph "In the-way itself, before anything else"
  and the paragraph "Take a link to the request".
- `task-cycle/record_template.md` — +4 / -1: the *Events* paragraph (one sentence on the row of the
  reconciliation that gives the conversion).

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` (from the worktree root) —
  exit 0, `0 errors` (first run before the fix of the example numbers: 15 errors, `WAY-500`…`WAY-504`
  named no decision of the log; the examples now give bare numbers without the prefix; second run
  exit 0). Output in `reports/author-foundation-check.txt`.
- `python -B gate/run_tests.py task-cycle` — exit 0, 534 tests, OK (skipped=2).
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 37 tests, OK (expected failures=2).
- `python -B gate/run_tests.py elements/common` — exit 0, 257 tests, OK.
- `python -B gate/run_tests.py installation` — exit 0, 62 tests, OK.
- `python -B elements/common/decision_index.py --output .runs/author/index.md --decision WAY-403`
  and `--part task-cycle` — exit 0 (the index holds WAY-403).
- `python -B agent-instructions/skill_entry_points.py --write` not run: no skill was added, renamed,
  moved, and no description changed.
- Not run: the product's full gate (`python -B gate/run_tests.py` with no directory), as the handoff
  says.

One-line result: all focused checks pass; the full gate was not run (the cycle's).

## Own-work check (section 3)

- Requirement most likely not met: To do 2 — a single pass that rewrites every reference, with no
  damage to a longer number (`WAY-35` inside `WAY-355`) and no chain (`355 -> 360`, `360 -> 365`),
  the human's quoted remarks left as they are. The change is text, so the check is on the mechanism
  the text prescribes: `reports/author-passcheck.py` applies a map `355..360 -> 360..365` once, with
  `re.sub(r"WAY-(\d+)\b", ...)`, to `WAY-355 and WAY-360 and WAY-35 and WAY-3550 and WAY-359` and
  asserts `WAY-360 and WAY-365 and WAY-35 and WAY-3550 and WAY-364`; `python -B
  reports/author-passcheck.py` exit 0. It shows that one pass with whole-number matching gives the
  result the text asks for, while a run decision by decision would chain `355 -> 360 -> 365`.
- A second weak point, read not run: the process remarks check (WAY-294) compares items of the
  reports and the remarks word for word. Both are rewritten with the same map in one pass, so they
  still agree; reading `task-cycle/remarks_check.py` was not needed for that, it follows from the
  map being the same.

## How the rule holds for the target-branch merges of both routes

Step 12 is the orchestrator's step on both routes; no slice or plan member merges the target branch
(`plan_member.md` has no merge of it), and the one author does not either. The renumbering sits in
that one step, before its merge, so the one-author route and the planned route take it the same
way. The two merges of a correction (`correction.md`, first the paragraph "In the-way itself, before
anything else" for a session in the request's worktree, then "Take a link to the request") name the
same section. A grep of `task-cycle`, `elements` and `agent-instructions` for "merge the remote" /
"reconciliation" / "target branch" found no other place that merges the target branch into the task
branch.

## Text of the skill changed, by file and heading

- `task-cycle/skill/SKILL.md`, "Request and handoff", step 12: the opening is now "fetch, and where
  the log of the remote target branch holds a number that a new decision of the task branch bears,
  renumber ... first, as "The renumbering of the task's decisions" below gives (WAY-403). Then
  merge ...", and the merge reviewer reviews "the merge, and the renumbering commit with it".
- `task-cycle/skill/SKILL.md`, new section "The renumbering of the task's decisions" (between step
  14 and "The process remarks check"): what a new decision is, the one sentence of reason, the
  comparison after a fetch, the five items — the map, the one pass over the files and the original
  of the record, the check, the commit alone before the merge, the conversion in the record's
  *Events* row.
- `task-cycle/skill/correction.md`: first paragraph — "renumber the task's decisions where the target
  branch has taken their numbers, as step 12 ... gives ... (WAY-403), merge the remote target branch
  into it ... have it reviewed, the renumbering commit with it"; paragraph "Take a link to the
  request" — "First, where the target branch has taken the numbers of the task's new decisions,
  renumber them as step 12 ... gives ... (WAY-403). Then merge ..." and "the renumbering commit
  among them" in the reviewer's range.
- `task-cycle/record_template.md`, "Events": one sentence — the row of the reconciliation gives each
  old number and the new one it now bears.

## Foundation entries

### WAY-403 — How does a task's branch give new numbers to its decisions that the target branch has taken?

Mark: `row 1` for its first paragraph (renumber before the merge, commit of its own, one pass over
the branch's files and the original of the record, in step 12 and in the correction's merges) and
`row 2` for its second paragraph (the conversion stands only in the row of the events that records
the reconciliation). Because the entry carries a pair of examples that neither row gives, the
entry is marked **`the cycle's`** as a whole (`foundation_step.md`); the pair is kept for the
description to quote under the entry, word for word:

- complies: the new decisions of a task branch bear the numbers 500 to 502, the target branch took
  500 and 501 for its own, and the task branch gives its three the numbers 502 to 504 in a commit of
  its own before the merge, in the log, the tests, the comments, the skills and the original of the
  record, the spec, the plan, the handoffs, the reports and the process remarks among them; a remark
  of the human quoted in the record keeps the number it was written with; the row of the
  reconciliation reads 500 → 502, 501 → 503 and 502 → 504; a correction after review that meets
  decisions taken by another merged request renumbers the same way before its merge;
- violates: the task branch merges first and renumbers afterwards, or in the merge commit; the
  decisions of the target branch are renumbered; the numbers are replaced one decision at a time, so
  that 502 becomes 504 after 500 became 502; the log is renumbered and the record keeps the old
  numbers under a note of the conversion at its head; the human's quoted remark is rewritten; the
  row of the reconciliation gives no conversion; a correction merges the target branch with no
  renumbering where the numbers clash.

Meaning, English: when the target branch took the numbers that a task's new decisions bear, the task
branch gives way — before the merge, in a commit of its own, it renumbers all its new decisions onto
the numbers after the target branch's highest, rewrites every reference to them in its files and in
the original of the cycle's record in one pass, leaves later texts and the human's quoted remarks as
they are, and says the old-to-new conversion only in the record's row of the reconciliation.

Meaning, Polish: gdy gałąź docelowa zajęła numery, które noszą nowe decyzje zadania, gałąź zadania
ustępuje — przed scaleniem, osobnym commitem, przenumerowuje wszystkie swoje nowe decyzje na numery
po najwyższym numerze gałęzi docelowej, jednym przebiegiem przepisuje każde odwołanie do nich w
swoich plikach i w oryginale zapisu cyklu, zostawia późniejsze teksty i cytowane uwagi Mariusza, a
przeliczenie starych numerów na nowe podaje tylko we wpisie zdarzeń, który odnotowuje uzgodnienie z
gałęzią docelową.

Pair of examples: the examples use bare numbers (500 to 504), not `WAY-5xx`: the check
(`foundation_check.py`) reports `WAY-500` as naming no decision of the log, so a number with the
prefix cannot stand as an invented example. No test holds the sentences (the change is text only),
so the pair is what holds the entry for WAY-12.

*Relations*: `derives from WAY-19 · derives from WAY-02` — both live. No withdrawn number is linked
(WAY-306, WAY-357, WAY-328 are not named anywhere in the text I wrote). *Scope*: `decisions,
task-cycle`. *Based on* and *Origin*: `none`.

## Choices (with the way rejected and its cost if wrong)

1. **One entry with a second paragraph, not two entries.** Row 2 (where the conversion stands) is a
   part of the question row 1 settles: it has no meaning without the renumbering. WAY-19 makes a
   part that "can change on its own" a question of its own; the location of the conversion could
   change on its own in principle, so the call is close. Rejected: two entries (WAY-403 and
   WAY-404). Cost if wrong: one more entry to split out later, with its references.
2. **The entry sits in the section "The course of a task cycle", at its end.** Rejected: "The
   request and the human" (the conversion is in the record's row, not in the request) and "Review of
   a change" (the review is a part of the rule, not its subject). Cost if wrong: moving an entry
   between sections breaks no reference (WAY-18).
3. **The renumbering rules stand in a new section of `SKILL.md`, which step 12 and `correction.md`
   point to, not inline in step 12.** The step is already about 60 lines; a section keeps the
   one-pass details apart, and the two paragraphs of `correction.md` need a single place to name.
   Rejected: all inline in the step-12 paragraph, the task's wording "akapit kroku 12". Cost if
   wrong: a reader of step 12 alone has to follow one pointer.
4. **The renumbering commit is in the range of the merge's review** (step 12 and `correction.md`),
   with the map named in the dispatch, so that the reviewer compares the pass with the map. Not in
   the task; I added it since the pass changes reviewed code and the merge review is where a
   mistaken number would be caught. Rejected: leaving the pass outside the review's range. Cost if
   wrong: one clause to remove from two places.
5. **A row of an earlier reconciliation's conversion is rewritten with the rest** (a second
   renumbering in a correction), so that it reads from the first numbers to the present ones. Not in
   the task; it follows from "every text of the record before the entering of the event". Rejected:
   leaving earlier rows alone, which would leave `old1 -> new1` pointing at numbers that no longer
   exist. Cost if wrong: a reader meets a conversion chain of two rows.
6. **The *Rejected* of WAY-403 holds only the ways the task's *Questions to settle* keep**, as the
   decisions' template gives it (WAY-134). For "renumbering the decisions of the target branch" and
   "a temporary marker in place of a number until the merge" the task keeps no reason beside the
   way, so none is written; the reasons for the first stand in *Rationale*. Rejected: writing
   reasons I derived. Cost if wrong: two bare items.
7. **Dropped from *Rejected*** nothing; the way "no entry, the rule as a sentence of the skill alone"
   (question 4's *Not chosen*) is kept as the last item, since the source keeps it with its reason.

## Reaches beyond the dispatch (section 1)

- `elements/decisions/skill/read.md` and `decide_entry.md` (named by `SKILL.md` of the element),
  read whole, as that skill gives.
- `elements/common/way_of_working.md`, read whole (the element's skill says to follow its steps).
- `task-cycle/record_template.md` lines 40–120 (the *Events* paragraph), to see the row's wording.
- `foundations/decisions.md`: the section headings, WAY-229's end and the withdrawn table (to place
  the entry and to find the highest withdrawn number, WAY-371), and WAY-33's rule through
  `way_of_working.md` step 2. No decision beyond the handoff's list was opened.
- A grep for "renumber / next free / same numbers" in `foundations`, `elements`, `task-cycle`,
  `project-level` and `agent-instructions` (the search of the whole foundation, WAY-33): no other
  entry or template answers the question; `elements/decisions/template.md` repeats WAY-19's
  "No entry and no withdrawn number holds the next free number", which the new entry follows.

## Working copies

All stood in `.runs/author/` of the worktree: helper scripts (`ent.py`, `fixdash.py`, `fixnum.py`,
`refl.py`, `fix2.py` to `fix5.py`, `passcheck.py`), the test outputs `t_*.txt`, `fc.txt` and
`index.md`. No worktree, clone or screenshot was made. The directory `.runs/author/` was removed
whole before the return (`ls .runs` shows `orchestrator` and `task-cycles` only). Kept in
`reports/` beside this report: `author-passcheck.py` (the own-work check) and
`author-foundation-check.txt` (the last run of the foundation check). Nothing remains.

## Unread material

- WAY-135 (`foundations/decisions.md`): read only its heading and first paragraph; my listing was cut
  at 400 lines inside it. Its rest (*Verification*, *Rationale*, *Rejected*) is unread.
- `.runs/orchestrator/index.md` (the orchestrator's index): not read; I wrote and read my own
  (`.runs/author/index.md`) for WAY-403 and the part `task-cycle`.
- `elements/decisions/examples.md` names WAY-03 only; WAY-03 itself not opened.
- Everything else the handoff names was read whole: the handoff, `task-cycle/change/SKILL.md`,
  `foundation_step.md`, the frozen task, WAY-19, WAY-02, WAY-18, WAY-05, WAY-12, WAY-22, WAY-36,
  WAY-293, WAY-294, WAY-11, WAY-150, WAY-161, WAY-162, `elements/decisions/` template, skill,
  `read.md`, `decide_entry.md`, `elements/common/rules.md` and `way_of_working.md`, step 12 and the
  changed files of `task-cycle/`.

## Searches not found or unclear

- The task's *Rejected* items "renumbering the decisions of the target branch" and "a temporary
  marker in place of a number" keep no reason beside the way in the task document, so the entry's
  *Rejected* lists them with none (choice 6).
- `task-cycle/skill/SKILL.md` step 12 does not say in what form the orchestrator sees "a new
  decision of the task branch" — the section I wrote gives it ("the log of the task branch holds it
  and its log at the merge base does not"); the task's wording did not.
- The handoff says WAY-306, WAY-357 and WAY-328 are withdrawn; confirmed in the withdrawn table
  (lines of `foundations/decisions.md` ending the file); none is linked.

## Late result

`python -B gate/run_tests.py installation` — exit 0, 62 tests, OK.
