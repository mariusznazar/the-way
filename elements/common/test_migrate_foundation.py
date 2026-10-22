"""Tests of the migration of a foundation from the earlier form of the-way to the current one.

Each test builds a small product in a temporary git repository, its foundation in the earlier form,
runs the script as a product runs it and reads the files, the exit code and the report. The
expected texts are written out below, never computed by the script's own code.

Run from the root of the-way: python -B gate/run_tests.py elements/common
"""

import codecs
import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "migrate_foundation.py")

DECISIONS = """# Decision log

The decisions of the game.

### ABC-01/1 — How is a game saved?

A game is saved to one file.

- **Change:** new decision
- **Scope:** core
- **Based on:** clock-tick@0123abcd
- **Relations:** none
- **Verification:** level 1 — invariants: save-round-trip@89abcdef. Level 2 for the name — an
  agent compares the change with the decision:
  - complies: a save writes `game.sav`;
  - violates: a save writes two files.
- **Review when:** the game saves to a server · check by: 2027-01-01
- **Origin:** none
- **Approved by:** Ann, 2026-09-01

*Rationale:* one file is easy to copy.
*Rejected:* none considered

### ABC-02/1 — Where does the clock run?

The clock runs in the shell.

- **Change:** new decision
- **Scope:** shell
- **Based on:** none
- **Relations:** derives from ABC-01@0123abcd
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the shell ticks;
  - violates: the core ticks.
- **Review when:** none
- **Origin:** none
- **Approved by:** Ann, 2026-09-01

*Rationale:* the shell owns time.
*Rejected:* none considered

### ABC-02 · review 2026-10-01

- **Result:** condition met, decision kept — the shell still ticks
- **Next check:** none
- **Checked by:** Ann

### ABC-04/1 — Who approves a release?

A human approves each release.

- **Change:** new decision
- **Scope:** core
- **Based on:** observation of the release page on 2026-10-01 using `curl`
- **Relations:** none
- **Verification:** level 3 — the human at the merge assesses the release.
- **Review when:** none
- **Origin:** inherited — searched: README.md; found: README.md
- **Approved by:** Ann, 2026-09-01

*Rationale:* unknown
*Rejected:* none considered

### ABC-02/2 — Where does the clock run?

The clock runs in the core.

- **Change:** new wording
- **Scope:** core
- **Based on:** none
- **Relations:** derives from ABC-01@0123abcd
- **Verification:** level 2 — an agent compares the change with the decision:
  - complies: the core ticks;
  - violates: the shell ticks.
- **Review when:** none
- **Origin:** none
- **Approved by:** Ann, 2026-10-02

*Rationale for change:* the shell lost its timer.
*Rejected:* the shell — it has no timer
"""

DECISIONS_AFTER = """# Decision log

The decisions of the game.

### ABC-01 — How is a game saved?

A game is saved to one file.

- **Scope:** core
- **Based on:** clock-tick
- **Relations:** none
- **Verification:** invariants: save-round-trip. For the name, an agent compares the change with the
  decision:
  - complies: a save writes `game.sav`;
  - violates: a save writes two files.
- **Origin:** none

*Rationale:* one file is easy to copy.
*Rejected:* none considered

### ABC-02 — Where does the clock run?

The clock runs in the core.

- **Scope:** core
- **Based on:** none
- **Relations:** derives from ABC-01
- **Verification:** an agent compares the change with the decision:
  - complies: the core ticks;
  - violates: the shell ticks.
- **Origin:** none

*Rationale:* the shell lost its timer.
*Rejected:* the shell — it has no timer

### ABC-04 — Who approves a release?

A human approves each release.

- **Scope:** core
- **Based on:** observation of the release page on 2026-10-01 using `curl`
- **Relations:** none
- **Verification:** level 3 — the human at the merge assesses the release.
- **Origin:** inherited — searched: README.md; found: README.md

*Rationale:* unknown
*Rejected:* none considered
"""

INVARIANTS = """# Invariants

What the game keeps true.

## save-round-trip/1

A saved game loads back unchanged.

- **Method:** `python -B -m unittest tests/test_saving.py`
- **Rests on:** clock-tick@0123abcd
- **Derives from:** ABC-01@0123abcd
- **Part:** core · shell
- **Correction:** none

## clock-steady/1

The clock never runs backwards.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** ABC-02@0123abcd
- **Part:** every
- **Correction:** none

## save-name/1

A save is named after its player.

- **Method:** docs/save_review.md
- **Rests on:** none
- **Derives from:** none
- **Part:** core
- **Correction:** none

## save-load/1

A saved game loads in the next release.

- **Method:** tests/test_saving.py
- **Rests on:** none
- **Derives from:** ABC-01@0123abcd
- **Part:** core
- **Correction:** none

## save-size/1

A save stays under a megabyte.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** none
- **Part:** core
- **Correction:** none

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| save-format | merged into the round trip | save-round-trip |

## Quarantined invariants

| Identifier | Version | Until |
|---|---|---|

## Recovered invariants

| Identifier | Version | Searched | Found |
|---|---|---|---|
| save-name | 1 | searched: src/save.py | found: src/save.py, its name; GAME-7: "named after the player" |
| save-size | 1 | searched: GAME-9 | found: GAME-9, its description |
"""

INVARIANTS_AFTER = """# Invariants

What the game keeps true.

## save-round-trip

A saved game loads back unchanged.

- **Method:** test
- **Rests on:** clock-tick
- **Derives from:** ABC-01
- **Part:** core · shell
- **Violated:** no

## clock-steady

The clock never runs backwards.

- **Method:** review
- **Rests on:** none
- **Derives from:** ABC-02
- **Part:** every
- **Violated:** yes

## save-name

A save is named after its player.

- **Method:** docs/save_review.md
- **Rests on:** none
- **Derives from:** recovered from code — src/save.py, its name
- **Part:** core
- **Violated:** no

## save-load

A saved game loads in the next release.

- **Method:** test
- **Rests on:** none
- **Derives from:** ABC-01
- **Part:** core
- **Violated:** no

## save-size

A save stays under a megabyte.

- **Method:** review
- **Rests on:** none
- **Derives from:** none
- **Part:** core
- **Violated:** no

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| save-format | merged into the round trip | save-round-trip |
"""

FACTS = """# Environment facts

## clock-tick/1

The system clock ticks once a millisecond.

- **Holds for:** ClockOS 3
- **Source:** https://example.org/clock § Ticks — "one tick a millisecond" · "never backwards";
  read 2026-10-01
- **Method:** `TODO`

## disk-space/1

The disk keeps a megabyte for saves.

- **Holds for:** ClockOS 3
- **Source:** observed: `df -h` on ClockOS 3; run 2026-10-01
- **Method:** `TODO`
"""

FACTS_AFTER = """# Environment facts

## clock-tick

The system clock ticks once a millisecond.

- **Source:** https://example.org/clock § Ticks — "one tick a millisecond" · "never backwards";
  read 2026-10-01

## disk-space

The disk keeps a megabyte for saves.

- **Source:** observed: `df -h` on ClockOS 3; run 2026-10-01
"""

GLOSSARY = """# Glossary

## tick

A tick is one step of the game clock.

- **Avoid:** beat — same thing
- **Not:** none
"""

GLOSSARY_AFTER = """# Glossary

## tick

A tick is one step of the game clock.

- **Not:** none
"""

PART_MAP = """# Part map

## core

The part answers for the rules of the game.

- **Files:** src/**
  tests/**
- **Depends on:** shell (separated — the shell only reads the clock)
- **Failure modes:**
  - a save loses a field — a player loses progress — high — detected by save-round-trip
- **Trust boundary:** none

## shell

The part answers for the window and the clock.

- **Files:** foundations/violated_invariants.md
  foundations/**
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none

## save-flow

A player saves and loads a game.

- **Criticality:** high
- **Parts:** core · shell
- **Invariant:** save-round-trip
- **Coverage:** none

## save-file

A save file of one release loads in the next.

- **Declared at:** not markable — test: tests/test_saving.py

## Criticality scale

1. low — a player retries
2. high — a player loses progress

## External context

| Partner | Direction | What comes in | Updates with the product |
|---|---|---|---|
| the player's disk | both | untrusted | no |

## Change paths

| Promise level | What a change at this level may do | What it owes the consumer first |
|---|---|---|

## Files left out on purpose

| File | Why |
|---|---|
| README.md | it binds nothing |

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
"""

PART_MAP_AFTER = """# Part map

## core

The part answers for the rules of the game.

- **Files:** src/**
  tests/**
- **Depends on:** shell
- **Trust boundary:** none

## shell

The part answers for the window and the clock.

- **Files:** foundations/**
- **Depends on:** none
- **Trust boundary:** none

## save-file

A save file of one release loads in the next.

- **Declared at:** not markable — test: tests/test_saving.py

## External context

| Partner | Direction | What comes in |
|---|---|---|
| the player's disk | both | untrusted |

## Files left out on purpose

| File | Why |
|---|---|
| README.md | it binds nothing |

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
"""

VIOLATED = """## Violated invariants

| Identifier | Version |
|---|---|
| clock-steady | 1 |
"""

VERDICTS = """| Entry | Version | Verdict | By | On | Commit | Until |
|---|---|---|---|---|---|---|
| save-name | 1 | pass | Ann | 2026-10-01 | 0123abc | none |
"""

GUIDELINES = """# Coding

- **Decision:** ABC-01@0123abcd
- **Invariant:** save-round-trip@89abcdef

An example of the earlier form: `ABC-01@0123abcd`, and a passage: "ABC-02@0123abcd".

```text
ABC-02@0123abcd
```
"""

GUIDELINES_AFTER = """# Coding

- **Decision:** ABC-01
- **Invariant:** save-round-trip

An example of the earlier form: `ABC-01@0123abcd`, and a passage: "ABC-02@0123abcd".

```text
ABC-02@0123abcd
```
"""

# A test file of the product, its lines joined so that no line of this file is a citation.
SAVING = "\n".join([
    '"""Tests of saving, as save-round-trip/1 has it."""',
    "import unittest",
    "",
    'FIXTURE = "invariant: save-round-trip/1"',
    "",
    "",
    "class Saving(unittest.TestCase):",
    "    def test_round_trip(self):",
    "        # invariant: save-round-trip/1",
    "        # The rule of ABC-01@0123abcd and of `clock-tick/1`.",
    '        # An example: "ABC-01@0123abcd".',
    "        self.assertTrue(True)",
    "",
])

SAVING_AFTER = "\n".join([
    '"""Tests of saving, as save-round-trip has it."""',
    "import unittest",
    "",
    'FIXTURE = "invariant: save-round-trip/1"',
    "",
    "",
    "class Saving(unittest.TestCase):",
    "    def test_round_trip(self):",
    "        # invariant: save-round-trip",
    "        # The rule of ABC-01 and of `clock-tick/1`.",
    '        # An example: "ABC-01@0123abcd".',
    "        self.assertTrue(True)",
    "",
])

# A test in another language, with Windows line endings but for its last line.
CLOCK = "// " + "invariant: clock-steady/2\r\nconst name = 'clock-steady/2';\r\n// done\n"
CLOCK_AFTER = "// " + "invariant: clock-steady\r\nconst name = 'clock-steady/2';\r\n// done\n"

FILES = {
    "foundations/decisions.md": DECISIONS,
    "foundations/invariants.md": INVARIANTS,
    "foundations/environment_facts.md": FACTS,
    "foundations/glossary.md": GLOSSARY,
    "foundations/part_map.md": PART_MAP,
    "foundations/violated_invariants.md": VIOLATED,
    "foundations/human_verdicts.md": VERDICTS,
    "guidelines/coding.md": GUIDELINES,
    "tests/test_saving.py": SAVING,
    "tests/clock.test.mjs": CLOCK,
    "src/save.py": "def save():\n    return 'game.sav'\n",
    "README.md": "The rules follow ABC-01@0123abcd.\n",
}


def build(files, raw=None):
    """A temporary git repository holding the files, each written as UTF-8 with its text's own
    line endings, and the files of `raw` written byte for byte; git adds them all."""
    root = tempfile.mkdtemp()
    for path, text in files.items():
        write(root, path, text.encode("utf-8"))
    for path, data in (raw or {}).items():
        write(root, path, data)
    for command in (["init", "-q"], ["add", "-A"]):
        subprocess.run(["git", "-c", "core.autocrlf=false", *command], cwd=root, check=True,
                       capture_output=True)
    return root


def write(root, path, data):
    full = os.path.join(root, *path.split("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "wb") as handle:
        handle.write(data)


def read(root, path):
    with open(os.path.join(root, *path.split("/")), "rb") as handle:
        return handle.read()


def run(root, *arguments):
    report = os.path.join(tempfile.mkdtemp(), "report.md")
    result = subprocess.run([sys.executable, "-B", SCRIPT, root, "--report", report, *arguments],
                            capture_output=True, text=True, encoding="utf-8")
    with open(report, encoding="utf-8") as handle:
        return result.returncode, result.stdout, handle.read()


class Applied(unittest.TestCase):
    """One product in the earlier form, migrated once with --apply."""

    @classmethod
    def setUpClass(cls):
        cls.root = build(FILES)
        cls.code, cls.output, cls.report = run(cls.root, "--apply")

    def text(self, path):
        return read(self.root, path).decode("utf-8")

    def test_decisions_keep_the_last_version_in_the_place_of_the_first(self):
        self.assertEqual(self.text("foundations/decisions.md"), DECISIONS_AFTER)

    def test_invariants_take_the_current_form(self):
        self.assertEqual(self.text("foundations/invariants.md"), INVARIANTS_AFTER)

    def test_facts_lose_holds_for_and_method(self):
        self.assertEqual(self.text("foundations/environment_facts.md"), FACTS_AFTER)

    def test_glossary_loses_avoid(self):
        self.assertEqual(self.text("foundations/glossary.md"), GLOSSARY_AFTER)

    def test_part_map_takes_the_current_form(self):
        self.assertEqual(self.text("foundations/part_map.md"), PART_MAP_AFTER)

    def test_guidelines_lose_fingerprints_outside_code(self):
        self.assertEqual(self.text("guidelines/coding.md"), GUIDELINES_AFTER)

    def test_comments_and_docstrings_of_code_lose_versions_and_strings_stay(self):
        self.assertEqual(self.text("tests/test_saving.py"), SAVING_AFTER)

    def test_other_languages_keep_their_line_endings(self):
        self.assertEqual(read(self.root, "tests/clock.test.mjs"), CLOCK_AFTER.encode("utf-8"))

    def test_files_of_removed_lists_are_gone(self):
        for path in ("foundations/violated_invariants.md", "foundations/human_verdicts.md"):
            self.assertFalse(os.path.exists(os.path.join(self.root, *path.split("/"))), path)

    def test_files_it_does_not_migrate_stay(self):
        self.assertEqual(self.text("README.md"), "The rules follow ABC-01@0123abcd.\n")

    def test_the_report_names_what_a_human_settles(self):
        for line in [
            "- **ABC-01** — the game saves to a server · check by: 2027-01-01",
            "- **foundations/violated_invariants.md** — | clock-steady | 1 |",
            "- **foundations/human_verdicts.md** — | save-name | 1 | pass | Ann | 2026-10-01 | "
            "0123abc | none |",
            "- **foundations/decisions.md** — ABC-03",
            "- **ABC-02** — ABC-02/1: new decision; ABC-02/2: new wording",
            "  *Rationale:* the shell lost its timer.",
            "  The first version's:",
            "  *Rationale:* the shell owns time.",
            "- **ABC-04** — observation of the release page on 2026-10-01 using `curl`",
            "- **ABC-04** — inherited — searched: README.md; found: README.md",
            "- **save-name** — docs/save_review.md",
            "- **save-size** — Identifier: save-size | Version: 1 | Searched: searched: GAME-9 | "
            "Found: found: GAME-9, its description",
            "- **clock-steady** — tests/clock.test.mjs",
            "- **disk-space** — observed: `df -h` on ClockOS 3; run 2026-10-01",
            "- **tick** — beat — same thing",
            "- **the player's disk** — no",
            "- **guidelines/coding.md** — `ABC-01@0123abcd`",
            "- **guidelines/coding.md** — ABC-02@0123abcd",
            "- **tests/test_saving.py:10** — `clock-tick/1`",
            "- **tests/test_saving.py:11** — \"ABC-01@0123abcd\"",
            "- **guidelines/coding.md** — \"ABC-02@0123abcd\"",
            "- **tests/test_saving.py** — line 4",
            "- **tests/clock.test.mjs** — line 2",
            "- **README.md** — 1 line",
        ]:
            self.assertIn(line, self.report.split("\n"), line)
        for text in ["condition met, decision kept — the shell still ticks",
                     "- **Verification:** level 3 — the human at the merge assesses the release.",
                     "## save-flow", "## save-file", "1. low — a player retries"]:
            self.assertIn(text, self.report)
        self.assertNotIn("**clock-tick** — https", self.report)
        self.assertNotIn("- **save-name** — Identifier: save-name", self.report.split(
            "### Recovered invariants (list removed): Derives from not filled")[1])

    def test_exit_code_says_a_human_has_work(self):
        self.assertEqual(self.code, 1, self.output)
        self.assertTrue(self.output.startswith("applied: "), self.output)

    def test_a_second_run_changes_nothing(self):
        before = {path: read(self.root, path) for path in FILES
                  if os.path.exists(os.path.join(self.root, *path.split("/")))}
        code, output, _ = run(self.root, "--apply")
        after = {path: read(self.root, path) for path in before}
        self.assertEqual(after, before)
        self.assertTrue(output.startswith("applied: 0 changes in 0 files, 0 files removed;"),
                        output)


class Trial(unittest.TestCase):
    def test_a_run_without_apply_writes_nothing_but_its_report(self):
        root = build(FILES)
        code, output, report = run(root)
        for path, text in FILES.items():
            self.assertEqual(read(root, path), text.encode("utf-8"), path)
        self.assertEqual(code, 1, output)
        self.assertTrue(output.startswith("trial run, nothing written: "), output)
        self.assertIn("| `foundations/decisions.md` | older version of a decision removed | 1 |",
                      report)

    def test_the_default_report_goes_to_runs(self):
        root = build({"foundations/glossary.md": GLOSSARY})
        result = subprocess.run([sys.executable, "-B", SCRIPT, root], capture_output=True,
                                text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 1, result.stdout)
        with open(os.path.join(root, ".runs", "foundation_migration.md"), encoding="utf-8") as f:
            self.assertIn("| `foundations/glossary.md` | field removed: Avoid | 1 |", f.read())


class LineEndings(unittest.TestCase):
    def test_a_foundation_file_keeps_its_byte_order_mark_and_windows_line_endings(self):
        glossary = codecs.BOM_UTF8 + GLOSSARY.replace("\n", "\r\n").encode("utf-8")
        root = build({}, {"foundations/glossary.md": glossary})
        run(root, "--apply")
        self.assertEqual(read(root, "foundations/glossary.md"),
                         codecs.BOM_UTF8 + GLOSSARY_AFTER.replace("\n", "\r\n").encode("utf-8"))


class Current(unittest.TestCase):
    def test_a_foundation_in_the_current_form_gives_nothing_to_do(self):
        files = {"foundations/decisions.md": DECISIONS_AFTER.replace(
                     "- **Based on:** observation of the release page on 2026-10-01 using `curl`",
                     "- **Based on:** none").replace(
                     "level 3 — the human at the merge assesses the release.", "none").replace(
                     "inherited — searched: README.md; found: README.md", "none").replace(
                     "### ABC-04", "### ABC-03"),
                 "foundations/glossary.md": GLOSSARY_AFTER,
                 "src/save.py": "def save():\n    return 'game.sav'\n"}
        root = build(files)
        code, output, report = run(root, "--apply")
        self.assertEqual(code, 0, report)
        self.assertTrue(output.startswith("applied: 0 changes in 0 files"), output)
        for path, text in files.items():
            self.assertEqual(read(root, path), text.encode("utf-8"), path)


class CannotRun(unittest.TestCase):
    def test_outside_a_git_repository(self):
        result = subprocess.run([sys.executable, "-B", SCRIPT, tempfile.mkdtemp()],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 2, result.stdout)

    def test_a_repository_without_a_foundation(self):
        root = build({"src/save.py": "def save():\n    return 'game.sav'\n"})
        result = subprocess.run([sys.executable, "-B", SCRIPT, root], capture_output=True,
                                text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("holds no foundation", result.stdout)


if __name__ == "__main__":
    unittest.main()
