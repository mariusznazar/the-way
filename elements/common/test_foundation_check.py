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

### ABC-01/1 — How is a game saved?

A game is saved to one file.

- **Scope:** core
- **Based on:** a save holds the whole state: clock-tick@0123abcd
- **Relations:** none
- **Verification:** level 1 — invariants: save-round-trip. Level 2 for the rest.

### ABC-02 — Where does the clock run?

The clock runs in the core, ABC-01 aside.

- **Scope:** core, shell
- **Based on:** none
- **Relations:** derives from ABC-01@0123abcd
- **Verification:** level 1 — invariants: save-round-trip · clock-steady.
"""

INVARIANTS = """# Invariants

## save-round-trip/1

A saved game loads back unchanged.

- **Method:** `python -B -m unittest tests/test_saving.py`
- **Rests on:** clock-tick@0123abcd
- **Derives from:** ABC-01@0123abcd
- **Part:** core · shell

## clock-steady

The clock never runs backwards.

- **Method:** review
- **Rests on:** none
- **Derives from:** ABC-02
- **Part:** every

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| save-format | merged into the round trip | save-round-trip |
"""

FACTS = """# Environment facts

## clock-tick/1

The system clock ticks once a millisecond.

- **Source:** https://example.org/clock — "one tick a millisecond"; read 2026-10-01
"""

GLOSSARY = """# Glossary

## tick

A tick is one step of the game's clock.

## save

A save is the file that holds a game.
"""

PART_MAP = """# Part map

## core

The part answers for the rules of the game.

- **Files:** src/**
- **Depends on:** none
- **Failure modes:**
  - a save loses a field — high — detected by save-round-trip

## shell

The part answers for everything around the rules.

- **Files:** /README.md
  foundations/**
  tests/**
  guidelines/**
- **Depends on:** core

## saving-works

Someone saves a game and loads it back.

- **Parts:** core · shell
- **Invariant:** save-round-trip

## Files left out on purpose

| File | Why |
|---|---|
| notes.txt | it binds nothing |

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| engine | split | core · shell |
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
            with open(full, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        git(self.root, "add", "-A")

    def check(self, *args, cwd=None):
        """(exit code, report) of the script run on the product."""
        result = subprocess.run([sys.executable, "-B", SCRIPT, *args],
                                cwd=cwd or self.root, capture_output=True, text=True,
                                encoding="utf-8")
        return result.returncode, result.stdout + result.stderr


class FoundationCheckTest(unittest.TestCase):

    def run_on(self, **changes):
        """Run the script on the good product with some files replaced, added or (None) left out."""
        files = dict(FILES)
        files.update({path.replace("__", "/").replace("_dot_", "."): text
                      for path, text in changes.items()})
        return Product(self, files).check()

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

    def test_decision_versions_of_one_number_pass(self):
        decisions = DECISIONS + "\n### ABC-01/2 — How is a game saved?\n\nTwo files.\n"
        self.assertPasses(self.run_on(foundations__decisions_dot_md=decisions))

    def test_decision_version_twice(self):
        decisions = DECISIONS + "\n### ABC-01/1 — How is a game saved?\n\nTwo files.\n"
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
        facts = self.edit(FACTS, "## clock-tick/1\n", "## clock-steady/1\n")
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

    def test_decision_number_without_leading_zero_names_the_same_decision(self):
        self.assertPasses(self.run_on(README_dot_md="See ABC-1 and ABC-002.\n"))

    def test_other_prefix_is_no_reference(self):
        self.assertPasses(self.run_on(README_dot_md="Unlike XYZ-99 and abc-42.\n"))

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
        self.assertFails(self.run_on(tests__test_more_dot_py="# fact:\n"),
                         "tests/test_more.py:1:", "`fact: `")

    def test_invariant_line_inside_a_string_is_no_citation(self):
        tests = 'TEXT = "# invariant: save-trip/1"\n'
        self.assertPasses(self.run_on(tests__test_text_dot_py=tests))

    def test_flow_names_no_invariant(self):
        part_map = self.edit(PART_MAP, "- **Invariant:** save-round-trip",
                             "- **Invariant:** save-trip")
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
                         "foundations/decisions.md:17: `saves`")

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
        part_map = self.edit(PART_MAP, "- **Parts:** core · shell", "- **Parts:** core · ui")
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

    def test_based_on_no_fact(self):
        decisions = self.edit(DECISIONS, "state: clock-tick@0123abcd", "state: clock-tock@0123abcd")
        self.assertFails(self.run_on(foundations__decisions_dot_md=decisions),
                         "foundations/decisions.md:", "`clock-tock`")

    def test_test_cites_no_fact(self):
        tests = self.edit(FILES["tests/test_saving.py"], "fact: clock-tick/1", "fact: clock-tock/1")
        self.assertFails(self.run_on(tests__test_saving_dot_py=tests),
                         "tests/test_saving.py:3:", "`clock-tock`")

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

    # --- the-way's own foundation -------------------------------------------------------------

    def test_the_way_foundation_passes(self):
        result = subprocess.run([sys.executable, "-B", SCRIPT, THE_WAY], capture_output=True,
                                text=True, encoding="utf-8")
        self.assertPasses((result.returncode, result.stdout + result.stderr))


if __name__ == "__main__":
    unittest.main()
