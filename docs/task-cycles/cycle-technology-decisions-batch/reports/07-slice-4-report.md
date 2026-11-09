# Slice 4 report — The remarks script reads reports by name

**Status:** done

**Commit:** `491f048` — "Read the remarks check's reports as the .md files whose name holds neither handoff nor findings, in WAY-294" (on `task/cycle-technology-decisions-batch`, on top of `8b5662d`).

## Files changed

| File | Added | Removed |
|---|---|---|
| `task-cycle/remarks_check.py` | 13 | 4 |
| `task-cycle/test_remarks_check.py` | 23 | 2 |
| `task-cycle/skill/SKILL.md` | 5 | 4 |

Committed by path (`git add` of the three files). No `git add -A`; no other file touched.

## What changed

- `task-cycle/remarks_check.py`
  - Module docstring, reports sentence: now the words item 8 gives ("The reports are the `.md` files of `reports/` whose name holds neither `handoff` nor `findings`, read in the order of their names; a handoff, a findings file and a log are not read.").
  - Module docstring, items sentence: now "its paragraphs, a paragraph after a list included, so that nothing written in the section goes unread; a sub-heading is no item." The code already read a paragraph after a list as an item (`split_items`, the `blank and indent <= base` branch), so the docstring now says what the code does.
  - New helper `is_report(path)`: a file that is a `.md` file (case-sensitive `endswith`), whose name has no `handoff` and no `findings` (case-sensitive substring), and `is_file()`.
  - `check()`: `reports_dir.glob("*report.md")` replaced by `reports_dir.glob("*.md")` filtered with `is_report`; sorting by name unchanged. Exit codes unchanged.
- `task-cycle/test_remarks_check.py`
  - `test_only_files_whose_name_ends_in_report_are_read`: the fixture now names `handoff_author.md`, `notes.txt`, `gate.log`, `slice-1-findings.md`, `01-author-handoff.md` and `02-report.md.bak` as not read, with `01-report.md` of `none` (exit 0 expected).
  - New `test_every_md_file_whose_name_holds_neither_handoff_nor_findings_is_read`: `review_whole.md` and `report-planner.md` are read (listed in name order); `01-author-handoff.md`, `handoff_author.md`, `slice-1-findings.md`, `notes.txt`, `gate.log` are not.
  - New `test_a_paragraph_after_a_list_is_an_item_of_its_own` in `SectionFormsTest`: a list of `one`, `two`, then the paragraph "A paragraph after the list." gives three items. No test pinned this before.
- `task-cycle/skill/SKILL.md`
  - Line 144 (the sentence "Write each dispatch's full handoff to a file in `reports/`"): now "… to a file in `reports/` whose name holds `handoff`; …", reflowed.
  - Line 478 ("The process remarks check", the sentence that says which reports the script reads): now adds "a file whose name holds neither `handoff` nor `findings`," after the `reports/` phrase, reflowed.

## Checks

Commands run from the worktree root, with exit codes:

1. Test first (before the code change): `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` — **exit 1**. One failure: `test_every_md_file_whose_name_holds_neither_handoff_nor_findings_is_read`, `AssertionError: 0 != 1` (the script listed nothing because `review_whole.md` was not read). The new paragraph test passed on the unchanged code, as expected for a behaviour already in place.
2. After the change: `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` — **exit 0**, 47 tests, OK.
3. `python -B gate/run_tests.py task-cycle` — **exit 0**, 211 tests, OK.
4. `python -B elements/common/foundation_check.py --skip-test-citations` — **exit 0**, "0 errors".
5. `git diff --check` — **exit 0**, no output.

Own-work check (section 3 of make-change): the requirement is that the new glob reads the same reports on the real cycle record as the old pattern did, and that no handoff or findings file is read. Run: `python -B task-cycle/remarks_check.py .runs/task-cycles/cycle-technology-decisions-batch` — **exit 1**, `checked: 6 reports, 18 items other than none, 18 not in the process remarks`. The six reports are the six `*report.md` files of that `reports/` directory (`01-planner-report.md`, `02-foundation-entries-report.md`, `03-slice-1-report.md`, `04-slice-2-report.md`, `05-slice-3-report.md`, `06-slice-3-review-report.md`); the handoffs and `07-slice-4-handoff.md` are not read. The exit 1 is expected: the 18 items are not yet appended to the record's process remarks, which is the orchestrator's step before the record is committed (WAY-294). I did not run the pre-change script on that record for comparison; the equality of the six is shown by the listing, not by an old-version run.

Not run: the full suite `python -B gate/run_tests.py` (the handoff and the method forbid it here).

## Reaches beyond the handoff

- `task-cycle/change/SKILL.md` read whole; `task-cycle/change/slice.md` read whole (the method sends a slice there).
- `agent-instructions/README.md` read whole.
- `.runs/task-cycles/cycle-technology-decisions-batch/plan.md`: its *Foundation entries* table and the slice 4 section, to confirm the change list and the dependency on Slice 1 (already on the branch, commit `932726d` and the four before it).
- `task-cycle/remarks_check.py` read whole; `task-cycle/test_remarks_check.py` read at its helpers (lines 1–50, 238–280) and at the target tests.
- `task-cycle/record_template.md:174-196` (Request handoff) and `foundations/invariants.md:86-94` (tracked-file-private-paths), read as the handoff names them. The test `test_tracked_files_private_paths.py` lies in `task-cycle`, and the `task-cycle` run covers it (exit 0). No change to either file was needed.
- `foundations/decisions.md`, WAY-294 to WAY-296, read in their current text (WAY-294 found by its heading, not by the handoff's line range). WAY-294 already states row 5's rule (commit `932726d`, from the earlier cycle). No foundation edit was needed in this slice.
- WAY-322 (row 1) was not read; this slice does not depend on it.

## Choices made

- **Filter `is_file()` added to the rule.** Rejected: letting a directory whose name ends in `.md` through the glob, which would make `read_text` raise and exit 2 on a directory the rule never meant to read. Cost if wrong: a directory named `x.md` inside `reports/` is skipped silently instead of read; no such directory exists in any cycle record, so the cost is low.
- **The "handoff" sentence edited at line 144, not at 137–138.** The sentence at 137–138 ("Keep each full handoff and report beside it in `reports/`") also mentions where a handoff stands, but does not say what its file's name holds. I edited the sentence that says a dispatch's handoff is written to a file in `reports/` (line 144), which is the sentence the task item describes as saying where a stage's handoff stands. Cost if wrong: a reader of 137–138 alone would not learn the naming rule; it is stated at 144 in the same section.
- **Paragraph-after-list test added** as a new test, though it passes on the old code. It pins existing behaviour that the docstring now states, as the handoff asked.
- The docstring's items paragraph now has a short final line ("in the section goes unread; a sub-heading is no item. An item"), which is a wrapping artefact, not a wording change.

## Drift (places found by content)

| Cited | Found at (before this slice) |
|---|---|
| `remarks_check.py:12-13` | 12–14 (reports sentence) |
| `remarks_check.py:26-27` | 26–27 (items sentence) |
| `remarks_check.py:318` | 318 (the `reports/*report.md` glob) |
| `test_remarks_check.py:362` | 362 (test name) |
| `skill/SKILL.md:140` | 144 (handoff sentence) |
| `skill/SKILL.md:474` | 478 (remarks check sentence) |
| `decisions.md:9235-9274` (plan) / `9285-9336` (handoff) for WAY-294 | heading found by content; line numbers not checked against the handoff's current range |

## Searches not found or unclear

- Foundation WAY-294's current text against the handoff's range `decisions.md:9285-9336`: found by heading; the exact line range I did not verify. Not relevant to the change, which edits no foundation entry.
- `task-cycle/skill/SKILL.md:140` as cited by the task item: no sentence there says the handoff's file name holds `handoff`; the nearest sentence is at 144, which I edited (see Choices).
- Whether the "a log" of the docstring sentence means only `gate.log`-type files: unclear; it is covered by the `.md` rule anyway (every log is non-`.md`), so the sentence stays as the task words it.
- None else found.
