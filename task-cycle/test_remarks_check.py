"""Tests of task-cycle/remarks_check.py on cycle records and stage reports written for the tests.

The fixtures are trimmed from the forms real stage reports and cycle records take: a heading
`## Searches not found or unclear` with bullets, a bold label with bullets below it or with the
item on its own line, and the process remarks as an indented list, as a heading or as a paragraph.
Expected items are written out here, never taken from the script.
"""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import remarks_check  # noqa: E402

TEMPLATE = HERE / "record_template.md"

HEADING_REPORT = """\
# Report

## Checks

- `python -B x.py` exit 0

## Searches not found or unclear

- A route to a screenshot of the running product in the foundation: not found (see *Checks*).
- A source outside the product that the change rests on and the foundation lacks: none found.
- Unclear: whether the last sentence needs code today. No case exists,
  so I made no change.
- none

## Problems

None observed.
"""


def items(text: str) -> list[str]:
    return remarks_check.section_items(text)


class SectionFormsTest(unittest.TestCase):
    def test_a_heading_section_gives_each_bullet_but_none(self) -> None:
        self.assertEqual(items(HEADING_REPORT), [
            "A route to a screenshot of the running product in the foundation: not found "
            "(see *Checks*).",
            "A source outside the product that the change rests on and the foundation lacks: "
            "none found.",
            "Unclear: whether the last sentence needs code today. No case exists, so I made "
            "no change.",
        ])

    def test_a_section_that_is_only_none_gives_nothing(self) -> None:
        for body in ("none", "None", "none.", "`none`", "**None.**", "- none", "- None."):
            report = f"## Searches not found or unclear\n\n{body}\n"
            self.assertEqual(items(report), [], body)

    def test_none_found_and_none_unresolved_are_items(self) -> None:
        report = ("## Searches not found or unclear\n\n- A word used against its glossary entry: "
                  "none found.\n- None unresolved. Unclear: `rsync` availability on a new host "
                  "is not stated by any source.\n")
        self.assertEqual(items(report), [
            "A word used against its glossary entry: none found.",
            "None unresolved. Unclear: `rsync` availability on a new host is not stated by any "
            "source.",
        ])

    def test_a_heading_section_ends_at_the_next_heading_of_its_level_or_higher(self) -> None:
        report = ("# T\n\n## Searches not found or unclear\n\n- first\n\n### Detail\n\n- second\n\n"
                  "## After the answer\n\n- not an item\n")
        self.assertEqual(items(report), ["first", "second"])

    def test_a_heading_of_another_level_and_a_trailing_colon_still_name_the_section(self) -> None:
        for heading in ("### Searches not found or unclear", "## Searches not found or unclear:",
                        "## **Searches not found or unclear**",
                        "## Searches not found or unclear (WAY-260)"):
            report = f"{heading}\n\n- one item\n"
            self.assertEqual(items(report), ["one item"], heading)

    def test_a_numbered_heading_names_the_section(self) -> None:
        report = ("## 11. Own-work check\n\n- `python -B x.py` exit 0\n\n"
                  "## 12. Searches not found or unclear\n\n- The route to the host: not found.\n"
                  "- Unclear: which release the handoff means.\n\n"
                  "## 13. Problems\n\n- not an item\n")
        self.assertEqual(items(report), [
            "The route to the host: not found.",
            "Unclear: which release the handoff means.",
        ])

    def test_a_section_number_may_take_the_forms_of_a_numbered_heading(self) -> None:
        for heading in ("## 12) Searches not found or unclear",
                        "### 3.1 Searches not found or unclear",
                        "### 3.1. Searches not found or unclear:",
                        "## **12.** Searches not found or unclear",
                        "## 7. **Searches not found or unclear**",
                        "## 12. Searches not found or unclear (WAY-260)"):
            report = f"{heading}\n\n- one item\n"
            self.assertEqual(items(report), ["one item"], heading)

    def test_a_heading_with_other_words_before_the_name_does_not_name_the_section(self) -> None:
        for heading in ("## Section 12. Searches not found or unclear",
                        "## 12.Searches not found or unclear",
                        "## 12. Other searches not found or unclear",
                        "## 12. Searches found"):
            report = f"{heading}\n\n- one item\n"
            self.assertEqual(items(report), [], heading)

    def test_a_bold_label_with_bullets_below_it_gives_the_bullets(self) -> None:
        report = ("**Choices**\n- x\n\n**Searches not found or unclear:**\n\n"
                  "- Whether the host's cron daemon runs: the record does not say.\n"
                  "- The server's time zone: unread.\n\n**Problems:** none\n")
        self.assertEqual(items(report), [
            "Whether the host's cron daemon runs: the record does not say.",
            "The server's time zone: unread.",
        ])

    def test_the_label_may_have_its_colon_inside_outside_or_nowhere(self) -> None:
        for label in ("**Searches not found or unclear:**", "**Searches not found or unclear**:",
                      "**Searches not found or unclear**"):
            report = f"{label}\n- one\n"
            self.assertEqual(items(report), ["one"], label)

    def test_a_label_with_the_item_on_its_own_line_gives_that_text(self) -> None:
        report = ("**Searches not found or unclear:** none for the code; unclear: the handoff says "
                  "\"the script's refusal\"; I read it as the refusal case.\n\n"
                  "**Choices:** none\n")
        self.assertEqual(items(report), [
            "none for the code; unclear: the handoff says \"the script's refusal\"; I read it as "
            "the refusal case."])

    def test_a_label_line_reading_none_gives_nothing(self) -> None:
        for line in ("**Searches not found or unclear:** none.",
                     "**Searches not found or unclear:** none"):
            self.assertEqual(items(f"{line}\n\n**Problems:** none\n"), [], line)

    def test_a_label_line_reading_none_and_more_gives_the_whole_text(self) -> None:
        report = ("**Searches not found or unclear:** none. `refusalCodes` already holds the "
                  "codes, so no change there.\n\n**Choices:** none\n")
        self.assertEqual(items(report), [
            "none. `refusalCodes` already holds the codes, so no change there."])

    def test_a_label_in_a_list_ends_at_the_next_item_of_that_list(self) -> None:
        report = ("- **Status:** done\n- **Searches not found or unclear:**\n"
                  "  - the first search\n  - the second search\n- **Problems:** none\n")
        self.assertEqual(items(report), ["the first search", "the second search"])

    def test_a_non_list_label_section_ends_at_the_next_bold_label_or_heading(self) -> None:
        report = ("**Searches not found or unclear**\n- inside\n\n"
                  "**Own-work check.** not inside\n")
        self.assertEqual(items(report), ["inside"])
        report = "**Searches not found or unclear**\n- inside\n\n## Heading\n\n- outside\n"
        self.assertEqual(items(report), ["inside"])

    def test_a_bullet_that_starts_with_bold_text_stays_in_the_section(self) -> None:
        report = ("**Searches not found or unclear:**\n\n"
                  "- **The server's Node.js release:** unread.\n"
                  "- **What Strych does at its limit:** still no source.\n")
        self.assertEqual(items(report), [
            "**The server's Node.js release:** unread.",
            "**What Strych does at its limit:** still no source.",
        ])

    def test_the_unread_material_section_before_the_searches_is_no_item(self) -> None:
        # The report methods put **Unread material** before **Searches not found or unclear**.
        forms = (
            "- **Unread material:** the guidelines file, read in part\n"
            "- **Searches not found or unclear:**\n  - the first search\n",
            "**Unread material:** the guidelines file, read in part\n\n"
            "**Searches not found or unclear:**\n- the first search\n",
            "## Unread material\n\nthe guidelines file, read in part\n\n"
            "## Searches not found or unclear\n\n- the first search\n",
        )
        for report in forms:
            self.assertEqual(items(report), ["the first search"], report)

    def test_an_unread_material_bullet_after_a_non_list_searches_label_is_an_item(self) -> None:
        # Recorded behaviour, not a wish: a report that writes the Searches label outside a list and
        # then **Unread material** as a list item, against the order the methods give, has the
        # bullet read as an item of the Searches section. The script lists, and judges nothing.
        report = ("**Searches not found or unclear:**\n\n- item one\n\n"
                  "- **Unread material:** the file\n")
        self.assertEqual(items(report), ["item one", "**Unread material:** the file"])
        report = "**Searches not found or unclear:** none\n\n- **Unread material:** the file\n"
        self.assertEqual(items(report), ["**Unread material:** the file"])
        # The same two sections in the other forms stay apart.
        report = "**Searches not found or unclear:**\n- item one\n\n**Unread material:** the file\n"
        self.assertEqual(items(report), ["item one"])
        report = ("- **Searches not found or unclear:**\n  - item one\n"
                  "- **Unread material:** the file\n")
        self.assertEqual(items(report), ["item one"])

    def test_the_unread_material_section_never_gives_an_item_when_searches_read_none(self) -> None:
        forms = (
            "- **Unread material:** the guidelines file, read in part\n"
            "- **Searches not found or unclear:** none\n",
            "**Unread material:** a decision, read by title only\n\n"
            "**Searches not found or unclear:** none\n",
        )
        for report in forms:
            self.assertEqual(items(report), [], report)

    def test_paragraphs_separated_by_blank_lines_are_separate_items(self) -> None:
        report = "## Searches not found or unclear\n\nFirst line\nof one.\n\nSecond item.\n"
        self.assertEqual(items(report), ["First line of one.", "Second item."])

    def test_a_paragraph_after_a_list_is_an_item_of_its_own(self) -> None:
        report = ("## Searches not found or unclear\n\n- one\n- two\n\n"
                  "A paragraph after the list.\n")
        self.assertEqual(items(report), ["one", "two", "A paragraph after the list."])

    def test_sub_bullets_belong_to_their_item(self) -> None:
        report = ("## Searches not found or unclear\n\n- Parent item:\n  - child one\n"
                  "  - child two\n- Next item\n")
        self.assertEqual(items(report), ["Parent item: - child one - child two", "Next item"])

    def test_a_numbered_list_and_star_bullets_give_items(self) -> None:
        report = "## Searches not found or unclear\n\n1. one\n2. two\n* three\n"
        self.assertEqual(items(report), ["one", "two", "three"])

    def test_a_mention_of_the_section_in_prose_is_no_section(self) -> None:
        report = ("**Status:** done with concerns (see Searches not found or unclear)\n\n"
                  "None. Each fact became a check (see *Searches not found or unclear*), and the "
                  "design stands.\n\nThe reviewer names it in *Searches not found* too.\n")
        self.assertEqual(items(report), [])

    def test_a_section_inside_fenced_code_is_no_section(self) -> None:
        report = ("```\n## Searches not found or unclear\n\n- shown as an example\n```\n\n"
                  "## Searches not found or unclear\n\n- the real item\n")
        self.assertEqual(items(report), ["the real item"])

    def test_a_heading_inside_fenced_code_does_not_end_the_section(self) -> None:
        report = ("## Searches not found or unclear\n\n- before\n\n```\n## not a heading\n```\n\n"
                  "- after\n")
        self.assertEqual(items(report), ["before ``` ## not a heading ```", "after"])

    def test_two_sections_in_one_report_give_both(self) -> None:
        report = ("## Searches not found or unclear\n\n- first\n\n## Other\n\ntext\n\n"
                  "**Searches not found or unclear:**\n- second\n")
        self.assertEqual(items(report), ["first", "second"])

    def test_a_report_with_windows_line_ends_is_read(self) -> None:
        report = "## Searches not found or unclear\r\n\r\n- one\r\n  wrapped\r\n- two\r\n"
        self.assertEqual(items(report), ["one wrapped", "two"])

    def test_a_report_without_the_section_gives_nothing(self) -> None:
        self.assertEqual(items("# Report\n\n## Checks\n\n- exit 0\n"), [])
        self.assertEqual(items(""), [])

    def test_a_thematic_break_in_a_section_is_no_item(self) -> None:
        for rule in ("---", "***", "___", "- - -", "* * *"):
            report = f"## Searches not found or unclear\n\n- first\n\n{rule}\n\n- second\n"
            self.assertEqual(items(report), ["first", "second"], rule)
            report = f"## Searches not found or unclear\n\n- first\n\n{rule}\n"
            self.assertEqual(items(report), ["first"], rule)

    def test_a_bold_label_on_a_second_line_of_a_paragraph_opens_no_section(self) -> None:
        self.assertEqual(items("A paragraph that goes on\n"
                               "**Searches not found or unclear:** an item\n"), [])
        self.assertEqual(items("A paragraph\n**Searches not found or unclear:**\n- an item\n"), [])

    def test_a_bold_label_right_after_a_heading_or_a_rule_opens_a_section(self) -> None:
        self.assertEqual(items("# T\n**Searches not found or unclear:** x\n"), ["x"])
        self.assertEqual(items("text\n\n---\n**Searches not found or unclear:** x\n"), ["x"])

    def test_a_bold_label_right_after_a_code_block_opens_a_section(self) -> None:
        report = "```\ncode\n```\n**Searches not found or unclear:** an item\n"
        self.assertEqual(items(report), ["an item"])

    def test_two_bold_labels_on_consecutive_lines_are_both_read(self) -> None:
        report = ("**Unread material:** the file\n"
                  "**Searches not found or unclear:**\n- the first search\n")
        self.assertEqual(items(report), ["the first search"])
        report = ("**Searches not found or unclear:** first\n"
                  "**Searches not found or unclear:** second\n")
        self.assertEqual(items(report), ["first", "second"])


class RemarkBlockTest(unittest.TestCase):
    def blocks(self, text: str) -> list[str]:
        return remarks_check.remark_blocks(text)

    def test_a_list_item_with_indented_lines_under_it_is_one_block(self) -> None:
        text = ("- Questions: none\n"
                "- Process remarks on the-way:\n"
                "  - `make-change`, `reports/02-author-report.md`: an item\n"
                "    that wraps.\n"
                "\n"
                "  - `review-change`, `reports/04-report.md`: another\n")
        found = self.blocks(text)
        self.assertEqual(len(found), 1)
        self.assertIn("an item\n    that wraps.", found[0])
        self.assertIn("another", found[0])
        self.assertNotIn("Questions", found[0])

    def test_the_block_ends_at_a_line_not_indented_deeper_than_its_marker(self) -> None:
        text = ("- Process remarks on the-way:\n  - inside\n- Writes to the backlog: outside\n")
        found = self.blocks(text)
        self.assertEqual(len(found), 1)
        self.assertIn("inside", found[0])
        self.assertNotIn("outside", found[0])

    def test_a_heading_block_runs_to_the_next_heading_of_its_rank_or_higher(self) -> None:
        text = ("## Process remarks\n\n- one\n\n### Sub\n\n- two\n\n## Next\n\n- outside\n")
        found = self.blocks(text)
        self.assertEqual(len(found), 1)
        self.assertIn("two", found[0])
        self.assertNotIn("outside", found[0])

    def test_a_paragraph_block_runs_to_the_first_blank_line(self) -> None:
        text = "Process remarks of the orchestrator: first\nsecond line\n\nunrelated\n"
        found = self.blocks(text)
        self.assertEqual(found, ["Process remarks of the orchestrator: first\nsecond line"])

    def test_the_other_openings_the_digest_accepts_open_a_block(self) -> None:
        for opening in ("Process remark", "Process improvements to consider",
                        "Other process remarks",
                        "Searches not found or unclear", "process REMARKS"):
            self.assertEqual(len(self.blocks(f"- {opening}:\n  - x\n")), 1, opening)

    def test_text_that_only_mentions_process_remarks_opens_nothing(self) -> None:
        self.assertEqual(self.blocks("- Writes: see the process remarks below\n"), [])

    def test_a_block_after_a_blank_line_and_a_sibling_item_is_a_lead_in(self) -> None:
        text = "- Process remarks on the-way: below\n\n- first\n- second\n\n## Next\n"
        found = self.blocks(text)
        self.assertEqual(len(found), 1)
        self.assertIn("second", found[0])


def write_record(root: Path, cycle: str | None, reports: dict[str, str],
                 name: str = "record") -> Path:
    record = root / name
    record.mkdir()
    if cycle is not None:
        (record / "cycle.md").write_text(cycle, encoding="utf-8")
    if reports:
        (record / "reports").mkdir()
        for name, text in reports.items():
            (record / "reports" / name).write_text(text, encoding="utf-8")
    return record


def section(*lines: str) -> str:
    return "## Searches not found or unclear\n\n" + "\n".join(f"- {line}" for line in lines) + "\n"


def cycle_with(*entries: str) -> str:
    body = "".join(f"  - {entry}\n" for entry in entries)
    return f"# Cycle record\n\n- Process remarks on the-way:\n{body}"


def run_main(arguments: list[str]) -> tuple[int, str, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = remarks_check.main(arguments)
    return code, stdout.getvalue(), stderr.getvalue()


class CommandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def record(self, cycle: str | None, reports: dict[str, str]) -> str:
        self.made = getattr(self, "made", 0) + 1
        return str(write_record(self.root, cycle, reports, f"record{self.made}"))

    def listing(self, out: str) -> list[str]:
        return [line for line in out.splitlines() if not line.startswith("checked: ")]

    def test_items_the_remarks_hold_word_for_word_give_exit_zero(self) -> None:
        record = self.record(
            cycle_with("`make-change`, reports/02-author-report.md: item one",
                       "`review-change`, reports/04-review-report.md: item two"),
            {"02-author-report.md": section("item one", "none"),
             "04-review-report.md": section("item two")})
        code, out, err = run_main([record])
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(self.listing(out), [])
        self.assertTrue(out.splitlines()[-1].startswith("checked: "), out)

    def test_a_report_without_the_section_gives_no_item_and_exit_zero(self) -> None:
        record = self.record(cycle_with("none"), {
            "02-author-report.md": "# Report\n\n## Checks\n\n- `python -B x.py` exit 0\n"})
        code, out, err = run_main([record])
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(self.listing(out), [])
        self.assertEqual(out.splitlines()[-1], "checked: 1 reports, 0 items other than none, "
                         "0 not in the process remarks")

    def test_a_missing_item_is_listed_with_its_report_path_and_exit_one(self) -> None:
        record = self.record(
            cycle_with("`make-change`, reports/02-author-report.md: item one"),
            {"02-author-report.md": section("item one", "item the remarks lack"),
             "04-review-report.md": section("none")})
        code, out, err = run_main([record])
        self.assertEqual((code, err), (1, ""))
        self.assertEqual(self.listing(out),
                         [f"{Path(record).as_posix()}/reports/02-author-report.md: "
                          "item the remarks lack"])

    def test_an_item_beside_none_rows_is_listed(self) -> None:
        # The form of the plomyk archive: three rows reading none, one item beside them.
        report = ("## Searches not found or unclear\n\n"
                  "- Other projected entries: none besides the two above.\n"
                  "- A source outside the product: none found.\n"
                  "- Unclear: whether the last sentence needs code today.\n")
        record = self.record(cycle_with("`x`, p: Other projected entries: none besides the two "
                                        "above.", "`x`, p: A source outside the product: none "
                                        "found."),
                             {"06-return-step-report.md": report})
        code, out, _ = run_main([record])
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), [
            f"{Path(record).as_posix()}/reports/06-return-step-report.md: "
            "Unclear: whether the last sentence needs code today."])

    def test_the_match_ignores_how_lines_are_wrapped_and_indented(self) -> None:
        cycle = ("# Record\n\n- Process remarks on the-way:\n"
                 "  - `stage`, report: Unclear: whether the table is\n"
                 "      meant to be complete.\n")
        record = self.record(cycle, {"01-report.md":
                                     "## Searches not found or unclear\n\n"
                                     "- Unclear: whether the table\n  is meant to be complete.\n"})
        self.assertEqual(run_main([record])[0], 0)

    def test_the_match_is_exact_in_words_and_in_case(self) -> None:
        for changed in ("Unclear: whether the table is meant to be complete",
                        "Unclear: whether the table is meant to be done.",
                        "unclear: whether the table is meant to be complete."):
            record = self.record(cycle_with(f"`s`, p: {changed}"), {
                "01-report.md": section("Unclear: whether the table is meant to be complete.")})
            self.assertEqual(run_main([record])[0], 1, changed)

    def test_an_item_that_stands_outside_the_remarks_block_does_not_count(self) -> None:
        cycle = ("# Record\n\n## Events\n\n| 1 | the item lives here |\n\n"
                 "- Process remarks on the-way: none\n")
        record = self.record(cycle, {"01-report.md": section("the item lives here")})
        code, out, _ = run_main([record])
        self.assertEqual(code, 1)
        self.assertEqual(len(self.listing(out)), 1)

    def test_a_record_with_no_remarks_block_lists_every_item(self) -> None:
        record = self.record("# Record\n\nnothing\n",
                             {"01-report.md": section("one", "two")})
        code, out, _ = run_main([record])
        self.assertEqual(code, 1)
        self.assertEqual(len(self.listing(out)), 2)

    def test_a_repeated_item_must_stand_once_for_each_report_that_gives_it(self) -> None:
        repeated = "A word used against its glossary entry: none found."
        record = self.record(cycle_with(f"`a`, 01: {repeated}"),
                             {"01-report.md": section(repeated), "02-report.md": section(repeated)})
        code, out, _ = run_main([record])
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out),
                         [f"{Path(record).as_posix()}/reports/02-report.md: {repeated}"])
        record = self.record(cycle_with(f"`a`, 01: {repeated}", f"`b`, 02: {repeated}"),
                             {"01-report.md": section(repeated), "02-report.md": section(repeated)})
        self.assertEqual(run_main([record])[0], 0)

    def test_files_that_are_no_reports_are_not_read(self) -> None:
        text = section("an item in a file that is no report")
        record = self.record(cycle_with("none"), {
            "01-author-handoff.md": text, "handoff_author.md": text,
            "slice-1-findings.md": text, "notes.txt": text, "gate.log": text,
            "02-report.md.bak": text, "01-report.md": section("none")})
        self.assertEqual(run_main([record])[0], 0)

    def test_every_md_file_whose_name_holds_neither_handoff_nor_findings_is_read(self) -> None:
        record = self.record(cycle_with("none"), {
            "review_whole.md": section("read in review whole"),
            "planner-report.md": section("read in planner report"),
            "01-author-handoff.md": section("not read in author handoff"),
            "handoff_author.md": section("not read in handoff author"),
            "slice-1-findings.md": section("not read in slice findings"),
            "notes.txt": section("not read in notes"),
            "gate.log": section("not read in gate log")})
        code, out, _ = run_main([record])
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), [
            f"{Path(record).as_posix()}/reports/planner-report.md: read in planner report",
            f"{Path(record).as_posix()}/reports/review_whole.md: read in review whole"])

    def test_reports_are_read_in_the_order_of_their_names(self) -> None:
        record = self.record("# Record\n", {"10-b-report.md": section("second"),
                                            "02-a-report.md": section("first")})
        _, out, _ = run_main([record])
        self.assertEqual([line.rsplit(": ", 1)[1] for line in self.listing(out)],
                         ["first", "second"])

    def test_a_record_with_no_reports_directory_lists_nothing(self) -> None:
        record = self.record("# Record\n", {})
        code, out, err = run_main([record])
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(self.listing(out), [])

    def test_a_missing_cycle_file_or_a_wrong_argument_exits_two(self) -> None:
        record = self.record(None, {"01-report.md": section("one")})
        for arguments in ([record], [], [record, "extra"], [str(self.root / "absent")]):
            code, out, err = run_main(arguments)
            self.assertEqual(code, 2, arguments)
            self.assertEqual(out, "")
            self.assertTrue(err.startswith("Error: "), err)

    def test_a_file_that_is_not_utf8_exits_two(self) -> None:
        record = self.record("# Record\n", {"01-report.md": section("one")})
        (Path(record) / "reports" / "02-report.md").write_bytes("zażółć".encode("cp1250"))
        code, out, err = run_main([record])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertTrue(err.startswith("Error: "), err)

    def test_a_byte_order_mark_at_the_start_of_a_file_is_ignored(self) -> None:
        # The section opens the report, so a mark left in the text would hide it.
        record = self.record("# Record\n", {})
        (Path(record) / "reports").mkdir()
        (Path(record) / "reports" / "01-report.md").write_bytes(
            "## Searches not found or unclear\n\n- item one\n".encode("utf-8-sig"))
        code, out, _ = run_main([record])
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out),
                         [f"{Path(record).as_posix()}/reports/01-report.md: item one"])

    def test_the_script_writes_no_file(self) -> None:
        record = self.record("# Record\n", {"01-report.md": section("one")})
        before = sorted(path.name for path in self.root.rglob("*"))
        run_main([record])
        self.assertEqual(sorted(path.name for path in self.root.rglob("*")), before)


class TemplateTest(unittest.TestCase):
    def test_the_templates_remarks_block_is_one_the_script_cuts_and_reads(self) -> None:
        text = TEMPLATE.read_text(encoding="utf-8")
        tail = text[text.index("- Process remarks on the-way:"):]
        blocks = remarks_check.remark_blocks(tail)
        self.assertEqual(len(blocks), 1)
        entry = "`stage`, `path/report.md`: Unclear: a thing"
        filled = tail.split("\n", 1)[0] + "\n  - " + entry + "\n"
        self.assertIn(entry, remarks_check.remark_blocks(filled)[0])


if __name__ == "__main__":
    unittest.main()
