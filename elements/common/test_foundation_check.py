"""Tests of the check of a foundation: identifiers, references and the files of the part map.

Each test builds a small product in a temporary git repository, breaks one thing in it, runs the
script as a product runs it and reads its exit code and report. The expected messages name the
entries and paths written out below, never values the script computes.

Run from the root of the-way: python -B gate/run_tests.py elements/common
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
THE_WAY = os.path.dirname(os.path.dirname(HERE))
SCRIPT = os.path.join(HERE, "foundation_check.py")

DECISIONS = """# Decision log

### ABC-01 — How is a game saved?

A game is saved to one file.

- **Scope:** core
- **Based on:** a save holds the whole state: clock-tick@0123abcd
- **Relations:** none
- **Verification:** level 1 — invariants: save-round-trip. Level 2 for the rest.
- **Origin:** none

*Rationale:* one file is easy to copy.
*Rejected:* none considered

### ABC-02 — Where does the clock run?

The clock runs in the core, ABC-01 aside.

- **Scope:** core, shell
- **Based on:** none
- **Relations:** derives from ABC-01@0123abcd
- **Verification:** level 1 — invariants: save-round-trip · clock-steady.
- **Origin:** none

*Rationale:* the core holds time.
*Rejected:* none considered
"""

INVARIANTS = """# Invariants

## save-round-trip

A saved game loads back unchanged.

- **Method:** test
- **Rests on:** clock-tick@0123abcd
- **Derives from:** ABC-01@0123abcd
- **Part:** core · shell
- **Violated:** no

## clock-steady

The clock never runs backwards.

- **Method:** review
- **Rests on:** none
- **Derives from:** ABC-02
- **Part:** every
- **Violated:** no

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| save-format | merged into the round trip | save-round-trip |
"""

FACTS = """# Environment facts

## clock-tick

The system clock ticks once a millisecond.

- **Source:** https://example.org/clock — "one tick a millisecond"; read 2026-10-01
"""

GLOSSARY = """# Glossary

## tick

A tick is one step of the game's clock.

- **Not:** none

## save

A save is the file that holds a game.

- **Not:** none
"""

PART_MAP = """# Part map

## core

The part answers for the rules of the game.

- **Files:** src/**
- **Depends on:** none
- **Failure modes:**
  - a save loses a field — high — detected by save-round-trip
- **Trust boundary:** none

## shell

The part answers for everything around the rules.

- **Files:** /README.md
  foundations/**
  tests/**
  guidelines/**
- **Depends on:** core
- **Trust boundary:** none

## Files left out on purpose

| File | Why |
|---|---|
| notes.txt | it binds nothing |

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| engine | split | core · shell |
"""

# A critical flow, an entry of the map's earlier form.
FLOW = """## saving-works

Someone saves a game and loads it back.

- **Parts:** core · shell
- **Invariant:** save-round-trip

"""

GUIDELINES = """# Coding guidelines — the game's code

- **Discipline:** coding
- **Applies to:** core

## Rules

### One save file

- **Decision:** ABC-01@0123abcd
- **Invariant:** save-round-trip@0123abcd · clock-steady
- **Good:** one file
- **Bad:** two files

Keep the save in one file; see clock-steady@89abcdef.
"""

FILES = {
    "foundations/decisions.md": DECISIONS,
    "foundations/invariants.md": INVARIANTS,
    "foundations/environment_facts.md": FACTS,
    "foundations/glossary.md": GLOSSARY,
    "foundations/part_map.md": PART_MAP,
    "guidelines/coding.md": GUIDELINES,
    "src/game.py": "# The rules of the game (ABC-01/1).\n",
    "tests/test_saving.py": ("def test_round_trip():\n"
                             "    # invariant: save-round-trip/1\n"
                             "    # fact: clock-tick/1\n"
                             "    assert True\n"),
    "README.md": "# The game\n\nSaves follow ABC-01 and ABC-02.\n",
    "notes.txt": "loose notes\n",
}


def git(root, *args):
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


class Product:
    """A product in a temporary git repository, every file added to git's index."""

    def __init__(self, test, files):
        self.directory = tempfile.TemporaryDirectory()
        test.addCleanup(self.directory.cleanup)
        self.root = self.directory.name
        git(self.root, "init", "-q")
        for path, text in files.items():
            if text is None:
                continue
            full = os.path.join(self.root, *path.split("/"))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "wb") as handle:
                handle.write(text if isinstance(text, bytes) else text.encode("utf-8"))
        git(self.root, "add", "-A")

    def on_branch(self, name):
        """Make `name` the branch the next commit goes on; works before the first commit too."""
        git(self.root, "symbolic-ref", "HEAD", "refs/heads/" + name)

    def write(self, path, text):
        """Write a file and add it to git's index."""
        full = os.path.join(self.root, *path.split("/"))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "wb") as handle:
            handle.write(text if isinstance(text, bytes) else text.encode("utf-8"))
        git(self.root, "add", "--", path)

    def commit(self):
        """Commit the index, the author given by options and no network anywhere."""
        git(self.root, "-c", "user.name=Test", "-c", "user.email=test@example.org", "-c",
            "commit.gpgsign=false", "commit", "-q", "--no-verify", "-m", "a commit")

    def check(self, *args, cwd=None):
        """(exit code, report) of the script run on the product."""
        result = subprocess.run([sys.executable, "-B", SCRIPT, *args],
                                cwd=cwd or self.root, capture_output=True, text=True,
                                encoding="utf-8")
        return result.returncode, result.stdout + result.stderr


class FoundationCheckTest(unittest.TestCase):

    def run_on(self, **changes):
        """Run the script on the good product with some files replaced, added or (None) left out."""
        return self.run_with((), **changes)

    def run_with(self, arguments, **changes):
        """The same, with the arguments given to the script."""
        files = dict(FILES)
        files.update({path.replace("__", "/").replace("_dot_", "."): text
                      for path, text in changes.items()})
        return Product(self, files).check(*arguments)

    def assertPasses(self, result):
        code, report = result
        self.assertEqual(code, 0, report)
        self.assertIn("0 errors", report)

    def assertFails(self, result, *messages):
        code, report = result
        self.assertEqual(code, 1, report)
        for message in messages:
            self.assertIn(message, report)

    def edit(self, text, old, new):
        self.assertIn(old, text)
        return text.replace(old, new, 1)

    # --- the good product, and how the script is run ------------------------------------------

    def test_good_product_passes(self):
        self.assertPasses(self.run_on())

    def test_root_given_as_argument(self):
        product = Product(self, FILES)
        self.assertPasses(product.check(product.root, cwd=HERE))

    def test_not_a_git_repository_cannot_run(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, "-B", SCRIPT, directory],
                                    capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_git_missing_cannot_run(self):
        product = Product(self, FILES)
        with tempfile.TemporaryDirectory() as empty:
            environment = {"PATH": empty, "SYSTEMROOT": os.environ.get("SYSTEMROOT", "")}
            result = subprocess.run([sys.executable, "-B", SCRIPT, product.root], env=environment,
                                    capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("git cannot run", result.stdout)

    def test_errors_counted(self):
        decisions = self.edit(DECISIONS, "- **Scope:** core\n", "- **Scope:** saves\n")
        readme = "# The game\n\nSee ABC-07.\n"
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions,
                                     README_dot_md=readme), "2 errors")

    # --- identifiers are unique ---------------------------------------------------------------

    def test_decision_number_twice(self):
        decisions = DECISIONS + "\n### ABC-02 — Where does the clock run again?\n\nText.\n"
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "`ABC-02` stands twice")

    def test_decision_version_is_the_earlier_form(self):
        decisions = DECISIONS.replace("### ABC-02 —", "### ABC-02/2 —")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:16: `ABC-02/2` stands in the earlier form",
                         "migrate_foundation.py", "1 error")

    def test_decision_version_twice(self):
        decisions = DECISIONS.replace("### ABC-01 —", "### ABC-01/1 —") + (
            "\n### ABC-01/1 — How is a game saved?\n\nTwo files.\n")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "`ABC-01/1` stands twice")

    def test_decision_number_with_and_without_version(self):
        decisions = DECISIONS + "\n### ABC-01 — How is a game saved?\n\nTwo files.\n"
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "`ABC-01` stands twice")

    def test_invariant_identifier_twice(self):
        invariants = self.edit(INVARIANTS, "## clock-steady\n", "## save-round-trip\n")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:", "`save-round-trip` stands twice")

    def test_fact_identifier_held_by_invariant(self):
        facts = self.edit(FACTS, "## clock-tick\n", "## clock-steady\n")
        invariants = INVARIANTS.replace("clock-tick@0123abcd", "none")
        decisions = DECISIONS.replace("clock-tick@0123abcd", "none")
        tests = FILES["tests/test_saving.py"].replace("    # fact: clock-tick/1\n", "")
        self.assertFails(self.run_on(foundations__environment_facts_dot_md=facts,
                                     foundations__invariants_dot_md=invariants,
                                     foundations__decisions_dot_md=decisions,
                                     tests__test_saving_dot_py=tests),
                         "foundations/environment_facts.md:", "`clock-steady` stands twice")

    def test_part_identifier_held_by_invariant(self):
        part_map = PART_MAP + ("\n## clock-steady\n\nSomeone watches the clock.\n\n"
                               "- **Parts:** core\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "foundations/part_map.md:", "`clock-steady` stands twice")

    def test_message_outside_ascii(self):
        glossary = GLOSSARY + "\n## żółw → tick\n\nOne.\n\n## żółw → tick\n\nTwo.\n"
        self.assertFails(self.run_on(foundations__glossary_dot_md=glossary),
                         "`żółw → tick` stands twice")

    def test_glossary_term_twice(self):
        glossary = GLOSSARY + "\n## tick\n\nA tick is a mark.\n"
        self.assertFails(self.run_on(foundations__glossary_dot_md=glossary),
                         "foundations/glossary.md:", "`tick` stands twice")

    # --- withdrawn identifiers are never used again -------------------------------------------

    def test_withdrawn_identifier_names_an_entry_again(self):
        invariants = self.edit(INVARIANTS, "## clock-steady\n", "## save-format\n")
        invariants = invariants.replace("save-round-trip · clock-steady", "save-round-trip")
        decisions = DECISIONS.replace("save-round-trip · clock-steady", "save-round-trip")
        guidelines = GUIDELINES.replace(" · clock-steady", "").replace(
            "; see clock-steady@89abcdef", "")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants,
                                     foundations__decisions_dot_md=decisions,
                                     guidelines__coding_dot_md=guidelines),
                         "`save-format` stands twice")

    def test_withdrawn_part_names_a_part_again(self):
        part_map = self.edit(PART_MAP, "## shell\n", "## engine\n")
        part_map = part_map.replace("core · shell\n- **Invariant", "core · engine\n- **Invariant")
        decisions = DECISIONS.replace("core, shell", "core, engine")
        invariants = INVARIANTS.replace("core · shell", "core · engine")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map,
                                     foundations__decisions_dot_md=decisions,
                                     foundations__invariants_dot_md=invariants),
                         "`engine` stands twice")

    def test_successor_that_is_no_entry(self):
        invariants = self.edit(INVARIANTS, "| save-round-trip |", "| save-all |")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:", "`save-all`")

    def test_successor_withdrawn_in_the_same_file_passes(self):
        invariants = self.edit(INVARIANTS, "| save-round-trip |", "| save-format |")
        self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_successor_none_passes(self):
        invariants = self.edit(INVARIANTS, "| save-round-trip |", "| none |")
        self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    # --- references to decisions --------------------------------------------------------------

    def test_decision_named_anywhere_that_does_not_exist(self):
        readme = "# The game\n\nSaves follow ABC-09.\n"
        self.assertFails(self.run_on(README_dot_md=readme), "README.md:3:", "`ABC-09`")

    def test_decision_named_with_fingerprint_or_version_that_does_not_exist(self):
        code = "# ABC-03@0123abcd and ABC-04/1\n"
        self.assertFails(self.run_on(src__game_dot_py=code), "src/game.py:1:", "`ABC-03`",
                         "`ABC-04`")

    def test_decision_relation_that_does_not_exist(self):
        decisions = self.edit(DECISIONS, "derives from ABC-01@0123abcd",
                              "derives from ABC-11@0123abcd")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "`ABC-11`")

    # A list of withdrawn decision numbers after the last entry of the log; line 25 is its row.
    WITHDRAWN_DECISION = ("\n## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n"
                          "|---|---|---|\n| ABC-03 | merged into ABC-02 | ABC-02 |\n")

    def test_withdrawn_decision_number_with_its_successor_passes(self):
        self.assertPasses(self.run_on(
            foundations__decisions_dot_md=DECISIONS + self.WITHDRAWN_DECISION))

    def test_withdrawn_decision_number_named_anywhere(self):
        self.assertFails(self.run_on(
            foundations__decisions_dot_md=DECISIONS + self.WITHDRAWN_DECISION,
            README_dot_md="# The game\n\nSee ABC-03.\n"),
            "README.md:3: `ABC-03` is withdrawn; name its successor", "1 error")

    def test_withdrawn_decision_number_names_an_entry_again(self):
        decisions = DECISIONS + self.WITHDRAWN_DECISION.replace("| ABC-03 |", "| ABC-02 |")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:33: `ABC-02` stands twice")

    def test_withdrawn_decision_number_twice(self):
        decisions = DECISIONS + self.WITHDRAWN_DECISION + "| ABC-03 | again | none |\n"
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:34: `ABC-03` stands twice")

    def test_withdrawn_decision_successor_that_is_no_decision(self):
        decisions = DECISIONS + self.WITHDRAWN_DECISION.replace("| ABC-02 |\n", "| ABC-09 |\n")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:33: withdrawn `ABC-03` names the successor "
                         "`ABC-09`, which this file does not hold")

    def test_withdrawn_decision_successor_none_passes(self):
        decisions = DECISIONS + self.WITHDRAWN_DECISION.replace("| ABC-02 |\n", "| none |\n")
        self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_decision_number_without_leading_zero_names_the_same_decision(self):
        self.assertPasses(self.run_on(README_dot_md="See ABC-1 and ABC-002.\n"))

    def test_other_prefix_is_no_reference(self):
        self.assertPasses(self.run_on(README_dot_md="Unlike XYZ-99 and abc-42.\n"))

    # A source outside the log an invariant's *Derives from* quotes, its ticket's key and its
    # passage holding numbers of the log's prefix that the log does not hold.
    TICKET = ("https://tracker.example.org/browse/ABC-45 § Acceptance criteria —\n"
              "  \"the clock never runs backwards, as ABC-46 asked\"; read 2026-10-21")

    def test_derives_from_quoted_source_is_no_reference(self):
        invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-02\n",
                               "- **Derives from:** ABC-02 · %s\n" % self.TICKET)
        self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_derives_from_source_quoted_in_typographic_marks_is_no_reference(self):
        ticket = self.TICKET.replace("\"the", "“the").replace("asked\"", "asked”")
        invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-02\n",
                               "- **Derives from:** ABC-02 · %s\n" % ticket)
        self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_derives_from_decision_beside_quoted_source_that_does_not_exist(self):
        invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-02\n",
                               "- **Derives from:** ABC-09 · %s\n" % self.TICKET)
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:19: `ABC-09` names no decision of the log",
                         "1 error")

    def test_derives_from_decision_after_quoted_source_on_next_line(self):
        invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-02\n",
                               "- **Derives from:** %s ·\n  ABC-09\n" % self.TICKET)
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:21: `ABC-09` names no decision of the log",
                         "1 error")

    def test_derives_from_text_quoting_nothing_is_read_for_decisions(self):
        invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-02\n",
                               "- **Derives from:** recovered from code — src/game.py, after "
                               "ABC-09\n")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:19: `ABC-09` names no decision of the log")

    # --- references to invariants -------------------------------------------------------------

    def test_verification_names_no_invariant(self):
        decisions = self.edit(DECISIONS, "invariants: save-round-trip. Level",
                              "invariants: save-whole. Level")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "`save-whole`")

    def test_verification_names_withdrawn_invariant(self):
        decisions = self.edit(DECISIONS, "invariants: save-round-trip · clock-steady",
                              "invariants: save-round-trip · save-format")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "`save-format`", "withdrawn")

    def test_test_cites_no_invariant(self):
        tests = self.edit(FILES["tests/test_saving.py"], "invariant: save-round-trip/1",
                          "invariant: save-trip/1")
        self.assertFails(self.run_on(tests__test_saving_dot_py=tests),
                         "tests/test_saving.py:2:", "`save-trip`")

    def test_test_cites_invariant_in_other_comment_forms(self):
        tests = "// invariant: save-round-trip\n// invariant: clock-steady/2\n"
        self.assertPasses(self.run_on(tests__saving_dot_test_dot_js=tests))

    def test_test_cites_withdrawn_invariant(self):
        tests = "// invariant: save-format\n"
        self.assertFails(self.run_on(tests__saving_dot_test_dot_js=tests),
                         "tests/saving.test.js:1:", "`save-format`", "withdrawn")

    def test_citation_of_more_than_one_word(self):
        tests = "# invariant: save-round-trip and more\n"
        self.assertFails(self.run_on(tests__test_more_dot_py=tests),
                         "tests/test_more.py:1:", "`invariant: save-round-trip and more`")

    def test_citation_of_nothing(self):
        self.assertFails(self.run_on(tests__test_more_dot_py="# invariant:\n"),
                         "tests/test_more.py:1:", "`invariant: `")

    def test_invariant_line_inside_a_string_is_no_citation(self):
        tests = 'TEXT = "# invariant: save-trip/1"\n'
        self.assertPasses(self.run_on(tests__test_text_dot_py=tests))

    def test_flow_names_no_invariant(self):
        part_map = self.edit(PART_MAP, "## Files left out on purpose\n", FLOW.replace(
            "- **Invariant:** save-round-trip", "- **Invariant:** save-trip") +
            "## Files left out on purpose\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "foundations/part_map.md:", "`save-trip`")

    def test_failure_mode_detected_by_on_next_line(self):
        part_map = self.edit(PART_MAP, "detected by save-round-trip", "detected by\n    save-trip")
        # the failure mode opens on line 10, so `save-trip` stands on line 11
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "foundations/part_map.md:11: `save-trip`")

    def test_failure_mode_detected_by_no_invariant(self):
        part_map = self.edit(PART_MAP, "detected by save-round-trip", "detected by save-trip")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "foundations/part_map.md:", "`save-trip`")

    def test_guidelines_name_no_invariant(self):
        guidelines = self.edit(GUIDELINES, "· clock-steady\n", "· clock-even\n")
        self.assertFails(self.run_on(guidelines__coding_dot_md=guidelines),
                         "guidelines/coding.md:", "`clock-even`")

    def test_guidelines_invariant_continued_on_next_line(self):
        guidelines = self.edit(GUIDELINES, " · clock-steady\n", " ·\n  clock-even\n")
        self.assertFails(self.run_on(guidelines__coding_dot_md=guidelines),
                         "guidelines/coding.md:12: `clock-even`")

    def test_guidelines_reference_with_fingerprint_to_no_invariant(self):
        guidelines = self.edit(GUIDELINES, "see clock-steady@89abcdef", "see clock-even@89abcdef")
        self.assertFails(self.run_on(guidelines__coding_dot_md=guidelines),
                         "guidelines/coding.md:", "`clock-even`")

    def test_guidelines_fenced_code_holds_no_reference(self):
        case = ("\n```good save-round-trip src/save.py\n"
                "# made-up@0123abcd\n- **Invariant:** made-up\n```\n")
        self.assertPasses(self.run_on(guidelines__coding_dot_md=GUIDELINES + case))

    def test_violated_list_names_no_invariant(self):
        violated = ("## Violated invariants\n\n| Identifier | Version |\n|---|---|\n"
                    "| clock-steady | 1 |\n| save-trip | 1 |\n")
        self.assertFails(self.run_on(foundations__violated_invariants_dot_md=violated),
                         "foundations/violated_invariants.md:6:", "`save-trip`")

    # --- references to parts ------------------------------------------------------------------

    def test_list_item_that_is_no_identifier(self):
        decisions = self.edit(DECISIONS, "- **Scope:** core, shell", "- **Scope:** core, Shell UI")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions), "`Shell UI`")

    def test_scope_names_no_part(self):
        decisions = self.edit(DECISIONS, "- **Scope:** core, shell", "- **Scope:** core, saves")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "`saves`")

    def test_scope_continued_on_next_line(self):
        decisions = self.edit(DECISIONS, "- **Scope:** core, shell", "- **Scope:** core,\n  saves")
        # *Scope* of ABC-02 opens on line 16, so `saves` stands on line 17
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:21: `saves`")

    def test_scope_naming_a_flow_names_no_part(self):
        decisions = self.edit(DECISIONS, "- **Scope:** core, shell", "- **Scope:** saving-works")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "`saving-works`")

    def test_invariant_part_names_no_part(self):
        invariants = self.edit(INVARIANTS, "- **Part:** core · shell", "- **Part:** core · ui")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:", "`ui`")

    def test_dependency_on_no_part(self):
        part_map = self.edit(PART_MAP, "- **Depends on:** core\n", "- **Depends on:** engine\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "foundations/part_map.md:", "`engine`", "withdrawn")

    def test_flow_names_no_part(self):
        part_map = self.edit(PART_MAP, "## Files left out on purpose\n", FLOW.replace(
            "- **Parts:** core · shell", "- **Parts:** core · ui") +
            "## Files left out on purpose\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map), "`ui`")

    def test_guidelines_apply_to_no_part(self):
        guidelines = self.edit(GUIDELINES, "- **Applies to:** core", "- **Applies to:** ui")
        self.assertFails(self.run_on(guidelines__coding_dot_md=guidelines),
                         "guidelines/coding.md:", "`ui`")

    # --- references to environment facts ------------------------------------------------------

    def test_rests_on_no_fact(self):
        invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                               "- **Rests on:** clock-tock@0123abcd")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:", "`clock-tock`")

    def test_rests_on_an_invariant_names_no_fact(self):
        invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                               "- **Rests on:** clock-steady")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "`clock-steady`")

    def test_rests_on_a_missing_fact_described_passes_whole(self):
        # a description is read as one: its commas and the words in it name no entry
        for value in ("TODO — the store of documents",
                      "TODO — the store of documents, once a task chooses it",
                      "TODO — clock-tock, the clock the game runs on · its source",
                      "`TODO — the store of documents, once a task chooses it`"):
            with self.subTest(value=value):
                invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                                       "- **Rests on:** " + value)
                self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_rests_on_a_missing_fact_described_over_two_lines_passes(self):
        invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                               "- **Rests on:** TODO — the store of documents,\n"
                               "  once a task chooses it")
        self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_rests_on_a_bare_todo_names_no_fact(self):
        for value in ("TODO", "`TODO`", "TODO —", "TODO — "):
            with self.subTest(value=value):
                invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                                       "- **Rests on:** " + value)
                self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                                 "foundations/invariants.md:8: *Rests on* reads `TODO` and names "
                                 "no fact: write `TODO — <the fact, with its source>`", "1 error")

    def test_rests_on_a_word_that_only_starts_with_todo_is_no_todo(self):
        invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                               "- **Rests on:** TODOs")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:8: `TODOs` is no identifier of a fact")

    def test_rests_on_none_and_a_fact_still_pass(self):
        invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                               "- **Rests on:** none")
        self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_based_on_a_missing_thing_described_passes_whole(self):
        # a description is read as one: its commas, ` · ` and the words in it name no entry
        for value in ("TODO — the source of the save format",
                      "TODO — the source of the save format, once the vendor answers",
                      "TODO — clock-tock, ABC-77 · its source",
                      "`TODO — the source of the save format, once the vendor answers`"):
            with self.subTest(value=value):
                decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                                      "- **Based on:** " + value + "\n")
                self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_based_on_a_missing_thing_described_over_two_lines_passes(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                              "- **Based on:** TODO — the source of the save format,\n"
                              "  once the vendor answers\n")
        self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_based_on_a_bare_todo_names_nothing_missing(self):
        for value in ("TODO", "`TODO`", "TODO —", "TODO — "):
            with self.subTest(value=value):
                decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                                      "- **Based on:** " + value + "\n")
                self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                                 "foundations/decisions.md:21: *Based on* reads `TODO` and says "
                                 "nothing of what is missing: write `TODO — <what is missing, "
                                 "with its source>`", "1 error")

    def test_based_on_a_word_that_only_starts_with_todo_is_read_as_before(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n", "- **Based on:** TODOs\n")
        self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_derives_from_a_missing_decision_described_passes_whole(self):
        for value in ("TODO — the decision on where saves live",
                      "TODO — the decision on where saves live, expected in the save task",
                      "TODO — ABC-77, expected next · or ABC-78",
                      "`TODO — the decision on where saves live, expected in the save task`"):
            with self.subTest(value=value):
                invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-01@0123abcd",
                                       "- **Derives from:** " + value)
                self.assertPasses(self.run_on(foundations__invariants_dot_md=invariants))

    def test_derives_from_a_bare_todo_names_no_decision(self):
        for value in ("TODO", "`TODO`", "TODO —", "TODO — "):
            with self.subTest(value=value):
                invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-01@0123abcd",
                                       "- **Derives from:** " + value)
                self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                                 "foundations/invariants.md:9: *Derives from* reads `TODO` and "
                                 "names no decision: write `TODO — <the decision, and where it is "
                                 "expected>`", "1 error")

    def test_derives_from_other_values_are_read_as_before(self):
        invariants = self.edit(INVARIANTS, "- **Derives from:** ABC-01@0123abcd",
                               "- **Derives from:** ABC-77")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:9: `ABC-77` names no decision of the log")

    def test_relations_and_origin_take_no_todo(self):
        for field, old in (("Relations", "- **Relations:** none\n"),
                           ("Origin", "- **Origin:** none\n")):
            for value in ("TODO", "TODO — the reasoning"):
                with self.subTest(field=field, value=value):
                    decisions = self.edit(DECISIONS, old, "- **%s:** %s\n" % (field, value))
                    self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                                     "*%s* does not take `%s`" % (field, value), "1 error")

    # --- a missing thing as the last item of a value that names known ones ----------------------

    def mixed_rests_on(self, value):
        return self.run_on(foundations__invariants_dot_md=self.edit(
            INVARIANTS, "- **Rests on:** clock-tick@0123abcd", "- **Rests on:** " + value))

    def mixed_derives_from(self, value):
        return self.run_on(foundations__invariants_dot_md=self.edit(
            INVARIANTS, "- **Derives from:** ABC-01@0123abcd", "- **Derives from:** " + value))

    def mixed_based_on(self, value):
        return self.run_on(foundations__decisions_dot_md=self.edit(
            DECISIONS, "- **Based on:** none\n", "- **Based on:** " + value + "\n"))

    def test_rests_on_a_known_fact_then_a_missing_one_described_passes(self):
        for value in ("clock-tick · TODO — a second fact, from the vendor",
                      "clock-tick · TODO — a second fact, from the vendor, read once",
                      "clock-tick · TODO — a second fact · from the vendor",
                      "clock-tick@0123abcd · TODO — a second fact"):
            with self.subTest(value=value):
                self.assertPasses(self.mixed_rests_on(value))

    def test_rests_on_a_known_fact_then_a_bare_todo_names_no_fact(self):
        for value in ("clock-tick · TODO", "clock-tick · `TODO`", "clock-tick · TODO —"):
            with self.subTest(value=value):
                self.assertFails(self.mixed_rests_on(value),
                                 "foundations/invariants.md:8: *Rests on* reads `TODO` and names "
                                 "no fact: write `TODO — <the fact, with its source>`", "1 error")

    def test_rests_on_a_known_fact_before_a_todo_is_still_checked(self):
        self.assertFails(self.mixed_rests_on("clock-tock · TODO — a second fact"),
                         "foundations/invariants.md:8: `clock-tock` names no fact", "1 error")

    def test_rests_on_a_todo_first_reads_the_rest_as_its_description(self):
        self.assertPasses(self.mixed_rests_on("TODO — a second fact · clock-tock, fact-x"))

    def test_rests_on_a_known_fact_after_a_description_is_part_of_it(self):
        self.assertPasses(self.mixed_rests_on("clock-tick · TODO — a second fact · clock-tock"))

    def test_derives_from_a_known_decision_then_a_missing_one_described_passes(self):
        for value in ("ABC-01 · TODO — the decision on saves, expected in the save task",
                      "ABC-01@0123abcd · TODO — the decision on saves · or its successor",
                      "ABC-01 · TODO — ABC-77, expected next"):
            with self.subTest(value=value):
                self.assertPasses(self.mixed_derives_from(value))

    def test_derives_from_a_known_decision_then_a_bare_todo_names_no_decision(self):
        for value in ("ABC-01 · TODO", "ABC-01 · `TODO`", "ABC-01 · TODO —"):
            with self.subTest(value=value):
                self.assertFails(self.mixed_derives_from(value),
                                 "foundations/invariants.md:9: *Derives from* reads `TODO` and "
                                 "names no decision: write `TODO — <the decision, and where it is "
                                 "expected>`", "1 error")

    def test_derives_from_a_decision_before_a_todo_is_still_checked(self):
        self.assertFails(self.mixed_derives_from("ABC-77 · TODO — the decision on saves"),
                         "foundations/invariants.md:9: `ABC-77` names no decision of the log",
                         "1 error")

    def test_derives_from_a_quoted_source_then_a_missing_decision_passes(self):
        self.assertPasses(self.mixed_derives_from(
            "https://example.org/clock § Ticks — \"one tick · a millisecond\"; read 2026-10-01 · "
            "TODO — the decision on ticks, once the clock task is made"))

    def test_based_on_a_known_fact_then_a_missing_source_described_passes(self):
        for value in ("clock-tick · TODO — the source of the save format, from the vendor",
                      "clock-tick · TODO — the source of the save format · from the vendor",
                      "clock-tick · TODO — the source named by ABC-77, once it is written",
                      "https://example.org/clock — \"one tick, a millisecond\"; read 2026-10-01 · "
                      "TODO — the source of the save format, once the vendor answers"):
            with self.subTest(value=value):
                self.assertPasses(self.mixed_based_on(value))

    def test_based_on_a_known_fact_then_a_bare_todo_says_nothing_is_missing(self):
        for value in ("clock-tick · TODO", "clock-tick · `TODO`", "clock-tick · TODO —"):
            with self.subTest(value=value):
                self.assertFails(self.mixed_based_on(value),
                                 "foundations/decisions.md:21: *Based on* reads `TODO` and says "
                                 "nothing of what is missing: write `TODO — <what is missing, "
                                 "with its source>`", "1 error")

    def test_based_on_a_fact_before_a_todo_is_still_checked(self):
        self.assertFails(self.mixed_based_on("clock-tock · TODO — the source of the save format"),
                         "foundations/decisions.md:21: `clock-tock` names no fact", "1 error")

    def test_based_on_a_todo_inside_a_quoted_source_is_no_todo_item(self):
        for value in ("https://example.org/clock — \"one · TODO tick\"; read 2026-10-01 · "
                      "clock-tick",
                      "https://example.org/clock — \"a TODO\"; read 2026-10-01",
                      "clock-tick · https://example.org/clock — \"one · TODO\"; read 2026-10-01"):
            with self.subTest(value=value):
                self.assertPasses(self.mixed_based_on(value))

    def test_based_on_a_quoted_source_with_a_todo_inside_still_has_its_references_checked(self):
        self.assertFails(self.mixed_based_on(
            "https://example.org/clock — \"one · TODO tick\"; read 2026-10-01 · clock-tock"),
            "foundations/decisions.md:21: `clock-tock` names no fact", "1 error")

    def test_based_on_no_fact(self):
        decisions = self.edit(DECISIONS, "state: clock-tick@0123abcd", "state: clock-tock@0123abcd")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "`clock-tock`")

    def test_based_on_names_by_identifier_alone_no_fact(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                              "- **Based on:** clock-tock · https://example.org/clock, § Ticks — "
                              "\"the clock, steady, ticks\"; read 2026-10-01\n")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:21: `clock-tock` names no fact", "1 error")

    def test_based_on_fact_by_identifier_alone_and_quoted_source_pass(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                              "- **Based on:** clock-tick · https://example.org/clock, § Ticks — "
                              "\"the clock, steady, ticks\"; read 2026-10-01\n")
        self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_based_on_fact_by_identifier_alone_on_next_line(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                              "- **Based on:** https://example.org/clock — \"one tick\"; read "
                              "2026-10-01 ·\n  clock-tock\n")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:22: `clock-tock` names no fact")

    def test_fact_in_the_form_without_version_is_named_by_identifier_alone(self):
        # the form the environment facts template gives: a heading with no version, the sentence
        # and *Source*
        facts = FACTS
        invariants = self.edit(INVARIANTS, "- **Rests on:** clock-tick@0123abcd",
                               "- **Rests on:** clock-tick")
        decisions = self.edit(DECISIONS, "- **Based on:** none\n", "- **Based on:** clock-tick\n")
        self.assertPasses(self.run_on(foundations__environment_facts_dot_md=facts,
                                      foundations__invariants_dot_md=invariants,
                                      foundations__decisions_dot_md=decisions))

    def test_fact_line_is_no_citation(self):
        tests = self.edit(FILES["tests/test_saving.py"], "fact: clock-tick/1", "fact: clock-tock/1")
        self.assertPasses(self.run_on(tests__test_saving_dot_py=tests))

    # --- every field of an entry ----------------------------------------------------------------

    def test_decision_lacks_a_field(self):
        decisions = self.edit(DECISIONS, "- **Origin:** none\n", "")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "the entry lacks *Origin*")

    def test_decision_lacks_its_rationale(self):
        decisions = self.edit(DECISIONS, "*Rationale:* the core holds time.\n", "")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "the entry lacks *Rationale*")

    def test_invariant_lacks_violated(self):
        invariants = self.edit(INVARIANTS, "- **Violated:** no\n", "")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "foundations/invariants.md:", "the entry lacks *Violated*")

    def test_invariant_method_of_the_earlier_form(self):
        invariants = self.edit(INVARIANTS, "- **Method:** review\n", "- **Method:** `TODO`\n")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "*Method* does not take ``TODO``")

    def test_invariant_violated_takes_yes_or_no(self):
        invariants = self.edit(INVARIANTS, "- **Violated:** no\n", "- **Violated:** maybe\n")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants),
                         "*Violated* does not take `maybe`")

    def test_fact_source_takes_no_todo(self):
        facts = FACTS.replace(
            '- **Source:** https://example.org/clock — "one tick a millisecond"; read 2026-10-01',
            "- **Source:** TODO")
        self.assertFails(self.run_on(foundations__environment_facts_dot_md=facts),
                         "*Source* does not take `TODO`")

    def test_part_lacks_its_trust_boundary(self):
        part_map = self.edit(PART_MAP, "- **Depends on:** core\n- **Trust boundary:** none\n",
                             "- **Depends on:** core\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "foundations/part_map.md:", "the entry lacks *Trust boundary*")

    def test_surface_names_who_relies_on_it(self):
        surface = "## save-promise\n\nA save of one release loads in the next.\n\n"
        good = self.edit(PART_MAP, "## Files left out on purpose\n", surface +
                         "- **Relied on by:** the players' saves\n\n## Files left out on purpose\n")
        self.assertPasses(self.run_on(foundations__part_map_dot_md=good))
        bad = good.replace("- **Relied on by:** the players' saves", "- **Relied on by:** none")
        self.assertFails(self.run_on(foundations__part_map_dot_md=bad),
                         "*Relied on by* does not take `none`")

    def test_map_entry_neither_part_nor_surface(self):
        part_map = self.edit(PART_MAP, "## Files left out on purpose\n",
                             "## save-promise\n\nA save loads.\n\n## Files left out on purpose\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "`save-promise` is neither a part")

    def test_glossary_entry_lacks_not(self):
        glossary = self.edit(GLOSSARY, "A save is the file that holds a game.\n\n- **Not:** none\n",
                             "A save is the file that holds a game.\n")
        self.assertFails(self.run_on(foundations__glossary_dot_md=glossary),
                         "foundations/glossary.md:", "the entry lacks *Not*")

    def test_entries_of_the_earlier_form_are_errors(self):
        invariants = self.edit(INVARIANTS, "## clock-steady\n", "## clock-steady/1\n")
        facts = self.edit(FACTS, "## clock-tick\n", "## clock-tick/1\n")
        part_map = self.edit(PART_MAP, "- **Depends on:** core\n",
                             "- **Depends on:** core\n- **Criticality:** high\n")
        self.assertFails(self.run_on(foundations__invariants_dot_md=invariants,
                                     foundations__environment_facts_dot_md=facts,
                                     foundations__part_map_dot_md=part_map),
                         "foundations/invariants.md:13: `clock-steady/1` stands in the earlier form",
                         "foundations/environment_facts.md:3: `clock-tick/1` stands in the earlier",
                         "foundations/part_map.md:13: `shell` stands in the earlier form",
                         "3 errors")

    def test_flow_is_the_earlier_form(self):
        part_map = self.edit(PART_MAP, "## Files left out on purpose\n",
                             FLOW + "## Files left out on purpose\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "`saving-works` stands in the earlier form", "1 error")

    def test_part_and_scope_take_parts_only(self):
        for field, old in (("Part", "- **Part:** every\n"), ("Scope", "- **Scope:** core\n")):
            for word in ("none", "TODO"):
                with self.subTest(field=field, word=word):
                    new = "- **%s:** %s\n" % (field, word)
                    if field == "Part":
                        result = self.run_on(foundations__invariants_dot_md=self.edit(
                            INVARIANTS, old, new))
                    else:
                        result = self.run_on(foundations__decisions_dot_md=self.edit(
                            DECISIONS, old, new))
                    self.assertFails(result, "*%s* does not take `%s`" % (field, word))

    def test_pattern_of_the_map_matching_no_file(self):
        for field, old, new in (
                ("Files", "  tests/**\n", "  tests/**\n  docs/**\n"),
                ("Trust boundary", "- **Depends on:** core\n- **Trust boundary:** none\n",
                 "- **Depends on:** core\n- **Trust boundary:** tests/net/*.py\n")):
            with self.subTest(field=field):
                part_map = self.edit(PART_MAP, old, new)
                self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                                 "foundations/part_map.md:", "in the *%s* of `shell` matches no "
                                 "file git tracks" % field, "1 error")

    # --- a decision's Based on quoting a source --------------------------------------------------

    def test_number_in_a_source_based_on_quotes_is_no_reference(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n",
                              '- **Based on:** https://example.org/log § 2 — "as ABC-07 says"; '
                              "read 2026-10-01\n")
        self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_number_in_based_on_outside_a_quotation_is_a_reference(self):
        decisions = self.edit(DECISIONS, "- **Based on:** none\n", "- **Based on:** ABC-07\n")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "`ABC-07` names no decision of the log")

    # --- every file git tracks belongs to one part --------------------------------------------

    def test_file_no_part_claims(self):
        self.assertFails(self.run_on(docs__guide_dot_md="A guide.\n"),
                         "docs/guide.md", "no part")

    def test_file_two_parts_claim(self):
        part_map = self.edit(PART_MAP, "- **Files:** src/**\n", "- **Files:** src/**\n  tests/**\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "tests/test_saving.py", "`core`", "`shell`")

    def test_root_anchored_pattern_claims_only_the_root_file(self):
        self.assertFails(self.run_on(src__README_dot_md="Inner.\n", docs__README_dot_md="Docs.\n"),
                         "docs/README.md")

    def test_file_left_out_on_purpose_and_claimed(self):
        part_map = self.edit(PART_MAP, "  guidelines/**\n", "  guidelines/**\n  notes.txt\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "notes.txt", "left out on purpose")

    def test_file_left_out_on_purpose_needs_no_part(self):
        part_map = self.edit(PART_MAP, "| notes.txt |", "| `notes.txt` |")
        self.assertPasses(self.run_on(foundations__part_map_dot_md=part_map))

    def test_pattern_letter_case_counts(self):
        part_map = self.edit(PART_MAP, "- **Files:** src/**\n", "- **Files:** SRC/**\n")
        self.assertFails(self.run_on(foundations__part_map_dot_md=part_map),
                         "src/game.py", "no part")

    # --- an invariant that reads `test` is cited by a test ------------------------------------

    # In the good product `save-round-trip` reads `test` and tests/test_saving.py cites it;
    # `clock-steady` reads `review` and nothing cites it. These tests move the citation.
    UNCITED = "foundations/invariants.md:7:"

    def other_citation(self):
        """tests/test_saving.py citing the review invariant instead of the test one."""
        return self.edit(FILES["tests/test_saving.py"], "save-round-trip/1", "clock-steady")

    def test_invariant_reading_test_that_no_test_cites_is_reported(self):
        self.assertFails(self.run_on(tests__test_saving_dot_py=self.other_citation()),
                         self.UNCITED, "`save-round-trip`", "1 error")

    def test_invariant_reading_test_cited_in_another_file_passes(self):
        tests = "// invariant: save-round-trip\n"
        self.assertPasses(self.run_on(tests__test_saving_dot_py=self.other_citation(),
                                      tests__saving_dot_test_dot_js=tests))

    def test_citation_in_markdown_does_not_count(self):
        readme = "# The game\n\nSaves follow ABC-01.\n\n<!-- invariant: save-round-trip -->\n"
        self.assertFails(self.run_on(tests__test_saving_dot_py=self.other_citation(),
                                     README_dot_md=readme),
                         self.UNCITED, "`save-round-trip`")

    def test_citation_in_a_file_git_does_not_track_does_not_count(self):
        files = dict(FILES, **{"tests/test_saving.py": self.other_citation()})
        product = Product(self, files)
        with open(os.path.join(product.root, "tests", "untracked.js"), "w", encoding="utf-8",
                  newline="\n") as handle:
            handle.write("// invariant: save-round-trip\n")
        self.assertFails(product.check(), self.UNCITED, "`save-round-trip`")

    def test_skip_switch_skips_the_report_of_an_uncited_test_invariant(self):
        self.assertPasses(self.run_with(("--skip-test-citations",),
                                        tests__test_saving_dot_py=self.other_citation()))

    def test_skip_switch_before_or_after_the_root(self):
        files = dict(FILES, **{"tests/test_saving.py": self.other_citation()})
        product = Product(self, files)
        self.assertPasses(product.check("--skip-test-citations", product.root, cwd=HERE))
        self.assertPasses(product.check(product.root, "--skip-test-citations", cwd=HERE))

    def test_skip_switch_skips_no_other_error(self):
        readme = "# The game\n\nSee ABC-07.\n"
        self.assertFails(self.run_with(("--skip-test-citations",),
                                       tests__test_saving_dot_py=self.other_citation(),
                                       README_dot_md=readme),
                         "`ABC-07` names no decision of the log", "1 error")

    def test_unknown_switch_cannot_run(self):
        code, report = self.run_with(("--skip-everything",))
        self.assertEqual(code, 2, report)
        self.assertIn("usage: foundation_check.py", report)

    # --- the line `decision:` of a test that holds a sentence of a decision -------------------

    def decision_test(self, *lines, **changes):
        """The good product with a test file holding each line as a comment, under one test."""
        text = "def test_saved():\n" + "".join("    # %s\n" % line for line in lines) + \
            "    assert True\n"
        return self.run_on(tests__test_decision_dot_py=text, **changes)

    def test_decision_line_quoting_a_sentence_passes(self):
        # decision: WAY-12 "A test that holds a sentence of a decision carries beside it a line"
        self.assertPasses(self.decision_test('decision: ABC-01 "A game is saved to one file"'))

    def test_decision_line_quoting_no_sentence_fails(self):
        self.assertFails(self.decision_test('decision: ABC-01 "A game is stored in a cloud"'),
                         "tests/test_decision.py:2: the quotation stands in no binding sentence "
                         "of `ABC-01`", "1 error")

    def test_decision_line_quoting_only_rationale_fails(self):
        self.assertFails(self.decision_test('decision: ABC-01 "one file is easy to copy"'),
                         "tests/test_decision.py:2: the quotation stands in no binding sentence "
                         "of `ABC-01`", "1 error")

    def test_decision_line_quoting_inside_a_sentence_fails(self):
        self.assertFails(self.decision_test('decision: ABC-01 "game is saved to one file"'),
                         "tests/test_decision.py:2: the quotation does not begin a sentence of "
                         "`ABC-01`", "1 error")

    def test_decision_line_quotation_wrapped_over_two_lines_passes(self):
        decisions = self.edit(DECISIONS, "A game is saved to one file.",
                              "A game is saved\nto one file.")
        self.assertPasses(self.decision_test('decision: ABC-01 "A game is saved to one file"',
                                             foundations__decisions_dot_md=decisions))

    def test_decision_line_quoting_fewer_than_three_words_fails(self):
        self.assertFails(self.decision_test('decision: ABC-01 "A game"'),
                         "tests/test_decision.py:2: the quotation has fewer than three words",
                         "1 error")

    def test_decision_line_without_quotation_fails(self):
        self.assertFails(self.decision_test("decision: ABC-01"),
                         "tests/test_decision.py:2: `decision:` gives no quotation of the sentence",
                         "1 error")

    def test_decision_line_with_text_after_quotation_fails(self):
        self.assertFails(self.decision_test('decision: ABC-01 "A game is saved to one file" more'),
                         "tests/test_decision.py:2: `decision:` has text after the quotation",
                         "1 error")

    def test_decision_line_naming_no_decision_fails(self):
        self.assertFails(self.decision_test('decision: ABC-07 "A game is saved to one file"'),
                         "tests/test_decision.py:2: `ABC-07` names no decision of the log",
                         "1 error")

    def test_decision_line_naming_a_withdrawn_decision_fails(self):
        self.assertFails(self.decision_test(
            'decision: ABC-03 "A game is saved to one file"',
            foundations__decisions_dot_md=DECISIONS + self.WITHDRAWN_DECISION),
            "tests/test_decision.py:2: `ABC-03` is withdrawn; name its successor", "1 error")

    def test_decision_line_without_number_fails(self):
        self.assertFails(self.decision_test('decision: "A game is saved to one file"'),
                         "tests/test_decision.py:2: `decision:` gives no decision number as the "
                         "log writes it", "1 error")

    def test_decision_line_number_with_a_suffix_fails(self):
        self.assertFails(self.decision_test('decision: ABC-01/1 "A game is saved to one file"'),
                         "tests/test_decision.py:2: `decision:` gives no decision number as the "
                         "log writes it", "1 error")

    def test_decision_line_in_markdown_counts_for_nothing(self):
        readme = ("# The game\n\nSaves follow ABC-01 and ABC-02.\n\n"
                  '<!-- decision: "stands nowhere" -->\n')
        self.assertPasses(self.run_on(README_dot_md=readme))

    def test_decision_line_in_untracked_file_counts_for_nothing(self):
        product = Product(self, FILES)
        with open(os.path.join(product.root, "tests", "untracked.js"), "w", encoding="utf-8",
                  newline="\n") as handle:
            handle.write('// decision: ABC-01 "stands nowhere in the entry"\n')
        self.assertPasses(product.check())

    # --- the commit the branch left, and the line written where it is not known ---------------

    UNKNOWN_BASE = ("foundations/decisions.md: listed: the commit the branch left the main branch "
                    "from is not known, so nothing was compared with it")
    NO_DECISIONS_AT_BASE = ("foundations/decisions.md: listed: the commit the branch left the main "
                            "branch from holds no readable foundations/decisions.md, so nothing "
                            "of it was compared")
    NO_INVARIANTS_AT_BASE = ("foundations/invariants.md: listed: the commit the branch left the "
                             "main branch from holds no readable foundations/invariants.md, so "
                             "nothing of it was compared")

    def lines(self, result, code=0):
        """The lines of a report whose exit code is `code`."""
        self.assertEqual(result[0], code, result[1])
        return result[1].splitlines()

    def committed(self, branch, **changes):
        """The good product with some files replaced or (None) left out, committed on a branch."""
        files = dict(FILES)
        files.update({path.replace("__", "/").replace("_dot_", "."): text
                      for path, text in changes.items()})
        product = Product(self, files)
        product.on_branch(branch)
        product.commit()
        return product

    def test_no_commit_and_a_log_with_a_decision_lists_the_unknown_base(self):
        self.assertEqual(self.lines(self.run_on()), [self.UNKNOWN_BASE, "0 errors"])

    def test_listed_line_stands_after_the_errors_and_before_the_count(self):
        readme = "# The game\n\nSee ABC-07.\n"
        self.assertEqual(self.lines(self.run_on(README_dot_md=readme), 1),
                         ["README.md:3: `ABC-07` names no decision of the log",
                          self.UNKNOWN_BASE, "1 error"])

    def test_no_commit_and_an_empty_log_writes_no_such_line(self):
        empty = self.run_on(foundations__decisions_dot_md="# Decision log\n")[1]
        self.assertNotIn("listed:", empty)
        self.assertIn("listed:", self.run_on()[1])

    def test_commits_on_no_main_branch_leave_the_base_unknown(self):
        product = self.committed("topic")
        self.assertEqual(self.lines(product.check()), [self.UNKNOWN_BASE, "0 errors"])

    def test_base_on_main(self):
        product = self.committed("topic")
        self.assertEqual(self.lines(product.check()), [self.UNKNOWN_BASE, "0 errors"])
        git(product.root, "branch", "main")
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_base_on_master_where_there_is_no_main(self):
        product = self.committed("topic")
        self.assertEqual(self.lines(product.check()), [self.UNKNOWN_BASE, "0 errors"])
        git(product.root, "branch", "master")
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_remote_head_naming_another_branch_is_preferred_over_main(self):
        product = self.committed("main")
        # `work` shares no history with `main`, so `main` gives no base for it.
        git(product.root, "checkout", "-q", "--orphan", "work")
        product.write("notes.txt", "other notes\n")  # the same root commit would be `main` itself
        product.commit()
        self.assertEqual(self.lines(product.check()), [self.UNKNOWN_BASE, "0 errors"])
        git(product.root, "update-ref", "refs/remotes/origin/trunk", "HEAD")
        git(product.root, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/trunk")
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_remote_head_naming_a_branch_that_does_not_exist_leaves_main(self):
        product = self.committed("topic")
        git(product.root, "branch", "main")
        git(product.root, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/gone")
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_base_lacking_the_decisions_is_unknown_for_them(self):
        product = self.committed("main", foundations__decisions_dot_md=None)
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/decisions.md", DECISIONS)
        product.commit()
        self.assertEqual(self.lines(product.check()), [self.NO_DECISIONS_AT_BASE, "0 errors"])

    def test_base_lacking_the_invariants_is_unknown_for_them(self):
        product = self.committed("main", foundations__invariants_dot_md=None)
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/invariants.md", INVARIANTS)
        product.commit()
        self.assertEqual(self.lines(product.check()), [self.NO_INVARIANTS_AT_BASE, "0 errors"])

    def test_base_lacking_both_files_writes_a_line_for_each(self):
        product = self.committed("main", foundations__decisions_dot_md=None,
                                 foundations__invariants_dot_md=None)
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/decisions.md", DECISIONS)
        product.write("foundations/invariants.md", INVARIANTS)
        product.commit()
        self.assertEqual(self.lines(product.check()),
                         [self.NO_DECISIONS_AT_BASE, self.NO_INVARIANTS_AT_BASE, "0 errors"])

    def test_base_holding_a_file_git_cannot_read_as_text_is_no_exit_2(self):
        product = self.committed("main", foundations__decisions_dot_md=b"\xff\xfe not text\n")
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/decisions.md", DECISIONS)
        product.commit()
        self.assertEqual(self.lines(product.check()), [self.NO_DECISIONS_AT_BASE, "0 errors"])

    def test_base_lacking_the_files_and_an_empty_log_writes_no_line(self):
        product = self.committed("main", foundations__decisions_dot_md=None,
                                 foundations__invariants_dot_md=None)
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/decisions.md", "# Decision log\n")
        product.write("foundations/invariants.md", INVARIANTS)
        product.commit()
        self.assertNotIn("listed:", product.check()[1])

    # --- a decision that nothing holds --------------------------------------------------------

    # ABC-03 stands at line 29 of the log of the good product once it is added to its end.
    NOT_HELD = "foundations/decisions.md:29: `ABC-03`"
    LISTED = "foundations/decisions.md:29: listed: `ABC-03`"
    NOTHING = "- **Verification:** an agent compares the change with the decision."
    BY_INVARIANT = "- **Verification:** invariants: clock-steady."
    BY_PAIR = ("- **Verification:** an agent compares the change with the decision:\n"
               "  - complies: a save sits in one folder;\n"
               "  - violates: a save is sent to a server.")
    STORE_TEST = ("def test_store():\n"
                  "    # decision: ABC-03 \"A save is stored in one folder\"\n"
                  "    assert True\n")

    def decision(self, verification, sentence="A save is stored in one folder.",
                 rationale="a folder is known.", heading="ABC-03"):
        """An entry ABC-03 of the log, its *Verification* given whole."""
        return ("### %s — Where is a save stored?\n\n%s\n\n- **Scope:** core\n"
                "- **Based on:** none\n- **Relations:** none\n%s\n- **Origin:** none\n\n"
                "*Rationale:* %s\n*Rejected:* a cloud\n"
                % (heading, sentence, verification, rationale))

    def on_topic(self, decisions, base=DECISIONS, **files):
        """The good product with the log `base` committed on `main`, then the log `decisions` and
        the files written, not committed, on a branch `topic` that left it."""
        product = self.committed("main", foundations__decisions_dot_md=base)
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/decisions.md", decisions)
        for path, text in files.items():
            product.write(path.replace("__", "/").replace("_dot_", "."), text)
        return product

    def test_new_decision_that_nothing_holds_is_an_error(self):
        # decision: WAY-12 "The check of the foundation reports as an error"
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.NOTHING))
        self.assertFails(product.check(), self.NOT_HELD, "1 error")
        self.assertNotIn("listed: `ABC-03`", product.check()[1])

    def test_new_decision_held_by_an_invariant_passes(self):
        # decision: WAY-12 "A decision is held when its"
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.BY_INVARIANT))
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_new_decision_held_by_a_pair_of_examples_passes(self):
        # decision: WAY-12 "A decision is held when its"
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.BY_PAIR))
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_new_decision_held_by_a_line_decision_passes(self):
        # decision: WAY-12 "A decision is held when its"
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.NOTHING),
                                tests__test_store_dot_py=self.STORE_TEST)
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_new_decision_held_by_a_stale_line_decision_is_reported_once(self):
        stale = self.STORE_TEST.replace("one folder", "two folders")
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.NOTHING),
                                tests__test_store_dot_py=stale)
        self.assertEqual(self.lines(product.check(), 1),
                         ["tests/test_store.py:2: the quotation stands in no binding sentence of "
                          "`ABC-03`", "1 error"])

    def test_new_decision_with_only_one_half_of_a_pair_is_not_held(self):
        half = "- **Verification:** an agent compares the change with the decision:\n" \
               "  - complies: a save sits in one folder."
        product = self.on_topic(DECISIONS + "\n" + self.decision(half))
        self.assertFails(product.check(), self.NOT_HELD, "1 error")

    def test_new_decision_naming_no_invariant_after_invariants_is_not_held(self):
        product = self.on_topic(DECISIONS + "\n" + self.decision("- **Verification:** "
                                                                "invariants: none."))
        self.assertFails(product.check(), self.NOT_HELD, "1 error")

    def test_line_decision_in_a_markdown_file_holds_nothing(self):
        notes = "# The game\n\nSaves follow ABC-01.\n\n" \
                "<!-- decision: ABC-03 \"A save is stored in one folder\" -->\n"
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.NOTHING),
                                README_dot_md=notes)
        self.assertFails(product.check(), self.NOT_HELD, "1 error")

    def test_decision_whose_binding_sentence_changed_and_none_held_is_an_error(self):
        # decision: WAY-12 "The check of the foundation reports as an error"
        base = DECISIONS + "\n" + self.decision(self.NOTHING)
        product = self.on_topic(DECISIONS + "\n" + self.decision(
            self.NOTHING, sentence="A save is stored in two folders."), base=base)
        self.assertFails(product.check(), self.NOT_HELD, "1 error")

    def test_decision_whose_binding_sentence_changed_and_held_passes(self):
        base = DECISIONS + "\n" + self.decision(self.NOTHING)
        product = self.on_topic(DECISIONS + "\n" + self.decision(
            self.BY_PAIR, sentence="A save is stored in two folders."), base=base)
        self.assertEqual(self.lines(product.check()), ["0 errors"])

    def test_decision_with_only_its_rationale_changed_is_listed(self):
        # decision: WAY-12 "Any other decision that nothing holds stands"
        base = DECISIONS + "\n" + self.decision(self.NOTHING)
        product = self.on_topic(DECISIONS + "\n" + self.decision(
            self.NOTHING, rationale="a folder is easy to find."), base=base)
        code, report = product.check()
        self.assertEqual(code, 0, report)
        self.assertIn(self.LISTED, report)
        self.assertIn("0 errors", report)

    def test_decision_with_only_its_spacing_changed_is_listed(self):
        base = DECISIONS + "\n" + self.decision(self.NOTHING)
        product = self.on_topic(DECISIONS + "\n" + self.decision(
            self.NOTHING, sentence="A save   is stored\nin one  folder."), base=base)
        code, report = product.check()
        self.assertEqual(code, 0, report)
        self.assertIn(self.LISTED, report)

    def test_old_decision_that_nothing_holds_is_listed_after_the_errors(self):
        # decision: WAY-12 "Any other decision that nothing holds stands"
        base = DECISIONS + "\n" + self.decision(self.NOTHING)
        product = self.on_topic(base + "\n" + self.decision(self.NOTHING, heading="ABC-04"),
                                base=base)
        lines = self.lines(product.check(), 1)
        self.assertEqual(len(lines), 3, lines)
        self.assertTrue(lines[0].startswith("foundations/decisions.md:42: `ABC-04`"), lines)
        self.assertTrue(lines[1].startswith(self.LISTED), lines)
        self.assertEqual(lines[2], "1 error")

    def test_decision_that_nothing_holds_is_listed_where_the_base_is_unknown(self):
        code, report = self.run_on(foundations__decisions_dot_md=DECISIONS + "\n" +
                                   self.decision(self.NOTHING))
        self.assertEqual(code, 0, report)
        self.assertIn(self.LISTED, report)

    def test_decision_that_nothing_holds_is_listed_where_the_base_lacks_the_log(self):
        product = self.committed("main", foundations__decisions_dot_md=None)
        git(product.root, "checkout", "-q", "-b", "topic")
        product.write("foundations/decisions.md", DECISIONS + "\n" + self.decision(self.NOTHING))
        code, report = product.check()
        self.assertEqual(code, 0, report)
        self.assertIn(self.LISTED, report)

    def test_entry_lacking_its_verification_is_left_to_the_check_of_fields(self):
        entry = self.decision(self.NOTHING).replace(self.NOTHING + "\n", "")
        product = self.on_topic(DECISIONS + "\n" + entry)
        self.assertEqual(self.lines(product.check(), 1),
                         ["foundations/decisions.md:29: the entry lacks *Verification*",
                          "1 error"])

    def test_entry_of_the_earlier_form_is_left_to_the_check_of_fields(self):
        entry = self.decision(self.NOTHING, heading="ABC-03/1")
        product = self.on_topic(DECISIONS + "\n" + entry)
        code, report = product.check()
        self.assertEqual(code, 1, report)
        self.assertIn("`ABC-03/1` stands in the earlier form", report)
        self.assertIn("1 error", report)
        self.assertNotIn("nothing holds", report)

    def test_skip_switch_skips_nothing_of_the_decisions_nothing_holds(self):
        product = self.on_topic(DECISIONS + "\n" + self.decision(self.NOTHING))
        self.assertFails(product.check("--skip-test-citations"), self.NOT_HELD, "1 error")

    # --- the-way's own foundation -------------------------------------------------------------

    def test_the_way_foundation_passes(self):
        result = subprocess.run([sys.executable, "-B", SCRIPT, THE_WAY], capture_output=True,
                                text=True, encoding="utf-8")
        # invariant: map-reference-target
        # invariant: test-method-citation
        self.assertPasses((result.returncode, result.stdout + result.stderr))


if __name__ == "__main__":
    unittest.main()
