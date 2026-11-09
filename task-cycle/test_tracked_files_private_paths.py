"""The invariant `tracked-file-private-paths`: no file git tracks holds an absolute path or a note link.

The test reads every file git tracks in this repository and runs the pattern of
`private_paths_check.py` over it, the pattern that WAY-309 gives for the text a cycle publishes. It
fails with the file and the line of each finding. Four files write example paths by their nature
and are not read; the list stands below and is the same as the one the invariant names.

The second class feeds the same function files made up for the test, to show that a path put into
a tracked file is reported with its file and line and that a file on the list is skipped. It checks
the function, not the invariant, which is about the files of this repository.

A path written in this file would be a finding too, so the fixtures are assembled from pieces.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import private_paths_check  # noqa: E402

# The files the sentence of the invariant names: they write example paths in order to find or to
# test the finding of paths, so the pattern lists them by design.
EXEMPT = (
    "task-cycle/private_paths_check.py",
    "task-cycle/test_private_paths_check.py",
    "instruction-files/check_instructions.py",
    "instruction-files/test_check_instructions.py",
)
INVARIANT = "tracked-file-private-paths"


def tracked_files(root: Path) -> list[str]:
    """The files git tracks below `root`, as paths with `/`, that exist in the working tree."""
    listed = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True)
    names = [name for name in listed.stdout.decode("utf-8").split("\0") if name]
    return [name for name in names if (root / name).is_file()]


def findings(root: Path, exempt: tuple[str, ...]) -> list[str]:
    """One `file:line: kind: text` per absolute path or note link in a tracked file not exempt."""
    found = []
    for name in tracked_files(root):
        if name in exempt:
            continue
        result = private_paths_check.Result()
        private_paths_check.check_file(root / name, result)
        for _, number, kind, shown in result.listed:
            found.append(f"{name}:{number}: {kind}: {shown}")
    return found


class TrackedFilesOfThisRepositoryTest(unittest.TestCase):
    # invariant: tracked-file-private-paths
    def test_no_tracked_file_holds_an_absolute_path_or_a_note_link(self) -> None:
        found = findings(ROOT, EXEMPT)
        self.assertEqual(found, [], "absolute paths or note links in tracked files:\n"
                         + "\n".join(found))

    def test_every_exempt_file_is_tracked(self) -> None:
        tracked = set(tracked_files(ROOT))
        self.assertEqual([name for name in EXEMPT if name not in tracked], [])

    def test_the_exempt_files_are_the_ones_the_invariant_names(self) -> None:
        text = (ROOT / "foundations" / "invariants.md").read_text(encoding="utf-8")
        section = re.search(r"^## " + INVARIANT + r"\n\n(.+)\n", text, re.MULTILINE)
        self.assertIsNotNone(section, "the invariant is not in foundations/invariants.md")
        named = re.findall(r"`([^`]+\.py)`", section.group(1))
        self.assertEqual(sorted(named), sorted(EXEMPT))


class FindingsOnMadeUpFilesTest(unittest.TestCase):
    """Files written for the test; the expected lines are written out here."""

    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)

    def track(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")
        subprocess.run(["git", "add", "--", name], cwd=self.root, check=True)

    def test_a_drive_path_is_reported_with_its_file_and_line(self) -> None:
        drive = "D" + ":/"
        self.track("notes/plan.md", "first line\nsecond line\nsee " + drive + "work/proj now\n")
        self.assertEqual(findings(self.root, ()),
                         ["notes/plan.md:3: absolute path: " + drive + "work/proj"])

    def test_a_note_link_is_reported_with_its_file_and_line(self) -> None:
        self.track("a.md", "[" + "[Meeting notes]]\n")
        self.assertEqual(findings(self.root, ()), ["a.md:1: note link: [" + "[Meeting notes]]"])

    def test_a_home_directory_after_a_clean_line_is_reported_on_its_own_line(self) -> None:
        home = "/ho" + "me/alice"
        self.track("x/y.py", "x = 1\n# " + home + "/data\n")
        self.assertEqual(findings(self.root, ()), ["x/y.py:2: absolute path: " + home + "/data"])

    def test_a_file_on_the_list_is_skipped_and_one_off_it_is_not(self) -> None:
        drive = "C" + ":/"
        self.track("listed.py", "p = '" + drive + "dir'\n")
        self.track("other.py", "p = '" + drive + "dir'\n")
        self.assertEqual(findings(self.root, ("listed.py",)),
                         ["other.py:1: absolute path: " + drive + "dir"])

    def test_text_without_a_path_or_a_link_is_clean(self) -> None:
        self.track("clean.md", "Tasks are in ~/.the-way/locations.json; see ../x and docs/y.md\n")
        self.assertEqual(findings(self.root, ()), [])

    def test_a_file_that_is_listed_by_git_but_gone_from_the_tree_is_not_read(self) -> None:
        self.track("gone.md", "text\n")
        (self.root / "gone.md").unlink()
        self.assertEqual(findings(self.root, ()), [])


if __name__ == "__main__":
    unittest.main()
