# Install the-way in a product repository

This directory owns the first connection between a product repository and the-way. The installer
pins one commit of this repository, creates the five empty foundation files, and makes the five
foundation skills available to Claude Code in local and cloud sessions. It does not write product
entries or start the product's task cycle. The `installation` part and its failure modes are in
`foundations/part_map.md`; WAY-09 describes its place in this repository and WAY-34 governs the pin.

## Requirements

- Python 3.14, as declared by `.python-version` (WAY-38), and Git on `PATH`.
- A Git repository for the product, with a reachable root directory.
- A Git URL from which the selected the-way commit can be fetched. By default this is this
  checkout's `origin`; `--url` selects another URL. The URL is stored in the product's
  `.gitmodules`, so it must work on every machine and cloud session that uses the product.

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
contents of new files. The second prints the same plan and asks for `y` before writing. A
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
| `.claude/skills/the-way-*/SKILL.md` | Five project skill entry points with names distinct from personal skills. Each reads the skill, template, and shared rules from `.the-way` at the pinned commit. |
| `.claude/rules/the-way.md` | Tells Claude Code to use those project skills and to initialize the submodule after a fresh clone. |

The product commits the gitlink, `.gitmodules`, the foundation files, and the `.claude` files as
one product change. The installer stages only the two submodule paths; review and stage the other
files in the product's normal workflow. A later process version enters the product through a
separate product task that moves the gitlink and updates its project skill entry points (WAY-34).
In that task, move the gitlink and the `.the-way` checkout to the new commit, delete the five
`.claude/skills/the-way-*/SKILL.md` files and `.claude/rules/the-way.md`, then run the installer
from a the-way checkout at the new commit with `--apply`. It recreates those six files for the new
commit and leaves the foundation files as they are.

## Existing files and incomplete setup

An existing foundation file is preserved byte for byte. An existing project skill or rule at a
path the installer owns is accepted only if its content matches; a different one stops the run.
An existing `.the-way` pin to another commit also stops the run. The installer never changes an
existing product entry to make it fit a template. Before adding a new submodule, an existing
`.gitmodules` must be tracked and clean; Git then adds the new section without replacing its
other sections.

An empty map has no parts to claim the product's tracked files. Its format is valid, but its
content check reports unassigned files until the product writes its first parts. The installer
does not treat that report as a successful product check.

After a fresh clone, run `git submodule update --init -- .the-way` before using the skills or
format guards. A cloud session must have read access to the Git URL in `.gitmodules`. If it cannot
fetch the pinned commit, the project skills instruct the agent to stop rather than use a personal
copy of the-way.

## Check the installer

```text
python -B gate/run_tests.py installation
```

The tests use temporary Git repositories to check the preview, refusal, exact gitlink, repeated
run, preservation of existing files, empty file form, and initialization in a fresh checkout. They
install this checkout's committed `HEAD`, so uncommitted changes to skills, templates or guards are
not exercised until they are committed.
