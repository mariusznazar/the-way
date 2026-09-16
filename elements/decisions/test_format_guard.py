"""Tests of the format guard: every check fires on a log broken on purpose.

Run from anywhere: python -B -m unittest discover -s <the-way>/elements/decisions -p "test_*.py"
"""

import datetime
import io
import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402
from fingerprint import fingerprint  # noqa: E402

TODAY = datetime.date(2026, 9, 17)
BINDING = "The product keeps every saved game after a reload."


def version(number, ver=1, binding=BINDING, change=None, relations="none", outranks="none",
            review_when="none", approved="Anna, 2026-09-01", rationale=None, omit=()):
    change = change or ("new decision" if ver == 1 else
                        "field change · previous: ABC-%02d/%d" % (number, ver - 1))
    rationale = rationale or ("Rationale" if ver == 1 else "Rationale for change")
    fields = [("Change", change), ("Scope", "saving"), ("Based on", "none"),
              ("Relations", relations), ("Outranks", outranks),
              ("Verification", "level 2 — an agent compares the change with the decision:\n"
                               "  - complies: a reload keeps the game;\n"
                               "  - violates: a reload loses the game."),
              ("Review when", review_when), ("Origin", "none"), ("Approver override", "none"),
              ("Approved by", approved)]
    lines = ["### ABC-%02d/%d — Is a saved game kept?" % (number, ver), ""]
    if binding is not None:
        lines += [binding, ""]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    lines += [""]
    lines += ["*%s:* %s" % (name, value) for name, value in
              ((rationale, "players lose trust."), ("Rejected", "none considered"),
               ("Consequences", "saving needs a test.")) if name not in omit]
    return "\n".join(lines)


def review(number, date, result, next_check):
    return "\n".join(["### ABC-%02d · review %s" % (number, date), "",
                      "- **Result:** %s" % result, "- **Next check:** %s" % next_check,
                      "- **Checked by:** Anna"])


def log(*entries):
    return "# Decision log\n\nIntro.\n\n" + "\n\n".join(entries) + "\n"


class GuardTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.directory.name, "decisions.md")

    def tearDown(self):
        self.directory.cleanup()

    def guard(self, text, base=None):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        output = io.StringIO()
        code = format_guard.run(self.path, base=base, today=TODAY, stream=output)
        return code, output.getvalue()

    def assertPasses(self, text):
        code, output = self.guard(text)
        self.assertEqual(code, 0, output)
        self.assertIn("0 error(s), 0 warning(s)", output)

    def assertFails(self, text, fragment):
        code, output = self.guard(text)
        self.assertEqual(code, 1, output)
        self.assertIn(fragment, output)


class Headings(GuardTestCase):
    def test_valid_log_with_another_prefix_passes(self):
        self.assertPasses(log(version(1), version(2)))

    def test_malformed_heading(self):
        self.assertFails(log(version(1).replace("ABC-01/1 —", "ABC-01 —")), "heading is neither")

    def test_versions_not_consecutive(self):
        self.assertFails(log(version(1), version(1, ver=3, change="field change · previous: ABC-01/2")),
                         "version 3 where version 2 is next")


class Fields(GuardTestCase):
    def test_missing_field(self):
        self.assertFails(log(version(1, omit=("Origin",))), "field *Origin* is missing")

    def test_missing_prose_field(self):
        self.assertFails(log(version(1, omit=("Rejected",))), "field *Rejected* is missing")

    def test_todo_is_a_warning(self):
        code, output = self.guard(log(version(1).replace("**Origin:** none", "**Origin:** TODO — find it")))
        self.assertEqual(code, 0, output)
        self.assertIn("warning: *Origin* is `TODO`", output)

    def test_todo_in_approved_by_is_an_error(self):
        self.assertFails(log(version(1, approved="TODO")), "*Approved by* is `TODO`")

    def test_approved_by_without_date(self):
        self.assertFails(log(version(1, approved="Anna")), "*Approved by* is not")

    def test_rationale_for_change_in_later_versions(self):
        self.assertFails(log(version(1), version(1, ver=2, rationale="Rationale")),
                         "field *Rationale for change* is missing")


class BindingSentences(GuardTestCase):
    def test_four_sentences(self):
        self.assertFails(log(version(1, binding="A is B. C is D. E is F. G is H.")),
                         "4 binding sentences")

    def test_should(self):
        self.assertFails(log(version(1, binding="The product should keep a game.")), "*should*")

    def test_will(self):
        self.assertFails(log(version(1, binding="The product will keep a game.")), "*will*")

    def test_rfc_keyword_in_capitals(self):
        self.assertFails(log(version(1, binding="The product MUST keep a game.")), "use MUST")

    def test_other_capitals_and_lower_case_must_pass(self):
        self.assertPasses(log(version(1, binding="A CI check must reject a lost game.")))

    def test_words_in_code_are_ignored(self):
        self.assertPasses(log(version(1, binding="The `SHOULD` file is kept. `README.md` stays.")))


class Changes(GuardTestCase):
    def test_first_version_is_a_new_decision(self):
        self.assertFails(log(version(1, change="field change · previous: ABC-01/0")),
                         "is not `new decision`")

    def test_unknown_kind(self):
        self.assertFails(log(version(1), version(1, ver=2, change="tweak · previous: ABC-01/1")),
                         "`tweak` is not a kind of change")

    def test_previous_points_to_the_version_before(self):
        self.assertFails(log(version(1), version(2),
                             version(1, ver=2, change="field change · previous: ABC-02/1")),
                         "`previous:` names ABC-02/1 instead of ABC-01/1")

    def test_field_change_keeps_binding_sentences(self):
        self.assertFails(log(version(1), version(1, ver=2, binding="Another rule holds.")),
                         "a field change keeps the binding sentences")

    def test_rewrapped_binding_sentences_are_identical(self):
        self.assertPasses(log(version(1), version(1, ver=2, binding=BINDING.replace(" after ", "\nafter "))))

    def test_editorial_correction_may_change_them(self):
        self.assertPasses(log(version(1), version(
            1, ver=2, binding="The product keeps every saved game after reload.",
            change="editorial correction · previous: ABC-01/1")))

    def test_repeal_has_no_binding_sentences(self):
        self.assertFails(log(version(1), version(1, ver=2, change="repeal · previous: ABC-01/1")),
                         "a repeal has no binding sentences")
        self.assertPasses(log(version(1), version(1, ver=2, binding=None,
                                                  change="repeal · previous: ABC-01/1")))

    def test_binding_sentences_missing(self):
        self.assertFails(log(version(1, binding=None)), "binding sentences are missing")


class Relations(GuardTestCase):
    def test_numbers_exist(self):
        self.assertFails(log(version(1, relations="related to ABC-07")), "names ABC-07")
        self.assertFails(log(version(1, outranks="ABC-07")), "names ABC-07")

    def test_unknown_relation_type(self):
        self.assertFails(log(version(1), version(2, relations="supersedes ABC-01")),
                         "is not of a known type")

    def test_derives_from_needs_a_fingerprint(self):
        self.assertFails(log(version(1), version(2, relations="derives from ABC-01")),
                         "carries no fingerprint")

    def test_related_to_has_none(self):
        self.assertFails(log(version(1), version(2, relations="related to ABC-01@%s" % fingerprint(BINDING))),
                         "carries a fingerprint")

    def test_current_fingerprint_passes(self):
        self.assertPasses(log(version(1), version(2, relations="narrows ABC-01@%s" % fingerprint(BINDING))))

    def test_stale_fingerprint(self):
        self.assertFails(log(version(1), version(2, relations="derives from ABC-01@00000000")),
                         "the current fingerprint of ABC-01 is %s" % fingerprint(BINDING))

    def test_old_version_keeps_its_old_fingerprint(self):
        changed = "The product keeps every saved game after any reload."
        self.assertPasses(log(
            version(1), version(2, relations="derives from ABC-01@%s" % fingerprint(BINDING)),
            version(1, ver=2, binding=changed, change="new wording · previous: ABC-01/1"),
            version(2, ver=2, relations="derives from ABC-01@%s" % fingerprint(changed))))

    def test_mutual_outranks(self):
        self.assertFails(log(version(1, outranks="ABC-02"), version(2, outranks="ABC-01")),
                         "ABC-01 and ABC-02 outrank each other")


class Reviews(GuardTestCase):
    DUE = "saves move to a server · check by: 2026-09-01"

    def test_passed_date_without_review_warns(self):
        code, output = self.guard(log(version(1, review_when=self.DUE)))
        self.assertEqual(code, 0, output)
        self.assertIn("check-by date 2026-09-01 has passed without a review", output)

    def test_review_moves_the_date(self):
        self.assertPasses(log(version(1, review_when=self.DUE),
                              review(1, "2026-09-01", "condition not met — saves stay local",
                                     "2026-10-01")))

    def test_review_that_passed_again_warns(self):
        code, output = self.guard(log(version(1, review_when=self.DUE),
                                      review(1, "2026-09-01", "condition not met — local", "2026-09-10")))
        self.assertIn("check-by date 2026-09-10 has passed", output)

    def test_not_met_needs_a_date(self):
        self.assertFails(log(version(1, review_when=self.DUE),
                             review(1, "2026-09-01", "condition not met — local", "none")),
                         "needs a date in *Next check*")

    def test_changed_in_needs_the_version(self):
        self.assertFails(log(version(1, review_when=self.DUE),
                             review(1, "2026-09-01", "condition met — changed in ABC-01/2", "none")),
                         "names a version that does not exist")

    def test_unknown_result(self):
        self.assertFails(log(version(1), review(1, "2026-09-01", "looked at it", "none")),
                         "has none of the forms")

    def test_malformed_review_when(self):
        self.assertFails(log(version(1, review_when="next year")), "*Review when* is not")


class Examples(GuardTestCase):
    def test_example_differs(self):
        text = log(version(1))
        self.guard(text)
        entries = format_guard.parse_log(text, "ABC")
        examples = os.path.join(self.directory.name, "examples.md")
        with open(examples, "w", encoding="utf-8") as handle:
            handle.write("# Examples\n\n## New decision\n\n" + version(1).replace("Anna", "Ben") + "\n")
        report = format_guard.Report(self.path)
        format_guard.check_examples(entries, examples, report)
        self.assertTrue(any("differs from the log" in m for _, m in report.errors), report.errors)


class AgainstBase(GuardTestCase):
    def setUp(self):
        super().setUp()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "guard@example.com")
        self.git("config", "user.name", "Guard")

    def git(self, *arguments):
        subprocess.run(["git"] + list(arguments), cwd=self.directory.name, check=True,
                       capture_output=True)

    def commit(self, text):
        self.guard(text)
        self.git("add", "decisions.md")
        self.git("commit", "-q", "-m", "log")

    def test_appending_passes(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1), version(2)), base="main")
        self.assertEqual(code, 0, output)

    def test_editing_an_entry_on_the_main_branch(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1, approved="Anna, 2026-09-02")), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("only grows at the end", output)

    def test_two_versions_in_one_merge(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1), version(1, ver=2), version(1, ver=3,
                                  change="field change · previous: ABC-01/2")), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("2 versions added against main", output)

    def test_missing_base(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1)), base="origin/main")
        self.assertEqual(code, 1, output)
        self.assertIn("does not exist", output)

    def test_base_without_the_log(self):
        with open(os.path.join(self.directory.name, "other.txt"), "w") as handle:
            handle.write("x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")
        code, output = self.guard(log(version(1)), base="main")
        self.assertEqual(code, 0, output)
        self.assertIn("compared with an empty one", output)


class OwnLog(unittest.TestCase):
    def test_the_way_log_passes(self):
        output = io.StringIO()
        code = format_guard.run(format_guard.OWN_LOG, stream=output)
        self.assertEqual(code, 0, output.getvalue())


if __name__ == "__main__":
    unittest.main()
