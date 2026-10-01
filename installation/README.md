# Install the-way in a product repository

This directory owns the first connection between a product repository and the-way. The installer
pins one commit of this repository, creates the five empty foundation files, makes the five
foundation skills available to Claude Code and Codex in local and cloud sessions, gives both tools
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
  and the guidance from `.claude/rules/the-way.md`; Codex reads the same skills from
  `.agents/skills/` and the same guidance from the product's root `AGENTS.md`.

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
| `.claude/skills/the-way-*/SKILL.md` | Five project skill entry points for Claude Code, with names distinct from personal skills. Each reads the skill, template, and shared rules from `.the-way` at the pinned commit, and sends work that the skill hands to another the-way skill to the `the-way-` project skill of that name. |
| `.agents/skills/the-way-*/SKILL.md` | The same five entry points for Codex, byte for byte. |
| `.claude/rules/the-way.md` | The product guidance for Claude Code: initializing the submodule, using only the `the-way-*` skills, running the-way's scripts as `.the-way/<path>` on the product's files, the `--base` and `--merge-onto` commits, the empty part map's reports, and running the checks before a merge. It names no commit, so it changes only when the guidance changes. |
| `AGENTS.md` | The same guidance for Codex, between `<!-- the-way:begin -->` and `<!-- the-way:end -->`. |
| `.gitignore` | The line `.runs/`. The invariants format guard requires the record of a run that a command names to be ignored by Git. |

The product commits the gitlink, `.gitmodules`, the foundation files, the `.claude` and `.agents`
files, `AGENTS.md` and `.gitignore` as one product change. The installer stages only the two submodule paths; review and stage the other
files in the product's normal workflow. A later process version enters the product through a
separate product task that moves the gitlink and updates its project skill entry points (WAY-34).
In that task, move the gitlink and the `.the-way` checkout to the new commit, delete the ten
wrappers in `.claude/skills/the-way-*/SKILL.md` and `.agents/skills/the-way-*/SKILL.md` and
`.claude/rules/the-way.md`, then run the installer from a the-way checkout at the new commit with
`--apply`. It recreates those eleven files for the new commit and leaves the foundation files as
they are. The block in `AGENTS.md` stays as it is unless the guidance text changed between the two
commits; then the installer stops on the block, and the task removes it, markers included, before
running the installer again.

## Existing files and incomplete setup

An existing foundation file is preserved byte for byte. An existing project skill or rule at a
path the installer owns is accepted only if its content matches; a different one stops the run.
An existing `AGENTS.md` without the markers gets the block appended after a blank line, and an
existing `.gitignore` without the exact line `.runs/` gets that line appended on a line of its own;
the existing content of both stays byte for byte, and the added lines use the file's own line
ending. An `AGENTS.md` that holds the same block, or a `.gitignore` that holds the line, is left
unchanged. The run stops when `AGENTS.md` holds a different block, only one of the markers, or two
blocks, and when either file is not a regular UTF-8 file. Every refusal happens before anything is
written. The preview warns when an `AGENTS.override.md` at the root would hide `AGENTS.md` from
Codex, or when `AGENTS.md` would exceed the 32 KiB Codex reads.
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
run, preservation of existing files, both wrapper locations, the guidance without a commit, each
case of `AGENTS.md` and `.gitignore`, empty file form, the invariants guard accepting a record
under `.runs/`, and initialization in a fresh checkout. They
install this checkout's committed `HEAD`, so uncommitted changes to skills, templates or guards are
not exercised until they are committed.
