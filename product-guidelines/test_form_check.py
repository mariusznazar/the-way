"""Ordinary tests of the form check of guidelines, `product-guidelines/form_check.py`.

They cover what no invariant's sentence holds: what a run records and prints, which paths it does
not read, how it treats a product's files as untrusted input (WAY-48), how the foundation after a
merge is read, and when it cannot run. The checks of the invariants of guidelines stand in
`test_form_check_invariants.py`, written by another agent (WAY-03, WAY-69).

Each test builds a product in a temporary git repository and runs the command on it, as a
subprocess or, where a test watches what the script calls, in this process. Expected values are
written out as literals; each fingerprint below was computed once, by hand, with
`relation-model/fingerprint.py` from the sentence beside it.

Run from the root of the-way:
    python -B gate/run_tests.py product-guidelines
"""

import contextlib
import importlib.util
import io
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

sys.dont_write_bytecode = True
THE_WAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(THE_WAY, "product-guidelines", "form_check.py")
FORM = "guidelines-form/1"
REFERENCES = "guidelines-reference-current/1"
# The reason a check needing a commit given as `none` records, word for word as the invariants
# template lists it.
NO_COMMIT_REASON = "the method takes a commit the gate filled in as not existing"
LIMIT = 1048576

FIXTURES_DECISION = "Each test of the product sets up its data through the product's fixtures."
FIXTURES_FP = "016b5b2a"

LOG = "\n".join([
    "# Decision log", "", "Intro.", "",
    "### ABC-05/1 — How does a test set up its data?", "",
    FIXTURES_DECISION, "",
    "- **Change:** new decision", "- **Scope:** web", "- **Based on:** none",
    "- **Relations:** none",
    "- **Verification:** level 2 — an agent compares the change with the decision:",
    "  - complies: a test sets up its data through the fixtures;",
    "  - violates: a test writes rows straight into the store of data.",
    "- **Review when:** none", "- **Origin:** none",
    "- **Approved by:** Anna, 2026-09-01", "",
    "*Rationale:* one way of setting up data.",
    "*Rejected:* none considered", ""])

INVARIANTS = ("# Invariants\n\n"
              "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n\n"
              "## Quarantined invariants\n\n| Identifier | Version | Until |\n|---|---|---|\n")

# An invariant `fixture-named` in three wordings, for the reading of the foundation after a merge.
NAMED = "Every test of the product names the fixture it sets up its data through."
NAMED_FP = "f60b0650"
NAMED_ON_BRANCH = "Every test of the product names each fixture it sets up its data through."
NAMED_ON_BRANCH_FP = "dbcd43ec"
NAMED_ON_ONTO = "Every test of the product names the one fixture it sets up its data through."
NAMED_ON_ONTO_FP = "85090d30"


def invariants_with(sentence=None, version=1, withdrawn=False):
    """An invariants file holding `fixture-named` at the version and with the sentence given, or
    listing it as withdrawn, or holding neither."""
    entry = ""
    if sentence is not None:
        entry = ("## fixture-named/%d\n\n%s\n\n- **Method:** `python -B tests/check_named.py`\n"
                 "- **Rests on:** none\n- **Derives from:** ABC-05@%s\n- **Part:** web\n"
                 "- **Correction:** none\n\n" % (version, sentence, FIXTURES_FP))
    row = "| fixture-named | merged with another entry | none |\n" if withdrawn else ""
    return ("# Invariants\n\n" + entry
            + "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n"
            + row + "\n## Quarantined invariants\n\n| Identifier | Version | Until |\n"
            "|---|---|---|\n")

PART_MAP = """# Part map

## web

The part answers for the screens of the product.

- **Files:** src/
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none
"""

FOUNDATION = {
    "foundations/decisions.md": LOG,
    "foundations/invariants.md": INVARIANTS,
    "foundations/part_map.md": PART_MAP,
    "tests/fixtures.py": "PLAYER = {}\n",
}

# Guidelines of a discipline the-way gives no template of; the comments give line numbers.
TESTING = """# Testing guidelines — the tests of the web interface

- **Discipline:** testing
- **Applies to:** web

## When to read

Before writing a test of the web interface.

## Rules

### Test data through fixtures

- **Decision:** ABC-05@016b5b2a
- **Invariant:** none
- **Good:** a test sets up its player through the fixtures.
- **Bad:** a test writes rows straight into the store of data.

Set up each test's data through the product's fixtures.

## Examples

### Branch names

The team names its branches after their tasks.

## Where in code

- `tests/fixtures.py`
"""
WHEN_LINE = 8        # "Before writing a test of the web interface."
DECISION_LINE = 14   # "- **Decision:** ABC-05@016b5b2a"
INVARIANT_LINE = 15  # "- **Invariant:** none"
PROSE_LINE = 19      # "Set up each test's data through the product's fixtures."
WHERE_LINE = 29      # "- `tests/fixtures.py`"

def as_coding(text):
    """`text` as guidelines of a second discipline the-way gives no template of, in a file
    `guidelines/coding.md`."""
    return text.replace("- **Discipline:** testing", "- **Discipline:** coding")


NO_GOOD = TESTING.replace("- **Good:** a test sets up its player through the fixtures.\n", "")
ELSEWHERE = TESTING.replace("- **Applies to:** web", "- **Applies to:** mobile")


def with_line(text, number, new):
    lines = text.split("\n")
    lines[number - 1] = new
    return "\n".join(lines)


def load_form_check():
    """The form check loaded by its path, to run it in this process."""
    spec = importlib.util.spec_from_file_location("product_guidelines_form_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Case(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        self.base = os.path.realpath(directory.name)
        self.root = os.path.join(self.base, "product")
        os.makedirs(self.root)
        self.record = os.path.join(self.base, "guidelines.jsonl")

    def write(self, files):
        for path, content in files.items():
            full = os.path.join(self.root, *path.split("/"))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            data = content if isinstance(content, bytes) else content.encode("utf-8")
            with open(full, "wb") as handle:
                handle.write(data)

    def git(self, *arguments):
        subprocess.run(["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com",
                        "-c", "core.autocrlf=false"] + list(arguments),
                       cwd=self.root, check=True, capture_output=True)

    def product(self, guidelines, untracked=None):
        """A product whose base commit holds FOUNDATION and whose next commit adds `guidelines`
        ({path: text or bytes}); `untracked` files are written and never added."""
        self.git("init", "-q", "-b", "main")
        self.write(FOUNDATION)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "foundation")
        if guidelines:
            self.write(guidelines)
            self.git("add", "-A")
            self.git("commit", "-q", "-m", "guidelines")
        if untracked:
            self.write(untracked)
        return self.root

    def product_onto(self, guidelines, onto, branch=None, base=None):
        """A product whose base commit holds FOUNDATION, with the files `base` changed; a branch
        `onto` leaves it with the files `onto` changed, and the main branch then gains a commit
        holding `guidelines` and the files `branch` changes."""
        self.git("init", "-q", "-b", "main")
        self.write(dict(FOUNDATION, **(base or {})))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "foundation")
        self.git("checkout", "-q", "-b", "onto")
        self.write(onto)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "onto")
        self.git("checkout", "-q", "main")
        self.write(dict(branch or {}, **guidelines))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "guidelines")
        return self.root

    def records(self):
        if not os.path.isfile(self.record):
            return []
        with open(self.record, encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]

    def run_check(self, *options, cwd=None, timeout=120):
        """Exit code, output and record lines of the command run as a subprocess."""
        environment = dict(os.environ, PYTHONIOENCODING="utf-8")
        run = subprocess.run([sys.executable, "-B", SCRIPT] + list(options)
                             + ["--record", self.record], cwd=cwd or self.root,
                             capture_output=True, text=True, encoding="utf-8",
                             errors="replace", env=environment, timeout=timeout)
        return run.returncode, run.stdout + run.stderr, self.records()

    def run_inside(self, *options):
        """Exit code and output of the command's main run in this process, on self.root."""
        module = load_form_check()
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            code = module.main([self.root] + list(options) + ["--record", self.record])
        return code, output.getvalue()

    def errors(self, output, path):
        pattern = re.compile(r"^%s:(\d+): error: (.*)$" % re.escape(path), re.M)
        return [(int(line), message) for line, message in pattern.findall(output)]

    def count_lines(self, output):
        return re.findall(r"(?m)^\d+ error\(s\), \d+ warning\(s\), \d+ unchecked$", output)


class Runs(Case):
    def test_a_repository_with_no_guidelines_exits_0_with_a_note(self):
        """Breaks caught: an absent `guidelines/` taken as an error, or passed in silence."""
        self.product({})
        code, output, lines = self.run_check()
        self.assertEqual(code, 0, output)
        self.assertRegex(output, r"(?m)^note: .*guidelines/")
        self.assertNotIn(": error:", output)
        self.assertEqual({("pass", FORM)}, {(line["verdict"], line["invariant"]) for line in lines})

    def test_a_run_with_no_option_records_lines_of_guidelines_form_alone(self):
        """Break caught: a run with no option recording checks its options do not select."""
        self.product({"guidelines/testing.md": TESTING, "guidelines/coding.md": as_coding(NO_GOOD)})
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue(lines, output)
        self.assertEqual({FORM}, {line["invariant"] for line in lines}, lines)
        self.assertIn("fail", [line["verdict"] for line in lines])

    def test_findings_of_two_files_print_under_their_own_paths(self):
        """Break caught: one report for every file, so a finding names the wrong file."""
        self.product({"guidelines/testing.md": NO_GOOD,
                      "guidelines/coding.md": as_coding(ELSEWHERE)})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        first = self.errors(output, "guidelines/testing.md")
        second = self.errors(output, "guidelines/coding.md")
        self.assertTrue(any("Good" in message for _, message in first), output)
        self.assertFalse(any("mobile" in message for _, message in first), output)
        self.assertIn(4, [line for line, message in second if "mobile" in message], output)
        self.assertFalse(any("Good" in message for _, message in second), output)

    def test_each_report_ends_with_its_count_line(self):
        """Break caught: a report whose count line is missing or counts another report's
        findings. The run's report comes first, then each file's, by path."""
        self.product({"guidelines/testing.md": TESTING,
                      "guidelines/coding.md": as_coding(NO_GOOD).replace(
                          "- **Applies to:** web", "- **Applies to:** mobile"),
                      "guidelines/x.MD": TESTING})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertEqual(["0 error(s), 1 warning(s), 0 unchecked",
                          "2 error(s), 0 warning(s), 0 unchecked",
                          "0 error(s), 0 warning(s), 0 unchecked"], self.count_lines(output),
                         output)

    def test_a_file_with_crlf_line_endings_is_read_as_its_lines(self):
        """Break caught: a carriage return left at the end of each line, so no heading or field
        of a file written on Windows is found."""
        self.product({"guidelines/testing.md": TESTING.replace("\n", "\r\n")})
        code, output, lines = self.run_check()
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)
        self.assertIn("pass", [line["verdict"] for line in lines])


class Names(Case):
    def test_a_name_of_a_discipline_with_a_template_under_another_discipline_is_an_error(self):
        """Break caught: `guidelines/styleguide-web.md` whose *Discipline* reads
        `styleguide-web` accepted as a discipline of its own and held to the common form, so
        none of the styleguide's template is checked (spec §5.3, 5a)."""
        self.product({"guidelines/styleguide-web.md": TESTING.replace(
            "- **Discipline:** testing", "- **Discipline:** styleguide-web")})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue([message for _, message in
                         self.errors(output, "guidelines/styleguide-web.md")
                         if "styleguide-web" in message and "Discipline" in message], output)


    def test_a_part_in_the_name_of_guidelines_other_than_a_styleguide_is_an_error(self):
        """Break caught: guidelines of a discipline other than the styleguide accepted under a
        part's name, `guidelines/<discipline>-<part>.md`, which WAY-167 gives the styleguide
        alone — even where the part is one the map holds."""
        self.product({"guidelines/testing-web.md": TESTING})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue([message for _, message in self.errors(output, "guidelines/testing-web.md")
                         if "`guidelines/testing.md`" in message and "Discipline" in message],
                        output)


class Paths(Case):
    def test_a_path_refused_for_its_form_whose_remainder_git_tracks_is_an_error(self):
        """Break caught: the guard against an absolute path, or a `..` segment, dropped, so
        `/tests/fixtures.py` or `./../tests/fixtures.py` passes once its slash, `.` and `..` are
        set aside, as `tests/fixtures.py` is a tracked file."""
        for path, why in (("/tests/fixtures.py", "absolute"),
                          ("./../tests/fixtures.py", "`..` segment")):
            with self.subTest(path=path):
                self.setUp()
                self.product({"guidelines/testing.md": with_line(TESTING, WHERE_LINE,
                                                                 "- `%s`" % path)})
                code, output, _ = self.run_check()
                self.assertEqual(code, 1, output)
                self.assertEqual([WHERE_LINE], [line for line, message in
                                                self.errors(output, "guidelines/testing.md")
                                                if path in message and why in message], output)


class References(Case):
    """What a run records and prints of the checks of references, and how it reads what a
    reference names, beyond what the invariants of guidelines assert (spec §§3.2, 5.1, 5.2)."""

    def assert_clean(self, code, output):
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)

    def test_a_run_with_merge_onto_records_lines_of_guidelines_reference_current_alone(self):
        """Breaks caught: a run given `--merge-onto` recording the checks of form, or no check of
        references; `none` given and the check after the merge recorded as anything but
        `unchecked` with the shared reason, or the check on the commit itself left out."""
        self.product({"guidelines/testing.md": TESTING, "guidelines/coding.md": as_coding(NO_GOOD)})
        code, output, lines = self.run_check("--merge-onto", "none")
        self.assertEqual(code, 1, output)   # the form error of NO_GOOD prints, unrecorded
        self.assertTrue(lines, output)
        self.assertEqual({REFERENCES}, {line["invariant"] for line in lines}, lines)
        self.assertEqual({"pass", "unchecked"}, {line["verdict"] for line in lines}, lines)
        unchecked = [line for line in lines if line["verdict"] == "unchecked"]
        self.assertEqual(1, len(unchecked), lines)
        self.assertEqual(NO_COMMIT_REASON, unchecked[0]["reason"])
        self.assertTrue(unchecked[0]["description"].startswith("--merge-onto none"), unchecked)
        self.assertRegex(output, r"(?m)^unchecked: ")

    def test_a_repository_with_no_guidelines_records_the_checks_of_references(self):
        """Break caught: no file of guidelines taken as nothing to record, so the method of
        guidelines-reference-current gives no verdict in the-way itself."""
        self.product({})
        code, output, lines = self.run_check("--merge-onto", "none")
        self.assertEqual(code, 0, output)
        self.assertEqual({("pass", REFERENCES), ("unchecked", REFERENCES)},
                         {(line["verdict"], line["invariant"]) for line in lines}, lines)

    def test_a_run_with_no_option_prints_a_reference_error_and_records_no_reference_check(self):
        """Breaks caught: a no-option run that skips the checks of references, passes on a
        reference error, or records them (spec §5.1: every check runs and prints in every run;
        ruling C28 (5))."""
        self.product({"guidelines/testing.md": with_line(
            TESTING, PROSE_LINE, "Set up each test's data as ABC-09@0123abcd has it.")})
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertIn(PROSE_LINE, [line for line, message in
                                   self.errors(output, "guidelines/testing.md")
                                   if "ABC-09@0123abcd" in message], output)
        self.assertEqual({FORM}, {line["invariant"] for line in lines}, lines)
        self.assertNotIn("fail", [line["verdict"] for line in lines], lines)

    def test_a_run_with_no_option_says_in_a_note_that_the_merge_is_not_checked(self):
        """Break caught: the check after the merge left out in silence."""
        self.product({"guidelines/testing.md": TESTING})
        code, output, _ = self.run_check()
        self.assertEqual(code, 0, output)
        self.assertRegex(output, r"(?m)^note: .*--merge-onto")

    def test_a_package_name_a_bare_identifier_or_another_log_s_number_is_no_reference(self):
        """Breaks caught: a versioned package name, an address, a bare identifier, or a decision
        number with another log's prefix taken for a reference (spec §3.2). The control at the
        same line shows the check of references reads it."""
        line = "Set up each test's data through the product's fixtures, as %s has it."
        for mention in ("`react@18`", "tailwindcss@4", "lucide-react@0", "left-pad@1.3.0",
                        "anna@example.com", "ABC-05", "ABC-05/1", "fixture-named",
                        "WAY-169@e2fb088c", "`WAY-169@e2fb088c`"):
            with self.subTest(mention=mention):
                self.setUp()
                self.product({"guidelines/testing.md": with_line(TESTING, PROSE_LINE,
                                                                 line % mention)})
                self.assert_clean(*self.run_check("--merge-onto", "none")[:2])
        self.setUp()
        self.product({"guidelines/testing.md": with_line(TESTING, PROSE_LINE,
                                                         line % "ABC-09@0123abcd")})
        code, output, _ = self.run_check("--merge-onto", "none")
        self.assertEqual(code, 1, output)
        self.assertIn(PROSE_LINE, [at for at, _ in self.errors(output, "guidelines/testing.md")])

    def test_a_reference_in_fenced_code_of_any_fence_is_ignored(self):
        """Breaks caught: a longer fence, a fence indented by up to three spaces, or a fence of
        one character holding the other read as prose, so a sample in it is reported. The
        control shows the same tokens outside the fence reported."""
        tokens = "ABC-09@0123abcd · ABC-05@016b5b2b · fixture-named@0123abcd · left-pad@0123abcd"
        for fence, inside, closing in (("~~~~", ["```", tokens, "```"], "~~~~~"),
                                       ("   ```text", [tokens, "~~~"], "```"),
                                       ("~~~", [tokens], "~~~")):
            with self.subTest(fence=fence):
                self.setUp()
                block = "\n".join(["Set up each test's data through the product's fixtures.",
                                   "", fence] + inside + [closing])
                self.product({"guidelines/testing.md": with_line(TESTING, PROSE_LINE, block)})
                self.assert_clean(*self.run_check("--merge-onto", "none")[:2])
        self.setUp()
        self.product({"guidelines/testing.md": with_line(TESTING, PROSE_LINE, tokens)})
        code, output, _ = self.run_check("--merge-onto", "none")
        self.assertEqual(code, 1, output)
        self.assertEqual(4, len(self.errors(output, "guidelines/testing.md")), output)

    def test_a_decision_number_of_another_log_names_no_decision_of_the_log(self):
        """Breaks caught: a rule's *Decision*, or a dropped section, taken to name a decision of
        the log by the shape of a number alone, though its prefix is another log's."""
        cases = (
            ("a rule's Decision", DECISION_LINE, "- **Decision:** WAY-169@e2fb088c"),
            ("a dropped section", WHEN_LINE, "none — WAY-169@e2fb088c"),
        )
        for name, number, line in cases:
            with self.subTest(name):
                self.setUp()
                self.product({"guidelines/testing.md": with_line(TESTING, number, line)})
                code, output, lines = self.run_check()
                self.assertEqual(code, 1, output)
                self.assertIn(number, [at for at, _ in
                                       self.errors(output, "guidelines/testing.md")], output)
                self.assertIn("fail", [entry["verdict"] for entry in lines])

    def test_log_copies_that_differ_on_the_commit_merged_onto_give_no_finding_of_the_log(self):
        """Break caught: the decisions guard's report of the merged log carried over, so the
        form check fails on a rule of the log (`log-merge-copies`) and not of guidelines
        (spec §5.1, finding 15)."""
        rationale = "*Rationale:* one way of setting up data."
        self.product_onto({"guidelines/testing.md": TESTING},
                          {"foundations/decisions.md": LOG.replace(
                              rationale, rationale[:-1] + ", kept on the main branch.")},
                          {"foundations/decisions.md": LOG.replace(
                              rationale, rationale[:-1] + ", kept on the branch.")})
        code, output, lines = self.run_check("--merge-onto", "onto")
        self.assert_clean(code, output)
        self.assertNotIn("log-merge-copies", output + json.dumps(lines))
        self.assertNotIn("differs from its copy", output)
        self.assertEqual({"pass"}, {line["verdict"] for line in lines}, lines)

    def test_an_invariant_after_a_merge_is_the_branch_s_where_its_sentence_changed_there(self):
        """Breaks caught: an invariant after the merge read from one side only — the branch's
        own rewording lost to the commit merged onto, or a withdrawal or removal there taken for
        no change (spec §5.2)."""
        cited = "- **Invariant:** fixture-named@%s"
        cases = (
            ("withdrawn on the commit merged onto", NAMED_FP,
             {"foundations/invariants.md": invariants_with(withdrawn=True)}, None,
             ("not in force after a merge onto onto", "withdrawn")),
            ("removed on the commit merged onto", NAMED_FP,
             {"foundations/invariants.md": invariants_with()}, None,
             ("not in force after a merge onto onto", "does not hold")),
            ("reworded on both sides", NAMED_ON_BRANCH_FP,
             {"foundations/invariants.md": invariants_with(NAMED_ON_ONTO, 2)},
             {"foundations/invariants.md": invariants_with(NAMED_ON_BRANCH, 2)}, None),
            ("reworded on the commit merged onto alone", NAMED_FP,
             {"foundations/invariants.md": invariants_with(NAMED_ON_ONTO, 2)}, None,
             ("after a merge onto onto, the current fingerprint", NAMED_ON_ONTO_FP)),
        )
        for name, carried, onto, branch, expected in cases:
            with self.subTest(name):
                self.setUp()
                self.product_onto({"guidelines/testing.md": with_line(
                    TESTING, INVARIANT_LINE, cited % carried)}, onto, branch,
                    base={"foundations/invariants.md": invariants_with(NAMED)})
                code, output, lines = self.run_check("--merge-onto", "onto")
                errors = self.errors(output, "guidelines/testing.md")
                if expected is None:
                    self.assert_clean(code, output)
                    continue
                self.assertEqual(code, 1, output)
                self.assertTrue([message for at, message in errors if at == INVARIANT_LINE
                                 and "fixture-named" in message
                                 and all(fragment in message for fragment in expected)], output)
                self.assertIn("fail", [line["verdict"] for line in lines
                                       if line["invariant"] == REFERENCES])

    def test_a_decision_the_commit_merged_onto_repeals_is_not_in_force_after_the_merge(self):
        """Break caught: the log after the merge read for fingerprints alone, so a decision the
        main branch repealed, which a branch's guidelines still name, passes the merge."""
        repeal = "\n".join([
            "### ABC-05/2 — How does a test set up its data?", "",
            "- **Change:** repeal", "- **Scope:** web", "- **Based on:** none",
            "- **Relations:** none",
            "- **Verification:** level 2 — an agent compares the change with the decision:",
            "  - complies: a test sets up its data as it needs;",
            "  - violates: a test is held to the fixtures.",
            "- **Review when:** none", "- **Origin:** none",
            "- **Approved by:** Anna, 2026-09-02", "",
            "*Rationale for change:* the question no longer needs an answer.",
            "*Rejected:* none considered", ""])
        self.product_onto({"guidelines/testing.md": TESTING},
                          {"foundations/decisions.md": LOG + "\n" + repeal})
        code, output, lines = self.run_check("--merge-onto", "onto")
        self.assertEqual(code, 1, output)
        self.assertTrue([message for at, message in self.errors(output, "guidelines/testing.md")
                         if at == DECISION_LINE and "ABC-05@016b5b2a" in message
                         and "not in force after a merge onto onto" in message
                         and "ABC-05/2" in message], output)
        self.assertIn("fail", [line["verdict"] for line in lines
                               if line["invariant"] == REFERENCES])

    def test_a_commit_to_merge_onto_that_does_not_exist_is_an_error(self):
        """Break caught: a mistyped commit taken as no commit to merge onto, so the check after
        the merge passes unrun."""
        self.product({"guidelines/testing.md": TESTING})
        code, output, lines = self.run_check("--merge-onto", "nowhere")
        self.assertEqual(code, 1, output)
        self.assertRegex(output, r"(?m)^guidelines:\d+: error: .*nowhere")
        self.assertIn("fail", [line["verdict"] for line in lines])


class NotRead(Case):
    def test_a_path_that_is_not_guidelines_name_md_gets_a_warning(self):
        """Breaks caught: a file one level deeper, or with an upper-case extension, read as
        guidelines, or left out with no word."""
        self.product({"guidelines/styleguide/web.md": TESTING, "guidelines/x.MD": TESTING})
        code, output, _ = self.run_check()
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)
        warnings = re.findall(r"(?m)^.*: warning: .*$", output)
        for path in ("guidelines/styleguide/web.md", "guidelines/x.MD"):
            self.assertTrue([line for line in warnings if path in line], output)


class TrustBoundary(Case):
    """A product's files are untrusted input (WAY-48, spec §5.4)."""

    def outside(self, name, text):
        path = os.path.join(self.base, name)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        return path

    def test_a_guidelines_file_that_is_a_symbolic_link_is_an_error_and_not_followed(self):
        """Break caught: a link read through, so a file outside the repository is read."""
        target = self.outside("outside.md", ELSEWHERE)
        self.product({"guidelines/testing.md": TESTING})
        link = os.path.join(self.root, "guidelines", "link.md")
        try:
            os.symlink(target, link)
        except (OSError, NotImplementedError) as problem:
            self.skipTest("the platform cannot create a symbolic link: %s" % problem)
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        errors = self.errors(output, "guidelines/link.md")
        self.assertEqual(1, len(errors), output)
        self.assertIn("link", errors[0][1])
        self.assertNotIn("mobile", output)
        self.assertIn("fail", [line["verdict"] for line in lines])

    def test_guidelines_that_is_a_symbolic_link_is_an_error_and_not_followed(self):
        """Break caught: the directory `guidelines` followed through a link."""
        directory = os.path.join(self.base, "elsewhere")
        os.makedirs(directory)
        with open(os.path.join(directory, "testing.md"), "w", encoding="utf-8") as handle:
            handle.write(ELSEWHERE)
        self.product({})
        try:
            os.symlink(directory, os.path.join(self.root, "guidelines"),
                       target_is_directory=True)
        except (OSError, NotImplementedError) as problem:
            self.skipTest("the platform cannot create a symbolic link: %s" % problem)
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertRegex(output, r"(?m)^guidelines:\d+: error: .*link")
        self.assertNotIn("mobile", output)

    def test_a_directory_named_like_a_guidelines_file_is_an_error(self):
        """Break caught: a directory `x.md` opened as a file, or passed in silence."""
        self.product({"guidelines/x.md": TESTING})
        os.remove(os.path.join(self.root, "guidelines", "x.md"))
        os.makedirs(os.path.join(self.root, "guidelines", "x.md"))
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        errors = self.errors(output, "guidelines/x.md")
        self.assertTrue([message for _, message in errors if "directory" in message], output)
        self.assertIn("fail", [line["verdict"] for line in lines])

    def test_an_untracked_directory_named_like_a_guidelines_file_is_an_error(self):
        """Break caught: a directory `y.md` that git lists only through the files below it,
        warned of as a deeper path and never reported as the directory it is."""
        self.product({"guidelines/testing.md": TESTING},
                     untracked={"guidelines/y.md/inner.md": TESTING})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        errors = self.errors(output, "guidelines/y.md")
        self.assertTrue([message for _, message in errors if "directory" in message], output)
        self.assertEqual([], self.errors(output, "guidelines/y.md/inner.md"), output)

    def test_guidelines_that_is_a_file_is_an_error(self):
        """Break caught: a file `guidelines` taken for a repository with no guidelines."""
        self.product({"guidelines": "not a directory\n"})
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertRegex(output, r"(?m)^guidelines:\d+: error: ")
        self.assertIn("fail", [line["verdict"] for line in lines])

    def test_text_that_is_not_utf_8_is_an_error(self):
        """Break caught: bytes decoded by a guess, or a decoding error stopping the run."""
        self.product({"guidelines/testing.md": TESTING.encode("utf-8") + b"\xff\xfe\x80\n"})
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        errors = self.errors(output, "guidelines/testing.md")
        self.assertEqual(1, len(errors), output)
        self.assertIn("UTF-8", errors[0][1])
        self.assertIn("fail", [line["verdict"] for line in lines])

    def test_a_file_over_one_mebibyte_is_refused_unread(self):
        """Break caught: a large file read whole. Were it read, its missing header lines and
        sections would be reported beside the refusal."""
        self.product({"guidelines/testing.md": b"x" * (LIMIT + 1)})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        errors = self.errors(output, "guidelines/testing.md")
        self.assertEqual(1, len(errors), output)
        self.assertIn(str(LIMIT), errors[0][1])

    def test_a_file_just_under_one_mebibyte_of_one_crafted_line_finishes_within_a_bound(self):
        """Break caught: matching that runs away on a long line of backticks, `@` and
        hexadecimal runs, so the run never ends with a report."""
        unit = "``@" + "0123abcd" * 3 + "@`"
        for name, number, prefix in (("prose", PROSE_LINE, ""), ("where", WHERE_LINE, "- ")):
            with self.subTest(name):
                self.setUp()
                head = with_line(TESTING, number, prefix + "\0").encode("utf-8")
                room = LIMIT - 16 - (len(head) - 1)
                line = (unit * (room // len(unit) + 1))[:room]
                data = head.replace(b"\0", line.encode("ascii"))
                self.assertLess(len(data), LIMIT)
                self.assertGreater(len(data), LIMIT - 64)
                self.product({"guidelines/testing.md": data})
                started = time.monotonic()
                code, output, _ = self.run_check(timeout=120)
                elapsed = time.monotonic() - started
                self.assertIn(code, (0, 1), output[-2000:])
                self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
                self.assertEqual(2, len(self.count_lines(output)), output[-2000:])

    def test_a_line_of_words_and_at_signs_just_under_one_mebibyte_finishes_within_a_bound(self):
        """Break caught: a pattern of references that tries every shorter name before each `@`
        from every place in a long word, so one line of a crafted file takes quadratic time.
        The line is one word of letters, digits and hyphens ending in `@` and a backtick, or
        many names each followed by `@` and no letter or digit."""
        for name, unit, tail in (("one word", "a0-" * 7, "@`"), ("many names", "ab-c9@`", "")):
            with self.subTest(name):
                self.setUp()
                head = with_line(TESTING, PROSE_LINE, "\0").encode("utf-8")
                room = LIMIT - 16 - (len(head) - 1) - len(tail)
                line = (unit * (room // len(unit) + 1))[:room] + tail
                data = head.replace(b"\0", line.encode("ascii"))
                self.assertLess(len(data), LIMIT)
                self.product({"guidelines/testing.md": data})
                started = time.monotonic()
                code, output, _ = self.run_check("--merge-onto", "none", timeout=120)
                elapsed = time.monotonic() - started
                self.assertIn(code, (0, 1), output[-2000:])
                self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
                self.assertEqual(2, len(self.count_lines(output)), output[-2000:])

    def test_a_value_taken_from_a_file_is_printed_escaped(self):
        """Break caught: a control character of a file written to the terminal as it stands,
        so a crafted file can rewrite what a person reads."""
        escape = chr(27) + "[2J"
        self.product({"guidelines/testing.md": TESTING.replace(
            "- **Applies to:** web", "- **Applies to:** web · " + escape + "mobile")})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertNotIn(chr(27), output)
        self.assertIn(4, [line for line, message in self.errors(output, "guidelines/testing.md")
                          if "\\x1b[2Jmobile" in message], output)

    def test_no_refused_path_reaches_git(self):
        """Break caught: a path of `## Where in code` handed to git before its shape is tested,
        so pathspec magic, a path outside the repository or a network share reaches git."""
        refused = ("../outside.md", "/etc/passwd", "C:\\x", "\\\\host\\share\\x", ":(glob)**",
                   "http://host/x")
        where = "".join("- `%s`\n" % path for path in refused)
        self.product({"guidelines/testing.md": TESTING.replace("- `tests/fixtures.py`\n",
                                                               "- `tests/fixtures.py`\n" + where)})
        calls = []
        original = subprocess.run

        def recording(arguments, *rest, **keywords):
            calls.append([str(argument) for argument in arguments])
            return original(arguments, *rest, **keywords)

        with mock.patch.object(subprocess, "run", side_effect=recording):
            code, output = self.run_inside()
        self.assertEqual(code, 1, output)
        self.assertEqual(list(range(WHERE_LINE + 1, WHERE_LINE + 1 + len(refused))),
                         sorted(line for line, _ in self.errors(output, "guidelines/testing.md")),
                         output)
        self.assertTrue([call for call in calls if "ls-files" in call], calls)
        for path in refused:
            for call in calls:
                self.assertFalse([argument for argument in call if path in argument],
                                 "%r reached git: %r" % (path, call))

    def test_the_script_opens_no_socket(self):
        """Break caught: the script's own code reaching a network host. This covers the
        script's code, not git's."""
        self.product({"guidelines/testing.md": TESTING})
        opened = []

        def refuse(*arguments, **keywords):
            opened.append(arguments)
            raise AssertionError("a socket was opened")

        with mock.patch.object(socket, "socket", side_effect=refuse), \
                mock.patch.object(socket, "create_connection", side_effect=refuse), \
                mock.patch.object(socket, "getaddrinfo", side_effect=refuse):
            code, output = self.run_inside()
            self.assertEqual([], opened)
            with self.assertRaises(AssertionError):
                socket.create_connection(("localhost", 9))
        self.assertEqual(code, 0, output)
        self.assertEqual(1, len(opened))


class CannotRun(Case):
    def test_a_record_path_not_ending_in_jsonl_exits_2(self):
        """Break caught: a record written under a name the gate does not read."""
        self.product({"guidelines/testing.md": NO_GOOD})
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)   # the control: the same run with a `.jsonl` record
        self.assertTrue(lines, output)
        self.record = os.path.join(self.base, "guidelines.txt")
        code, output, _ = self.run_check()
        self.assertEqual(code, 2, output)
        self.assertIn(".jsonl", output)
        self.assertFalse(os.path.exists(self.record))

    def test_a_root_that_is_not_the_top_of_a_repository_exits_2(self):
        """Break caught: a run from a subdirectory reading no guidelines and passing."""
        self.product({"guidelines/testing.md": NO_GOOD})
        code, output, _ = self.run_check(self.root, cwd=self.base)
        self.assertEqual(code, 1, output)   # the control: the top of the repository, given
        for root in (os.path.join(self.root, "tests"), self.base):
            with self.subTest(root=root):
                code, output, _ = self.run_check(root, cwd=self.base)
                self.assertEqual(code, 2, output)
                self.assertNotIn(": error: the rule", output)

    def test_a_checkout_of_the_way_with_no_template_exits_2(self):
        """Break caught: a run with no template to read passing every file."""
        self.product({"guidelines/testing.md": NO_GOOD})
        copy = os.path.join(self.base, "the-way", "product-guidelines")
        os.makedirs(copy)
        shutil.copy(SCRIPT, copy)
        environment = dict(os.environ, PYTHONIOENCODING="utf-8")
        run = subprocess.run([sys.executable, "-B", os.path.join(copy, "form_check.py"),
                              "--record", self.record], cwd=self.root, capture_output=True,
                             text=True, encoding="utf-8", errors="replace", env=environment)
        self.assertEqual(run.returncode, 2, run.stdout + run.stderr)
        self.assertIn("template", run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
