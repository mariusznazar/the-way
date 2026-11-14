# Return step report: service-reading-and-invariant-condition

**Status:** done

**Commits** (on the same branch, after the reviewed head `4f26b6b`): `43ffa5a` Return step: rewrap WAY-80 and state WAY-84's example of a reading in plain words

## Foundation compared with code

Range compared: base `0e1cd3c` to head `4f26b6b`, against the frozen task (*Decisions in play*, *Settlements to record*), the entries the change writes or changes, the entries the search of the foundation found, the part map and the files of the repository.

| Entry or file | Compared with | What no longer matched, and its correction |
|---|---|---|
| WAY-80 (`foundations/decisions.md`) | task items 1, 3, 5; the facts template; the *Verification* pair | One line of the second binding paragraph was left long by the fix (`... that sets those rules and` then a short line). Rewrapped in `43ffa5a`; wording unchanged. Otherwise the binding sentences, *Rationale*, *Rejected* and the pair agree with the template's *Source* rules. |
| WAY-84 | task items 1, 2 | The `complies` example read "which no page open without the product's people's access shows", awkward. Reworded in `43ffa5a` ("without the access of the product's people"); no binding sentence touched. |
| WAY-60 | task item 7; invariants template | none: the new sentence, its two paragraphs, *Rationale*, *Rejected* and the pair agree with the template's *The sentence* bullet, which cites WAY-60 and says the same. |
| WAY-35 *Verification* | invariants file | none: names `elements-no-pending-marker` beside `skill-rule-source`. |
| `elements-no-pending-marker` (`foundations/invariants.md`) | its test `elements/common/test_elements_pending_marker.py`; WAY-35 | none: the sentence ("every run of spaces and line breaks counting as one space") and the pattern `decision[ \n]+pending` mean the same; *Part* names the six parts whose files stand under `elements/`; the test file is in `elements/common/`, part `elements-common`. |
| `elements/environment-facts/template.md` | WAY-80, WAY-84; the entries of `foundations/environment_facts.md` | none: the opening paragraph, the *Source* form line, the three forms, the reading rules (one invocation, code block indented under the line, versions, no secret), the setting bullet and the rule for code at a fixed commit agree with WAY-80 and WAY-84; the rule for code cites no decision, as the task says it changes none. Existing fact entries are in the forms of editions and archived pages; none is a reading, so none needs a correction. |
| `elements/invariants/template.md` | WAY-60, WAY-58 | none: the pending note is gone; the bullet on *Links* that says a decision of the pinned the-way is no decision entry of the product's log (WAY-58) agrees with the new rule (named in the sentence). |
| `elements/environment-facts/skill/draft.md`, `write.md` | the template (WAY-35) | none: `draft.md` holds the way of working only (run the call, narrow it to the fields the sentence rests on, look at the answer before quoting); `write.md`'s "the output quoted is the output of the run the entry names" still holds. |
| `README.md` (list of elements, row of `environment_facts.md`) | the template | none: both places cover a reading in a service. |
| `foundation-review/weak_points.md` (facts: "open its source at the address it gives ... A source that cannot be opened is reported as not checked") | WAY-82, WAY-84 | none: a reading in a service has no address to open and falls under "cannot be opened, reported as not checked", as a reading of a host already did; the task asks for no change there. |
| `agent-instructions/README.md` | the foundation check | none: it says the check lists invariants that read `test` and have no citing test; the change adds no switch and no report to the check, and the answer to the carried question changed no check. |
| `foundations/part_map.md` (`elements-common`, `invariants`, `decisions`, `environment-facts`) | the files the change adds or changes | none: the new test stands in `elements/common/**`; the parts' *Files* and *Depends on* hold (the test imports only the standard library and calls git, which the part map lists as a trusted partner). |

## Decisions written or changed

WAY-80, WAY-84, WAY-60 (changed in place, rows 1-5); WAY-35 (*Verification* only). In the return step: wording of WAY-80 and WAY-84 as above, no meaning changed.

## Invariants written or changed

`elements-no-pending-marker`, written by the foundation step: sets its rule row 6 of the task, derived from WAY-35. None written or changed in the return step.

## Environment facts

none: the change rests on no source outside the product that the foundation lacks.

## Glossary terms

none: the words the change uses ("reading", "source", "marker") keep the meaning they had; the glossary holds no entry for them and WAY-95 gives none for these.

## Part-map changes

none.

## Projected entries written whole or in part

none (the task is not a projected task).

## Rows of *Settlements to record* written

| Row | Went to |
|---|---|
| 1 | WAY-80 and WAY-84 (changed) |
| 2 | WAY-84 *Rejected* (changed) |
| 3 | WAY-80 (changed) |
| 4 | WAY-80 (changed) |
| 5 | WAY-60 (changed) |
| 6 | invariant `elements-no-pending-marker`, WAY-35 *Verification* |

No choice that binds after the merge was left unwritten; the task excludes none beyond item 6 (template text, no decision), which went to `elements/environment-facts/template.md`. Where a decision carries a pair of examples and a test holds part of its sentence: no test cites WAY-80, WAY-84 or WAY-60 by a line `decision:`, so no pair is reduced and no clause `tests:` is added.

## Checks (command, exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check after the return step's edits | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (`checked: 298 files, 0 listed`) |

Not run: `python -B gate/run_tests.py <directory>` after the return step's edits (they changed only prose of `foundations/decisions.md`, read by no test of a directory but the foundation check); the full gate (the orchestrator runs it). The gate of `elements/common` passed (201 tests, exit 0) on `4f26b6b`.

## Unread material

none (the handoff, `task-cycle/skill/return_step.md`, the record template's *Return step*, WAY-80, WAY-84, WAY-60 in their current text, the facts template's *Source* section, and the files in the table above were read; the review reports were not opened, since the handoff gives only their verdicts).

## Searches not found or unclear

none
