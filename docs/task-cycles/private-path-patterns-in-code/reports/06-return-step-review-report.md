FAIL 3057f161ed49c7a4de582243f334dc8807b71d04

# Report 06 — review of the return step's commits

Range `578a8bd..3057f16`, one commit (`3057f16`, "Record the command that checks tracked files for
private paths as a surface and name how its sentence is read"); `git rev-parse HEAD` is
`3057f161ed49c7a4de582243f334dc8807b71d04`, the head given. Files: `foundations/decisions.md`
(one sentence added to WAY-324) and `foundations/part_map.md` (new surface
`tracked-private-paths-command`).

## Verdict on what the return step wrote

- **WAY-324, the added sentence** (`foundations/decisions.md:10471-10472`): matches the code.
  `task-cycle/tracked_private_paths_check.py:93` takes every backticked text of the sentence as a
  name and `:94-98` raises an error (exit 2, `:123-125`) for a name not in `git ls-files`; `:107`
  skips exactly those names. Tests cover both halves
  (`task-cycle/test_tracked_private_paths_check.py:91`, `:190`). It binds products after the merge,
  so it belongs in the decision (WAY-36). No finding.
- **The choice to write a surface entry:** right. A product's test runs the command at
  `.the-way/task-cycle/tracked_private_paths_check.py` with one argument and reads its exit code
  (`installation/README.md:104-110`); WAY-49 names a command someone outside relies on as a
  surface, and WAY-324's own *complies* ("a product moves its pin and its test runs the command of
  the new commit unchanged") is a promise only a surface entry records. The form follows
  `foundation-check-command` ("keeps its path, its argument and its exit codes"). Two findings
  below concern the wording, not the choice.

## Findings

### Critical

none

### Important

1. **`foundations/part_map.md:213-214` — the surface drops the qualification "in a Markdown
   file" for note links.** The entry says the command "checks the files git tracks ... for absolute
   paths and note links". The code looks for note links only in a file whose name ends in `.md`
   (`task-cycle/tracked_private_paths_check.py:110`, `note_links=name.lower().endswith(MARKDOWN_SUFFIX)`;
   test `task-cycle/test_tracked_private_paths_check.py:78`
   `test_a_note_link_is_listed_in_a_markdown_file_only`). That restriction is the settlement of the
   task's question 1 (*Settlements to record* row 1), and every other account of it in the change
   carries the qualification: the invariant (`foundations/invariants.md:88`, "an absolute path or,
   in a Markdown file, a note link") and the installation section (`installation/README.md:116`,
   "each note link in a Markdown file"). The surface is the entry a product reads as the promise of
   the command; read as written, a product expects a `[[...]]` in a `.txt` or `.py` file it tracks to
   be listed, and it is not. A foundation entry the change writes that restates the rule without its
   qualification is Important by WAY-263. Fix: "for absolute paths, and for note links in Markdown
   files," or drop the "for ..." clause and identify the command by its path.

2. **`installation/README.md:121` — the installation section restates the promise the new
   surface makes, differently.** It says "the command keeps its name, argument and exit codes, the
   functions are not promised"; the surface (`foundations/part_map.md:215-216`) says the command
   "keeps its path, its argument, the meaning of the backticked texts in that sentence and its exit
   codes". Two differences: *name* against *path* — the product's test in the same section hardcodes
   the directory (`installation/README.md:104`), so a move inside the-way that keeps the file name
   breaks every product while the section says nothing was promised there; and the meaning of the
   backticked texts, which the surface promises and the README's sentence of promise leaves out
   (item 1 at `:84-87` describes the reading, but not as something kept across moves of the pin).
   The README line predates this range (`578a8bd`), but writing the surface made it a second account
   of the entry, and the return step corrects in the same change whatever no longer matches it
   (`task-cycle/skill/return_step.md:6-8`, WAY-11); the README is the file of *To do* 6, within the
   task. Another changed file repeating an entry the change writes, differently, is Important by
   WAY-263. Fix: "the command keeps its path, its argument, the meaning of the backticked texts and
   its exit codes (the surface `tracked-private-paths-command` of the-way's part map); its functions
   are not promised."

### Minor

none

Blocking: 2 (both Important, both within the task). Out of scope: 0.

## Declined to judge

- That the request names the new surface (WAY-49): a matter of the request's description, which
  this range does not hold; the orchestrator writes it.
- A `# surface: <id>` comment at the command's code, as `project-level/plan_state.py:486` has for
  `project-plan-state-command`: one instance in the repository, no entry requires it, so its absence
  is no finding.

## Author's claims checked

- "WAY-324 matched except one thing ... added as a third sentence": confirmed (above).
- "No decision, invariant, fact or glossary entry otherwise needed": no counter-evidence found for
  decisions, invariants, facts or glossary; the two findings concern the surface's wording and a
  restatement of it.
- Checks: reproduced (below).

## Checks

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| `python -B gate/run_tests.py elements/part-map` | 0 (39 tests OK) |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 ("checked: 275 files, 0 listed") |
| `git status --short` after the checks | empty (nothing changed) |
| Manual: the two new sentences and the surface compared line by line with `task-cycle/tracked_private_paths_check.py` (whole) and the test names of `task-cycle/test_tracked_private_paths_check.py` | findings 1 and 2; the WAY-324 sentence matches |

Not run: the whole gate (the orchestrator runs it, per the handoff).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-263, whole — the grade of a restatement of an entry the change
  writes (findings 1 and 2).
- `foundations/decisions.md` WAY-36, whole — whether the added WAY-324 sentence binds after the
  merge; WAY-38, WAY-45, WAY-48 were partly in the same read window and were not used.
- `foundations/invariants.md:86-92`, the entry `tracked-file-private-paths` — its sentence, to
  compare with the surface and to see that it holds no backticked text other than file names.
- `installation/README.md:71-125` — the section restating the command's promise (finding 2).
- `task-cycle/test_tracked_private_paths_check.py`, its test names and `:78`, `:91`, `:190` — the
  coverage of the WAY-324 sentence and of the Markdown-only rule.
- `git grep` for `tracked_private_paths_check`, `tracked-private-paths-command`,
  `project-plan-state-command` and `surface:` — other places that name the command or mark a
  surface in code.

## Searches not found or unclear

none
