# Author report: posix-class-not-a-link (the whole change as the one author)

**Status:** done
**Commit:** `8fa6bac` on `task/posix-class-not-a-link` (base `e1726b7`); one commit, explicit paths.
**Worktree:** `the root of the task's worktree`

## Files changed

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` (WAY-323, in place) | 26 | 10 |
| `task-cycle/private_paths_check.py` | 14 | 7 |
| `task-cycle/test_private_paths_check.py` | 29 | 0 |
| `task-cycle/test_tracked_private_paths_check.py` | 9 | 0 |

Not changed: `foundations/part_map.md` (the `task-cycle` part covers `task-cycle/**`, no file is new and no
entry stops matching), `foundations/invariants.md` (the sentence of `tracked-file-private-paths` already says
"a note link as WAY-309 and WAY-323 name them"; its *Derives from* still holds), `task-cycle/skill/*`
and `installation/README.md` (they describe what the check is asked for, not the class; nothing they say is contradicted).

## Foundation step: row 1 of *Settlements to record*

Entry: WAY-323 (`foundations/decisions.md`), edited in place per WAY-07 and the decision skill
(`.claude/skills/the-way-record-decision/SKILL.md`, `elements/decisions/skill/*`, `elements/decisions/template.md`).

- Binding sentence (row 1, English): the note-link rule takes no `[ [:name:] ]` for a link when name is one of the
  twelve POSIX classes (`alnum` … `xdigit`), and every other `[[...]]` with a letter or digit stays listed.
- Meaning (row 1, Polish): kontrola nie zgłasza `[ [:nazwa:] ]` jako linku do notatki, gdy nazwa to jedna z dwunastu
  klas znaków POSIX; każdy inny tekst `[[...]]` z literą lub cyfrą dalej jest zgłaszany.
- *Verification*: complies/violates examples extended. *Rationale*: one measurement sentence (2026-11-11, twelve texts)
  and the price taken. *Rejected*: the two not-chosen ways from pytania 1 and 2 of the task, each with its cost
  (every `[[:...:]]` — a note titled between colons passes; every `[[` followed by a parenthesis or another mark —
  cuts real links; exception only in the tracked-files check — two rule sets). Existing *Rejected* kept.
- Search of the whole foundation (WAY-33): `[[:` and the class appear in no entry except WAY-323; WAY-309, WAY-320,
  WAY-324, the invariant and `installation/README.md` describe the rule without contradicting the exception.
  Glossary: no entry for note link or character class (grep, none).
- The form check (`python -B elements/common/foundation_check.py --skip-test-citations`) reports 0 errors.
- Before the edit, the old script lists the class in the entry's own text (3 hits); after, 0 — so the decision text
  itself needed the change to be checkable.

## Checks (command, exit code)

Before the code change (test-first):

1. `python -B gate/run_tests.py task-cycle` — exit 0, 257 tests OK (baseline, before any edit).
2. `python -B -m unittest task-cycle.test_private_paths_check` — exit 1, FAILED (failures=3) on the new class tests;
   `test_a_class_in_a_line_of_a_shell_command_is_no_link`, `test_each_of_the_twelve_classes_in_double_brackets_is_no_link`,
   `test_a_real_link_and_a_path_on_a_line_with_a_class_are_still_listed`. The caret test passed trivially
   (`[^[:space:]]` holds no `[[`), as expected.
3. `python -B task-cycle/test_tracked_private_paths_check.py CommandTest.test_a_character_class_of_the_shell_in_a_markdown_file_is_no_note_link`
   — exit 1, AssertionError: `a.md:1: note link: [[:space:]]` listed where only the real link belongs.

After the code change:

4. `python -B task-cycle/test_private_paths_check.py` — exit 0, 51 tests OK.
5. `python -B task-cycle/test_tracked_private_paths_check.py` — exit 0, 20 tests OK.
6. `python -B task-cycle/test_tracked_files_private_paths.py` — exit 0, 1 test OK (the invariant's test).
7. Invariant seen failing once: appended `Probe: [ [Probe note] ]` to `installation/README.md`, then
   `python -B task-cycle/test_tracked_files_private_paths.py` — exit 1, listed `installation/README.md:233: note link: [ [Probe note] ]`;
   restored with `git checkout -- installation/README.md`, rerun of the same command — exit 0, OK.
8. Old vs new script on a probe file holding `[[:space:]]`, `[ [Notatka] ]`, `[ [:other:] ]`:
   `git show HEAD:task-cycle/private_paths_check.py` (saved to scratchpad) — exit 1, lists all three;
   new `python -B task-cycle/private_paths_check.py <probe>` — exit 1, lists `[ [Notatka] ]` and `[ [:other:] ]` only.
9. Old vs new on `foundations/decisions.md`: old lists 3 (the class texts of the entry), new lists 0.
10. `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` — exit 0, `checked: 275 files, 0 listed`.
11. `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`.
12. `python -B elements/common/foundation_check.py` (without the switch) — exit 0, `0 errors`.
13. `python -B -m unittest discover -s elements/common -p "test_foundation_check.py"` — exit 0, OK (not in task-cycle; run because the decision's form check is its code; I did not change it).
14. `python -B gate/run_tests.py task-cycle` — exit 0, 263 tests OK (257 + 6 new).

Not run: the full gate `python -B gate/run_tests.py` (not asked for; per the handoff). `gate/` unchanged, so its
discover run was not needed.

## Own-work check (section 3)

- Requirement most likely missed: the exception must hold in every check that looks for a link, the cycle-record copy
  and the request description included, not only in the tracked-files check; and a real link or a path on the same line
  with a class must stay listed.
- Check: a scratch record directory (`cycle.md` with `[[:space:]]` only; `reports/01-report.md` with `[ [Notatka] ]`,
  `[[:alpha:]]` and `a made-up drive path to a file `a.md``), run as
  `python -B task-cycle/private_paths_check.py <dir>` — exit 1, lists `[ [Notatka] ]` and the path, does not list
  `[[:alpha:]]`, `checked: 2 files, 2 listed`. The same run on `cycle.md` alone — exit 0, `checked: 1 files, 0 listed`.
- Showed: holds. The unit tests cover the same from the function level; this check is the command level.

## Choices made (way rejected, cost if wrong)

- Exception covers exactly the twelve names, not any `[[:...:]]`: rejected (per pytania 1 — a note titled `:name:`
  between colons would pass); cost if wrong: a note with such a title is missed. Case-sensitive: `[ [:Space:] ]` stays listed
  (my choice; cost if wrong: none seen).
- `[ [:alpha] ]` (no closing colon) is not exempt and stays a link (my choice, follows "exact form only"; cost if wrong:
  a false hit on a rare text).
- Exception placed in the shared `NOTE_LINK` pattern via a negative lookahead, not in the tracked-files check
  (per pytanie 2). Cost if wrong: two rule sets to keep.
- In WAY-323 the class clause went into the first binding sentence, so the entry keeps two sentences
  (binding sentences limit is three).

## Adaptations of section 4

None (whole change, no slice).

## Changed invariant test

None. `tracked-file-private-paths` and its test are unchanged; the test was run, seen failing on a probe, restored, and rerun.

## Each reach beyond the dispatch (section 1)

- Read whole: `foundations/decisions.md` WAY-308, WAY-07, WAY-328 (read to know the departure; no guideline read, per the
  handoff); WAY-320 and WAY-324 (as neighbours that use the check's rules); the decision skill
  `.claude/skills/the-way-record-decision/SKILL.md`, `elements/decisions/skill/{SKILL.md,read.md,decide_entry.md}`,
  `elements/decisions/template.md`, `elements/decisions/examples.md`, `elements/common/way_of_working.md`,
  `elements/common/rules.md`, `agent-instructions/README.md` ("Make the change", "Check the change").
  Why: the handoff names the foundation step's skill and the pinned rules for a decision edit.
- Read in part: `foundations/part_map.md` lines 88–100 and 208–218 (the `task-cycle` part and the command entry); `foundations/invariants.md` lines 84–95 (the invariant entry only).
- Searched only (grep, not read): `installation/README.md` lines 79–117, `task-cycle/skill/SKILL.md` and
  `task-cycle/skill/request_template.md` lines naming note links, `foundations/glossary.md` (no match).
  Why: to confirm the rule's prose elsewhere is not contradicted.
- Not read: `project-level/technology/reserved_choices.md` (section 5 asks for it where a change needs a language,
  library or store the task does not settle; this change uses the existing Python standard-library code, so nothing
  of that kind is needed). `elements/common/projected_mode.md` and `elements/decisions/skill/projected.md` (not projected mode).

## Unread material

- `foundations/part_map.md` (other parts), `foundations/invariants.md` (other invariants), `foundations/environment_facts.md`: not read; not named by the dispatch and not touched by the change.
- `task-cycle/change/ui_check.md`, `slice.md`, `fix.md`: not needed (no screen, not a slice, not a fix).
- `installation/README.md`, `task-cycle/skill/*`: grep only (see above).
- Of the dispatch's named files: `task-cycle/private_paths_check.py`, both test files, `tracked_private_paths_check.py`,
  `test_tracked_files_private_paths.py`, `task.md`, WAY-323, WAY-324, WAY-309, WAY-308, WAY-328, WAY-07, the invariant — all read whole, except WAY-324 and WAY-320, which I read to their end in two reads; no gap.

## Searches not found or unclear

- How the gate calls `foundation_check.py`: the handoff says "see how the gate calls it". `grep` for `foundation_check` in `gate/` finds no call; the form check is run by its own tests (`elements/common/test_foundation_check.py`) and by the decision skill's command. I did not find the gate's call and did not dig further; the gate was not run.
- The first read of `task-cycle/change/SKILL.md` used a relative path from the reports directory; I re-read it by its absolute path from the worktree root, and the text matches the one that was read. Recorded because the first path resolved without an error and I did not establish why.
- No glossary entry for note link or character class (grep, none found).

## Problems observed

- None blocking. The class `[[:alpha:]]` as a note link in the decision text was a real finding of the old script on the decision's own text; resolved by the change.
