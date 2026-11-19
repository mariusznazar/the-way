"""Tests of the invariants blocked-request-wording and blocked-request-label: the wording that the
plan-state reader takes for the field `Request URL and status` of a record committed before its
request exists is the wording that the files of `task-cycle` which tell the cycle what to write
there give, under the label its record template gives the field.

The reader, `project-level/plan_state.py`, is imported: it is a file of this part. The writing side
is read as text, the way a skill of `task-cycle` is read by an agent: a literal text that the file
holds, found in the whitespace-normalised text of the file.

Run from the root of the-way: python -B gate/run_tests.py project-level
"""

import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
THE_WAY = HERE.parent
sys.path.insert(0, str(HERE))

import plan_state  # noqa: E402

# The files of `task-cycle` that tell the cycle what to write in the field of a record committed
# before its request exists, and the file that gives the field its label.
WRITERS = ("task-cycle/skill/reserved_return.md", "task-cycle/skill/blocked_finding.md")
RECORD_TEMPLATE = "task-cycle/record_template.md"


def text_of(path):
    """The text of a file of the-way, every run of spaces and line breaks made one space."""
    return " ".join((THE_WAY / path).read_text(encoding="utf-8").split())


def reads_as_blocked():
    """(the label of the line, the wording after it) that the reader takes for a blocked request:
    the reader's own constant, split at the first colon and space."""
    label, _, wording = plan_state.BLOCKED_DRAFT.partition(": ")
    return label, wording


class BlockedRequestLine(unittest.TestCase):
    def test_each_writer_gives_the_wording_the_reader_takes(self):
        # invariant: blocked-request-wording
        # Break caught: rewording what a skill of `task-cycle` tells the cycle to write, or what
        # the reader takes for it, in one place only; the reader then never reports the task as
        # blocked and the blocked task drops out of the plan's evidence unseen.
        _, wording = reads_as_blocked()
        for path in WRITERS:
            with self.subTest(path=path):
                self.assertIn("`" + wording + "`", text_of(path))

    def test_the_record_template_gives_the_label_the_reader_takes(self):
        # invariant: blocked-request-label
        # Break caught: renaming the field in the record's template while the reader keeps
        # looking for the old label.
        label, _ = reads_as_blocked()
        lines = (THE_WAY / RECORD_TEMPLATE).read_text(encoding="utf-8").splitlines()
        self.assertTrue([line for line in lines if line.startswith(label + ":")])

    def test_the_reader_takes_a_wording_it_splits_into_a_label_and_a_wording(self):
        # Break caught: a reader whose constant has no label or no wording, which would leave the
        # two tests above to check an empty text, found in every file.
        label, wording = reads_as_blocked()
        self.assertTrue(label.startswith("- ") and wording)


if __name__ == "__main__":
    unittest.main()
