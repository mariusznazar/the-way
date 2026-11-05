# Report 02 — the one author of the whole change

**Status:** `done`

## Commits (branch `task/cycle-remarks-batch-2`, base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a`)

- `b2a52f695637a1665f815a837177f656c70e99f3` — foundation entries: new WAY-293, WAY-05 and WAY-148 edited in place, the decision template.
- `3023f604d5517ca157b3cb6bb9135a360d7e29f3` — the task-cycle instructions (To do 1, 3 and 4).

The worktree is clean after the second commit.

## Files changed

| File | Added / removed lines |
|---|---|
| `foundations/decisions.md` | 56 / 7 (WAY-293 new at the end of the entries; WAY-05 binding sentence, Verification and Rationale; WAY-148 binding sentence) |
| `elements/decisions/template.md` | 4 / 2 |
| `task-cycle/skill/return_step.md` | 4 / 2 |
| `task-cycle/record_template.md` | 3 / 2 |
| `task-cycle/skill/SKILL.md` | 14 / 8 |
| `task-cycle/review/SKILL.md` | 2 / 1 |
| `task-cycle/spec/SKILL.md` | 4 / 2 |
| `task-cycle/spec/review.md` | 1 / 1 |

(Counts are from `git diff --numstat 61c72fb HEAD`.)

## What was done, by To do item

1. (AIR-585) Sentence added to `task-cycle/skill/return_step.md` after "(WAY-36)." and the "unless ... excludes the entry" clause to `task-cycle/skill/record_template.md` (record_template.md is `task-cycle/record_template.md`), both in the task's wording. New decision WAY-293 (row 1).
2. (AIR-586) WAY-05: fragment in the binding sentence, the same fragment in `elements/decisions/template.md`, the new last sentence of *Rationale*, the example pair in *Verification*.
3. (AIR-592) `task-cycle/skill/SKILL.md`: new sentence after "(WAY-159)." and the mechanical check of a slice executor's report in the task's wording.
4. (AIR-587) WAY-148 binding sentence; `task-cycle/review/SKILL.md`, `task-cycle/spec/SKILL.md`, the parenthetical in `task-cycle/skill/SKILL.md`, `task-cycle/spec/review.md`, each in the task's wording.

Quoted line numbers: all matched the files at the base (return_step.md:13, record_template.md:99, review/SKILL.md:140-141, spec/SKILL.md:51, skill/SKILL.md:178, :187-189 and :283-289, spec/review.md:26, decisions.md WAY-05 :128-130 and WAY-148 :3888-3890, template.md:53-55). No correction.

## Checks (command, exit code)

All run from the worktree root.

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (after the entries, and again after the commits; output `0 errors`) | 0 |
| `python -B gate/run_tests.py task-cycle` (92 tests, OK) | 0 |
| `python -B gate/run_tests.py elements/common` (109 tests, OK) | 0 |
| `python -B gate/run_tests.py relation-model` (12 tests, OK) | 0 |
| `python -B gate/run_tests.py agent-instructions` (18 tests, OK) | 0 |
| `python -B gate/run_tests.py instruction-files` (104 tests, OK, 5 skipped by the tests themselves) | 0 |
| `python -B gate/run_tests.py elements/decisions` | 1 — "no test found in elements/decisions": the directory holds no test; not a failure of the change |
| `python -B gate/run_tests.py foundations` | 1 — "no test found in foundations": same, no tests there |

Not run: the product's gate without an argument (the orchestrator's, per the handoff). Skill entry points were not regenerated: no description changed.

## Own-work check (WAY-164)

- **Requirement most likely not met:** "copy it exactly where it gives a sentence" — thirteen quoted sentences and fragments across eight files, several wrapped over lines and containing em dashes, backticks and bold markers, with a template and a decision that must carry the same WAY-05 fragment.
- **Check:** scratch script `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\693489a7-cb0e-4eb7-9d76-91dc04059916\scratchpad\check_wording.py`, which looks for each sentence of the task in its target file with whitespace normalised (14 cases). Also a grep of WAY-293's binding sentences for `should`, `will`, `must`, `shall`, `may`.
- **Failing run:** `python -B check_wording.py HEAD` (reads the base commit's files with `git show HEAD:<path>`, before the commits) — 14 of 14 `MISS`, exit 1.
- **Passing run:** `python -B check_wording.py` on the tree — 0 `MISS`, exit 0. The word grep found nothing (exit 1 of grep = no match, which is the wanted result).
- **What it showed:** every sentence of the task stands in its place word for word. It does not show that the meaning is right; that is for the review.

## Foundation entries

- **WAY-293** — `row 1` — new decision, "What prevails where a task or its spec excludes the entry for a choice?", scope `decisions, task-cycle`, *Relations* `narrows WAY-22 · narrows WAY-18`, written at the end of the log (next free number; the largest held was WAY-292, no withdrawn number above it).
  - English: Where a task or its spec explicitly excludes an entry in the foundation for a choice, that exclusion prevails over the rule that a choice binding after the merge is written into the foundation and the choice stays a row of the cycle record's questions table, narrowing WAY-22 and WAY-18 in that area; a candidate left out of a task's settlements to record is no exclusion.
  - Polish: Gdy zadanie albo jego spec wprost wykluczają wpis w fundamencie dla wyboru, wykluczenie wygrywa z regułą, że wybór wiążący po scaleniu trafia do fundamentu, a wybór zostaje wierszem tabeli pytań w zapisie cyklu — to zawęża WAY-22 i WAY-18 w tym obszarze; kandydat wycięty z rozliczeń do zapisania wykluczeniem nie jest.
- **WAY-05** — `row 2` — edited in place (binding sentence, *Verification*, *Rationale*).
  - English: A decision's rationale and rejected options may give a measurement the choice rests on, with what was measured and under which conditions and never as a general bound; the ban on counts protects decisions from history and chronicle that the reader does not need.
  - Polish: Uzasadnienie i odrzucone warianty decyzji mogą podać pomiar, na którym opiera się wybór, z tym, co zmierzono i w jakich warunkach, nigdy jako ogólną granicę; zakaz liczb chroni decyzje przed historią i kroniką, których czytelnik nie potrzebuje.
- **WAY-148** — `row 3` — edited in place (binding sentence only).
  - English: A stage returns a one-line check result only where it runs a test or another check of the product, so the designer and the reviewer of a spec return no check result.
  - Polish: Etap zwraca jednolinijkowy wynik sprawdzeń tylko tam, gdzie uruchamia test albo inne sprawdzenie produktu, więc projektant i recenzent specu nie zwracają wyniku sprawdzeń.

The decisions' *Rejected* of WAY-293 holds only the ways the task document keeps for its row: the exception for every choice written in a skill or template (cost as the question gives it), no change (which withdraws the rule), and only the task excluding, not its spec. No question to the human arose.

## Reaches beyond the dispatch

- Read `task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md`, its `read.md` and `decide_entry.md`, `elements/common/way_of_working.md`, `elements/decisions/template.md`, `elements/decisions/examples.md` and `elements/common/rules.md` — named by the handoff through the skill's steps; not a reach.
- Read selectively for the search of the foundation (WAY-33): WAY-114 and WAY-134 whole (to place the exclusion against them and to write *Rejected* of WAY-293 as WAY-134 gives), WAY-268 and WAY-29 as examples of `narrows` and of two pairs in *Verification*, the tail of WAY-148 and the entries WAY-290 to WAY-292 (to take the form of recent task-cycle decisions and the next free number). Why: WAY-114 and WAY-134 are the rules the new decision sits beside; the rest is form and numbering. The handoff did not name them.
- Grep over `task-cycle/`, `elements/`, `project-level/`, `agent-instructions/`, `foundations/` for the phrases "check result", "WAY-148", "names no file, script or count", "binds after the merge", "exclud": found no other place to change (see the section below for one place that quotes WAY-148).
- Read `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md` and `git.md` (instructions outside the repository, before writing the check script and committing).

## Choices

- **WAY-05 *Verification*: one pair, extended, not two pairs.** The task says "nowa para" with `complies:` and `violates:`. I appended the new example to the existing `complies:` and `violates:` lines, separated by a semicolon, since the template's "pair of examples" is one `complies` and one `violates`, and two lines of the same label would be a form the template does not give. Rejected: a second labelled pair, as WAY-29 has; its cost if wrong is a change of the lines' layout, no change of meaning. The sentences themselves stand as the task gives them.
- **WAY-293 scope `decisions, task-cycle`**, not `task-cycle` alone: the decision narrows two decisions of `decisions`, and a link is written only at its own end (WAY-18), so someone reading by the part `decisions` finds it only through *Scope*. Rejected: `task-cycle` alone — a reader of WAY-22 and WAY-18 would meet no mention. Cost if wrong: one more entry in lists of the part `decisions`.
- **WAY-293 has no `derives from WAY-36`.** The task and the row say only `narrows WAY-22 and WAY-18`; the exclusion sets aside the return step's rule, not WAY-36 itself, which says what may enter the log and not what must. Cost if wrong: one `Relations` item to add.
- **WAY-293 binding sentences:** three; the third ("A candidate left out of a task's *Settlements to record* is no exclusion.") carries the task's last sentence of To do 1, which would otherwise stand only in prose. Rejected: leaving it to *Verification*, where it is also an example of a violation.
- **WAY-148 binding sentence:** the inserted clause stands as the task gives it; I rewrapped the paragraph lines. *Verification* and *Rationale* of WAY-148 were not changed (the task asks only for the binding sentence).
- **No *Verification* invariant for WAY-293:** the invariants file holds none that derives from it and none is called for by the task; the entry gives a `complies`/`violates` pair.

## Problems as observed

none.

## Searches not found or unclear

- `task-cycle/test_request_check.py:60-62` quotes the first sentence of WAY-148 in a task-document fixture ("... a one-line check result naming what failed or did not run, and the report's path."). After the change the decision reads "..., where the stage runs a test or another check of the product, and the report's path". The fixture is a made-up task, no test compares it with the log, and `python -B gate/run_tests.py task-cycle` passes (exit 0); I left it as is. Unclear whether the reviewer wants it brought in line.
- `task-cycle/plan/SKILL.md:202` (the planner returns "the status, the plan's path, a one-line check ...") was not changed: the planner is a stage that runs checks of its plan (the size check), so WAY-148's clause does not reach it; I did not verify what the planner's checks are.
- `task-cycle/spec/design.md:60` and `:70` ("the four checks") say the designer has checks; the new sentence in `task-cycle/spec/SKILL.md` says neither runs "a test or another check of the product". The four checks read the spec, not the product, so they do not contradict it (the question 4 control of the task settles the same); I read those lines only through the task's quotation and did not open `design.md` whole.
- A section of the request or of `request_template.md` that names "a missing own-work check (WAY-164)" (task, Context) was not opened; the change to the repair rule does not need it.
