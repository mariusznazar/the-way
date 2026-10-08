# Final fix wave — the complete findings list (one dispatch)

The final whole-branch review (opus) of 252152a..c60f3ea: Ready with fixes; no Critical; all 17
deliberate breaks behave as the sentences predict. Fix everything below in one pass, test first where
behaviour changes. Files: `instruction-files/SKILL.md`, `instruction-files/check_instructions.py`,
`instruction-files/test_check_instructions.py`, `instruction-files/principles.md`,
`instruction-files/tool_loading.md`. Never touch `foundations/` or `agent-instructions/`.

## Important

1. **The skill can judge a product under a copy other than that product's pinned commit**
   (`SKILL.md:16-30`; WAY-127 as narrowed, WAY-34).
   - Check 1 "go on" only when the superproject it prints is the repository under review, or the review
     is `--file` only; otherwise fall through to check 2 (a session in product A judging product B must
     follow B's pin, not A's).
   - Check 2, after the `ls-files --stage` line: compare `git -C <repository>/.the-way rev-parse HEAD`
     with the pinned hash; if `.the-way/` is empty → the submodule is not initialised (the human
     initialises it); if HEAD differs from the pin → stop: the submodule is not at its pin (the human runs
     `git submodule update`); only then `cat-file -e <pinned hash>:instruction-files/SKILL.md` failing →
     the pin lacks the directory (the product moves its pin first).
2. **Near-miss phrases lower really dead paths to INFO** (`check_instructions.py:55-63`): append `\b`
   to every phrase except the deliberate prefix `nie jest wczytywan`. Tests (failing first): "is not
   ready", "is not readable", "does not readily", and "Nie czytaj tego pliku, otwórz `docs/zasady/styl.md`."
   each keep a dead path at WARN; the wrapped memory sentence still gives INFO.
3. **Off Windows, two common setups reach the network** (`check_instructions.py:64, 126-129, 144-145,
   177-178, 412-416`; docstring line 21). Guard, do not only document:
   - Python on Cygwin or MSYS2 (`sys.platform in ("cygwin", "msys")`) is judged like Windows for
     network shapes;
   - on any POSIX, a path whose normalised form starts with exactly `//` (two slashes, not three) is
     network-shaped;
   - on macOS (`sys.platform == "darwin"`), a path starting `/net/` or `/Network/` is network-shaped;
   - a network-shaped token gets the existing INFO "network path, not checked"; a network-shaped ROOT or
     `--file` the existing usage error;
   - make the platform decision testable (module-level values the tests patch) and test each rule
     offline (no lookup reaches the file system: the existing `guard_network_paths`);
   - correct the module docstring to what the code guards, and name what it does not (a drive letter or
     a mount point the user mapped to a share is looked up — the user chose that server).

## Minor (fix in the same pass)

4. `tool_loading.md:27-28`: "Not read **as project instructions**: …"; and the check script's WARN
   "Claude Code does not read .agents/skills" (`check_instructions.py:620`) becomes "not documented as
   read by Claude Code; give it a copy in .claude/skills" (the test asserts the check name; update any
   test asserting the message).
5. `principles.md:213`: use the documented Codex command `codex --ask-for-approval never "Summarize the
   current instructions."`, as `tool_loading.md` does.
6. `principles.md:132`: "Codex and Cursor always read it" → "read it in a trusted project".
7. `check_instructions.py` docstring (around :8 and fix D at :541-556) and `principles.md:205`: say that
   the script follows only files the root files name **in backticks**, while the glossary term and the
   invariant count a file named by its path anywhere in the text.
8. `tool_loading.md`: the "loads at launch" statement under § User-level rules of the Claude Code memory
   page — reword to what that section says ("applies to every project; loads before project rules"),
   re-reading the section at https://code.claude.com/docs/en/memory; cite `~/.claude/CLAUDE.md` to the
   section of that page that names it (re-read; if none names it, say "not established").
9. `principles.md:250`: "a linter, a hook, CI" → "a linter, CI, or a local hook only against slips".

## Not changed (controller's rulings, for the record)

- WAY-132's *Rejected* clause on the interactive notice: the public memory page (the source of fact
  `claude-code-agents-md`) states the notice; a foundation entry is not reopened in this wave.
- The invariant checks' positive control failing when the root `CLAUDE.md` is untracked: the checks are
  read-only (WAY-03); recorded as a reading.
- Task point 5's partial answer: stated in the request.

## Rules

Write/Edit tools only. Python 3.14 standard library; the script starts no program, writes nothing.
Run `python -B gate/run_tests.py instruction-files` (seconds), `python -B gate/run_tests.py
agent-instructions`, `python -B agent-instructions/skill_entry_points.py` (must print `entry points are
current`), and the script on the-way (expected 0 error, 1 warn, 3 info). Commit by paths (one or more
commits), messages in the repository's style ending with
`Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ`. No background process left.
Write the full report to `C:\Storage\repos\the-way-instruction-files-part\reports\sdd\final-fix-report.md`
(each finding: what changed, sentence or code before and after, covering tests with RED and GREEN
output). Reply with the short status contract.
