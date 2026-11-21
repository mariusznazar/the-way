"""Tests of the versions of the process: their series, their three questions and the measures
of each version, moved here from process-audit/test_audit_count.py to keep that file readable;
the fixtures they use are imported from it."""

import subprocess
import sys
from pathlib import Path

from test_audit_count import (
    GATE,
    GIT_ENV,
    MEASURES,
    MEASURE_LABELS,
    MEASURE_VALUES,
    PIN,
    STAGE_MODULE,
    STAGE_SCRIPT,
    STAGES_HEADER,
    TEST_PRICES,
    AuditCountCase,
    Repository,
    gate_file,
    gate_row,
    measures_file,
    older_row,
    older_stages,
    record,
    register_text,
    split_row,
    stage_row,
)

HERE = Path(__file__).resolve().parent


NL = chr(10)

# Q1 of a group is the number of its cycles that answer yes, the number that answer no and the
# number that answer unknown, never one word (WAY-417, row 3 of the settlements of the task). These
# are the cell of a version of one cycle that answers yes, no and unknown; a version of several
# cycles shows each count written out.
Q1_YES = "yes 1 · no 0 · unknown 0"
Q1_NO = "yes 0 · no 1 · unknown 0"
Q1_UNKNOWN = "yes 0 · no 0 · unknown 1"


def process_record(
    pin,
    discarded="none",
    plan="none on the one-author route",
    too_large="none",
    rounds="none",
    extra="",
) -> str:
    """A cycle record whose items the questions of a process version read; `extra` adds lines
    under the status line, for a doubled item."""
    items = (
        f"- Discarded attempt: {discarded}\n- Plan: {plan}\n"
        f"- Slices returned too large: {too_large}\n- Review rounds: {rounds}\n{extra}"
    )
    return record(pin_line=f"- Process pin: `{pin}`").replace(
        "- Status: request open\n", "- Status: request open\n" + items
    )


class VersionsCase(AuditCountCase):
    """The reading of the two tables under the heading of a series: the image of all its cycles
    and, after it, the table with a row for each version (WAY-417)."""

    def tables(self, kind, number) -> list[tuple[list[str], list[list[str]]]]:
        """The tables under `### <kind>, series <number>` of the latest result, each as its header
        cells and its rows."""
        text = self.latest()
        heading = f"\n### {kind}, series {number}\n"
        self.assertIn(heading, text, "the result has no such series")
        part = text.split(heading, 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
        found: list[list[str]] = []
        inside = False
        for line in part.splitlines():
            if line.startswith("|"):
                if not inside:
                    found.append([])
                found[-1].append(line)
            inside = line.startswith("|")
        self.assertEqual(2, len(found), "a series holds its image and its table of versions")
        return [(split_row(lines[0]), [split_row(line) for line in lines[2:]]) for lines in found]

    def section(self, kind, number) -> list[list[str]]:
        """The rows of the table of the versions of a series, which stands after its image."""
        return self.tables(kind, number)[1][1]

    def image(self, kind, number) -> list[list[str]]:
        """The rows of the image of a series, which stands first under its heading."""
        return self.tables(kind, number)[0][1]


class ProcessVersions(VersionsCase):
    """The process versions, their series and the three questions (WAY-339)."""

    FIRST = 1759968000  # 2025-10-09, UTC midnight
    LATER = 1760054400  # 2025-10-10
    MARCH = 1772323200  # 2026-03-01
    BASE_FILES = {
        "README.md": "the-way\n",
        "task-cycle/change/SKILL.md": "change\n",
        "task-cycle/cycle_stages.py": "stages\n",
    }

    def the_way(self) -> Repository:
        way = self.repository("the-way")
        return way

    def version_at(self, way, when, parent=None, changed=None) -> str:
        """A commit of the-way dated `when`: the base files, with the files of `changed` replaced
        or added."""
        way.time = when - 3600
        files = {**self.BASE_FILES, **(changed or {})}
        return way.commit(files, f"Version at {when}", *([parent] if parent else []))

    def stages_of(self, tokens) -> str:
        return STAGES_HEADER + stage_row(1, "orchestrator", "model-a", tokens, 0, 0)

    def add_cycles(self, product, specs) -> None:
        """Each cycle as (folder, record text, tokens), chained so that all stay in the history;
        a fourth item is the text of its `stages.md`, where it is not the newer form."""
        parent = product.commit({"README.md": "a product\n"}, "Start")
        for folder, text, tokens, *stages in specs:
            _, parent = product.cycle(
                folder,
                {"cycle.md": text, "stages.md": stages[0] if stages else self.stages_of(tokens)},
                parent=parent,
                branch=None,
            )
        product.branch("main", parent)

    def run_versions(self, way, product, prices=TEST_PRICES):
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        test_prices = self.home / "prices.md"
        test_prices.write_text(prices, encoding="utf-8")
        done = self.run_count("--prices", str(test_prices), "--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)

    def cost_series(self, number) -> list[list[str]]:
        """The rows of a series of the cost: version, day, cycles, cycles with a known cost, median
        cost and Q3."""
        return self.section("Cost", number)

    def count_series(self, number) -> list[list[str]]:
        """The rows of a series of the count of remarks: version, day, cycles, Q1, plans read and
        Q2."""
        return self.section("Count of remarks", number)

    def test_the_cost_is_compared_inside_a_series_of_the_cost_across_a_new_class(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # v1 and v2 share a series of both kinds; a class added on the day of v3 starts a series of
        # the count of remarks and none of the cost. Medians: v1 is (2 + 4) / 2 = 3 dollars, v2 is
        # 1 dollar, v3 is 0.5 dollar. v2 falls against v1, and so does v3 against v2 (0.5 < 1):
        # the cost of v3 is compared with v2's, the count of remarks of v3 is not.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.LATER, parent=v1)
        v3 = self.version_at(way, self.MARCH, parent=v2)
        product = self.repository()
        self.add_cycles(
            product,
            [
                ("one", process_record(v1), 1_000_000),
                ("two", process_record(v1), 2_000_000),
                ("three", process_record(v2), 500_000),
                ("four", process_record(v3), 250_000),
                ("five", process_record("none"), 100),
            ],
        )
        # The class is added on the day of v3, which counts as between the two versions.
        self.register.write_text(
            register_text(classes=["| sharp | x | 2026-03-01 | none |"]), encoding="utf-8"
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "2025-10-09", "2", "2", "3.000000", "unknown"],
                [v2, "2025-10-10", "1", "1", "1.000000", "yes"],
                [v3, "2026-03-01", "1", "1", "0.500000", "yes"],
            ],
            self.cost_series(1),
        )
        self.assertNotIn("### Cost, series 2", self.latest())
        # The expected Q1 changes with the requirement (WAY-417, row 3): the cell of a version is
        # the numbers of its cycles that answer yes, no and unknown, where it was the word `no`
        # for a version whose cycles all answer no. v1 has two such cycles, v2 and v3 one each.
        self.assertEqual(
            [
                [v1, "2025-10-09", "2", "yes 0 · no 2 · unknown 0", "0 of 0", "unknown"],
                [v2, "2025-10-10", "1", Q1_NO, "0 of 0", "unknown"],
            ],
            self.count_series(1),
        )
        self.assertEqual(
            [[v3, "2026-03-01", "1", Q1_NO, "0 of 0", "unknown"]], self.count_series(2)
        )
        self.assertIn("### No version", self.latest())
        self.assertIn("## Process versions", self.latest())
        self.assertIn(
            "Begins at this version: the register's list of classes changed between "
            "the two versions.",
            self.latest(),
        )

    def test_no_row_of_a_series_of_one_kind_holds_a_figure_of_the_other(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # A table of the cost holds the median and Q3 and none of Q1 and Q2; a table of the count
        # of remarks holds Q1 and Q2 and none of the cost.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(product, [("one", process_record(v1), 1_000_000)])
        self.run_versions(way, product)
        text = self.latest()
        parts = []
        for heading in ("\n### Cost, series 1\n", "\n### Count of remarks, series 1\n"):
            self.assertIn(heading, text)
            parts.append(text.split(heading, 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0])
        cost, count = parts
        for name in ("Median cost (USD)", "Q3: cost falls"):
            self.assertIn(name, cost)
            self.assertNotIn(name, count)
        for name in ("Q1: contradiction only after code", "Q2: more than a third", "Plans read"):
            self.assertIn(name, count)
            self.assertNotIn(name, cost)

    def test_a_change_under_the_change_starts_a_series_of_the_count_and_none_of_the_cost(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # task-cycle/change is one of the files the form of a stage report is taken from; v2's
        # cost (0.5) falls against v1's (2) in a series of the cost that the change does not end.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way, self.LATER, parent=v1, changed={"task-cycle/change/SKILL.md": "changed\n"}
        )
        product = self.repository()
        self.add_cycles(
            product, [("one", process_record(v1), 1_000_000), ("two", process_record(v2), 250_000)]
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "2025-10-09", "1", "1", "2.000000", "unknown"],
                [v2, "2025-10-10", "1", "1", "0.500000", "yes"],
            ],
            self.cost_series(1),
        )
        self.assertNotIn("### Cost, series 2", self.latest())
        # The expected Q1 changes with the requirement (WAY-417, row 3): the numbers of the one
        # cycle of each version, which answers no, where the cell was the word `no`.
        self.assertEqual(
            [[v1, "2025-10-09", "1", Q1_NO, "0 of 0", "unknown"]], self.count_series(1)
        )
        self.assertEqual(
            [[v2, "2025-10-10", "1", Q1_NO, "0 of 0", "unknown"]], self.count_series(2)
        )

    def test_a_change_under_the_review_starts_a_series_of_the_count_and_none_of_the_cost(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # The reviewer's instructions: a change of `task-cycle/review` ends the count of remarks
        # and none of the cost, whose median of v2 (0.5) is compared with v1's (2).
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way, self.LATER, parent=v1, changed={"task-cycle/review/SKILL.md": "reviewer\n"}
        )
        product = self.repository()
        self.add_cycles(
            product, [("one", process_record(v1), 1_000_000), ("two", process_record(v2), 250_000)]
        )
        self.run_versions(way, product)
        self.assertEqual(["unknown", "yes"], [row[5] for row in self.cost_series(1)])
        self.assertNotIn("### Cost, series 2", self.latest())
        self.assertEqual(
            [[v1], [v2]], [[row[0] for row in self.count_series(number)] for number in (1, 2)]
        )
        self.assertIn(
            "Begins at this version: `task-cycle/review` changed between the two versions.",
            self.latest(),
        )

    def test_a_change_of_the_reviewers_type_of_agent_starts_a_series_of_the_count_alone(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # `the-way-stage.md` is the instruction the reviewer receives: a change of it ends the
        # count of remarks and none of the cost. A change of `the-way-author.md`, beside it in
        # the same folder, ends neither.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way,
            self.LATER,
            parent=v1,
            changed={"task-cycle/agent-types/the-way-stage.md": "reviewer\n"},
        )
        v3 = self.version_at(
            way,
            self.MARCH,
            parent=v2,
            changed={
                "task-cycle/agent-types/the-way-stage.md": "reviewer\n",
                "task-cycle/agent-types/the-way-author.md": "author\n",
            },
        )
        product = self.repository()
        self.add_cycles(
            product,
            [
                ("one", process_record(v1), 1_000_000),
                ("two", process_record(v2), 500_000),
                ("three", process_record(v3), 250_000),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(["unknown", "yes", "yes"], [row[5] for row in self.cost_series(1)])
        self.assertNotIn("### Cost, series 2", self.latest())
        self.assertEqual(
            [[v1], [v2, v3]], [[row[0] for row in self.count_series(number)] for number in (1, 2)]
        )
        self.assertNotIn("### Count of remarks, series 3", self.latest())
        self.assertIn(
            "Begins at this version: `task-cycle/agent-types/the-way-stage.md` changed "
            "between the two versions.",
            self.latest(),
        )

    def test_a_change_of_the_stage_script_starts_a_series_of_both_kinds(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(
            way, self.LATER, parent=v1, changed={"task-cycle/cycle_stages.py": "changed\n"}
        )
        product = self.repository()
        self.add_cycles(
            product, [("one", process_record(v1), 1_000_000), ("two", process_record(v2), 250_000)]
        )
        self.run_versions(way, product)
        self.assertEqual([[v1, "2025-10-09", "1", "1", "2.000000", "unknown"]], self.cost_series(1))
        self.assertEqual([[v2, "2025-10-10", "1", "1", "0.500000", "unknown"]], self.cost_series(2))
        self.assertEqual(
            [[v1], [v2]], [[row[0] for row in self.count_series(number)] for number in (1, 2)]
        )
        self.assertEqual(
            2,
            self.latest().count(
                "Begins at this version: "
                "`task-cycle/cycle_stages.py` changed between the "
                "two versions."
            ),
        )

    def test_a_cycle_that_changed_the_stage_script_stays_in_its_version_with_no_known_cost(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # The cycle stays in the version it ran on and in its series: its row counts it, its
        # answers are those of the record, and only its cost is out of the median. Unchanged, the
        # same cycle costs 1,000,000 * 2 / 1,000,000 = 2 dollars.
        day = "2025-10-09"
        for changed, cost, known in (
            ({STAGE_SCRIPT: "version two\n"}, "unknown", "0"),
            ({STAGE_MODULE: "version two\n"}, "unknown", "0"),
            ({}, "2.000000", "1"),
        ):
            with self.subTest(sorted(changed)):
                self.fresh()
                _, version = self.own_cycle(
                    {"stages.md": self.stages_of(1_000_000)}, changed, process_record(PIN)
                )
                done = self.run_with_prices()
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertEqual([[version, day, "1", known, cost, "unknown"]], self.cost_series(1))
                # The expected Q1 changes with the requirement (WAY-417, row 3): the numbers of
                # the one cycle, which answers no, where the cell was the word `no`.
                self.assertEqual(
                    [[version, day, "1", Q1_NO, "0 of 0", "unknown"]], self.count_series(1)
                )
                self.assertNotIn("### Cost, series 2", self.latest())

    # Each path, with whether a change of the file starts a series of the cost and of the count of
    # remarks, and the reason the count gives: the files of the count are named by the path of the
    # list (a folder, or the one file), and the stage script stands in both.
    BOUNDARIES = (
        ("task-cycle/change/SKILL.md", False, "`task-cycle/change`"),
        ("task-cycle/plan/SKILL.md", False, "`task-cycle/plan`"),
        ("task-cycle/review/SKILL.md", False, "`task-cycle/review`"),
        ("task-cycle/spec/SKILL.md", False, "`task-cycle/spec`"),
        (
            "task-cycle/agent-types/the-way-stage.md",
            False,
            "`task-cycle/agent-types/the-way-stage.md`",
        ),
        ("task-cycle/cycle_stages.py", True, "`task-cycle/cycle_stages.py`"),
        ("task-cycle/stage_transcripts.py", True, "`task-cycle/stage_transcripts.py`"),
        # Files that start neither: the other type of agent, the other scripts, the rest of the
        # method of the cycle and a file of another part.
        ("task-cycle/agent-types/the-way-author.md", False, None),
        ("task-cycle/cycle_measures.py", False, None),
        ("task-cycle/gate_times.py", False, None),
        ("gate/run_tests.py", False, None),
        ("task-cycle/skill/SKILL.md", False, None),
        ("README.md", False, None),
    )

    def two_versions(self, name, path):
        """Two commits of a temporary the-way that hold every file of BOUNDARIES, the second with
        `path` changed (None: unchanged), as the versions the audit compares, and the Ancestry that
        reads the repository."""
        sys.path.insert(0, str(HERE))
        from audit_shared import Git
        from version_analysis import Ancestry, Version

        way = self.repository(name)
        files = {listed: "a\n" for listed, _, _ in self.BOUNDARIES}
        first = way.commit(files, "First")
        second = way.commit({**files, **({path: "b\n"} if path else {})}, "Second", first)
        return (
            Version(first, 1, "2025-10-09", "2026-01-01", []),
            Version(second, 2, "2025-10-10", "2026-01-01", []),
            Ancestry(Git(way.root)),
        )

    def test_each_file_starts_the_series_of_its_own_kind_and_no_other(self):
        sys.path.insert(0, str(HERE))
        from problem_register import Register
        from version_analysis import cost_boundary, count_boundary

        for number, (path, in_cost, reason) in enumerate(self.BOUNDARIES):
            with self.subTest(path):
                earlier, later, ancestry = self.two_versions(f"way-{number}", path)
                cost = cost_boundary(earlier, later, ancestry)
                count = count_boundary(earlier, later, Register(), ancestry)
                if reason is None:
                    self.assertIsNone(cost)
                    self.assertIsNone(count)
                    continue
                expected = f"{reason} changed between the two versions"
                self.assertEqual(expected if in_cost else None, cost)
                self.assertEqual(expected, count)

    def test_two_identical_versions_share_a_series_of_each_kind(self):
        sys.path.insert(0, str(HERE))
        from problem_register import Register
        from version_analysis import cost_boundary, count_boundary

        earlier, later, ancestry = self.two_versions("way-same", None)
        self.assertIsNone(cost_boundary(earlier, later, ancestry))
        self.assertIsNone(count_boundary(earlier, later, Register(), ancestry))

    def test_a_date_of_the_list_of_classes_starts_a_series_of_the_count_alone(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        sys.path.insert(0, str(HERE))
        from problem_register import Register
        from version_analysis import cost_boundary, count_boundary

        earlier, later, ancestry = self.two_versions("way-classes", None)
        known = Register(class_dates=["2025-10-10"])
        self.assertIsNone(cost_boundary(earlier, later, ancestry))
        self.assertEqual(
            "the register's list of classes changed between the two versions",
            count_boundary(earlier, later, known, ancestry),
        )
        # A date after the two versions, and one before them, divide nothing.
        for days in (["2025-10-08"], ["2025-10-11"]):
            with self.subTest(days):
                self.assertIsNone(
                    count_boundary(earlier, later, Register(class_dates=days), ancestry)
                )
        unknown = Register(class_dates_unknown=True)
        self.assertIsNone(cost_boundary(earlier, later, ancestry))
        self.assertIn("not given in full", count_boundary(earlier, later, unknown, ancestry))

    def test_a_git_that_cannot_compare_the_two_versions_counts_as_a_change_of_both_kinds(self):
        # Versions that the checkout does not hold: `git diff --quiet` ends with exit 128, and a
        # series is never joined by mistake.
        sys.path.insert(0, str(HERE))
        from problem_register import Register
        from version_analysis import Version, cost_boundary, count_boundary

        _, _, ancestry = self.two_versions("way-failing", None)
        earlier = Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = Version("b" * 40, 2, "2025-10-10", "2026-01-01", [])
        # Git cannot tell which file changed, so the reason names each file of the script that
        # measures the cost: `cycle_stages.py` and the module `stage_transcripts.py` it imports
        # (WAY-339); the expected value changes with that cause (WAY-233).
        stage = (
            "`task-cycle/cycle_stages.py` and `task-cycle/stage_transcripts.py` "
            "changed between the two versions"
        )
        self.assertEqual(stage, cost_boundary(earlier, later, ancestry))
        self.assertEqual(stage, count_boundary(earlier, later, Register(), ancestry))

    def test_each_path_that_starts_a_series_is_a_path_git_tracks(self):
        # Break caught: a rename of one of these files while the audit keeps the old path: the
        # history of a path that does not exist is empty, so no change would ever start a series.
        sys.path.insert(0, str(HERE))
        from version_analysis import COST_SCRIPTS, COUNT_PATHS

        for path in (*COST_SCRIPTS, *COUNT_PATHS):
            with self.subTest(path):
                done = subprocess.run(
                    ["git", "-C", str(HERE.parent), "ls-files", "-z", "--", ":(literal)" + path],
                    capture_output=True,
                    env=GIT_ENV,
                    check=True,
                )
                self.assertTrue(done.stdout, f"git tracks no file at {path}")
        # The script that measures the cost spans two files, `cycle_stages.py` and the module
        # `stage_transcripts.py` it imports, since the reading of the transcripts moved out of
        # `cycle_stages.py` (WAY-339, `audit-series-script-paths`); the expected value changes with
        # that cause (WAY-233).
        self.assertEqual(
            ("task-cycle/cycle_stages.py", "task-cycle/stage_transcripts.py"), COST_SCRIPTS
        )
        self.assertEqual(
            (
                "task-cycle/change",
                "task-cycle/plan",
                "task-cycle/review",
                "task-cycle/spec",
                "task-cycle/agent-types/the-way-stage.md",
            ),
            COUNT_PATHS,
        )

    def test_the_older_and_the_newer_form_of_the_stage_report_are_never_in_one_comparison(self):
        # decision: WAY-339 "A new series of the cost of cycles, the two numbers of WAY-337"
        # The form changes with `cycle_stages.py`, a file whose change starts a series of both
        # kinds; a change of the scripts that measure the mechanism or the gate does not. v1 to v3
        # are of the older form, v4 of the newer; the costs are 2, 1, 0.5 and 0.25 dollars. The
        # median of v4 is not set against v3's: it begins its own series.
        way = self.the_way()
        measures = {"task-cycle/cycle_measures.py": "measures\n"}
        gate = {**measures, "task-cycle/gate_times.py": "gate\n"}
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.FIRST + 86400, parent=v1, changed=measures)
        v3 = self.version_at(way, self.FIRST + 2 * 86400, parent=v2, changed=gate)
        v4 = self.version_at(
            way,
            self.FIRST + 3 * 86400,
            parent=v3,
            changed={**gate, "task-cycle/cycle_stages.py": "newer form\n"},
        )
        product = self.repository()

        def older(tokens):
            return older_stages(older_row("model-a", tokens, 0, 0))

        self.add_cycles(
            product,
            [
                ("one", process_record(v1), 1_000_000, older(1_000_000)),
                ("two", process_record(v2), 500_000, older(500_000)),
                ("three", process_record(v3), 250_000, older(250_000)),
                ("four", process_record(v4), 125_000),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "2025-10-09", "1", "1", "2.000000", "unknown"],
                [v2, "2025-10-10", "1", "1", "1.000000", "yes"],
                [v3, "2025-10-11", "1", "1", "0.500000", "yes"],
            ],
            self.cost_series(1),
        )
        self.assertEqual([[v4, "2025-10-12", "1", "1", "0.250000", "unknown"]], self.cost_series(2))
        self.assertNotIn("### Cost, series 3", self.latest())
        self.assertEqual(
            [[v1, v2, v3], [v4]],
            [[row[0] for row in self.count_series(number)] for number in (1, 2)],
        )

    def test_the_questions_read_the_record_items_and_say_unknown_otherwise(self):
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        listed = "\n  - slice 2\n  - slice 4\n  - slice 7\n  - slice 8"
        self.add_cycles(
            product,
            [
                (
                    "reading-a",
                    process_record(
                        v1,
                        discarded="reason: `open design choice`; the spec left the field open",
                        plan="11 slices and 12 foundation entries",
                        too_large=listed,
                    ),
                    1_000_000,
                ),
                (
                    "reading-b",
                    process_record(v1, plan="3 slices", too_large="\n  - slice 1"),
                    1_000_000,
                ),
                (
                    "reading-c",
                    process_record(v1, plan="5 slices", extra="- Plan: 6 slices\n"),
                    1_000_000,
                ),
            ],
        )
        self.run_versions(way, product)
        # Q1 is yes for reading-a, from its discarded attempt, and no for the other two: the cell
        # gives the three numbers, where it gave the word `yes` for the one yes (WAY-417, row 3,
        # the cause of this expected value). Q2 is unknown: reading-c's doubled item is not read,
        # and its slices could change the share of the other two plans.
        self.assertEqual(
            [[v1, "2025-10-09", "3", "yes 1 · no 2 · unknown 0", "2 of 3", "unknown"]],
            self.count_series(1),
        )
        self.assertEqual([[v1, "2025-10-09", "3", "3", "2.000000", "unknown"]], self.cost_series(1))
        plan_reasons = [row[3] for row in self.rows("Unknown values") if row[2] == "Plan"]
        self.assertEqual(["the record holds the item `Plan` more than once"], plan_reasons)
        self.assertIn(
            "1 cycle(s) are not read",
            self.reasons_of(self.rows("Unknown values"), f"slices too large, version {v1}"),
        )

    def test_the_slices_of_every_plan_of_a_version_are_summed(self):
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        listed = "\n  - slice 2\n  - slice 4\n  - slice 7\n  - slice 8"
        self.add_cycles(
            product,
            [
                (
                    "reading-a",
                    process_record(
                        v1, plan="11 slices and 12 foundation entries", too_large=listed
                    ),
                    1_000_000,
                ),
                (
                    "reading-b",
                    process_record(v1, plan="3 slices", too_large="\n  - slice 1"),
                    1_000_000,
                ),
                ("one-author", process_record(v1), 1_000_000),
            ],
        )
        self.run_versions(way, product)
        # 4 + 1 too large of 11 + 3 planned: 15 > 14, so yes; the one-author cycle has no plan.
        self.assertEqual(["2 of 2", "yes"], self.count_series(1)[0][4:6])

    def test_the_count_of_slices_is_the_figure_just_before_the_word(self):
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (
                    "apart",
                    process_record(
                        v1, plan="reviewed by 2 agents; slices: 8", too_large="\n  - slice 1"
                    ),
                    1_000_000,
                ),
                (
                    "tight",
                    process_record(
                        v1,
                        plan="the plan has 4 slices, reviewed by 2 agents",
                        too_large="\n  - slice 1",
                    ),
                    1_000_000,
                ),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual("1 of 2", self.count_series(1)[0][4])
        self.assertEqual(
            ["the item `Plan` does not give one count of slices before the word `slices`"],
            [row[3] for row in self.rows("Unknown values") if row[2] == "Plan"],
        )

    def versions(self, way, count):
        """`count` versions of the-way dated one day apart, the first of them FIRST: each commit
        holds the base files, so they all stand in one series of the count of remarks."""
        versions = []
        for number in range(count):
            versions.append(
                self.version_at(
                    way, self.FIRST + number * 86_400, parent=versions[-1] if versions else None
                )
            )
        return versions

    def q1_of_each_version(self, texts, rounds="none"):
        """Q1 of the series of the count of remarks, version by version, where the cycle of each
        version has the text `texts[n]` as its item *Discarded attempt* and `rounds` as its item
        *Review rounds*; `rounds` may be a list of one text for each version."""
        way = self.the_way()
        versions = self.versions(way, len(texts))
        product = self.repository()
        self.add_cycles(
            product,
            [
                (
                    f"cycle-{number}",
                    process_record(
                        version,
                        discarded=texts[number],
                        rounds=rounds[number] if isinstance(rounds, list) else rounds,
                    ),
                    1_000,
                )
                for number, version in enumerate(versions)
            ],
        )
        self.run_versions(way, product)
        return [row[3] for row in self.count_series(1)]

    def test_the_marker_of_a_discarded_attempt_gives_q1(self):
        # decision: WAY-405 "The reason of a discarded attempt stands at the start of the record's item"
        # The form of `task-cycle/record_template.md`: the marker first, in backticks, then the time,
        # the report and the rest, which holds `none` in its other parts.
        rest = "; 10:32, report reports/x.md; foundation entries none; reset to abc1234"
        answers = self.q1_of_each_version(
            [
                "reason: `open design choice`" + rest,
                "reason: `reserved choice`" + rest,
                "reason: `size`" + rest,
                "none",
                NL + "  - reason: `open design choice`" + rest + NL + "  - reason: `size`; 14:05",
                NL + "  - reason: `size`; 14:05" + NL + "  - reason: `reserved choice`" + rest,
                NL + "  reason: `open design choice`" + rest + NL + "  - reason: `size`; 14:05",
                NL + "  reason: `open design choice`" + rest + NL + "  - report reports/x.md",
            ]
        )
        # Each version holds one cycle, so its cell shows that cycle's answer as three numbers,
        # where it showed the word (WAY-417, row 3, the cause of these expected values).
        self.assertEqual([Q1_YES, Q1_NO, Q1_NO, Q1_NO, Q1_YES, Q1_NO, Q1_UNKNOWN, Q1_YES], answers)

    def test_the_four_denials_of_review_100_leave_q1_unknown(self):
        # decision: WAY-405 "The audit of the process takes from this item, for its answer whether"
        # The texts are the four examples of remark 6 of the review of the foundation of 2026-11-14:
        # each names an open design choice in words and none carries the marker, so none is a yes.
        texts = (
            "open design choice not found",
            "an open design choice did not apply",
            "no sign whatsoever that this was an open design choice",
            "No attempt was discarded for a reserved choice, an oversized change or an open "
            "design choice",
        )
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (f"denial-{number}", process_record(v1, discarded=text), 1_000)
                for number, text in enumerate(texts)
            ],
        )
        self.run_versions(way, product)
        # The four cycles stand in one version, none answers: the cell counts them as unknown, and
        # no cycle is a no (WAY-417, row 3, the cause of this expected value).
        self.assertEqual("yes 0 · no 0 · unknown 4", self.count_series(1)[0][3])
        [pair] = [row for row in self.pair_rows() if row[0] == "Discarded attempt"]
        self.assertEqual("4", pair[1])
        self.assertIn("opens with no marker of its reason", pair[2])

    def test_a_marker_that_is_not_at_the_start_or_not_in_its_form_is_not_read(self):
        # decision: WAY-405 "The audit of the process takes from this item, for its answer whether"
        texts = [
            "10:32; reason: `open design choice`",
            "reason: open design choice",
            "none — reason: `size`",
            "reason: `size`; reason: `open design choice`",
        ]
        # One cycle in each version: the cell gives that cycle's answer as three numbers (WAY-417,
        # row 3, the cause of this expected value).
        self.assertEqual([Q1_UNKNOWN] * 4, self.q1_of_each_version(texts))

    def test_a_second_reason_in_a_detail_or_at_the_margin_is_not_read_and_gives_the_first_one(self):
        # decision: WAY-405 "Where the lines are sub-items at one indent alone and nothing stands beside the colon"
        # decision: WAY-405 "The item reads down to the next line at the left margin"
        # The shapes the rule names as not read: a marker in a deeper line of a sub-item, a second
        # attempt in other words than the marker among the details of the first, and a line at the
        # left margin. Each gives the answer of the first attempt, `size`, which is no contradiction.
        odc = "reason: `open design choice`"
        texts = [
            NL + "  - reason: `size`; 14:05" + NL + "    " + odc,
            NL + "  reason: `size`; 10:32" + NL + "  - reason: open design choice",
            " reason: `size`; 10:32" + NL + "  - report reports/x.md",
            NL + "  - reason: `size`; 14:05" + NL + odc,
        ]
        # One cycle in each version: the cell gives that cycle's answer as three numbers (WAY-417,
        # row 3, the cause of this expected value).
        self.assertEqual([Q1_NO] * 4, self.q1_of_each_version(texts))

    def test_the_crafted_discarded_attempts_break_no_cell_and_no_pattern(self):
        sys.path.insert(0, str(HERE))
        sys.path.insert(0, str(HERE.parent / "task-cycle"))
        import remarks_check
        from record_items import read_contradiction

        crafted = (
            ("very long", "reason: `open design choice` " + "x " * 100_000),
            ("very long before", "no " * 200_000 + "reason: `open design choice`"),
            ("long without clause marks", "x" * 500_000 + " reason: `open design choice`"),
            ("control characters", "\x1b[2J reason: `open design choice` \x00\x07 | no | x"),
            ("many markers", "reason: `size` " * 50_000),
            ("a bar", "reason: `open design choice` a | b | c"),
        )
        for label, text in crafted:
            with self.subTest(label):
                lines = remarks_check.split_lines(f"- Discarded attempt: {text}\n")
                answer, why = read_contradiction(lines, remarks_check.fenced_flags(lines))
                self.assertIn(answer, ("yes", None))
                self.assertEqual(answer is None, why is not None)
        # Run whole: no cell of the result holds a bar or a control character from the item.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (f"crafted-{number}", process_record(v1, discarded=text.replace("\n", " ")), 1_000)
                for number, (_, text) in enumerate(crafted)
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [], [char for char in self.latest() if not char.isprintable() and char != "\n"]
        )
        # Of the six crafted items two open with the marker `open design choice` and answer yes (the
        # very long one and the one with a bar); the other four give no answer that they state, so
        # the cell counts them as unknown (WAY-417, row 3, the cause of this expected value).
        self.assertEqual("yes 2 · no 0 · unknown 4", self.count_series(1)[0][3])

    def test_a_round_marked_as_a_contradiction_gives_yes_and_an_unmarked_round_unknown(self):
        # decision: WAY-404 "The cycle writes the mark into the sub-item of the round in the record's item"
        # Four cycles, each in a version of its own; the item *Discarded attempt* reads `none`. The
        # sub-item of the fourth is the form from before the mark, the third one has a mark that is
        # none of the two: both give the one reason.
        marked = "\n  - findings `reports/a_findings.md`, contradiction {}: the whole change"
        rounds = [
            marked.format("yes"),
            marked.format("no") + "\n  - review `reports/r.md`, PASS: the return step",
            marked.format("maybe"),
            "\n  - findings `reports/a_findings.md`: the whole change, range a1b2c3d..e4f5a6b",
        ]
        # One cycle in each version: the cell gives that cycle's answer as three numbers (WAY-417,
        # row 3, the cause of these expected values).
        self.assertEqual(
            [Q1_YES, Q1_NO, Q1_UNKNOWN, Q1_UNKNOWN], self.q1_of_each_version(["none"] * 4, rounds)
        )
        [pair] = [row for row in self.pair_rows() if row[0] == "Discarded attempt"]
        self.assertEqual("2", pair[1])
        self.assertEqual(
            "the sub-item of a round does not say whether there was a contradiction", pair[2]
        )

    def test_crafted_sub_items_of_review_rounds_break_no_cell_and_give_no_answer_they_do_not_state(
        self,
    ):
        # decision: WAY-404 "The cycle writes the mark into the sub-item of the round in the record's item"
        # A sub-item that is in neither form, a path with a control
        # character, a bar or a `..`, a mark
        # that runs on, and forty thousand sub-items give Q1 unknown, or the answer the sub-items
        # state (the mark that runs on is none); no text of a sub-item reaches a cell of the result, which names only fixed reasons.
        many = "".join(
            f"\n  - findings `reports/f{number}.md`, contradiction no: x"
            for number in range(40_000)
        )
        rounds = [
            "\n  - findings `reports/a\x1b[2J.md`, contradiction yes: x",
            "\n  - findings `reports/a|b.md`, contradiction yes: x",
            "\n  - review `reports/../a.md`, PASS: x",
            "\n  - findings `reports/a.md`, contradiction yes | no: x" + "x" * 300_000,
            many,
        ]
        answers = self.q1_of_each_version(["none"] * len(rounds), rounds)
        # One cycle in each version: the cell gives that cycle's answer as three numbers (WAY-417,
        # row 3, the cause of these expected values).
        self.assertEqual([Q1_UNKNOWN] * 4 + [Q1_NO], answers)
        self.assertEqual(
            [], [char for char in self.latest() if not char.isprintable() and char != "\n"]
        )

    def test_a_record_without_the_item_discarded_attempt_or_review_rounds_gives_q1_unknown(self):
        # decision: WAY-344 "Each reading of a file that the rule covers has one test"
        # A record of an earlier form lacks the items, as the records the count reads from history
        # do: Q1 is unknown, the reason names the item, and the exit code stays 0 (run_versions
        # asserts it), as for the other items of the record.
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.LATER, parent=v1)
        product = self.repository()
        no_discarded = process_record(v1).replace("- Discarded attempt: none\n", "")
        no_rounds = process_record(v2).replace("- Review rounds: none\n", "")
        self.add_cycles(
            product, [("no-discarded", no_discarded, 1_000), ("no-rounds", no_rounds, 1_000)]
        )
        self.run_versions(way, product)
        # One cycle in each of the two versions: the cell gives that cycle's answer as three
        # numbers (WAY-417, row 3, the cause of this expected value).
        self.assertEqual([Q1_UNKNOWN] * 2, [row[3] for row in self.count_series(1)])
        reasons = {row[2] for row in self.pair_rows() if row[0] == "Discarded attempt"}
        self.assertEqual(
            {
                "the record holds no item `Discarded attempt`",
                "the item `Review rounds` does not give its sub-items, so whether a "
                "review round found a contradiction is not known",
            },
            reasons,
        )

    def test_a_third_is_not_above_a_third(self):
        # One slice too large of three planned is exactly a third, which is not above it: no.
        way = self.the_way()
        v2 = self.version_at(way, self.LATER)
        product = self.repository()
        self.add_cycles(
            product,
            [("exact", process_record(v2, plan="3 slices", too_large="\n  - slice 1"), 1_000_000)],
        )
        self.run_versions(way, product)
        self.assertEqual(["1 of 1", "no"], self.count_series(1)[0][4:6])

    def test_unknown_reads_stay_unknown(self):
        # The prose discarded attempt makes Q1 unknown; the cycle whose plan has no figure just
        # before the word `slices` makes Q2 unknown with its reason, and does not stall the run.
        way = self.the_way()
        v2 = self.version_at(way, self.LATER)
        product = self.repository()
        self.add_cycles(
            product,
            [
                (
                    "exact",
                    process_record(v2, plan="3 slices", too_large="\n  - slice 1"),
                    1_000_000,
                ),
                ("prose", process_record(v2, discarded="a time overrun"), 1_000_000),
                ("crawling", process_record(v2, plan="9" * 200_000 + " slices"), 1_000_000),
            ],
        )
        self.run_versions(way, product)
        [row] = self.count_series(1)
        # Q1 is the numbers of the three cycles: exact and crawling answer no, prose answers
        # unknown, where the cell was the word `unknown` for the one that did not answer (WAY-417,
        # row 3, the cause of this expected value).
        self.assertEqual(
            [v2, "2025-10-10", "3", "yes 0 · no 2 · unknown 1", "1 of 2", "unknown"], row
        )
        self.assertEqual([[v2, "2025-10-10", "3", "3", "2.000000", "unknown"]], self.cost_series(1))
        unknown = self.rows("Unknown values")
        self.assertEqual(1, len([row for row in unknown if row[2] == "Discarded attempt"]))
        self.assertEqual(
            ["the item `Plan` does not give one count of slices before the word `slices`"],
            [row[3] for row in unknown if row[2] == "Plan"],
        )


def gate_run(second, others, total, *directories, code=0) -> str:
    """The rows of one run of gate_times.md: its start differs with `second`, so that runs stay
    apart; each directory is (name, seconds), and a run with none has the one row with dashes;
    `code` is the exit code written."""
    started = f"2026-11-11 10:00:{second:02}.000"
    if not directories:
        return gate_row(started, code, total, others)
    return "".join(
        gate_row(started, code, total, others, name, seconds) for name, seconds in directories
    )


TOTAL = "Total time of the run"


class MeasureVersions(VersionsCase):
    """The series of the mechanism measures and of the gate times, each by the change of its own
    instrument alone, and the median of each measure of each version (WAY-339, WAY-350).
    The helpers are those of ProcessVersions."""

    FIRST = ProcessVersions.FIRST
    BASE_FILES = ProcessVersions.BASE_FILES
    the_way = ProcessVersions.the_way
    version_at = ProcessVersions.version_at
    run_versions = ProcessVersions.run_versions
    cost_series = ProcessVersions.cost_series
    count_series = ProcessVersions.count_series

    def day(self, number) -> int:
        return self.FIRST + number * 86400

    def add_measured(self, product, specs) -> None:
        """Each cycle as (folder, pin, values, runs), chained so that all stay in the history:
        `values` maps a label of mechanism_measures.md to its value, the other labels keeping the
        value of MEASURE_VALUES, and is None for a copy with no such file; `runs` is the rows of
        gate_times.md, None for a copy with no such file."""
        parent = product.commit({"README.md": "a product\n"}, "Start")
        for folder, pin, values, runs in specs:
            files = {"cycle.md": process_record(pin)}
            if values is not None:
                files[MEASURES] = measures_file(
                    [(label, values.get(label, default)) for label, default in MEASURE_VALUES]
                )
            if runs is not None:
                files[GATE] = gate_file(rows=runs)
            _, parent = product.cycle(folder, files, parent=parent, branch=None)
        product.branch("main", parent)

    def measure(self, number, label) -> list[list[str]]:
        """The rows of a series of mechanism measures that are of one measure."""
        return [row for row in self.section("Mechanism measures", number) if row[1] == label]

    def gate(self, number, measure=TOTAL) -> list[list[str]]:
        return [row for row in self.section("Gate times", number) if row[1] == measure]

    def test_a_change_of_an_instrument_starts_only_the_series_of_its_own_measures(self):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # v2 changes the script of the measures, v3 the script of the gate times, v4 the reviewer's
        # instructions and `cycle_stages.py`. The cost splits at v4 alone; the mechanism measures
        # at v2 alone; the gate times at v3 alone, and no median is set across a split.
        way = self.the_way()
        measures = {"task-cycle/cycle_measures.py": "measures\n"}
        both = {**measures, "task-cycle/gate_times.py": "gate\n"}
        reviewed = {
            **both,
            "task-cycle/review/SKILL.md": "reviewer\n",
            "task-cycle/cycle_stages.py": "newer form\n",
        }
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1, changed=measures)
        v3 = self.version_at(way, self.day(2), parent=v2, changed=both)
        v4 = self.version_at(way, self.day(3), parent=v3, changed=reviewed)
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, {"Calls in all": "8"}, gate_run(2, 0, "90.000")),
                ("three", v3, {"Calls in all": "9"}, gate_run(3, 0, "80.000")),
                ("four", v4, {"Calls in all": "5"}, gate_run(4, 0, "70.000")),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual([v1, v2, v3], [row[0] for row in self.cost_series(1)])
        self.assertEqual([v4], [row[0] for row in self.cost_series(2)])
        self.assertNotIn("### Cost, series 3", self.latest())
        self.assertEqual([v1, v2, v3], [row[0] for row in self.count_series(1)])
        self.assertEqual([v4], [row[0] for row in self.count_series(2)])
        self.assertNotIn("### Count of remarks, series 3", self.latest())
        calls = "Calls in all"
        self.assertEqual([[v1, calls, "1", "10", "unknown"]], self.measure(1, calls))
        self.assertEqual(
            [
                [v2, calls, "1", "8", "unknown"],
                [v3, calls, "1", "9", "no"],
                [v4, calls, "1", "5", "yes"],
            ],
            self.measure(2, calls),
        )
        self.assertNotIn("### Mechanism measures, series 3", self.latest())
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"],
                [v2, TOTAL, "1", "90.000", "yes", "0", "unknown"],
            ],
            self.gate(1),
        )
        self.assertEqual(
            [
                [v3, TOTAL, "1", "80.000", "unknown", "0", "unknown"],
                [v4, TOTAL, "1", "70.000", "yes", "0", "unknown"],
            ],
            self.gate(2),
        )
        self.assertNotIn("### Gate times, series 3", self.latest())
        text = self.latest()
        self.assertLess(text.index("## Process versions"), text.index("## Measure versions"))
        self.assertLess(text.index("## Measure versions"), text.index("## Problems by cycle"))

    def test_a_changed_tool_of_a_measure_gives_no_value_to_the_median_of_its_version(self):
        # decision: WAY-339 "The audit compares each measure only within a series"
        # One own cycle with both files, in the version it ran on. Where it changed the script of
        # the measures, its version gives no value of them and its gate times stand; where it
        # changed the test runner, the gate times are the ones without a value and the mechanism
        # measures stand; where it changed none, both give their one value (12 calls, 100 seconds).
        calls = "Calls in all"
        for changed, mechanism, runs in (
            ({"task-cycle/cycle_measures.py": "two\n"}, False, True),
            ({"gate/run_tests.py": "two\n"}, True, False),
            ({"task-cycle/gate_times.py": "two\n"}, True, False),
            ({}, True, True),
        ):
            with self.subTest(sorted(changed)):
                self.fresh()
                files = {MEASURES: measures_file(), GATE: gate_file(rows=gate_run(1, 0, "100.000"))}
                _, version = self.own_cycle(files, changed, process_record(PIN))
                done = self.run_with_prices()
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertEqual(
                    [[version, calls, "1", "12", "unknown"]]
                    if mechanism
                    else [[version, "—", "0", "unknown", "unknown"]],
                    self.measure(1, calls if mechanism else "—"),
                )
                self.assertEqual(
                    [[version, TOTAL, "1", "100.000", "unknown", "0", "unknown"]]
                    if runs
                    else [[version, "—", "0", "unknown", "unknown", "0", "unknown"]],
                    self.gate(1, TOTAL if runs else "—"),
                )

    def test_a_change_of_the_test_runner_starts_a_new_series_of_gate_times_only(self):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # v2 changes the test runner of the gate, v3 the script of the measures. The gate times
        # split at v2 alone, the mechanism measures at v3 alone, and the reason of the split
        # names the file that changed. Medians: the gate series of v2 and v3 has 90 and 80, so v3
        # falls; v1 stands alone in its series.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1, changed={"gate/run_tests.py": "runner\n"})
        # A commit lists the files it keeps, so v3 lists the runner again, unchanged.
        v3 = self.version_at(
            way,
            self.day(2),
            parent=v2,
            changed={"gate/run_tests.py": "runner\n", "task-cycle/cycle_measures.py": "measures\n"},
        )
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, {"Calls in all": "9"}, gate_run(2, 0, "90.000")),
                ("three", v3, {"Calls in all": "8"}, gate_run(3, 0, "80.000")),
            ],
        )
        self.run_versions(way, product)
        calls = "Calls in all"
        self.assertEqual(
            [[v1, calls, "1", "10", "unknown"], [v2, calls, "1", "9", "yes"]],
            self.measure(1, calls),
        )
        self.assertEqual([[v3, calls, "1", "8", "unknown"]], self.measure(2, calls))
        self.assertEqual([[v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"]], self.gate(1))
        self.assertEqual(
            [
                [v2, TOTAL, "1", "90.000", "unknown", "0", "unknown"],
                [v3, TOTAL, "1", "80.000", "yes", "0", "unknown"],
            ],
            self.gate(2),
        )
        self.assertIn(
            "Begins at this version: `gate/run_tests.py` changed between the two versions.",
            self.latest(),
        )

    def test_the_reason_of_a_gate_split_names_the_scripts_that_changed(self):
        # Asked of two versions directly: the gate times split at a change of either of their
        # scripts and the reason names the ones that changed, in the order of the scripts; the
        # mechanism measures split at no change of the test runner.
        sys.path.insert(0, str(HERE))
        from version_analysis import Version, instrument_series

        class Changed:
            def __init__(self, paths):
                self.paths = paths

            def differs(self, earlier, later, paths):
                return any(path in self.paths for path in paths)

        scripts = ("task-cycle/gate_times.py", "gate/run_tests.py")
        earlier = Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = Version("b" * 40, 2, "2025-10-10", "2026-02-01", [])
        runner = instrument_series([earlier, later], Changed({"gate/run_tests.py"}), scripts)
        self.assertEqual("`gate/run_tests.py` changed between the two versions", runner[1].begins)
        both = instrument_series([earlier, later], Changed(set(scripts)), scripts)
        self.assertEqual(
            "`task-cycle/gate_times.py` and `gate/run_tests.py` changed between the two versions",
            both[1].begins,
        )
        measures = instrument_series(
            [earlier, later], Changed({"gate/run_tests.py"}), ("task-cycle/cycle_measures.py",)
        )
        self.assertEqual([[earlier, later]], [block.versions for block in measures])

    def test_the_reviewer_the_stage_script_and_the_list_of_classes_split_no_series_of_measures(
        self,
    ):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # v2 changes the reviewer's instructions, v3 `cycle_stages.py`, and a class is added on the
        # day of v4: each splits the series of the count of remarks, `cycle_stages.py` alone the
        # series of the cost, and none splits the measures, whose medians fall from version to
        # version across all three.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(
            way, self.day(1), parent=v1, changed={"task-cycle/review/SKILL.md": "reviewer\n"}
        )
        v3 = self.version_at(
            way,
            self.day(2),
            parent=v2,
            changed={
                "task-cycle/review/SKILL.md": "reviewer\n",
                "task-cycle/cycle_stages.py": "newer form\n",
            },
        )
        v4 = self.version_at(
            way,
            self.day(3),
            parent=v3,
            changed={
                "task-cycle/review/SKILL.md": "reviewer\n",
                "task-cycle/cycle_stages.py": "newer form\n",
            },
        )
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, {"Calls in all": "9"}, gate_run(2, 0, "90.000")),
                ("three", v3, {"Calls in all": "8"}, gate_run(3, 0, "80.000")),
                ("four", v4, {"Calls in all": "7"}, gate_run(4, 0, "70.000")),
            ],
        )
        self.register.write_text(
            register_text(classes=["| sharp | x | 2025-10-12 | none |"]), encoding="utf-8"
        )
        self.run_versions(way, product)
        self.assertEqual(
            [[v1], [v2], [v3], [v4]],
            [[row[0] for row in self.count_series(number)] for number in (1, 2, 3, 4)],
        )
        self.assertEqual(
            [[v1, v2], [v3, v4]],
            [[row[0] for row in self.cost_series(number)] for number in (1, 2)],
        )
        self.assertNotIn("### Cost, series 3", self.latest())
        self.assertEqual(
            [
                [v1, "Calls in all", "1", "10", "unknown"],
                [v2, "Calls in all", "1", "9", "yes"],
                [v3, "Calls in all", "1", "8", "yes"],
                [v4, "Calls in all", "1", "7", "yes"],
            ],
            self.measure(1, "Calls in all"),
        )
        self.assertEqual(["unknown", "yes", "yes", "yes"], [row[4] for row in self.gate(1)])
        self.assertNotIn("### Mechanism measures, series 2", self.latest())
        self.assertNotIn("### Gate times, series 2", self.latest())

    def test_a_new_price_list_splits_no_series_of_measures(self):
        # decision: WAY-339 "The measures of how a cycle's agents use context and the prompt"
        # One price list prices a whole run, so no real run splits at it: the series of the
        # measures are asked of the two versions directly, and ask git about their scripts alone.
        sys.path.insert(0, str(HERE))
        from version_analysis import Version, cost_boundary, instrument_series

        asked = []

        class Unchanged:
            def differs(self, earlier, later, paths):
                asked.append(tuple(paths))
                return False

        earlier = Version("a" * 40, 1, "2025-10-09", "2026-01-01", [])
        later = Version("b" * 40, 2, "2025-10-10", "2026-02-01", [])
        for scripts in (
            ("task-cycle/cycle_measures.py",),
            ("task-cycle/gate_times.py", "gate/run_tests.py"),
        ):
            with self.subTest(scripts):
                blocks = instrument_series([earlier, later], Unchanged(), scripts)
                self.assertEqual([[earlier, later]], [block.versions for block in blocks])
                self.assertEqual(scripts, asked[-1])
        self.assertEqual("the price list changed", cost_boundary(earlier, later, None))

    def test_medians_and_falls_of_three_versions_over_an_odd_and_an_even_number_of_cycles(self):
        # Calls in all: v1 has 10, 4 and 7 (median 7, odd), v2 has 6 and 9 (median 7.5, even, so
        # not lower than 7), v3 has 2, 8, 5 and 6 (sorted 2, 5, 6, 8: median 5.5, lower than 7.5).
        # The share has a value in 2 of 3 cycles of v1 (12.5 and 13.0: 12.75), in 1 of 2 of v2
        # (12.0, lower) and in 2 of 4 of v3 (12.0 and 12.5: 12.25, not lower than 12.0). A cycle
        # of no version, with 1 call, stands in no median.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        v3 = self.version_at(way, self.day(2), parent=v2)
        share = "Share of the context in calls above 200000 tokens"
        product = self.repository()
        self.add_measured(
            product,
            [
                ("a", v1, {"Calls in all": "10", share: "12.5%"}, None),
                ("b", v1, {"Calls in all": "4", share: "13.0%"}, None),
                ("c", v1, {"Calls in all": "7", share: "unknown"}, None),
                ("d", v2, {"Calls in all": "6", share: "12.0%"}, None),
                ("e", v2, {"Calls in all": "9", share: "unknown"}, None),
                ("f", v3, {"Calls in all": "2", share: "12.0%"}, None),
                ("g", v3, {"Calls in all": "8", share: "12.5%"}, None),
                ("h", v3, {"Calls in all": "5", share: "unknown"}, None),
                ("i", v3, {"Calls in all": "6", share: "unknown"}, None),
                ("stray", "none", {"Calls in all": "1"}, None),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, "Calls in all", "3", "7", "unknown"],
                [v2, "Calls in all", "2", "7.5", "no"],
                [v3, "Calls in all", "4", "5.5", "yes"],
            ],
            self.measure(1, "Calls in all"),
        )
        self.assertEqual(
            [
                [v1, share, "2", "12.75%", "unknown"],
                [v2, share, "1", "12.0%", "yes"],
                [v3, share, "2", "12.25%", "no"],
            ],
            self.measure(1, share),
        )
        # A measure that does not change does not fall; every one of the fifteen has a row.
        self.assertEqual(
            [
                [v1, "Calls of subagents", "3", "7", "unknown"],
                [v2, "Calls of subagents", "2", "7", "no"],
                [v3, "Calls of subagents", "4", "7", "no"],
            ],
            self.measure(1, "Calls of subagents"),
        )
        self.assertEqual(3 * len(MEASURE_LABELS), len(self.section("Mechanism measures", 1)))
        unknown = self.rows("Unknown values")
        self.assertEqual(
            "no previous version in the series",
            self.reasons_of(unknown, f"Measure falls: Calls in all, version {v1}"),
        )
        self.assertEqual("", self.reasons_of(unknown, f"Measure falls: Calls in all, version {v2}"))

    def test_the_gate_times_take_only_runs_with_no_other_gate_and_show_the_others_apart(self):
        # Medians by hand. v1: total of the runs alone 100 and 110 (105.000), apart 200 (company: 1
        # other gate) and 300 (count unknown): 250.000; gate/a alone 60.0 and 70.0 (65.0), apart
        # 135.0; gate/b alone 40.0, apart 80.0. v2: alone 90 and 95 (92.500, lower than 105), apart
        # 10.000 (it would pull the median down if it entered); gate/a 51.0, apart 1.0; no gate/b
        # run. v3: total alone 100 (not lower than 92.5: apart 1.000 enters no comparison),
        # gate/a in a run with company only, gate/b alone 41.0 with no previous gate/b. v4: every
        # run has company, so no comparison.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        v3 = self.version_at(way, self.day(2), parent=v2)
        v4 = self.version_at(way, self.day(3), parent=v3)
        product = self.repository()
        self.add_measured(
            product,
            [
                (
                    "a",
                    v1,
                    {},
                    gate_run(1, 0, "100.000", ("gate/a", "60.0"), ("gate/b", "40.0"))
                    + gate_run(2, 1, "200.000", ("gate/a", "120.0"), ("gate/b", "80.0")),
                ),
                (
                    "b",
                    v1,
                    {},
                    gate_run(3, 0, "110.000", ("gate/a", "70.0"))
                    + gate_run(4, "unknown", "300.000", ("gate/a", "150.0")),
                ),
                (
                    "c",
                    v2,
                    {},
                    gate_run(5, 0, "90.000", ("gate/a", "50.0"))
                    + gate_run(6, 0, "95.000", ("gate/a", "52.0"))
                    + gate_run(7, 3, "10.000", ("gate/a", "1.0")),
                ),
                (
                    "d",
                    v3,
                    {},
                    gate_run(8, 0, "100.000", ("gate/b", "41.0"))
                    + gate_run(9, 1, "1.000", ("gate/a", "0.5")),
                ),
                ("e", v4, {}, gate_run(10, 2, "50.000", ("gate/a", "20.0"))),
            ],
        )
        self.run_versions(way, product)
        a, b = "Directory: gate/a", "Directory: gate/b"
        self.assertEqual(
            [
                [v1, TOTAL, "2", "105.000", "unknown", "2", "250.000"],
                [v1, a, "2", "65.0", "unknown", "2", "135.0"],
                [v1, b, "1", "40.0", "unknown", "1", "80.0"],
                [v2, TOTAL, "2", "92.500", "yes", "1", "10.000"],
                [v2, a, "2", "51.0", "yes", "1", "1.0"],
                [v3, TOTAL, "1", "100.000", "no", "1", "1.000"],
                [v3, a, "0", "unknown", "unknown", "1", "0.5"],
                [v3, b, "1", "41.0", "unknown", "0", "unknown"],
                [v4, TOTAL, "0", "unknown", "unknown", "1", "50.000"],
                [v4, a, "0", "unknown", "unknown", "1", "20.0"],
            ],
            self.section("Gate times", 1),
        )
        unknown = self.rows("Unknown values")
        self.assertIn(
            "no previous version in the series",
            self.reasons_of(unknown, f"Gate time falls: {TOTAL}, version {v1}"),
        )
        self.assertIn(
            "no run of the version that passed with no other gate",
            self.reasons_of(unknown, f"Gate time falls: {TOTAL}, version {v4}"),
        )
        self.assertIn(
            "no run of the previous version that passed with no other gate",
            self.reasons_of(unknown, f"Gate time falls: {b}, version {v3}"),
        )

    def test_a_version_with_no_cycle_that_gave_a_value_has_one_row_and_one_line_of_reason(self):
        # v2's cycle has neither file: one row in each table, `—` for the measure and no median, and
        # one line in *Unknown values* for each instrument instead of one for each measure. v3 has
        # values, keeps its rows as they are, and is not compared with v2.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        v3 = self.version_at(way, self.day(2), parent=v2)
        product = self.repository()
        self.add_measured(
            product,
            [
                ("one", v1, {"Calls in all": "10"}, gate_run(1, 0, "100.000")),
                ("two", v2, None, None),
                ("three", v3, {"Calls in all": "9"}, gate_run(3, 0, "90.000")),
            ],
        )
        self.run_versions(way, product)
        calls = "Calls in all"
        self.assertEqual(
            [[v1, calls, "1", "10", "unknown"], [v3, calls, "1", "9", "unknown"]],
            self.measure(1, calls),
        )
        self.assertEqual([[v2, "—", "0", "unknown", "unknown"]], self.measure(1, "—"))
        self.assertEqual(2 * len(MEASURE_LABELS) + 1, len(self.section("Mechanism measures", 1)))
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"],
                [v3, TOTAL, "1", "90.000", "unknown", "0", "unknown"],
            ],
            self.gate(1),
        )
        self.assertEqual([[v2, "—", "0", "unknown", "unknown", "0", "unknown"]], self.gate(1, "—"))
        unknown = self.rows("Unknown values")
        self.assertIn(
            "no cycle of this version gives a value",
            self.reasons_of(unknown, f"Mechanism measures of version {v2}"),
        )
        self.assertIn(
            "an earlier cycle, or a script that failed",
            self.reasons_of(unknown, f"Mechanism measures of version {v2}"),
        )
        self.assertIn(
            "no run of this version gives a time",
            self.reasons_of(unknown, f"Gate times of version {v2}"),
        )
        # The cause named for a version with no gate times is the task's row 6: a final gate that
        # ran in CI; the mechanism measures, which no CI run leaves out, do not name it.
        self.assertIn(
            "a final gate that ran in CI", self.reasons_of(unknown, f"Gate times of version {v2}")
        )
        self.assertNotIn(
            "a final gate that ran in CI",
            self.reasons_of(unknown, f"Mechanism measures of version {v2}"),
        )
        self.assertEqual(
            [],
            [
                row
                for row in unknown
                if row[2].startswith("Measure falls") and f"version {v2}" in row[2]
            ],
        )
        self.assertEqual(
            "no cycle of the previous version gives a value",
            self.reasons_of(unknown, f"Measure falls: {calls}, version {v3}"),
        )

    def test_a_failed_run_enters_no_median_and_is_shown_apart_with_the_runs_with_company(self):
        # v1: passed and alone: 100.000 (gate/a 60.0). A run alone that exited 2 (5.000, gate/a
        # 1.0) and one alone whose exit code is unknown (300.000) are not compared: apart, the
        # median of 5.000 and 300.000 is 152.500. v2: passed and alone 90.000 (gate/a 50.0), so the
        # total falls from 100.000 and gate/a from 60.0; a failed run alone, 2.000, is apart.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        product = self.repository()
        self.add_measured(
            product,
            [
                (
                    "a",
                    v1,
                    {},
                    gate_run(1, 0, "100.000", ("gate/a", "60.0"))
                    + gate_run(2, 0, "5.000", ("gate/a", "1.0"), code=2)
                    + gate_run(3, 0, "300.000", code="unknown"),
                ),
                (
                    "b",
                    v2,
                    {},
                    gate_run(4, 0, "90.000", ("gate/a", "50.0")) + gate_run(5, 0, "2.000", code=1),
                ),
            ],
        )
        self.run_versions(way, product)
        a = "Directory: gate/a"
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "2", "152.500"],
                [v1, a, "1", "60.0", "unknown", "1", "1.0"],
                [v2, TOTAL, "1", "90.000", "yes", "1", "2.000"],
                [v2, a, "1", "50.0", "yes", "0", "unknown"],
            ],
            self.section("Gate times", 1),
        )

    def test_a_version_whose_only_run_failed_has_no_median_and_no_comparison(self):
        # v1 passed (100.000); v2's only run failed (4.000): v2 has no median, no comparison, and
        # its run is apart.
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        v2 = self.version_at(way, self.day(1), parent=v1)
        product = self.repository()
        self.add_measured(
            product,
            [
                ("a", v1, {}, gate_run(1, 0, "100.000")),
                ("b", v2, {}, gate_run(2, 0, "4.000", code=2)),
            ],
        )
        self.run_versions(way, product)
        self.assertEqual(
            [
                [v1, TOTAL, "1", "100.000", "unknown", "0", "unknown"],
                [v2, TOTAL, "0", "unknown", "unknown", "1", "4.000"],
            ],
            self.gate(1),
        )
        self.assertIn(
            "no run of the version that passed with no other gate",
            self.reasons_of(self.rows("Unknown values"), f"Gate time falls: {TOTAL}, version {v2}"),
        )

    def test_a_directory_written_twice_in_one_run_counts_once_and_says_so(self):
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        product = self.repository()
        self.add_measured(
            product, [("a", v1, {}, gate_run(1, 0, "10.000", ("gate/a", "5.0"), ("gate/a", "7.0")))]
        )
        self.run_versions(way, product)
        self.assertEqual(
            [[v1, "Directory: gate/a", "1", "5.0", "unknown", "0", "unknown"]],
            self.gate(1, "Directory: gate/a"),
        )
        self.assertTrue(any("twice" in row[3] for row in self.rows("Unknown values")))

    def test_crafted_directories_and_runs_break_no_cell_and_cost_bounded_work(self):
        way = self.the_way()
        v1 = self.version_at(way, self.day(0))
        product = self.repository()
        crafted = (
            gate_run(1, 0, "1.000", ("gate\\|x\x1b[2J\x07y", "1.0"), ("d" * 500, "2.0"))
            + "".join(
                gate_row(f"2026-11-11 11:00:00.{index:03}", 0, "1.000", 0, f"gate/d{index}", "1.0")
                for index in range(700)
            )
            + "| a | b |\n" * 30
        )
        self.add_measured(product, [("a", v1, {}, crafted)])
        self.run_versions(way, product)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        self.assertNotIn("d" * 201, text)
        rows = self.section("Gate times", 1)
        self.assertEqual({7}, {len(row) for row in rows})
        # 500 runs are read, the first of them the crafted one: the total, its two directories and
        # the 499 directories of the runs after it.
        self.assertEqual(1 + 2 + 499, len(rows))
        self.assertIn(["Directory: " + "d" * 200], [[row[1]] for row in rows])


class SeriesImages(VersionsCase):
    """The image of each series of each of the four kinds, in the result of the count, and Q1 of
    the row of a version as numbers (WAY-339, WAY-350, WAY-417). The helpers are those of
    ProcessVersions."""

    FIRST = ProcessVersions.FIRST
    LATER = ProcessVersions.LATER
    BASE_FILES = ProcessVersions.BASE_FILES
    the_way = ProcessVersions.the_way
    version_at = ProcessVersions.version_at
    run_versions = ProcessVersions.run_versions
    stages_of = ProcessVersions.stages_of
    cost_series = ProcessVersions.cost_series
    count_series = ProcessVersions.count_series

    CALLS = "Calls in all"
    GATE_A = "Directory: gate/a"
    GATE_B = "Directory: gate/b"
    # The four cycles, in the order of their versions: cycle a and b run on the first version and
    # c and d on the second. The cost is that of 1,000,000 tokens of model-a at 2 dollars; cycle d
    # has no stage report, so no known cost, and no file of measures. Q1: a yes (an open design
    # choice), b no, c unknown (an overrun in prose), d no. Plans: a has 4 slices and 1 too large,
    # b 2 and 0, c 3 and 0, and d, on the one-author route, none. The calls: 10, 4 and 7. The runs:
    # a and b alone and passed (total 100 and 110, gate/a 60.0 and 70.0); c one with company (200,
    # gate/a 120.0) and one that failed (5.000, gate/b 1.0); d one whose exit code is unknown (300).
    SPECS = (
        (
            "a",
            0,
            "reason: `open design choice`; 10:32",
            "4 slices",
            "\n  - slice 1",
            1_000_000,
            {"Calls in all": "10"},
            gate_run(1, 0, "100.000", ("gate/a", "60.0")),
        ),
        (
            "b",
            0,
            "none",
            "2 slices",
            "none",
            2_000_000,
            {"Calls in all": "4"},
            gate_run(2, 0, "110.000", ("gate/a", "70.0")),
        ),
        (
            "c",
            1,
            "a time overrun",
            "3 slices",
            "none",
            500_000,
            {"Calls in all": "7"},
            gate_run(3, 1, "200.000", ("gate/a", "120.0"))
            + gate_run(4, 0, "5.000", ("gate/b", "1.0"), code=2),
        ),
        (
            "d",
            1,
            "none",
            "none on the one-author route",
            "none",
            None,
            None,
            gate_run(5, 0, "300.000", code="unknown"),
        ),
    )

    def add_images(self, product, versions, specs) -> None:
        """Each spec as (folder, number of its version in `versions`, discarded attempt, plan,
        slices too large, tokens of its stage report or None for no report, values of the
        measures or None for no file, rows of the gate times), chained in the history."""
        parent = product.commit({"README.md": "a product\n"}, "Start")
        for folder, number, discarded, plan, too_large, tokens, values, runs in specs:
            files = {
                "cycle.md": process_record(
                    versions[number], discarded=discarded, plan=plan, too_large=too_large
                ),
                GATE: gate_file(rows=runs),
            }
            if tokens is not None:
                files["stages.md"] = self.stages_of(tokens)
            if values is not None:
                files[MEASURES] = measures_file(
                    [(label, values.get(label, default)) for label, default in MEASURE_VALUES]
                )
            _, parent = product.cycle(folder, files, parent=parent, branch=None)
        product.branch("main", parent)

    def two_versions(self, specs, changed=None):
        """The result of the count for the cycles of `specs` in two versions of the-way, the
        second with the files of `changed` replaced; returns the two commits."""
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        v2 = self.version_at(way, self.LATER, parent=v1, changed=changed)
        product = self.repository()
        self.add_images(product, [v1, v2], specs)
        self.run_versions(way, product)
        return v1, v2

    def test_a_series_of_two_versions_with_two_cycles_each_has_an_image_of_each_kind(self):
        # decision: WAY-339 "The audit shows each series as an image of all its cycles"
        # decision: WAY-417 "The image of a series, which sets no two groups against each other"
        # Every figure by hand from the description of SPECS. Cost: the cycles 4, the known costs 3
        # (2, 4 and 1 dollars), median 2. Count: Q1 of the four cycles, yes 1, no 2, unknown 1;
        # the plans of a, b and c read (3 of 3: d is on the one-author route), 4 + 2 + 3 = 9
        # slices planned and 1 too large, three times 1 is not above 9, so no. The calls in all:
        # 10, 4 and 7 of three cycles (d gives none), median 7; the share: 12.5% in each of the
        # three. The gate, total: compared 100 and 110 (105.000), not compared 200, 5 and 300
        # (200.000); gate/a: compared 60.0 and 70.0 (65.0), not compared 120.0; gate/b: none
        # compared, not compared 1.0.
        self.two_versions(self.SPECS)
        self.assertEqual([["4", "3", "2.000000"]], self.image("Cost", 1))
        self.assertEqual(
            [["4", "yes 1 · no 2 · unknown 1", "3 of 3", "9", "1", "no"]],
            self.image("Count of remarks", 1),
        )
        mechanism = {row[0]: row for row in self.image("Mechanism measures", 1)}
        self.assertEqual(15, len(mechanism))
        self.assertEqual([self.CALLS, "3", "7"], mechanism[self.CALLS])
        self.assertEqual(
            ["Share of the context in calls above 200000 tokens", "3", "12.5%"],
            mechanism["Share of the context in calls above 200000 tokens"],
        )
        self.assertEqual(
            [
                [TOTAL, "2", "105.000", "3", "200.000"],
                [self.GATE_A, "2", "65.0", "1", "120.0"],
                [self.GATE_B, "0", "unknown", "1", "1.0"],
            ],
            self.image("Gate times", 1),
        )
        for kind in ("Cost", "Count of remarks", "Mechanism measures", "Gate times"):
            self.assertNotIn(f"### {kind}, series 2", self.latest())

    def test_the_rows_of_the_versions_stay_and_give_q1_as_numbers_of_their_cycles(self):
        # decision: WAY-417 "the rows of the versions of a series give Q1 as a word while its image"
        # The tables per version stay beside the image. v1 has a (yes) and b (no); v2 has c
        # (unknown) and d (no): the old cell would read `yes` for v1 and `unknown` for v2.
        v1, v2 = self.two_versions(self.SPECS)
        self.assertEqual(
            [
                [v1, "2025-10-09", "2", "yes 1 · no 1 · unknown 0", "2 of 2", "no"],
                [v2, "2025-10-10", "2", "yes 0 · no 1 · unknown 1", "1 of 1", "no"],
            ],
            self.count_series(1),
        )
        self.assertEqual(
            [
                [v1, "2025-10-09", "2", "2", "3.000000", "unknown"],
                [v2, "2025-10-10", "2", "1", "1.000000", "yes"],
            ],
            self.cost_series(1),
        )

    def test_a_version_has_no_reason_for_its_q1_and_each_cycle_keeps_its_own(self):
        # decision: WAY-417 "The answer Q1 of the audit ... is given for each group of cycles"
        # v2 holds c, whose Q1 is unknown, and d: the version no longer has an answer of its own
        # to be unknown, so *Unknown values* holds no line for the Q1 of a version, and the reason
        # of cycle c, that its discarded attempt opens with no marker, stays.
        self.two_versions(self.SPECS)
        unknown = self.rows("Unknown values")
        self.assertEqual(
            [], [row for row in unknown if row[2].startswith("contradiction only after code")]
        )
        [reason] = [row[3] for row in unknown if row[2] == "Discarded attempt"]
        self.assertTrue(reason.startswith("the item `Discarded attempt` opens with no marker"))

    def test_the_image_stands_under_the_heading_of_the_series_before_its_table_per_version(self):
        # decision: WAY-417 "shows each series as an image of all its cycles"
        # The image carries no Q3 and no fall: its columns are those of its kind alone.
        self.two_versions(self.SPECS)
        expected = {
            "Cost": (["Cycles", "Cycles with a known cost", "Median cost (USD)"], 3),
            "Count of remarks": (
                [
                    "Cycles",
                    "Q1: contradiction only after code",
                    "Plans read",
                    "Slices planned",
                    "Slices returned too large",
                    "Q2: more than a third of slices too large",
                ],
                6,
            ),
            "Mechanism measures": (["Measure", "Cycles with a value", "Median"], 3),
            "Gate times": (
                [
                    "Measure",
                    "Runs compared",
                    "Median (seconds)",
                    "Runs not compared",
                    "Median of those (seconds)",
                ],
                5,
            ),
        }
        for kind, (header, width) in expected.items():
            with self.subTest(kind):
                image, versions = self.tables(kind, 1)
                self.assertEqual(header, image[0])
                self.assertEqual({width}, {len(row) for row in image[1]})
                self.assertEqual("Version (commit)", versions[0][0])

    def test_the_image_of_a_series_takes_only_the_cycles_of_that_series(self):
        # decision: WAY-339 "The audit shows each series as an image of all its cycles"
        # A change of the stage script splits the series of the cost and of the count of remarks
        # between v1 (a and b) and v2 (c and d) and splits neither the mechanism measures nor the
        # gate times. Cost: 2 and 4 dollars, median 3; then 1 dollar, d's cost unknown. Q1: a yes
        # and b no; then c unknown and d no. Plans: 6 slices, 1 too large; then 3 and 0, d being
        # on the one-author route.
        self.two_versions(self.SPECS, changed={"task-cycle/cycle_stages.py": "newer form\n"})
        self.assertEqual([["2", "2", "3.000000"]], self.image("Cost", 1))
        self.assertEqual([["2", "1", "1.000000"]], self.image("Cost", 2))
        self.assertEqual(
            [["2", "yes 1 · no 1 · unknown 0", "2 of 2", "6", "1", "no"]],
            self.image("Count of remarks", 1),
        )
        self.assertEqual(
            [["2", "yes 0 · no 1 · unknown 1", "1 of 1", "3", "0", "no"]],
            self.image("Count of remarks", 2),
        )
        calls = [row for row in self.image("Mechanism measures", 1) if row[0] == self.CALLS]
        self.assertEqual([[self.CALLS, "3", "7"]], calls)
        self.assertNotIn("### Mechanism measures, series 2", self.latest())
        self.assertNotIn("### Gate times, series 2", self.latest())

    def test_a_series_of_one_cycle_has_an_image_of_that_cycle(self):
        # decision: WAY-417 "The image of a series, which sets no two groups against each other"
        # Cycle b alone: cost 4 dollars, Q1 no, its plan of 2 slices read with none too large, 4
        # calls, one run alone that passed (110.000, gate/a 70.0).
        way = self.the_way()
        v1 = self.version_at(way, self.FIRST)
        product = self.repository()
        self.add_images(product, [v1], [self.SPECS[1]])
        self.run_versions(way, product)
        self.assertEqual([["1", "1", "4.000000"]], self.image("Cost", 1))
        self.assertEqual(
            [["1", "yes 0 · no 1 · unknown 0", "1 of 1", "2", "0", "no"]],
            self.image("Count of remarks", 1),
        )
        calls = [row for row in self.image("Mechanism measures", 1) if row[0] == self.CALLS]
        self.assertEqual([[self.CALLS, "1", "4"]], calls)
        self.assertEqual(
            [
                [TOTAL, "1", "110.000", "0", "unknown"],
                [self.GATE_A, "1", "70.0", "0", "unknown"],
            ],
            self.image("Gate times", 1),
        )
