"""Tests of the generator of the copies of the-way's agent type definitions (WAY-127).

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
import agent_type_copies as generator  # noqa: E402

MARK = "Dispatched only by the task cycle of the-way."
STAGE = ("---\nname: the-way-stage\ndescription: Stage agent. " + MARK + "\n"
         "disallowedTools: Skill\n---\n\nYou are a stage agent. You read the file you are given.\n")
AUTHOR = ("---\nname: the-way-author\ndescription: Author agent. " + MARK + "\n"
          "experimental:\n  cacheTtl: 1h\n---\n\nYou are the author. You read the file you are "
          "given.\n")


class Repository:
    """A temporary git repository with no commit; untracked files count as definitions."""

    def __init__(self, test: unittest.TestCase) -> None:
        directory = tempfile.TemporaryDirectory(prefix="the-way-agent-copies-")
        test.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)

    def write(self, relative: str, data: str | bytes) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)

    def run(self, *arguments: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = generator.main(list(arguments), root=self.root)
        return code, out.getvalue(), err.getvalue()

    def files(self) -> dict[str, bytes]:
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*")
                if path.is_file() and ".git" not in path.relative_to(self.root).parts}


class Writing(unittest.TestCase):
    def test_write_creates_a_byte_identical_copy_of_each_definition(self) -> None:
        repository = Repository(self)
        repository.write("task-cycle/agent-types/the-way-stage.md", STAGE)
        repository.write("task-cycle/agent-types/the-way-author.md", AUTHOR)
        sources = repository.files()
        code, out, err = repository.run("--write")
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out, "created .claude/agents/the-way-author.md\n"
                              "created .claude/agents/the-way-stage.md\n")
        written = {path: data for path, data in repository.files().items() if path not in sources}
        self.assertEqual(written, {".claude/agents/the-way-stage.md": STAGE.encode("utf-8"),
                                   ".claude/agents/the-way-author.md": AUTHOR.encode("utf-8")})
        self.assertEqual(repository.run("--write"), (0, "agent type copies are current\n", ""))

    def test_without_write_it_lists_the_plan_and_writes_nothing(self) -> None:
        repository = Repository(self)
        repository.write("task-cycle/agent-types/the-way-stage.md", STAGE)
        repository.write("task-cycle/agent-types/the-way-author.md", AUTHOR)
        repository.write(".claude/agents/the-way-stage.md", "stale\n")
        before = repository.files()
        self.assertEqual(repository.run(), (
            0, "would create .claude/agents/the-way-author.md\n"
               "would change .claude/agents/the-way-stage.md\n", ""))
        self.assertEqual(repository.files(), before)

    def test_a_changed_definition_rewrites_its_copy(self) -> None:
        repository = Repository(self)
        repository.write("task-cycle/agent-types/the-way-stage.md", STAGE)
        repository.run("--write")
        repository.write("task-cycle/agent-types/the-way-stage.md", STAGE + "More.\n")
        self.assertEqual(repository.run("--write"), (0, "changed .claude/agents/the-way-stage.md\n",
                                                     ""))
        self.assertEqual((repository.root / ".claude/agents/the-way-stage.md").read_bytes(),
                         (STAGE + "More.\n").encode("utf-8"))

    def test_an_orphan_is_listed_and_kept_and_a_file_of_another_name_is_not_touched(self) -> None:
        repository = Repository(self)
        repository.write("task-cycle/agent-types/the-way-stage.md", STAGE)
        repository.run("--write")
        repository.write(".claude/agents/the-way-renamed.md", "old\n")
        repository.write(".claude/agents/reviewer.md", "theirs\n")
        self.assertEqual(repository.run("--write"), (
            0, "orphan .claude/agents/the-way-renamed.md: no definition produces it; remove it "
               "with git rm -- .claude/agents/the-way-renamed.md\n", ""))
        self.assertEqual((repository.root / ".claude/agents/the-way-renamed.md").read_bytes(),
                         b"old\n")
        self.assertEqual((repository.root / ".claude/agents/reviewer.md").read_bytes(), b"theirs\n")

    def test_an_ignored_definition_is_none(self) -> None:
        repository = Repository(self)
        repository.write(".gitignore", "task-cycle/agent-types/the-way-stage.md\n")
        repository.write("task-cycle/agent-types/the-way-stage.md", STAGE)
        self.assertEqual(generator.produce(repository.root), {})


class Errors(unittest.TestCase):
    CASES = (
        ("name is not the file's", "the-way-stage.md", STAGE.replace("name: the-way-stage",
                                                                       "name: the-way-other"),
         "Error: task-cycle/agent-types/the-way-stage.md: name 'the-way-other' is not the "
         "file's name without `.md`\n"),
        ("no mark", "the-way-stage.md", STAGE.replace(" " + MARK, ""),
         "Error: task-cycle/agent-types/the-way-stage.md: the description does not end with "
         "`Dispatched only by the task cycle of the-way.`\n"),
        ("no frontmatter", "the-way-stage.md", "You are a stage agent.\n",
         "Error: task-cycle/agent-types/the-way-stage.md: the file must open with `---`, a "
         "`name:` line and a `description:` line, each on one line\n"),
        ("description before name", "the-way-stage.md",
         STAGE.replace("name: the-way-stage\ndescription: Stage agent. " + MARK,
                       "description: Stage agent. " + MARK + "\nname: the-way-stage"),
         "Error: task-cycle/agent-types/the-way-stage.md: the file must open with `---`, a "
         "`name:` line and a `description:` line, each on one line\n"),
        ("unclosed frontmatter", "the-way-stage.md",
         "---\nname: the-way-stage\ndescription: Stage agent. " + MARK + "\nBody.\n",
         "Error: task-cycle/agent-types/the-way-stage.md: the frontmatter is not closed by a "
         "`---` line\n"),
        ("colon and space in the description", "the-way-stage.md",
         STAGE.replace("Stage agent.", "Stage agent: yes."),
         "Error: task-cycle/agent-types/the-way-stage.md: description is not a safe plain YAML "
         "scalar\n"),
        ("carriage return", "the-way-stage.md", STAGE.replace("\n", "\r\n"),
         "Error: task-cycle/agent-types/the-way-stage.md: holds a carriage return; the file "
         "uses LF line ends\n"),
        ("not UTF-8", "the-way-stage.md", STAGE.encode("utf-8") + b"\xff\xfe",
         "Error: task-cycle/agent-types/the-way-stage.md: not UTF-8\n"),
        ("name without the prefix", "stage.md", STAGE.replace("the-way-stage", "stage"),
         "Error: task-cycle/agent-types/stage.md: not a definition; its name must be "
         "`the-way-<words>.md` directly in task-cycle/agent-types/\n"),
        ("name with a capital", "the-way-Stage.md", STAGE.replace("the-way-stage", "the-way-Stage"),
         "Error: task-cycle/agent-types/the-way-Stage.md: not a definition; its name must be "
         "`the-way-<words>.md` directly in task-cycle/agent-types/\n"),
        ("another kind of file", "notes.txt", "Notes.\n",
         "Error: task-cycle/agent-types/notes.txt: not a definition; its name must be "
         "`the-way-<words>.md` directly in task-cycle/agent-types/\n"),
        ("a file in a subdirectory", "sub/the-way-stage.md", STAGE,
         "Error: task-cycle/agent-types/sub/the-way-stage.md: not a definition; its name must be "
         "`the-way-<words>.md` directly in task-cycle/agent-types/\n"),
        ("a name that would leave the directory", "the-way-..%2fx.md", STAGE,
         "Error: task-cycle/agent-types/the-way-..%2fx.md: not a definition; its name must be "
         "`the-way-<words>.md` directly in task-cycle/agent-types/\n"),
    )

    def test_each_error_stops_with_its_message_and_writes_nothing(self) -> None:
        for label, filename, content, message in self.CASES:
            with self.subTest(label):
                repository = Repository(self)
                repository.write("task-cycle/agent-types/" + filename, content)
                repository.write("task-cycle/agent-types/the-way-author.md", AUTHOR)
                before = repository.files()
                self.assertEqual(repository.run("--write"), (1, "", message))
                self.assertEqual(repository.files(), before)


class TrackedCopies(unittest.TestCase):
    def test_the_tracked_copies_are_what_the_generator_produces(self) -> None:
        produced = generator.produce(ROOT)
        listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--", ".claude/agents"],
                                check=True, capture_output=True).stdout
        tracked = sorted(path for path in listed.decode("utf-8").split("\0") if path)
        # invariant: derived-file-content
        self.assertEqual(tracked, sorted(produced),
                         "run python -B agent-instructions/agent_type_copies.py --write and "
                         "commit what it writes")
        for path, data in produced.items():
            self.assertEqual((ROOT / path).read_bytes(), data, path)
        self.assertEqual(generator.orphans(ROOT, produced), [])
        # A positive control: the two types of the cycle are among the definitions found.
        self.assertTrue({".claude/agents/the-way-stage.md",
                         ".claude/agents/the-way-author.md"} <= set(produced))


if __name__ == "__main__":
    unittest.main()
