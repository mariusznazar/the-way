# Correction report — cycle `cycle-remarks-batch-4`, the human's remarks R1–R3

**Status:** `done`

**Commit:** `10d443f` (range `14b7680..10d443f`): `elements/common/foundation_check.py`,
`elements/common/test_foundation_check.py`, `elements/common/rules.md`,
`elements/decisions/template.md`, `elements/invariants/template.md`, `foundations/decisions.md`,
`task-cycle/skill/request_template.md`.

Foundation entries edited, each `the cycle's` (edited in place on the human's remarks, WAY-114,
WAY-30):

- WAY-71 — EN: The main branch may hold `TODO` only where an entry stands on something the
  foundation lacks, in three fields and three forms, and a change that leaves one puts it before the
  human. PL: Gałąź główna może mieć `TODO` tylko tam, gdzie wpis opiera się na czymś, czego fundament
  jeszcze nie ma — w trzech polach i trzech postaciach — a zmiana, która je zostawia, pokazuje to
  człowiekowi.
- WAY-160 — EN: The gate rule's *violates* example also names a gate failure whose fix the return step
  does not compare. PL: Przykład naruszający regułę bramki obejmuje też błąd bramki, którego
  poprawki krok powrotu nie porównał.
- WAY-287 — EN: The section for the human's decisions holds each descriptive `TODO` of the three fields
  that stands on the tree after the change. PL: Sekcja decyzji człowieka obejmuje każde opisowe `TODO`
  z trzech pól, które stoi na drzewie po zmianie.

## What I did for each remark

**R1.1 — WAY-71 *Scope*:** `task-cycle` added.

**R1.2 — WAY-160 *Verification*:** the *violates* example gained "the gate fails, its fix changes code,
and the return step does not compare the fix's range". The *complies* sentence is untouched.

**R2 (route B):**
- WAY-71 binding sentence and `elements/common/rules.md` carry one extended sentence (same text in both,
  checked by a whole-whitespace comparison): `TODO` only where an entry stands on something the
  foundation does not hold yet — *Rests on* as `TODO — <the fact, with its source>`, *Derives from* as
  `TODO — <the decision, and where it is expected>`, *Based on* as
  `TODO — <what is missing, with its source>`; "a change that leaves one there puts it before the human".
- WAY-71 *Rationale* rewritten for the three fields (the reason is that of *Rests on*, in the human's
  words "a cycle would stop to write a fact outside its task" stays in *Rejected*); one sentence added
  on *Relations* and *Origin* (they state what the author knows of the entry itself, so a gap there is
  an unfilled field, not a missing thing). That sentence is my wording; it is the reason for the
  human's rejection of `TODO` in them and the human should read it. *Rejected* keeps the two earlier
  ways and gains "`TODO` only in *Rests on* — an author of a decision whose source is silent, or of an
  invariant whose decision is not written yet, would have to stop the cycle or write `none`, which is
  false".
- WAY-71 *Verification*: the *complies* example `Based on: TODO — <what is missing>` now reads
  `<what is missing, with its source>` (the exact form) and is true; a *complies* case for *Derives
  from* was added; the *violates* cases gained a bare `TODO` in *Rests on*, *Derives from* or *Based
  on*, and `TODO` in *Relations* or *Origin*.
- The decision template: the *Based on* line of the form gained `| TODO — <what is missing, with its
  source>`, and a bullet says where a source is silent *Based on* reads that form, never a bare `TODO`
  and never `none`, that the main branch may hold it with the human told, and that *Relations* and
  *Origin* never read `TODO`.
- The invariants template's *Links* bullet now names both forms (*Rests on*, *Derives from*) and says
  the bare word is an error in each. Its form lines already had both.
- `foundation_check.py`: `check_rests_on` became `missing_thing`, used for *Rests on*, *Derives from*
  (invariant) and *Based on* (decision): a value that begins with the word `TODO` (also in backticks) is
  read whole — no fact, decision-number or fingerprint reading of its text — and a bare `TODO` (also
  `TODO —` with nothing after) is reported as
  `*<Field>* reads `TODO` and <says what it fails to say>: write `TODO — <form>`` with the form of that
  field; a value that does not begin with `TODO` is read as before (existing tests for quoted
  sources, fact identifiers and fingerprints pass unchanged). `Relations` and `Origin` of a decision now
  do not take a value that begins with `TODO` ("does not take"); the fields that already forbid `TODO`
  are unchanged. Docstring updated in both bullets.
- Tests (8 new test methods; `test_foundation_check` 103 → 111 tests): descriptive form with a
  comma, with ` · ` inside, with a decision number or identifier inside, in backticks, over two lines
  (for *Based on* and *Derives from*); bare forms `TODO`, `` `TODO` ``, `TODO —`, `TODO — ` for both;
  `TODOs` read as before; a normal bad *Derives from* number still reported; `TODO` and `TODO — the
  reasoning` in *Relations* and *Origin*. Red run before the code: 14 failures in the new tests
  (`python -B -m unittest test_foundation_check` from `elements/common/`, exit 1); green after: OK,
  111 tests.
- WAY-287 binding sentence, rationale and *Verification* (a *complies* case with `Based on: TODO — ...`
  and `Derives from: TODO — ...`; the *violates* case names the three fields) and item 15 of
  `request_template.md` now cover the three fields: read the invariants file and the decision log of the
  tree after the change; one item for each gap, in plain words (the rule the invariant states or the
  question the decision answers, and what is missing), with "Merge with the gap?"; the first
  correction's settlement (the whole tree after the change; one item per request while an old gap
  stands) is kept. The item's own text names the three forms in code spans, as the item list of the
  template already does; the sentence to write in the description stays in plain words.

**R3 — what does not change:** the gate order, step 10 and 11, and the other items stand; I touched no
file outside the list above.

## Search of the foundation (WAY-33) and projected mode

- Searched `TODO` in `elements/*/skill`, `elements/*/template.md`, `elements/common/*.md`,
  `product-guidelines/`, `project-level/` (forms, skills, technology, task, lead), `instruction-files/`
  and `foundations/*.md`. Nothing else states the old "only *Rests on*" rule.
- Conflict check, **none found** but two places read:
  - `elements/glossary/template.md:92` says the glossary's `TODO` in *Not* never stays on the main
    branch; it is another field and the rule's "only where an entry stands on something" does not
    cover it, so the two agree.
  - Projected mode (`project-level/definition_template.md` around 345–356, `elements/invariants/skill/SKILL.md`
    line 60, `elements/common/projected_mode.md`) lets a projected entry's *Derives from* read
    `TODO — <the decision's question>, projected in <the definition's path>`; a projected entry is
    in a definition, not on the main branch, and `foundation_check.py` reads it after it is written
    into the foundation, where the task that writes it completes the field. The projected form and the
    main-branch form `TODO — <the decision, and where it is expected>` are compatible (the path is where
    the decision is expected); I changed nothing there.
- Glossary: no term in a new meaning; `gate` and `return step` unchanged.

## Counts of `foundation_check.py`

- the-way, on this tree: `python -B elements/common/foundation_check.py .` exit 0, "0 errors"; the
  foundation holds no `Rests on`, `Derives from` or `Based on` `TODO`, nor `TODO` in *Relations* or
  *Origin* (grep of `foundations/*.md`).
- loop2, read-only: `python -B elements/common/foundation_check.py <the loop2 checkout>` exit 1, 1 error:
  `foundations/invariants.md:1244: *Rests on* reads `TODO` and names no fact` — the bare `TODO` the
  task already names (loop2 PR #70). Reports about *Based on*: 0, *Derives from*: 0, *Relations*: 0,
  *Origin*: 0, *Rests on*: 1. So loop2 holds no such entry for the four new fields, as the human was
  told, but it does hold one bare `TODO` in *Rests on*; the task's *Out of scope* leaves it to loop2's
  update.

## Checks (command and exit code)

- `python -B -m unittest test_foundation_check` (in `elements/common/`), before the code: FAILED
  (failures=14), exit 1; after: OK, 111 tests.
- `python -B gate/run_tests.py task-cycle` exit 0 (238 tests)
- `python -B gate/run_tests.py elements/common` exit 0 (130 tests)
- `python -B gate/run_tests.py instruction-files` exit 0 (104, 5 skipped)
- `python -B gate/run_tests.py agent-instructions` exit 0 (18)
- `python -B gate/run_tests.py elements/part-map` exit 0 (39)
- `python -B gate/run_tests.py relation-model` exit 0 (12)
- `python -B gate/run_tests.py installation` exit 0 (44 tests)
- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors")
- Not run: the full gate.

## Own-work check

The requirement most likely unmet: that the extended sentence is the same in WAY-71 and `rules.md`.
Check: both files read with whitespace collapsed and the sentence tested as a substring; both true.
The second: that the script now says what the rule says. Checked by the tests above: each of the three
forms passes in descriptive form (with a comma, ` · `, an ABC number in the text) and fails bare, and
`TODO` in *Relations* and *Origin* fails. Mutation thought through: dropping the strip characters makes
`TODO —` pass (caught); dropping the word boundary reads `TODOs` as `TODO` (the "read as before" test
for *Based on* only shows it passes either way, so it does not catch that mutation: the *Rests on* test
from the first run still does).

## Unread material

none (the handoff, the remarks and the four templates and files I edited were read; projected-mode files
were read at the places named above only: `project-level/definition_template.md` lines 345–358 and
`elements/invariants/skill/SKILL.md` lines 52–66, `elements/common/projected_mode.md` by search).

## Searches not found or unclear

- Unclear: whether the unrelated `Rests on` bare `TODO` in loop2 (1 error) conflicts with "the-way and
  loop2 hold no such entry" in R2; I read it as meaning the four new cases (the report above separates
  them).
- Unclear: the exact wording of the *Relations*/*Origin* sentence in WAY-71's *Rationale*; the remarks
  give the rejection but not its reason, so the reason is mine (see R2).
