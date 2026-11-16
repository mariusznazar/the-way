# Author report — relations-todo-for-unwritten-decision

**Status:** done with concerns (the concerns: one stale list in WAY-287, the decision to put the
WAY-126 sentence in a second paragraph, ruff not available; all below).

## Commits and files

One commit on `task/relations-todo-for-unwritten-decision`: `452f123`. Added/removed lines:

| File | + / - |
|---|---|
| `elements/common/foundation_check.py` | 24 / 16 (net +8: 984 -> 992 lines, under the 1000-line file threshold of WAY-385) |
| `elements/common/test_foundation_check.py` | 52 / 8 |
| `elements/common/rules.md` | 6 / 4 |
| `elements/decisions/template.md` | 9 / 3 |
| `foundations/decisions.md` (WAY-71, WAY-126 only) | 38 / 16 |
| `task-cycle/skill/request_template.md` | 3 / 2 |

(From `git diff --numstat HEAD~1 HEAD`: 132 insertions, 49 deletions in total.)

## What was done, by To do item

1. WAY-71: binding sentence lists a decision's *Relations* in the form
   `TODO — <the decision, and where it is expected>`, for any decision the entry derives from that
   the foundation does not hold yet, between *Derives from* and *Based on*; the "last item after the
   known items" clause of the sentence covers it. *Origin* stays without `TODO`. *Verification*
   (complies gains the `derives from WAY-x · TODO — …` case; violates names a bare `TODO` in
   *Relations* and the comma join), *Rationale* (the *Relations* sentence rewritten: only *Origin* is
   a field left unfilled when it has a gap) and *Rejected* (the three ways of the task's questions 1
   and 2, each with its cost; plus "or whose higher decision is not written yet" in the existing
   `TODO` only in *Rests on* clause) follow.
2. `elements/common/rules.md`: same change in the bullet "The main branch holds `TODO` only where".
3. `elements/decisions/template.md`: the *Relations* line of the block gains
   `| TODO — <the decision, and where it is expected>`; the sentence "*Relations* and *Origin* never
   read `TODO`" is replaced by the new one (Origin never; *Relations* only the descriptive form, last
   item after the known relations, description runs to the end of the value; the script reports a
   bare `TODO` in *Relations* and any `TODO` in *Origin*). I added one sentence to the first bullet
   of "Relations and precedence": the `TODO` of *Relations* is no third type (the closed list of
   two types would otherwise contradict it).
4. `elements/common/foundation_check.py`: `MISSING` gains `Relations`; the `Relations` entry is out of
   `DECISION_WORDS`; `known_part` is called for `Relations` in `check_foundation_references`, which
   then checks the decision numbers of the known part only, line by line; a new set `relation_lines`
   makes `check_decision_numbers` skip the lines of *Relations* (as it does for *Based on*), so a
   number inside the description names no entry. Docstring paragraph and the "does not take" list
   follow. The bare `TODO` is reported once (by `known_part`), never twice.
   `test_foundation_check.py`: the three cases the task asks for, plus the neighbours below.
5. WAY-126: a second paragraph of one binding sentence ("A change that writes a projected entry into
   the foundation replaces with its identifier each descriptive `TODO` that points at it, in a
   decision's *Relations* and in an invariant's *Derives from*."), and one example in each of
   *Verification*'s complies and violates for it.
6. `task-cycle/skill/request_template.md` item 16: lists `TODO — <the decision, and where it is
   expected>` in a decision's *Relations* beside the one in an invariant's *Derives from*.

## Checks (command, exit code)

- `python -B gate/run_tests.py elements/common` — 0, 252 tests OK (run before the final docstring
  reflow in `foundation_check.py` too; the final tree was run again: 0, 252 OK, 114.8 s).
- `python -B gate/run_tests.py task-cycle` — 0, 534 tests OK (2 skipped, as before).
- `python -B gate/run_tests.py product-guidelines` — 0, 14 OK (reads the skill texts).
- `python -B gate/run_tests.py agent-instructions` — 0, 37 OK (2 expected failures, as before).
- `python -B elements/common/foundation_check.py` — 0, `0 errors`, on the final tree.
- The full gate (`python -B gate/run_tests.py` with no directory) was not run (handoff, WAY-160).
- `ruff` is not installed in this environment (`ruff: command not found`, `No module named ruff`):
  the linter's blocking rules were not run on the two changed Python files; the gate's run will.

### New tests: the break each catches, and that each was seen failing

All in `elements/common/test_foundation_check.py`. Each is a files-and-process test of the real script
on a temporary git repository, like its neighbours; the expected messages and line numbers are
written out. Failing run before the code: `python -B -m unittest elements/common/test_foundation_check.py -k relations -k origin`
-> `FAILED (failures=14)` (7 tests run; the failures named below); passing run after the code:
`python -B gate/run_tests.py elements/common` -> exit 0.

- `test_relations_a_missing_decision_described_passes_whole` (4 values) — catches: the script
  rejects a described `TODO` in *Relations*, or reads the decision number in its description as a
  reference (a bug). Failed before (3 of 4 subtests; the fourth, a backticked form, too).
- `test_relations_a_missing_decision_described_over_two_lines_passes` — catches: the lines of the
  value after the first are not skipped by the check of decision numbers (a bug). Failed before.
- `test_relations_a_known_decision_then_a_missing_one_described_passes` (3 values) — catches: a
  known relation followed by the description is rejected or read wrong. One value (with `ABC-77`
  in the description) failed before; the two others passed before as well (they name no number in
  the description) and stay as guards for the form.
- `test_relations_a_bare_todo_names_no_decision` (7 values, bare, backticked, dash alone, after a
  known relation) — catches: a bare `TODO` accepted, or reported without the hint of the form, or
  at the wrong line (a bug). Failed before (the old message was "does not take").
- `test_relations_a_decision_before_a_todo_is_still_checked` — catches: the known relation before
  the description is no longer checked against the log (a bug). It passed on the old code, so I broke
  the new code for a moment (the loop that refers the decisions of the known part replaced by
  `pass`), saw it fail (`-k relations`: `FAILED (failures=1)`, this test), and restored the code
  before the commit.
- `test_relations_a_described_todo_after_a_comma_is_no_joined_list` — catches: a comma accepted
  between a relation and the `TODO` (a bug; the items are joined by ` · `). Failed before.
- `test_origin_takes_no_todo` — replaces `test_relations_and_origin_take_no_todo`: the *Origin* half
  is unchanged (same two values, same message). The *Relations* half of the old test asserted the
  rule this task deliberately reverses (To do 4), so it went; its cause is on the side of the
  requirement (task To do 1 and 4, "gołe `TODO` w *Relations* zgłasza jako błąd z podpowiedzią
  postaci"), and the new bare-`TODO` test replaces it with the new message.

Mutation in the head: skipping `relation_lines` in the number check — caught by the two-line and
described tests; a `MISSING` entry with another hint — caught by the bare test (message text is
asserted because the task asks for the hint of the form); `Relations` left in `DECISION_WORDS` —
caught by every passing test; `Origin` accepting `TODO` — caught by `test_origin_takes_no_todo`. No
mutation left unprotected that I found.

## Own-work check (WAY-164)

Requirement most likely not met: the check accepts the form in the real log, not only in the test's
small product, and still checks what stands before it. Check: in the worktree, copied
`foundations/decisions.md` aside, set WAY-71's *Relations* to four values in turn, ran
`python -B elements/common/foundation_check.py` on the real tree, restored the file after each. Showed:
`derives from WAY-01 · TODO — WAY-9999, expected in the save task` -> `0 errors`; `TODO` ->
`foundations/decisions.md:617: *Relations* reads `TODO` and names no decision: write `TODO — <the
decision, and where it is expected>``, 1 error; `derives from WAY-01, TODO — x` -> `*Relations*
joins its items by ` · `...`, 1 error; `derives from WAY-9999 · TODO — x` -> ``WAY-9999` names no
decision of the log`, 1 error. The file was restored; final check `0 errors`.

## Choices (with the way rejected and the cost if wrong)

- **Second paragraph for the WAY-126 sentence.** The first paragraph already holds three sentences
  (template: 1–3 per paragraph); a fourth would break that, folding it into the first sentence would
  make a very long one. Rejected: both. Cost if wrong: the reviewer or the human prefers it merged;
  a one-line move.
- **Pair of examples added to WAY-126** (one complies, one violates), although the task says "reszta
  bez zmiany": the new sentence is held by no test and the template asks a pair for such a part.
  Cost if wrong: two lines to remove. Because of this pair (and WAY-71's changed pair), the entries
  are marked below as `the cycle's`; the request must quote the added pairs word for word (see the
  quotes below).
- **Sentence in the "Relations and precedence" bullet of the decision template** (the `TODO` of
  *Relations* is no third type) — not in the task's list, written because the search of the
  foundation (WAY-33) finds the closed list of two types contradicting a new word in the field.
- **The check of numbers in *Relations* reads each line of the known part**, rather than
  `unquoted(...)` as for *Based on*: *Relations* quotes no source, and `unquoted` would skip an item
  that quotes a passage, which would loosen today's check of *Relations*. Rejected: `unquoted`.
- **No move before the change (WAY-365):** `foundation_check.py` stood at 984 lines (file threshold
  1000) and no function I changed is near 80 lines; no move was due. File ends at 992 lines.

## Foundation step: the entries, with their meaning

Both are marked `the cycle's` (no row of *Settlements to record* carries them — the section reads
`none` — and each holds a pair of examples I wrote or changed). The meaning was settled by the human's
answers in *Questions to settle* (1 a, 2 a, 3 a, 2026-11-14), which the task document carries.

- **WAY-71** (changed). English: A decision's *Relations* may read `TODO — <the decision, and where it
  is expected>` — as the last item after the known relations — for any decision the entry derives
  from that the foundation does not hold yet; a bare `TODO` there is an error and *Origin* never reads
  `TODO`. Polish: *Relations* decyzji może mieć opisowe `TODO — <decyzja i gdzie się jej spodziewać>`
  jako ostatnią pozycję po znanych powiązaniach, dla dowolnej decyzji, z której wpis się wywodzi,
  a której fundament jeszcze nie ma; gołe `TODO` to błąd, a *Origin* nigdy nie ma `TODO`.
- **WAY-126** (changed). English: A change that writes a projected entry into the foundation replaces
  with its identifier each descriptive `TODO` that points at it, in a decision's *Relations* and in an
  invariant's *Derives from*. Polish: zmiana, która zapisuje wpis zaprojektowany do fundamentu,
  zastępuje jego identyfikatorem każde opisowe `TODO`, które go wskazuje — w *Relations* decyzji
  i w *Derives from* niezmiennika.

Pairs added, word for word, for the request to quote under the entries:

- WAY-71 *Verification* complies, added: "a decision that derives from one decision the log holds and
  from one it does not hold yet reads `Relations: derives from WAY-x · TODO — <the decision, and
  where it is expected>`"; violates, changed: "an entry reads a bare `TODO` in *Rests on*, *Derives
  from*, *Based on* or *Relations*; a decision reads `TODO` in *Origin*; a decision joins `TODO —
  <the decision, and where it is expected>` to the relations before it with a comma instead of ` · `."
- WAY-126 *Verification* complies, added: "a task whose code makes a projected decision true writes it
  into the log and replaces with its number the `TODO` that names it in the *Relations* of a decision
  and in the *Derives from* of an invariant"; violates, added: "a task writes a projected decision into
  the log and leaves a decision's *Relations* reading `TODO — <that decision, and where it is
  expected>`".

The search of the whole foundation (WAY-33) for the entries the change touches: the entries and files
it found and what was done are in the next section.

## Concerns, problems as observed

1. **WAY-287 lists the descriptive `TODO` fields and was left as the task says ("Bez zmiany").** Its
   binding sentence (`foundations/decisions.md`, "each descriptive `TODO` in an invariant's *Rests on*
   or *Derives from* or in a decision's *Based on* that stands on the main branch after the change
   (WAY-71)"), its *Verification* violates line ("the section reads `none` while an invariant's *Rests
   on* or *Derives from* or a decision's *Based on* holds a descriptive `TODO`") and its *Rationale*
   ("...in an invariant's *Rests on* or *Derives from* or in a decision's *Based on* once the change
   is merged") now name three fields, while item 16 of the request template names four. WAY-71
   carries the new kind into the request ("a change that leaves one there puts it before the human"),
   and WAY-287 says another decision may add a kind of item, so I read this as consistent; but the
   list in WAY-287 is a stale enumeration. Recommendation: a one-clause edit ("or *Relations*") in the
   three places in a later change or in a correction, if the human wants the enumeration kept whole.
   Not done: the task fixes WAY-287 as unchanged.
2. `ruff` is absent here (see Checks); not run.
3. Two statements of the task do not hold against the sources (both already in the handoff): the
   task says the-way has no `guidelines/` directory (it has one; read as the handoff says), and
   it names WAY-37 and WAY-32 as entries that stay (both are withdrawn; I named no withdrawn
   identifier in my sentences, and left `elements/common/way_of_working.md` and the template
   sentences that stand in their place unchanged except as listed).

## Searches (WAY-33 and the places that quote the changed sentences)

- Searched the repository for `TODO` with `Relations`, `WAY-71`, `never read`, the form
  `TODO — <the decision, and where it is expected>`, and the field names `Rests on* or`. Found and
  changed: the five places in the task's list; the docstring of `foundation_check.py`;
  `foundations/decisions.md` WAY-71 and WAY-126. Found and not changed, on purpose:
  `elements/invariants/template.md` and `elements/invariants/skill/SKILL.md` (about an invariant's
  *Derives from*, unchanged), `elements/environment-facts/template.md` (about a fact),
  `elements/common/way_of_working.md` lines 167–168 (generic: "what stays open ... is written as
  `rules.md` gives it"), `project-level/definition_template.md` (a project definition's `TODO`),
  WAY-287 (concern 1), and `elements/common/migrate_foundation.py` (reads the earlier form only).
- A project definition / `skill` copies: `.claude/skills` and the agent-type copies read no changed
  description; no `skill_entry_points.py` or `agent_type_copies.py` run was needed (no skill
  description and no agent-type definition changed).

## Reach beyond the dispatch

- Read in full for the foundation search, beyond the named entries: nothing. Selectively read:
  WAY-385 (the size rule, for the thresholds) and `foundations/part_map.md` entries `decisions`,
  `elements-common`, `part-map` (to see the parts' files; no map change needed — no file added or
  removed), `elements/decisions/skill/SKILL.md` (as the foundation step names it) and
  `elements/common/way_of_working.md` lines 160–170. Also read the three `guidelines/` files whole.
- I did not read whole the other invariants of the parts `elements-common` and `decisions`: a search
  of `foundations/invariants.md` for `TODO`, `Relations`, `foundation_check`, `rules.md` and
  `template.md` found only unrelated lines (390, 420), so none was found that this change touches.

## Unread material

- `foundations/part_map.md`: read the entries `decisions`, `part-map`, `elements-common` (and the first
  lines of `project-level`); not the rest of the file.
- `foundations/invariants.md`: not read whole; searched, as above; the two lines found were read.
- `.runs/orchestrator/index.md`: read its head only (heading and counts); located entries through
  `grep` of `foundations/decisions.md`, then read each named entry whole (WAY-07, WAY-17, WAY-33,
  WAY-114, WAY-287 — WAY-287 read to its *Verification*, not through its *Rationale* and *Rejected*;
  its lines 7040–7064 were read for the concern).
- `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`:
  template and rules read whole; `way_of_working.md` read at lines 160–170 only (not whole), though
  `foundation_step.md` names it among the files of the element's skill.
- `elements/decisions/skill/read.md`, `decide_entry.md`, `projected.md`, `elements/decisions/examples.md`:
  not opened (a search of the whole `elements/decisions/` for `TODO` and `Relations` found nothing
  in them).

## Searches not found or unclear

- `elements/common/way_of_working.md` was named by the handoff but, as the foundation step reads it,
  the step table in it was not read whole; whether a step there needs a sentence for the *Relations*
  `TODO` is unclear to me. I found only the generic lines 167–168 (reads "what stays open ... is
  written as `rules.md` gives it"), which already cover it.
- No test in the repository holds a sentence of WAY-71 or WAY-126 by a line `decision:`; both are held
  by their pairs of examples, as before.

## Working copies

None left. The directory `.runs/author/` held my edit scripts, a backup of `foundation_check.py` and
of `decisions.md`, and the three test outputs; it stood at
`.runs/author/` and was removed
(`rm -rf`) before this report was written. No git worktree or clone was made.
