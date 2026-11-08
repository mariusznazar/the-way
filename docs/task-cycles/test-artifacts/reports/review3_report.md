PASS 25dd4bac8cb40dafe51ff04b4c945f3206a2b874

# Review of the return step's commits, task cycle `test-artifacts`

Range `ef0195edb7128b30f9768aab89e3b8846d2d8d5e..25dd4ba` (one commit). `git rev-parse HEAD` = `25dd4bac8cb40dafe51ff04b4c945f3206a2b874`, as dispatched. `git diff ef0195e..25dd4ba --stat`: one file, `task-cycle/image_files_check.py`, 2 insertions and 1 deletion, docstring only.

## Findings

Blocking: 0. Minor: 0. Out of scope: 0.

None. The claims of the return report checked out.

### Verification of the author's claims

- The docstring sentence now reads: `private_paths_check.py` "reads the text of the files for paths and links, skipping as binary a file with a NUL byte near its start, which most images have". `task-cycle/private_paths_check.py` does this: `check_file` (line 113) counts a file as binary when `b"\0" in data[:BINARY_PROBE]` (8192 bytes) and the file has no UTF-16 BOM, and does not read it. Its own docstring (lines 37-40) says the same. The earlier wording ("counts an image there as a binary file it does not read") was wrong for an SVG, which is text and is read. The new wording is correct for that case and for the PNG and JPEG headers, which carry NUL bytes in the first bytes. "Most images" is a hedge that stays true.
- The diff changes nothing outside the docstring, so no behaviour changes. The argparse description is `__doc__.split("\n\n")[0]`, the first paragraph, which the edit does not touch.
- Foundation entries compared with the code, for a mismatch the return step may have missed:
  - `record-copy-image-check` (`foundations/invariants.md:318`): the extension list is the same, in the same order, as `IMAGE_EXTENSIONS` and the docstring list: png, jpg, jpeg, gif, webp, bmp, tif, tiff, ico, svg, avif, heic. The match is case-insensitive (`name.lower().endswith`). Exit 1 with listed files and 0 with none, as in `main`. The invariant says "below the directory it is given"; the script also takes a single file. That is a superset the sentence does not forbid, not a mismatch.
  - `record-copy-image-files`: a review invariant, with nothing in the range to compare. No commit of the range adds a file below `docs/task-cycles/`.
  - WAY-316: the script writes no file and opens no file; it names no place for screenshots, as the decision requires of the-way.
  - WAY-317, WAY-318, WAY-319, WAY-121 and WAY-165: nothing in this range touches them. The return report names the files they were compared against; I made no new comparison.

## Declined to judge

none

## Checks

- `git rev-parse HEAD` -> `25dd4bac8cb40dafe51ff04b4c945f3206a2b874`.
- `git diff ef0195e..25dd4ba` and `git log` of the range -> one commit, docstring only.
- `git status --short | wc -l` -> 0 (worktree clean, nothing in it changed by this review).
- `python -B -m unittest test_image_files_check` run in `task-cycle/` -> exit 0, 13 tests OK. The same via the module path from the worktree root -> OK.
- `python -B task-cycle/image_files_check.py task-cycle` -> `checked: 38 files, 0 listed`, exit 0.
- `python -B` parse of `task-cycle/image_files_check.py` with `ast.parse` -> ok.
- Manual: read `check_file` and the docstring of `task-cycle/private_paths_check.py` against the new docstring sentence -> they agree.
- Not run: the full gate (already running in this worktree, per the dispatch).
- Not run: the author's `python -B gate/run_tests.py task-cycle` (200 tests) and `foundation_check.py`. They are the author's claims; the range changes no code path, so the focused test above is enough.

## Reaches beyond the dispatch

- `task-cycle/private_paths_check.py` (docstring lines 30-40, `check_file` lines 107-120): to verify the claim about what the private-paths check skips.
- `foundations/invariants.md` entries `record-copy-image-check` and `record-copy-image-files`, and `foundations/decisions.md` WAY-316 to WAY-319, each read whole: to check for a mismatch with the code, as the dispatch asked.

## Searches not found or unclear

none
