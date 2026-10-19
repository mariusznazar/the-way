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

def as_observability(text):
    """`text` as guidelines of a second discipline the-way gives no template of, in a file
    `guidelines/observability.md`."""
    return text.replace("- **Discipline:** testing", "- **Discipline:** observability")


# A good and a bad case of `fixture-named`, for a rule of TESTING that names it (WAY-168).
FIXTURE_CASES = ("```good fixture-named tests/test_player.py\n"
                 "def test_player(player_fixture):\n    assert player_fixture\n```\n\n"
                 "```bad fixture-named tests/test_player.py\n"
                 "def test_player():\n    assert {}\n```\n\n")
NO_GOOD = TESTING.replace("- **Good:** a test sets up its player through the fixtures.\n", "")
ELSEWHERE = TESTING.replace("- **Applies to:** web", "- **Applies to:** mobile")

# Coding guidelines in the two forms of the coding template: a general file and the file of the
# kind `endpoint`. The decision ABC-06 designates the exemplar by its path and its kind in
# backticks, and the invariant `endpoint-handler` checks the kind's rule; the commit adding the
# guidelines adds both to the foundation, with the files they name.
EXEMPLAR_DECISION = "The file `src/api/orders.ts` is the exemplar of the kind `endpoint`."
EXEMPLAR_FP = "a7f9c135"
HANDLER = "Every file of the kind endpoint answers through the shared handler."
HANDLER_FP = "8c2ca199"
CODING_LOG = LOG + "\n".join([
    "", "### ABC-06/1 — Which file is the exemplar of an endpoint?", "",
    EXEMPLAR_DECISION, "",
    "- **Change:** new decision", "- **Scope:** web", "- **Based on:** none",
    "- **Relations:** none",
    "- **Verification:** level 2 — an agent compares the change with the decision:",
    "  - complies: a new endpoint follows the exemplar;",
    "  - violates: a new endpoint answers on its own.",
    "- **Review when:** none", "- **Origin:** none",
    "- **Approved by:** Anna, 2026-09-01", "",
    "*Rationale:* one way of answering a request.",
    "*Rejected:* none considered", ""])
CODING_INVARIANTS = ("# Invariants\n\n## endpoint-handler/1\n\n%s\n\n"
                     "- **Method:** `python -B tests/check_handler.py`\n- **Rests on:** none\n"
                     "- **Derives from:** ABC-06@%s\n- **Part:** web\n- **Correction:** none\n\n"
                     "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n"
                     "|---|---|---|\n"
                     "\n## Quarantined invariants\n\n| Identifier | Version | Until |\n"
                     "|---|---|---|\n" % (HANDLER, EXEMPLAR_FP))
KINDS_HEADER = "| Kind | File | When to read |"
KINDS_ROW = "| endpoint | `guidelines/coding-endpoint.md` | before adding or changing an endpoint |"
CODING = "\n".join([
    "# Coding guidelines — the product", "",
    "- **Discipline:** coding", "- **Applies to:** web", "",
    "## When to read", "", "Before changing the product's code.", "",
    "## Kinds of code", "", KINDS_HEADER, "|---|---|---|", KINDS_ROW, "",
    "## Rules", "",
    "### Linter", "", "none — ABC-05@016b5b2a", "",
    "### Formatter", "", "none — ABC-05@016b5b2a", "",
    "### Dependency audit", "", "none — ABC-05@016b5b2a", "",
    "## Examples", "", "### Short functions", "",
    "The team keeps a function short enough to read at a glance.", "",
    "## Where in code", "", "- `src/api`", ""])
FILES_HEADER = "| File | Status | Decision |"
EXEMPLAR_ROW = "| `src/api/orders.ts` | exemplar | ABC-06@a7f9c135 |"
CODING_ENDPOINT = "\n".join([
    "# Coding guidelines — endpoint", "",
    "- **Discipline:** coding", "- **Applies to:** web", "",
    "## When to read", "", "Before adding or changing an endpoint.", "",
    "## Files of this kind", "", FILES_HEADER, "|---|---|---|", EXEMPLAR_ROW, "",
    "## Rules", "",
    "### Through the shared handler", "",
    "- **Decision:** ABC-06@a7f9c135",
    "- **Invariant:** endpoint-handler@8c2ca199",
    "- **Good:** an endpoint answers through the shared handler.",
    "- **Bad:** an endpoint answers on its own.", "",
    "Answer every request through the shared handler.", "",
    "```good endpoint-handler src/api/carts.ts",
    'import { handle } from "./handler";',
    "export const POST = handle((input: unknown) => input);",
    "```", "",
    "```bad endpoint-handler src/api/carts.ts",
    "export const POST = (input: unknown) => input;",
    "```", "",
    "## Examples", "", "### Names of inputs", "",
    "The exemplar names each input after what it holds.", "",
    "## Where in code", "", "- `src/api/orders.ts`", ""])
CODING_FILES = {
    "foundations/decisions.md": CODING_LOG,
    "foundations/invariants.md": CODING_INVARIANTS,
    "src/api/handler.ts": "export const handle = (answer: Function) => answer;\n",
    "src/api/orders.ts": ('import { handle } from "./handler";\n'
                          "export const POST = handle((input: unknown) => input);\n"),
    "guidelines/coding.md": CODING,
    "guidelines/coding-endpoint.md": CODING_ENDPOINT,
}


def line_of(text, line):
    """The number (from 1) of the one line of `text` reading `line`."""
    lines = text.split("\n")
    if lines.count(line) != 1:
        raise AssertionError("the fixture holds %r %d times, not once" % (line, lines.count(line)))
    return lines.index(line) + 1


def replaced(text, old, new):
    """`text` with the one occurrence of `old` replaced by `new`."""
    if text.count(old) != 1:
        raise AssertionError("the fixture holds %r %d times, not once" % (old, text.count(old)))
    return text.replace(old, new)


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
        self.product({"guidelines/testing.md": TESTING,
                      "guidelines/observability.md": as_observability(NO_GOOD)})
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue(lines, output)
        self.assertEqual({FORM}, {line["invariant"] for line in lines}, lines)
        self.assertIn("fail", [line["verdict"] for line in lines])

    def test_findings_of_two_files_print_under_their_own_paths(self):
        """Break caught: one report for every file, so a finding names the wrong file."""
        self.product({"guidelines/testing.md": NO_GOOD,
                      "guidelines/observability.md": as_observability(ELSEWHERE)})
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        first = self.errors(output, "guidelines/testing.md")
        second = self.errors(output, "guidelines/observability.md")
        self.assertTrue(any("Good" in message for _, message in first), output)
        self.assertFalse(any("mobile" in message for _, message in first), output)
        self.assertIn(4, [line for line, message in second if "mobile" in message], output)
        self.assertFalse(any("Good" in message for _, message in second), output)

    def test_each_report_ends_with_its_count_line(self):
        """Break caught: a report whose count line is missing or counts another report's
        findings. The run's report comes first, then each file's, by path."""
        self.product({"guidelines/testing.md": TESTING,
                      "guidelines/observability.md": as_observability(NO_GOOD).replace(
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
        none of the styleguide's template is checked (WAY-167, WAY-170)."""
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


class Coding(Case):
    """The two forms of the coding template: the general file `guidelines/coding.md` and a file
    `guidelines/coding-<kind>.md` for each kind of code (WAY-167), read with crafted names
    (WAY-48)."""

    def test_a_general_file_and_a_file_of_a_kind_pass(self):
        """Break caught: a file `guidelines/coding-<kind>.md` refused for its name, or held to the
        form of the general file, so the coding guidelines a product writes never pass."""
        self.product(CODING_FILES)
        for options in ((), ("--merge-onto", "none")):
            with self.subTest(options=options):
                code, output, lines = self.run_check(*options)
                self.assertEqual(code, 0, output)
                self.assertNotIn(": error:", output)
                self.assertNotIn("fail", [line["verdict"] for line in lines], lines)

    def test_a_name_whose_kind_is_no_identifier_is_an_error(self):
        """Breaks caught: a kind of no word, an upper-case one, one starting with a hyphen or
        holding a dot, or a name whose discipline differs in case, taken for a file of a kind;
        or the error not naming the two forms the discipline gives."""
        for name in ("coding-.md", "coding--a.md", "coding-A.md", "coding-a.md.md",
                     "Coding-a.md"):
            with self.subTest(name=name):
                self.setUp()
                self.product(dict(CODING_FILES, **{"guidelines/" + name: CODING_ENDPOINT}))
                code, output, _ = self.run_check()
                self.assertEqual(code, 1, output)
                self.assertTrue([message for _, message in self.errors(output, "guidelines/" + name)
                                 if "*Discipline* `coding`" in message
                                 and "`guidelines/coding-<kind>.md`" in message], output)

    def test_a_file_below_a_directory_named_like_a_kind_is_warned_of_and_not_read(self):
        """Break caught: `guidelines/coding-a/b.md` read as guidelines, or passed with no word."""
        self.product(dict(CODING_FILES, **{"guidelines/coding-a/b.md": CODING_ENDPOINT}))
        code, output, _ = self.run_check()
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)
        self.assertRegex(output, r"(?m)^guidelines:\d+: warning: `guidelines/coding-a/b\.md`")


class Tables(Case):
    """Every table a template gives is checked for its header and the number of its cells; a
    table of roles is checked beyond that by the rules of the styleguide (WAY-171)."""

    def broken(self, path, old, new):
        """Runs the check on the coding guidelines with the line `old` of the file `path` read as
        `new`; returns the exit code, the output and the number of the line."""
        text = CODING_FILES[path]
        number = line_of(text, old)
        self.product(dict(CODING_FILES, **{path: replaced(text, old, new)}))
        code, output, _ = self.run_check()
        return code, output, number

    def test_a_row_whose_number_of_cells_differs_from_the_columns_is_an_error(self):
        """Breaks caught: a row of a table other than the roles' left unchecked, or a `|` in
        backticks taken as no border of a cell — as Markdown splits a row on it — so a row
        holding four cells passes; or an empty last cell written `||` lost."""
        general, kind = "guidelines/coding.md", "guidelines/coding-endpoint.md"
        cases = (
            ("a | inside backticks", general, KINDS_ROW,
             "| endpoint | `guidelines/coding-endpoint.md|x` | before adding or changing an "
             "endpoint |", "4 cells"),
            ("too few cells", general, KINDS_ROW, "| endpoint | `guidelines/coding-endpoint.md` |",
             "2 cells"),
            ("too many cells", general, KINDS_ROW, KINDS_ROW + " now |", "4 cells"),
            ("an empty cell too many", general, KINDS_ROW, KINDS_ROW + "|", "4 cells"),
            ("too few cells in the files of a kind", kind, EXEMPLAR_ROW,
             "| `src/api/orders.ts` | exemplar |", "2 cells"),
        )
        for name, path, old, new, fragment in cases:
            with self.subTest(name):
                self.setUp()
                code, output, number = self.broken(path, old, new)
                self.assertEqual(code, 1, output)
                self.assertIn(number, [line for line, message in self.errors(output, path)
                                       if fragment in message and "3 columns" in message], output)

    def test_a_separator_row_among_the_rows_is_an_error(self):
        """Break caught: a row of dashes anywhere in a table skipped as its separator."""
        code, output, number = self.broken("guidelines/coding.md", KINDS_ROW,
                                           KINDS_ROW + "\n|---|---|---|")
        self.assertEqual(code, 1, output)
        self.assertIn(number + 1, [line for line, message
                                   in self.errors(output, "guidelines/coding.md")
                                   if "separator" in message], output)

    def test_a_header_that_differs_from_the_columns_is_an_error(self):
        """Breaks caught: a header compared with the columns loosely, so a column named with
        a space more or less passes; or the space around each cell, which Markdown sets aside,
        taken for part of its name (the control)."""
        for header in ("| Kind | File | When to  read |", "| Kind | File | Whento read |",
                       "| Kind | File |"):
            with self.subTest(header=header):
                self.setUp()
                code, output, number = self.broken("guidelines/coding.md", KINDS_HEADER, header)
                self.assertEqual(code, 1, output)
                self.assertIn(number, [line for line, message
                                       in self.errors(output, "guidelines/coding.md")
                                       if "Kind | File | When to read" in message], output)
        self.setUp()
        code, output, _ = self.broken("guidelines/coding.md", KINDS_HEADER,
                                      "|Kind|  File  |   When to read |")
        self.assertEqual(code, 0, output)

    def test_a_section_of_a_table_holding_none_is_an_error(self):
        """Break caught: `## Kinds of code` written as prose, so the table the template gives
        is missing with no word."""
        table = "\n".join([KINDS_HEADER, "|---|---|---|", KINDS_ROW])
        self.product(dict(CODING_FILES, **{"guidelines/coding.md": replaced(
            CODING, table, "Before an endpoint, read the file of endpoints.")}))
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue([message for _, message in self.errors(output, "guidelines/coding.md")
                         if "Kinds of code" in message and "no table" in message], output)

    def test_a_table_with_a_header_and_no_row_passes(self):
        """Break caught: a table of no row taken for no table: a product with no exemplar yet
        keeps the table of its kinds with its header alone (WAY-167)."""
        self.product({path: text for path, text in CODING_FILES.items()
                      if path != "guidelines/coding-endpoint.md"}
                     | {"guidelines/coding.md": replaced(CODING, KINDS_ROW + "\n", "")})
        code, output, _ = self.run_check()
        self.assertEqual(code, 0, output)

    def test_a_row_of_one_mebibyte_of_bars_finishes_within_a_bound(self):
        """Break caught: splitting a crafted row that runs away, so the run never ends with a
        report."""
        head = replaced(CODING, KINDS_ROW, "\0").encode("utf-8")
        room = LIMIT - 16 - (len(head) - 1)
        data = head.replace(b"\0", b"|" * room)
        self.assertLess(len(data), LIMIT)
        self.product(dict(CODING_FILES, **{"guidelines/coding.md": data}))
        started = time.monotonic()
        code, output, _ = self.run_check(timeout=120)
        elapsed = time.monotonic() - started
        self.assertEqual(code, 1, output[-2000:])
        self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
        self.assertTrue([message for _, message in self.errors(output, "guidelines/coding.md")
                         if "cells" in message], output[-2000:])


class TemplateWords(Case):
    """The structural words of the coding template that the checks act on are read back from it
    (WAY-171): a copy of the templates lacking one is refused."""

    def templates(self, coding):
        """A copy of the-way's templates whose coding template reads `coding`; returns the
        directory that stands for `product-guidelines`."""
        here = os.path.join(self.base, "the-way", "product-guidelines")
        source = os.path.join(THE_WAY, "product-guidelines")
        for relative in ("template.md", os.path.join("styleguide", "template.md")):
            os.makedirs(os.path.dirname(os.path.join(here, relative)), exist_ok=True)
            shutil.copy(os.path.join(source, relative), os.path.join(here, relative))
        os.makedirs(os.path.join(here, "coding"), exist_ok=True)
        with open(os.path.join(here, "coding", "template.md"), "w", encoding="utf-8",
                  newline="\n") as handle:
            handle.write(coding)
        return here

    def coding_template(self):
        with open(os.path.join(THE_WAY, "product-guidelines", "coding", "template.md"),
                  encoding="utf-8") as handle:
            return handle.read()

    def test_a_coding_template_lacking_a_word_the_checks_act_on_is_refused(self):
        """Breaks caught: a template read without the section, column or value of *Status* a
        check of the coding discipline acts on, so the check passes every file. The control:
        the template as it stands is read."""
        text = self.coding_template()
        statuses = "*Status*: one of `exemplar`, `copy` or `do not copy`;"
        cases = (
            ("Required form of a kind", "\n## Required form of a kind\n", "\n## Form of a kind\n"),
            ("Kinds of code", "\n## Kinds of code\n", "\n## Kinds\n"),
            ("Files of this kind", "\n## Files of this kind\n", "\n## Files\n"),
            ("Kind", "| Kind | File | When to read |", "| Sort | File | When to read |"),
            ("File", "| Kind | File | When to read |", "| Kind | Path | When to read |"),
            ("When to read", "| Kind | File | When to read |", "| Kind | File | When |"),
            ("File", "| File | Status | Decision |", "| Path | Status | Decision |"),
            ("Status", "| File | Status | Decision |", "| File | State | Decision |"),
            ("Decision", "| File | Status | Decision |", "| File | Status | Reason |"),
            ("exemplar", statuses, "*Status*: one of `model`, `copy` or `do not copy`;"),
            ("copy", statuses, "*Status*: one of `exemplar`, `follow` or `do not copy`;"),
            ("do not copy", statuses, "*Status*: one of `exemplar`, `copy` or `avoid`;"),
        )
        module = load_form_check()
        common, disciplines = module.read_templates(self.templates(text))
        self.assertIn("coding", disciplines)
        for word, old, new in cases:
            with self.subTest(word=word, old=old):
                self.setUp()
                here = self.templates(replaced(text, old, new))
                with self.assertRaises(module.TemplateError) as raised:
                    module.read_templates(here)
                self.assertIn(word, str(raised.exception))

    def test_the_command_exits_2_on_a_coding_template_lacking_a_word(self):
        """Break caught: a template the checks cannot act on read anyway, so the run passes."""
        self.product(CODING_FILES)
        here = self.templates(replaced(self.coding_template(), "\n## Files of this kind\n",
                                       "\n## Files\n"))
        shutil.copy(SCRIPT, here)
        environment = dict(os.environ, PYTHONIOENCODING="utf-8")
        run = subprocess.run([sys.executable, "-B", os.path.join(here, "form_check.py"),
                              "--record", self.record], cwd=self.root, capture_output=True,
                             text=True, encoding="utf-8", errors="replace", env=environment)
        self.assertEqual(run.returncode, 2, run.stdout + run.stderr)
        self.assertIn("Files of this kind", run.stdout + run.stderr)

    def test_each_form_of_a_discipline_reads_its_own_demand_of_an_invariant(self):
        """Break caught: the demand of an invariant in every rule read once for a discipline, so
        a template that states it for one of its forms alone holds the other to it too."""
        sentence = "its *Invariant* names at least one invariant"
        text = self.coding_template()
        section = text.index("\n## Required form of a kind\n")
        head, tail = text[:section], text[section:]
        self.assertIn(sentence, " ".join(head.split()))
        self.assertIn(sentence, " ".join(tail.split()))
        # The sentence may wrap over lines; only the section of the form of a kind loses it.
        loosened = head + re.sub(r"its \*Invariant\*\s+names\s+at\s+least\s+one\s+invariant",
                                 "its *Invariant* may name an invariant", tail)
        self.assertNotIn(sentence, " ".join(loosened[section:].split()))
        module = load_form_check()
        _, disciplines = module.read_templates(self.templates(loosened))
        self.assertTrue(disciplines["coding"].requires_invariant)
        self.assertFalse(disciplines["coding"].of_a_kind.requires_invariant)


# Decisions beside ABC-06 for the checks of the exemplar: one naming the path outside backticks,
# and one in force at its first version and repealed at its second, whose first version names the
# path and the kind in backticks, so that only the repeal is wrong.
BARE_PATH_DECISION = "The file src/api/orders.ts is the exemplar of the kind `endpoint`."
BARE_PATH_FP = "5047a97d"
REPEALED_DECISION = ("The file `src/api/orders.ts` was the exemplar of the kind `endpoint` until "
                     "the API was split.")
REPEALED_FP = "cc24fd66"


def decision_version(number, version, question, binding, change):
    """A version of a decision of the log, in the form the decisions template gives."""
    lines = ["", "### ABC-%02d/%d — %s" % (number, version, question), ""]
    if binding is not None:
        lines += [binding, ""]
    return "\n".join(lines + [
        "- **Change:** " + change, "- **Scope:** web", "- **Based on:** none",
        "- **Relations:** none",
        "- **Verification:** level 2 — an agent compares the change with the decision:",
        "  - complies: a new endpoint follows the exemplar;",
        "  - violates: a new endpoint answers on its own.",
        "- **Review when:** none", "- **Origin:** none",
        "- **Approved by:** Anna, 2026-09-01", "",
        "*Rationale:* one way of answering a request.", "*Rejected:* none considered", ""])


EXEMPLAR_LOG = (CODING_LOG
                + decision_version(7, 1, "Which file was the exemplar before the split?",
                                   REPEALED_DECISION, "new decision")
                + decision_version(7, 2, "Which file was the exemplar before the split?", None,
                                   "repeal")
                + decision_version(8, 1, "Which file is the exemplar, named bare?",
                                   BARE_PATH_DECISION, "new decision"))


def crafted(path):
    """(what, a crafted spelling of `path`) for each shape of path that is refused, or that names
    nothing git tracks, before git sees it (WAY-48)."""
    windows = path.replace("/", "\\")
    return (("absolute", "/" + path), ("a UNC prefix", "//host/share/" + path),
            ("a UNC prefix written for Windows", "\\\\host\\share\\" + windows),
            ("a `..` segment", "src/../" + path), ("a backslash", windows),
            ("a drive", "C:/" + path), ("a drive with no slash", "C:" + path),
            ("a character that is not printable", path + "\x07"),
            ("a zero-width space", path[:3] + "\u200b" + path[3:]),
            ("a pathspec magic word", ":(literal)" + path), ("a short pathspec magic", ":!" + path),
            ("200 KiB", "a" * 204800 + "/" + path))


class Watched(Case):
    def run_watched(self):
        """Exit code, output, the arguments of every program the run starts and the seconds it
        takes, of the command's main run in this process, every socket refused."""
        calls, original = [], subprocess.run

        def recording(arguments, *rest, **keywords):
            calls.append([str(argument) for argument in arguments])
            return original(arguments, *rest, **keywords)

        def refuse(*arguments, **keywords):
            raise AssertionError("a socket was opened")

        started = time.monotonic()
        with mock.patch.object(subprocess, "run", side_effect=recording), \
                mock.patch.object(socket, "socket", side_effect=refuse), \
                mock.patch.object(socket, "create_connection", side_effect=refuse), \
                mock.patch.object(socket, "getaddrinfo", side_effect=refuse):
            code, output = self.run_inside()
        return code, output, calls, time.monotonic() - started

    def assert_unseen(self, paths, calls):
        """No path of `paths` reached git, and git was asked for what it tracks."""
        self.assertTrue([call for call in calls if "ls-files" in call], calls)
        for path in paths:
            for call in calls:
                self.assertFalse([argument for argument in call if path in argument],
                                 "%r reached git: %r" % (path[:80], call[:6]))


class KindIndex(Watched):
    """The table under `## Kinds of code` of `guidelines/coding.md` and the files of a kind git
    lists (WAY-167, WAY-212), read with crafted rows (WAY-48)."""

    def test_a_kind_file_no_row_names_is_an_error(self):
        """Break caught: a file of a kind left out of the index passing, so an agent led by the
        general file never finds it."""
        self.product(dict(CODING_FILES, **{"guidelines/coding.md": replaced(
            CODING, KINDS_ROW + "\n", "")}))
        code, output, lines = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue([message for _, message in self.errors(output,
                                                               "guidelines/coding-endpoint.md")
                         if "Kinds of code" in message], output)
        self.assertIn("fail", [line["verdict"] for line in lines if line["invariant"] == FORM])

    def test_a_row_differing_from_its_file_only_by_case_or_a_look_alike_is_an_error(self):
        """Breaks caught: the *File* of a row compared with what git lists ignoring case or
        folding Unicode, so a row naming `coding-Endpoint.md` or a Cyrillic `е` passes for the
        file `coding-endpoint.md`; the file itself is then named by no row."""
        for path in ("guidelines/coding-Endpoint.md", "guidelines/coding-\u0435ndpoint.md"):
            with self.subTest(path=path):
                self.setUp()
                row = KINDS_ROW.replace("guidelines/coding-endpoint.md", path)
                general = replaced(CODING, KINDS_ROW, row)
                self.product(dict(CODING_FILES, **{"guidelines/coding.md": general}))
                code, output, _ = self.run_check()
                self.assertEqual(code, 1, output)
                self.assertIn(line_of(general, row),
                              [line for line, message in self.errors(output,
                                                                     "guidelines/coding.md")
                               if "git" in message], output)
                self.assertTrue(self.errors(output, "guidelines/coding-endpoint.md"), output)

    def test_a_row_naming_a_tracked_file_that_is_no_file_of_a_kind_is_an_error(self):
        """Break caught: any path git tracks taken for a file of a kind, so a row pointing to the
        general file or to code passes."""
        for path in ("guidelines/coding.md", "src/api/orders.ts"):
            with self.subTest(path=path):
                self.setUp()
                row = "| endpoint | `%s` | before adding or changing an endpoint |" % path
                general = replaced(CODING, KINDS_ROW, KINDS_ROW + "\n" + row)
                self.product(dict(CODING_FILES, **{"guidelines/coding.md": general}))
                code, output, _ = self.run_check()
                self.assertEqual(code, 1, output)
                self.assertIn(line_of(general, row),
                              [line for line, message in self.errors(output,
                                                                     "guidelines/coding.md")
                               if "guidelines/coding-<kind>.md" in message], output)

    def test_a_file_cell_holding_no_path_in_backticks_is_an_error(self):
        """Break caught: the *File* of a row read bare, though the template gives a path in
        backticks (spec §4.3), so a path written as prose passes."""
        for cell in ("guidelines/coding-endpoint.md", "``", "`guidelines/coding-endpoint.md` x"):
            with self.subTest(cell=cell):
                self.setUp()
                row = KINDS_ROW.replace("`guidelines/coding-endpoint.md`", cell)
                general = replaced(CODING, KINDS_ROW, row)
                self.product(dict(CODING_FILES, **{"guidelines/coding.md": general}))
                code, output, _ = self.run_check()
                self.assertEqual(code, 1, output)
                self.assertIn(line_of(general, row),
                              [line for line, message in self.errors(output,
                                                                     "guidelines/coding.md")
                               if "backticks" in message], output)

    def test_a_kind_file_beside_a_general_file_that_cannot_be_read_is_an_error(self):
        """Break caught: a general file refused unread taken for an index of no row or for a
        complete one, so the file of a kind passes unchecked."""
        self.product(dict(CODING_FILES, **{"guidelines/coding.md": b"x" * (LIMIT + 1)}))
        code, output, _ = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertTrue([message for _, message in self.errors(output,
                                                               "guidelines/coding-endpoint.md")
                         if "guidelines/coding.md" in message], output)

    def test_a_crafted_index_path_is_refused_before_git_sees_it(self):
        """Breaks caught: a *File* of the index handed to git, or tested only once git has seen
        it, so pathspec magic, a path outside the repository or a network share reaches git; a
        socket opened; or matching that runs away on a long path."""
        paths = [path for _, path in crafted("guidelines/coding-endpoint.md")]
        rows = ["| endpoint | `%s` | before adding or changing an endpoint |" % path
                for path in paths]
        general = replaced(CODING, KINDS_ROW, "\n".join([KINDS_ROW] + rows))
        self.product(dict(CODING_FILES, **{"guidelines/coding.md": general}))
        code, output, calls, elapsed = self.run_watched()
        self.assertEqual(code, 1, output[-2000:])
        self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
        reported = {line for line, _ in self.errors(output, "guidelines/coding.md")}
        for what, row in zip([what for what, _ in crafted("x")], rows):
            with self.subTest(what):
                self.assertIn(line_of(general, row), reported, output[-2000:])
        self.assert_unseen(paths, calls)


class FilesOfAKind(Watched):
    """The table under `## Files of this kind` of a file `guidelines/coding-<kind>.md`: one
    exemplar designated by a decision, the closed list of *Status*, each *File* a path git
    tracks (WAY-198, WAY-199), read with crafted rows (WAY-48)."""

    def kind_file(self, text, files=None):
        """Runs the check on the coding guidelines, the file of a kind reading `text`, the log
        holding EXEMPLAR_LOG and the files `files` added."""
        self.product(dict(CODING_FILES, **dict(files or {}, **{
            "foundations/decisions.md": EXEMPLAR_LOG, "guidelines/coding-endpoint.md": text})))
        return self.run_check()

    def exemplar_errors(self, output, line):
        return [message for at, message in self.errors(output, "guidelines/coding-endpoint.md")
                if at == line and "exemplar" in message]

    def test_two_exemplar_rows_are_an_error(self):
        """Break caught: the first `exemplar` row taken and the others passed, so a kind has two
        exemplars and an agent copies either."""
        second = "| `src/api/handler.ts` | exemplar | ABC-06@a7f9c135 |"
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, EXEMPLAR_ROW + "\n" + second)
        code, output, _ = self.kind_file(text)
        self.assertEqual(code, 1, output)
        self.assertTrue([message for message in self.exemplar_errors(output,
                                                                     line_of(text, second))
                         if "line %d" % line_of(text, EXEMPLAR_ROW) in message], output)

    def test_no_exemplar_row_is_an_error(self):
        """Break caught: a table of no `exemplar` row passing, so a kind has no exemplar."""
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, "| `src/api/orders.ts` | copy | — |")
        code, output, _ = self.kind_file(text)
        self.assertEqual(code, 1, output)
        self.assertTrue([message for _, message in self.errors(output,
                                                               "guidelines/coding-endpoint.md")
                         if "no row whose *Status* is `exemplar`" in message], output)

    def test_a_kind_file_lacking_files_of_this_kind_is_an_error(self):
        """Break caught: a file of a kind with no section `## Files of this kind` passing as one
        of no exemplar to check (C32): both the missing section and the missing exemplar are
        reported."""
        text = replaced(CODING_ENDPOINT, "\n".join(["## Files of this kind", "", FILES_HEADER,
                                                    "|---|---|---|", EXEMPLAR_ROW, "", ""]), "")
        code, output, _ = self.kind_file(text)
        self.assertEqual(code, 1, output)
        messages = [message for _, message in self.errors(output, "guidelines/coding-endpoint.md")]
        self.assertTrue([message for message in messages
                         if "`## Files of this kind` is missing" in message], output)
        self.assertTrue([message for message in messages
                         if "no row whose *Status* is `exemplar`" in message], output)

    def test_a_decision_naming_the_path_only_outside_backticks_is_an_error(self):
        """Break caught: the binding sentences searched for the path bare, so a decision that
        names the file in passing designates it."""
        row = EXEMPLAR_ROW.replace("ABC-06@a7f9c135", "ABC-08@" + BARE_PATH_FP)
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, row)
        code, output, _ = self.kind_file(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.exemplar_errors(output, line_of(text, row)), output)

    def test_a_decision_naming_a_shorter_path_than_the_row_is_an_error(self):
        """Break caught: the path searched without its closing backtick, so the decision's
        `` `src/api/orders.ts` `` designates the row's `src/api/orders.tsx`."""
        row = EXEMPLAR_ROW.replace("`src/api/orders.ts`", "`src/api/orders.tsx`")
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, row)
        code, output, _ = self.kind_file(text, {"src/api/orders.tsx": "export {};\n"})
        self.assertEqual(code, 1, output)
        self.assertTrue(self.exemplar_errors(output, line_of(text, row)), output)

    def test_a_decision_number_of_another_log_s_prefix_is_an_error(self):
        """Break caught: a decision number taken with any prefix, so `XYZ-06` stands for the
        log's `ABC-06`."""
        row = EXEMPLAR_ROW.replace("ABC-06@a7f9c135", "XYZ-06@a7f9c135")
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, row)
        code, output, _ = self.kind_file(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.exemplar_errors(output, line_of(text, row)), output)

    def test_a_repealed_decision_is_an_error(self):
        """Break caught: the binding sentences of a decision's first version read where its
        latest repeals it, so a repealed decision still designates the exemplar."""
        row = EXEMPLAR_ROW.replace("ABC-06@a7f9c135", "ABC-07@" + REPEALED_FP)
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, row)
        code, output, lines = self.kind_file(text)
        self.assertEqual(code, 1, output)
        self.assertTrue([message for message in self.exemplar_errors(output, line_of(text, row))
                         if "ABC-07" in message], output)
        self.assertIn("fail", [line["verdict"] for line in lines if line["invariant"] == FORM])

    def test_a_stale_fingerprint_of_the_exemplar_s_decision_is_an_error(self):
        """Break caught: the reference in the exemplar's row left out of the checks of
        references, so the exemplar stays designated by a decision whose binding sentences
        changed (spec §5.2 item 4, WAY-169)."""
        row = EXEMPLAR_ROW.replace("ABC-06@a7f9c135", "ABC-06@a7f9c130")
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, row)
        self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": text}))
        code, output, lines = self.run_check("--merge-onto", "none")
        self.assertEqual(code, 1, output)
        self.assertTrue([message for at, message in self.errors(
            output, "guidelines/coding-endpoint.md") if at == line_of(text, row)
            and "a7f9c135" in message], output)
        self.assertIn("fail", [line["verdict"] for line in lines
                               if line["invariant"] == REFERENCES])

    def test_a_file_of_the_kind_the_table_leaves_out_passes(self):
        """Break caught: the table of the files of a kind asked to list every file of the kind,
        so a file added after the audit fails until someone writes its row (C13)."""
        self.product(dict(CODING_FILES, **{"src/api/carts.ts": CODING_FILES["src/api/orders.ts"],
                                           "src/api/users.ts": CODING_FILES["src/api/orders.ts"]}))
        code, output, _ = self.run_check()
        self.assertEqual(code, 0, output)

    def test_a_file_cell_holding_no_path_in_backticks_is_an_error(self):
        """Break caught: the *File* of a row read bare, though the template gives a path in
        backticks (spec §4.3)."""
        row = "| src/api/handler.ts | copy | — |"
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, EXEMPLAR_ROW + "\n" + row)
        code, output, _ = self.kind_file(text)
        self.assertEqual(code, 1, output)
        self.assertIn(line_of(text, row), [line for line, message in self.errors(
            output, "guidelines/coding-endpoint.md") if "backticks" in message], output)

    def test_a_crafted_file_path_is_refused_before_git_sees_it(self):
        """Breaks caught: a *File* handed to git, or tested only once git has seen it; a socket
        opened; or matching that runs away on a long path."""
        paths = [path for _, path in crafted("src/api/handler.ts")]
        rows = ["| `%s` | copy | — |" % path for path in paths]
        text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, "\n".join([EXEMPLAR_ROW] + rows))
        self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": text}))
        code, output, calls, elapsed = self.run_watched()
        self.assertEqual(code, 1, output[-2000:])
        self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
        reported = {line for line, _ in self.errors(output, "guidelines/coding-endpoint.md")}
        for what, row in zip([what for what, _ in crafted("x")], rows):
            with self.subTest(what):
                self.assertIn(line_of(text, row), reported, output[-2000:])
        self.assert_unseen(paths, calls)

    def test_a_row_of_one_mebibyte_of_bars_or_backticks_finishes_within_a_bound(self):
        """Break caught: reading a crafted row of the files of a kind that runs away, so the run
        never ends with a report."""
        for name, make in (("bars", lambda room: "|" * room),
                           ("backticks",
                            lambda room: "| " + "`" * (room - 20) + " | copy | — |")):
            with self.subTest(name):
                self.setUp()
                head = replaced(CODING_ENDPOINT, EXEMPLAR_ROW,
                                EXEMPLAR_ROW + "\n\0").encode("utf-8")
                room = LIMIT - 16 - (len(head) - 1)
                data = head.replace(b"\0", make(room).encode("utf-8"))
                self.assertLess(len(data), LIMIT)
                self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": data}))
                started = time.monotonic()
                code, output, _ = self.run_check(timeout=120)
                elapsed = time.monotonic() - started
                self.assertEqual(code, 1, output[-2000:])
                self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
                self.assertTrue(self.errors(output, "guidelines/coding-endpoint.md"),
                                output[-2000:])


# The test cases of the rule of the file of a kind (WAY-168): the pair of `endpoint-handler`, as
# CODING_ENDPOINT holds it, and a second invariant and the product's `guidelines-form`, which a
# rule may name beside it.
LOCATION = "Every file of the kind endpoint lies under the directory src/api."
LOCATION_FP = "f58796ac"
GUIDELINES_FORM = (
    "Every file `guidelines/<name>.md` holds, in their order, the header lines, sections, rules, "
    "rule fields and tables that the template of guidelines and the template of its discipline "
    "require at the commit of the-way the repository uses — the commit checked, in the-way itself, "
    "and the pinned commit, in a product — each with the values and the links those templates give "
    "it, with a name that agrees with its *Discipline*, each section or rule it drops reading "
    "`none —` with a decision of the log and that decision's fingerprint, each part it names being "
    "a part of the map, and each path under `## Where in code` naming something git tracks.")
GUIDELINES_FORM_FP = "7196030f"


def invariant_entry(identifier, sentence):
    """An entry of the invariants file, deriving from the exemplar's decision."""
    return ("## %s/1\n\n%s\n\n- **Method:** `python -B tests/check.py`\n- **Rests on:** none\n"
            "- **Derives from:** ABC-06@%s\n- **Part:** web\n- **Correction:** none\n\n"
            % (identifier, sentence, EXEMPLAR_FP))


CASES_INVARIANTS = replaced(CODING_INVARIANTS, "## Withdrawn identifiers",
                            invariant_entry("endpoint-location", LOCATION)
                            + invariant_entry("guidelines-form", GUIDELINES_FORM)
                            + "## Withdrawn identifiers")
INVARIANT_FIELD = "- **Invariant:** endpoint-handler@8c2ca199"
GOOD_OPEN = "```good endpoint-handler src/api/carts.ts"
GOOD_TEXT = ('import { handle } from "./handler";',
             "export const POST = handle((input: unknown) => input);")
GOOD_CASE = "\n".join((GOOD_OPEN,) + GOOD_TEXT + ("```",))
BAD_OPEN = "```bad endpoint-handler src/api/carts.ts"
BAD_CASE = "\n".join([BAD_OPEN, "export const POST = (input: unknown) => input;", "```"])
CASES = GOOD_CASE + "\n\n" + BAD_CASE + "\n\n"
OPEN_LINE = line_of(CODING_ENDPOINT, GOOD_OPEN)
CHECK_CASES = "product-guidelines/form_check.py::check_cases"


def pair(identifier, path="src/api/carts.ts"):
    """A good and a bad case of the invariant `identifier`, each followed by a blank line."""
    return ("```good %s %s\nexport {};\n```\n\n```bad %s %s\nexport const x = 1;\n```\n\n"
            % (identifier, path, identifier, path))


class TestCases(Watched):
    """The test cases of every rule whose *Invariant* names an invariant other than
    `guidelines-form`: a good and a bad case of each such invariant after the rule's fields, each
    a fenced block of three backticks whose info string reads `good|bad <identifier> <path>`
    (WAY-168, spec §5.2 item 5), read with crafted fences, info strings and paths (WAY-48)."""

    def endpoint(self, text, invariants=CASES_INVARIANTS):
        """Exit code, output and record of the check run on the coding guidelines, the file of a
        kind reading `text` and the invariants file `invariants`."""
        self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": text,
                                           "foundations/invariants.md": invariants}))
        return self.run_check()

    def at(self, output, line, fragment=""):
        """The messages of the errors the file of a kind reports at `line` holding `fragment`."""
        return [message for at, message in self.errors(output, "guidelines/coding-endpoint.md")
                if at == line and fragment in message]

    def missing(self, output, which, identifier="endpoint-handler"):
        """The messages reporting that the rule gives no `which` case of `identifier`."""
        return [message for _, message in self.errors(output, "guidelines/coding-endpoint.md")
                if "no `%s %s <path>`" % (which, identifier) in message]

    def run_sealed(self):
        """As run_watched, with every path the run gives `os.open`, `os.lstat`, `os.stat` or
        `open` recorded too: (exit code, output, git's arguments, paths opened, seconds)."""
        opened, real_open = [], open
        real = {name: getattr(os, name) for name in ("open", "lstat", "stat")}

        def watching(name):
            def wrapper(path, *rest, **keywords):
                opened.append(os.fsdecode(path) if isinstance(path, (str, bytes)) else str(path))
                return real[name](path, *rest, **keywords)
            return wrapper

        def opening(path, *rest, **keywords):
            opened.append(os.fsdecode(path) if isinstance(path, (str, bytes)) else str(path))
            return real_open(path, *rest, **keywords)

        with mock.patch.object(os, "open", watching("open")), \
                mock.patch.object(os, "lstat", watching("lstat")), \
                mock.patch.object(os, "stat", watching("stat")), \
                mock.patch("builtins.open", opening):
            code, output, calls, elapsed = self.run_watched()
        return code, output, calls, opened, elapsed

    def assert_sealed(self, paths, calls, opened):
        """No path of `paths` reached git or the file system, and both were asked something."""
        self.assert_unseen(paths, calls)
        self.assertTrue([path for path in opened if "guidelines" in path], opened[:20])
        for path in paths:
            self.assertFalse([each for each in opened if path in each],
                             "%r was opened or looked at" % path[:80])

    def test_the_cases_of_the_valid_file_pass_and_are_recorded(self):
        """Break caught: the check of test cases recorded under no check of its own, or failing
        a rule that gives its pair, so the valid coding guidelines never pass."""
        code, output, lines = self.endpoint(CODING_ENDPOINT)
        self.assertEqual(code, 0, output)
        self.assertIn("pass", [line["verdict"] for line in lines
                               if line["check"] == CHECK_CASES and line["invariant"] == FORM])

    def test_a_rule_naming_an_invariant_with_no_case_is_an_error(self):
        """Break caught: a rule naming an invariant passing without its good case, its bad case
        or both, so its *Good* and *Bad* stay descriptions no gate can apply (WAY-168)."""
        for name, old, gone in (("no case", CASES, ("good", "bad")),
                                ("no good case", GOOD_CASE + "\n\n", ("good",)),
                                ("no bad case", BAD_CASE + "\n\n", ("bad",))):
            with self.subTest(name):
                self.setUp()
                text = replaced(CODING_ENDPOINT, old, "")
                code, output, lines = self.endpoint(text)
                self.assertEqual(code, 1, output)
                for which in ("good", "bad"):
                    reported = [message for message in self.missing(output, which)
                                if message in self.at(output, line_of(text, INVARIANT_FIELD))]
                    self.assertEqual(bool(reported), which in gone, output)
                self.assertIn("fail", [line["verdict"] for line in lines
                                       if line["check"] == CHECK_CASES
                                       and line["invariant"] == FORM], lines)

    def test_a_case_left_open_to_the_end_of_the_file_is_an_error_at_its_opening_line(self):
        """Break caught: a case never closed taken as a case holding the rest of the file, so the
        sections it swallows go unread and the case counts (spec §5.2 item 5)."""
        text = replaced(CODING_ENDPOINT, BAD_CASE, BAD_CASE[:-len("\n```")])
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.at(output, line_of(text, BAD_OPEN), "open to the end"), output)

    def test_a_tilde_fence_or_four_backticks_opening_a_case_is_a_malformed_case(self):
        """Break caught: a case's info string read from a fence other than three backticks, which
        the template gives as its outer fence, so a tilde fence counts as the case."""
        for name, case in (("tildes", BAD_CASE.replace("```", "~~~")),
                           ("four backticks", BAD_CASE.replace("```", "````"))):
            with self.subTest(name):
                self.setUp()
                text = replaced(CODING_ENDPOINT, BAD_CASE, case)
                code, output, _ = self.endpoint(text)
                self.assertEqual(code, 1, output)
                self.assertTrue(self.at(output, line_of(text, case.split("\n")[0]),
                                        "malformed test case"), output)
                self.assertTrue(self.missing(output, "bad"), output)

    def test_a_fence_of_four_backticks_closing_a_case_is_an_error_at_that_line(self):
        """Break caught: a case closed by a fence other than three backticks passing, though the
        template gives three backticks as the outer fence of a case."""
        text = replaced(CODING_ENDPOINT, GOOD_CASE, GOOD_CASE + "`")
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.at(output, line_of(text, "````"), "three backticks"), output)
        self.assertFalse(self.missing(output, "good"), output)

    def test_a_line_inside_a_case_that_would_open_a_fence_is_an_error_at_that_line(self):
        """Breaks caught: a line starting with three tildes, or three backticks followed by text,
        passing inside a case; or one indented by four spaces or more, a tab or a no-break space
        passing because Markdown would read no fence there, though
        `instruction-files/check_instructions.py` toggles code after any leading whitespace (C33).
        The case itself still counts."""
        for fence in ("~~~", "~~~ts", "```ts", "   ```ts", "    ```", "        ~~~ts", "\t```ts",
                      "  ~~~", " ```ts"):
            with self.subTest(fence=fence):
                self.setUp()
                case = "\n".join((GOOD_OPEN, GOOD_TEXT[0], fence, GOOD_TEXT[1], "```"))
                text = replaced(CODING_ENDPOINT, GOOD_CASE, case)
                code, output, _ = self.endpoint(text)
                self.assertEqual(code, 1, output)
                self.assertTrue(self.at(output, line_of(text, fence), "opens a fence"), output)
                self.assertFalse(self.missing(output, "good"), output)

    def test_a_fence_after_a_line_break_python_splits_lines_on_inside_a_case_is_an_error(self):
        """Break caught: a line inside a case read whole where
        `instruction-files/check_instructions.py`, which splits lines as Python's `splitlines`
        does, sees two — after a carriage return, a line or paragraph separator, a next-line
        character, a vertical tab, a form feed or a file separator — the second starting with a
        fence on which that script switches between code and text (C33)."""
        for name, mark in (("carriage return", "\r"), ("line separator", " "),
                           ("paragraph separator", " "), ("next line", "\x85"),
                           ("vertical tab", "\x0b"), ("form feed", "\x0c"),
                           ("file separator", "\x1c")):
            with self.subTest(name):
                self.setUp()
                inner = GOOD_TEXT[0] + mark + "  ~~~ts"
                case = "\n".join((GOOD_OPEN, inner, GOOD_TEXT[1], "```"))
                text = replaced(CODING_ENDPOINT, GOOD_CASE, case)
                code, output, _ = self.endpoint(text)
                self.assertEqual(code, 1, output)
                self.assertTrue(self.at(output, line_of(text, inner), "opens a fence"), output)

    def test_a_bare_fence_inside_a_good_case_is_a_malformed_case_at_its_former_closing_fence(self):
        """Break caught (C21): a bare line of three backticks inside a case read as anything but
        the case's end, so the case's own closing line, which then opens a block with no info
        string, goes unreported; the shortened case still counts as the good case."""
        case = "\n".join((GOOD_OPEN, GOOD_TEXT[0], "```", GOOD_TEXT[1], "```"))
        text = replaced(CODING_ENDPOINT, GOOD_CASE, case)
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.at(output, line_of(text, GOOD_TEXT[1]) + 1, "malformed test case"),
                        output)
        self.assertFalse(self.missing(output, "good"), output)

    def test_an_info_string_of_another_form_is_a_malformed_case_at_its_opening_line(self):
        """Breaks caught: an info string with no identifier or no path, two spaces or two paths,
        a word other than `good` or `bad` in its case, an identifier that is no identifier, or
        none at all, taken for a case, so a block no gate can apply counts."""
        for opening in ("```good", "```good endpoint-handler",
                        "```good endpoint-handler  src/api/carts.ts src/api/users.ts",
                        "```good endpoint-handler src/api/carts.ts src/api/users.ts",
                        "```GOOD endpoint-handler src/api/carts.ts",
                        "```good Endpoint-handler src/api/carts.ts",
                        "```sample endpoint-handler src/api/carts.ts", "```ts", "```"):
            with self.subTest(opening=opening):
                self.setUp()
                text = replaced(CODING_ENDPOINT, GOOD_OPEN, opening)
                code, output, _ = self.endpoint(text)
                self.assertEqual(code, 1, output)
                self.assertTrue(self.at(output, OPEN_LINE, "malformed test case"), output)
                self.assertTrue(self.missing(output, "good"), output)

    def test_an_info_string_on_a_closing_fence_is_a_line_that_opens_a_fence(self):
        """Break caught: an info string read from the line meant to close a case, which closes
        nothing, so the case runs on and a second case is taken from its end."""
        closing = "```good endpoint-handler src/api/elsewhere.ts"
        text = replaced(CODING_ENDPOINT, GOOD_CASE, GOOD_CASE[:-len("```")] + closing)
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.at(output, line_of(text, closing), "opens a fence"), output)

    def test_a_case_naming_an_invariant_the_rule_does_not_name_is_an_error(self):
        """Break caught: a case counted whatever invariant it names, so a pair for an invariant
        of the file, for one the file does not hold, or for `guidelines-form` passes beside a
        rule that names none of them."""
        for identifier in ("endpoint-location", "lint-clean", "guidelines-form"):
            with self.subTest(identifier=identifier):
                self.setUp()
                text = replaced(CODING_ENDPOINT, CASES, CASES + pair(identifier))
                code, output, _ = self.endpoint(text)
                self.assertEqual(code, 1, output)
                self.assertTrue(self.at(output, line_of(text, "```good %s src/api/carts.ts"
                                                        % identifier), "does not name"), output)

    def test_a_rule_naming_two_invariants_with_the_pair_of_one_only_is_an_error(self):
        """Break caught: a rule naming two invariants passing on the pair of the first, so the
        second has no case (C18); its control, with both pairs, passes."""
        two = "- **Invariant:** endpoint-handler@8c2ca199 · endpoint-location@" + LOCATION_FP
        text = replaced(CODING_ENDPOINT, INVARIANT_FIELD, two)
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        for which in ("good", "bad"):
            self.assertTrue([message for message in self.missing(output, which,
                                                                 "endpoint-location")
                             if message in self.at(output, line_of(text, two))], output)
            self.assertFalse(self.missing(output, which), output)
        self.setUp()
        code, output, _ = self.endpoint(replaced(text, CASES, CASES + pair("endpoint-location")))
        self.assertEqual(code, 0, output)

    def test_a_second_case_of_one_kind_is_an_error_at_its_opening_line(self):
        """Break caught: a second good case of the same invariant passing, so the gate cannot
        tell which file the rule gives."""
        second = GOOD_CASE.replace("src/api/carts.ts", "src/api/baskets.ts")
        text = replaced(CODING_ENDPOINT, CASES, CASES + second + "\n\n")
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.at(output, line_of(text, second.split("\n")[0]),
                                "line %d" % OPEN_LINE), output)

    def test_a_block_before_the_rule_s_fields_end_is_a_malformed_case(self):
        """Break caught: a case standing among the rule's fields counted, though the cases stand
        after them."""
        text = replaced(CODING_ENDPOINT, CASES, "")
        text = replaced(text, INVARIANT_FIELD, GOOD_CASE + "\n" + INVARIANT_FIELD)
        code, output, _ = self.endpoint(text)
        self.assertEqual(code, 1, output)
        self.assertTrue(self.at(output, line_of(text, GOOD_OPEN), "malformed test case"), output)

    def test_a_rule_naming_guidelines_form_needs_no_case_and_takes_none_of_it(self):
        """Breaks caught: a rule naming the product's `guidelines-form` alone asked for cases,
        or its fenced blocks read as cases although no case of it is given (C11); a rule naming
        it beside another invariant asked for its cases, passing with no case of the other
        invariant, as if naming `guidelines-form` exempted the whole rule, or passing a pair of
        it."""
        alone = "- **Invariant:** guidelines-form@" + GUIDELINES_FORM_FP
        beside = ("- **Invariant:** guidelines-form@%s · endpoint-handler@8c2ca199"
                  % GUIDELINES_FORM_FP)
        clean = (("alone, with no block", replaced(replaced(CODING_ENDPOINT, CASES, ""),
                                                    INVARIANT_FIELD, alone)),
                 ("alone, with blocks", replaced(replaced(CODING_ENDPOINT, CASES,
                                                          pair("guidelines-form",
                                                               "guidelines/coding-x.md")),
                                                 INVARIANT_FIELD, alone)),
                 ("beside another, with its pair", replaced(CODING_ENDPOINT, INVARIANT_FIELD,
                                                            beside)))
        for name, text in clean:
            with self.subTest(name):
                self.setUp()
                code, output, _ = self.endpoint(text)
                self.assertEqual(code, 0, output)
                self.assertNotIn(": error:", output)
        with self.subTest("beside another, with no case of the other"):
            self.setUp()
            text = replaced(replaced(CODING_ENDPOINT, INVARIANT_FIELD, beside), CASES, "")
            code, output, _ = self.endpoint(text)
            self.assertEqual(code, 1, output)
            for which in ("good", "bad"):
                self.assertTrue([message for message in self.missing(output, which)
                                 if message in self.at(output, line_of(text, beside))], output)
                self.assertFalse(self.missing(output, which, "guidelines-form"), output)
        with self.subTest("beside another, with a pair of it"):
            self.setUp()
            text = replaced(replaced(CODING_ENDPOINT, INVARIANT_FIELD, beside), CASES,
                            CASES + pair("guidelines-form", "guidelines/coding-x.md"))
            code, output, _ = self.endpoint(text)
            self.assertEqual(code, 1, output)
            self.assertTrue(self.at(output, line_of(text, "```good guidelines-form "
                                                    "guidelines/coding-x.md"),
                                    "guidelines-form"), output)

    def test_a_crafted_case_path_is_refused_and_never_reaches_git_or_the_file_system(self):
        """Breaks caught: a case path outside the repository passing — absolute, a UNC prefix, a
        `..` segment, a backslash, a drive, a character that is not printable, pathspec magic —
        or any case path, refused or not, given to git, opened or looked at; a socket opened; or
        matching that runs away on a path of 200 KiB, which, relative, names a file not yet
        written and passes."""
        for what, path in crafted("src/api/carts.ts") + (("the valid path", "src/api/carts.ts"),):
            with self.subTest(what):
                self.setUp()
                text = replaced(CODING_ENDPOINT, GOOD_OPEN,
                                "```good endpoint-handler " + path)
                self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": text,
                                                   "foundations/invariants.md": CASES_INVARIANTS}))
                code, output, calls, opened, elapsed = self.run_sealed()
                self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
                allowed = what in ("200 KiB", "the valid path")
                self.assertEqual(code, 0 if allowed else 1, output[-2000:])
                self.assertEqual(bool(self.at(output, OPEN_LINE, "path")), not allowed,
                                 output[-2000:])
                self.assert_sealed([path, "src/api/carts.ts"], calls, opened)

    def test_an_info_string_of_one_mebibyte_finishes_within_a_bound(self):
        """Break caught: reading a crafted info string that runs away, or printing it whole: a
        path of nearly one MiB, which names a file not yet written and passes unopened, and an
        identifier of nearly one MiB, which the rule does not name and is printed cut."""
        for name in ("path", "identifier"):
            with self.subTest(name):
                self.setUp()
                head = replaced(CODING_ENDPOINT, GOOD_OPEN, "\0").encode("utf-8")
                room = LIMIT - len(head) - 64
                opening = ("```good endpoint-handler src/" + "a" * room if name == "path"
                           else "```good " + "a" * room + " src/api/carts.ts")
                data = head.replace(b"\0", opening.encode("utf-8"))
                self.assertLess(len(data), LIMIT)
                self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": data,
                                                   "foundations/invariants.md": CASES_INVARIANTS}))
                code, output, calls, opened, elapsed = self.run_sealed()
                self.assertLess(elapsed, 30, "the run took %.1f s" % elapsed)
                self.assertLess(len(output), 20000)
                if name == "path":
                    self.assertEqual(code, 0, output[-2000:])
                    self.assert_sealed(["a" * 100], calls, opened)
                else:
                    self.assertEqual(code, 1, output[-2000:])
                    self.assertTrue(self.at(output, OPEN_LINE, "does not name"), output[-2000:])

    def test_a_file_of_cases_just_over_one_mebibyte_is_refused_unread(self):
        """Break caught: a file of guidelines over the limit read for its cases, so a crafted
        file of cases costs what it likes and its paths are seen (WAY-48)."""
        padding = "// " + "x" * 100
        head = replaced(CODING_ENDPOINT, GOOD_CASE, "\n".join(
            (GOOD_OPEN, GOOD_TEXT[0], "\0", GOOD_TEXT[1], "```"))).encode("utf-8")
        room = LIMIT + 1 - (len(head) - 1)
        lines = "\n".join([padding] * (room // (len(padding) + 1)))
        body = (lines + "\n" + "x" * (room - len(lines) - 1)).encode("utf-8")
        data = head.replace(b"\0", body)
        self.assertEqual(len(data), LIMIT + 1)
        self.product(dict(CODING_FILES, **{"guidelines/coding-endpoint.md": data,
                                           "foundations/invariants.md": CASES_INVARIANTS}))
        code, output, calls, opened, elapsed = self.run_sealed()
        self.assertEqual(code, 1, output[-2000:])
        self.assertTrue([message for _, message in self.errors(output,
                                                               "guidelines/coding-endpoint.md")
                         if "holds more than 1048576 bytes; it is not read" in message], output)
        self.assertFalse(self.missing(output, "good"), output)
        self.assert_sealed(["src/api/carts.ts"], calls, opened)


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
    reference names, beyond what the invariants of guidelines assert (WAY-169, WAY-74)."""

    def assert_clean(self, code, output):
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)

    def test_a_run_with_merge_onto_records_lines_of_guidelines_reference_current_alone(self):
        """Breaks caught: a run given `--merge-onto` recording the checks of form, or no check of
        references; `none` given and the check after the merge recorded as anything but
        `unchecked` with the shared reason, or the check on the commit itself left out."""
        self.product({"guidelines/testing.md": TESTING,
                      "guidelines/observability.md": as_observability(NO_GOOD)})
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
        reference error, or records them: every check runs and prints in every run, and the
        record holds the checks the run's options select."""
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
        number with another log's prefix taken for a reference (the forms the sentence of
        `guidelines-reference-current` gives). The control at the
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
        form check fails on a rule of the log (`log-merge-copies`) and not of guidelines."""
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
        no change (WAY-169)."""
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
                # The rule names `fixture-named`, so it gives a good and a bad case of it.
                text = replaced(with_line(TESTING, INVARIANT_LINE, cited % carried),
                                "fixtures.\n\n## Examples", "fixtures.\n\n" + FIXTURE_CASES
                                + "## Examples")
                self.product_onto({"guidelines/testing.md": text}, onto, branch,
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
    """A product's files are untrusted input (WAY-48)."""

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
