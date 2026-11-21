"""The writing of the result of the audit, moved out of `audit_count.py`.

The result of the count as Markdown in UTF-8 with LF line ends, the same bytes for the same input:
the cells of a table (`cell`, `table`), the sections of the result (`render`) and its writing into
the directory of the results (`write`), as `process-audit/audit_count.py` writes it (WAY-330,
WAY-337, WAY-339). The cycles, the versions and the counts it writes are made by
`record_reading.py` and `version_analysis.py`; no file outside the product is read here. It is
imported, never run, and runs nothing when imported. Standard library only.
"""

from __future__ import annotations

import os
import sys
from decimal import Decimal
from pathlib import Path

from problem_register import COST_LEVELS
from audit_shared import THE_WAY, AuditCountError
from record_reading import MEASURE_LABELS, Cycle, Read
from series_summary import money
from stage_pricing import UNKNOWN, Prices
from version_analysis import (
    COST_MODULE,
    COST_SCRIPT,
    GATE_SCRIPT,
    GATE_TEST_RUNNER,
    MEASURES_SCRIPT,
    Analysis,
    MeasureVersions,
    Series,
    Versions,
    unknown_rows,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

display = remarks_check.display

RESULTS_ENTRY = "audit_results"
SHARE = Decimal("0.1")
UNKNOWN_HEADER = ["Field", "Values", "Why", "First examples"]
SERIES_COST = "Cost"
SERIES_COUNT = "Count of remarks"
COST_HEADER = [
    "Version (commit)",
    "Committed",
    "Cycles",
    "Cycles with a known cost",
    "Median cost (USD)",
    "Q3: cost falls",
]
# The image of a series, the table that stands first under its heading: what its kind carries over
# all the cycles of the series, and no Q3 and no fall (WAY-417).
COST_IMAGE_HEADER = ["Cycles", "Cycles with a known cost", "Median cost (USD)"]
COUNT_IMAGE_HEADER = [
    "Cycles",
    "Q1: contradiction only after code",
    "Plans read",
    "Slices planned",
    "Slices returned too large",
    "Q2: more than a third of slices too large",
]
MECHANISM_IMAGE_HEADER = ["Measure", "Cycles with a value", "Median"]
GATE_IMAGE_HEADER = [
    "Measure",
    "Runs compared",
    "Median (seconds)",
    "Runs not compared",
    "Median of those (seconds)",
]
COUNT_HEADER = [
    "Version (commit)",
    "Committed",
    "Cycles",
    "Q1: contradiction only after code",
    "Plans read",
    "Q2: more than a third of slices too large",
]

# The comparison before and after a fix, the table that stands under the image of a series where it
# has one: a pair of rows for each fixed issue of the register or, for the measures, for each
# measure of it, the side before first. The kind's own columns follow the issue, its fix and the
# side; Q3 and the fall stand beside the side after and nowhere else (WAY-339, WAY-417).
COMPARISON_LEAD = ["Issue", "Fix", "Side"]
COST_COMPARISON_HEADER = [*COMPARISON_LEAD, *COST_IMAGE_HEADER, "Q3: cost falls"]
COUNT_COMPARISON_HEADER = [*COMPARISON_LEAD, *COUNT_IMAGE_HEADER]
MECHANISM_COMPARISON_HEADER = [*COMPARISON_LEAD, *MECHANISM_IMAGE_HEADER, "Falls"]
GATE_COMPARISON_HEADER = [*COMPARISON_LEAD, *GATE_IMAGE_HEADER, "Falls"]

MECHANISM_HEADER = ["Version (commit)", "Measure", "Cycles with a value", "Median", "Falls"]
GATE_HEADER = [
    "Version (commit)",
    "Measure",
    "Runs compared",
    "Median (seconds)",
    "Falls",
    "Runs not compared",
    "Median of those (seconds)",
]


def series_lines(
    title: str,
    number: int,
    block: Series,
    headers: tuple[list[str], list[str], list[str]],
) -> list[str]:
    """The subsection of a series: its heading, the reason it begins where it does, the image of
    all its cycles, the comparisons before and after a fix where it has any and then the table
    with a row for each of its versions; `headers` are those of the image, the comparisons and the
    versions, in that order."""
    image_header, comparison_header, header = headers
    comparison = []
    if block.comparison:
        comparison = [
            "Before and after a fix, inside the series, for each fixed issue of the register "
            "that has cycles on both sides of its fix (the side before first):",
            "",
            *table(comparison_header, block.comparison),
            "",
        ]
    return [
        f"### {title}, series {number}",
        "",
        f"Begins at this version: {block.begins}.",
        "",
        "The image of the series, over all its cycles:",
        "",
        *table(image_header, block.image),
        "",
        *comparison,
        "By version:",
        "",
        *table(header, block.rows),
        "",
    ]


def versions_lines(versions: Versions) -> list[str]:
    """The section *Process versions*: a table per series of the cost and per series of the
    count of remarks, each with the reason it begins where it does, and a note of the cycles in no
    version."""
    lines = [
        "## Process versions",
        "",
        "A version of the process is the commit of the-way that its cycles' *Process pin* "
        "resolves to, ordered by the commit's date. The versions are cut into series of two kinds "
        "(WAY-339), and a measure is compared only inside a series of its own kind: no cell sets "
        "a number of one kind of series beside a number of the other.",
        "",
        "A series of the cost holds the median cost and the answer Q3. It begins at a new price "
        f"list or at a change of `{COST_SCRIPT}` or of the module `{COST_MODULE}` that it imports, "
        "the two files of the script that measures the cost, and at no "
        "other change: not at a change of the instructions of the reviewer.",
        "",
        "A series of the count of remarks holds the answers Q1 and Q2. It begins wherever a "
        "series of the cost begins, and also at a date of *Added* or *Withdrawn* of the "
        "register's list of classes, and at any change of the files that give the form of a "
        "stage report or the instructions of the reviewer: those under `task-cycle/change`, "
        "`task-cycle/plan`, `task-cycle/review` and `task-cycle/spec`, and "
        "`task-cycle/agent-types/the-way-stage.md`, whose text the reviewer receives as its "
        "instruction. The test is `git diff --quiet` (exit 1, or any other failure, counts as "
        "changed), and any change of those files begins a series, whether or not it alters that "
        "form or those instructions. The price of keeping the series of the cost whole across "
        "such a change: a rise of the cost after a change of the reviewer's instructions may be "
        "the reviewer finding more or the process getting dearer, and the count of remarks, "
        "whose meaning changes with the reviewer, is the series that ends there.",
        "",
        "Each series opens with an image of all its cycles, and below it stands a table with a row "
        "for each version. The image of a series of the cost gives its cycles, those with a known "
        "cost and their median cost; the image of a series of the count of remarks gives Q1 and Q2. "
        "Q1 of a group of cycles, a version or a whole series, is the number of its cycles that "
        "answer `yes`, the number that answer `no` and the number that answer `unknown` "
        "(`yes n · no n · unknown n`); each cycle answers for itself. Q2 of a group is the "
        "answer, `yes`, `no` or `unknown`, that the sum of the slices planned and the sum of the "
        "slices returned too large over the cycles whose plans are read (*Plans read*) give: "
        "`unknown` where a plan of the group is not read, or no plan holds a slice. The image and "
        "each side of a comparison show the two sums beside the answer, and the row of a version "
        "shows *Plans read* and the answer. Q3 is `yes`, `no` or `unknown`, and stands only where "
        "two groups meet: in the row of a version, set against the previous version of its "
        "series, and beside the side after of a comparison; an image sets no two groups against "
        "each other, so it holds no Q3. *Unknown values* says why the answer of a version or the "
        "verdict of a comparison is unknown, a cycle's Q1 included; the reason of an unknown "
        "answer of an image or of a side follows from the lines of its versions. The reason each "
        "series begins where it does stands under its heading.",
        "",
        "Where a fixed issue of the register of problems has cycles on both sides of its fix "
        "inside a series, a table under the image compares them: the cycles on the versions that "
        "lack the fix (the side before) against the cycles on the versions that hold it (the side "
        "after), a pair of rows for each such issue, the issues in the order of the register and "
        "never ranked. Whether a version holds the fix is read from the history of git and never "
        "from a date, so a version that is later by date and lacks the fix stands before it; a "
        "version for which git cannot say stands on neither side, and *Unknown values* gives the "
        "reason. Each side gives what the image of its series gives. In a series of the cost, Q3 "
        "stands beside the side after: `yes` where its median cost is lower than that of the side "
        "before, `no` where it is not, `unknown` where a median is not known. A series of the "
        "count of remarks gives the two sides and no answer of its own. A change of the process "
        "with no fixed issue in the register gets no comparison.",
        "",
    ]
    for title, blocks, headers in (
        (SERIES_COST, versions.cost, (COST_IMAGE_HEADER, COST_COMPARISON_HEADER, COST_HEADER)),
        (
            SERIES_COUNT,
            versions.count,
            (COUNT_IMAGE_HEADER, COUNT_COMPARISON_HEADER, COUNT_HEADER),
        ),
    ):
        for number, block in enumerate(blocks, 1):
            lines += series_lines(title, number, block, headers)
    if versions.no_version:
        lines += [
            "### No version",
            "",
            f"{len(versions.no_version)} cycle(s) stand in no version and in no series: their "
            "*Process pin* is unknown, does not resolve in the-way's history, or names a commit "
            "with no readable date. Each reason is in *Unknown values*.",
            "",
        ]
    if lines[-1] == "":
        lines.pop()
    return lines


def measure_versions_lines(measured: MeasureVersions) -> list[str]:
    """The section *Measure versions*: a table per series of each instrument, the median of each
    measure of each version and whether it falls against the previous version of its series."""
    lines = [
        "## Measure versions",
        "",
        "The versions are those of *Process versions*, but the series are not: the measures of how "
        "a cycle's agents use context and the prompt cache and the times of the gate are the "
        "numbers by which a change to the instructions of the cycle is judged, so only a change of "
        "the instrument that measures them splits them (WAY-339). A series of the mechanism "
        f"measures begins at a version whose `{MEASURES_SCRIPT}` differs from the previous "
        f"version's, and a series of the gate times at one whose `{GATE_SCRIPT}` or "
        f"`{GATE_TEST_RUNNER}` differs, by "
        "`git diff --quiet` (exit 1, or any other failure, counts as changed). A new price list, a "
        "date of the register's list of classes and a change under `task-cycle/change`, "
        "`task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` or of "
        f"`{COST_SCRIPT}` or `{COST_MODULE}` split neither, "
        "though a new price list and a change of "
        f"`{COST_SCRIPT}` or `{COST_MODULE}` split the series "
        "of the cost, and the others the series "
        "of the count of remarks. "
        "Each series is its own subsection, a number of one series is never set beside a number of "
        "another, and the cycles in no version stand in no series. *Falls* is `yes` where the "
        "median is lower than the previous version's median of the same measure in the same "
        "series, `no` where it is not, and `unknown` where the version is the first of its series "
        "or either median is not known; *Unknown values* says why. A median is written as the "
        "exact value, a half with its decimal.",
        "",
        "Each series opens with an image of all its cycles, and below it stands a table with a row "
        "for each version. The image holds no *Falls*, which sets a version against the previous "
        "one: it gives the measures of the series as their medians and the numbers behind them.",
        "",
        "Under the image a series has, for each fixed issue of the register of problems that "
        "has cycles on both sides of its fix, the same comparison as in *Process versions*: the "
        "side before and the side after, a pair of rows for each measure, with *Falls* beside the "
        "side after, `yes` where its median is lower than that of the side before. For the gate "
        "times the comparison stands where runs compared (see below) stand on both sides of the "
        "total, and each side takes only the runs compared for its fall.",
        "",
        "*Mechanism measures*: the median is of the values of the version's cycles that give one, "
        "and *Cycles with a value* counts them; in the image they are the cycles of the whole "
        "series.",
        "",
        "*Gate times*: the runs are taken together over all the cycles of the version. The median "
        "and *Falls* take only the runs that passed (exit code 0) during which no other gate run by "
        "the script was going (*Runs compared*, WAY-350). The runs not compared are those with "
        "another gate, with the count `unknown`, that failed (a failed run's time says how soon "
        "it failed, not how long the gate takes) or whose exit code is unknown: they are counted "
        "and their median shown apart in the last two columns and are never compared, so a "
        "version in which no run passed alone has no comparison. Each count is of the runs that "
        "give the time of its row, and a directory's median takes the runs that give its time. A "
        "version in which no cycle gives a value, or no run a time, has one row, with `—` for the "
        "measure, and a value in *Unknown values*. The image of a series takes the runs of all its "
        "cycles, compared and not compared apart in the same way, for the total and for each "
        "directory that any of them has.",
        "",
    ]
    for title, blocks, headers in (
        (
            "Mechanism measures",
            measured.mechanism,
            (MECHANISM_IMAGE_HEADER, MECHANISM_COMPARISON_HEADER, MECHANISM_HEADER),
        ),
        ("Gate times", measured.gate, (GATE_IMAGE_HEADER, GATE_COMPARISON_HEADER, GATE_HEADER)),
    ):
        for number, block in enumerate(blocks, 1):
            lines += series_lines(title, number, block, headers)
    if lines[-1] == "":
        lines.pop()
    return lines


def cell(text: str) -> str:
    """Text on one line that cannot end or split a cell of a table: a bar is written `\\x7c`, as
    `display` writes a control character, so that no cell holds a bar at all. An escaped bar
    `\\|` would not do: Markdown readers differ on whether a backslash before it escapes the bar
    or is itself escaped, and a reader of the second kind ends the cell there."""
    return display(" ".join(str(text).split())).replace("|", "\\x7c")


def duration(seconds: int | None) -> str:
    if seconds is None:
        return UNKNOWN
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"


def share_text(value: Decimal | None) -> str:
    return UNKNOWN if value is None else f"{value.quantize(SHARE)}%"


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    """A Markdown table of the header and the rows, every cell written through `cell`."""
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(cell(text) for text in row) + " |" for row in rows]
    return lines


def measures_lines(cycles: list[Cycle]) -> list[str]:
    """The section *Mechanism measures*: one row per cycle, each label of the file a column."""
    lines = [
        "## Mechanism measures",
        "",
        "Written by `task-cycle/cycle_measures.py` into each cycle's record as "
        "`mechanism_measures.md`; `unknown` is never zero, and *Unknown values* says why. The "
        "table of agents stays in that file.",
        "",
    ]
    rows = [
        [
            cycle.repository,
            cycle.record,
            *[cycle.measures.get(label, UNKNOWN) for label in MEASURE_LABELS],
        ]
        for cycle in cycles
    ]
    return lines + table(["Repository", "Record", *MEASURE_LABELS], rows)


def gate_lines(cycles: list[Cycle]) -> list[str]:
    """The section *Gate runs*: one row per run, a cycle with no run having none."""
    lines = [
        "## Gate runs",
        "",
        "Written by `task-cycle/gate_times.py` into each cycle's record as `gate_times.md`, one row "
        "per run of the gate; times are seconds, and `unknown` is never zero. *Directories* lists "
        "each directory the gate printed with its seconds, and `—` where it printed none.",
        "",
    ]
    rows = [[cycle.repository, cycle.record, *run] for cycle in cycles for run in cycle.gate_runs]
    return lines + table(
        [
            "Repository",
            "Record",
            "Started (UTC)",
            "Exit code",
            "Total seconds",
            "Other gate runs at the same time",
            "Directories",
        ],
        rows,
    )


def intro_lines(reads: list[Read]) -> list[str]:
    """The opening of the result: its description and the section *Repositories*."""
    lines = [
        "# Count of the audit of the process",
        "",
        "Written by `process-audit/audit_count.py`. A cycle is named by its repository and *Record*, "
        "the commit that adds the first copy of its record; *Later copies* are the commits that "
        "add it again after a correction, and the values are read from the last copy. *Process "
        "pin* is the version of the-way the cycle ran on, *Remarks* the number of its process "
        "remarks, and the times are h:mm:ss from the copy's `stages.md`. `unknown` is a value the "
        "copy does not give, never zero; *Unknown values* says why. A cycle of the-way whose own "
        "change changed the tool that wrote a file of its copy has the values of that file "
        "`unknown` for that reason (WAY-339), and stands in the version it ran on.",
        "",
        "## Repositories",
        "",
        "| Repository | Cycles | Read |",
        "|---|---|---|",
    ]
    for read in reads:
        if read.error:
            state = "no: " + read.error
        else:
            state = "yes, a shallow clone whose history may lack cycles" if read.shallow else "yes"
        lines.append(f"| {cell(read.key)} | {len(read.cycles)} | {cell(state)} |")
    return lines


def cycles_lines(cycles: list[Cycle]) -> list[str]:
    """The section *Cycles*: one row per cycle."""
    lines = [
        "",
        "## Cycles",
        "",
        "| Repository | Record | Committed | Folder | Later copies | Process pin | Remarks "
        "| Working time without waiting for tools | Waiting for tools |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for cycle in cycles:
        lines.append(
            f"| {cell(cycle.repository)} | {cycle.record} | {cycle.committed} | {cell(cycle.folder)} "
            f"| {' · '.join(cycle.later) or 'none'} | {cycle.pin or UNKNOWN} "
            f"| {UNKNOWN if cycle.remarks is None else cycle.remarks} | {duration(cycle.working)} "
            f"| {duration(cycle.waiting)} |"
        )
    return lines


def cost_lines(cycles: list[Cycle], prices: Prices) -> list[str]:
    """The section *Cost*: one row per cycle."""
    lines = [
        "",
        "## Cost",
        "",
        f"Prices of the list dated {prices.date}: a cost belongs to that series only, and a new "
        f"list or a change of `{COST_SCRIPT}` or `{COST_MODULE}` "
        "starts a new one (WAY-339). A stretch of "
        "the orchestrator with no token usage costs nothing. A stage report whose section of "
        "stages has the columns *Cache write (5 minutes)* and *Cache write (1 hour)* is priced "
        "with each of them at its own price; an earlier form "
        "has its cache writes inside its input and prices them as input, an approximation. "
        "A cycle whose stage report has no section of stages is priced from its table of "
        "tokens by model at the same prices, and its share of the cost in fix rounds is unknown. "
        "*Fix rounds* is the number of findings files the record's *Review rounds* "
        "names; *Share of the cost in fix rounds* is the cost of the subagent turns given one of "
        "those findings files — each fix and the review of that fix — over the cycle's cost. "
        "`unknown` has its reason in *Unknown values*.",
        "",
        "| Repository | Record | Price list | Cost (USD) | Fix rounds "
        "| Share of the cost in fix rounds |",
        "|---|---|---|---|---|---|",
    ]
    for cycle in cycles:
        lines.append(
            f"| {cell(cycle.repository)} | {cycle.record} | {cell(prices.date)} "
            f"| {money(cycle.cost)} | {UNKNOWN if cycle.rounds is None else cycle.rounds} "
            f"| {share_text(cycle.share)} |"
        )
    return lines


def measures_and_versions_lines(
    cycles: list[Cycle], versions: Versions, measured: MeasureVersions
) -> list[str]:
    """The sections *Mechanism measures*, *Gate runs*, *Process versions* and *Measure versions*."""
    lines = [
        "",
        *measures_lines(cycles),
        "",
        *gate_lines(cycles),
        "",
        *versions_lines(versions),
        "",
        *measure_versions_lines(measured),
        "",
    ]
    return lines


def problems_by_cycle_lines(analysis: Analysis) -> list[str]:
    """The section *Problems by cycle*."""
    lines = [
        "## Problems by cycle",
        "",
        "The problems of the register by class and weight, each problem once; a cycle "
        "with no problem has one row, `none`. *Refused rows* are rows of *Problems* that name this "
        "cycle and were refused for a class, weight, cost of an occurrence or issue the register "
        "lacks; a count with one reads `at least n`, as the refused row is not in it. A count "
        "reads `at least n` also where a problem names as its *Record* a commit that adds the "
        "records of more than one cycle: it counts in none of them. Problems whose cycle no named repository holds, or "
        "whose *Record* names more than one cycle, are in *Unknown values*.",
        "",
    ]
    lines += table(
        [
            "Repository",
            "Record",
            "Class",
            "No problem",
            "Minor",
            "Important",
            "Critical",
            "Refused rows",
        ],
        analysis.cycle_rows,
    )
    return lines


def fixed_issues_lines(analysis: Analysis) -> list[str]:
    """The section *Fixed issues*."""
    lines = [
        "",
        "## Fixed issues",
        "",
        "A fixed issue's problems count apart by whether the *Process pin* of their cycle holds "
        "the fix, by the commit and never by date. `unknown` where the fix is not in the "
        "checkout of the-way, and the reasons are in *Unknown values*. *Refused rows* are refused "
        "rows of *Problems* that name this issue; a count with one reads `at least n`.",
        "",
    ]
    lines += table(
        [
            "Issue",
            "Fix",
            "Problems in cycles whose pin holds the fix",
            "Problems in cycles whose pin lacks it",
            "Problems with an unknown pin",
            "Problems whose cycle is not read",
            "Refused rows",
        ],
        analysis.fixed_rows,
    )
    return lines


def open_issues_lines(analysis: Analysis) -> list[str]:
    """The section *Open issues*."""
    lines = [
        "",
        "## Open issues",
        "",
        "*Cycles its problems came back in* counts the cycles in which a problem of the issue "
        "stands, except the first of them, where it stood and did not come back: `0` where it "
        "stands in one cycle only. It reads `at least n` where refused rows of the issue or "
        "problems of a cycle that is not read may belong to cycles not counted. *Days waiting* "
        "counts from the earliest commit date of the copies its problems' *Record* names to the "
        "day of the run; `—` where the issue has no problem yet. A count of problems with refused "
        "rows of the issue reads `at least n`. The issues are in the order of the register, never "
        "ranked by their counts, and the weighing is the human's.",
        "",
    ]
    lines += table(
        [
            "Issue",
            "Cycles its problems came back in",
            "Problems",
            "Problems whose cycle is not read",
            "Days waiting",
            "Refused rows",
        ],
        analysis.open_rows,
    )
    return lines


def dropped_issues_lines(analysis: Analysis) -> list[str]:
    """The section *Dropped issues*."""
    lines = [
        "",
        "## Dropped issues",
        "",
        "A dropped issue's problems are counted apart; it has no waiting. A count with refused "
        "rows of the issue reads `at least n`.",
        "",
    ]
    lines += table(
        ["Issue", "Cycles", "Problems", "Problems whose cycle is not read", "Refused rows"],
        analysis.dropped_rows,
    )
    return lines


def occurrence_cost_lines(analysis: Analysis) -> list[str]:
    """The section *Cost of an occurrence by issue*."""
    lines = [
        "",
        "## Cost of an occurrence by issue",
        "",
        "For each issue, whatever its fate, how many of its problems stand on each level of the cost "
        "of an occurrence: the highest level that the actual cost of one occurrence reached, the "
        "levels running from the cheapest to the dearest as the columns do; the meaning of each is "
        "in the register's table *Costs of an occurrence*. This is no cost of a cycle, which the "
        "section *Cost* gives in money. A problem counts by its row, whether or not its cycle is "
        "read. *Refused rows* are refused rows of *Problems* that name this issue; a count with one "
        "reads `at least n`. The issues are in the order of the register, never ranked by their "
        "costs, and the weighing is the human's.",
        "",
    ]
    lines += table(["Issue", "Fate", *COST_LEVELS, "Refused rows"], analysis.cost_rows)
    return lines


def unknown_values_lines(
    cycles: list[Cycle], analysis: Analysis, versions: Versions, measured: MeasureVersions
) -> list[str]:
    """The section *Unknown values*: one row for each field and reason of the values the count did
    not establish."""
    lines = [
        "",
        "## Unknown values",
        "",
        "The values the count did not establish, one row for each field and reason, with how many "
        "values the pair has and its first three examples, each as repository, record and value. "
        "The result keeps the number and three examples of each pair, and no option of the count "
        "lists the rest. The full list of a pair's values stands where they are read: the "
        "register's own values (its refused rows and the problems of a cycle it names) in the "
        "register; the cycles' values in the copies of the cycles' records in the history of git. "
        "The values about an issue or a version are made by the count from the register and from "
        "those copies, and have no list of their own.",
        "",
    ]
    entries = [
        (cycle.repository, cycle.record, value, why)
        for cycle in cycles
        for value, why in cycle.unknown
    ]
    entries += dict.fromkeys(analysis.unknown + versions.unknown + measured.unknown)
    entries += analysis.held
    lines += table(UNKNOWN_HEADER, unknown_rows(entries))
    return lines


def render(
    reads: list[Read],
    prices: Prices,
    analysis: Analysis,
    versions: Versions,
    measured: MeasureVersions,
) -> str:
    """The result as the text of one Markdown file: the sections of the count in their order."""
    cycles = [cycle for read in reads for cycle in read.cycles]
    lines = [
        *intro_lines(reads),
        *cycles_lines(cycles),
        *cost_lines(cycles, prices),
        *measures_and_versions_lines(cycles, versions, measured),
        *problems_by_cycle_lines(analysis),
        *fixed_issues_lines(analysis),
        *open_issues_lines(analysis),
        *dropped_issues_lines(analysis),
        *occurrence_cost_lines(analysis),
        *unknown_values_lines(cycles, analysis, versions, measured),
    ]
    return "\n".join(lines) + "\n"


def write(folder: Path, name: str, text: str) -> None:
    target = folder / name
    temporary = folder / f".{name}.tmp"
    try:
        with open(temporary, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(temporary, target)
    except OSError as error:
        raise AuditCountError(
            f"cannot write {name} in the directory of the key "
            f"`{RESULTS_ENTRY}` under `{THE_WAY}`: "
            f"{display(error.strerror or error)}"
        ) from None
