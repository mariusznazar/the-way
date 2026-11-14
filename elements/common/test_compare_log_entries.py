"""Tests of the comparison of the entries of two copies of a decision log, byte for byte.

Each test writes two copies of a log to a temporary directory, runs the script on them as a product
runs it and reads its exit code and report. The expected texts are written out below, never computed
by the script's code.

Run from the root of the-way: python -B gate/run_tests.py elements/common
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "compare_log_entries.py")

# A log of two entries, the first at line 3 and the second at line 12.
LOG = """# Decision log

### GAME-01 — How is a game saved?

A game is saved to one file.

- **Scope:** core
- **Origin:** none

*Rationale:* one file is easy to copy.

### GAME-02 — Where does the clock run?

The clock runs in the core.

- **Scope:** core, shell
- **Origin:** none

*Rationale:* the core holds time.
"""


class CompareLogEntriesTest(unittest.TestCase):

    def compare(self, before, after):
        """(exit code, report) of the script run on two copies, each written as its text is."""
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        paths = []
        for name, text in (("before.md", before), ("after.md", after)):
            path = os.path.join(directory.name, name)
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)
            paths.append(path)
        result = subprocess.run([sys.executable, "-B", SCRIPT, *paths], capture_output=True,
                                text=True, encoding="utf-8")
        return result.returncode, result.stdout + result.stderr

    def test_entry_whose_text_differs_is_reported_with_its_first_line(self):
        after = LOG.replace("A game is saved to one file.", "A game is saved to two files.")
        code, report = self.compare(LOG, after)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-01 differs: the first line that differs is line 5 in", report)
        self.assertIn("A game is saved to two files.", report)


if __name__ == "__main__":
    unittest.main()
