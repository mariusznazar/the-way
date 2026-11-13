# Author report — review-structure-form-class

**Status:** done with concerns (the concerns are the items under "Searches not found or unclear" and the
choices below; none stops the change).

Worktree `the worktree's root`, branch
`task/review-structure-form-class`, base `65b6d7007ec4fffad998612e5c521eee93c7b8b5`, head `5353268`.

## Commits

| Commit | What |
|---|---|
| `c7a6733` | the rule of size in `product-guidelines/coding/` (template, settle, trial run, recognize, task document, hand back, skill), WAY-355, WAY-356 |
| `093b901` | `task-cycle/change_file_sizes.py` with `task-cycle/test_change_file_sizes.py`, `task-cycle/review/whole_change.md`, `task-cycle/review/SKILL.md` section 3, WAY-357, WAY-358, WAY-359 |
| `76b038c` | `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`, WAY-360 |
| `5353268` | WAY-229 (*Rationale*, *Rejected*) and WAY-164 (*Rejected*) edited in place, binding sentences and fields untouched |

The first commit of the script was undone with a soft reset and made again inside `093b901`, so that each commit
passes `elements/common/foundation_check.py` (the script's docstring cites WAY-357, which the log holds from `093b901`).

## Files changed (lines added / removed against the base)

- `foundations/decisions.md` +253 / -5
- `product-guidelines/coding/template.md` +33 / -2
- `product-guidelines/coding/settle.md` +37 / -2
- `product-guidelines/coding/trial_run.md` +7 / -0
- `product-guidelines/coding/recognize.md` +5 / -0
- `product-guidelines/coding/task_document.md` +7 / -1
- `product-guidelines/coding/hand_back.md` +4 / -1
- `product-guidelines/coding/SKILL.md` +4 / -4
- `task-cycle/review/SKILL.md` +8 / -0
- `task-cycle/review/whole_change.md` +22 / -0
- `task-cycle/plan/SKILL.md` +11 / -0
- `task-cycle/change/SKILL.md` +8 / -0
- `task-cycle/change_file_sizes.py` new, 252 lines
- `task-cycle/test_change_file_sizes.py` new, 230 lines (15 tests)

No skill description changed, so no entry point was rewritten. `task-cycle/**` already assigns both new files to the part
`task-cycle` in the part map, so the return step needs no map entry for them. No part was added, so the *Scope* of WAY-328
and WAY-344 stays as it is.

## Foundation entries: which row each holds, and the meaning in two languages

The numbers follow the order of the commits, not the order of the task's rows.

| Entry | Row | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-355 | row 3 | The coding template requires a rule of the size of a function and a file, with its own invariant and test outside the linter's set; a product sets thresholds after a trial run and exceptions in its decision, or departs by a decision with a reason; a product with guidelines gets it by an extension, and the invariant is marked violated while code stands over a threshold. | Szablon wytycznych kodowania wymaga reguły rozmiaru funkcji i pliku z własnym niezmiennikiem i testem poza zestawem lintera; produkt ustala progi po próbie na swoim kodzie, a wyjątki w decyzji, albo odstępuje decyzją z powodem; produkt z wytycznymi dostaje ją rozszerzeniem, a niezmiennik jest oznaczony jako naruszony, dopóki kod przekracza próg. |
| WAY-356 | row 4 | The test of the rule names every function and file over a threshold with its size, the reviewer of the whole change runs it on the state before the change and after it, and a product has no command of its own for sizes. | Test reguły wymienia każdą funkcję i plik ponad progiem z ich rozmiarem, recenzent całej zmiany uruchamia go na stanie sprzed zmiany i po niej, a produkt nie ma osobnego polecenia liczącego rozmiary. |
| WAY-357 | row 6 | The reviewer of the whole change judges what the change leaves in the structure of the code, with the lines of each changed file before and after (a script of the-way) and the test of the rule of size on both states. | Recenzent całej zmiany ocenia, co zmiana zostawia w strukturze kodu, z liczbami linii każdego zmienionego pliku przed zmianą i po niej (skrypt the way) oraz z testem reguły rozmiaru na obu stanach. |
| WAY-358 | row 1 | A finding about the structure of code below the product's threshold is Minor and its scope is judged as for any finding; a finding about code over the threshold is graded as any other. Narrows WAY-161. | Znalezisko o strukturze kodu poniżej progu produktu jest drobne, a zakres ocenia recenzent jak każdej uwagi; znalezisko o kodzie ponad progiem ma stopień jak każde inne. Zawęża WAY-161. |
| WAY-359 | row 2 | A finding that an entry departs from the form of its template, where its content agrees with the code, is Minor unless it cites a sentence a reader would read wrongly through the departure; a mismatch of content with the code stays Important. Narrows WAY-161. | Uwaga, że wpis odstępuje od formy szablonu przy treści zgodnej z kodem, jest drobna, chyba że wskazuje zdanie, które czytelnik przez to odstępstwo odczyta źle; rozjazd treści z kodem zostaje ważny. Zawęża WAY-161. |
| WAY-360 | row 5 | Where a slice adds to a function or a file over the threshold, the plan begins with a slice that moves a part out without a change of behaviour, written in the table of choices; the author without a plan makes that move the first commit that changes the code; no spec. | Gdy kawałek dopisuje do funkcji albo pliku ponad progiem, plan zaczyna od kawałka wydzielającego część bez zmiany zachowania, zapisanego w tabeli wyborów; autor bez planu robi to pierwszym commitem zmieniającym kod; bez specyfikacji. |
| WAY-229 | task item 7 (no row; the task's own item) | Binding sentences unchanged; *Rationale* holds the measurement of the reviewer's class with its conditions; *Rejected* holds the variant of two cheaper runs with its result. | Zdania wiążące bez zmiany; *Rationale* ma wynik pomiaru klasy recenzenta z warunkami; *Rejected* ma wariant dwóch przebiegów tańszej klasy z wynikiem. |
| WAY-164 | task item 8 (no row; the task's own item) | Binding sentences unchanged; *Rejected* holds the variant "a review without the author's report" with its result and a pointer to WAY-229 for the conditions. | Zdania wiążące bez zmiany; *Rejected* ma wariant „recenzja bez raportu autora” z wynikiem i odesłaniem do WAY-229 po warunki. |

Each of rows 1 to 6 is its own entry (six entries): each answers one question (WAY-19), and rows 1 and 2 each narrow
WAY-161 on their own, as WAY-297 does. None of the six is marked `the cycle's`; no row is already stated in the log, so no
row is tied to an older entry. *Origin* is `none` in all six, *Based on* is `none` in all six.

*Rejected* of each entry takes only what the task keeps: WAY-355 from question 4, WAY-356 from question 5, WAY-358 from
question 3, WAY-359 from question 2, WAY-360 from question 6. WAY-357 (row 6) has `unknown`: the task keeps no way not
chosen under row 6, and a way I derived must not enter (WAY-134).

## Checks (command, exit code)

- `python -B gate/run_tests.py task-cycle` — final run exit 0, 380 tests (the new script's 15 included). An earlier run
  exited 1: my own new test file had a syntax error from a mangled heredoc; fixed with the Edit tool and rerun.
- `python -B elements/common/foundation_check.py` — final exit 0, `0 errors`. A run in between exited 1 for
  `task-cycle/change_file_sizes.py:2: WAY-357 names no decision of the log`, before WAY-357 was written; resolved by the
  commit order above.
- `python -B task-cycle/private_paths_check.py <file>` — run once per changed file (14 files, it takes one file), each exit 0.
- `python -B agent-instructions/skill_entry_points.py` — exit 0, `entry points are current`.
- `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests, 5 skipped); `python -B gate/run_tests.py agent-instructions`
  — exit 0 (18 tests).
- Own-work check script (scratchpad, `own_check.py`) — exit 0, see below.
- Not run: the whole gate (`python -B gate/run_tests.py` without a directory), as the handoff says; no product tests and no
  mutation tool apply to the-way itself.

### Tests of the new script: failing runs

The tests were written after the script, not before it: the script's behaviour is a clear contract but I did not stage a
failing test first. In place, I broke the script on purpose six times and each break was caught, then restored it
(`cmp` against a copy):

- last line without a line feed not counted: `test_a_last_line_without_a_line_feed_counts_and_an_empty_file_has_none` fails;
- binary probe off: `test_a_binary_file_is_listed_and_adds_no_line_to_the_totals` fails;
- rename detection off (`--no-renames`): `test_a_renamed_file_is_measured_at_its_old_path_before_the_change` fails;
- the before side read from the after blob: seven tests fail;
- a submodule read as a blob: `test_a_submodule_is_listed_with_no_lines` fails;
- `-z` dropped: eight tests fail, among them the name with a space and a letter outside ASCII.

Each mutation was run as `python -B -m unittest discover -s task-cycle -p "test_change_file_sizes.py"`, exit 1 each time.
The unbroken run of the same command passes.

## The own-work check

- **Requirement most likely unmet:** items 7 and 8 — WAY-229 and WAY-164 change *Rationale* and *Rejected* only, binding
  sentences and fields stay as they are, and the numbers and conditions are copied from the task.
- **Check:** `own_check.py` in the scratchpad compares, between the base and the head, the binding paragraph and the fields
  (*Scope* to *Origin*) of each of the two entries, and looks for each number of the task's items 7 and 8 in the new text
  (959, 1740, 8 runs a variant, Sonnet 5.5, 4 of the 8, Opus 5.5, 1 of the 8, 5 of the 14, 5 and 6, three blocking flaws;
  4 and 3 of the 14, 5 and 6 with the report, 112.47 million, 90.20 million, the pointer to WAY-229).
- **Result:** exit 0. Binding and fields are identical for both entries; every number is present. (A crude test of whether
  the old *Rationale* and *Rejected* survive as one contiguous text said `False` for WAY-229 only because the new sentences
  stand in the middle; the diff of the file shows the old text kept and re-wrapped.)

## Reach beyond the handoff

- `product-guidelines/coding/recognize.md`, `task_document.md`, `hand_back.md` and `SKILL.md`, read whole and changed: the
  handoff names `settle.md`, `template.md`, `trial_run.md` and `starting_set.md`. They carry the refresh check, the *To do*
  and *Questions to settle* lists and the hand-back check of the rules on failures and logs; the extension route of row 3
  (WAY-278) does not work without the same lines for the rule of size.
- `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/decisions/skill/*.md`, `elements/decisions/examples.md`
  and WAY-03, WAY-254, read for the foundation step.
- `task-cycle/skill/SKILL.md` (lines 150-225, 340-420, the dispatch of the review of the whole change), `task-cycle/slice_size.py`
  and `task-cycle/test_slice_size.py`, `gate/run_tests.py` (head), `task-cycle/test_tracked_private_paths_check.py` (how its tests
  build a git repository), `product-guidelines/reading.md` (first 60 lines), `foundations/invariants.md` (the headings with
  *Part* `every`, `task-cycle`, and the sections `script-*`, `cross-part-imports`, `skill-entry-points`, `record-copy-*`).
- Outside the repository, as the user's instructions require before a script, a commit and a knowledge artifact:
  `.ai\rules\scripts.md`, `.ai\rules\knowledge_artifacts.md`, `.ai\rules\git.md`.

## Unread material

- WAY-229, WAY-164, WAY-161, WAY-297, WAY-263, WAY-51, WAY-135, WAY-16, WAY-271, WAY-278, WAY-168, WAY-173, WAY-203, WAY-05,
  WAY-27, WAY-328 and the 35 selected entries (WAY-07 to WAY-344 of the list): read whole.
- `foundations/part_map.md` and `foundations/glossary.md`: read whole.
- Invariants: I read the headings with their *Part* and, whole, only `script-language`, `script-imports`, `script-subprocesses`,
  `fingerprint-definition`, `skill-entry-points`, `instruction-file-imports`, `root-claude-md-import`,
  `installation-claude-guidance`, `project-plan-state-evidence`, `project-plan-state-subprocesses`, `cross-part-imports`,
  `record-copy-image-check`, `record-copy-image-files`. Read by heading and *Part* only: `foundation-file-kinds`,
  `foundation-change-merge-route`, `repository-file-location`, `element-directory-contents`, `return-step-record`,
  `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`, `skill-rule-source`,
  `map-reference-target`, `test-method-citation`. `foundation_check.py` passed, and none of these concerns files I changed beyond
  what the check covers.
- `product-guidelines/reading.md`: first 60 lines only (the handoff says the-way has no guidelines of its own, and I changed nothing there).
- The critique skill was not read: the entries of a change are no set of proposals for collective review (way_of_working.md).

## Searches not found or unclear

- The conditions of the measurement of the form of an entry (9 blocking, 8 Minor, 6 of 32 runs) are not in the task. WAY-359
  states the counts and says "an experiment with reviewers"; I did not say the experiment is the one of WAY-229, since the task
  does not say so. WAY-05 asks for the conditions of a measurement; these stay missing.
- The task's "below the threshold" (rows 1, item 4): a finding of structure that is not about size at all (code with no user,
  a name no longer true) has no size to compare. WAY-358 reads it as "below the threshold", so such a finding is Minor; a
  product with no rule of size (a departure) has no threshold and the entry says nothing for it, so a finding there is graded
  as any other by default. Nothing settles that in the task.
- WAY-05 and the decisions template ask for an environment fact in *Based on* where a citation is a finding about agents or
  models "once the environment facts element has entries"; the task says the measurement stands in *Rationale* and *Origin* is
  `none`. I followed the task and left *Based on* `none`.
- "Błędy wzorcowe" is written "reference errors" in WAY-229 and WAY-164; the task does not say what the 14 are or over which
  changes the 5 and 6, the 4 and 3 were counted. I copied the numbers and no more.
- Whether "the first commit" of the author without a plan (task item 5) comes before or after the commits of its foundation
  entries: I read it as the first commit that changes the code, and wrote it so in WAY-360 and `task-cycle/change/SKILL.md`.
- Who runs the new script: the handoff says the reviewer. `whole_change.md` says so; WAY-357 does not name who runs the script.
- When a rule's invariant is marked violated its test stands marked as an expected failure (WAY-51), which can hide the
  test's message. I added to `whole_change.md` that the reviewer takes the mark off in its own separate worktrees. This is
  mine, not the task's.

## Choices (each with the way not taken)

1. **Command line and output of the script.** `python -B task-cycle/change_file_sizes.py BASE HEAD [--root DIR]`; a Markdown table
   (file, lines before, lines after, change, note) and one line `Summary: ...`; exit 0, or 2 with one `Error:` line
   (no repository, no directory, no commit, git not startable, git's answer unreadable). Git is called with argument lists,
   never a shell, with `git diff --raw -z -M` for names and modes and one `git cat-file --batch` for contents by blob id.
   Not taken: one `A..B` argument (an extra parse for no gain); a plan-style input as `slice_size.py` has (the reviewer has a
   range, not a plan); `git diff --numstat` (it gives added and removed lines, not the totals before and after); `git show
   rev:path` per file (it passes names back to git); output as JSON (the reviewer reads the table). Cost if wrong: a reviewer
   who wants machine output has to parse the table.
2. **Rename detection on (`-M`); binary files and submodules listed and not counted.** Not taken: rename detection off (a
   moved file would show as a whole deleted file and a whole added one, and read as growth); counting a binary file's
   lines (meaningless). Cost if wrong: git's similarity guess (50%) can call a rewrite a rename; the note says so in
   the row.
3. **The place and form of the rule in the template.** A heading of its own, `### Size of a function and a file`, after
   `### Logging scope` and before the product's further rules (WAY-271 keeps the six and their order); size is counted in
   lines; thresholds and exceptions stand only in the product's decision, never in the rule's text (WAY-312); the test's
   configuration lists no exception that the decision does not. Not taken: the rule before the six, or among the standing
   checks (WAY-203 and the task's question 4 rule that out); thresholds written in the rule text; a unit other than lines. Cost
   if wrong: a product that counts in statements or in complexity has to depart or the template changes.
4. **Six entries, one for each row**, numbered in the order of the commits (355 row 3, 356 row 4, 357 row 6, 358 row 1,
   359 row 2, 360 row 5). Not taken: one entry for rows 3 and 4 or for rows 1 and 2 (two questions, and the two grades narrow
   WAY-161 each), numbers in the order of the task's rows (a forward reference would stand in a commit before the entry).
5. **Where the rule is said beside the template and `settle.md`.** `trial_run.md` (the trial of sizes), `recognize.md` (the
   refresh check of the heading, so the extension route of WAY-278 has a trigger), `task_document.md`, `hand_back.md` and
   `SKILL.md` of the coding skill; `task-cycle/review/whole_change.md` (a section of its own for the structure) and
   `task-cycle/review/SKILL.md` section 3 for the two grades. Not taken: only `template.md` and `settle.md` (a refresh would
   not notice the missing heading and the hand back would not check for the decision); a change to
   `task-cycle/skill/SKILL.md` (the reviewer runs the script itself on the dispatch's range, so the dispatch list needs no
   new item); a change to section 2 of the review skill. Cost if wrong: a skill that lists what the reviewer is given and
   that I did not find would disagree.
6. **The plan's bullet in section 3 (after the bullet on *Checks*, before the order of slices) and the author's
   paragraph in section 1 of `task-cycle/change/SKILL.md`.** Not taken: a section of its own in either skill.
7. **WAY-359's scope is `task-cycle` alone**, as WAY-263 has it. Not taken: the five element parts of the foundation (each
   change to any of them would then load the decision).

## Problems observed

- The Bash tool halves backslashes before a Python heredoc: `"a\\n"` reached Python as a real line feed and broke a test file
  (syntax error at the string). Evidence: the failing `gate/run_tests.py task-cycle` run quoted above. Cause not verified
  beyond that: the tool, not Python, rewrote the text (guess). I used the Edit tool and `chr(92)` afterwards.
