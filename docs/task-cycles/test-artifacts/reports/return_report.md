# Report of the return step — task cycle `test-artifacts`

## Status

`done`

## Commits

One commit from the reviewed head `ef0195e`: see `git log --oneline -1` ("Say in the image check's
docstring which files the private-paths check skips"); it changes `task-cycle/image_files_check.py`
only (a docstring). Worktree clean; nothing pushed.

## Foundation compared with code

Compared: decisions WAY-316, WAY-317, WAY-318, WAY-319, WAY-121, WAY-165, WAY-267, WAY-270; the
invariants `record-copy-image-check` and `record-copy-image-files`; the entries the task names
(WAY-219, WAY-286, WAY-308) and those the search found (WAY-287, WAY-309, WAY-166, WAY-33,
WAY-134); the part map entries `task-cycle`, `project-level`, `decisions`, `invariants`; against
`task-cycle/image_files_check.py`, `task-cycle/test_image_files_check.py`,
`task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`, `task-cycle/change/ui_check.md`,
`task-cycle/record_template.md`, `task-cycle/review/SKILL.md` and the technology documents.

- What matched, with the check:
  - The extension list of the invariant `record-copy-image-check` equals the script's
    `IMAGE_EXTENSIONS` and the list in its docstring (compared by a script, result `True True`);
    the script's exit codes (0, 1, 2) and the test's citations of the invariant agree with its sentence.
  - WAY-316, WAY-317 and WAY-318 agree with `request_template.md` (*What you will see*, item 13,
    *Checks*), `ui_check.md`, `record_template.md` and `review/SKILL.md`; the step order of
    "The record before it is committed" (steps 5 to 7) calls the script as WAY-316's verification
    asks. WAY-319 agrees with `ui_check.md` (browser closed after the check).
  - "Four matters": no repeat of "three matters" is left in the foundation or the technology
    documents (grep of the tracked `.md` files, last done in the fix).
  - Part map: the new files stand under `task-cycle/**`; the script and its test import only the
    standard library and each other, so no *Depends on* of `task-cycle` changes; no surface or trust
    boundary line applies. No part-map change.
  - WAY-287 lists what the section for the human's decisions holds without the new item 13 of the
    request template; the template's items 10 and 12 are also absent from that list, and WAY-317
    derives from WAY-287 and names the section, so I took the list as not exhaustive and changed
    nothing.
- What no longer matched, and its correction: one thing. The docstring of
  `task-cycle/image_files_check.py` said `private_paths_check.py` "counts an image there as a binary
  file it does not read"; an SVG is text and that script reads it. The docstring now says the
  private-paths check skips as binary a file with a NUL byte near its start, which most images have.
  No behaviour changed.
- Not acted on, as the handoff says: the reviewer's three notes of `reports/review2_report.md`
  (glossary definition against "four matters"; the `{merge-onto}` binding in the-way; the reviewer's
  report not saying that no place is settled). My comparison found no mismatch of its own beyond them.

## Entries written or changed

- Decisions written or changed: none.
- Invariants written or changed: none.
- Environment facts: none (no source outside the product beyond what the foundation holds).
- Glossary terms: none.
- Part-map changes: none.
- Projected entries written whole or in part: none (the task is independent).
- Rows of *Settlements to record* written: none in this step; rows 1 to 7 were written in the
  foundation step and the fix (WAY-316 rows 1 and 2, WAY-317 row 3, WAY-121 and WAY-165 row 4,
  WAY-318 row 5, WAY-319 row 6, `record-copy-image-check` and `record-copy-image-files` row 7).

## Checks (command and exit code)

- `python -B gate/run_tests.py task-cycle` -> exit 0, 200 tests OK (run after the docstring edit).
- `python -B elements/common/foundation_check.py` -> `0 errors`, exit 0.
- Not run: the full gate (the orchestrator's); the docstring edit changes no code path.

## Reaches beyond the handoff

- WAY-287 (whole), to judge whether item 13 of the request template stands outside it.
- `task-cycle/image_files_check.py` (the changed file, read whole) and the invariant sentence, to
  compare the extension lists.

## Searches not found or unclear

none
