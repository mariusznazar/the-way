"""Test of the invariant audit-series-script-paths: each path of a script whose history
`process-audit/audit_count.py` reads through `process-audit/version_analysis.py`, which it
imports, to start a new series of the cost of cycles, of the measures of how a cycle's agents use
context and the prompt cache or of the gate times, is a file git tracks — the script that measures
the cost, `task-cycle/cycle_stages.py` with the module `task-cycle/stage_transcripts.py` that it
imports, the script that counts those measures, the script that records the gate times and the
test runner of the gate.

The reader holds those paths in `version_analysis.py`, which is imported: it is a file of this
part. The writing side is the repository itself, read through git, never imported.

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

from version_analysis import (  # noqa: E402
    COST_SCRIPTS,
    GATE_SCRIPT,
    GATE_TEST_RUNNER,
    MEASURES_SCRIPT,
    TOOL_GROUPS,
)


def tracked(path):
    """The files git tracks that the path names, as `git ls-files` lists them."""
    done = subprocess.run(
        ["git", "-C", str(THE_WAY), "ls-files", "-z", "--", ":(literal)" + path],
        capture_output=True,
        check=True,
    )
    return [name for name in done.stdout.decode("utf-8").split("\0") if name]


class AuditSeriesScriptPaths(unittest.TestCase):
    def test_each_path_the_audit_reads_the_history_of_is_a_file_git_tracks(self):
        # invariant: audit-series-script-paths
        # Break caught: moving or renaming one of the files while the audit keeps the old
        # path; the history of a path that does not exist is empty, so no change of the script
        # would ever start a new series and the audit would compare measures of two scripts.
        # The script that measures the cost spans two files, `cycle_stages.py` and the module
        # `stage_transcripts.py` it imports, since the reading of the transcripts moved out of
        # `cycle_stages.py` (WAY-339, `audit-series-script-paths`); the expected value changes with
        # that cause (WAY-233), and the request names this invariant test (WAY-03).
        paths = (
            *COST_SCRIPTS,
            MEASURES_SCRIPT,
            GATE_SCRIPT,
            GATE_TEST_RUNNER,
        )
        for path in paths:
            with self.subTest(path=path):
                self.assertEqual([path], tracked(path))

    def test_the_paths_are_those_that_start_the_series(self):
        # Break caught: a path added to the audit's series that the test above does not name, so
        # that it would stand unguarded.
        # The script that measures the cost spans two files, `cycle_stages.py` and the module
        # `stage_transcripts.py` it imports, since the reading of the transcripts moved out of
        # `cycle_stages.py` (WAY-339, `audit-series-script-paths`); the expected value changes with
        # that cause (WAY-233), and the request names this invariant test (WAY-03).
        started = {path for _file, paths in TOOL_GROUPS for path in paths}
        self.assertEqual(
            {
                "task-cycle/cycle_stages.py",
                "task-cycle/stage_transcripts.py",
                MEASURES_SCRIPT,
                GATE_SCRIPT,
                GATE_TEST_RUNNER,
            },
            started,
        )

    def test_a_path_git_does_not_track_is_listed_as_no_file(self):
        # Break caught: a listing that names a path git does not track, which would let the test
        # above pass whatever the reader holds.
        self.assertEqual([], tracked("gate/no_such_runner.py"))


if __name__ == "__main__":
    unittest.main()
