# Return step report — request-decision-groups

**Status:** done. Nothing needed correcting; **no commit** was made. Head stays `9d4bdcde27179325126d1431e6cb825df3290754`; the worktree is clean.

## For the record's *Return step*

- **Foundation compared with code:** the entries WAY-287, WAY-289, WAY-290, WAY-317 (edited) and WAY-327 (new), the entries the task names (WAY-286, WAY-288, WAY-114) and those the search found, against `task-cycle/skill/request_template.md`, `task-cycle/request_check.py`, `task-cycle/test_request_check.py`, `task-cycle/skill/correction.md` and `task-cycle/skill/SKILL.md`. What no longer matched: **none**. Points compared:
  - WAY-287 (three groups with headings `Needed from you`, `Fix or let through`, `You accept by merging`; every group stands with `none`; continuous numbering; `none` alone for the whole section; unrun stages of a blocked request under *Needed from you*) against the template's group paragraph, skeleton, kinds 1-15 and variants, and against `check_decision_groups` in `request_check.py`: agree.
  - WAY-289 (title, three answers, the same answer for steps and checks skipped, proposals not applied and an incomplete reading, the leftover after a correction carries only the question of a task) against kinds 4, 8, 9, 14, the *A correction* row and `correction.md`: agree.
  - WAY-290 (group headings in what the form check holds, no content judged) against the script's docstring and behaviour and its tests: agree.
  - WAY-327 (four parts of an item in which the human chooses; the writer checks before the request opens) against "What an item carries" and step 2 of "Write, check, publish": agree. The action item (kind 3) and the accepting group's content are in the template only, as the task gives them.
  - WAY-317 (corrected in the change: no screenshot shown, accepted by merging) against kind 13: agree.
  - WAY-286, WAY-288, WAY-292, WAY-114, WAY-291, WAY-295, WAY-308, WAY-274, WAY-163, WAY-219, WAY-10: read in the passages that name the section or its items; each agrees (WAY-114's plain sentence is kind 6; WAY-308 and WAY-274 are kinds 12 and 11; WAY-163's "the request names each stage not run" is kind 1; WAY-219's unchecked screenshot is kind 4; WAY-291's form error is kind 15). None says that the request *asks* a question for an item of the accepting group.
  - Numbered references by kind: `correction.md` "item 8" (and the new "items 4, 9, 14"), `SKILL.md:563` "item 12", the template's "item 4" at kind 13: unchanged and pointing at the same kinds (mapping to the base `e3825a8` verified in the author report).
  - Part map entries `task-cycle` (files `task-cycle/**`) and `decisions` (`elements/decisions/**`, `foundations/decisions.md`): every changed file lies in them; no file is unclaimed; responsibilities unchanged; no surface changed. `agent-instructions/README.md` points at the template and needs no word on the groups.
- **Decisions written or changed:** WAY-287, WAY-289, WAY-290, WAY-317 (edited in place) and WAY-327 (new), all written in the change's foundation step and the fix (commits `ff77994`, `9d4bdcd`). The return step writes none.
- **Invariants written or changed:** none. No invariant concerns the form check's group headings; none is set by the task, a decision or the human.
- **Environment facts:** none (the change rests on no source outside the product).
- **Glossary terms:** none (no word used against its entry or in a meaning WAY-95 gives an entry; "kind" and "group" are ordinary words).
- **Part-map changes:** none.
- **Projected entries:** none (the task has no project definition).
- **Rows of *Settlements to record* written:** row 1 — WAY-287; row 2 — WAY-287; row 3 — WAY-327; row 4 — WAY-289; row 5 — WAY-290. All five were written by the foundation step; the return step missed no row.
- **Choices that bind after the merge not yet recorded:** none. The choices the author report names are covered: the leftover rule and the blocked-request rule are in WAY-289 and WAY-287; the "kind 15" placement, the removal of questions from accepting items and the example's wording are template-level and stay rows of the questions table.

## Checks

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Focused: task-cycle | `python -B gate/run_tests.py task-cycle` | 0 (254 tests, OK) |
| Worktree state | `git status --short` | empty |

Not run: the whole gate (the orchestrator's; it ran on this head with exit 0, 883 tests, as the handoff says).

## Unread material

- Decisions WAY-10, WAY-274, WAY-163, WAY-219, WAY-308, WAY-140, WAY-325: read in part (their binding sentences, and for WAY-274, WAY-163, WAY-219, WAY-325 also *Verification* and the start of *Rationale*); not read whole, since only their mention of the section or of the request's items was compared.
- `task-cycle/skill/SKILL.md`: not read whole; only the passages that name the section or the request's items, as before.
- Invariants and the rest of `foundations/part_map.md`: not read beyond the entries `task-cycle` and `decisions` and a grep for the request description.
- Otherwise as in `author_report.md` and `fix_report.md`.

## Searches not found or unclear

- A search of `foundations/part_map.md` for `request_check`, `request description` and `request_template` found nothing: the part map names no file of the change, only globs.
- A search of `foundations/decisions.md` for wording in which a request *asks* the human for an item now in the accepting group (`whether to merge`, `merge anyway`, `merge without`, `Accept`) found none left besides the example in WAY-327's *Verification* (`violates`, the bad item) and WAY-289's own questions for *Fix or let through*.
- None unclear.
