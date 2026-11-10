PASS 287a02712e683f4a3694d5ef46b795b253a1b1fc

# Review 02 — the whole change

Range `73b51db53716f5a7656ae73f327c18e30e9fd5c5..287a027` (one commit, one author, no plan, no
spec). `git rev-parse HEAD` = `287a02712e683f4a3694d5ef46b795b253a1b1fc`, the head given.

Blocking findings: 0. Minor: 3 (all within the task). Out of scope: 0 findings; 4 lines under
Declined to judge.

## Coverage of the task

| Item | Met by | Verdict |
|---|---|---|
| To do 1 — links only in `.md` for tracked files, everywhere for the copy and description | `task-cycle/tracked_private_paths_check.py:107-112` (`note_links=name.lower().endswith(".md")`); `private_paths_check.main`/`check` unchanged, default `note_links=True` | met; tested by `test_a_note_link_is_listed_in_a_markdown_file_only` and `test_the_command_still_lists_a_link_in_a_file_of_any_kind` |
| To do 2 — `[[` stuck to letter, digit, dot, underscore is no link, in every check | `task-cycle/private_paths_check.py:76` `(?<![\w.])` on `NOTE_LINK`, shared by both uses | met |
| To do 3 — letter after backslash starts no drive; hit of only `\n`/`\t`/`\r` after `X:` is no path | `task-cycle/private_paths_check.py:67` (`\\` added to the lookbehind), `:79` and `:119-121` (`ESCAPE_SEQUENCES_ONLY.fullmatch` on the shown text) | met |
| To do 4 — command in `.the-way/task-cycle/` checking the tracked files of the repository it runs in, skipping the files the invariant's sentence names | `task-cycle/tracked_private_paths_check.py` (new) | met; also run by me in a crafted product repository with a gitlink `.the-way` (below) |
| To do 5 — the-way's test calls the command with `tracked-file-private-paths`, no copy of the list, still passes | `task-cycle/test_tracked_files_private_paths.py:21-30` | met; the check that the named files are tracked moved into the command (exit 2) |
| To do 6 — `installation/README.md` says a public product adds the check, and how | `installation/README.md:78-115` | met (Minor 2 and 3 below on completeness) |
| Acceptance 1 — 10 places on loop2 `2fe922c` | not run: no access to loop2 (author and reviewer alike) | see "The count of 10" below |
| Acceptance 2 — `"C<colon>\new\dir"` in a `.py` still listed | `test_a_real_path_that_starts_like_an_escape_sequence_is_still_listed`; my scratch run lists `src/app.py:4: absolute path: C<colon>\new\dir` | met |
| Question 1 | WAY-320 edited (`foundations/decisions.md:10286-10290`), invariant sentence (`foundations/invariants.md:88`); WAY-309 untouched | met |
| Question 2 | `NOTE_LINK` lookbehind; `zob.[[Notatka]]` not listed, as an accepted miss (WAY-323 price) | met; I agree with the orchestrator's reading of "przepuszczony" as "not listed" — the task's own *Po co to* uses "przepuszcza" for a miss, and rule 2 cannot tell `zob.[[` from `p.[[` |
| Question 3 | as To do 3; `C<colon>\n`/`C<colon>\t`/`C<colon>\r` alone not listed, `C<colon>\new\dir`, `C<colon>\n\dir` and `s<colon>\nWynik` listed | met, same reading |
| Question 4 | command + README section + WAY-324 | met |
| Question 5 | no guidelines awaited | met (nothing to check) |
| Settlement row 1 | WAY-320 binding sentence, *violates* example, rationale and three rejected ways of question 1 | met (Minor 1 on a number in its rationale) |
| Settlement row 2 | WAY-323 (`foundations/decisions.md:10416`), `narrows WAY-309`, rejected ways of questions 2 and 3 (small drive letter, parser per language, file on the product's list, no change) | met |
| Settlement row 3 | WAY-324 (`foundations/decisions.md:10464`), its relation to the way WAY-321 rejected in the rationale, four rejected ways of question 4 | met |

### The count of 10 (acceptance criterion 1)

Not runnable here. Judged on the shapes the task names (`task.md` *Need*): the 70 arrays in arrays
are in `.js`/`.ts`/`.py` files and the `[ [:space:]]` is in an extensionless script, so the `.md`-only
rule drops all 71; the two `p.[[PromiseResult]]` in a `.md` file are dropped by the dot in the
lookbehind; the four `s<colon>\n` of the form `f"... within {SERVE_WAIT} s<colon>\n"` end at the `"` that
`PATH_TAIL` excludes, so the shown text is `s<colon>\n` and is dropped; `d:` of `\d\d<colon>\d\d` has a
backslash before it and is dropped. That is 78 of 78. The rules as coded are the rules the task's own
trial (`task.md` *Context*, the trial on loop2 that gave 10) applied, with no broadening I could find
beyond the escape rule being tested after the trailing `.,;:` is trimmed. The author's made-up
shapes (`test_the_shapes_of_a_product_with_code_give_only_the_real_findings`) match the task's
shapes, and my own crafted repository (below) gave the same. What stays unverified: that none of
loop2's four `s<colon>\n` has text glued after it and none of its nine real paths stands after a backslash —
the count 10 itself.

## Findings

### Critical

none

### Important

none

### Minor (each within the task)

1. **`foundations/decisions.md:10316-10318` — a number in WAY-320's rationale is not the source's.**
   The sentence reads: "in code the same brackets are an array inside an array or a test of the
   shell, and a run of the check over every tracked file of one public product on 2026-11-09 listed
   73 such texts among 88 findings." The task (`task.md:27`) gives 73 `[[...]]` hits of which 70 are
   arrays in arrays and 1 a shell class — 71 "such texts" — while the other 2 are specification slots
   in a Markdown file, which the `.md`-only rule of WAY-320 does not remove (WAY-323 does). The
   rationale therefore credits the rule it argues for with two hits it does not remove. It binds no
   behaviour, so Minor; fix: "71 such texts" or "73 note-link-shaped texts, 71 of them in code".
   Evidence: `task.md:27`; WAY-323's rationale (`foundations/decisions.md:10445-10447`) states the
   split correctly.

2. **`installation/README.md:109-112` — the exit codes a product relies on are given in part.**
   The README is the only text a product reads before writing its test, and WAY-324 makes the
   command's exit codes something the product relies on. The README names exit 2 only for "the
   identifier is missing from the invariants file or the sentence names a file git does not track";
   the command also exits 2 for a missing argument, a directory outside a git repository, a missing
   `foundations/invariants.md`, and a tracked file that is not UTF-8
   (`task-cycle/tracked_private_paths_check.py:20-23`). The last one is the one a product is likely
   to meet (a tracked text file in another encoding) and the README says nothing about it. Also
   unsaid at `installation/README.md:85-86`: every backticked text of the sentence is taken as a file
   name, so a product that writes, say, a backticked word in its sentence gets exit 2. The test fails
   with the message in both cases, so nothing passes silently; Minor.

3. **`installation/README.md:82-87` — the invariant a product is told to write lacks its
   *Derives from*.** The README tells the product to write the invariant "as WAY-309 and WAY-323 name
   them" and gives its method, but not what it derives from. `elements/invariants/template.md:122-124`
   makes *Derives from* mandatory and `:139-142` says a decision of the-way at the pinned commit "is no
   decision entry" of the product, so a product following the README alone has no valid value
   (WAY-324 or WAY-320 of the-way would be wrong there). An agent writing the entry through
   `the-way-record-invariant` will meet this and write `TODO` or ask; the README could say that the
   product records its own decision (its repository is public, no private paths in tracked files) or
   names a source. Minor: the task's item 6 asks for the invariant with the list and the method
   `test`, which the README gives.

## Declined to judge

- The part-map surface entry for the new command (author's concern 1): outside this range; the
  handoff says the cycle's return step writes it through `the-way-update-part-map`.
- Note links in `.mdc`, `.markdown` or `.mdx` files are not looked for in tracked files: the task
  (item 1, question 1) says `.md` literally; the-way tracks none such (`git ls-files`, extensions:
  229 md, 47 py, 3 other).
- A long-path prefix `\\?\C<colon>\work` no longer starts a drive (backslash rule); `\\?\C<colon>\Users\<name>`
  is still listed through the home-directory pattern (scratch line 8). Task-mandated rule (question 3);
  the price is not named in WAY-323 but the task's answer named only `C<colon>\n`/`C<colon>\t`/`C<colon>\r` — left to
  the human if wanted.
- A non-UTF-8 tracked file stops the whole run with exit 2 and the only remedy the command offers is
  naming the file in the sentence, which also exempts it from the path check: unchanged behaviour of
  the old test, outside the task.

## Checks run

| Check | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `287a02712e683f4a3694d5ef46b795b253a1b1fc` |
| `python -B gate/run_tests.py task-cycle` | 0, 232 tests OK |
| `python -B gate/run_tests.py installation` | 0, 44 tests OK |
| `python -B elements/common/foundation_check.py` | 0, "0 errors" |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (in the worktree root) | 0, "checked: 275 files, 0 listed" |
| Scratch: `python -B .runs/review02_script/scratch.py` — a git repository in `.runs/review02_scratch/repo` with an untracked copy of the two scripts under `.the-way/task-cycle/`, a gitlink entry `.the-way` (mode 160000, as a submodule gives), a product invariant naming `tests/deploy/deploy_script_support.py`, and the README's test extracted word for word into `tests/test_tracked.py` | script 0; command exit 1; README test exit 1 |
| What the scratch run listed | exactly: `docs/a.md:1` `[ [Real note]]` (not `zob.[[Notatka]]` on the same line); `src/app.py:4` `C<colon>\new\dir`; `:5` `C<colon>\Users<backslash>alice\n`; `:6` `s<colon>\nWynik`; `:8` `\Users<backslash>alice` (from the long-path line); `:11` `e<colon>\tools`. Not listed: `s<colon>\n`, `s<colon>\n\n`, `s<colon>\r\n`, `C<colon>\t` alone, `\d\d<colon>\d\d`, `[ [a, b]]` in `.ts`/`.py`, `[ [:space:]]` in an extensionless script, `p.[[PromiseResult]]` in `.md`, `[ [Txt note]]` in a `.txt`, the Git Bash example in the named file; the gitlink was skipped (8 files counted) |
| Scratch, after replacing `src/app.py` and `docs/a.md` by clean text: `python -B -m unittest tests.test_tracked` in the scratch repository | 0, 1 test OK — the README's test passes on a clean product and fails with the listing on a dirty one |
| Manual: diff read whole (8 files); the author's mutation claims spot-checked by reading which test pins each branch (`.lower()` by `B.MD`, backslash lookbehind, dot lookbehind, `fullmatch`, untracked named file, sentence end at blank line) | each branch has an asserting test |

Not run: the whole gate (the orchestrator runs it); acceptance criterion 1 on loop2 `2fe922c` (no
access to that repository).

No tracked file was changed; the scratch files lie under the ignored `.runs/` of this worktree
(`.runs/review02_script/`, `.runs/review02_scratch/`, `.runs/review02_tc.txt`,
`.runs/review02_inst.txt`).

## Foundation read

Selected by "Reading the foundation" (`elements/common/way_of_working.md:59`), narrowed: the parts
touched are `task-cycle`, `installation` and, through the foundation files, `every`. Read whole:
WAY-309, WAY-320, WAY-321, WAY-323, WAY-324 and the sentences of WAY-16 and WAY-34 the task quotes;
the invariants file lines 1-200 and 318-357 (all invariants with *Part* `every` or `task-cycle`:
`tracked-file-private-paths`, `outbound-link-reach`, `script-language`, `script-imports`,
`script-subprocesses`, `test-method-citation`, `cross-part-imports` among them — the new script
imports only the standard library and a file of its own part and starts only git and the running
interpreter); the part-map entries `task-cycle`, `installation`, `installation-command`,
`foundation-check-command`. Not read whole: the other ~100 decisions whose *Scope* names
`task-cycle` and the 14 naming `installation` — a full read was out of proportion; none of the
entries above links to them.

## Reaches beyond the dispatch

- `elements/decisions/template.md:155-202` — the meaning of `narrows` and of *Verification*
  `invariants:`, to judge WAY-323's relation and both new entries' verification lines.
- `elements/invariants/template.md:120-159` — *Derives from* rules, for Minor 3.
- `elements/common/foundation_check.py` (grep `prefix`) — whether a product's foundation check would
  reject `WAY-309` in a product's invariant sentence: references are checked only for the log's own
  prefix, so it would not.
- `foundations/part_map.md` (grep) — that `task-cycle/**` covers the new file and which surfaces
  exist.
- `the author's rule on writing scripts` — the user's rule read before writing the
  scratch script.

## Searches not found or unclear

- The author's report and the handoff speak of loop2's four `s<colon>\n` only through one example; whether
  each of the four ends at a quote or bracket (so that the shown text is the sequence alone) is not
  in the task and could not be checked.
