Status: done with concerns

# Author report — strongest-model probe and slice base measure

**Status:** `done with concerns` (the concerns are listed below; none blocks).
**Commit:** `60561fba` on `task/strongest-model-probe-and-slice-base-measure` (base `b502011f`).

## Files changed (added / removed lines)

| File | + / - |
|---|---|
| `foundations/decisions.md` (WAY-229, WAY-136) | 132 changed lines (net, see `git diff --stat`) |
| `task-cycle/skill/SKILL.md` | 65 changed lines |
| `task-cycle/record_template.md` | 18 changed lines |
| `task-cycle/change/slice.md` | 20 changed lines |
| `task-cycle/plan/SKILL.md` | 13 changed lines |
| `task-cycle/skill/planning.md` | 13 changed lines |
| `task-cycle/change/SKILL.md` | 2 changed lines |

Total: 189 insertions, 74 deletions. No code, no test, no change of `task-cycle/cycle_stages.py` and no skill name
or description changed, so `skill_entry_points.py --write` was not run.

## What was made, point by point

1. **Probe (WAY-229 and `task-cycle/skill/SKILL.md`).** WAY-229's first paragraph no longer sources the strongest
   class from `availableModels` or from every model the session offers: it is "the strongest model the session
   actually gives, fixed as the next paragraph says". A new second paragraph of WAY-229 holds the probe: in every
   cycle, before the first dispatch of the strongest class, a small agent on the candidate model, the model it worked
   on read from the session record, first candidate the model named at the start (checked like any other) else the
   strongest the dispatch tool offers, the next model down on a substitution, every dispatch of the class on the model
   so fixed, no question to the human (WAY-227, now also in *Relations*), the record giving the tries. *Verification*
   (complies and violates), *Rationale* and *Rejected* (the five *Not chosen* of the task's first question) are
   rewritten to match. In `SKILL.md` a new paragraph before step 9 gives the probe's procedure, the three places the
   task names (step 9 sub-step 2, the whole-change review, step 11) now say "the model the probe fixed", and the
   one-author dispatch reaches the rule through sub-step 2 as before.
2. **Record models (`record_template.md`, `SKILL.md` step 12).** *Author*, the *Slices* column and the *Events*
   actor now give the model the agent actually worked on, read from the session record, and both models where they
   differ; a new record item *Strongest class* gives the probe's tries and the model fixed. Step 12 has the
   orchestrator set the models in those rows from `stages.md` after it is written (rows written before a dispatch hold
   the model asked for, marked so).
3. **Measure on the base (`task-cycle/change/slice.md`, WAY-136).** New section "A failing test" in `slice.md`; WAY-136
   gets a new third paragraph with the measure, its two exceptions and the base result in the report; the *Checks*
   row of the variants table in `change/SKILL.md` names the new content of `slice.md`.
4. **No list (`SKILL.md` step 9, `planning.md`).** Sub-step 2 no longer copies the list and says the handoff lists no
   failing test; sub-step 3 compares the base result the report gives for each failing test and returns a report that
   names a failing test without it; sub-step 4 (the retry rule) uses the measure; `planning.md` keeps the rule of an
   owner by an edit of the plan before the next slice is dispatched, now for a test shown failing on the base that no
   *Goal* names.
5. **Announced test in the owner's *Checks* (`plan/SKILL.md`, WAY-136).** The planner writes the announced test into
   the *Checks* of the slice that repairs it; a test of those *Checks* that still fails is that slice's failed check
   though it failed on its base too. WAY-136's *Verification* and *Rationale* and *Rejected* carry points 3-5.

## Foundation entries

- **WAY-229** — marked `row 1`. Meaning, English: the strongest class available is not read from a list of allowed
  models but fixed in every cycle by a probe: a small agent is asked for the candidate model (the one named at the
  start, else the strongest the dispatch tool offers), the model it really worked on is read from the session record,
  the next model down is tried on a substitution, and every dispatch of the class then runs on the model fixed; the
  record gives the tries and the human is asked nothing. Znaczenie, po polsku: najmocniejszą dostępną klasę ustala w
  każdym cyklu próbne wywołanie, a nie lista dozwolonych modeli: mały agent dostaje prośbę o model-kandydata (podany
  przy starcie, a bez niego najmocniejszy, jaki oferuje narzędzie), z zapisu sesji odczytuje się model, na którym
  faktycznie pracował, przy zastępstwie próbuje się następnego w dół, a wszystkie zlecenia tej klasy idą na ustalony
  model; zapis podaje próby, a człowieka się nie pyta.
- **WAY-136** — marked `row 2` and `row 3`. Meaning, English: a slice's executor decides whether a failing test is its
  slice's fault by running the tests that failed for it on the slice's base: a test failing there too is no fault of the
  slice, except a test of the slice's own *Checks*; a test passing there and failing after is the slice's fault, except
  one the slice's own *Goal* announces it leaves failing with the slice that repairs it; the announced test stands in
  the *Checks* of the repairing slice, and the report gives the base result of each such test. Znaczenie, po polsku:
  wykonawca kawałka rozstrzyga, czy padający test jest błędem jego kawałka, uruchamiając na bazie kawałka testy, które
  mu padły: test padający także na bazie nie jest błędem kawałka, poza testem z jego własnych *Checks*; test, który na
  bazie przechodzi, a po zmianie pada, jest błędem kawałka, chyba że *Goal* tego kawałka zapowiada go jako czerwony i
  wskazuje kawałek naprawiający; zapowiedziany test stoi też w *Checks* kawałka naprawiającego, a raport podaje wynik na
  bazie każdego takiego testu.
- The two entries keep their *Based on*, *Origin* and *Scope*. Added link: WAY-229 *Relations* now also `derives from
  WAY-227` (a link in *Relations* does not make the entry `the cycle's`). No pair of examples was added: the pair that
  stood in each *Verification* was edited in place for the new wording (the *complies* and *violates* clauses named in
  the diff of `foundations/decisions.md`); no new part beyond the rows.
- Placement: the leaves-failing rule moved out of WAY-136's first paragraph (which then keeps its first two sentences)
  into a new third paragraph, since the first paragraph was near the word limit; the two entries stand at 509 and 459
  words of binding sentences, paragraphs of 148 / 211 / 150 and 159 / 127 / 80 / 93 words.
- Search of the foundation (WAY-33): done once for `availableModels`, `strongest class`, `leaves failing`, `fails as
  expected`, `fails as the plan says`, `known failing`, the failing-check wording, owners of tests and the
  record-of-models wording, over decisions, invariants, glossary, part map and the instruction files. The only other
  entries touched are the two above; WAY-227, WAY-160, WAY-125 stay as they are. After the edit no file holds the old
  wording (`git ls-files | xargs grep` for the old phrases finds only the new text of WAY-136's own entry).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors" (run on the tree with the change).
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 5 info".
- `python -B gate/run_tests.py task-cycle` — exit 0, 570 tests OK (2 skipped on Windows).
- `python -B gate/run_tests.py project-level` — exit 0, 302 tests OK.
- `python -B gate/run_tests.py process-audit` — exit 0 (first attempt under `timeout 280` ended with exit 124 because
  of my timeout, not a failure; rerun with no timeout exit 0).
- `python -B gate/run_tests.py elements/common` — exit 0, 316 tests OK (holds `test_the_way_foundation_passes`).
- Did not run: the full gate `python -B gate/run_tests.py` (the orchestrator's or CI's, WAY-160);
  `skill_entry_points.py --write` (no skill name or description changed; `--check` is no flag of that script).
- No test holds the present wording of these rules (confirmed by `grep` over `*.py` for the old phrases and for
  `decision:` lines naming WAY-136 or WAY-229: none), so no test changed.

## Own-work check (section 3)

Requirement likeliest not met: **the probe can be carried out as written** — that the orchestrator can read, from the
session record and with the existing script, the model a probe agent worked on, so that the rule does not rest on a
tool behaviour that does not exist. I checked it by running `python -B task-cycle/cycle_stages.py` with no argument on
the live session of this author (`CLAUDE_CODE_SESSION_ID` set): exit 0, no `--output`, the table printed on stdout and
its row "Author of the change (the-way-author)" gave `claude-sonnet-5-5` in the column *Subagent model*. The row
names its agent by its description and its type (read in `task-cycle/stage_transcripts.py`: `name = f"{description}
({kind})"`), which is why the procedure says the row "named by that description". The scratch output was removed.
The second likeliest miss, a stale restatement of the old rule, was checked by the grep named above (nothing left).

## Walkthrough

The change alters no behaviour a user sees in a running product (prose of the process, a decision and a record
template); no walk of `walkthrough.md`.

## Choices made (with the way rejected and the cost if wrong)

- WAY-136's leaves-failing rule stands in a new third paragraph; rejected: keep it as the third sentence of the first
  paragraph — the word limit of a paragraph (300) is an error for an altered decision and the clause would need
  shortening it. Cost if wrong: none to the meaning; the division into paragraphs is only form.
- The probe's procedure stands in `SKILL.md` as a paragraph before step 9 rather than inside sub-step 2, since the
  first dispatch of the class can also be the one author or a retry. Rejected: put it in sub-step 2 and refer to it
  from the others. Cost if wrong: one paragraph to move.
- Orchestrator's plan review (`planning.md`) now also checks that a test a *Goal* announces left failing stands in the
  *Checks* of the slice it names. Rejected: leave the planner's rule unchecked. Cost if wrong: one clause to delete;
  the task's *Not chosen* lists no such clause, but it adds no condition for a test to join a list.
- The record fills rows with the model asked for at dispatch (marked so) and `stages.md` completes them at step 12;
  rejected: run the script after every agent returns (a script run per agent). Cost if wrong: the rows stay with the
  asked-for model where `stages.md` is missing, which the text says.
- No environment fact was written for the behaviour of the dispatch tool on a blocked model (the task *Context* quotes
  the documentation, read 2026-11-26): the template asks for a fact entry with an archived address and a read date I
  could not obtain without a fetch of an external archive, and the *Rationale* states the substitution as an
  observation of this product's own cycles instead, as WAY-229's *Rationale* already did for its measurement.
  Rejected: write the fact with the address and passage from the task's *Context*. Cost if wrong: a later cycle writes
  that fact; WAY-229's *Based on* holds none of it.

## Concerns

- The probe's rule does not say what happens when every candidate is substituted (the offer of the tool ends below the
  session's own model). In practice the session's own model always answers as asked, so the loop ends; I added no rule
  for exhaustion to avoid widening. If the orchestrator wants one, it is a sentence in `SKILL.md`.
- WAY-229 now holds no environment fact for the tool's substitution of a blocked model (see the last choice). A reviewer
  who holds that WAY-90 requires one should treat it as a task of its own.
- The measure of point 3 cannot tell a test that fails on the base and fails again for a new reason of the slice; the
  entry's *Rationale* names this as the price (left to the reviews and the gate).

## Reaches beyond the handoff

- Read `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/environment-facts/skill/SKILL.md` and the head
  of `foundations/environment_facts.md` (to decide whether to write a fact), `task-cycle/stage_transcripts.py` (lines
  715-745, how a stage is named) and `task-cycle/cycle_stages.py` (docstring and the table builder), and the
  `task-cycle/review`/`spec_review`/`correction`/`blocked_finding`/`return_step` files for model wording by `grep`
  (none found). Why: the handoff says to select the rest of the reading by `way_of_working.md`; these served the
  decision and the probe's wording. I did not write the decision index file; I selected the entries by identifier and
  by search of `foundations/decisions.md` (see Unread material).

## Working copies

None made. Test outputs went to `.runs/author/` (ignored by git; `tc.txt`, `pl.txt`, `project-level.txt`,
`process-audit.txt`, `ec.txt`) and stay there as logs; no worktree, clone or screenshot. The scratch output of the
probe check was removed.

## Unread material

- `elements/common/decision_index.py` was not run and no index file was written: the entries the change touches
  (WAY-229, WAY-136, WAY-227, WAY-160, WAY-125) were read whole by their headings, and the search for the rest was by
  `grep` over the foundation (WAY-33), not by the part-selected index. Decisions of the part `task-cycle` other than
  those named were therefore read only where the search hit them (lines near 6277, 2956, 7833 read whole; others by
  hit).
- `guidelines/coding.md` and `guidelines/testing.md` were not read: the change is prose and writes no code or test.
- `elements/common/projected_mode.md`, `missing_element_file.md`, `reaching_another_skill.md` and the glossary/part-map
  entries were not read: no glossary term, part-map entry, invariant or projected entry was written.
- `elements/decisions/examples.md` (named by the template) was not read.

## Searches not found or unclear

- none
