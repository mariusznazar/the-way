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

    def write(self, name, text):
        """The path of a copy of a log, written in a temporary directory as its text is."""
        if not hasattr(self, "directory"):
            self.directory = tempfile.TemporaryDirectory()
            self.addCleanup(self.directory.cleanup)
        path = os.path.join(self.directory.name, name)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        return path

    def run_script(self, before, after):
        """(exit code, report) of the script run on two copies, each given by its path."""
        result = subprocess.run([sys.executable, "-B", SCRIPT, before, after], capture_output=True,
                                text=True, encoding="utf-8")
        return result.returncode, result.stdout + result.stderr

    def compare(self, before, after):
        """(exit code, report) of the script run on two copies, each written as its text is."""
        return self.run_script(self.write("before.md", before), self.write("after.md", after))

    def test_entry_whose_text_differs_is_reported_with_its_first_line(self):
        after = LOG.replace("A game is saved to one file.", "A game is saved to two files.")
        code, report = self.compare(LOG, after)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-01 differs: the first line that differs is line 5 in", report)
        self.assertIn("A game is saved to two files.", report)
        self.assertIn("1 report.", report)

    def test_identical_copies_pass(self):
        code, report = self.compare(LOG, LOG)
        self.assertEqual(code, 0, report)
        self.assertIn("Compared 2 entries of", report)
        self.assertIn("all the same byte for byte", report)

    def test_entry_standing_in_one_copy_only_is_reported_for_each_side(self):
        added = LOG + "\n### GAME-03 — Where is a save stored?\n\nIn a folder.\n"
        code, report = self.compare(LOG, added)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-03 stands only in", report)
        self.assertIn("after.md", report)
        code, report = self.compare(added, LOG[:LOG.index("### GAME-02")])
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-03 stands only in", report)
        self.assertIn("before.md", report)

    def test_entry_standing_twice_in_a_copy_is_reported_with_its_lines(self):
        twice = LOG + "\n### GAME-02 — Where does the clock run again?\n\nAgain.\n"
        code, report = self.compare(LOG, twice)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-02 stands 2 times in", report)
        self.assertIn("at lines 12 and 21", report)
        self.assertNotIn("differs", report)

    def test_blank_lines_at_the_end_of_an_entry_are_no_difference(self):
        after = LOG.replace("*Rationale:* one file is easy to copy.\n\n",
                            "*Rationale:* one file is easy to copy.\n\n\n\n")
        self.assertEqual(self.compare(LOG, after)[0], 0)

    def test_section_heading_and_sentence_between_entries_are_no_difference(self):
        # the division of a log into sections adds headings and sentences, and no entry changes
        after = LOG.replace("### GAME-01", "## Saving\n\nHow a game is saved.\n\n### GAME-01", 1)
        after = after.replace("### GAME-02", "## Clock\n\nWhere the clock runs.\n\n### GAME-02", 1)
        code, report = self.compare(LOG, after)
        self.assertEqual(code, 0, report)
        self.assertIn("all the same byte for byte", report)

    def test_entry_whose_heading_differs_is_reported_at_its_heading(self):
        after = LOG.replace("How is a game saved?", "How is a game kept?")
        code, report = self.compare(LOG, after)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-01 differs: the first line that differs is line 3 in", report)

    def test_difference_in_a_later_entry_is_reported_at_its_own_line(self):
        after = LOG.replace("The clock runs in the core.", "The clock runs in the shell.")
        code, report = self.compare(LOG, after)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-02 differs: the first line that differs is line 14 in", report)
        self.assertNotIn("GAME-01", report)

    def test_entry_that_ends_before_the_other_copy_does_is_a_difference(self):
        after = LOG.replace("*Rationale:* one file is easy to copy.\n", "")
        code, report = self.compare(LOG, after)
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-01 differs", report)
        self.assertIn("(the entry ends before this line)", report)

    def test_line_ending_is_a_byte_that_differs(self):
        code, report = self.compare(LOG, LOG.replace("\n", "\r\n"))
        self.assertEqual(code, 1, report)
        self.assertIn("GAME-01 differs: the first line that differs is line 3 in", report)

    def test_withdrawn_block_is_compared_as_an_entry(self):
        withdrawn = LOG + "\n## Withdrawn identifiers\n\n| Identifier | Why |\n|---|---|\n" \
                          "| GAME-09 | merged |\n"
        code, report = self.compare(withdrawn, withdrawn.replace("| merged |", "| folded in |"))
        self.assertEqual(code, 1, report)
        self.assertIn("## Withdrawn identifiers differs: the first line that differs is line 25 in",
                      report)
        code, report = self.compare(LOG, withdrawn)
        self.assertEqual(code, 1, report)
        self.assertIn("## Withdrawn identifiers stands only in", report)

    def test_copy_holding_no_entry_ends_with_an_error_naming_the_file(self):
        # WAY-344: the script reads the entry headings it needs, and a copy without one ends with
        # exit code 2 and a message that names the file
        for text in ("# Decision log\n\nNo decision yet.\n",
                     "## Withdrawn identifiers\n\n| Identifier | Why |\n|---|---|\n"):
            with self.subTest(text=text):
                code, report = self.compare(LOG, text)
                self.assertEqual(code, 2, report)
                self.assertIn("Error: ", report)
                self.assertIn("after.md holds no entry", report)

    def test_copy_that_cannot_be_read_ends_with_an_error_naming_the_file(self):
        before = self.write("before.md", LOG)
        code, report = self.run_script(before, os.path.join(self.directory.name, "no such copy.md"))
        self.assertEqual(code, 2, report)
        self.assertIn("Error: ", report)
        self.assertIn("no such copy.md cannot be read", report)


if __name__ == "__main__":
    unittest.main()
