# Slice 8 report — the refinement skill: the logs item, lasting exclusions and the split

**Status:** done
**Commit:** `eac1751` on `task/cycle-technology-decisions-batch` (base `22c626c`)
**Model class:** cheaper (the slice's *Model*)
**Method:** `task-cycle/change/SKILL.md` read whole; variant `slice.md` (read whole). `agent-instructions/README.md` read.

## Files changed

| File | Added | Removed | Item |
|---|---|---|---|
| `project-level/task/skill/resolve_gaps.md` | 15 | 9 | item 16 and foundation entry row 3 |
| `project-level/task/template.md` | 2 | 2 | item 25 |
| `project-level/task/skill/read_sources.md` | 1 | 1 | item 30 |

No skill description changed, so `skill_entry_points.py --write` was not needed.

## Changes made

- **Item 16 (`resolve_gaps.md`).** The list now holds three items the check handles apart: how to read the logs, the record's life, and the failure. Changes:
  - The quoting bullet says a logs decision silent on how an agent reads the logs answers nothing for the reading item, as a decision silent on the record's life answers nothing for that item.
  - A new bullet: where nothing answers the reading item, it goes as the other items of the list do (*To do* item for that work, or the split). This follows WAY-139 ("it goes as the other items of the list do").
  - The ask-the-human bullet is limited to the record's life and the failure, since WAY-139 gives the reading item no such question. Its text is otherwise unchanged.
- **Item 25 (`template.md`, *Out of scope*).** The existing sentence said a lasting exclusion belongs in a decision or a *Settlements to record* row. It lacked the qualifier "that later work builds on" and the term "decision candidate" from `SKILL.md` ("Carry the foundation decisions", WAY-26). I judged that as not already saying it, and rewrote the sentence to match: "A lasting exclusion that later work builds on is a decision candidate: a row of *Settlements to record* or a projected or current decision, not here." This is the one judgement call in the slice; if the orchestrator reads the old sentence as already saying it, the commit can be reverted for this file alone.
- **Item 30 (`read_sources.md:23`).** The two sentences "Check that this is one task. If it joins independent outcomes, identify the split." were replaced by the item's sentence, word for word. Verified by a fixed-string match against `task.md:79`. The following sentence ("For a project member…") is untouched.

Foundation entry row 3 (WAY-139, reworded in commit `a0c6607`) was read in its current text, and the wording of item 16 follows it: the logs item is tied to the logs decision as the record's life and the failure items are.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Project-level tests | `python -B gate/run_tests.py project-level` | 0 | 275 tests, OK |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | 0 errors |
| Private paths test | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 | 9 tests, OK |
| Diff check | `git diff --check` | 0 | clean |

Prose-only slice: no test was written first and none was changed. The full suite was not run (per the handoff).

## Own-work check (section 3)

- **Requirement:** item 16 must not make a reading-item decision the authority for the record's life (or vice versa), and the failure item must still ask the human.
- **Check:** read the final bullets of `resolve_gaps.md:66-86` against WAY-139 Verification (complies and violates lines) and the slice goal. The logs decision answers only the reading item; the record's life and the failure keep their ask-the-human path.
- **Result:** the text matches WAY-139. No test runs this; it was checked by reading. Nothing failed, so there is no rerun.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-139 read whole (in its current text at the handoff's range) to word the logs bullet. WAY-165 read in its handoff range, to confirm that the logs decision says "how an agent reads it".
- `project-level/task/skill/SKILL.md:48-52` read to compare the wording of item 25.
- `task.md` lines 52, 70 and 79 read to confirm the item texts.
- WAY-13 (`foundations/decisions.md:403-442`) and WAY-26 (`:688-717`) were **not** read whole. Item 30's sentence is given word for word, so I did not need WAY-13 to write it. For item 25 I relied on the `SKILL.md` sentence, not on WAY-26's text.

## Searches not found or unclear

- Whether the template's sentence on lasting exclusions "already says it" for item 25: unclear, decided as not already saying it (see above).
- The handoff's *Entries and files* list gives WAY-13 at `decisions.md:403-442`; the current location was not checked by a search.
- None otherwise.

## Problems observed

- None in the change. The handoff's drift note (line numbers in the task and plan are old) was not an issue: each place was found by its content.
