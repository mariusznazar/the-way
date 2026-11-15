"""Test of the invariant review-tag-pattern: every name that `foundation-review/SKILL.md` gives the
tag that marks a review done is found by the pattern from which `task-cycle/review_reminder.py`
counts the merges since the last review.

The reader, `review_reminder.py`, is imported: it is a file of this part. The writing side is the
skill of `foundation-review`, read as text for the form of the name, and the tags are made on a
repository built for the test, so that git itself matches them.

Run from the root of the-way: python -B gate/run_tests.py task-cycle
"""

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
THE_WAY = HERE.parent
sys.path.insert(0, str(HERE))

import review_reminder  # noqa: E402

SKILL = "foundation-review/SKILL.md"
IDENTITY = ["-c", "user.name=Test", "-c", "user.email=test@example.com",
            "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false"]
# What the skill puts where the date goes, and the date this test gives it.
DATE_FORM = "YYYY-MM-DD"
DATE = "2026-01-10"


def skill_text():
    """The text of the skill, every run of spaces and line breaks made one space."""
    return " ".join((THE_WAY / SKILL).read_text(encoding="utf-8").split())


def names_the_skill_gives():
    """The tag names the skill's step "Mark the review done" gives: the name with the date, and
    that name with each suffix the skill adds where a tag of the date exists."""
    text = skill_text()
    named = re.search(r"Name the tag `([^`]*%s[^`]*)`" % DATE_FORM, text)
    suffixes = re.search(r"add `(-[0-9]+)`, then `(-[0-9]+)`", text)
    if not named or not suffixes:
        raise AssertionError("%s no longer gives the name of the tag as this test reads it" % SKILL)
    first = named.group(1).replace(DATE_FORM, DATE)
    return [first] + [first + suffix for suffix in suffixes.groups()]


def last_review_tag_after_tagging(name):
    """What the reader finds as the last review tag on a repository whose one commit carries a tag
    of this name, made as the skill makes it: annotated."""
    with tempfile.TemporaryDirectory() as directory:
        for arguments in (["init", "--quiet"], ["commit", "--quiet", "--allow-empty", "-m", "root"],
                          ["tag", "-a", "-m", "review", name]):
            subprocess.run(["git", *IDENTITY, "-C", directory, *arguments], check=True,
                           capture_output=True)
        return review_reminder.last_review_tag(Path(directory), "HEAD")


class ReviewTagPattern(unittest.TestCase):

    def test_the_reader_finds_every_name_the_skill_gives(self):
        # invariant: review-tag-pattern
        # Break caught: renaming the tag in the skill, or the pattern in the script, in one place
        # only; the script then counts from the start of history in every repository and the
        # reminder tells the human to review what a review has just read.
        for name in names_the_skill_gives():
            with self.subTest(name=name):
                self.assertEqual(name, last_review_tag_after_tagging(name))

    def test_the_names_the_skill_gives_are_three_and_differ(self):
        # Break caught: a skill that gives one name for the tag three times, which would let the
        # test above check one name.
        names = names_the_skill_gives()
        self.assertEqual(3, len(set(names)))

    def test_a_tag_of_another_name_is_not_found(self):
        # Break caught: a pattern that finds every tag, which would let the first test pass for
        # any name the skill gives.
        self.assertIsNone(last_review_tag_after_tagging("v" + DATE))


if __name__ == "__main__":
    unittest.main()
