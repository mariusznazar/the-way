"""The invariant `elements-no-pending-marker`: no file git tracks under `elements/` holds the marker
of a decision still to be made.

The test reads the files of this repository that git tracks under `elements/`, this file among them,
so the marker is written here as a pattern and never as the text it looks for. Two words broken by a
line end or by several spaces count as the text.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MARKER = re.compile(r"decision[ \n]+pending")


def tracked_files_under_elements() -> list[str]:
    run = subprocess.run(["git", "ls-files", "-z", "--", "elements"], cwd=ROOT,
                         capture_output=True, check=True)
    return [name for name in run.stdout.decode("utf-8").split("\0") if name]


class TrackedFilesUnderElementsTest(unittest.TestCase):
    # invariant: elements-no-pending-marker
    def test_no_tracked_file_under_elements_holds_the_pending_marker(self) -> None:
        names = tracked_files_under_elements()
        self.assertTrue(names, "git lists no file under elements/")
        found = []
        for name in names:
            path = ROOT / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for match in MARKER.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                found.append(f"{name}:{line}")
        self.assertEqual(found, [], "files under elements/ hold the pending-decision marker")


if __name__ == "__main__":
    unittest.main()
