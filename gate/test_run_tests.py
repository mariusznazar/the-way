"""Tests of the test runner: which tests one command runs, and the exit code it gives.

Every test writes modules of tests out into a directory of its own, runs the runner there in a
process of its own, and compares its exit code and report with the values written out below.

Run from the root of the-way: python -B gate/run_tests.py gate
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
RUNNER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_tests.py")


def module(*tests):
    """A module of tests, one test method for each line of body given."""
    lines = ["import unittest", "", "", "class Checks(unittest.TestCase):"]
    for number, body in enumerate(tests):
        lines += ["    def test_%d(self):" % number, "        " + body, ""]
    return "\n".join(lines) + "\n"


PASSING = module("self.assertTrue(True)")


class RunnerTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = self.directory.name

    def tearDown(self):
        self.directory.cleanup()

    def write(self, relative, text):
        path = os.path.join(self.root, *relative.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)

    def runner(self, *arguments, cwd=None):
        """Runs the runner from the root, or from `cwd` below it; returns its exit code and all
        it printed."""
        done = subprocess.run([sys.executable, "-B", RUNNER] + list(arguments),
                              cwd=os.path.join(self.root, cwd or ""), capture_output=True,
                              text=True, encoding="utf-8", errors="replace")
        return done.returncode, done.stdout + done.stderr

    def git(self, *arguments):
        subprocess.run(["git", "-c", "user.name=Runner", "-c", "user.email=runner@example.com"]
                       + list(arguments), cwd=self.root, check=True, capture_output=True)

    def track(self, *paths):
        """Makes the root a git repository tracking the files given."""
        self.git("init", "-q")
        self.git("add", "--", *paths)


class OneDirectory(RunnerTestCase):
    def test_passing_tests_exit_zero(self):
        self.write("tests/test_sample.py",
                   module("self.assertTrue(True)", "self.assertEqual(2, 2)"))
        code, output = self.runner("tests")
        self.assertEqual(code, 0, output)
        self.assertIn("Ran 2 tests", output)

    def test_a_failing_test_exits_one(self):
        # invariant: gate-exit-code
        self.write("tests/test_sample.py",
                   module("self.assertTrue(True)", "self.assertEqual(2, 3)"))
        code, output = self.runner("tests")
        self.assertEqual(code, 1, output)
        self.assertIn("FAILED (failures=1)", output)

    def test_an_erring_test_exits_one(self):
        # invariant: gate-exit-code
        self.write("tests/test_sample.py", module("raise RuntimeError('broken')"))
        code, output = self.runner("tests")
        self.assertEqual(code, 1, output)
        self.assertIn("RuntimeError: broken", output)

    def test_a_module_that_cannot_be_imported_exits_one(self):
        # invariant: gate-exit-code
        self.write("tests/test_sample.py", "import no_such_module_anywhere\n" + PASSING)
        code, output = self.runner("tests")
        self.assertEqual(code, 1, output)
        self.assertIn("no_such_module_anywhere", output)

    def test_an_unexpected_success_exits_one(self):
        # invariant: gate-exit-code
        self.write("tests/test_sample.py", "\n".join((
            "import unittest", "", "",
            "class Checks(unittest.TestCase):",
            "    @unittest.expectedFailure",
            "    def test_known_to_break(self):",
            "        self.assertTrue(True)", "")))
        code, output = self.runner("tests")
        self.assertEqual(code, 1, output)
        self.assertIn("unexpected successes=1", output)

    def test_a_directory_holding_no_test_exits_one(self):
        # invariant: gate-exit-code
        self.write("tests/helper.py", "VALUE = 1\n")
        code, output = self.runner("tests")
        self.assertEqual(code, 1, output)
        self.assertIn("no test found in tests", output)

    def test_a_path_that_is_no_directory_exits_two(self):
        code, output = self.runner("missing")
        self.assertEqual(code, 2, output)
        self.assertIn("missing is not a directory", output)

    def test_tests_import_from_the_working_directory(self):
        self.write("helper_at_root.py", "VALUE = 7\n")
        self.write("tests/test_sample.py", "import helper_at_root\n"
                   + module("self.assertEqual(helper_at_root.VALUE, 7)"))
        code, output = self.runner("tests")
        self.assertEqual(code, 0, output)


class EveryDirectory(RunnerTestCase):
    def test_every_directory_holding_a_tracked_test_file_runs_in_a_process_of_its_own(self):
        # invariant: gate-exit-code
        # Two modules of one name in two directories: run in one process, the second would be
        # taken for the first, and its tests would not run.
        self.write("a/test_same.py", PASSING)
        self.write("b/c/test_same.py", module("self.assertTrue(True)", "self.assertTrue(True)"))
        self.write("b/c/notes.txt", "not a test\n")
        self.write("untracked/test_other.py", module("self.fail('an untracked file ran')"))
        self.track("a/test_same.py", "b/c/test_same.py", "b/c/notes.txt")
        code, output = self.runner()
        self.assertEqual(code, 0, output)
        self.assertIn("== a\n", output)
        self.assertIn("== b/c\n", output)
        self.assertNotIn("untracked", output)
        self.assertTrue(output.rstrip().endswith("3 tests in 2 directories; every directory "
                                                 "passed"), output)

    def test_a_failing_directory_fails_the_run_and_the_rest_still_run(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", module("self.assertEqual(1, 2)"))
        self.write("b/test_two.py", PASSING)
        self.track("a/test_one.py", "b/test_two.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        self.assertIn("== b\n", output)
        self.assertTrue(output.rstrip().endswith("2 tests in 2 directories; failed: a (exit "
                                                 "code 1)"), output)

    def test_a_directory_whose_tracked_test_file_is_gone_does_not_run(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", PASSING)
        self.write("gone/test_gone.py", PASSING)
        self.track("a/test_one.py", "gone/test_gone.py")
        os.remove(os.path.join(self.root, "gone", "test_gone.py"))
        code, output = self.runner()
        self.assertEqual(code, 0, output)
        self.assertNotIn("== gone", output)

    def test_a_process_exiting_zero_before_unittest_reports_fails_the_run(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", module("import os; os._exit(0)"))
        self.write("b/test_two.py", PASSING)
        self.track("a/test_one.py", "b/test_two.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        self.assertTrue(output.rstrip().endswith("1 tests in 2 directories; failed: a (exit "
                                                 "code 0 without unittest's OK)"), output)

    def test_a_report_that_does_not_end_with_ok_fails_the_run(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", "import atexit\n"
                   "atexit.register(print, 'printed after the report')\n" + PASSING)
        self.track("a/test_one.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        self.assertIn("printed after the report", output)
        self.assertTrue(output.rstrip().endswith("1 tests in 1 directories; failed: a (exit "
                                                 "code 0 without unittest's OK)"), output)

    def test_a_repository_without_a_tracked_test_file_exits_one(self):
        # invariant: gate-exit-code
        self.write("a/helper.py", "VALUE = 1\n")
        self.track("a/helper.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        self.assertIn("no directory holds a test_*.py file git tracks", output)

    def test_a_run_from_a_folder_below_the_root_runs_every_directory(self):
        self.write("a/test_one.py", PASSING)
        self.write("b/test_two.py", PASSING)
        self.track("a/test_one.py", "b/test_two.py")
        code, output = self.runner(cwd="b")
        self.assertEqual(code, 0, output)
        self.assertIn("== a\n", output)
        self.assertIn("2 tests in 2 directories", output)

    def test_outside_a_git_repository_it_exits_two(self):
        outside = tempfile.TemporaryDirectory()
        self.addCleanup(outside.cleanup)
        done = subprocess.run([sys.executable, "-B", RUNNER], cwd=outside.name,
                              capture_output=True, text=True,
                              env=dict(os.environ, GIT_CEILING_DIRECTORIES=os.path.dirname(
                                  outside.name)))
        self.assertEqual(done.returncode, 2, done.stdout + done.stderr)
        self.assertIn("git cannot list the files of the repository", done.stdout)


if __name__ == "__main__":
    unittest.main()
