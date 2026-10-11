# Install the-way in a product repository

This directory owns the first connection between a product repository and the-way. The installer
pins one commit of this repository, creates the five empty foundation files, makes thirteen skills
available to Claude Code and Codex in local and cloud sessions, gives both tools
the same guidance for working with the pinned process, and makes Git ignore the-way's records of a
run. It does not write product entries or start the product's task cycle. The `installation` part and its failure modes are in
`foundations/part_map.md`; WAY-09 describes its place in this repository and WAY-34 governs the pin.

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
| `foundations/invariants.md` | Empty invariant file with its required list tables. |
| `foundations/glossary.md` | Empty glossary with its required description. |
| `foundations/part_map.md` | Empty map with its required sections and table headers. |
| `foundations/environment_facts.md` | Empty fact file with its required withdrawn identifiers table. |
| `.claude/skills/the-way-*/SKILL.md` | Thirteen project skill entry points for Claude Code: the five foundation entry skills, `find-foundation-entries`, `define-project`, `plan-project`, `settle-technology`, `refine-task`, `implement-task`, `plan-task`, and `critique`. Each reads its source skill and referenced files from `.the-way` at the pinned commit, and sends work that skill hands to another the-way skill to the `the-way-` project skill of that name. |
| `.agents/skills/the-way-*/SKILL.md` | The same thirteen entry points for Codex, byte for byte. |
| `AGENTS.md` | The shared product guidance for Claude Code and Codex, between `<!-- the-way:begin -->` and `<!-- the-way:end -->`: initializing the submodule, using only the `the-way-*` skills, running the-way's scripts as `.the-way/<path>` on the product's files, the `--base` and `--merge-onto` commits, the empty part map's reports, and running the checks before a merge. It names no commit, so it changes only when the guidance changes. |
| `CLAUDE.md` | Created at the product root with the sole line `@AGENTS.md` when absent, so Claude Code receives the shared guidance and the product's other instructions in `AGENTS.md`. An existing file is preserved byte for byte. |
| `.gitignore` | The line `.runs/`. The invariants format guard requires the record of a run that a command names to be ignored by Git. |

The `implement-task` entry point requires Superpowers 6.4.1 and a harness that can dispatch
subagents. The installer creates its wrapper but does not install Superpowers; the skill checks
these prerequisites before starting a task cycle.

The product commits the gitlink, `.gitmodules`, the foundation files, the `.claude` and `.agents`
files, `AGENTS.md`, `CLAUDE.md` and `.gitignore` as one product change. The installer stages only
the two submodule paths; review and stage the other files in the product's normal workflow. A later process version enters the product through a
separate product task that moves the gitlink and updates its project skill entry points (WAY-34).
In that task, move the gitlink and the `.the-way` checkout to the new commit, delete the installed
wrappers in `.claude/skills/the-way-*/SKILL.md` and `.agents/skills/the-way-*/SKILL.md`, then
run the installer from a the-way checkout at the new commit with `--apply`. It recreates the
twenty-four wrappers for the new commit and leaves the foundation files as they are. Only when
migrating from an older pin that installed `.claude/rules/the-way.md`, remove that old rule in the
product task; the current installer neither writes nor deletes it. The installer creates root
`CLAUDE.md` if absent and preserves it if present. The block in `AGENTS.md` stays as it is unless
the guidance text changed between the two commits; then the installer stops on the block, and the task removes it, markers included, before
running the installer again. After the installer, run the format guard of every foundation file
and the product's tests with the new pin, and name the result in the request; a pin move that
changes no foundation file still changes the guards that judge them.

## Existing files and incomplete setup

An existing foundation file is preserved byte for byte. An existing project skill at a path
the installer owns is accepted only if its content matches; a different one stops the run.
An existing `AGENTS.md` without the markers gets the block appended after a blank line, and an
existing `.gitignore` without the exact line `.runs/` gets that line appended on a line of its own;
the existing content of both stays byte for byte, and the added lines use the file's own line
ending. An `AGENTS.md` that holds the same block, or a `.gitignore` that holds the line, is left
unchanged. The run stops when `AGENTS.md` holds a different block, only one of the markers, or two
blocks, and when either file is not a regular UTF-8 file. It also stops when Git ignores
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
An existing `.the-way` pin to another commit also stops the run. The installer never changes an
existing product entry to make it fit a template. Before adding a new submodule, an existing
`.gitmodules` must be tracked and clean; Git then adds the new section without replacing its
other sections.

An empty map has no parts to claim the product's tracked files. Its format is valid, but its
content check reports unassigned files until the product writes its first parts. The installer
does not treat that report as a successful product check, and the product guidance tells the agent
the report is expected.

After a fresh clone, run `git submodule update --init -- .the-way` before using the skills or
format guards. A cloud session must have read access to the Git URL in `.gitmodules`. If it cannot
fetch the pinned commit, the project skills and the guidance instruct the agent to stop rather than
use a personal copy of the-way.

## Check the installer

```text
python -B gate/run_tests.py installation
```

The tests use temporary Git repositories to check the preview, refusal, exact gitlink, repeated
run, preservation of existing files, a conflicting wrapper in either skill directory, the guidance
without a commit or a branch name and its commands on a main branch not called `main`, each case of
`AGENTS.md` and `.gitignore` above — created, appended with the lines the preview shows, kept, or
refused as a directory, as non-UTF-8 text or for its markers — the refusal of an ignored
`.the-way`, the four warnings, creation and preservation of root `CLAUDE.md`, effective import detection,
the absence of a generated Claude rule, empty file form,
the invariants guard accepting a record under `.runs/`, and initialization in a fresh checkout.
A symlinked `AGENTS.md` or `.gitignore` is refused by the same check as a directory but is not
tested, since creating a symlink needs extra rights on Windows. They
install this checkout's committed `HEAD`, so uncommitted changes to skills, templates or guards are
not exercised until they are committed.
