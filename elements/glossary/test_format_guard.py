"""Tests of the glossary guard: every check fires on a file broken on purpose.

Run from the root of the-way:
    python -B gate/run_tests.py elements/glossary --record .runs/glossary-tests.jsonl

Inputs and expected record lines are written out, never computed by the code under test (WAY-70).
Each test repository holds its own element template, given to the guard in place of the-way's, so
that the words of the-way's templates do not reach the counts.
"""

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402

NO_COMMIT = "the method takes a commit the gate filled in as not existing"

SLOT = "A save slot is the storage that holds one saved game."
RUN = "A run is one play of the game from its start to the player's death."


def entry(term="save slot", definition=SLOT, avoid="storage cell — the same storage",
          not_="none", heading=None, omit=(), extra=()):
    lines = [heading or "## %s" % term, ""]
    if definition is not None:
        lines += [definition, ""]
    fields = [("Avoid", avoid), ("Not", not_)] + list(extra)
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def run_entry(**changes):
    values = dict(term="run", definition=RUN, avoid="none",
                  not_="a check the gate makes — `saving-check`")
    values.update(changes)
    return entry(**values)


def glossary(*entries, head="# Glossary\n\nThe words of the game, each in one meaning."):
    return head + "\n\n" + "\n\n".join(list(entries) or [entry(), run_entry()]) + "\n"


MAP = "\n".join([
    "# Part map", "",
    "## saving — Saving a game", "", "The part answers for writing and reading a saved game.", "",
    "- **Files:** src/saving.py", "- **Depends on:** none", "- **Failure modes:** none",
    "- **Trust boundary:** none", "",
    "## glossary — The glossary", "", "The part answers for the words of the game.", "",
    "- **Files:** elements/glossary/**", "- **Depends on:** none", "- **Failure modes:** none",
    "- **Trust boundary:** none", "",
    "## Withdrawn identifiers", "", "| Identifier | Successors |", "|---|---|",
    "| game-state | saving |", ""])


def invariant(identifier="saving-check", sentence="Every run ends with its game in a save slot."):
    return "\n".join(["## %s/1" % identifier, "", sentence, "",
                      "- **Method:** docs/review.md", "- **Rests on:** none",
                      "- **Derives from:** WAY-01@4dd7fb86", "- **Part:** saving",
                      "- **Correction:** none", "- **Recovered:** none"])


def invariants(*entries):
    return "# Invariants\n\n" + "\n\n".join(list(entries or [invariant()]) + [
        "## Withdrawn identifiers\n\n| Identifier | Successors |\n|---|---|",
        "## Quarantined invariants\n\n| Identifier | Version | Until |\n|---|---|---|"]) + "\n"


def decision(version=1, binding="A saved game is written to a save slot of the player's own.",
             rationale="The player owns the game."):
    return "\n".join(["### WAY-01/%d — Where does a saved game go?" % version, "", binding, "",
                      "- **Change:** %s" % ("new decision" if version == 1 else
                                            "reword · previous: WAY-01/%d" % (version - 1)),
                      "- **Scope:** saving", "",
                      ("*Rationale:* " if version == 1 else "*Rationale for change:* ") + rationale])


def log(*versions):
    return "# Decision log\n\n## WAY-01 — Where does a saved game go?\n\n" + \
        "\n\n".join(versions or [decision()]) + "\n"


TEMPLATE_TEXT = "\n".join([
    "# Demo template", "", "A check gives `pass` or `fail`.", "",
    "| Kind | Meaning |", "|---|---|", "| new entry | an entry first written |", ""])

FILES = {"src/saving.py": "def save():\n    pass\n",
         "docs/review.md": "# What a reviewer checks\n",
         "elements/demo/template.md": TEMPLATE_TEXT,
         "foundations/part_map.md": MAP,
         "foundations/invariants.md": invariants(),
         "foundations/decisions.md": log()}

# The invariants each run records, as the method lines of the-way's own entries name the runs.
PLAIN = sorted(["glossary-file/1", "glossary-file-sections/1", "glossary-term-holder/1",
                "glossary-entry-version/1", "glossary-entry-version/1",
                "glossary-entry-field-presence/1", "glossary-entry-field-words/1",
                "glossary-entry-field-words/1", "glossary-definition-count/1", "glossary-definition-words/1",
                "glossary-avoid-single/1", "glossary-avoid-term/1", "glossary-avoid-carrier/1",
                "glossary-not-target/1",
                "glossary-not-quoted-word/1"])
BASE = ["glossary-avoid-growth/1"]
MERGE = sorted(["glossary-entry-merge-todo/1", "glossary-term-use/1"])


class GuardTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.outside = tempfile.TemporaryDirectory()
        self.root = self.directory.name
        self.path = os.path.join(self.root, "foundations", "glossary.md")
        self.record_path = os.path.join(self.outside.name, ".runs", "glossary.jsonl")
        self.templates = [os.path.join(self.root, "elements", "demo", "template.md")]
        self.examples = os.path.join(self.root, "elements", "glossary", "examples.md")
        self.lines = []
        for name, content in FILES.items():
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

    def commit(self, text, **files):
        self.write("foundations/glossary.md", text)
        for name, content in files.items():
            self.write(name.replace("__", "/"), content)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")

    def guard(self, text, base=None, merge_onto=None, path=None, uses=None, common=None, own=None,
              **files):
        if text is not None:
            self.write("foundations/glossary.md", text)
        for name, content in files.items():
            self.write(name.replace("__", "/"), content)
        self.git("add", "-A")
        output = io.StringIO()
        # the part the elements share and the-way's own file are given only where a test sets them
        given = {name: value for name, value in (("common", common), ("own", own))
                 if value is not None}
        code = format_guard.run(path or self.path, base=base, stream=output, merge_onto=merge_onto,
                                record=self.record_path, templates=self.templates,
                                examples=self.examples, uses=uses, **given)
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

    def assertWarns(self, text, fragment, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 0, output)
        self.assertIn("warning: " + fragment, output)
        return output

    def verdicts(self, invariant):
        return [line["verdict"] for line in self.lines if line["invariant"] == invariant]


class ValidFile(GuardTestCase):
    def test_valid_file_passes(self):
        self.assertPasses(glossary())

    def test_without_options_notes_say_what_is_not_compared(self):
        output = self.assertPasses(glossary())
        self.assertIn("note: no --base given", output)
        self.assertIn("note: no --merge-onto given", output)

    def test_without_the_files_beside_it_notes_say_so(self):
        for name in ("part_map.md", "invariants.md"):
            os.remove(os.path.join(self.root, "foundations", name))
        code, output = self.guard(glossary(entry(), run_entry(not_="none")))
        self.assertIn("note: there is no part_map.md beside the file", output)
        self.assertIn("note: there is no environment_facts.md beside the file", output)
        self.assertEqual(code, 0, output)


class Layout(GuardTestCase):
    def test_no_title(self):
        # invariant: glossary-file-sections/1
        self.assertFails(glossary(head="The words of the game."), "opens with no title")
        self.assertEqual(self.verdicts("glossary-file-sections/1"), ["fail"])

    def test_two_paragraphs_under_the_title(self):
        # invariant: glossary-file-sections/1
        self.assertFails(glossary(head="# Glossary\n\nThe words of the game.\n\nMore words."),
                         "2 paragraphs under the title")

    def test_no_paragraph_under_the_title(self):
        # invariant: glossary-file-sections/1
        self.assertFails(glossary(head="# Glossary"), "0 paragraphs under the title")

    def test_other_heading_level(self):
        # invariant: glossary-file-sections/1
        self.assertFails(glossary(entry(), run_entry() + "\n\n### Notes\n\nMore to come."),
                         "heading `### Notes` is neither")

    def test_second_title(self):
        # invariant: glossary-file-sections/1
        self.assertFails(glossary(entry(), "# More words", run_entry()),
                         "heading `# More words` is neither")

    def test_section_without_fields(self):
        # invariant: glossary-file-sections/1
        self.assertFails(glossary(entry(), run_entry(), "## Notes\n\nMore to come."),
                         "section `## Notes` holds no field of an entry")


class File(GuardTestCase):
    def test_file_elsewhere(self):
        # invariant: glossary-file/1
        path = os.path.join(self.root, "foundations", "words.md")
        self.write("foundations/words.md", glossary())
        self.assertFails(None, "stands in foundations/glossary.md, not in foundations/words.md",
                         path=path)

    def test_file_in_other_letter_case(self):
        # invariant: glossary-file/1
        self.write("foundations/Glossary.md", glossary())
        self.git("add", "-A")
        path = os.path.join(self.root, "foundations", "Glossary.md")
        output = io.StringIO()
        format_guard.run(path, stream=output, templates=self.templates, examples=self.examples)
        self.assertIn("not in foundations/Glossary.md", output.getvalue())

    def test_second_file_of_entries(self):
        # invariant: glossary-file/1
        self.write("docs/words.md", "# Words\n\n" + entry(term="slot") + "\n")
        self.assertFails(glossary(), "`docs/words.md` is a second file of glossary entries")

    def test_entry_in_a_fenced_block_is_no_file_of_entries(self):
        # invariant: glossary-file/1
        self.write("docs/form.md", "# Form\n\n```markdown\n" + entry() + "\n```\n")
        self.assertPasses(glossary())

    def test_examples_beside_the_template_are_no_file_of_entries(self):
        # invariant: glossary-file/1
        self.write("elements/glossary/examples.md", "# Examples\n\n" + entry() + "\n")
        self.assertPasses(glossary())


class Terms(GuardTestCase):
    def test_term_heading_two_entries(self):
        # invariant: glossary-term-holder/1
        self.assertFails(glossary(entry(), run_entry(), entry(avoid="none")),
                         "term `save slot` heads two entries")

    def test_term_heading_two_entries_in_another_case(self):
        # invariant: glossary-term-holder/1
        self.assertFails(glossary(entry(), run_entry(), entry(term="Save slot", avoid="none")),
                         "term `Save slot` heads two entries")

    def test_heading_with_a_version(self):
        # invariant: glossary-entry-version/1
        self.assertFails(glossary(entry(heading="## save slot/1"), run_entry()),
                         "`## save slot/1` carries a version")

    def test_version_field(self):
        # invariant: glossary-entry-version/1
        self.assertFails(glossary(entry(extra=[("Version", "1")]), run_entry()),
                         "field *Version* is not in the template")
        self.assertIn("fail", self.verdicts("glossary-entry-version/1"))


class Fields(GuardTestCase):
    def test_field_missing(self):
        # invariant: glossary-entry-field-presence/1
        self.assertFails(glossary(entry(omit=("Not",)), run_entry()), "field *Not* is missing")

    def test_field_empty(self):
        # invariant: glossary-entry-field-presence/1
        self.assertFails(glossary(entry(avoid=""), run_entry()), "field *Avoid* is missing")

    def test_field_not_in_the_template(self):
        self.assertFails(glossary(entry(extra=[("Forms", "save slots")]), run_entry()),
                         "field *Forms* is not in the template")

    def test_todo_in_avoid(self):
        # invariant: glossary-entry-field-words/1
        self.assertFails(glossary(entry(avoid="TODO"), run_entry()), "*Avoid* may not hold `TODO`")

    def test_not_reading_todo_whole(self):
        # invariant: glossary-entry-field-words/1
        self.assertFails(glossary(entry(not_="TODO"), run_entry()), "*Not* reads `TODO` whole")

    def test_todo_as_definition(self):
        # invariant: glossary-entry-field-words/1
        self.assertFails(glossary(entry(definition="TODO"), run_entry()),
                         "the definition holds `TODO`")


class Definitions(GuardTestCase):
    def test_definition_missing(self):
        # invariant: glossary-definition-count/1
        self.assertFails(glossary(entry(definition=None), run_entry()),
                         "save slot: the definition is missing")

    def test_two_sentences(self):
        # invariant: glossary-definition-count/1
        self.assertFails(glossary(entry(definition=SLOT + " It never moves."), run_entry()),
                         "the definition is 2 sentences")

    def test_period_inside_code_is_no_end(self):
        # invariant: glossary-definition-count/1
        self.assertPasses(glossary(entry(definition="A save slot is the storage that `save.py` "
                                                    "holds one saved game in."), run_entry()))

    def test_text_outside_the_definition_and_fields(self):
        # invariant: glossary-definition-count/1
        text = glossary(entry() + "\n\nA note on slots.", run_entry())
        self.assertFails(text, "text outside the definition and the fields")

    def test_must(self):
        # invariant: glossary-definition-words/1
        self.assertFails(glossary(entry(definition="A save slot is the storage that must hold one "
                                                   "saved game."), run_entry()),
                         "the definition holds *must*")

    def test_word_the_decision_template_forbids(self):
        # invariant: glossary-definition-words/1
        self.assertFails(glossary(entry(definition="A save slot is the storage that will hold one "
                                                   "saved game."), run_entry()),
                         "the definition holds *will*")

    def test_keyword_in_capitals(self):
        # invariant: glossary-definition-words/1
        self.assertFails(glossary(entry(definition="A save slot is the storage that SHALL hold one "
                                                   "saved game."), run_entry()),
                         "the definition holds SHALL")

    def test_forbidden_word_in_code_passes(self):
        # invariant: glossary-definition-words/1
        self.assertPasses(glossary(entry(definition="A save slot is the storage that `must_keep` "
                                                    "holds one saved game in."), run_entry()))


class Avoid(GuardTestCase):
    def test_word_in_two_avoids(self):
        # invariant: glossary-avoid-single/1
        self.assertFails(glossary(entry(), run_entry(avoid="storage cell — a run's storage")),
                         "which the *Avoid* of `save slot` lists too")

    def test_word_that_is_a_term(self):
        # invariant: glossary-avoid-term/1
        self.assertFails(glossary(entry(avoid="run — a play"), run_entry()),
                         "*Avoid* lists `run`, which is the term `run`")

    def test_word_that_is_a_form_of_a_term(self):
        # invariant: glossary-avoid-term/1
        self.assertFails(glossary(entry(avoid="runs — plays"), run_entry()),
                         "*Avoid* lists `runs`, which is the term `run`")

    def test_word_in_two_avoids_in_two_forms(self):
        # invariant: glossary-avoid-single/1
        self.assertFails(glossary(entry(), run_entry(avoid="storage cells — a run's storage")),
                         "which the *Avoid* of `save slot` lists too")

    def test_word_in_backticks_is_compared_plain(self):
        # invariant: glossary-avoid-term/1
        output = self.assertFails(glossary(entry(avoid="`run` — a play"), run_entry()),
                                  "*Avoid* lists `run` with marks around it")
        self.assertIn("*Avoid* lists `run`, which is the term `run`", output)

    def test_word_a_not_names(self):
        # invariant: glossary-avoid-carrier/1
        self.assertFails(glossary(entry(), run_entry(not_="a box — \"storage cell\"")),
                         "*Avoid* lists `storage cell`, which the *Not* of `run` names")
        self.assertEqual(self.verdicts("glossary-avoid-carrier/1"), ["fail"])

    def test_word_a_not_names_in_another_form(self):
        # invariant: glossary-avoid-carrier/1
        self.assertFails(glossary(entry(), run_entry(not_="a box — \"storage cells\"")),
                         "which the *Not* of `run` names")

    def test_word_without_what_a_reader_takes_it_for(self):
        self.assertFails(glossary(entry(avoid="storage cell"), run_entry()),
                         "*Avoid* lists `storage cell` without what a reader takes it for")


class Not(GuardTestCase):
    def test_term_carrier(self):
        # invariant: glossary-not-target/1
        self.assertPasses(glossary(entry(not_="one play of the game — run"), run_entry()))

    def test_carrier_that_is_no_term(self):
        # invariant: glossary-not-target/1
        self.assertFails(glossary(entry(not_="one play of the game — session"), run_entry()),
                         "names `session`, which is no term of the glossary")

    def test_identifier_carrier(self):
        # invariant: glossary-not-target/1
        self.assertPasses(glossary(entry(not_="the part — `saving`"), run_entry()))

    def test_withdrawn_identifier_carrier(self):
        # invariant: glossary-not-target/1
        self.assertFails(glossary(entry(not_="the old part — `game-state`"), run_entry()),
                         "names `game-state`, which is neither")

    def test_closed_value_in_backticks(self):
        # invariant: glossary-not-target/1
        self.assertPasses(glossary(entry(not_="a verdict — `pass`"), run_entry()))

    def test_kind_of_change(self):
        # invariant: glossary-not-target/1
        self.assertPasses(glossary(entry(not_="a kind of change — `new wording`"), run_entry()))

    def test_value_the_gate_fills_in(self):
        # invariant: glossary-not-target/1
        self.assertPasses(glossary(entry(not_="where a branch left — `{fork-point}`"), run_entry()))

    def test_result_of_a_check(self):
        # invariant: glossary-not-target/1
        self.assertPasses(glossary(entry(not_="a result — `unchecked`"), run_entry()))

    def test_cell_of_a_table_of_no_closed_list(self):
        # invariant: glossary-not-target/1
        self.assertFails(glossary(entry(not_="a kind of entry — `new entry`"), run_entry()),
                         "names `new entry`, which is neither")

    def test_todo_in_place_of_a_meaning(self):
        # invariant: glossary-entry-field-words/1
        self.assertFails(glossary(entry(not_="one play — run · TODO — run"), run_entry()),
                         "*Not* reads `TODO` in place of a meaning")

    def test_unknown_value_in_backticks(self):
        # invariant: glossary-not-target/1
        self.assertFails(glossary(entry(not_="a verdict — `maybe`"), run_entry()),
                         "names `maybe`, which is neither")

    def test_quoted_word_the_foundation_uses(self):
        # invariant: glossary-not-quoted-word/1
        self.assertPasses(glossary(entry(not_="what a player owns — \"saved game\""), run_entry()))

    def test_quoted_word_only_between_quotation_marks(self):
        # invariant: glossary-not-quoted-word/1
        text = glossary(entry(not_="a box — \"crate\""), run_entry())
        self.write("foundations/notes.md", "# Notes\n\nA \"crate\" is never meant.\n")
        self.assertFails(text, "names \"crate\", which the foundation does not use")

    def test_quoted_word_only_in_the_glossary(self):
        # invariant: glossary-not-quoted-word/1
        text = glossary(entry(not_="a box — \"crate\""),
                        run_entry(definition="A run is one play of the game from a crate to the "
                                             "player's death."))
        self.assertFails(text, "names \"crate\", which the foundation does not use")

    def test_carrier_holding_the_term(self):
        # invariant: glossary-not-quoted-word/1
        self.assertFails(glossary(entry(not_="a slot of a menu — \"save slots\""), run_entry()),
                         "names \"save slots\", which holds the term")

    def test_identifier_holding_the_term_through_a_hyphen(self):
        # invariant: glossary-not-quoted-word/1
        self.write("foundations/invariants.md", invariants(invariant(), invariant("run-check")))
        self.assertFails(glossary(entry(), run_entry(not_="a check — `run-check`")),
                         "names `run-check`, which holds the term")

    def test_quoted_word_only_inside_an_identifier(self):
        # invariant: glossary-not-quoted-word/1
        self.assertFails(glossary(entry(not_="a state — \"state\""), run_entry()),
                         "names \"state\", which the foundation does not use")

    def test_quoted_word_only_in_backticks(self):
        # invariant: glossary-not-quoted-word/1
        self.write("foundations/notes.md", "# Notes\n\nThe file `crate` holds nothing.\n")
        self.assertFails(glossary(entry(not_="a box — \"crate\""), run_entry()),
                         "names \"crate\", which the foundation does not use")

    def test_todo_carrier_is_a_warning(self):
        self.assertWarns(glossary(entry(not_="a box — TODO"), run_entry()),
                         "save slot: *Not* reads `TODO` in place of what carries \"a box\"")

    def test_meaning_without_carrier(self):
        self.assertFails(glossary(entry(not_="a box"), run_entry()),
                         "*Not* gives `a box` without what carries it")


class TermUse(GuardTestCase):
    def test_term_with_no_use_is_a_warning(self):
        self.assertWarns(glossary(entry(), run_entry(), entry(term="menu", avoid="none",
                                                              definition="A menu is a list.")),
                         "menu: the term has no use outside the glossary")

    def test_term_with_no_use_fails_a_merge(self):
        # invariant: glossary-term-use/1
        text = glossary(entry(), run_entry(), entry(term="menu", avoid="none",
                                                     definition="A menu is a list."))
        self.commit(text)
        self.assertFails(text, "menu: the term has no use outside the glossary", merge_onto="HEAD")
        self.assertEqual(self.verdicts("glossary-term-use/1"), ["fail"])

    def test_merge_onto_none_records_the_use_unchecked(self):
        # invariant: glossary-term-use/1
        self.guard(glossary(), merge_onto="none")
        self.assertIn({"check": "elements/glossary/format_guard.py::check_term_use",
                       "verdict": "unchecked", "invariant": "glossary-term-use/1",
                       "reason": NO_COMMIT,
                       "description": "--merge-onto none: there is no commit to merge onto"},
                      self.lines)

    def test_use_in_another_form(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every run ends with its game in one of the save slots.")))
        self.assertPasses(glossary())

    def test_use_across_a_line_break(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every run ends with its game in a save\nslot of its own.")))
        self.assertPasses(glossary())

    def test_use_in_backticks_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every run ends with its game in `save slot`.")))
        self.write("foundations/decisions.md", log(decision(binding="A saved game is written "
                                                                    "to storage.")))
        self.assertWarns(glossary(), "save slot: the term has no use outside the glossary")

    def test_use_in_a_token_with_a_hyphen_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every run ends with its game in a save slot-like storage.")))
        self.write("foundations/decisions.md", log(decision(binding="A saved game is written "
                                                                    "to storage.")))
        self.assertWarns(glossary(), "save slot: the term has no use outside the glossary")

    def test_use_in_a_value_of_part_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends saved.").replace("- **Part:** saving",
                                                                 "- **Part:** run")))
        self.assertWarns(glossary(), "run: the term has no use outside the glossary")

    def test_use_in_a_field_name_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends saved.") + "\n- **Run:** nightly"))
        self.assertWarns(glossary(), "run: the term has no use outside the glossary")

    def test_use_inside_a_longer_term_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        text = glossary(entry(), run_entry(),
                        entry(term="slot", avoid="none",
                              definition="A slot is a place in a list of places."))
        self.assertWarns(text, "slot: the term has no use outside the glossary")

    def test_use_in_a_template_counts(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        self.write("elements/demo/template.md", TEMPLATE_TEXT + "\nA run gives a verdict.\n")
        self.assertPasses(glossary())

    def test_use_in_a_token_with_a_slash_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot or in run/saves.")))
        self.assertWarns(glossary(), "run: the term has no use outside the glossary")

    def test_use_in_a_fenced_block_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        self.write("foundations/notes.md", "# Notes\n\n```\nA run gives a verdict.\n```\n")
        self.assertWarns(glossary(), "run: the term has no use outside the glossary")

    def test_merge_reads_a_file_the_main_branch_changed(self):
        # invariant: glossary-term-use/1
        self.commit(glossary())
        self.git("checkout", "-q", "-b", "main-line")
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        self.git("commit", "-qam", "main drops the run")
        self.git("checkout", "-q", "main")
        self.assertFails(glossary(), "run: the term has no use outside the glossary",
                         merge_onto="main-line")

    def main_drops_the_run(self):
        self.commit(glossary())
        self.git("checkout", "-q", "-b", "main-line")
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        self.git("commit", "-qam", "main drops the run")
        self.git("checkout", "-q", "main")

    def test_merge_keeps_a_use_the_branch_added(self):
        # invariant: glossary-term-use/1
        self.main_drops_the_run()
        self.write("foundations/invariants.md", invariants(
            invariant(), invariant("run-check", "Every run is checked.")))
        self.assertPasses(glossary(), merge_onto="main-line")

    def test_merge_of_both_sides_drops_the_last_use(self):
        # invariant: glossary-term-use/1
        self.main_drops_the_run()
        self.write("foundations/invariants.md", invariants(
            invariant(), invariant("game-check", "Every game is checked.")))
        self.assertFails(glossary(), "run: the term has no use outside the glossary",
                         merge_onto="main-line")

    def test_merge_with_a_conflict_is_a_failure_of_the_run(self):
        # invariant: glossary-term-use/1
        self.main_drops_the_run()
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every run ends in a save slot of its own.")))
        self.assertFails(glossary(), "foundations/invariants.md: git cannot merge the file onto "
                                     "main-line (1 conflict(s))", merge_onto="main-line")
        self.assertEqual(self.verdicts("glossary-term-use/1"), [])


class AgainstBase(GuardTestCase):
    def grown(self, name, before, after, fragment="`storage cell`, which the *Avoid* of"):
        self.commit(glossary(), **{name: before})
        return self.assertFails(glossary(), fragment, base="HEAD", **{name: after})

    def test_word_of_avoid_added(self):
        # invariant: glossary-avoid-growth/1
        self.grown("foundations__notes.md", "# Notes\n", "# Notes\n\nThe storage cell of a game.\n")
        self.assertEqual(self.verdicts("glossary-avoid-growth/1"), ["fail"])

    def test_word_added_in_another_form_and_case(self):
        # invariant: glossary-avoid-growth/1
        self.grown("foundations__notes.md", "# Notes\n", "# Notes\n\nStorage cells of a game.\n")

    def test_word_added_across_a_line_break(self):
        # invariant: glossary-avoid-growth/1
        self.grown("foundations__notes.md", "# Notes\n", "# Notes\n\nThe storage\ncell of a game.\n")

    def test_rewrapped_line_passes(self):
        # invariant: glossary-avoid-growth/1
        self.commit(glossary(), **{"foundations__notes.md": "# Notes\n\nThe storage cell of a game.\n"})
        self.assertPasses(glossary(), base="HEAD",
                          **{"foundations__notes.md": "# Notes\n\nThe storage\ncell of a game.\n"})
        self.assertEqual(self.verdicts("glossary-avoid-growth/1"), ["pass"])

    def test_word_added_in_the_template_counts(self):
        # invariant: glossary-avoid-growth/1
        self.grown("elements__demo__template.md", TEMPLATE_TEXT,
                   TEMPLATE_TEXT + "\nThe storage cell holds a game.\n")

    def test_left_out_text_passes(self):
        # invariant: glossary-avoid-growth/1
        self.commit(glossary(), **{"foundations__notes.md": "# Notes\n"})
        added = ("# Notes\n\nA \"storage cell\" is a word; `storage cell` is code; "
                 "storage-cells is a token.\n\n```\nstorage cell\n```\n")
        self.assertPasses(glossary(), base="HEAD", **{"foundations__notes.md": added})

    def test_word_in_the_glossary_passes(self):
        # invariant: glossary-avoid-growth/1
        self.commit(glossary())
        self.assertPasses(glossary(entry(), run_entry(definition="A run is one play of the game "
                                                                 "that fills a storage cell.")),
                          base="HEAD")

    def test_identifier_in_a_field_value_passes(self):
        # invariant: glossary-avoid-growth/1
        text = glossary(entry(avoid="saving — the same storage"), run_entry())
        self.commit(text, **{"foundations__notes.md": "# Notes\n"})
        self.assertPasses(text, base="HEAD",
                          **{"foundations__notes.md": "# Notes\n\n- **Owner:** saving\n"})

    def test_identifier_spelling_in_running_text_counts(self):
        # invariant: glossary-avoid-growth/1
        text = glossary(entry(avoid="saving — the same storage"), run_entry())
        self.commit(text, **{"foundations__notes.md": "# Notes\n"})
        self.assertFails(text, "`saving`, which the *Avoid* of `save slot` lists", base="HEAD",
                         **{"foundations__notes.md": "# Notes\n\nSaving happens often.\n"})

    def test_word_inside_a_longer_term_passes(self):
        # invariant: glossary-avoid-growth/1
        text = glossary(entry(avoid="slot — the same storage"), run_entry())
        self.commit(text, **{"foundations__notes.md": "# Notes\n"})
        self.assertPasses(text, base="HEAD",
                          **{"foundations__notes.md": "# Notes\n\nA save slot again.\n"})

    def test_word_in_a_value_of_change_passes(self):
        # invariant: glossary-avoid-growth/1
        text = glossary(entry(avoid="reword — a change of words"), run_entry())
        self.commit(text, **{"foundations__decisions.md": log(decision())})
        self.assertPasses(text, base="HEAD",
                          **{"foundations__decisions.md": log(decision(), decision(2))})

    def test_new_version_restating_the_word_passes(self):
        # invariant: glossary-avoid-growth/1
        first = decision(rationale="The player owns the storage cell.")
        self.commit(glossary(), **{"foundations__decisions.md": log(first)})
        second = decision(2, binding="A saved game is written to the player's own save slot.",
                          rationale="The player owns the storage cell.")
        self.assertPasses(glossary(), base="HEAD",
                          **{"foundations__decisions.md": log(first, second)})

    def test_new_version_with_a_new_sentence_fails(self):
        # invariant: glossary-avoid-growth/1
        first = decision()
        self.commit(glossary(), **{"foundations__decisions.md": log(first)})
        second = decision(2, rationale="The player owns the storage cell.")
        self.assertFails(glossary(), "`storage cell`, which the *Avoid* of `save slot` lists",
                         base="HEAD", **{"foundations__decisions.md": log(first, second)})

    def test_base_none_records_the_count_unchecked(self):
        # invariant: glossary-avoid-growth/1
        self.guard(glossary(), base="none")
        self.assertEqual(self.lines, [{"check": "elements/glossary/format_guard.py::"
                                                "check_against_base", "verdict": "unchecked",
                                       "invariant": "glossary-avoid-growth/1", "reason": NO_COMMIT,
                                       "description": "--base none: there is no commit the branch "
                                                      "left the main branch from"}])

    def test_base_that_does_not_exist(self):
        self.assertFails(glossary(), "--base nowhere does not exist", base="nowhere")


class Collision(GuardTestCase):
    def test_new_term_reading_like_a_part(self):
        # invariant: glossary-term-collision/1
        self.commit(glossary())
        self.assertWarns(glossary(entry(), run_entry(),
                                  entry(term="saving", avoid="none",
                                        definition="Saving is writing a game to a save slot.")),
                         "term `saving` and identifier `saving` read alike", base="HEAD")

    def test_new_term_reading_like_an_invariant_in_a_form(self):
        # invariant: glossary-term-collision/1
        self.commit(glossary())
        self.write("foundations/invariants.md", invariants(invariant(), invariant("saving-checks")))
        self.assertWarns(glossary(entry(), run_entry(),
                                  entry(term="saving check", avoid="none",
                                        definition="A saving check is a check of a save slot.")),
                         "term `saving check` and identifier `saving-check` read alike", base="HEAD")

    def test_new_identifier_reading_like_a_term(self):
        # invariant: glossary-term-collision/1
        self.commit(glossary())
        self.write("foundations/invariants.md", invariants(invariant(), invariant("run")))
        self.assertWarns(glossary(), "term `run` and identifier `run` read alike", base="HEAD")

    def element_term(self):
        return glossary(entry(), run_entry(),
                        entry(term="glossary", avoid="none",
                              definition="A glossary is the file of a game's words, each in one "
                                         "meaning of a save slot."))

    def test_term_naming_the_element_of_its_part_in_the_way(self):
        # invariant: glossary-term-collision/1
        self.commit(glossary())
        self.assertPasses(self.element_term(), base="HEAD", own=True)

    def test_term_naming_the_element_of_its_part_outside_the_way(self):
        # invariant: glossary-term-collision/1
        self.commit(glossary())
        self.assertWarns(self.element_term(), "term `glossary` and identifier `glossary` read alike",
                         base="HEAD")

    def test_pair_that_read_alike_on_the_base(self):
        # invariant: glossary-term-collision/1
        text = glossary(entry(), run_entry(), entry(term="saving", avoid="none",
                                                    definition="Saving is writing a game to a "
                                                               "save slot."))
        self.commit(text)
        self.assertPasses(text, base="HEAD")

    def test_no_warning_without_a_base(self):
        # invariant: glossary-term-collision/1
        self.assertPasses(glossary(entry(), run_entry(),
                                   entry(term="saving", avoid="none",
                                         definition="Saving is writing a game to a save slot.")))


class DefinitionUses(GuardTestCase):
    def test_changed_definition_lists_the_uses(self):
        # invariant: glossary-definition-uses/1
        self.commit(glossary())
        output = self.assertPasses(glossary(entry(definition="A save slot is the storage that "
                                                             "holds one saved game at a time."),
                                            run_entry(definition="A run is one play of the game "
                                                                 "that ends in a save slot.")),
                                   base="HEAD")
        self.assertIn("note: uses of `save slot`, whose definition differs from HEAD", output)
        self.assertIn("  foundations/invariants.md:5: Every run ends with its game in a save slot.",
                      output)
        self.assertIn("  foundations/glossary.md:", output)
        self.assertIn("A run is one play of the game that ends in a save slot.", output)

    def test_unchanged_definition_lists_nothing(self):
        # invariant: glossary-definition-uses/1
        self.commit(glossary())
        output = self.assertPasses(glossary(), base="HEAD")
        self.assertNotIn("note: uses of", output)

    def test_new_entry_lists_nothing(self):
        # invariant: glossary-definition-uses/1
        self.commit(glossary(entry(not_="none")))
        output = self.assertPasses(glossary(), base="HEAD")
        self.assertNotIn("note: uses of", output)

    def test_rewrapped_definition_lists_nothing(self):
        # invariant: glossary-definition-uses/1
        self.commit(glossary())
        output = self.assertPasses(glossary(entry(definition="A save slot is the storage\nthat "
                                                             "holds one saved game."),
                                            run_entry()), base="HEAD")
        self.assertNotIn("note: uses of", output)


class Merge(GuardTestCase):
    def test_todo_fails_a_merge(self):
        # invariant: glossary-entry-merge-todo/1
        text = glossary(entry(not_="a box — TODO"), run_entry())
        self.commit(text)
        output = self.assertFails(text, "*Not* holds `TODO`, which a merge onto the main branch",
                                  merge_onto="HEAD")
        self.assertNotIn("warning:", output)

    def test_merge_onto_none_records_todo_unchecked(self):
        # invariant: glossary-entry-merge-todo/1
        self.guard(glossary(entry(not_="a box — TODO"), run_entry()), merge_onto="none")
        self.assertEqual(self.verdicts("glossary-entry-merge-todo/1"), ["unchecked"])


class PanelCorrections(GuardTestCase):
    def test_field_written_twice(self):
        self.assertFails(glossary(entry(extra=[("Avoid", "crate — a box")]), run_entry()),
                         "field *Avoid* is written a second time")

    def test_text_after_the_fields_belongs_to_no_invariant(self):
        # invariant: glossary-definition-count/1
        self.assertFails(glossary(entry() + "\n\nA note on slots.", run_entry()),
                         "text outside the definition and the fields")
        self.assertEqual(self.verdicts("glossary-definition-count/1"), ["pass"])

    def test_contracted_word_kept_out(self):
        # invariant: glossary-definition-words/1
        self.assertFails(glossary(entry(definition="A save slot is the storage that shouldn't hold "
                                                   "two saved games."), run_entry()),
                         "the definition holds *should*")

    def test_contraction_of_will(self):
        # invariant: glossary-definition-words/1
        self.assertFails(glossary(entry(definition="A save slot is the storage that won't hold two "
                                                   "saved games."), run_entry()),
                         "the definition holds *will*")

    def test_term_and_its_form_head_two_entries(self):
        # invariant: glossary-term-holder/1
        self.assertFails(glossary(entry(), run_entry(), entry(term="save slots", avoid="none")),
                         "term `save slots` heads two entries (`save slot`")

    def test_second_file_with_another_extension(self):
        # invariant: glossary-file/1
        self.write("docs/words.markdown", "# Words\n\n" + entry(term="slot") + "\n")
        self.assertFails(glossary(), "`docs/words.markdown` is a second file of glossary entries")

    def test_tag_line_is_no_heading(self):
        # invariant: glossary-file-sections/1
        self.assertPasses(glossary(head="# Glossary\n\nThe words of the game, each in one meaning.\n"
                                        "#words"))

    def test_hyphenated_term_reads_like_the_same_identifier(self):
        # invariant: glossary-term-collision/1
        self.commit(glossary())
        self.write("foundations/invariants.md", invariants(invariant(), invariant("save-slot")))
        self.assertWarns(glossary(entry(term="save-slot"), run_entry()),
                         "term `save-slot` and identifier `save-slot` read alike", base="HEAD")

    def test_field_name_in_a_table_cell_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends saved.") + "\n- **Run:** nightly"))
        self.write("foundations/notes.md", "# Notes\n\n| Field | Reader |\n|---|---|\n| Run | a person |\n")
        self.assertWarns(glossary(), "run: the term has no use outside the glossary")

    def test_foundations_at_the_root_are_read_for_a_glossary_elsewhere(self):
        # invariant: glossary-not-quoted-word/1
        path = os.path.join(self.root, "foundations", "words", "glossary.md")
        self.write("foundations/words/glossary.md",
                   glossary(entry(not_="what a player owns — \"saved game\""), run_entry()))
        code, output = self.guard(None, path=path)
        self.assertIn("stands in foundations/glossary.md, not in foundations/words/glossary.md",
                      output)
        self.assertNotIn("\"saved game\", which the foundation does not use", output)
        self.assertNotIn("there is no part_map.md", output)

    def test_list_item_restated_in_a_new_version_passes(self):
        # invariant: glossary-avoid-growth/1
        first = decision(rationale="The player owns the game.") + \
            "\n- complies: the storage cell holds the game."
        self.commit(glossary(), **{"foundations__decisions.md": log(first)})
        second = decision(2, binding="A saved game is written to the player's own save slot.",
                          rationale="The player owns every game.") + \
            "\n- complies: the storage cell holds the game."
        self.assertPasses(glossary(), base="HEAD",
                          **{"foundations__decisions.md": log(first, second)})

    def test_renamed_field_of_the_template_stops_the_run(self):
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            text = handle.read().replace("- **Not:**", "- **Meanings:**")
        self.write("renamed.md", text)
        output = io.StringIO()
        self.write("foundations/glossary.md", glossary())
        code = format_guard.run(self.path, stream=output, templates=self.templates,
                                template=os.path.join(self.root, "renamed.md"))
        self.assertEqual(code, 2)
        self.assertIn("the entry form has no field *Not*", output.getvalue())

    def test_template_naming_no_word_kept_out_stops_the_run(self):
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            text = handle.read().replace("neither *must* nor", "neither must nor")
        self.write("reworded.md", text)
        output = io.StringIO()
        self.write("foundations/glossary.md", glossary())
        code = format_guard.run(self.path, stream=output, templates=self.templates,
                                template=os.path.join(self.root, "reworded.md"))
        self.assertEqual(code, 2)
        self.assertIn("names no words a definition may not hold", output.getvalue())


class Uses(GuardTestCase):
    def test_uses_take_no_other_option(self):
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output, templates=self.templates, uses="run",
                                base="HEAD")
        self.assertEqual(code, 2)
        self.assertIn("--uses lists the uses of a word and runs no check", output.getvalue())

    def test_uses_report_what_they_could_not_read(self):
        self.write("foundations/glossary.md", glossary())
        with open(os.path.join(self.root, "foundations", "latin1.md"), "wb") as handle:
            handle.write(b"# Notes\n\ncaf\xe9\n")
        self.git("add", "-A")
        output = io.StringIO()
        format_guard.run(self.path, stream=output, templates=self.templates, uses="run")
        self.assertIn("unchecked: the words of foundations/latin1.md", output.getvalue())

    def test_uses_of_a_word_before_any_entry(self):
        os.makedirs(os.path.join(self.root, "foundations"), exist_ok=True)
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output, templates=self.templates,
                                uses="saved game")
        self.assertEqual(code, 0)
        self.assertIn("foundations/decisions.md:", output.getvalue())
        self.assertIn("use(s) of `saved game`", output.getvalue())

    def test_uses_hold_the_definitions_of_other_entries(self):
        self.write("foundations/glossary.md", glossary())
        self.git("add", "-A")
        output = io.StringIO()
        format_guard.run(self.path, stream=output, templates=self.templates, uses="game")
        self.assertIn("foundations/glossary.md:7: A save slot is the storage that holds one saved "
                      "game.", output.getvalue())


class Record(GuardTestCase):
    def test_plain_run_records_the_checks_of_the_file_alone(self):
        self.assertPasses(glossary())
        self.assertEqual(sorted(line["invariant"] for line in self.lines), PLAIN)

    def test_base_run_records_the_checks_against_the_base(self):
        self.commit(glossary())
        self.assertPasses(glossary(), base="HEAD")
        self.assertEqual(sorted(line["invariant"] for line in self.lines), BASE)

    def test_merge_run_records_the_checks_of_a_merge(self):
        self.commit(glossary())
        self.assertPasses(glossary(), merge_onto="HEAD")
        self.assertEqual(sorted(line["invariant"] for line in self.lines), MERGE)

    def test_error_of_no_invariant_is_a_null_line(self):
        self.assertFails(glossary(entry(avoid="storage cell"), run_entry()), "without what")
        self.assertIn({"check": "elements/glossary/format_guard.py::check_avoid",
                       "verdict": "fail", "invariant": None,
                       "description": "line 9: save slot: *Avoid* lists `storage cell` without "
                                      "what a reader takes it for, as `<word> — <what>`"},
                      self.lines)

    def test_unreadable_template_stops_the_run(self):
        output = io.StringIO()
        self.write("foundations/glossary.md", glossary())
        code = format_guard.run(self.path, stream=output, record=self.record_path,
                                template=os.path.join(self.root, "missing.md"))
        self.assertEqual(code, 2)
        self.assertIn("cannot read the rules", output.getvalue())

    def test_missing_glossary_stops_the_run(self):
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output, record=self.record_path,
                                templates=self.templates)
        self.assertEqual(code, 2)
        self.assertIn("cannot read the glossary", output.getvalue())


class Examples(GuardTestCase):
    def run_examples(self, examples):
        _, items = format_guard.parse_file(glossary(), format_guard.read_rules())
        path = os.path.join(self.root, "examples.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(examples)
        report = format_guard.Report(self.path)
        format_guard.check_examples(items, path, report)
        return report.errors

    def test_example_matching_the_file(self):
        self.assertEqual(self.run_examples("# Examples\n\n" + entry() + "\n"), [])

    def test_example_differing_from_the_file(self):
        errors = self.run_examples("# Examples\n\n" + entry(avoid="none") + "\n")
        self.assertIn("differs from the file", errors[0][1])


class Rules(GuardTestCase):
    """What the guard reads from the template, where the template states it."""

    def test_words_kept_out_of_a_definition_are_read_from_the_definition(self):
        # invariant: glossary-definition-words/1
        template = "\n".join([
            "# Glossary entry template", "", "## Entry", "", "```markdown", "## <term>", "",
            "<one sentence: the definition>", "",
            "- **Avoid:** <word> — <what a reader takes it for> · … | none",
            "- **Not:** <meaning> — <what carries it, or TODO> · … | none", "```", "",
            "## The definition", "",
            "- The definition is one sentence in the present tense, with no normative word: neither "
            "*must* nor *ought* nor any word the decision template keeps out of binding sentences "
            "(WAY-96).", ""])
        self.write("demo-template.md", template)
        self.write("foundations/glossary.md",
                   glossary(entry(definition="A save slot is the storage that ought to hold one "
                                             "saved game."), run_entry()))
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(self.path, stream=output, templates=self.templates,
                                template=os.path.join(self.root, "demo-template.md"),
                                examples=self.examples)
        self.assertEqual(code, 1, output.getvalue())
        self.assertIn("save slot: the definition holds *ought*", output.getvalue())


class Common(GuardTestCase):
    """The part the elements share is searched as the elements' templates are."""

    def common(self):
        return os.path.join(self.root, "elements", "common")

    def test_code_of_the_part_the_elements_share_is_not_searched(self):
        # invariant: glossary-avoid-growth/1
        self.commit(glossary(), **{"elements__common__rules.md": "# Shared rules\n",
                                   "elements__common__shared.py": "def share():\n    pass\n"})
        self.assertPasses(glossary(), base="HEAD", common=self.common(),
                          **{"elements__common__shared.py": "def share():\n    # the storage cell "
                                                            "of a game\n    return 'storage cell'\n"})
        self.assertEqual(self.verdicts("glossary-avoid-growth/1"), ["pass"])

    def test_use_only_in_the_code_of_the_part_the_elements_share_is_no_use(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        self.write("elements/common/rules.md", "# Shared rules\n")
        self.write("elements/common/shared.py", "# A run gives a verdict.\n")
        self.assertWarns(glossary(), "run: the term has no use outside the glossary",
                         common=self.common())

    def test_use_in_the_part_the_elements_share_counts(self):
        # invariant: glossary-term-use/1
        self.write("foundations/invariants.md", invariants(
            invariant(sentence="Every game ends in a save slot.")))
        self.write("elements/common/rules.md", "# Shared rules\n\nA run gives a verdict.\n")
        self.assertWarns(glossary(), "run: the term has no use outside the glossary")
        self.assertPasses(glossary(), common=self.common())

    def test_word_of_avoid_added_in_the_part_the_elements_share(self):
        # invariant: glossary-avoid-growth/1
        self.commit(glossary(), **{"elements__common__rules.md": "# Shared rules\n"})
        self.assertFails(glossary(), "elements/common/rules.md: `storage cell`, which the *Avoid* "
                                     "of `save slot` lists", base="HEAD", common=self.common(),
                         **{"elements__common__rules.md": "# Shared rules\n\nThe storage cell of a "
                                                          "game.\n"})
        self.assertEqual(self.verdicts("glossary-avoid-growth/1"), ["fail"])

    def test_quoted_word_used_in_the_part_the_elements_share(self):
        # invariant: glossary-not-quoted-word/1
        self.write("elements/common/rules.md", "# Shared rules\n\nA crate holds nothing.\n")
        text = glossary(entry(not_="a box — \"crate\""), run_entry())
        self.assertFails(text, "names \"crate\", which the foundation does not use")
        self.assertPasses(text, common=self.common())

    def test_the_way_corpus_reads_the_part_the_elements_share(self):
        # invariant: glossary-term-use/1
        self.write("foundations/glossary.md", glossary())
        self.git("add", "-A")
        output = io.StringIO()
        format_guard.run(self.path, stream=output, uses="identifier")
        self.assertIn("\nelements/common/rules.md:", "\n" + output.getvalue())


class Forms(unittest.TestCase):
    """The forms of a word the guard finds: the one place the endings are written (WAY-97)."""

    def test_endings_of_a_word(self):
        self.assertEqual(format_guard.last_word_forms("run"),
                         {"run", "runs", "runes", "run's", "run’s", "rund", "runed", "runing",
                          "runned", "running"})

    def test_final_y(self):
        self.assertIn("entries", format_guard.last_word_forms("entry"))

    def test_multi_word_term_takes_the_ending_on_its_last_word(self):
        forms = format_guard.forms_of("Save slot")
        self.assertIn("save slots", forms)
        self.assertNotIn("saves slot", forms)


class OwnFile(unittest.TestCase):
    """The-way's own glossary holds its entries in the form of the template."""

    def test_the_way_glossary_holds_no_error(self):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            record = os.path.join(directory, "glossary.jsonl")
            code = format_guard.run(format_guard.OWN_FILE, stream=output, record=record)
            with open(record, encoding="utf-8") as handle:
                lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(code, 0, output.getvalue())
        self.assertIn("0 error(s)", output.getvalue())
        self.assertEqual(sorted(line["invariant"] for line in lines), PLAIN)


if __name__ == "__main__":
    unittest.main()
