"""Invariant tests of the form check of guidelines, `product-guidelines/form_check.py`.

Each test builds a product in a temporary git repository — a decision log, an invariants file, a
part map, the files `## Where in code` points to and one or more files `guidelines/<name>.md` —
runs the command as a subprocess on it and asserts its exit code, its report lines
`guidelines/<name>.md:<line>: error: …` and the lines of its record.

Inputs, expected fingerprints and expected fragments of the report are written out below, never
computed by the code under test (WAY-69): each fingerprint was computed once, by hand, with
`relation-model/fingerprint.py` from the binding sentence it stands beside. A valid styleguide and
a valid file of a discipline the-way has no template of pass first; every other test breaks one
thing in them, so a test that sees an error sees the one its break caused. The tests that replace
a line name the line they expect there, so a fixture whose lines move fails loudly instead of
making a check pass for the wrong reason.

Run from the root of the-way:
    python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
THE_WAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(THE_WAY, "product-guidelines", "form_check.py")

FORM = "guidelines-form/1"
REFERENCES = "guidelines-reference-current/1"

# Binding sentences of the fixture's foundation, each with its fingerprint written out.
ROLES_DECISION = ("The background role primary marks the main action of a screen, and the text "
                  "role primary-text stands on it.")
ROLES_FP = "daa9cf8d"
ROLES_REWORDED = ("The background role primary marks the one main action of a screen, and the "
                  "text role primary-text stands on it.")
ROLES_REWORDED_FP = "cca35182"
MUTED_DECISION = "The role muted marks what matters less than what is around it."
MUTED_FP = "9bb0959d"
DEPARTURE_DECISION = ("The product's styleguide drops the rules on design tokens, focus, contrast, "
                      "shared controls, global values, sources of values and the kitchen-sink "
                      "page until the product draws screens of its own.")
DEPARTURE_FP = "8503cafa"
FONT_DECISION = "The product draws its text in one font of its own."
FONT_FP = "7ba1b4bb"
FIXTURES_DECISION = "Each test of the product sets up its data through the product's fixtures."
FIXTURES_FP = "016b5b2a"
ROLE_MEANING = ("No screen of the web interface uses a colour role in a meaning other than the "
                "one its decision gives.")
ROLE_MEANING_FP = "a2557545"
ROLE_MEANING_REWORDED = ("No screen of the web interface uses a colour role in any meaning other "
                         "than the one its decision gives.")
ROLE_MEANING_REWORDED_FP = "cbbaa72e"
PAIR = "Every background role of the styleguide's table names the text role that stands on it."
PAIR_FP = "169d4c67"

# Fingerprints that differ from the current one only in their last character.
ROLES_STALE = "daa9cf80"
ROLE_MEANING_STALE = "a2557540"
DEPARTURE_STALE = "8503cafb"


def decision(number, ver, question, binding, change):
    """A decision version in the form of the decisions template."""
    lines = ["### ABC-%02d/%d — %s" % (number, ver, question), ""]
    if binding is not None:
        lines += [binding, ""]
    lines += ["- **Change:** " + change, "- **Scope:** web", "- **Based on:** none",
              "- **Relations:** none",
              "- **Verification:** level 2 — an agent compares the change with the decision:",
              "  - complies: a screen follows the decision;",
              "  - violates: a screen goes against it.",
              "- **Review when:** none", "- **Origin:** none",
              "- **Approved by:** Anna, 2026-09-01", "",
              "*%s:* one role carries one meaning." % ("Rationale" if ver == 1
                                                      else "Rationale for change"),
              "*Rejected:* none considered"]
    return "\n".join(lines)


def log(*versions):
    return "# Decision log\n\nIntro.\n\n" + "\n\n".join(versions) + "\n"


ABC_01 = decision(1, 1, "Which roles mark the main action?", ROLES_DECISION, "new decision")
ABC_01_REWORDED = decision(1, 2, "Which roles mark the main action?", ROLES_REWORDED,
                           "new wording")
ABC_02 = decision(2, 1, "Which role marks what matters less?", MUTED_DECISION, "new decision")
ABC_03 = decision(3, 1, "Which rules of the styleguide does the product drop?",
                  DEPARTURE_DECISION, "new decision")
ABC_04 = decision(4, 1, "Which font does the product draw its text in?", FONT_DECISION,
                  "new decision")
ABC_04_REPEALED = decision(4, 2, "Which font does the product draw its text in?", None, "repeal")
ABC_05 = decision(5, 1, "How does a test set up its data?", FIXTURES_DECISION, "new decision")

LOG = log(ABC_01, ABC_02, ABC_03, ABC_04, ABC_04_REPEALED, ABC_05)
# The log the commit merged onto holds: ABC-01 reworded there, and only there.
LOG_ONTO = log(ABC_01, ABC_02, ABC_03, ABC_04, ABC_04_REPEALED, ABC_05, ABC_01_REWORDED)


def invariant(identifier, ver, sentence):
    return "\n".join(["## %s/%d" % (identifier, ver), "", sentence, "",
                      "- **Method:** `python -B tests/check_roles.py`", "- **Rests on:** none",
                      "- **Derives from:** ABC-01@" + ROLES_FP, "- **Part:** web",
                      "- **Correction:** none"])


def invariants(*entries):
    return "# Invariants\n\n" + "\n\n".join(entries + (
        "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n"
        "| old-pair | merged with another entry | background-pair |",
        "## Quarantined invariants\n\n| Identifier | Version | Until |\n|---|---|---|")) + "\n"


INVARIANTS = invariants(invariant("role-meaning", 1, ROLE_MEANING),
                        invariant("background-pair", 1, PAIR))
# The invariants file the commit merged onto holds: role-meaning reworded there, and only there.
INVARIANTS_ONTO = invariants(invariant("role-meaning", 2, ROLE_MEANING_REWORDED),
                             invariant("background-pair", 1, PAIR))

PART_MAP = """# Part map

## web — The web interface

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
    "src/tokens.css": ":root { --primary: #1d4ed8; }\n",
    "src/components/button.tsx": "export const Button = () => null;\n",
    "tests/fixtures.py": "PLAYER = {}\n",
}

# A styleguide holding every part its template requires; seven required rules are dropped by
# ABC-03. The comments give the line each piece starts on.
TITLE = "# Styleguide guidelines — the web interface\n\n"                          # 1
HEADER = "- **Discipline:** styleguide\n- **Applies to:** web\n\n"                  # 3
WHEN = "## When to read\n\nBefore changing a screen of the web interface.\n\n"      # 6
ROLES = ("## Roles\n\n"                                                             # 10
         "| Role | Kind | Meaning for the user | Text on it | Decision |\n"
         "|---|---|---|---|---|\n"
         "| primary | background | this is the main action of the screen | primary-text | "
         "ABC-01@" + ROLES_FP + " |\n"                                              # 14
         "| primary-text | text | this text stands on the main action | — | "
         "ABC-01@" + ROLES_FP + " |\n"
         "| muted | other | this matters less than what is around it | — | "
         "ABC-02@" + MUTED_FP + " |\n\n")                                           # 16
EACH_ROLE = ("### Each role in its meaning\n\n"                                     # 20
             "- **Decision:** ABC-01@" + ROLES_FP + " · ABC-02@" + MUTED_FP + "\n"  # 22
             "- **Invariant:** role-meaning@" + ROLE_MEANING_FP + "\n"              # 23
             "- **Good:** the main action of a form uses `primary`.\n"
             "- **Bad:** a warning uses `primary`.\n\n"
             "Use each role only in the meaning its decision gives.\n\n")           # 27
BACKGROUND = ("### Every background with its text\n\n"                              # 29
              "- **Decision:** ABC-01@" + ROLES_FP + "\n"                           # 31
              "- **Invariant:** background-pair@" + PAIR_FP + "\n"                  # 32
              "- **Good:** `primary` stands in the table with `primary-text`.\n"
              "- **Bad:** `primary` stands in the table with no text role.\n\n"
              "Write every background role with the text role that stands on it.\n\n")  # 36
DROPPED = ("No value in place of a design token", "Visible focus", "Contrast of every pair",
           "States of shared controls", "A fault of one screen is fixed in its component",
           "Every value with its source", "The kitchen-sink page")


def dropped(name):
    return "### %s\n\nnone — ABC-03@%s\n\n" % (name, DEPARTURE_FP)


RULES = ("## Rules\n\n" + EACH_ROLE + BACKGROUND                                    # 18
         + "".join(dropped(name) for name in DROPPED))                              # 38 … 64
EXAMPLES = ("## Examples\n\n"                                                       # 66
            "### Mockups\n\n"
            "A mockup is a pattern to compare against; meanings come from this file.\n\n"  # 70
            "### Plan of a user-interface change\n\n"
            "Settle the library, then the values, then one screen, then its states.\n\n")
WHERE = "## Where in code\n\n- `src/tokens.css`\n- `src/components`\n"              # 76, 78
STYLEGUIDE = TITLE + HEADER + WHEN + ROLES + RULES + EXAMPLES + WHERE
STYLEGUIDE_FILE = "guidelines/styleguide-web.md"

# Guidelines of a discipline the-way gives no template of: the common form alone.
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
TESTING_FILE = "guidelines/testing.md"


def with_line(text, number, expected, new):
    """`text` with its line `number` (from 1) replaced by `new`; the line must read `expected`."""
    lines = text.split("\n")
    if lines[number - 1] != expected:
        raise AssertionError("line %d of the fixture reads %r, not %r"
                             % (number, lines[number - 1], expected))
    lines[number - 1] = new
    return "\n".join(lines)


def replaced(text, old, new):
    """`text` with the one occurrence of `old` replaced by `new`."""
    if text.count(old) != 1:
        raise AssertionError("the fixture holds %r %d times, not once" % (old, text.count(old)))
    return text.replace(old, new)


class FormCheckTestCase(unittest.TestCase):
    def check(self, guidelines, options=("--merge-onto", "none"), onto=None, untracked=None):
        """Runs the form check on a product whose base commit holds FOUNDATION, and whose main
        branch then gains a commit holding `guidelines` ({path: text}). Given `onto` ({path:
        text}), a branch `onto` leaves the base commit with those files changed, so that a merge
        onto it takes them. `untracked` files are written into the working tree and never added.
        Returns the exit code, the output, the record's lines and the options given."""
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory, \
                tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as outside:
            root = os.path.join(os.path.realpath(directory), "product")
            os.makedirs(root)

            def write(files):
                for path, text in files.items():
                    full = os.path.join(root, *path.split("/"))
                    os.makedirs(os.path.dirname(full), exist_ok=True)
                    with open(full, "w", encoding="utf-8", newline="\n") as handle:
                        handle.write(text)

            def git(*arguments):
                subprocess.run(["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com",
                                "-c", "core.autocrlf=false"] + list(arguments),
                               cwd=root, check=True, capture_output=True)

            git("init", "-q", "-b", "main")
            write(FOUNDATION)
            git("add", "-A")
            git("commit", "-q", "-m", "foundation")
            if onto is not None:
                git("checkout", "-q", "-b", "onto")
                write(onto)
                git("add", "-A")
                git("commit", "-q", "-m", "onto")
                git("checkout", "-q", "main")
            write(guidelines)
            git("add", "-A")
            git("commit", "-q", "-m", "guidelines")
            if untracked:
                write(untracked)
            record = os.path.join(os.path.realpath(outside), "guidelines.jsonl")
            environment = dict(os.environ, PYTHONIOENCODING="utf-8")
            run = subprocess.run([sys.executable, "-B", SCRIPT] + list(options)
                                 + ["--record", record], cwd=root, capture_output=True,
                                 text=True, encoding="utf-8", errors="replace", env=environment)
            lines = []
            if os.path.isfile(record):
                with open(record, encoding="utf-8") as handle:
                    lines = [json.loads(line) for line in handle if line.strip()]
            return run.returncode, run.stdout + run.stderr, lines, tuple(options)

    def errors(self, output, path):
        """(line, message) of every error the output reports in the file `path`."""
        pattern = re.compile(r"^%s:(\d+): error: (.*)$" % re.escape(path), re.MULTILINE)
        return [(int(line), message) for line, message in pattern.findall(output)]

    def assert_reported(self, result, path, line=None, fragments=(), record=FORM):
        """The run exits 1, reports an error in `path` — at `line` where given — whose message
        holds each fragment of `fragments` (a tuple standing for any of its members), and its
        record gives `record` a `fail`."""
        code, output, lines, _ = result
        self.assertEqual(code, 1, output)
        found = [message for at, message in self.errors(output, path)
                 if line is None or at == line]
        for fragment in fragments:
            alternatives = fragment if isinstance(fragment, tuple) else (fragment,)
            found = [message for message in found
                     if any(alternative in message for alternative in alternatives)]
        self.assertTrue(found, "no error in %s%s naming %r:\n%s"
                        % (path, "" if line is None else ":%d" % line, fragments, output))
        self.assertIn("fail", [entry.get("verdict") for entry in lines
                               if entry.get("invariant") == record], lines)

    def assert_clean(self, result):
        """The run exits 0, reports no error, and its record gives `pass` to what it records:
        the checks of form with no option, the checks of references with `--merge-onto`."""
        code, output, lines, options = result
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)
        self.assertNotIn("fail", [entry.get("verdict") for entry in lines
                                  if entry.get("invariant") in (FORM, REFERENCES)], lines)
        recorded = REFERENCES if "--merge-onto" in options else FORM
        self.assertIn("pass", [entry.get("verdict") for entry in lines
                               if entry.get("invariant") == recorded], lines)


class Fixtures(FormCheckTestCase):
    def test_the_valid_fixtures_pass(self):
        """The styleguide and the guidelines of a discipline with no template, as written above,
        hold no error: every other test breaks one thing in them. Were they to fail, no error
        another test sees could be told from one the fixture itself carries."""
        # invariant: guidelines-check-form/1
        # invariant: guidelines-check-carrier/1
        # invariant: guidelines-check-colour-pair/1
        # invariant: guidelines-check-reference-target/1
        # invariant: guidelines-check-stale-reference/1
        # invariant: guidelines-check-code-path/1
        files = {STYLEGUIDE_FILE: STYLEGUIDE, TESTING_FILE: TESTING}
        for options in ((), ("--merge-onto", "none")):
            with self.subTest(options=options):
                self.assert_clean(self.check(files, options))
        self.assert_clean(self.check(files, ("--merge-onto", "onto"),
                                     onto={"src/other.css": "a {}\n"}))


class Form(FormCheckTestCase):
    def test_a_missing_or_misplaced_header_line_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Applies to", replaced(STYLEGUIDE, "- **Applies to:** web\n", ""), ("Applies to",)),
            ("no Discipline", replaced(TESTING, "- **Discipline:** testing\n", ""), ("Discipline",)),
            ("header lines swapped",
             replaced(STYLEGUIDE, "- **Discipline:** styleguide\n- **Applies to:** web\n",
                      "- **Applies to:** web\n- **Discipline:** styleguide\n"),
             (("Discipline", "Applies to"),)),
        )
        for name, text, fragments in cases:
            path = TESTING_FILE if text.startswith("# Testing") else STYLEGUIDE_FILE
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path, fragments=fragments)

    def test_a_missing_or_misplaced_section_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no When to read", STYLEGUIDE_FILE,
             TITLE + HEADER + ROLES + RULES + EXAMPLES + WHERE, ("When to read",)),
            ("no Roles in a styleguide", STYLEGUIDE_FILE,
             TITLE + HEADER + WHEN + RULES + EXAMPLES + WHERE, ("Roles",)),
            ("no Examples", TESTING_FILE,
             replaced(TESTING, "## Examples\n\n### Branch names\n\nThe team names its branches "
                               "after their tasks.\n\n", ""), ("Examples",)),
            ("no Where in code", STYLEGUIDE_FILE,
             TITLE + HEADER + WHEN + ROLES + RULES + EXAMPLES.rstrip("\n") + "\n",
             ("Where in code",)),
            ("Roles before When to read", STYLEGUIDE_FILE,
             TITLE + HEADER + ROLES + WHEN + RULES + EXAMPLES + WHERE,
             (("Roles", "When to read"),)),
            ("Where in code before Examples", STYLEGUIDE_FILE,
             TITLE + HEADER + WHEN + ROLES + RULES + WHERE + "\n" + EXAMPLES.rstrip("\n") + "\n",
             (("Where in code", "Examples"),)),
        )
        for name, path, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path, fragments=fragments)

    def test_a_missing_or_misplaced_required_rule_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Visible focus", replaced(STYLEGUIDE, dropped("Visible focus"), ""),
             ("Visible focus",)),
            ("no Every background with its text", replaced(STYLEGUIDE, BACKGROUND, ""),
             ("Every background with its text",)),
            ("Contrast of every pair before Visible focus",
             with_line(with_line(STYLEGUIDE, 42, "### Visible focus", "### Contrast of every pair"),
                       46, "### Contrast of every pair", "### Visible focus"),
             (("Visible focus", "Contrast of every pair"),)),
        )
        for name, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                                     fragments=fragments)

    def test_a_missing_or_misplaced_rule_field_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Good in a styleguide", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 24, "- **Good:** the main action of a form uses `primary`.",
                       ""), ("Good",)),
            ("no Bad in guidelines with no template", TESTING_FILE,
             with_line(TESTING, 17, "- **Bad:** a test writes rows straight into the store of "
                                    "data.", ""), ("Bad",)),
            ("no Invariant field", TESTING_FILE,
             with_line(TESTING, 15, "- **Invariant:** none", ""), ("Invariant",)),
            ("Bad before Good", STYLEGUIDE_FILE,
             with_line(with_line(STYLEGUIDE, 24,
                                 "- **Good:** the main action of a form uses `primary`.",
                                 "- **Bad:** a warning uses `primary`."),
                       25, "- **Bad:** a warning uses `primary`.",
                       "- **Good:** the main action of a form uses `primary`."),
             (("Good", "Bad"),)),
        )
        for name, path, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path, fragments=fragments)

    def test_a_drop_with_any_text_but_a_departing_decision_is_reported(self):
        # invariant: guidelines-check-form/1
        line = "none — ABC-03@" + DEPARTURE_FP
        cases = (
            ("a reason in place of a decision", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 44, line, "none — the browser draws focus")),
            ("none alone", STYLEGUIDE_FILE, with_line(STYLEGUIDE, 44, line, "none")),
            ("a decision with no fingerprint", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 44, line, "none — ABC-03")),
            ("another marker", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 44, line, "n/a — ABC-03@" + DEPARTURE_FP)),
            ("text beside the departure", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 44, line, line + "\n\nThe browser draws focus.")),
            ("a dropped section with a reason", TESTING_FILE,
             replaced(TESTING, "Before writing a test of the web interface.",
                      "none — no one reads it first")),
        )
        for name, path, text in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path)

    def test_a_drop_naming_its_departing_decision_passes(self):
        """The control of the test above: a section and a rule dropped as the template has it."""
        # invariant: guidelines-check-form/1
        text = replaced(TESTING, "Before writing a test of the web interface.",
                        "none — ABC-03@" + DEPARTURE_FP)
        self.assert_clean(self.check({TESTING_FILE: text}, ()))

    def test_a_part_the_map_does_not_hold_is_reported(self):
        # invariant: guidelines-check-form/1
        self.assert_reported(
            self.check({STYLEGUIDE_FILE: with_line(STYLEGUIDE, 4, "- **Applies to:** web",
                                                   "- **Applies to:** web · mobile")}, ()),
            STYLEGUIDE_FILE, line=4, fragments=("mobile",))
        self.assert_reported(
            self.check({TESTING_FILE: replaced(TESTING, "- **Applies to:** web",
                                               "- **Applies to:** mobile")}, ()),
            TESTING_FILE, line=4, fragments=("mobile",))
        for path, text in (("guidelines/styleguide-mobile.md", STYLEGUIDE),
                           ("guidelines/testing-mobile.md", TESTING)):
            with self.subTest(path):
                self.assert_reported(self.check({path: text}, ()), path, fragments=("mobile",))

    def test_a_file_whose_name_and_discipline_disagree_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("guidelines/styleguide-web.md", TESTING),
            ("guidelines/web.md", TESTING),
            ("guidelines/look-web.md", STYLEGUIDE),
            ("guidelines/styleguide.md", STYLEGUIDE),
            ("guidelines/testing-web.md", STYLEGUIDE),
        )
        for path, text in cases:
            with self.subTest(path):
                self.assert_reported(self.check({path: text}, ()), path)

    def test_a_file_whose_name_follows_its_discipline_passes(self):
        """The control of the test above: the same texts under names that agree with them."""
        # invariant: guidelines-check-form/1
        for path, text in (("guidelines/testing.md", TESTING),
                           ("guidelines/testing-web.md", TESTING),
                           ("guidelines/styleguide-web.md", STYLEGUIDE)):
            with self.subTest(path):
                self.assert_clean(self.check({path: text}, ()))


class Carrier(FormCheckTestCase):
    def test_a_rule_naming_no_decision_is_reported(self):
        # invariant: guidelines-check-carrier/1
        cases = (
            ("a styleguide's rule", STYLEGUIDE_FILE, with_line(
                STYLEGUIDE, 31, "- **Decision:** ABC-01@" + ROLES_FP, "- **Decision:** none")),
            ("a styleguide's rule naming an invariant only", STYLEGUIDE_FILE, with_line(
                STYLEGUIDE, 31, "- **Decision:** ABC-01@" + ROLES_FP,
                "- **Decision:** background-pair@" + PAIR_FP)),
            ("a rule of guidelines with no template", TESTING_FILE, replaced(
                TESTING, "- **Decision:** ABC-05@" + FIXTURES_FP, "- **Decision:** none")),
        )
        for name, path, text in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path)

    def test_a_styleguide_rule_naming_no_invariant_is_reported(self):
        # invariant: guidelines-check-carrier/1
        further = ("### Spacing on a grid\n\n- **Decision:** ABC-02@" + MUTED_FP + "\n"
                   "- **Invariant:** none\n- **Good:** a card keeps the grid's gap.\n"
                   "- **Bad:** a card sets a gap of its own.\n\nKeep every gap on the grid.\n\n")
        cases = (
            ("a required rule", with_line(STYLEGUIDE, 32,
                                          "- **Invariant:** background-pair@" + PAIR_FP,
                                          "- **Invariant:** none")),
            ("a required rule naming a decision only", with_line(
                STYLEGUIDE, 32, "- **Invariant:** background-pair@" + PAIR_FP,
                "- **Invariant:** ABC-01@" + ROLES_FP)),
            ("a further rule of the product", replaced(STYLEGUIDE, "## Examples\n",
                                                       further + "## Examples\n")),
        )
        for name, text in cases:
            with self.subTest(name):
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE)

    def test_a_rule_naming_no_invariant_outside_a_styleguide_passes(self):
        """The control of the test above: TESTING's rule names `none` in *Invariant*."""
        # invariant: guidelines-check-carrier/1
        self.assertIn("- **Invariant:** none\n", TESTING)
        self.assert_clean(self.check({TESTING_FILE: TESTING}, ()))

    def test_a_decision_of_the_roles_the_meaning_rule_does_not_name_is_reported(self):
        # invariant: guidelines-check-carrier/1
        text = with_line(STYLEGUIDE, 22, "- **Decision:** ABC-01@%s · ABC-02@%s"
                         % (ROLES_FP, MUTED_FP), "- **Decision:** ABC-01@" + ROLES_FP)
        self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                             fragments=("ABC-02",))

    def test_a_decision_of_the_roles_passes_where_the_meaning_rule_is_dropped(self):
        """The control of the test above: the rule "Each role in its meaning" dropped by a
        decision leaves the table's decisions unnamed by it, and that is no error."""
        # invariant: guidelines-check-carrier/1
        text = replaced(STYLEGUIDE, EACH_ROLE, dropped("Each role in its meaning"))
        self.assert_clean(self.check({STYLEGUIDE_FILE: text}, ()))


class ColourPair(FormCheckTestCase):
    def test_a_background_without_a_text_role_is_reported(self):
        # invariant: guidelines-check-colour-pair/1
        row = ("| primary | background | this is the main action of the screen | primary-text | "
               "ABC-01@" + ROLES_FP + " |")
        for text_on_it in ("", "—", "muted", "primary", "ink"):
            with self.subTest(text_on_it=text_on_it):
                text = with_line(STYLEGUIDE, 14, row, row.replace(
                    "| primary-text |", "| %s |" % text_on_it if text_on_it else "|  |"))
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                                     line=14)


# Where a reference can stand: (where, line, the line as STYLEGUIDE holds it, the line with the
# reference `%s` in it).
PLACES = (
    ("a Decision field", 31, "- **Decision:** ABC-01@" + ROLES_FP,
     "- **Decision:** ABC-01@" + ROLES_FP + " · %s"),
    ("an Invariant field", 32, "- **Invariant:** background-pair@" + PAIR_FP,
     "- **Invariant:** background-pair@" + PAIR_FP + " · %s"),
    ("a row of Roles", 16, "| muted | other | this matters less than what is around it | — | "
     "ABC-02@" + MUTED_FP + " |",
     "| muted | other | this matters less than what is around it, as %s has it | — | "
     "ABC-02@" + MUTED_FP + " |"),
    ("a rule's prose", 36, "Write every background role with the text role that stands on it.",
     "Write every background role with the text role that stands on it, as %s has it."),
    ("inline code in a rule's prose", 36,
     "Write every background role with the text role that stands on it.",
     "Write every background role with the text role that stands on it, as `%s` has it."),
    ("an example", 70, "A mockup is a pattern to compare against; meanings come from this file.",
     "A mockup is a pattern to compare against; meanings come from %s."),
    ("a departure", 44, "none — ABC-03@" + DEPARTURE_FP, "none — %s"),
)


class ReferenceTarget(FormCheckTestCase):
    def test_a_reference_to_an_entry_not_in_force_is_reported_wherever_it_stands(self):
        # invariant: guidelines-check-reference-target/1
        targets = (
            ("a decision the log does not hold", "ABC-09@0123abcd"),
            ("a repealed decision", "ABC-04@" + FONT_FP),
            ("an invariant the file does not hold", "missing-pair@0123abcd"),
            ("a withdrawn invariant", "old-pair@0123abcd"),
        )
        for where, line, old, new in PLACES:
            for target, reference in targets:
                with self.subTest(where=where, target=target):
                    text = with_line(STYLEGUIDE, line, old, new % reference)
                    self.assert_reported(self.check({STYLEGUIDE_FILE: text}), STYLEGUIDE_FILE,
                                         line=line, fragments=(reference,), record=REFERENCES)

    def test_a_reference_whose_fingerprint_is_not_eight_hexadecimal_characters_is_reported(self):
        # invariant: guidelines-check-reference-target/1
        references = ("ABC-01@daa9", "ABC-01@DAA9CF8D", "ABC-01@daa9cf8d0", "ABC-01@zz",
                      "role-meaning@v2", "old-pair@x")
        for where, line, old, new in PLACES:
            for reference in references:
                with self.subTest(where=where, reference=reference):
                    text = with_line(STYLEGUIDE, line, old, new % reference)
                    self.assert_reported(self.check({STYLEGUIDE_FILE: text}), STYLEGUIDE_FILE,
                                         line=line, fragments=(reference,), record=REFERENCES)

    def test_a_versioned_package_name_or_a_bare_identifier_is_no_reference(self):
        """`react@18`, `tailwindcss@4` and `lucide-react@0` fit neither form of a reference, and
        an identifier with no `@` is a bare mention; none is reported."""
        # invariant: guidelines-check-reference-target/1
        line = "Write every background role with the text role that stands on it."
        for mention in ("`react@18`", "react@18", "`tailwindcss@4`", "lucide-react@0",
                        "ABC-01", "ABC-01/1", "role-meaning", "old-pair", "ABC-09"):
            with self.subTest(mention=mention):
                text = with_line(STYLEGUIDE, 36, line, line[:-1] + ", as %s has it." % mention)
                self.assert_clean(self.check({STYLEGUIDE_FILE: text}))

    def test_a_reference_in_fenced_code_is_ignored(self):
        # invariant: guidelines-check-reference-target/1
        # invariant: guidelines-check-stale-reference/1
        example = "A mockup is a pattern to compare against; meanings come from this file."
        for fence in ("```", "~~~"):
            with self.subTest(fence=fence):
                block = "\n".join([
                    example, "", fence + "text",
                    "ABC-09@0123abcd · ABC-04@%s · missing-pair@0123abcd · old-pair@x" % FONT_FP,
                    "ABC-01@%s · role-meaning@%s · left-pad@0123abcd" % (ROLES_STALE,
                                                                         ROLE_MEANING_STALE),
                    fence])
                text = with_line(STYLEGUIDE, 70, example, block)
                self.assert_clean(self.check({STYLEGUIDE_FILE: text}))


class StaleReference(FormCheckTestCase):
    def test_a_stale_reference_on_the_commit_checked_is_reported_wherever_it_stands(self):
        # invariant: guidelines-check-stale-reference/1
        cases = (
            ("a Decision field", 22, "- **Decision:** ABC-01@%s · ABC-02@%s" % (ROLES_FP, MUTED_FP),
             "- **Decision:** ABC-01@%s · ABC-02@%s" % (ROLES_STALE, MUTED_FP), "ABC-01",
             ROLES_FP),
            ("an Invariant field", 23, "- **Invariant:** role-meaning@" + ROLE_MEANING_FP,
             "- **Invariant:** role-meaning@" + ROLE_MEANING_STALE, "role-meaning",
             ROLE_MEANING_FP),
            ("a row of Roles", 14, "| primary | background | this is the main action of the "
             "screen | primary-text | ABC-01@" + ROLES_FP + " |",
             "| primary | background | this is the main action of the screen | primary-text | "
             "ABC-01@" + ROLES_STALE + " |", "ABC-01", ROLES_FP),
            ("a rule's prose", 27, "Use each role only in the meaning its decision gives.",
             "Use each role only in the meaning role-meaning@%s guards." % ROLE_MEANING_STALE,
             "role-meaning", ROLE_MEANING_FP),
            ("an example", 70,
             "A mockup is a pattern to compare against; meanings come from this file.",
             "A mockup is a pattern to compare against; meanings come from ABC-01@%s."
             % ROLES_STALE, "ABC-01", ROLES_FP),
            ("a departure", 44, "none — ABC-03@" + DEPARTURE_FP,
             "none — ABC-03@" + DEPARTURE_STALE, "ABC-03", DEPARTURE_FP),
        )
        for where, line, old, new, entry, current in cases:
            with self.subTest(where):
                text = with_line(STYLEGUIDE, line, old, new)
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}), STYLEGUIDE_FILE,
                                     line=line, fragments=(entry, current), record=REFERENCES)

    def test_a_reference_a_merge_leaves_stale_is_reported(self):
        """The commit merged onto rewords a decision, or an invariant, that the branch never
        touched: the references the branch carries are current on its own commit and stale in
        the foundation the merge leaves."""
        # invariant: guidelines-check-stale-reference/1
        cases = (
            ("a decision reworded on the commit merged onto",
             {"foundations/decisions.md": LOG_ONTO}, 22, "ABC-01", ROLES_REWORDED_FP),
            ("an invariant reworded on the commit merged onto",
             {"foundations/invariants.md": INVARIANTS_ONTO}, 23, "role-meaning",
             ROLE_MEANING_REWORDED_FP),
        )
        for name, onto, line, entry, current in cases:
            with self.subTest(name):
                self.assert_reported(
                    self.check({STYLEGUIDE_FILE: STYLEGUIDE}, ("--merge-onto", "onto"), onto=onto),
                    STYLEGUIDE_FILE, line=line, fragments=(entry, current), record=REFERENCES)

    def test_a_reference_a_merge_leaves_stale_is_current_on_the_commit_checked(self):
        """The control of the test above: the same branch, checked with no commit to merge onto,
        holds no error, so what the test above sees comes from the merge."""
        # invariant: guidelines-check-stale-reference/1
        for onto in ({"foundations/decisions.md": LOG_ONTO},
                     {"foundations/invariants.md": INVARIANTS_ONTO}):
            with self.subTest(onto=sorted(onto)):
                self.assert_clean(self.check({STYLEGUIDE_FILE: STYLEGUIDE}, onto=onto))


class CodePath(FormCheckTestCase):
    def test_a_path_outside_what_git_tracks_is_reported(self):
        # invariant: guidelines-check-code-path/1
        line = "- `src/tokens.css`"
        paths = ("../outside.md", "src/../src/tokens.css", "/etc/passwd", r"C:\x", "C:/x",
                 r"\\host\share\x", "//host/share/x", ":(glob)**", "http://host/x",
                 "src/missing.css", "src/draft.css")
        for path in paths:
            with self.subTest(path=path):
                text = with_line(STYLEGUIDE, 78, line, "- `%s`" % path)
                fragments = () if "\\" in path else (path,)
                self.assert_reported(
                    self.check({STYLEGUIDE_FILE: text}, (),
                               untracked={"src/draft.css": ":root {}\n"}),
                    STYLEGUIDE_FILE, line=78, fragments=fragments)

    def test_a_tracked_file_or_directory_passes(self):
        """The control of the test above: STYLEGUIDE names a tracked file and a directory whose
        files git tracks."""
        # invariant: guidelines-check-code-path/1
        self.assertIn("- `src/tokens.css`\n- `src/components`\n", STYLEGUIDE)
        self.assert_clean(self.check({STYLEGUIDE_FILE: STYLEGUIDE}, ()))


if __name__ == "__main__":
    unittest.main()
