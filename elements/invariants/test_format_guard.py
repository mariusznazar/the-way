"""Tests of the invariants guard: every check fires on a file broken on purpose.

Run from the root of the-way:
    python -B gate/run_tests.py elements/invariants --record .runs/invariants-tests.jsonl

Inputs, expected fingerprints and expected record lines are written out, never computed by the
code under test (WAY-70).
"""

import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402

GUARD = "elements/invariants/format_guard.py"
NO_COMMIT = "the method takes a commit the gate filled in as not existing"

DECISION = "A saved game is written to the player's own storage only."
DECISION_FINGERPRINT = "4dd7fb86"
DECISION_REWORDED = "A saved game is written to the player's own storage, and nowhere else."
DECISION_REWORDED_FINGERPRINT = "4b7b9b75"
SENTENCE = "A game saved and loaded back holds the same state as before it was saved."
SENTENCE_FINGERPRINT = "885f5dbb"
REWORDED = "A game saved and loaded back holds the same state as when it was saved."
REWORDED_FINGERPRINT = "f2ad38fc"
OTHER = "A saved game loads in any later version of the product."


def decision(version=1, binding=DECISION, verification=None, change=None):
    lines = ["### WAY-01/%d — Where does a saved game go?" % version, ""]
    if binding is not None:
        lines += [binding, ""]
    lines.append("- **Change:** %s" % (change or ("new decision" if version == 1 else
                                                 "new wording")))
    if verification is not None:
        lines.append("- **Verification:** %s" % verification)
    return "\n".join(lines) + "\n"


LOG = "# Decision log\n\n" + decision()

MAP = "\n".join([
    "# Part map", "",
    "## saving — Saving a game", "", "The part answers for writing and reading a saved game.", "",
    "- **Files:** src/saving.py", "- **Depends on:** none", "- **Failure modes:** none",
    "- **Trust boundary:** none", "",
    "## loading — Loading a game", "", "The part answers for reading a saved game back.", "",
    "- **Files:** src/loading.py", "- **Depends on:** none", "- **Failure modes:** none",
    "- **Trust boundary:** none", "",
    "## save-and-load — Save and load", "", "The player saves a game and loads it back.", "",
    "- **Criticality:** high", "- **Parts:** saving · loading",
    "- **Invariant:** loads-in-later-versions — test: tests/test_saving.py", "- **Coverage:** none",
    "",
    "## Withdrawn identifiers", "", "| Identifier | Successors |", "|---|---|",
    "| game-state | saving |", ""])


def entry(identifier="save-round-trip", version=1, sentence=SENTENCE,
          method="`python -m unittest tests/test_saving.py`", rests="none",
          derives="WAY-01@" + DECISION_FINGERPRINT, part="saving · loading", correction="none",
          omit=(), heading=None):
    lines = [heading or "## %s/%d" % (identifier, version), "", sentence, ""]
    fields = [("Method", method), ("Rests on", rests), ("Derives from", derives), ("Part", part),
              ("Correction", correction)]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def later(**changes):
    values = dict(identifier="loads-in-later-versions", sentence=OTHER, derives="none",
                  part="loading")
    values.update(changes)
    return entry(**values)


WITHDRAWN = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Why | Successors |",
                       "|---|---|---|", "| save-format | merged with another entry | save-round-trip |"])
QUARANTINE = "\n".join(["## Quarantined invariants", "", "| Identifier | Version | Until |",
                        "|---|---|---|"])
RECOVERED_HEADER = "\n".join(["## Recovered invariants", "",
                              "| Identifier | Version | Searched | Found |", "|---|---|---|---|"])


def recovered(*rows):
    """The list of recovered invariants, with a row for each `identifier | version | searched: … |
    found: …` given."""
    return "\n".join([RECOVERED_HEADER] + ["| %s |" % row for row in rows])


RECOVERED = recovered("loads-in-later-versions | 1 | searched: the decision log | found: nothing")


def invariants(*entries, withdrawn=WITHDRAWN, quarantine=QUARANTINE, recovered=RECOVERED):
    sections = list(entries) or [entry(), later()]
    return "# Invariants\n\n" + "\n\n".join(
        sections + [s for s in (withdrawn, quarantine, recovered) if s]) + "\n"


FACT_FINGERPRINT = "b28784ec"
FACTS = "\n".join([
    "# Environment facts", "",
    "## storage-quota/1", "", "The browser keeps at least 5 MB of local storage for each origin.",
    "", "- **Holds for:** Firefox 130",
    '- **Source:** https://developer.mozilla.org/docs/storage/130 § Web Storage — "at least 5 MB '
    'per origin"; read 2026-09-26',
    "- **Method:** `TODO`", "",
    "## Withdrawn identifiers", "", "| Identifier | Why | Successors |", "|---|---|---|",
    "| storage-limit | split into two facts | storage-quota |", ""])
VERDICT_HEADER = "| Entry | Version | Verdict | By | On | Commit | Until |\n|---|---|---|---|---|---|---|\n"


def human_verdicts(*rows):
    return "# Human verdicts\n\n" + VERDICT_HEADER + "".join("| %s |\n" % " | ".join(row)
                                                             for row in rows)


def violated(*rows):
    return "\n".join(["## Violated invariants", "", "| Identifier | Version |", "|---|---|"] +
                     ["| %s | %s |" % row for row in rows]) + "\n"


FILES = {"src/saving.py": "def save():\n    pass\n",
         "src/loading.py": "def load():\n    pass\n",
         "tests/test_saving.py": "# invariant: save-round-trip/1\n# data: tests/saved_game.json\n"
                                 "def test_round_trip():\n    pass\n",
         "tests/saved_game.json": "{}\n",
         "docs/review_checklist.md": "# What a reviewer looks at\n",
         "README.md": "# Product\n\n# invariant: nothing-here/1\n"}

# The invariants each run records, as the method lines of the-way's own entries name the runs.
PLAIN = sorted([
    "invariant-version-number/1", "invariants-file/1", "invariant-identifier-form/1",
    "withdrawal-successors/1", "identifier-holders/1", "invariant-entry-field-presence/1",
    "invariant-entry-field-words/1", "invariant-sentence-count/1", "sentence-branch-names/1",
    "sentence-gate-values/1", "method-gate-values/1", "invariant-method-form/1",
    "link-fingerprint-presence/1", "invariant-part-form/1", "invariant-part-names/1",
    "invariant-recovered-form/1", "invariant-recovered-derived/1",
    "level-one-decision-invariants/1", "verification-invariant-derivation/1",
    "quarantine-position-form/1", "quarantine-flow-invariants/1", "violated-position-version/1",
    "invariant-citation-version/1", "invariant-citation-target/1", "data-line-target/1",
    "run-record-path/1", "human-verdict-invariant-row/1"])
BASE = sorted([
    "invariant-version-new/1", "invariant-version-changed/1", "invariant-version-unchanged/1",
    "invariant-earlier-wording/1", "invariant-identifier-persistence/1",
    "invariant-withdrawal-persistence/1", "violated-list-growth/1"])
MERGE = sorted(["invariant-entry-merge-todo/1", "link-fingerprint-value/1"])


class GuardTestCase(unittest.TestCase):
    files = FILES

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.outside = tempfile.TemporaryDirectory()
        self.root = self.directory.name
        self.path = os.path.join(self.root, "foundations", "invariants.md")
        self.record_path = os.path.join(self.outside.name, ".runs", "invariants.jsonl")
        self.lines = []
        files = dict(self.files)
        files["foundations/part_map.md"] = MAP
        files["foundations/decisions.md"] = LOG
        for name, content in files.items():
            self.write(name, content)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "guard@example.com")
        self.git("config", "user.name", "Guard")

    def tearDown(self):
        self.directory.cleanup()
        self.outside.cleanup()

    def write(self, name, content):
        full = os.path.join(self.root, name.replace("/", os.sep))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)

    def git(self, *arguments):
        subprocess.run(["git"] + list(arguments), cwd=self.root, check=True, capture_output=True)

    def commit(self, text, violated_text=None):
        self.write("foundations/invariants.md", text)
        if violated_text is not None:
            self.write("foundations/violated_invariants.md", violated_text)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")

    def guard(self, text, base=None, violated_text=None, merge_onto=None, path=None, own=None,
              examples=None):
        self.write("foundations/invariants.md", text)
        if violated_text is not None:
            self.write("foundations/violated_invariants.md", violated_text)
        self.git("add", "-A")
        output = io.StringIO()
        # the examples and the-way's own file are given only where a test sets them
        given = {name: value for name, value in (("own", own), ("examples", examples))
                 if value is not None}
        code = format_guard.run(path or self.path, base=base, stream=output,
                                merge_onto=merge_onto, record=self.record_path, **given)
        with open(self.record_path, encoding="utf-8") as handle:
            self.lines = [json.loads(item) for item in handle.read().split("\n") if item]
        return code, output.getvalue()

    def assertPasses(self, text, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 0, output)
        self.assertIn("0 error(s), 0 warning(s)", output)
        return output

    def assertFails(self, text, fragment, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 1, output)
        self.assertIn(fragment, output)
        return output

    def verdicts(self, invariant):
        return [line["verdict"] for line in self.lines if line["invariant"] == invariant]

    def assertRecorded(self, invariant, verdict):
        self.assertIn(verdict, self.verdicts(invariant), self.lines)


class ValidFile(GuardTestCase):
    def test_valid_file_passes(self):
        self.assertPasses(invariants())

    def test_without_options_a_note_says_what_is_not_compared(self):
        output = self.assertPasses(invariants())
        self.assertIn("note: no --base given: identifiers, versions, corrections and the list of "
                      "violated invariants are not compared with the main branch", output)
        self.assertIn("note: no --merge-onto given: `TODO` in the entries is not checked against a "
                      "merge", output)

    def test_method_as_the_path_of_a_file_a_human_assesses_against(self):
        self.assertPasses(invariants(entry(method="docs/review_checklist.md"), later()))

    def test_todo_the_main_branch_holds(self):
        self.assertPasses(invariants(entry(method="`TODO`", rests="TODO — the store keeps 5 MB, "
                                           "per its documentation"), later()))

    def test_todo_the_form_gives_in_derives_from_is_a_warning(self):
        code, output = self.guard(invariants(entry(derives="`TODO — a decision on saves, expected "
                                                           "with the first task`"), later()))
        self.assertEqual(code, 0, output)
        self.assertIn("save-round-trip/1: *Derives from* holds `TODO`, which a merge onto the main "
                      "branch does not take", output)
        self.assertIn("0 error(s), 1 warning(s)", output)
        self.assertEqual(self.verdicts("invariant-entry-field-words/1"), ["pass"])

    def test_every_as_the_part(self):
        self.assertPasses(invariants(entry(part="every"), later()))

    def test_a_recovered_invariant_on_the_list_passes(self):
        # invariant: invariant-recovered-form/1
        # invariant: invariant-recovered-derived/1
        self.assertPasses(invariants(entry(derives="none"), later(), recovered=recovered(
            "save-round-trip | 1 | searched: the decision log, git history | found: nothing",
            "loads-in-later-versions | 1 | searched: the decision log | "
            "found: docs/saves.md § Versions")))
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["pass"])
        self.assertEqual(self.verdicts("invariant-recovered-derived/1"), ["pass"])

    def test_an_entry_off_the_list_of_recovered_invariants_may_derive_from_no_decision(self):
        self.assertPasses(invariants(entry(), later(), recovered=recovered()))


class Rules(unittest.TestCase):
    """What the guard reads from the template and from the rules the elements share."""

    def edited(self, path, change):
        """The path of a copy of the file at `path`, changed by `change`."""
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        changed = change(text)
        self.assertNotEqual(changed, text)
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        copy = os.path.join(directory.name, os.path.basename(path))
        with open(copy, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(changed)
        return copy

    def test_the_fields_the_main_branch_holds_todo_in_are_read_from_the_rules_the_elements_share(
            self):
        self.assertEqual(format_guard.read_rules().main_todo, ["Method", "Rests on"])
        common = self.edited(format_guard.COMMON_RULES, lambda text: re.sub(
            r",\s+and\s+in\s+an\s+invariant's\s+\*Rests\s+on\*\s+until\s+the\s+environment\s+facts"
            r"\s+element\s+has\s+entries", "", text, count=1))
        self.assertEqual(format_guard.read_rules(common=common).main_todo, ["Method"])

    def test_the_list_of_withdrawn_identifiers_is_read_from_the_rules_the_elements_share(self):
        self.assertEqual(format_guard.read_rules().lists[0],
                         ("Withdrawn identifiers", ["Identifier", "Why", "Successors"]))
        common = self.edited(format_guard.COMMON_RULES, lambda text: text.replace(
            "| Identifier | Why | Successors |", "| Identifier | Why | Successors | Since |", 1))
        self.assertEqual(format_guard.read_rules(common=common).lists[0][1],
                         ["Identifier", "Why", "Successors", "Since"])

    def test_the_lists_closing_the_file_stand_in_their_order(self):
        self.assertEqual([title for title, _ in format_guard.read_rules().lists],
                         ["Withdrawn identifiers", "Quarantined invariants", "Recovered invariants"])
        self.assertEqual(format_guard.read_rules().lists[2][1],
                         ["Identifier", "Version", "Searched", "Found"])

    def test_the_row_of_a_human_verdict_is_read_from_the_rules_the_elements_share(self):
        rules = format_guard.read_rules()
        self.assertEqual((rules.verdicts_file, rules.verdicts_columns),
                         ("human_verdicts.md",
                          ["Entry", "Version", "Verdict", "By", "On", "Commit", "Until"]))
        common = self.edited(format_guard.COMMON_RULES, lambda text: text.replace(
            "| Entry | Version | Verdict | By | On | Commit | Until |",
            "| Entry | Version | Verdict | By | On | Commit | Until | Note |", 1))
        self.assertEqual(format_guard.read_rules(common=common).verdicts_columns[-1], "Note")

    def test_the_words_a_sentence_may_not_hold_are_read_from_the_sentence_section(self):
        self.assertEqual(format_guard.read_rules().forbidden_words, ["main branch", "task branch"])
        template = self.edited(format_guard.TEMPLATE, lambda text: text.replace(
            'nor "task branch"', 'nor "task branch" nor "release branch"', 1))
        self.assertEqual(format_guard.read_rules(template).forbidden_words,
                         ["main branch", "task branch", "release branch"])

    def test_the_rules_stand_without_a_list_of_checks(self):
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            self.assertNotIn("## What the format guard checks", handle.read())
        self.assertTrue(format_guard.read_rules().fields)


class EntriesInAText(unittest.TestCase):
    def test_a_section_with_a_version_and_a_method_is_an_entry(self):
        self.assertTrue(format_guard.holds_entries(
            "# Notes\n\n## loads-fast/1\n\nA saved game loads.\n\n- **Method:** `TODO`\n"))

    def test_a_section_without_a_method_is_no_entry(self):
        self.assertFalse(format_guard.holds_entries("# Notes\n\n## release/2\n\nShipped.\n"))

    def test_a_method_under_a_heading_without_a_version_is_no_entry(self):
        self.assertFalse(format_guard.holds_entries(
            "# Notes\n\n## How to check\n\n- **Method:** `TODO`\n"))

    def test_an_environment_fact_entry_is_no_invariant_entry(self):
        self.assertFalse(format_guard.holds_entries(FACTS))

    def test_an_entry_before_a_block_left_open_is_an_entry(self):
        self.assertTrue(format_guard.holds_entries(
            "# Notes\n\n## loads-fast/1\n\nA saved game loads.\n\n- **Method:** `TODO`\n\n```\n"))

    def test_an_entry_in_a_tilde_fence_is_no_entry(self):
        self.assertFalse(format_guard.holds_entries(
            "# Notes\n\n~~~\n## loads-fast/1\n\nA saved game loads.\n\n- **Method:** `TODO`\n~~~\n"))

    def test_an_invariant_entry_after_a_fact_entry_is_an_entry(self):
        self.assertTrue(format_guard.holds_entries(
            FACTS + "\n## loads-fast/1\n\nA saved game loads.\n\n- **Method:** `TODO`\n"))


class Layout(GuardTestCase):
    def test_file_elsewhere_than_foundations_invariants(self):
        self.write("foundations/other.md", invariants())
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(os.path.join(self.root, "foundations", "other.md"), stream=output)
        self.assertEqual(code, 1, output.getvalue())
        self.assertIn("a product's invariants stand in foundations/invariants.md, not in "
                      "foundations/other.md", output.getvalue())

    def test_file_in_a_foundations_directory_below_the_root(self):
        for name, content in (("product/foundations/part_map.md", MAP),
                              ("product/foundations/decisions.md", LOG)):
            self.write(name, content)
        self.write("product/foundations/invariants.md", invariants())
        self.git("add", "-A")
        self.write("foundations/invariants.md", invariants())
        output = io.StringIO()
        code = format_guard.run(os.path.join(self.root, "product", "foundations", "invariants.md"),
                                stream=output)
        self.assertEqual(code, 1, output.getvalue())
        self.assertIn("a product's invariants stand in foundations/invariants.md, not in "
                      "product/foundations/invariants.md", output.getvalue())

    def test_second_file_of_invariant_entries(self):
        self.write("docs/invariants.md", invariants())
        self.assertFails(invariants(), "`docs/invariants.md` is a second file of invariant entries")
        self.assertRecorded("invariants-file/1", "fail")

    def test_second_file_of_invariant_entries_under_another_name(self):
        self.write("foundations/invariants_extra.md", "# Extra\n\n" + later(
            identifier="loads-fast", sentence="A saved game loads in one second.") + "\n")
        self.assertFails(invariants(), "`foundations/invariants_extra.md` is a second file of "
                                       "invariant entries")
        self.assertEqual(self.verdicts("invariants-file/1"), ["fail"])

    def test_a_copy_in_the_examples_beside_the_template_is_a_second_file(self):
        # invariant: invariants-file/1
        self.write("elements/invariants/examples.md", "# Examples\n\n" + entry() + "\n")
        self.assertFails(invariants(), "`elements/invariants/examples.md` is a second file of "
                                       "invariant entries")
        self.assertEqual(self.verdicts("invariants-file/1"), ["fail"])

    def test_entry_shown_in_a_fenced_block_is_no_file_of_entries(self):
        self.write("docs/guide.md", "# Guide\n\n```markdown\n" + entry() + "\n```\n")
        self.assertPasses(invariants())
        self.assertEqual(self.verdicts("invariants-file/1"), ["pass"])

    def test_file_named_in_another_letter_case(self):
        self.write("foundations/Invariants.md", invariants())
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(os.path.join(self.root, "foundations", "Invariants.md"),
                                stream=output, record=self.record_path)
        self.assertEqual(code, 1, output.getvalue())
        self.assertIn("a product's invariants stand in foundations/invariants.md, not in "
                      "foundations/Invariants.md", output.getvalue())

    def test_heading_that_is_neither_an_entry_nor_a_list(self):
        self.assertFails(invariants(entry(), later(), "## Notes\n\nSome notes."),
                         "heading `## Notes` is neither")
        self.assertEqual(self.verdicts("invariant-version-number/1"), ["pass"])

    def test_heading_of_an_entry_without_a_version(self):
        self.assertFails(invariants(entry(heading="## save-round-trip"), later()),
                         "heading `## save-round-trip` of an entry carries no version number")
        self.assertEqual(self.verdicts("invariant-version-number/1"), ["fail"])

    def test_heading_of_an_entry_with_a_version_that_is_no_number(self):
        self.assertFails(invariants(entry(heading="## save-round-trip/v2"), later()),
                         "heading `## save-round-trip/v2` of an entry carries no version number")

    def test_missing_list(self):
        self.assertFails(invariants(quarantine=None), "the file has no list `Quarantined invariants`")

    def test_missing_list_of_recovered_invariants(self):
        self.assertFails(invariants(recovered=None),
                         "the file has no list `Recovered invariants`")

    def test_lists_out_of_order(self):
        self.assertFails(invariants(withdrawn=QUARANTINE, quarantine=WITHDRAWN),
                         "not in the order")

    def test_list_of_recovered_invariants_that_does_not_close_the_file(self):
        self.assertFails(invariants(quarantine=RECOVERED, recovered=QUARANTINE),
                         "the lists closing the file are not in the order `Withdrawn identifiers`, "
                         "`Quarantined invariants`, `Recovered invariants`")

    def test_list_of_withdrawn_identifiers_without_why(self):
        self.assertFails(invariants(withdrawn="\n".join([
            "## Withdrawn identifiers", "", "| Identifier | Successors |", "|---|---|",
            "| save-format | save-round-trip |"])),
            "the list `Withdrawn identifiers` has columns Identifier | Successors, not "
            "Identifier | Why | Successors")

    def test_entry_after_a_list(self):
        text = "# Invariants\n\n" + "\n\n".join([entry(), WITHDRAWN, later(), QUARANTINE]) + "\n"
        self.assertFails(text, "entry `loads-in-later-versions` stands after the list")

    def test_list_with_other_columns(self):
        self.assertFails(invariants(quarantine=QUARANTINE.replace("| Until |", "| End |")),
                         "has columns Identifier | Version | End")


class Identifiers(GuardTestCase):
    def test_identifier_with_capitals(self):
        self.assertFails(invariants(entry("Save-Round-Trip"), later()),
                         "`Save-Round-Trip` is not an identifier")
        self.assertRecorded("invariant-identifier-form/1", "fail")

    def test_identifier_with_a_space(self):
        self.assertFails(invariants(entry(heading="## save round-trip/1"), later()),
                         "`save round-trip` is not an identifier")
        self.assertEqual(self.verdicts("invariant-identifier-form/1"), ["fail"])
        self.assertEqual(self.verdicts("invariant-version-number/1"), ["pass"])

    def test_none_as_an_identifier(self):
        self.assertFails(invariants(entry("none"), later()), "`none` is not an identifier")

    def test_withdrawn_identifier_of_another_form_is_no_entry_identifier(self):
        self.assertFails(invariants(withdrawn=WITHDRAWN + "\n| Old_Name | renamed | none |"),
                         "`Old_Name` is not an identifier")
        self.assertEqual(self.verdicts("invariant-identifier-form/1"), ["pass"])

    def test_identifier_used_twice(self):
        self.assertFails(invariants(entry(), later(), entry(sentence=OTHER)),
                         "identifier `save-round-trip` is used twice")
        self.assertRecorded("identifier-holders/1", "fail")

    def test_identifier_of_a_withdrawn_one(self):
        self.assertFails(invariants(entry("save-format"), later()),
                         "identifier `save-format` is used twice")

    def test_identifier_held_by_a_part_of_the_map(self):
        self.assertFails(invariants(entry("saving"), later()), "`saving` is held by the part map")
        self.assertRecorded("identifier-holders/1", "fail")

    def test_identifier_withdrawn_in_the_map(self):
        self.assertFails(invariants(entry("game-state"), later()),
                         "`game-state` is held by the part map")

    def test_identifier_held_twice_in_the_map(self):
        self.write("foundations/part_map.md", MAP.replace("## loading — Loading a game",
                                                          "## saving — Loading a game"))
        self.assertFails(invariants(), "part_map.md:12: identifier `saving` is held twice in the "
                                       "part map")
        self.assertRecorded("identifier-holders/1", "fail")

    def test_withdrawn_identifier_names_an_unknown_successor(self):
        self.assertFails(invariants(withdrawn=WITHDRAWN.replace("| save-round-trip |",
                                                                "| save-trip |")),
                         "names successor `save-trip`")
        self.assertRecorded("withdrawal-successors/1", "fail")

    def test_withdrawn_identifier_with_no_successor(self):
        self.assertPasses(invariants(withdrawn=WITHDRAWN.replace("| save-round-trip |", "| none |")))

    def test_withdrawn_identifier_giving_why(self):
        # invariant: withdrawal-successors/1
        self.assertPasses(invariants())
        self.assertEqual(self.verdicts("withdrawal-successors/1"), ["pass"])

    def test_withdrawn_identifier_off_the_form(self):
        # invariant: withdrawal-successors/1
        for identifier in ("Save-Format", "save_format", "none"):
            with self.subTest(identifier=identifier):
                self.assertFails(invariants(withdrawn=WITHDRAWN.replace(
                    "| save-format |", "| %s |" % identifier)),
                    "`%s` is not an identifier of words in lower case joined by hyphens"
                    % identifier)
                self.assertEqual(self.verdicts("withdrawal-successors/1"), ["fail"])
                self.assertEqual(self.verdicts("invariant-identifier-form/1"), ["pass"])

    def test_withdrawn_identifier_giving_no_why(self):
        # invariant: withdrawal-successors/1
        for why in ("", "none", "`none`", "TODO"):
            with self.subTest(why=why):
                self.assertFails(invariants(withdrawn=WITHDRAWN.replace(
                    "| merged with another entry |", "| %s |" % why)),
                    "withdrawn `save-format` gives no reason in *Why*")
                self.assertEqual(self.verdicts("withdrawal-successors/1"), ["fail"])


class Fields(GuardTestCase):
    def test_missing_field(self):
        self.assertFails(invariants(entry(omit=("Correction",)), later()),
                         "field *Correction* is missing")
        self.assertRecorded("invariant-entry-field-presence/1", "fail")

    def test_a_recovered_field_is_not_a_field_of_the_form(self):
        output = self.assertFails(invariants(entry() + "\n- **Recovered:** none", later()),
                                  "save-round-trip/1: *Recovered* is not a field of the form; "
                                  "a recovered invariant stands on the list of recovered invariants")
        self.assertNotIn("field *Recovered* is not in the template", output)
        self.assertEqual(self.verdicts("invariant-entry-field-presence/1"), ["pass"])

    def test_field_not_in_the_template(self):
        self.assertFails(invariants(entry() + "\n- **Owner:** the saving team", later()),
                         "field *Owner* is not in the template")

    def test_none_where_the_form_does_not_give_it(self):
        self.assertFails(invariants(entry(method="none"), later()), "*Method* may not hold `none`")
        self.assertRecorded("invariant-entry-field-words/1", "fail")

    def test_todo_where_the_form_does_not_give_it(self):
        self.assertFails(invariants(entry(part="TODO"), later()), "*Part* may not hold `TODO`")
        self.assertRecorded("invariant-entry-field-words/1", "fail")

    def test_todo_inside_a_part_of_a_value(self):
        self.assertFails(invariants(entry(part="saving (TODO: loading)"), later()),
                         "*Part* may not hold `TODO`")
        self.assertEqual(self.verdicts("invariant-entry-field-words/1"), ["fail"])

    def test_todo_inside_a_path_is_no_todo(self):
        self.write("docs/TODO.md", "# What is left\n")
        self.assertPasses(invariants(entry(method="docs/TODO.md"), later()))

    def test_todo_as_one_item_of_a_list(self):
        self.assertFails(invariants(entry(part="saving · TODO"), later()),
                         "*Part* may not hold `TODO`")


class Sentence(GuardTestCase):
    def test_missing_sentence(self):
        broken = entry().replace(SENTENCE + "\n\n", "")
        self.assertFails(invariants(broken, later()), "the sentence is missing")
        self.assertRecorded("invariant-sentence-count/1", "fail")

    def test_two_sentences(self):
        self.assertFails(invariants(entry(sentence=SENTENCE + " " + OTHER), later()),
                         "2 sentences, an entry states one")
        self.assertRecorded("invariant-sentence-count/1", "fail")

    def test_main_branch_outside_quoted_text(self):
        self.assertFails(invariants(entry(sentence="On the main branch, a saved game loads."),
                                    later()), 'the sentence names "main branch"')
        self.assertRecorded("sentence-branch-names/1", "fail")

    def test_main_branches_outside_quoted_text(self):
        self.assertFails(invariants(entry(sentence="No saved game differs between main branches."),
                                    later()), 'the sentence names "main branch"')

    def test_second_paragraph_after_the_sentence(self):
        broken = entry().replace(SENTENCE + "\n", SENTENCE + "\n\n" + OTHER + "\n")
        self.assertFails(invariants(broken, later()), "text outside the sentence and the fields")
        self.assertRecorded("invariant-sentence-count/1", "fail")

    def test_prose_after_the_fields(self):
        self.assertFails(invariants(entry() + "\n\nThis holds since the first release.", later()),
                         "text outside the sentence and the fields")

    def test_bound_with_a_tilde_before_a_word(self):
        self.assertFails(invariants(entry(sentence="A saved game loads within ~two seconds."),
                                    later()), "a bound with a tilde")

    def test_main_branch_inside_quoted_text(self):
        self.assertPasses(invariants(entry(sentence='The guard reports "main branch missing" when '
                                                    'given no commit.'), later()))

    def test_bound_with_a_tilde(self):
        self.assertFails(invariants(entry(sentence="A saved game loads within ~2 seconds."),
                                    later()), "a bound with a tilde")

    def test_value_the_gate_does_not_fill_in(self):
        # invariant: sentence-gate-values/1
        self.assertFails(invariants(entry(sentence="No saved game changes since {base}."), later()),
                         "`{base}` is not a value the gate fills in")
        self.assertEqual(self.verdicts("sentence-gate-values/1"), ["fail"])

    def test_value_its_command_does_not_take(self):
        self.assertFails(invariants(entry(sentence="No saved game changes since {fork-point}."),
                                    later()), "names `{fork-point}`, which its command does not take")
        self.assertRecorded("sentence-gate-values/1", "fail")

    def test_value_its_command_takes(self):
        self.assertPasses(invariants(entry(sentence="No saved game changes since {fork-point}.",
                                           method="`python tests/compare.py {fork-point}`"), later()))


class Method(GuardTestCase):
    def test_command_that_is_a_path_alone(self):
        self.assertFails(invariants(entry(method="`tests/test_saving.py`"), later()),
                         "a command begins with the name of the program it runs")
        self.assertRecorded("invariant-method-form/1", "fail")

    def test_command_taking_a_value_the_gate_does_not_fill_in(self):
        self.assertFails(invariants(entry(method="`python tests/compare.py {base}`"), later()),
                         "the command takes `{base}`")
        self.assertRecorded("method-gate-values/1", "fail")

    def test_path_of_no_file(self):
        self.assertFails(invariants(entry(method="docs/missing.md"), later()),
                         "*Method* names `docs/missing.md`, which is not a file")
        self.assertRecorded("invariant-method-form/1", "fail")

    def test_command_beginning_with_a_flag(self):
        self.assertFails(invariants(entry(method="`--verbose python tests/test_saving.py`"),
                                    later()),
                         "a command begins with the name of the program it runs, not `--verbose`")
        self.assertEqual(self.verdicts("invariant-method-form/1"), ["fail"])

    def test_command_beginning_with_a_variable(self):
        self.assertFails(invariants(entry(method="`PYTHONPATH=src python tests/test_saving.py`"),
                                    later()),
                         "a command begins with the name of the program it runs, not "
                         "`PYTHONPATH=src`")
        self.assertEqual(self.verdicts("invariant-method-form/1"), ["fail"])

    def test_empty_method(self):
        self.assertFails(invariants(entry(method=""), later()), "field *Method* is missing")
        self.assertEqual(self.verdicts("invariant-method-form/1"), ["fail"])

    def test_shell_variable_in_a_command(self):
        self.assertPasses(invariants(entry(method='`sh -c "python tests/test_saving.py ${HOME}"`'),
                                     later()))
        self.assertEqual(self.verdicts("method-gate-values/1"), ["pass"])

    def test_shell_variable_in_a_sentence(self):
        self.assertPasses(invariants(entry(sentence="A game saved under ${HOME} loads back whole."),
                                     later()))
        self.assertEqual(self.verdicts("sentence-gate-values/1"), ["pass"])

    def test_method_in_prose(self):
        self.assertFails(invariants(entry(method="a reviewer reads the save code"), later()),
                         "*Method* is neither a command in backticks")


class Links(GuardTestCase):
    def test_stale_fingerprint_without_a_commit_to_merge_onto(self):
        self.assertPasses(invariants(entry(derives="WAY-01@00000000"), later()))
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), [])

    def test_decision_that_does_not_exist(self):
        self.assertFails(invariants(entry(derives="WAY-07@" + DECISION_FINGERPRINT), later()),
                         "names a decision that does not exist or binds nothing any more")

    def test_decision_repealed_since(self):
        self.write("foundations/decisions.md", LOG + "\n" + decision(
            2, binding=None, change="repeal"))
        self.assertFails(invariants(), "`WAY-01@4dd7fb86` names a decision that does not exist or "
                                       "binds nothing any more")

    def test_decision_without_a_fingerprint(self):
        self.assertFails(invariants(entry(derives="WAY-01"), later()),
                         "`WAY-01` carries no fingerprint of 8 hex digits; it reads "
                         "`WAY-NN@<fingerprint>`")
        self.assertRecorded("link-fingerprint-presence/1", "fail")

    def test_fingerprint_shorter_than_the_relation_model_gives(self):
        self.assertFails(invariants(entry(derives="WAY-01@1a2b3c"), later()),
                         "`WAY-01@1a2b3c` carries no fingerprint of 8 hex digits")
        self.assertEqual(self.verdicts("link-fingerprint-presence/1"), ["fail"])

    def test_fingerprint_longer_than_the_relation_model_gives(self):
        self.assertFails(invariants(entry(derives="WAY-01@4dd7fb860"), later()),
                         "`WAY-01@4dd7fb860` carries no fingerprint of 8 hex digits")
        self.assertEqual(self.verdicts("link-fingerprint-presence/1"), ["fail"])

    def test_named_fact_while_facts_have_no_entries(self):
        self.assertFails(invariants(entry(rests="storage-quota@1234abcd"), later()),
                         "the environment facts element has no entries")
        self.assertEqual(self.verdicts("link-fingerprint-presence/1"), ["pass"])

    def test_named_fact_without_a_fingerprint(self):
        self.assertFails(invariants(entry(rests="storage-quota"), later()),
                         "the environment facts element has no entries")
        self.assertEqual(self.verdicts("link-fingerprint-presence/1"), ["fail"])


class Part(GuardTestCase):
    def test_every_and_parts_at_once(self):
        self.assertFails(invariants(entry(part="every · saving"), later()),
                         "names `every` and parts at once")
        self.assertRecorded("invariant-part-form/1", "fail")

    def test_none_as_the_part(self):
        self.assertFails(invariants(entry(part="none"), later()), "*Part* may not hold `none`")
        self.assertEqual(self.verdicts("invariant-part-form/1"), ["fail"])

    def test_part_not_in_the_map(self):
        self.assertFails(invariants(entry(part="saving · cloud"), later()),
                         "names `cloud`, which is not a part of the part map")
        self.assertRecorded("invariant-part-names/1", "fail")

    def test_flow_is_not_a_part(self):
        self.assertFails(invariants(entry(part="save-and-load"), later()),
                         "names `save-and-load`, which is not a part")


class Correction(GuardTestCase):
    def test_correction_of_another_form(self):
        self.assertFails(invariants(entry(correction="the wording was fixed"), later()),
                         "*Correction* is neither `none` nor")

    def test_correction_naming_another_current_fingerprint(self):
        # invariant: invariant-fingerprint-input/1
        self.assertFails(invariants(entry(correction="%s → %s" % (REWORDED_FINGERPRINT,
                                                                  REWORDED_FINGERPRINT)), later()),
                         "*Correction* names %s as the current fingerprint, but it is %s"
                         % (REWORDED_FINGERPRINT, SENTENCE_FINGERPRINT))

    def test_a_sentence_over_several_lines_is_fingerprinted_whole(self):
        """SENTENCE wrapped over two lines, over three, and one word to a line: its fingerprint
        is still SENTENCE_FINGERPRINT."""
        # invariant: invariant-fingerprint-input/1
        for wrapped in ("A game saved and loaded back holds the same state as\nbefore it was "
                        "saved.",
                        "A game saved and loaded\nback holds the same state\nas before it was "
                        "saved.",
                        SENTENCE.replace(" ", "\n")):
            with self.subTest(lines=wrapped.count("\n") + 1):
                self.assertFails(invariants(entry(sentence=wrapped,
                                                  correction="%s → %s" % (REWORDED_FINGERPRINT,
                                                                          REWORDED_FINGERPRINT)),
                                            later()),
                                 "*Correction* names %s as the current fingerprint, but it is %s"
                                 % (REWORDED_FINGERPRINT, SENTENCE_FINGERPRINT))

    def test_a_correction_naming_the_fingerprint_of_the_whole_wrapped_sentence_passes(self):
        """SENTENCE wrapped over several lines, with the correction naming its fingerprint as the
        current one: no error."""
        # invariant: invariant-fingerprint-input/1
        for wrapped in ("A game saved and loaded back holds the same state as\nbefore it was "
                        "saved.",
                        "A game saved and loaded\nback holds the same state\nas before it was "
                        "saved.",
                        SENTENCE.replace(" ", "\n")):
            with self.subTest(lines=wrapped.count("\n") + 1):
                self.assertPasses(invariants(entry(sentence=wrapped,
                                                   correction="%s → %s" % (REWORDED_FINGERPRINT,
                                                                           SENTENCE_FINGERPRINT)),
                                             later()))

    def test_fields_right_under_the_sentence_stay_out_of_its_fingerprint(self):
        # invariant: invariant-fingerprint-input/1
        text = entry(correction="%s → %s" % (REWORDED_FINGERPRINT, REWORDED_FINGERPRINT)) \
            .replace(SENTENCE + "\n\n", SENTENCE + "\n")
        self.assertIn(SENTENCE + "\n- **Method:**", text)
        self.assertFails(invariants(text, later()),
                         "*Correction* names %s as the current fingerprint, but it is %s"
                         % (REWORDED_FINGERPRINT, SENTENCE_FINGERPRINT))

class RecoveredList(GuardTestCase):
    """The list of recovered invariants that closes the file: a row names an entry at its current
    version and holds `searched: <…>` and `found: <…>` (WAY-58)."""

    def test_row_of_no_entry(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "save-trip | 1 | searched: the log | found: nothing")),
            "the list of recovered invariants names `save-trip`, which is not an entry")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_row_at_another_version(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 2 | searched: the log | found: nothing")),
            "the list of recovered invariants names `loads-in-later-versions` at version 2; its "
            "current version is 1")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_row_naming_nothing_searched(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 |  | found: nothing")),
            "the row of `loads-in-later-versions` on the list of recovered invariants names "
            "nothing in *Searched*")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_row_naming_nothing_found(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | searched: the log |  ")),
            "the row of `loads-in-later-versions` on the list of recovered invariants names "
            "nothing in *Found*")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_row_naming_nothing_after_searched(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | searched: | found: nothing")),
            "the row of `loads-in-later-versions` on the list of recovered invariants names "
            "nothing in *Searched*")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_row_naming_nothing_after_found(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | searched: the log | found:")),
            "the row of `loads-in-later-versions` on the list of recovered invariants names "
            "nothing in *Found*")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_searched_without_searched(self):
        # invariant: invariant-recovered-form/1
        output = self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | the log | found: nothing")),
            "the row of `loads-in-later-versions` on the list of recovered invariants holds "
            "`the log` in *Searched*, which does not open with `searched:`")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])
        self.assertIn("1 error(s)", output)

    def test_found_without_found(self):
        # invariant: invariant-recovered-form/1
        output = self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | searched: the log | nothing")),
            "the row of `loads-in-later-versions` on the list of recovered invariants holds "
            "`nothing` in *Found*, which does not open with `found:`")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])
        self.assertIn("1 error(s)", output)

    def test_the_words_of_the_other_cell(self):
        # invariant: invariant-recovered-form/1
        output = self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | found: nothing | searched: the log")),
            "the row of `loads-in-later-versions` on the list of recovered invariants holds "
            "`found: nothing` in *Searched*, which does not open with `searched:`")
        self.assertIn("the row of `loads-in-later-versions` on the list of recovered invariants "
                      "holds `searched: the log` in *Found*, which does not open with `found:`",
                      output)
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail", "fail"])

    def test_row_with_a_cell_missing(self):
        # invariant: invariant-recovered-form/1
        self.assertFails(invariants(recovered=recovered(
            "loads-in-later-versions | 1 | searched: the log")),
            "a row of the list of recovered invariants names an identifier, a version, "
            "what was searched and what was found")
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["fail"])

    def test_row_of_an_entry_that_derives_from_a_decision(self):
        # invariant: invariant-recovered-derived/1
        output = self.assertFails(
            invariants(recovered=recovered(
                "loads-in-later-versions | 1 | searched: the log | found: nothing",
                "save-round-trip | 1 | searched: the log | found: nothing")),
            "save-round-trip/1 stands on the list of recovered invariants, while its *Derives "
            "from* names a decision")
        self.assertEqual(self.verdicts("invariant-recovered-derived/1"), ["fail"])
        self.assertEqual(self.verdicts("invariant-recovered-form/1"), ["pass"])
        self.assertIn("1 error(s)", output)


class Verifications(GuardTestCase):
    def log(self, *versions):
        self.write("foundations/decisions.md", "# Decision log\n\n" + "\n".join(versions))

    def test_level_one_decision_with_an_entry_named_that_derives_from_it(self):
        self.log(decision(verification="level 1 — invariants: save-round-trip. Level 2 for the "
                                       "rest — an agent compares the change with the decision."))
        self.assertPasses(invariants())
        self.assertEqual(self.verdicts("level-one-decision-invariants/1"), ["pass"])
        self.assertEqual(self.verdicts("verification-invariant-derivation/1"), ["pass"])

    def test_level_one_decision_no_entry_derives_from(self):
        self.log(decision(verification="level 1 — invariants: loads-in-later-versions."))
        self.assertFails(invariants(entry(derives="none"), later()),
                         "decisions.md:8: WAY-01 is in force and verified at level 1, but no entry "
                         "of the file derives from it")
        self.assertEqual(self.verdicts("level-one-decision-invariants/1"), ["fail"])

    def test_level_two_decision_no_entry_derives_from(self):
        self.log(decision(verification="level 2 — an agent compares the change with the decision."))
        self.assertPasses(invariants(entry(derives="none"), later()))

    def test_repealed_decision_no_entry_derives_from(self):
        self.log(decision(verification="level 1 — invariants: save-round-trip."),
                 decision(2, binding=None, change="repeal",
                          verification="level 2 — an agent compares the change with the decision."))
        self.assertPasses(invariants(entry(derives="none"), later()))
        self.assertEqual(self.verdicts("level-one-decision-invariants/1"), ["pass"])

    def test_repealed_decision_verified_at_level_one_needs_no_entry_deriving_from_it(self):
        self.log(decision(verification="level 1 — invariants: save-round-trip."),
                 decision(2, binding=None, change="repeal",
                          verification="level 1 — invariants: save-round-trip."))
        self.assertFails(invariants(entry(derives="none"), later()),
                         "its *Derives from* does not name WAY-01")
        self.assertEqual(self.verdicts("level-one-decision-invariants/1"), ["pass"])

    def test_verification_names_no_entry(self):
        self.log(decision(verification="level 1 — invariants: save-round-trip · save-trip."))
        self.assertFails(invariants(), "decisions.md:8: the level 1 verification of WAY-01/1 names "
                                       "`save-trip`, which is not an entry of the file")
        self.assertEqual(self.verdicts("verification-invariant-derivation/1"), ["fail"])

    def test_verification_names_an_entry_that_does_not_derive_from_it(self):
        self.log(decision(verification="level 1 — invariants: save-round-trip · "
                                       "loads-in-later-versions."))
        self.assertFails(invariants(), "loads-in-later-versions/1: the level 1 verification of "
                                       "WAY-01/1 names it, but its *Derives from* does not name "
                                       "WAY-01")
        self.assertEqual(self.verdicts("verification-invariant-derivation/1"), ["fail"])

    def test_only_the_latest_version_is_read(self):
        self.log(decision(verification="level 1 — invariants: save-trip."),
                 decision(2, binding=DECISION_REWORDED,
                          verification="level 1 — invariants: save-round-trip."))
        self.assertPasses(invariants(entry(derives="WAY-01@" + DECISION_REWORDED_FINGERPRINT),
                                     later()))

    def test_level_one_verification_off_its_form(self):
        self.log(decision(verification="level 1 — the gate checks it."))
        self.assertFails(invariants(), "decisions.md:8: the level 1 verification of WAY-01/1 names "
                                       "no invariants as")
        self.assertEqual(self.verdicts("verification-invariant-derivation/1"), [])


class Lists(GuardTestCase):
    def quarantine(self, row):
        return QUARANTINE + "\n| %s |" % row

    def test_quarantine_position(self):
        self.assertPasses(invariants(quarantine=self.quarantine("save-round-trip | 1 | 2026-12-31")))

    def test_quarantine_of_no_entry(self):
        self.assertFails(invariants(quarantine=self.quarantine("save-trip | 1 | 2026-12-31")),
                         "quarantine names `save-trip`, which is not an entry")
        self.assertRecorded("quarantine-position-form/1", "fail")

    def test_quarantine_at_another_version(self):
        self.assertFails(invariants(quarantine=self.quarantine("save-round-trip | 2 | 2026-12-31")),
                         "its current version is 1")

    def test_quarantine_without_a_date(self):
        self.assertFails(invariants(quarantine=self.quarantine("save-round-trip | 1 | soon")),
                         "which is not a date YYYY-MM-DD")
        self.assertRecorded("quarantine-position-form/1", "fail")

    def test_quarantine_of_an_invariant_a_critical_flow_names(self):
        self.assertFails(invariants(quarantine=self.quarantine("loads-in-later-versions | 1 | "
                                                               "2026-12-31")),
                         "which a critical flow names")
        self.assertRecorded("quarantine-flow-invariants/1", "fail")

    def test_flow_naming_its_invariant_in_prose(self):
        self.write("foundations/part_map.md", MAP.replace(
            "loads-in-later-versions — test:", "every saved game loads in a later version — test:"))
        output = self.assertPasses(invariants())
        self.assertIn("unchecked: whether a quarantine names the invariant of `save-and-load` — the "
                      "flow names its invariant in prose, not by identifier", output)
        self.assertEqual(self.verdicts("quarantine-flow-invariants/1"), ["pass"])

    def test_flow_naming_its_invariant_in_prose_beside_a_quarantine(self):
        self.write("foundations/part_map.md", MAP.replace(
            "loads-in-later-versions — test:", "every saved game loads in a later version — test:"))
        self.assertPasses(invariants(quarantine=self.quarantine("save-round-trip | 1 | 2026-12-31")))
        self.assertEqual(self.verdicts("quarantine-flow-invariants/1"), [])

    def test_violated_list_with_other_columns(self):
        # invariant: violated-position-version/1
        self.assertFails(invariants(), "the list has columns Id | Ver, not Identifier | Version",
                         violated_text="## Violated invariants\n\n| Id | Ver |\n|---|---|\n")
        self.assertEqual(self.verdicts("violated-position-version/1"), ["fail"])

    def test_violated_position(self):
        self.assertPasses(invariants(), violated_text=violated(("save-round-trip", "1")))

    def test_violated_position_of_no_entry(self):
        self.assertFails(invariants(), "`save-trip` is not an entry",
                         violated_text=violated(("save-trip", "1")))
        self.assertRecorded("violated-position-version/1", "fail")

    def test_violated_position_at_another_version(self):
        self.assertFails(invariants(), "`save-round-trip` at version 2; its current version is 1",
                         violated_text=violated(("save-round-trip", "2")))
        self.assertRecorded("violated-position-version/1", "fail")


class Citations(GuardTestCase):
    def cite(self, *lines):
        self.write("tests/test_other.py", "\n".join(lines) + "\n")

    def test_prose_comments_are_no_citations(self):
        self.write("src/queue.py", "# invariant: head stays below tail\n# data: loaded lazily\n"
                                   "def push():\n    pass\n")
        self.assertPasses(invariants())

    def test_data_line_in_a_file_citing_nothing(self):
        self.write("src/cache.py", "# data: cache/index.json\n")
        self.assertPasses(invariants())

    def test_citation_without_a_version(self):
        self.cite("# invariant: save-round-trip")
        self.assertFails(invariants(), "does not cite `<identifier>/<version>`")
        self.assertEqual(self.verdicts("invariant-citation-version/1"), ["fail"])
        self.assertEqual(self.verdicts("invariant-citation-target/1"), ["pass"])

    def test_citation_of_a_version_with_a_leading_zero(self):
        self.cite("# invariant: save-round-trip/01")
        self.assertFails(invariants(), "`invariant: save-round-trip/01` does not cite "
                                       "`<identifier>/<version>`")
        self.assertEqual(self.verdicts("invariant-citation-version/1"), ["fail"])

    def test_citation_of_another_version(self):
        self.cite("// invariant: save-round-trip/2")
        self.assertFails(invariants(), "cites `save-round-trip/2`, whose current version is 1")
        self.assertEqual(self.verdicts("invariant-citation-version/1"), ["fail"])

    def test_citation_of_no_entry(self):
        self.cite("# invariant: save-trip/1")
        self.assertFails(invariants(), "cites `save-trip`, which is not an entry")
        self.assertEqual(self.verdicts("invariant-citation-target/1"), ["fail"])

    def test_citation_of_a_withdrawn_identifier(self):
        self.cite("# invariant: save-format/1")
        self.assertFails(invariants(), "cites `save-format`, which is withdrawn (successors: "
                                       "save-round-trip)")
        self.assertEqual(self.verdicts("invariant-citation-target/1"), ["fail"])

    def test_data_line_naming_no_file(self):
        self.cite("# invariant: save-round-trip/1", "# data: tests/missing.json")
        self.assertFails(invariants(), "`data: tests/missing.json` names no file")
        self.assertEqual(self.verdicts("data-line-target/1"), ["fail"])


class RecordPaths(GuardTestCase):
    def command(self, arguments):
        return "`python -B tools/check.py %s`" % arguments

    def test_record_in_a_folder_git_ignores(self):
        self.write(".gitignore", ".runs/\n")
        self.assertPasses(invariants(entry(method=self.command("--record .runs/saving.jsonl")),
                                     later(method=self.command("--record .runs/saving.jsonl"))))
        self.assertEqual(self.verdicts("run-record-path/1"), ["pass"])

    def test_record_git_does_not_ignore(self):
        self.write(".gitignore", "build/\n")
        self.assertFails(invariants(entry(method=self.command("--record .runs/saving.jsonl")),
                                    later()),
                         "save-round-trip/1: git does not ignore `.runs/saving.jsonl`")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_record_letter_case_counts_where_git_ignores_it(self):
        self.git("config", "core.ignorecase", "true")
        self.write(".gitignore", ".runs/\n")
        self.assertFails(invariants(entry(method=self.command("--record .Runs/saving.jsonl")),
                                    later()),
                         "save-round-trip/1: git does not ignore `.Runs/saving.jsonl`")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_record_git_tracks(self):
        self.write(".gitignore", "*.jsonl\n")
        self.write("records/saving.jsonl", "{}\n")
        self.git("add", "-f", "records/saving.jsonl")
        self.assertFails(invariants(entry(method=self.command("--record records/saving.jsonl")),
                                    later()),
                         "git does not ignore `records/saving.jsonl`")

    def test_record_outside_the_repository(self):
        self.assertFails(invariants(entry(method=self.command("--record ../saving.jsonl")),
                                    later()),
                         "`../saving.jsonl` lies outside the repository")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_command_naming_two_records(self):
        self.write(".gitignore", ".runs/\n")
        self.assertFails(invariants(entry(method=self.command("--record .runs/a.jsonl --out "
                                                              ".runs/b.jsonl")), later()),
                         "save-round-trip/1: the command names 2 records of a run "
                         "(`.runs/a.jsonl`, `.runs/b.jsonl`); it names one")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])


class FactRecordPaths(GuardTestCase):
    """The commands of the environment facts beside the file name their records of a run under
    the same rule as the invariants' own (WAY-74)."""

    def facts(self, arguments):
        self.write("foundations/environment_facts.md", FACTS.replace(
            "- **Method:** `TODO`", "- **Method:** `python -B probes/quota.py %s`" % arguments))

    def test_record_of_a_fact_in_a_folder_git_ignores(self):
        # invariant: run-record-path/1
        self.write(".gitignore", ".runs/\n")
        self.facts("--record .runs/quota.jsonl")
        self.assertPasses(invariants())
        self.assertEqual(self.verdicts("run-record-path/1"), ["pass"])

    def test_record_of_a_fact_git_does_not_ignore(self):
        # invariant: run-record-path/1
        self.write(".gitignore", "build/\n")
        self.facts("--record .runs/quota.jsonl")
        self.assertFails(invariants(), "environment_facts.md:9: storage-quota/1: git does not "
                                       "ignore `.runs/quota.jsonl`")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_record_of_a_fact_outside_the_repository(self):
        # invariant: run-record-path/1
        self.facts("--record ../quota.jsonl")
        self.assertFails(invariants(), "environment_facts.md:9: storage-quota/1: "
                                       "`../quota.jsonl` lies outside the repository")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_fact_command_naming_two_records(self):
        # invariant: run-record-path/1
        self.write(".gitignore", ".runs/\n")
        self.facts("--record .runs/a.jsonl --out .runs/b.jsonl")
        self.assertFails(invariants(), "environment_facts.md:9: storage-quota/1: the command names "
                                       "2 records of a run (`.runs/a.jsonl`, `.runs/b.jsonl`); it "
                                       "names one")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])


class AgainstTheBranchPoint(GuardTestCase):
    def test_unchanged_file_passes(self):
        self.commit(invariants())
        output = self.assertPasses(invariants(), base="HEAD")
        self.assertNotIn("no --base given", output)

    def test_base_that_does_not_exist(self):
        self.commit(invariants())
        self.assertFails(invariants(), "--base nowhere does not exist", base="nowhere")
        self.assertEqual(self.lines, [{"check": GUARD, "verdict": "fail", "invariant": None,
                                       "description": "--base nowhere does not exist"}])

    def test_new_entry_above_version_1(self):
        self.commit(invariants(entry(), withdrawn=WITHDRAWN))
        self.assertFails(invariants(entry(), later(version=2)),
                         "loads-in-later-versions/2: a new entry carries version 1", base="HEAD")
        self.assertRecorded("invariant-version-new/1", "fail")

    def test_identifier_dropped(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(), recovered=recovered()),
                         "`loads-in-later-versions` stands in the file on HEAD and is gone",
                         base="HEAD")
        self.assertEqual(self.verdicts("invariant-identifier-persistence/1"), ["fail"])
        self.assertEqual(self.verdicts("invariant-withdrawal-persistence/1"), ["pass"])

    def test_withdrawn_identifier_dropped(self):
        self.commit(invariants())
        self.assertFails(invariants(withdrawn=WITHDRAWN.replace("| save-format | merged with another entry | save-round-trip |",
                                                                "| save-slot | dropped | none |")),
                         "`save-format` stands in the file on HEAD and is gone", base="HEAD")
        self.assertEqual(self.verdicts("invariant-withdrawal-persistence/1"), ["fail"])
        self.assertEqual(self.verdicts("invariant-identifier-persistence/1"), ["fail"])

    def test_identifier_withdrawn_there_is_an_entry_again(self):
        self.commit(invariants())
        text = invariants(entry(), later(), entry("save-format", sentence="A save file names its "
                                                  "format version."),
                          withdrawn=WITHDRAWN.replace("| save-format | merged with another entry | save-round-trip |",
                                                      "| save-slot | dropped | none |"))
        self.assertFails(text, "`save-format` is withdrawn on HEAD and stands as an entry again",
                         base="HEAD")
        self.assertRecorded("invariant-withdrawal-persistence/1", "fail")

    def test_changed_sentence_at_the_same_version(self):
        # invariant: invariant-fingerprint-input/1
        self.commit(invariants())
        self.assertFails(invariants(entry(sentence=REWORDED), later()),
                         "the sentence changed since HEAD (%s → %s); the version is 2"
                         % (SENTENCE_FINGERPRINT, REWORDED_FINGERPRINT), base="HEAD")
        self.assertRecorded("invariant-version-changed/1", "fail")

    def test_changed_sentence_at_a_raised_version(self):
        self.commit(invariants())
        self.write("tests/test_saving.py", "# invariant: save-round-trip/2\n"
                                           "# data: tests/saved_game.json\n")
        self.assertPasses(invariants(entry(version=2, sentence=REWORDED), later()), base="HEAD")

    def test_raised_version_leaves_its_citing_test_behind(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(version=2, sentence=REWORDED), later()),
                         "cites `save-round-trip/1`, whose current version is 2", base="HEAD")

    def test_changed_sentence_declared_a_correction(self):
        self.commit(invariants())
        correction = "%s → %s" % (SENTENCE_FINGERPRINT, REWORDED_FINGERPRINT)
        output = self.assertPasses(invariants(entry(sentence=REWORDED, correction=correction),
                                              later()), base="HEAD")
        self.assertIn("unchecked: the correction of `save-round-trip` — correction declared, "
                      "confirmation not checked", output)
        # the record gives the sentence as written its verdict; the confirmation has no entry yet
        self.assertEqual(self.verdicts("invariant-version-changed/1"), ["pass"])

    def test_raised_version_declaring_a_correction(self):
        self.commit(invariants())
        self.write("tests/test_saving.py", "# invariant: save-round-trip/2\n")
        correction = "%s → %s" % (SENTENCE_FINGERPRINT, REWORDED_FINGERPRINT)
        self.assertFails(invariants(entry(version=2, sentence=REWORDED, correction=correction),
                                    later()), "a raised version declares no correction", base="HEAD")
        self.assertRecorded("invariant-version-changed/1", "fail")

    def test_unchanged_sentence_at_a_raised_version(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(version=2), later()),
                         "the sentence is unchanged since HEAD, where the version is 1", base="HEAD")
        self.assertRecorded("invariant-version-unchanged/1", "fail")

    def test_change_outside_the_sentence_keeps_the_version(self):
        self.commit(invariants())
        self.assertPasses(invariants(entry(part="every"), later()), base="HEAD")

    def test_old_wording_kept_beside_the_new(self):
        self.commit(invariants())
        kept = entry(version=2, sentence=REWORDED) + "\n\nEarlier: " + SENTENCE
        self.assertFails(invariants(kept, later()), "still holds its wording from HEAD",
                         base="HEAD")
        self.assertRecorded("invariant-earlier-wording/1", "fail")

    def test_violated_list_grows(self):
        self.commit(invariants(), violated_text=violated())
        self.assertFails(invariants(), "`save-round-trip` at version 1 is not on the list on HEAD",
                         base="HEAD", violated_text=violated(("save-round-trip", "1")))
        self.assertEqual(self.verdicts("violated-list-growth/1"), ["fail"])

    def test_violated_list_shrinks(self):
        self.commit(invariants(), violated_text=violated(("save-round-trip", "1")))
        self.assertPasses(invariants(), base="HEAD", violated_text=violated())
        self.assertEqual(self.verdicts("violated-list-growth/1"), ["pass"])


class BaseNone(GuardTestCase):
    def test_none_records_the_checks_against_the_base_unchecked(self):
        code, output = self.guard(invariants(), base="none")
        self.assertEqual(code, 0, output)
        self.assertIn("note: --base none: there is no commit the branch left the main branch from",
                      output)
        self.assertEqual(sorted(line["invariant"] for line in self.lines), BASE)
        for line in self.lines:
            self.assertEqual((line["verdict"], line["reason"]), ("unchecked", NO_COMMIT))

    def test_none_gives_no_error_where_the_file_would_fail_against_a_base(self):
        self.commit(invariants())
        code, output = self.guard(invariants(entry(), recovered=recovered()), base="none")
        self.assertEqual(code, 0, output)
        self.assertNotIn("is gone", output)

    def test_none_records_no_failure_for_no_entry(self):
        self.guard(invariants(), base="none")
        self.assertEqual([line for line in self.lines if line["invariant"] is None], [])


class MergeOntoNone(GuardTestCase):
    def test_none_records_the_checks_of_a_merge_unchecked(self):
        code, output = self.guard(invariants(entry(derives="`TODO — a decision on saves`"),
                                             later()), merge_onto="none")
        self.assertEqual(code, 0, output)
        self.assertIn("note: --merge-onto none: there is no commit to merge onto", output)
        self.assertEqual(sorted(line["invariant"] for line in self.lines), MERGE)
        for line in self.lines:
            self.assertEqual((line["verdict"], line["reason"]), ("unchecked", NO_COMMIT))

    def test_a_commit_that_does_not_exist_stays_an_error(self):
        self.commit(invariants())
        self.assertFails(invariants(), "--merge-onto nowhere does not exist", merge_onto="nowhere")
        self.assertEqual(self.lines, [{"check": GUARD, "verdict": "fail", "invariant": None,
                                       "description": "--merge-onto nowhere does not exist"}])


class MergeTodo(GuardTestCase):
    def test_todo_in_derives_from_fails_a_merge(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(derives="`TODO — a decision on saves`"), later()),
                         "save-round-trip/1: *Derives from* holds `TODO`, which a merge onto the "
                         "main branch does not take", merge_onto="HEAD")
        self.assertEqual(self.verdicts("invariant-entry-merge-todo/1"), ["fail"])

    def test_todo_in_a_field_the_form_does_not_give_it_fails_a_merge(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(part="TODO"), later()),
                         "save-round-trip/1: *Part* holds `TODO`, which a merge onto the main "
                         "branch does not take", merge_onto="HEAD")
        self.assertEqual(self.verdicts("invariant-entry-merge-todo/1"), ["fail"])

    def test_todo_inside_a_part_of_a_value_fails_a_merge(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(part="saving (TODO: loading)"), later()),
                         "save-round-trip/1: *Part* holds `TODO`, which a merge onto the main "
                         "branch does not take", merge_onto="HEAD")
        self.assertEqual(self.verdicts("invariant-entry-merge-todo/1"), ["fail"])

    def test_todo_in_method_and_rests_on_passes_a_merge(self):
        self.commit(invariants())
        self.assertPasses(invariants(entry(method="`TODO`", rests="TODO — the store keeps 5 MB, "
                                           "per its documentation"), later()), merge_onto="HEAD")
        self.assertEqual(self.verdicts("invariant-entry-merge-todo/1"), ["pass"])

    def test_no_todo_passes_a_merge(self):
        self.commit(invariants())
        self.assertPasses(invariants(), merge_onto="HEAD")
        self.assertEqual(sorted(line["invariant"] for line in self.lines), MERGE)
        self.assertEqual({line["verdict"] for line in self.lines}, {"pass"})


class Fingerprints(GuardTestCase):
    def test_stale_fingerprint_fails_a_merge(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(derives="WAY-01@00000000"), later()),
                         "save-round-trip/1: `WAY-01@00000000` — the current fingerprint of WAY-01 "
                         "after the merge is 4dd7fb86", merge_onto="HEAD")
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), ["fail"])

    def test_decision_reworded_on_the_commit_merged_onto(self):
        self.write("foundations/decisions.md", LOG + "\n" + decision(2, binding=DECISION_REWORDED))
        self.commit(invariants())
        self.write("foundations/decisions.md", LOG)
        self.assertFails(invariants(), "save-round-trip/1: `WAY-01@4dd7fb86` — the current "
                                       "fingerprint of WAY-01 after the merge is 4b7b9b75",
                         merge_onto="HEAD")
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), ["fail"])

    def test_decision_reworded_on_the_branch(self):
        self.commit(invariants())
        self.write("foundations/decisions.md", LOG + "\n" + decision(2, binding=DECISION_REWORDED))
        self.assertPasses(invariants(entry(derives="WAY-01@4b7b9b75"), later()),
                          merge_onto="HEAD")

    def test_entry_the_commit_merged_onto_alone_holds(self):
        self.commit(invariants(entry(), later(), entry("loads-fast", sentence="A saved game loads "
                                                       "in one second.", part="loading",
                                                       derives="WAY-01@00000000")))
        self.assertFails(invariants(), "loads-fast/1 (on HEAD): `WAY-01@00000000` — the current "
                                       "fingerprint of WAY-01 after the merge is 4dd7fb86",
                         merge_onto="HEAD")

    def test_named_fact_fails_a_merge(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(rests="storage-quota@1234abcd"), later()),
                         "`storage-quota@1234abcd` in *Rests on* names no environment fact the "
                         "merge holds", merge_onto="HEAD")
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), ["fail"])


class Record(GuardTestCase):
    def test_plain_run_records_the_checks_of_the_file_alone(self):
        self.assertPasses(invariants())
        self.assertEqual(sorted(line["invariant"] for line in self.lines), PLAIN)
        self.assertEqual({line["verdict"] for line in self.lines}, {"pass"})

    def test_a_line_names_the_program_and_its_check(self):
        self.assertPasses(invariants())
        self.assertIn({"check": GUARD + "::check_sentence", "verdict": "pass",
                       "invariant": "invariant-sentence-count/1"}, self.lines)

    def test_run_against_the_base_records_its_checks_alone(self):
        self.commit(invariants())
        self.assertPasses(invariants(), base="HEAD")
        self.assertEqual(sorted(line["invariant"] for line in self.lines), BASE)

    def test_run_against_the_base_leaves_out_failures_of_the_file_alone(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(part="saving · cloud"), later()),
                         "names `cloud`", base="HEAD")
        self.assertEqual([line for line in self.lines if line["verdict"] == "fail"], [])

    def test_failure_for_no_entry(self):
        self.assertFails(invariants(entry(), later(), "## Notes\n\nSome notes."),
                         "heading `## Notes` is neither")
        self.assertIn({"check": GUARD + "::check_layout", "verdict": "fail", "invariant": None,
                       "description": "line 23: heading `## Notes` is neither "
                                      "`## <identifier>/<version>` nor a list of the template"},
                      self.lines)

    def test_record_when_the_template_cannot_be_read(self):
        self.write("broken_template.md", "# Template\n\n## Entry\n\nNothing here.\n")
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output, record=self.record_path,
                                template=os.path.join(self.root, "broken_template.md"))
        self.assertEqual(code, 2)
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual([(line["check"], line["verdict"], line["invariant"]) for line in lines],
                         [(GUARD, "fail", None)])

    def test_file_outside_a_git_repository_is_a_failure_of_the_run(self):
        with tempfile.TemporaryDirectory() as loose:
            for name, content in (("foundations/part_map.md", MAP),
                                  ("foundations/decisions.md", LOG),
                                  ("foundations/invariants.md", invariants())):
                os.makedirs(os.path.join(loose, "foundations"), exist_ok=True)
                with open(os.path.join(loose, *name.split("/")), "w", encoding="utf-8",
                          newline="\n") as handle:
                    handle.write(content)
            output = io.StringIO()
            code = format_guard.run(os.path.join(loose, "foundations", "invariants.md"),
                                    stream=output, record=self.record_path)
        self.assertEqual(code, 1, output.getvalue())
        self.assertIn("the file does not lie in a git repository", output.getvalue())
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        recorded = {line["invariant"] for line in lines}
        for invariant in ("invariants-file/1", "invariant-citation-target/1", "run-record-path/1"):
            self.assertNotIn(invariant, recorded)
        self.assertIn({"check": GUARD, "verdict": "fail", "invariant": None,
                       "description": "the file does not lie in a git repository, so no check "
                                      "that asks git which files it tracks or ignores can run"},
                      lines)

    def test_outside_a_git_repository_the_failure_stands_in_every_record(self):
        """A failed call to git is a failure of the run, not of a check an option selects, so the
        records of --base none and --merge-onto none hold it too (WAY-63)."""
        failure = {"check": GUARD, "verdict": "fail", "invariant": None,
                   "description": "the file does not lie in a git repository, so no check that "
                                  "asks git which files it tracks or ignores can run"}
        for option in ("base", "merge_onto"):
            with self.subTest(option), tempfile.TemporaryDirectory() as loose:
                os.makedirs(os.path.join(loose, "foundations"))
                for name, content in (("part_map.md", MAP), ("decisions.md", LOG),
                                      ("invariants.md", invariants())):
                    with open(os.path.join(loose, "foundations", name), "w", encoding="utf-8",
                              newline="\n") as handle:
                        handle.write(content)
                output = io.StringIO()
                code = format_guard.run(os.path.join(loose, "foundations", "invariants.md"),
                                        stream=output, record=self.record_path,
                                        **{option: "none"})
                with open(self.record_path, encoding="utf-8") as handle:
                    lines = [json.loads(item) for item in handle.read().split("\n") if item]
                self.assertEqual(code, 1, output.getvalue())
                self.assertIn(failure, lines)
                self.assertEqual([line for line in lines
                                  if line != failure and line["verdict"] != "unchecked"], [])


class Unreadable(GuardTestCase):
    def test_invariants_file_that_is_not_utf_8(self):
        with open(self.path, "wb") as handle:
            handle.write(b"# Invariants\n\ncaf\xe9\n")
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output, record=self.record_path,
                                base="none")
        self.assertEqual(code, 2, output.getvalue())
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(len(lines), 1, lines)
        self.assertEqual({key: lines[0][key] for key in ("check", "verdict", "invariant")},
                         {"check": GUARD, "verdict": "fail", "invariant": None})
        self.assertTrue(lines[0]["description"].startswith("cannot read the invariants file: "
                                                           "'utf-8' codec can't decode"), lines)

    def test_decision_log_beside_it_that_is_not_utf_8(self):
        with open(os.path.join(self.root, "foundations", "decisions.md"), "wb") as handle:
            handle.write(b"# Decision log\n\ncaf\xe9\n")
        code, output = self.guard(invariants(), merge_onto="none")
        self.assertEqual(code, 1, output)
        failures = [line for line in self.lines if line["invariant"] is None]
        self.assertEqual([line["check"] for line in failures], [GUARD], self.lines)
        self.assertTrue(failures[0]["description"].startswith(
            "cannot read the decision log beside the file: 'utf-8' codec can't decode"),
            failures)

    def test_missing_file(self):
        output = io.StringIO()
        self.assertEqual(format_guard.run(self.path, stream=output), 2)
        self.assertIn("cannot read the invariants file", output.getvalue())

    def test_template_without_the_entry_form(self):
        self.write("broken_template.md", "# Template\n\n## Entry\n\nNothing here.\n")
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output,
                                template=os.path.join(self.root, "broken_template.md"))
        self.assertEqual(code, 2)
        self.assertIn("cannot read the rules", output.getvalue())

    def test_rules_the_elements_share_without_the_list_of_withdrawn_identifiers(self):
        self.write("broken_rules.md", "# Rules of form the elements share\n\n## Language\n\nEnglish.\n")
        self.write("foundations/invariants.md", invariants())
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output,
                                common=os.path.join(self.root, "broken_rules.md"))
        self.assertEqual(code, 2)
        self.assertIn("cannot read the rules", output.getvalue())


class FactsBeside(GuardTestCase):
    """The file of environment facts beside the invariants, once it has entries (WAY-31, WAY-75)."""

    def setUp(self):
        super().setUp()
        self.write("foundations/environment_facts.md", FACTS)

    def test_facts_file_is_no_second_file_of_invariants(self):
        # invariant: invariants-file/1
        self.assertPasses(invariants())
        self.assertEqual(self.verdicts("invariants-file/1"), ["pass"])

    def test_rests_on_a_fact_entry(self):
        # invariant: link-fingerprint-presence/1
        self.assertPasses(invariants(entry(rests="storage-quota@" + FACT_FINGERPRINT), later()))
        self.assertEqual(self.verdicts("link-fingerprint-presence/1"), ["pass"])

    def test_rests_on_a_fact_without_a_fingerprint(self):
        # invariant: link-fingerprint-presence/1
        self.assertFails(invariants(entry(rests="storage-quota"), later()),
                         "`storage-quota` in *Rests on* carries no fingerprint of 8 hex digits; it "
                         "reads `<fact>@<fingerprint>`")
        self.assertEqual(self.verdicts("link-fingerprint-presence/1"), ["fail"])

    def test_rests_on_a_withdrawn_fact(self):
        self.assertFails(invariants(entry(rests="storage-limit@1234abcd"), later()),
                         "*Rests on* names `storage-limit`, a withdrawn environment fact")

    def test_rests_on_no_fact(self):
        self.assertFails(invariants(entry(rests="storage-cap@1234abcd"), later()),
                         "*Rests on* names `storage-cap`, which is not an entry of the environment "
                         "facts")

    def test_identifier_held_by_a_fact(self):
        # invariant: identifier-holders/1
        self.assertFails(invariants(entry(), later(identifier="storage-quota")),
                         "identifier `storage-quota` is held by the environment facts (line 3)")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_identifier_withdrawn_from_the_facts(self):
        # invariant: identifier-holders/1
        self.assertFails(invariants(entry(), later(identifier="storage-limit")),
                         "identifier `storage-limit` is held by the environment facts")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_stale_fingerprint_of_a_fact_fails_a_merge(self):
        # invariant: link-fingerprint-value/1
        self.commit(invariants())
        self.assertFails(invariants(entry(rests="storage-quota@1234abcd"), later()),
                         "`storage-quota@1234abcd` — the current fingerprint of `storage-quota` "
                         "after the merge is " + FACT_FINGERPRINT, merge_onto="HEAD")
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), ["fail"])

    def test_current_fingerprint_of_a_fact_passes_a_merge(self):
        # invariant: link-fingerprint-value/1
        self.commit(invariants())
        self.assertPasses(invariants(entry(rests="storage-quota@" + FACT_FINGERPRINT), later()),
                          merge_onto="HEAD")
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), ["pass"])

    def test_identifier_held_twice_in_the_facts(self):
        # invariant: identifier-holders/1
        self.write("foundations/environment_facts.md", FACTS.replace(
            "| storage-limit | split", "| storage-quota | shown false | none |\n| storage-limit | split"))
        self.assertFails(invariants(), "identifier `storage-quota` is held twice in the environment "
                                       "facts")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_fact_held_by_the_part_map(self):
        # invariant: identifier-holders/1
        self.write("foundations/environment_facts.md", FACTS.replace("storage-limit", "saving"))
        self.assertFails(invariants(), "environment_facts.md:15: identifier `saving` is held by the "
                                       "part map")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_todo_in_rests_on_warns_once_facts_have_entries(self):
        # invariant: invariant-entry-field-words/1
        code, output = self.guard(invariants(entry(rests="TODO — the store keeps 5 MB"), later()))
        self.assertEqual(code, 0, output)
        self.assertIn("save-round-trip/1: *Rests on* holds `TODO`, which a merge onto the main "
                      "branch does not take", output)
        self.assertEqual(self.verdicts("invariant-entry-field-words/1"), ["pass"])

    def test_fact_the_main_branch_raised_and_the_branch_left_alone(self):
        # invariant: link-fingerprint-value/1
        self.commit(invariants(entry(rests="storage-quota@" + FACT_FINGERPRINT), later()))
        self.git("checkout", "-q", "-b", "task")
        self.git("checkout", "-q", "main")
        self.write("foundations/environment_facts.md", FACTS.replace(
            "## storage-quota/1", "## storage-quota/2").replace("Firefox 130", "Firefox 131"))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "raise")
        self.git("checkout", "-q", "task")
        self.assertFails(invariants(entry(rests="storage-quota@" + FACT_FINGERPRINT), later()),
                         "`storage-quota@%s` — the current fingerprint of `storage-quota` after the "
                         "merge is" % FACT_FINGERPRINT, merge_onto="main")
        self.assertEqual(self.verdicts("link-fingerprint-value/1"), ["fail"])

    def test_successors_none_in_backticks(self):
        # invariant: withdrawal-successors/1
        self.assertPasses(invariants(entry(), later(), withdrawn=WITHDRAWN.replace(
            "| save-round-trip |", "| `none` |")))
        self.assertEqual(self.verdicts("withdrawal-successors/1"), ["pass"])

    def test_todo_in_rests_on_fails_a_merge_once_facts_have_entries(self):
        # invariant: invariant-entry-merge-todo/1
        self.commit(invariants())
        self.assertFails(invariants(entry(rests="TODO — the store keeps 5 MB"), later()),
                         "*Rests on* holds `TODO`, which a merge onto the main branch does not take "
                         "once the environment facts element has entries", merge_onto="HEAD")
        self.assertEqual(self.verdicts("invariant-entry-merge-todo/1"), ["fail"])


class HumanVerdicts(GuardTestCase):
    def row(self, **changes):
        values = dict(entry="save-round-trip", version="1", verdict="pass", by="Mariusz",
                      on="2026-09-26", commit="b06eacd", until="none")
        values.update(changes)
        return tuple(values[name] for name in ("entry", "version", "verdict", "by", "on", "commit",
                                               "until"))

    def check(self, row, fragment=None, method="docs/review_checklist.md"):
        # every test calling this cites human-verdict-invariant-row, whose verdict it asserts
        self.write("foundations/human_verdicts.md", human_verdicts(row))
        text = invariants(entry(method=method), later())
        if fragment is None:
            self.assertPasses(text)
            self.assertEqual(self.verdicts("human-verdict-invariant-row/1"), ["pass"])
        else:
            self.assertFails(text, fragment)
            self.assertEqual(self.verdicts("human-verdict-invariant-row/1"), ["fail"])

    def test_no_file(self):
        # invariant: human-verdict-invariant-row/1
        output = self.assertPasses(invariants())
        self.assertIn("note: there is no human_verdicts.md", output)
        self.assertEqual(self.verdicts("human-verdict-invariant-row/1"), ["pass"])

    def test_row_in_its_form(self):
        # invariant: human-verdict-invariant-row/1
        self.check(self.row())

    def test_row_for_an_invariant_whose_method_is_a_command(self):
        # invariant: human-verdict-invariant-row/1
        self.check(self.row(), "human_verdicts.md:5: the method of `save-round-trip` is not a path",
                   method="`python -m unittest tests/test_saving.py`")

    def test_row_for_an_invariant_whose_method_is_prose(self):
        # invariant: human-verdict-invariant-row/1
        self.write("foundations/human_verdicts.md", human_verdicts(self.row()))
        self.assertFails(invariants(entry(method="ask the reviewer"), later()),
                         "the method of `save-round-trip` is not a path")
        self.assertEqual(self.verdicts("human-verdict-invariant-row/1"), ["fail"])

    def test_verdict_neither_pass_nor_fail(self):
        # invariant: human-verdict-invariant-row/1
        self.check(self.row(verdict="holds"), "*Verdict* is neither `pass` nor `fail`")

    def test_until_a_date(self):
        # invariant: human-verdict-invariant-row/1
        self.check(self.row(until="2026-12-31"), "an invariant's verdict reads `none` in *Until*")

    def test_row_naming_a_fact_is_the_facts_guards(self):
        # invariant: human-verdict-invariant-row/1
        self.write("foundations/environment_facts.md", FACTS)
        self.check(self.row(entry="storage-quota", until="2026-12-31"))

    def test_row_naming_neither(self):
        """A row reading `none` in *Until* has an invariant's form (rules.md), so one that names no
        entry of either file is an invariant row naming no invariant."""
        # invariant: human-verdict-invariant-row/1
        self.write("foundations/human_verdicts.md", human_verdicts(self.row(entry="storage-cap")))
        self.assertFails(invariants(), "`storage-cap` is neither an invariant nor an environment "
                                       "fact")
        self.assertEqual(self.verdicts("human-verdict-invariant-row/1"), ["fail"])

    def test_row_naming_neither_with_a_date_in_until_is_the_facts_guards(self):
        """A row carrying a date in *Until* has a fact's form; one that names no entry of either
        file is reported, and the facts guard judges it as a fact row."""
        # invariant: human-verdict-invariant-row/1
        self.write("foundations/human_verdicts.md",
                   human_verdicts(self.row(entry="storage-cap", until="2026-12-31")))
        self.assertFails(invariants(), "`storage-cap` is neither an invariant nor an environment "
                                       "fact")
        self.assertEqual(self.verdicts("human-verdict-invariant-row/1"), ["pass"])

    def test_list_with_other_columns(self):
        self.write("foundations/human_verdicts.md", "| Entry | Verdict |\n|---|---|\n"
                                                    "| save-round-trip | pass |\n")
        self.assertFails(invariants(), "the list has columns Entry | Verdict")


class Examples(GuardTestCase):
    """`examples.md` names, by identifier, entries of the-way's own invariants, which the guard
    checks on that file alone."""

    def examples(self, *items):
        path = os.path.join(self.root, "examples.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("# Examples\n\nThe entries of `foundations/invariants.md` that show the "
                         "form of an entry.\n\n" + "\n".join(items) + "\n")
        return path

    def failures(self, invariant):
        return [line["description"] for line in self.lines
                if line["invariant"] == invariant and line["verdict"] == "fail"]

    def test_identifiers_of_entries_pass(self):
        # invariant: invariant-example-target/1
        self.assertPasses(invariants(), own=True, examples=self.examples(
            "- `save-round-trip` — a method that runs the tests of the product",
            "- `loads-in-later-versions` — an entry on the list of recovered invariants"))
        self.assertIn({"check": GUARD + "::check_examples", "verdict": "pass",
                       "invariant": "invariant-example-target/1"}, self.lines)

    def test_an_identifier_outside_the_file(self):
        # invariant: invariant-example-target/1
        self.assertFails(invariants(), "is not the identifier of an entry", own=True,
                         examples=self.examples("- `save-round-trip` — an entry",
                                                "- `save-trip` — an entry"))
        self.assertEqual(self.failures("invariant-example-target/1"),
                         ["examples.md:6: `save-trip` is not the identifier of an entry of the "
                          "file"])

    def test_a_withdrawn_identifier_is_no_entry(self):
        # invariant: invariant-example-target/1
        self.assertFails(invariants(), "is not the identifier of an entry", own=True,
                         examples=self.examples("- save-format — an entry"))
        self.assertEqual(self.failures("invariant-example-target/1"),
                         ["examples.md:5: `save-format` is not the identifier of an entry of the "
                          "file"])

    def test_an_identifier_with_its_version_is_no_identifier(self):
        # invariant: invariant-example-target/1
        self.assertFails(invariants(), "is not the identifier of an entry", own=True,
                         examples=self.examples("- `save-round-trip/1` — an entry"))
        self.assertEqual(self.failures("invariant-example-target/1"),
                         ["examples.md:5: `save-round-trip/1` is not the identifier of an entry "
                          "of the file"])

    def test_a_copied_entry_names_no_identifier_of_the_file(self):
        # invariant: invariant-example-target/1
        self.assertFails(invariants(), "is not the identifier of an entry", own=True,
                         examples=self.examples("## save-round-trip/1", "", SENTENCE, "",
                                                "- **Method:** `TODO`"))
        self.assertEqual(self.failures("invariant-example-target/1"),
                         ["examples.md:9: `**Method:**` is not the identifier of an entry of the "
                          "file"])

    def test_examples_are_checked_on_the_way_s_own_file_alone(self):
        self.assertPasses(invariants(), examples=self.examples("- `save-trip` — an entry"))
        self.assertNotIn("invariant-example-target/1", [line["invariant"] for line in self.lines])


class OwnFile(unittest.TestCase):
    """The entries of the-way's invariants still carry *Recovered*, which is not a field of the
    form, and which the guard reports in one place only: a *Recovered* line in an entry. Once the
    entries are rewritten in the new form, the file passes with no error."""

    OLD_FORM = re.compile(r"^line \d+: [a-z0-9-]+/\d+: \*Recovered\* is not a field of the "
                          r"form; a recovered invariant stands on the list of recovered "
                          r"invariants$")

    def test_the_way_invariants_hold_no_error_but_the_old_form(self):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            record = os.path.join(directory, "invariants.jsonl")
            code = format_guard.run(format_guard.OWN_FILE, stream=output, record=record)
            with open(record, encoding="utf-8") as handle:
                lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertIn(code, (0, 1), output.getvalue())
        self.assertEqual(sorted({item["invariant"] for item in lines if item["invariant"]}),
                         sorted(PLAIN + ["invariant-example-target/1"]))
        failures = [item for item in lines if item["verdict"] == "fail"]
        self.assertEqual([item for item in failures
                          if not self.OLD_FORM.search(item["description"])], [])
        self.assertEqual(code == 1, bool(failures))


if __name__ == "__main__":
    unittest.main()
