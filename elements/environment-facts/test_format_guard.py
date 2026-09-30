"""Tests of the environment facts guard: every check fires on a file broken on purpose.

Run from the root of the-way:
    python -B gate/run_tests.py elements/environment-facts --record .runs/environment-facts-tests.jsonl

Inputs, expected fingerprints and expected record lines are written out, never computed by the
code under test (WAY-69).
"""

import inspect
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

NO_COMMIT = "the method takes a commit the gate filled in as not existing"

QUOTA = "Firefox keeps up to 10 MiB of web storage for each origin."
QUOTA_HOLDS = "Firefox 130"
QUOTA_FINGERPRINT = "11ba3f2d"
QUOTA_WIDER_FINGERPRINT = "82f5d0f4"        # the same sentence holding for Firefox 131
QUOTA_REWORDED = "Firefox keeps at most 10 MiB of web storage for each origin."
QUOTA_REWORDED_FINGERPRINT = "0635a942"
QUOTA_SENTENCE_ALONE_FINGERPRINT = "dcd2b282"
QUOTA_SOURCE = ('https://developer.mozilla.org/docs/storage/130 § Web Storage — "Web Storage is '
                'limited to a total of 10 MiB of data per origin."; read 2026-09-26')
LINES = "A JSON Lines file holds one JSON value on each line."
LINES_HOLDS = "JSON Lines, which jsonlines.org publishes without versions"
LINES_FINGERPRINT = "ffce9572"
LINES_SOURCE = ('https://jsonlines.org/ (archived: http://web.archive.org/web/20260918132122/'
                'https://jsonlines.org/, 2026-09-18) § 2 — "Each Line is a Valid JSON Value"; '
                'read 2026-09-26')
DECISION_FINGERPRINT = "4dd7fb86"


def fact(identifier="storage-quota", version=1, sentence=QUOTA, holds=QUOTA_HOLDS,
         source=QUOTA_SOURCE, method="`python -B probes/storage_quota.py`", omit=(), heading=None,
         extra=()):
    lines = [heading or "## %s/%d" % (identifier, version), ""]
    if sentence is not None:
        lines += [sentence, ""]
    fields = [("Holds for", holds), ("Source", source), ("Method", method)] + list(extra)
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def old_fields(set_by="none", correction="none"):
    """*Set by* and *Correction*, which the-way's entries still carry."""
    return [("Set by", set_by), ("Correction", correction)]


def lines_fact(**changes):
    values = dict(identifier="json-lines", sentence=LINES, holds=LINES_HOLDS, source=LINES_SOURCE,
                  method="`TODO`")
    values.update(changes)
    return fact(**values)


WITHDRAWN = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Why | Successors |",
                       "|---|---|---|", "| storage-limit | split into two facts | storage-quota · "
                                        "json-lines |"])


def facts(*entries, withdrawn=WITHDRAWN):
    sections = list(entries) or [fact(), lines_fact()]
    return "# Environment facts\n\n" + "\n\n".join(sections + ([withdrawn] if withdrawn else [])) \
        + "\n"


def invariant(identifier="saves-fit-quota", rests="storage-quota@" + QUOTA_FINGERPRINT,
              method="docs/review.md"):
    return "\n".join(["## %s/1" % identifier, "",
                      "A saved game fits within the storage an origin keeps.", "",
                      "- **Method:** %s" % method, "- **Rests on:** %s" % rests,
                      "- **Derives from:** WAY-01@%s" % DECISION_FINGERPRINT, "- **Part:** saving",
                      "- **Correction:** none"])


def invariants(*entries):
    return "# Invariants\n\n" + "\n\n".join(list(entries or [invariant()]) + [
        "## Withdrawn identifiers\n\n| Identifier | Successors |\n|---|---|\n"
        "| save-size | saves-fit-quota |",
        "## Quarantined invariants\n\n| Identifier | Version | Until |\n|---|---|---|"]) + "\n"


def decision(version=1, based_on="JSON Lines holds one value on each line: json-lines@%s."
             % LINES_FINGERPRINT):
    return "\n".join(["### WAY-01/%d — Where does a saved game go?" % version, "",
                      "A saved game is written to the player's own storage only.", "",
                      "- **Change:** %s" % ("new decision" if version == 1 else
                                            "new wording"),
                      "- **Based on:** %s" % based_on]) + "\n"


def log(*versions):
    return "# Decision log\n\n" + "\n".join(versions or [decision()])


MAP = "\n".join([
    "# Part map", "",
    "## saving — Saving a game", "", "The part answers for writing and reading a saved game.", "",
    "- **Files:** src/saving.py", "- **Depends on:** none", "- **Failure modes:** none",
    "- **Trust boundary:** none", "",
    "## Withdrawn identifiers", "", "| Identifier | Successors |", "|---|---|",
    "| game-state | saving |", ""])

VERDICT_HEADER = "| Entry | Version | Verdict | By | On | Commit | Until |\n|---|---|---|---|---|---|---|\n"


def verdicts(*rows):
    return "# Human verdicts\n\n" + VERDICT_HEADER + "".join("| %s |\n" % " | ".join(row)
                                                             for row in rows)


FILES = {"src/saving.py": "def save():\n    pass\n",
         "docs/review.md": "# What a reviewer checks\n",
         "docs/audience.md": "# Who can open the repository\n",
         "probes/storage_quota.py": "# fact: storage-quota/1\nprint('10 MiB')\n",
         ".gitignore": ".runs/\n"}

# The invariants each run records, as the method lines of the-way's own entries name the runs.
PLAIN = sorted([
    "environment-facts-file/1", "fact-identifier-form/1", "identifier-holders/1",
    "fact-withdrawal-successors/1", "fact-entry-field-presence/1", "fact-entry-field-words/1",
    "fact-sentence-count/1", "fact-scope-word/1", "fact-source-form/1", "fact-method-form/1",
    "human-verdict-fact-row/1", "based-on-fact-fingerprint/1", "fact-citation-target/1",
    "fact-citation-version/1", "run-record-path/1"])
BASE = sorted(["fact-version-new/1", "fact-version-changed/1", "fact-version-unchanged/1",
               "fact-identifier-persistence/1", "fact-withdrawal-persistence/1"])
MERGE = sorted(["fact-entry-merge-todo/1", "based-on-fact-fingerprint-value/1",
                "fact-dependants/1"])


class GuardTestCase(unittest.TestCase):
    files = FILES

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.outside = tempfile.TemporaryDirectory()
        self.root = self.directory.name
        self.path = os.path.join(self.root, "foundations", "environment_facts.md")
        self.record_path = os.path.join(self.outside.name, ".runs", "environment-facts.jsonl")
        self.lines = []
        files = dict(self.files)
        files["foundations/part_map.md"] = MAP
        files["foundations/decisions.md"] = log()
        files["foundations/invariants.md"] = invariants()
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

    def commit(self, text, **files):
        self.write("foundations/environment_facts.md", text)
        for name, content in files.items():
            self.write(name, content)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")

    def guard(self, text, base=None, merge_onto=None, path=None, **files):
        self.write("foundations/environment_facts.md", text)
        for name, content in files.items():
            self.write(name, content)
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(path or self.path, base=base, stream=output,
                                merge_onto=merge_onto, record=self.record_path)
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


class Rules(unittest.TestCase):
    """What the guard reads from the template and from the rules the elements share."""

    def template(self):
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            return handle.read()

    def common(self, **replacements):
        with open(format_guard.COMMON_RULES, encoding="utf-8") as handle:
            text = handle.read()
        for old, new in replacements.items():
            self.assertIn(old, text)
            text = text.replace(old, new)
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = os.path.join(directory.name, "rules.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        return path

    def test_the_form_holds_three_fields(self):
        # a fact names no one who sets it (WAY-84) and declares no correction (WAY-79)
        rules = format_guard.read_rules()
        self.assertEqual([rule.name for rule in rules.fields], ["Holds for", "Source", "Method"])
        self.assertEqual(rules.todo_fields, ["Method"])
        self.assertEqual([rule.name for rule in rules.fields if rule.none], [])

    def test_withdrawn_list_is_read_from_the_rules_the_elements_share(self):
        path = self.common(**{"| Identifier | Why | Successors |":
                              "| Identifier | Reason | Successors |"})
        rules = format_guard.read_rules(common=path)
        self.assertEqual(rules.lists, [("Withdrawn identifiers",
                                        ["Identifier", "Reason", "Successors"])])

    def test_human_verdicts_are_read_from_the_rules_the_elements_share(self):
        path = self.common(**{"| Entry | Version | Verdict | By | On | Commit | Until |":
                              "| Entry | Version | Verdict | By | Until |",
                              "`foundations/human_verdicts.md`": "`foundations/human_rows.md`"})
        rules = format_guard.read_rules(common=path)
        self.assertEqual(rules.verdicts_file, "human_rows.md")
        self.assertEqual(rules.verdicts_columns, ["Entry", "Version", "Verdict", "By", "Until"])

    def test_scope_words_are_read_from_the_section_holds_for(self):
        self.assertEqual(format_guard.read_rules().scope_words, ["latest", "newest"])
        self.assertIn('It never reads "latest" or "newest"',
                      format_guard._section(self.template(), "Holds for"))

    def test_the_template_lists_no_checks_of_the_guard(self):
        self.assertNotIn("## What the format guard checks", self.template())

    def test_the_template_carries_no_draft_banner(self):
        self.assertNotIn("> **Draft.**", self.template())

    def test_the_template_keeps_no_list_of_unchecked_reasons(self):
        result = format_guard._section(self.template(), "Result")
        self.assertNotIn("Reasons for `unchecked`", result)
        self.assertIn("the invariants template", " ".join(result.split()))

    def test_the_examples_are_the_way_s_own_entries(self):
        examples = format_guard._section(self.template(), "Examples")
        self.assertIn("`foundations/environment_facts.md`", examples)
        self.assertNotIn("examples.md", self.template())

    def test_the_guard_reads_no_examples_file(self):
        self.assertFalse(hasattr(format_guard, "check_examples"))
        self.assertFalse(hasattr(format_guard, "EXAMPLES"))
        self.assertNotIn("examples", inspect.signature(format_guard.run).parameters)

    def test_the_template_names_the_obligation_rule_in_the_map_template(self):
        # the rule of WAY-46 stands in the part map template, which this one points to
        catalogues = " ".join(format_guard._section(self.template(), "Catalogues and obligations")
                              .split())
        self.assertNotIn("enters the part map as a failure mode", catalogues)
        with open(os.path.join(format_guard.HERE, "..", "part-map", "template.md"),
                  encoding="utf-8") as handle:
            map_template = " ".join(handle.read().split())
        self.assertIn("enters the map as a failure mode of that part, whose detection names an "
                      "invariant resting on the environment fact of that obligation (WAY-46)",
                      map_template)


class ValidFile(GuardTestCase):
    def test_valid_file_passes(self):
        self.assertPasses(facts())

    def test_without_options_a_note_says_what_is_not_compared(self):
        output = self.assertPasses(facts())
        self.assertIn("note: no --base given", output)
        self.assertIn("note: no --merge-onto given", output)

    def test_without_the_files_beside_it_notes_say_so(self):
        os.remove(os.path.join(self.root, "foundations", "invariants.md"))
        os.remove(os.path.join(self.root, "foundations", "part_map.md"))
        os.remove(os.path.join(self.root, "foundations", "decisions.md"))
        code, output = self.guard(facts())
        self.assertIn("note: there is no invariants.md beside the file", output)
        self.assertIn("note: there is no part_map.md beside the file", output)
        self.assertIn("note: there is no decisions.md beside the file", output)
        self.assertIn("warning: storage-quota/1: no invariant's *Rests on*", output)


class Layout(GuardTestCase):
    def test_heading_without_a_version(self):
        self.assertFails(facts(fact(heading="## storage-quota"), lines_fact()),
                         "heading `## storage-quota` of an entry carries no version number")

    def test_heading_neither_entry_nor_list(self):
        self.assertFails(facts(fact(), lines_fact(), "## Notes\n\nMore to come."),
                         "heading `## Notes` is neither")

    def test_entry_after_the_list(self):
        text = facts(fact(), withdrawn=WITHDRAWN) + "\n" + lines_fact() + "\n"
        self.assertFails(text, "entry `json-lines` stands after the list `Withdrawn identifiers`")

    def test_list_missing(self):
        self.assertFails(facts(fact(), lines_fact(), withdrawn=None),
                         "the file has no list `Withdrawn identifiers`")

    def test_list_with_other_columns(self):
        withdrawn = "## Withdrawn identifiers\n\n| Identifier | Successors |\n|---|---|"
        self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                         "the list `Withdrawn identifiers` has columns Identifier | Successors")


class File(GuardTestCase):
    def test_file_elsewhere(self):
        # invariant: environment-facts-file/1
        path = os.path.join(self.root, "foundations", "facts.md")
        self.write("foundations/facts.md", facts())
        self.assertFails(facts(), "stand in foundations/environment_facts.md, not in "
                                  "foundations/facts.md", path=path)
        self.assertIn("fail", self.verdicts("environment-facts-file/1"))

    def test_second_file_of_entries(self):
        # invariant: environment-facts-file/1
        self.write("docs/more_facts.md", facts(fact()))
        self.assertFails(facts(), "`docs/more_facts.md` is a second file of environment fact "
                                  "entries")
        self.assertEqual(self.verdicts("environment-facts-file/1"), ["fail"])

    def test_entry_in_a_fenced_block_is_no_entry(self):
        # invariant: environment-facts-file/1
        self.write("docs/how_to.md", "# How to\n\n```markdown\n" + fact() + "\n```\n")
        self.assertPasses(facts())
        self.assertEqual(self.verdicts("environment-facts-file/1"), ["pass"])

    def test_invariants_file_is_no_file_of_facts(self):
        # invariant: environment-facts-file/1
        self.assertPasses(facts())
        self.assertEqual(self.verdicts("environment-facts-file/1"), ["pass"])

    def test_file_outside_a_repository(self):
        with tempfile.TemporaryDirectory() as elsewhere:
            path = os.path.join(elsewhere, "foundations", "environment_facts.md")
            os.makedirs(os.path.dirname(path))
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(facts())
            output = io.StringIO()
            code = format_guard.run(path, stream=output)
        self.assertEqual(code, 1)
        self.assertIn("the file does not lie in a git repository", output.getvalue())


class Identifiers(GuardTestCase):
    def test_identifier_off_the_form(self):
        # invariant: fact-identifier-form/1
        self.assertFails(facts(fact(identifier="Storage-Quota"), lines_fact()),
                         "`Storage-Quota` is not an identifier")
        self.assertEqual(self.verdicts("fact-identifier-form/1"), ["fail"])

    def test_none_is_no_identifier(self):
        # invariant: fact-identifier-form/1
        self.assertFails(facts(fact(identifier="none"), lines_fact()),
                         "`none` is not an identifier")
        self.assertEqual(self.verdicts("fact-identifier-form/1"), ["fail"])

    def test_identifier_twice_in_the_file(self):
        # invariant: identifier-holders/1
        self.assertFails(facts(fact(), lines_fact(identifier="storage-quota")),
                         "identifier `storage-quota` is used twice")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_identifier_held_by_an_invariant(self):
        # invariant: identifier-holders/1
        self.assertFails(facts(fact(), lines_fact(identifier="saves-fit-quota")),
                         "identifier `saves-fit-quota` is held by invariants.md:3")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_identifier_withdrawn_from_the_invariants(self):
        # invariant: identifier-holders/1
        self.assertFails(facts(fact(), lines_fact(identifier="save-size")),
                         "identifier `save-size` is held by invariants.md")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_identifier_held_by_the_part_map(self):
        # invariant: identifier-holders/1
        self.assertFails(facts(fact(), lines_fact(identifier="saving")),
                         "identifier `saving` is held by part_map.md:3")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_withdrawn_identifier_held_by_the_part_map(self):
        # invariant: identifier-holders/1
        withdrawn = WITHDRAWN + "\n| game-state | shown false | none |"
        self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                         "identifier `game-state` is held by part_map.md")
        self.assertEqual(self.verdicts("identifier-holders/1"), ["fail"])

    def test_withdrawn_without_a_reason(self):
        # invariant: fact-withdrawal-successors/1
        withdrawn = WITHDRAWN.replace("split into two facts", "")
        self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                         "withdrawn `storage-limit` gives no reason in *Why*")
        self.assertEqual(self.verdicts("fact-withdrawal-successors/1"), ["fail"])

    def test_successor_that_does_not_exist(self):
        # invariant: fact-withdrawal-successors/1
        withdrawn = WITHDRAWN.replace("storage-quota · json-lines", "storage-cap")
        self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                         "withdrawn `storage-limit` names successor `storage-cap`")
        self.assertEqual(self.verdicts("fact-withdrawal-successors/1"), ["fail"])

    def test_withdrawn_identifier_off_the_form(self):
        # invariant: fact-withdrawal-successors/1
        for identifier in ("Storage-Limit", "storage_limit", "none"):
            with self.subTest(identifier=identifier):
                withdrawn = WITHDRAWN.replace("| storage-limit |", "| %s |" % identifier)
                self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                                 "`%s` is not an identifier of words in lower case joined by "
                                 "hyphens" % identifier)
                self.assertEqual(self.verdicts("fact-withdrawal-successors/1"), ["fail"])
                self.assertEqual(self.verdicts("fact-identifier-form/1"), ["pass"])

    def test_successors_none(self):
        # invariant: fact-withdrawal-successors/1
        withdrawn = WITHDRAWN.replace("storage-quota · json-lines", "none")
        self.assertPasses(facts(fact(), lines_fact(), withdrawn=withdrawn))
        self.assertEqual(self.verdicts("fact-withdrawal-successors/1"), ["pass"])


class Fields(GuardTestCase):
    def test_field_missing(self):
        # invariant: fact-entry-field-presence/1
        self.assertFails(facts(fact(omit=("Method",)), lines_fact()),
                         "storage-quota/1: field *Method* is missing")
        self.assertEqual(self.verdicts("fact-entry-field-presence/1"), ["fail"])

    def test_field_empty(self):
        # invariant: fact-entry-field-presence/1
        self.assertFails(facts(fact(holds=""), lines_fact()),
                         "storage-quota/1: field *Holds for* is missing")
        self.assertEqual(self.verdicts("fact-entry-field-presence/1"), ["fail"])

    def test_none_where_the_form_does_not_give_it(self):
        # invariant: fact-entry-field-words/1
        self.assertFails(facts(fact(method="none"), lines_fact()),
                         "*Method* may not hold `none`")
        self.assertEqual(self.verdicts("fact-entry-field-words/1"), ["fail"])

    def test_source_takes_no_none(self):
        # invariant: fact-entry-field-words/1
        self.assertFails(facts(fact(source="none"), lines_fact()), "*Source* may not hold `none`")
        self.assertEqual(self.verdicts("fact-entry-field-words/1"), ["fail"])

    def test_source_takes_no_todo(self):
        # invariant: fact-entry-field-words/1
        self.assertFails(facts(fact(source="TODO — the MDN page"), lines_fact()),
                         "*Source* may not hold `TODO`")
        self.assertEqual(self.verdicts("fact-entry-field-words/1"), ["fail"])

    def test_todo_inside_a_value(self):
        # invariant: fact-entry-field-words/1
        self.assertFails(facts(fact(holds="Firefox 130; TODO: Chrome"), lines_fact()),
                         "*Holds for* may not hold `TODO`")
        self.assertEqual(self.verdicts("fact-entry-field-words/1"), ["fail"])

    def test_an_entry_without_set_by_and_correction_passes(self):
        # invariant: fact-entry-field-presence/1
        self.assertPasses(facts(fact(), lines_fact()))
        self.assertEqual(self.verdicts("fact-entry-field-presence/1"), ["pass"])

    def test_set_by_is_no_field_of_the_form(self):
        # invariant: fact-entry-field-presence/1
        output = self.assertFails(facts(fact(extra=[("Set by", "the repository owner")]),
                                        lines_fact()),
                                  "storage-quota/1: *Set by* is not a field of the form; the "
                                  "form of a fact holds no field naming who sets what it states")
        self.assertNotIn("field *Set by* is not in the template", output)
        self.assertEqual(self.verdicts("fact-entry-field-presence/1"), ["pass"])

    def test_correction_is_no_field_of_the_form(self):
        # invariant: fact-entry-field-presence/1
        output = self.assertFails(facts(fact(extra=[("Correction", "none")]), lines_fact()),
                                  "storage-quota/1: *Correction* is not a field of the form; "
                                  "every change of the sentence or *Holds for* raises the version")
        self.assertNotIn("field *Correction* is not in the template", output)
        self.assertEqual(self.verdicts("fact-entry-field-presence/1"), ["pass"])

    def test_field_the_form_does_not_hold(self):
        self.assertFails(facts(fact(extra=[("Checked", "2026-09-26")]), lines_fact()),
                         "storage-quota/1: field *Checked* is not in the template")


class Sentence(GuardTestCase):
    def test_two_sentences(self):
        # invariant: fact-sentence-count/1
        self.assertFails(facts(fact(sentence=QUOTA + " Chrome keeps more."), lines_fact()),
                         "storage-quota/1: 2 sentences")
        self.assertEqual(self.verdicts("fact-sentence-count/1"), ["fail"])

    def test_sentence_missing(self):
        # invariant: fact-sentence-count/1
        self.assertFails(facts(fact(sentence=None), lines_fact()),
                         "storage-quota/1: the sentence is missing")
        self.assertEqual(self.verdicts("fact-sentence-count/1"), ["fail"])

    def test_text_after_the_fields(self):
        # invariant: fact-sentence-count/1
        self.assertFails(facts(fact() + "\n\nChrome keeps more.", lines_fact()),
                         "text outside the sentence and the fields")
        self.assertEqual(self.verdicts("fact-sentence-count/1"), ["fail"])


class Scope(GuardTestCase):
    def test_latest(self):
        # invariant: fact-scope-word/1
        self.assertFails(facts(fact(holds="the latest Firefox"), lines_fact()),
                         '*Holds for* reads "latest"')
        self.assertEqual(self.verdicts("fact-scope-word/1"), ["fail"])

    def test_newest_in_capitals(self):
        # invariant: fact-scope-word/1
        self.assertFails(facts(fact(holds="Newest Firefox"), lines_fact()),
                         '*Holds for* reads "newest"')
        self.assertEqual(self.verdicts("fact-scope-word/1"), ["fail"])

    def test_a_word_holding_latest_is_no_scope_word(self):
        # invariant: fact-scope-word/1
        self.assertPasses(facts(fact(holds="Firefox 130 (Latestbuild channel)"), lines_fact()))
        self.assertEqual(self.verdicts("fact-scope-word/1"), ["pass"])


class Source(GuardTestCase):
    def passes(self, source):
        # every test calling this cites fact-source-form, whose pass it asserts
        self.assertPasses(facts(fact(source=source), lines_fact()))
        self.assertEqual(self.verdicts("fact-source-form/1"), ["pass"])

    def fails(self, source):
        self.assertFails(facts(fact(source=source), lines_fact()),
                         "storage-quota/1: *Source* is neither")
        self.assertEqual(self.verdicts("fact-source-form/1"), ["fail"])

    def test_page_of_an_edition(self):
        # invariant: fact-source-form/1
        self.passes(QUOTA_SOURCE)

    def test_page_without_editions_and_its_archived_copy(self):
        # invariant: fact-source-form/1
        self.passes(LINES_SOURCE)

    def test_two_passages_of_one_place(self):
        # invariant: fact-source-form/1
        self.passes('https://developer.mozilla.org/docs/storage/130 § Web Storage — "Web Storage is '
                    'limited" · "to a total of 10 MiB of data per origin."; read 2026-09-26')

    def test_two_places_of_one_page(self):
        # invariant: fact-source-form/1
        self.passes('https://www.rfc-editor.org/rfc/rfc8259.html § 2 — "A JSON text is a serialized '
                    'value." · § 6 — "Numeric values that cannot be represented in the grammar '
                    'below (such as Infinity and NaN) are not permitted."; read 2026-09-26')

    def test_two_pages_of_one_edition(self):
        # invariant: fact-source-form/1
        self.passes(QUOTA_SOURCE + ' · https://developer.mozilla.org/docs/storage/130/limits '
                                   '§ Limits — "per origin"; read 2026-09-26')

    def test_observation(self):
        # invariant: fact-source-form/1
        self.passes("observed: `curl https://example.org/` on curl 8.21.0, "
                    "Windows; run 2026-09-26")

    def test_passage_in_curly_quotes_holding_straight_ones(self):
        # invariant: fact-source-form/1
        self.passes('https://csrc.nist.gov/fips/180-4 § 6.2 — “Input Message: "abc"”; '
                    'read 2026-09-26')

    def test_no_date_read(self):
        # invariant: fact-source-form/1
        self.fails('https://developer.mozilla.org/docs/storage/130 § Web Storage — "Web Storage is '
                   'limited to a total of 10 MiB of data per origin."')

    def test_no_place(self):
        # invariant: fact-source-form/1
        self.fails('https://developer.mozilla.org/docs/storage/130 — "Web Storage is limited to a '
                   'total of 10 MiB of data per origin."; read 2026-09-26')

    def test_summary_in_place_of_the_passage(self):
        # invariant: fact-source-form/1
        self.fails("https://developer.mozilla.org/docs/storage/130 § Web Storage — web storage is "
                   "limited to 10 MiB; read 2026-09-26")

    def test_work_without_an_address(self):
        # invariant: fact-source-form/1
        self.fails('MDN, Storage quotas § Web Storage — "Web Storage is limited to a total of '
                   '10 MiB of data per origin."; read 2026-09-26')

    def test_observation_without_a_platform(self):
        # invariant: fact-source-form/1
        self.fails("observed: `curl https://example.org/` on curl 8.21.0; "
                   "run 2026-09-26")

    def test_date_that_does_not_exist(self):
        # invariant: fact-source-form/1
        self.assertFails(facts(fact(source=QUOTA_SOURCE.replace("2026-09-26", "2026-02-30")),
                               lines_fact()), "`2026-02-30`, which is not a date")
        self.assertEqual(self.verdicts("fact-source-form/1"), ["fail"])

    def test_archived_copy_with_a_date_that_does_not_exist(self):
        # invariant: fact-source-form/1
        self.assertFails(facts(fact(), lines_fact(source=LINES_SOURCE.replace("2026-09-18",
                                                                              "2026-13-18"))),
                         "`2026-13-18`, which is not a date")
        self.assertEqual(self.verdicts("fact-source-form/1"), ["fail"])


class Method(GuardTestCase):
    def test_path_of_a_file_that_exists(self):
        # invariant: fact-method-form/1
        self.assertPasses(facts(fact(method="docs/audience.md"), lines_fact()))
        self.assertEqual(self.verdicts("fact-method-form/1"), ["pass"])

    def test_path_of_no_file(self):
        # invariant: fact-method-form/1
        self.assertFails(facts(fact(method="docs/missing.md"), lines_fact()),
                         "*Method* names `docs/missing.md`, which is not a file")
        self.assertEqual(self.verdicts("fact-method-form/1"), ["fail"])

    def test_command_beginning_with_a_flag(self):
        # invariant: fact-method-form/1
        self.assertFails(facts(fact(method="`-B probes/storage_quota.py`"), lines_fact()),
                         "a command begins with the name of the program it runs, not `-B`")
        self.assertEqual(self.verdicts("fact-method-form/1"), ["fail"])

    def test_prose_in_place_of_a_method(self):
        # invariant: fact-method-form/1
        self.assertFails(facts(fact(method="read the MDN page again"), lines_fact()),
                         "*Method* is neither a command in backticks, the path of a file, nor `TODO`")
        self.assertEqual(self.verdicts("fact-method-form/1"), ["fail"])

    def test_todo(self):
        # invariant: fact-method-form/1
        self.assertPasses(facts(fact(method="`TODO`"), lines_fact()))
        self.assertEqual(self.verdicts("fact-method-form/1"), ["pass"])


class Fingerprint(unittest.TestCase):
    def entry(self, text):
        return [item for item in format_guard.parse_file(text, format_guard.read_rules())
                if isinstance(item, format_guard.Entry)][0]

    def test_fingerprint_of_the_sentence_and_holds_for(self):
        # invariant: fact-fingerprint-input/1
        self.assertEqual(format_guard.entry_fingerprint(self.entry(fact())), QUOTA_FINGERPRINT)

    def test_holds_for_moves_the_fingerprint(self):
        # invariant: fact-fingerprint-input/1
        self.assertEqual(format_guard.entry_fingerprint(self.entry(fact(holds="Firefox 131"))),
                         QUOTA_WIDER_FINGERPRINT)

    def test_the_rest_of_the_entry_leaves_it(self):
        # invariant: fact-fingerprint-input/1
        entry = self.entry(fact(source=LINES_SOURCE, method="`TODO`",
                                extra=old_fields("the owner", "0635a942 → 11ba3f2d")))
        self.assertEqual(format_guard.entry_fingerprint(entry), QUOTA_FINGERPRINT)

    def test_the_sentence_alone_is_not_it(self):
        # invariant: fact-fingerprint-input/1
        self.assertNotEqual(format_guard.entry_fingerprint(self.entry(fact())),
                            QUOTA_SENTENCE_ALONE_FINGERPRINT)


class RecordPaths(GuardTestCase):
    def test_record_git_ignores(self):
        # invariant: run-record-path/1
        self.assertPasses(facts(fact(method="`python -B probes/storage_quota.py --record "
                                            ".runs/facts.jsonl`"), lines_fact()))
        self.assertEqual(self.verdicts("run-record-path/1"), ["pass"])

    def test_record_git_does_not_ignore(self):
        # invariant: run-record-path/1
        self.assertFails(facts(fact(method="`python -B probes/storage_quota.py --record "
                                           "runs/facts.jsonl`"), lines_fact()),
                         "git does not ignore `runs/facts.jsonl`")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_record_ignored_only_by_letter_case(self):
        # invariant: run-record-path/1
        self.assertFails(facts(fact(method="`python -B probes/storage_quota.py --record "
                                           ".Runs/facts.jsonl`"), lines_fact()),
                         "git does not ignore `.Runs/facts.jsonl`")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_two_records(self):
        # invariant: run-record-path/1
        self.assertFails(facts(fact(method="`python -B probes/storage_quota.py --record "
                                           ".runs/a.jsonl --also .runs/b.jsonl`"), lines_fact()),
                         "the command names 2 records of a run")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])

    def test_record_outside_the_repository(self):
        # invariant: run-record-path/1
        self.assertFails(facts(fact(method="`python -B probes/storage_quota.py --record "
                                           "../facts.jsonl`"), lines_fact()),
                         "lies outside the repository")
        self.assertEqual(self.verdicts("run-record-path/1"), ["fail"])


class Citations(GuardTestCase):
    def cite(self, line, name="probes/storage_quota.py"):
        self.write(name, line + "\nprint('10 MiB')\n")

    def test_citation_of_the_current_version(self):
        # invariant: fact-citation-version/1
        # invariant: fact-citation-target/1
        self.assertPasses(facts())
        self.assertEqual(self.verdicts("fact-citation-version/1"), ["pass"])
        self.assertEqual(self.verdicts("fact-citation-target/1"), ["pass"])

    def test_citation_of_another_version(self):
        # invariant: fact-citation-version/1
        self.cite("# fact: storage-quota/2")
        self.assertFails(facts(), "probes/storage_quota.py:1: cites `storage-quota/2`, whose "
                                  "current version is 1")
        self.assertEqual(self.verdicts("fact-citation-version/1"), ["fail"])

    def test_citation_without_a_version(self):
        # invariant: fact-citation-version/1
        self.cite("# fact: storage-quota")
        self.assertFails(facts(), "`fact: storage-quota` does not cite `<identifier>/<version>`")
        self.assertEqual(self.verdicts("fact-citation-version/1"), ["fail"])

    def test_citation_with_a_leading_zero(self):
        # invariant: fact-citation-version/1
        self.cite("# fact: storage-quota/01")
        self.assertFails(facts(), "`fact: storage-quota/01` does not cite")
        self.assertEqual(self.verdicts("fact-citation-version/1"), ["fail"])

    def test_citation_of_a_withdrawn_fact(self):
        # invariant: fact-citation-target/1
        self.cite("# fact: storage-limit/1")
        self.assertFails(facts(), "cites `storage-limit`, which is withdrawn")
        self.assertEqual(self.verdicts("fact-citation-target/1"), ["fail"])

    def test_citation_of_no_fact(self):
        # invariant: fact-citation-target/1
        self.cite("// fact: storage-cap/1", name="probes/storage.js")
        self.assertFails(facts(), "probes/storage.js:1: cites `storage-cap`, which is not an "
                                  "environment fact")
        self.assertEqual(self.verdicts("fact-citation-target/1"), ["fail"])

    def test_markdown_holds_no_check(self):
        # invariant: fact-citation-target/1
        self.cite("# fact: storage-cap/1", name="docs/notes.md")
        self.assertPasses(facts())
        self.assertEqual(self.verdicts("fact-citation-target/1"), ["pass"])

    def test_comment_of_several_words_is_no_citation(self):
        # invariant: fact-citation-target/1
        self.cite("# fact: the quota moved in Firefox 131")
        self.assertPasses(facts())
        self.assertEqual(self.verdicts("fact-citation-target/1"), ["pass"])


class HumanVerdicts(GuardTestCase):
    def row(self, **changes):
        values = dict(entry="storage-quota", version="1", verdict="pass", by="Mariusz",
                      on="2026-09-26", commit="b06eacd", until="2026-12-31")
        values.update(changes)
        return tuple(values[name] for name in ("entry", "version", "verdict", "by", "on", "commit",
                                               "until"))

    def check(self, row, fragment=None):
        # every test calling this cites human-verdict-fact-row, whose verdict it asserts
        text = facts(fact(method="docs/audience.md"), lines_fact())
        files = {"foundations/human_verdicts.md": verdicts(row)}
        if fragment is None:
            self.assertPasses(text, **files)
            self.assertEqual(self.verdicts("human-verdict-fact-row/1"), ["pass"])
        else:
            self.assertFails(text, fragment, **files)
            self.assertEqual(self.verdicts("human-verdict-fact-row/1"), ["fail"])

    def test_no_file(self):
        # invariant: human-verdict-fact-row/1
        output = self.assertPasses(facts())
        self.assertIn("note: there is no human_verdicts.md", output)
        self.assertEqual(self.verdicts("human-verdict-fact-row/1"), ["pass"])

    def test_row_in_its_form(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row())

    def test_row_for_a_fact_whose_method_is_a_command(self):
        # invariant: human-verdict-fact-row/1
        self.assertFails(facts(), "human_verdicts.md:5: the method of `storage-quota` is not a "
                                  "path", **{"foundations/human_verdicts.md": verdicts(self.row())})
        self.assertEqual(self.verdicts("human-verdict-fact-row/1"), ["fail"])

    def test_verdict_neither_pass_nor_fail(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(verdict="holds"), "*Verdict* is neither `pass` nor `fail`")

    def test_nobody_gave_it(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(by="none"), "*By* names nobody")

    def test_given_on_no_date(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(on="yesterday"), "*On* is not a date")

    def test_no_commit(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(commit="HEAD"), "*Commit* names no commit")

    def test_until_none(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(until="none"), "*Until* is not a date")

    def test_version_not_a_number(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(version="one"), "*Version* is not a number")

    def test_row_naming_an_invariant_is_the_invariants_guards(self):
        # invariant: human-verdict-fact-row/1
        self.check(self.row(entry="saves-fit-quota", until="none"))

    def test_row_naming_neither(self):
        """A row carrying a date in *Until* has a fact's form (rules.md), so one that names no
        entry of either file is a fact row naming no fact."""
        # invariant: human-verdict-fact-row/1
        self.assertFails(facts(), "`storage-cap` is neither an invariant nor an environment fact",
                         **{"foundations/human_verdicts.md": verdicts(self.row(entry="storage-cap"))})
        self.assertEqual(self.verdicts("human-verdict-fact-row/1"), ["fail"])

    def test_row_naming_neither_with_none_in_until_is_the_invariants_guards(self):
        """A row reading `none` in *Until* has an invariant's form; one that names no entry of
        either file is reported, and the invariants guard judges it as an invariant row."""
        # invariant: human-verdict-fact-row/1
        self.assertFails(facts(), "`storage-cap` is neither an invariant nor an environment fact",
                         **{"foundations/human_verdicts.md":
                            verdicts(self.row(entry="storage-cap", until="none"))})
        self.assertEqual(self.verdicts("human-verdict-fact-row/1"), ["pass"])

    def test_list_with_other_columns(self):
        self.assertFails(facts(), "the list has columns Entry | Verdict",
                         **{"foundations/human_verdicts.md": "| Entry | Verdict |\n|---|---|\n"
                                                             "| storage-quota | pass |\n"})


class BasedOn(GuardTestCase):
    def check(self, based_on, fragment=None, *earlier):
        # every test calling this cites based-on-fact-fingerprint, whose verdict it asserts
        files = {"foundations/decisions.md": log(*(list(earlier) + [
            decision(len(earlier) + 1, based_on)]))}
        if fragment is None:
            self.assertPasses(facts(), **files)
            self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["pass"])
        else:
            self.assertFails(facts(), fragment, **files)

    def test_fact_named_without_a_fingerprint(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("JSON Lines holds one value on each line: json-lines.",
                   "WAY-01/1: *Based on* names the fact `json-lines` with no fingerprint")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_fact_named_in_backticks_without_a_fingerprint(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("JSON Lines holds one value on each line (`json-lines`).",
                   "names the fact `json-lines` with no fingerprint")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_withdrawn_fact_named_without_a_fingerprint(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s · storage-limit" % LINES_FINGERPRINT,
                   "names the fact `storage-limit` with no fingerprint")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_identifier_inside_an_address_is_no_fact(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s, read at https://example.org/json-lines.html and "
                   "https://example.org/json-lines/" % LINES_FINGERPRINT)

    def test_identifier_inside_quoted_text_is_no_fact(self):
        # invariant: based-on-fact-fingerprint/1
        self.check('json-lines@%s; the page says "see json-lines for more"' % LINES_FINGERPRINT)

    def test_identifier_inside_a_longer_word_is_no_fact(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s, unlike strict-json-lines-v2" % LINES_FINGERPRINT)

    def test_fingerprint_shorter_than_the_relation_model_gives(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@ffce95", "`json-lines@ffce95` carries no fingerprint of 8 hex digits")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_fact_named_with_its_version(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("JSON Lines holds one value on each line: json-lines/1.",
                   "names the fact `json-lines` as `json-lines/1`; it reads "
                   "`json-lines@<fingerprint>`")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_fact_named_with_the_placeholder_of_a_message(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@<fingerprint>", "names the fact `json-lines` as "
                                               "`json-lines@<fingerprint>`")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_fact_named_with_nothing_after_the_at(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("JSON Lines, json-lines@ and more", "names the fact `json-lines` as "
                                                       "`json-lines@`")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_version_inside_an_address_is_no_fact(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s, read at https://example.org/json-lines/1" % LINES_FINGERPRINT)

    def test_link_to_no_fact(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s · storage-cap@12345678" % LINES_FINGERPRINT,
                   "*Based on* names `storage-cap@12345678`, which is no environment fact")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_link_to_a_withdrawn_fact_is_left_to_the_merge(self):
        """A withdrawn fact has no current fingerprint; that is reported against a merge
        (based-on-fact-fingerprint-value), not here."""
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s · storage-limit@12345678" % LINES_FINGERPRINT)

    def test_earlier_version_is_not_read(self):
        # invariant: based-on-fact-fingerprint/1
        self.check("json-lines@%s" % LINES_FINGERPRINT, None, decision(1, "json-lines, bare"))


class Dependants(GuardTestCase):
    def test_fact_nothing_names_warns_on_a_task_branch(self):
        code, output = self.guard(facts(fact(), lines_fact(),
                                        fact(identifier="storage-events", sentence="Firefox fires a "
                                                                                   "storage event.")))
        self.assertEqual(code, 0, output)
        self.assertIn("warning: storage-events/1: no invariant's *Rests on* and no decision's "
                      "*Based on* names it", output)
        self.assertEqual(self.verdicts("fact-dependants/1"), [])

    def test_fact_nothing_names_fails_a_merge(self):
        # invariant: fact-dependants/1
        self.commit(facts())
        text = facts(fact(), lines_fact(), fact(identifier="storage-events",
                                                sentence="Firefox fires a storage event."))
        self.assertFails(text, "storage-events/1: no invariant's *Rests on* and no decision's "
                               "*Based on* names it", merge_onto="HEAD")
        self.assertEqual(self.verdicts("fact-dependants/1"), ["fail"])

    def test_facts_named_by_an_invariant_and_by_a_decision_pass_a_merge(self):
        # invariant: fact-dependants/1
        self.commit(facts())
        self.assertPasses(facts(), merge_onto="HEAD")
        self.assertEqual(self.verdicts("fact-dependants/1"), ["pass"])

    def test_invariant_only_the_commit_merged_onto_holds_names_it(self):
        # invariant: fact-dependants/1
        self.commit(facts(), **{"foundations/invariants.md": invariants(invariant(
            rests="storage-quota@" + QUOTA_FINGERPRINT), invariant("saves-small", rests="none"))})
        self.write("foundations/invariants.md", invariants(invariant("saves-small", rests="none")))
        self.assertPasses(facts(), merge_onto="HEAD")
        self.assertEqual(self.verdicts("fact-dependants/1"), ["pass"])


class AgainstBase(GuardTestCase):
    def test_new_entry_at_version_two(self):
        # invariant: fact-version-new/1
        self.commit(facts(fact()))
        self.assertFails(facts(fact(), lines_fact(version=2)),
                         "json-lines/2: a new entry carries version 1", base="HEAD")
        self.assertEqual(self.verdicts("fact-version-new/1"), ["fail"])

    def test_new_entry_at_version_one_carrying_a_correction(self):
        # invariant: fact-version-new/1
        self.commit(facts(fact()))
        output = self.assertFails(facts(fact(), lines_fact(extra=old_fields(
            correction="00000000 → " + LINES_FINGERPRINT))), "*Correction* is not a field",
            base="HEAD")
        self.assertNotIn("declares no correction", output)
        self.assertEqual(self.verdicts("fact-version-new/1"), ["pass"])

    def test_reworded_sentence_at_the_same_version(self):
        # invariant: fact-version-changed/1
        self.commit(facts())
        self.assertFails(facts(fact(sentence=QUOTA_REWORDED), lines_fact()),
                         "storage-quota/1: the sentence or *Holds for* changed since HEAD (%s → %s)"
                         % (QUOTA_FINGERPRINT, QUOTA_REWORDED_FINGERPRINT), base="HEAD")
        self.assertEqual(self.verdicts("fact-version-changed/1"), ["fail"])

    def test_widened_scope_at_the_same_version(self):
        # invariant: fact-version-changed/1
        self.commit(facts())
        self.assertFails(facts(fact(holds="Firefox 131"), lines_fact()),
                         "(%s → %s)" % (QUOTA_FINGERPRINT, QUOTA_WIDER_FINGERPRINT), base="HEAD")
        self.assertEqual(self.verdicts("fact-version-changed/1"), ["fail"])

    def test_raised_version(self):
        # invariant: fact-version-changed/1
        self.commit(facts())
        self.assertPasses(facts(fact(version=2, holds="Firefox 131"), lines_fact()), base="HEAD",
                          **{"probes/storage_quota.py": "# fact: storage-quota/2\n"})
        self.assertEqual(self.verdicts("fact-version-changed/1"), ["pass"])

    def test_a_correction_keeps_no_version(self):
        # invariant: fact-version-changed/1
        self.commit(facts())
        output = self.assertFails(facts(fact(sentence=QUOTA_REWORDED, extra=old_fields(
            correction="%s → %s" % (QUOTA_FINGERPRINT, QUOTA_REWORDED_FINGERPRINT))), lines_fact()),
            "storage-quota/1: the sentence or *Holds for* changed since HEAD (%s → %s); the version "
            "is 2" % (QUOTA_FINGERPRINT, QUOTA_REWORDED_FINGERPRINT), base="HEAD")
        self.assertNotIn("correction declared", output)
        self.assertEqual(self.verdicts("fact-version-changed/1"), ["fail"])

    def test_a_typo_fixed_raises_the_version(self):
        # invariant: fact-version-changed/1
        self.commit(facts())
        self.assertPasses(facts(fact(version=2, sentence=QUOTA_REWORDED), lines_fact()),
                          base="HEAD", **{"probes/storage_quota.py": "# fact: storage-quota/2\n"})
        self.assertEqual(self.verdicts("fact-version-changed/1"), ["pass"])

    def test_new_source_leaves_the_version(self):
        # invariant: fact-version-unchanged/1
        self.commit(facts())
        self.assertPasses(facts(fact(source=QUOTA_SOURCE.replace("2026-09-26", "2026-10-01")),
                                lines_fact()), base="HEAD")
        self.assertEqual(self.verdicts("fact-version-unchanged/1"), ["pass"])

    def test_version_raised_with_nothing_changed(self):
        # invariant: fact-version-unchanged/1
        self.commit(facts())
        self.assertFails(facts(fact(version=2), lines_fact()),
                         "storage-quota/2: the sentence and *Holds for* are unchanged since HEAD, "
                         "where the version is 1", base="HEAD")
        self.assertEqual(self.verdicts("fact-version-unchanged/1"), ["fail"])

    def test_unchanged_entry_carrying_a_correction(self):
        # invariant: fact-version-unchanged/1
        self.commit(facts())
        output = self.assertFails(facts(fact(extra=old_fields(correction="00000000 → 12345678")),
                                        lines_fact()), "*Correction* is not a field",
                                  base="HEAD")
        self.assertNotIn("the correction names", output)
        self.assertEqual(self.verdicts("fact-version-unchanged/1"), ["pass"])

    def test_identifier_gone(self):
        # invariant: fact-identifier-persistence/1
        self.commit(facts())
        withdrawn = WITHDRAWN.replace("storage-quota · json-lines", "storage-quota")
        self.assertFails(facts(fact(), withdrawn=withdrawn), "`json-lines` stands in the file on "
                                                             "HEAD and is gone", base="HEAD")
        self.assertEqual(self.verdicts("fact-identifier-persistence/1"), ["fail"])

    def test_withdrawn_identifier_gone(self):
        # invariant: fact-withdrawal-persistence/1
        self.commit(facts())
        self.assertFails(facts(fact(), lines_fact(), withdrawn="## Withdrawn identifiers\n\n"
                                                               "| Identifier | Why | Successors |\n"
                                                               "|---|---|---|"),
                         "`storage-limit` stands in the file on HEAD and is gone", base="HEAD")
        self.assertEqual(self.verdicts("fact-withdrawal-persistence/1"), ["fail"])

    def test_withdrawn_identifier_back_as_an_entry(self):
        # invariant: fact-withdrawal-persistence/1
        self.commit(facts())
        withdrawn = WITHDRAWN.replace("storage-limit", "json-lines").replace(
            "storage-quota · json-lines", "storage-quota")
        self.write("foundations/environment_facts.md", facts(fact(), withdrawn=withdrawn))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "withdraw")
        self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                         "`json-lines` is withdrawn on HEAD and stands as an entry again",
                         base="HEAD")
        self.assertIn("fail", self.verdicts("fact-withdrawal-persistence/1"))

    def test_split_entry_withdrawn_under_new_identifiers(self):
        # invariant: fact-identifier-persistence/1
        self.commit(facts(fact(identifier="web-storage"), withdrawn=WITHDRAWN.replace(
            "storage-quota · json-lines", "web-storage")))
        withdrawn = WITHDRAWN.replace("storage-quota · json-lines", "web-storage") + \
            "\n| web-storage | split into two facts | storage-quota · json-lines |"
        self.assertPasses(facts(fact(), lines_fact(), withdrawn=withdrawn), base="HEAD")
        self.assertEqual(self.verdicts("fact-identifier-persistence/1"), ["pass"])

    def test_no_main_branch(self):
        output = self.assertPasses(facts(), base="none")
        self.assertIn("--base none", output)
        for invariant in BASE:
            self.assertEqual(self.verdicts(invariant), ["unchecked"], invariant)
        self.assertTrue(all(line.get("reason") == NO_COMMIT for line in self.lines))

    def test_base_that_does_not_exist(self):
        self.commit(facts())
        code, output = self.guard(facts(), base="no-such-commit")
        self.assertEqual(code, 1, output)
        self.assertIn("no-such-commit", output)


class Merge(GuardTestCase):
    def test_stale_fingerprint_in_based_on(self):
        # invariant: based-on-fact-fingerprint-value/1
        self.commit(facts())
        self.assertFails(facts(fact(), lines_fact(version=2, holds="JSON Lines 1.1")),
                         "`json-lines@%s` — the current fingerprint of `json-lines` after the merge"
                         % LINES_FINGERPRINT, merge_onto="HEAD")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])

    def test_current_fingerprint_in_based_on(self):
        # invariant: based-on-fact-fingerprint-value/1
        self.commit(facts())
        self.assertPasses(facts(), merge_onto="HEAD")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["pass"])

    def test_decision_only_the_commit_merged_onto_holds(self):
        # invariant: based-on-fact-fingerprint-value/1
        self.commit(facts(), **{"foundations/decisions.md": log(
            decision(), decision(2, "storage-quota@00000000 · json-lines@" + LINES_FINGERPRINT))})
        self.write("foundations/decisions.md", log())
        self.assertFails(facts(), "WAY-01/2: `storage-quota@00000000` — the current fingerprint of "
                                  "`storage-quota` after the merge is " + QUOTA_FINGERPRINT,
                         merge_onto="HEAD")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])

    def test_fact_only_the_commit_merged_onto_holds(self):
        # invariant: based-on-fact-fingerprint-value/1
        events = fact(identifier="storage-events", sentence="Firefox fires a storage event.",
                      holds="Firefox 130")
        self.commit(facts(fact(), lines_fact(), events))
        self.assertFails(facts(), "`storage-events@00000000` — the current fingerprint of "
                                  "`storage-events` after the merge is",
                         merge_onto="HEAD", **{"foundations/decisions.md": log(decision(
                             1, "json-lines@%s · storage-events@00000000" % LINES_FINGERPRINT))})
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])

    def test_todo_in_method_is_taken(self):
        # invariant: fact-entry-merge-todo/1
        self.commit(facts())
        self.assertPasses(facts(), merge_onto="HEAD")
        self.assertEqual(self.verdicts("fact-entry-merge-todo/1"), ["pass"])

    def test_todo_elsewhere_is_not_taken(self):
        # invariant: fact-entry-merge-todo/1
        self.commit(facts())
        self.assertFails(facts(fact(holds="Firefox 130; TODO — which release"), lines_fact()),
                         "*Holds for* holds `TODO`, which a merge onto the main branch does not "
                         "take", merge_onto="HEAD")
        self.assertEqual(self.verdicts("fact-entry-merge-todo/1"), ["fail"])

    def test_no_main_branch(self):
        output = self.assertPasses(facts(), merge_onto="none")
        self.assertIn("--merge-onto none", output)
        for invariant in MERGE:
            self.assertEqual(self.verdicts(invariant), ["unchecked"], invariant)


class MergeOfTwoBranches(GuardTestCase):
    """The main branch moved on after the task branch left it (WAY-07, WAY-73, WAY-90)."""

    def branch_off(self, main_text, **main_files):
        """Commits a base, leaves it on a task branch, and commits the main branch's next state."""
        self.commit(facts())
        self.git("checkout", "-q", "-b", "task")
        self.git("checkout", "-q", "main")
        self.commit(main_text, **main_files)
        self.git("checkout", "-q", "task")

    def test_fact_the_main_branch_raised_and_the_branch_left_alone(self):
        # invariant: based-on-fact-fingerprint-value/1
        self.branch_off(facts(fact(), lines_fact(version=2, holds="JSON Lines 1.1")))
        self.assertFails(facts(), "`json-lines@%s` — the current fingerprint of `json-lines` after "
                                  "the merge is" % LINES_FINGERPRINT, merge_onto="main")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])

    def test_fact_the_branch_raised_itself(self):
        # invariant: based-on-fact-fingerprint-value/1
        self.branch_off(facts(), **{"src/saving.py": "def save():\n    return None\n"})
        self.assertFails(facts(fact(), lines_fact(version=2, holds="JSON Lines 1.1")),
                         "the current fingerprint of `json-lines` after the merge is",
                         merge_onto="main")
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])

    def test_invariant_the_branch_withdrew_names_no_fact(self):
        # invariant: fact-dependants/1
        self.branch_off(facts(), **{"src/saving.py": "def save():\n    return None\n"})
        withdrawn_invariant = invariants(invariant("saves-small", rests="none")).replace(
            "| save-size | saves-fit-quota |",
            "| save-size | saves-fit-quota |\n| saves-fit-quota | none |")
        self.assertFails(facts(), "storage-quota/1: no invariant's *Rests on* and no decision's "
                                  "*Based on* names it", merge_onto="main",
                         **{"foundations/invariants.md": withdrawn_invariant})
        self.assertEqual(self.verdicts("fact-dependants/1"), ["fail"])

    def test_withdrawn_fact_cited_by_a_decision(self):
        # invariant: based-on-fact-fingerprint-value/1
        self.commit(facts())
        self.assertFails(facts(), "`storage-limit@12345678` names a withdrawn environment fact, "
                                  "which has no current fingerprint; the decision is renewed on its "
                                  "successors, storage-quota · json-lines",
                         merge_onto="HEAD", **{"foundations/decisions.md": log(decision(
                             1, "json-lines@%s · storage-limit@12345678" % LINES_FINGERPRINT))})
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])

    def test_fact_shown_false_cited_by_a_decision(self):
        # invariant: based-on-fact-fingerprint-value/1
        withdrawn = WITHDRAWN + "\n| storage-cap | shown false by Firefox 131 | none |"
        self.commit(facts(fact(), lines_fact(), withdrawn=withdrawn))
        self.assertFails(facts(fact(), lines_fact(), withdrawn=withdrawn),
                         "`storage-cap@12345678` names a withdrawn environment fact, which has no "
                         "current fingerprint; the decision goes to review", merge_onto="HEAD",
                         **{"foundations/decisions.md": log(decision(
                             1, "json-lines@%s · storage-cap@12345678" % LINES_FINGERPRINT))})
        self.assertEqual(self.verdicts("based-on-fact-fingerprint-value/1"), ["fail"])


class PanelCorrections(GuardTestCase):
    def test_citation_with_words_after_it(self):
        # invariant: fact-citation-version/1
        self.write("probes/storage_quota.py", "# fact: storage-quota/2 (the MDN page)\n")
        self.assertFails(facts(), "`fact: storage-quota/2 (the MDN page)` does not cite")
        self.assertEqual(self.verdicts("fact-citation-version/1"), ["fail"])

    def test_source_holding_todo_among_other_text(self):
        # invariant: fact-source-form/1
        self.assertFails(facts(fact(source="the MDN page, TODO: find the edition"), lines_fact()),
                         "*Source* is neither")
        self.assertEqual(self.verdicts("fact-source-form/1"), ["fail"])

    def test_passage_holding_the_word_todo(self):
        # invariant: fact-entry-field-words/1
        # invariant: fact-entry-merge-todo/1
        self.commit(facts())
        source = ('https://example.org/linter/4.0 § Rules — "Comments marked TODO are reported."; '
                  'read 2026-09-26')
        self.assertPasses(facts(fact(source=source), lines_fact()))
        self.assertEqual(self.verdicts("fact-entry-field-words/1"), ["pass"])
        self.assertPasses(facts(fact(source=source), lines_fact()), merge_onto="HEAD")
        self.assertEqual(self.verdicts("fact-entry-merge-todo/1"), ["pass"])

    def test_text_between_two_quoted_parts(self):
        # invariant: fact-source-form/1
        self.assertFails(facts(fact(source='https://developer.mozilla.org/docs/storage/130 § Web '
                                           'Storage — "Web Storage" is said to be "limited"; read '
                                           '2026-09-26'), lines_fact()), "*Source* is neither")
        self.assertEqual(self.verdicts("fact-source-form/1"), ["fail"])

    def test_address_holding_parentheses(self):
        # invariant: fact-source-form/1
        self.assertPasses(facts(fact(source='https://learn.microsoft.com/library/aa365247(v=vs.85) '
                                           '§ Naming — "Do not use the following reserved names"; '
                                           'read 2026-09-26'), lines_fact()))
        self.assertEqual(self.verdicts("fact-source-form/1"), ["pass"])

    def test_fingerprint_in_capitals(self):
        # invariant: based-on-fact-fingerprint/1
        self.assertFails(facts(), "`json-lines@FFCE9572` carries no fingerprint of 8 hex digits",
                         **{"foundations/decisions.md": log(decision(1, "json-lines@FFCE9572"))})
        self.assertEqual(self.verdicts("based-on-fact-fingerprint/1"), ["fail"])

    def test_entry_named_none_is_no_fact_of_a_based_on_reading_none(self):
        code, output = self.guard(facts(fact(), lines_fact(), fact(identifier="none")),
                                  **{"foundations/decisions.md": log(decision(), decision(
                                      2, "json-lines@%s" % LINES_FINGERPRINT).replace(
                                      "WAY-01/2", "WAY-02/1").replace(
                                      "new wording", "new decision"),
                                      decision(1, "none").replace("WAY-01/1", "WAY-03/1"))})
        self.assertIn("`none` is not an identifier", output)
        self.assertNotIn("names the fact `none`", output)

    def test_successors_none_in_backticks(self):
        # invariant: fact-withdrawal-successors/1
        withdrawn = WITHDRAWN.replace("storage-quota · json-lines", "`none`")
        self.assertPasses(facts(fact(), lines_fact(), withdrawn=withdrawn))
        self.assertEqual(self.verdicts("fact-withdrawal-successors/1"), ["pass"])

    def test_entry_in_a_tilde_fence_is_no_entry(self):
        # invariant: environment-facts-file/1
        self.write("docs/how_to.md", "# How to\n\n~~~markdown\n" + fact() + "\n~~~\n")
        self.assertPasses(facts())
        self.assertEqual(self.verdicts("environment-facts-file/1"), ["pass"])

    def test_version_zero(self):
        self.assertFails(facts(fact(version=0), lines_fact()),
                         "heading `## storage-quota/0` of an entry carries no version number")

    def test_version_with_a_leading_zero(self):
        self.assertFails(facts(fact(heading="## storage-quota/01"), lines_fact()),
                         "heading `## storage-quota/01` of an entry carries no version number")

    def test_method_path_in_another_letter_case(self):
        # invariant: fact-method-form/1
        self.assertFails(facts(fact(method="docs/Audience.md"), lines_fact()),
                         "*Method* names `docs/Audience.md`, which is not a file git tracks")
        self.assertEqual(self.verdicts("fact-method-form/1"), ["fail"])

    def test_method_path_git_does_not_track(self):
        # invariant: fact-method-form/1
        self.write(".gitignore", ".runs/\ndocs/private.md\n")
        self.write("docs/private.md", "# Private\n")
        self.assertFails(facts(fact(method="docs/private.md"), lines_fact()),
                         "*Method* names `docs/private.md`, which is not a file git tracks")
        self.assertEqual(self.verdicts("fact-method-form/1"), ["fail"])


class Record(GuardTestCase):
    def test_plain_run_records_the_checks_of_the_file_alone(self):
        self.assertPasses(facts())
        self.assertEqual(sorted(line["invariant"] for line in self.lines), PLAIN)

    def test_base_run_records_the_checks_against_the_base(self):
        self.commit(facts())
        self.assertPasses(facts(), base="HEAD")
        self.assertEqual(sorted(line["invariant"] for line in self.lines), BASE)

    def test_merge_run_records_the_checks_of_a_merge(self):
        self.commit(facts())
        self.assertPasses(facts(), merge_onto="HEAD")
        self.assertEqual(sorted(line["invariant"] for line in self.lines), MERGE)

    def test_error_of_no_invariant_is_a_null_line(self):
        self.assertFails(facts(fact(extra=[("Set by", "none")]), lines_fact()), "*Set by*")
        self.assertIn({"check": "elements/environment-facts/format_guard.py::check_fields",
                       "verdict": "fail", "invariant": None,
                       "description": "line 10: storage-quota/1: *Set by* is not a field of the "
                                      "form; the form of a fact holds no field naming who sets "
                                      "what it states"}, self.lines)

    def test_unreadable_template_stops_the_run(self):
        output = io.StringIO()
        self.write("foundations/environment_facts.md", facts())
        code = format_guard.run(self.path, stream=output, record=self.record_path,
                                template=os.path.join(self.root, "missing.md"))
        self.assertEqual(code, 2)
        self.assertIn("cannot read the rules", output.getvalue())


class OwnFile(unittest.TestCase):
    """The entries of the-way's environment facts still carry *Set by* and *Correction*, which the
    guard reports in one place only: such a line in an entry. Once the entries drop them, the file
    passes with no error."""

    OLD_FORM = re.compile(r"^line \d+: [a-z0-9-]+/\d+: \*(?:Set by|Correction)\* is not a field "
                          r"of the form; ")

    def test_the_way_facts_hold_no_error_but_the_old_form(self):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            record = os.path.join(directory, "environment-facts.jsonl")
            code = format_guard.run(format_guard.OWN_FILE, stream=output, record=record)
            with open(record, encoding="utf-8") as handle:
                lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertIn(code, (0, 1), output.getvalue())
        self.assertEqual(sorted({item["invariant"] for item in lines if item["invariant"]}), PLAIN)
        failures = [item for item in lines if item["verdict"] == "fail"]
        self.assertEqual([item for item in failures
                          if not self.OLD_FORM.search(item["description"])], [])
        self.assertEqual(code == 1, bool(failures))


if __name__ == "__main__":
    unittest.main()
