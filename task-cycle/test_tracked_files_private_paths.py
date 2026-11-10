"""The invariant `tracked-file-private-paths`: no file git tracks holds an absolute path or a note link.

The test runs the command `tracked_private_paths_check.py` in the root of this repository with the
identifier of the invariant, as a product does. The command reads the files that the sentence of the
invariant in `foundations/invariants.md` names, skips them and reads every other file git tracks;
this file keeps no list of its own. The test fails with the file and the line of each finding.
What the command lists and skips is tested on repositories made up for it, in
`test_tracked_private_paths_check.py`.
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
COMMAND = HERE / "tracked_private_paths_check.py"
INVARIANT = "tracked-file-private-paths"


class TrackedFilesOfThisRepositoryTest(unittest.TestCase):
    # invariant: tracked-file-private-paths
    def test_no_tracked_file_holds_an_absolute_path_or_a_note_link(self) -> None:
        run = subprocess.run([sys.executable, "-B", str(COMMAND), INVARIANT], cwd=ROOT,
                             capture_output=True, encoding="utf-8")
        self.assertEqual(run.returncode, 0,
                         "absolute paths or note links in tracked files:\n" + run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
