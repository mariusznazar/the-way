"""Generator of the tracked copies of the definitions of the agent types of the-way's task cycle,
through which a session working on the-way itself reaches those types (WAY-127).

Usage, from the root of the-way:

    python -B agent-instructions/agent_type_copies.py [--write]

A definition is a file directly in `task-cycle/agent-types/` that `git ls-files --cached --others
--exclude-standard` lists and that exists on disk. Its name is `the-way-<words>.md`; its frontmatter
opens the file with `name:` equal to the file's name without `.md`, then `description:` on one line
that ends with the sentence every definition of the-way ends with. The generator produces a
byte-identical copy of each definition as `.claude/agents/<file name>`. The repository is the one
this script lies in, whatever the current directory, so a run from a product's `.the-way` writes
nothing into the product.

Without --write the generator prints what it would create or change and writes nothing; with
--write it writes those files. Either way it prints each file `the-way-*.md` under
`.claude/agents/` that no definition produces, for the author to remove with `git rm`; it deletes
nothing. A definition that breaks the form above, a file in the directory that is no definition, or
a failed git call stops the run before anything is written.

Exit code: 0 on success; 1 with `Error: <message>` on stderr otherwise.

Standard library only; the only program started is git.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from skill_entry_points import GeneratorError, git

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIRECTORY = "task-cycle/agent-types"
COPY_DIRECTORY = ".claude/agents"
PREFIX = "the-way-"
OWN_MARK = "Dispatched only by the task cycle of the-way."
NAME = re.compile(r"the-way-[a-z0-9]+(?:-[a-z0-9]+)*")
HEAD = re.compile(r"---\nname: ([^\n]*)\ndescription: ([^\n]*)\n")


def definition_paths(root: Path) -> list[str]:
    """Every path git lists below the source directory, sorted: tracked or untracked and not
    ignored, and present on disk."""
    listed = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--",
                 SOURCE_DIRECTORY + "/")
    paths = set()
    for raw in listed.split(b"\0"):
        if not raw:
            continue
        try:
            path = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise GeneratorError(f"a path git lists is not UTF-8: {raw!r}") from error
        if (root / path).is_file():
            paths.add(path)
    return sorted(paths)


def check_definition(path: str, data: bytes) -> None:
    """Stop with the first way the definition at `path` breaks the form."""
    stem = path.removeprefix(SOURCE_DIRECTORY + "/")
    if "/" in stem or not stem.endswith(".md") or not NAME.fullmatch(stem.removesuffix(".md")):
        raise GeneratorError(f"{path}: not a definition; its name must be `{PREFIX}<words>.md` "
                             f"directly in {SOURCE_DIRECTORY}/")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise GeneratorError(f"{path}: not UTF-8") from error
    if "\r" in text:
        raise GeneratorError(f"{path}: holds a carriage return; the file uses LF line ends")
    head = HEAD.match(text)
    if not head:
        raise GeneratorError(f"{path}: the file must open with `---`, a `name:` line and a "
                             "`description:` line, each on one line")
    name, description = head.groups()
    if name != stem.removesuffix(".md"):
        raise GeneratorError(f"{path}: name '{name}' is not the file's name without `.md`")
    if not description.endswith(OWN_MARK):
        raise GeneratorError(f"{path}: the description does not end with `{OWN_MARK}`")
    if ": " in description or " #" in description or description[0] in "-?:,[]{}#&*!|>'\"%@`":
        raise GeneratorError(f"{path}: description is not a safe plain YAML scalar")
    if "\n---\n" not in text[head.end() - 1:]:
        raise GeneratorError(f"{path}: the frontmatter is not closed by a `---` line")


def produce(root: Path) -> dict[str, bytes]:
    """Path from the repository root -> bytes, one copy per definition, in the order of paths."""
    produced: dict[str, bytes] = {}
    for path in definition_paths(root):
        data = (root / path).read_bytes()
        check_definition(path, data)
        produced[f"{COPY_DIRECTORY}/{path.removeprefix(SOURCE_DIRECTORY + '/')}"] = data
    return produced


def orphans(root: Path, produced: dict[str, bytes]) -> list[str]:
    """Every entry whose name starts with `the-way-` under the copy directory that no definition
    produces."""
    base = root / COPY_DIRECTORY
    if not base.is_dir():
        return []
    return [f"{COPY_DIRECTORY}/{child.name}"
            for child in sorted(base.iterdir(), key=lambda entry: entry.name)
            if child.name.startswith(PREFIX) and f"{COPY_DIRECTORY}/{child.name}" not in produced]


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the copies of the agent type definitions of the-way's task cycle.")
    parser.add_argument("--write", action="store_true",
                        help="write the copies; without it, print what would change")
    arguments = parser.parse_args(argv)
    try:
        produced = produce(root)
        changes = []
        for relative, data in produced.items():
            target = root / relative
            if not target.is_file():
                changes.append(("create", relative, target, data))
            elif target.read_bytes() != data:
                changes.append(("change", relative, target, data))
        left = orphans(root, produced)
        for kind, relative, target, data in changes:
            if arguments.write:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                print(f"{kind}d {relative}")
            else:
                print(f"would {kind} {relative}")
        for path in left:
            print(f"orphan {path}: no definition produces it; remove it with git rm -- {path}")
        if not changes and not left:
            print("agent type copies are current")
        return 0
    except (GeneratorError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
