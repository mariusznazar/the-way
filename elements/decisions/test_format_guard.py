"""Tests of the format guard: every check fires on a log broken on purpose.

Run from the root of the-way:
    python -B gate/run_tests.py elements/decisions --record .runs/decisions-tests.jsonl
"""

import contextlib
import datetime
import inspect
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import unittest.mock

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import format_guard  # noqa: E402

TODAY = datetime.date(2026, 9, 17)
BINDING = "The product keeps every saved game after a reload."
# The fingerprint of BINDING, and of CHANGED, written out (WAY-70).
CURRENT = "798975ff"
CHANGED = "The product keeps every saved game after any reload."
CHANGED_FINGERPRINT = "69b731d5"
GUARD = "elements/decisions/format_guard.py"


def version(number, ver=1, binding=BINDING, change=None, relations="none", outranks=None,
            review_when="none", approved="Anna, 2026-09-01", rationale=None, omit=(),
            verification=None, origin="none", override=None):
    """A decision version in the form of the template. `outranks` and `override` add the fields
    *Outranks* and *Approver override*, which the form no longer holds, where a test needs them."""
    change = change or ("new decision" if ver == 1 else "unchanged sentences")
    rationale = rationale or ("Rationale" if ver == 1 else "Rationale for change")
    verification = verification or ("level 2 — an agent compares the change with the decision:\n"
                                    "  - complies: a reload keeps the game;\n"
                                    "  - violates: a reload loses the game.")
    fields = [("Change", change), ("Scope", "saving"), ("Based on", "none"),
              ("Relations", relations), ("Outranks", outranks),
              ("Verification", verification),
              ("Review when", review_when), ("Origin", origin), ("Approver override", override),
              ("Approved by", approved)]
    fields = [(name, value) for name, value in fields if value is not None]
    lines = ["### ABC-%02d/%d — Is a saved game kept?" % (number, ver), ""]
    if binding is not None:
        lines += [binding, ""]
    lines += ["- **%s:** %s" % (name, value) for name, value in fields if name not in omit]
    lines += [""]
    lines += ["*%s:* %s" % (name, value) for name, value in
              ((rationale, "players lose trust."), ("Rejected", "none considered"))
              if name not in omit]
    return "\n".join(lines)


def review(number, date, result, next_check, checked_by="Anna"):
    return "\n".join(["### ABC-%02d · review %s" % (number, date), "",
                      "- **Result:** %s" % result, "- **Next check:** %s" % next_check,
                      "- **Checked by:** %s" % checked_by])


def log(*entries):
    return "# Decision log\n\nIntro.\n\n" + "\n\n".join(entries) + "\n"


def line(function, verdict, invariant, description=None):
    """A line of the record, written out as the test expects it."""
    written = {"check": "%s::%s" % (GUARD, function) if function else GUARD,
               "verdict": verdict, "invariant": invariant}
    if description is not None:
        written["description"] = description
    return written


class GuardTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.directory.name, "decisions.md")
        self.record_path = os.path.join(self.directory.name, ".runs", "decisions.jsonl")
        self.lines = []

    def tearDown(self):
        self.directory.cleanup()

    def guard(self, text, base=None, merge_onto=None, approver=None, today=TODAY):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        output = io.StringIO()
        code = format_guard.run(self.path, base=base, today=today, stream=output,
                                merge_onto=merge_onto, record=self.record_path, approver=approver)
        with open(self.record_path, encoding="utf-8") as handle:
            self.lines = [json.loads(item) for item in handle.read().split("\n") if item]
        return code, output.getvalue()

    def assertPasses(self, text, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 0, output)
        self.assertIn("0 error(s), 0 warning(s)", output)
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])

    def assertFails(self, text, fragment, **options):
        code, output = self.guard(text, **options)
        self.assertEqual(code, 1, output)
        self.assertIn(fragment, output)

    def assertRecords(self, expected):
        self.assertIn(expected, self.lines)


class Headings(GuardTestCase):
    def test_valid_log_with_another_prefix_passes(self):
        self.assertPasses(log(version(1), version(2)))

    def test_malformed_heading(self):
        self.assertFails(log(version(1).replace("ABC-01/1 —", "ABC-01 —")), "heading is neither")
        self.assertRecords(line("check_headings", "fail", "decision-heading-form/1",
                                "line 5: heading is neither `### ABC-NN/V — <question>` nor "
                                "`### ABC-NN · review YYYY-MM-DD`"))

    def test_versions_not_consecutive(self):
        self.assertFails(log(version(1), version(1, ver=3)),
                         "version 3 where version 2 is next")
        self.assertRecords(line("check_headings", "fail", "decision-version-sequence/1",
                                "line 23: ABC-01: version 3 where version 2 is next"))


class HeadingsOffTheForm(GuardTestCase):
    SHAPE = "`### ABC-NN/V — <question>`"

    def test_a_heading_one_level_up(self):
        self.assertFails(log(version(1), version(2).replace("### ABC-02/1", "## ABC-02/1")),
                         "the heading of a decision version is")
        self.assertRecords(line("check_headings", "fail", "decision-heading-form/1",
                                "line 23: the heading of a decision version is `## ABC-02/1 — Is a "
                                "saved game kept?`, not `### ABC-NN/V — <question>`"))
        self.assertNotIn(line("check_headings", "pass", "decision-heading-form/1"), self.lines)

    def test_a_heading_one_level_down(self):
        self.assertFails(log(version(1), version(2).replace("### ABC-02/1", "#### ABC-02/1")),
                         "the heading of a decision version is `#### ABC-02/1")

    def test_the_only_version_under_another_level(self):
        self.assertFails(log(version(1).replace("### ABC-01/1", "## ABC-01/1")),
                         "the heading of a decision version is `## ABC-01/1")

    def test_a_version_with_no_heading(self):
        self.assertFails(log(version(1), version(2).split("\n", 1)[1]),
                         "a decision version stands here with no heading of its own")
        self.assertRecords(line("check_headings", "fail", "decision-heading-form/1",
                                "line 26: a decision version stands here with no heading of its "
                                "own; its heading has the form `### ABC-NN/V — <question>`"))

    def test_a_version_under_a_heading_that_names_no_version(self):
        self.assertFails(log(version(1), version(2).replace("### ABC-02/1 — Is a saved game kept?",
                                                            "## Saving")),
                         "a decision version stands under `## Saving`")
        self.assertRecords(line("check_headings", "fail", "decision-heading-form/1",
                                "line 27: a decision version stands under `## Saving`, not under a "
                                "heading of the form `### ABC-NN/V — <question>`"))

    def test_a_version_under_a_review_heading(self):
        self.assertFails(log(version(1), version(2).replace("### ABC-02/1 — Is a saved game kept?",
                                                            "### ABC-01 · review 2026-09-01")),
                         "a decision version stands under `### ABC-01 · review 2026-09-01`")


class Fields(GuardTestCase):
    def test_missing_field(self):
        self.assertFails(log(version(1, omit=("Origin",))), "field *Origin* is missing")
        self.assertRecords(line("check_fields", "fail", "log-entry-field-presence/1",
                                "line 5: field *Origin* is missing"))

    def test_missing_prose_field(self):
        self.assertFails(log(version(1, omit=("Rejected",))), "field *Rejected* is missing")

    def test_todo_is_a_warning(self):
        code, output = self.guard(log(version(1).replace("**Origin:** none", "**Origin:** TODO — find it")))
        self.assertEqual(code, 0, output)
        self.assertIn("warning: *Origin* is `TODO`", output)
        self.assertRecords(line("check_fields", "pass", "log-entry-field-words/1"))

    def test_todo_in_approved_by_is_an_error(self):
        self.assertFails(log(version(1, approved="TODO")), "*Approved by* is `TODO`")
        self.assertRecords(line("check_fields", "fail", "log-entry-field-words/1",
                                "line 18: *Approved by* is `TODO`"))
        self.assertRecords(line("check_approval", "fail", "decision-approval-record/1",
                                "line 18: *Approved by* is `TODO`"))

    def test_approved_by_without_date(self):
        self.assertFails(log(version(1, approved="Anna")), "*Approved by* is not")
        self.assertRecords(line("check_approval", "fail", "decision-approval-record/1",
                                "line 18: ABC-01/1: *Approved by* is not `<who>, YYYY-MM-DD`"))

    def test_rationale_for_change_in_later_versions(self):
        self.assertFails(log(version(1), version(1, ver=2, rationale="Rationale")),
                         "field *Rationale for change* is missing")
        self.assertRecords(line("check_change_rationale", "fail", "decision-change-rationale/1",
                                "line 23: field *Rationale for change* is missing"))

    def test_todo_rationale_for_change_passes_with_a_warning(self):
        code, output = self.guard(log(version(1), version(1, ver=2).replace(
            "*Rationale for change:* players lose trust.", "*Rationale for change:* TODO — ask Anna")))
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:38: warning: *Rationale for change* is `TODO`", output)
        self.assertRecords(line("check_change_rationale", "pass", "decision-change-rationale/1"))
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])

    def test_none_rationale_for_change_is_an_error(self):
        self.assertFails(log(version(1), version(1, ver=2).replace(
            "*Rationale for change:* players lose trust.", "*Rationale for change:* none")),
            "decisions.md:38: error: *Rationale for change* is `none`")
        self.assertRecords(line("check_fields", "fail", "log-entry-field-words/1",
                                "line 38: *Rationale for change* is `none`"))
        self.assertRecords(line("check_change_rationale", "fail", "decision-change-rationale/1",
                                "line 38: *Rationale for change* is `none`"))


class FieldWords(GuardTestCase):
    def test_none_where_the_template_gives_it_passes(self):
        self.assertPasses(log(version(1).replace("**Scope:** saving", "**Scope:** none")))

    def test_none_in_change(self):
        self.assertFails(log(version(1, change="none")), "*Change* is `none`")
        self.assertRecords(line("check_fields", "fail", "log-entry-field-words/1",
                                "line 9: *Change* is `none`"))

    def test_none_in_approved_by(self):
        self.assertFails(log(version(1, approved="none")), "*Approved by* is `none`")
        self.assertRecords(line("check_fields", "fail", "log-entry-field-words/1",
                                "line 18: *Approved by* is `none`"))

    def test_none_in_a_review_field_the_template_gives_no_none(self):
        self.assertFails(log(version(1), review(1, "2026-09-01", "condition met, decision kept — "
                                                "saves stay local", "none", checked_by="none")),
                         "*Checked by* is `none`")
        self.assertRecords(line("check_fields", "fail", "log-entry-field-words/1",
                                "line 27: *Checked by* is `none`"))

    def test_none_in_next_check_passes(self):
        self.assertPasses(log(version(1), review(1, "2026-09-01", "condition met, decision kept — "
                                                 "saves stay local", "none")))


class BindingSentences(GuardTestCase):
    def test_four_sentences(self):
        self.assertFails(log(version(1, binding="A is B. C is D. E is F. G is H.")),
                         "4 binding sentences")
        self.assertRecords(line("check_bindings", "fail", "binding-sentence-count/1",
                                "line 7: ABC-01/1: 4 binding sentences, at most 3"))

    def test_should(self):
        self.assertFails(log(version(1, binding="The product should keep a game.")), "*should*")
        self.assertRecords(line("check_bindings", "fail", "binding-sentence-words/1",
                                "line 7: ABC-01/1: binding sentences use *should*"))

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
        self.assertFails(log(version(1, change="unchanged sentences")),
                         "is not `new decision`")
        self.assertRecords(line("check_changes", "fail", "decision-change-kind/1",
                                "line 9: ABC-01/1: *Change* of version 1 is not `new decision`"))

    def test_unknown_kind(self):
        self.assertFails(log(version(1), version(1, ver=2, change="tweak")),
                         "`tweak` is not a kind of change")
        self.assertRecords(line("check_changes", "fail", "decision-change-kind/1",
                                "line 27: ABC-01/2: `tweak` is not a kind of change"))

    def test_todo_kind_passes_with_a_warning(self):
        code, output = self.guard(log(version(1), version(1, ver=2, change="TODO — which kind")))
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:27: warning: *Change* is `TODO`", output)
        self.assertRecords(line("check_changes", "pass", "decision-change-kind/1"))
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])

    def test_a_missing_change_names_no_kind(self):
        self.guard(log(version(1), version(1, ver=2, omit=("Change",))))
        self.assertRecords(line("check_changes", "fail", "decision-change-kind/1",
                                "line 23: field *Change* is missing"))

    def test_rewrapped_binding_sentences_are_identical(self):
        self.assertPasses(log(version(1), version(1, ver=2, binding=BINDING.replace(" after ", "\nafter "))))

    def test_editorial_correction_may_change_them(self):
        self.assertPasses(log(version(1), version(
            1, ver=2, binding="The product keeps every saved game after reload.",
            change="editorial correction")))

    def test_repeal_has_no_binding_sentences(self):
        self.assertFails(log(version(1), version(1, ver=2, change="repeal")),
                         "a repeal has no binding sentences")
        self.assertRecords(line("check_bindings", "fail", "repeal-binding-sentences/1",
                                "line 25: ABC-01/2: a repeal has no binding sentences"))
        self.assertPasses(log(version(1), version(1, ver=2, binding=None, change="repeal")))

    def test_binding_sentences_missing(self):
        self.assertFails(log(version(1, binding=None)), "binding sentences are missing")
        self.assertRecords(line("check_bindings", "fail", "binding-sentence-count/1",
                                "line 5: ABC-01/1: binding sentences are missing"))


class Verification(GuardTestCase):
    def test_each_level_passes(self):
        self.assertPasses(log(version(1, verification="level 1 — invariants: saved-game-kept"),
                              version(2, verification="level 3 — Anna assesses the change")))

    def test_no_level(self):
        self.assertFails(log(version(1, verification="none")), "names no level of verification")
        self.assertRecords(line("check_verification", "fail", "decision-verification-level/1",
                                "line 13: ABC-01/1: *Verification* names no level of verification, "
                                "as `level 1 | 2 | 3`"))

    def test_a_level_the_template_does_not_list(self):
        self.assertFails(log(version(1, verification="level 4 — a committee")),
                         "names no level of verification")

    def test_todo_passes_with_a_warning(self):
        code, output = self.guard(log(version(1, verification="TODO — choose a level")))
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:13: warning: *Verification* is `TODO`", output)
        self.assertRecords(line("check_verification", "pass", "decision-verification-level/1"))
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])


class Approver(GuardTestCase):
    def test_the_approver_passes(self):
        self.assertPasses(log(version(1)), approver="Anna")

    def test_another_approver(self):
        self.assertFails(log(version(1)), "*Approved by* names Anna, not Mariusz",
                         approver="Mariusz")
        self.assertRecords(line("check_approver", "fail", "decision-approver/1",
                                "line 18: ABC-01/1: *Approved by* names Anna, not Mariusz"))

    def test_not_checked_outside_the_way_s_own_log(self):
        code, output = self.guard(log(version(1)))
        self.assertIn("note: who approves a version is checked only in the-way's own log", output)
        self.assertNotIn("decision-approver/1", [item["invariant"] for item in self.lines])


class Inherited(GuardTestCase):
    def test_inherited_origin_in_its_form_passes(self):
        self.assertPasses(log(version(1, origin="inherited — searched: the merge requests of "
                                                "saving; found: nothing")))

    def test_inherited_origin_out_of_form(self):
        self.assertFails(log(version(1, origin="inherited from the old loader")),
                         "*Origin* of an inherited decision is not")
        self.assertRecords(line("check_inherited", "fail", "inherited-origin-form/1",
                                "line 17: ABC-01/1: *Origin* of an inherited decision is not "
                                "`inherited — searched: <…>; found: <…>`"))

    def test_inherited_origin_without_what_was_found(self):
        self.assertFails(log(version(1, origin="inherited — searched: the merge requests")),
                         "*Origin* of an inherited decision is not")


class Relations(GuardTestCase):
    def test_numbers_exist(self):
        self.assertFails(log(version(1, relations="derives from ABC-07@" + CURRENT)),
                         "names ABC-07")
        self.assertRecords(line("check_references", "fail", "log-reference-target/1",
                                "line 12: *Relations* names ABC-07, which does not exist"))
        self.assertFails(log(version(1, outranks="ABC-07")), "names ABC-07")

    def test_numbers_in_prose_exist(self):
        self.assertFails(log(version(1).replace("players lose trust.",
                                                "players lose trust, as ABC-09 says.")),
                         "*Rationale* names ABC-09, which does not exist")
        self.assertFails(log(version(1, binding="The product keeps the games ABC-09 names.")),
                         "the text names ABC-09, which does not exist")
        self.assertRecords(line("check_references", "fail", "log-reference-target/1",
                                "line 7: the text names ABC-09, which does not exist"))

    def test_a_version_named_in_prose_need_not_exist(self):
        self.assertPasses(log(version(1).replace("players lose trust.",
                                                 "a later rule would be ABC-01/2.")))

    def test_unknown_relation_type(self):
        self.assertFails(log(version(1), version(2, relations="supersedes ABC-01")),
                         "is not of a known type")
        self.assertRecords(line("check_relations", "fail", "relation-type/1",
                                "line 30: ABC-02/1: relation `supersedes ABC-01` is not of a known "
                                "type"))

    def test_derives_from_needs_a_fingerprint(self):
        self.assertFails(log(version(1), version(2, relations="derives from ABC-01")),
                         "carries no fingerprint")
        self.assertRecords(line("check_relations", "fail", "relation-fingerprint-presence/1",
                                "line 30: ABC-02/1: `derives from ABC-01` carries no fingerprint"))

    def test_current_fingerprint_passes(self):
        self.assertPasses(log(version(1), version(2, relations="narrows ABC-01@" + CURRENT)))

    def test_mutual_outranks(self):
        self.assertFails(log(version(1, outranks="ABC-02"), version(2, outranks="ABC-01")),
                         "ABC-01 and ABC-02 outrank each other")


class Reviews(GuardTestCase):
    DUE = "saves move to a server · check by: 2026-09-01"

    def test_passed_date_without_review_warns(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(version(1, review_when=self.DUE)))
        self.assertEqual(code, 0, output)
        self.assertIn("check-by date 2026-09-01 has passed without a review record", output)

    def test_review_moves_the_date(self):
        self.assertPasses(log(version(1, review_when=self.DUE),
                              review(1, "2026-09-01", "condition not met — saves stay local",
                                     "2026-10-01")))

    def test_review_that_passed_again_warns(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(version(1, review_when=self.DUE),
                                      review(1, "2026-09-01", "condition not met — local",
                                             "2026-09-14")))
        self.assertIn("check-by date 2026-09-14 has passed", output)

    # The dates below have a day above 12, so that no swap of day and month reads them as a date.

    def test_a_date_one_day_before_the_given_date_warns(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(version(1, review_when="saves move to a server · check by: "
                                                             "2026-09-16")))
        self.assertEqual(code, 0, output)
        self.assertIn("ABC-01: check-by date 2026-09-16 has passed without a review record", output)

    def test_the_date_compared_is_the_one_given_not_the_day_of_the_run(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(version(1, review_when="saves move to a server · check by: "
                                                             "2099-01-15")),
                                  today=datetime.date(2099, 6, 1))
        self.assertEqual(code, 0, output)
        self.assertIn("ABC-01: check-by date 2099-01-15 has passed without a review record", output)

    def test_a_review_before_the_version_does_not_answer_its_date(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(
            version(1), review(1, "2026-09-01", "condition not met — local", "2026-12-01"),
            version(1, ver=2, review_when="saves move to a server · check by: 2026-09-15")))
        self.assertIn("ABC-01: check-by date 2026-09-15 has passed without a review record", output)

    def test_a_review_of_another_decision_does_not_answer_its_date(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(
            version(1, review_when="saves move to a server · check by: 2026-09-15"),
            version(2, review_when="saves move to a server · check by: 2026-09-01"),
            review(2, "2026-09-01", "condition not met — local", "2026-12-01")))
        self.assertIn("ABC-01: check-by date 2026-09-15 has passed without a review record", output)

    def test_a_passed_date_after_a_decision_with_none_warns(self):
        """ABC-01 has no check-by date; ABC-02, after it, has one that has passed."""
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(
            version(1), version(2, review_when="saves move to a server · check by: 2026-09-15")))
        self.assertEqual(code, 0, output)
        self.assertIn("ABC-02: check-by date 2026-09-15 has passed without a review record", output)

    def test_every_passed_date_warns(self):
        # invariant: decision-guard-overdue-review/1
        code, output = self.guard(log(
            version(1, review_when="saves move to a server · check by: 2026-09-15"),
            version(2, review_when="saves move to a server · check by: 2026-09-14")))
        self.assertEqual(code, 0, output)
        self.assertIn("ABC-01: check-by date 2026-09-15 has passed without a review record", output)
        self.assertIn("ABC-02: check-by date 2026-09-14 has passed without a review record", output)

    def test_not_met_needs_a_date(self):
        self.assertFails(log(version(1, review_when=self.DUE),
                             review(1, "2026-09-01", "condition not met — local", "none")),
                         "needs a date in *Next check*")
        self.assertRecords(line("check_reviews", "fail", "review-next-check/1",
                                "line 26: ABC-01 · review 2026-09-01: `condition not met` needs a "
                                "date in *Next check*"))

    def test_changed_in_needs_the_version(self):
        self.assertFails(log(version(1, review_when=self.DUE),
                             review(1, "2026-09-01", "condition met — changed in ABC-01/2", "none")),
                         "names a version that does not exist")
        self.assertRecords(line("check_reviews", "fail", "review-named-version/1",
                                "line 25: ABC-01 · review 2026-09-01: *Result* names a version that "
                                "does not exist"))

    def test_every_version_a_review_names_exists(self):
        self.assertFails(log(version(1, review_when=self.DUE),
                             review(1, "2026-09-01", "condition not met — ABC-01/3 is still a draft",
                                    "2026-10-01")),
                         "names ABC-01/3, a version that does not exist")
        self.assertRecords(line("check_reviews", "fail", "review-named-version/1",
                                "line 25: ABC-01 · review 2026-09-01: names ABC-01/3, a version "
                                "that does not exist"))

    def test_review_of_a_number_that_does_not_exist(self):
        self.assertFails(log(version(1), review(4, "2026-09-01", "condition not met — local",
                                                "2026-10-01")),
                         "ABC-04 does not exist")
        self.assertRecords(line("check_reviews", "fail", "log-reference-target/1",
                                "line 23: ABC-04 · review 2026-09-01: ABC-04 does not exist"))

    def test_unknown_result(self):
        self.assertFails(log(version(1), review(1, "2026-09-01", "looked at it", "none")),
                         "has none of the forms")

    def test_todo_next_check_of_a_condition_not_met_passes_with_a_warning(self):
        code, output = self.guard(log(version(1, review_when=self.DUE),
                                      review(1, "2026-09-01", "condition not met — saves stay local",
                                             "TODO — ask Anna when to look again")))
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:26: warning: *Next check* is `TODO`", output)
        self.assertTrue(output.endswith("0 error(s), 1 warning(s)\n"), output)
        self.assertRecords(line("check_reviews", "pass", "review-next-check/1"))
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])

    def test_malformed_review_when(self):
        self.assertFails(log(version(1, review_when="next year")), "*Review when* is not")
        self.assertRecords(line("check_review_when", "fail", "review-when-form/1",
                                "line 16: ABC-01/1: *Review when* is not `<observable state> · "
                                "check by: YYYY-MM-DD`"))

    def test_todo_review_when_passes_with_a_warning(self):
        code, output = self.guard(log(version(1, review_when="TODO — which state to watch")))
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:16: warning: *Review when* is `TODO`", output)
        self.assertRecords(line("check_review_when", "pass", "review-when-form/1"))
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])


class Record(GuardTestCase):
    def test_a_plain_run_records_a_verdict_for_each_check_that_ran(self):
        self.guard(log(version(1), version(2)))
        self.assertEqual(self.lines, [
            line("check_headings", "pass", "decision-heading-form/1"),
            line("check_headings", "pass", "decision-version-sequence/1"),
            line("check_fields", "pass", "log-entry-field-presence/1"),
            line("check_fields", "pass", "log-entry-field-words/1"),
            line("check_change_rationale", "pass", "decision-change-rationale/1"),
            line("check_changes", "pass", "decision-change-kind/1"),
            line("check_bindings", "pass", "binding-sentence-count/1"),
            line("check_bindings", "pass", "binding-sentence-words/1"),
            line("check_bindings", "pass", "repeal-binding-sentences/1"),
            line("check_binding_across_versions", "pass", "decision-binding-across-versions/1"),
            line("check_relations", "pass", "relation-type/1"),
            line("check_relations", "pass", "relation-fingerprint-presence/1"),
            line("check_verification", "pass", "decision-verification-level/1"),
            line("check_approval", "pass", "decision-approval-record/1"),
            line("check_review_when", "pass", "review-when-form/1"),
            line("check_inherited", "pass", "inherited-origin-form/1"),
            line("check_references", "pass", "log-reference-target/1"),
            line("check_reviews", "pass", "review-next-check/1"),
            line("check_reviews", "pass", "review-named-version/1"),
            line("check_reviews", "pass", "log-reference-target/1"),
            line("check_outranks", "pass", "outranks-pairs/1"),
        ])

    def test_a_line_holds_only_the_keys_of_the_form(self):
        self.guard(log(version(1, outranks="ABC-02"), version(2, outranks="ABC-01"),
                       version(3, change="unchanged sentences")))
        for item in self.lines:
            self.assertTrue(set(item) <= {"check", "verdict", "invariant", "description"}, item)
            self.assertIn(item["verdict"], ("pass", "fail"), item)
            self.assertEqual("description" in item, item["verdict"] == "fail", item)

    def test_a_finding_records_fail_and_no_pass(self):
        self.guard(log(version(1, outranks="ABC-02"), version(2, outranks="ABC-01")))
        self.assertRecords(line("check_outranks", "fail", "outranks-pairs/1",
                                "line 13: ABC-01 and ABC-02 outrank each other"))
        self.assertNotIn(line("check_outranks", "pass", "outranks-pairs/1"), self.lines)

    def test_an_error_of_no_cited_invariant_records_null(self):
        self.guard(log(version(1).replace("- **Scope:**", "*Rationale for change:* x\n- **Scope:**")))
        self.assertRecords(line("check_fields", "fail", None,
                                "line 10: ABC-01/1: version 1 uses *Rationale for change*"))

    def test_a_failure_no_rule_gave_names_the_program(self):
        output = io.StringIO()
        code = format_guard.run(os.path.join(self.directory.name, "missing.md"), today=TODAY,
                                stream=output, record=self.record_path)
        self.assertEqual(code, 2, output.getvalue())
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(len(lines), 1, lines)
        self.assertEqual({key: lines[0][key] for key in ("check", "verdict", "invariant")},
                         {"check": GUARD, "verdict": "fail", "invariant": None})
        self.assertTrue(lines[0]["description"].startswith("cannot read the log: "), lines)

    def test_a_skipped_check_records_no_line(self):
        self.guard(log(version(1), version(2, relations="derives from ABC-01@00000000")))
        recorded = [item["invariant"] for item in self.lines]
        for skipped in ("relation-fingerprint-value/1", "log-existing-lines/1",
                        "log-versions-added-per-number/1", "decision-template-change/1",
                        "decision-approver/1", "decision-example-numbers/1"):
            self.assertNotIn(skipped, recorded)

    def test_the_record_is_overwritten(self):
        os.makedirs(os.path.dirname(self.record_path))
        with open(self.record_path, "w", encoding="utf-8") as handle:
            handle.write('{"check": "old", "verdict": "pass", "invariant": "outranks-pairs/1"}\n')
        self.guard(log(version(1)))
        self.assertNotIn({"check": "old", "verdict": "pass", "invariant": "outranks-pairs/1"},
                         self.lines)

    def test_the_report_for_a_person_stays(self):
        code, output = self.guard(log(version(1, outranks="ABC-02"), version(2, outranks="ABC-01")))
        self.assertEqual(code, 1)
        self.assertIn("decisions.md:13: error: ABC-01 and ABC-02 outrank each other\n", output)
        # The other two errors are the field *Outranks* itself, which the form no longer holds.
        self.assertTrue(output.endswith("3 error(s), 0 warning(s)\n"), output)

    def test_each_verdict_stands_at_a_check_citing_its_invariant(self):
        self.guard(log(version(1, outranks="ABC-02", review_when="next year", approved="Anna"),
                       version(2, outranks="ABC-01", relations="supersedes ABC-07",
                               verification="none", origin="inherited"),
                       version(2, ver=3, binding="Must not. A. B. C!"),
                       review(5, "2026-09-01", "condition not met — ABC-01/4", "none")),
                   approver="Mariusz")
        self.assertTrue(any(item["verdict"] == "fail" for item in self.lines))
        for item in self.lines:
            if item["invariant"] is None:
                continue
            function = item["check"].split("::")[1]
            self.assertIn("# invariant: %s\n" % item["invariant"],
                          inspect.getsource(getattr(format_guard, function)), item)


class InGit(GuardTestCase):
    def setUp(self):
        super().setUp()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "guard@example.com")
        self.git("config", "user.name", "Guard")

    def git(self, *arguments):
        subprocess.run(["git"] + list(arguments), cwd=self.directory.name, check=True,
                       capture_output=True)

    def write(self, relative, text):
        path = os.path.join(self.directory.name, *relative.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)

    def commit(self, text, *others):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        self.git("add", "decisions.md", *others)
        self.git("commit", "-q", "-m", "log")


class AgainstBase(InGit):
    def test_appending_passes(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1), version(2)), base="main")
        self.assertEqual(code, 0, output)
        self.assertRecords(line("check_against_base", "pass", "log-existing-lines/1"))
        self.assertRecords(line("check_against_base", "pass", "log-versions-added-per-number/1"))
        self.assertRecords(line("check_template_change", "pass", "decision-template-change/1"))

    def test_editing_an_entry_on_the_main_branch(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1, approved="Anna, 2026-09-02")), base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("only grows at the end", output)
        self.assertRecords(line("check_against_base", "fail", "log-existing-lines/1",
                                "line 18: the log differs from main here; on the main branch it "
                                "only grows at the end"))

    def test_two_versions_in_one_merge(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1), version(1, ver=2), version(1, ver=3)),
                                  base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("2 versions added against main", output)
        self.assertRecords(line("check_against_base", "fail", "log-versions-added-per-number/1",
                                "line 41: ABC-01: 2 versions added against main, at most one"))

    def test_missing_base(self):
        self.commit(log(version(1)))
        code, output = self.guard(log(version(1)), base="origin/main")
        self.assertEqual(code, 1, output)
        self.assertIn("does not exist", output)
        self.assertEqual(self.lines, [line(None, "fail", None, "--base origin/main does not exist")])

    def test_the_last_line_of_the_base_lengthened(self):
        self.commit(log(version(1)))
        self.assertFails(log(version(1)).rstrip() + " Saves are kept.\n", "only grows at the end",
                         base="main")
        self.assertRecords(line("check_against_base", "fail", "log-existing-lines/1",
                                "line 21: the log differs from main here; on the main branch it "
                                "only grows at the end"))

    def test_a_base_with_an_empty_log(self):
        self.commit("")
        code, output = self.guard(log(version(1)), base="main")
        self.assertEqual(code, 0, output)
        self.assertRecords(line("check_against_base", "pass", "log-existing-lines/1"))

    def test_base_without_the_log(self):
        with open(os.path.join(self.directory.name, "other.txt"), "w") as handle:
            handle.write("x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")
        code, output = self.guard(log(version(1)), base="main")
        self.assertEqual(code, 0, output)
        self.assertIn("compared with an empty one", output)
        self.assertRecords(line("check_against_base", "pass", "log-existing-lines/1"))


class RecordPerCommand(InGit):
    """A run records the checks its options select; the report for a person keeps them all."""

    LOG_ALONE = [
        "binding-sentence-count/1", "binding-sentence-words/1", "decision-approval-record/1",
        "decision-binding-across-versions/1", "decision-change-kind/1",
        "decision-change-rationale/1", "decision-heading-form/1", "decision-verification-level/1",
        "decision-version-sequence/1", "inherited-origin-form/1", "log-entry-field-presence/1",
        "log-entry-field-words/1", "log-reference-target/1", "outranks-pairs/1",
        "relation-fingerprint-presence/1", "relation-type/1", "repeal-binding-sentences/1",
        "review-named-version/1", "review-next-check/1", "review-when-form/1"]

    def setUp(self):
        super().setUp()
        self.commit(log(version(1)))

    def identifiers(self):
        return sorted({item["invariant"] for item in self.lines})

    def test_the_plain_command(self):
        self.guard(log(version(1), version(2)))
        self.assertEqual(self.identifiers(), self.LOG_ALONE)

    def test_the_command_with_base(self):
        self.guard(log(version(1), version(2)), base="main")
        self.assertEqual(self.identifiers(), ["decision-template-change/1", "log-existing-lines/1",
                                              "log-versions-added-per-number/1"])

    def test_the_command_with_merge_onto(self):
        self.guard(log(version(1), version(2)), merge_onto="main")
        self.assertEqual(self.identifiers(), ["log-entry-merge-todo/1",
                                              "relation-fingerprint-value/1"])

    def test_both_options(self):
        self.guard(log(version(1), version(2)), base="main", merge_onto="main")
        self.assertEqual(self.identifiers(), ["decision-template-change/1",
                                              "log-entry-merge-todo/1", "log-existing-lines/1",
                                              "log-versions-added-per-number/1",
                                              "relation-fingerprint-value/1"])

    def test_a_failure_of_the_log_alone_stays_out_of_the_base_record(self):
        code, output = self.guard(log(version(1), version(2, verification="TODO — choose a level",
                                                         change="unchanged sentences")),
                                  base="main")
        self.assertEqual(code, 1, output)
        self.assertIn("*Change* of version 1 is not `new decision`", output)
        self.assertEqual(self.lines, [
            line("check_against_base", "pass", "log-existing-lines/1"),
            line("check_against_base", "pass", "log-versions-added-per-number/1"),
            line("check_template_change", "pass", "decision-template-change/1"),
        ])


class GitFailures(InGit):
    """Only a path the commit does not hold reads as an empty file; any other failure of git is
    a failure of the run, and the checks that need the file record nothing."""

    MESSAGE = "fatal: cannot create the file: Filename too long"

    def setUp(self):
        super().setUp()
        self.commit(log(version(1)))

    def failing_show(self):
        real = format_guard.git

        def git(arguments, cwd):
            if arguments[0] == "show":
                return 128, "", self.MESSAGE
            return real(arguments, cwd)
        return unittest.mock.patch.object(format_guard, "git", git)

    def test_a_failed_call_is_no_absent_log_against_the_base(self):
        with self.failing_show():
            code, output = self.guard(log(version(1)), base="main")
        self.assertEqual(code, 1, output)
        self.assertNotIn("compared with an empty one", output)
        self.assertEqual(self.lines, [line(None, "fail", None, "git cannot read decisions.md at main: "
                                                               "fatal: cannot create the file: "
                                                               "Filename too long")])

    def test_a_failed_call_is_no_absent_log_on_the_commit_merged_onto(self):
        """The check of `TODO` reads the branch's log alone, so it keeps its verdict."""
        with self.failing_show():
            code, output = self.guard(log(version(1)), merge_onto="main")
        self.assertEqual(code, 1, output)
        self.assertEqual(self.lines, [line("check_merge_todo", "pass", "log-entry-merge-todo/1"),
                                      line(None, "fail", None, "git cannot read decisions.md at main: "
                                                               "fatal: cannot create the file: "
                                                               "Filename too long")])

    def test_an_absent_path_compares_with_an_empty_log(self):
        code, output = self.guard(log(version(1)), base="main")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.lines, [
            line("check_against_base", "pass", "log-existing-lines/1"),
            line("check_against_base", "pass", "log-versions-added-per-number/1"),
            line("check_template_change", "pass", "decision-template-change/1"),
        ])


class TemplateChange(InGit):
    TEMPLATE = "elements/decisions/template.md"

    def setUp(self):
        super().setUp()
        self.write(self.TEMPLATE, "# Decision entry template\n\nA field has a reader.\n")
        self.commit(log(version(1)), self.TEMPLATE)

    def test_a_template_left_alone_passes(self):
        self.assertPasses(log(version(1)), base="main")

    def test_a_changed_template_without_a_version(self):
        self.write(self.TEMPLATE, "# Decision entry template\n\nA field has two readers.\n")
        self.assertFails(log(version(1)), "elements/decisions/template.md differs from main, and "
                                          "the log gains no version against it", base="main")
        self.assertRecords(line("check_template_change", "fail", "decision-template-change/1",
                                "elements/decisions/template.md differs from main, and the log "
                                "gains no version against it"))

    def test_a_removed_template_without_a_version(self):
        os.remove(os.path.join(self.directory.name, *self.TEMPLATE.split("/")))
        self.assertFails(log(version(1)), "differs from main", base="main")

    def test_a_changed_template_with_a_version(self):
        self.write(self.TEMPLATE, "# Decision entry template\n\nA field has two readers.\n")
        self.assertPasses(log(version(1), version(1, ver=2)), base="main")


class FingerprintValue(InGit):
    def setUp(self):
        super().setUp()
        self.commit(log(version(1)))

    def test_current_fingerprint_passes(self):
        self.assertPasses(log(version(1), version(2, relations="derives from ABC-01@" + CURRENT)),
                          merge_onto="main")
        self.assertRecords(line("check_fingerprints", "pass", "relation-fingerprint-value/1"))

    def test_stale_fingerprint(self):
        # invariant: decision-fingerprint-input/1
        self.assertFails(log(version(1), version(2, relations="derives from ABC-01@00000000")),
                         "the current fingerprint of ABC-01 is " + CURRENT, merge_onto="main")
        self.assertRecords(line("check_fingerprints", "fail", "relation-fingerprint-value/1",
                                "line 30: ABC-02/1: `derives from ABC-01@00000000` — the current "
                                "fingerprint of ABC-01 is " + CURRENT))

    def test_a_binding_paragraph_over_several_lines_is_fingerprinted_whole(self):
        """BINDING wrapped over two lines, over three, and one word to a line: its fingerprint is
        still CURRENT."""
        # invariant: decision-fingerprint-input/1
        for wrapped in ("The product keeps every saved game\nafter a reload.",
                        "The product keeps\nevery saved game\nafter a reload.",
                        "The\nproduct\nkeeps\nevery\nsaved\ngame\nafter\na\nreload."):
            with self.subTest(lines=wrapped.count("\n") + 1):
                self.commit(log(version(1, binding=wrapped)))
                self.assertFails(log(version(1, binding=wrapped),
                                     version(2, relations="derives from ABC-01@00000000")),
                                 "the current fingerprint of ABC-01 is " + CURRENT,
                                 merge_onto="main")

    def test_stale_fingerprint_without_merge_onto_is_not_checked(self):
        code, output = self.guard(log(version(1), version(2, relations="derives from ABC-01@00000000")))
        self.assertEqual(code, 0, output)
        self.assertIn("note: no --merge-onto given", output)
        self.assertNotIn("relation-fingerprint-value/1", [item["invariant"] for item in self.lines])

    def test_old_version_keeps_its_old_fingerprint(self):
        self.assertPasses(log(
            version(1), version(2, relations="derives from ABC-01@" + CURRENT),
            version(1, ver=2, binding=CHANGED, change="new wording"),
            version(2, ver=2, relations="derives from ABC-01@" + CHANGED_FINGERPRINT)),
            merge_onto="main")

    def test_merge_onto_that_does_not_exist(self):
        code, output = self.guard(log(version(1)), merge_onto="origin/main")
        self.assertEqual(code, 1, output)
        self.assertIn("--merge-onto origin/main does not exist", output)
        self.assertRecords(line(None, "fail", None, "--merge-onto origin/main does not exist"))
        self.assertEqual(self.lines, [line(None, "fail", None,
                                           "--merge-onto origin/main does not exist")])


class MergedLog(InGit):
    """The current fingerprint is the one in the log after the merge onto the given commit."""

    REWORDED = version(1, ver=2, binding=CHANGED, change="new wording")

    def test_a_decision_reworded_only_on_the_commit_merged_onto(self):
        self.commit(log(version(1), self.REWORDED))
        text = log(version(1), version(2, relations="derives from ABC-01@" + CURRENT))
        self.assertPasses(text)
        self.assertFails(text, "the current fingerprint of ABC-01 is " + CHANGED_FINGERPRINT,
                         merge_onto="main")
        self.assertRecords(line("check_fingerprints", "fail", "relation-fingerprint-value/1",
                                "line 30: ABC-02/1: `derives from ABC-01@798975ff` — the current "
                                "fingerprint of ABC-01 is 69b731d5"))

    def test_a_relation_renewed_for_the_wording_on_the_commit_merged_onto(self):
        self.commit(log(version(1), self.REWORDED))
        self.assertPasses(log(version(1), version(2, relations="derives from ABC-01@"
                                                   + CHANGED_FINGERPRINT)), merge_onto="main")
        self.assertRecords(line("check_fingerprints", "pass", "relation-fingerprint-value/1"))

    def test_a_decision_only_the_commit_merged_onto_holds_leans_on_a_reworded_one(self):
        self.commit(log(version(1), version(2, relations="derives from ABC-01@" + CURRENT)))
        self.assertFails(log(version(1), self.REWORDED), "ABC-02/1 (on main)", merge_onto="main")
        self.assertRecords(line("check_fingerprints", "fail", "relation-fingerprint-value/1",
                                "ABC-02/1 (on main): `derives from ABC-01@798975ff` — the current "
                                "fingerprint of ABC-01 is 69b731d5"))

    def test_a_version_both_sides_hold_with_different_text(self):
        self.commit(log(version(1), version(2)))
        self.assertFails(log(version(1), version(2, approved="Anna, 2026-09-02")),
                         "ABC-02/1 differs from its copy on main", merge_onto="main")
        self.assertRecords(line("merged_log", "fail", None,
                                "line 23: ABC-02/1 differs from its copy on main; the log after the "
                                "merge holds this copy"))
        self.assertRecords(line("check_fingerprints", "pass", "relation-fingerprint-value/1"))

    def test_a_relation_edited_in_place_to_a_wrong_fingerprint(self):
        self.commit(log(version(1), version(2, relations="derives from ABC-01@798975ff")))
        self.assertFails(log(version(1), version(2, relations="derives from ABC-01@00000000")),
                         "the current fingerprint of ABC-01 is 798975ff", merge_onto="main")
        self.assertRecords(line("check_fingerprints", "fail", "relation-fingerprint-value/1",
                                "line 30: ABC-02/1: `derives from ABC-01@00000000` — the current "
                                "fingerprint of ABC-01 is 798975ff"))
        self.assertRecords(line("merged_log", "fail", None,
                                "line 23: ABC-02/1 differs from its copy on main; the log after the "
                                "merge holds this copy"))

    def test_a_decision_reworded_in_place_on_the_branch(self):
        self.commit(log(version(1), version(2, relations="derives from ABC-01@798975ff")))
        self.assertFails(log(version(1, binding=CHANGED),
                             version(2, relations="derives from ABC-01@798975ff")),
                         "the current fingerprint of ABC-01 is 69b731d5", merge_onto="main")
        self.assertRecords(line("check_fingerprints", "fail", "relation-fingerprint-value/1",
                                "line 30: ABC-02/1: `derives from ABC-01@798975ff` — the current "
                                "fingerprint of ABC-01 is 69b731d5"))


class MergeTodo(InGit):
    """Given a commit to merge onto, `TODO` in any field of the log is an error (WAY-71). The
    commit merged onto holds no log, so no copy of an entry there differs from the branch's."""

    MESSAGE = "is `TODO`, which a merge onto the main branch does not take"
    REVIEW_DONE = "condition met, decision kept — saves stay local"

    def setUp(self):
        super().setUp()
        with open(os.path.join(self.directory.name, "other.txt"), "w") as handle:
            handle.write("x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")

    def cases(self):
        """(what the case holds, the log, the line of the field, the entry, the field)."""
        return [
            ("change", log(version(1), version(1, ver=2, change="TODO — which kind")),
             27, "ABC-01/2", "Change"),
            ("rationale for change", log(version(1), version(1, ver=2).replace(
                "*Rationale for change:* players lose trust.",
                "*Rationale for change:* TODO — ask Anna")),
             38, "ABC-01/2", "Rationale for change"),
            ("verification", log(version(1, verification="TODO — choose a level")),
             13, "ABC-01/1", "Verification"),
            ("review when", log(version(1, review_when="TODO — which state to watch")),
             16, "ABC-01/1", "Review when"),
            ("another field of a version", log(version(1, origin="TODO — find it")),
             17, "ABC-01/1", "Origin"),
            ("approved by", log(version(1, approved="TODO")), 18, "ABC-01/1", "Approved by"),
            ("a prose field", log(version(1).replace("*Rejected:* none considered",
                                                     "*Rejected:* TODO — ask Ben")),
             21, "ABC-01/1", "Rejected"),
            ("the result of a review", log(version(1), review(1, "2026-09-01", "TODO — ask Anna",
                                                              "none")),
             25, "ABC-01 · review 2026-09-01", "Result"),
            ("who checked a review", log(version(1), review(1, "2026-09-01", self.REVIEW_DONE,
                                                            "none", checked_by="TODO — who")),
             27, "ABC-01 · review 2026-09-01", "Checked by"),
        ]

    def test_todo_in_each_kind_of_field_fails_given_a_commit_to_merge_onto(self):
        for what, text, number, label, name in self.cases():
            with self.subTest(what):
                code, output = self.guard(text, merge_onto="main")
                description = "line %d: %s: *%s* %s" % (number, label, name, self.MESSAGE)
                self.assertEqual(code, 1, output)
                self.assertIn("decisions.md:%d: error: %s: *%s* %s" % (number, label, name,
                                                                      self.MESSAGE), output)
                self.assertRecords(line("check_merge_todo", "fail", "log-entry-merge-todo/1",
                                        description))
                self.assertNotIn(line("check_merge_todo", "pass", "log-entry-merge-todo/1"),
                                 self.lines)

    def test_todo_in_each_kind_of_field_is_not_recorded_without_merge_onto(self):
        for what, text, _, _, _ in self.cases():
            with self.subTest(what):
                self.guard(text)
                self.assertNotIn("log-entry-merge-todo/1",
                                 [item["invariant"] for item in self.lines])

    def test_a_log_without_todo_passes(self):
        self.assertPasses(log(version(1), version(2)), merge_onto="main")
        self.assertRecords(line("check_merge_todo", "pass", "log-entry-merge-todo/1"))

    def test_the_check_cites_its_invariant(self):
        self.assertIn("# invariant: log-entry-merge-todo/1\n",
                      inspect.getsource(format_guard.check_merge_todo))


class TodoInBackticks(InGit):
    """`TODO` wrapped in backticks, as a literal word, is `TODO` like the bare form."""

    TEXT = log(version(1, review_when="`TODO`", origin="`TODO — find it`"))

    def setUp(self):
        super().setUp()
        with open(os.path.join(self.directory.name, "other.txt"), "w") as handle:
            handle.write("x")
        self.git("add", "other.txt")
        self.git("commit", "-q", "-m", "start")

    def test_a_warning_on_a_branch_and_a_failure_given_a_commit_to_merge_onto(self):
        code, output = self.guard(self.TEXT)
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:16: warning: *Review when* is `TODO`", output)
        self.assertIn("decisions.md:17: warning: *Origin* is `TODO`", output)
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [])
        code, output = self.guard(self.TEXT, merge_onto="main")
        self.assertEqual(code, 1, output)
        self.assertEqual([item for item in self.lines if item["verdict"] != "pass"], [
            line("check_merge_todo", "fail", "log-entry-merge-todo/1",
                 "line 16: ABC-01/1: *Review when* is `TODO`, which a merge onto the main branch "
                 "does not take"),
            line("check_merge_todo", "fail", "log-entry-merge-todo/1",
                 "line 17: ABC-01/1: *Origin* is `TODO`, which a merge onto the main branch does "
                 "not take"),
        ])


class TableOfStates(unittest.TestCase):
    def test_the_fields_where_each_word_is_an_error(self):
        """Pins what the guard reads off the template's table of states: a word in italics added
        to the prose of a cell would otherwise become a field silently."""
        self.assertEqual(format_guard.read_rules().word_errors,
                         {"none": ["Change", "Rationale for change", "Approved by"],
                          "TODO": ["Approved by"]})


class MergeOntoNone(GuardTestCase):
    """`none` is what the gate fills in where the main branch does not exist (WAY-61): the checks
    that need that commit are unchecked, and nothing fails. The log stands outside any git
    repository, so the run does not ask git for the commit."""

    REASON = "the method takes a commit the gate filled in as not existing"
    DESCRIPTION = "--merge-onto none: there is no commit to merge onto"
    NOTE = ("note: --merge-onto none: there is no commit to merge onto; `TODO` in the log and the "
            "fingerprints relations carry are unchecked\n")
    UNCHECKED = [
        {"check": GUARD + "::check_merge_todo", "verdict": "unchecked",
         "invariant": "log-entry-merge-todo/1", "reason": REASON, "description": DESCRIPTION},
        {"check": GUARD + "::check_fingerprints", "verdict": "unchecked",
         "invariant": "relation-fingerprint-value/1", "reason": REASON,
         "description": DESCRIPTION},
    ]

    def test_a_clean_log_exits_zero_and_records_both_checks_unchecked(self):
        code, output = self.guard(log(version(1), version(2)), merge_onto="none")
        self.assertEqual(code, 0, output)
        self.assertIn(self.NOTE, output)
        self.assertTrue(output.endswith("0 error(s), 0 warning(s)\n"), output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_todo_stays_a_warning(self):
        code, output = self.guard(log(version(1, origin="TODO — find it")), merge_onto="none")
        self.assertEqual(code, 0, output)
        self.assertIn("decisions.md:17: warning: *Origin* is `TODO`", output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_a_stale_fingerprint_is_not_compared(self):
        code, output = self.guard(log(version(1), version(2, relations="derives from ABC-01@00000000")),
                                  merge_onto="none")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_the_command_line_takes_none(self):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(log(version(1)))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = format_guard.main([self.path, "--merge-onto", "none", "--today", "2026-09-17",
                                      "--record", self.record_path])
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(code, 0, output.getvalue())
        self.assertEqual(lines, self.UNCHECKED)


class BaseNone(GuardTestCase):
    """`none` in place of the commit the branch left the main branch from (WAY-61): the checks
    against it are unchecked, and nothing fails. The log stands outside any git repository."""

    REASON = "the method takes a commit the gate filled in as not existing"
    DESCRIPTION = "--base none: there is no commit the branch left the main branch from"
    NOTE = ("note: --base none: there is no commit the branch left the main branch from; the "
            "checks against it are unchecked\n")
    UNCHECKED = [
        {"check": GUARD + "::check_against_base", "verdict": "unchecked",
         "invariant": "log-existing-lines/1", "reason": REASON, "description": DESCRIPTION},
        {"check": GUARD + "::check_against_base", "verdict": "unchecked",
         "invariant": "log-versions-added-per-number/1", "reason": REASON,
         "description": DESCRIPTION},
        {"check": GUARD + "::check_template_change", "verdict": "unchecked",
         "invariant": "decision-template-change/1", "reason": REASON, "description": DESCRIPTION},
    ]

    def test_a_clean_log_exits_zero_and_records_every_base_check_unchecked(self):
        code, output = self.guard(log(version(1), version(2)), base="none")
        self.assertEqual(code, 0, output)
        self.assertIn(self.NOTE, output)
        self.assertTrue(output.endswith("0 error(s), 0 warning(s)\n"), output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_two_versions_of_one_number_are_not_counted(self):
        code, output = self.guard(log(version(1), version(1, ver=2), version(1, ver=3)),
                                  base="none")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.lines, self.UNCHECKED)

    def test_both_options_none(self):
        code, output = self.guard(log(version(1)), base="none", merge_onto="none")
        self.assertEqual(code, 0, output)
        self.assertEqual(self.lines, self.UNCHECKED + MergeOntoNone.UNCHECKED)

    def test_the_command_line_takes_none(self):
        with open(self.path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(log(version(1)))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = format_guard.main([self.path, "--base", "none", "--today", "2026-09-17",
                                      "--record", self.record_path])
        with open(self.record_path, encoding="utf-8") as handle:
            lines = [json.loads(item) for item in handle.read().split("\n") if item]
        self.assertEqual(code, 0, output.getvalue())
        self.assertEqual(lines, self.UNCHECKED)


# The fields a decision version no longer carries (WAY-05, WAY-14, WAY-25).
DROPPED = ("Outranks", "Approver override", "Consequences")
NEW_KINDS = ("editorial correction", "unchanged sentences", "new wording", "narrowing",
             "challenge", "repeal")


class SlimForm(GuardTestCase):
    """The form of a decision version once the fields nothing reads left it."""

    def test_a_version_without_each_dropped_field_passes(self):
        for name in DROPPED:
            with self.subTest(name):
                self.assertPasses(log(version(1, omit=(name,))))

    def test_a_version_without_any_dropped_field_passes(self):
        self.assertPasses(log(version(1, omit=DROPPED), version(2, omit=DROPPED)))

    def test_a_dropped_field_is_no_field_of_the_form(self):
        texts = {"Outranks": version(1, outranks="none"),
                 "Approver override": version(1, override="none"),
                 "Consequences": version(1).replace("*Rejected:*",
                                                    "*Consequences:* more tests.\n*Rejected:*")}
        for name, text in texts.items():
            with self.subTest(name):
                self.assertFails(log(text), "ABC-01/1: *%s* is not a field of the form; " % name)
                self.assertEqual([item["invariant"] for item in self.lines
                                  if item["verdict"] == "fail"], [None])

    def test_a_later_version_names_its_kind_alone(self):
        for kind in NEW_KINDS:
            binding = {"unchanged sentences": BINDING, "challenge": BINDING,
                       "repeal": None}.get(kind, CHANGED)
            with self.subTest(kind):
                self.assertPasses(log(version(1, omit=DROPPED),
                                      version(1, ver=2, change=kind, binding=binding, omit=DROPPED)))

    def test_previous_is_no_part_of_the_kind(self):
        self.assertFails(log(version(1, omit=DROPPED),
                             version(1, ver=2, change="unchanged sentences · previous: ABC-01/1",
                                     omit=DROPPED)),
                         "`unchanged sentences · previous: ABC-01/1` is not a kind of change")
        self.assertRecords(line("check_changes", "fail", "decision-change-kind/1",
                                "line 27: ABC-01/2: `unchanged sentences · previous: ABC-01/1` is "
                                "not a kind of change"))

    def test_the_kinds_the_list_no_longer_holds(self):
        for kind in ("rationale change", "field change", "replacement"):
            with self.subTest(kind):
                self.assertFails(log(version(1, omit=DROPPED),
                                     version(1, ver=2, change=kind, omit=DROPPED)),
                                 "`%s` is not a kind of change" % kind)

    def test_unchanged_sentences_and_a_challenge_keep_the_binding_sentences(self):
        for kind in ("unchanged sentences", "challenge"):
            message = ("ABC-01/2: a version of the kind %s keeps the binding sentences of ABC-01/1"
                       % kind)
            with self.subTest(kind):
                self.assertFails(log(version(1, omit=DROPPED),
                                     version(1, ver=2, change=kind, binding=CHANGED, omit=DROPPED)),
                                 message)
                self.assertRecords(line("check_binding_across_versions", "fail",
                                        "decision-binding-across-versions/1", "line 25: " + message))

    def test_a_first_version_that_is_no_new_decision_fails_its_invariant(self):
        self.assertFails(log(version(1, change="new wording", omit=DROPPED)),
                         "is not `new decision`")
        self.assertRecords(line("check_changes", "fail", "decision-change-kind/1",
                                "line 9: ABC-01/1: *Change* of version 1 is not `new decision`"))

    def test_related_to_is_no_type_of_relation(self):
        self.assertFails(log(version(1, omit=DROPPED),
                             version(2, relations="related to ABC-01", omit=DROPPED)),
                         "relation `related to ABC-01` is not of a known type")
        self.assertRecords(line("check_relations", "fail", "relation-type/1",
                                "line 30: ABC-02/1: relation `related to ABC-01` is not of a known "
                                "type"))

    def test_the_approver_is_the_one_given_whatever_an_override_names(self):
        self.assertFails(log(version(1, override="Anna", omit=("Outranks", "Consequences"))),
                         "*Approved by* names Anna, not Mariusz", approver="Mariusz")
        self.assertRecords(line("check_approver", "fail", "decision-approver/1",
                                "line 19: ABC-01/1: *Approved by* names Anna, not Mariusz"))


class NumberingGap(GuardTestCase):
    def test_a_gap_in_the_numbers_is_no_error(self):
        """ABC-01 and ABC-03 without ABC-02: a number cut before the main branch stays a gap."""
        self.assertPasses(log(version(1, omit=DROPPED),
                              version(3, relations="derives from ABC-01@" + CURRENT, omit=DROPPED)))


class ExampleNumbers(GuardTestCase):
    """`examples.md` names decisions of the log by number instead of copying them (WAY-05)."""

    def check(self, text, examples):
        path = os.path.join(self.directory.name, "examples.md")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(examples)
        report = format_guard.Report(self.path)
        format_guard.check_examples(format_guard.parse_log(text, "ABC"), path, "ABC", report)
        return report

    def test_numbers_the_log_holds_pass(self):
        report = self.check(log(version(1), version(2)), "# Examples\n\n- ABC-01\n- ABC-02\n")
        self.assertEqual(report.errors, [])
        self.assertEqual(report.record(), [line("check_examples", "pass",
                                                "decision-example-numbers/1")])

    def test_a_number_the_log_lacks_fails(self):
        report = self.check(log(version(1)), "# Examples\n\n- ABC-01\n- ABC-04\n")
        self.assertEqual(report.record(), [line("check_examples", "fail",
                                                "decision-example-numbers/1",
                                                "examples.md:4: ABC-04 is not a number of the log")])

    def test_a_copy_that_differs_from_its_version_is_no_error(self):
        report = self.check(log(version(1)),
                            "# Examples\n\n" + version(1).replace("Anna", "Ben") + "\n")
        self.assertEqual(report.errors, [])


class RulesFromTheTemplate(unittest.TestCase):
    """The guard reads the number of binding sentences and the words kept out of them from the
    section "Binding sentences" of the template (WAY-05)."""

    def rules(self, change):
        with open(format_guard.TEMPLATE, encoding="utf-8") as handle:
            text = handle.read()
        start = text.index("## Binding sentences\n")
        end = text.index("\n## ", start + 1)
        text = text[:start] + change(text[start:end]) + text[end:]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "template.md")
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            return format_guard.read_rules(path)

    def test_the_rules_stand_without_a_list_of_checks(self):
        rules = self.rules(lambda section: section)
        self.assertEqual(rules.max_sentences, 3)
        self.assertEqual(sorted(word.lower() for word in rules.forbidden_words), ["should", "will"])

    def test_the_count_comes_from_binding_sentences(self):
        self.assertEqual(self.rules(lambda section: section.replace("One to three", "One to two",
                                                                    1)).max_sentences, 2)

    def test_a_word_added_to_binding_sentences_is_kept_out(self):
        rules = self.rules(lambda section: section.replace("*will*", "*will*, *perhaps*", 1))
        self.assertIn("perhaps", rules.forbidden_words)


class OwnLog(unittest.TestCase):
    """The entries of the-way's log still carry what is not in the form, which the guard reports
    in three places only: relations `related to`, a kind of change followed by `previous:`, and
    the fields *Outranks*, *Approver override* and *Consequences*. Once the entries are rewritten
    in the new form, the log passes with no error."""

    OLD_FORM = (re.compile(r": [A-Z]+-\d{2,}/\d+: relation `related to [A-Z]+-\d{2,}` is not of a "
                           r"known type$"),
                re.compile(r": [A-Z]+-\d{2,}/\d+: `[a-z ]+ · previous: [A-Z]+-\d{2,}/\d+` is not a "
                           r"kind of change$"),
                re.compile(r": [A-Z]+-\d{2,}/\d+: \*(?:Outranks|Approver override|Consequences)\* "
                           r"is not a field of the form; "))

    def test_the_way_log_holds_no_error_but_the_old_form(self):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            record = os.path.join(directory, "decisions.jsonl")
            code = format_guard.run(format_guard.OWN_LOG, stream=output, record=record)
            with open(record, encoding="utf-8") as handle:
                lines = [json.loads(item) for item in handle.read().split("\n") if item]
        errors = [item for item in output.getvalue().split("\n") if ": error: " in item]
        self.assertIn(code, (0, 1), output.getvalue())
        self.assertEqual([item for item in errors
                          if not any(form.search(item) for form in self.OLD_FORM)], [])
        self.assertEqual(code == 1, bool(errors))
        self.assertEqual(sorted({item["invariant"] for item in lines if item["invariant"]}), [
            "binding-sentence-count/1", "binding-sentence-words/1", "decision-approval-record/1",
            "decision-approver/1", "decision-binding-across-versions/1",
            "decision-change-kind/1", "decision-change-rationale/1", "decision-example-numbers/1",
            "decision-heading-form/1", "decision-verification-level/1",
            "decision-version-sequence/1", "inherited-origin-form/1", "log-entry-field-presence/1",
            "log-entry-field-words/1", "log-reference-target/1", "outranks-pairs/1",
            "relation-fingerprint-presence/1", "relation-type/1", "repeal-binding-sentences/1",
            "review-named-version/1", "review-next-check/1", "review-when-form/1"])


if __name__ == "__main__":
    unittest.main()
