# Task 3 — fix round 1 (findings and the controller's ruling)

The task review (opus) found the code exactly as the brief gave it, and one Critical finding that the
brief's own design causes. The controller rules on it (the spec is the authority; §4.6 requires that a
network path is never passed to the file system and that the run goes on with no traceback).

## Critical 1 — a file link to a network path makes the walk reach the network; an instruction-named one crashes the run

Reviewer's evidence (reproduced on this Windows machine with an unreachable test address):
- `instruction-files/check_instructions.py:139` calls `os.path.realpath(full)` on every
  instruction-named link; on Windows this opens the link's target. `AGENTS.md` linked to
  `\\192.0.2.1\share\x.md`: 40 s of network attempts, then `OSError: [WinError 64]` from `realpath`,
  a traceback, exit 1.
- `:115` `os.walk` sorts entries with `entry.is_dir()`, which follows links: any file link anywhere in
  the tree is looked up through its target (a link `notes.txt` to the same address: 20 s of attempts).

**Ruling (the fix to make):**
1. Replace `os.walk` in `instruction_files` with the script's own walk over `os.scandir`, using
   `entry.is_dir(follow_symlinks=False)`, `entry.is_symlink()` and `entry.is_junction()` — no call that
   follows a link while walking. Keep today's behaviour and findings for directory links and junctions
   (`walk` INFO "a link to a directory, not followed"), for directories that cannot be listed, for
   `SKIP_DIRS` and nested repositories (a nested repository's `.git` is detected without following a
   link: `os.path.lexists` / `os.lstat`, not `os.path.exists`).
2. For a file link found by the walk, decide whether it stays inside the root **without opening
   anything**: follow the chain with `os.readlink`, at most a fixed number of hops (e.g. 8), resolving
   each relative target against the link's directory with `os.path.normpath`, never calling
   `realpath`, `exists`, `stat` or `open` on a target. A target that is network-shaped after `/` → `\`
   normalisation (starts with `\\` or `\??\`, including `\\?\UNC\` and `\\.\`), absolute outside the
   root, outside the root after resolution, or a chain longer than the limit is "a link out of the
   repository" — reported as the existing `read` INFO and neither read nor listed, its target never
   touched. Only a chain that ends inside the root is read, through the existing `read_text`.
3. Any `OSError` while resolving a link becomes a `read` WARN "cannot be read: <reason>" (through
   `reason()`), and the run goes on.
4. `--file` keeps its behaviour (read through its link, as today) — a file the user names is the
   user's choice; but a `--file` value that is network-shaped is refused like a token (usage error,
   exit 2), so the script never opens a network path.

**Tests to add (test first, see them fail on the current code):**
- a file link named `AGENTS.md` whose target is `\\192.0.2.1\share\x.md` (and one `notes.txt` with the
  same target): with `os.stat`, `os.lstat`, `os.path.realpath`, `os.path.exists`, `os.path.isdir`,
  `os.scandir`'s entries' following calls and `open` wrapped so that any call receiving a
  network-shaped path fails the test, the run ends with exit 0, the link reported as out of the
  repository, and no such call made. Create the link with `os.symlink` where allowed; skip with the
  reason where links cannot be made (as the existing link tests do).
- a chain of links that leaves the root after two hops → out of the repository, not read;
- a chain longer than the hop limit → out of the repository, not read;
- a nested repository whose `.git` is a link → still treated as a nested repository, its target not
  looked up.

## Minor items fixed in the same round (controller's choice: cheap, in this file)

- `test_check_instructions.py:341-342, :365, :368, :371` hold literal U+FEFF and U+202E: write them as
  `"﻿"` and `"‮"` (same behaviour, visible to a reader and to GitHub).
- `check_instructions.py:182`: a decode error in the last bytes of a cut file counts as a split
  character only when it is the end of the data (`error.reason == "unexpected end of data"`, or an
  incremental decode with `final=False`); a real invalid byte such as `\xff` near the cut stays
  "not UTF-8 text". Add a test for `\xff` in the last three bytes of a file over 1 MiB.

## Deferred (ledger, for the final review)

`shown()` may cut through an escape (cosmetic); only `MAIN_NAMES` directories reported as directories;
stat/open race to a FIFO; `--file` without read permission untested; FIFO test would hang on a
regression; three blank lines before `def check`.

## Constraints

Edit only `instruction-files/check_instructions.py` and `instruction-files/test_check_instructions.py`,
with the Write/Edit tools (never a shell heredoc, printf or python -c — they collapse backslashes).
Keep every name Task 3's brief lists under "Produces" with its signature (Tasks 4 and 5 use them).
Python 3.14 standard library only; no program started; nothing written by the script. Commit by
paths, message in the repository's style ending with the line
`Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ`. Run
`python -B gate/run_tests.py instruction-files` and the script on the-way
(`python -B instruction-files/check_instructions.py .`). Append a fix report to `task-3-report.md`:
the RED and GREEN commands and output, what changed, the covering tests.
