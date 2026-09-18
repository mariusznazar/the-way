"""Tests of the part map guard: every check fires on a map broken on purpose.

Run from anywhere: python -B -m unittest discover -s <the-way>/elements/part-map -p "test_*.py"
"""

import io
import os
import subprocess
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402


def part(identifier="saving", title="Saving a game", responsibility=None,
         files=("src/saving.py", "tests/**"),
         depends="none", failure_modes=("a save is lost — the player loses the game — high — "
                                        "detected by INV-2",),
         boundary="none", omit=()):
    if responsibility is None:
        responsibility = "The part answers for writing and reading a saved game."
    lines = ["## %s — %s" % (identifier, title), "", responsibility, ""]
    if not isinstance(files, str):
        files = "\n  ".join(files)
    fields = [("Files", files), ("Depends on", depends),
              ("Failure modes", "\n" + "\n".join("  - %s" % mode for mode in failure_modes)),
              ("Trust boundary", boundary)]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def flow(identifier="save-and-load", title="Save and load", description=None, criticality="high",
         parts="saving", invariant="INV-2 — test: tests/test_saving.py", coverage="none", omit=()):
    if description is None:
        description = "The player saves a game and loads it back after a restart."
    lines = ["## %s — %s" % (identifier, title), "", description, ""]
    fields = [("Criticality", criticality), ("Parts", parts), ("Invariant", invariant),
              ("Coverage", coverage)]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    return "\n".join(lines)


def surface(identifier="save-format", title="The format of a saved game", promise=None,
            declared="src/saving.py · SaveFile", omit=()):
    if promise is None:
        promise = "The product reads back every saved game written by an earlier version."
    lines = ["## %s — %s" % (identifier, title), "", promise, ""]
    lines += [("- **Declared at:** %s" % declared)] if "Declared at" not in omit else []
    return "\n".join(lines)


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

WITHDRAWN = "\n".join(["## Withdrawn identifiers", "", "| Identifier | Successors |", "|---|---|",
                       "| game-state | saving |"])


def part_map(*entries, **lists):
    sections = list(entries) or [part(), flow(), surface(),
                                 part("foundations", "The foundation", files="foundations/**",
                                      responsibility="The part answers for what binds the product.",
                                      failure_modes=("a rule read wrong — work goes the light "
                                                     "path — low — not detected",))]
    tail = [lists.get("scale", SCALE), lists.get("context", CONTEXT), lists.get("paths", PATHS),
            lists.get("left_out", LEFT_OUT), lists.get("withdrawn", WITHDRAWN)]
    return "# Part map\n\nWhat the product is made of.\n\n" + \
        "\n\n".join(sections + [section for section in tail if section]) + "\n"


FILES = {"src/saving.py": "def save():\n    pass\n",
         "tests/test_saving.py": "# save-and-load\ndef test_save():\n    pass\n",
         "README.md": "# Product\n"}


class GuardTestCase(unittest.TestCase):
    files = FILES

    def setUp(self):
        self.directory = __import__("tempfile").TemporaryDirectory()
        self.root = self.directory.name
        self.path = os.path.join(self.root, "foundations", "part_map.md")
        os.makedirs(os.path.join(self.root, "foundations"))
        for name, content in self.files.items():
            full = os.path.join(self.root, name.replace("/", os.sep))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "guard@example.com")
        self.git("config", "user.name", "Guard")

    def tearDown(self):
        self.directory.cleanup()

    def git(self, *arguments):
        subprocess.run(["git"] + list(arguments), cwd=self.root, check=True, capture_output=True)

    def guard(self, text, base=None):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(self.path, base=base, stream=output)
        return code, output.getvalue()

    def assertPasses(self, text):
        code, output = self.guard(text)
        self.assertEqual(code, 0, output)
        self.assertIn("0 error(s), 0 warning(s)", output)

    def assertFails(self, text, fragment):
        code, output = self.guard(text)
        self.assertEqual(code, 1, output)
        self.assertIn(fragment, output)


class ValidMap(GuardTestCase):
    def test_valid_map_passes(self):
        self.assertPasses(part_map())


class Entries(GuardTestCase):
    def test_entry_of_no_known_kind(self):
        strange = "\n".join(["## ghost — A ghost", "", "The part answers for nothing.", "",
                             "- **Notes:** none"])
        self.assertFails(part_map(part(), strange), "is neither a part, a critical flow nor a "
                                                    "surface")

    def test_two_entries_with_one_identifier(self):
        self.assertFails(part_map(part(), part(title="Saving again", files="tests/**")),
                         "identifier `saving` is used twice")

    def test_identifier_with_capitals(self):
        self.assertFails(part_map(part(identifier="Saving")), "`Saving` is not an identifier of "
                                                              "words in lower case")

    def test_missing_field(self):
        self.assertFails(part_map(part(omit=("Trust boundary",))),
                         "field *Trust boundary* is missing")

    def test_missing_binding_sentence(self):
        self.assertFails(part_map(part(responsibility="")), "binding sentence is missing")

    def test_entry_reuses_a_withdrawn_identifier(self):
        self.assertFails(part_map(part(identifier="game-state")),
                         "`game-state` is withdrawn")

    def test_flow_names_a_part_that_does_not_exist(self):
        self.assertFails(part_map(part(), flow(parts="saving · rendering")),
                         "*Parts* names `rendering`, which is not in the map")

    def test_dependency_on_a_part_that_does_not_exist(self):
        self.assertFails(part_map(part(depends="rendering")),
                         "*Depends on* names `rendering`, which is not in the map")


class Files(GuardTestCase):
    files = dict(FILES, **{"src/render.py": "def draw():\n    pass\n"})

    def test_file_no_pattern_claims(self):
        self.assertFails(part_map(), "no part claims `src/render.py`")

    def test_file_claimed_by_two_parts(self):
        both = part("rendering", "Rendering", files="src/**",
                    responsibility="The part answers for drawing the board.",
                    failure_modes=("nothing is drawn — the player is stuck — high — "
                                   "not detected",))
        self.assertFails(part_map(part(), flow(), surface(), both,
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "`src/saving.py` is claimed by `saving` and `rendering`")

    def test_pattern_that_matches_nothing(self):
        self.assertFails(part_map(part(files=("src/saving.py", "tests/**", "src/audio/**")),
                                  part("rendering", "Rendering", files="src/render.py",
                                       responsibility="The part answers for drawing.",
                                       failure_modes=("nothing is drawn — the player is stuck — "
                                                      "high — not detected",)),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "pattern `src/audio/**` of `saving` matches no file git tracks")

    def test_left_out_file_that_a_part_also_claims(self):
        left_out = "\n".join(["## Files left out on purpose", "", "| File | Why |", "|---|---|",
                              "| README.md | the entry point of the repository |",
                              "| src/render.py | drawn by hand |"])
        self.assertFails(part_map(part(), flow(), surface(),
                                  part("rendering", "Rendering", files="src/render.py",
                                       responsibility="The part answers for drawing.",
                                       failure_modes=("nothing is drawn — the player is stuck — "
                                                      "high — not detected",)),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",)),
                                  left_out=left_out),
                         "`src/render.py` is left out on purpose and claimed by `rendering`")

    def test_trust_boundary_pattern_that_matches_nothing(self):
        self.assertFails(part_map(part(boundary="src/parser.py"),
                                  part("rendering", "Rendering", files="src/render.py",
                                       responsibility="The part answers for drawing.",
                                       failure_modes=("nothing is drawn — the player is stuck — "
                                                      "high — not detected",)),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "trust boundary `src/parser.py` of `saving` matches no file git tracks")


class Flows(GuardTestCase):
    files = dict(FILES, **{"src/render.py": "def draw():\n    pass\n",
                           "coverage/save-and-load.info": "SF:src/saving.py\nDA:1,1\nend_of_record\n"})

    def rendering(self):
        return part("rendering", "Rendering", files="src/render.py",
                    responsibility="The part answers for drawing the board.",
                    failure_modes=("nothing is drawn — the player is stuck — high — "
                                   "not detected",))

    def foundations(self):
        return part("foundations", "The foundation", files=("foundations/**", "coverage/**"),
                    responsibility="The part answers for what binds the product.",
                    failure_modes=("a rule read wrong — work goes the light path — low — "
                                   "not detected",))

    def map_with(self, the_flow):
        return part_map(part(), the_flow, surface(), self.rendering(), self.foundations())

    def test_invariant_without_a_test(self):
        self.assertFails(self.map_with(flow(invariant="INV-2")),
                         "*Invariant* names no test of the flow")

    def test_test_that_does_not_exist(self):
        self.assertFails(self.map_with(flow(invariant="INV-2 — test: tests/test_missing.py")),
                         "test `tests/test_missing.py` of `save-and-load` does not exist")

    def test_test_that_does_not_name_the_flow(self):
        self.assertFails(self.map_with(flow(identifier="load-and-save",
                                            invariant="INV-2 — test: tests/test_saving.py")),
                         "test `tests/test_saving.py` does not name `load-and-save`")

    def test_flow_without_coverage_is_reported_unchecked(self):
        code, output = self.guard(self.map_with(flow()))
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the list of parts of `save-and-load`", output)

    def test_coverage_names_a_part_outside_the_list(self):
        covers_both = "SF:src/saving.py\nDA:1,1\nend_of_record\nSF:src/render.py\nDA:1,1\n" \
                      "end_of_record\n"
        path = os.path.join(self.root, "coverage", "save-and-load.info")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(covers_both)
        self.assertFails(self.map_with(flow(coverage="coverage/save-and-load.info")),
                         "coverage of `save-and-load` runs through `rendering`, which is not in "
                         "its list of parts")

    def test_coverage_inside_the_list_passes(self):
        self.assertPasses(self.map_with(flow(coverage="coverage/save-and-load.info")))


class Surfaces(GuardTestCase):
    def test_declaration_that_does_not_exist(self):
        self.assertFails(part_map(part(), flow(), surface(declared="src/missing.py · SaveFile"),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "declaration `src/missing.py` of `save-format` does not exist")

    def test_promise_level_written_in_the_map(self):
        self.assertFails(part_map(part(), flow(), surface(declared="src/saving.py · SaveFile · "
                                                                   "stable"),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "the promise level `stable` belongs at the declaration, not in the map")

    def test_withdrawal_date_written_in_the_map(self):
        self.assertFails(part_map(part(), flow(),
                                  surface(declared="src/saving.py · SaveFile · withdrawn "
                                                   "2027-01-01"),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "a withdrawal date belongs at the declaration, not in the map")

    def test_surface_that_cannot_be_marked_needs_a_test_that_exists(self):
        self.assertFails(part_map(part(), flow(),
                                  surface(declared="not markable — test: tests/test_missing.py"),
                                  part("foundations", "The foundation", files="foundations/**",
                                       responsibility="The part answers for what binds.",
                                       failure_modes=("a rule read wrong — work goes the light "
                                                      "path — low — not detected",))),
                         "test `tests/test_missing.py` of `save-format` does not exist")

    def test_promise_levels_are_reported_unchecked(self):
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the change path of every promise level in use", output)


class ExternalContext(GuardTestCase):
    def row(self, cells):
        return "\n".join(["## External context", "",
                          "| Partner | Direction | What comes in | Updates with the product |",
                          "|---|---|---|---|", "| %s |" % " | ".join(cells)])

    def test_direction_outside_the_template(self):
        self.assertFails(part_map(context=self.row(["the player's browser", "sideways",
                                                    "untrusted", "no"])),
                         "`sideways` is not one of `them → us`, `us → them`, `both`")

    def test_trust_outside_the_template(self):
        self.assertFails(part_map(context=self.row(["the player's browser", "both", "maybe",
                                                    "no"])),
                         "`maybe` is not one of `trusted`, `untrusted`, `—`")

    def test_missing_column(self):
        self.assertFails(part_map(context=self.row(["the player's browser", "both", "untrusted"])),
                         "records no *Updates with the product*")


class Scopes(GuardTestCase):
    def decisions(self, scope):
        path = os.path.join(self.root, "foundations", "decisions.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("# Decision log\n\n### WAY-01/1 — A question?\n\nA sentence.\n\n"
                         "- **Scope:** %s\n" % scope)

    def test_scope_names_a_part_that_does_not_exist(self):
        self.decisions("saving, rendering")
        self.assertFails(part_map(), "the scope of WAY-01/1 names `rendering`, which is not in "
                                     "the map")

    def test_scope_names_a_withdrawn_part(self):
        self.decisions("game-state")
        self.assertFails(part_map(), "the scope of WAY-01/1 names `game-state`, which is "
                                     "withdrawn")

    def test_scope_of_parts_in_the_map_passes(self):
        self.decisions("saving, foundations")
        self.assertPasses(part_map())


class KnownViolations(GuardTestCase):
    def violations(self, *lines):
        path = os.path.join(self.root, "foundations", "known_violations.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(["# Known violations", "", "## Known violations", "",
                                    "| Source | Target | File | What it reaches for |",
                                    "|---|---|---|---|"] + list(lines)) + "\n")

    def test_position_naming_a_part_outside_the_map(self):
        self.violations("| saving | rendering | src/saving.py | the drawing of a board |")
        self.assertFails(part_map(), "known violation names `rendering`, which is not in the map")

    def test_position_with_a_line_number(self):
        self.violations("| saving | foundations | src/saving.py:12 | the log of decisions |")
        self.assertFails(part_map(), "known violation names a line number")

    def test_new_and_stale_violations_are_reported_unchecked(self):
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the dependencies between parts", output)

    def test_dependencies_are_reported_unchecked_without_a_list_of_violations(self):
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the dependencies between parts", output)

    def test_a_position_added_against_the_main_branch(self):
        self.violations()
        self.guard(part_map())
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "map")
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("is not on the list of main", output)

    def test_a_position_kept_from_the_main_branch_passes(self):
        self.violations("| saving | foundations | src/saving.py | the log of decisions |")
        self.guard(part_map())
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "map")
        code, output = self.guard(part_map(), base="main")
        self.assertEqual(code, 0, output)


class Criticality(GuardTestCase):
    def test_degree_outside_the_scale(self):
        self.assertFails(part_map(part(), flow(criticality="fatal")),
                         "`fatal` is not on the criticality scale")

    def test_failure_mode_with_a_degree_outside_the_scale(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — the game is lost — "
                                                      "fatal — not detected",))),
                         "`fatal` is not on the criticality scale")

    def test_criticality_written_at_a_part(self):
        written = part() + "\n- **Criticality:** high"
        self.assertFails(part_map(written), "carries the fields of a part and of a critical flow")

    def test_failure_mode_without_detection(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — the game is lost — high",))),
                         "names neither a detecting invariant nor `not detected`")

    def test_failure_mode_wrapped_over_two_lines(self):
        wrapped = part(failure_modes=("a save is lost — the player loses the game — high —\n"
                                      "    detected by INV-2",))
        foundations = part("foundations", "The foundation", files="foundations/**",
                           responsibility="The part answers for what binds.",
                           failure_modes=("a rule read wrong — work goes the light path — low — "
                                          "not detected",))
        self.assertPasses(part_map(wrapped, flow(), surface(), foundations))

    def test_failure_mode_without_severity(self):
        self.assertFails(part_map(part(failure_modes=("a save is lost — not detected",))),
                         "is not `<what fails> — <damage> — <severity> — <detection>`")


class Reported(GuardTestCase):
    files = dict(FILES, **{"src/storage.py": "def write():\n    pass\n"})

    def test_dependency_from_higher_to_lower_is_reported(self):
        storage = part("storage", "Storage", files="src/storage.py",
                       responsibility="The part answers for the disk.",
                       failure_modes=("a write fails — a step is repeated — low — not detected",))
        foundations = part("foundations", "The foundation", files="foundations/**",
                           responsibility="The part answers for what binds.",
                           failure_modes=("a rule read wrong — work goes the light path — low — "
                                          "not detected",))
        code, output = self.guard(part_map(part(depends="storage"), flow(), surface(), storage,
                                           foundations))
        self.assertEqual(code, 0, output)
        self.assertIn("so storage is computed as `high`, above its own failure modes", output)

    def test_a_degree_outside_the_scale_at_a_part_something_depends_on(self):
        storage = part("storage", "Storage", files="src/storage.py",
                       responsibility="The part answers for the disk.",
                       failure_modes=("a write fails — a step is repeated — fatal — "
                                      "not detected",))
        foundations = part("foundations", "The foundation", files="foundations/**",
                           responsibility="The part answers for what binds.",
                           failure_modes=("a rule read wrong — work goes the light path — low — "
                                          "not detected",))
        self.assertFails(part_map(part(depends="storage"), flow(), surface(), storage,
                                  foundations),
                         "`fatal` is not on the criticality scale")

    def test_a_map_outside_a_git_repository_is_reported_unchecked(self):
        import shutil
        shutil.rmtree(os.path.join(self.root, ".git"))
        code, output = self.guard(part_map())
        self.assertEqual(code, 0, output)
        self.assertIn("unchecked: the assignment of files to parts", output)

    def guard(self, text, base=None):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        if os.path.exists(os.path.join(self.root, ".git")):
            self.git("add", "-A")
        output = io.StringIO()
        code = format_guard.run(self.path, base=base, stream=output)
        return code, output.getvalue()


class Examples(GuardTestCase):
    def examples(self, *blocks):
        path = os.path.join(self.root, "examples.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("# Examples\n\nCopies.\n\n" + "\n\n".join(blocks) + "\n")
        return path

    def report_on(self, text, examples_path):
        rules = format_guard.read_rules()
        entries, _ = format_guard.parse_map(text, rules)
        report = format_guard.Report(self.path)
        format_guard.check_examples(entries, examples_path, report)
        return report

    def test_example_that_differs_from_its_entry(self):
        text = part_map()
        changed = part().replace("writing and reading a saved game", "drawing a board")
        report = self.report_on(text, self.examples("*A part:*", changed))
        self.assertTrue(any("differs from the map" in message for _, message in report.errors),
                        report.errors)

    def test_example_of_an_entry_outside_the_map(self):
        text = part_map()
        stranger = part("rendering", "Rendering", files="src/render.py",
                        responsibility="The part answers for drawing.")
        report = self.report_on(text, self.examples("*A part:*", stranger))
        self.assertTrue(any("is not in the map" in message for _, message in report.errors),
                        report.errors)

    def test_caption_of_the_next_example_does_not_count_as_a_difference(self):
        text = part_map()
        blocks = text.split("\n\n## ")
        first, second = "## " + blocks[1].rstrip(), "## " + blocks[2].rstrip()
        report = self.report_on(text, self.examples("*A part:*", first, "*A flow:*", second))
        self.assertEqual(report.errors, [])

    def test_example_copied_word_for_word_passes(self):
        text = part_map()
        copy = "\n".join(text.split("\n\n## ")[1].split("\n")).rstrip()
        report = self.report_on(text, self.examples("*A part:*", "## " + copy))
        self.assertEqual(report.errors, [])


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
        text = part_map(part(), part("storage", "Storage", files="src/storage.py",
                                     responsibility="The part answers for the disk.",
                                     failure_modes=("a write fails — a step is repeated — low — "
                                                    "not detected",)),
                        part("saving2", "Saving again", files="src/other.py", depends="storage",
                             responsibility="The part answers for saving elsewhere.",
                             failure_modes=("a save is lost — the game is lost — high — "
                                            "not detected",)))
        self.assertEqual(self.compute(text)["storage"], "high")

    def test_a_separation_stops_the_inheritance(self):
        text = part_map(part("storage", "Storage", files="src/storage.py",
                             responsibility="The part answers for the disk.",
                             failure_modes=("a write fails — a step is repeated — low — "
                                            "not detected",)),
                        part("saving2", "Saving again", files="src/other.py",
                             depends="storage (separated — a failed write leaves the game intact)",
                             responsibility="The part answers for saving elsewhere.",
                             failure_modes=("a save is lost — the game is lost — high — "
                                            "not detected",)))
        self.assertEqual(self.compute(text)["storage"], "low")

    def test_a_part_without_failure_modes_is_the_highest_degree(self):
        text = part_map(part(failure_modes=()))
        self.assertEqual(self.compute(text)["saving"], "high")

    def test_a_part_takes_the_degree_of_a_flow_it_lies_on(self):
        text = part_map(part(failure_modes=("a save is lost — a step is repeated — low — "
                                            "not detected",)),
                        flow(criticality="high", parts="saving"))
        self.assertEqual(self.compute(text)["saving"], "high")


class OwnMap(unittest.TestCase):
    def test_the_way_map_passes(self):
        output = io.StringIO()
        code = format_guard.run(format_guard.OWN_MAP, stream=output)
        self.assertEqual(code, 0, output.getvalue())


if __name__ == "__main__":
    unittest.main()
