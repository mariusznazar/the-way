# Dispatch — foundation 1.8: the checks of two invariants (WAY-69)

You write the checks of two invariants of the-way. You wrote neither their sentences nor any code
they cover, and you must not read that code. The orchestrator (the session that sent you) runs this
under the owner's delegation; your questions go back to it in your final message, and it answers
from the sentences only. Commit nothing. Write files with the Write/Edit tools only.

**Write boundary:** create only
`C:\Storage\repos\the-way-instruction-files-part\agent-instructions\test_instruction_files.py`.

**What you may read** (nothing else in the repository beyond what these name, and never
`instruction-files/`, `.runs/`, `.superpowers/` other than this file and your brief, or any spec or plan):

- The two entries `instruction-file-imports/1` and `root-claude-md-import/1` in
  `C:\Storage\repos\the-way-instruction-files-part\foundations\invariants.md` (sentence, method, links).
- The glossary entry `repository instruction file` in `…\foundations\glossary.md` (the first
  sentence uses that term).
- The "Test" section of `C:\Storage\repos\the-way-process\elements\invariants\template.md` and the binding
  sentences of WAY-69 in `C:\Storage\repos\the-way-process\foundations\decisions.md`.
- The docstring of `…\gate\run_tests.py` (how a test cites its invariant) and, as the form of a test
  that finds its population with its own call to git and holds its expected values as literals,
  `…\gate\test_skills_reach_the_way_sessions.py`.
- Your brief: `C:\Storage\repos\the-way-instruction-files-part\reports\sdd\foundation-1.8-brief.md`
  ("Step 1" is your task; run "Step 2" yourself and report its output).

**What the test must do** (beyond the brief): every property the sentences state, with their literals —
the files covered (the test's own `git ls-files` in the root it checks; tracked `AGENTS.md`/`CLAUDE.md`
anywhere, plus the tracked Markdown files the root `AGENTS.md` or `CLAUDE.md` names by path as the
sentence defines naming: `.md` or `.markdown`, path from the repository root with `/` or `\` between
directories, with none of an ASCII letter or digit, `.`, `-`, `_`, `/`, `\` right before it); the
characters that may stand before a counted `@` (start of line, whitespace, `(`, `[`, `{`, `"`, `'`, `“`,
`‘`, `„`) and that a `.` or `/` must follow it before the next whitespace; the code-span rule (a run of
backticks to the next run of as many backticks on the same line) and the fence rule (a line whose first
non-space characters are three backticks or three tildes, to the next such line); the first-line
exception of the root `CLAUDE.md`; the byte-level start of the root `CLAUDE.md` (`@AGENTS.md` then `\n`,
`\r\n` or the end of the text), and nothing required where no root `CLAUDE.md` is tracked. Each citing
test asserts its `problems(root)` list empty, with a positive control that the population includes the
root `AGENTS.md`, `CLAUDE.md` and `agent-instructions/README.md`. Tests citing nothing, on temporary
`git init` repositories, show each `problems()` reporting every kind of violation its sentence names and
passing what it allows (code spans, fences, an address such as `a@example.com`, an untracked file, a
named file git does not track, a path preceded by a letter or `/`). Build fixtures only in temporary
directories; never write a tracked file named `AGENTS.md`, `CLAUDE.md` or `SKILL.md`.

**Return** as the text of your final message: the file written, the Step 2 output whole, and any
question (with what in the sentence left it open).
