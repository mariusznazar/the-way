"""Tests of the relation model's fingerprint (WAY-02): the first eight lower-case hexadecimal
characters of the SHA-256 digest of the text in UTF-8, after every run of spaces and line breaks
becomes one space and both ends are trimmed.

Every expected fingerprint is written out, computed apart from the script under test:
the texts below that differ only in spaces and line breaks all normalize to WORDING, whose
digest begins with WORDING_FINGERPRINT.

Run from the root of the-way:
    python -B gate/run_tests.py relation-model
"""

import contextlib
import io
import os
import runpy
import sys
import unittest
import unittest.mock

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fingerprint import fingerprint  # noqa: E402

WORDING = "The product keeps every saved game after a reload."
WORDING_FINGERPRINT = "798975ff"
# Polish, with an em dash and a letter outside ASCII; its UTF-8 digest begins with 88df410e.
NON_ASCII = "Zapisana gra przetrwa ponowne wczytanie — zawsze, także po awarii."
NON_ASCII_FINGERPRINT = "88df410e"


class Fingerprint(unittest.TestCase):
    def test_a_text_gives_the_first_eight_lower_case_hex_characters_of_its_digest(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint(WORDING), WORDING_FINGERPRINT)

    def test_a_run_of_spaces_counts_as_one_space(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("The product keeps  every   saved game after a reload."),
                         WORDING_FINGERPRINT)

    def test_a_line_break_counts_as_one_space(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("The product keeps every saved game\nafter a reload."),
                         WORDING_FINGERPRINT)

    def test_a_carriage_return_and_line_feed_count_as_one_space(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("The product keeps every saved game\r\nafter a reload."),
                         WORDING_FINGERPRINT)

    def test_a_lone_carriage_return_counts_as_one_space(self):
        """A text file ends a line with LF, CR LF or a lone CR, the three line endings Python's
        universal newlines read; a lone CR is a line break under the sentence as well."""
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("The product keeps every saved game\rafter a reload."),
                         WORDING_FINGERPRINT)

    def test_a_tab_is_kept(self):
        """A tab is neither a space nor a line break, so it stays in the text digested: the
        digest is that of the text with the tab, 78afb3c6, not WORDING_FINGERPRINT."""
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("The product keeps every saved game\tafter a reload."),
                         "78afb3c6")

    def test_a_tab_at_either_end_is_kept(self):
        """Trimming removes what the replacement left at an end, a space; nothing else in the text
        is changed (WAY-02), so a tab at an end stays in the text digested."""
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("\tThe product keeps every saved game after a reload."),
                         "10fdd923")
        self.assertEqual(fingerprint("The product keeps every saved game after a reload.\t"),
                         "58c9b2a7")

    def test_a_run_of_spaces_and_line_breaks_counts_as_one_space(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("The product keeps every saved game  \r\n\n  after a "
                                     "reload."), WORDING_FINGERPRINT)
        self.assertEqual(fingerprint("The product keeps every saved game \r \r\r\n after a "
                                     "reload."), WORDING_FINGERPRINT)

    def test_spaces_and_line_breaks_at_both_ends_are_trimmed(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint("  The product keeps every saved game after a reload."),
                         WORDING_FINGERPRINT)
        self.assertEqual(fingerprint("The product keeps every saved game after a reload.  "),
                         WORDING_FINGERPRINT)
        self.assertEqual(fingerprint("\r\n The product keeps every saved game after a reload.\n"),
                         WORDING_FINGERPRINT)

    def test_a_text_outside_ascii_is_digested_as_utf_8(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint(NON_ASCII), NON_ASCII_FINGERPRINT)

    def test_letter_case_is_kept(self):
        # invariant: fingerprint-definition
        self.assertEqual(fingerprint(NON_ASCII.upper()), "05617e92")

    def test_the_script_run_as_a_program_gives_the_same(self):
        """The script's program path, run in this process with its standard input fed the text,
        so that the test starts no program (script-subprocesses)."""
        # invariant: fingerprint-definition
        stdin = io.TextIOWrapper(io.BytesIO((NON_ASCII + "\n").encode("utf-8")),
                                 encoding="utf-8")
        printed = io.StringIO()
        with unittest.mock.patch.object(sys, "stdin", stdin), contextlib.redirect_stdout(printed):
            runpy.run_path(os.path.join(HERE, "fingerprint.py"), run_name="__main__")
        self.assertEqual(printed.getvalue().strip(), NON_ASCII_FINGERPRINT)


if __name__ == "__main__":
    unittest.main()
