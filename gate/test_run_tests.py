"""Tests of the test runner: each outcome a `unittest` test can have reaches the record as its line.

Every test writes a module of tests out, runs the runner on it in a process of its own, and
compares the record with the lines written out below (WAY-70). The citations in those modules
stand inside strings, never at the start of a line of this file, so that the invariants guard
reads none of them as a citation of this file.

Run from the root of the-way: python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
RUNNER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_tests.py")
PROGRAM = "gate/run_tests.py"
SAMPLE = "tests/test_sample.py"
RECORD = os.path.join(".runs", "tests.jsonl")
# The null line for a citation that stands outside any test: file, line and value.
STRAY = "%s:%d: `invariant: %s` stands outside any test, and a check cites at the check (WAY-65)"


def module(*lines):
    return "\n".join(("import os", "import unittest", "", "") + lines) + "\n"


def line(check, verdict, invariant, description=None):
    """A line of the record, written out as the test expects it."""
    written = {"check": check, "verdict": verdict, "invariant": invariant}
    if description is not None:
        written["description"] = description
    return written


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

    def run_tests(self, directory="tests", **files):
        """Writes each module under tests/, runs the runner on `directory` from the root, and
        returns its exit code, the lines of its record and what it printed for a person."""
        for name, text in files.items():
            self.write("tests/%s.py" % name, text)
        done = subprocess.run([sys.executable, "-B", RUNNER, directory, "--record", RECORD],
                              cwd=self.root, capture_output=True, text=True, encoding="utf-8")
        path = os.path.join(self.root, RECORD)
        lines = []
        if os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                lines = [json.loads(item) for item in handle.read().split("\n") if item]
        return done.returncode, lines, done.stderr


class Passing(RunnerTestCase):
    def test_a_passing_test_records_pass_for_each_invariant_it_cites(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/2",
            "        self.assertTrue(True)",
            "",
            "    def test_uncited(self):",
            "        pass"))
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1"),
                                 line(SAMPLE + "::Checks.test_holds", "pass", "beta-rule/2")])

    def test_a_citation_outside_the_body_of_a_test_cites_nothing_and_is_named(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "# invariant: alpha-rule/1",
            "class Checks(unittest.TestCase):",
            "    # invariant: beta-rule/1",
            "",
            "    def helper(self):",
            "        # invariant: gamma-rule/1",
            "        return True",
            "",
            "    def test_holds(self):",
            "        self.assertTrue(self.helper())  # invariant: delta-rule/1"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE, "fail", None, STRAY % (SAMPLE, number, value))
                                 for number, value in ((5, "alpha-rule/1"), (7, "beta-rule/1"),
                                                       (10, "gamma-rule/1"))])

    def test_a_decorated_test_and_a_nested_function_keep_their_citations(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "def plain(function):",
            "    return function",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    @plain",
            "    def test_holds(self):",
            "        def inner():",
            "            # invariant: alpha-rule/1",
            "            return True",
            "        self.assertTrue(inner())"))
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1")])

    def test_the_record_is_overwritten(self):
        self.write(".runs/tests.jsonl", "a line of an earlier run\n")
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1")])

    def test_the_report_for_a_person_stays(self):
        _, _, printed = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')"))
        self.assertIn("Ran 1 test", printed)
        self.assertIn("FAILED (failures=1)", printed)
        self.assertIn("AssertionError: the rule is broken", printed)


class Failing(RunnerTestCase):
    def test_a_failing_test_records_fail_for_each_invariant_it_cites(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')"))
        self.assertEqual(code, 1)
        failed = "failed: AssertionError: the rule is broken"
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_breaks", "fail", "alpha-rule/1",
                                      failed),
                                 line(SAMPLE + "::Checks.test_breaks", "fail", "beta-rule/1",
                                      failed)])

    def test_a_failing_test_that_cites_nothing_records_null(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_breaks(self):",
            "        self.fail('the rule is broken')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_breaks", "fail", None,
                                      "failed: AssertionError: the rule is broken")])

    def test_an_error_records_fail(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_crashes(self):",
            "        # invariant: alpha-rule/1",
            "        raise ValueError('no disk')",
            "",
            "    def test_uncited_crashes(self):",
            "        raise ValueError('no disk')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_crashes", "fail", "alpha-rule/1",
                                      "error: ValueError: no disk"),
                                 line(SAMPLE + "::Checks.test_uncited_crashes", "fail", None,
                                      "error: ValueError: no disk")])

    def test_an_error_in_set_up_and_tear_down_records_fail(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Before(unittest.TestCase):",
            "    def setUp(self):",
            "        raise ValueError('no disk')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "",
            "class After(unittest.TestCase):",
            "    def tearDown(self):",
            "        raise ValueError('disk full')",
            "",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::After.test_holds", "fail", "beta-rule/1",
                                      "error: ValueError: disk full"),
                                 line(SAMPLE + "::Before.test_holds", "fail", "alpha-rule/1",
                                      "error: ValueError: no disk")])

    def test_a_failing_subtest_records_fail(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_each(self):",
            "        # invariant: alpha-rule/1",
            "        for number in (2, 3):",
            "            with self.subTest(number=number):",
            "                self.assertEqual(number % 2, 0, 'odd')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_each", "fail", "alpha-rule/1",
                                      "failed in (number=3): AssertionError: 1 != 0 : odd")])

    def test_one_failing_check_of_an_invariant_leaves_the_other_s_pass_beside_it(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_b_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_b_breaks", "fail", "alpha-rule/1",
                                      "failed: AssertionError: the rule is broken"),
                                 line(SAMPLE + "::Checks.test_a_holds", "pass", "alpha-rule/1")])

    def test_citations_off_the_form_record_null(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/01",
            "        # invariant: Alpha-rule/1",
            "        # invariant: alpha-rule/",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "cites `%s`, which is not `<identifier>/<version>`" % value)
                                 for value in ("alpha-rule/01", "Alpha-rule/1", "alpha-rule/")])

    def test_an_interrupted_test_leaves_no_line_for_what_it_cites(self):
        """test_b is interrupted: alpha-rule, which test_a passed, gets no line, and the run
        says it stopped."""
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_b_interrupted(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        raise KeyboardInterrupt"))
        self.assertEqual(code, 2)
        self.assertEqual(lines, [line(PROGRAM, "fail", None,
                                      "the run stopped before every test ran")])

    def test_a_citation_off_the_form_records_null(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "cites `alpha-rule`, which is not "
                                      "`<identifier>/<version>`")])


class NoPass(RunnerTestCase):
    """A verdict is what a test gave (WAY-61, WAY-63): a skipped test gives none, and what it
    cites gets no pass from any test of the run; an expected failure that fails gives `fail`; an
    unexpected success gives `pass`, with a null line on its stale mark."""

    def test_a_skipped_test_gives_no_verdict_and_a_null_line(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @unittest.skip('waits for a disk')",
            "    def test_decorated(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_skips_itself(self):",
            "        # invariant: beta-rule/1",
            "        self.skipTest('no disk here')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_decorated", "fail", None,
                                      "no verdict for alpha-rule/1: skipped: waits for a disk"),
                                 line(SAMPLE + "::Checks.test_skips_itself", "fail", None,
                                      "no verdict for beta-rule/1: skipped: no disk here")])

    def test_a_skipped_test_takes_the_pass_of_another_test_citing_the_same_invariant(self):
        """test_a passes alpha-rule, test_b skips it: alpha-rule gets no line at all."""
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_b_skips(self):",
            "        # invariant: alpha-rule/1",
            "        self.skipTest('no disk here')",
            "",
            "    def test_c_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_b_skips", "fail", None,
                                      "no verdict for alpha-rule/1: skipped: no disk here")])

    def test_a_fail_stands_beside_a_skip(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_b_skips(self):",
            "        # invariant: alpha-rule/1",
            "        self.skipTest('no disk here')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_a_breaks", "fail", "alpha-rule/1",
                                      "failed: AssertionError: the rule is broken"),
                                 line(SAMPLE + "::Checks.test_b_skips", "fail", None,
                                      "no verdict for alpha-rule/1: skipped: no disk here")])

    def test_a_skip_inside_a_subtest_gives_no_verdict_saying_it_was_skipped(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_each(self):",
            "        # invariant: alpha-rule/1",
            "        for number in (2, 3):",
            "            with self.subTest(number=number):",
            "                if number == 3:",
            "                    self.skipTest('no disk here')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_each", "fail", None,
                                      "no verdict for alpha-rule/1: skipped in (number=3): no "
                                      "disk here")])

    def test_a_failing_subtest_beside_a_skipped_one_gives_fail(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_each(self):",
            "        # invariant: alpha-rule/1",
            "        for number in (2, 3):",
            "            with self.subTest(number=number):",
            "                if number == 2:",
            "                    self.skipTest('no disk here')",
            "                self.fail('odd')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_each", "fail", "alpha-rule/1",
                                      "failed in (number=3): AssertionError: odd")])

    def test_a_skipped_test_that_cites_nothing_records_no_line(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @unittest.skip('waits for a disk')",
            "    def test_decorated(self):",
            "        pass"))
        self.assertEqual(code, 0)
        self.assertEqual(lines, [])

    def test_an_expected_failure_records_fail(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @unittest.expectedFailure",
            "    def test_known_to_break(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    @unittest.expectedFailure",
            "    def test_uncited_known_to_break(self):",
            "        self.fail('the rule is broken')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_known_to_break", "fail",
                                      "alpha-rule/1", "marked as an expected failure, and "
                                      "failed: AssertionError: the rule is broken")])

    def test_an_expected_failure_that_cites_nothing_records_no_line(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @unittest.expectedFailure",
            "    def test_known_to_break(self):",
            "        self.fail('the rule is broken')"))
        self.assertEqual(code, 0)
        self.assertEqual(lines, [])

    def test_an_unexpected_success_gives_pass_and_a_null_line_on_the_stale_mark(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @unittest.expectedFailure",
            "    def test_cited(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    @unittest.expectedFailure",
            "    def test_uncited(self):",
            "        pass"))
        self.assertEqual(code, 1)
        stale = "marked as an expected failure, yet passed: the mark is stale"
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_cited", "fail", None, stale),
                                 line(SAMPLE + "::Checks.test_cited", "pass", "alpha-rule/1"),
                                 line(SAMPLE + "::Checks.test_uncited", "fail", None, stale)])


class Fixtures(RunnerTestCase):
    def test_a_failed_set_up_of_a_class_records_null_and_fails_what_its_tests_cite(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @classmethod",
            "    def setUpClass(cls):",
            "        raise ValueError('no disk')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_uncited(self):",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.setUpClass", "fail", None,
                                      "setUpClass failed: ValueError: no disk"),
                                 line(SAMPLE + "::Checks.test_holds", "fail", "alpha-rule/1",
                                      "not run: setUpClass failed: ValueError: no disk")])

    def test_a_failed_set_up_of_a_module_records_null_and_fails_what_its_tests_cite(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "def setUpModule():",
            "    raise ValueError('no disk')",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::setUpModule", "fail", None,
                                      "setUpModule failed: ValueError: no disk"),
                                 line(SAMPLE + "::Checks.test_holds", "fail", "alpha-rule/1",
                                      "not run: setUpModule failed: ValueError: no disk")])

    def test_a_failed_tear_down_of_a_class_records_null_beside_the_verdicts(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @classmethod",
            "    def tearDownClass(cls):",
            "        raise ValueError('disk full')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1"),
                                 line(SAMPLE + "::Checks.tearDownClass", "fail", None,
                                      "tearDownClass failed: ValueError: disk full")])


class Skips(RunnerTestCase):
    def test_a_skip_in_set_up_class_gives_no_verdict(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @classmethod",
            "    def setUpClass(cls):",
            "        raise unittest.SkipTest('no disk here')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: not run: setUpClass skipped "
                                      "it: no disk here")])


class Modules(RunnerTestCase):
    def test_a_module_that_cannot_be_imported_records_null_and_fails_what_it_cites(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "import no_such_module_anywhere",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_uncited(self):",
            "        pass"))
        self.assertEqual(code, 1)
        failure = "cannot be imported: ModuleNotFoundError: No module named " \
                  "'no_such_module_anywhere'"
        self.assertEqual(lines, [line(SAMPLE, "fail", None, failure),
                                 line(SAMPLE + "::Checks.test_holds", "fail", "alpha-rule/1",
                                      "not run: " + failure)])

    def test_a_module_that_cannot_be_parsed_fails_every_invariant_it_cites(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        return (",
            "",
            "    def test_other(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual([(item["check"], item["verdict"], item["invariant"]) for item in lines],
                         [(SAMPLE, "fail", None), (SAMPLE, "fail", "alpha-rule/1"),
                          (SAMPLE, "fail", "beta-rule/1")])

    def test_a_module_that_skips_itself_gives_no_verdict(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "raise unittest.SkipTest('no disk here')",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: not run: the module is "
                                      "skipped: no disk here")])

    def test_a_test_file_discovery_does_not_reach_gives_fail(self):
        """plain/ has no __init__.py, so discovery never enters it; its citing test never runs
        beside the passing one in the top file."""
        self.write("tests/plain/test_plain.py", module(
            "class Plain(unittest.TestCase):",
            "    def test_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')"))
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line("tests/plain/test_plain.py::Plain.test_breaks", "fail",
                                      "alpha-rule/1",
                                      "not run: discovery does not reach its file"),
                                 line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1")])

    def test_a_test_its_module_s_load_tests_leaves_out_gives_fail(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "",
            "def load_tests(loader, tests, pattern):",
            "    return unittest.TestSuite([Checks('test_holds')])"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_breaks", "fail", "alpha-rule/1",
                                      "not run: its module's suite leaves it out"),
                                 line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1")])

    def test_a_directory_with_no_test_records_null(self):
        self.write("tests/helpers.py", "VALUE = 1\n")
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(PROGRAM, "fail", None, "no test found in tests")])

    def test_a_directory_that_does_not_exist(self):
        code, lines, printed = self.run_tests(directory="missing")
        self.assertEqual(code, 2)
        self.assertIn("missing is not a directory", printed)
        self.assertEqual(lines, [line(PROGRAM, "fail", None, "missing is not a directory")])


class Stopped(RunnerTestCase):
    def test_a_run_that_stops_halfway_leaves_its_lines_and_no_pass_short_of_a_check(self):
        """The first test passes an invariant the third cites as well, and the process ends in
        the third: the failure of the second is readable, and no pass stands for the first."""
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_b_breaks(self):",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_c_stops(self):",
            "        # invariant: alpha-rule/1",
            "        os._exit(3)"))
        self.assertEqual(code, 3)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_b_breaks", "fail", "beta-rule/1",
                                      "failed: AssertionError: the rule is broken")])


class Form(RunnerTestCase):
    def test_a_line_holds_only_the_keys_of_the_form(self):
        _, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_breaks(self):",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_uncited(self):",
            "        raise ValueError('no disk')"))
        self.assertEqual(len(lines), 3)
        for item in lines:
            self.assertLessEqual(set(item), {"check", "verdict", "invariant", "description"})
            self.assertLessEqual({"check", "verdict", "invariant"}, set(item))
            self.assertIn(item["verdict"], ("pass", "fail"))


class Command(RunnerTestCase):
    """The command's own arguments: --record is optional, names one path, and a `.jsonl` one."""

    def setUp(self):
        super().setUp()
        self.write("tests/test_sample.py", module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))

    def invoke(self, *arguments):
        done = subprocess.run([sys.executable, "-B", RUNNER, "tests"] + list(arguments),
                              cwd=self.root, capture_output=True, text=True, encoding="utf-8")
        return done.returncode, done.stderr

    def files(self):
        found = set()
        for directory, _, names in os.walk(self.root):
            found.update(os.path.relpath(os.path.join(directory, name), self.root)
                         .replace(os.sep, "/") for name in names)
        return found

    def test_without_a_record_no_file_appears(self):
        before = self.files()
        code, printed = self.invoke()
        self.assertEqual(code, 0, printed)
        self.assertIn("Ran 1 test", printed)
        self.assertEqual(self.files(), before)

    def test_a_record_whose_path_does_not_end_in_jsonl_is_refused(self):
        code, printed = self.invoke("--record", ".runs/tests.txt")
        self.assertEqual(code, 2, printed)
        self.assertIn("--record .runs/tests.txt: the record of a run is a JSON Lines file, whose "
                      "path ends in .jsonl", printed)
        self.assertFalse(os.path.exists(os.path.join(self.root, ".runs")))

    def test_a_record_given_twice_is_refused(self):
        code, printed = self.invoke("--record", ".runs/one.jsonl", "--record", ".runs/two.jsonl")
        self.assertEqual(code, 2, printed)
        self.assertIn("--record is given twice; a run writes one record", printed)
        self.assertFalse(os.path.exists(os.path.join(self.root, ".runs")))


class InARepository(RunnerTestCase):
    """The runner run from the root of a repository as the gate runs it: git holds the tree on a
    task branch, `foundations/invariants.md` lists entries, and code that is not a test, some of
    it holding citation lines, lies beside the tests and elsewhere."""

    INVARIANTS = "\n".join([
        "# Invariants", "",
        "## alpha-rule/1", "", "The first rule holds.", "", "- **Method:** `TODO`", "",
        "## beta-rule/1", "", "The second rule holds.", "", "- **Method:** `TODO`", "",
        "## gamma-rule/1", "", "The third rule holds.", "", "- **Method:** `TODO`", ""])

    FIRST = module(
        "from helper import VALUE",
        "",
        "",
        "class First(unittest.TestCase):",
        "    def test_holds(self):",
        "        # invariant: alpha-rule/2",
        "        self.assertEqual(VALUE, 1)")

    SECOND = module(
        "class Second(unittest.TestCase):",
        "    def test_holds(self):",
        "        # invariant: beta-rule/1",
        "        pass")

    HELPER = "\n".join([
        "VALUE = 1",
        "",
        "",
        "def check():",
        "    # invariant: gamma-rule/1",
        "    return VALUE", ""])

    TOOL = "\n".join([
        "def tool():",
        "    # invariant: gamma-rule/1",
        "    return 0", ""])

    def git(self, *arguments):
        subprocess.run(["git"] + list(arguments), cwd=self.root, check=True,
                       capture_output=True)

    def setUp(self):
        super().setUp()
        self.write("foundations/invariants.md", self.INVARIANTS)
        self.write(".gitignore", ".runs/\n")
        self.write("src/tool.py", self.TOOL)
        self.write("tests/helper.py", self.HELPER)
        self.write("tests/test_first.py", self.FIRST)
        self.write("tests/test_second.py", self.SECOND)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "runner@example.com")
        self.git("config", "user.name", "Runner")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "main")
        # the-way's own work runs on a branch named `foundations`; a product's on others
        self.git("branch", "foundations")
        self.git("checkout", "-q", "-b", "task")

    def test_only_what_the_tests_cite_is_recorded_as_they_cite_it(self):
        """alpha-rule stands at version 1 in the invariants, and the test cites version 2; the
        helper and the code outside the tests cite gamma-rule, and no test does."""
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "pass",
                                      "beta-rule/1")])

    def test_a_file_the_branch_changed_leaves_the_others_their_lines(self):
        self.write("tests/test_second.py", self.SECOND.replace("        pass",
                                                               "        self.assertTrue(True)"))
        self.git("commit", "-q", "-am", "task")
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "pass",
                                      "beta-rule/1")])

    def test_a_second_run_follows_a_change_made_after_the_first(self):
        self.run_tests()
        self.write("tests/test_second.py", self.SECOND.replace(
            "        pass", "        self.fail('the rule is broken')"))
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "fail",
                                      "beta-rule/1",
                                      "failed: AssertionError: the rule is broken")])

    def test_a_helper_or_set_up_defined_after_a_citing_test_lends_it_nothing(self):
        self.write("tests/test_second.py", module(
            "class Second(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        self.assertTrue(self.helper())",
            "",
            "    def helper(self):",
            "        # invariant: gamma-rule/1",
            "        return True",
            "",
            "    def setUp(self):",
            "        # invariant: alpha-rule/1",
            "        self.ready = True"))
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 1)
        second = "tests/test_second.py"
        self.assertEqual(lines, [line(second, "fail", None, STRAY % (second, 11, "gamma-rule/1")),
                                 line(second, "fail", None, STRAY % (second, 15, "alpha-rule/1")),
                                 line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "pass",
                                      "beta-rule/1")])

    def test_other_spellings_and_text_in_a_string_are_no_citations(self):
        self.write("tests/test_second.py", module(
            "class Second(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        # Invariant: gamma-rule/1",
            "        # invariants: alpha-rule/1",
            "        text = '# invariant: delta-rule/1'",
            "        other = '''",
            "        # invariant: epsilon-rule/1",
            "        '''",
            "        self.assertTrue(text and other)"))
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "pass",
                                      "beta-rule/1")])

    def test_a_test_imports_the_product_s_own_modules_from_the_working_directory(self):
        self.write("app.py", "def add(first, second):\n    return first + second\n")
        self.write("tests/test_second.py", module(
            "import app",
            "",
            "",
            "class Second(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        self.assertEqual(app.add(2, 3), 5)"))
        code, lines, printed = self.run_tests()
        self.assertEqual(code, 0, printed)
        self.assertEqual(lines, [line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "pass",
                                      "beta-rule/1")])

    def test_a_citation_with_words_after_it_is_off_the_form(self):
        self.write("tests/test_second.py", module(
            "class Second(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1 and more",
            "        pass"))
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line("tests/test_first.py::First.test_holds", "pass",
                                      "alpha-rule/2"),
                                 line("tests/test_second.py::Second.test_holds", "fail", None,
                                      "cites `beta-rule/1 and more`, which is not "
                                      "`<identifier>/<version>`")])


if __name__ == "__main__":
    unittest.main()
