"""The figures of a group of cycles, and the image of a series of them.

The figures that depend on the cycles of a group alone, as `process-audit/version_analysis.py` and
the image of a series both need them (WAY-339, WAY-350, WAY-417): the median (`median_of`,
`median_text`, `money`), the number of a mechanism measure (`measure_number`), the times of the
runs of the gate (`gate_values`), Q1 as the numbers of the cycles that answer each way (`q1_text`)
and Q2 as the sums of the slices of the plans (`plan_sums`). The image of a series is made of those
figures over all the cycles of the series, as the cells of its table: `cost_image`, `count_image`,
`mechanism_image` and `gate_image`, each taking the list of cycles of one series of its kind. An
image sets no two groups against each other, so it carries no answer Q3 and no fall. The cycles it
reads are those of `record_reading.py`; it reads no file and runs no command. It is imported, never
run, and runs nothing when imported. Standard library only.

The comparison before and after a fix is made of the same figures for two groups of cycles, those
on the versions that lack a fix and those on the versions that hold it, both of one series
(WAY-339, WAY-417): `cost_comparison`, `count_comparison`, `mechanism_comparison` and
`gate_comparison`, each taking the issue, its fix and the two lists of cycles, and giving the rows
of a pair for each issue or each measure, with the answer Q3 or the fall where the kind has one,
and the unknown answers with their reasons. Which cycles stand on which side is no business of
this module: `version_analysis.py` decides it from the history of git.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from record_reading import MEASURE_LABELS, SHARE_LABEL, Cycle
from stage_pricing import UNKNOWN

MONEY = Decimal("0.000001")
# The measures of a gate time are the total of the run and each directory it printed (WAY-350).
TOTAL_MEASURE = "Total time of the run"
DIRECTORY_MEASURE = "Directory: "


def median_of(costs: list[Decimal]) -> Decimal | None:
    """The median of the costs: the middle one, or the mean of the two middle ones; None where
    there is none."""
    if not costs:
        return None
    ordered = sorted(costs)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def median_text(median: Decimal | None, suffix: str = "") -> str:
    """A median as the exact value of its Decimal, a half with its decimal, never in exponent
    form."""
    return UNKNOWN if median is None else format(median, "f") + suffix


def money(value: Decimal | None) -> str:
    return UNKNOWN if value is None else format(value.quantize(MONEY), "f")


def measure_number(label: str, text: str) -> Decimal:
    """The value of a cycle-level line that `read_measures` kept: a whole number, or for the share
    a number of percent with one decimal."""
    return Decimal(text[:-1] if label == SHARE_LABEL else text)


def measure_values(cycles: list[Cycle], label: str) -> list[Decimal]:
    """The values of a mechanism measure over the cycles that give one."""
    return [
        measure_number(label, cycle.measures[label]) for cycle in cycles if label in cycle.measures
    ]


def gate_values(cycles: list[Cycle]) -> dict[str, tuple[list[Decimal], list[Decimal]]]:
    """The times of the runs of a group of cycles, by measure: the total first and then each
    directory that any run has, by name. Each measure holds the values of the runs that passed with
    no other gate and apart those of the runs not compared: with another gate, with an unknown
    count, that failed or whose exit code is unknown; a run that does not give the time adds to
    neither (WAY-350)."""
    found: dict[str, tuple[list[Decimal], list[Decimal]]] = {TOTAL_MEASURE: ([], [])}
    for cycle in cycles:
        for run in cycle.gate_timed:
            side = 0 if run.others == 0 and run.code == 0 else 1
            if run.total is not None:
                found[TOTAL_MEASURE][side].append(run.total)
            for name, seconds in run.directories:
                lists = found.setdefault(DIRECTORY_MEASURE + name, ([], []))
                if seconds is not None:
                    lists[side].append(seconds)
    return {name: found[name] for name in [TOTAL_MEASURE, *sorted(found.keys() - {TOTAL_MEASURE})]}


def q1_text(cycles: list[Cycle]) -> str:
    """Q1 of a group of cycles: the number of its cycles whose own answer is `yes`, the number
    whose answer is `no` and the number whose answer is unknown, never one word taken from them
    (WAY-417)."""
    yes = sum(1 for cycle in cycles if cycle.contradiction == "yes")
    no = sum(1 for cycle in cycles if cycle.contradiction == "no")
    return f"yes {yes} · no {no} · unknown {len(cycles) - yes - no}"


@dataclass
class PlanSums:
    """Q2 of a group of cycles: the cell *Plans read*, the sum of the slices planned and the sum of
    those returned too large over the cycles whose plans are read, the answer those sums give and,
    where it is unknown, why."""

    plans_read: str
    planned: int
    too_large: int
    answer: str
    why: str | None


def plan_sums(cycles: list[Cycle]) -> PlanSums:
    """Q2 for a group of cycles: the sums of the slices of the plans that are read, too-large over
    planned, above one third is yes. Where a plan is not read, its slices could turn either answer,
    so the answer is unknown (WAY-417)."""
    planned_cycles = [cycle for cycle in cycles if not cycle.plan_left_out]
    read = [
        cycle
        for cycle in planned_cycles
        if cycle.planned is not None and cycle.too_large is not None
    ]
    plans_read = f"{len(read)} of {len(planned_cycles)}"
    planned = sum(cycle.planned for cycle in read if cycle.planned is not None)
    large = sum(cycle.too_large for cycle in read if cycle.too_large is not None)
    if not read:
        return PlanSums(plans_read, planned, large, "unknown", "no cycle's plan can be read")
    if len(read) < len(planned_cycles):
        why = (
            f"the plans of {len(planned_cycles) - len(read)} cycle(s) are not read, so the share "
            "of the version's slices is not known"
        )
        return PlanSums(plans_read, planned, large, "unknown", why)
    if planned == 0:
        return PlanSums(
            plans_read, planned, large, "unknown", "the plans that are read hold no slice"
        )
    return PlanSums(plans_read, planned, large, "yes" if 3 * large > planned else "no", None)


# The image of a series: one table for each kind of series, as its rows of cells


def cost_image(cycles: list[Cycle]) -> list[list[str]]:
    """The image of a series of the cost: its cycles, those with a known cost, and the median cost
    of those. One row."""
    costs = [cycle.cost for cycle in cycles if cycle.cost is not None]
    return [[str(len(cycles)), str(len(costs)), money(median_of(costs))]]


def count_image(cycles: list[Cycle]) -> list[list[str]]:
    """The image of a series of the count of remarks: its cycles, Q1 as the numbers of the cycles
    that answer each way, *Plans read*, the sums of the slices planned and returned too large over
    the plans that are read, and the answer Q2 those sums give. One row."""
    sums = plan_sums(cycles)
    return [
        [
            str(len(cycles)),
            q1_text(cycles),
            sums.plans_read,
            str(sums.planned),
            str(sums.too_large),
            sums.answer,
        ]
    ]


def mechanism_image(cycles: list[Cycle]) -> list[list[str]]:
    """The image of a series of the mechanism measures: for each measure the number of cycles that
    give a value and the median of those values."""
    rows = []
    for label in MEASURE_LABELS:
        values = measure_values(cycles, label)
        rows.append(
            [
                label,
                str(len(values)),
                median_text(median_of(values), "%" if label == SHARE_LABEL else ""),
            ]
        )
    return rows


def gate_image(cycles: list[Cycle]) -> list[list[str]]:
    """The image of a series of the gate times: for the total and for each directory any run has,
    the runs compared (passed with no other gate beside them) with their number and median, and the
    runs not compared with their number and median, apart (WAY-350)."""
    return [
        [
            name,
            str(len(compared)),
            median_text(median_of(compared)),
            str(len(apart)),
            median_text(median_of(apart)),
        ]
        for name, (compared, apart) in gate_values(cycles).items()
    ]


# The comparison before and after a fix: the rows of a pair for each issue, or each measure of it,
# the side before first (WAY-339, WAY-417)

BEFORE = "before"
AFTER = "after"
NO_ANSWER = "—"  # the cell of the answer in the row of the side before, which answers nothing


@dataclass
class Comparison:
    """The rows of the comparison of a series for one issue, none where it stands in no
    comparison, and its answers that are unknown as (value, why)."""

    rows: list[list[str]] = field(default_factory=list)
    unknown: list[tuple[str, str]] = field(default_factory=list)


def falls_between(
    before: Decimal | None, after: Decimal | None, what: str
) -> tuple[str, str | None]:
    """`yes` where the median after the fix is lower than the median before it, `no` where it is
    not, and `unknown`, with the reason, where either median is not known (WAY-417)."""
    if before is None and after is None:
        return UNKNOWN, f"no median of {what} is known on either side of the fix"
    if before is None:
        return UNKNOWN, f"the median of {what} before the fix is not known"
    if after is None:
        return UNKNOWN, f"the median of {what} after the fix is not known"
    return ("yes" if after < before else "no"), None


def side_rows(
    name: str, fix: str, label: list[str], sides: list[list[str]], answer: str | None
) -> list[list[str]]:
    """The pair of rows of one issue, or of one measure of it: the side before and the side after,
    each as the issue, its fix, the side, the label of the measure where the kind has one, the cells
    of the side and, where the kind has an answer, `—` for the side before and the answer for the
    side after."""
    before, after = sides
    ending = ([], []) if answer is None else ([NO_ANSWER], [answer])
    return [
        [name, fix, BEFORE, *label, *before, *ending[0]],
        [name, fix, AFTER, *label, *after, *ending[1]],
    ]


def cost_comparison(name: str, fix: str, before: list[Cycle], after: list[Cycle]) -> Comparison:
    """The comparison of the cost for a fix: the pair of rows of the issue, where cycles stand on
    both sides, each side as the image of a series of the cost gives it and Q3 beside the side
    after, `yes` where its median cost is lower."""
    if not before or not after:
        return Comparison()
    medians = [
        median_of([cycle.cost for cycle in cycles if cycle.cost is not None])
        for cycles in (before, after)
    ]
    answer, why = falls_between(medians[0], medians[1], "the cost")
    unknown = [(f"cost falls after the fix of issue `{name}`", why)] if why else []
    rows = side_rows(name, fix, [], [cost_image(before)[0], cost_image(after)[0]], answer)
    return Comparison(rows, unknown)


def count_comparison(name: str, fix: str, before: list[Cycle], after: list[Cycle]) -> Comparison:
    """The comparison of the count of remarks for a fix: the pair of rows of the issue, where
    cycles stand on both sides, each side as the image of a series of the count gives it, Q1 as the
    numbers of its cycles and the sums of Q2. It has no answer of its own, only the two sides."""
    if not before or not after:
        return Comparison()
    return Comparison(
        side_rows(name, fix, [], [count_image(before)[0], count_image(after)[0]], None)
    )


def mechanism_comparison(
    name: str, fix: str, before: list[Cycle], after: list[Cycle]
) -> Comparison:
    """The comparison of the mechanism measures for a fix: for each measure the pair of rows of the
    issue, where cycles stand on both sides and any of them gives a value of a measure, each side as
    the image of a series of those measures gives it, and the fall beside the side after: `yes`
    where its median is lower. Where no cycle of either side gives any value there is no median to
    set against another, and no row stands for the issue."""
    if not before or not after:
        return Comparison()
    if not any(measure_values(before + after, label) for label in MEASURE_LABELS):
        return Comparison()
    result = Comparison()
    for label in MEASURE_LABELS:
        suffix = "%" if label == SHARE_LABEL else ""
        values = [measure_values(cycles, label) for cycles in (before, after)]
        medians = [median_of(each) for each in values]
        answer, why = falls_between(medians[0], medians[1], "this measure")
        if why:
            result.unknown.append((f"Measure falls after the fix of issue `{name}`: {label}", why))
        cells = [
            [str(len(each)), median_text(median, suffix)] for each, median in zip(values, medians)
        ]
        result.rows += side_rows(name, fix, [label], cells, answer)
    return result


def gate_comparison(name: str, fix: str, before: list[Cycle], after: list[Cycle]) -> Comparison:
    """The comparison of the gate times for a fix: where runs compared stand on both sides of the
    total, for the total and each directory that any run of either side has, the pair of rows of
    the issue with the runs compared and not compared of each side, as the image of a series of
    the gate times gives them, and the fall beside the side after: `yes` where the median of its
    runs compared is lower (WAY-350)."""
    sides = [gate_values(before), gate_values(after)]
    if not all(side[TOTAL_MEASURE][0] for side in sides):
        return Comparison()
    result = Comparison()
    measures = [TOTAL_MEASURE, *sorted({*sides[0], *sides[1]} - {TOTAL_MEASURE})]
    for measure in measures:
        runs = [side.get(measure, ([], [])) for side in sides]
        medians = [median_of(compared) for compared, _ in runs]
        answer, why = falls_between(medians[0], medians[1], "the runs compared")
        if why:
            result.unknown.append(
                (f"Gate time falls after the fix of issue `{name}`: {measure}", why)
            )
        cells = [
            [
                str(len(compared)),
                median_text(median_of(compared)),
                str(len(apart)),
                median_text(median_of(apart)),
            ]
            for compared, apart in runs
        ]
        result.rows += side_rows(name, fix, [measure], cells, answer)
    return result
