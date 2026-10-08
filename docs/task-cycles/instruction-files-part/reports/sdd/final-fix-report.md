# Final fix wave report

Files touched: `instruction-files/SKILL.md`, `check_instructions.py`, `test_check_instructions.py`,
`principles.md`, `tool_loading.md`. Nothing under `foundations/` or `agent-instructions/`.

RED run (new tests, before the code change): 104 tests, 5 failures and 8 errors, all in the new tests
(near-miss phrases x3 subtests, skill-dir message, NetworkShapesOffWindows x8: `PLATFORM` missing).
GREEN run after: `instruction-files` 104 tests OK (5 skipped, Windows-only); `agent-instructions` 18 OK;
`skill_entry_points.py` prints `entry points are current`; the script on the-way: 0 error, 1 warn, 3 info.

1. **SKILL.md, which copy governs.** Check 1 now goes on only when the superproject printed is the
   repository under review (or the review is `--file` only); another repository falls through to check 2.
   Check 2, after the `ls-files --stage` line, tests in order: `.the-way/` empty (not initialised);
   `rev-parse HEAD` differs from the pin (stop, `git submodule update`); `cat-file -e <hash>:instruction-files/SKILL.md`
   fails (the pin lacks the directory). An empty `ls-files` line says the repository pins no the-way and
   this copy governs. Procedure text; no test.
2. **Near-miss phrases.** `check_instructions.py`: `\b` appended to every phrase except the
   prefix `nie jest wczytywan` (new `PREFIX_PHRASES`). Tests `test_a_near_miss_of_a_phrase_keeps_a_dead_path_a_warning`
   (is not ready / is not readable / does not readily / Nie czytaj ...) RED then GREEN;
   `test_the_prefix_phrase_still_matches_every_ending` and the wrapped memory sentence stay INFO.
3. **Network shapes off Windows.** New module value `PLATFORM = sys.platform` beside `WINDOWS`;
   `network_shaped`: Windows, cygwin, msys keep the old rule; other POSIX: `posixpath.normpath` form with
   exactly two leading slashes; darwin also `/net/` and `/Network/`. Tokens get the existing INFO, a root
   or `--file` the usage error (same function). Class `NetworkShapesOffWindows` (6 tests, platform patched,
   lookups guarded and failing on any network-shaped path) RED (PLATFORM missing) then GREEN.
   Docstring corrected; says what is not guarded (mapped drive letter or mount point is looked up).
4. `tool_loading.md`: "Not read as project instructions:"; script WARN now "not documented as read by
   Claude Code; give it a copy in .claude/skills" (test added).
5. `principles.md`: `codex --ask-for-approval never "Summarize the current instructions."`.
6. `principles.md`: "Codex and Cursor read it in a trusted project".
7. Backticks-only following stated in the script docstring and `principles.md` (checks list), with the
   glossary term and invariant counting a path anywhere in the text.
8. `tool_loading.md`: re-read https://code.claude.com/docs/en/memory. User-level rules now "applies to
   every project and loads before project rules". `~/.claude/CLAUDE.md` is named in § Choose where to put
   CLAUDE.md files (personal preferences for all projects, before project files in load order); § How
   CLAUDE.md files load does not name it, so "loads at session start" is stated as not established, and
   it left the "At session start" bullet.
9. `principles.md`: "a linter, CI, or a local hook only against slips".

## Settlement

- (a) `principles.md` head: added "Sections that name no decision are the skill's own method, offered as
  proposals, not rules that bind a repository; the sections that cite WAY-128 to WAY-133 are what the-way adopted."
- (b) `tool_loading.md`: new bullet "`@path` right after a hyphen (for example `-@x.md`): whether Claude Code
  imports it is not established."
- (c) `check_instructions.py` docstring: states an `@` import is reported only when the word after the `@`
  holds a `.` or `/`; the invariant `instruction-file-imports` counts every word-initial `@` followed by non-whitespace.
- (d) docstring: "never looks a network path up" -> "looks up no network path it has recognised"; added that
  link targets are judged without following the link on Windows only, and on Cygwin, MSYS2 and macOS a symlink
  target is followed, so a link to a network location there is not guarded.
- (e) `NetworkShapesOffWindows`: new `stub_lookup` (records the argument of `lexists`, returns False); the
  three-slash/one-slash test and the mapped-drive test use it and assert the lookup happened (before: real `lexists`).
- Results: instruction-files 104 OK (5 skipped); entry points current; script on the-way 0 error, 1 warn, 3 info.
- Review fixes: principles head now per principle ("Principles that name no decision ... those that cite one are what the-way adopted"); two docstring paragraphs of check_instructions.py rewrapped to 100 columns, no wording change.
