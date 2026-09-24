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
import subprocess
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
# A new wording of that decision, which the commit merged onto holds, and its fingerprint.
NEW_WORDING = "The product keeps every saved game after any reload."
NEW_WORDING_FINGERPRINT = "69b731d5"


class WordingReachesDependants(unittest.TestCase):
    def guard(self, text, onto=None):
        """Runs the guard as it checks a merge onto the main branch, the only run that compares
        fingerprints with the current wording. The commit it merges onto holds the log `onto`,
        or is an empty one; the working tree holds the branch's log `text`."""
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "decisions.md")
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=directory, check=True,
                           capture_output=True)
            if onto is not None:
                with open(path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(onto)
                subprocess.run(["git", "add", "decisions.md"], cwd=directory, check=True,
                               capture_output=True)
            subprocess.run(["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com",
                            "commit", "-q", "--allow-empty", "-m", "main"], cwd=directory,
                           check=True, capture_output=True)
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            output = io.StringIO()
            code = format_guard.run(path, today=TODAY, stream=output, merge_onto="main")
            return code, output.getvalue()

    def test_the_wording_this_test_stands_on_has_not_changed(self):
        """Guards the literals below: a changed fixture fails here, loudly, instead of making
        the checks below pass for the wrong reason."""
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

    def test_a_reference_on_a_wording_the_merge_replaces_is_reported(self):
        """The commit merged onto holds a new wording of ABC-01; the branch's relation still
        carries the fingerprint of the old one."""
        code, output = self.guard(
            log(version(1), version(2, relations="derives from ABC-01@" + CURRENT)),
            onto=log(version(1), version(1, ver=2, binding=NEW_WORDING,
                                         change="new wording · previous: ABC-01/1")))
        self.assertEqual(code, 1, output)
        self.assertIn("ABC-02/1: `derives from ABC-01@" + CURRENT + "` — the current fingerprint "
                      "of ABC-01 is " + NEW_WORDING_FINGERPRINT, output)


if __name__ == "__main__":
    unittest.main()
