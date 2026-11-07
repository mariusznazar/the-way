# Fix report — review of the whole change (reviewed head b6d93e8)

**Status:** done

Commits of the fix (range from `b6d93e8`): `d745246` (script, its tests, reader tests) and `4deb195`
(rules, templates, decisions). Worktree clean. Nothing pushed.

## Findings, one by one

**1. Blocking — the cleaned copy cannot be anchored by the plan-state reader, and WAY-308 said it
could. Fixed by the orchestrator's ruling (way c), without a change of `plan_state.py`.**
- `foundations/decisions.md` WAY-308 *Rationale*: now says three readers go on as before (the human by
  the link, the plan's link to the task's document, the nightly review) and the reader of a plan's state
  reads the copy with one loss: it ties the record to the plan's task by `Task relation:` and
  `Project relation:`, which stay, but until the plan row's document link names the frozen copy it anchors by
  the absolute path of `Task source:`, which the cleaning replaces; for a plan task it reports the copy
  as unchecked and proposes no move to done, fails closed, until a human links the frozen copy; a task
  of no plan is not read this way. The loss is also in the "price taken". The binding sentence, the
  *Verification* lines and the *Scope* name the `Task relation:` line too (see 1b).
- `task-cycle/record_template.md` (`Task source:`): says the committed copy is cleaned and that for a
  plan item the reader cannot anchor the copy until the row's *Document* links the frozen copy.
- `task-cycle/skill/SKILL.md` section "The record before it is committed", step 3: a bullet for
  `Task source:` says the same cost, and that an independent task is not touched.
- Tests that pin the reader's output on a cleaned copy, in `project-level/test_plan_state.py` (the
  reader's own test class; helper `archive_cleaned`):
  - `test_cleaned_copy_of_an_unfinished_plan_item_is_unchecked_until_the_copy_is_linked`: state
    `in cycle`, archived merged copy with `Task source:` "the task document in the author's backlog",
    *Document* still the task file. Asserts `unchecked 1 reports:`, `original Task source or Document
    cannot be anchored`, no ` -> done`, no `conflict`.
  - `test_cleaned_copy_anchors_a_done_task_once_the_document_links_the_frozen_copy`: state `done`,
    *Document* links the frozen copy: asserts the line `cycle record docs/task-cycles/reports/record.md
    commit <sha>` is printed, no `unchecked 1 reports:`, no `conflict`.
  - Mutation seen: with the absolute path restored in the first test, the reader proposes
    `in cycle -> done` and the test fails (AssertionError on `unchecked 1 reports:`); file restored from
    a copy, tests pass again.
- Not done, as ruled: `plan_state.py` and the invariant `project-plan-state-evidence` are unchanged.

**1b. The `Task relation:` form of the same finding.** The cleaning rule now leaves `Task relation:`
(record) and `Project relation:` (task copy) as they are (SKILL.md step 3, record template, WAY-308
binding sentence and examples). Third test pins why:
`test_task_relation_naming_the_plan_by_a_description_conflicts_when_the_copy_is_linked`: a cleaned
expanded relation (plan given by a description) with *Document* linking the copy gives `conflict 1
reports:`, `human reconciliation required`, exit 1, no proposal.
If the script lists either line: SKILL.md step 4 says do not rewrite it, commit the copy with that line
as it is and put it to the human by the existing row "A draft for another reason" of
`request_template.md` (first line `**State: draft**`; the row now gives this reason as an example, the
item naming the file and line and never the text, *Checks* naming the check, exit code and listed
line by file and line). No new variant. The orchestrator wrote "draft marked blocked"; the existing
row gives a plain draft with "Merge as it stands?", and I kept the row's state (the cycle needs nothing
to go on that the human's merge decision does not give) — change the row's first-line text if you want
`blocked`.

**2. WAY-294 against step 5.** WAY-309 gained a third binding sentence ("The check of WAY-294 runs once
more on the cleaned copy, and there an item it lists is made to read the same in the report and in the
remarks, not appended again"), `Relations: derives from WAY-308 · narrows WAY-294` (WAY-25: the one that
prevails names the other and states the area), a complies and a violates line in *Verification*.
`foundation_check.py` exit 0 (it accepts the narrowing). SKILL.md step 5 points to WAY-309.

**3. Scope.** `project-level` added to the *Scope* of WAY-308 and WAY-309.

**4. Checks line for the copy's run.** SKILL.md step 12 and `request_template.md` (step 5 of "Write,
check, publish"): the edit that adds the record's link also fills in *Checks* with the runs of the two
checks on the copy.

**5. `record_template.md` Verification paragraph** (the "At the request, copy that whole directory"
sentence): now says the copy is cleaned and checked as the section gives.

**6. Path with spaces / real directory name in a test.** Test sample renamed to a made-up path on a drive, with a space in a directory name
(expects the path up to the space). Rule: SKILL.md step 4 and `request_template.md` step 4 say replace the whole
path, to the end of the phrase that names it, not the printed part. Choice: I did not make the script
print more (printing to the end of the line would show unrelated words and still guess the end); the
script's docstring says a path with a space is shown to the space and the rest is still the path.

**7. Files not read (UTF-16 / binary).** Two changes, both tested: (a) the script reads a file that
starts with a UTF-16 byte order mark (what PowerShell 5.1 writes) as UTF-16 instead of skipping it
(`test_a_utf16_file_with_a_byte_order_mark_is_read`; mutation of either line is caught); (b) SKILL.md
step 4 says a counted-unread text file is read by hand or saved as UTF-8 and checked again, an image
needs no reading. I did not make the script exit 1 on a count of files not read: a record may legitimately hold a
screenshot, and exit 1 would then never clear. Cost if wrong: a UTF-16 file without a byte order mark
still passes as "binary" (counted in the last line).

**8. Edges.** a web address with a drive-like segment is no longer listed (the drive lookbehind excludes a letter after a
slash) and file addresses that name a drive, a Linux home directory, a macOS home directory or a WSL drive are
listed (`(?<=file://)` alternatives); tests `test_a_path_in_a_file_url_is_listed` and the added URL
case in `test_a_letter_that_ends_a_word_starts_no_drive`. Mutations of each lookbehind are caught (6
mutations, each 1 failure). Left as documented: an array index with two brackets is listed, `~` and
`%USERPROFILE%` paths and UNC paths are not.

## Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | 187 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 271 tests OK (268 + the 3 new) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B -m unittest project-level/test_plan_state.py -k cleaned -k description_conflicts` | 0 | 3 tests OK |
| same, with the cleaned source replaced by the absolute path (mutation) | 1 | first test failed as expected, then restored: exit 0 |
| `python -B task-cycle/private_paths_check.py` on `task-cycle/skill`, `task-cycle/record_template.md`, `foundations/decisions.md`, `agent-instructions/README.md`, `project-level/test_plan_state.py` | 0 each | 0 listed |

Not run: the full gate. `skill_entry_points.py`: no skill description changed.

## Own-work check

Requirement most likely not met: "WAY-308 must stop saying what does not hold" and the three claims of
the rules (record template, SKILL step 3, the decision) agree with what the reader does. Check: the
reader's actual output on a cleaned copy, in the two states (tests 1 and 2 above, output spelled out)
and the mutation that shows test 1 fails when the path stays. Result: the claim in all three places is
exactly what tests 1 and 2 assert (unchecked, no done proposal before the link; anchored after it).
Second check: the new rule for the `Task relation:` line against test 3, which shows a cleaned line
makes the reader report a conflict with exit 1.
Weakest point: the draft item for a listed relation line is stated through an existing row; no
cycle has run it yet. A listing of that line should not occur for a task that follows the template
(the form is the plan's file name), so the path is a rare one.

## Concerns (not in the decision, as ruled)

- A reader that anchors a copy whose `Task source:` is cleaned (for example by the plan row's document
  file name together with the frozen task's `Project relation:`) would remove the loss; that is a change
  of `plan_state.py` with its tests and is a task of its own. Until then, for a plan task the
  `in cycle -> done` proposal waits for a human to link the frozen copy.

## Reach beyond the handoff

`project-level/test_plan_state.py` (read in full, lines 1-200 and 555-end, to build the fixtures);
`project-level/plan_state.py` lines 228-330 (already read in the first pass). No other.

## Searches not found or unclear

- none.

## Problems as observed

- Tool layer: a heredoc literal with doubled backslashes or a Python escape reached the interpreter
  with one backslash twice more (a script aborted before writing; a test file got a literal line break
  in a string). Both found by the next run and redone through the edit tool. No effect on the commits.
