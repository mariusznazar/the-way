"""End-to-end test of the critical flow `wording-reaches-dependants`.

Someone rewrites the binding sentences of a decision; every reference that leans on the old
wording has to be reported before the change reaches the main branch. This test runs the whole
path: the fingerprint of an entry's binding part, a reference in another entry that carries a
fingerprint, and the guard that compares the two.

The expected fingerprints are written out below on purpose. A test does not compute its expected
value with the code it checks: were this test to call `fingerprint()`, a change to that function
would make it pass instead of fail.

Run: python -B -m unittest discover -s <the-way>/gate -p "test_*.py"
"""

# flow: wording-reaches-dependants

import io
import os
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "elements", "decisions"))
import format_guard  # noqa: E402
from test_format_guard import BINDING, TODAY, log, version  # noqa: E402

WORDING = "The product keeps every saved game after a reload."
CURRENT = "798975ff"
SUPERSEDED = "69b731d5"


class WordingReachesDependants(unittest.TestCase):
    def guard(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "decisions.md")
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            output = io.StringIO()
            code = format_guard.run(path, today=TODAY, stream=output)
            return code, output.getvalue()

    def test_the_wording_this_test_stands_on_has_not_changed(self):
        """Guards the literals below: a changed fixture fails here, loudly, instead of making
        the two checks below pass for the wrong reason."""
        self.assertEqual(BINDING, WORDING)

    def test_a_reference_on_the_current_wording_passes(self):
        code, output = self.guard(
            log(version(1), version(2, relations="derives from ABC-01@" + CURRENT)))
        self.assertEqual(code, 0, output)

    def test_a_reference_on_a_superseded_wording_is_reported(self):
        code, output = self.guard(
            log(version(1), version(2, relations="derives from ABC-01@" + SUPERSEDED)))
        self.assertEqual(code, 1, output)
        self.assertIn(CURRENT, output)


if __name__ == "__main__":
    unittest.main()
