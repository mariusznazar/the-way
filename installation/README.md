# Install the-way in a product repository

This directory owns the first connection between a product repository and the-way. The installer
pins one commit of this repository, creates the five empty foundation files, makes its project skills
available to Claude Code and Codex in local and cloud sessions, gives both tools
the same guidance for working with the pinned process, and makes Git ignore the working files of
the-way's skills. It does not write product entries or start the product's task cycle. The
`installation` part is in `foundations/part_map.md`; WAY-09 describes its place in this repository
and WAY-34 governs the pin.

## Requirements

- Python 3.14, as declared by `.python-version` (WAY-38), and Git on `PATH`.
- A Git repository for the product, with a reachable root directory.
- A Git URL from which the selected the-way commit can be fetched. By default this is this
  checkout's `origin`; `--url` selects another URL. The URL is stored in the product's
  `.gitmodules`, so it must work on every machine and cloud session that uses the product. While
  the-way is private, each of them needs read access to it.
- Claude Code or Codex as the agent. Claude Code reads the project skills from `.claude/skills/`
  and imports the product's root `AGENTS.md` through root `CLAUDE.md`; Codex reads the same
  skills from `.agents/skills/` and the shared guidance from root `AGENTS.md`.

The installer uses Python's standard library and Git. It calls no shell and installs no package.
Its paths and subprocess arguments do not depend on PowerShell, Bash, or a particular operating
system. The repository's tests exercise it on a separate Git repository; a platform is covered
only when those tests run there.

## Use

From any working directory, with this repository checked out at the commit the product is to use:

```text
python -B <the-way>/installation/install.py <product-repository>
python -B <the-way>/installation/install.py <product-repository> --apply
```

The first command only prints the commit, submodule URL, and proposed changes, including the
contents of new files and the lines added to existing ones. The second prints the same plan and asks for `y` before writing. A
noninteractive run without an answer stops. `--help` lists the arguments.

The script pins this checkout's `HEAD`, not a moving branch. It verifies that the selected commit
can be fetched from the URL before changing the product. A local checkout ahead of its remote can
be used for a local test with `--url <local-the-way-path>`; that URL is unsuitable for a product
used on other machines or in the cloud. Git refuses local paths in submodules by default, so the
installer allows Git's file protocol only when the URL is a local path or a `file://` URL.

## Files in the product

| Path | Purpose |
|---|---|
| `.gitmodules` and `.the-way` | A Git submodule whose gitlink records the exact the-way commit. Git stages these two paths when it adds the submodule. |
| `foundations/decisions.md` | Empty decision log. |
| `foundations/invariants.md` | Empty invariant file with its withdrawn identifiers table. |
| `foundations/glossary.md` | Empty glossary with its required description. |
| `foundations/part_map.md` | Empty map with its external context, files left out on purpose and withdrawn identifiers tables. |
| `foundations/environment_facts.md` | Empty fact file with its required withdrawn identifiers table. |
| `.claude/skills/the-way-*/SKILL.md` | Project skill entry points for Claude Code: the five foundation entry skills, `find-foundation-entries`, `define-project`, `plan-project`, `lead-project`, `settle-technology`, `refine-task`, `implement-task`, `plan-task`, `write-spec`, `make-change`, `review-change`, `critique`, `maintain-styleguide`, `maintain-coding-guidelines`, and `maintain-testing-guidelines`. Each checks that the gitlink and the `.the-way` checkout show the same commit, reads its source skill from `.the-way` and each file the skill names there when the step that names it comes, then sends work that skill hands to another the-way skill to the `the-way-` project skill of that name. It names no commit. The installer owns it and rewrites it when the pin moves; do not edit it by hand. |
| `.agents/skills/the-way-*/SKILL.md` | The same entry points for Codex, byte for byte. |
| `AGENTS.md` | The shared product guidance for Claude Code and Codex, between `<!-- the-way:begin -->` and `<!-- the-way:end -->`: initializing the submodule, using only the `the-way-*` skills, the-way's methods in a task cycle even where a plugin offers its own, running the-way's scripts as `.the-way/<path>`, the empty part map's report and the skill that writes the first map, and running the product's tests with its one command before a merge, `elements/common/foundation_check.py` among them, or that check on its own while the command does not run it. It names no commit. The installer owns the block and rewrites it in place when the pin moves; do not edit it by hand, and keep the product's own instructions outside the markers. |
| `CLAUDE.md` | Created at the product root with the sole line `@AGENTS.md` when absent, so Claude Code receives the shared guidance and the product's other instructions in `AGENTS.md`. An existing file is preserved byte for byte. |
| `.gitignore` | The line `.runs/`, under which the-way's skills keep their working files: a task cycle's record, the reports of research and the conversation of a project's refinement. |

The `implement-task` entry point requires a harness that can dispatch subagents; the skill checks
it before starting a task cycle. The methods the cycle uses are skills of the-way, installed with
it.

The product commits the gitlink, `.gitmodules`, the foundation files, the `.claude` and `.agents`
files, `AGENTS.md`, `CLAUDE.md` and `.gitignore` as one product change. The installer stages only
the two submodule paths; review and stage the other files in the product's normal workflow.

The installer does not change the product's tests. The product adds
`python -B .the-way/elements/common/foundation_check.py`, run from its root, to the one command
that runs all its tests (WAY-16). Until it does, the guidance in `AGENTS.md` tells the agent to run
the check on its own and to report that the one command leaves it unchecked.

## Moving the pin

A later version of the process enters the product only when the product moves its pin (WAY-34).
The move is one commit, made when a task of the product needs a change of the process, or in a
step of its own that takes several changes of the-way at once — not after every change of the-way.
In a task cycle the move is the task branch's first commit, made before the cycle chooses its route,
so the whole cycle works under the new commit (step 2 of `task-cycle/skill/SKILL.md`).
It takes one command, run from a checkout of the-way at the commit the product is to use, once
that commit is published where the URL in `.gitmodules` reaches it:

```text
python -B <the-way>/installation/install.py <product-repository>
python -B <the-way>/installation/install.py <product-repository> --apply
```

The first prints what the move changes, and says when the commit is older than the pin; the second
prints it again and asks for `y`. The URL is that checkout's `origin` unless `--url` names another;
it must be the one `.gitmodules` holds. The installer stops before writing when `.the-way` holds
uncommitted changes to files git tracks, and names them; it warns about files git does not track
there, which the move keeps. It checks that the commit can be fetched from that URL, checks it out
in `.the-way` and stages the gitlink. It rewrites what it owns to match the new commit: its block in
`AGENTS.md`, where the block stands, and the skill entry points in both tool directories. It
creates the entry points of skills the commit adds and deletes those of skills the commit no longer
has. An entry point is its own, whatever commit wrote it, when its header names the skill of its
directory, its description ends with "Use this product's pinned the-way commit." and it points to
`.the-way`. It leaves the foundation
files, root `CLAUDE.md` and every other file as they are, and stops before writing on a file at an
entry point's path that is not its own. Commit the gitlink together with everything the installer
rewrote; where nothing reads differently at the new commit, the gitlink is the only change. The
block and the entry points are generated: an edit by hand is lost at the next move. Only when
moving from an older pin that installed `.claude/rules/the-way.md`, remove that old rule; the
installer neither writes nor deletes it.

Moving the pin changes the product's test command: `foundation_check.py`, and every other script
of the-way that command runs, now comes from the new commit and may judge the same files
differently. Run the product's tests with the new pin and name the result in the request. A
foundation in the form of an earlier the-way is brought to the current form with
`python -B .the-way/elements/common/migrate_foundation.py`.

## Existing files and incomplete setup

An existing foundation file is preserved byte for byte. A file at an entry point's path is
rewritten when it is the installer's own entry point and stops the run otherwise.
An existing `AGENTS.md` without the markers gets the block appended after a blank line, and an
existing `.gitignore` without the exact line `.runs/` gets that line appended on a line of its own;
the existing content of both stays byte for byte, and the added lines use the file's own line
ending. An `AGENTS.md` that holds the same block, or a `.gitignore` that holds the line, is left
unchanged; one that holds a different block gets it rewritten where it stands, in the file's own
line ending. The run stops when `AGENTS.md` holds only one of the markers or two blocks, and when
either file is not a regular UTF-8 file. It also stops when Git ignores
`.the-way` while the submodule is still to be added, since `git submodule add` refuses an ignored
path. Every refusal happens before
anything is written. The plan, shown both in the preview and before the `--apply` confirmation, warns when Git
ignores a path the installer writes — through `.gitignore` or any other ignore source Git applies —
since such a file cannot be committed and other clones and cloud sessions never get it; it warns
when an `AGENTS.override.md` at the root would hide `AGENTS.md` from Codex, and when `AGENTS.md`
would exceed the 32 KiB Codex reads. It also warns when an existing root `CLAUDE.md` has no
effective `@AGENTS.md` import: add the import by hand so Claude Code receives the shared
instructions. A mention inside a Markdown code span or fenced code block does not count as an
import, nor does an import followed immediately by punctuation. A warning does not stop the run.
An existing `CLAUDE.md` must be a regular UTF-8 file; otherwise the run stops before writing.
An existing `.the-way` pin to another commit is moved, as "Moving the pin" gives; a `.the-way`
checkout that differs from its gitlink stops the run. The installer never changes an
existing product entry to make it fit a template. Before adding a new submodule, an existing
`.gitmodules` must be tracked and clean; Git then adds the new section without replacing its
other sections.

An empty map has no parts to claim the product's tracked files, so
`elements/common/foundation_check.py`, and with it the product's tests, reports each of them as
claimed by no part until the product writes its first parts with `the-way-update-part-map`. The
installer does not treat that report as a successful product check, and the product guidance tells
the agent the report is expected and which skill writes the first map.

After a fresh clone, run `git submodule update --init -- .the-way` before using the skills or
scripts. A cloud session must have read access to the Git URL in `.gitmodules`. If it cannot
fetch the pinned commit, the project skills and the guidance instruct the agent to stop rather than
use a personal copy of the-way.

## Check the installer

```text
python -B gate/run_tests.py installation
```

The tests use temporary Git repositories to check the preview, refusal, exact gitlink, repeated
run, preservation of existing files, a conflicting wrapper in either skill directory, entry points
and guidance without a commit, guidance naming only scripts the pinned commit holds, a moved
pin — the gitlink alone where nothing else reads differently, and otherwise the block rewritten in
place, every entry point rewritten, one created for an added skill and one deleted for a removed
skill, with the product's own skill kept —, a preview of a move that changes nothing, a move
refused for uncommitted changes in `.the-way` or for a commit its URL does not reach, a move back
named as older than the pin, its own entry point rewritten and a file lacking a mark of one kept,
the Codex limit counted on a rewritten `AGENTS.md`, each case of
`AGENTS.md` and `.gitignore` above — created, appended with the lines the preview shows, kept,
rewritten in place, or refused as a directory, as non-UTF-8 text or for its markers — the refusal
of an ignored `.the-way`, the four warnings, creation and preservation of root `CLAUDE.md`, effective import detection,
the absence of a generated Claude rule, the empty files in the current form with the foundation
check's report on them, the `maintain-styleguide` entry points and the foundation check the block
names, the `maintain-coding-guidelines` and `maintain-testing-guidelines` entry points and the refusal of a conflicting file, a
directory or a non-UTF-8 file at their path in either skill directory, and initialization in a
fresh checkout.
A symlinked `AGENTS.md` or `.gitignore` is refused by the same check as a directory but is not
tested, since creating a symlink needs extra rights on Windows. They
install this checkout's committed `HEAD`, so uncommitted changes to skills, templates or scripts
are not exercised until they are committed.
