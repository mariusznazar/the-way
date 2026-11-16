"""Tests of process-audit/record_items.py: the reading of the items `Discarded attempt` and
`Review rounds` of a cycle record, as lines of text with no git and no file."""

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import record_items  # noqa: E402

remarks_check = record_items.remarks_check

NL = chr(10)
BESIDE = "is no entry or stands at another indent than its entries"
SILENT = "the entry of a round does not say whether there was a contradiction"
NO_MARKER = "opens with no marker of its reason"
SEVERAL_REASONS = "holds more than one reason in a form that is not read"


def read(record: str):
    lines = remarks_check.split_lines(record)
    return record_items.read_contradiction(lines, remarks_check.fenced_flags(lines))


def q1(discarded: str, rounds: str = " none"):
    """Q1 of a record whose item `Discarded attempt` reads `discarded` and whose item
    `Review rounds` is `- Review rounds:` followed by `rounds`."""
    return read(f"- Discarded attempt: {discarded}\n- Review rounds:{rounds}\n")


ENTRIES_IN_NEITHER_FORM = (
    "the return step: fix `reports/return_fix.md`", "review `reports/r.md`, FAIL: x",
    "review `reports/r.md`: PASS", "review `reports/r.md`, PASSED",
    "review `reports/../r.md`, PASS: x", "review `reports/" + "r" * 200 + ".md`, PASS: x",
    "Review `reports/r.md`, PASS", "reviews `reports/r.md`, PASS",
    "findings `notes/a.md`, contradiction yes: x", "a review: review `reports/r.md`, PASS")


def findings(name: str, mark: str = "", details: str = "the whole change") -> str:
    return f"\n  - findings `reports/{name}_findings.md`{mark}: {details}"


class DiscardedAttemptReason(unittest.TestCase):
    """The reason is the marker at the start of the item, and nothing the text says."""

    def test_the_marker_at_the_start_gives_the_answer_whatever_follows(self):
        # decision: WAY-404 "The reason of a discarded attempt stands at the start of the record's item"
        # Worked from the answers of the task, row 3 of its *To do*: the marker `open design choice`
        # is a yes; `none` and the markers `reserved choice` and `size` leave no contradiction.
        for text, answer in (
                ("reason: `open design choice`; 10:32, report reports/x.md; entries none", "yes"),
                ("reason: `reserved choice`; the blocked draft request", "no"),
                ("reason: `size`; planning next, no open design choice", "no"),
                ("reason: `size`" + " x" * 100_000, "no"),
                ("none", "no"), ("None.", "no")):
            with self.subTest(text[:50]):
                self.assertEqual((answer, None), q1(text))

    def test_the_four_denials_of_review_100_give_unknown(self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        # The texts are the four examples of remark 6 of the review of the foundation of 2026-11-14.
        for text in ("open design choice not found", "an open design choice did not apply",
                     "no sign whatsoever that this was an open design choice",
                     "No attempt was discarded for a reserved choice, an oversized change or an "
                     "open design choice"):
            with self.subTest(text[:40]):
                answer, why = q1(text)
                self.assertIsNone(answer)
                self.assertIn(NO_MARKER, why)

    def test_a_text_without_the_marker_at_its_start_or_in_its_form_gives_unknown(self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        for text in ("", "a time overrun", "10:32; reason: `open design choice`",
                     "reason: open design choice", "reason:`size`", "Reason: `size`",
                     "reason: `Size`", "reason: `size and open design choice`",
                     "reason: `open design choice ", "reason: `big`",
                     "none — reason: `open design choice`", "no code kept; reason: `size`",
                     "x" * 500_000 + " reason: `open design choice`",
                     "no " * 200_000 + "reason: `open design choice`"):
            with self.subTest(text[:50]):
                self.assertIsNone(q1(text)[0])

    def test_two_markers_in_the_text_give_unknown_with_a_reason_of_their_own(self):
        # A text that gives two reasons does not say which one it is, and the reason says so and
        # points to the form that holds two attempts; it is not the reason of a text with no marker.
        for text in ("reason: `size`; reason: `open design choice`",
                     "reason: `open design choice`; reason: `size`",
                     "reason: `size` " * 50_000):
            with self.subTest(text[:50]):
                answer, why = q1(text)
                self.assertIsNone(answer)
                self.assertIn(SEVERAL_REASONS, why)
                self.assertNotIn(NO_MARKER, why)

    def test_one_entry_for_each_attempt_gives_yes_where_any_marker_is_an_open_design_choice(self):
        # decision: WAY-404 "The reason of a discarded attempt stands at the start of the record's item"
        # A cycle that discarded an attempt for an open design choice and, after the spec, another
        # for size writes one entry for each, in either order; the entries carry the details.
        def read_entries(*texts):
            body = "".join(f"{NL}  - {text}" for text in texts)
            return read("- Discarded attempt:" + body + NL + "- Review rounds: none" + NL)

        first = "reason: `open design choice`; 10:32, report reports/x.md; entries none"
        second = "reason: `size`; 14:05, report reports/y.md"
        reserved = "reason: `reserved choice`; the blocked request"
        for texts, answer in (((first, second), "yes"), ((second, first), "yes"),
                              ((first,), "yes"), ((reserved, second), "no"), ((second,), "no")):
            with self.subTest(str(texts)[:50]):
                self.assertEqual((answer, None), read_entries(*texts))

    def test_an_entry_without_a_marker_gives_unknown_unless_another_entry_is_an_open_design_choice(
            self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        def read_entries(*texts):
            body = "".join(f"{NL}  - {text}" for text in texts)
            return read("- Discarded attempt:" + body + NL + "- Review rounds: none" + NL)

        for texts in (("reason: `size`", "a time overrun"), ("reason: `size`", "none"),
                      ("reason: `size`", "no open design choice"),
                      ("reason: `size`", "10:32; reason: `reserved choice`"),
                      ("reason: `size`; reason: `reserved choice`",)):
            with self.subTest(texts):
                answer, why = read_entries(*texts)
                self.assertIsNone(answer)
                self.assertIn("opens with no marker of its reason", why)
        self.assertEqual(("yes", None), read_entries("reason: `size`", "a time overrun",
                                                      "reason: `open design choice`"))

    def test_a_plain_first_attempt_under_an_empty_item_beside_an_entry_gives_unknown(self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        # The record a leader writes for two discards when it only adds an entry: the first attempt
        # as plain text on the line under the empty item, the second as an entry. It holds the marker
        # `open design choice` and two reasons; it must give neither no nor a reason of "no marker".
        record = ("- Discarded attempt:" + NL + "  reason: `open design choice`; 10:32, report "
                  "reports/x.md" + NL + "  - reason: `size`; 14:05" + NL + "- Review rounds: none" + NL)
        answer, why = read(record)
        self.assertIsNone(answer)
        self.assertIn(SEVERAL_REASONS, why)
        self.assertNotIn(NO_MARKER, why)

    def test_one_attempt_on_the_line_under_the_item_with_its_details_as_a_list_is_read(self):
        # decision: WAY-404 "The reason of a discarded attempt stands at the start of the record's item"
        # The form the earlier reading accepted: the text of one attempt, its details as a list.
        for marker, answer in (("open design choice", "yes"), ("size", "no"),
                               ("reserved choice", "no")):
            with self.subTest(marker):
                record = ("- Discarded attempt:" + NL + f"  reason: `{marker}`; 10:32" + NL
                          + "  - report reports/x.md" + NL + "  - reset to abc1234" + NL
                          + "- Review rounds: none" + NL)
                self.assertEqual((answer, None), read(record))

    def test_a_plain_line_beside_the_entries_gives_unknown_with_its_reason(self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        beside = "a plain line"
        for body in (NL + "  - reason: `open design choice`" + NL + "  " + beside,
                     NL + "  - reason: `open design choice`" + NL + "  - reason: `size`" + NL
                     + "  " + beside,
                     NL + "  " + beside + NL + "  - reason: `open design choice`"):
            with self.subTest(body[:40]):
                answer, why = read("- Discarded attempt:" + body + NL + "- Review rounds: none" + NL)
                self.assertIsNone(answer)
                self.assertIn(BESIDE, why)

    def test_a_line_deeper_than_the_entries_continues_an_entry(self):
        record = ("- Discarded attempt:" + NL + "  - reason: `open design choice`; 10:32" + NL
                  + "    the report reports/x.md, no code kept" + NL + "  - reason: `size`; 14:05"
                  + NL + "- Review rounds: none" + NL)
        self.assertEqual(("yes", None), read(record))

    def test_an_entry_first_under_the_item_and_deeper_than_the_next_one_is_not_dropped(self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        # As Markdown the entries of such a list are two entries of one list; the first holds the
        # marker `open design choice` and must not give no. The list is not read as a list of
        # entries at one indent, so the answer is unknown, with the reason that names the indent.
        for first, others in (("open design choice", ("size",)),
                              ("open design choice", ("size", "reserved choice")),
                              ("size", ("open design choice",)),
                              ("open design choice", ("size", "reserved choice", "size"))):
            body = NL + "      - reason: `" + first + "`"
            body += "".join(NL + "    - reason: `" + other + "`" for other in others)
            with self.subTest(first + str(others)):
                answer, why = read("- Discarded attempt:" + body + NL + "- Review rounds: none" + NL)
                self.assertIsNone(answer)
                self.assertIn(BESIDE, why)
        # The same entries at one indent give the answers the entries give.
        same = ("- Discarded attempt:" + NL + "    - reason: `open design choice`" + NL
                + "    - reason: `size`" + NL + "- Review rounds: none" + NL)
        self.assertEqual(("yes", None), read(same))

    def test_a_sub_entry_under_the_first_entry_is_no_entry_of_the_list(self):
        record = ("- Discarded attempt:" + NL + "  - reason: `size`; details" + NL
                  + "      - reason: `open design choice`" + NL + "  - reason: `reserved choice`"
                  + NL + "- Review rounds: none" + NL)
        self.assertEqual(("no", None), read(record))

    def test_a_hundred_thousand_entries_with_a_plain_line_beside_them_are_read_at_once(self):
        # decision: WAY-404 "The audit of the process takes from this item, for its answer whether"
        body = "".join(NL + "  - reason: `size`; x" for _ in range(100_000)) + NL + "  a plain line"
        answer, why = read("- Discarded attempt:" + body + NL + "- Review rounds: none" + NL)
        self.assertIsNone(answer)
        self.assertIn(BESIDE, why)

    def test_text_beside_the_entries_or_an_entry_deeper_or_fenced_is_not_a_second_attempt(self):
        beside = ("- Discarded attempt: reason: `size`" + NL + "  - reason: `open design choice`" + NL
                  + "- Review rounds: none" + NL)
        answer, why = read(beside)
        self.assertIsNone(answer)
        self.assertIn(SEVERAL_REASONS, why)
        deeper = ("- Discarded attempt:" + NL + "  - reason: `size`; details" + NL
                  + "    - reason: `open design choice`" + NL + "- Review rounds: none" + NL)
        self.assertEqual(("no", None), read(deeper))
        fenced = ("- Discarded attempt:" + NL + "  - reason: `size`" + NL + "  ```" + NL
                  + "  - reason: `open design choice`" + NL + "  ```" + NL
                  + "- Review rounds: none" + NL)
        self.assertEqual(("no", None), read(fenced))

    def test_entries_of_discarded_attempts_leave_the_rounds_to_say_whether_there_was_a_contradiction(self):
        entries = NL + "  - reason: `size`" + NL + "  - reason: `reserved choice`"
        self.assertEqual(("no", None), q1(entries, findings("a", ", contradiction no")))
        self.assertEqual((None, SILENT), q1(entries, findings("a")))

    def test_a_missing_or_doubled_item_gives_unknown_with_its_reason(self):
        # decision: WAY-344 "Each reading of a file that the rule covers has one test"
        self.assertEqual((None, "the record holds no item `Discarded attempt`"),
                         read("- Review rounds: none\n"))
        self.assertEqual((None, "the record holds the item `Discarded attempt` more than once"),
                         read("- Discarded attempt: none\n- Discarded attempt: none\n"
                              "- Review rounds: none\n"))

    def test_an_item_in_a_code_fence_is_not_read(self):
        record = ("```\n- Discarded attempt: reason: `open design choice`\n```\n"
                  "- Discarded attempt: none\n- Review rounds: none\n")
        self.assertEqual(("no", None), read(record))

    def test_the_marker_on_the_line_under_an_empty_item_is_read(self):
        record = ("- Discarded attempt:\n  reason: `open design choice`; report reports/x.md\n"
                  "- Review rounds: none\n")
        self.assertEqual(("yes", None), read(record))


class RoundEntries(unittest.TestCase):
    """The mark of an entry of *Review rounds*, in either of its two forms."""

    def test_an_entry_marked_yes_gives_yes_whatever_the_other_item_says(self):
        # decision: WAY-403 "The cycle writes the mark into the entry of the round in the record's item"
        marked = findings("a", ", contradiction yes")
        self.assertEqual(("yes", None), q1("none", marked))
        self.assertEqual(("yes", None), q1("reason: `size`", marked))
        self.assertEqual(("yes", None), q1("a time overrun", marked))
        self.assertEqual(("yes", None), q1("none", findings("b") + marked))

    def test_every_entry_marked_no_and_a_review_that_passed_give_no(self):
        # decision: WAY-403 "The cycle writes the mark into the entry of the round in the record's item"
        passed = "\n  - review `reports/review_return_step.md`, PASS: the return step, range a..b"
        for rounds in (findings("a", ", contradiction no"), passed,
                       findings("a", ", contradiction no") + passed,
                       findings("a", ", contradiction no") + findings("b", ", contradiction no")):
            with self.subTest(rounds[:60]):
                self.assertEqual(("no", None), q1("none", rounds))

    def test_an_entry_without_its_mark_gives_unknown_with_the_one_reason(self):
        # decision: WAY-403 "The cycle writes the mark into the entry of the round in the record's item"
        # The first is the form from before the mark, the others are marks of a form it is not.
        for rounds in (findings("a"), findings("a", ", contradiction maybe"),
                       findings("a", ", contradiction no longer applies"),
                       findings("a", ", contradiction YES"),
                       findings("a", ", contradiction  yes"),
                       findings("a", "", "contradiction yes"),
                       findings("a", ", contradiction yes, and more"),
                       findings("a", ", contradiction no") + findings("b")):
            with self.subTest(rounds[:70]):
                self.assertEqual((None, SILENT), q1("none", rounds))

    def test_an_entry_marked_yes_wins_over_an_entry_without_a_mark(self):
        self.assertEqual(("yes", None),
                         q1("none", findings("a") + findings("b", ", contradiction yes")))

    def test_an_entry_in_neither_form_gives_unknown_and_names_no_findings_file(self):
        for entry in ENTRIES_IN_NEITHER_FORM:
            with self.subTest(entry[:50]):
                answer, why = q1("none", f"\n  - {entry}")
                self.assertIsNone(answer)
                self.assertIn("does not give its entries", why)
                rounds, why = record_items.read_rounds(
                    *lines_of(f"- Review rounds:\n  - {entry}\n"))
                self.assertIsNone(rounds)
                self.assertIn("names no findings file", why)

    def test_an_entry_in_neither_form_does_not_hide_a_yes_of_the_item_discarded_attempt(self):
        self.assertEqual(("yes", None),
                         q1("reason: `open design choice`", "\n  - the return step: fix"))

    def test_only_the_entries_at_the_first_indent_and_outside_a_fence_are_read(self):
        # decision: WAY-403 "The cycle writes the mark into the entry of the round in the record's item"
        # A line that quotes an entry deeper in the item, in a code fence or in another item is no
        # entry of the item.
        deeper = findings("a", ", contradiction no") + (
            "\n    - findings `reports/b_findings.md`, contradiction yes: quoted")
        fenced = findings("a", ", contradiction no") + (
            "\n  ```\n  - findings `reports/b_findings.md`, contradiction yes: quoted\n  ```")
        for rounds in (deeper, fenced):
            with self.subTest(rounds[-30:]):
                self.assertEqual(("no", None), q1("none", rounds))
        other = ("- Discarded attempt: none\n- Review rounds: none\n- Process remarks on the-way:\n"
                 "  - findings `reports/b_findings.md`, contradiction yes: quoted\n")
        self.assertEqual(("no", None), read(other))

    def test_the_item_review_rounds_out_of_its_form_gives_unknown_unless_the_marker_says_yes(self):
        # decision: WAY-344 "Each reading of a file that the rule covers has one test"
        # The item is missing, doubled or holds text beside its entries.
        for record, words in (
                ("- Discarded attempt: none\n", "does not give its entries"),
                ("- Discarded attempt: none\n- Review rounds: none\n- Review rounds: none\n",
                 "does not give its entries"),
                ("- Discarded attempt: none\n- Review rounds: none\n  - findings "
                 "`reports/a_findings.md`, contradiction no: x\n", "does not give its entries"),
                ("- Discarded attempt: none\n- Review rounds:\n  - findings "
                 "`reports/a_findings.md`, contradiction no: x\n  - findings "
                 "`reports/a_findings.md`, contradiction no: again\n", "does not give its entries")):
            with self.subTest(record[-40:]):
                answer, why = read(record)
                self.assertIsNone(answer)
                self.assertIn(words, why)
        for record in ("- Discarded attempt: reason: `open design choice`\n",
                       "- Discarded attempt: reason: `open design choice`\n- Review rounds: none\n"
                       "- Review rounds: none\n"):
            self.assertEqual(("yes", None), read(record))

    def test_a_hundred_thousand_entries_are_read_at_once(self):
        # The names stand once each: a reading that compared each entry with the ones before it
        # would not finish.
        rounds = "".join(findings(f"f{number}", ", contradiction no", "x")
                         for number in range(100_000))
        self.assertEqual(("no", None), q1("none", rounds))
        names = record_items.review_rounds(*lines_of(f"- Review rounds:{rounds}\n"))[0]
        self.assertEqual(100_000, len(names))


def lines_of(record: str):
    lines = remarks_check.split_lines(record)
    return lines, remarks_check.fenced_flags(lines)


class FixRounds(unittest.TestCase):
    """`review_rounds` gives the findings files of the fix rounds, and a review that passed with no
    fix is none."""

    def test_a_review_that_passed_is_no_fix_round_and_a_findings_file_is_one(self):
        # decision: WAY-337 "The record's item *Review rounds* also takes an entry for a review"
        rounds = (findings("a", ", contradiction no")
                  + "\n  - review `reports/review_return_step.md`, PASS: the return step"
                  + findings("b") + "\n  - review `reports/review_fix.md`, PASS: the fix")
        names, why = record_items.review_rounds(*lines_of(f"- Review rounds:{rounds}\n"))
        self.assertEqual(["reports/a_findings.md", "reports/b_findings.md"], names)
        self.assertIsNone(why)

    def test_the_item_reading_none_has_no_round_and_an_item_of_reviews_alone_has_none(self):
        self.assertEqual(([], None), record_items.review_rounds(*lines_of("- Review rounds: none\n")))
        only = "\n  - review `reports/r.md`, PASS: the return step"
        self.assertEqual(([], None), record_items.review_rounds(*lines_of(f"- Review rounds:{only}\n")))

    def test_a_findings_file_named_twice_or_an_entry_in_neither_form_gives_none(self):
        twice = findings("a") + findings("a", ", contradiction no")
        names, why = record_items.review_rounds(*lines_of(f"- Review rounds:{twice}\n"))
        self.assertIsNone(names)
        self.assertIn("names a findings file twice", why)
        names, why = record_items.review_rounds(*lines_of("- Review rounds:\n  - prose about it\n"))
        self.assertIsNone(names)
        self.assertIn("names no findings file", why)

    def test_a_record_without_the_item_gives_none_with_its_reason(self):
        # decision: WAY-344 "Each reading of a file that the rule covers has one test"
        names, why = record_items.review_rounds(*lines_of("- Discarded attempt: none\n"))
        self.assertIsNone(names)
        self.assertIn("no item `Review rounds`", why)


if __name__ == "__main__":
    unittest.main()
