"""Tests of the part map guard: every check fires on a map broken on purpose.

Inputs and expected values are written out, never computed by the guard (WAY-69).

Run from the root of the-way:
    python -B gate/run_tests.py elements/part-map --record .runs/part-map-tests.jsonl
"""

import contextlib
import inspect
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import unittest.mock

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402

GUARD = "elements/part-map/format_guard.py"
NOT_PRODUCED = "the method's command or file is not declared or produced by the product"
NO_COMMIT = "the method takes a commit the gate filled in as not existing"


def heading(identifier, title=None):
    """The heading of an entry: `## <identifier>`, or `## <identifier> — <title>`, which the form
    does not use, where a title is given."""
    return "## %s" % identifier if title is None else "## %s — %s" % (identifier, title)


def part(identifier="saving", title=None, responsibility=None,
         files=("src/saving.py", "tests/**"),
         depends="none", failure_modes=("a save is lost — the player loses the game — high — "
                                        "detected by INV-2",),
         boundary="none", omit=()):
    if responsibility is None:
        responsibility = "The part answers for writing and reading a saved game."
    lines = [heading(identifier, title), "", responsibility, ""]
    if not isinstance(files, str):
        files = "\n  ".join(files)
    fields = [("Files", files), ("Depends on", depends),
              ("Failure modes", "\n" + "\n".join("  - %s" % mode for mode in failure_modes)),
              ("Trust boundary", boundary)]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def flow(identifier="save-and-load", title=None, description=None, criticality="high",
         parts="saving", invariant="INV-2", coverage="none", omit=()):
    if description is None:
        description = "The player saves a game and loads it back after a restart."
    lines = [heading(identifier, title), "", description, ""]
    fields = [("Criticality", criticality), ("Parts", parts), ("Invariant", invariant),
              ("Coverage", coverage)]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def surface(identifier="save-format", title=None, promise=None,
            declared="src/saving.py · SaveFile", omit=()):
    if promise is None:
        promise = "The product reads back every saved game written by an earlier version."
    lines = [heading(identifier, title), "", promise, ""]
    lines += [("- **Declared at:** %s" % declared)] if "Declared at" not in omit else []
    return "\n".join(lines)


def foundations_part(files="foundations/**", title=None):
    return part("foundations", title, files=files,
                responsibility="The part answers for what binds the product.",
                failure_modes=("a rule read wrong — work goes the light path — low — "
                               "not detected",))


SCALE = "\n".join(["## Criticality scale", "", "1. low — the player retries a step",
                   "2. high — the player loses the game"])

CONTEXT = "\n".join(["## External context", "",
                     "| Partner | Direction | What comes in | Updates with the product |",
                     "|---|---|---|---|",
                     "| the player's browser | both | untrusted | no |"])

PATHS = "\n".join(["## Change paths", "",
                   "| Promise level | What a change at this level may do | "
                   "What it owes the consumer first |", "|---|---|---|",
                   "| stable | add a field, never remove one | a year and an announcement |"])

LEFT_OUT = "\n".join(["## Files left out on purpose", "", "| File | Why |", "|---|---|",
                      "| README.md | the entry point of the repository |"])

WITHDRAWN = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Why | Successors |",
                       "|---|---|---|", "| game-state | merged into saving | saving |"])


def part_map(*entries, **lists):
    sections = list(entries) or [part(), flow(), surface(), foundations_part()]
    tail = [lists.get("scale", SCALE), lists.get("context", CONTEXT), lists.get("paths", PATHS),
            lists.get("left_out", LEFT_OUT), lists.get("withdrawn", WITHDRAWN)]
    return "# Part map\n\nWhat the product is made of.\n\n" + \
        "\n\n".join(sections + [section for section in tail if section]) + "\n"


def line(function, verdict, invariant, description=None, reason=None):
    """A line of the record, written out as the test expects it."""
    written = {"check": "%s::%s" % (GUARD, function) if function else GUARD,
               "verdict": verdict, "invariant": invariant}
    if reason is not None:
        written["reason"] = reason
    if description is not None:
        written["description"] = description
    return written


# The whole report for a person of a clean map whose product declares no command the guard asks
# for: what it could not check, and no line of agreement (WAY-38).
REPORT_WITHOUT_COMMANDS = "\n".join([
    "unchecked: the list of parts of `save-and-load` — its test leaves no coverage file",
    "unchecked: the change path of every promise level in use — the levels sit at the "
    "declarations, and no command of the product reports them",
    "unchecked: the dependencies between parts, and new or stale violations — no command of the "
    "product reports the dependency graph",
    "note: there is no invariants.md beside the map: the invariants the map names are not checked",
    "note: there is no decisions.md beside the map: the scopes of decisions are not checked",
    "note: no --base given: the list of known violations is not compared with the main branch; "
    "that check is not run, and is not counted in the last line",
    "note: no --base given: the computed criticality of the parts is not compared with the main "
    "branch, so no lowering is reported; that check is not run, and is not counted in the last "
    "line",
    "0 error(s), 0 warning(s), 3 unchecked", ""])


FILES = {"src/saving.py": "class SaveFile:\n    pass\n\n\ndef save():\n    pass\n",
         "tests/test_saving.py": "# flow: save-and-load\ndef test_save():\n    pass\n",
         "README.md": "# Product\n"}


class GuardTestCase(unittest.TestCase):
    files = FILES

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.outside = tempfile.TemporaryDirectory()
        self.root = self.directory.name
        self.path = os.path.join(self.root, "foundations", "part_map.md")
        self.record_path = os.path.join(self.outside.name, ".runs", "part-map.jsonl")
        self.lines = []
        os.makedirs(os.path.join(self.root, "foundations"))
        for name, content in self.files.items():
            self.write(name, content)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "guard@example.com")
        self.git("config", "user.name", "Guard")

    def tearDown(self):
        self.directory.cleanup()
        self.outside.cleanup()

    def git(self, *arguments):
        subprocess.run(["git"] + list(arguments), cwd=self.root, check=True, capture_output=True)

    def write(self, relative, text):
        full = os.path.join(self.root, *relative.split("/"))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)

    def guard(self, text, base=None, own=False, path=None, examples=None):
        path = path or self.path
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        if os.path.exists(os.path.join(self.root, ".git")):
            self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(path, base=base, stream=output,
                                record=self.record_path, own=own,
                                examples=examples or os.path.join(self.root, "no-examples.md"))
        with open(self.record_path, encoding="utf-8") as handle:
            self.lines = [json.loads(item) for item in handle.read().split("\n") if item]
        return code, output.getvalue()

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "map")

    def assertPasses(self, text, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 0, output)
        self.assertIn("0 error(s), 0 warning(s)", output)
        self.assertEqual([item for item in self.lines if item["verdict"] == "fail"], [])

    def assertFails(self, text, fragment, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 1, output)
        self.assertIn(fragment, output)

    def assertRecords(self, expected):
        self.assertIn(expected, self.lines)

    def failures(self, invariant):
        return [item["description"] for item in self.lines
                if item["verdict"] == "fail" and item["invariant"] == invariant]


class ValidMap(GuardTestCase):
    def test_valid_map_passes(self):
        self.assertPasses(part_map())


class Entries(GuardTestCase):
    def test_entry_of_no_known_kind(self):
        strange = "\n".join(["## ghost", "", "The part answers for nothing.", "",
                             "- **Notes:** nothing"])
        self.assertFails(part_map(part(), strange), "is neither a part, a critical flow nor a "
                                                    "surface")
        self.assertEqual(self.failures("map-entry-kinds/1"),
                         ["line 16: `ghost` is neither a part, a critical flow nor a surface: no "
                          "field of the template names its kind"])

    def test_two_entries_with_one_identifier(self):
        self.assertFails(part_map(part(), part(files="tests/**")),
                         "identifier `saving` is used twice")
        self.assertRecords(line("check_identifiers", "fail", None,
                                "line 16: identifier `saving` is used twice, here and at line 5"))

    def test_identifier_with_capitals(self):
        self.assertFails(part_map(part(identifier="Saving")), "`Saving` is not an identifier of "
                                                              "words in lower case")
        self.assertEqual(self.failures("map-identifier-form/1"),
                         ["line 5: `Saving` is not an identifier of words in lower case joined "
                          "by hyphens"])

    def test_missing_field(self):
        self.assertFails(part_map(part(omit=("Trust boundary",))),
                         "field *Trust boundary* is missing")
        self.assertEqual(self.failures("map-entry-field-presence/1"),
                         ["line 5: saving: field *Trust boundary* is missing"])

    def test_missing_binding_sentence(self):
        self.assertFails(part_map(part(responsibility="")), "binding sentence is missing")

    def test_entry_reuses_a_withdrawn_identifier(self):
        self.assertFails(part_map(part(identifier="game-state")),
                         "`game-state` is withdrawn")

    def test_flow_names_a_part_that_does_not_exist(self):
        self.assertFails(part_map(part(), flow(parts="saving · rendering")),
                         "*Parts* names `rendering`, which is not in the map")
        self.assertEqual(self.failures("flow-part-names/1"),
                         ["line 21: save-and-load: *Parts* names `rendering`, which is not in the "
                          "map as a part"])

    def test_flow_names_a_withdrawn_part(self):
        self.guard(part_map(part(), flow(parts="saving · game-state")))
        self.assertEqual(self.failures("flow-part-names/1"),
                         ["line 21: save-and-load: *Parts* names `game-state`, which is withdrawn"])

    def test_dependency_on_a_part_that_does_not_exist(self):
        self.assertFails(part_map(part(depends="rendering")),
                         "*Depends on* names `rendering`, which is not in the map")
        self.assertRecords(line("check_references", "fail", "flow-part-names/1",
                                "line 11: saving: *Depends on* names `rendering`, which is not in "
                                "the map as a part"))

    def test_dependency_on_a_withdrawn_part(self):
        self.guard(part_map(part(depends="game-state"), flow(), surface(), foundations_part()))
        self.assertEqual(self.failures("flow-part-names/1"),
                         ["line 11: saving: *Depends on* names `game-state`, which is withdrawn"])


class Headings(GuardTestCase):
    """An entry's heading is its identifier alone, `## <identifier>` (WAY-41). A heading with a
    title, `## <identifier> — <title>`, is reported, and its identifier is still read, so that
    every other check runs on the entry."""

    TITLE = ("line 5: `saving` carries a title after its identifier; an entry's heading is "
             "`## <identifier>`")

    def test_a_heading_of_the_identifier_alone_passes(self):
        text = part_map()
        self.assertIn("\n## saving\n", text)
        self.assertPasses(text)
        self.assertRecords(line("check_identifiers", "pass", "map-identifier-form/1"))

    def test_a_heading_with_a_title(self):
        self.assertFails(part_map(part(title="Saving a game"), flow(), surface(),
                                  foundations_part()),
                         "`saving` carries a title after its identifier")
        self.assertEqual([item for item in self.lines if item["verdict"] == "fail"],
                         [line("check_identifiers", "fail", None, self.TITLE)])

    def test_every_other_check_reads_the_identifier_of_a_heading_with_a_title(self):
        self.write("foundations/decisions.md",
                   "### WAY-01/1 — Q?\n\nS.\n\n- **Scope:** saving, foundations\n")
        code, output = self.guard(part_map(part(title="Saving a game"),
                                           flow(title="Save and load"),
                                           surface(title="The format of a saved game"),
                                           foundations_part(title="The foundation")))
        self.assertEqual(code, 1, output)
        self.assertEqual([item["description"] for item in self.lines
                          if item["verdict"] == "fail"],
                         [self.TITLE,
                          "line 16: `save-and-load` carries a title after its identifier; an "
                          "entry's heading is `## <identifier>`",
                          "line 25: `save-format` carries a title after its identifier; an "
                          "entry's heading is `## <identifier>`",
                          "line 31: `foundations` carries a title after its identifier; an "
                          "entry's heading is `## <identifier>`"])
        self.assertRecords(line("check_references", "pass", "flow-part-names/1"))
        self.assertRecords(line("check_flows", "pass", "flow-invariant-link/1"))
        self.assertRecords(line("check_scopes", "pass", "decision-scope-names/1"))

    def test_a_section_with_no_field_under_a_word_is_no_entry(self):
        self.guard(part_map(part(), flow(), surface(), foundations_part(),
                            "## Notes\n\nSomething to remember."))
        self.assertEqual(len(self.failures("map-section-kinds/1")), 1, self.lines)
        self.assertEqual(self.failures("map-entry-kinds/1"), [])


class Sections(GuardTestCase):
    """The map holds its entries and the five lists its template names for it (WAY-40)."""

    def test_a_section_of_no_known_kind(self):
        notes = "## Notes\n\nSomething to remember."
        self.assertFails(part_map(part(), flow(), surface(), foundations_part(), notes),
                         "section `## Notes` is neither an entry nor one of the lists")
        self.assertEqual(self.failures("map-section-kinds/1"),
                         ["line 41: section `## Notes` is neither an entry nor one of the lists "
                          "the template names for the map (Criticality scale, External context, "
                          "Change paths, Files left out on purpose, Withdrawn identifiers)"])

    def test_the_list_of_known_violations_stands_in_its_own_file(self):
        listed = "\n".join(["## Known violations", "",
                            "| Source | Target | File | What it reaches for |", "|---|---|---|---|"])
        self.guard(part_map(part(), flow(), surface(), foundations_part(), listed))
        self.assertEqual(len(self.failures("map-section-kinds/1")), 1, self.lines)

    def test_the_lists_of_the_template_pass(self):
        self.guard(part_map())
        self.assertRecords(line("check_sections", "pass", "map-section-kinds/1"))


class Versions(GuardTestCase):
    def test_an_identifier_with_a_version(self):
        self.guard(part_map(part(identifier="saving/2"), flow(parts="none"), surface(),
                            foundations_part()))
        self.assertEqual(self.failures("map-entry-version/1"),
                         ["line 5: `saving/2` carries a version; an entry of the map is edited "
                          "in place"])

    def test_a_version_field(self):
        self.guard(part_map(part() + "\n- **Version:** 2", flow(), surface(), foundations_part()))
        self.assertEqual(self.failures("map-entry-version/1"),
                         ["line 15: saving: *Version* is written; an entry of the map carries no "
                          "version"])

    def test_no_version_passes(self):
        self.guard(part_map())
        self.assertRecords(line("check_identifiers", "pass", "map-entry-version/1"))


class FieldWords(GuardTestCase):
    """`none` stands only where the form of an entry's kind gives it, and `TODO` nowhere, since the
    template gives it to no field (WAY-71)."""

    def test_the_words_the_template_gives(self):
        """Pins what the guard reads off the forms: a word added to a field's form would otherwise
        change what the guard accepts silently."""
        self.assertEqual(format_guard.read_rules().words, {
            "part": {"Files": ["none"], "Depends on": ["none"], "Failure modes": ["none"],
                     "Trust boundary": ["none"]},
            "critical flow": {"Criticality": [], "Parts": [], "Invariant": [],
                              "Coverage": ["none"]},
            "surface": {"Declared at": []}})

    def test_the_rules_stand_without_a_list_of_checks(self):
        """The template holds no list of the guard's checks: each check cites its invariant, and
        the guard reads its rules from the forms and the lists alone."""
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            text = handle.read()
        self.assertNotIn("## What the format guard checks", text)
        self.assertNotIn("(generated)", format_guard._code_block(text, "Part"))
        self.assertNotIn("test:", format_guard._code_block(text, "Critical flow"))
        for title in ("Part", "Critical flow", "Surface"):
            self.assertIn("## <identifier>\n", format_guard._code_block(text, title))

    def test_none_where_the_form_gives_it_passes(self):
        self.assertPasses(part_map(part(), flow(coverage="none"), surface(),
                                   part("foundations", files="foundations/**",
                                        responsibility="The part answers for what binds.",
                                        failure_modes=("none",)),
                                   part("idle", files="none",
                                        responsibility="The part answers for nothing yet.",
                                        failure_modes=("none",))))

    def test_none_where_the_form_does_not_give_it(self):
        self.guard(part_map(part(), flow(parts="none"), surface(declared="none"),
                            foundations_part()))
        self.assertEqual(self.failures("map-entry-field-words/1"), [
            "line 21: save-and-load: *Parts* is `none`, which its form does not give it",
            "line 29: save-format: *Declared at* is `none`, which its form does not give it"])

    def test_todo_in_depends_on_is_todo_not_an_empty_list(self):
        code, output = self.guard(part_map(part(depends="TODO"), flow(), surface(),
                                           foundations_part()))
        self.assertEqual(code, 1, output)
        self.assertIn("part_map.md:11: error: saving: *Depends on* holds `TODO`, which its form "
                      "does not give it", output)
        self.assertEqual(self.failures("map-entry-field-words/1"),
                         ["line 11: saving: *Depends on* holds `TODO`, which its form does not "
                          "give it"])

    def test_todo_in_each_kind_of_field(self):
        cases = [
            ("an item among others", part(depends="foundations · TODO — the storage part"),
             "line 11: saving: *Depends on* holds `TODO`, which its form does not give it"),
            ("a line of a list", part(files=("src/saving.py", "tests/**", "TODO")),
             "line 9: saving: *Files* holds `TODO`, which its form does not give it"),
            ("a piece of a failure mode", part(failure_modes=("a save is lost — the player loses "
                                                              "the game — TODO — not detected",)),
             "line 12: saving: *Failure modes* holds `TODO`, which its form does not give it"),
            ("backticks", part(boundary="`TODO`"),
             "line 14: saving: *Trust boundary* holds `TODO`, which its form does not give it"),
        ]
        for what, entry, description in cases:
            with self.subTest(what):
                self.guard(part_map(entry, flow(), surface(), foundations_part()))
                self.assertEqual(self.failures("map-entry-field-words/1"), [description])

    def test_todo_in_a_table_is_a_failure(self):
        context = "\n".join(["## External context", "",
                             "| Partner | Direction | What comes in | Updates with the product |",
                             "|---|---|---|---|", "| the player's browser | TODO | untrusted | no |"])
        self.assertFails(part_map(context=context), "the list `External context` holds `TODO`")
        self.assertEqual(self.failures("external-exchange-row/1"),
                         ["line 50: the list `External context` holds `TODO`"])

    def test_todo_in_a_list_of_no_invariant_is_a_failure_for_no_entry(self):
        left_out = "\n".join(["## Files left out on purpose", "", "| File | Why |", "|---|---|",
                              "| README.md | TODO |"])
        self.assertFails(part_map(left_out=left_out),
                         "the list `Files left out on purpose` holds `TODO`")
        self.assertRecords(line("check_lists", "fail", None,
                                "line 62: the list `Files left out on purpose` holds `TODO`"))

    def test_todo_in_the_criticality_scale_is_no_degree(self):
        scale = "\n".join(["## Criticality scale", "", "1. low — the player retries a step",
                           "2. high — the player loses the game", "3. TODO — a third degree"])
        self.assertFails(part_map(scale=scale), "the list `Criticality scale` holds `TODO`")


class TodoInEveryField(GuardTestCase):
    """`TODO` in any field of any entry is an error on every run, since the template gives it to no
    field (WAY-71): map-entry-field-words fails, with or without --base."""

    MESSAGE = "holds `TODO`, which its form does not give it"

    def setUp(self):
        super().setUp()
        self.write("other.txt", "x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")
        self.files_in_map = ("src/saving.py", "tests/**", "other.txt")

    def cases(self):
        """(what the case holds, the map, the line of the field, the entry, the field)."""
        files = self.files_in_map
        return [
            ("files", part_map(part(files=files + ("TODO",)), flow(), surface(),
                               foundations_part()), 9, "saving", "Files"),
            ("depends on", part_map(part(files=files, depends="TODO"), flow(), surface(),
                                    foundations_part()), 12, "saving", "Depends on"),
            ("failure modes", part_map(part(files=files, failure_modes=("TODO — ask Anna",)),
                                       flow(), surface(), foundations_part()),
             13, "saving", "Failure modes"),
            ("trust boundary", part_map(part(files=files, boundary="TODO"), flow(), surface(),
                                        foundations_part()), 15, "saving", "Trust boundary"),
            ("criticality", part_map(part(files=files), flow(criticality="TODO"), surface(),
                                     foundations_part()), 21, "save-and-load", "Criticality"),
            ("parts", part_map(part(files=files), flow(parts="saving · TODO"), surface(),
                               foundations_part()), 22, "save-and-load", "Parts"),
            ("invariant", part_map(part(files=files), flow(invariant="TODO"),
                                   surface(), foundations_part()), 23, "save-and-load",
             "Invariant"),
            ("coverage", part_map(part(files=files), flow(coverage="TODO"), surface(),
                                  foundations_part()), 24, "save-and-load", "Coverage"),
            ("declared at", part_map(part(files=files), flow(), surface(declared="TODO"),
                                     foundations_part()), 30, "save-format", "Declared at"),
        ]

    def test_todo_in_each_kind_of_field_fails_on_a_plain_run(self):
        for what, text, number, identifier, name in self.cases():
            with self.subTest(what):
                code, output = self.guard(text)
                self.assertEqual(code, 1, output)
                self.assertIn("part_map.md:%d: error: %s: *%s* %s"
                              % (number, identifier, name, self.MESSAGE), output)
                self.assertRecords(line("check_fields", "fail", "map-entry-field-words/1",
                                        "line %d: %s: *%s* %s"
                                        % (number, identifier, name, self.MESSAGE)))
                self.assertEqual(len(self.failures("map-entry-field-words/1")), 1, self.lines)

    def test_todo_fails_the_run_given_a_base_as_well(self):
        text = self.cases()[1][1]
        code, output = self.guard(text, base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("part_map.md:12: error: saving: *Depends on* %s" % self.MESSAGE, output)

    def test_the_command_line_takes_no_merge_onto(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                format_guard.main([self.path, "--merge-onto", "none"])


class Files(GuardTestCase):
    files = dict(FILES, **{"src/render.py": "def draw():\n    pass\n"})

    def rendering(self, files="src/render.py"):
        return part("rendering", files=files,
                    responsibility="The part answers for drawing the board.",
                    failure_modes=("nothing is drawn — the player is stuck — high — "
                                   "not detected",))

    def test_file_no_pattern_claims(self):
        self.assertFails(part_map(), "no part claims `src/render.py`")
        self.assertEqual(self.failures("file-part-assignment/1"),
                         ["no part claims `src/render.py`: give it to a part or put it on the "
                          "list of files left out on purpose"])

    def test_file_claimed_by_two_parts(self):
        self.assertFails(part_map(part(), flow(), surface(), self.rendering("src/**"),
                                  foundations_part()),
                         "`src/saving.py` is claimed by `saving` and `rendering`")
        self.assertEqual(self.failures("file-part-assignment/1"),
                         ["line 31: `src/saving.py` is claimed by `saving` and `rendering`"])

    def test_pattern_that_matches_nothing(self):
        self.assertFails(part_map(part(files=("src/saving.py", "tests/**", "src/audio/**")),
                                  self.rendering(), foundations_part()),
                         "pattern `src/audio/**` of `saving` matches no file git tracks")
        self.assertEqual(self.failures("path-pattern-reach/1"),
                         ["line 9: pattern `src/audio/**` of `saving` matches no file git tracks"])

    def test_left_out_file_that_a_part_also_claims(self):
        left_out = "\n".join(["## Files left out on purpose", "", "| File | Why |", "|---|---|",
                              "| README.md | the entry point of the repository |",
                              "| src/render.py | drawn by hand |"])
        self.assertFails(part_map(part(), flow(), surface(), self.rendering(), foundations_part(),
                                  left_out=left_out),
                         "`src/render.py` is left out on purpose and claimed by `rendering`")
        self.assertEqual(self.failures("left-out-file-assignment/1"),
                         ["line 73: `src/render.py` is left out on purpose and claimed by "
                          "`rendering`"])
        self.assertEqual(self.failures("file-part-assignment/1"), [])

    def test_left_out_file_git_does_not_track_that_a_part_claims(self):
        left_out = "\n".join(["## Files left out on purpose", "", "| File | Why |", "|---|---|",
                              "| README.md | the entry point of the repository |",
                              "| src/cache.bin | written at run time |"])
        self.guard(part_map(part(), flow(), surface(), self.rendering("src/render.py\n  src/*.bin"),
                            foundations_part(), left_out=left_out))
        self.assertEqual(self.failures("left-out-file-assignment/1"),
                         ["line 74: `src/cache.bin` is left out on purpose and claimed by "
                          "`rendering`"])
        self.assertEqual(self.failures("path-pattern-reach/1"),
                         ["line 35: pattern `src/*.bin` of `rendering` matches no file git tracks"])

    def test_pattern_letter_case_counts_where_git_ignores_it(self):
        self.git("config", "core.ignorecase", "true")
        self.assertFails(part_map(part(), flow(), surface(), self.rendering("src/Render.py"),
                                  foundations_part()),
                         "pattern `src/Render.py` of `rendering` matches no file git tracks")
        self.assertEqual(self.failures("file-part-assignment/1"),
                         ["no part claims `src/render.py`: give it to a part or put it on the "
                          "list of files left out on purpose"])

    def test_a_generated_mark_is_not_part_of_the_form(self):
        """*Files* holds git path patterns alone (WAY-44); a pattern marked `(generated)` is
        reported, and the pattern is still matched."""
        self.guard(part_map(part(files=("src/saving.py (generated)", "tests/**")), flow(),
                            surface(), self.rendering(), foundations_part()))
        self.assertEqual([item for item in self.lines if item["verdict"] == "fail"],
                         [line("check_fields", "fail", None,
                               "line 9: saving: `(generated)` follows the pattern `src/saving.py`; "
                               "*Files* holds git path patterns alone")])
        self.assertRecords(line("check_files", "pass", "file-part-assignment/1"))

    def test_trust_boundary_pattern_that_matches_nothing(self):
        self.assertFails(part_map(part(boundary="src/parser.py"), self.rendering(),
                                  foundations_part()),
                         "trust boundary `src/parser.py` of `saving` matches no file git tracks")
        self.assertEqual(self.failures("path-pattern-reach/1"),
                         ["line 14: trust boundary `src/parser.py` of `saving` matches no file git "
                          "tracks"])


class MapFile(GuardTestCase):
    """The repository holds one part map, foundations/part_map.md (WAY-40)."""

    def test_the_map_where_the_template_puts_it_passes(self):
        self.guard(part_map())
        self.assertRecords(line("check_map_file", "pass", "part-map-file/1"))

    def test_a_map_elsewhere(self):
        os.makedirs(os.path.join(self.root, "docs"))
        self.guard(part_map(part(), flow(), surface(), foundations_part("foundations/**\n  docs/**")),
                   path=os.path.join(self.root, "docs", "part_map.md"))
        self.assertEqual(self.failures("part-map-file/1"),
                         ["the part map stands in foundations/part_map.md, not in "
                          "docs/part_map.md"])

    def test_a_second_map_in_the_repository(self):
        self.write("old/part_map.md", "# Part map\n")
        self.guard(part_map(part(), flow(), surface(), foundations_part("foundations/**\n  old/**")))
        self.assertEqual(self.failures("part-map-file/1"),
                         ["`old/part_map.md` is a second part map; the repository holds one, "
                          "foundations/part_map.md"])


class Flows(GuardTestCase):
    files = dict(FILES, **{"src/render.py": "def draw():\n    pass\n",
                           "coverage/save-and-load.info": "SF:src/saving.py\nDA:1,1\nend_of_record\n",
                           "gate/test_save_and_load.py": "# flow: save-and-load\n"})

    def rendering(self):
        return part("rendering", files="src/render.py",
                    responsibility="The part answers for drawing the board.",
                    failure_modes=("nothing is drawn — the player is stuck — high — "
                                   "not detected",))

    def foundations(self):
        return foundations_part(files=("foundations/**", "coverage/**", "gate/**"))

    def map_with(self, the_flow):
        return part_map(part(), the_flow, surface(), self.rendering(), self.foundations())

    def test_a_test_naming_the_flow_in_a_flow_line_passes(self):
        """The map names no test: the guard finds the flow's test by its line `# flow:`."""
        self.assertPasses(self.map_with(flow(invariant="INV-2")))
        self.assertRecords(line("check_flows", "pass", "flow-invariant-link/1"))

    def test_a_flow_no_test_names(self):
        self.assertFails(self.map_with(flow(identifier="load-and-save")),
                         "no test names the flow in a line `# flow: load-and-save`")
        self.assertEqual(self.failures("flow-invariant-link/1"),
                         ["line 22: load-and-save: no test names the flow in a line "
                          "`# flow: load-and-save`"])

    def test_a_mention_of_the_flow_outside_a_flow_line_names_no_test(self):
        self.write("tests/test_saving.py", "# save-and-load\ndef test_save():\n    pass\n")
        self.write("gate/test_save_and_load.py", "# the flow save-and-load\n")
        self.guard(self.map_with(flow()))
        self.assertEqual(self.failures("flow-invariant-link/1"),
                         ["line 22: save-and-load: no test names the flow in a line "
                          "`# flow: save-and-load`"])

    def test_a_flow_without_an_invariant(self):
        self.guard(self.map_with(flow(invariant="none")))
        self.assertEqual(self.failures("flow-invariant-link/1"),
                         ["line 22: save-and-load: *Invariant* names no invariant"])

    def test_a_test_path_in_the_invariant_is_not_part_of_the_form(self):
        """The map names no test; a flow that names a test after `— test:` is reported, and its
        invariant still read."""
        self.write("foundations/invariants.md", "# Invariants\n\n## save-round-trip/1\n\nOne.\n")
        code, output = self.guard(part_map(
            part(failure_modes=("a save is lost — the game is lost — high — detected by "
                                "save-round-trip",)),
            flow(invariant="save-round-trip — test: gate/test_save_and_load.py"), surface(),
            self.rendering(), self.foundations()))
        self.assertEqual(code, 1, output)
        self.assertRecords(line("check_flows", "fail", None,
                                "line 22: save-and-load: *Invariant* names a test after `— test:`; "
                                "the flow's test names the flow in a line `# flow: save-and-load` "
                                "instead"))
        self.assertEqual([item for item in self.lines if item["verdict"] == "fail"
                          and item["invariant"] is not None], [])
        self.assertRecords(line("check_invariant_names", "pass", "map-invariant-names/1"))

    def test_flow_without_coverage_is_reported_unchecked(self):
        # invariant: map-guard-missing-coverage/1
        code, output = self.guard(self.map_with(flow()))
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the list of parts of `save-and-load`", output)
        self.assertRecords(line("check_flows", "unchecked", "flow-coverage-parts/1",
                                "the test of `save-and-load` leaves no coverage file",
                                NOT_PRODUCED))

    def test_coverage_names_a_part_outside_the_list(self):
        covers_both = "SF:src/saving.py\nDA:1,1\nend_of_record\nSF:src/render.py\nDA:1,1\n" \
                      "end_of_record\n"
        self.write("coverage/save-and-load.info", covers_both)
        self.assertFails(self.map_with(flow(coverage="coverage/save-and-load.info")),
                         "coverage of `save-and-load` runs through `rendering`, which is not in "
                         "its list of parts")
        self.assertEqual(self.failures("flow-coverage-parts/1"),
                         ["line 23: save-and-load: coverage of `save-and-load` runs through "
                          "`rendering`, which is not in its list of parts"])

    def test_coverage_inside_the_list_passes(self):
        self.assertPasses(self.map_with(flow(coverage="coverage/save-and-load.info")))
        self.assertRecords(line("check_flows", "pass", "flow-coverage-parts/1"))

    def test_coverage_file_that_does_not_exist(self):
        # invariant: map-guard-missing-coverage/1
        code, output = self.guard(self.map_with(flow(coverage="coverage/missing.info")))
        self.assertEqual(code, 1, output)
        self.assertRecords(line("check_flows", "fail", None,
                                "line 23: save-and-load: coverage file `coverage/missing.info` "
                                "does not exist"))
        self.assertRecords(line("check_flows", "unchecked", "flow-coverage-parts/1",
                                "coverage file `coverage/missing.info` of `save-and-load` does "
                                "not exist", NOT_PRODUCED))
        self.assertIn("unchecked: the list of parts of `save-and-load` — its coverage file "
                      "`coverage/missing.info` does not exist\n", output)

    def test_coverage_file_the_guard_cannot_read_is_reported_unchecked(self):
        """A coverage file that holds no `SF:` record names no file the guard can read; silence is
        reported as the list of parts unchecked, never as agreement (WAY-47)."""
        # invariant: map-guard-missing-coverage/1
        self.write("coverage/save-and-load.json",
                   '{"files": {"src/render.py": {"executed_lines": [1]}}}\n')
        code, output = self.guard(self.map_with(flow(coverage="coverage/save-and-load.json")))
        self.assertEqual(code, 0, output)
        self.assertEqual([item["verdict"] for item in self.lines
                          if item["invariant"] == "flow-coverage-parts/1"], ["unchecked"])
        self.assertRecords(line("check_flows", "unchecked", "flow-coverage-parts/1",
                                "coverage file `coverage/save-and-load.json` of `save-and-load` "
                                "holds no `SF:` record the guard reads", NOT_PRODUCED))
        self.assertIn("unchecked: the list of parts of `save-and-load` — its coverage file "
                      "`coverage/save-and-load.json` holds no `SF:` record the guard reads\n",
                      output)

    def test_every_flow_that_leaves_no_coverage_file_is_reported_unchecked(self):
        """Two flows leave no coverage file and two name one that does not exist; each is
        reported as its list of parts unchecked, and the record gives the invariant no pass."""
        # invariant: map-guard-missing-coverage/1
        self.write("tests/test_more.py", "# flow: load-after-restart\n# flow: save-on-exit\n"
                                         "# flow: load-on-start\n")
        more = "INV-2"
        code, output = self.guard(part_map(
            part(), flow(), flow("load-after-restart", invariant=more),
            flow("save-on-exit", invariant=more,
                 coverage="coverage/missing.info"),
            flow("load-on-start", invariant=more, coverage="coverage/gone.info"),
            surface(), self.rendering(), self.foundations()))
        self.assertEqual(code, 1, output)
        for unchecked in ("the list of parts of `save-and-load` — its test leaves no coverage "
                          "file",
                          "the list of parts of `load-after-restart` — its test leaves no "
                          "coverage file",
                          "the list of parts of `save-on-exit` — its coverage file "
                          "`coverage/missing.info` does not exist",
                          "the list of parts of `load-on-start` — its coverage file "
                          "`coverage/gone.info` does not exist"):
            self.assertIn("unchecked: " + unchecked + "\n", output)
        self.assertEqual([item["verdict"] for item in self.lines
                          if item["invariant"] == "flow-coverage-parts/1"], ["unchecked"])

    def test_a_flow_test_outside_gate_in_the_way_s_own_map(self):
        """tests/test_saving.py and gate/test_save_and_load.py both name the flow; the first lies
        outside gate/."""
        self.guard(self.map_with(flow()), own=True)
        self.assertEqual(self.failures("flow-test-location/1"),
                         ["line 22: save-and-load: `tests/test_saving.py` names the flow in a line "
                          "`# flow: save-and-load` and lies outside `gate/`"])

    def test_a_flow_test_under_gate_in_the_way_s_own_map_passes(self):
        self.write("tests/test_saving.py", "def test_save():\n    pass\n")
        self.guard(self.map_with(flow()), own=True)
        self.assertRecords(line("check_flow_tests", "pass", "flow-test-location/1"))
        self.assertEqual(self.failures("flow-invariant-link/1"), [])

    def test_the_test_location_is_checked_only_in_the_way_s_own_map(self):
        self.guard(self.map_with(flow()))
        self.assertNotIn("flow-test-location/1", [item["invariant"] for item in self.lines])


class InvariantNames(GuardTestCase):
    """Every invariant the map names is an entry of foundations/invariants.md (WAY-64)."""

    INVARIANTS = "# Invariants\n\n## save-round-trip/1\n\nA sentence.\n\n## load-order/2\n\nOne.\n"

    def setUp(self):
        super().setUp()
        self.write("foundations/invariants.md", self.INVARIANTS)

    def test_names_that_are_entries_pass(self):
        self.guard(part_map(part(failure_modes=("a save is lost — the game is lost — high — "
                                                "detected by load-order",)),
                            flow(invariant="save-round-trip"),
                            surface(), foundations_part()))
        self.assertRecords(line("check_invariant_names", "pass", "map-invariant-names/1"))

    def test_names_that_are_not_entries(self):
        self.assertFails(part_map(), "invariant `INV-2` is not an entry of "
                                     "foundations/invariants.md")
        self.assertEqual(self.failures("map-invariant-names/1"), [
            "line 12: saving: invariant `INV-2` is not an entry of foundations/invariants.md",
            "line 22: save-and-load: invariant `INV-2` is not an entry of "
            "foundations/invariants.md"])

    def test_without_an_invariants_file_nothing_is_recorded(self):
        os.remove(os.path.join(self.root, "foundations", "invariants.md"))
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertIn("note: there is no invariants.md beside the map", output)
        self.assertNotIn("map-invariant-names/1", [item["invariant"] for item in self.lines])


class Surfaces(GuardTestCase):
    def test_declaration_that_does_not_exist(self):
        self.assertFails(part_map(part(), flow(), surface(declared="src/missing.py · SaveFile"),
                                  foundations_part()),
                         "declaration `src/missing.py` of `save-format` does not exist")
        self.assertEqual(self.failures("surface-declaration/1"),
                         ["line 29: save-format: declaration `src/missing.py` of `save-format` "
                          "does not exist"])

    def test_symbol_that_does_not_stand_in_the_declaration(self):
        self.guard(part_map(part(), flow(), surface(declared="src/saving.py · LoadFile"),
                            foundations_part()))
        self.assertEqual(self.failures("surface-declaration/1"),
                         ["line 29: save-format: `LoadFile` does not stand in `src/saving.py`"])

    def test_declaration_that_names_no_item(self):
        self.assertFails(part_map(part(), flow(), surface(declared="src/saving.py"),
                                  foundations_part()),
                         "declaration `src/saving.py` of `save-format` names no item")
        self.assertEqual(self.failures("surface-declaration/1"),
                         ["line 29: save-format: declaration `src/saving.py` of `save-format` "
                          "names no item"])

    def test_promise_level_written_in_the_map(self):
        self.assertFails(part_map(part(), flow(), surface(declared="src/saving.py · SaveFile · "
                                                                   "stable"),
                                  foundations_part()),
                         "the promise level `stable` belongs at the declaration, not in the map")

    def test_withdrawal_date_written_in_the_map(self):
        self.assertFails(part_map(part(), flow(),
                                  surface(declared="src/saving.py · SaveFile · withdrawn "
                                                   "2027-01-01"),
                                  foundations_part()),
                         "a withdrawal date belongs at the declaration, not in the map")
        self.assertEqual(self.failures("map-withdrawal-date/1"),
                         ["line 29: a withdrawal date belongs at the declaration, not in the map "
                          "(written in `save-format`)"])

    def test_withdrawal_date_elsewhere_in_the_map(self):
        withdrawn = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Why | Successors |",
                               "|---|---|---|",
                               "| game-state | merged into saving | saving, 2026-12-01 |"])
        self.guard(part_map(part(responsibility="The part answers for saving, withdrawn on "
                                                "2027-03-01."), flow(), surface(),
                            foundations_part(), withdrawn=withdrawn))
        self.assertEqual(self.failures("map-withdrawal-date/1"), [
            "line 7: a withdrawal date belongs at the declaration, not in the map (written in a "
            "line that speaks of withdrawal)",
            "line 68: a withdrawal date belongs at the declaration, not in the map (written in "
            "the list of withdrawn identifiers)"])

    def test_surface_that_cannot_be_marked_needs_a_test_that_exists(self):
        self.assertFails(part_map(part(), flow(),
                                  surface(declared="not markable — test: tests/test_missing.py"),
                                  foundations_part()),
                         "test `tests/test_missing.py` of `save-format` does not exist")

    def test_surface_with_a_change_path_of_its_own(self):
        own_path = surface() + "\n- **Change path:** a year's notice"
        self.guard(part_map(part(), flow(), own_path, foundations_part()))
        self.assertEqual(self.failures("surface-change-path/1"),
                         ["line 30: save-format: *Change path* gives the surface a change path of "
                          "its own; a change path belongs to a promise level"])

    def test_change_path_row_for_one_surface(self):
        paths = "\n".join(["## Change paths", "",
                           "| Promise level | What a change at this level may do | "
                           "What it owes the consumer first |", "|---|---|---|",
                           "| save-format | nothing | a year |"])
        self.guard(part_map(paths=paths))
        self.assertEqual(self.failures("surface-change-path/1"),
                         ["line 56: the change path `save-format` names a surface; a change path "
                          "belongs to a promise level, never to one surface"])

    def test_promise_levels_are_reported_unchecked(self):
        # invariant: map-guard-missing-command/1
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertEqual(output, REPORT_WITHOUT_COMMANDS)
        why = "the levels sit at the declarations, and no command of the product reports them"
        self.assertRecords(line("check_promise_levels", "unchecked", "surface-promise-level/1",
                                why, NOT_PRODUCED))
        self.assertRecords(line("check_promise_levels", "unchecked", "promise-level-policy/1",
                                why, NOT_PRODUCED))


class ExternalContext(GuardTestCase):
    def row(self, cells):
        return "\n".join(["## External context", "",
                          "| Partner | Direction | What comes in | Updates with the product |",
                          "|---|---|---|---|", "| %s |" % " | ".join(cells)])

    def test_direction_outside_the_template(self):
        self.assertFails(part_map(context=self.row(["the player's browser", "sideways",
                                                    "untrusted", "no"])),
                         "`sideways` is not one of `them → us`, `us → them`, `both`")
        self.assertEqual(self.failures("external-exchange-row/1"),
                         ["line 50: `sideways` is not one of `them → us`, `us → them`, `both`"])

    def test_trust_outside_the_template(self):
        self.assertFails(part_map(context=self.row(["the player's browser", "both", "maybe",
                                                    "no"])),
                         "`maybe` is not one of `trusted`, `untrusted`, `—`")

    def test_missing_column(self):
        self.assertFails(part_map(context=self.row(["the player's browser", "both", "untrusted"])),
                         "records no *Updates with the product*")
        self.assertEqual(self.failures("external-exchange-row/1"),
                         ["line 50: the row records no *Updates with the product*"])


class Scopes(GuardTestCase):
    def decisions(self, *versions):
        self.write("foundations/decisions.md", "# Decision log\n\n" + "\n\n".join(versions) + "\n")

    def version(self, scope, number=1, ver=1):
        return ("### WAY-%02d/%d — A question?\n\nA sentence.\n\n- **Change:** new decision\n"
                "- **Scope:** %s\n- **Based on:** none" % (number, ver, scope))

    def test_scope_names_a_part_that_does_not_exist(self):
        self.decisions(self.version("saving, rendering"))
        self.assertFails(part_map(), "the scope of WAY-01/1 names `rendering`, which is not in "
                                     "the map")
        self.assertEqual(self.failures("decision-scope-names/1"),
                         ["decisions.md:8: the scope of WAY-01/1 names `rendering`, which is not "
                          "in the map as a part"])

    def test_scope_names_a_withdrawn_part(self):
        self.decisions(self.version("game-state"))
        self.assertFails(part_map(), "the scope of WAY-01/1 names `game-state`, which is "
                                     "withdrawn")

    def test_scope_of_parts_in_the_map_passes(self):
        self.decisions(self.version("saving, foundations"))
        self.assertPasses(part_map())
        self.assertRecords(line("check_scopes", "pass", "decision-scope-names/1"))

    def test_a_scope_over_two_lines(self):
        self.decisions(self.version("saving,\n  foundations, rendering"))
        self.guard(part_map())
        self.assertEqual(self.failures("decision-scope-names/1"),
                         ["decisions.md:8: the scope of WAY-01/1 names `rendering`, which is not "
                          "in the map as a part"])

    def test_only_the_latest_version_counts(self):
        self.decisions(self.version("rendering"), self.version("saving", ver=2))
        self.assertPasses(part_map())

    def test_the_latest_version_is_read(self):
        self.decisions(self.version("saving"), self.version("rendering", ver=2))
        self.guard(part_map())
        self.assertEqual(self.failures("decision-scope-names/1"),
                         ["decisions.md:16: the scope of WAY-01/2 names `rendering`, which is not "
                          "in the map as a part"])

    def test_without_a_log_nothing_is_recorded(self):
        code, output = self.guard(part_map())
        self.assertIn("note: there is no decisions.md beside the map", output)
        self.assertNotIn("decision-scope-names/1", [item["invariant"] for item in self.lines])


class KnownViolations(GuardTestCase):
    def violations(self, *lines):
        self.write("foundations/known_violations.md",
                   "\n".join(["# Known violations", "", "## Known violations", "",
                              "| Source | Target | File | What it reaches for |",
                              "|---|---|---|---|"] + list(lines)) + "\n")

    def test_position_naming_a_part_outside_the_map(self):
        self.violations("| saving | rendering | src/saving.py | the drawing of a board |")
        self.assertFails(part_map(), "known violation names `rendering`, which is not in the map")
        self.assertEqual(self.failures("known-violation-fields/1"),
                         ["foundations/known_violations.md:7: the known violation names "
                          "`rendering`, which is not in the map as a part"])

    def test_position_missing_what_it_reaches_for(self):
        self.violations("| saving | foundations | src/saving.py |")
        self.guard(part_map())
        self.assertEqual(self.failures("known-violation-fields/1"),
                         ["foundations/known_violations.md:7: the known violation records no "
                          "*What it reaches for*"])

    def test_position_with_a_line_number(self):
        self.violations("| saving | foundations | src/saving.py:12 | the log of decisions |")
        self.assertFails(part_map(), "known violation names a line number")
        self.assertEqual(self.failures("known-violation-line-number/1"),
                         ["foundations/known_violations.md:7: the known violation names a line "
                          "number, which goes stale at the next edit"])

    def test_new_and_stale_violations_are_reported_unchecked(self):
        # invariant: map-guard-missing-command/1
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertEqual(output, REPORT_WITHOUT_COMMANDS)
        why = "no command of the product reports the dependency graph"
        self.assertRecords(line("check_dependencies", "unchecked", "known-violation-coverage/1",
                                why, NOT_PRODUCED))
        self.assertRecords(line("check_dependencies", "unchecked", "known-violation-currency/1",
                                why, NOT_PRODUCED))

    def test_dependencies_are_reported_unchecked_without_a_list_of_violations(self):
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the dependencies between parts", output)

    def test_a_position_added_against_the_main_branch(self):
        self.violations()
        self.guard(part_map())
        self.commit()
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("is not on the list of main", output)
        self.assertEqual(self.lines, [
            line("check_violations_growth", "fail", "known-violations-growth/1",
                 "foundations/known_violations.md: `saving · foundations · src/saving.py · the log "
                 "of decisions` is not on the list of main: a row is added only by a change "
                 "of the foundation a human accepts"),
            line("check_identifier_persistence", "pass", "map-identifier-persistence/1")])

    def test_a_base_without_the_list_and_no_position_needs_no_note(self):
        self.write("other.txt", "x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")
        code, output = self.guard(part_map(part(files=("src/saving.py", "tests/**", "other.txt")),
                                           flow(), surface(), foundations_part()), base="main")
        self.assertEqual(code, 0, output)
        self.assertNotIn("every row counts as added", output)
        self.assertEqual(self.lines, [line("check_violations_growth", "pass",
                                           "known-violations-growth/1"),
                                      line("check_identifier_persistence", "pass",
                                           "map-identifier-persistence/1")])

    def test_a_base_without_the_list_and_a_position_says_every_position_is_added(self):
        self.write("other.txt", "x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        code, output = self.guard(part_map(part(files=("src/saving.py", "tests/**", "other.txt")),
                                           flow(), surface(), foundations_part()), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("note: main has no foundations/known_violations.md; every row counts "
                      "as added\n", output)

    def test_a_position_kept_from_the_main_branch_passes(self):
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        self.guard(part_map())
        self.commit()
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.lines, [line("check_violations_growth", "pass",
                                           "known-violations-growth/1"),
                                      line("check_identifier_persistence", "pass",
                                           "map-identifier-persistence/1")])

    def test_a_base_that_does_not_exist_is_an_error(self):
        self.guard(part_map())
        self.commit()
        code, output = self.guard(part_map(), base="origin/main")
        self.assertEqual(code, 1, output)
        self.assertIn("--base origin/main does not exist", output)
        self.assertEqual(self.lines, [line(None, "fail", None, "--base origin/main does not exist")])

    def test_a_failed_call_to_git_is_no_absent_list(self):
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        self.guard(part_map())
        self.commit()
        real = format_guard.shared.call_git

        def failing(arguments, cwd, stdin=None):
            if arguments[0] in ("show", "ls-tree"):
                return 128, "", "fatal: cannot read the object"
            return real(arguments, cwd, stdin)

        with unittest.mock.patch.object(format_guard.shared, "call_git", failing):
            code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 1, output)
        self.assertEqual(self.lines, [
            line(None, "fail", None, "git cannot read foundations/known_violations.md at main: "
                                     "fatal: cannot read the object"),
            line(None, "fail", None, "git cannot read foundations/part_map.md at main: "
                                     "fatal: cannot read the object")])


class BaseNone(GuardTestCase):
    """`none` in place of the commit the branch left the main branch from (WAY-61): the check
    against it is unchecked, and nothing fails."""

    DESCRIPTION = "--base none: there is no commit the branch left the main branch from"
    # every check the run skips is a line of the report, and counts in its last line
    NOT_CHECKED = ("unchecked: the list of known violations — %s\n"
                   "unchecked: the identifiers of the map — %s\n"
                   "unchecked: the lowering of a part's computed criticality — %s\n"
                   ) % ((DESCRIPTION,) * 3)
    UNCHECKED = [line("check_violations_growth", "unchecked", "known-violations-growth/1",
                      DESCRIPTION, NO_COMMIT),
                 line("check_identifier_persistence", "unchecked", "map-identifier-persistence/1",
                      DESCRIPTION, NO_COMMIT)]

    def test_a_clean_map_exits_zero_and_records_the_check_unchecked(self):
        code, output = self.guard(part_map(), base="none")
        self.assertEqual(code, 0, output)
        self.assertIn(self.NOT_CHECKED, output)
        # three checks of the map the product gives no command for, three against the base
        self.assertTrue(output.endswith("0 error(s), 0 warning(s), 6 unchecked\n"), output)
        # the notes the `unchecked:` lines replace stay gone
        self.assertNotIn("note: --base none", output)
        self.assertNotIn("note: --merge-onto none", output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_a_real_base_counts_only_the_checks_the_product_gives_no_command_for(self):
        # the count of unchecked checks grows only where --base reads `none`
        self.guard(part_map())
        self.commit()
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 0, output)
        self.assertNotIn(self.DESCRIPTION, output)
        self.assertTrue(output.endswith("0 error(s), 0 warning(s), 3 unchecked\n"), output)

    def test_an_added_position_is_not_compared(self):
        self.write("foundations/known_violations.md",
                   "## Known violations\n\n| Source | Target | File | What it reaches for |\n"
                   "|---|---|---|---|\n| saving | foundations | src/saving.py | the log |\n")
        code, output = self.guard(part_map(), base="none")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_the_command_line_takes_none(self):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(part_map())
        self.git("add", "-A")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = format_guard.main([self.path, "--base", "none", "--record", self.record_path])
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(code, 0, output.getvalue())
        self.assertEqual(lines, self.UNCHECKED)


class Criticality(GuardTestCase):
    def test_degree_outside_the_scale(self):
        self.assertFails(part_map(part(), flow(criticality="fatal")),
                         "`fatal` is not on the criticality scale")

    def test_failure_mode_with_a_degree_outside_the_scale(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — the game is lost — "
                                                      "fatal — not detected",))),
                         "`fatal` is not on the criticality scale")
        self.assertEqual(self.failures("failure-mode-severity/1"),
                         ["line 12: saving: `fatal` is not on the criticality scale"])

    def test_a_severity_off_the_scale_names_no_severity(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — the game is lost — "
                                                      "medium — detected by INV-2",))),
                         "`medium` is not on the criticality scale")
        self.assertEqual(self.failures("failure-mode-severity/1"),
                         ["line 12: saving: `medium` is not on the criticality scale"])
        self.assertEqual(self.failures("failure-mode-detection/1"), [])

    def test_a_severity_todo_names_no_severity(self):
        self.guard(part_map(part(failure_modes=("a save is lost — the game is lost — TODO — "
                                                "not detected",))))
        self.assertEqual(self.failures("failure-mode-severity/1"),
                         ["line 12: saving: `TODO` is not on the criticality scale"])
        self.assertEqual(self.failures("map-entry-field-words/1"),
                         ["line 12: saving: *Failure modes* holds `TODO`, which its form does not "
                          "give it"])

    def test_a_severity_off_the_scale_without_detection_fails_both(self):
        self.guard(part_map(part(failure_modes=("a save is lost — the game is lost — medium",))))
        self.assertEqual(self.failures("failure-mode-severity/1"),
                         ["line 12: saving: `medium` is not on the criticality scale"])
        self.assertEqual(self.failures("failure-mode-detection/1"),
                         ["line 12: saving: `a save is lost — the game is lost — medium` names "
                          "neither a detecting invariant nor `not detected`"])

    def test_criticality_written_at_a_part(self):
        written = part() + "\n- **Criticality:** high"
        self.assertFails(part_map(written), "carries the fields of a part and of a critical flow")
        self.assertEqual(self.failures("part-criticality-field/1"),
                         ["line 5: `saving` carries the fields of a part and of a critical flow: "
                          "an entry is of one kind, and a part's criticality is computed, never "
                          "written"])
        self.assertEqual(len(self.failures("map-entry-kinds/1")), 1, self.lines)

    def test_criticality_under_another_name_at_a_part(self):
        written = part() + "\n- **Criticality (computed):** high"
        self.guard(part_map(written, flow(), surface(), foundations_part()))
        self.assertEqual(self.failures("part-criticality-field/1"),
                         ["line 15: saving: a part carries *Criticality (computed)*; its "
                          "criticality is computed, never written"])
        self.assertEqual(self.failures("map-entry-kinds/1"), [])

    def test_failure_mode_without_detection(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — the game is lost — high",))),
                         "names neither a detecting invariant nor `not detected`")
        self.assertEqual(self.failures("failure-mode-detection/1"),
                         ["line 12: saving: `a save is lost — the game is lost — high` names "
                          "neither a detecting invariant nor `not detected`"])
        self.assertEqual(self.failures("failure-mode-severity/1"), [])

    def test_failure_mode_wrapped_over_two_lines(self):
        wrapped = part(failure_modes=("a save is lost — the player loses the game — high —\n"
                                      "    detected by INV-2",))
        foundations = part("foundations", files="foundations/**",
                           responsibility="The part answers for what binds.",
                           failure_modes=("a rule read wrong — work goes the light path — low — "
                                          "not detected",))
        self.assertPasses(part_map(wrapped, flow(), surface(), foundations))

    def test_failure_mode_without_severity(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — not detected",))),
                         "is not `<what fails> — <damage> — <severity> — <detection>`")
        self.assertEqual(self.failures("failure-mode-severity/1"),
                         ["line 12: saving: `a save is lost — not detected` is not `<what fails> "
                          "— <damage> — <severity> — <detection>`"])
        self.assertEqual(self.failures("failure-mode-detection/1"), [])

    def test_failure_mode_with_neither(self):
        self.guard(part_map(part(failure_modes=("a save is lost",))))
        self.assertEqual(len(self.failures("failure-mode-severity/1")), 1, self.lines)
        self.assertEqual(len(self.failures("failure-mode-detection/1")), 1, self.lines)

    def test_detected_by_todo_names_no_detecting_invariant(self):
        code, output = self.guard(part_map(part(failure_modes=("a save is lost — the game is lost "
                                                               "— high — detected by TODO",))))
        self.assertEqual(code, 1, output)
        self.assertEqual(self.failures("failure-mode-detection/1"),
                         ["line 12: saving: `a save is lost — the game is lost — high — detected "
                          "by TODO` names neither a detecting invariant nor `not detected`"])
        self.assertEqual(self.failures("map-entry-field-words/1"),
                         ["line 12: saving: *Failure modes* holds `TODO`, which its form does not "
                          "give it"])

    def test_todo_as_a_word_inside_a_value(self):
        cases = [
            ("a flow's invariant", part_map(part(), flow(invariant="the TODO invariant"),
                                            surface(), foundations_part()),
             "line 22: save-and-load: *Invariant* holds `TODO`, which its form does not give it"),
            ("a symbol", part_map(part(), flow(), surface(declared="src/saving.py · (TODO)"),
                                  foundations_part()),
             "line 29: save-format: *Declared at* holds `TODO`, which its form does not give it"),
        ]
        for what, text, description in cases:
            with self.subTest(what):
                self.guard(text)
                self.assertEqual(self.failures("map-entry-field-words/1"), [description])

    def test_todo_inside_a_path_is_no_todo(self):
        self.write("docs/TODO.md", "# Later\n")
        self.assertPasses(part_map(part(files=("src/saving.py", "tests/**", "docs/TODO.md")),
                                   flow(), surface(), foundations_part()))


class Reported(GuardTestCase):
    files = dict(FILES, **{"src/storage.py": "def write():\n    pass\n"})

    def test_dependency_from_higher_to_lower_is_reported(self):
        # invariant: map-guard-dependency-report/1
        storage = part("storage", files="src/storage.py",
                       responsibility="The part answers for the disk.",
                       failure_modes=("a write fails — a step is repeated — low — not detected",))
        code, output = self.guard(part_map(part(depends="storage"), flow(), surface(), storage,
                                           foundations_part()))
        self.assertEqual(code, 0, output)
        self.assertIn("so storage is computed as `high`, above its own failure modes", output)

    def test_a_degree_outside_the_scale_at_a_part_something_depends_on(self):
        storage = part("storage", files="src/storage.py",
                       responsibility="The part answers for the disk.",
                       failure_modes=("a write fails — a step is repeated — fatal — "
                                      "not detected",))
        self.assertFails(part_map(part(depends="storage"), flow(), surface(), storage,
                                  foundations_part()),
                         "`fatal` is not on the criticality scale")

    def test_a_map_outside_a_git_repository_is_a_failure_of_the_run(self):
        """A guard whose call to git fails reports no check as unchecked (WAY-63)."""
        shutil.rmtree(os.path.join(self.root, ".git"))
        code, output = self.guard(part_map())
        self.assertEqual(code, 1, output)
        self.assertIn("error: the map does not lie in a git repository", output)
        self.assertRecords(line(None, "fail", None,
                                "the map does not lie in a git repository, so no check that asks "
                                "git which files it tracks can run"))
        recorded = {item["invariant"] for item in self.lines}
        for invariant in ("file-part-assignment/1", "path-pattern-reach/1", "part-map-file/1",
                          "flow-invariant-link/1", "surface-declaration/1"):
            self.assertNotIn(invariant, recorded)


class Dependencies(GuardTestCase):
    """The map guard computes the criticality of a part that has failure modes recorded as the
    highest of its own failure modes, of the flows it lies on and of the parts that depend on it by
    a dependency recording no separation; the tests read the computed value from its warning."""

    files = dict(FILES, **{"src/storage.py": "def write():\n    pass\n",
                           "src/cache.py": "def keep():\n    pass\n"})

    def lower(self, identifier, title, depends="none"):
        """A part of low criticality of its own, in src/<identifier>.py."""
        return part(identifier, files="src/%s.py" % identifier, depends=depends,
                    responsibility="The part answers for %s." % title.lower(),
                    failure_modes=("it fails — a step is repeated — low — not detected",))

    def test_a_dependency_is_reported_beside_a_separated_one(self):
        # invariant: map-guard-dependency-report/1
        code, output = self.guard(part_map(
            part(depends="storage · cache (separated — a lost cache is rebuilt)"), flow(),
            surface(), self.lower("storage", "Storage"), self.lower("cache", "Cache"),
            foundations_part()))
        self.assertEqual(code, 0, output)
        self.assertIn("saving depends on storage with no separation recorded, so storage is "
                      "computed as `high`, above its own failure modes", output)

    def test_a_separation_the_lower_part_records_elsewhere_does_not_count(self):
        # invariant: map-guard-dependency-report/1
        code, output = self.guard(part_map(
            part(depends="storage"), flow(), surface(),
            self.lower("storage", "Storage", depends="cache (separated — a lost cache is rebuilt)"),
            self.lower("cache", "Cache"), foundations_part()))
        self.assertEqual(code, 0, output)
        self.assertIn("saving depends on storage with no separation recorded, so storage is "
                      "computed as `high`, above its own failure modes", output)

    def test_a_part_raised_by_a_flow_it_lies_on_reports_its_dependency(self):
        """saving's own failure mode is low; the high flow it lies on raises it to high."""
        # invariant: map-guard-dependency-report/1
        code, output = self.guard(part_map(
            part(depends="storage", failure_modes=("a save is slow — a step is repeated — low — "
                                                   "not detected",)),
            flow(criticality="high", parts="saving"), surface(),
            self.lower("storage", "Storage"), self.lower("cache", "Cache"), foundations_part()))
        self.assertEqual(code, 0, output)
        self.assertIn("saving depends on storage with no separation recorded, so storage is "
                      "computed as `high`, above its own failure modes", output)

    def test_a_dependency_down_a_chain_is_reported(self):
        """cache, then storage depending on it, then saving (high) depending on storage, listed
        in that order: high reaches storage, and through it cache."""
        # invariant: map-guard-dependency-report/1
        code, output = self.guard(part_map(
            self.lower("cache", "Cache"), self.lower("storage", "Storage", depends="cache"),
            part(depends="storage"), flow(), surface(), foundations_part()))
        self.assertEqual(code, 0, output)
        self.assertIn("saving depends on storage with no separation recorded, so storage is "
                      "computed as `high`, above its own failure modes", output)
        self.assertIn("storage depends on cache with no separation recorded, so cache is "
                      "computed as `high`, above its own failure modes", output)

    def test_every_dependency_of_a_part_is_reported(self):
        # invariant: map-guard-dependency-report/1
        code, output = self.guard(part_map(
            part(depends="storage · cache"), flow(), surface(), self.lower("storage", "Storage"),
            self.lower("cache", "Cache"), foundations_part()))
        self.assertEqual(code, 0, output)
        self.assertIn("saving depends on storage with no separation recorded, so storage is "
                      "computed as `high`, above its own failure modes", output)
        self.assertIn("saving depends on cache with no separation recorded, so cache is "
                      "computed as `high`, above its own failure modes", output)


class Record(GuardTestCase):
    def test_a_plain_run_records_a_verdict_for_each_check_that_ran(self):
        self.guard(part_map())
        self.assertEqual(self.lines, [
            line("check_sections", "pass", "map-section-kinds/1"),
            line("check_kinds", "pass", "map-entry-kinds/1"),
            line("check_kinds", "pass", "part-criticality-field/1"),
            line("check_identifiers", "pass", "map-identifier-form/1"),
            line("check_identifiers", "pass", "map-entry-version/1"),
            line("check_fields", "pass", "map-entry-field-presence/1"),
            line("check_fields", "pass", "map-entry-field-words/1"),
            line("check_references", "pass", "flow-part-names/1"),
            line("check_criticality", "pass", "failure-mode-severity/1"),
            line("check_criticality", "pass", "failure-mode-detection/1"),
            line("check_map_file", "pass", "part-map-file/1"),
            line("check_files", "pass", "file-part-assignment/1"),
            line("check_files", "pass", "path-pattern-reach/1"),
            line("check_files", "pass", "left-out-file-assignment/1"),
            line("check_flows", "pass", "flow-invariant-link/1"),
            line("check_flows", "unchecked", "flow-coverage-parts/1",
                 "the test of `save-and-load` leaves no coverage file", NOT_PRODUCED),
            line("check_surfaces", "pass", "map-withdrawal-date/1"),
            line("check_surfaces", "pass", "surface-change-path/1"),
            line("check_surfaces", "pass", "surface-declaration/1"),
            line("check_promise_levels", "unchecked", "surface-promise-level/1",
                 "the levels sit at the declarations, and no command of the product reports them",
                 NOT_PRODUCED),
            line("check_promise_levels", "unchecked", "promise-level-policy/1",
                 "the levels sit at the declarations, and no command of the product reports them",
                 NOT_PRODUCED),
            line("check_lists", "pass", "external-exchange-row/1"),
            line("check_withdrawn", "pass", "map-withdrawal-successors/1"),
            line("check_violations", "pass", "known-violation-fields/1"),
            line("check_violations", "pass", "known-violation-line-number/1"),
            line("check_dependencies", "unchecked", "known-violation-coverage/1",
                 "no command of the product reports the dependency graph", NOT_PRODUCED),
            line("check_dependencies", "unchecked", "known-violation-currency/1",
                 "no command of the product reports the dependency graph", NOT_PRODUCED),
        ])

    def test_a_line_holds_only_the_keys_of_the_form(self):
        self.guard(part_map(part(identifier="Saving", depends="TODO"), flow(parts="none"),
                            surface(declared="src/missing.py"), foundations_part()))
        self.assertTrue(any(item["verdict"] == "fail" for item in self.lines))
        for item in self.lines:
            self.assertTrue(set(item) <= {"check", "verdict", "invariant", "reason",
                                          "description"}, item)
            self.assertIn(item["verdict"], ("pass", "fail", "unchecked"), item)
            self.assertEqual("reason" in item, item["verdict"] == "unchecked", item)
            self.assertEqual("description" in item, item["verdict"] != "pass", item)

    def test_a_finding_records_fail_and_no_pass(self):
        self.guard(part_map(part(identifier="Saving")))
        self.assertNotIn(line("check_identifiers", "pass", "map-identifier-form/1"), self.lines)

    def test_a_map_that_is_not_utf_8_is_a_failure_of_the_run_in_every_record(self):
        with open(self.path, "wb") as handle:
            handle.write(b"# Part map\n\ncaf\xe9\n")
        for base in (None, "none"):
            with self.subTest(base=base):
                output = io.StringIO()
                code = format_guard.run(self.path, base=base, stream=output,
                                        record=self.record_path)
                with open(self.record_path, encoding="utf-8") as handle:
                    lines = [json.loads(item) for item in handle.read().split("\n") if item]
                self.assertEqual(code, 2, output.getvalue())
                self.assertEqual(len(lines), 1, lines)
                self.assertEqual({key: lines[0][key] for key in ("check", "verdict", "invariant")},
                                 {"check": GUARD, "verdict": "fail", "invariant": None})
                self.assertTrue(lines[0]["description"].startswith(
                    "cannot read the map: 'utf-8' codec can't decode"), lines)

    def test_a_side_file_that_is_not_utf_8_is_a_failure_of_the_run_in_every_record(self):
        with open(os.path.join(self.root, "foundations", "decisions.md"), "wb") as handle:
            handle.write(b"### WAY-01/1 \xe9\n")
        for base in (None, "none"):
            with self.subTest(base=base):
                code, output = self.guard(part_map(), base=base)
                self.assertEqual(code, 1, output)
                self.assertEqual([item["check"] for item in self.lines
                                  if item["invariant"] is None], [GUARD], self.lines)
                self.assertNotIn("decision-scope-names/1",
                                 [item["invariant"] for item in self.lines])

    def test_a_failure_no_rule_gave_names_the_program(self):
        output = io.StringIO()
        code = format_guard.run(os.path.join(self.root, "missing.md"), stream=output,
                                record=self.record_path)
        self.assertEqual(code, 2, output.getvalue())
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(len(lines), 1, lines)
        self.assertEqual({key: lines[0][key] for key in ("check", "verdict", "invariant")},
                         {"check": GUARD, "verdict": "fail", "invariant": None})
        self.assertTrue(lines[0]["description"].startswith("cannot read the map: "), lines)

    def test_the_record_is_overwritten(self):
        os.makedirs(os.path.dirname(self.record_path))
        with open(self.record_path, "w", encoding="utf-8") as handle:
            handle.write('{"check": "old", "verdict": "pass", "invariant": "map-entry-kinds/1"}\n')
        self.guard(part_map())
        self.assertNotIn({"check": "old", "verdict": "pass", "invariant": "map-entry-kinds/1"},
                         self.lines)

    def test_the_report_for_a_person_stays(self):
        code, output = self.guard(part_map(part(identifier="Saving")))
        self.assertEqual(code, 1)
        self.assertIn("part_map.md:5: error: `Saving` is not an identifier of words in lower case "
                      "joined by hyphens\n", output)

    def test_each_verdict_stands_at_a_check_citing_its_invariant(self):
        self.write("foundations/invariants.md", "# Invariants\n\n## other/1\n\nA sentence.\n")
        self.write("foundations/decisions.md", "### WAY-01/1 — Q?\n\nS.\n\n- **Scope:** nothing\n")
        self.guard(part_map(part(identifier="Saving/2", depends="TODO"),
                            flow(parts="none", invariant="— test: tests/missing.py"),
                            surface(declared="src/saving.py · SaveFile · 2027-01-01"),
                            foundations_part()), own=True)
        self.assertTrue(any(item["verdict"] == "fail" for item in self.lines))
        for item in self.lines:
            if item["invariant"] is None:
                continue
            function = item["check"].split("::")[1]
            self.assertIn("# invariant: %s\n" % item["invariant"],
                          inspect.getsource(getattr(format_guard, function)), item)


class RecordPerCommand(GuardTestCase):
    """A run records the checks its options select; the report for a person keeps them all."""

    files = dict(FILES, **{"gate/test_save_and_load.py": "# flow: save-and-load\n",
                           "tests/test_saving.py": "def test_save():\n    pass\n"})
    MAP_ALONE = [
        "decision-scope-names/1", "external-exchange-row/1", "failure-mode-detection/1",
        "failure-mode-severity/1", "file-part-assignment/1", "flow-coverage-parts/1",
        "flow-invariant-link/1", "flow-part-names/1", "flow-test-location/1",
        "known-violation-coverage/1", "known-violation-currency/1", "known-violation-fields/1",
        "known-violation-line-number/1", "left-out-file-assignment/1",
        "map-entry-field-presence/1", "map-entry-field-words/1", "map-entry-kinds/1",
        "map-entry-version/1", "map-identifier-form/1", "map-invariant-names/1",
        "map-section-kinds/1", "map-withdrawal-date/1", "map-withdrawal-successors/1",
        "part-criticality-field/1",
        "part-map-file/1", "path-pattern-reach/1", "promise-level-policy/1",
        "surface-change-path/1", "surface-declaration/1", "surface-promise-level/1"]

    def setUp(self):
        super().setUp()
        self.write("foundations/invariants.md", "# Invariants\n\n## save-round-trip/1\n\nOne.\n")
        self.write("foundations/decisions.md", "### WAY-01/1 — Q?\n\nS.\n\n- **Scope:** saving\n")
        self.text = part_map(part(failure_modes=("a save is lost — the game is lost — high — "
                                                 "detected by save-round-trip",)),
                             flow(invariant="save-round-trip"),
                             surface(), foundations_part("foundations/**\n  gate/**"))
        self.guard(self.text)
        self.commit()

    def identifiers(self):
        return sorted({item["invariant"] for item in self.lines})

    def test_the_plain_command(self):
        code, output = self.guard(self.text, own=True)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.identifiers(), self.MAP_ALONE)

    def test_the_command_with_base(self):
        self.guard(self.text, base="main", own=True)
        self.assertEqual(self.identifiers(), ["known-violations-growth/1",
                                              "map-identifier-persistence/1"])

    def test_a_failure_of_the_map_alone_stays_out_of_the_base_record(self):
        code, output = self.guard(self.text.replace("## saving\n", "## Saving\n"), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("`Saving` is not an identifier", output)
        self.assertEqual(self.lines, [line("check_violations_growth", "pass",
                                           "known-violations-growth/1"),
                                      line("check_identifier_persistence", "fail",
                                           "map-identifier-persistence/1",
                                           "`saving` stands in the map on main and is gone; it "
                                           "stays as an entry or a withdrawn identifier")])


class Examples(GuardTestCase):
    """`examples.md` names, by identifier, entries of the-way's own map, which the guard checks on
    that map alone."""

    def examples(self, *items):
        path = os.path.join(self.root, "examples.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("# Examples\n\nThe entries of `foundations/part_map.md` that show the "
                         "form of an entry.\n\n" + "\n".join(items) + "\n")
        return path

    def test_identifiers_of_entries_pass(self):
        self.guard(part_map(), own=True,
                   examples=self.examples("- `saving` — a part", "- `save-and-load` — a flow",
                                          "- `save-format` — a surface"))
        self.assertRecords(line("check_examples", "pass", "map-example-target/1"))
        self.assertEqual(self.failures("map-example-target/1"), [])

    def test_an_identifier_outside_the_map(self):
        self.guard(part_map(), own=True,
                   examples=self.examples("- `saving` — a part", "- `rendering` — a part"))
        self.assertEqual(self.failures("map-example-target/1"),
                         ["examples.md:6: `rendering` is not the identifier of an entry of the "
                          "map"])

    def test_a_withdrawn_identifier_is_no_entry(self):
        self.guard(part_map(), own=True, examples=self.examples("- game-state — a part"))
        self.assertEqual(self.failures("map-example-target/1"),
                         ["examples.md:5: `game-state` is not the identifier of an entry of the "
                          "map"])

    def test_a_copied_entry_names_no_identifier_of_the_map(self):
        self.guard(part_map(), own=True,
                   examples=self.examples("## rendering — Rendering", "",
                                          "The part answers for drawing.", "",
                                          "- **Files:** src/render.py"))
        self.assertEqual(self.failures("map-example-target/1"),
                         ["examples.md:9: `**Files:**` is not the identifier of an entry of the "
                          "map"])

    def test_examples_are_checked_on_the_way_s_own_map_alone(self):
        self.guard(part_map(), examples=self.examples("- `rendering` — a part"))
        self.assertNotIn("map-example-target/1", [item["invariant"] for item in self.lines])


class Withdrawn(GuardTestCase):
    """Every withdrawn identifier of the map gives why it was withdrawn and names one or more
    successors, each an entry or a withdrawn identifier of the map."""

    def withdrawn(self, *rows, header=("Identifier", "Why", "Successors")):
        return "\n".join(["## Withdrawn identifiers", "", "| %s |" % " | ".join(header),
                          "|%s" % ("---|" * len(header))] + list(rows))

    def test_why_and_successors_of_the_map_pass(self):
        self.assertPasses(part_map(withdrawn=self.withdrawn(
            "| game-state | merged into save-data | save-data |",
            "| save-data | split into saving and save-format | saving · save-format |")))
        self.assertRecords(line("check_withdrawn", "pass", "map-withdrawal-successors/1"))

    def test_a_row_that_gives_no_why(self):
        for why in ("", "TODO", "none", "`none`"):
            with self.subTest(why=why):
                self.guard(part_map(withdrawn=self.withdrawn("| game-state | %s | saving |" % why)))
                self.assertEqual(self.failures("map-withdrawal-successors/1"),
                                 ["line 68: `game-state` gives no why it was withdrawn"])

    def test_a_row_that_names_no_successor(self):
        for successors in ("none", ""):
            with self.subTest(successors=successors):
                self.guard(part_map(withdrawn=self.withdrawn(
                    "| game-state | merged into saving | %s |" % successors)))
                self.assertEqual(self.failures("map-withdrawal-successors/1"),
                                 ["line 68: `game-state` names no successor; the map withdraws an "
                                  "identifier only on a split or a merge, which leaves entries in "
                                  "its place"])

    def test_a_successor_outside_the_map(self):
        self.guard(part_map(withdrawn=self.withdrawn(
            "| game-state | split into saving and rendering | saving · rendering |")))
        self.assertEqual(self.failures("map-withdrawal-successors/1"),
                         ["line 68: `game-state` names `rendering` as a successor, which is "
                          "neither an entry nor a withdrawn identifier of the map"])

    def test_todo_in_any_cell_of_a_row(self):
        for row in ("| TODO | merged into saving | saving |",
                    "| game-state | merged into saving | TODO |"):
            with self.subTest(row=row):
                self.assertFails(part_map(withdrawn=self.withdrawn(row)),
                                 "the list `Withdrawn identifiers` holds `TODO`")
                self.assertRecords(line("check_withdrawn", "fail", None,
                                        "line 68: the list `Withdrawn identifiers` holds `TODO`"))

    def test_an_identifier_whose_row_holds_todo_stays_withdrawn(self):
        self.assertFails(part_map(part(identifier="game-state"), part(files="tests/**"),
                                  withdrawn=self.withdrawn("| game-state | TODO | saving |")),
                         "`game-state` is withdrawn: a withdrawn identifier is never reused")

    def test_a_row_that_names_itself_as_its_successor(self):
        self.guard(part_map(withdrawn=self.withdrawn("| game-state | merged into saving | "
                                                     "game-state |")))
        self.assertEqual(self.failures("map-withdrawal-successors/1"),
                         ["line 68: `game-state` names itself as a successor"])

    def test_the_form_of_the_list_is_read_from_the_rules_the_elements_share(self):
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            self.assertNotIn("| Identifier | Why | Successors |", handle.read())
        self.assertEqual(format_guard.read_rules().lists["Withdrawn identifiers"],
                         ["Identifier", "Why", "Successors"])
        with open(format_guard.shared.COMMON_RULES, encoding="utf-8") as handle:
            text = handle.read()
        common = os.path.join(self.root, "rules.md")
        with open(common, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text.replace("| Identifier | Why | Successors |",
                                      "| Identifier | Why | Successors | Since |", 1))
        self.assertEqual(format_guard.read_rules(common=common).lists["Withdrawn identifiers"],
                         ["Identifier", "Why", "Successors", "Since"])

    def test_a_list_without_why(self):
        self.guard(part_map(withdrawn=self.withdrawn("| game-state | saving |",
                                                     header=("Identifier", "Successors"))))
        self.assertEqual(self.failures("map-withdrawal-successors/1"), [
            "line 66: the list of withdrawn identifiers has the columns Identifier, Successors, "
            "not Identifier, Why, Successors",
            "line 68: `game-state` gives no why it was withdrawn"])


class IdentifierPersistence(GuardTestCase):
    """Given the commit the branch left the main branch from, every identifier the map held there
    stands in it as an entry or as a withdrawn identifier (WAY-41)."""

    def test_a_withdrawn_identifier_gone_from_the_list(self):
        # invariant: map-identifier-persistence/1
        self.guard(part_map())
        self.commit()
        code, output = self.guard(part_map(withdrawn=""), base="main")
        self.assertEqual(code, 1, output)
        self.assertEqual(self.failures("map-identifier-persistence/1"),
                         ["`game-state` stands in the map on main and is gone; it stays as an "
                          "entry or a withdrawn identifier"])

    def test_an_entry_gone_from_the_map(self):
        # invariant: map-identifier-persistence/1
        self.guard(part_map())
        self.commit()
        self.guard(part_map(part(), flow(), foundations_part()), base="main")
        self.assertEqual(self.failures("map-identifier-persistence/1"),
                         ["`save-format` stands in the map on main and is gone; it stays as an "
                          "entry or a withdrawn identifier"])

    def test_an_entry_moved_to_the_list_of_withdrawn_identifiers(self):
        # invariant: map-identifier-persistence/1
        self.guard(part_map())
        self.commit()
        withdrawn = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Why | Successors |",
                               "|---|---|---|", "| game-state | merged into saving | saving |",
                               "| save-format | merged into saving | saving |"])
        self.guard(part_map(part(), flow(), foundations_part(), withdrawn=withdrawn), base="main")
        self.assertEqual(self.failures("map-identifier-persistence/1"), [])
        self.assertRecords(line("check_identifier_persistence", "pass",
                                "map-identifier-persistence/1"))

    def test_an_identifier_added_since_the_base(self):
        # invariant: map-identifier-persistence/1
        self.guard(part_map(withdrawn=""))
        self.commit()
        self.guard(part_map(), base="main")
        self.assertEqual(self.failures("map-identifier-persistence/1"), [])
        self.assertRecords(line("check_identifier_persistence", "pass",
                                "map-identifier-persistence/1"))


class CriticalityLowering(GuardTestCase):
    """Given the commit the branch left the main branch from, the guard warns of every part whose
    computed criticality is lower than on that commit."""

    LOW = ("a save is lost — a step is repeated — low — detected by INV-2",)

    def storage(self):
        return part("storage", files="src/storage.py",
                    responsibility="The part answers for the disk.",
                    failure_modes=("a write fails — a step is repeated — low — not detected",))

    def test_a_lowered_part_is_reported(self):
        # invariant: criticality-lowering-report/1
        self.guard(part_map())
        self.commit()
        code, output = self.guard(part_map(part(failure_modes=self.LOW), flow(criticality="low"),
                                           surface(), foundations_part()), base="main")
        self.assertEqual(code, 0, output)
        self.assertIn("part_map.md:5: warning: saving: the computed criticality is `low`, lower "
                      "than `high` on main\n", output)
        self.assertTrue(output.endswith("0 error(s), 1 warning(s), 3 unchecked\n"), output)

    def test_every_lowered_part_is_reported_a_dependency_included(self):
        # invariant: criticality-lowering-report/1
        self.write("src/storage.py", "def write():\n    pass\n")
        self.guard(part_map(part(depends="storage"), flow(), surface(), self.storage(),
                            foundations_part()))
        self.commit()
        code, output = self.guard(part_map(
            part(depends="storage (separated — a failed write leaves the game intact)",
                 failure_modes=self.LOW),
            flow(criticality="low"), surface(), self.storage(), foundations_part()), base="main")
        self.assertEqual(code, 0, output)
        self.assertIn("part_map.md:5: warning: saving: the computed criticality is `low`, lower "
                      "than `high` on main\n", output)
        self.assertIn("part_map.md:31: warning: storage: the computed criticality is `low`, lower "
                      "than `high` on main\n", output)

    def test_a_raised_part_is_not_reported(self):
        # invariant: criticality-lowering-report/1
        self.guard(part_map(part(failure_modes=self.LOW), flow(criticality="low"), surface(),
                            foundations_part()))
        self.commit()
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 0, output)
        self.assertNotIn("lower than", output)

    def test_a_degree_off_the_scale_is_not_compared(self):
        # invariant: criticality-lowering-report/1
        scale = "\n".join(["## Criticality scale", "", "1. low — the player retries a step",
                           "2. high — the player loses the game",
                           "3. fatal — the player loses every game"])
        self.guard(part_map(part(failure_modes=("a save is lost — every game is lost — fatal — "
                                                "detected by INV-2",)),
                            flow(), surface(), foundations_part(), scale=scale))
        self.commit()
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 0, output)
        self.assertNotIn("lower than", output)
        self.assertIn("note: saving: `fatal` on main is not on the criticality scale, so its "
                      "computed criticality is not compared\n", output)

    def test_a_base_without_the_map_compares_nothing(self):
        # invariant: criticality-lowering-report/1
        self.commit()
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 0, output)
        self.assertIn("note: main has no foundations/part_map.md, so no part's computed "
                      "criticality is compared with it\n", output)

    def test_base_none_says_it_cannot_compare(self):
        # invariant: criticality-lowering-report/1
        code, output = self.guard(part_map(), base="none")
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the lowering of a part's computed criticality — --base none: "
                      "there is no commit the branch left the main branch from\n", output)


class ComputedCriticality(unittest.TestCase):
    def rules(self):
        return format_guard.read_rules()

    def compute(self, text):
        entries, sections = format_guard.parse_map(text, self.rules())
        return format_guard.criticality(entries, sections)

    def test_a_part_takes_the_degree_of_its_own_worst_failure(self):
        text = part_map(part(failure_modes=("a save is lost — the game is lost — low — "
                                            "not detected",
                                            "a save is corrupted — the game is lost — high — "
                                            "not detected")))
        self.assertEqual(self.compute(text)["saving"], "high")

    def test_a_part_inherits_from_the_part_that_depends_on_it(self):
        text = part_map(part(), part("storage", files="src/storage.py",
                                     responsibility="The part answers for the disk.",
                                     failure_modes=("a write fails — a step is repeated — low — "
                                                    "not detected",)),
                        part("saving2", files="src/other.py", depends="storage",
                             responsibility="The part answers for saving elsewhere.",
                             failure_modes=("a save is lost — the game is lost — high — "
                                            "not detected",)))
        self.assertEqual(self.compute(text)["storage"], "high")

    def test_a_separation_stops_the_inheritance(self):
        text = part_map(part("storage", files="src/storage.py",
                             responsibility="The part answers for the disk.",
                             failure_modes=("a write fails — a step is repeated — low — "
                                            "not detected",)),
                        part("saving2", files="src/other.py",
                             depends="storage (separated — a failed write leaves the game intact)",
                             responsibility="The part answers for saving elsewhere.",
                             failure_modes=("a save is lost — the game is lost — high — "
                                            "not detected",)))
        self.assertEqual(self.compute(text)["storage"], "low")

    def test_a_part_without_failure_modes_is_the_highest_degree(self):
        # invariant: map-guard-unrecorded-criticality/1
        text = part_map(part(failure_modes=()))
        self.assertEqual(self.compute(text)["saving"], "high")

    def test_a_part_recording_none_takes_the_highest_degree_of_the_map_s_own_scale(self):
        # invariant: map-guard-unrecorded-criticality/1
        scale = "\n".join(["## Criticality scale", "", "1. low — the player retries a step",
                           "2. high — the player loses the game",
                           "3. fatal — the player loses every game"])
        text = part_map(part(failure_modes=()).replace("- **Failure modes:** \n",
                                                       "- **Failure modes:** none"),
                        scale=scale)
        self.assertIn("- **Failure modes:** none\n", text)
        self.assertEqual(self.compute(text)["saving"], "fatal")

    def test_a_part_takes_the_degree_of_a_flow_it_lies_on(self):
        text = part_map(part(failure_modes=("a save is lost — a step is repeated — low — "
                                            "not detected",)),
                        flow(criticality="high", parts="saving"))
        self.assertEqual(self.compute(text)["saving"], "high")


class TestRuns(GuardTestCase):
    """The map guard reads what a test run left and starts none itself (WAY-47).

    The outcome is watched: each flow's test file writes a marker when it is imported and when a
    test in it runs, so a run of it by any route — a child process of any kind, a test runner in
    the process, an import of the file and a call of its tests — leaves the marker behind. The
    guard runs on maps whose flow leaves a coverage file, leaves none, or names one that does not
    exist, with the flow named by a test outside `gate/` and by one under it. Beside that, every program the
    guard starts through `subprocess.Popen` or the `os` functions that start one must be git, and
    no `unittest` runner or loader may be called inside the process."""

    files = dict(FILES, **{"coverage/save-and-load.info": "SF:src/saving.py\nend_of_record\n",
                           "foundations/known_violations.md": "## Known violations\n"})

    def setUp(self):
        super().setUp()
        self.marker = os.path.join(self.root, "flow-test-ran.txt")
        test = "\n".join([
            "# flow: save-and-load",
            "import unittest",
            "",
            "MARKER = %r" % self.marker,
            "with open(MARKER, 'a') as handle:",
            "    handle.write('imported ' + __name__ + '\\n')",
            "",
            "",
            "def test_save():",
            "    with open(MARKER, 'a') as handle:",
            "        handle.write('ran\\n')",
            "",
            "",
            "class SaveTest(unittest.TestCase):",
            "    def test_save(self):",
            "        test_save()", ""])
        self.write("tests/test_saving.py", test)
        self.write("gate/test_save_and_load.py", test)

    def maps(self):
        parts = foundations_part("foundations/**\n  coverage/**\n  gate/**")
        return [part_map(part(), flow(coverage="coverage/save-and-load.info"), surface(), parts),
                part_map(part(), flow(), surface(), parts),
                part_map(part(), flow(coverage="coverage/missing.info"), surface(), parts)]

    def watchers(self, started):
        """Patches that note every start of a program or of a test run in `started`."""
        real = subprocess.Popen

        def popen(arguments, *rest, **options):
            started.append(list(arguments) if not isinstance(arguments, str) else [arguments])
            return real(arguments, *rest, **options)

        def noted(name, result=None):
            def call(*arguments, **options):
                started.append([name] + [str(item) for item in arguments])
                return result
            return call

        def in_process(name, real_method):
            def call(*arguments, **options):
                started.append([name])
                return real_method(*arguments, **options)
            return call

        patches = [unittest.mock.patch.object(subprocess, "Popen", popen),
                   unittest.mock.patch.object(os, "system", noted("os.system", 0))]
        for name in dir(os):
            if name.startswith(("spawn", "exec", "posix_spawn", "startfile", "fork")) and \
                    callable(getattr(os, name)):
                patches.append(unittest.mock.patch.object(os, name, noted("os." + name)))
        for owner, name in ((unittest.TestSuite, "run"), (unittest.TestCase, "run"),
                            (unittest.TestLoader, "discover"),
                            (unittest.TestLoader, "loadTestsFromName"),
                            (unittest.TestLoader, "loadTestsFromNames"),
                            (unittest.TestLoader, "loadTestsFromModule"),
                            (unittest.TestLoader, "loadTestsFromTestCase"),
                            (unittest.TextTestRunner, "run")):
            patches.append(unittest.mock.patch.object(
                owner, name, in_process("unittest.%s.%s" % (owner.__name__, name),
                                        getattr(owner, name))))
        return patches

    def test_the_guard_starts_no_program_but_git(self):
        # invariant: map-guard-test-runs/1
        maps = self.maps()
        self.guard(maps[0])
        self.commit()
        started = []
        codes = []
        with contextlib.ExitStack() as stack:
            for patch in self.watchers(started):
                stack.enter_context(patch)
            codes.append(format_guard.run(self.path, base="main", stream=io.StringIO(),
                                          record=self.record_path))
            for text in maps:
                with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(text)
                codes.append(format_guard.run(self.path, stream=io.StringIO(), own=True,
                                              examples=os.path.join(self.root, "no-examples.md")))
        self.assertEqual(codes[0], 0)
        self.assertFalse(os.path.exists(self.marker), "the flow's test ran during a guard run")
        self.assertTrue(started)
        self.assertEqual({arguments[0] for arguments in started}, {"git"}, started)
        self.assertEqual([arguments for arguments in started
                          if arguments[1] not in ("rev-parse", "ls-files", "-c", "show",
                                                  "ls-tree")], [], started)


class OwnMap(unittest.TestCase):
    """The-way's own map holds its entries in the form of the template."""

    def test_the_way_map_holds_no_error(self):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            record = os.path.join(directory, "part-map.jsonl")
            code = format_guard.run(format_guard.OWN_MAP, stream=output, record=record)
            with open(record, encoding="utf-8") as handle:
                lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(code, 0, output.getvalue())
        self.assertEqual(sorted({item["invariant"] for item in lines if item["invariant"]}),
                         sorted(RecordPerCommand.MAP_ALONE + ["map-example-target/1"]))
        self.assertEqual([item for item in lines if item["verdict"] == "fail"], [])


if __name__ == "__main__":
    unittest.main()
