"""Tests of the test runner: each outcome a `unittest` test can have reaches the record as its line.

Every test writes a module of tests out, runs the runner on it in a process of its own, and
compares the record with the lines written out below (WAY-69). The citations in those modules
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


def without_passes(lines, *invariants):
    """The lines of a record but the pass lines of the invariants named: where a fail line stands
    for one of them, test-runner-pass-line leaves a pass beside it to the runner."""
    return [item for item in lines
            if not (item["verdict"] == "pass" and item["invariant"] in invariants)]


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

    def assertPassWithheld(self, lines, invariant):
        """The record holds no pass line for the invariant, or holds a fail line for it."""
        passed = [item for item in lines
                  if item["invariant"] == invariant and item["verdict"] == "pass"]
        failed = [item for item in lines
                  if item["invariant"] == invariant and item["verdict"] == "fail"]
        if passed and not failed:
            self.fail("%s has a pass line and no fail line: %s" % (invariant, passed))


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

    def test_identical_tests_in_two_files_both_pass(self):
        """Their code objects compare equal; each is still watched as its own."""
        same = module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        self.assertTrue(True)")
        code, lines, _ = self.run_tests(test_one=same, test_two=same)
        self.assertEqual(code, 0)
        self.assertEqual(lines, [line("tests/test_one.py::Checks.test_holds", "pass",
                                      "alpha-rule/1"),
                                 line("tests/test_two.py::Checks.test_holds", "pass",
                                      "alpha-rule/1")])

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
        # invariant: test-runner-pass-line/1
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
        """test_crashes errs mid-body, after an assertion that holds."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_crashes(self):",
            "        # invariant: alpha-rule/1",
            "        self.assertEqual(1, 1)",
            "        raise ValueError('no disk')",
            "        self.assertEqual(2, 2)",
            "",
            "    def test_uncited_crashes(self):",
            "        raise ValueError('no disk')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_crashes", "fail", "alpha-rule/1",
                                      "error: ValueError: no disk"),
                                 line(SAMPLE + "::Checks.test_uncited_crashes", "fail", None,
                                      "error: ValueError: no disk")])

    def test_an_error_in_set_up_records_fail(self):
        """setUp errs, so the test method never runs."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Before(unittest.TestCase):",
            "    def setUp(self):",
            "        raise ValueError('no disk')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Before.test_holds", "fail", "alpha-rule/1",
                                      "error: ValueError: no disk")])

    def test_an_error_in_tear_down_records_fail(self):
        """The test method ran to its end; tearDown errs after it."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class After(unittest.TestCase):",
            "    def tearDown(self):",
            "        raise ValueError('disk full')",
            "",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::After.test_holds", "fail", "beta-rule/1",
                                      "error: ValueError: disk full")])

    def test_a_failing_subtest_records_fail(self):
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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
        """A decorated method, a method skipping itself mid-body and a decorated class each
        skip; test_z_holds passes every invariant they cite."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @unittest.skip('waits for a disk')",
            "    def test_decorated(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "    def test_skips_itself(self):",
            "        # invariant: beta-rule/1",
            "        self.assertTrue(True)",
            "        self.skipTest('no disk here')",
            "        self.assertTrue(True)",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass",
            "",
            "",
            "@unittest.skip('waits for a disk')",
            "class Skipped(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_decorated", "fail", None,
                                      "no verdict for alpha-rule/1: skipped: waits for a disk"),
                                 line(SAMPLE + "::Checks.test_skips_itself", "fail", None,
                                      "no verdict for beta-rule/1: skipped: no disk here"),
                                 line(SAMPLE + "::Skipped.test_holds", "fail", None,
                                      "no verdict for gamma-rule/1: skipped: waits for a disk")])

    def test_a_skipped_test_takes_the_pass_of_another_test_citing_the_same_invariant(self):
        """test_a passes alpha-rule, test_b skips it: alpha-rule gets no line at all."""
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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

    BODIES = {"holds": "pass", "breaks": "self.fail('the rule is broken')",
              "skips": "self.skipTest('no disk here')"}

    def test_the_test_that_does_not_succeed_withholds_the_pass_wherever_it_stands(self):
        """Three tests cite alpha-rule; the one that fails or skips stands first, in the middle
        or last, and the other two pass."""
        # invariant: test-runner-pass-line/1
        broken = "failed: AssertionError: the rule is broken"
        skipped = "no verdict for alpha-rule/1: skipped: no disk here"
        cases = [
            (("a_breaks", "b_holds", "c_holds"),
             [line(SAMPLE + "::Checks.test_a_breaks", "fail", "alpha-rule/1", broken)]),
            (("a_holds", "b_breaks", "c_holds"),
             [line(SAMPLE + "::Checks.test_b_breaks", "fail", "alpha-rule/1", broken)]),
            (("a_holds", "b_holds", "c_breaks"),
             [line(SAMPLE + "::Checks.test_c_breaks", "fail", "alpha-rule/1", broken)]),
            (("a_skips", "b_holds", "c_holds"),
             [line(SAMPLE + "::Checks.test_a_skips", "fail", None, skipped)]),
            (("a_holds", "b_skips", "c_holds"),
             [line(SAMPLE + "::Checks.test_b_skips", "fail", None, skipped)]),
            (("a_holds", "b_holds", "c_skips"),
             [line(SAMPLE + "::Checks.test_c_skips", "fail", None, skipped)])]
        for methods, expected in cases:
            with self.subTest(methods=methods):
                text = ["class Checks(unittest.TestCase):"]
                for method in methods:
                    text += ["    def test_%s(self):" % method,
                             "        # invariant: alpha-rule/1",
                             "        " + self.BODIES[method[2:]], ""]
                code, lines, _ = self.run_tests(test_sample=module(*text))
                self.assertEqual(code, 1)
                self.assertEqual(without_passes(lines, "alpha-rule/1"), expected)
                self.assertPassWithheld(lines, "alpha-rule/1")

    def test_a_pass_an_earlier_run_left_in_the_record_does_not_stand(self):
        """The record holds a pass for alpha-rule from an earlier run; in this run the one test
        citing it skips."""
        # invariant: test-runner-pass-line/1
        self.write(".runs/tests.jsonl", '{"check": "tests/test_sample.py::Checks.test_holds", '
                                        '"verdict": "pass", "invariant": "alpha-rule/1"}\n')
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        self.skipTest('no disk here')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: skipped: no disk here")])


class Fixtures(RunnerTestCase):
    def test_a_failed_set_up_of_a_class_records_null_and_fails_what_its_tests_cite(self):
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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
        """Other.test_holds passes the invariant the skipped class's test cites."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    @classmethod",
            "    def setUpClass(cls):",
            "        raise unittest.SkipTest('no disk here')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "",
            "class Other(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: not run: setUpClass skipped "
                                      "it: no disk here")])

    def test_a_skip_in_set_up_module_gives_no_verdict(self):
        """test_second passes the invariant the skipped module's test cites."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(
            test_sample=module(
                "def setUpModule():",
                "    raise unittest.SkipTest('no disk here')",
                "",
                "",
                "class Checks(unittest.TestCase):",
                "    def test_holds(self):",
                "        # invariant: alpha-rule/1",
                "        pass"),
            test_second=module(
                "class Second(unittest.TestCase):",
                "    def test_holds(self):",
                "        # invariant: alpha-rule/1",
                "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: not run: setUpModule skipped "
                                      "it: no disk here")])


class Modules(RunnerTestCase):
    def test_a_module_that_cannot_be_imported_records_null_and_fails_what_it_cites(self):
        # invariant: test-runner-pass-line/1
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
        # invariant: test-runner-pass-line/1
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
        """test_second passes the invariant the skipped module's test cites."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(
            test_sample=module(
                "raise unittest.SkipTest('no disk here')",
                "",
                "",
                "class Checks(unittest.TestCase):",
                "    def test_holds(self):",
                "        # invariant: alpha-rule/1",
                "        pass"),
            test_second=module(
                "class Second(unittest.TestCase):",
                "    def test_holds(self):",
                "        # invariant: alpha-rule/1",
                "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: not run: the module is "
                                      "skipped: no disk here")])

    def test_a_test_file_discovery_does_not_reach_gives_fail(self):
        """plain/ has no __init__.py, so discovery enters neither it nor plain/inner/, nor
        package/plain/ below a package; the test in the top file passes all three invariants."""
        # invariant: test-runner-pass-line/1
        self.write("tests/plain/test_plain.py", module(
            "class Plain(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.write("tests/plain/inner/test_inner.py", module(
            "class Inner(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.write("tests/package/__init__.py", "")
        self.write("tests/package/plain/test_deep.py", module(
            "class Deep(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: gamma-rule/1",
            "        pass"))
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        not_reached = "not run: discovery does not reach its file"
        self.assertEqual(without_passes(lines, "alpha-rule/1", "beta-rule/1", "gamma-rule/1"), [
            line("tests/package/plain/test_deep.py::Deep.test_holds", "fail", "gamma-rule/1",
                 not_reached),
            line("tests/plain/test_plain.py::Plain.test_holds", "fail", "alpha-rule/1",
                 not_reached),
            line("tests/plain/inner/test_inner.py::Inner.test_holds", "fail", "beta-rule/1",
                 not_reached)])
        for invariant in ("alpha-rule/1", "beta-rule/1", "gamma-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_a_test_file_in_a_hidden_folder_gives_fail(self):
        """.hidden/, package/.cache/ and package/__pycache__/ have no __init__.py, and a folder
        named with a leading dot, or __pycache__, is under the directory as much as any other."""
        # invariant: test-runner-pass-line/1
        self.write("tests/.hidden/test_hidden.py", module(
            "class Hidden(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.write("tests/package/__init__.py", "")
        self.write("tests/package/.cache/test_cached.py", module(
            "class Cached(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.write("tests/package/__pycache__/test_compiled.py", module(
            "class Compiled(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: gamma-rule/1",
            "        pass"))
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        not_reached = "not run: discovery does not reach its file"
        self.assertEqual(without_passes(lines, "alpha-rule/1", "beta-rule/1", "gamma-rule/1"), [
            line("tests/.hidden/test_hidden.py::Hidden.test_holds", "fail", "alpha-rule/1",
                 not_reached),
            line("tests/package/.cache/test_cached.py::Cached.test_holds", "fail",
                 "beta-rule/1", not_reached),
            line("tests/package/__pycache__/test_compiled.py::Compiled.test_holds", "fail",
                 "gamma-rule/1", not_reached)])
        for invariant in ("alpha-rule/1", "beta-rule/1", "gamma-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_a_file_that_cannot_be_parsed_where_discovery_does_not_reach_gives_fail(self):
        """plain/ has no __init__.py, and plain/test_broken.py is no Python; the test in the
        top file passes the invariant the broken file cites."""
        # invariant: test-runner-pass-line/1
        self.write("tests/plain/test_broken.py", module(
            "class Broken(unittest.TestCase):",
            "    def test_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        return ("))
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1"), [
            line("tests/plain/test_broken.py", "fail", "alpha-rule/1",
                 "not run: its file cannot be parsed")])
        self.assertPassWithheld(lines, "alpha-rule/1")

    def test_a_test_class_under_an_if_a_try_or_a_function_is_found(self):
        """Runs and InTry are defined and run; NeverDefined stands under an `if` that is false,
        and Local in a function no code calls. Checks passes what those two cite."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "import sys",
            "",
            "",
            "if sys.platform != 'no-such-platform':",
            "    class Runs(unittest.TestCase):",
            "        def test_holds(self):",
            "            # invariant: alpha-rule/1",
            "            pass",
            "",
            "if sys.platform == 'no-such-platform':",
            "    class NeverDefined(unittest.TestCase):",
            "        def test_breaks(self):",
            "            # invariant: beta-rule/1",
            "            self.fail('the rule is broken')",
            "",
            "",
            "def build():",
            "    class Local(unittest.TestCase):",
            "        def test_breaks(self):",
            "            # invariant: gamma-rule/1",
            "            self.fail('the rule is broken')",
            "    return Local",
            "",
            "",
            "try:",
            "    class InTry(unittest.TestCase):",
            "        def test_holds(self):",
            "            # invariant: delta-rule/1",
            "            pass",
            "except ImportError:",
            "    pass",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        left_out = "not run: its module's suite leaves it out"
        self.assertEqual(without_passes(lines, "beta-rule/1", "gamma-rule/1"), [
            line(SAMPLE + "::NeverDefined.test_breaks", "fail", "beta-rule/1", left_out),
            line(SAMPLE + "::build.<locals>.Local.test_breaks", "fail", "gamma-rule/1",
                 left_out),
            line(SAMPLE + "::InTry.test_holds", "pass", "delta-rule/1"),
            line(SAMPLE + "::Runs.test_holds", "pass", "alpha-rule/1")])
        for invariant in ("beta-rule/1", "gamma-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_tests_a_load_tests_leaves_out_below_the_top_give_fail(self):
        """The load_tests of grouped/ and of nested/grouped/ return no test of their files, and
        the one of nested/deeper/test_deeper.py leaves test_left_out out."""
        # invariant: test-runner-pass-line/1
        leave_out = "def load_tests(loader, tests, pattern):\n    return tests\n"
        self.write("tests/grouped/__init__.py", leave_out)
        self.write("tests/grouped/test_grouped.py", module(
            "class Grouped(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.write("tests/nested/__init__.py", "")
        self.write("tests/nested/grouped/__init__.py", leave_out)
        self.write("tests/nested/grouped/test_grouped.py", module(
            "class NestedGrouped(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.write("tests/nested/deeper/__init__.py", "")
        self.write("tests/nested/deeper/test_deeper.py", module(
            "class Deeper(unittest.TestCase):",
            "    def test_kept(self):",
            "        # invariant: gamma-rule/1",
            "        pass",
            "",
            "    def test_left_out(self):",
            "        # invariant: gamma-rule/1",
            "        pass",
            "",
            "",
            "def load_tests(loader, tests, pattern):",
            "    return unittest.TestSuite([Deeper('test_kept')])"))
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1", "beta-rule/1", "gamma-rule/1"), [
            line("tests/grouped/test_grouped.py::Grouped.test_holds", "fail", "alpha-rule/1",
                 "not run: discovery does not reach its file"),
            line("tests/nested/deeper/test_deeper.py::Deeper.test_left_out", "fail",
                 "gamma-rule/1", "not run: its module's suite leaves it out"),
            line("tests/nested/grouped/test_grouped.py::NestedGrouped.test_holds", "fail",
                 "beta-rule/1", "not run: discovery does not reach its file")])
        for invariant in ("alpha-rule/1", "beta-rule/1", "gamma-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_a_test_its_module_s_load_tests_leaves_out_gives_fail(self):
        # invariant: test-runner-pass-line/1
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
        self.assertEqual(without_passes(lines, "alpha-rule/1"), [
            line(SAMPLE + "::Checks.test_breaks", "fail", "alpha-rule/1",
                 "not run: its module's suite leaves it out")])
        self.assertPassWithheld(lines, "alpha-rule/1")

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
        # invariant: test-runner-pass-line/1
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

    STOPPING = (
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
        "        %s",
        "",
        "    def test_d_holds(self):",
        "        # invariant: alpha-rule/1",
        "        pass")

    def test_a_process_that_ends_before_a_later_citing_test_leaves_no_pass(self):
        """test_c, which cites nothing, ends the process: test_d, which cites what test_a
        passed, never runs."""
        # invariant: test-runner-pass-line/1
        text = "\n".join(self.STOPPING) % "os._exit(3)"
        code, lines, _ = self.run_tests(test_sample=module(*text.split("\n")))
        self.assertEqual(code, 3)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_b_breaks", "fail", "beta-rule/1",
                                      "failed: AssertionError: the rule is broken")])

    def test_an_interruption_before_a_later_citing_test_leaves_no_pass(self):
        """test_c, which cites nothing, is interrupted: test_d, which cites what test_a
        passed, never runs."""
        # invariant: test-runner-pass-line/1
        text = "\n".join(self.STOPPING) % "raise KeyboardInterrupt"
        code, lines, _ = self.run_tests(test_sample=module(*text.split("\n")))
        self.assertEqual(code, 2)
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_b_breaks", "fail", "beta-rule/1",
                                      "failed: AssertionError: the rule is broken"),
                                 line(PROGRAM, "fail", None,
                                      "the run stopped before every test ran")])


class Bodies(RunnerTestCase):
    """Where a citing test's body did not execute and return, or something was raised out of it,
    its set-up, its tear-down or a subtest, the invariant it cites gets no pass without a fail —
    beside a test passing the same invariant."""

    def test_a_coroutine_or_a_generator_method_never_executes_its_body(self):
        """unittest calls such a method and leaves its body unrun, except a coroutine of an
        IsolatedAsyncioTestCase, which it awaits and whose body executes."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Awaited(unittest.IsolatedAsyncioTestCase):",
            "    async def test_awaited(self):",
            "        # invariant: gamma-rule/1",
            "        self.assertTrue(True)",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    async def test_a_coroutine(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_b_generator(self):",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')",
            "        yield",
            "",
            "    async def test_c_asynchronous_generator(self):",
            "        # invariant: delta-rule/1",
            "        self.fail('the rule is broken')",
            "        yield",
            "",
            "    def test_d_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: delta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        never = "its body never executed"
        self.assertEqual(without_passes(lines, "alpha-rule/1", "beta-rule/1", "delta-rule/1"), [
            line(SAMPLE + "::Awaited.test_awaited", "pass", "gamma-rule/1"),
            line(SAMPLE + "::Checks.test_a_coroutine", "fail", "alpha-rule/1", never),
            line(SAMPLE + "::Checks.test_b_generator", "fail", "beta-rule/1", never),
            line(SAMPLE + "::Checks.test_c_asynchronous_generator", "fail", "delta-rule/1",
                 never)])
        for invariant in ("alpha-rule/1", "beta-rule/1", "delta-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_a_failing_test_s_citation_counts_wherever_it_stands_in_the_body(self):
        # invariant: test-runner-pass-line/1
        # After a docstring or a statement, in a loop, a `with` or an `if`, and in a function
        # nested in the method.
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_after_a_docstring(self):",
            "        \"\"\"Breaks the rule.\"\"\"",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_b_after_a_statement(self):",
            "        value = 1",
            "        # invariant: beta-rule/1",
            "        self.assertEqual(value, 2)",
            "",
            "    def test_c_in_a_loop(self):",
            "        for value in (1,):",
            "            # invariant: gamma-rule/1",
            "            self.assertEqual(value, 2)",
            "",
            "    def test_d_in_a_with(self):",
            "        with open(os.devnull) as handle:",
            "            # invariant: delta-rule/1",
            "            self.assertEqual(handle.closed, True)",
            "",
            "    def test_e_in_an_if(self):",
            "        if True:",
            "            # invariant: epsilon-rule/1",
            "            self.fail('the rule is broken')",
            "",
            "    def test_f_in_a_nested_function(self):",
            "        def inner():",
            "            # invariant: zeta-rule/1",
            "            return False",
            "        self.assertTrue(inner())",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        # invariant: delta-rule/1",
            "        # invariant: epsilon-rule/1",
            "        # invariant: zeta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        invariants = ("alpha-rule/1", "beta-rule/1", "gamma-rule/1", "delta-rule/1",
                      "epsilon-rule/1", "zeta-rule/1")
        broken = "failed: AssertionError: the rule is broken"
        self.assertEqual(without_passes(lines, *invariants), [
            line(SAMPLE + "::Checks.test_a_after_a_docstring", "fail", "alpha-rule/1", broken),
            line(SAMPLE + "::Checks.test_b_after_a_statement", "fail", "beta-rule/1",
                 "failed: AssertionError: 1 != 2"),
            line(SAMPLE + "::Checks.test_c_in_a_loop", "fail", "gamma-rule/1",
                 "failed: AssertionError: 1 != 2"),
            line(SAMPLE + "::Checks.test_d_in_a_with", "fail", "delta-rule/1",
                 "failed: AssertionError: False != True"),
            line(SAMPLE + "::Checks.test_e_in_an_if", "fail", "epsilon-rule/1", broken),
            line(SAMPLE + "::Checks.test_f_in_a_nested_function", "fail", "zeta-rule/1",
                 "failed: AssertionError: False is not true")])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)

    def test_a_failing_test_s_citation_counts_however_it_is_spaced(self):
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_unspaced(self):",
            "        #invariant:alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_b_widely_spaced(self):",
            "        #   invariant:   beta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_c_trailing_spaces(self):",
            "        # invariant: gamma-rule/1   ",
            "        self.fail('the rule is broken')",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        broken = "failed: AssertionError: the rule is broken"
        invariants = ("alpha-rule/1", "beta-rule/1", "gamma-rule/1")
        self.assertEqual(without_passes(lines, *invariants), [
            line(SAMPLE + "::Checks.test_a_unspaced", "fail", "alpha-rule/1", broken),
            line(SAMPLE + "::Checks.test_b_widely_spaced", "fail", "beta-rule/1", broken),
            line(SAMPLE + "::Checks.test_c_trailing_spaces", "fail", "gamma-rule/1", broken)])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)

    def test_two_classes_with_a_method_of_one_name_keep_their_own_citations(self):
        """First.test_x and Second.test_x cite different invariants; the second fails, and
        Third passes what it cites."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class First(unittest.TestCase):",
            "    def test_x(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "",
            "class Second(unittest.TestCase):",
            "    def test_x(self):",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "",
            "class Third(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "beta-rule/1"), [
            line(SAMPLE + "::First.test_x", "pass", "alpha-rule/1"),
            line(SAMPLE + "::Second.test_x", "fail", "beta-rule/1",
                 "failed: AssertionError: the rule is broken")])
        self.assertPassWithheld(lines, "beta-rule/1")

    def test_a_citing_method_inherited_from_a_mixin_fails_in_its_subclass(self):
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Mixin:",
            "    value = 1",
            "",
            "    def test_inherited(self):",
            "        # invariant: alpha-rule/1",
            "        self.assertEqual(self.value, 1)",
            "",
            "",
            "class Checks(Mixin, unittest.TestCase):",
            "    value = 2",
            "",
            "",
            "class Holds(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1"), [
            line(SAMPLE + "::Checks.test_inherited", "fail", "alpha-rule/1",
                 "failed: AssertionError: 2 != 1")])
        self.assertPassWithheld(lines, "alpha-rule/1")

    def test_a_file_named_with_a_digit_after_test_is_a_test_file(self):
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(
            test_1case=module(
                "class Checks(unittest.TestCase):",
                "    def test_breaks(self):",
                "        # invariant: alpha-rule/1",
                "        self.fail('the rule is broken')"),
            test_sample=module(
                "class Checks(unittest.TestCase):",
                "    def test_holds(self):",
                "        # invariant: alpha-rule/1",
                "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1"), [
            line("tests/test_1case.py::Checks.test_breaks", "fail", "alpha-rule/1",
                 "failed: AssertionError: the rule is broken")])
        self.assertPassWithheld(lines, "alpha-rule/1")

    def test_an_error_inside_a_subtest_records_fail(self):
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_each(self):",
            "        # invariant: alpha-rule/1",
            "        for number in (2, 3):",
            "            with self.subTest(number=number):",
            "                if number == 3:",
            "                    raise KeyError('three')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1"), [
            line(SAMPLE + "::Checks.test_each", "fail", "alpha-rule/1",
                 "error in (number=3): KeyError: 'three'")])
        self.assertPassWithheld(lines, "alpha-rule/1")

    def test_a_message_the_record_cannot_encode_or_read_still_gives_fail(self):
        """test_a fails with a lone surrogate in its message, and test_b raises an exception
        whose text cannot be read; the run goes on to test_z."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Odd(Exception):",
            "    def __str__(self):",
            "        raise RuntimeError('no text')",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    def test_a_unwritable_message(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('broken \\ud800')",
            "",
            "    def test_b_unreadable_exception(self):",
            "        # invariant: beta-rule/1",
            "        raise Odd()",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1", "beta-rule/1"), [
            line(SAMPLE + "::Checks.test_a_unwritable_message", "fail", "alpha-rule/1",
                 "failed: AssertionError: broken \ud800"),
            line(SAMPLE + "::Checks.test_b_unreadable_exception", "fail", "beta-rule/1",
                 "error: Odd: <exception str() failed>")])
        for invariant in ("alpha-rule/1", "beta-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_a_test_left_with_no_outcome_gives_no_pass(self):
        """Silent's run() does nothing, so its test never starts; Checks passes the invariant
        it cites."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass",
            "",
            "",
            "class Silent(unittest.TestCase):",
            "    def run(self, result=None):",
            "        return result",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Silent.test_holds", "fail", None,
                                      "no verdict for alpha-rule/1: the test gave no outcome")])

    def test_an_earlier_pass_goes_when_the_process_ends_before_any_line(self):
        """The record holds a pass for alpha-rule from an earlier run; the one test citing it
        ends the process before the run writes a line."""
        # invariant: test-runner-pass-line/1
        self.write(".runs/tests.jsonl", '{"check": "tests/test_sample.py::Checks.test_holds", '
                                        '"verdict": "pass", "invariant": "alpha-rule/1"}\n')
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        os._exit(3)"))
        self.assertEqual(code, 3)
        self.assertEqual(lines, [])

    def test_a_body_run_outside_its_own_test_does_not_count_for_it(self):
        """Replaced's and CalledInSetUpClass's methods are replaced in __init__; Caller runs
        Replaced's real function in its own test, and setUpClass runs the other's."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "CALLS = []",
            "",
            "",
            "class CalledInSetUpClass(unittest.TestCase):",
            "    def __init__(self, name='runTest'):",
            "        super().__init__(name)",
            "        setattr(self, name, lambda: None)",
            "",
            "    @classmethod",
            "    def setUpClass(cls):",
            "        cls.__dict__['test_holds'](None)",
            "",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        CALLS.append('beta')",
            "",
            "",
            "class Caller(unittest.TestCase):",
            "    def test_calls(self):",
            "        Replaced.__dict__['test_holds'](None)",
            "",
            "",
            "class Holds(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        pass",
            "",
            "",
            "class Replaced(unittest.TestCase):",
            "    def __init__(self, name='runTest'):",
            "        super().__init__(name)",
            "        setattr(self, name, lambda: None)",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        CALLS.append('alpha')"))
        self.assertEqual(code, 1)
        never = "its body never executed"
        self.assertEqual(without_passes(lines, "alpha-rule/1", "beta-rule/1"), [
            line(SAMPLE + "::CalledInSetUpClass.test_holds", "fail", "beta-rule/1", never),
            line(SAMPLE + "::Replaced.test_holds", "fail", "alpha-rule/1", never)])
        for invariant in ("alpha-rule/1", "beta-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_an_equal_function_from_another_file_does_not_count_for_a_test(self):
        """twin_copy.py's Twin.test_holds matches the body of Twin.test_holds line for line, so
        the two code objects compare equal. Caller runs the real body in its own test; Twin's
        method is replaced in __init__ by a call to the copy, so its own body never executes."""
        # invariant: test-runner-pass-line/1
        self.write("tests/twin_copy.py", "\n" * 12 + "class Twin:\n" + "\n" * 4 +
                   "    def test_holds(self):\n\n        self.assertTrue(True)\n")
        code, lines, _ = self.run_tests(test_sample=module(
            "import twin_copy",
            "",
            "",
            "class Caller(unittest.TestCase):",
            "    def test_calls(self):",
            "        Twin.__dict__['test_holds'](self)",
            "",
            "",
            "class Twin(unittest.TestCase):",
            "    def __init__(self, name='runTest'):",
            "        super().__init__(name)",
            "        setattr(self, name, lambda: twin_copy.Twin.test_holds(self))",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        self.assertTrue(True)",
            "",
            "",
            "class Zeta(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1"), [
            line(SAMPLE + "::Twin.test_holds", "fail", "alpha-rule/1",
                 "its body never executed")])
        self.assertPassWithheld(lines, "alpha-rule/1")

    def test_a_test_method_defined_outside_its_class_is_watched_and_cites(self):
        """Assigned takes a module-level coroutine, a module-level function and a coroutine a
        factory builds as its test methods; only the plain function's body executes."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "async def shared(self):",
            "    # invariant: alpha-rule/1",
            "    self.fail('the rule is broken')",
            "",
            "",
            "def plain(self):",
            "    # invariant: beta-rule/1",
            "    self.assertTrue(True)",
            "",
            "",
            "def make():",
            "    async def built(self):",
            "        # invariant: gamma-rule/1",
            "        self.fail('the rule is broken')",
            "    return built",
            "",
            "",
            "class Assigned(unittest.TestCase):",
            "    test_a_shared = shared",
            "    test_b_plain = plain",
            "    test_c_built = make()",
            "",
            "",
            "class Holds(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        never = "its body never executed"
        self.assertEqual(without_passes(lines, "alpha-rule/1", "gamma-rule/1"), [
            line(SAMPLE + "::Assigned.test_a_shared", "fail", "alpha-rule/1", never),
            line(SAMPLE + "::Assigned.test_b_plain", "pass", "beta-rule/1"),
            line(SAMPLE + "::Assigned.test_c_built", "fail", "gamma-rule/1", never)])
        for invariant in ("alpha-rule/1", "gamma-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_a_body_that_never_executed_gives_fail_whatever_unittest_reports(self):
        """Reporting's and Bare's run() only report success; a method replaced in __init__ or in
        setUpClass; a decorator that never calls the method; a coroutine a decorator returns
        unawaited; a coroutine inherited from a mixin; a generator a decorator starts and leaves
        suspended. A coroutine asyncio.run drives executes. Holds passes every invariant the
        others cite."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "import asyncio",
            "import functools",
            "",
            "",
            "def never_call(function):",
            "    @functools.wraps(function)",
            "    def wrapper(self):",
            "        return None",
            "    return wrapper",
            "",
            "",
            "def plain_call(function):",
            "    @functools.wraps(function)",
            "    def wrapper(self):",
            "        return function(self)",
            "    return wrapper",
            "",
            "",
            "def run_async(function):",
            "    @functools.wraps(function)",
            "    def wrapper(self):",
            "        return asyncio.run(function(self))",
            "    return wrapper",
            "",
            "",
            "KEPT = []",
            "",
            "",
            "def first_step(function):",
            "    @functools.wraps(function)",
            "    def wrapper(self):",
            "        steps = function(self)",
            "        KEPT.append(steps)",
            "        next(steps)",
            "    return wrapper",
            "",
            "",
            "class AsyncMixin:",
            "    async def test_inherited(self):",
            "        # invariant: eta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "",
            "class Bare(unittest.TestCase):",
            "    def run(self, result=None):",
            "        result.addSuccess(self)",
            "        return result",
            "",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    @run_async",
            "    async def test_awaited(self):",
            "        # invariant: theta-rule/1",
            "        await asyncio.sleep(0)",
            "        self.assertTrue(True)",
            "",
            "    @never_call",
            "    def test_never_called(self):",
            "        # invariant: epsilon-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    @plain_call",
            "    async def test_not_awaited(self):",
            "        # invariant: zeta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    @first_step",
            "    def test_suspended(self):",
            "        # invariant: iota-rule/1",
            "        yield",
            "        self.fail('the rule is broken')",
            "",
            "",
            "class Holds(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        # invariant: delta-rule/1",
            "        # invariant: epsilon-rule/1",
            "        # invariant: zeta-rule/1",
            "        # invariant: eta-rule/1",
            "        # invariant: iota-rule/1",
            "        pass",
            "",
            "",
            "class Inheriting(AsyncMixin, unittest.TestCase):",
            "    pass",
            "",
            "",
            "class ReplacedInInit(unittest.TestCase):",
            "    def __init__(self, name='runTest'):",
            "        super().__init__(name)",
            "        setattr(self, name, lambda: None)",
            "",
            "    def test_holds(self):",
            "        # invariant: gamma-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "",
            "class ReplacedInSetUpClass(unittest.TestCase):",
            "    @classmethod",
            "    def setUpClass(cls):",
            "        cls.test_holds = lambda self: None",
            "",
            "    def test_holds(self):",
            "        # invariant: delta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "",
            "class Reporting(unittest.TestCase):",
            "    def run(self, result=None):",
            "        result.startTest(self)",
            "        result.addSuccess(self)",
            "        result.stopTest(self)",
            "        return result",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')"))
        self.assertEqual(code, 1)
        never = "its body never executed"
        invariants = ("alpha-rule/1", "beta-rule/1", "gamma-rule/1", "delta-rule/1",
                      "epsilon-rule/1", "zeta-rule/1", "eta-rule/1", "iota-rule/1")
        self.assertEqual(without_passes(lines, *invariants), [
            line(SAMPLE + "::Checks.test_awaited", "pass", "theta-rule/1"),
            line(SAMPLE + "::Checks.test_never_called", "fail", "epsilon-rule/1", never),
            line(SAMPLE + "::Checks.test_not_awaited", "fail", "zeta-rule/1", never),
            line(SAMPLE + "::Checks.test_suspended", "fail", "iota-rule/1",
                 "its body never returned"),
            line(SAMPLE + "::Inheriting.test_inherited", "fail", "eta-rule/1", never),
            line(SAMPLE + "::ReplacedInInit.test_holds", "fail", "gamma-rule/1", never),
            line(SAMPLE + "::ReplacedInSetUpClass.test_holds", "fail", "delta-rule/1", never),
            line(SAMPLE + "::Reporting.test_holds", "fail", "alpha-rule/1", never),
            line(SAMPLE + "::Bare.test_holds", "fail", "beta-rule/1", never)])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)

    def test_a_body_retried_or_run_twice_gives_fail_when_any_run_fails(self):
        """A decorator retries test_retried after its first run raised; the suite runs
        Twice.test_twice twice, and its second run fails; test_flaky fails in its one run and
        would pass in a second."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "import functools",
            "",
            "ATTEMPTS = []",
            "FLAKY = []",
            "RUNS = []",
            "",
            "",
            "def retry(function):",
            "    @functools.wraps(function)",
            "    def wrapper(self):",
            "        try:",
            "            function(self)",
            "        except AssertionError:",
            "            function(self)",
            "    return wrapper",
            "",
            "",
            "class Checks(unittest.TestCase):",
            "    @retry",
            "    def test_retried(self):",
            "        # invariant: alpha-rule/1",
            "        ATTEMPTS.append(1)",
            "        self.assertEqual(len(ATTEMPTS), 2)",
            "",
            "    def test_flaky(self):",
            "        # invariant: gamma-rule/1",
            "        FLAKY.append(1)",
            "        self.assertGreater(len(FLAKY), 1)",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass",
            "",
            "",
            "class Twice(unittest.TestCase):",
            "    def test_twice(self):",
            "        # invariant: beta-rule/1",
            "        RUNS.append(1)",
            "        self.assertEqual(len(RUNS), 1)",
            "",
            "",
            "def load_tests(loader, tests, pattern):",
            "    return unittest.TestSuite([Checks('test_retried'), Twice('test_twice'),",
            "                               Twice('test_twice'), Checks('test_flaky'),",
            "                               Checks('test_z_holds')])"))
        self.assertEqual(code, 1)
        invariants = ("alpha-rule/1", "beta-rule/1", "gamma-rule/1")
        self.assertEqual(without_passes(lines, *invariants), [
            line(SAMPLE + "::Checks.test_retried", "fail", "alpha-rule/1",
                 "raised out of its body"),
            line(SAMPLE + "::Twice.test_twice", "fail", "beta-rule/1",
                 "failed: AssertionError: 2 != 1"),
            line(SAMPLE + "::Checks.test_flaky", "fail", "gamma-rule/1",
                 "failed: AssertionError: 1 not greater than 1")])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)

    def test_each_version_of_an_identifier_gets_its_own_fail(self):
        """alpha-rule/1 fails beside alpha-rule/2 passing; beta-rule/2 fails before beta-rule/1
        fails; one method citing gamma-rule/1 and gamma-rule/2 fails."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_first_version_breaks(self):",
            "        # invariant: alpha-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_b_second_version_holds(self):",
            "        # invariant: alpha-rule/2",
            "        pass",
            "",
            "    def test_c_second_version_breaks(self):",
            "        # invariant: beta-rule/2",
            "        self.fail('the rule is broken')",
            "",
            "    def test_d_first_version_breaks(self):",
            "        # invariant: beta-rule/1",
            "        self.fail('the rule is broken')",
            "",
            "    def test_e_both_versions_break(self):",
            "        # invariant: gamma-rule/1",
            "        # invariant: gamma-rule/2",
            "        self.fail('the rule is broken')",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: beta-rule/2",
            "        # invariant: gamma-rule/1",
            "        # invariant: gamma-rule/2",
            "        pass"))
        self.assertEqual(code, 1)
        broken = "failed: AssertionError: the rule is broken"
        invariants = ("alpha-rule/1", "beta-rule/1", "beta-rule/2", "gamma-rule/1",
                      "gamma-rule/2")
        self.assertEqual(without_passes(lines, *invariants), [
            line(SAMPLE + "::Checks.test_a_first_version_breaks", "fail", "alpha-rule/1",
                 broken),
            line(SAMPLE + "::Checks.test_b_second_version_holds", "pass", "alpha-rule/2"),
            line(SAMPLE + "::Checks.test_c_second_version_breaks", "fail", "beta-rule/2",
                 broken),
            line(SAMPLE + "::Checks.test_d_first_version_breaks", "fail", "beta-rule/1",
                 broken),
            line(SAMPLE + "::Checks.test_e_both_versions_break", "fail", "gamma-rule/1",
                 broken),
            line(SAMPLE + "::Checks.test_e_both_versions_break", "fail", "gamma-rule/2",
                 broken)])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)

    def test_a_failing_subtest_gives_fail_wherever_it_stands_among_them(self):
        """Of three subtests, the first, the middle or the last fails, and the others pass."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Checks(unittest.TestCase):",
            "    def test_a_first(self):",
            "        # invariant: alpha-rule/1",
            "        for number in (1, 2, 3):",
            "            with self.subTest(number=number):",
            "                if number == 1:",
            "                    self.fail('the rule is broken')",
            "",
            "    def test_b_middle(self):",
            "        # invariant: beta-rule/1",
            "        for number in (1, 2, 3):",
            "            with self.subTest(number=number):",
            "                if number == 2:",
            "                    self.fail('the rule is broken')",
            "",
            "    def test_c_last(self):",
            "        # invariant: gamma-rule/1",
            "        for number in (1, 2, 3):",
            "            with self.subTest(number=number):",
            "                if number == 3:",
            "                    self.fail('the rule is broken')",
            "",
            "    def test_z_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        invariants = ("alpha-rule/1", "beta-rule/1", "gamma-rule/1")
        self.assertEqual(without_passes(lines, *invariants), [
            line(SAMPLE + "::Checks.test_a_first", "fail", "alpha-rule/1",
                 "failed in (number=1): AssertionError: the rule is broken"),
            line(SAMPLE + "::Checks.test_b_middle", "fail", "beta-rule/1",
                 "failed in (number=2): AssertionError: the rule is broken"),
            line(SAMPLE + "::Checks.test_c_last", "fail", "gamma-rule/1",
                 "failed in (number=3): AssertionError: the rule is broken")])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)

    def test_set_up_tear_down_and_cleanups_raising_leave_no_pass(self):
        """A cleanup raises after a clean body; setUp skips; tearDown skips after a clean body;
        an assertion fails in setUp. Holds passes every invariant they cite."""
        # invariant: test-runner-pass-line/1
        code, lines, _ = self.run_tests(test_sample=module(
            "class Cleaned(unittest.TestCase):",
            "    def fails_later(self):",
            "        raise ValueError('disk full')",
            "",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        self.addCleanup(self.fails_later)",
            "",
            "",
            "class FailInSetUp(unittest.TestCase):",
            "    def setUp(self):",
            "        self.fail('not ready')",
            "",
            "    def test_holds(self):",
            "        # invariant: delta-rule/1",
            "        pass",
            "",
            "",
            "class Holds(unittest.TestCase):",
            "    def test_holds(self):",
            "        # invariant: alpha-rule/1",
            "        # invariant: beta-rule/1",
            "        # invariant: gamma-rule/1",
            "        # invariant: delta-rule/1",
            "        pass",
            "",
            "",
            "class SkipInSetUp(unittest.TestCase):",
            "    def setUp(self):",
            "        raise unittest.SkipTest('no disk here')",
            "",
            "    def test_holds(self):",
            "        # invariant: beta-rule/1",
            "        pass",
            "",
            "",
            "class SkipInTearDown(unittest.TestCase):",
            "    def tearDown(self):",
            "        raise unittest.SkipTest('no disk here')",
            "",
            "    def test_holds(self):",
            "        # invariant: gamma-rule/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "alpha-rule/1", "delta-rule/1"), [
            line(SAMPLE + "::Cleaned.test_holds", "fail", "alpha-rule/1",
                 "error: ValueError: disk full"),
            line(SAMPLE + "::FailInSetUp.test_holds", "fail", "delta-rule/1",
                 "failed: AssertionError: not ready"),
            line(SAMPLE + "::SkipInSetUp.test_holds", "fail", None,
                 "no verdict for beta-rule/1: skipped: no disk here"),
            line(SAMPLE + "::SkipInTearDown.test_holds", "fail", None,
                 "no verdict for gamma-rule/1: skipped: no disk here")])
        for invariant in ("alpha-rule/1", "beta-rule/1", "gamma-rule/1", "delta-rule/1"):
            self.assertPassWithheld(lines, invariant)

    def test_test_files_changed_during_the_run_are_judged_as_the_run_started(self):
        """test_a_changes runs first: it deletes test_b_deleted.py, takes the citation out of
        test_c_uncited.py, and rewrites test_d_rewritten.py into a test that passes."""
        # invariant: test-runner-pass-line/1
        failing = [
            "class Later(unittest.TestCase):",
            "    def test_breaks(self):",
            "        # invariant: %s",
            "        self.fail('the rule is broken')"]
        code, lines, _ = self.run_tests(
            test_a_changes=module(
                "PASSING = ('import unittest\\n\\n\\nclass Later(unittest.TestCase):\\n'",
                "           '    def test_breaks(self):\\n'",
                "           '        # invariant: gamma-rule/1\\n'",
                "           '        pass\\n')",
                "",
                "",
                "class Changes(unittest.TestCase):",
                "    def test_changes(self):",
                "        os.remove(os.path.join('tests', 'test_b_deleted.py'))",
                "        path = os.path.join('tests', 'test_c_uncited.py')",
                "        with open(path, encoding='utf-8') as handle:",
                "            text = handle.read()",
                "        with open(path, 'w', encoding='utf-8') as handle:",
                "            handle.write(text.replace('# invariant: beta-rule/1', ''))",
                "        path = os.path.join('tests', 'test_d_rewritten.py')",
                "        with open(path, 'w', encoding='utf-8') as handle:",
                "            handle.write(PASSING)"),
            test_b_deleted=module(*failing) % "alpha-rule/1",
            test_c_uncited=module(*failing) % "beta-rule/1",
            test_d_rewritten=module(*failing) % "gamma-rule/1",
            test_z_holds=module(
                "class Holds(unittest.TestCase):",
                "    def test_holds(self):",
                "        # invariant: alpha-rule/1",
                "        # invariant: beta-rule/1",
                "        # invariant: gamma-rule/1",
                "        pass"))
        self.assertEqual(code, 1)
        broken = "failed: AssertionError: the rule is broken"
        invariants = ("alpha-rule/1", "beta-rule/1", "gamma-rule/1")
        self.assertEqual(without_passes(lines, *invariants), [
            line("tests/test_b_deleted.py::Later.test_breaks", "fail", "alpha-rule/1", broken),
            line("tests/test_c_uncited.py::Later.test_breaks", "fail", "beta-rule/1", broken),
            line("tests/test_d_rewritten.py::Later.test_breaks", "fail", "gamma-rule/1",
                 broken)])
        for invariant in invariants:
            self.assertPassWithheld(lines, invariant)


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

    def run_beside(self, taken):
        """Runs the runner in a process where another tool already holds the sys.monitoring
        tool ids `taken`; returns its exit code, the tool ids in use once it has ended, and its
        record."""
        script = "\n".join([
            "import runpy, sys",
            "for tool in %r:" % (taken,),
            "    sys.monitoring.use_tool_id(tool, 'another tool')",
            "sys.argv = [%r, 'tests', '--record', %r]" % (RUNNER, RECORD),
            "code = 0",
            "try:",
            "    runpy.run_path(%r, run_name='__main__')" % RUNNER,
            "except SystemExit as done:",
            "    code = done.code",
            "print(code, [tool for tool in range(6) if sys.monitoring.get_tool(tool)])"])
        done = subprocess.run([sys.executable, "-B", "-c", script], cwd=self.root,
                              capture_output=True, text=True, encoding="utf-8")
        with open(os.path.join(self.root, RECORD), encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        return done.stdout.strip(), lines

    def test_a_debugger_or_coverage_keeps_its_tool_id_and_the_runner_frees_its_own(self):
        printed, lines = self.run_beside((0, 1))
        self.assertEqual(printed, "0 [0, 1]")
        self.assertEqual(lines, [line(SAMPLE + "::Checks.test_holds", "pass", "alpha-rule/1")])

    def test_no_free_tool_id_is_a_failure_of_the_run(self):
        """The watch cannot run, so the run stops before any test: no pass names an invariant,
        Never's coroutine, whose body never executes, included."""
        # invariant: test-runner-pass-line/1
        self.write("tests/test_never.py", module(
            "class Never(unittest.TestCase):",
            "    async def test_never(self):",
            "        # invariant: beta-rule/1",
            "        pass"))
        printed, lines = self.run_beside((0, 1, 2, 3, 4, 5))
        self.assertEqual(printed, "2 [0, 1, 2, 3, 4, 5]")
        self.assertEqual(lines, [line(PROGRAM, "fail", None,
                                      "no sys.monitoring tool id is free to watch the test "
                                      "bodies (3, 4, 2, 5 are taken)")])

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
        """The first run passes beta-rule; in the second, its one citing test fails."""
        # invariant: test-runner-pass-line/1
        self.run_tests()
        self.write("tests/test_second.py", self.SECOND.replace(
            "        pass", "        self.fail('the rule is broken')"))
        code, lines, _ = self.run_tests()
        self.assertEqual(code, 1)
        self.assertEqual(without_passes(lines, "beta-rule/1"), [
            line("tests/test_first.py::First.test_holds", "pass", "alpha-rule/2"),
            line("tests/test_second.py::Second.test_holds", "fail", "beta-rule/1",
                 "failed: AssertionError: the rule is broken")])
        self.assertPassWithheld(lines, "beta-rule/1")

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


def fact_line(check, verdict, fact, description=None):
    """A line of the record holding a fact's verdict, written out as the test expects it."""
    written = {"check": check, "verdict": verdict, "fact": fact}
    if description is not None:
        written["description"] = description
    return written


class Facts(RunnerTestCase):
    """A test citing an environment fact gives it a verdict under the key `fact` (WAY-74, WAY-81)."""

    def test_a_passing_test_records_pass_for_a_fact_it_cites(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Probes(unittest.TestCase):",
            "    def test_quota(self):",
            "        # fact: storage-quota/1",
            "        # invariant: saves-fit-quota/1",
            "        self.assertTrue(True)"))
        self.assertEqual(code, 0)
        self.assertEqual(lines, [fact_line(SAMPLE + "::Probes.test_quota", "pass", "storage-quota/1"),
                                 line(SAMPLE + "::Probes.test_quota", "pass", "saves-fit-quota/1")])

    def test_a_failing_test_records_fail_for_a_fact_it_cites(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Probes(unittest.TestCase):",
            "    def test_quota(self):",
            "        # fact: storage-quota/1",
            "        self.fail('the quota moved')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [fact_line(SAMPLE + "::Probes.test_quota", "fail", "storage-quota/1",
                                           "failed: AssertionError: the quota moved")])

    def test_a_fact_and_an_invariant_of_one_name_are_two_citations(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Probes(unittest.TestCase):",
            "    def test_a_rule(self):",
            "        # invariant: storage-quota/1",
            "        pass",
            "",
            "    def test_b_probe(self):",
            "        # fact: storage-quota/1",
            "        self.fail('the quota moved')"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Probes.test_a_rule", "pass", "storage-quota/1"),
                                 fact_line(SAMPLE + "::Probes.test_b_probe", "fail",
                                           "storage-quota/1",
                                           "failed: AssertionError: the quota moved")])

    def test_a_skipped_test_gives_a_fact_no_verdict(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Probes(unittest.TestCase):",
            "    @unittest.skip('offline')",
            "    def test_quota(self):",
            "        # fact: storage-quota/1",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Probes.test_quota", "fail", None,
                                      "no verdict for fact storage-quota/1: skipped: offline")])

    def test_a_fact_citation_off_the_form_records_null(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "class Probes(unittest.TestCase):",
            "    def test_quota(self):",
            "        # fact: storage-quota/01",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE + "::Probes.test_quota", "fail", None,
                                      "cites fact `storage-quota/01`, which is not "
                                      "`<identifier>/<version>`")])

    def test_a_fact_citation_outside_a_test_is_named(self):
        code, lines, _ = self.run_tests(test_sample=module(
            "# fact: storage-quota/1",
            "class Probes(unittest.TestCase):",
            "    def test_quota(self):",
            "        pass"))
        self.assertEqual(code, 1)
        self.assertEqual(lines, [line(SAMPLE, "fail", None,
                                      "%s:5: `fact: storage-quota/1` stands outside any test, and a "
                                      "check cites at the check (WAY-65)" % SAMPLE)])


if __name__ == "__main__":
    unittest.main()
