# Report 01 — the one author of the whole change

**Status:** done with concerns (two concerns, below; neither blocks the change).

**Commit:** `287a027` on `task/private-path-patterns-in-code` (one commit, base `73b51db`).

## Files changed (added / removed lines)

| File | + / - |
|---|---|
| `task-cycle/private_paths_check.py` | 49 / 22 |
| `task-cycle/test_private_paths_check.py` | 63 / 0 |
| `task-cycle/tracked_private_paths_check.py` (new, the command) | 130 / 0 |
| `task-cycle/test_tracked_private_paths_check.py` (new) | 220 / 0 |
| `task-cycle/test_tracked_files_private_paths.py` | 11 / 105 |
| `installation/README.md` | 39 / 0 |
| `foundations/decisions.md` | 117 / 9 |
| `foundations/invariants.md` | 2 / 2 |

## What was made

1. Items 2 and 3 of the task, in `private_paths_check.py`: `NOTE_LINK` gets `(?<![\w.])`; `WINDOWS_DRIVE` gets a backslash in its lookbehind; a path hit whose text matches `[A-Za-z]:(?:\\[ntr])+` entirely is dropped (`ESCAPE_SEQUENCES_ONLY`, tested on the shown text after the closing punctuation is trimmed). The docstring says all three.
2. Item 1: `find_in_text(text, note_links=True)` and `check_file(path, result, note_links=True, name=None)` take the new parameters; `main` (the cycle's use with a directory or a file) keeps links in every file, so WAY-309's use is unchanged. The printing moved to `report(result)` so the new command prints the same lines.
3. Item 4: the command `task-cycle/tracked_private_paths_check.py INVARIANT`, run from any directory of the repository to check (it asks git for the top level). It reads `foundations/invariants.md`, takes the first paragraph under `## <INVARIANT>`, takes every backticked text in it as a skipped file, and reads all other tracked files that the working tree still has; note links count only in files whose name ends in `.md` (any letter case).
4. Item 5: `test_tracked_files_private_paths.py` now only runs that command in the root of the-way with `tracked-file-private-paths` and expects exit 0; the copy of the four-file list and the two tests about the list are gone (the "listed files are tracked" check now lives in the command, exit 2).
5. Item 6: a new section in `installation/README.md` (after the paragraph on the product's tests), with the invariant, the short test (I ran that exact code in a throwaway repository: passes on a clean one, fails with `a.md:1: note link` when a link is added) and the command's exit codes.
6. Foundation (rows 1–3), written by the steps of `foundation_step.md` and the skills of decision and invariant:
   - `row 1` — WAY-320 edited in place (binding sentence, a verification line, rationale, rejected);
   - row 2 `row 2` — new WAY-323 (the three rules, relation `narrows WAY-309`, rejected ways of questions 2 and 3);
   - row 3 `row 3` — new WAY-324 (the command and what a public product adds, derives from WAY-320, WAY-16, WAY-34, WAY-321; how it differs from the mode WAY-321 rejected is in its rationale);
   - invariant `tracked-file-private-paths`: *Method* stays `test`.

One sentence per entry (English / Polish):

- WAY-320: in a tracked file a note link counts only in a Markdown file, an absolute path in every file; the copy of the record and the description keep the check of WAY-309 in every file. / W pliku śledzonym link do notatki liczy się tylko w pliku Markdown, ścieżka bezwzględna w każdym; kopia zapisu i opis requestu zostają sprawdzane jak dotąd we wszystkich plikach.
- WAY-323: a `[[` stuck to a letter, digit, dot or underscore is no link, a letter after a backslash starts no drive, and a hit that is only `\n`/`\t`/`\r` sequences after the colon is no path. / `[[` przyklejony do litery, cyfry, kropki lub podkreślnika nie jest linkiem, litera po backslashu nie zaczyna dysku, a trafienie złożone po dwukropku z samych sekwencji `\n`, `\t`, `\r` nie jest ścieżką.
- WAY-324: a command checks the tracked files of the repository it runs in and skips the files named in the sentence of the invariant its argument names; a public product adds an invariant with method `test` and a short test that runs it. / Komenda sprawdza pliki śledzone repozytorium, w którym ją uruchomiono, i pomija pliki ze zdania niezmiennika z argumentu; produkt z publicznym repozytorium dodaje taki niezmiennik z metodą `test` i krótki test, który ją woła.
- Invariant, wording on the fork point beside the new one. Before: "...contains an absolute path or a note link as WAY-309 names them." (*Derives from* WAY-320 · WAY-309). Now: "...contains an absolute path or, in a Markdown file, a note link, as WAY-309 and WAY-323 name them." (*Derives from* WAY-320 · WAY-309 · WAY-323 · WAY-324). The list of four files is unchanged. The one test that cites it is `task-cycle/test_tracked_files_private_paths.py`, checked against the new wording (it runs the command on the real tracked files).

## Checks (command and exit code)

| Check | Result |
|---|---|
| `python -B gate/run_tests.py task-cycle` | exit 0, 232 tests OK |
| `python -B gate/run_tests.py installation` | exit 0, 44 tests OK |
| `python -B elements/common/foundation_check.py` | exit 0, 0 errors (also with `--skip-test-citations` right after writing the entries, exit 0) |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | exit 0, "checked: 275 files, 0 listed" |
| `python -B gate/run_tests.py` (whole gate) | not run, the orchestrator runs it |

Failing runs before passing (command, exit code):

- Pattern tests: `python -B -m unittest discover -s task-cycle -p test_private_paths_check.py` after the new tests and before the patterns, with the new parameters accepted and ignored: exit 1, 5 failures by assertion (the dot/underscore link rule, the paths-only parameter, the file-with-name case, the escape-sequence rule, the backslash rule). After the patterns: exit 0, 46 tests.
- The invariant's test: the command and its made-up-repository tests were written after the code (the command's tests passed first time but for one wrong count of mine), so the invariant's test was seen failing by breaking the behaviour: I appended a path (letter D, colon, slash, `work/x`) to `installation/README.md` in the worktree, ran `python -B -m unittest discover -s task-cycle -p test_tracked_files_private_paths.py`: exit 1 with `installation/README.md:184: absolute path: ...`; restored with `git checkout -- installation/README.md`; then the same command: exit 0.
- Mutations (each reverted): note link counted in every file; no skipping of named files; skipping without the "file exists" condition; no error for a named untracked file; sentence not ending at the blank line; heading matched by prefix; backslash removed from the drive lookbehind; dot removed from the link lookbehind; `r` removed from the sequences; `fullmatch` changed to `match`. Each made at least one test fail (`test_private_paths_check.py` or `test_tracked_private_paths_check.py`). I did not mutate "the line `## ` is searched only in `foundations/invariants.md`" nor the order of the output.

## Own-work check (WAY-164)

- Requirement most likely not met: acceptance criterion 1 (exactly 10 places in the tracked files of loop2) and criterion 2 (a real path in a string of code is still listed). I have no access to loop2 and **the loop2 count itself was not run**.
- Check written and run instead: the command run on a made-up repository holding the same shapes, through `python -B task-cycle/tracked_private_paths_check.py inv` (also as the test `test_the_shapes_of_a_product_with_code_give_only_the_real_findings`, exit 0 there). Shapes and what the command printed (a copy of the output, with the Git Bash example in a file the sentence names):
  - an array in an array in a `.ts` file, the shell class of a script without extension, `p.[[PromiseResult]]` in a `.md` file: not listed;
  - `... s<colon>\n`, `s<colon>\n\n`, `\d\d<colon>\d\d` and `C<colon>\n` standing alone in `.py`: not listed;
  - `zob.[[Notatka]]` in `.md`: not listed (the accepted miss), `see [ [Notatka]]` in `.md`: listed (`docs/n.md:1`);
  - the Windows path through a directory named `new` in a `.py`: listed (`src/real.py:1`); the path through a directory named `n` followed by `dir`: listed (`src/real.py:2`); the text with `s<colon>\n` stuck to `Wynik` : listed (`src/real.py:3`);
  - the Git Bash example `/c<slash>...`: listed unless its file is named in the sentence (test `test_a_posix_example_of_a_shell_is_listed_unless_its_file_is_named`).
  Result: 4 listed, exit 1, as the criteria give for these shapes. This shows the rules, not the count 10 on loop2.
- A second reckoning: the pattern change is on a shared script. `private_paths_check.py TARGET` (the cycle's use) was run by its existing tests (CommandTest) and a new one (`test_the_command_still_lists_a_link_in_a_file_of_any_kind`) shows that the links in `.txt` and `.jsonl` of a copy are still listed.

## Choices made (way rejected, cost if wrong)

- Name and form: `task-cycle/tracked_private_paths_check.py INVARIANT`, no `ROOT` argument and no option; it works on the git top level of the current directory. Rejected: a `ROOT` argument like `foundation_check.py` (more surface to promise); cost if wrong: a product whose test cannot set the working directory (rare; `subprocess` can).
- Reading the file names out of the sentence: every text between backticks in the paragraph under `## <id>` is a file name, as git writes it. Rejected: only texts ending in `.py` (as the old test did) or with a `/` or `.`; cost if wrong: a product that writes a backticked word that is not a file in its sentence gets exit 2 "names files git does not track", which tells it at once.
- A named file that git does not track is an error (exit 2), not a silent skip: it keeps the list honest (the old test `test_every_exempt_file_is_tracked`). Cost if wrong: a product that renames a file must fix its sentence in the same change (it learns it from the test).
- "Markdown file" = name ending in `.md`, case-insensitive. Rejected: `.markdown`, `.mdx`; cost if wrong: a link in those is not seen.
- `ESCAPE_SEQUENCES_ONLY` is tested on the shown text (trailing `.,;:` trimmed), so `s<colon>\n.` and `s<colon>\n:` also count as sequences only.
- A binary file is counted, an unreadable-as-UTF-8 file is exit 2 (unchanged from the old test; a product with a tracked text file in another encoding gets exit 2 until it names the file or saves it as UTF-8).
- WAY-323 `narrows WAY-309` and WAY-309 is not edited (the handoff forbids changing its rule about the copy and description). WAY-324 `derives from` WAY-320, WAY-16, WAY-34, WAY-321, scope `task-cycle, installation`; WAY-323 scope `task-cycle`.
- The tests of the command run it as a process in made-up git repositories (the real thing), in a new file `test_tracked_private_paths_check.py`; the old `FindingsOnMadeUpFilesTest` moved there in this form.

## Concerns (for the orchestrator)

1. **No entry in the part map for the new command.** `test-runner-command`, `installation-command` and `foundation-check-command` are surfaces (WAY-49: what a product relies on), and WAY-324 makes `tracked_private_paths_check.py` something a product relies on (its name, argument and exit codes), so a surface entry would be expected by WAY-37. The task's *Settlements to record* has no row for it ("7 shown, 3 accepted"), so I did not write it and did not mark one as `the cycle's`. Draft if wanted: `## tracked-private-paths-command` — "The command that checks the files git tracks in the repository it runs in for absolute paths and note links, and skips the files the sentence of the invariant named by its argument lists, keeps its path, its argument and its exit codes." — *Relied on by:* a product pinned to a commit of the-way. Cost of leaving it out: a later change may rename the command without naming a surface in its request. Cost of adding it: one more promise.
2. Inconsistency between the sentences of the task and its text, resolved by reading, not by the task's words: the answers of questions 1–3 say "Przepuszczony zostaje" about `zob.[[Notatka]]` and about `C<colon>\n`, `C<colon>\t`, `C<colon>\r` standing alone. I read "przepuszczony" as "slips through, not listed" (the accepted misses), because the rule of item 2 (`[ [` stuck to a dot is no link) gives no way to list `zob.[[Notatka]]` and `p.[[PromiseResult]]` apart, and the rule of item 3 drops a hit that is only sequences. The handoff's shape list is then: `zob.[[Notatka]]` not listed, `C<colon>\n` alone not listed, `s<colon>\n\n` not listed, "... s<colon>\nWynik" listed, `C<colon>\new\dir` listed. If the task meant that `zob.[[Notatka]]` must be listed, rule 2 needs a different cut (for example only a single letter or digit before the dot) — please say; WAY-323 and its tests would change.

## Reaches beyond the handoff

- `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/decisions/skill/*`, `elements/invariants/skill/*` and `elements/invariants/template.md`: read whole, as the skills of `record-decision` and `record-invariant` name them (the handoff named the skills).
- `elements/part-map/template.md` (sections on surfaces) and `elements/part-map/skill/*`, and `foundations/part_map.md` lines 60–260: to decide on a surface (concern 1).
- `agent-instructions/README.md:91`, `task-cycle/skill/request_template.md:26`, `task-cycle/skill/SKILL.md:456,544`, `task-cycle/image_files_check.py:20`: found by a grep for the script's name, to see that the cycle's uses stay as they are (no edit needed).
- `foundations/decisions.md` WAY-71 header and its neighbours: not read. WAY-320's and WAY-309's whole text was read.

## Searches not found or unclear

- The handoff names `foundations/part_map.md` entries `task-cycle`, `installation`, `gate`, `elements-common`, `test-runner-command`, but gives no word on whether a surface entry is to be written for the new command: see concern 1.
- The words "przepuszczony/przepuszczone zostaje" in questions 2 and 3 of the task are ambiguous (listed or not): see concern 2.
- *Settlements to record* row 1 says the change is to WAY-320 and the invariant; whether the sentence of the invariant is to name WAY-323 (I added it, as the pattern rules are WAY-323's) is not given.

## Problems observed

- `git add -N` makes a new file visible to `git ls-files` before the commit; the invariant test therefore already reads new files that are intent-to-add. No problem seen.
- A heredoc Python script that wrote regexes with backslashes lost the backslashes once (found by the diff and repaired with the edit tool); no code in the commit is affected (checked by the diff of `private_paths_check.py` and the mutation runs).
