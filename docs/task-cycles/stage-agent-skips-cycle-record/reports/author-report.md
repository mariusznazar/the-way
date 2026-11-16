# Author report — stage-agent-skips-cycle-record

**Status:** done

## Commits

- `de24e5b8` on `task/stage-agent-skips-cycle-record` (base `3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898`): "Tell each stage agent in its handoff that the cycle record directory is not its to read (WAY-148)". Amended once before return (an earlier `68b7ce04`), so no review saw the earlier hash.

## Files changed

- `task-cycle/skill/SKILL.md` — +3 / -1: the sentence of the task's *To do* 1, word for word ("It tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them."), placed after the sentence of the list of what every handoff carries (which now ends "(WAY-148)." and not "and the report path." as the task's line reference says; the list grew since the task was written) and before "The agent reads that `SKILL.md` whole".
- `foundations/decisions.md` — WAY-148 changed in place:
  - binding sentence 2: "…and since only the orchestrator reads the cycle record, the handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them, and an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it." The first paragraph stays at three sentences.
  - *Verification*: complies gains a handoff that tells its agent so and a reviewer that reads the author's report because its handoff names it; violates replaces "an agent other than the orchestrator reads the cycle record to learn an answer" with an agent reading `cycle.md` or another file of the record directory its handoff does not name, and a handoff lacking the sentence.
  - *Rationale*: adds the independence of the assessment (the loop2 case, written as "a reviewer of a spec in a cycle of a game product", no repository named) and why the handoff carries the sentence.
  - *Rejected*: adds, from the *Not chosen* of questions 1 (b), 1 (c), 2 (a) and 3 (b), the four ways with their costs.

Foundation entry marking (foundation step): the WAY-148 change is `row 1`. Meaning in English: a stage agent reads `cycle.md` and the other files of the cycle's record directory only where its handoff names them, the handoff tells it so, and the reason is the independence of its assessment. Znaczenie po polsku: agent etapu czyta `cycle.md` i inne pliki katalogu zapisu cyklu tylko wtedy, gdy zlecenie je wskazuje; zlecenie mu to mówi, a powodem jest niezależność jego oceny. No part added beyond the row; no pair of examples added.

## Checks

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`), exit 0, "0 errors" — run twice, the second time on the final committed text.
- `python -B -m unittest discover -s task-cycle -p "test_*.py"`, exit 0 (534 tests, 2 skipped).
- `python -B -m unittest discover -s elements/common -p "test_*.py"`, exit 0 (257 tests).
- Not run: the full gate of the product (the handoff forbids it); `agent-instructions/skill_entry_points.py --write` and `agent_type_copies.py --write` (no skill description changed, no agent-type definition changed).
- No test cites WAY-148 by a `decision:` line (searched the repository); `task-cycle/test_request_check.py:61` only quotes WAY-148 in a fixture and is unchanged and passing.

## Own-work check

Requirement most likely missed: the sentence for the skill is word for word, and WAY-148's first paragraph stays within three sentences with the foundation check passing. Check: a multiline search of `task-cycle/skill/SKILL.md` for the task's sentence across the line break found it once (after I removed a "(WAY-148)" I had first put inside the sentence, which a first run of the same search did not match — the first run found 0, the run after the removal found 1). The foundation check was green on the first run.

## Search of the foundation (WAY-33)

Searched the foundation and the skills once for sentences on who reads the cycle record or other agents' files ("only the orchestrator", "alone read", "reads the cycle record", "other agents' handoffs/reports"). Found only WAY-148 and the orchestrator's sentence "You alone read `cycle.md`" in `task-cycle/skill/SKILL.md` — consistent with the change and left as it is. WAY-150 ("every other agent of the cycle reads what its handoff names") agrees; WAY-368 and WAY-370 are kept as they are, as the task asks. The decisions that derive from WAY-148 (WAY-150 and five others) are not altered: the change adds to WAY-148 and removes no sentence they rest on. The glossary holds no entry for "cycle record" or "handoff"; no term added.

## Reach beyond the dispatch

none (all entries and files read were named by the handoff; I also read `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/way_of_working.md` and `rules.md`, which the element's `SKILL.md` and the foundation step name).

## Choices

- Sentence position in the skill: after the sentence ending "(WAY-148).", as its own sentence. Rejected: appending inside the list sentence (it would no longer read "It tells the agent"). Cost if wrong: none beyond wording.
- No "(WAY-148)" citation inside the new sentence, to keep it verbatim; the sentence before it carries it.
- In *Rationale* the loop2 case is stated without a repository name and without a claim that its record is closed to a reader (the task does not say so).
- The parking variant of the task's *Context* (the same sentence in four stage skills) is not in *Rejected*, since the row's source does not keep it and the foundation step bars a way the writer derives.

## Unread material

- `elements/decisions/examples.md` (named by the element's reading rules): not read; I took the form from WAY-148 itself and the template.
- `foundations/part_map.md` parts `task-cycle` and `decisions`: not read whole; the entry's *Scope* is unchanged (`task-cycle`), no file added.
- Glossary entries: searched for the terms used (`cycle record`, `record directory`, `handoff`), none held.

## Searches not found or unclear

- The task's reference to the skill sentence "ending 'and the report path.'" no longer matches the file: that list sentence now continues with the copy of the "Working copies" paragraph and ends "(WAY-148)."; I placed the new sentence after it. Not otherwise unclear.

## Working copies

none made.
