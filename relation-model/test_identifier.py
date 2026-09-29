"""Tests of the form of an identifier and of a version (WAY-41, WAY-64, WAY-75, WAY-57, WAY-79):
words of lower-case letters and digits joined by hyphens, and a version as a number without a
leading zero.

Run from the root of the-way:
    python -B gate/run_tests.py relation-model --record .runs/relation-model-tests.jsonl
"""

import os
import re
import sys
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from identifier import CITED, IDENTIFIER, VERSION, is_cited, is_identifier  # noqa: E402


class Identifier(unittest.TestCase):
    def test_words_in_lower_case_joined_by_hyphens_are_an_identifier(self):
        for text in ("relation-model", "gate", "json-text", "run-record-keys", "python-3-14"):
            with self.subTest(text=text):
                self.assertTrue(is_identifier(text))

    def test_anything_else_is_no_identifier(self):
        for text in ("", "Relation-model", "relation_model", "relation--model", "-gate", "gate-",
                     "relation model", "gate/1", "elements/common", "WAY-09", "gate."):
            with self.subTest(text=text):
                self.assertFalse(is_identifier(text))

    def test_the_pattern_matches_what_is_identifier_accepts(self):
        self.assertEqual(IDENTIFIER, r"[a-z0-9]+(?:-[a-z0-9]+)*")
        self.assertIsNotNone(re.fullmatch(IDENTIFIER, "entry-version-number"))


class Version(unittest.TestCase):
    def test_a_number_without_a_leading_zero_is_a_version(self):
        for text in ("1", "2", "10", "205"):
            with self.subTest(text=text):
                self.assertIsNotNone(re.fullmatch(VERSION, text))

    def test_zero_a_leading_zero_and_anything_else_are_no_version(self):
        for text in ("0", "01", "007", "", "1a", "v1", "-1"):
            with self.subTest(text=text):
                self.assertIsNone(re.fullmatch(VERSION, text))


class Cited(unittest.TestCase):
    def test_an_identifier_at_a_version_is_cited(self):
        for text in ("map-identifier-form/1", "storage-quota/12"):
            with self.subTest(text=text):
                self.assertTrue(is_cited(text))
                self.assertIsNotNone(re.fullmatch(CITED, text))

    def test_a_citation_off_the_form_is_not_cited(self):
        for text in ("map-identifier-form", "map-identifier-form/01", "map-identifier-form/0",
                     "Map-identifier-form/1", "map-identifier-form/1 (the map)",
                     "map-identifier-form/1/2", "/1"):
            with self.subTest(text=text):
                self.assertFalse(is_cited(text))


if __name__ == "__main__":
    unittest.main()
