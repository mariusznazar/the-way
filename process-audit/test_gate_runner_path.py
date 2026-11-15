"""Test of the invariant gate-runner-path: the path of the test runner of the gate, from whose
history `process-audit/audit_count.py` starts a series of the gate times, is a file git tracks.

The reader, `audit_count.py`, is imported: it is a file of this part. The writing side is the
repository itself, read through git, never imported.

Run from the root of the-way: python -B gate/run_tests.py process-audit
"""

import subprocess
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
THE_WAY = HERE.parent
sys.path.insert(0, str(HERE))

import audit_count  # noqa: E402


def tracked(path):
    """The files git tracks that the path names, as `git ls-files` lists them."""
    done = subprocess.run(["git", "-C", str(THE_WAY), "ls-files", "-z", "--", ":(literal)" + path],
                          capture_output=True, check=True)
    return [name for name in done.stdout.decode("utf-8").split("\0") if name]


class GateRunnerPath(unittest.TestCase):

    def test_the_path_the_audit_reads_the_history_of_is_a_file_git_tracks(self):
        # invariant: gate-runner-path
        # Break caught: moving or renaming the test runner of the gate while the audit keeps the
        # old path; the history of a path that does not exist is empty, so no change of the runner
        # would ever start a new series of the gate times and the audit would compare times of
        # two runners.
        path = audit_count.GATE_TEST_RUNNER
        self.assertEqual([path], tracked(path))

    def test_a_path_git_does_not_track_is_listed_as_no_file(self):
        # Break caught: a listing that names a path git does not track, which would let the test
        # above pass whatever the reader holds.
        self.assertEqual([], tracked("gate/no_such_runner.py"))


if __name__ == "__main__":
    unittest.main()
