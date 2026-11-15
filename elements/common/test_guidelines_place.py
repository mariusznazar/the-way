"""Test of the invariant guidelines-file-place: every file of a product's guidelines that
`product-guidelines/template.md` names, and the directory it names for them, lies where
`elements/common/foundation_check.py` reads the files of guidelines.

The reader, `foundation_check.py`, is imported: it is a file of this part. The writing side is the
template of `product-guidelines`, read as text for the paths in its section "Where guidelines go".

Run from the root of the-way: python -B gate/run_tests.py elements/common
"""

import re
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
THE_WAY = HERE.parent.parent
sys.path.insert(0, str(HERE))

import foundation_check  # noqa: E402

TEMPLATE = "product-guidelines/template.md"
SECTION = "Where guidelines go"
# What stands for a name the product chooses, `<discipline>` and `<part>` in the template.
PLACEHOLDER = re.compile(r"<[^>]+>")


def section_text():
    """The text of the template's section "Where guidelines go", up to the next `## ` heading."""
    text = (THE_WAY / TEMPLATE).read_text(encoding="utf-8")
    start = re.search(r"^## %s\s*$" % SECTION, text, re.MULTILINE)
    if not start:
        raise AssertionError("%s has no section %r" % (TEMPLATE, SECTION))
    rest = text[start.end():]
    following = re.search(r"^## ", rest, re.MULTILINE)
    return rest[:following.start()] if following else rest


def named_places():
    """(the files, the directories) the section names in backticks, whatever directory they lie
    in: a file as the path with each placeholder made `x`, a directory as the path ending in `/`;
    a pattern of the part map, which holds `*`, is neither."""
    files, directories = [], []
    for path in re.findall(r"`([^`\s]*/[^`\s]*)`", section_text()):
        if "*" in path:
            continue
        if path.endswith("/"):
            directories.append(path)
        else:
            files.append(PLACEHOLDER.sub("x", path))
    return files, directories


class GuidelinesFilePlace(unittest.TestCase):

    def test_every_file_the_template_names_is_read_by_the_check(self):
        # invariant: guidelines-file-place
        # Break caught: moving the directory of the guidelines, or nesting them, in the template
        # while the check keeps reading `guidelines/*.md`; the check would then stop reading the
        # references of the guidelines, and a reference naming no entry would pass.
        files, _ = named_places()
        self.assertTrue(files, "the section names no file of guidelines")
        for path in files:
            with self.subTest(path=path):
                self.assertTrue(foundation_check.GUIDELINES.match(path))

    def test_the_directory_the_template_names_holds_the_files_the_check_reads(self):
        # invariant: guidelines-file-place
        # Break caught: the template and the check agreeing on the shape of a file name while
        # naming different directories.
        _, directories = named_places()
        self.assertTrue(directories, "the section names no directory of guidelines")
        for path in directories:
            with self.subTest(path=path):
                self.assertTrue(foundation_check.GUIDELINES.match(path + "x.md"))

    def test_the_check_reads_no_file_outside_the_directory_or_below_it(self):
        # Break caught: a pattern of the check so loose that every file passes the two tests above.
        for path in ("docs/x.md", "guidelines/x/y.md", "guidelines/x.txt", "x/guidelines/x.md"):
            with self.subTest(path=path):
                self.assertFalse(foundation_check.GUIDELINES.match(path))


if __name__ == "__main__":
    unittest.main()
