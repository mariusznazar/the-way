# Correction report — drop the exception for a listed relation line (finding N1)

**Status:** done

Commit (range from `acbcb15`): `a5ea36f`. Worktree clean, nothing pushed. Code as at `4deb195`
otherwise; `plan_state.py` and the invariants unchanged. Minor findings N2 and N3 left alone.

## The remark as made, and how

"Poprawimy zatem tak jak proponujesz": a `Task relation:` or `Project relation:` line that the check
of private paths lists is cleaned like any other; nothing the check lists is committed; the lines stay
as they are when the check does not list them; the conflict the reader may report is a known, visible
consequence.

## Places changed and why

| Place | Change |
|---|---|
| `task-cycle/skill/SKILL.md`, "The record before it is committed", step 3, bullet on the two relation lines | they stay as they are unless the check of step 4 lists them; a listed line is cleaned like any other and the reader may then report a conflict with exit 1 for this task, which the human sees in the request |
| same section, step 4, exit-1 paragraph | the exception that committed the listed line is removed; "no listing is left in place, a `Task relation:` or `Project relation:` line included"; where such a line had to be cleaned the request tells the human, pointing to item 12 of *For you to decide* |
| `task-cycle/skill/request_template.md` | the row "A draft for another reason" is back to its original text (the listed-line example and its *Checks* detail removed); new item 12 among the items of *For you to decide* ("A relation line the cleaning rewrote"): which of the two lines, never its text, that the reader of a plan's state may now report a conflict for this task, and "Merge as it stands?". Least machinery: one item in the existing list, no new variant row |
| `task-cycle/record_template.md` (`Task relation:` line) | the cleaning leaves it as it is unless the check of private paths lists it |
| `foundations/decisions.md` WAY-308 | binding paragraph (3 sentences): the two lines stay as they are unless the check of WAY-309 lists them, and a listed line is cleaned like any other; *Verification* complies/violates: kept as they were when not listed, cleaned when listed with the request telling the human, not rewritten when not listed, a cleaned relation line left out of the request; *Rationale*: the reader's lines stay unless listed, a listed one is cleaned and the reader may report a conflict that the request shows; *price taken*: that consequence added. The lines I rewrote are wrapped at 100 columns, also the first lines of the rationale (finding N4 of the review of my fix) |
| `foundations/decisions.md` WAY-309 | no change: it did not repeat the exception (searched) |
| `project-level/test_plan_state.py` | only the comment of `test_task_relation_naming_the_plan_by_a_description_conflicts_when_the_copy_is_linked` (it said the cycle's rule leaves the line to the human); the test itself is unchanged and still passes |

## Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | 187 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 271 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py` on `task-cycle/skill`, `task-cycle/record_template.md`, `foundations/decisions.md` | 0 each | 0 listed |

Not run: the full gate (the orchestrator's); `skill_entry_points.py` (no skill description changed).

## Own-work check

Requirement most likely unmet: no file still says a listed line is committed or left to the human.
Search (repository outside `.runs/` and `docs/`):
`grep -rn -i "commit the copy with that line\|may not rewrite\|do not rewrite it\|draft for another reason\|stay unchanged\|line as it is"` over `*.md` and `*.py`. Result: the only hits are
the record template line (now "unless the check of private paths lists it"), the original text of
the row "A draft for another reason" (no relation example any more) and an unrelated sentence of
`project-level/definition_template.md`. A second search for `Task relation` and `Project relation`
over all `*.md` and `*.py` found them only in the places above, the reader and its tests, the task
template and `plan_member.md` (none states an exception). WAY-308 and the SKILL section now agree in
words: unless listed, stays; listed, cleaned; the human is told through item 12.

Weakest point: item 12 has no check that the orchestrator writes it (like the other items, it rests on
the cycle's care); and the item names a reader loss the human can see only if the cycle writes it.

## Choices (with the way rejected)

- Item 12 as an entry in the list of items of *For you to decide*, not a new variant row: the file's
  form for conditions that add one item (items 10, 11). Rejected: a variant row (more machinery, and
  the state of the request does not change).
- WAY-309 left alone; the exception was only in WAY-308 (and the SKILL, template). Rejected: touching
  WAY-309 for symmetry.

## Searches not found or unclear

- none.
