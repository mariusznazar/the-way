### Task 2: Generator and its tests (`agent-instructions`)

**Files:**
- Create: `agent-instructions/skill_entry_points.py`
- Create: `agent-instructions/test_skill_entry_points.py`

**Interfaces:**
- Consumes: nothing from earlier tasks (it does not read the gate's test, and the gate's test does not import it).
- Produces: `ROOT: Path`; `ENTRY_DIRECTORIES = (".claude/skills", ".agents/skills")`; `PREFIX = "the-way-"`; `class GeneratorError(Exception)`; `@dataclass(frozen=True) class Skill(path: str, name: str, description: str)`; `discover(root: Path) -> list[Skill]` (sorted by path); `sibling_names(skills: list[Skill]) -> str`; `entry_point_text(skill: Skill, skills: list[Skill]) -> str`; `produce(skills: list[Skill]) -> dict[str, str]` (path from root → text); `orphans(root: Path, skills: list[Skill]) -> list[str]`; `main(argv: list[str] | None = None, root: Path = ROOT) -> int`. Output lines: `would create|would change <path>`, `created|changed <path>`, `orphan <dir>: no skill produces it; remove it with git rm -r -- <dir>`, `entry points are current`; errors `Error: <message>` on stderr, exit 1.

The planner ran this code and these tests in a scratch copy of the repository (11 tests OK; the generator produced 22 files, byte-identical pairs, and a rerun printed `entry points are current`).

- [ ] **Step 1: Write the failing tests** — create `agent-instructions/test_skill_entry_points.py`:

```python
"""Tests of the generator of the project skill entry points (WAY-127).

The expected texts are written out on purpose: a test that built them with the generator's own
functions would pass whatever those functions produce.

Run from the root of the-way: python -B gate/run_tests.py agent-instructions
"""

from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import skill_entry_points as generator  # noqa: E402

CRITIQUE = ("---\nname: critique\ndescription: Use when a proposal needs a second reader.\n---\n\n"
            "# Critique\n")
DECISION = ("---\nname: record-decision\ndescription: Use when a decision has to be written.\n"
            "---\n\n# Record a decision\n")

# The entry point of `record-decision` beside `critique`, written out in full.
DECISION_ENTRY = (
    "---\n"
    "name: the-way-record-decision\n"
    "description: Use when a decision has to be written. Use this checkout's own the-way.\n"
    "---\n"
    "\n"
    "# the-way-record-decision\n"
    "\n"
    "This entry point serves a session that works on the-way itself. Stop following it, and use "
    "the product's own project skill `the-way-record-decision`, if either check shows a "
    "product:\n"
    "\n"
    "- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` "
    "prints a path: this file lies in a product's `.the-way` submodule;\n"
    "- `git ls-files --stage -- ':/.the-way'`, run in the directory the session was started in, "
    "prints a line: the session works in a product that pins the-way.\n"
    "\n"
    "The process root is the checkout or worktree the session was started in: the directory "
    "`git rev-parse --show-toplevel` prints when run in the session's start directory, not in the "
    "shell's current directory, which moves. Read `elements/decisions/skill/SKILL.md` there in "
    "full and follow it, and read the files it names under the same root, never a copy in "
    "another checkout or worktree. If the skill tells you to resolve a link to find the-way, skip "
    "that: the root is the one above. Do not substitute a global skill.\n"
    "\n"
    "Where this skill or a file it reads names another the-way skill — `critique` or "
    "`record-decision` — use this repository's project skill of the same name with the "
    "`the-way-` prefix, never an unprefixed one.\n")


class Repository:
    """A temporary git repository with no commit; untracked files count as skills."""

    def __init__(self, test: unittest.TestCase) -> None:
        directory = tempfile.TemporaryDirectory(prefix="the-way-entry-points-")
        test.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def run(self, *arguments: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = generator.main(list(arguments), root=self.root)
        return code, out.getvalue(), err.getvalue()

    def files(self) -> dict[str, bytes]:
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*")
                if path.is_file() and ".git" not in path.relative_to(self.root).parts}


class EntryPointText(unittest.TestCase):
    def test_text_is_the_written_out_form(self) -> None:
        skills = [generator.Skill("elements/common/critique/SKILL.md", "critique",
                                  "Use when a proposal needs a second reader."),
                  generator.Skill("elements/decisions/skill/SKILL.md", "record-decision",
                                  "Use when a decision has to be written.")]
        self.assertEqual(generator.entry_point_text(skills[1], skills), DECISION_ENTRY)

    def test_one_skill_names_itself_alone(self) -> None:
        skill = generator.Skill("a/SKILL.md", "alpha", "Use for alpha.")
        self.assertIn("another the-way skill — `alpha` — use", generator.entry_point_text(
            skill, [skill]))

    def test_siblings_follow_the_order_of_paths_with_or_before_the_last(self) -> None:
        repository = Repository(self)
        repository.write("zeta/SKILL.md", "---\nname: alpha\ndescription: Use for alpha.\n---\n")
        repository.write("beta/SKILL.md", "---\nname: zulu\ndescription: Use for zulu.\n---\n")
        repository.write("dir with space/SKILL.md",
                         "---\nname: mike\ndescription: Use for mike.\n---\n")
        skills = generator.discover(repository.root)
        self.assertEqual([skill.path for skill in skills],
                         ["beta/SKILL.md", "dir with space/SKILL.md", "zeta/SKILL.md"])
        self.assertEqual(generator.sibling_names(skills), "`zulu`, `mike` or `alpha`")


class Discovery(unittest.TestCase):
    def test_skills_under_the_entry_directories_and_ignored_ones_are_not_skills(self) -> None:
        repository = Repository(self)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        repository.write(".claude/skills/own/SKILL.md", CRITIQUE)
        repository.write(".agents/skills/own/SKILL.md", CRITIQUE)
        repository.write(".gitignore", ".runs/\n")
        repository.write(".runs/copy/SKILL.md", CRITIQUE)
        self.assertEqual([skill.path for skill in generator.discover(repository.root)],
                         ["elements/decisions/skill/SKILL.md"])

    def test_a_tracked_skill_deleted_on_disk_is_not_a_skill(self) -> None:
        repository = Repository(self)
        repository.write("gone/SKILL.md", CRITIQUE)
        subprocess.run(["git", "-C", str(repository.root), "add", "gone/SKILL.md"], check=True,
                       capture_output=True)
        (repository.root / "gone" / "SKILL.md").unlink()
        self.assertEqual(generator.discover(repository.root), [])

    def test_a_non_ascii_path_and_crlf_frontmatter_are_read(self) -> None:
        repository = Repository(self)
        repository.write("zażółć/SKILL.md",
                         "---\r\nname: alpha\r\ndescription: Use for alpha.\r\n---\r\n")
        self.assertEqual(generator.discover(repository.root),
                         [generator.Skill("zażółć/SKILL.md", "alpha", "Use for alpha.")])


class FrontmatterErrors(unittest.TestCase):
    CASES = (
        ("no frontmatter", "# A skill\n",
         "Error: a/SKILL.md: no frontmatter between the first two '---' lines\n"),
        ("unclosed frontmatter", "---\nname: alpha\ndescription: Use for alpha.\n",
         "Error: a/SKILL.md: no frontmatter between the first two '---' lines\n"),
        ("byte order mark", "\ufeff---\nname: alpha\ndescription: Use for alpha.\n---\n",
         "Error: a/SKILL.md: no frontmatter between the first two '---' lines\n"),
        ("no name", "---\ndescription: Use for alpha.\n---\n",
         "Error: a/SKILL.md: frontmatter has no 'name:' with a value\n"),
        ("empty name", "---\nname:\ndescription: Use for alpha.\n---\n",
         "Error: a/SKILL.md: frontmatter has no 'name:' with a value\n"),
        ("no description", "---\nname: alpha\n---\n",
         "Error: a/SKILL.md: frontmatter has no 'description:' with a value\n"),
        ("folded description", "---\nname: alpha\ndescription: >\n  Use for alpha.\n---\n",
         "Error: a/SKILL.md: description is not on one line\n"),
        ("name off the form", "---\nname: Record_Decision\ndescription: Use for it.\n---\n",
         "Error: a/SKILL.md: name 'Record_Decision' is not lowercase words joined by hyphens\n"),
        ("name with the prefix", "---\nname: the-way-alpha\ndescription: Use for it.\n---\n",
         "Error: a/SKILL.md: name 'the-way-alpha' already starts with 'the-way-'\n"),
    )

    def test_each_error_stops_with_its_message_and_writes_nothing(self) -> None:
        for label, text, message in self.CASES:
            with self.subTest(label):
                repository = Repository(self)
                repository.write("a/SKILL.md", text)
                repository.write("b/SKILL.md", DECISION)
                before = repository.files()
                self.assertEqual(repository.run("--write"), (1, "", message))
                self.assertEqual(repository.files(), before)

    def test_a_name_two_skills_hold_stops_and_writes_nothing(self) -> None:
        repository = Repository(self)
        repository.write("a/SKILL.md", DECISION)
        repository.write("b/SKILL.md", DECISION)
        before = repository.files()
        self.assertEqual(repository.run("--write"), (
            1, "", "Error: name 'record-decision' is held by both a/SKILL.md and b/SKILL.md\n"))
        self.assertEqual(repository.files(), before)


class Writing(unittest.TestCase):
    def test_write_creates_both_copies_and_a_rerun_finds_them_current(self) -> None:
        repository = Repository(self)
        repository.write("elements/common/critique/SKILL.md", CRITIQUE)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        sources = repository.files()
        code, out, err = repository.run("--write")
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out, "created .claude/skills/the-way-critique/SKILL.md\n"
                              "created .agents/skills/the-way-critique/SKILL.md\n"
                              "created .claude/skills/the-way-record-decision/SKILL.md\n"
                              "created .agents/skills/the-way-record-decision/SKILL.md\n")
        written = {path: data for path, data in repository.files().items() if path not in sources}
        self.assertEqual(set(written), {".claude/skills/the-way-critique/SKILL.md",
                                        ".agents/skills/the-way-critique/SKILL.md",
                                        ".claude/skills/the-way-record-decision/SKILL.md",
                                        ".agents/skills/the-way-record-decision/SKILL.md"})
        self.assertEqual(written[".claude/skills/the-way-record-decision/SKILL.md"],
                         DECISION_ENTRY.encode("utf-8"))
        self.assertEqual(written[".agents/skills/the-way-record-decision/SKILL.md"],
                         DECISION_ENTRY.encode("utf-8"))
        self.assertEqual(written[".claude/skills/the-way-critique/SKILL.md"],
                         written[".agents/skills/the-way-critique/SKILL.md"])
        self.assertEqual(repository.run("--write"), (0, "entry points are current\n", ""))

    def test_without_write_it_lists_the_plan_and_writes_nothing(self) -> None:
        repository = Repository(self)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        repository.write(".claude/skills/the-way-record-decision/SKILL.md", "stale\n")
        before = repository.files()
        self.assertEqual(repository.run(), (
            0, "would change .claude/skills/the-way-record-decision/SKILL.md\n"
               "would create .agents/skills/the-way-record-decision/SKILL.md\n", ""))
        self.assertEqual(repository.files(), before)

    def test_an_orphan_directory_is_listed_and_kept(self) -> None:
        repository = Repository(self)
        repository.write("elements/decisions/skill/SKILL.md", DECISION)
        repository.run("--write")
        repository.write(".agents/skills/the-way-renamed/SKILL.md", "old\n")
        repository.write(".claude/skills/someone-elses/SKILL.md", "theirs\n")
        self.assertEqual(repository.run("--write"), (
            0, "orphan .agents/skills/the-way-renamed: no skill produces it; remove it with "
               "git rm -r -- .agents/skills/the-way-renamed\n", ""))
        self.assertEqual((repository.root / ".agents/skills/the-way-renamed/SKILL.md").read_bytes(),
                         b"old\n")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to see them fail**

Run: `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions`
Expected: exit 1, `ImportError: Failed to import test module: test_skill_entry_points` caused by `ModuleNotFoundError: No module named 'skill_entry_points'`.

- [ ] **Step 3: Write the generator** — create `agent-instructions/skill_entry_points.py`:

```python
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
        "- `git ls-files --stage -- ':/.the-way'`, run in the directory the session was started "
        "in, prints a line: the session works in a product that pins the-way.\n"
        "\n"
        "The process root is the checkout or worktree the session was started in: the directory "
        "`git rev-parse --show-toplevel` prints when run in the session's start directory, not in "
        "the shell's current directory, which moves. "
        f"Read `{skill.path}` there in full and follow it, and read the files it names under the "
        "same root, never a copy in another checkout or worktree. If the skill tells you to "
        "resolve a link to find the-way, skip that: the root is the one above. Do not substitute "
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
```

The text of each paragraph is one line (no hard wraps), so no literal phrase of the entry point is split by a line break.

- [ ] **Step 4: Run the tests to see them pass, and a dry run on the repository**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py agent-instructions > $R/reports/check_2_tests_agent_instructions.txt 2>&1; echo $?; tail -3 $R/reports/check_2_tests_agent_instructions.txt; python -B agent-instructions/skill_entry_points.py | head -3; git status --short
```
Expected: exit 0, `Ran 11 tests`, `OK`; the dry run prints `would create .claude/skills/the-way-critique/SKILL.md` first (22 `would create` lines in all); status shows only the two new files (`??`): the dry run wrote nothing.

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git add agent-instructions/skill_entry_points.py agent-instructions/test_skill_entry_points.py && git commit -m "feat(agent-instructions): Generate the project skill entry points of the-way's skills"
```

---

