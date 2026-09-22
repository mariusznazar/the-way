"""Tests of the invariants guard: every check fires on a file broken on purpose.

Run from anywhere: python -B -m unittest discover -s <the-way>/elements/invariants -p "test_*.py"

Inputs and expected fingerprints are written out, never computed by the code under test (WAY-70).
"""

import io
import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402

DECISION = "A saved game is written to the player's own storage only."
DECISION_FINGERPRINT = "4dd7fb86"
SENTENCE = "A game saved and loaded back holds the same state as before it was saved."
SENTENCE_FINGERPRINT = "885f5dbb"
REWORDED = "A game saved and loaded back holds the same state as when it was saved."
REWORDED_FINGERPRINT = "f2ad38fc"
OTHER = "A saved game loads in any later version of the product."

LOG = "\n".join(["# Decision log", "", "### WAY-01/1 — Where does a saved game go?", "", DECISION,
                 "", "- **Change:** new decision", ""])

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
          recovered="none", omit=()):
    lines = ["## %s/%d" % (identifier, version), "", sentence, ""]
    fields = [("Method", method), ("Rests on", rests), ("Derives from", derives), ("Part", part),
              ("Correction", correction), ("Recovered", recovered)]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def later():
    return entry("loads-in-later-versions", sentence=OTHER, derives="none", part="loading")


WITHDRAWN = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Successors |", "|---|---|",
                       "| save-format | save-round-trip |"])
QUARANTINE = "\n".join(["## Quarantined invariants", "", "| Identifier | Version | Until |",
                        "|---|---|---|"])


def invariants(*entries, withdrawn=WITHDRAWN, quarantine=QUARANTINE):
    sections = list(entries) or [entry(), later()]
    return "# Invariants\n\n" + "\n\n".join(sections + [s for s in (withdrawn, quarantine) if s]) + "\n"


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


class GuardTestCase(unittest.TestCase):
    files = FILES

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = self.directory.name
        self.path = os.path.join(self.root, "foundations", "invariants.md")
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

    def guard(self, text, base=None, violated_text=None):
        self.write("foundations/invariants.md", text)
        if violated_text is not None:
            self.write("foundations/violated_invariants.md", violated_text)
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(self.path, base=base, stream=output)
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


class ValidFile(GuardTestCase):
    def test_valid_file_passes(self):
        self.assertPasses(invariants())

    def test_without_base_the_checks_against_the_branch_point_are_unchecked(self):
        output = self.assertPasses(invariants())
        self.assertIn("unchecked: identifiers, versions and corrections against the commit", output)
        self.assertIn("unchecked: the list of violated invariants against that commit", output)

    def test_method_as_the_path_of_a_file_a_human_assesses_against(self):
        self.assertPasses(invariants(entry(method="docs/review_checklist.md"), later()))

    def test_todo_where_the_form_gives_it(self):
        self.assertPasses(invariants(entry(method="`TODO`", rests="TODO — the store keeps 5 MB, "
                                           "per its documentation", derives="`TODO — a decision on "
                                           "saves, expected with the first task`"), later()))

    def test_every_as_the_part(self):
        self.assertPasses(invariants(entry(part="every"), later()))

    def test_recovered_entry(self):
        self.assertPasses(invariants(entry(derives="none", recovered="recovered — searched: the "
                                           "decision log, git history; found: nothing"), later()))


class Layout(GuardTestCase):
    def test_file_elsewhere_than_foundations_invariants(self):
        self.write("foundations/other.md", invariants())
        output = io.StringIO()
        code = format_guard.run(os.path.join(self.root, "foundations", "other.md"), stream=output)
        self.assertEqual(code, 1, output.getvalue())
        self.assertIn("stand in foundations/invariants.md", output.getvalue())

    def test_heading_that_is_neither_an_entry_nor_a_list(self):
        self.assertFails(invariants(entry(), later(), "## Notes\n\nSome notes."),
                         "heading `## Notes` is neither")

    def test_missing_list(self):
        self.assertFails(invariants(quarantine=None), "the file has no list `Quarantined invariants`")

    def test_lists_out_of_order(self):
        self.assertFails(invariants(withdrawn=QUARANTINE, quarantine=WITHDRAWN),
                         "not in the order")

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

    def test_none_as_an_identifier(self):
        self.assertFails(invariants(entry("none"), later()), "`none` is not an identifier")

    def test_identifier_used_twice(self):
        self.assertFails(invariants(entry(), later(), entry(sentence=OTHER)),
                         "identifier `save-round-trip` is used twice")

    def test_identifier_of_a_withdrawn_one(self):
        self.assertFails(invariants(entry("save-format"), later()),
                         "identifier `save-format` is used twice")

    def test_identifier_held_by_a_part_of_the_map(self):
        self.assertFails(invariants(entry("saving"), later()), "`saving` is held by the part map")

    def test_identifier_withdrawn_in_the_map(self):
        self.assertFails(invariants(entry("game-state"), later()),
                         "`game-state` is held by the part map")

    def test_withdrawn_identifier_names_an_unknown_successor(self):
        self.assertFails(invariants(withdrawn=WITHDRAWN.replace("| save-round-trip |",
                                                                "| save-trip |")),
                         "names successor `save-trip`")

    def test_withdrawn_identifier_with_no_successor(self):
        self.assertPasses(invariants(withdrawn=WITHDRAWN.replace("| save-round-trip |", "| none |")))


class Fields(GuardTestCase):
    def test_missing_field(self):
        self.assertFails(invariants(entry(omit=("Recovered",)), later()),
                         "field *Recovered* is missing")

    def test_field_not_in_the_template(self):
        self.assertFails(invariants(entry() + "\n- **Owner:** the saving team", later()),
                         "field *Owner* is not in the template")

    def test_none_where_the_form_does_not_give_it(self):
        self.assertFails(invariants(entry(method="none"), later()), "*Method* may not hold `none`")

    def test_todo_where_the_form_does_not_give_it(self):
        self.assertFails(invariants(entry(part="TODO"), later()), "*Part* may not hold `TODO`")



class Sentence(GuardTestCase):
    def test_missing_sentence(self):
        broken = entry().replace(SENTENCE + "\n\n", "")
        self.assertFails(invariants(broken, later()), "the sentence is missing")

    def test_two_sentences(self):
        self.assertFails(invariants(entry(sentence=SENTENCE + " " + OTHER), later()),
                         "2 sentences, an entry states one")

    def test_main_branch_outside_quoted_text(self):
        self.assertFails(invariants(entry(sentence="On the main branch, a saved game loads."),
                                    later()), 'the sentence names "main branch"')

    def test_main_branches_outside_quoted_text(self):
        self.assertFails(invariants(entry(sentence="No saved game differs between main branches."),
                                    later()), 'the sentence names "main branch"')

    def test_second_paragraph_after_the_sentence(self):
        broken = entry().replace(SENTENCE + "\n", SENTENCE + "\n\n" + OTHER + "\n")
        self.assertFails(invariants(broken, later()), "text outside the sentence and the fields")

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
        self.assertFails(invariants(entry(sentence="No saved game changes since {base}."), later()),
                         "`{base}` is not a value the gate fills in")

    def test_value_its_command_does_not_take(self):
        self.assertFails(invariants(entry(sentence="No saved game changes since {fork-point}."),
                                    later()), "names `{fork-point}`, which its command does not take")

    def test_value_its_command_takes(self):
        self.assertPasses(invariants(entry(sentence="No saved game changes since {fork-point}.",
                                           method="`python tests/compare.py {fork-point}`"), later()))


class Method(GuardTestCase):
    def test_command_that_is_a_path_alone(self):
        self.assertFails(invariants(entry(method="`tests/test_saving.py`"), later()),
                         "a command begins with the name of the program it runs")

    def test_command_taking_a_value_the_gate_does_not_fill_in(self):
        self.assertFails(invariants(entry(method="`python tests/compare.py {base}`"), later()),
                         "the command takes `{base}`")

    def test_path_of_no_file(self):
        self.assertFails(invariants(entry(method="docs/missing.md"), later()),
                         "*Method* names `docs/missing.md`, which is not a file")

    def test_method_in_prose(self):
        self.assertFails(invariants(entry(method="a reviewer reads the save code"), later()),
                         "*Method* is neither a command in backticks")


class Links(GuardTestCase):
    def test_stale_fingerprint_of_a_decision(self):
        self.assertFails(invariants(entry(derives="WAY-01@00000000"), later()),
                         "`WAY-01@00000000` — the current fingerprint of WAY-01 is 4dd7fb86")

    def test_decision_that_does_not_exist(self):
        self.assertFails(invariants(entry(derives="WAY-07@" + DECISION_FINGERPRINT), later()),
                         "names a decision that does not exist or binds nothing any more")

    def test_decision_repealed_since(self):
        self.write("foundations/decisions.md", LOG + "\n".join([
            "", "### WAY-01/2 — Where does a saved game go?", "",
            "- **Change:** repeal · previous: WAY-01/1", ""]))
        self.assertFails(invariants(), "`WAY-01@4dd7fb86` names a decision that does not exist or "
                                       "binds nothing any more")

    def test_decision_without_a_fingerprint(self):
        self.assertFails(invariants(entry(derives="WAY-01"), later()), "`WAY-01` is not `WAY-NN@")

    def test_named_fact_while_facts_have_no_entries(self):
        self.assertFails(invariants(entry(rests="storage-quota@1234abcd"), later()),
                         "the environment facts element has no entries")


class Part(GuardTestCase):
    def test_every_and_parts_at_once(self):
        self.assertFails(invariants(entry(part="every · saving"), later()),
                         "names `every` and parts at once")

    def test_part_not_in_the_map(self):
        self.assertFails(invariants(entry(part="saving · cloud"), later()),
                         "names `cloud`, which is not a part of the part map")

    def test_flow_is_not_a_part(self):
        self.assertFails(invariants(entry(part="save-and-load"), later()),
                         "names `save-and-load`, which is not a part")


class CorrectionAndRecovered(GuardTestCase):
    def test_correction_of_another_form(self):
        self.assertFails(invariants(entry(correction="the wording was fixed"), later()),
                         "*Correction* is neither `none` nor")

    def test_correction_naming_another_current_fingerprint(self):
        self.assertFails(invariants(entry(correction="%s → %s" % (REWORDED_FINGERPRINT,
                                                                  REWORDED_FINGERPRINT)), later()),
                         "*Correction* names %s as the current fingerprint, but it is %s"
                         % (REWORDED_FINGERPRINT, SENTENCE_FINGERPRINT))

    def test_recovered_of_another_form(self):
        self.assertFails(invariants(entry(derives="none", recovered="recovered from the code"),
                                    later()), "*Recovered* is neither `none` nor")

    def test_recovered_while_it_derives_from_a_decision(self):
        self.assertFails(invariants(entry(recovered="recovered — searched: the log; found: "
                                                    "nothing"), later()),
                         "*Recovered* is not `none`, while *Derives from* names a decision")


class Lists(GuardTestCase):
    def quarantine(self, row):
        return QUARANTINE + "\n| %s |" % row

    def test_quarantine_position(self):
        self.assertPasses(invariants(quarantine=self.quarantine("save-round-trip | 1 | 2026-12-31")))

    def test_quarantine_of_no_entry(self):
        self.assertFails(invariants(quarantine=self.quarantine("save-trip | 1 | 2026-12-31")),
                         "quarantine names `save-trip`, which is not an entry")

    def test_quarantine_at_another_version(self):
        self.assertFails(invariants(quarantine=self.quarantine("save-round-trip | 2 | 2026-12-31")),
                         "its current version is 1")

    def test_quarantine_without_a_date(self):
        self.assertFails(invariants(quarantine=self.quarantine("save-round-trip | 1 | soon")),
                         "which is not a date YYYY-MM-DD")

    def test_quarantine_of_an_invariant_a_critical_flow_names(self):
        self.assertFails(invariants(quarantine=self.quarantine("loads-in-later-versions | 1 | "
                                                               "2026-12-31")),
                         "which a critical flow names")

    def test_flow_naming_its_invariant_in_prose(self):
        self.write("foundations/part_map.md", MAP.replace(
            "loads-in-later-versions — test:", "every saved game loads in a later version — test:"))
        output = self.assertPasses(invariants())
        self.assertIn("unchecked: whether a quarantine names the invariant of `save-and-load` — the "
                      "flow names its invariant in prose, not by identifier", output)

    def test_violated_list_with_other_columns(self):
        self.assertFails(invariants(), "the list has columns Id | Ver, not Identifier | Version",
                         violated_text="## Violated invariants\n\n| Id | Ver |\n|---|---|\n")

    def test_violated_position(self):
        self.assertPasses(invariants(), violated_text=violated(("save-round-trip", "1")))

    def test_violated_position_of_no_entry(self):
        self.assertFails(invariants(), "`save-trip` is not an entry",
                         violated_text=violated(("save-trip", "1")))

    def test_violated_position_at_another_version(self):
        self.assertFails(invariants(), "`save-round-trip` at version 2; its current version is 1",
                         violated_text=violated(("save-round-trip", "2")))


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

    def test_citation_of_another_version(self):
        self.cite("// invariant: save-round-trip/2")
        self.assertFails(invariants(), "cites `save-round-trip/2`, whose current version is 1")

    def test_citation_of_no_entry(self):
        self.cite("# invariant: save-trip/1")
        self.assertFails(invariants(), "cites `save-trip`, which is not an entry")

    def test_citation_of_a_withdrawn_identifier(self):
        self.cite("# invariant: save-format/1")
        self.assertFails(invariants(), "cites `save-format`, which is withdrawn (successors: "
                                       "save-round-trip)")

    def test_data_line_naming_no_file(self):
        self.cite("# invariant: save-round-trip/1", "# data: tests/missing.json")
        self.assertFails(invariants(), "`data: tests/missing.json` names no file")


class AgainstTheBranchPoint(GuardTestCase):
    def test_unchanged_file_passes(self):
        self.commit(invariants())
        output = self.assertPasses(invariants(), base="HEAD")
        self.assertNotIn("unchecked: identifiers", output)

    def test_base_that_does_not_exist(self):
        self.commit(invariants())
        self.assertFails(invariants(), "--base nowhere does not exist", base="nowhere")

    def test_new_entry_above_version_1(self):
        self.commit(invariants(entry(), withdrawn=WITHDRAWN))
        self.assertFails(invariants(entry(), entry("loads-in-later-versions", 2, sentence=OTHER,
                                                   derives="none", part="loading")),
                         "loads-in-later-versions/2: a new entry carries version 1", base="HEAD")

    def test_identifier_dropped(self):
        self.commit(invariants())
        self.assertFails(invariants(entry()), "`loads-in-later-versions` stands in the file on HEAD "
                                              "and is gone", base="HEAD")

    def test_identifier_withdrawn_there_is_an_entry_again(self):
        self.commit(invariants())
        text = invariants(entry(), later(), entry("save-format", sentence="A save file names its "
                                                  "format version."),
                          withdrawn=WITHDRAWN.replace("| save-format | save-round-trip |",
                                                      "| save-slot | none |"))
        self.assertFails(text, "`save-format` is withdrawn on HEAD and stands as an entry again",
                         base="HEAD")

    def test_changed_sentence_at_the_same_version(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(sentence=REWORDED), later()),
                         "the sentence changed since HEAD (%s → %s); the version is 2"
                         % (SENTENCE_FINGERPRINT, REWORDED_FINGERPRINT), base="HEAD")

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

    def test_raised_version_declaring_a_correction(self):
        self.commit(invariants())
        self.write("tests/test_saving.py", "# invariant: save-round-trip/2\n")
        correction = "%s → %s" % (SENTENCE_FINGERPRINT, REWORDED_FINGERPRINT)
        self.assertFails(invariants(entry(version=2, sentence=REWORDED, correction=correction),
                                    later()), "a raised version declares no correction", base="HEAD")

    def test_unchanged_sentence_at_a_raised_version(self):
        self.commit(invariants())
        self.assertFails(invariants(entry(version=2), later()),
                         "the sentence is unchanged since HEAD, where the version is 1", base="HEAD")

    def test_change_outside_the_sentence_keeps_the_version(self):
        self.commit(invariants())
        self.assertPasses(invariants(entry(part="every"), later()), base="HEAD")

    def test_old_wording_kept_beside_the_new(self):
        self.commit(invariants())
        kept = entry(version=2, sentence=REWORDED) + "\n\nEarlier: " + SENTENCE
        self.assertFails(invariants(kept, later()), "still holds its wording from HEAD",
                         base="HEAD")

    def test_violated_list_grows(self):
        self.commit(invariants(), violated_text=violated())
        self.assertFails(invariants(), "`save-round-trip` at version 1 is not on the list on HEAD",
                         base="HEAD", violated_text=violated(("save-round-trip", "1")))

    def test_violated_list_shrinks(self):
        self.commit(invariants(), violated_text=violated(("save-round-trip", "1")))
        self.assertPasses(invariants(), base="HEAD", violated_text=violated())


class Unreadable(GuardTestCase):
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


if __name__ == "__main__":
    unittest.main()
