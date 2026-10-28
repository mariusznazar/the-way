"""Generator of the project skill entry points through which a session working on the-way itself
reaches the-way's own skills (WAY-127).

Usage, from the root of the-way:

    python -B agent-instructions/skill_entry_points.py [--write]

A skill of the-way is a file `SKILL.md` that `git ls-files --cached --others --exclude-standard`
lists in this repository outside `.claude/` and `.agents/`, and that exists on disk. From its
frontmatter the generator takes `name:` and `description:`, each on one line, and produces
`.claude/skills/the-way-<name>/SKILL.md` for Claude Code and a byte-identical
`.agents/skills/the-way-<name>/SKILL.md` for Codex. The repository is the one this script lies in,
whatever the current directory, so a run from a product's `.the-way` writes nothing into the
product.

Without --write the generator prints what it would create or change and writes nothing; with
--write it writes those files, UTF-8 with LF line ends. Either way it prints each directory
`the-way-*` under `.claude/skills/` or `.agents/skills/` that no skill produces, for the author to
remove with `git rm -r`; it deletes nothing. A malformed frontmatter, a name two skills hold, or a
failed git call stops the run before anything is written.

Exit code: 0 on success; 1 with `Error: <message>` on stderr otherwise.

Standard library only; the only program started is git.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRY_DIRECTORIES = (".claude/skills", ".agents/skills")
PREFIX = "the-way-"
SUFFIX = " Use this checkout's own the-way."
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
BLOCK_SCALAR = re.compile(r"[|>][-+0-9]*")
UNSAFE_START = "-?:,[]{}#&*!|>'\"%@`"
FIELD = re.compile(r"(name|description):(.*)")


class GeneratorError(Exception):
    """A skill or the repository keeps the entry points from being produced."""


@dataclass(frozen=True)
class Skill:
    path: str          # from the repository root, with `/`, e.g. "task-cycle/skill/SKILL.md"
    name: str          # e.g. "implement-task"
    description: str   # the frontmatter's one-line description, as written


def git(root: Path, *arguments: str) -> bytes:
    try:
        completed = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True,
                                   check=False)
    except OSError as error:
        raise GeneratorError(f"git cannot run: {error}") from error
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", "replace").strip()
        raise GeneratorError(f"git {' '.join(arguments)} failed: {message}")
    return completed.stdout


def skill_paths(root: Path) -> list[str]:
    """Every skill's path, sorted, as git lists it: tracked or untracked and not ignored, outside
    `.claude/` and `.agents/`, and present on disk."""
    listed = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--",
                 ":(glob)**/SKILL.md")
    paths = set()
    for raw in listed.split(b"\0"):
        if not raw:
            continue
        try:
            path = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise GeneratorError(f"a path git lists is not UTF-8: {raw!r}") from error
        if path.startswith((".claude/", ".agents/")):
            continue
        if (root / path).is_file():
            paths.add(path)
    return sorted(paths)


def frontmatter(path: str, text: str) -> dict[str, str]:
    """The first `name:` and `description:` between the file's first two `---` lines."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise GeneratorError(f"{path}: no frontmatter between the first two '---' lines")
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if end is None:
        raise GeneratorError(f"{path}: no frontmatter between the first two '---' lines")
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        found = FIELD.fullmatch(line)
        if found and found.group(1) not in fields:
            fields[found.group(1)] = found.group(2).strip()
    return fields


def read_skill(root: Path, path: str) -> Skill:
    try:
        text = (root / path).read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise GeneratorError(f"{path}: not UTF-8") from error
    fields = frontmatter(path, text)
    for field in ("name", "description"):
        value = fields.get(field, "")
        if not value:
            raise GeneratorError(f"{path}: frontmatter has no '{field}:' with a value")
        if BLOCK_SCALAR.fullmatch(value):
            raise GeneratorError(f"{path}: {field} is not on one line")
    description = fields["description"]
    if (description[0] in UNSAFE_START or ": " in description or " #" in description
            or description.endswith(":")):
        raise GeneratorError(f"{path}: description is not a safe plain YAML scalar")
    name = fields["name"]
    if not NAME.fullmatch(name):
        raise GeneratorError(f"{path}: name '{name}' is not lowercase words joined by hyphens")
    if name.startswith(PREFIX):
        raise GeneratorError(f"{path}: name '{name}' already starts with '{PREFIX}'")
    return Skill(path, name, fields["description"])


def discover(root: Path) -> list[Skill]:
    """Every skill of the repository at `root`, sorted by path."""
    skills: list[Skill] = []
    holders: dict[str, str] = {}
    for path in skill_paths(root):
        skill = read_skill(root, path)
        if skill.name in holders:
            raise GeneratorError(f"name '{skill.name}' is held by both {holders[skill.name]} and "
                                 f"{path}")
        holders[skill.name] = path
        skills.append(skill)
    return skills


def sibling_names(skills: list[Skill]) -> str:
    """The backticked names of all skills in their order, joined with `, ` and ` or `."""
    names = [f"`{skill.name}`" for skill in skills]
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " or " + names[-1]


def entry_point_text(skill: Skill, skills: list[Skill]) -> str:
    """The text of both entry points of `skill`; each paragraph and list item is one line."""
    name = PREFIX + skill.name
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {skill.description}{SUFFIX}\n"
        "---\n"
        "\n"
        f"# {name}\n"
        "\n"
        "This entry point serves a session that works on the-way itself. Stop following it, and "
        f"use the product's own project skill `{name}`, if either check shows a product:\n"
        "\n"
        "- `git -C <the directory that holds this file> rev-parse "
        "--show-superproject-working-tree` prints a path: this file lies in a product's "
        "`.the-way` submodule;\n"
        "- `git ls-files --stage -- ':/.the-way'`, run in the session's working directory, "
        "prints a line: the session works in a product that pins the-way.\n"
        "\n"
        "The process root is the checkout or worktree the session works in: the directory "
        "`git rev-parse --show-toplevel` prints when run in the session's working directory — the "
        "directory the session was started in, or the one it was last moved to (Claude Code's "
        "`/cd`) — not in the shell's current directory, which moves with `cd`. "
        f"Read `{skill.path}` there in full and follow it, and read a file it names under the "
        "same root when the step or variant that names it comes, not all of them at the start, "
        "never a copy in another checkout or worktree. "
        f"If `{skill.path}` is absent there, stop and say so. "
        "If the skill tells you to resolve a link to find the-way, skip that: the root is the one above. Do not substitute "
        "a global skill.\n"
        "\n"
        "Where this skill or a file it reads names another the-way skill — "
        f"{sibling_names(skills)} — use this repository's project skill of the same name with the "
        "`the-way-` prefix, never an unprefixed one.\n")


def produce(skills: list[Skill]) -> dict[str, str]:
    """Path from the repository root -> text, two entry points per skill, in skill order."""
    produced: dict[str, str] = {}
    for skill in skills:
        text = entry_point_text(skill, skills)
        for directory in ENTRY_DIRECTORIES:
            produced[f"{directory}/{PREFIX}{skill.name}/SKILL.md"] = text
    return produced


def orphans(root: Path, skills: list[Skill]) -> list[str]:
    """Every directory `the-way-*` under either skills directory that no skill produces."""
    names = {PREFIX + skill.name for skill in skills}
    found = []
    for directory in ENTRY_DIRECTORIES:
        base = root / directory
        if not base.is_dir():
            continue
        for child in sorted(base.iterdir(), key=lambda entry: entry.name):
            if child.is_dir() and child.name.startswith(PREFIX) and child.name not in names:
                found.append(f"{directory}/{child.name}")
    return found


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the project skill entry points of the-way's own skills.")
    parser.add_argument("--write", action="store_true",
                        help="write the entry points; without it, print what would change")
    arguments = parser.parse_args(argv)
    try:
        skills = discover(root)
        changes = []
        for relative, text in produce(skills).items():
            target = root / relative
            data = text.encode("utf-8")
            if not target.is_file():
                changes.append(("create", relative, target, data))
            elif target.read_bytes() != data:
                changes.append(("change", relative, target, data))
        left = orphans(root, skills)
        for kind, relative, target, data in changes:
            if arguments.write:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                print(f"{kind}d {relative}")
            else:
                print(f"would {kind} {relative}")
        for directory in left:
            print(f"orphan {directory}: no skill produces it; remove it with "
                  f"git rm -r -- {directory}")
        if not changes and not left:
            print("entry points are current")
        return 0
    except (GeneratorError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
