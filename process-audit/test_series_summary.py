"""Tests of process-audit/series_summary.py: the cells of the image of a series of cycles, from a
list of cycles built here by hand, with each input and each expected value written out (WAY-339,
WAY-417). The same images in the result of the count, and the Q1 of the rows of the versions, are
tested in process-audit/test_process_versions.py.

Run from the root of the-way: python -B gate/run_tests.py process-audit
"""

import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from record_reading import Cycle, GateRun  # noqa: E402
from series_summary import (  # noqa: E402
    DIRECTORY_MEASURE,
    TOTAL_MEASURE,
    cost_image,
    count_image,
    gate_image,
    gate_values,
    mechanism_image,
    median_of,
    plan_sums,
    q1_text,
)

CALLS = "Calls in all"
SHARE = "Share of the context in calls above 200000 tokens"


def cycle(**fields) -> Cycle:
    """A cycle with the fields a test gives and the rest as an empty record leaves them."""
    return Cycle("product", "a-task", "0" * 40, "2026-11-11", **fields)


def planned(slices, large) -> Cycle:
    """A cycle whose plan is read: `slices` planned, `large` returned too large."""
    return cycle(planned=slices, too_large=large)


class Median(unittest.TestCase):
    def test_the_median_of_an_odd_number_is_the_middle_one(self):
        self.assertEqual(Decimal(4), median_of([Decimal(9), Decimal(1), Decimal(4)]))

    def test_the_median_of_an_even_number_is_the_mean_of_the_two_middle_ones(self):
        self.assertEqual(
            Decimal("2.5"), median_of([Decimal(4), Decimal(1), Decimal(2)] + [Decimal(3)])
        )

    def test_there_is_no_median_of_nothing(self):
        self.assertIsNone(median_of([]))


class CostImage(unittest.TestCase):
    def test_the_image_gives_the_cycles_those_with_a_known_cost_and_their_median(self):
        # Four cycles of two versions, two each; the cost of one is unknown. The known costs 4, 1
        # and 2 sort to 1, 2, 4: the median is 2.
        cycles = [
            cycle(cost=Decimal(4)),
            cycle(cost=Decimal(1)),
            cycle(cost=None),
            cycle(cost=Decimal(2)),
        ]
        self.assertEqual([["4", "3", "2.000000"]], cost_image(cycles))

    def test_the_median_of_an_even_number_of_known_costs_is_the_mean_of_the_middle_two(self):
        # 1 and 2 dollars: the mean of the two is 1.5.
        cycles = [cycle(cost=Decimal(2)), cycle(cost=Decimal(1))]
        self.assertEqual([["2", "2", "1.500000"]], cost_image(cycles))

    def test_a_series_with_no_known_cost_has_no_median(self):
        self.assertEqual([["2", "0", "unknown"]], cost_image([cycle(), cycle()]))

    def test_a_series_of_one_cycle_gives_its_cost(self):
        self.assertEqual([["1", "1", "0.250000"]], cost_image([cycle(cost=Decimal("0.25"))]))

    def test_the_image_holds_no_question_q3_and_no_fall(self):
        [row] = cost_image([cycle(cost=Decimal(2)), cycle(cost=Decimal(1))])
        self.assertEqual(3, len(row))


class Q1Numbers(unittest.TestCase):
    def test_the_numbers_are_those_of_the_cycles_answering_each(self):
        # Five cycles, as the verification of WAY-417 gives: two yes, two no and one unknown.
        cycles = [
            cycle(contradiction="yes"),
            cycle(contradiction="no"),
            cycle(contradiction=None),
            cycle(contradiction="yes"),
            cycle(contradiction="no"),
        ]
        self.assertEqual("yes 2 · no 2 · unknown 1", q1_text(cycles))

    def test_one_cycle_that_answers_yes_does_not_make_the_group_yes(self):
        # Break caught: a word taken from the cycles, `yes` where any one of them says yes.
        cycles = [cycle(contradiction="yes"), cycle(contradiction="no"), cycle(contradiction="no")]
        self.assertEqual("yes 1 · no 2 · unknown 0", q1_text(cycles))

    def test_a_cycle_that_did_not_answer_is_counted_apart_and_not_as_no(self):
        cycles = [cycle(contradiction="no"), cycle(contradiction=None)]
        self.assertEqual("yes 0 · no 1 · unknown 1", q1_text(cycles))

    def test_a_group_of_one_cycle(self):
        self.assertEqual("yes 0 · no 0 · unknown 1", q1_text([cycle()]))
        self.assertEqual("yes 1 · no 0 · unknown 0", q1_text([cycle(contradiction="yes")]))


class Q2Sums(unittest.TestCase):
    def test_the_sums_of_all_the_plans_give_the_answer(self):
        # 4 + 2 planned, 3 + 0 too large: 3 times 3 is 9, above 6, so yes.
        sums = plan_sums([planned(4, 3), planned(2, 0)])
        self.assertEqual(("2 of 2", 6, 3, "yes", None), tuple_of(sums))

    def test_a_third_is_not_above_a_third(self):
        # 2 of 6: 3 times 2 is 6, not above 6, so no.
        sums = plan_sums([planned(4, 1), planned(2, 1)])
        self.assertEqual(("2 of 2", 6, 2, "no", None), tuple_of(sums))

    def test_a_plan_that_is_not_read_makes_the_answer_unknown_and_the_sums_those_of_the_read(self):
        # The second plan is not read: its slices could turn either answer. The sums are over the
        # plan that is read, 4 planned and 3 too large.
        sums = plan_sums([planned(4, 3), cycle(planned=None, too_large=None)])
        self.assertEqual(("1 of 2", 4, 3, "unknown"), tuple_of(sums)[:4])
        self.assertIn("1 cycle(s)", sums.why)

    def test_a_cycle_on_the_one_author_route_has_no_plan_to_read(self):
        sums = plan_sums([planned(3, 0), cycle(plan_left_out=True)])
        self.assertEqual(("1 of 1", 3, 0, "no", None), tuple_of(sums))

    def test_no_plan_read_gives_no_sums_and_unknown(self):
        sums = plan_sums([cycle(), cycle()])
        self.assertEqual(("0 of 2", 0, 0, "unknown"), tuple_of(sums)[:4])

    def test_plans_that_hold_no_slice_give_unknown(self):
        sums = plan_sums([planned(0, 0)])
        self.assertEqual(("1 of 1", 0, 0, "unknown"), tuple_of(sums)[:4])


def tuple_of(sums):
    """The plans read, the sum planned, the sum too large, the answer and its reason."""
    return (sums.plans_read, sums.planned, sums.too_large, sums.answer, sums.why)


class CountImage(unittest.TestCase):
    def test_the_image_gives_q1_as_numbers_and_the_sums_of_q2(self):
        # Four cycles of two versions: yes, no, unknown and no; the plans 4 (3 too large), 2 (0),
        # none (the one-author route) and 3 (0) read: 9 planned, 3 too large, 9 is not above 9.
        cycles = [
            cycle(contradiction="yes", planned=4, too_large=3),
            cycle(contradiction="no", planned=2, too_large=0),
            cycle(contradiction=None, plan_left_out=True),
            cycle(contradiction="no", planned=3, too_large=0),
        ]
        self.assertEqual(
            [["4", "yes 1 · no 2 · unknown 1", "3 of 3", "9", "3", "no"]], count_image(cycles)
        )

    def test_a_plan_not_read_makes_q2_unknown_in_the_image(self):
        cycles = [
            cycle(contradiction="no", planned=4, too_large=4),
            cycle(contradiction="no", planned=None, too_large=None),
        ]
        self.assertEqual(
            [["2", "yes 0 · no 2 · unknown 0", "1 of 2", "4", "4", "unknown"]], count_image(cycles)
        )

    def test_a_series_of_one_cycle(self):
        cycles = [cycle(contradiction="yes", planned=3, too_large=2)]
        self.assertEqual(
            [["1", "yes 1 · no 0 · unknown 0", "1 of 1", "3", "2", "yes"]], count_image(cycles)
        )


class MechanismImage(unittest.TestCase):
    def rows(self, cycles) -> dict[str, list[str]]:
        """The image as its rows by the measure each is of."""
        return {row[0]: row for row in mechanism_image(cycles)}

    def test_each_measure_gives_the_cycles_with_a_value_and_their_median(self):
        # Calls in all: 10, 4 and 7 in three of four cycles, whose median is 7; the fourth gives
        # none. The share: 12.5% and 13.0% in two cycles, whose median is 12.75%.
        cycles = [
            cycle(measures={CALLS: "10", SHARE: "12.5%"}),
            cycle(measures={CALLS: "4", SHARE: "13.0%"}),
            cycle(measures={CALLS: "7"}),
            cycle(measures={}),
        ]
        rows = self.rows(cycles)
        self.assertEqual([CALLS, "3", "7"], rows[CALLS])
        self.assertEqual([SHARE, "2", "12.75%"], rows[SHARE])

    def test_a_measure_no_cycle_gives_has_a_row_with_no_median(self):
        rows = self.rows([cycle(measures={CALLS: "10"})])
        self.assertEqual(["Calls of subagents", "0", "unknown"], rows["Calls of subagents"])

    def test_every_measure_has_one_row_and_none_a_fall(self):
        rows = mechanism_image([cycle(measures={CALLS: "10"})])
        self.assertEqual(15, len(rows))
        self.assertEqual({3}, {len(row) for row in rows})

    def test_a_series_of_one_cycle_gives_its_values(self):
        self.assertEqual([CALLS, "1", "10"], self.rows([cycle(measures={CALLS: "10"})])[CALLS])


def run(others, total, *directories, code=0) -> GateRun:
    """A run of the gate with the seconds written as decimals; a directory is (name, seconds)."""
    return GateRun(
        others,
        None if total is None else Decimal(total),
        [(name, None if seconds is None else Decimal(seconds)) for name, seconds in directories],
        code,
    )


class GateImage(unittest.TestCase):
    A = DIRECTORY_MEASURE + "gate/a"
    B = DIRECTORY_MEASURE + "gate/b"

    def rows(self, cycles) -> dict[str, list[str]]:
        return {row[0]: row for row in gate_image(cycles)}

    def cycles(self) -> list[Cycle]:
        """Four cycles of two versions. Compared (passed, no other gate): total 100 and 110, gate/a
        60.0 and 70.0. Not compared: with company, total 200 and gate/a 120.0; failed (exit code
        2), total 5.000 and gate/b 1.0; the exit code unknown, total 300 and no directory."""
        return [
            cycle(gate_timed=[run(0, "100.000", ("gate/a", "60.0"))]),
            cycle(gate_timed=[run(0, "110.000", ("gate/a", "70.0"))]),
            cycle(
                gate_timed=[
                    run(1, "200.000", ("gate/a", "120.0")),
                    run(0, "5.000", ("gate/b", "1.0"), code=2),
                ]
            ),
            cycle(gate_timed=[run(0, "300.000", code=None)]),
        ]

    def test_the_runs_compared_and_the_runs_not_compared_are_each_a_number_and_a_median(self):
        # Total: compared 100 and 110 (105.000); not compared 200, 5 and 300 (median 200.000).
        # gate/a: compared 60.0 and 70.0 (65.0); not compared 120.0 (120.0). gate/b: none compared;
        # not compared 1.0.
        rows = self.rows(self.cycles())
        self.assertEqual([TOTAL_MEASURE, "2", "105.000", "3", "200.000"], rows[TOTAL_MEASURE])
        self.assertEqual([self.A, "2", "65.0", "1", "120.0"], rows[self.A])
        self.assertEqual([self.B, "0", "unknown", "1", "1.0"], rows[self.B])

    def test_the_total_stands_first_and_then_each_directory_by_name(self):
        names = [row[0] for row in gate_image(self.cycles())]
        self.assertEqual([TOTAL_MEASURE, self.A, self.B], names)

    def test_the_image_holds_no_fall(self):
        self.assertEqual({5}, {len(row) for row in gate_image(self.cycles())})

    def test_a_run_that_failed_is_not_compared_and_enters_no_median_of_the_compared(self):
        # Break caught: the median taken over all the runs. The failed run of 1.000 second would
        # pull the compared median of 100.000 and 90.000 (95.000) down to 90.000.
        cycles = [
            cycle(gate_timed=[run(0, "100.000"), run(0, "1.000", code=1)]),
            cycle(gate_timed=[run(0, "90.000")]),
        ]
        self.assertEqual([TOTAL_MEASURE, "2", "95.000", "1", "1.000"], gate_image(cycles)[0])

    def test_a_series_of_one_cycle_with_one_run(self):
        cycles = [cycle(gate_timed=[run(0, "100.000", ("gate/a", "60.0"))])]
        self.assertEqual(
            [
                [TOTAL_MEASURE, "1", "100.000", "0", "unknown"],
                [self.A, "1", "60.0", "0", "unknown"],
            ],
            gate_image(cycles),
        )

    def test_a_series_with_no_run_gives_the_total_with_no_run(self):
        self.assertEqual([[TOTAL_MEASURE, "0", "unknown", "0", "unknown"]], gate_image([cycle()]))

    def test_the_values_are_the_times_of_the_two_sorts_of_run_by_measure(self):
        values = gate_values(self.cycles())
        self.assertEqual([Decimal("100.000"), Decimal("110.000")], sorted(values[TOTAL_MEASURE][0]))
        self.assertEqual(
            [Decimal("5.000"), Decimal("200.000"), Decimal("300.000")],
            sorted(values[TOTAL_MEASURE][1]),
        )
        self.assertEqual([TOTAL_MEASURE, self.A, self.B], list(values))


if __name__ == "__main__":
    unittest.main()
