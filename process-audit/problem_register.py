"""The register of problems, moved out of `audit_count.py`.

The register of problems the user keeps (`process-audit/problem_register.md` is its template) read
as untrusted input: the problem and the register it fills (`Problem`, `Register`), the checks of
the rows of its tables and of the tables of levels, and the reading of the file (`read_register`),
as `process-audit/audit_count.py` counts the problems against the cycles (WAY-330, WAY-344,
WAY-48). It is imported, never run, and runs nothing when imported. Standard library only.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from record_reading import MAX_BYTES, THE_WAY, AuditCountError, is_separator, table_cells
from stage_pricing import TEXT_CAP

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

display = remarks_check.display

COSTS_TITLE = "Costs of an occurrence"
# The five tables of the register, each under its heading, with the header row the template gives.
REGISTER_TABLES = (
    ("Classes", ["Class", "Meaning", "Added", "Withdrawn"]),
    ("Weights", ["Weight", "Meaning"]),
    (COSTS_TITLE, ["Cost of an occurrence", "Meaning"]),
    ("Issues", ["Issue", "What", "Fate", "Fix"]),
    (
        "Problems",
        [
            "Repository",
            "Record",
            "Stages",
            "What",
            "Class",
            "Weight",
            "Cost of an occurrence",
            "Issue",
        ],
    ),
)
# The scale of weight has these four levels and no other.
LEVELS = ["no problem", "Minor", "Important", "Critical"]
# The scale of the cost of an occurrence has these five levels, each dearer than the one before, and
# no other. It is a different thing from the cost of a cycle in money (WAY-337).
COST_LEVELS = ["nothing", "steps", "stage", "round", "human"]
FATES = ["open", "fixed", "dropped"]
FIXED = "fixed"
START = "start"
NONE = "none"
NAME_LENGTH = 80
# Lower-case letters and digits in words joined by single hyphens: each hyphen must stand between
# two runs of them, so the pattern takes one way through any text and cannot backtrack.
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
DATE_TEXT = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
FULL_HASH = re.compile(r"[0-9a-fA-F]{40}")
# A commit as the records write it, in lower-case hexadecimal characters only, so that no value
# given to git begins with `-`.
SHORT_HASH = re.compile(r"[0-9a-f]{7,40}")


@dataclass
class Problem:
    """A row of the table *Problems* that the checks accept."""

    number: int
    repository: str
    record: str
    cls: str
    weight: str
    cost: str
    issue: str


@dataclass
class Register:
    """What the register gives: its classes and issues in the order of their tables, the problems
    that pass the checks, and each refused row or table with its reason."""

    classes: list[str] = field(default_factory=list)
    issues: list[tuple[str, str, str]] = field(default_factory=list)
    problems: list[Problem] = field(default_factory=list)
    # The Repository, Record and Issue texts of each refused row of *Problems*, as the row gives them
    # (Issue empty where the row is too short to have one): a refused row still belongs to the cycle
    # and the issue it names, and the counts that include it say so.
    refused_problems: list[tuple[str, str, str]] = field(default_factory=list)
    refused: list[tuple[str, str, str, str]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    # The dates of *Added* and *Withdrawn* of the valid rows of *Classes*, sorted as text (they are
    # written YYYY-MM-DD); unknown where a row or the table does not read, so that a change of the
    # list cannot be ruled out.
    class_dates: list[str] = field(default_factory=list)
    class_dates_unknown: bool = False

    def refuse(self, value: str, why: str, repository: str = THE_WAY, record: str = "none") -> None:
        self.refused.append(tuple(text[:TEXT_CAP] for text in (repository, record, value, why)))


def valid_name(text: str) -> bool:
    return len(text) <= NAME_LENGTH and NAME.fullmatch(text) is not None


def valid_date(text: str) -> bool:
    if DATE_TEXT.fullmatch(text) is None:
        return False
    try:
        date.fromisoformat(text)
    except ValueError:
        return False
    return True


def check_class(cells: list[str]) -> tuple[str, str | None]:
    name = cells[0]
    if not valid_name(name) or name == NONE:
        return name, "the class name is not lower-case letters, digits and hyphens, or it is `none`"
    if cells[2] != START and not valid_date(cells[2]):
        return name, "the column Added is neither `start` nor a date written YYYY-MM-DD"
    if cells[3] != NONE and not valid_date(cells[3]):
        return name, "the column Withdrawn is neither `none` nor a date written YYYY-MM-DD"
    return name, None


def check_weight(cells: list[str]) -> tuple[str, str | None]:
    if cells[0] not in LEVELS:
        return cells[0], "the weight is not one of the four levels"
    return cells[0], None


def check_cost_level(cells: list[str]) -> tuple[str, str | None]:
    if cells[0] not in COST_LEVELS:
        return cells[0], "the cost of an occurrence is not one of the five levels"
    return cells[0], None


def check_issue(cells: list[str]) -> tuple[str, str | None]:
    name, fate, fix = cells[0], cells[2], cells[3]
    if not valid_name(name) or name == NONE:
        return name, "the issue name is not lower-case letters, digits and hyphens, or it is `none`"
    if fate not in FATES:
        return name, "the fate is not `open`, `fixed` or `dropped`"
    if fate == FIXED and FULL_HASH.fullmatch(fix) is None:
        return name, "the Fix of a fixed issue is no commit of 40 hexadecimal characters"
    if fate != FIXED and fix != NONE:
        return name, "the Fix of an issue that is not fixed must read `none`"
    return name, None


def named_rows(
    register: Register, title: str, rows: list[list[str]], width: int, check
) -> list[tuple[str, int, list[str]]]:
    """The rows of one table that pass `check`, as (name, row number, cells) in table order. A row
    of the wrong width or refused by `check` is refused with its reason; a name written in two
    rows refuses both of them."""
    kept = []
    for number, cells in enumerate(rows, 1):
        value = f"row {number} of `{title}`"
        if len(cells) != width:
            register.refuse(value, f"the row has {len(cells)} cells, not {width}")
            continue
        name, why = check(cells)
        if why:
            register.refuse(value, why)
            continue
        kept.append((name, number, cells))
    count = Counter(name for name, _, _ in kept)
    valid = []
    for name, number, cells in kept:
        if count[name] > 1:
            register.refuse(f"row {number} of `{title}`", "the name is written in two rows")
        else:
            valid.append((name, number, cells))
    return valid


def level_faults(rows: list[list[str]], levels: list[str]) -> str | None:
    """What a table of levels lacks, in words the `Error:` line can name: each level that none of
    its rows of the right width names, and each written in two rows; None where each is named
    once. A row of the wrong width is refused on its own and counts for no level."""
    width = 2
    names = [cells[0] for cells in rows if len(cells) == width]
    missing = [level for level in levels if level not in names]
    doubled = [level for level in levels if names.count(level) > 1]
    parts = []
    if missing:
        parts.append("lacks " + ", ".join(f"`{level}`" for level in missing))
    if doubled:
        parts.append("writes " + ", ".join(f"`{level}`" for level in doubled) + " in two rows")
    return " and ".join(parts) or None


def check_levels(
    register: Register, title: str, rows: list[list[str]], levels: list[str], check
) -> None:
    """Refuse the rows of a table of levels that `check` refuses, and where the table does not name
    each of its levels once, add an `Error:` of the register that names the level it lacks or
    writes twice (WAY-344). The result is still written: what depends on the table is unknown."""
    named_rows(register, title, rows, 2, check)
    fault = level_faults(rows, levels)
    if fault is not None:
        why = f"the table `{title}` must name each level once: it {fault}"
        register.errors.append(why)
        register.refuse(f"table `{title}`", why)


def register_table(
    lines: list[str], fenced: list[bool], title: str, columns: list[str], missing: list[str]
) -> tuple[list[list[str]] | None, str | None]:
    """The rows of the table under the heading `## <title>`, or None with the reason. The table
    starts at the first line that begins with `|` before the next heading, and its header row must
    be `columns`; its rows run on until a line that does not begin with `|`. A heading, a table or
    a column the register lacks is a field missing (WAY-344): it is added to `missing`, in words
    that name it, as well as returned as the reason."""
    headings = [
        index
        for index, (line, inside) in enumerate(zip(lines, fenced))
        if not inside and line.strip() == f"## {title}"
    ]
    if len(headings) != 1:
        if not headings:
            missing.append(f"the heading `## {title}`")
        return None, (
            f"the register holds the heading `## {title}` "
            + ("more than once" if headings else "not at all")
        )
    start = None
    for index in range(headings[0] + 1, len(lines)):
        if fenced[index]:
            continue
        if lines[index].startswith("## "):
            break
        if lines[index].startswith("|"):
            start = index
            break
    if start is None:
        missing.append(f"the table under the heading `## {title}`")
        return None, f"the table `{title}` is missing"
    found = table_cells(lines[start])
    if found != columns:
        # A column absent from the header row, or standing under another name, is a field missing;
        # the columns all there in another order, or with another beside them, are not.
        absent = [name for name in columns if name not in found]
        missing.extend(f"the column `{name}` of the table `{title}`" for name in absent)
        return None, f"the table `{title}` does not have the header row the template gives"
    separator = start + 1
    if (
        separator >= len(lines)
        or not lines[separator].startswith("|")
        or not is_separator(table_cells(lines[separator]))
    ):
        return None, f"the table `{title}` lacks its separator row"
    rows = []
    for index in range(separator + 1, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            break
        rows.append(table_cells(lines[index]))
    return rows, None


def read_register(path: Path) -> Register:
    """The register of problems at `path`, read as untrusted input. A file larger than the cap, or
    not UTF-8, stops the run with nothing written. A table or a row that does not read is refused
    with its reason, and what depends on it is unknown; a missing table is also an error of the
    register."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read(MAX_BYTES + 1)
    except OSError as error:
        raise AuditCountError(
            f"cannot read the register of problems: {display(error.strerror or error)}"
        ) from None
    if len(raw) > MAX_BYTES:
        raise AuditCountError(f"the register of problems is larger than {MAX_BYTES} bytes")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError("the register of problems is not UTF-8") from None
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    register = Register()
    tables: dict[str, list[list[str]] | None] = {}
    missing: list[str] = []
    for title, columns in REGISTER_TABLES:
        rows, why = register_table(lines, fenced, title, columns, missing)
        if why:
            register.errors.append(why)
            register.refuse(f"table `{title}`", why)
        tables[title] = rows
    if missing:
        # The register is a file a human or a tool writes, and a field the count looks for data by
        # that it cannot find ends the run; the absence is never read as no rows (WAY-344).
        raise AuditCountError("the register of problems lacks " + ", ".join(missing))
    if tables["Classes"] is None:
        register.class_dates_unknown = True
    else:
        register.classes = [
            name
            for name, _, _ in named_rows(register, "Classes", tables["Classes"], 4, check_class)
        ]
        for cells in tables["Classes"]:
            if len(cells) != 4 or check_class(cells)[1] is not None:
                register.class_dates_unknown = True
                continue
            register.class_dates += [text for text in (cells[2], cells[3]) if valid_date(text)]
        register.class_dates.sort()
    if tables["Weights"] is not None:
        check_levels(register, "Weights", tables["Weights"], LEVELS, check_weight)
    if tables[COSTS_TITLE] is not None:
        check_levels(register, COSTS_TITLE, tables[COSTS_TITLE], COST_LEVELS, check_cost_level)
    if tables["Issues"] is not None:
        register.issues = [
            (name, cells[2], cells[3].lower())
            for name, _, cells in named_rows(register, "Issues", tables["Issues"], 4, check_issue)
        ]
    if tables["Problems"] is not None:
        class_names = set(register.classes)
        issue_names = {name for name, _, _ in register.issues}
        for number, cells in enumerate(tables["Problems"], 1):
            value = f"row {number} of `Problems`"
            if len(cells) != 8:
                register.refuse(
                    value,
                    f"the row has {len(cells)} cells, not 8",
                    cells[0] if cells else "",
                    cells[1] if len(cells) > 1 else "",
                )
                register.refused_problems.append(
                    (cells[0] if cells else "", cells[1] if len(cells) > 1 else "", "")
                )
                continue
            repository, record, _, _, cls, weight, cost, issue = cells
            why = None
            if not repository:
                why = "the row names no repository"
            elif FULL_HASH.fullmatch(record) is None:
                why = "the Record is no commit of 40 hexadecimal characters"
            elif cls not in class_names:
                why = "the class is not in the list of classes"
            elif weight not in LEVELS:
                why = "the weight is not one of the four levels"
            elif cost not in COST_LEVELS:
                why = "the cost of an occurrence is not one of the five levels"
            elif issue != NONE and issue not in issue_names:
                why = "the issue is in no valid row of Issues"
            if why:
                register.refuse(value, why, repository, record)
                register.refused_problems.append((repository, record, issue))
                continue
            register.problems.append(
                Problem(number, repository, record.lower(), cls, weight, cost, issue)
            )
    return register
