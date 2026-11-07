PASS a5ea36fb9dbc97336f9013d0d419ca0239f0dc51

# Review of the correction for the human's remark (range acbcb15..a5ea36f)

`git rev-parse HEAD` is `a5ea36fb9dbc97336f9013d0d419ca0239f0dc51`; one commit, `a5ea36f`. Method:
`task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` (correction: the human's remark in place of
a findings file). The remark (`reports/correction-handoff.md`, "The human's remark (binds)"): drop the
exception for a listed relation line; clean such a line like any other so nothing the check lists is
published; the lines stay as they are when the check does not list them; a cleaned relation line can
make the plan reader report a conflict, which is a known and visible consequence. Counts: blocking 0,
Minor 0 new, out of scope 0.

## The remark, made or not

Made. Each point of the remark, with its evidence:

1. A listed `Task relation:` or `Project relation:` line is cleaned like any other.
   - `task-cycle/skill/SKILL.md` step 4 (exit-1 paragraph): "No listing is left in place, a `Task relation:`
     or `Project relation:` line included"; the sentence that committed the listed line is gone
     (`git diff acbcb15..a5ea36f -- task-cycle/skill/SKILL.md`).
   - Step 3 bullet: the two lines "stay as they are unless the check of step 4 lists them"; a listed one
     "is cleaned like any other, and the reader may then report a conflict with exit 1 for this task,
     which the human sees in the request (step 4)".
2. Nothing the check lists is committed: the loop "until it exits 0" in steps 4 and 5 now holds without an
   exception; step 6 (records the exit code) is consistent.
3. The lines stay as they are when not listed: step 3, `task-cycle/record_template.md` (`Task relation:`:
   "leaves this line as it is unless the check of private paths lists it"), WAY-308.
4. The conflict is stated as a known, visible consequence: SKILL.md step 3, WAY-308 *Rationale* and "price
   taken", and `task-cycle/skill/request_template.md` item 12 ("A relation line the cleaning rewrote":
   which of the two lines, never its text; that the reader of a project plan's state may now report a
   conflict for this task; "Merge as it stands?"). Item 12 sits in the list of items of *For you to decide*
   after item 11, in the file's form for conditions that add one item (as items 10 and 11), with no new
   variant row. Nothing in `task-cycle/request_check.py` or its test counts or names the items (grep for
   item counts found none).
5. The row "A draft for another reason" of `request_template.md` is back to its original text (the
   listed-line example and its *Checks* detail removed).

## N1 gone in every file and entry

Searched the repository outside `.runs/` and `docs/` for `Task relation`, `Project relation` and the
words of the exception (`may not rewrite`, `do not rewrite`, `with that line as it is`, `leaves that
line`, `to the human`). The relation lines occur in `foundations/decisions.md` (WAY-308 only),
`task-cycle/record_template.md:7`, `task-cycle/skill/SKILL.md:526,550`,
`task-cycle/skill/request_template.md:221-222`, the reader and its tests, the task template and
`plan_member.md` and `foundation-review/with_the_human.md` (the last four state no exception). No file
says a listed line is committed or left to the human. WAY-309 never held the exception and its binding
sentence ("corrects what it lists until it lists nothing") and violates line ("stops after a run that
listed something") now agree with SKILL.md and WAY-308 with no edit.

## Agreement of the five texts

SKILL.md (steps 3, 4), `request_template.md` (item 12, the draft row), `record_template.md` (line 7),
WAY-308 (binding paragraph, *Verification* complies and violates, *Rationale*, price taken) and WAY-309
say the same: unless listed, the two lines stay; listed, cleaned like any other; the request tells the
human. WAY-308 *Verification* violates adds "a relation line the check lists" to the committed path
cases and "a cleaned relation line is left out of what the request tells the human", matching item 12.
The listed-line draft is no longer a draft by that cause; the request keeps whatever state its other
causes give, as the remark's "least machinery" asked.

## What else changed, and whether it broke anything

- `project-level/test_plan_state.py`: only the comment of
  `test_task_relation_naming_the_plan_by_a_description_conflicts_when_the_copy_is_linked`; the test body
  and assertions are unchanged (conflict, "human reconciliation required", exit 1), and the comment now
  matches the rule. `plan_state.py` and the invariants are unchanged (not in `git diff --stat`).
- The edited paragraphs of WAY-308 are wrapped within the file's 100 columns (lines over 100 in the range
  are only the pre-existing *Rejected* sentence and the entry's heading). This closes Minor N4 of the
  earlier review for the lines edited; N2 and N3 were left as the human's decision.
- WAY-308's *Rejected* and *Scope* are unchanged; the changed entry still carries the task's *Not chosen*
  material and the earlier finding-1 wording (the reader's `Task source:` loss). Items 1-8 of the earlier
  findings are unaffected.

## Checks I ran (focused only)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `a5ea36fb9dbc97336f9013d0d419ca0239f0dc51` |
| `git diff --stat acbcb15..a5ea36f` | 0 | 5 files, 52 insertions, 38 deletions |
| `python -B gate/run_tests.py task-cycle` | 0 | 187 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 271 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py task-cycle/skill` | 0 | 10 files, 0 listed |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 | 0 listed |
| searches above (Grep/grep over `*.md` and `*.py` outside `.runs/` and `docs/`) | 0 | no remaining exception |

Not run: the full gate (the orchestrator's).

## Declined to judge

- Whether a request that carries item 12 should also change state (draft or blocked): the remark and the
  handoff ask for the least machinery, an item and no variant.
- Minor N2 and N3 of the review of the fix: left by the human's decision.

## Reach beyond the dispatch

None beyond the diff, `request_template.md` lines 160-225 (the form of the item list) and the grep above.

## Searches not found or unclear

- none.
