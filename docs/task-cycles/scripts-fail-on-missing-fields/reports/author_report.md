# Report — the one author of the change (scripts-fail-on-missing-fields)

**Status:** done with concerns (concerns below are for the orchestrator's judgment; none blocks)

## Change

- `foundations/decisions.md`: +79 lines, -0. One new entry, WAY-330 — "What does a script of the-way
  do when a file it reads lacks a field it needs?", placed after WAY-329 and before the
  *Withdrawn identifiers* list. WAY-330 was the next free number: no entry and no withdrawn number
  holds it.
- No script, test, skill or part-map file changed.
- Commit: see the return message (one commit on `task/scripts-fail-on-missing-fields`, base
  `e9a0f926dc9758f6554e8c0a30925d3e4d68cfed`).

## Entry and its meaning (foundation step, `row 1`–`row 4`)

- English: a script of the-way that reads a file written by an agent or a human checks that the file
  holds each field it needs (a field = section heading, row label, table column, JSON key) and ends
  with an error naming the missing or renamed field; the rule binds new scripts and, in a changed
  script, every field of each file whose way of reading the change reworks; a missing field gives
  exit code 2 with file and field in the message, except in a script that exists to check the form of
  a file, where it is a finding of its list with exit code 1; each covered reading has one test that
  omits one field and asserts the failure naming it; the *Scope* lists all 16 parts and a new part is
  added to it.
- Polish: skrypt the way, który czyta plik pisany przez agenta albo człowieka, sprawdza, czy są w nim
  pola, których potrzebuje, i kończy się błędem z nazwą brakującego pola; reguła obejmuje nowe
  skrypty i w zmienianym skrypcie cały odczyt każdego pliku, którego sposób czytania zmiana przerabia;
  brak pola to kod 2 z plikiem i polem w komunikacie, a w skrypcie sprawdzającym formę pliku —
  ustalenie listy z kodem 1; każdy objęty odczyt ma jeden test bez jednego pola; *Scope* wymienia
  wszystkie 16 części, a nowa część mapy się do niego dopisuje.
- Rows: row 1 (form: separate decision beside WAY-328, Scope of 16 parts, new-part sentence; changed
  script = whole reading of the file reworked), row 2 (one test per covered reading), row 3 (exit
  codes 2 / 1), row 4 (definition of a field). Marked `row 1`, `row 2`, `row 3`, `row 4`: no entry
  is `projected`, none is `the cycle's` — except the Verification examples and the last sentence of
  *Rationale* (see Choices).

## Checks (own work)

- `python -B elements/common/foundation_check.py` — exit code 0, output `0 errors`.
  Run with no `--skip-test-citations` switch: the entry writes no invariant.
- Own-work check (section 3). Requirement most likely unmet: row 1's "*Scope* of the decision names
  all 16 parts of the part map". Check: a one-off Python run (`python -I -c ...`) that took the part
  headings with a `- **Files:**` line from `foundations/part_map.md` (16) and the items of WAY-330's
  *Scope*, and compared them as sets; it also searched the binding sentences for *should*, *will* and
  RFC 2119 capitals. Showed: 16 parts, 16 Scope items, sets equal, no forbidden words, no CR bytes
  in the file. Exit code 0.
- The product's gate (`gate/run_tests.py`): not run — the orchestrator's (handoff). No test exists
  or was written: the change is one foundation entry.
- No review run, by the handoff.

## Search of the foundation (WAY-33)

Done once after the entry was settled. Read whole: WAY-12, WAY-33, WAY-38, WAY-51, WAY-173, WAY-217,
WAY-294, WAY-328 (the handoff's list); invariants `script-language`, `script-imports`,
`script-subprocesses`; the part map and the glossary whole; `task-cycle/skill/SKILL.md:495-509`;
`task-cycle/remarks_check.py` whole and `task-cycle/request_check.py` lines 1-120. Searches over
`foundations/*.md` for `exit`, `exit 2`, `quietly`, `silently`, `never agreement`, `could not check`,
`cannot be read`, `missing field`, `missing section`, and over decisions for `script` with `test`;
`git grep WAY-328` outside the log.

Findings:
- No entry the new decision makes false; no entry corrected. WAY-328 is unchanged (its price sentence
  is true still); WAY-38 is unchanged (its Scope has 8 parts, which does not narrow the new one).
- WAY-12 says "tests live only with invariants". The task's *Context* reads it as about the check of a
  decision, and a script-behaviour test needs no invariant. I followed the task and put one sentence
  at the end of *Rationale* saying so; no *Relations* line (the list has only `derives from` and
  `narrows`, and neither fits). See Concerns.
- WAY-294's *Rejected* uses exit 2 as "no listing was made" and `SKILL.md:502` reads exit 2 as "no
  listing: fix the call, or the file that could not be read"; the new rule's exit 2 fits that
  reading. `remarks_check.py` (exit 2 for a record without `cycle.md` or an unreadable report) and
  `request_check.py` (problems listed, exit 1; exit 2 for an unreadable file) are consistent with the
  rule as far as read; the decision claims nothing about them.
- Nothing outside `decisions.md` names WAY-328 or lists a *Scope* to extend; the part-map skill's
  `decide_entry.md:10` rewrites *Scope* references only for identifiers left behind by a split or
  merge.
- Glossary: *field* is not a glossary term; it is defined in the binding sentence itself, so no
  `record-glossary-term` run (WAY-95 not triggered: the word keeps a reader's meaning there).

## Reaches beyond the dispatch

- `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`:
  read whole — they are what `the-way-record-decision` names; the handoff pointed to the skill.
- `foundations/decisions.md` lines 10851-10984 (WAY-328, WAY-329, the withdrawn list): to place the
  entry and find the free number.
- `agent-instructions/README.md` and `task-cycle/change/SKILL.md`: whole, as the handoff gave.
- WAY-03 (the example `examples.md` names) was not read: see Unread material.

## Unread material

- WAY-03 (named by `elements/decisions/examples.md` as the form example): not read; the form was
  taken from WAY-328, WAY-329 and the template, and `foundation_check` passes.
- `task-cycle/request_check.py` lines 121-end: not read (the exit-code contract is in its docstring
  and `main` was not needed for the judgment).
- `foundations/decisions.md` beyond the entries named above and the lines the greps hit: not read
  (the handoff asks for no whole-file read).
- `foundations/invariants.md` beyond the three `script-*` entries and the grep hits: not read.

## Searches not found or unclear

- none found for anything the handoff asked to find; two points were unclear:
- The handoff says the foundation step is read "whole" in `task-cycle/skill/foundation_step.md`; the
  file is 33 lines and was read whole. It says "a question for the human arises only where..."; I
  found no such case. Unclear: whether the Verification examples count as an entry content "no row
  carries" (see Choices) — I treated them as the writer's wording under row 1–4 and flag them here.

## Choices, with the way rejected and its cost if wrong

- Relation `derives from WAY-38` (the task: "spokrewniona z WAY-38 jako reguła z tej samej rodziny").
  Rejected: `none`, since the quiet pass of WAY-38's Rationale is the very reason of the rule. If
  wrong: a reader follows a link that overstates the dependency; remove the line.
- *Based on:* `none`. The course lesson in the task's *Context* is the idea's origin, not a source the
  decision rests on, and no environment fact holds it. Rejected: naming the lesson's repository URL
  with a quoted passage and a read date — I did not read it, and the rule forbids a value from memory.
  If wrong: a missing source on the decision; add it through the environment-facts element.
- *Origin:* `none`: the task document may not be named (template), and the reasoning is in
  *Rationale* and *Rejected*.
- *Verification* pair of examples: the template's skill step 3 says to add a pair "where the human
  gives one or accepts one you propose". The human gave no pair. I wrote one from the task's *Context*
  (the `due` -> `due_date` case) and from rows 1-3, with nothing about existing scripts. Rejected:
  `Verification: none`. If wrong: the examples bind agents comparing a change with the decision more
  or less sharply than Mariusz would; he accepts them at the merge, so the request should name them as
  "the cycle's" in its section for the human's decisions.
- The last sentence of *Rationale* (tests of a script's behaviour stand without an invariant; WAY-12
  concerns how a decision is checked) and the price list are the writer's, derived from the task's
  *Context* and the *Not chosen* costs. Rejected: leaving WAY-12 unmentioned — a future agent reading
  "tests live only with invariants" would see a collision. If wrong: remove the sentence.
- *Rejected* holds only the *Not chosen* ways the task keeps (questions 1-4 of *Questions to settle*),
  each with its cost, translated. No way of my own entered it (WAY-134). It states, from the task's
  source, that the skills that read exit codes know only 0, 1 and 2 — a statement on what tools do
  today, allowed there because it is a source's, not the author's.
- Row 4 (definition of a field) has no *Not chosen*, so nothing for it in *Rejected*.
- The binding part is three long sentences, so as to stay within 1-3 (the template); it reads heavily.
  Alternative, splitting into more sentences, breaks the template. If wrong: reword in place.

## Concerns

1. WAY-12's sentence "tests live only with invariants" and this decision's required test collide in
   letter; I followed the task's *Context* and said so in *Rationale*. Mariusz may want WAY-12's
   wording narrowed (a separate change).
2. Part-map surfaces `tracked-private-paths-command` and `project-plan-state-command` "keep ... exit
   codes". A later change that gives such a script exit code 2 for a missing field changes what the
   surface promises; the decision does not say which wins. Not settled here (decision claims nothing
   about existing scripts).
3. Observed in `remarks_check.py` (docstring and `check`): a record with no `reports/` directory lists
   nothing and exits 0. Not judged; review of existing scripts is out of scope. Recorded as an
   observation only; no cause or consequence verified.
