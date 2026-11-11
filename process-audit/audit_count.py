"""The counting command of the audit of the process: the cycles whose records the user's
repositories hold in their history, and for each the version of the-way it ran on, its number of
process remarks and its times (WAY-329, WAY-331, WAY-337, WAY-340).

Usage:

    python -B process-audit/audit_count.py [--locations FILE] [--repository KEY ...]

In a product, the path starts with `.the-way/`. The command asks nothing and reads nothing from
stdin, and git runs with its terminal prompt off, so that a system scheduler can start it with no
human present and stdin closed or empty.

The places it needs are entries of the user's locations file (WAY-320), read as
`project-level/backlog_place.md` reads an entry; FILE defaults to `~/.the-way/locations.json`:

- under the key `the-way`, the entry `problem_register`, the file of the register of problems
  (`process-audit/problem_register.md` is its template), and the entry `audit_results`, the
  directory where the result is written;
- under the key of each repository whose cycles it reads — the name of a product, as the
  register's *Repository* column gives it — the entry `repository`, the path of that product's
  checkout. Each `--repository KEY` names a repository to read; without one, it reads every key
  that holds an entry `repository`. The-way's own checkout is the entry `repository` under
  `the-way`, and where that entry is missing, the checkout this script lies in.

A path is absolute or starts with `~`. Where the file, a key, an entry or the path an entry holds
is missing, or an entry is not a path, the command writes nothing and names it in an `Error:` line
on stderr, so that the skill of the audit asks the human; it never asks itself.

The price list is the file `price_list.md` beside this script (`--prices FILE` names another, as the
tests do). It holds the line `- List date: <YYYY-MM-DD>`, the date its prices were read, and a table
per provider whose header has the columns *Model id in stages.md*, *Input*, *Cached input* and
*Output*, per million tokens; a price cell `—` is a model with no price (WAY-336, WAY-338).

A cycle is found where a commit adds the copy of its record, `docs/task-cycles/<folder>/cycle.md`
(`task-cycle/record_template.md`), in the history of every branch and remote branch, merges
followed into each of their parents. A cycle committed more than once, after a correction, counts
once: it is named by its repository and the first commit that adds a copy in its folder, the later
ones noted, and its values are read from the last copy, the most complete. For each cycle:

- *Process pin*: the version of the-way the cycle ran on — the commit the record's header line
  `Process pin` names (in earlier records `Process pin and ...`), or the commit it moved to where
  the line says the pin moved; for a cycle of the-way's own history, whose line names no commit,
  the commit of its line `Target branch and base`;
- *Remarks*: the number of entries under the record's item `Process remarks on the-way`, `0`
  where the item reads `none`;
- the agents' working time without waiting for tools, and the time they waited for tools, from the
  lines of the copy's `stages.md` that `task-cycle/cycle_stages.py` writes, as h:mm:ss;
- the cost at constant prices: each row of the section *Stages: start, waiting for tools and
  tokens by model* of the copy's `stages.md` is priced at the list's prices, its input less its
  cached input at the *Input* price, its cached input at the *Cached input* price and its output at
  the *Output* price. Cache writes are inside *Input* (`task-cycle/cycle_stages.py` folds them in),
  so they are priced as input: an approximation. A model the list gives no price for, a row that
  does not read, a subagent stage with no token usage (the model `—`), a section where no stage has
  any, or a `stages.md` without that section (an earlier form) gives the cost `unknown`, never
  zero; a stretch of the orchestrator with no token usage, time it worked with no response of a
  model, costs nothing;
- *Fix rounds*: the number of findings files the record's item `Review rounds` names, `0` where it
  reads `none`. A fix round is the fix of a review's findings and the review of that fix; the
  orchestrator gives both the findings file, by its path in `reports/`, and the item names each
  round by that path: one entry for each round under the item, opening with the word `findings`
  and the path between backticks (`task-cycle/record_template.md`);
- the share of the cost spent in fix rounds (WAY-336): the cost of the subagent turns whose cell
  *Files named* in that section of `stages.md` names a findings file of a round the record names,
  each turn counted once, over the cycle's cost. It is `0.0%` only where the item reads `none` and
  no subagent turn was given a findings file, told by the word `findings` in its name as the check
  of process remarks tells one (WAY-294). It is `unknown`, with the reason, where the item is
  missing, doubled or names a round otherwise than by its findings file, where `stages.md` has no
  column *Files named* (an earlier form), where a cell of it is not a list of files of `reports/`,
  where a findings file the record names is named by fewer than two subagent turns, the fix and
  the review of that fix, or where a turn was given a findings file the record does not name: a
  wrong figure is worse than `unknown`. The cost is still given.

A value a record or a `stages.md` does not give — an earlier form, a missing, doubled or malformed
line, a file that is no regular file, too large or not UTF-8 — is `unknown`, never zero, and the
result says why. The records, the `stages.md` files and the locations file are untrusted input:
their text reaches the result only as a commit, a number or a time it was read as, and a folder or
a key on one line with each control character and each bar written as `\\x..`, so that no cell of
a table holds a bar; no path written in them is followed, and nothing of them is run. A commit
dated outside the years the platform reads gives *Committed* `unknown`. Git runs only to read:
`rev-parse`, `log`, `diff-tree`, `ls-tree` and `cat-file`.

The result is Markdown in UTF-8 with LF line ends, the same bytes for the same input, written to
`count-<YYYY-MM-DD>.md`, the date of the run, and `count-latest.md` in the directory of
`audit_results`, never inside a repository it reads: a section *Repositories*, a table of each
repository read and its cycles; a section *Cycles*, a table of one row per cycle; and a section
*Unknown values*, a table of each value given as `unknown` and why. A section *Cost*, a table of
one row per cycle with its price list's date (the series the cost belongs to), its cost in USD, its
number of fix rounds and the share of the cost in them. On stdout it names the two files and the
counts.

Exit code: 0 with the result written; 1 with the result written but a repository that could not be
read, named in the result and in an `Error:` line on stderr; 2 with `Error: <message>` on stderr and
nothing written, when an argument is wrong, the locations file, the price list or an entry it needs
is missing or wrong, the result directory lies inside a repository to read, or the result cannot be
written.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

display = remarks_check.display

DEFAULT_LOCATIONS = "~/.the-way/locations.json"
THE_WAY = "the-way"
REGISTER_ENTRY = "problem_register"
RESULTS_ENTRY = "audit_results"
REPOSITORY_ENTRY = "repository"
# The checkout of the-way this script lies in, used where `the-way` has no entry `repository`.
OWN_CHECKOUT = Path(__file__).resolve().parent.parent
# The price list of this part, read as a file of the-way (`--prices` names another one).
PRICES = Path(__file__).resolve().parent / "price_list.md"

RECORDS = "docs/task-cycles/"
RECORD_PATHSPEC = ":(glob)docs/task-cycles/*/cycle.md"
LATEST = "count-latest.md"
UNKNOWN = "unknown"
# A copy's file larger than this is not read: no record or `stages.md` comes near it.
MAX_BYTES = 4 * 1024 * 1024
GIT_TIMEOUT = 120

# A commit as a record writes it: 7 to 40 hexadecimal characters, a digit among them, so that an
# English word written in the letters a-f is not taken for one, standing apart from other letters
# and digits.
COMMIT = r"(?<![0-9A-Za-z])(?=[0-9a-fA-F]*[0-9])[0-9a-fA-F]{7,40}(?![0-9A-Za-z])"
COMMIT_IN_TEXT = re.compile(COMMIT)
MOVED_PIN = re.compile(r"moved to `?(" + COMMIT + r")`?", re.I)
REMARKS_OPENER = re.compile(r"(?P<indent>[ \t]*)[-*+][ \t]+Process remarks on the-way(?![\w-])"
                            r"[ \t]*:?[ \t]*(?P<rest>.*)")
DURATION = re.compile(r"(\d{1,7}):([0-5]\d):([0-5]\d)")
WORKING_LINE = "- Working time without waiting for tools:"
WAITING_LINE = "- Waiting for tools:"
STAGES_HEADING = "## Stages: start, waiting for tools and tokens by model"
STAGE_COLUMNS = ["#", "Stage", "Start", "Waiting for tools", "Model", "Input", "Cached input",
                 "Output"]
FILES_COLUMN = "Files named"
NO_MODEL = "—"
ORCHESTRATOR = "orchestrator"
# A file of the cycle's `reports/` as `task-cycle/cycle_stages.py` writes it and as the record's
# item `Review rounds` names a findings file: a name that starts with a letter, a digit or `_`,
# holds letters, digits, `_`, `-` and `.`, ends in `.md` and is at most 120 characters long. The
# repetition is bounded and nothing follows it but the end, so no text makes it try again.
REPORT_FILE = re.compile(r"reports/[A-Za-z0-9_][A-Za-z0-9_.-]{0,116}\.md")
ROUNDS_LABEL = "Review rounds"
ROUND_ENTRY = re.compile(r"findings `([^`\n]{1,200})`")
# A findings file is told by the word in its name, as the check of process remarks tells it
# (WAY-294); used only to find a turn given a findings file the record does not name.
FINDINGS_WORD = "findings"
PRICE_HEADING = "List date"
PRICE_MODEL = "Model id in stages.md"
PRICE_COLUMNS = ("Input", "Cached input", "Output")
# A token count longer than this is not a count of tokens: no model's input comes near it.
TOKEN_DIGITS = 15
PRICE = re.compile(r"[0-9]{1,6}(?:\.[0-9]{1,6})?")
TURN_SUFFIX = re.compile(r" — turn [0-9]{1,6}$")
MILLION = Decimal(1_000_000)
MONEY = Decimal("0.000001")
SHARE = Decimal("0.1")
# A cost at or above this many dollars is not given: a crafted count would otherwise overrun the
# precision the cost is written with.
COST_CEILING = Decimal(10) ** 18


class AuditCountError(Exception):
    """A wrong argument, a missing or wrong entry of the locations file, or a result that cannot
    be written: nothing is written."""


class GitError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise AuditCountError(message)


# The locations file


def read_locations(name: str) -> dict:
    """The locations file as a JSON object; a key or an entry written twice is an error, since
    JSON readers disagree on which of the two counts."""
    path = Path(name).expanduser()
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        raise AuditCountError(f"the locations file {display(name)} does not exist") from None
    except OSError as error:
        raise AuditCountError(f"cannot read the locations file {display(name)}: "
                              f"{display(error.strerror or error)}") from None
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError(f"the locations file {display(name)} is not UTF-8") from None

    def unique(pairs: list[tuple[str, object]]) -> dict:
        seen: dict[str, object] = {}
        for key, value in pairs:
            if key in seen:
                raise AuditCountError(f"the locations file {display(name)} holds the key or entry "
                                      f"`{display(key)}` twice in one object")
            seen[key] = value
        return seen

    try:
        data = json.loads(text, object_pairs_hook=unique)
    except json.JSONDecodeError as error:
        raise AuditCountError(f"the locations file {display(name)} is not JSON: line "
                              f"{error.lineno}, column {error.colno}") from None
    except RecursionError:
        raise AuditCountError(f"the locations file {display(name)} is nested too deeply") from None
    if not isinstance(data, dict):
        raise AuditCountError(f"the locations file {display(name)} is not a JSON object")
    return data


def key_object(locations: dict, key: str) -> dict:
    if key not in locations:
        raise AuditCountError(f"the locations file holds no key `{display(key)}`")
    value = locations[key]
    if not isinstance(value, dict):
        raise AuditCountError(f"the key `{display(key)}` of the locations file is not a JSON "
                              f"object")
    return value


def entry_path(locations: dict, key: str, entry: str, kind: str) -> Path:
    """The path the entry `entry` under `key` holds, which must exist as a `kind`: "file" or
    "directory". The path itself is never printed: an error names the entry (WAY-320)."""
    where = f"the entry `{display(entry)}` under `{display(key)}`"
    entries = key_object(locations, key)
    if entry not in entries:
        raise AuditCountError(f"the locations file holds no entry `{display(entry)}` under "
                              f"`{display(key)}`")
    value = entries[entry]
    if not isinstance(value, str) or not value.strip():
        raise AuditCountError(f"{where} of the locations file is not a path written as a string")
    try:
        path = Path(value).expanduser()
        if not path.is_absolute():
            raise AuditCountError(f"{where} of the locations file is not an absolute path or a "
                                  f"path from `~`")
        exists = path.is_dir() if kind == "directory" else path.is_file()
    except (OSError, ValueError, RuntimeError):
        exists = False
    if not exists:
        raise AuditCountError(f"the path of {where} of the locations file is no existing {kind}")
    return path


def the_way_checkout(locations: dict) -> Path:
    """The checkout of the-way: the entry `repository` under `the-way`, or this script's own."""
    if REPOSITORY_ENTRY in key_object(locations, THE_WAY):
        return entry_path(locations, THE_WAY, REPOSITORY_ENTRY, "directory")
    return OWN_CHECKOUT


def repositories(locations: dict, named: list[str]) -> dict[str, Path]:
    """The repositories to read, by key, in the order of their keys."""
    found: dict[str, Path] = {}
    if named:
        for key in dict.fromkeys(named):
            if key == THE_WAY:
                found[key] = the_way_checkout(locations)
            else:
                found[key] = entry_path(locations, key, REPOSITORY_ENTRY, "directory")
    else:
        for key in locations:
            if REPOSITORY_ENTRY in key_object(locations, key):
                found[key] = entry_path(locations, key, REPOSITORY_ENTRY, "directory")
    if not found:
        raise AuditCountError("no key of the locations file holds an entry `repository`; add one "
                              "or name a repository with --repository")
    return dict(sorted(found.items()))


def inside(path: Path, folder: Path) -> bool:
    child = os.path.normcase(os.path.abspath(os.path.realpath(path)))
    parent = os.path.normcase(os.path.abspath(os.path.realpath(folder)))
    return child == parent or child.startswith(parent.rstrip(os.sep) + os.sep)


# Git


class Git:
    """Git run to read only, with no prompt, no pager and nothing on stdin."""

    def __init__(self, repository: Path):
        self.repository = repository

    def run(self, *arguments: str) -> bytes:
        environment = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never",
                           GIT_OPTIONAL_LOCKS="0")
        try:
            result = subprocess.run(
                ["git", "--no-pager", "-c", "core.fsmonitor=false", "-C", str(self.repository),
                 *arguments], stdin=subprocess.DEVNULL, capture_output=True,
                timeout=GIT_TIMEOUT, env=environment)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitError(f"git {arguments[0]}: {display(error)}") from None
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise GitError(f"git {arguments[0]} failed ({result.returncode}): "
                           f"{display(detail)}")
        return result.stdout


# Reading a cycle


@dataclass
class Cycle:
    repository: str
    folder: str
    record: str
    committed: str
    later: list[str] = field(default_factory=list)
    pin: str | None = None
    remarks: int | None = None
    working: int | None = None
    waiting: int | None = None
    cost: Decimal | None = None
    rounds: int | None = None
    share: Decimal | None = None
    unknown: list[tuple[str, str]] = field(default_factory=list)


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


def header_field(line: str) -> tuple[str, str] | None:
    """The label and the value of a header line `- <label>: <value>`, or None. It is cut at the
    first colon in one pass, never by a pattern that could try every way of splitting a run of
    blanks, so that no crafted line costs more than its length."""
    if line[:1] != "-" or line[1:2] not in (" ", "\t"):
        return None
    label, colon, value = line[1:].partition(":")
    label = label.strip(" \t")
    if not colon or not label:
        return None
    return label, value.strip(" \t")


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
        return None, ("the line `Process pin` names no commit, and the line "
                      "`Target branch and base` is " + ("doubled" if bases else "missing"))
    found = COMMIT_IN_TEXT.search(bases[0])
    if not found:
        return None, "neither the line `Process pin` nor `Target branch and base` names a commit"
    return found.group(0).lower(), None


def remarks_count(lines: list[str], fenced: list[bool]) -> tuple[int | None, str | None]:
    """The number of entries under the item `Process remarks on the-way`, or None with the
    reason."""
    openers = [index for index, line in enumerate(lines)
               if not fenced[index] and REMARKS_OPENER.fullmatch(line)]
    if not openers:
        return None, "the record holds no item `Process remarks on the-way`: an earlier form"
    if len(openers) > 1:
        return None, "the record holds the item `Process remarks on the-way` more than once"
    start = openers[0]
    opener = REMARKS_OPENER.fullmatch(lines[start])
    base = remarks_check.indent_of(lines[start])
    markers: list[int] = []
    for line, inside_fence in zip(lines[start + 1:], fenced[start + 1:]):
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
    return None, ("the item `Process remarks on the-way` holds no entries under it and does not "
                  "read `none`: an earlier form")


def stages_time(lines: list[str], fenced: list[bool], prefix: str,
                what: str) -> tuple[int | None, str | None]:
    """The seconds a line of `stages.md` gives, or None with the reason."""
    values = [line[len(prefix):].strip() for line, inside_fence in zip(lines, fenced)
              if not inside_fence and line.startswith(prefix)]
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


# Tables and the price list


def table_cells(line: str) -> list[str]:
    """The cells of a table row; a backslash escapes the character after it, so that an escaped
    bar stays inside its cell. Linear in the length of the line."""
    text = line.strip()
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in text:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip())
    if text.startswith("|") and cells[0] == "":
        cells.pop(0)
    if text.endswith("|") and cells and cells[-1] == "":
        cells.pop()
    return cells


def is_separator(cells: list[str]) -> bool:
    return all(cell and set(cell) <= set("-:") for cell in cells)


@dataclass
class Prices:
    """The price list: its date, and per model its prices per million tokens as (input, cached
    input, output), or None where no page gives a price."""
    date: str
    table: dict[str, tuple[Decimal, Decimal, Decimal] | None]


@dataclass
class StageTokens:
    """One row of the section of `stages.md` that gives each stage's tokens by model. `files` is
    what its cell *Files named* gives: the files of `reports/` the turn was given, None where the
    cell reads `unknown` or the form has no such column; `files_read` is False where the cell is
    not a list of such files."""
    number: str
    name: str
    model: str
    input: int
    cached: int
    output: int
    files: frozenset[str] | None = None
    files_read: bool = True


def read_prices(name: str) -> Prices:
    """The price list, read as a file of the-way: a missing or wrong list stops the run with
    nothing written, as a wrong entry of the locations file does."""
    path = Path(name).expanduser()
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        raise AuditCountError(f"the price list {display(name)} does not exist") from None
    except OSError as error:
        raise AuditCountError(f"cannot read the price list {display(name)}: "
                              f"{display(error.strerror or error)}") from None
    if len(raw) > MAX_BYTES:
        raise AuditCountError(f"the price list {display(name)} is larger than {MAX_BYTES} bytes")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError(f"the price list {display(name)} is not UTF-8") from None
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    dates = header_fields(lines, fenced, PRICE_HEADING)
    if len(dates) != 1:
        raise AuditCountError(f"the price list {display(name)} "
                              + ("holds the line `List date` more than once" if dates
                                 else "holds no line `List date`"))
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", dates[0]):
        raise AuditCountError(f"the line `List date` of the price list {display(name)} is no date "
                              "written YYYY-MM-DD")
    try:
        date.fromisoformat(dates[0])
    except ValueError:
        raise AuditCountError(f"the line `List date` of the price list {display(name)} is no "
                              "date") from None
    table: dict[str, tuple[Decimal, Decimal, Decimal] | None] = {}
    columns: list[int] | None = None
    for line, inside in zip(lines, fenced):
        if inside or not line.startswith("|"):
            columns = None
            continue
        cells = table_cells(line)
        if columns is None:
            if cells[:1] == [PRICE_MODEL]:
                if not all(name_of in cells for name_of in PRICE_COLUMNS):
                    raise AuditCountError(f"a table of the price list {display(name)} lacks one "
                                          f"of the columns {', '.join(PRICE_COLUMNS)}")
                columns = [cells.index(name_of) for name_of in PRICE_COLUMNS]
            continue
        if is_separator(cells):
            continue
        if not cells or max(columns) >= len(cells) or not cells[0]:
            raise AuditCountError(f"a row of a table of the price list {display(name)} has fewer "
                                  "cells than its header")
        model = cells[0]
        if model in table:
            raise AuditCountError(f"the price list {display(name)} names model `{display(model)}` "
                                  "twice")
        numbers = [Decimal(cells[index]) if PRICE.fullmatch(cells[index]) else None
                   for index in columns]
        table[model] = None if any(number is None for number in numbers) else (
            numbers[0], numbers[1], numbers[2])
    if not table:
        raise AuditCountError(f"the price list {display(name)} names no model")
    return Prices(dates[0], table)


def token_count(text: str) -> int | None:
    digits = text.replace(",", "")
    if digits.isascii() and digits.isdigit() and len(digits) <= TOKEN_DIGITS:
        return int(digits)
    return None


def is_report_file(path: str) -> bool:
    """A file of `reports/` written as `reports/<name>` in the form REPORT_FILE gives, with no
    `..` in it."""
    return REPORT_FILE.fullmatch(path) is not None and ".." not in path


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


def stage_tokens(lines: list[str], fenced: list[bool]) -> tuple[list[StageTokens] | None, bool,
                                                                 str | None]:
    """The rows of the section of `stages.md` that gives each stage's tokens by model, whether its
    table has the column *Files named*, or None with the reason: an earlier form has no such
    section (WAY-336)."""
    headings = [index for index, (line, inside) in enumerate(zip(lines, fenced))
                if not inside and line.strip() == STAGES_HEADING]
    if not headings:
        return None, False, ("`stages.md` holds no section `Stages: start, waiting for tools and "
                             "tokens by model`: an earlier form")
    if len(headings) > 1:
        return None, False, "`stages.md` holds that section more than once"
    table: list[list[str]] = []
    for line, inside in zip(lines[headings[0] + 1:], fenced[headings[0] + 1:]):
        if inside:
            continue
        if line.startswith("#"):
            break
        if line.startswith("|"):
            table.append(table_cells(line))
    named = bool(table) and table[0] == STAGE_COLUMNS + [FILES_COLUMN]
    if not table or (table[0] != STAGE_COLUMNS and not named):
        return None, False, ("the table of the section in `stages.md` is not of the form the stage "
                             "report gives")
    columns = len(table[0])
    body = [cells for cells in table[1:] if not is_separator(cells)]
    if not body:
        return None, False, "the section in `stages.md` holds no stage row"
    rows: list[StageTokens] = []
    for cells in body:
        if len(cells) != columns:
            return None, False, (f"a row of the section in `stages.md` has {len(cells)} cells, not "
                                 f"{columns}")
        counts = [token_count(cells[index]) for index in (5, 6, 7)]
        if any(count is None for count in counts):
            return None, False, ("a token count in the section of `stages.md` is not a number of at "
                                 f"most {TOKEN_DIGITS} digits")
        row = StageTokens(cells[0], cells[1], cells[4], counts[0], counts[1], counts[2])
        if named:
            row.files, row.files_read = files_cell(cells[8])
        rows.append(row)
    return rows, named, None


def review_rounds(lines: list[str], fenced: list[bool]) -> tuple[list[str] | None, str | None]:
    """The findings files of the fix rounds that the record's item `Review rounds` names, in its
    form: the item reading `none`, or nothing after its colon and one entry indented under it for
    each round, opening with the word `findings` and `reports/<file>.md` between backticks. None
    with the reason where the item is missing, doubled, or not in that form. Outside code fences
    only; one pass over the lines."""
    openers = [index for index, line in enumerate(lines)
               if not fenced[index] and line.startswith("- ")
               and (header_field(line) or ("", ""))[0] == ROUNDS_LABEL]
    if not openers:
        return None, "the record holds no item `Review rounds`: an earlier form"
    if len(openers) > 1:
        return None, "the record holds the item `Review rounds` more than once"
    start = openers[0]
    rest = header_field(lines[start])[1]
    markers: list[tuple[int, str]] = []
    for line, inside in zip(lines[start + 1:], fenced[start + 1:]):
        if not line.strip():
            continue
        indent = remarks_check.indent_of(line)
        if indent == 0:
            break
        marker = None if inside else remarks_check.MARKER.fullmatch(line)
        if marker:
            markers.append((indent, marker.group("text")))
    if not markers:
        if remarks_check.reads_none(rest):
            return [], None
        return None, ("the item `Review rounds` names no findings file: it reads neither `none` nor "
                      "an entry for each round")
    if rest:
        return None, "the item `Review rounds` holds text beside its entries"
    base = min(indent for indent, _ in markers)
    found: list[str] = []
    for _, text in (marker for marker in markers if marker[0] == base):
        entry = ROUND_ENTRY.match(text)
        if not entry or not is_report_file(entry.group(1)):
            return None, ("an entry of the item `Review rounds` names no findings file: it does not "
                          "open with the word findings and reports/<file>.md between backticks")
        if entry.group(1) in found:
            return None, "the item `Review rounds` names a findings file twice"
        found.append(entry.group(1))
    return found, None


def is_orchestrator_row(name: str) -> bool:
    """The orchestrator's own rows, as `cycle_stages.py` names them: its stretches and the rows of
    its work while subagents run in parallel. Their work is the orchestrator's, so they serve no
    fix round by the files they name; the orchestrator's tokens while a fix runs stand in the
    fix's own row."""
    return name == ORCHESTRATOR or name.startswith("orchestrator while in parallel: ")


def priced(rows: list[StageTokens], prices: Prices) -> tuple[list[Decimal] | None, str | None]:
    """The cost in dollars of each row at the list's prices, or None with the reason: a model with
    no price, a cached input above its input, a subagent stage with no token usage, or a section
    with no stage that has any, make the cost unknown. An orchestrator stretch with no token usage
    costs nothing."""
    costs: list[Decimal] = []
    if all(row.model == NO_MODEL for row in rows):
        return None, "every stage of `stages.md` has no token usage, so the cost is not known"
    for row in rows:
        if row.model == NO_MODEL:
            if row.name == ORCHESTRATOR:
                # A stretch of the orchestrator's own work with time and no response of a model:
                # `cycle_stages.py` reads every response of the orchestrator's transcript.
                costs.append(Decimal(0))
                continue
            # `cycle_stages.py` writes this mark for a stage it found no token usage for: its
            # tokens are not known, so its cost is not zero.
            return None, (f"stage `{row.name}` has no token usage in its transcript, so its cost "
                          "is not known")
        if row.cached > row.input:
            return None, f"the cached input of stage `{row.name}` is above its input"
        price = prices.table.get(row.model)
        if price is None:
            return None, f"the price list gives no price for model `{row.model}`"
        input_price, cached_price, output_price = price
        costs.append((Decimal(row.input - row.cached) * input_price
                      + Decimal(row.cached) * cached_price
                      + Decimal(row.output) * output_price) / MILLION)
    return costs, None


def add_cost(cycle: Cycle, record_lines: list[str] | None, record_fenced: list[bool] | None,
             record_reason: str | None, stages_lines: list[str], stages_fenced: list[bool],
             prices: Prices) -> None:
    """The cycle's cost at the list's prices and the share of its fix rounds in it; a value that
    cannot be given is `unknown` with its reason, never zero."""
    rows, named, reason = stage_tokens(stages_lines, stages_fenced)
    if rows is None:
        cycle.unknown += [("Cost", reason), ("Fix rounds share", reason)]
        return
    costs, reason = priced(rows, prices)
    if costs is None:
        cycle.unknown += [("Cost", reason), ("Fix rounds share", reason)]
        return
    total = sum(costs, Decimal(0))
    if total >= COST_CEILING:
        cycle.unknown += [("Cost", "the cost is at or above the command's limit of 10^18 USD"),
                          ("Fix rounds share", "the cost is at or above the command's limit")]
        return
    cycle.cost = total
    if record_lines is None:
        cycle.unknown.append(("Fix rounds share", record_reason))
        return
    findings, reason = review_rounds(record_lines, record_fenced)
    if findings is None:
        cycle.unknown.append(("Fix rounds share", reason))
        return
    cycle.rounds = len(findings)
    reason = fix_rounds_share(rows, costs, total, named, findings, cycle)
    if reason:
        cycle.unknown.append(("Fix rounds share", reason))


def fix_rounds_share(rows: list[StageTokens], costs: list[Decimal], total: Decimal, named: bool,
                     findings: list[str], cycle: Cycle) -> str | None:
    """Set the share of the cost spent in the fix rounds whose findings files the record names:
    the cost of the subagent turns given one of those files, each turn once, over the cycle's
    cost (WAY-336). Returns the reason where it cannot be given."""
    if not named:
        return f"`stages.md` has no column `{FILES_COLUMN}`: an earlier form"
    if total == 0:
        return "the stages hold no tokens"
    turns: dict[str, tuple[frozenset[str] | None, Decimal]] = {}
    for row, cost in zip(rows, costs):
        if is_orchestrator_row(row.name):
            continue
        if not row.files_read:
            return (f"the cell `{FILES_COLUMN}` of stage `{row.name}` is not a list of files of "
                    "`reports/`")
        files, spent = turns.get(row.number, (row.files, Decimal(0)))
        turns[row.number] = (files, spent + cost)
    given = [files for files, _ in turns.values() if files is not None]
    unread = len(turns) - len(given)
    extra = sorted({path for files in given for path in files
                    if FINDINGS_WORD in path.rsplit("/", 1)[-1]} - set(findings))
    if extra:
        return (f"{len(extra)} findings file(s) the subagent turns were given are not named by "
                f"the item `Review rounds`, which names {len(findings)}: the record and "
                "`stages.md` do not agree")
    for path in findings:
        count = sum(1 for files in given if path in files)
        if count < 2:
            return (f"the findings file `{path}` that the item `Review rounds` names is named by "
                    f"{count} subagent turn(s), and a round has a fix and the review of that fix"
                    + (f"; the message of {unread} turn(s) could not be read" if unread else ""))
    spent = sum((cost for files, cost in turns.values()
                 if files is not None and files & set(findings)), Decimal(0))
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


def fill(cycle: Cycle, git: Git, commit: str, folder: bytes, own: bool, prices: Prices) -> None:
    """Read the values of a cycle from the copy its commit holds."""
    prefix = RECORDS.encode("ascii") + folder + b"/"
    try:
        entries = tree_entries(git, commit)
        record, record_reason = read_file(git, entries, prefix + b"cycle.md")
        stages, stages_reason = read_file(git, entries, prefix + b"stages.md")
    except (GitError, ValueError, UnicodeError) as error:
        reason = f"git could not read the copy: {display(error)}"
        record = stages = None
        record_reason = stages_reason = reason
    record_lines = record_fenced = None
    if record is None:
        cycle.unknown += [("Process pin", record_reason), ("Remarks", record_reason)]
    else:
        record_lines = remarks_check.split_lines(record)
        record_fenced = remarks_check.fenced_flags(record_lines)
        cycle.pin, reason = process_pin(record_lines, record_fenced, own)
        if reason:
            cycle.unknown.append(("Process pin", reason))
        cycle.remarks, reason = remarks_count(record_lines, record_fenced)
        if reason:
            cycle.unknown.append(("Remarks", reason))
    working_name = "Working time without waiting for tools"
    if stages is None:
        cycle.unknown += [(working_name, stages_reason), ("Waiting for tools", stages_reason),
                          ("Cost", stages_reason), ("Fix rounds share", stages_reason)]
        return
    lines = remarks_check.split_lines(stages)
    fenced = remarks_check.fenced_flags(lines)
    cycle.working, reason = stages_time(lines, fenced, WORKING_LINE,
                                        "working time without waiting for tools")
    if reason:
        cycle.unknown.append((working_name, reason))
    cycle.waiting, reason = stages_time(lines, fenced, WAITING_LINE, "waiting for tools")
    if reason:
        cycle.unknown.append(("Waiting for tools", reason))
    add_cost(cycle, record_lines, record_fenced, record_reason, lines, fenced, prices)


def committed_date(stamp: str) -> str | None:
    """The UTC date of a commit's timestamp as `git log` gives it, or None where the commit holds
    a value outside the years the platform can read: a commit's date is written by whoever made
    it, and one such commit must not end the count of every repository."""
    try:
        return datetime.fromtimestamp(int(stamp), timezone.utc).date().isoformat()
    except (OSError, OverflowError, ValueError):
        return None


def read_repository(key: str, path: Path, prices: Prices) -> Read:
    """The cycles whose records the history of one repository holds."""
    result = Read(key)
    git = Git(path)
    try:
        git.run("rev-parse", "--git-dir")
        result.shallow = git.run("rev-parse", "--is-shallow-repository").strip() == b"true"
        listed = git.run("log", "--full-history", "--branches", "--remotes", "--diff-filter=A",
                         "--no-renames", "--topo-order", "--reverse", "--format=%H %ct", "--",
                         RECORD_PATHSPEC).decode("ascii")
        copies: dict[bytes, list[tuple[str, str]]] = {}
        for line in listed.splitlines():
            commit, _, stamp = line.partition(" ")
            added = git.run("diff-tree", "--root", "--no-commit-id", "-r", "-z", "--no-renames",
                            "--diff-filter=A", "--name-only", commit, "--", RECORD_PATHSPEC)
            for name in added.split(b"\0"):
                parts = name.split(b"/")
                if len(parts) == 4 and parts[3] == b"cycle.md" and parts[2]:
                    copies.setdefault(parts[2], []).append((commit, stamp))
    except (GitError, ValueError, UnicodeError) as error:
        result.error = display(error)
        return result
    for folder, commits in copies.items():
        first, stamp = commits[0]
        committed = committed_date(stamp)
        cycle = Cycle(key, display(folder.decode("utf-8", errors="replace")), first,
                      committed or UNKNOWN, [commit for commit, _ in commits[1:]])
        if committed is None:
            cycle.unknown.append(("Committed", "the commit's date lies outside the years the "
                                               "command can read"))
        fill(cycle, git, commits[-1][0], folder, key == THE_WAY, prices)
        result.cycles.append(cycle)
    result.cycles.sort(key=lambda cycle: (cycle.committed, cycle.folder, cycle.record))
    return result


# The result


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


def money(value: Decimal | None) -> str:
    return UNKNOWN if value is None else format(value.quantize(MONEY), "f")


def share_text(value: Decimal | None) -> str:
    return UNKNOWN if value is None else f"{value.quantize(SHARE)}%"


def render(reads: list[Read], prices: Prices) -> str:
    cycles = [cycle for read in reads for cycle in read.cycles]
    lines = [
        "# Count of the audit of the process",
        "",
        "Written by `process-audit/audit_count.py`. A cycle is named by its repository and *Record*, "
        "the commit that adds the first copy of its record; *Later copies* are the commits that "
        "add it again after a correction, and the values are read from the last copy. *Process "
        "pin* is the version of the-way the cycle ran on, *Remarks* the number of its process "
        "remarks, and the times are h:mm:ss from the copy's `stages.md`. `unknown` is a value the "
        "copy does not give, never zero; *Unknown values* says why.",
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
    lines += [
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
            f"| {duration(cycle.waiting)} |")
    lines += [
        "",
        "## Cost",
        "",
        f"Prices of the list dated {prices.date}: a cost belongs to that series only, and a new "
        "list starts a new one (WAY-338). A stretch of the orchestrator with no token usage costs "
        "nothing. *Fix rounds* is the number of findings files the record's *Review rounds* "
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
            f"| {share_text(cycle.share)} |")
    lines += [
        "",
        "## Unknown values",
        "",
        "| Repository | Record | Value | Why |",
        "|---|---|---|---|",
    ]
    for cycle in cycles:
        for value, why in cycle.unknown:
            lines.append(f"| {cell(cycle.repository)} | {cycle.record} | {value} | {cell(why)} |")
    return "\n".join(lines) + "\n"


def write(folder: Path, name: str, text: str) -> None:
    target = folder / name
    temporary = folder / f".{name}.tmp"
    try:
        with open(temporary, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(temporary, target)
    except OSError as error:
        raise AuditCountError(f"cannot write {name} in the directory of the entry "
                              f"`{RESULTS_ENTRY}` under `{THE_WAY}`: "
                              f"{display(error.strerror or error)}") from None


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--locations", default=DEFAULT_LOCATIONS, metavar="FILE")
    parser.add_argument("--repository", action="append", default=[], metavar="KEY")
    parser.add_argument("--prices", default=str(PRICES), metavar="FILE")
    try:
        args = parser.parse_args(argv)
        locations = read_locations(args.locations)
        entry_path(locations, THE_WAY, REGISTER_ENTRY, "file")
        results = entry_path(locations, THE_WAY, RESULTS_ENTRY, "directory")
        named = repositories(locations, args.repository)
        for key, path in named.items():
            if inside(results, path):
                raise AuditCountError(f"the directory of the entry `{RESULTS_ENTRY}` under "
                                      f"`{THE_WAY}` lies inside the repository "
                                      f"`{display(key)}`; the result is never written into a "
                                      f"repository")
        prices = read_prices(args.prices)
        reads = [read_repository(key, path, prices) for key, path in named.items()]
        text = render(reads, prices)
        dated = f"count-{date.today().isoformat()}.md"
        write(results, dated, text)
        write(results, LATEST, text)
    except AuditCountError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    failed = [read for read in reads if read.error]
    for read in failed:
        print(f"Error: repository `{display(read.key)}`: {read.error}", file=sys.stderr)
    count = sum(len(read.cycles) for read in reads)
    print(f"Wrote {dated} and {LATEST}: {count} cycles in {len(reads) - len(failed)} of "
          f"{len(reads)} repositories.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
