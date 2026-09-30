"""End-to-end test of the critical flow `wording-reaches-dependants`.

Someone rewrites the binding sentences of a decision; every `derives from` or `narrows` relation
carrying the old fingerprint has to be reported before the change reaches the main branch. This
test runs the whole path: the fingerprint of a decision's binding part, a relation in another
decision that carries it, and the guard that compares the two.

The expected fingerprints are written out below on purpose. A test does not compute its expected
value with the code it checks: were this test to call `fingerprint()`, a change to that function
would make it pass instead of fail.

Run from the root of the-way: python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl
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
        fingerprints with the current wording. The branch leaves the main branch at an empty
        commit; the commit it merges onto is that one, or, given `onto`, a later commit holding
        the log `onto`, so that the merge takes that log's versions as added on the main branch.
        The working tree holds the branch's log `text`."""
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "decisions.md")

            def git(*arguments):
                subprocess.run(["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com"]
                               + list(arguments), cwd=directory, check=True, capture_output=True)

            git("init", "-q", "-b", "main")
            git("commit", "-q", "--allow-empty", "-m", "main")
            if onto is not None:
                git("checkout", "-q", "-b", "onto")
                with open(path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(onto)
                git("add", "decisions.md")
                git("commit", "-q", "-m", "onto")
                git("checkout", "-q", "main")
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            output = io.StringIO()
            code = format_guard.run(path, today=TODAY, stream=output,
                                    merge_onto="main" if onto is None else "onto")
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
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(
            log(version(1), version(2, relations="derives from ABC-01@" + SUPERSEDED)))
        self.assertEqual(code, 1, output)
        self.assertIn(CURRENT, output)

    def test_a_reference_on_a_wording_the_merge_replaces_is_reported(self):
        """The commit merged onto holds a new wording of ABC-01; the branch's relation still
        carries the fingerprint of the old one."""
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(
            log(version(1), version(2, relations="derives from ABC-01@" + CURRENT)),
            onto=log(version(1), version(1, ver=2, binding=NEW_WORDING,
                                         change="new wording")))
        self.assertEqual(code, 1, output)
        self.assertIn("ABC-02/1: `derives from ABC-01@" + CURRENT + "` — the current fingerprint "
                      "of ABC-01 is " + NEW_WORDING_FINGERPRINT, output)

    def test_a_narrowing_on_a_superseded_wording_is_reported(self):
        """`narrows` carries a fingerprint as `derives from` does, and is reported the same way."""
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(
            log(version(1), version(2, relations="narrows ABC-01@" + SUPERSEDED)))
        self.assertEqual(code, 1, output)
        self.assertIn("ABC-02/1: `narrows ABC-01@" + SUPERSEDED + "` — the current fingerprint of "
                      "ABC-01 is " + CURRENT, output)

    def test_every_stale_relation_of_every_decision_is_reported(self):
        """ABC-03 carries a relation on the current wording and then a stale one; ABC-04 carries
        a stale one of its own."""
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(log(
            version(1), version(2),
            version(3, relations="derives from ABC-01@" + CURRENT + " · derives from ABC-02@"
                    + SUPERSEDED),
            version(4, relations="narrows ABC-01@" + SUPERSEDED)))
        self.assertEqual(code, 1, output)
        self.assertIn("ABC-03/1: `derives from ABC-02@" + SUPERSEDED + "` — the current "
                      "fingerprint of ABC-02 is " + CURRENT, output)
        self.assertIn("ABC-04/1: `narrows ABC-01@" + SUPERSEDED + "` — the current fingerprint "
                      "of ABC-01 is " + CURRENT, output)

    def test_every_stale_relation_is_reported_wherever_it_stands_in_the_list(self):
        """ABC-04 carries stale relations first and last with a current one between them; ABC-05
        carries a stale one between two current ones; ABC-06 carries two stale ones and nothing
        else."""
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(log(
            version(1), version(2), version(3),
            version(4, relations="derives from ABC-01@" + SUPERSEDED + " · derives from ABC-02@"
                    + CURRENT + " · narrows ABC-03@" + SUPERSEDED),
            version(5, relations="derives from ABC-01@" + CURRENT + " · narrows ABC-02@"
                    + SUPERSEDED + " · derives from ABC-03@" + CURRENT),
            version(6, relations="narrows ABC-01@" + SUPERSEDED + " · derives from ABC-02@"
                    + SUPERSEDED)))
        self.assertEqual(code, 1, output)
        for reported in ("ABC-04/1: `derives from ABC-01@%s` — the current fingerprint of ABC-01",
                         "ABC-04/1: `narrows ABC-03@%s` — the current fingerprint of ABC-03",
                         "ABC-05/1: `narrows ABC-02@%s` — the current fingerprint of ABC-02",
                         "ABC-06/1: `narrows ABC-01@%s` — the current fingerprint of ABC-01",
                         "ABC-06/1: `derives from ABC-02@%s` — the current fingerprint of ABC-02"):
            self.assertIn(reported % SUPERSEDED + " is " + CURRENT, output)

    def test_a_stale_relation_in_the_latest_version_is_reported(self):
        """ABC-02/1 leans on the current wording; ABC-02/2, the latest version, on a stale one."""
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(log(
            version(1), version(2, relations="derives from ABC-01@" + CURRENT),
            version(2, ver=2, relations="derives from ABC-01@" + SUPERSEDED)))
        self.assertEqual(code, 1, output)
        self.assertIn("ABC-02/2: `derives from ABC-01@" + SUPERSEDED + "` — the current "
                      "fingerprint of ABC-01 is " + CURRENT, output)

    def test_a_fingerprint_that_differs_only_after_its_fourth_character_is_reported(self):
        """79890000 shares its first four characters with the current 798975ff."""
        # invariant: decision-guard-stale-reference/1
        code, output = self.guard(log(version(1),
                                      version(2, relations="derives from ABC-01@79890000")))
        self.assertEqual(code, 1, output)
        self.assertIn("ABC-02/1: `derives from ABC-01@79890000` — the current fingerprint of "
                      "ABC-01 is " + CURRENT, output)


if __name__ == "__main__":
    unittest.main()
