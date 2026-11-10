# Report 05 — the return step

**Status:** done. **Commit:** the one commit on top of `578a8bd` named at the end of this report.

## Foundation compared with the code

- **WAY-320** (edited by the change), **WAY-323** and **WAY-324** (written by it), and the invariant
  `tracked-file-private-paths`: each read against `task-cycle/private_paths_check.py`,
  `task-cycle/tracked_private_paths_check.py` and their tests. WAY-320 (a note link counts in a
  Markdown file; a path in every file; the copy and the description keep the check in every file),
  WAY-323 (the three rules) and the invariant sentence (four files, "in a Markdown file", WAY-309
  and WAY-323) match the code. WAY-324 matched except one thing the code does and the entry did not
  say: every backticked text of the sentence is read as a file name, and a name git does not track is
  an error (exit 2). That binds products that write the sentence, so I added it to WAY-324's binding
  part as a third sentence (WAY-36: it binds after the merge).
- **WAY-309, WAY-16, WAY-321, WAY-34** (named by the task): compared; none needs a change. WAY-309's
  rule for the copy of the record and the description is untouched and the code still lists links in
  every file there; its "every absolute path and every note link" is narrowed by WAY-323
  (`narrows WAY-309`). WAY-321's rejected mode and WAY-324 are told apart in WAY-324's rationale. The
  command runs under the one command of tests (WAY-16) through the test that cites the invariant.
  WAY-34: no copy of the command in a product.
- **Part map, parts `task-cycle`, `installation`, `gate`:** `task-cycle/**` and `installation/**`
  already claim every new and changed file; `Depends on` of both parts already allows the
  dependencies the code has (the command imports only its neighbour in the same part; the test uses
  `gate/run_tests.py` only by being found by it). `gate` is unchanged. No sentence of a part is made
  false.

## Written

- **Part map, one surface:** `tracked-private-paths-command` in `foundations/part_map.md`, after
  `project-plan-state-command`, in the form of `test-runner-command` and `installation-command`:
  the command keeps its path, its argument, the meaning of the backticked texts in the sentence and
  its exit codes; *Relied on by:* a product pinned to a commit of the-way. Written by the steps of
  `the-way-update-part-map` (read its skill, `decide_entry.md`, `write.md` and `template.md`
  sections on surfaces; the search of the map found no entry for the same surface; no decision rests
  on a boundary this moves; WAY-49 asks that the request name the surface when a change alters it,
  so the request of this cycle names it). Marked: `the cycle's` (record Q4 of the orchestrator).
- **Decision:** WAY-324 edited in place (the third sentence above); no new decision.
- **Invariants:** none written or changed in this step.
- **Environment facts:** none. The change rests on no source outside the product that the foundation
  lacks (the Obsidian rendering of a link stuck to a word is only a price named in WAY-323, not a
  fact a decision or invariant rests on).
- **Glossary terms:** none. The words used (note link, absolute path, escape sequence, skipped
  file) mean what a reader of the field takes; none is used against an entry.
- **Projected entries:** none (the task is independent; no definition projects entries).
- **Rows of *Settlements to record* not yet written:** none; rows 1–3 are written (WAY-320, WAY-323,
  WAY-324) by the first pass.
- **A choice that binds after the merge not in a decision:** the one above (the file-name reading of
  the sentence). The smaller choices (a Markdown file is a name ending in `.md` in any letter case;
  a sentence is the first paragraph under the heading) stay in the code, the command's docstring and
  the README section; they bind no product beyond what that section says. None else.

## Checks

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0, 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0, 275 files, 0 listed |
| `python -B gate/run_tests.py elements/part-map` (the directory of the part-map test, touching `foundations/part_map.md`) | 0, 39 tests OK |
| `python -B gate/run_tests.py task-cycle`, `installation` | not run again: no file of those directories changed in this step (last run on `578a8bd`: exit 0 each) |
| whole gate | not run (the orchestrator runs it) |

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-11, WAY-36, WAY-37, WAY-40, WAY-49 and WAY-95: read whole, to apply
  the return step and the surface rule. `elements/part-map/template.md` read whole.

## Searches not found or unclear

none
