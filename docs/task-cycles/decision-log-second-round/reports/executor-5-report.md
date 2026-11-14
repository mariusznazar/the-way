# Executor 5 report (written by the orchestrator from the executor's return, which could not write the file)

Status: done with concerns. Commit `a0f6afc`, `elements/environment-facts/template.md` and `elements/glossary/template.md` (haiku executor).

## Checks
- `python -B elements/common/foundation_check.py`: exit 1, 0 lines for the two files.
- `python -B gate/run_tests.py elements/common`: exit 1, 201 tests, 1 failure `test_the_way_foundation_passes` (other slices' lines).
- `python -B gate/run_tests.py elements/part-map`: exit 0, 39 tests.
Own-work check: grep of both files for WAY-64, 72, 76, 77, 78, 80, 86, 96, 226: nothing left; full diff read.

## Reasons added (file, place, sentence, entry written from)
Environment facts template: (1) "What changes together stands together: a fact changes when its source changes, and two sources in one entry would send a new edition of one to every entry resting on the other." (WAY-76); (2) "The address of an edition already names what the fact is true of, and the date read does so for a source without editions, so a field naming it again is a copy that drifts." (WAY-77); (3) ""Latest" would make the sentence change with the date, not the world." (WAY-77); (4) "A voluntary catalogue binds only because someone chose it; without that choice an agent would bind the product to whatever it recognised." (WAY-86); (5) "A law binds whether chosen or not, and holding the product to it until a human settles otherwise makes silence raise checks rather than remove them." (WAY-86).
Glossary template: (6) "A definition of a word of the process stands once, in the-way, because copies drift between products." (WAY-226); (7) "A definition of one sentence is read whole beside every use of its word." (WAY-96).

## Entries left under the "stay" rule
WAY-93 (glossary lines 34, 36), WAY-94 (lines 85, 90), WAY-97 (lines 7, 37, 38, 98): numbers kept, no reason added. The plan's missing sentence of WAY-93's rule ("holds no other heading than its entries") was not added because the entry stays.

## Gaps noticed, not acted on
- Environment facts, the rule "nothing its sentence says is an invariant" (line 82) has no reason sentence; WAY-76 *Rationale* gives one ("An invariant written as a fact would never be checked on the commit that breaks it.").
- WAY-64, 72, 78, 80 numbers removed; the plan gave no reason sentence for them and the executor did not read them at base.

## Unread material
`task.md` beyond lines 33-40; `plan.md`; WAY-64, 72, 78, 80 at the base (not in the slice's *Read*). WAY-293 found by heading (the plan's range is of the base).

## Searches not found or unclear
The handoff's WAY-293 range was not a range of the current log; found by heading search.

## Working copies
`.runs/executor-5/` made and removed.
