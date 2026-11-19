"""Tests of the index of a product's decision log: the decisions it selects, written to a file.

Each test builds a small product in a temporary directory, its log written in the form the test
needs, runs the script as a product runs it and reads the file it writes, the exit code and the
message on stderr. The expected texts are written out below, never computed by the script's code.

Run from the root of the-way: python -B gate/run_tests.py elements/common
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "decision_index.py")

# A log of two topical sections and a section of withdrawn identifiers, as the log of a product
# that has been divided into sections holds it.
TWO_SECTIONS = """# Decision log

The decisions of the game.

## Saving

How a game is saved and what a save holds.

### GAME-01 — How is a game saved?

A game is saved to one file.

A save holds the whole state of the game.

- **Scope:** core, persistence
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a save writes `game.sav`;
  - violates: a save writes two files.
- **Origin:** none

*Rationale:* one file is easy to copy.
*Rejected:* a folder of files.

### GAME-02 — How is a save loaded?

A save is read back in one step.

- **Scope:** persistence
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a load reads `game.sav`;
  - violates: a load reads two files.
- **Origin:** none

*Rationale:* one read.
*Rejected:* a read per part.

## Play

How a level is played and won.

### GAME-03 — How is a level won?

A level is won when its goal is reached.

- **Scope:** core,
  levels
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a level ends at its goal;
  - violates: a level ends at a timer.
- **Origin:** none

*Rationale:* goals are visible to the player.
*Rejected:* timers.

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| GAME-00 | old | GAME-01 |
"""

# A log without topical sections; the Scope lines are the ones the part selection tests read.
NO_SECTIONS = """# Decision log

### GAME-01 — How is a game saved?

A game is saved to one file.

- **Scope:** core, persistence
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a save writes `game.sav`;
  - violates: a save writes two files.
- **Origin:** none

*Rationale:* one file is easy to copy.
*Rejected:* a folder of files.

### GAME-02 — How is a level scored?

A level is scored by its own rule.

- **Scope:** core-engine
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a score is set by the level;
  - violates: a score is set by the engine.
- **Origin:** none

*Rationale:* levels differ.
*Rejected:* one score rule.

### GAME-03 — How is a save written in parts?

A save is written in parts, one file each.

- **Scope:** persistence,
  core
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a part is one file;
  - violates: a part is two files.
- **Origin:** none

*Rationale:* files are small.
*Rejected:* one large file.

### GAME-04 — How is a sound played?

A sound plays once per event.

- **Scope:** levels · persistence
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a sound plays once;
  - violates: a sound plays twice.
- **Origin:** none

*Rationale:* repeats annoy.
*Rejected:* repeats.
"""


def read_text(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


class DecisionIndexTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = os.path.join(self.tmp.name, "product")
        os.makedirs(os.path.join(self.root, "foundations"))
        self.out = os.path.join(self.tmp.name, "index.md")

    def tearDown(self):
        self.tmp.cleanup()

    def write_log(self, text, bom=False, crlf=False):
        data = text.replace("\n", "\r\n") if crlf else text
        raw = data.encode("utf-8")
        if bom:
            raw = b"\xef\xbb\xbf" + raw
        with open(os.path.join(self.root, "foundations", "decisions.md"), "wb") as handle:
            handle.write(raw)

    def run_index(self, args, cwd=None):
        return subprocess.run(
            [sys.executable, "-B", SCRIPT] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def index(self, *switches):
        return self.run_index(list(switches) + ["--output", self.out, self.root])

    def assert_error(self, result, *names):
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertTrue(result.stderr.startswith("Error: "), result.stderr)
        for name in names:
            self.assertIn(name, result.stderr)
        self.assertFalse(os.path.exists(self.out), "a file was written for an error")

    def test_section_lists_its_decisions_in_full(self):
        self.write_log(TWO_SECTIONS)
        result = self.index("--section", "Saving")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(os.path.isfile(self.out), "no file written")
        text = read_text(self.out)
        self.assertIn("Listed in full: 2. Listed by heading alone: 0.", text)
        self.assertIn("### GAME-01 — How is a game saved?", text)
        self.assertIn("A game is saved to one file.", text)
        self.assertIn("A save holds the whole state of the game.", text)
        self.assertIn("- **Scope:** core, persistence", text)
        self.assertIn("### GAME-02 — How is a save loaded?", text)
        self.assertNotIn("GAME-03", text)

    def test_part_selects_decisions_whose_scope_names_the_part_as_a_whole_item(self):
        self.write_log(NO_SECTIONS)
        result = self.index("--part", "core")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = read_text(self.out)
        self.assertIn("Listed in full: 2. Listed by heading alone: 0.", text)
        self.assertIn("### GAME-01 — How is a game saved?", text)
        self.assertIn("### GAME-03 — How is a save written in parts?", text)
        self.assertNotIn("GAME-02", text)
        self.assertNotIn("GAME-04", text)
        result = self.index("--part", "persistence")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = read_text(self.out)
        self.assertIn("Listed in full: 3. Listed by heading alone: 0.", text)
        self.assertIn("### GAME-04 — How is a sound played?", text)
        self.assertNotIn("GAME-02", text)

    def test_a_part_that_no_scope_names_is_named_in_the_index(self):
        # "core-engin" is a misspelled part ("core-engine" is named) and "sound" a part no decision
        # of this log names yet: the index still lists the two decisions "core" selects and names
        # those two parts, and only those, as unnamed.
        self.write_log(NO_SECTIONS)
        result = self.index("--part", "core", "--part", "core-engin", "--part", "sound")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = read_text(self.out)
        self.assertIn(
            "Listed in full: 2. Listed by heading alone: 0.\n"
            "Parts that no Scope names: core-engin, sound.\n",
            text,
        )
        result = self.index("--part", "core")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("Parts that no Scope names", read_text(self.out))

    def test_section_and_part_list_outside_decisions_by_heading_after_the_others(self):
        self.write_log(TWO_SECTIONS)
        result = self.index("--section", "Saving", "--part", "levels")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = read_text(self.out)
        self.assertIn("Listed in full: 2. Listed by heading alone: 1.", text)
        self.assertIn("- GAME-03 — How is a level won?", text)
        self.assertNotIn("A level is won when its goal is reached.", text)
        self.assertLess(text.index("### GAME-02"), text.index("- GAME-03 — How is a level won?"))

    def test_decision_switch_adds_a_decision_by_its_number(self):
        self.write_log(TWO_SECTIONS)
        result = self.index("--decision", "GAME-03")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = read_text(self.out)
        self.assertIn("Listed in full: 1. Listed by heading alone: 0.", text)
        self.assertIn("A level is won when its goal is reached.", text)
        self.assertNotIn("GAME-01", text)

    def test_sections_lists_each_section_with_its_sentence_and_entries(self):
        self.write_log(TWO_SECTIONS)
        result = self.index("--sections")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = read_text(self.out)
        self.assertIn("Sections: 2.", text)
        self.assertIn(
            "## Saving\n\nHow a game is saved and what a save holds.\n\nEntries: 2.", text
        )
        self.assertIn("## Play\n\nHow a level is played and won.\n\nEntries: 1.", text)
        self.assertNotIn("Withdrawn", text)

    def test_log_without_sections_has_no_section_to_select(self):
        self.write_log(NO_SECTIONS)
        result = self.index("--sections")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Sections: 0.", read_text(self.out))
        os.remove(self.out)
        result = self.index("--section", "Saving")
        self.assert_error(result, "Saving")

    def test_byte_order_mark_and_crlf_line_endings_are_read(self):
        self.write_log(TWO_SECTIONS, bom=True, crlf=True)
        result = self.index("--section", "Saving")
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(self.out, "rb") as handle:
            raw = handle.read()
        self.assertNotIn(b"\r", raw)
        self.assertIn("A game is saved to one file.".encode("utf-8"), raw)

    def test_root_defaults_to_the_working_directory(self):
        self.write_log(NO_SECTIONS)
        result = self.run_index(["--part", "core", "--output", self.out], cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Listed in full: 2.", read_text(self.out))
        os.remove(self.out)
        result = self.run_index(
            ["--part", "core", "--output", self.out, self.root], cwd=self.tmp.name
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Listed in full: 2.", read_text(self.out))

    def test_missing_log_is_an_error_naming_the_file(self):
        result = self.index("--part", "core")
        self.assert_error(result, "foundations/decisions.md")

    def test_no_switch_is_an_error(self):
        self.write_log(TWO_SECTIONS)
        result = self.index()
        self.assert_error(result, "--part")

    def test_unknown_section_is_an_error_and_so_is_withdrawn_identifiers(self):
        self.write_log(TWO_SECTIONS)
        self.assert_error(self.index("--section", "Nope"), "Nope")
        self.assert_error(self.index("--section", "Withdrawn identifiers"), "Withdrawn identifiers")

    def test_unknown_decision_number_is_an_error(self):
        self.write_log(TWO_SECTIONS)
        self.assert_error(self.index("--decision", "GAME-99"), "GAME-99")

    def test_decision_without_scope_is_an_error_naming_the_entry_and_the_field(self):
        broken = TWO_SECTIONS.replace("- **Scope:** persistence\n", "", 1)
        self.assertEqual(broken.count("- **Scope:** persistence\n"), 0)
        self.write_log(broken)
        result = self.index("--section", "Saving")
        self.assert_error(result, "foundations/decisions.md", "GAME-02", "Scope")

    def test_heading_of_the_wrong_form_is_an_error_naming_the_file_and_the_line(self):
        broken = TWO_SECTIONS.replace(
            "### GAME-02 — How is a save loaded?", "### GAME-02 How is a save loaded?", 1
        )
        self.assertNotEqual(broken, TWO_SECTIONS)
        self.write_log(broken)
        result = self.index("--section", "Saving")
        self.assert_error(result, "foundations/decisions.md:", "GAME-02")

    def test_section_without_sentence_is_an_error_naming_the_section(self):
        broken = TWO_SECTIONS.replace(
            "## Play\n\nHow a level is played and won.\n\n", "## Play\n\n", 1
        )
        self.assertNotEqual(broken, TWO_SECTIONS)
        self.write_log(broken)
        result = self.index("--sections")
        self.assert_error(result, "foundations/decisions.md", "Play")


if __name__ == "__main__":
    unittest.main()
