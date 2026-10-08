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
    "- `git ls-files --stage -- ':/.the-way'`, run in the session's working directory, "
    "prints a line: the session works in a product that pins the-way.\n"
    "\n"
    "The process root is the checkout or worktree the session works in: the directory "
    "`git rev-parse --show-toplevel` prints when run in the session's working directory — the "
    "directory the session was started in, or the one it was last moved to (Claude Code's `/cd`) "
    "— not in the shell's current directory, which moves with `cd`. "
    "Read `elements/decisions/skill/SKILL.md` there in "
    "full and follow it, and read the files it names under the same root, never a copy in "
    "another checkout or worktree. If `elements/decisions/skill/SKILL.md` is absent there, stop "
    "and say so. If the skill tells you to resolve a link to find the-way, skip "
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
        ("byte order mark", "﻿---\nname: alpha\ndescription: Use for alpha.\n---\n",
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
        ("double-quoted description", '---\nname: alpha\ndescription: "Use for alpha."\n---\n',
         "Error: a/SKILL.md: description is not a safe plain YAML scalar\n"),
        ("single-quoted description", "---\nname: alpha\ndescription: 'Use for alpha.'\n---\n",
         "Error: a/SKILL.md: description is not a safe plain YAML scalar\n"),
        ("colon and space inside", "---\nname: alpha\ndescription: Use for alpha: always.\n---\n",
         "Error: a/SKILL.md: description is not a safe plain YAML scalar\n"),
        ("space and hash inside", "---\nname: alpha\ndescription: Use for alpha #1.\n---\n",
         "Error: a/SKILL.md: description is not a safe plain YAML scalar\n"),
        ("ending with a colon", "---\nname: alpha\ndescription: Use for alpha:\n---\n",
         "Error: a/SKILL.md: description is not a safe plain YAML scalar\n"),
        ("starting with a backtick", "---\nname: alpha\ndescription: `alpha` is used.\n---\n",
         "Error: a/SKILL.md: description is not a safe plain YAML scalar\n"),
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

    def test_a_colon_not_followed_by_a_space_is_accepted(self) -> None:
        repository = Repository(self)
        repository.write("a/SKILL.md", "---\nname: alpha\ndescription: Use at 10:30.\n---\n")
        self.assertEqual(generator.discover(repository.root),
                         [generator.Skill("a/SKILL.md", "alpha", "Use at 10:30.")])

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


class TrackedEntryPoints(unittest.TestCase):
    def test_the_tracked_entry_points_are_what_the_generator_produces(self) -> None:
        skills = generator.discover(ROOT)
        produced = generator.produce(skills)
        listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--", ".claude/skills",
                                 ".agents/skills"], check=True, capture_output=True).stdout
        tracked = sorted(path for path in listed.decode("utf-8").split("\0") if path)
        self.assertEqual(tracked, sorted(produced),
                         "run python -B agent-instructions/skill_entry_points.py --write and "
                         "commit what it writes")
        for path, text in produced.items():
            self.assertEqual((ROOT / path).read_bytes(), text.encode("utf-8"), path)
        self.assertEqual(generator.orphans(ROOT, skills), [])


if __name__ == "__main__":
    unittest.main()
