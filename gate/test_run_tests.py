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
SKIPPING = "\n".join((
    "import unittest", "", "",
    "class Checks(unittest.TestCase):",
    "    def test_passing(self):",
    "        self.assertTrue(True)", "",
    "    @unittest.skip('no network here')",
    "    def test_skipped(self):",
    "        self.fail('a skipped test ran')", ""))


def timed_module(log, name, wait_for=(), pause=0.0, lines=0, fail=False, after_an_end=False):
    """A module of one test for the runs of directories at the same time.

    The test appends `start <name>` to the file `log`, prints `lines` lines of its own to the error
    output (half of them before it waits, half after), waits until `log` holds each line of `wait_for`
    (up to 120 seconds, a failure after that), sleeps `pause` seconds and appends `end <name>`. With
    `after_an_end` it fails unless `log` already holds an `end` line when it starts. With `fail` it
    fails after the wait."""
    return "\n".join((
        "import sys, time, unittest", "",
        "LOG = %r" % log, "",
        "def logged():",
        "    try:",
        "        with open(LOG, encoding='utf-8') as handle:",
        "            return handle.read().splitlines()",
        "    except FileNotFoundError:",
        "        return []", "",
        "def append(text):",
        "    with open(LOG, 'a', encoding='utf-8') as handle:",
        "        handle.write(text + '\\n')", "",
        "def say(first, last):",
        "    for number in range(first, last):",
        "        print(%r + '-line-' + str(number), file=sys.stderr)" % name, "",
        "class Checks(unittest.TestCase):",
        "    def test_it(self):",
        "        append('start %s')" % name,
        "        if %r:" % after_an_end,
        "            self.assertTrue(any(line.startswith('end ') for line in logged()), "
        "'started before another directory ended')",
        "        say(0, %d)" % (lines // 2),
        "        deadline = time.time() + 120",
        "        while time.time() < deadline and not all(line in logged() for line in %r):"
        % list(wait_for),
        "            time.sleep(0.02)",
        "        self.assertTrue(all(line in logged() for line in %r), 'did not meet the others')"
        % list(wait_for),
        "        time.sleep(%r)" % pause,
        "        say(%d, %d)" % (lines // 2, lines),
        "        append('end %s')" % name,
        "        self.assertFalse(%r, 'broken')" % fail, ""))


def blocks(output):
    """The report of each directory in the order it stands in `output`, each as the lines between
    its `== <directory>` line and the next one, and the last line of the output."""
    lines = output.splitlines()
    found, name = [], None
    for line in lines[:-1]:
        if line.startswith("== "):
            name = line[3:]
            found.append((name, []))
        elif name is not None:
            found[-1][1].append(line)
    return found, lines[-1]


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

    def test_a_skipped_test_is_named_with_its_reason_before_the_closing_lines(self):
        self.write("tests/test_sample.py", SKIPPING)
        code, output = self.runner("tests")
        self.assertEqual(code, 0, output)
        lines = [line for line in output.splitlines() if line.strip()]
        self.assertEqual(lines[-4:], [
            "skipped: test_sample.Checks.test_skipped: no network here",
            "-" * 70,
            lines[-2],
            "OK (skipped=1)"], output)
        self.assertTrue(lines[-2].startswith("Ran 2 tests in "), output)

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

    def test_a_directory_with_a_skipped_test_still_passes_and_the_report_names_it(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", PASSING)
        self.write("b/test_sample.py", SKIPPING)
        self.track("a/test_one.py", "b/test_sample.py")
        code, output = self.runner()
        self.assertEqual(code, 0, output)
        self.assertIn("skipped: test_sample.Checks.test_skipped: no network here\n", output)
        self.assertLess(output.index("skipped: test_sample"), output.index("OK (skipped=1)"))
        self.assertTrue(output.rstrip().endswith("3 tests in 2 directories; every directory "
                                                 "passed"), output)

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


class DirectoriesAtOnce(RunnerTestCase):
    def log(self):
        return os.path.join(self.root, "timeline.log")

    def logged(self):
        with open(self.log(), encoding="utf-8") as handle:
            return handle.read().splitlines()

    def test_an_interrupt_leaves_the_directories_still_queued_unstarted(self):
        # The interrupt is made to come at once, when the runner starts waiting for the first
        # directory to end; with one job, the directories after the first are still queued.
        log = self.log()
        for name in "abc":
            self.write("%s/test_one.py" % name, timed_module(log, name, pause=0.3))
        self.track("a/test_one.py", "b/test_one.py", "c/test_one.py")
        interrupting = """
import runpy, sys

script = sys.argv[1]
loaded = runpy.run_path(script)


def interrupt(futures):
    raise KeyboardInterrupt


loaded['concurrent'].futures.as_completed = interrupt
try:
    loaded['run_all'](jobs=1)
except KeyboardInterrupt:
    print('interrupted')
"""
        done = subprocess.run([sys.executable, "-B", "-c", interrupting, RUNNER], cwd=self.root,
                              capture_output=True, text=True, encoding="utf-8", errors="replace")
        self.assertIn("interrupted", done.stdout, done.stdout + done.stderr)
        self.assertEqual(self.logged(), ["start a", "end a"], done.stdout + done.stderr)

    def test_by_default_every_directory_runs_at_the_same_time(self):
        # Each test waits until the other two have started, so a run one after another fails them.
        log = self.log()
        self.write("a/test_one.py", timed_module(log, "a", ["start b", "start c"]))
        self.write("b/test_one.py", timed_module(log, "b", ["start a", "start c"]))
        self.write("c/test_one.py", timed_module(log, "c", ["start a", "start b"]))
        self.track("a/test_one.py", "b/test_one.py", "c/test_one.py")
        code, output = self.runner()
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("3 tests in 3 directories; every directory "
                                                 "passed"), output)

    def test_one_job_runs_the_directories_one_after_another(self):
        log = self.log()
        for name in "abc":
            self.write("%s/test_one.py" % name, timed_module(log, name, pause=0.3))
        self.track("a/test_one.py", "b/test_one.py", "c/test_one.py")
        code, output = self.runner("--jobs", "1")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.logged(), ["start a", "end a", "start b", "end b", "start c",
                                         "end c"], output)

    def test_a_number_of_jobs_limits_the_directories_that_run_at_once(self):
        # a and b wait for each other, so both run at once; c fails unless one of them ended before
        # it started.
        log = self.log()
        self.write("a/test_one.py", timed_module(log, "a", ["start b"]))
        self.write("b/test_one.py", timed_module(log, "b", ["start a"]))
        self.write("c/test_one.py", timed_module(log, "c", after_an_end=True))
        self.track("a/test_one.py", "b/test_one.py", "c/test_one.py")
        code, output = self.runner("--jobs", "2")
        self.assertEqual(code, 0, output)
        self.assertEqual(sorted(self.logged()[:2]), ["start a", "start b"], output)

    def test_a_wrong_number_of_jobs_exits_two_and_runs_nothing(self):
        self.write("a/test_one.py", PASSING)
        self.track("a/test_one.py")
        for value in ("0", "-1", "many", "1.5"):
            code, output = self.runner("--jobs", value)
            self.assertEqual(code, 2, output)
            self.assertIn("--jobs", output)
            self.assertNotIn("== a", output)

    def test_jobs_given_with_a_directory_change_nothing(self):
        self.write("tests/test_sample.py", PASSING)
        code, output = self.runner("tests", "--jobs", "3")
        self.assertEqual(code, 0, output)
        self.assertIn("Ran 1 test", output)

    def test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end(self):
        # a stays running until b has ended, so b's report comes first although a sorts first; each
        # test prints lines before and after the wait, which a run that let the two reports run
        # into each other would mix.
        log = self.log()
        self.write("a/test_one.py",
                   timed_module(log, "a", ["end b"], pause=2.0, lines=4))
        self.write("b/test_one.py", timed_module(log, "b", lines=4))
        self.track("a/test_one.py", "b/test_one.py")
        code, output = self.runner()
        self.assertEqual(code, 0, output)
        found, last = blocks(output)
        self.assertEqual([name for name, _ in found], ["b", "a"], output)
        for name, body in found:
            self.assertEqual([line for line in body if "-line-" in line],
                             ["%s-line-%d" % (name, number) for number in range(4)], output)
            self.assertEqual(sum(1 for line in body if line.startswith("Ran 1 test in ")), 1,
                             output)
            self.assertEqual(body[-1], "OK", output)
        self.assertEqual(last, "2 tests in 2 directories; every directory passed")

    def test_failed_directories_are_named_in_sorted_order_whatever_the_order_they_ended_in(self):
        # invariant: gate-exit-code
        log = self.log()
        self.write("a/test_one.py", timed_module(log, "a", ["end b"], pause=1.0, fail=True))
        self.write("b/test_one.py", timed_module(log, "b", fail=True))
        self.write("c/test_one.py", PASSING)
        self.track("a/test_one.py", "b/test_one.py", "c/test_one.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        found, last = blocks(output)
        self.assertEqual(sorted(name for name, _ in found), ["a", "b", "c"], output)
        self.assertEqual(last, "3 tests in 3 directories; failed: a (exit code 1), b (exit code "
                               "1)")

    def test_a_report_with_no_line_end_at_its_end_does_not_run_into_the_next_line(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", "import atexit, sys\n"
                   "atexit.register(sys.stderr.write, 'cut off')\n" + PASSING)
        self.write("b/test_two.py", PASSING)
        self.track("a/test_one.py", "b/test_two.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        lines = output.splitlines()
        self.assertIn("cut off", lines, output)
        self.assertIn("== b", lines, output)
        self.assertTrue(output.rstrip().endswith("2 tests in 2 directories; failed: a (exit "
                                                 "code 0 without unittest's OK)"), output)

    def test_a_directory_that_prints_nothing_leaves_no_blank_line_under_its_name(self):
        # invariant: gate-exit-code
        self.write("a/test_one.py", module("import os; os._exit(0)"))
        self.track("a/test_one.py")
        code, output = self.runner()
        self.assertEqual(code, 1, output)
        self.assertEqual(output.splitlines(), ["== a", "0 tests in 1 directories; failed: a (exit "
                                                      "code 0 without unittest's OK)"], output)

    def test_a_run_of_one_directory_in_the_default_form_keeps_the_report_unittest_prints(self):
        self.write("a/test_one.py", PASSING)
        self.track("a/test_one.py")
        code, output = self.runner()
        self.assertEqual(code, 0, output)
        lines = output.splitlines()
        self.assertEqual(lines[:3], ["== a", ".", "-" * 70], output)
        self.assertRegex(lines[3], r"^Ran 1 test in \d+\.\d{3}s$")
        self.assertEqual(lines[4:], ["", "OK", "1 tests in 1 directories; every directory "
                                               "passed"], output)


SLOW_AND_FAST = "\n".join((
    "import time, unittest", "", "",
    "class Checks(unittest.TestCase):",
    "    def test_fast(self):",
    "        self.assertTrue(True)", "",
    "    def test_slow(self):",
    "        time.sleep(0.3)", ""))


class SlowestTests(RunnerTestCase):
    def test_the_option_names_the_slowest_tests_with_their_time(self):
        self.write("tests/test_sample.py", SLOW_AND_FAST)
        code, output = self.runner("tests", "--slowest", "1")
        self.assertEqual(code, 0, output)
        lines = output.splitlines()
        header = lines.index("Slowest test durations")
        listed = lines[header + 2:lines.index("", header)]
        self.assertEqual(len(listed), 1, output)
        self.assertRegex(listed[0], r"^0\.\d{3}s +test_slow ")
        self.assertNotIn("test_fast", output)

    def test_in_a_run_of_every_directory_each_report_holds_its_own_slowest_tests(self):
        self.write("a/test_sample.py", SLOW_AND_FAST)
        self.write("b/test_other.py", PASSING)
        self.track("a/test_sample.py", "b/test_other.py")
        code, output = self.runner("--slowest", "1")
        self.assertEqual(code, 0, output)
        found, last = blocks(output)
        slowest = {name: any(line == "Slowest test durations" for line in body)
                   for name, body in found}
        self.assertEqual(slowest, {"a": True, "b": True}, output)
        body = dict(found)["a"]
        self.assertTrue(any(line.endswith("test_slow (test_sample.Checks.test_slow)")
                            for line in body), output)
        self.assertEqual(last, "3 tests in 2 directories; every directory passed")

    def test_without_the_option_no_list_of_slowest_tests_is_printed(self):
        self.write("tests/test_sample.py", SLOW_AND_FAST)
        code, output = self.runner("tests")
        self.assertEqual(code, 0, output)
        self.assertNotIn("Slowest test durations", output)

    def test_a_wrong_number_of_slowest_tests_exits_two(self):
        self.write("tests/test_sample.py", PASSING)
        for value in ("0", "-2", "all"):
            code, output = self.runner("tests", "--slowest", value)
            self.assertEqual(code, 2, output)
            self.assertIn("--slowest", output)
            self.assertNotIn("Ran 1 test", output)

    def test_a_unittest_that_takes_no_durations_gives_a_message_and_exit_two(self):
        # What an older Python gives: a TextTestRunner with no `durations`, put in its place here.
        self.write("tests/test_sample.py", PASSING)
        patched = """
import runpy, sys, unittest


class Older:
    def __init__(self, stream=None, descriptions=True, verbosity=1, failfast=False,
                 buffer=False, resultclass=None, warnings=None, *, tb_locals=False):
        raise AssertionError('the runner was built')


unittest.TextTestRunner = Older
script = sys.argv[1]
sys.argv = [script, 'tests', '--slowest', '1']
runpy.run_path(script, run_name='__main__')
"""
        done = subprocess.run([sys.executable, "-B", "-c", patched, RUNNER], cwd=self.root,
                              capture_output=True, text=True, encoding="utf-8", errors="replace")
        self.assertEqual(done.returncode, 2, done.stdout + done.stderr)
        self.assertIn("--slowest", done.stderr)
        self.assertNotIn("Traceback", done.stderr)


if __name__ == "__main__":
    unittest.main()
