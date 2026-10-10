# Slice 1 report — technology step carries the tie-breaker and the "what will this break" tests

Status: DONE_WITH_CONCERNS

Commit: `a93b92a` feat(project-level): Break a tie between places to run and test the recommended
option for what it could break

## What changed

- `project-level/definition_template.md` (Technology section): two new bullets after the WAY-123
  bullet. One states WAY-137: the tie-break for a place to run and that it decides nothing else.
  The other states WAY-138: which option is tested, with which three tests, what is never tested,
  that the risks are hypotheses the critique does not strike, that they stand beside the
  recommended option before the choice, and that a risk taken reaches *Rationale* beside the
  lacks, marked as a hypothesis. The pointer "`settle-technology` leads that." moved from the end of
  the WAY-123 bullet to the end of the WAY-138 bullet, so it still closes the weighing rules.
  Wording follows the binding sentences of WAY-137/WAY-138 closely and adds no rule.
- `project-level/technology/SKILL.md`:
  - Intro: the template holds "the weighing and the tests of options".
  - Step 5 reordered: form recommendation + weak point (WAY-123), tie-break for a place to run with
    the reason given (WAY-137); then one fresh agent for the wave runs the three tests on the
    recommended option of every choice of the wave, constraint-settled ones included, never a
    `held by` choice nor a decision already written (WAY-138); then the contradiction critique,
    told the risks are hypotheses, not claimed differences, so it does not strike them (WAY-120,
    WAY-138); then the table shows the risks beside the recommended option, each marked as a
    hypothesis with no source.
  - Step 6: the human who chooses the recommended option takes its risks (WAY-138).
  - Step 7: the lacks of a chosen option and the risks taken with it go to *Rationale*, each risk
    marked as a hypothesis (WAY-138).
- `elements/decisions/skill/SKILL.md`, Projected mode: new Step 3 bullet — for a technology choice
  `settle-technology` hands over, the chosen option's lacks and the risks taken stand in
  *Rationale*, each risk marked as a hypothesis, never in *Based on* (WAY-122, WAY-138).
- `elements/common/critique/SKILL.md` and `foundations/` unchanged.

## Checks (run in the worktree)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py project-level` | 0 | 81 tests OK |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current |

Line endings: all three files `i/lf w/lf` before and after. No new line over 100 columns (the long
lines reported are pre-existing tables and the frontmatter `description`).

## Self-review against the brief, WAY-137, WAY-138

- Rules in the template, order of work in the skill; the skill points to "the template's rule" for
  the tie-break rather than restating it in full — one home per fact.
- Step 5 order matches the brief: recommendation → tie-break → one tester per wave → contradiction
  critique told risks are hypotheses → table with risks beside the recommended option.
- Tested set: only the recommended option (not every option — a WAY-138 violation case);
  constraint-settled choices included; `held by` never; already written decisions never.
- Risks shown before the human chooses; in *Rationale*, never *Based on* — both stated.
- WAY-137 limits honoured: tie-break only after cost/simplicity, no filter, no weight in the table.
- No `description` changed.

## Choices made

- Cited `(WAY-122, WAY-138)` in record-decision: WAY-122 says the decision records the lacks,
  WAY-138 places them (and the risks) in *Rationale*.
- Did not add persistence of the risks to `.runs/technology/<choice>.md`: a resumed step reruns
  step 5 from the passed reports, so nothing is lost, and the brief did not ask for it.
- Did not add a "stop if no fresh agent can run" clause for the tester: step 4 already stops the
  step when no fresh agent can run, so step 5 is never reached without one.

## Concerns

- A choice the human leaves unanswered "goes into the next table" (step 6). The text does not say
  whether its recommended option is tested again or its earlier risks are carried over; read
  literally, step 5 tests "every choice of the wave", and a carried choice belongs to its own
  wave. Low impact; left as is to avoid adding a rule. Orchestrator may want a word here.
- Step 5 is now a long paragraph (four actions). Splitting it into sub-steps would change the
  numbering other text refers to (`define-project`, step 0 resume), so it was kept as one step.

## Fix round 1

Finding (Important): a choice carried into the next table (step 6) could reach the human with no
risks beside its recommended option, since step 5 tests only "every choice of the wave".

Change, by the orchestrator's ruling, one sentence in step 6 of `project-level/technology/SKILL.md`:

> A choice the human leaves unanswered goes into the next table with the risks already shown beside
> its option recommended, and is not tested again unless that option changes, when the new one is
> tested (WAY-138).

No other rule added. The earlier concern about a carried choice is closed by this sentence.

Commit: `3a0e87a` fix(project-level): Keep a carried choice's risks beside its recommended option
in the next table

Checks:

```
$ python -B gate/run_tests.py project-level
Ran 81 tests in 0.035s
OK
exit=0
$ python -B agent-instructions/skill_entry_points.py
entry points are current
exit=0
```

Line endings: `i/lf w/lf`, unchanged.
