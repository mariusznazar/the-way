PASS 8c97482acb873cb2a6bb6744546499d64370020c

# Review of correction 1 — cycle-instruction-seven-fixes

Range `dcaa169c..8c97482a` (2 commits: `022a8b40`, `8c97482a`), diff computed by me;
`git rev-parse HEAD` is `8c97482a`. The diff holds three files: `task-cycle/skill/SKILL.md` (+3 −3),
`task-cycle/slice_size.py` (+8 −2), `task-cycle/test_slice_size.py` (+16 −2). The remarks file
stands in the place of a findings file; I take it as the dispatch gives it, as remarks that bind
the correction, and judge nothing of who gave them.

Counts: blocking 0 · Minor new in the correction 1 · out of scope 0.

## The remarks

**Remark A — "the lead": made.** `task-cycle/skill/SKILL.md:508` now reads "the orchestrator may
dispatch a fresh reviewer with `review-change` on groups of them in the plan's order, as for a
slice with a review of its own, and records the grouping and its reason." Only the name changed;
the other changed lines are the reflow of the same words. "The orchestrator" is the name the skill
gives its reader (its opening, line 9) and uses in the third person in the same step
(`:558`, `:560`), and the name WAY-136 uses for the same sentence. The sub-step around the
sentence names no actor — it speaks in imperatives — so either "you" or "the orchestrator" was open;
the author's choice keeps the verb "records" as it stood. A search of the `.md` and `.py` files
outside `.runs/` finds "the lead" nowhere any more, and no copy of the sentence elsewhere.

**Remark B — the measure counts a code file whole and a file of the foundation by its ranges:
made.** `task-cycle/slice_size.py:200-202`: a file of *Change* that exists counts whole unless
*Read* names it by ranges and its first directory under DIR is `foundations`. A file that *Read*
names whole, or both whole and by ranges, still counts whole, and a file of *Read* alone counts as
before. On the real files (scratch run below): the decision log named by a range counts 8 522
characters, the code file of the remark counts 25 907 where it counted 548, and a skill file named
by a range counts whole too. The test the remark asks for stands:
`test_changed_code_file_that_read_names_by_ranges_counts_whole`.

## What the dispatch asks me to judge

- **The tests.** The new test writes a code file of 29 characters ("line one\n" 9, "line two\n" 9,
  "line three\n" 11), names `:1-1` of it in *Read* and expects 29 characters, 12 tokens (29 / 2.5 =
  11.6, rounded up), `fits`; the numbers are right, written out and derived in the comment, not
  taken from the code. It fails on the code as it stood (mutation M1 below: 9 characters in place of
  29), which is the red run the author reports. The test of the both-ways case moved its file
  from `log.md` to `foundations/decisions.md` with its expected values unchanged (14 characters, 6
  tokens): the cause lies in the requirement, since a file outside `foundations/` now counts whole
  whatever *Read* names, and the test would no longer tell whole from ranges there; this is a change
  of an input, with its cause named, and no weakening (`guidelines/testing.md`, "Changing an
  existing test"). The test of the log named by a range already used `foundations/decisions.md`.
- **"A file of the foundation" as a file under `foundations/` of DIR.** Accepted. The place is the
  one the-way gives a product's foundation: the decisions template and the index script read
  `foundations/decisions.md` under the product's root, the part map lists the five files there as
  the files of its five parts, and WAY-04 closes the list of elements at five; I checked the last
  two, which the docstring names. A directory is the better rule than five names: it follows the
  item of point 4(c), "a file of the foundation", for every element, not the decision log alone,
  so the measure and the reading count the same for all of them, which is what the remark asks.
  The docstring's gloss names the five files while the code takes every file below the directory;
  no other file stands there, so I raise no finding on it.
- **The docstring against the code.** They agree: by ranges where the changed file is one of the
  foundation and *Read* names it by ranges; whole for a changed file that is none; "any other
  file" — a file of *Read* alone, or a changed file of the foundation that *Read* does not name by
  ranges — whole where a field names it whole, otherwise by its ranges; whole beats ranges. For a
  file of the foundation the sentence of point 4(a) reads as it did.
- **Nothing accepted changed.** `git diff --quiet dcaa169c..8c97482a -- foundations elements
  task-cycle/plan task-cycle/change task-cycle/review` exits 0: the three decisions, the template
  and the sentences of the other three skills are untouched. The sentence of point 4(b) and the
  item of point 4(c) speak of entries of the log and of a file of the foundation, and agree with
  the corrected measure as they stand.
- **No code made for a test (WAY-409).** The one branch added is the rule of the remark; the
  constant `FOUNDATION_DIRECTORY` is the place of the foundation, not the input of a test.
- **The author's own-work check** names the requirement where the correction is weakest — both
  cases in one run on real files — and its figures agree with mine (25 907 for the code file; the
  log by its range). Its judgment that no walk is due is the one I weighed in the first review; the
  command was run on real files all the same.

## Findings

### Minor, new in the correction

**1. No test tells `foundations/` at the root of DIR from a directory of that name deeper in the
tree.** Place: `task-cycle/slice_size.py:201` and `task-cycle/test_slice_size.py:63-97`. The
docstring says "one under `foundations/` of DIR" and the code tests the first directory of the
path; a mutation that takes the name anywhere in the path (M6 below) passes all 20 tests. The case
is real in a product, where the pinned the-way holds `.the-way/foundations/`, but a product's slice
does not change those files, so nothing counts wrongly today; this is coverage that would be good
to have, no defect of the code.

## Declined to judge

- A changed code file with a range in *Read* that runs beyond the file is counted whole and the
  range is not reported, so the slice is not left `unchecked`: this is how the script treated such
  a file before the task began (a file counted whole skips its ranges), and the remarks do not ask
  for it.

## Structure of the code the correction leaves

`python -B task-cycle/change_file_sizes.py dcaa169c 8c97482a`, exit 0: `task-cycle/slice_size.py`
259 → 265 lines, `task-cycle/test_slice_size.py` 223 → 237, `task-cycle/skill/SKILL.md` 906 → 906.
`measure` runs from line 168 to 217, as long as before. The test of the invariant
`function-and-file-size` on the head: 4 tests OK, exit 0; I did not run it on the base, whose tree
is that of `52801a69` (the two commits between hold the record's copy and its removal, and
`git diff --stat 52801a69..dcaa169c` is empty) and differs from the tree I ran it on at `bcaddc2b`
by prose of two decisions and one comment. One constant added, used once; no code without a user
and no name that stopped being true.

## Checks I ran

In the reviewed worktree, reading only:

- `git rev-parse HEAD`, `git log --stat dcaa169c..8c97482a`, `git diff dcaa169c..8c97482a`,
  `git diff --stat 52801a69..dcaa169c`, `git diff --quiet dcaa169c..8c97482a -- foundations elements
  task-cycle/plan task-cycle/change task-cycle/review` — exit 0 each.
- `python -B task-cycle/change_file_sizes.py dcaa169c 8c97482a` — exit 0.
- `python -B -m unittest task-cycle/test_slice_size.py` — exit 0, 20 tests OK.
- `python -B -m unittest agent-instructions/test_size_invariant.py` — exit 0, 4 tests OK.
- The pinned Ruff of the main checkout, with `--no-cache`, on `task-cycle/slice_size.py` and
  `task-cycle/test_slice_size.py`: `ruff check --no-cache --ignore-noqa --config ruff.toml` — exit 0,
  "All checks passed!"; `ruff format --check --no-cache --config ruff.toml` — exit 0, "2 files
  already formatted".
- `python -B gate/run_tests.py task-cycle` — exit 0, 538 tests OK, 2 skipped on Windows. It ran in
  the background for 649 seconds; I waited for it in stretches under four minutes and read its
  result before this report.
- `python -B gate/run_tests.py instruction-files` — exit 0, 105 tests OK, 5 skipped.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests OK.
- Scratch run, `python -B task-cycle/slice_size.py <plan>` on a plan of seven slices against the
  real files — exit 1, as expected, for the two slices too large:

  | Slice | *Change* | *Read* | Counted |
  |---|---|---|---|
  | 1 | `foundations/decisions.md` | a range of 97 lines of it | 8 522 characters, fits |
  | 2 | `foundations/decisions.md` | none | 905 485, too large |
  | 3 | `task-cycle/remove_merged_worktrees.py` | `:1-10` of it | 25 907 (the whole file), fits |
  | 4 | `foundations/invariants.md` | `:6-15` of it | 294, fits |
  | 5 | `foundations/decisions.md` | the file whole and a range of it | 905 485, too large |
  | 6 | `task-cycle/skill/SKILL.md` | `:1-5` of it | 74 345 (the whole file), fits |
  | 7 | none | `task-cycle/remove_merged_worktrees.py:1-10` | 548, fits |

Mutations, each on a copy of `slice_size.py` beside a copy of its test file, run with
`python -B -m unittest test_slice_size.py`:

- M1, the condition of the foundation dropped (the code before the correction): 1 failure, the new
  test of the code file.
- M2, `!=` turned to `==`: 2 failures, the new test and the test of the log named by a range.
- M3, another directory name: 1 failure, the test of the log named by a range.
- M4, every changed file counted whole: 1 failure, the test of the log named by a range.
- M5, ranges win over a whole entry of *Read*: 2 failures, the both-ways test and the new test.
- M6, the directory's name taken anywhere in the path: no failure (finding 1).

Not run: the full gate, by the handoff; `python -B elements/common/foundation_check.py`, since the
correction changes no file of the foundation.

## Reaches beyond the dispatch

- WAY-04, its binding sentences (`foundations/decisions.md:504-510`), and a search of
  `foundations/part_map.md` for `foundations/` — the two sources the docstring names for its rule.
- A search of `task-cycle/skill/SKILL.md` for "orchestrator" — the name the skill gives its reader.

## Working copies

My directory `.runs/review-correction-1/` held the mutated copies, the scratch plan and the outputs
of two test runs; it is removed. One file I wrote outside it by mistake, directly under `.runs/`:
`.runs/review-correction-1-task-cycle.out`, the output of the directory run; it is removed too.
Both removals were made by the path written out in full. No worktree was made: the checks ran in
the reviewed worktree with `python -B` and Ruff's `--no-cache`, and changed no file of it.
`.runs/` holds `task-cycles/` alone, and the worktree is clean at `8c97482a`. The file `.runs/fc.txt`
that the author's report names as a remainder was not there when I looked.

## Unread material

- `task-cycle/skill/SKILL.md`: on this head the diff and the lines the search gave; read in parts
  in the first review.
- `task-cycle/slice_size.py`: the diff and lines 160-205 on this head; read whole at `bcaddc2b`.
- `task-cycle/test_slice_size.py`: the diff on this head; read whole at `bcaddc2b`.
- WAY-04: its binding sentences, not its fields, rationale and rejected options.
- The handoff, the remarks, the author's handoff, the author's report and `task-cycle/review/fix.md`
  were read whole (`fix.md` at the review of the fix).

## Searches not found or unclear

- The remark asks for the name of the agent leading the cycle "as the sub-step around it does": the
  sub-step names no actor, only imperatives, so the words leave open whether "you" or "the
  orchestrator" is meant; the author's choice is judged above.
- The remark speaks of "the files of decisions the task was about", the author's handoff and the
  item of point 4(c) of "a file of the foundation": the correction follows the wider of the two,
  every file under `foundations/`, as judged above.
