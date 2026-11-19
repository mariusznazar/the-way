"""The reading of a cycle's record and of its files in git history, moved out of `audit_count.py`.

The values of a `Cycle` read from the copy of a record that a commit holds: the record `cycle.md`
(its *Process pin*, its process remarks and the items the questions of a process version read),
`stages.md` (the times, the cost and the share of the fix rounds), `mechanism_measures.md` and
`gate_times.md` (WAY-337, WAY-339, WAY-350), as `process-audit/audit_count.py` counts them; the
classes the reading fills (`Cycle`, `GateRun`, `Read`). The git it runs to read only, the error of the
command and the cells of a table stand in `audit_shared.py`. A record and each file of a copy are
untrusted input (WAY-48). It is imported, never run, and runs nothing when imported. Standard
library only.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

from audit_shared import MAX_BYTES, Git, GitError, is_separator, table_cells
from stage_pricing import (
    TEXT_CAP,
    UNKNOWN,
    Prices,
    StageTokens,
    is_orchestrator_row,
    priced,
    priced_older,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check
from record_items import (  # noqa: E402  the reading of the items of a record
    ITEM_DISCARDED,
    header_field,
    is_report_file,
    item_count_reason,
    item_texts,
    item_words,
    read_contradiction,
    reads_none_first,
    review_rounds,
)

display = remarks_check.display

RECORDS = "docs/task-cycles/"
# A commit as a record writes it: 7 to 40 hexadecimal characters, a digit among them, so that an
# English word written in the letters a-f is not taken for one, standing apart from other letters
# and digits.
COMMIT = r"(?<![0-9A-Za-z])(?=[0-9a-fA-F]*[0-9])[0-9a-fA-F]{7,40}(?![0-9A-Za-z])"
COMMIT_IN_TEXT = re.compile(COMMIT)
MOVED_PIN = re.compile(r"moved to `?(" + COMMIT + r")`?", re.I)
REMARKS_OPENER = re.compile(
    r"(?P<indent>[ \t]*)[-*+][ \t]+Process remarks on the-way(?![\w-])"
    r"[ \t]*:?[ \t]*(?P<rest>.*)"
)
DURATION = re.compile(r"(\d{1,7}):([0-5]\d):([0-5]\d)")
SECTION_TITLE = "Stages: start, waiting for tools and tokens by model"
STAGES_HEADING = "## " + SECTION_TITLE
STAGE_COLUMNS = [
    "#",
    "Stage",
    "Start",
    "Waiting for tools",
    "Model",
    "Input",
    "Cached input",
    "Output",
]
FILES_COLUMN = "Files named"
# The two columns of the cache writes of each lifetime, a pair that follows *Files named* in the
# newest form of the section and is never missing when neither stands (WAY-344).
WRITE_5M_COLUMN = "Cache write (5 minutes)"
WRITE_1H_COLUMN = "Cache write (1 hour)"
WRITE_COLUMNS = [WRITE_5M_COLUMN, WRITE_1H_COLUMN]
# The three forms of the header of the section, each a prefix of the next.
SECTION_FORMS = (
    STAGE_COLUMNS,
    STAGE_COLUMNS + [FILES_COLUMN],
    STAGE_COLUMNS + [FILES_COLUMN] + WRITE_COLUMNS,
)
# The table of tokens by model, which every form of `stages.md` has and the older form is read
# from: the table whose header row begins with `Model`.
MODEL_COLUMN = "Model"
OLDER_COLUMNS = [MODEL_COLUMN, "Total tokens", "Input", "Cached input", "Output"]
OLDER_NEEDED = ("Input", "Cached input", "Output")
# The fields of `stages.md` a form needs, as an `Error:` line names them (WAY-344): no backtick
# stands in a name, since the line writes the name between backticks.
FIELD_SECTION = f"section {SECTION_TITLE}"
FIELD_SECTION_TABLE = f"table of the section {SECTION_TITLE}"
FIELD_OLDER_TABLE = f"table with the first cell {MODEL_COLUMN}"
OLDER_NO_TURNS = (
    "`stages.md` is of the older form, whose table of tokens by model gives no turns, "
    "so no round is tied to the turns that served it"
)
# A findings file is told by the word in its name, as the check of process remarks tells it
# (WAY-294); used only to find a turn given a findings file the record does not name.
FINDINGS_WORD = "findings"
# A token count longer than this is not a count of tokens: no model's input comes near it.
TOKEN_DIGITS = 15
# A cost at or above this many dollars is not given: a crafted count would otherwise overrun the
# precision the cost is written with.
COST_CEILING = Decimal(10) ** 18
# The items of the record the questions of a process version read (task-cycle/record_template.md).
ITEM_PLAN = "Plan"
ITEM_TOO_LARGE = "Slices returned too large"
SLICES_WORD = re.compile(r"slices", re.I)
# The count of slices written just before the word, as `8 slices`: a figure standing alone, no
# letter or digit before it, so `F1a` and `F1–F4` give none. Every repetition is bounded.
SLICES_COUNT = re.compile(r"(?<![A-Za-z0-9])([0-9]{1,6})[ \t]{1,8}slices(?![A-Za-z0-9])", re.I)
# The two files of a cycle's record that the count reads (WAY-339), each written by its
# script: `mechanism_measures.md` by task-cycle/cycle_measures.py, `gate_times.md` by
# task-cycle/gate_times.py. A copy that holds neither is of an earlier cycle or of one whose script
# failed; the causes are named in ABSENCE_CAUSES below.
MEASURES_FILE = "mechanism_measures.md"
GATE_FILE = "gate_times.md"
# The causes of a copy's lacking the file of a script. `gate_times.md` is written only by a gate
# run on the cycle's own system, so a cycle whose final gate ran in CI may hold none (WAY-160).
ABSENCE_CAUSES = {
    MEASURES_FILE: "an earlier cycle, or a script that failed",
    GATE_FILE: "an earlier cycle, a final gate that ran in CI, or a script that failed",
}
MEASURE_LABELS = (
    "Calls in all",
    "Calls of the orchestrator",
    "Calls of subagents",
    "Mean context per call",
    "Mean context per call of the orchestrator",
    "Share of the context in calls above 200000 tokens",
    "Context of the orchestrator's first call",
    "Context of the orchestrator's middle call",
    "Context of the orchestrator's last call",
    "Cache written, 5 minutes",
    "Cache written, 1 hour",
    "Cache written again by the orchestrator",
    "Calls of the orchestrator with a cache write again",
    "Cache written again by subagents",
    "Calls of subagents with a cache write again",
)
SHARE_LABEL = "Share of the context in calls above 200000 tokens"
MEASURE_WHOLE = re.compile(r"[0-9]{1,15}")
MEASURE_SHARE = re.compile(r"([0-9]{1,3}\.[0-9])%")
GATE_COLUMNS = [
    "Started (UTC)",
    "Exit code",
    "Total seconds",
    "Other gate runs at the same time",
    "Directory",
    "Directory seconds",
]
GATE_RUN_COLUMNS = GATE_COLUMNS[:4]
GATE_TABLE_FIELD = "table of the runs"
GATE_STARTED = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}")
GATE_CODE = re.compile(r"[0-9]{1,10}")
GATE_TOTAL = re.compile(r"[0-9]{1,9}\.[0-9]{3}")
GATE_OTHERS = re.compile(r"[0-9]{1,6}")
GATE_SECONDS = re.compile(r"[0-9]{1,9}(?:\.[0-9]{1,9})?")
# The runs and the directories of one run read from `gate_times.md`, the rest not read and said so.
MAX_RUNS = 500
MAX_DIRECTORIES = 50
GATE_NONE = "—"
DIRECTORY_SEPARATOR = " · "


# Reading a cycle


@dataclass
class GateRun:
    """A run of `gate_times.md` as numbers, for the medians of a version: the count of other gate
    runs at the same time, the total seconds, the seconds of each directory and the exit code, each
    None where the file gives it as unknown or in a form that is not its column's."""

    others: int | None
    total: Decimal | None
    directories: list[tuple[str, Decimal | None]] = field(default_factory=list)
    code: int | None = None  # the exit code of the run, None where the file gives it as unknown


@dataclass
class Cycle:
    repository: str
    folder: str
    record: str
    committed: str
    later: list[str] = field(default_factory=list)
    # The commit date of each copy, the first and the later ones, by its commit; `unknown` where
    # the date cannot be read.
    copies: dict[str, str] = field(default_factory=dict)
    pin: str | None = None
    remarks: int | None = None
    working: int | None = None
    waiting: int | None = None
    cost: Decimal | None = None
    rounds: int | None = None
    share: Decimal | None = None
    # The questions of the process version: Q1 as yes, no or unknown; the plan's slices, and the
    # slices returned too large, each None where unknown; and whether the plan is left out (the
    # one-author route).
    contradiction: str | None = None
    plan_left_out: bool = False
    planned: int | None = None
    too_large: int | None = None
    unknown: list[tuple[str, str]] = field(default_factory=list)
    # The fields of `stages.md` a form needs that the copy lacks, as an `Error:` line names them
    # (WAY-344): the run ends with exit code 1 where any cycle has one.
    missing: list[str] = field(default_factory=list)
    # The values of `mechanism_measures.md` by label, each as the file writes it; a label not here
    # is unknown.
    measures: dict[str, str] = field(default_factory=dict)
    # The runs of `gate_times.md`, each as the cells after the repository and the record.
    gate_runs: list[list[str]] = field(default_factory=list)
    # The same runs as numbers, one for each of `gate_runs`, in the same order (WAY-350).
    gate_timed: list[GateRun] = field(default_factory=list)
    # The fields of the two files that the copy lacks, as (file, field), for the `Error:` line.
    missing_in: list[tuple[str, str]] = field(default_factory=list)
    # The files of the copy that held a text to read (`stages.md`, `mechanism_measures.md`,
    # `gate_times.md`): a copy that holds no such file is of an earlier form and is not put in
    # doubt by a change of the tool that would write it.
    held: set[str] = field(default_factory=set)


@dataclass
class Read:
    key: str
    cycles: list[Cycle] = field(default_factory=list)
    error: str | None = None
    shallow: bool = False


def header_fields(lines: list[str], fenced: list[bool], label: str) -> list[str]:
    """The values of the record's header lines `- <label>: ...`, or `- <label> and ...: ...` as
    earlier records join two fields, before its first `## ` heading, each with the indented lines
    that continue it joined to it."""
    values: list[list[str]] = []
    collecting = False
    for line, inside_fence in zip(lines, fenced):
        if inside_fence:
            collecting = False
            continue
        if line.startswith("## "):
            break
        found = header_field(line)
        if found:
            collecting = found[0] == label or found[0].startswith(label + " and ")
            if collecting:
                values.append([found[1]])
        elif collecting and line.strip() and line[:1] in " \t":
            values[-1].append(line.strip())
        else:
            collecting = False
    return [" ".join(part for part in parts if part) for parts in values]


def process_pin(text_lines, fenced, own: bool) -> tuple[str | None, str | None]:
    """The version of the-way the record names, or None with the reason."""
    pins = header_fields(text_lines, fenced, "Process pin")
    if len(pins) > 1:
        return None, "the record holds the line `Process pin` more than once"
    if pins:
        moved = MOVED_PIN.search(pins[0])
        if moved:
            return moved.group(1).lower(), None
        found = COMMIT_IN_TEXT.search(pins[0])
        if found:
            return found.group(0).lower(), None
        if not own:
            return None, "the line `Process pin` names no commit"
    elif not own:
        return None, "the record holds no line `Process pin`"
    bases = header_fields(text_lines, fenced, "Target branch and base")
    if len(bases) != 1:
        return None, (
            "the line `Process pin` names no commit, and the line "
            "`Target branch and base` is " + ("doubled" if bases else "missing")
        )
    found = COMMIT_IN_TEXT.search(bases[0])
    if not found:
        return None, "neither the line `Process pin` nor `Target branch and base` names a commit"
    return found.group(0).lower(), None


def remarks_count(lines: list[str], fenced: list[bool]) -> tuple[int | None, str | None]:
    """The number of sub-items under the item `Process remarks on the-way`, or None with the
    reason."""
    openers = [
        index
        for index, line in enumerate(lines)
        if not fenced[index] and REMARKS_OPENER.fullmatch(line)
    ]
    if not openers:
        return None, "the record holds no item `Process remarks on the-way`: an earlier form"
    if len(openers) > 1:
        return None, "the record holds the item `Process remarks on the-way` more than once"
    start = openers[0]
    opener = REMARKS_OPENER.fullmatch(lines[start])
    base = remarks_check.indent_of(lines[start])
    markers: list[int] = []
    for line, inside_fence in zip(lines[start + 1 :], fenced[start + 1 :]):
        if not line.strip():
            continue
        indent = remarks_check.indent_of(line)
        if indent <= base or (not inside_fence and remarks_check.HEADING.fullmatch(line)):
            break
        if not inside_fence and remarks_check.MARKER.fullmatch(line):
            markers.append(indent)
    if markers:
        return markers.count(min(markers)), None
    if remarks_check.reads_none(opener.group("rest")):
        return 0, None
    return None, (
        "the item `Process remarks on the-way` holds no sub-items under it and does not "
        "read `none`: an earlier form"
    )


def stages_time(
    lines: list[str], fenced: list[bool], prefix: str, what: str
) -> tuple[int | None, str | None]:
    """The seconds a line of `stages.md` gives, or None with the reason."""
    values = [
        line[len(prefix) :].strip()
        for line, inside_fence in zip(lines, fenced)
        if not inside_fence and line.startswith(prefix)
    ]
    if not values:
        return None, f"`stages.md` holds no line `{prefix[2:-1]}`: an earlier form"
    if len(values) > 1:
        return None, f"`stages.md` holds the line `{prefix[2:-1]}` more than once"
    if values[0].casefold().startswith(UNKNOWN):
        return None, f"`stages.md` gives the {what} as unknown"
    match = DURATION.fullmatch(values[0])
    if not match:
        return None, f"`stages.md` gives the {what} in a form that is not h:mm:ss"
    hours, minutes, seconds = (int(part) for part in match.groups())
    return hours * 3600 + minutes * 60 + seconds, None


def has_line(lines: list[str], fenced: list[bool], prefix: str) -> bool:
    """Whether a line of `stages.md` outside code fences begins with `prefix`."""
    return any(not inside and line.startswith(prefix) for line, inside in zip(lines, fenced))


def missing_line(cycle: Cycle, prefix: str) -> str:
    """Record the time line `prefix` as a field `stages.md` lacks, and give the reason."""
    name = f"line {prefix[2:-1]}"
    cycle.missing.append(name)
    return missing_reason(name)


def token_count(text: str) -> int | None:
    digits = text.replace(",", "")
    if digits.isascii() and digits.isdigit() and len(digits) <= TOKEN_DIGITS:
        return int(digits)
    return None


def files_cell(text: str) -> tuple[frozenset[str] | None, bool]:
    """The files a cell *Files named* gives, and whether it reads as such: empty, `unknown`, or
    files of `reports/` joined by `, `."""
    if not text:
        return frozenset(), True
    if text == UNKNOWN:
        return None, True
    files = [part.strip() for part in text.split(",")]
    if not all(is_report_file(path) for path in files):
        return None, False
    return frozenset(files), True


@dataclass
class StageTable:
    """What `stages.md` gives for its cost, in the form its own signs name (WAY-337): the
    rows of the section of the newer form, or of the table of tokens by model of the older form
    (`older`); `named` is whether the section's table has the column *Files named*. `rows` is None
    with the `reason` where they cannot be read; `missing` holds the fields the form needs that the
    file lacks (WAY-344), which are no refusal of the form but a field not found."""

    rows: list[StageTokens] | None = None
    named: bool = False
    older: bool = False
    reason: str | None = None
    missing: list[str] = field(default_factory=list)


def missing_columns(found: list[str], needed, where: str) -> list[str]:
    """The fields that name each column of `needed` that the header row `found` lacks, in the
    order of `needed`."""
    return [f"column {name} of the table {where}" for name in needed if name not in found]


def stage_table(lines: list[str], fenced: list[bool]) -> StageTable:
    """The rows `stages.md` gives for the cost. The newer form is known by the heading of its
    section, and is read from the table of that section; without the heading the file is of the
    older form, read from its table of tokens by model. A file with neither lacks the section and
    the table (WAY-344)."""
    headings = [
        index
        for index, (line, inside) in enumerate(zip(lines, fenced))
        if not inside and line.strip() == STAGES_HEADING
    ]
    if len(headings) > 1:
        return StageTable(reason="`stages.md` holds that section more than once")
    if headings:
        return section_table(lines, fenced, headings[0])
    return older_table(lines, fenced)


def section_table(lines: list[str], fenced: list[bool], heading: int) -> StageTable:
    """The newer form: the rows of the table under the heading of the section. A heading with no
    table, or a table whose header row lacks one of the columns the form needs, is a field missing;
    the column *Files named* is never one: a section without it is the earlier form of the
    section. The two columns of the cache writes are a pair: with neither the table is of an earlier
    form, and with one the other is a field missing."""
    table: list[list[str]] = []
    for line, inside in zip(lines[heading + 1 :], fenced[heading + 1 :]):
        if inside:
            continue
        if line.startswith("#"):
            break
        if line.startswith("|"):
            table.append(table_cells(line))
    if not table:
        return StageTable(
            reason="the section in `stages.md` holds no table", missing=[FIELD_SECTION_TABLE]
        )
    where = f"of the section {SECTION_TITLE}"
    absent = missing_columns(table[0], STAGE_COLUMNS, where)
    written = [name for name in WRITE_COLUMNS if name in table[0]]
    if len(written) == 1:
        absent += missing_columns(
            table[0], [name for name in WRITE_COLUMNS if name not in written], where
        )
    if absent:
        return StageTable(
            reason="the table of the section in `stages.md` lacks a column", missing=absent
        )
    if table[0] not in SECTION_FORMS:
        return StageTable(
            reason=(
                "the table of the section in `stages.md` is not of the form the stage report gives"
            )
        )
    named = len(table[0]) > len(STAGE_COLUMNS)
    writes = len(table[0]) > len(STAGE_COLUMNS) + 1
    columns = len(table[0])
    body = [cells for cells in table[1:] if not is_separator(cells)]
    if not body:
        return StageTable(reason="the section in `stages.md` holds no stage row")
    rows: list[StageTokens] = []
    for cells in body:
        if len(cells) != columns:
            return StageTable(
                reason=(
                    f"a row of the section in `stages.md` has {len(cells)} cells, not {columns}"
                )
            )
        counts = [token_count(cells[index]) for index in (5, 6, 7)]
        if writes:
            counts += [token_count(cells[index]) for index in (9, 10)]
        if any(count is None for count in counts):
            return StageTable(
                reason=(
                    "a token count in the section of `stages.md` is not a number "
                    f"of at most {TOKEN_DIGITS} digits"
                )
            )
        row = StageTokens(cells[0], cells[1], cells[4], *counts[:3])
        if writes:
            row.write_5m, row.write_1h = counts[3], counts[4]
        if named:
            row.files, row.files_read = files_cell(cells[8])
        rows.append(row)
    return StageTable(rows=rows, named=named)


def older_table(lines: list[str], fenced: list[bool]) -> StageTable:
    """The older form: the rows of the table of tokens by model, the one table of `stages.md`
    whose header row begins with `Model`, found exactly once. Without it the file lacks the section
    and the table; written twice, no row is chosen and the cost is unknown with no field missing;
    a header row without one of the columns the cost needs is a field missing, and in another
    order, or with another column beside them, none is and the table is refused."""
    starts = [
        index
        for index, (line, inside) in enumerate(zip(lines, fenced))
        if not inside
        and line.startswith("|")
        and table_cells(line)[:1] == [MODEL_COLUMN]
        and (index == 0 or fenced[index - 1] or not lines[index - 1].startswith("|"))
    ]
    if not starts:
        return StageTable(
            reason=(
                "`stages.md` holds neither the section `"
                + SECTION_TITLE
                + "` nor a table of tokens by model"
            ),
            missing=[FIELD_SECTION, FIELD_OLDER_TABLE],
        )
    if len(starts) > 1:
        return StageTable(reason="`stages.md` holds the table of tokens by model more than once")
    start = starts[0]
    header = table_cells(lines[start])
    absent = missing_columns(header, OLDER_NEEDED, f"with the first cell {MODEL_COLUMN}")
    if absent:
        return StageTable(
            reason="the table of tokens by model in `stages.md` lacks a column", missing=absent
        )
    form = "the table of tokens by model in `stages.md` is not of the form the stage report gives"
    if header != OLDER_COLUMNS:
        return StageTable(reason=form)
    if (
        start + 1 >= len(lines)
        or fenced[start + 1]
        or not lines[start + 1].startswith("|")
        or not is_separator(table_cells(lines[start + 1]))
    ):
        return StageTable(reason=form)
    body: list[list[str]] = []
    for index in range(start + 2, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            break
        body.append(table_cells(lines[index]))
    if not body:
        return StageTable(reason="the table of tokens by model in `stages.md` holds no model row")
    rows: list[StageTokens] = []
    for number, cells in enumerate(body, 1):
        if len(cells) != len(OLDER_COLUMNS):
            return StageTable(
                reason=(
                    f"a row of the table of tokens by model in `stages.md` has "
                    f"{len(cells)} cells, not {len(OLDER_COLUMNS)}"
                )
            )
        counts = [token_count(cells[index]) for index in range(1, len(OLDER_COLUMNS))]
        if any(count is None for count in counts):
            return StageTable(
                reason=(
                    "a token count in the table of tokens by model in "
                    f"`stages.md` is not a number of at most {TOKEN_DIGITS} "
                    "digits"
                )
            )
        rows.append(StageTokens(str(number), cells[0], cells[0], counts[1], counts[2], counts[3]))
    return StageTable(rows=rows, older=True)


def read_plan(lines: list[str], fenced: list[bool]) -> tuple[bool, int | None, str | None]:
    """The item *Plan* of a record: whether the plan is left out (the one-author route), the
    slices it made, or None with the reason. The count is the figure written just before the word
    `slices`, as in `8 slices`; with no such figure or with more than one, the count is not
    read."""
    items = item_texts(lines, fenced, ITEM_PLAN)
    if len(items) != 1:
        return False, None, item_count_reason(ITEM_PLAN, items)
    text = item_words(items[0][0], items[0][1])
    if reads_none_first(text):
        return True, None, None
    if SLICES_WORD.search(text) is None:
        return False, None, "the item `Plan` names no count of slices"
    figures = SLICES_COUNT.findall(text)
    if len(figures) != 1:
        return (
            False,
            None,
            ("the item `Plan` does not give one count of slices before the word `slices`"),
        )
    return False, int(figures[0]), None


def read_too_large(lines: list[str], fenced: list[bool]) -> tuple[int | None, str | None]:
    """The item *Slices returned too large*: 0 where it reads `none`, the number of its sub-items
    where it lists them, or None with the reason."""
    items = item_texts(lines, fenced, ITEM_TOO_LARGE)
    if len(items) != 1:
        return None, item_count_reason(ITEM_TOO_LARGE, items)
    rest, below = items[0]
    if reads_none_first(rest) and not any(text.strip() for text, _ in below):
        return 0, None
    markers = [
        remarks_check.indent_of(text)
        for text, inside in below
        if not inside and remarks_check.MARKER.fullmatch(text)
    ]
    if rest.strip() or not markers:
        return None, (
            "the item `Slices returned too large` reads neither none nor a sub-item per slice"
        )
    base = min(markers)
    return sum(1 for indent in markers if indent == base), None


def process_questions(
    cycle: Cycle, lines: list[str] | None, fenced: list[bool] | None, reason: str | None
) -> None:
    """Read the questions of a process version from the cycle's record; a value that cannot be
    read is `unknown` with its reason, and the record missing makes all of them unknown."""
    if lines is None or fenced is None:
        cycle.unknown += [(ITEM_DISCARDED, reason), (ITEM_PLAN, reason), (ITEM_TOO_LARGE, reason)]
        return
    cycle.contradiction, why = read_contradiction(lines, fenced)
    if why:
        cycle.unknown.append((ITEM_DISCARDED, why))
    cycle.plan_left_out, cycle.planned, why = read_plan(lines, fenced)
    if cycle.plan_left_out:
        return
    if why:
        cycle.unknown.append((ITEM_PLAN, why))
    cycle.too_large, why = read_too_large(lines, fenced)
    if why:
        cycle.unknown.append((ITEM_TOO_LARGE, why))
    elif cycle.planned is not None and cycle.too_large > cycle.planned:
        cycle.too_large = None
        cycle.unknown.append(
            (ITEM_TOO_LARGE, "more slices are returned too large than the plan made")
        )


def missing_reason(name: str, file: str = "stages.md") -> str:
    return f"the file `{file}` of the copy lacks the field `{name}`"


def add_cost(
    cycle: Cycle,
    record_lines: list[str] | None,
    record_fenced: list[bool] | None,
    record_reason: str | None,
    stages_lines: list[str],
    stages_fenced: list[bool],
    prices: Prices,
) -> None:
    """The cycle's cost at the list's prices and the share of its fix rounds in it; a value that
    cannot be given is `unknown` with its reason, never zero. A field the form of `stages.md` needs
    and the file lacks is also put on the cycle's `missing`, for the `Error:` line (WAY-344)."""
    table = stage_table(stages_lines, stages_fenced)
    if table.rows is None:
        if table.missing:
            for name in table.missing:
                cycle.missing.append(name)
                cycle.unknown += [
                    ("Cost", missing_reason(name)),
                    ("Fix rounds share", missing_reason(name)),
                ]
        else:
            cycle.unknown += [("Cost", table.reason), ("Fix rounds share", table.reason)]
        return
    costs, reason = (priced_older if table.older else priced)(table.rows, prices)
    if costs is None:
        cycle.unknown += [("Cost", reason), ("Fix rounds share", reason)]
        return
    total = sum(costs, Decimal(0))
    if total >= COST_CEILING:
        cycle.unknown += [
            ("Cost", "the cost is at or above the command's limit of 10^18 USD"),
            ("Fix rounds share", "the cost is at or above the command's limit"),
        ]
        return
    cycle.cost = total
    if table.older:
        # The table of tokens by model ties no round to the turns that served it: the share is
        # unknown, but the number of rounds stands in the record.
        cycle.unknown.append(("Fix rounds share", OLDER_NO_TURNS))
    if record_lines is None:
        cycle.unknown.append(("Fix rounds share", record_reason))
        return
    findings, reason = review_rounds(record_lines, record_fenced)
    if findings is None:
        cycle.unknown.append(("Fix rounds share", reason))
        return
    cycle.rounds = len(findings)
    if table.older:
        return
    reason = fix_rounds_share(table.rows, costs, total, table.named, findings, cycle)
    if reason:
        cycle.unknown.append(("Fix rounds share", reason))


def fix_rounds_share(
    rows: list[StageTokens],
    costs: list[Decimal],
    total: Decimal,
    named: bool,
    findings: list[str],
    cycle: Cycle,
) -> str | None:
    """Set the share of the cost spent in the fix rounds whose findings files the record names:
    the cost of the subagent turns given one of those files, each turn once, over the cycle's
    cost (WAY-337). Returns the reason where it cannot be given."""
    if not named:
        return f"`stages.md` has no column `{FILES_COLUMN}`: an earlier form"
    if total == 0:
        return "the stages hold no tokens"
    turns: dict[str, tuple[frozenset[str] | None, Decimal]] = {}
    names: dict[str, str] = {}
    for row, cost in zip(rows, costs):
        if is_orchestrator_row(row.name):
            continue
        if not row.files_read:
            return (
                f"the cell `{FILES_COLUMN}` of stage `{row.name[:TEXT_CAP]}` is not a list of "
                "files of `reports/`"
            )
        if row.number in turns:
            # The model rows of one turn repeat its stage and its files; rows that disagree do
            # not tell which of them the turn was given.
            files, spent = turns[row.number]
            if names[row.number] != row.name or files != row.files:
                return (
                    f"the rows of stage number {row.number[:TEXT_CAP]} disagree in their stage "
                    f"or in their cell `{FILES_COLUMN}`"
                )
            turns[row.number] = (files, spent + cost)
        else:
            turns[row.number] = (row.files, cost)
            names[row.number] = row.name
    given = [files for files, _ in turns.values() if files is not None]
    unread = len(turns) - len(given)
    extra = sorted(
        {path for files in given for path in files if FINDINGS_WORD in path.rsplit("/", 1)[-1]}
        - set(findings)
    )
    if extra:
        return (
            f"{len(extra)} findings file(s) the subagent turns were given are not named by "
            f"the item `Review rounds`, which names {len(findings)}: the record and "
            "`stages.md` do not agree"
        )
    if unread:
        # Such a turn may be a fix or the review of a fix: neither `none` nor a share without it
        # can be told.
        return (
            f"the message of {unread} subagent turn(s) could not be read, so whether they "
            "serve a fix round is not known"
        )
    for path in findings:
        count = sum(1 for files in given if path in files)
        if count < 2:
            return (
                f"the findings file `{path}` that the item `Review rounds` names is named by "
                f"{count} subagent turn(s), and a round has a fix and the review of that fix"
            )
    spent = sum(
        (cost for files, cost in turns.values() if files is not None and files & set(findings)),
        Decimal(0),
    )
    cycle.share = spent / total * 100
    return None


def tree_entries(git: Git, commit: str) -> dict[bytes, tuple[bytes, bytes, str, str]]:
    """Every file under docs/task-cycles/ at a commit: its mode, type, object and size."""
    raw = git.run("ls-tree", "-r", "-z", "-l", "--full-tree", commit, "--", ":(literal)" + RECORDS)
    found = {}
    for entry in raw.split(b"\0"):
        if entry:
            metadata, path = entry.split(b"\t", 1)
            mode, kind, sha, size = metadata.split()
            found[path] = (mode, kind, sha.decode("ascii"), size.decode("ascii"))
    return found


def read_file(git: Git, entries: dict, path: bytes) -> tuple[str | None, str | None]:
    """The text of a file of the copy, or None with the reason; a symbolic link or a submodule
    is not followed."""
    name = path.rsplit(b"/", 1)[-1].decode("ascii")
    if path not in entries:
        return None, f"the copy holds no `{name}`"
    mode, kind, sha, size = entries[path]
    if kind != b"blob" or not mode.startswith(b"100"):
        return None, f"`{name}` of the copy is no regular file"
    if not size.isdigit() or int(size) > MAX_BYTES:
        return None, f"`{name}` of the copy is larger than {MAX_BYTES} bytes"
    data = git.run("cat-file", "blob", sha)
    try:
        return data.decode("utf-8-sig"), None
    except UnicodeDecodeError:
        return None, f"`{name}` of the copy is not UTF-8"


def read_optional(
    git: Git, entries: dict, prefix: bytes, name: str
) -> tuple[str | None, str | None]:
    """The text of a file of the copy that an earlier form lacks, or None with the reason: the
    copy may be of an earlier cycle or of one whose script failed, and for `gate_times.md` of one
    whose final gate ran in CI."""
    path = prefix + name.encode("ascii")
    if path not in entries:
        return None, (
            f"the copy holds no `{name}`: {ABSENCE_CAUSES[name]} "
            "(the record's *Verification* says which)"
        )
    return read_file(git, entries, path)


def guarded_optional(
    git: Git, entries: dict, prefix: bytes, name: str
) -> tuple[str | None, str | None]:
    """`read_optional`, with a failure of git on this file given as its reason."""
    try:
        return read_optional(git, entries, prefix, name)
    except (GitError, ValueError, UnicodeError) as error:
        return None, f"git could not read the copy: {display(error)}"


def measure_fits(label: str, value: str) -> bool:
    """Whether a value of `mechanism_measures.md` is what its label gives: a whole number, and for
    the share a number of percent up to 100."""
    if label == SHARE_LABEL:
        found = MEASURE_SHARE.fullmatch(value)
        return found is not None and Decimal(found.group(1)) <= 100
    return MEASURE_WHOLE.fullmatch(value) is not None


def read_measures(cycle: Cycle, text: str | None, reason: str | None) -> None:
    """Read the cycle-level lines of `mechanism_measures.md` by their labels. A label the
    file lacks is a missing field: then every value of the file is unknown, and the field is named
    for the `Error:` line (WAY-344). A label written twice, a value that is not what its label gives
    or `unknown` is unknown with its reason, and the count goes on."""
    if text is None:
        cycle.unknown.append(("Mechanism measures", reason))
        return
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    found = {label: header_fields(lines, fenced, label) for label in MEASURE_LABELS}
    absent = [label for label in MEASURE_LABELS if not found[label]]
    if absent:
        for label in MEASURE_LABELS:
            if label in absent:
                cycle.missing_in.append((MEASURES_FILE, label))
                cycle.unknown.append((label, missing_reason(label, MEASURES_FILE)))
            else:
                cycle.unknown.append(
                    (label, f"`{MEASURES_FILE}` lacks a field, so its values are unknown")
                )
        return
    for label in MEASURE_LABELS:
        values = found[label]
        if len(values) > 1:
            cycle.unknown.append(
                (label, f"`{MEASURES_FILE}` holds the line `{label}` more than once")
            )
        elif values[0] == UNKNOWN:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` gives it as unknown"))
        elif measure_fits(label, values[0]):
            cycle.measures[label] = values[0]
        else:
            cycle.unknown.append(
                (label, f"`{MEASURES_FILE}` gives it in a form that is not what its label gives")
            )


def gate_value(
    reasons: list[tuple[str, str]], column: str, value: str, pattern: re.Pattern, why: str
) -> str:
    """A cell of a run in `gate_times.md` as written where it has the form of its column, else
    `unknown` with the reason kept in `reasons` under the value `Gate runs: <column>`."""
    if pattern.fullmatch(value):
        return value
    reasons.append(
        (f"Gate runs: {column}", f"`{GATE_FILE}` gives it as unknown" if value == UNKNOWN else why)
    )
    return UNKNOWN


def gate_header(cycle: Cycle, lines: list[str], fenced: list[bool]) -> tuple[int, list[str]] | None:
    """The index of the header row of the table of `gate_times.md` and its cells, or None where
    the file lacks the table or one of its six columns: each is a missing field (WAY-344), put on
    the cycle for the `Error:` line, and the runs are not read."""
    header = next(
        (
            index
            for index, (line, inside) in enumerate(zip(lines, fenced))
            if not inside and line.startswith("|")
        ),
        None,
    )
    if header is None:
        cycle.missing_in.append((GATE_FILE, GATE_TABLE_FIELD))
        cycle.unknown.append(("Gate runs", missing_reason(GATE_TABLE_FIELD, GATE_FILE)))
        return None
    names = table_cells(lines[header])
    absent = [name for name in GATE_COLUMNS if name not in names]
    for name in absent:
        field_name = f"column {name} of the table"
        cycle.missing_in.append((GATE_FILE, field_name))
        cycle.unknown.append(("Gate runs", missing_reason(field_name, GATE_FILE)))
    if absent:
        return None
    return header, names


def gate_table_runs(
    lines: list[str],
    fenced: list[bool],
    header: int,
    names: list[str],
    reasons: list[tuple[str, str]],
) -> list[tuple[list[str] | None, list[tuple[str, str]]]]:
    """The runs of the table under its header row, each as its four run cells, or None for a row
    of the wrong number of cells, and its directories as (name, seconds). The runs and the
    directories beyond the limits, and the rows after a line that is no row of the table, are not
    read, and the reason of each is added to `reasons`."""
    at = {name: names.index(name) for name in GATE_COLUMNS}
    runs: list[tuple[list[str] | None, list[tuple[str, str]]]] = []
    last: list[str] | None = None
    cut_directories = False
    table_end = len(lines)
    for index in range(header + 1, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            table_end = index
            break
        cells = table_cells(lines[index])
        if is_separator(cells):
            continue
        # A row of the wrong number of cells is a run of its own, and the limit counts it too.
        wide = len(cells) != len(names)
        key = None if wide else [cells[at[name]] for name in GATE_RUN_COLUMNS]
        if wide or last is None or key != last:
            if len(runs) >= MAX_RUNS:
                reasons.append(
                    (
                        "Gate runs",
                        f"`{GATE_FILE}` holds more than {MAX_RUNS} runs: the rest are not read",
                    )
                )
                break
            if wide:
                reasons.append(
                    (
                        "Gate runs",
                        f"a row of the table in `{GATE_FILE}` has "
                        f"{len(cells)} cells, not {len(names)}",
                    )
                )
                runs.append((None, []))
                last = None
                continue
            runs.append((key, []))
            last = key
        directory, seconds = cells[at["Directory"]], cells[at["Directory seconds"]]
        if directory == GATE_NONE and seconds == GATE_NONE:
            continue
        directories = runs[-1][1]
        if len(directories) >= MAX_DIRECTORIES:
            cut_directories = True
            continue
        directories.append((directory, seconds))
    if any(
        not fenced[index] and lines[index].startswith("|") for index in range(table_end, len(lines))
    ):
        reasons.append(
            (
                "Gate runs",
                f"`{GATE_FILE}` holds a row after a line that is not a row of "
                "the table: the rows after it are not read",
            )
        )
    if cut_directories:
        reasons.append(
            (
                "Gate runs: Directories",
                f"a run in `{GATE_FILE}` lists more than "
                f"{MAX_DIRECTORIES} directories: the rest are "
                "not listed",
            )
        )
    return runs


def add_gate_run(
    cycle: Cycle,
    key: list[str] | None,
    directories: list[tuple[str, str]],
    reasons: list[tuple[str, str]],
) -> None:
    """Add one run of the table to the cycle, as the cells of the table of runs and as the numbers
    for the medians of a version (WAY-350). A cell of the wrong form is `unknown`, with its reason
    added to `reasons`; a row of the wrong number of cells (`key` None) gives a run with every
    value unknown."""
    if key is None:
        cycle.gate_runs.append([UNKNOWN] * 5)
        cycle.gate_timed.append(GateRun(None, None))
        return
    started, code, total, others = [
        gate_value(reasons, column, value, pattern, why)
        for column, value, pattern, why in zip(
            GATE_RUN_COLUMNS,
            key,
            (GATE_STARTED, GATE_CODE, GATE_TOTAL, GATE_OTHERS),
            (
                "a start is not written YYYY-MM-DD HH:MM:SS.mmm",
                "an exit code is not a whole number",
                "a total is not written as seconds to three decimals",
                "a count of other gate runs is not a whole number",
            ),
        )
    ]
    listed = []
    # The numbers of the run: a directory written twice in it counts once, at its first time.
    timed = GateRun(
        None if others == UNKNOWN else int(others),
        None if total == UNKNOWN else Decimal(total),
        code=None if code == UNKNOWN else int(code),
    )
    named: set[str] = set()
    for name, seconds in directories:
        seconds = gate_value(
            reasons,
            "Directory seconds",
            seconds,
            GATE_SECONDS,
            "the seconds of a directory are not a number",
        )
        listed.append(f"{name[:TEXT_CAP]} " + (seconds if seconds == UNKNOWN else seconds + " s"))
        if name[:TEXT_CAP] in named:
            reasons.append(
                (
                    "Gate runs: Directories",
                    f"a run in `{GATE_FILE}` lists a directory twice: only its first "
                    "time is counted in the medians",
                )
            )
            continue
        named.add(name[:TEXT_CAP])
        timed.directories.append(
            (name[:TEXT_CAP], None if seconds == UNKNOWN else Decimal(seconds))
        )
    cycle.gate_runs.append(
        [started, code, total, others, DIRECTORY_SEPARATOR.join(listed) or GATE_NONE]
    )
    cycle.gate_timed.append(timed)


def read_gate(cycle: Cycle, text: str | None, reason: str | None) -> None:
    """Read the runs of `gate_times.md` from its table. A table lacking one of its six
    columns, or lacking the table, is a missing field, and the runs are not read; a row of the wrong
    number of cells is a run of its own with unknown values; the runs and the directories beyond the
    limits are not read, and the reason is given."""
    if text is None:
        cycle.unknown.append(("Gate runs", reason))
        return
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    found = gate_header(cycle, lines, fenced)
    if found is None:
        return
    reasons: list[tuple[str, str]] = []
    for key, directories in gate_table_runs(lines, fenced, *found, reasons):
        add_gate_run(cycle, key, directories, reasons)
    cycle.unknown.extend(dict.fromkeys(reasons))
