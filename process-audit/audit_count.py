"""The counting command of the audit of the process: the cycles whose records the user's
repositories hold in their history, and for each the version of the-way it ran on, its number of
process remarks and its times (WAY-330, WAY-332, WAY-338, WAY-341); and the problems of the user's
register of problems counted against those cycles (WAY-330, WAY-333 to WAY-336, WAY-345,
WAY-346).

Usage:

    python -B process-audit/audit_count.py [--locations FILE] [--repository KEY ...] [--today DATE]
                                           [--prices FILE]

In a product, the path starts with `.the-way/`. The command asks nothing and reads nothing from
stdin, and git runs with its terminal prompt off, so that a system scheduler can start it with no
human present and stdin closed or empty. DATE, written YYYY-MM-DD, is the day of the run, which
the days of waiting count to; the default is today in UTC, so that the same input and the same
DATE give the same bytes.

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
*Output*, per million tokens; a price cell `—` is a model with no price, and a cell that is neither
a number nor `—` refuses the list (WAY-337, WAY-339). An error about the locations file or the price
list names its option, `--locations` or `--prices`, never the path it was given (WAY-320).

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
- the cost at constant prices (WAY-337, WAY-352), from the copy's `stages.md` in either of its two
  forms. The newer form is known by its heading: each row of the section *Stages: start, waiting
  for tools and tokens by model* is priced at the list's prices, its input less its cached input at
  the *Input* price, its cached input at the *Cached input* price and its output at the *Output*
  price. The older form has no such section: it is known by its table of tokens by model, the one
  table whose header row begins with *Model* and has the columns *Model*, *Total tokens*, *Input*,
  *Cached input* and *Output*, found exactly once, and each of its rows is priced in the same way.
  Cache writes are inside *Input* (`task-cycle/cycle_stages.py` folds them in), so they are priced
  as input: an approximation. A model the list gives no price for, a row that does not read, a
  cached input above its input, a subagent stage with no token usage (the model `—`), a stage or a
  row whose usage the stage report could not read (the model `unknown`), a section where no stage
  has any, a table of the older form with no row, or such a table written twice, gives the cost
  `unknown`, never zero; a row of the orchestrator with no token usage, time it worked with no
  response of a model, costs nothing;
- *Fix rounds*: the number of findings files the record's item `Review rounds` names, `0` where it
  reads `none`. A fix round is the fix of a review's findings and the review of that fix; the
  orchestrator gives both the findings file, by its path in `reports/`, and the item names each
  round by that path: one entry for each round under the item, opening with the word `findings`
  and the path between backticks (`task-cycle/record_template.md`);
- the share of the cost spent in fix rounds (WAY-337): the cost of the subagent turns whose cell
  *Files named* in that section of `stages.md` names a findings file of a round the record names,
  each turn counted once, over the cycle's cost. It is `0.0%` only where the item reads `none` and
  no subagent turn was given a findings file, told by the word `findings` in its name as the check
  of process remarks tells one (WAY-294). It is `unknown`, with the reason, where the item is
  missing, doubled or names a round otherwise than by its findings file, where `stages.md` has no
  column *Files named* (an earlier form of the section), where `stages.md` is of the older form,
  whose table of tokens by model gives no turns (the number of fix rounds is still read from the
  record's item, as for the newer form), where a cell of it is not a list of files of `reports/`,
  where the rows of one turn disagree in their stage or their files, where a subagent turn's cell
  reads `unknown`, since that turn may serve a round, where a findings file the record names is
  named by fewer than two subagent turns, the fix and the review of that fix, or where a turn was
  given a findings file the record does not name: a wrong figure is worse than `unknown`. The cost
  is still given.

The process versions (WAY-339, WAY-341): each cycle is grouped by the version of the-way its
*Process pin* resolves to, the full commit that `git rev-parse --disambiguate` names in the
checkout of the-way. A cycle whose pin is unknown, does not resolve, is ambiguous, or whose commit
has no readable date stands apart as *no version*, with its reason, and is in no series. Versions
are ordered by their commit's date (`git log -1 --format=%ct`), ties by the full hash. A series is
a run of consecutive versions between which none of these changes:

- the price list the costs are priced by (one list per run, so this never splits a run);
- the register's list of classes: a date of *Added* or *Withdrawn* on or between the days of the
  two versions, or a list the register does not give in full, which splits at every version;
- the tree of the-way under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`,
  `task-cycle/spec` and `task-cycle/cycle_stages.py` (`git diff --quiet`; exit 1, or any other
  failure, counts as changed). This test is deliberately conservative: any change of those files
  starts a series, though not every change alters a stage report's form or the reviewer's
  instructions. It cannot tell such a change from another one, and errs toward fewer comparisons.

Measures are compared only within a series, and each series is its own section of the result
(WAY-339). Per version: the median cost at constant prices of its cycles with a known cost, and
three answers, each `yes`, `no` or `unknown`. Q1, a contradiction with the product's settlements
that came out only after code was written: from the item *Discarded attempt* of each cycle, `none`
is no, text naming an open design choice with no word that denies it (`no`, `not`, `without`...)
among the last four words just before the phrase, in the same clause, is yes (a denial elsewhere in
the item, as in the template's `foundation entries none`, does not count), other text or a missing
or doubled item is unknown; where the item reads `none` but
*Review rounds* names a findings file, the answer is unknown, since the findings are not in the
record. Q2, more than one third of the slices of the plans came back too large: from the item
*Plan* (`none` on the one-author route leaves the cycle out; otherwise the figure written just
before the word `slices`, as in `8 slices`, and where there is none or more than one, unknown)
and the entries of *Slices returned too large* (`none` is 0); the answer is yes where three times
the sum of too-large slices is above the sum of planned slices, and unknown where the plan of a
cycle that has one is not read, since its slices could change the answer. Q3, the cost falls: the
median against the previous version of the same series, yes where lower, unknown where there is
none.

A value a record or a `stages.md` does not give — an earlier form, a missing, doubled or malformed
line, a file that is no regular file, too large or not UTF-8 — is `unknown`, never zero, and the
result says why. A field of `stages.md` that the form the file's own signs name needs and the file
lacks is a missing field (WAY-344, which gives this command its own way to end): the values that need it
are `unknown`, the result is written, and the run ends with exit 1 and, for each missing field, a
line on stderr `Error: repository `<key>`: cycle `<folder>`: the file `stages.md` of the copy lacks
the field `<field>``. The fields are: the columns `#`, `Stage`, `Start`, `Waiting for tools`,
`Model`, `Input`, `Cached input` and `Output` of the table of the newer form's section, and that
table itself, which a heading with no table misses (the column `Files named` is never missing: a
section without it is the earlier form of the section); the columns `Input`, `Cached input` and
`Output` of the older form's table, `Model` being its sign; the section and the table both, where
the file has neither the heading nor a table beginning with `Model`; and, where the file has one of
the lines `- Working time without waiting for tools:` and `- Waiting for tools:`, the other (a file
with neither is an earlier form, read with both times unknown and no error). Every field of
`stages.md` is under this check, since this reading of the file is reworked. Where every field
stands in a table but in another order, or another column stands beside them, none is missing: the
table is refused with a reason, as before. The records, the `stages.md` files and the locations
file are untrusted input:
their text reaches the result only as a commit, a number or a time it was read as, and a folder,
a key or a name in a reason on one line, cut to 200 characters, with each control character and
each bar written as `\\x..`, so that no cell of a table holds a bar; a bar and the text `\\x7c`
then read alike. No path written in them is followed, and nothing of them is run. A commit dated
outside the years the platform reads gives *Committed* `unknown`. Git runs only to read, with no
`GIT_` variable of the environment it is started in and no signature shown: `rev-parse`, `log`,
`diff`, `diff-tree`, `ls-tree`, `cat-file` and `merge-base`.

The register of problems is read as untrusted input, in the form `process-audit/problem_register.md`
gives: five tables, *Classes*, *Weights*, *Costs of an occurrence*, *Issues* and *Problems*, found
by their headings and header rows. A heading, a table or a column of a header row the register lacks
is a missing field (WAY-344): the run ends with exit 2, nothing written, and the `Error:` line names
every field missing, never reading its absence as an empty value. Where every column stands in the
header row but not in the template's order, or another stands beside them, or a heading is written
twice, no field is missing: the table is refused. A row that does not read, an unknown class,
weight or cost of an occurrence, an issue in no row of *Issues*, a doubled name, a *Fix* that is no
commit or a date that is no date refuses that row or table with a reason. A table of *Weights* or of
*Costs of an occurrence* that does not name its levels, four or five, each once is refused, and an
`Error:` of the register on stderr gives exit 1. A refused row of *Problems* still belongs to the
cycle and the issue it names: each count of that cycle or issue reads `at least n`, as the row is
not in it. What else depends on a refused row or table is `unknown`. A problem whose cycle no named
repository holds is `unknown`, not dropped, and so is a
problem whose *Record* is a commit that adds the records of more than one cycle, whose counts then
read `at least n`. A problem is counted once, by its row (WAY-334); a cycle copied again after a
correction is one cycle, and its problems are counted once. *Unknown values* lists at most 500
values the register leaves unknown, and says how many more there are.

For each cycle, its problems by class and weight. For each issue whose *Fate* is `fixed`, its
problems in the cycles whose *Process pin* holds the fix, and apart those in the cycles whose pin
does not hold it, never by date: the holding is `git merge-base --is-ancestor <fix> <pin>` in the
checkout of the-way (the entry `repository` under `the-way`, or this checkout), a pin written as a
short hash resolved there, and a pin or a fix that checkout lacks, an ambiguous short hash or a pin
`unknown` gives `unknown` with its reason (WAY-335). For each issue whose *Fate* is `open`, the number
of cycles its problems came back in, and the days it has waited: the cycles in which a problem of
the issue stands, except the first of them, so `0` where it stands in one cycle only, and `at least
n` where a refused row or a problem of a cycle not read may belong to a cycle not counted; and from
the earliest commit date of the copies its problems' *Record* names to the day of the run,
`unknown` where a problem's cycle is not known. An
issue `dropped` is counted apart, with no waiting. The issues are listed in the order of the
register, never ranked by their counts (WAY-336). For each issue, whatever its fate, how many of its
problems stand on each of the five levels of the cost of an occurrence (WAY-345, WAY-346): a cost
counted by the issue and never by the cycle, and a different thing from the cost of a cycle in
money, which the section *Cost* gives (WAY-337). A level counts the issue's problems by their rows,
whether or not their cycles are read.

The result is Markdown in UTF-8 with LF line ends, the same bytes for the same input, written to
`count-<YYYY-MM-DD>.md`, the date of the run, and `count-latest.md` in the directory of
`audit_results`, never inside a repository it reads or the checkout of the-way, read or not
(WAY-332): a section *Repositories*, a table of each
repository read and its cycles; a section *Cycles*, a table of one row per cycle; and a section
*Unknown values*, a table of each value given as `unknown` and why. A section *Cost*, a table of
one row per cycle with its price list's date (the series the cost belongs to), its cost in USD, its
number of fix rounds and the share of the cost in them. The sections *Problems by cycle*, *Fixed
issues*, *Open issues*, *Dropped issues* and *Cost of an occurrence by issue* give the register's
counts, and sit before *Unknown values*. On stdout it names the two files and the counts.

Exit code: 0 with the result written; 1 with the result written but a repository that could not be
read, a table of the register refused as a whole, or a field missing in a `stages.md`, named in the
result and in an `Error:` line on stderr; 2 with `Error: <message>` on stderr and nothing written, when an argument is wrong, the
locations file, the price list, the register or an entry it needs is missing or wrong, the register
lacks a heading, a table or a column it needs, the register is larger than 4 MiB or not UTF-8, the
result directory lies inside a repository to read or the checkout of the-way, or the result cannot
be written.

Standard library only.
"""

from __future__ import annotations

import argparse
import bisect
import json
import os
import re
import subprocess
import sys
from collections import Counter
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
SECTION_TITLE = "Stages: start, waiting for tools and tokens by model"
STAGES_HEADING = "## " + SECTION_TITLE
STAGE_COLUMNS = ["#", "Stage", "Start", "Waiting for tools", "Model", "Input", "Cached input",
                 "Output"]
FILES_COLUMN = "Files named"
# The table of tokens by model, which every form of `stages.md` has and the older form is read
# from: the table whose header row begins with `Model` (WAY-352).
MODEL_COLUMN = "Model"
OLDER_COLUMNS = [MODEL_COLUMN, "Total tokens", "Input", "Cached input", "Output"]
OLDER_NEEDED = ("Input", "Cached input", "Output")
# The fields of `stages.md` a form needs, as an `Error:` line names them (WAY-344): no backtick
# stands in a name, since the line writes the name between backticks.
FIELD_SECTION = f"section {SECTION_TITLE}"
FIELD_SECTION_TABLE = f"table of the section {SECTION_TITLE}"
FIELD_OLDER_TABLE = f"table with the first cell {MODEL_COLUMN}"
OLDER_NO_TURNS = ("`stages.md` is of the older form, whose table of tokens by model gives no turns, "
                  "so no round is tied to the turns that served it")
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
# The reviewed files of the-way: a change of any of them between two versions starts a series.
TREE_PATHS = ("task-cycle/change", "task-cycle/plan", "task-cycle/review", "task-cycle/spec",
              "task-cycle/cycle_stages.py")
# The items of the record the questions of a process version read (task-cycle/record_template.md).
ITEM_DISCARDED = "Discarded attempt"
ITEM_PLAN = "Plan"
ITEM_TOO_LARGE = "Slices returned too large"
DESIGN_CHOICE = "open design choice"
SLICES_WORD = re.compile(r"slices", re.I)
# The count of slices written just before the word, as `8 slices`: a figure standing alone, no
# letter or digit before it, so `F1a` and `F1–F4` give none. Every repetition is bounded.
SLICES_COUNT = re.compile(r"(?<![A-Za-z0-9])([0-9]{1,6})[ \t]{1,8}slices(?![A-Za-z0-9])", re.I)
# Words that deny what follows them, so that `no open design choice` is not read as one.
NEGATIONS = frozenset({"no", "not", "none", "nor", "never", "without", "neither", "nothing"})
WORDS = re.compile(r"[a-z]+")
# A denial is looked for only among the last words just before the phrase, in the same clause: the
# template's own form of a discarded attempt holds `none` and the like in its other parts. At most
# this many characters before the phrase are read, so that the work per phrase is bounded.
DENIAL_WORDS = 4
DENIAL_REACH = 60
CLAUSE_MARKS = frozenset(";:,.—–()[]!?\"")
CONTRACTED_NOT = ("n't", "n’t")
# The locations file and the price list are named by their options in an error, never by their
# path, which is the user's (WAY-320).
LOCATIONS_LABEL = "the locations file (`--locations`)"
PRICES_LABEL = "the price list (`--prices`)"
# *Unknown values* lists at most this many values the register leaves unknown.
MAX_LISTED = 500
# The two files of a cycle's record that the count reads (WAY-347, WAY-349), each written by its
# script: `mechanism_measures.md` by task-cycle/cycle_measures.py, `gate_times.md` by
# task-cycle/gate_times.py. A copy holding neither is an earlier form.
MEASURES_FILE = "mechanism_measures.md"
GATE_FILE = "gate_times.md"
MEASURE_LABELS = (
    "Calls in all", "Calls of the orchestrator", "Calls of subagents", "Mean context per call",
    "Mean context per call of the orchestrator",
    "Share of the context in calls above 200000 tokens",
    "Context of the orchestrator's first call", "Context of the orchestrator's middle call",
    "Context of the orchestrator's last call", "Cache written, 5 minutes", "Cache written, 1 hour",
    "Cache written again by the orchestrator", "Calls of the orchestrator with a cache write again",
    "Cache written again by subagents", "Calls of subagents with a cache write again",
)
SHARE_LABEL = "Share of the context in calls above 200000 tokens"
MEASURE_WHOLE = re.compile(r"[0-9]{1,15}")
MEASURE_SHARE = re.compile(r"([0-9]{1,3}\.[0-9])%")
GATE_COLUMNS = ["Started (UTC)", "Exit code", "Total seconds", "Other gate runs at the same time",
                "Directory", "Directory seconds"]
GATE_RUN_COLUMNS = GATE_COLUMNS[:4]
GATE_TABLE_FIELD = "table of the runs"
GATE_STARTED = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}")
GATE_CODE = re.compile(r"[0-9]{1,3}")
GATE_TOTAL = re.compile(r"[0-9]{1,9}\.[0-9]{3}")
GATE_OTHERS = re.compile(r"[0-9]{1,6}")
GATE_SECONDS = re.compile(r"[0-9]{1,9}(?:\.[0-9]{1,9})?")
# The runs and the directories of one run read from `gate_times.md`, the rest not read and said so.
MAX_RUNS = 500
MAX_DIRECTORIES = 50
GATE_NONE = "—"
DIRECTORY_SEPARATOR = " · "


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
    label = LOCATIONS_LABEL
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        raise AuditCountError(f"{label} does not exist") from None
    except OSError as error:
        raise AuditCountError(f"cannot read {label}: {display(error.strerror or error)}") from None
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError(f"{label} is not UTF-8") from None

    def unique(pairs: list[tuple[str, object]]) -> dict:
        seen: dict[str, object] = {}
        for key, value in pairs:
            if key in seen:
                raise AuditCountError(f"{label} holds the key or entry "
                                      f"`{display(key[:TEXT_CAP])}` twice in one object")
            seen[key] = value
        return seen

    try:
        data = json.loads(text, object_pairs_hook=unique)
    except json.JSONDecodeError as error:
        raise AuditCountError(f"{label} is not JSON: line {error.lineno}, column "
                              f"{error.colno}") from None
    except ValueError:
        # A number of more digits than Python converts is no JSONDecodeError.
        raise AuditCountError(f"{label} is not JSON: it holds a number too long to read") from None
    except RecursionError:
        raise AuditCountError(f"{label} is nested too deeply") from None
    if not isinstance(data, dict):
        raise AuditCountError(f"{label} is not a JSON object")
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

    def execute(self, arguments: tuple[str, ...]) -> subprocess.CompletedProcess:
        # A `GIT_` variable of the environment the command starts in, such as GIT_DIR set by a
        # hook, would point git at another repository or add configuration: none is passed on.
        environment = {name: value for name, value in os.environ.items()
                       if not name.upper().startswith("GIT_")}
        environment.update(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never",
                           GIT_OPTIONAL_LOCKS="0")
        try:
            return subprocess.run(
                ["git", "--no-pager", "-c", "core.fsmonitor=false", "-c", "log.showSignature=false",
                 "-C", str(self.repository), *arguments], stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=GIT_TIMEOUT, env=environment)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitError(f"git {arguments[0]}: {display(error)}") from None

    def run(self, *arguments: str) -> bytes:
        result = self.execute(arguments)
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise GitError(f"git {arguments[0]} failed ({result.returncode}): "
                           f"{display(detail)}")
        return result.stdout

    def code(self, *arguments: str) -> int:
        """The exit code of git run to read, for a command whose exit code is its answer."""
        return self.execute(arguments).returncode


# Reading a cycle


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
    # is unknown (WAY-347).
    measures: dict[str, str] = field(default_factory=dict)
    # The runs of `gate_times.md`, each as the cells after the repository and the record (WAY-349).
    gate_runs: list[list[str]] = field(default_factory=list)
    # The fields of the two files that the copy lacks, as (file, field), for the `Error:` line.
    missing_in: list[tuple[str, str]] = field(default_factory=list)


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


def has_line(lines: list[str], fenced: list[bool], prefix: str) -> bool:
    """Whether a line of `stages.md` outside code fences begins with `prefix`."""
    return any(not inside and line.startswith(prefix) for line, inside in zip(lines, fenced))


def missing_line(cycle: Cycle, prefix: str) -> str:
    """Record the time line `prefix` as a field `stages.md` lacks, and give the reason."""
    name = f"line {prefix[2:-1]}"
    cycle.missing.append(name)
    return missing_reason(name)


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
    label = PRICES_LABEL
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        raise AuditCountError(f"{label} does not exist") from None
    except OSError as error:
        raise AuditCountError(f"cannot read {label}: {display(error.strerror or error)}") from None
    if len(raw) > MAX_BYTES:
        raise AuditCountError(f"{label} is larger than {MAX_BYTES} bytes")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError(f"{label} is not UTF-8") from None
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    dates = header_fields(lines, fenced, PRICE_HEADING)
    if len(dates) != 1:
        raise AuditCountError(f"{label} "
                              + ("holds the line `List date` more than once" if dates
                                 else "holds no line `List date`"))
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", dates[0]):
        raise AuditCountError(f"the line `List date` of {label} is no date written YYYY-MM-DD")
    try:
        date.fromisoformat(dates[0])
    except ValueError:
        raise AuditCountError(f"the line `List date` of {label} is no date") from None
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
                    raise AuditCountError(f"a table of {label} lacks one of the columns "
                                          f"{', '.join(PRICE_COLUMNS)}")
                columns = [cells.index(name_of) for name_of in PRICE_COLUMNS]
            continue
        if is_separator(cells):
            continue
        if not cells or max(columns) >= len(cells) or not cells[0]:
            raise AuditCountError(f"a row of a table of {label} has fewer cells than its header")
        model = cells[0]
        if model in table:
            raise AuditCountError(f"{label} names model `{display(model[:TEXT_CAP])}` twice")
        numbers: list[Decimal | None] = []
        for index in columns:
            if cells[index] == NO_MODEL:
                numbers.append(None)
            elif PRICE.fullmatch(cells[index]):
                numbers.append(Decimal(cells[index]))
            else:
                # A typo would otherwise leave the model unpriced, and every cycle that used it
                # would point away from the list.
                raise AuditCountError(f"a price of model `{display(model[:TEXT_CAP])}` in {label} "
                                      "is neither a number nor `—`")
        table[model] = None if any(number is None for number in numbers) else (
            numbers[0], numbers[1], numbers[2])
    if not table:
        raise AuditCountError(f"{label} names no model")
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


@dataclass
class StageTable:
    """What `stages.md` gives for its cost, in the form its own signs name (WAY-337, WAY-352): the
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
    headings = [index for index, (line, inside) in enumerate(zip(lines, fenced))
                if not inside and line.strip() == STAGES_HEADING]
    if len(headings) > 1:
        return StageTable(reason="`stages.md` holds that section more than once")
    if headings:
        return section_table(lines, fenced, headings[0])
    return older_table(lines, fenced)


def section_table(lines: list[str], fenced: list[bool], heading: int) -> StageTable:
    """The newer form: the rows of the table under the heading of the section. A heading with no
    table, or a table whose header row lacks one of the columns the form needs, is a field missing;
    the column *Files named* is never one: a section without it is the earlier form of the
    section."""
    table: list[list[str]] = []
    for line, inside in zip(lines[heading + 1:], fenced[heading + 1:]):
        if inside:
            continue
        if line.startswith("#"):
            break
        if line.startswith("|"):
            table.append(table_cells(line))
    if not table:
        return StageTable(reason="the section in `stages.md` holds no table",
                          missing=[FIELD_SECTION_TABLE])
    absent = missing_columns(table[0], STAGE_COLUMNS, f"of the section {SECTION_TITLE}")
    if absent:
        return StageTable(reason="the table of the section in `stages.md` lacks a column",
                          missing=absent)
    named = table[0] == STAGE_COLUMNS + [FILES_COLUMN]
    if table[0] != STAGE_COLUMNS and not named:
        return StageTable(reason=("the table of the section in `stages.md` is not of the form the "
                                  "stage report gives"))
    columns = len(table[0])
    body = [cells for cells in table[1:] if not is_separator(cells)]
    if not body:
        return StageTable(reason="the section in `stages.md` holds no stage row")
    rows: list[StageTokens] = []
    for cells in body:
        if len(cells) != columns:
            return StageTable(reason=(f"a row of the section in `stages.md` has {len(cells)} "
                                      f"cells, not {columns}"))
        counts = [token_count(cells[index]) for index in (5, 6, 7)]
        if any(count is None for count in counts):
            return StageTable(reason=("a token count in the section of `stages.md` is not a number "
                                      f"of at most {TOKEN_DIGITS} digits"))
        row = StageTokens(cells[0], cells[1], cells[4], counts[0], counts[1], counts[2])
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
    starts = [index for index, (line, inside) in enumerate(zip(lines, fenced))
              if not inside and line.startswith("|") and table_cells(line)[:1] == [MODEL_COLUMN]
              and (index == 0 or fenced[index - 1] or not lines[index - 1].startswith("|"))]
    if not starts:
        return StageTable(reason=("`stages.md` holds neither the section `" + SECTION_TITLE
                                  + "` nor a table of tokens by model"),
                          missing=[FIELD_SECTION, FIELD_OLDER_TABLE])
    if len(starts) > 1:
        return StageTable(reason="`stages.md` holds the table of tokens by model more than once")
    start = starts[0]
    header = table_cells(lines[start])
    absent = missing_columns(header, OLDER_NEEDED, f"with the first cell {MODEL_COLUMN}")
    if absent:
        return StageTable(reason="the table of tokens by model in `stages.md` lacks a column",
                          missing=absent)
    form = "the table of tokens by model in `stages.md` is not of the form the stage report gives"
    if header != OLDER_COLUMNS:
        return StageTable(reason=form)
    if (start + 1 >= len(lines) or fenced[start + 1] or not lines[start + 1].startswith("|")
            or not is_separator(table_cells(lines[start + 1]))):
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
            return StageTable(reason=(f"a row of the table of tokens by model in `stages.md` has "
                                      f"{len(cells)} cells, not {len(OLDER_COLUMNS)}"))
        counts = [token_count(cells[index]) for index in range(1, len(OLDER_COLUMNS))]
        if any(count is None for count in counts):
            return StageTable(reason=("a token count in the table of tokens by model in "
                                      f"`stages.md` is not a number of at most {TOKEN_DIGITS} "
                                      "digits"))
        rows.append(StageTokens(str(number), cells[0], cells[0], counts[1], counts[2], counts[3]))
    return StageTable(rows=rows, older=True)


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


def item_texts(lines: list[str], fenced: list[bool],
               label: str) -> list[tuple[str, list[tuple[str, bool]]]]:
    """The items `- <label>: ...` of a record outside code fences, each as its text on its line and
    the lines indented under it with their fence flags. The whole record is read, since the items
    of the spec and the plan sit below the header. One pass: each item reads down to the next line
    that starts at the margin."""
    found = []
    for index, line in enumerate(lines):
        if fenced[index] or not line.startswith("- "):
            continue
        field_found = header_field(line)
        if field_found is None or field_found[0] != label:
            continue
        below = []
        for next_index in range(index + 1, len(lines)):
            text = lines[next_index]
            if not text.strip():
                continue
            if remarks_check.indent_of(text) == 0:
                break
            below.append((text, fenced[next_index]))
        found.append((field_found[1], below))
    return found


def item_count_reason(label: str, items: list) -> str:
    return (f"the record holds the item `{label}` more than once" if items
            else f"the record holds no item `{label}`")


def item_words(rest: str, below: list[tuple[str, bool]]) -> str:
    """The item's text: its line and the lines under it, joined."""
    return " ".join([rest] + [text.strip() for text, _ in below if text.strip()]).strip()


def reads_none_first(text: str) -> bool:
    """Whether the text opens with the word `none`, as `none on the one-author route` does."""
    word = text.strip(" \t*_`.").casefold()
    return word.startswith("none") and not word[4:5].isalnum()


def read_contradiction(lines: list[str], fenced: list[bool]) -> tuple[str | None, str | None]:
    """Q1: whether a contradiction with the settlements came out only after code was written, as
    the record's item *Discarded attempt* and its *Review rounds* give it: `yes`, `no`, or None with
    the reason."""
    items = item_texts(lines, fenced, ITEM_DISCARDED)
    if len(items) != 1:
        return None, item_count_reason(ITEM_DISCARDED, items)
    text = item_words(items[0][0], items[0][1])
    if remarks_check.reads_none(text):
        findings, why = review_rounds(lines, fenced)
        if findings is None:
            return None, ("the item `Review rounds` does not give its findings files, so whether a "
                          "review round found a contradiction is not known")
        if findings:
            return None, "a review round names findings, and their content is not in the record"
        return "no", None
    if reads_none_first(text):
        # `none` followed by more words, such as `none — no open design choice`, is not read as a
        # discarded open design choice either way.
        return None, "the item `Discarded attempt` opens with none and holds more text"
    folded = text.casefold()
    if DESIGN_CHOICE in folded:
        if any(denied_before(folded, at) for at in phrase_starts(folded)):
            return None, ("the item `Discarded attempt` names an open design choice with a word "
                          "just before it that may deny it")
        return "yes", None
    return None, "the item `Discarded attempt` names neither none nor an open design choice"


def phrase_starts(folded: str) -> list[int]:
    """The place of each occurrence of the phrase in the case-folded text, one pass."""
    found = []
    at = folded.find(DESIGN_CHOICE)
    while at != -1:
        found.append(at)
        at = folded.find(DESIGN_CHOICE, at + len(DESIGN_CHOICE))
    return found


def denied_before(folded: str, at: int) -> bool:
    """Whether a denying word stands among the last words just before the phrase at `at`, in the
    same clause: at most DENIAL_REACH characters are read, cut after the last clause mark, and the
    last DENIAL_WORDS words of what remains are searched. Linear: no pattern is tried again."""
    before = folded[max(0, at - DENIAL_REACH):at]
    for index in range(len(before) - 1, -1, -1):
        if before[index] in CLAUSE_MARKS:
            before = before[index + 1:]
            break
    if any(mark in before for mark in CONTRACTED_NOT):
        return True
    return bool(NEGATIONS.intersection(WORDS.findall(before)[-DENIAL_WORDS:]))


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
        return False, None, ("the item `Plan` does not give one count of slices before the word "
                             "`slices`")
    return False, int(figures[0]), None


def read_too_large(lines: list[str], fenced: list[bool]) -> tuple[int | None, str | None]:
    """The item *Slices returned too large*: 0 where it reads `none`, the number of its entries
    where it lists them, or None with the reason."""
    items = item_texts(lines, fenced, ITEM_TOO_LARGE)
    if len(items) != 1:
        return None, item_count_reason(ITEM_TOO_LARGE, items)
    rest, below = items[0]
    if reads_none_first(rest) and not any(text.strip() for text, _ in below):
        return 0, None
    markers = [remarks_check.indent_of(text) for text, inside in below
               if not inside and remarks_check.MARKER.fullmatch(text)]
    if rest.strip() or not markers:
        return None, ("the item `Slices returned too large` reads neither none nor an entry "
                      "per slice")
    base = min(markers)
    return sum(1 for indent in markers if indent == base), None


def process_questions(cycle: Cycle, lines: list[str] | None, fenced: list[bool] | None,
                      reason: str | None) -> None:
    """Read the questions of a process version from the cycle's record; a value that cannot be
    read is `unknown` with its reason, and the record missing makes all of them unknown."""
    if lines is None or fenced is None:
        cycle.unknown += [(ITEM_DISCARDED, reason), (ITEM_PLAN, reason),
                          (ITEM_TOO_LARGE, reason)]
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
        cycle.unknown.append((ITEM_TOO_LARGE,
                              "more slices are returned too large than the plan made"))


def is_orchestrator_row(name: str) -> bool:
    """The orchestrator's own rows, as `cycle_stages.py` names them: its stretches and the rows of
    its work while subagents run in parallel. Their work is the orchestrator's, so they serve no
    fix round by the files they name; the orchestrator's tokens while a fix runs stand in the
    fix's own row."""
    return name == ORCHESTRATOR or name.startswith("orchestrator while in parallel: ")


def priced(rows: list[StageTokens], prices: Prices) -> tuple[list[Decimal] | None, str | None]:
    """The cost in dollars of each row at the list's prices, or None with the reason: a model with
    no price, a cached input above its input, a subagent stage with no token usage, a stage whose
    model is unknown, or a section with no stage that has any, make the cost unknown. A row of the
    orchestrator with no token usage — a stretch, or its work while subagents run in parallel —
    costs nothing."""
    costs: list[Decimal] = []
    if all(row.model == NO_MODEL for row in rows):
        return None, "every stage of `stages.md` has no token usage, so the cost is not known"
    for row in rows:
        # A name from `stages.md` is cut before it reaches a reason: the reason is written twice
        # per cycle, and a crafted name would otherwise make the result as large as the file.
        name = row.name[:TEXT_CAP]
        if row.model == UNKNOWN:
            # `cycle_stages.py` writes this for a stage whose transcript holds no token usage at
            # all, and for tokens of a response that names no model.
            return None, (f"stage `{name}` gives its model as unknown: its token usage was not "
                          "read, or names no model")
        if row.model == NO_MODEL:
            if is_orchestrator_row(row.name):
                # A row of the orchestrator's own work with no response of a model in it:
                # `cycle_stages.py` reads every response of the orchestrator's transcript.
                costs.append(Decimal(0))
                continue
            # `cycle_stages.py` writes this mark for a stage it found no token usage for: its
            # tokens are not known, so its cost is not zero.
            return None, (f"stage `{name}` has no token usage in its transcript, so its cost "
                          "is not known")
        if row.cached > row.input:
            return None, f"the cached input of stage `{name}` is above its input"
        price = prices.table.get(row.model)
        if price is None:
            return None, f"the price list gives no price for model `{row.model[:TEXT_CAP]}`"
        costs.append(cost_at(price, row))
    return costs, None


def cost_at(price: tuple[Decimal, Decimal, Decimal], row: StageTokens) -> Decimal:
    """The cost in dollars of a row at a price: its input less its cached input at the *Input*
    price, its cached input at the *Cached input* price and its output at the *Output* price."""
    input_price, cached_price, output_price = price
    return (Decimal(row.input - row.cached) * input_price + Decimal(row.cached) * cached_price
            + Decimal(row.output) * output_price) / MILLION


def priced_older(rows: list[StageTokens], prices: Prices) -> tuple[list[Decimal] | None, str | None]:
    """The cost in dollars of each row of the table of tokens by model at the list's prices, as
    `priced` gives it for the rows of the section, or None with the reason: a model `unknown`, a
    cached input above its input, or a model with no price make the cost unknown."""
    costs: list[Decimal] = []
    for row in rows:
        name = row.model[:TEXT_CAP]
        if row.model == UNKNOWN:
            return None, ("the table of tokens by model names the model `unknown`: its token usage "
                          "was not read, or names no model")
        if row.cached > row.input:
            return None, f"the cached input of model `{name}` is above its input"
        price = prices.table.get(row.model)
        if price is None:
            return None, f"the price list gives no price for model `{name}`"
        costs.append(cost_at(price, row))
    return costs, None


def missing_reason(name: str, file: str = "stages.md") -> str:
    return f"the file `{file}` of the copy lacks the field `{name}`"


def add_cost(cycle: Cycle, record_lines: list[str] | None, record_fenced: list[bool] | None,
             record_reason: str | None, stages_lines: list[str], stages_fenced: list[bool],
             prices: Prices) -> None:
    """The cycle's cost at the list's prices and the share of its fix rounds in it; a value that
    cannot be given is `unknown` with its reason, never zero. A field the form of `stages.md` needs
    and the file lacks is also put on the cycle's `missing`, for the `Error:` line (WAY-344)."""
    table = stage_table(stages_lines, stages_fenced)
    if table.rows is None:
        if table.missing:
            for name in table.missing:
                cycle.missing.append(name)
                cycle.unknown += [("Cost", missing_reason(name)),
                                  ("Fix rounds share", missing_reason(name))]
        else:
            cycle.unknown += [("Cost", table.reason), ("Fix rounds share", table.reason)]
        return
    costs, reason = (priced_older if table.older else priced)(table.rows, prices)
    if costs is None:
        cycle.unknown += [("Cost", reason), ("Fix rounds share", reason)]
        return
    total = sum(costs, Decimal(0))
    if total >= COST_CEILING:
        cycle.unknown += [("Cost", "the cost is at or above the command's limit of 10^18 USD"),
                          ("Fix rounds share", "the cost is at or above the command's limit")]
        return
    cycle.cost = total
    if table.older:
        # The table of tokens by model ties no round to the turns that served it: the share is
        # unknown (WAY-352), but the number of rounds stands in the record.
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


def fix_rounds_share(rows: list[StageTokens], costs: list[Decimal], total: Decimal, named: bool,
                     findings: list[str], cycle: Cycle) -> str | None:
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
            return (f"the cell `{FILES_COLUMN}` of stage `{row.name[:TEXT_CAP]}` is not a list of "
                    "files of `reports/`")
        if row.number in turns:
            # The model rows of one turn repeat its stage and its files; rows that disagree do
            # not tell which of them the turn was given.
            files, spent = turns[row.number]
            if names[row.number] != row.name or files != row.files:
                return (f"the rows of stage number {row.number[:TEXT_CAP]} disagree in their stage "
                        f"or in their cell `{FILES_COLUMN}`")
            turns[row.number] = (files, spent + cost)
        else:
            turns[row.number] = (row.files, cost)
            names[row.number] = row.name
    given = [files for files, _ in turns.values() if files is not None]
    unread = len(turns) - len(given)
    extra = sorted({path for files in given for path in files
                    if FINDINGS_WORD in path.rsplit("/", 1)[-1]} - set(findings))
    if extra:
        return (f"{len(extra)} findings file(s) the subagent turns were given are not named by "
                f"the item `Review rounds`, which names {len(findings)}: the record and "
                "`stages.md` do not agree")
    if unread:
        # Such a turn may be a fix or the review of a fix: neither `none` nor a share without it
        # can be told.
        return (f"the message of {unread} subagent turn(s) could not be read, so whether they "
                "serve a fix round is not known")
    for path in findings:
        count = sum(1 for files in given if path in files)
        if count < 2:
            return (f"the findings file `{path}` that the item `Review rounds` names is named by "
                    f"{count} subagent turn(s), and a round has a fix and the review of that fix")
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


def read_optional(git: Git, entries: dict, prefix: bytes, name: str) -> tuple[str | None, str | None]:
    """The text of a file of the copy that an earlier form lacks, or None with the reason."""
    path = prefix + name.encode("ascii")
    if path not in entries:
        return None, f"the copy holds no `{name}`: an earlier form"
    return read_file(git, entries, path)


def measure_fits(label: str, value: str) -> bool:
    """Whether a value of `mechanism_measures.md` is what its label gives: a whole number, and for
    the share a number of percent up to 100."""
    if label == SHARE_LABEL:
        found = MEASURE_SHARE.fullmatch(value)
        return found is not None and Decimal(found.group(1)) <= 100
    return MEASURE_WHOLE.fullmatch(value) is not None


def read_measures(cycle: Cycle, text: str | None, reason: str | None) -> None:
    """Read the cycle-level lines of `mechanism_measures.md` by their labels (WAY-347). A label the
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
                cycle.unknown.append((label, f"`{MEASURES_FILE}` lacks a field, so its values "
                                             "are unknown"))
        return
    for label in MEASURE_LABELS:
        values = found[label]
        if len(values) > 1:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` holds the line `{label}` more than "
                                         "once"))
        elif values[0] == UNKNOWN:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` gives it as unknown"))
        elif measure_fits(label, values[0]):
            cycle.measures[label] = values[0]
        else:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` gives it in a form that is not what "
                                         "its label gives"))


def gate_value(reasons: list[tuple[str, str]], column: str, value: str, pattern: re.Pattern,
               why: str) -> str:
    """A cell of a run in `gate_times.md` as written where it has the form of its column, else
    `unknown` with the reason kept in `reasons` under the value `Gate runs: <column>`."""
    if pattern.fullmatch(value):
        return value
    reasons.append((f"Gate runs: {column}",
                    f"`{GATE_FILE}` gives it as unknown" if value == UNKNOWN else why))
    return UNKNOWN


def read_gate(cycle: Cycle, text: str | None, reason: str | None) -> None:
    """Read the runs of `gate_times.md` from its table (WAY-349). A table lacking one of its six
    columns, or lacking the table, is a missing field, and the runs are not read; a row of the wrong
    number of cells is a run of its own with unknown values; the runs and the directories beyond the
    limits are not read, and the reason is given."""
    if text is None:
        cycle.unknown.append(("Gate runs", reason))
        return
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    header = next((index for index, (line, inside) in enumerate(zip(lines, fenced))
                   if not inside and line.startswith("|")), None)
    if header is None:
        cycle.missing_in.append((GATE_FILE, GATE_TABLE_FIELD))
        cycle.unknown.append(("Gate runs", missing_reason(GATE_TABLE_FIELD, GATE_FILE)))
        return
    names = table_cells(lines[header])
    absent = [name for name in GATE_COLUMNS if name not in names]
    if absent:
        for name in absent:
            field_name = f"column {name} of the table"
            cycle.missing_in.append((GATE_FILE, field_name))
            cycle.unknown.append(("Gate runs", missing_reason(field_name, GATE_FILE)))
        return
    at = {name: names.index(name) for name in GATE_COLUMNS}
    reasons: list[tuple[str, str]] = []
    # Each run: its four run cells, or None for a row of the wrong number of cells, and its
    # directories as (name, seconds).
    runs: list[tuple[list[str] | None, list[tuple[str, str]]]] = []
    last: list[str] | None = None
    cut_directories = False
    for index in range(header + 1, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            break
        cells = table_cells(lines[index])
        if is_separator(cells):
            continue
        if len(cells) != len(names):
            reasons.append(("Gate runs", f"a row of the table in `{GATE_FILE}` has {len(cells)} "
                                         f"cells, not {len(names)}"))
            runs.append((None, []))
            last = None
            continue
        key = [cells[at[name]] for name in GATE_RUN_COLUMNS]
        if last is None or key != last:
            if len(runs) >= MAX_RUNS:
                reasons.append(("Gate runs", f"`{GATE_FILE}` holds more than {MAX_RUNS} runs: the "
                                             "rest are not read"))
                break
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
    if cut_directories:
        reasons.append(("Gate runs: Directories", f"a run in `{GATE_FILE}` lists more than "
                                                  f"{MAX_DIRECTORIES} directories: the rest are "
                                                  "not listed"))
    for key, directories in runs:
        if key is None:
            cycle.gate_runs.append([UNKNOWN] * 5)
            continue
        started, code, total, others = [
            gate_value(reasons, column, value, pattern, why)
            for column, value, pattern, why in zip(
                GATE_RUN_COLUMNS, key,
                (GATE_STARTED, GATE_CODE, GATE_TOTAL, GATE_OTHERS),
                ("a start is not written YYYY-MM-DD HH:MM:SS.mmm",
                 "an exit code is not a whole number",
                 "a total is not written as seconds to three decimals",
                 "a count of other gate runs is not a whole number"))]
        listed = []
        for name, seconds in directories:
            seconds = gate_value(reasons, "Directory seconds", seconds, GATE_SECONDS,
                                 "the seconds of a directory are not a number")
            listed.append(f"{name[:TEXT_CAP]} " + (seconds if seconds == UNKNOWN
                                                   else seconds + " s"))
        cycle.gate_runs.append([started, code, total, others,
                                DIRECTORY_SEPARATOR.join(listed) or GATE_NONE])
    cycle.unknown.extend(dict.fromkeys(reasons))


def fill(cycle: Cycle, git: Git, commit: str, folder: bytes, own: bool, prices: Prices) -> None:
    """Read the values of a cycle from the copy its commit holds."""
    prefix = RECORDS.encode("ascii") + folder + b"/"
    try:
        entries = tree_entries(git, commit)
        record, record_reason = read_file(git, entries, prefix + b"cycle.md")
        stages, stages_reason = read_file(git, entries, prefix + b"stages.md")
        measures = read_optional(git, entries, prefix, MEASURES_FILE)
        gate = read_optional(git, entries, prefix, GATE_FILE)
    except (GitError, ValueError, UnicodeError) as error:
        reason = f"git could not read the copy: {display(error)}"
        record = stages = None
        record_reason = stages_reason = reason
        measures = gate = (None, reason)
    read_measures(cycle, *measures)
    read_gate(cycle, *gate)
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
    process_questions(cycle, record_lines, record_fenced, record_reason)
    working_name = "Working time without waiting for tools"
    if stages is None:
        cycle.unknown += [(working_name, stages_reason), ("Waiting for tools", stages_reason),
                          ("Cost", stages_reason), ("Fix rounds share", stages_reason)]
        return
    lines = remarks_check.split_lines(stages)
    fenced = remarks_check.fenced_flags(lines)
    # A file with one of the two time lines and not the other lacks the other (WAY-344); a file with
    # neither is an earlier form, whose two times are unknown with no field missing.
    has_working = has_line(lines, fenced, WORKING_LINE)
    has_waiting = has_line(lines, fenced, WAITING_LINE)
    cycle.working, reason = stages_time(lines, fenced, WORKING_LINE,
                                        "working time without waiting for tools")
    if has_waiting and not has_working:
        reason = missing_line(cycle, WORKING_LINE)
    if reason:
        cycle.unknown.append((working_name, reason))
    cycle.waiting, reason = stages_time(lines, fenced, WAITING_LINE, "waiting for tools")
    if has_working and not has_waiting:
        reason = missing_line(cycle, WAITING_LINE)
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
                      committed or UNKNOWN, [commit for commit, _ in commits[1:]],
                      {commit: committed_date(when) or UNKNOWN for commit, when in commits})
        if committed is None:
            cycle.unknown.append(("Committed", "the commit's date lies outside the years the "
                                               "command can read"))
        fill(cycle, git, commits[-1][0], folder, key == THE_WAY, prices)
        result.cycles.append(cycle)
    result.cycles.sort(key=lambda cycle: (cycle.committed, cycle.folder, cycle.record))
    return result


# The register of problems

COSTS_TITLE = "Costs of an occurrence"
# The five tables of the register, each under its heading, with the header row the template gives.
REGISTER_TABLES = (
    ("Classes", ["Class", "Meaning", "Added", "Withdrawn"]),
    ("Weights", ["Weight", "Meaning"]),
    (COSTS_TITLE, ["Cost of an occurrence", "Meaning"]),
    ("Issues", ["Issue", "What", "Fate", "Fix"]),
    ("Problems", ["Repository", "Record", "Stages", "What", "Class", "Weight",
                  "Cost of an occurrence", "Issue"]),
)
# The scale of weight has these four levels and no other (WAY-333).
LEVELS = ["no problem", "Minor", "Important", "Critical"]
# The scale of the cost of an occurrence has these five levels, each dearer than the one before, and
# no other (WAY-345). It is a different thing from the cost of a cycle in money (WAY-337).
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
# A text copied from the register into the result is cut to this many characters.
TEXT_CAP = 200


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
    # and the issue it names, and the counts that include it say so (WAY-336).
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


def named_rows(register: Register, title: str, rows: list[list[str]], width: int,
               check) -> list[tuple[str, int, list[str]]]:
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


def register_table(lines: list[str], fenced: list[bool], title: str, columns: list[str],
                   missing: list[str]) -> tuple[list[list[str]] | None, str | None]:
    """The rows of the table under the heading `## <title>`, or None with the reason. The table
    starts at the first line that begins with `|` before the next heading, and its header row must
    be `columns`; its rows run on until a line that does not begin with `|`. A heading, a table or
    a column the register lacks is a field missing (WAY-344): it is added to `missing`, in words
    that name it, as well as returned as the reason."""
    headings = [index for index, (line, inside) in enumerate(zip(lines, fenced))
                if not inside and line.strip() == f"## {title}"]
    if len(headings) != 1:
        if not headings:
            missing.append(f"the heading `## {title}`")
        return None, (f"the register holds the heading `## {title}` "
                      + ("more than once" if headings else "not at all"))
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
    if (separator >= len(lines) or not lines[separator].startswith("|")
            or not is_separator(table_cells(lines[separator]))):
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
        raise AuditCountError("cannot read the register of problems: "
                              f"{display(error.strerror or error)}") from None
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
        register.classes = [name for name, _, _ in
                            named_rows(register, "Classes", tables["Classes"], 4, check_class)]
        for cells in tables["Classes"]:
            if len(cells) != 4 or check_class(cells)[1] is not None:
                register.class_dates_unknown = True
                continue
            register.class_dates += [text for text in (cells[2], cells[3]) if valid_date(text)]
        register.class_dates.sort()
    if tables["Weights"] is not None:
        weights = named_rows(register, "Weights", tables["Weights"], 2, check_weight)
        if sorted(name for name, _, _ in weights) != sorted(LEVELS):
            why = "the table `Weights` must name the four levels, each once"
            register.errors.append(why)
            register.refuse("table `Weights`", why)
    if tables[COSTS_TITLE] is not None:
        costs = named_rows(register, COSTS_TITLE, tables[COSTS_TITLE], 2, check_cost_level)
        if sorted(name for name, _, _ in costs) != sorted(COST_LEVELS):
            why = f"the table `{COSTS_TITLE}` must name the five levels, each once"
            register.errors.append(why)
            register.refuse(f"table `{COSTS_TITLE}`", why)
    if tables["Issues"] is not None:
        register.issues = [(name, cells[2], cells[3].lower()) for name, _, cells in
                           named_rows(register, "Issues", tables["Issues"], 4, check_issue)]
    if tables["Problems"] is not None:
        class_names = set(register.classes)
        issue_names = {name for name, _, _ in register.issues}
        for number, cells in enumerate(tables["Problems"], 1):
            value = f"row {number} of `Problems`"
            if len(cells) != 8:
                register.refuse(value, f"the row has {len(cells)} cells, not 8",
                                cells[0] if cells else "", cells[1] if len(cells) > 1 else "")
                register.refused_problems.append((cells[0] if cells else "",
                                                  cells[1] if len(cells) > 1 else "", ""))
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
            register.problems.append(Problem(number, repository, record.lower(), cls, weight,
                                             cost, issue))
    return register


class Ancestry:
    """Whether the checkout of the-way holds a version: the answer of `git merge-base
    --is-ancestor`, asked of the checkout the entry `repository` under `the-way` names (WAY-335).
    A git that cannot read the checkout makes every answer unknown, with the reason."""

    def __init__(self, git: Git):
        self.git = git
        self.failure: str | None = None
        self.shallow = False
        self.commits: dict[str, tuple[str | None, str | None]] = {}
        self.holdings: dict[tuple[str, str], tuple[bool | None, str | None]] = {}
        try:
            self.shallow = git.run("rev-parse", "--is-shallow-repository").strip() == b"true"
        except GitError as error:
            self.failure = str(error)

    def commit(self, text: str) -> tuple[str | None, str | None]:
        """The full hash of the commit that `text` names in the checkout, or None with the reason:
        the checkout lacks it, a short hash is ambiguous, or it is no commit."""
        if text not in self.commits:
            self.commits[text] = self.resolve(text)
        return self.commits[text]

    def resolve(self, text: str) -> tuple[str | None, str | None]:
        if self.failure is not None:
            return None, f"the checkout of the-way could not be read by git: {self.failure}"
        if SHORT_HASH.fullmatch(text) is None:
            return None, "the commit is no hexadecimal name of a commit"
        shallow = " (the checkout is a shallow clone, which may lack it)" if self.shallow else ""
        try:
            names = self.git.run("rev-parse", f"--disambiguate={text}").decode("ascii").split()
            if not names:
                return None, f"the-way's history lacks commit {text}{shallow}"
            if len(names) > 1:
                return None, f"the short hash {text} is ambiguous in the-way's history"
            if self.git.code("rev-parse", "--verify", "--quiet", f"{names[0]}^{{commit}}") != 0:
                return None, f"{text} is no commit of the-way's history"
        except GitError as error:
            return None, f"git could not read the-way's history: {error}"
        return names[0], None

    def holds(self, pin: str, fix: str) -> tuple[bool | None, str | None]:
        """Whether the version `pin` holds the commit `fix`, or None with the reason."""
        if (pin, fix) not in self.holdings:
            self.holdings[(pin, fix)] = self.compare(pin, fix)
        return self.holdings[(pin, fix)]

    def compare(self, pin: str, fix: str) -> tuple[bool | None, str | None]:
        version, why = self.commit(pin)
        if version is None:
            return None, why
        fixed, why = self.commit(fix)
        if fixed is None:
            return None, why
        try:
            code = self.git.code("merge-base", "--is-ancestor", fixed, version)
        except GitError as error:
            return None, f"git could not compare the version {pin} with the fix: {error}"
        if code == 0:
            return True, None
        if code == 1:
            if self.shallow:
                return None, ("the version lacks the fix in a shallow clone of the-way, which may "
                              "lack its history")
            return False, None
        return None, f"git could not compare the version {pin} with the fix (exit code {code})"

    def stamp(self, version: str) -> tuple[int | None, str | None]:
        """The committer date of a full commit hash of the checkout, as a Unix time, or None with
        the reason; a value that is no number is not read (WAY-339)."""
        try:
            text = self.git.run("log", "-1", "--format=%ct", version, "--").decode("ascii").strip()
        except (GitError, ValueError) as error:
            return None, f"git could not read the date of the commit: {display(error)}"
        try:
            return int(text), None
        except ValueError:
            return None, "the date of the commit is not a number"

    def changed(self, earlier: str, later: str) -> bool:
        """Whether the reviewed files of the-way differ between two full commit hashes; a git
        that fails counts as changed, so that a series is never joined by mistake (WAY-339)."""
        try:
            return self.git.code("diff", "--quiet", earlier, later, "--", *TREE_PATHS) != 0
        except GitError:
            return True


def counted(count: int, refused: int) -> str:
    """A count as a cell: exact where no refused row belongs to it, `at least n` where some does."""
    return f"at least {count}" if refused else str(count)


@dataclass
class Analysis:
    """The tables the register adds to the result, as rows of text, and the values it leaves
    unknown as (repository, record, value, why)."""
    cycle_rows: list[list[str]]
    fixed_rows: list[list[str]]
    open_rows: list[list[str]]
    dropped_rows: list[list[str]]
    cost_rows: list[list[str]]
    unknown: list[tuple[str, str, str, str]]


def analyse(reads: list["Read"], register: Register, ancestry: Ancestry,
            today: date) -> Analysis:
    """Count the register's problems against the cycles the reads found: per cycle by class and
    weight (WAY-334), per fixed issue by whether the pin of its cycles holds the fix (WAY-335), and
    per open issue the cycles it came back in and the days it has waited (WAY-336)."""
    cycles = [cycle for read in reads for cycle in read.cycles]
    # Each commit that adds a copy of a record, with the cycles whose copy it adds: one commit may
    # add the records of several cycles, and then it names none of them.
    owners: dict[tuple[str, str], list[Cycle]] = {}
    for cycle in cycles:
        for record in dict.fromkeys([cycle.record, *cycle.later]):
            owners.setdefault((cycle.repository, record), []).append(cycle)
    index = {key: found[0] for key, found in owners.items() if len(found) == 1}
    shared = {key: found for key, found in owners.items() if len(found) > 1}
    # The problems of a *Record* that names several cycles count in none of them, so the counts of
    # each of those cycles read `at least n`.
    uncounted: Counter = Counter()
    found = [(problem, index.get((problem.repository, problem.record)))
             for problem in register.problems]
    unknown = list(register.refused)
    counts: dict[tuple[str, str], Counter] = {}
    for problem, cycle in found:
        if cycle is not None:
            tally = counts.setdefault((cycle.repository, cycle.record), Counter())
            tally[(problem.cls, problem.weight)] += 1
            continue
        key = (problem.repository, problem.record)
        if key in shared:
            for owner in shared[key]:
                uncounted[(owner.repository, owner.record)] += 1
            why = ("its Record is a commit that adds the records of more than one cycle, so the "
                   "cycle it belongs to is not known")
        else:
            why = ("no named repository holds the cycle of its record; name its key with "
                   "--repository")
        unknown.append((problem.repository[:TEXT_CAP], problem.record,
                        f"row {problem.number} of `Problems`", why))
    # A refused row belongs to the cycle its Repository and Record name, and to the issue its Issue
    # names, when each is usable; a row with neither stays in *Unknown values* only. Its count shows
    # as `at least n`, since the row's own figure is not in the count (the review's Important finding).
    refused_cycle: Counter = Counter()
    refused_issue: Counter = Counter()
    valid_issues = {name for name, _, _ in register.issues}
    for repository, record, issue in register.refused_problems:
        key = (repository, record.lower())
        cycle = index.get(key) if FULL_HASH.fullmatch(record) else None
        if cycle is not None:
            refused_cycle[(cycle.repository, cycle.record)] += 1
        elif FULL_HASH.fullmatch(record) and key in shared:
            for owner in shared[key]:
                uncounted[(owner.repository, owner.record)] += 1
        if issue in valid_issues:
            refused_issue[issue] += 1
    cycle_rows = []
    for cycle in cycles:
        key = (cycle.repository, cycle.record)
        mine = counts.get(key, Counter())
        refused = refused_cycle[key]
        partial = refused + uncounted[key]
        head = [cycle.repository, cycle.record]
        rows_here = []
        for cls in register.classes:
            tally = [mine[(cls, weight)] for weight in LEVELS]
            if any(tally):
                rows_here.append(head + [cls] + [counted(count, partial) for count in tally]
                                 + [str(refused)])
        if not rows_here:
            rows_here.append(head + [NONE] + [counted(0, partial)] * 4 + [str(refused)])
        cycle_rows += rows_here
    # The problems of each issue, gathered once rather than by a scan of every problem per issue.
    by_issue: dict[str, list[tuple[Problem, Cycle | None]]] = {}
    for problem, cycle in found:
        by_issue.setdefault(problem.issue, []).append((problem, cycle))
    fixed_rows, open_rows, dropped_rows, cost_rows = [], [], [], []
    for name, fate, fix in register.issues:
        members = by_issue.get(name, [])
        # The cost of an occurrence stands in the problem's row, so the cycle is not needed: a
        # problem of a cycle that is not read is counted, and a refused row makes the count a lower
        # bound.
        levels = Counter(problem.cost for problem, _ in members)
        cost_rows.append([name, fate] + [counted(levels[level], refused_issue[name])
                                         for level in COST_LEVELS] + [str(refused_issue[name])])
        hit = {(cycle.repository, cycle.record): cycle for _, cycle in members
               if cycle is not None}
        not_read = sum(1 for _, cycle in members if cycle is None)
        refused = refused_issue[name]
        if fate == FIXED:
            fixed, why = ancestry.commit(fix)
            if fixed is None:
                unknown.append((THE_WAY, NONE, f"the fix of issue `{name}`", why))
            holding = lacking = pin_unknown = 0
            for _, cycle in members:
                if cycle is None:
                    continue
                if cycle.pin is None:
                    pin_unknown += 1
                elif fixed is not None:
                    holds, why = ancestry.holds(cycle.pin, fix)
                    if holds is None:
                        pin_unknown += 1
                        unknown.append((cycle.repository, cycle.record, "Process pin", why))
                    elif holds:
                        holding += 1
                    else:
                        lacking += 1
            shown = (["unknown", "unknown"] if fixed is None
                     else [counted(holding, refused), counted(lacking, refused)])
            fixed_rows.append([name, fix] + shown + [counted(pin_unknown, refused),
                                                     counted(not_read, refused), str(refused)])
        elif fate == "open":
            # Each problem waits from the copy its Record names, which after a correction may be
            # a later copy than the cycle's first.
            dates = [cycle.copies.get(problem.record, cycle.committed)
                     for problem, cycle in members if cycle is not None]
            if refused:
                days = UNKNOWN
                unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                "some of its problem rows are refused, so its waiting is not "
                                "known"))
            elif not members:
                days = "—"
            elif not_read:
                days = UNKNOWN
                unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                "a problem's cycle is not known, so the day it came back first is "
                                "not known"))
            elif UNKNOWN in dates:
                days = UNKNOWN
                unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                "the commit date of the copy one of its problems names is unknown"))
            else:
                waited = (today - date.fromisoformat(min(dates))).days
                if waited < 0:
                    days = UNKNOWN
                    unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                    "its earliest copy is dated after the day of the run"))
                else:
                    days = str(waited)
            # The problem stands in the first cycle it is found in and comes back in each other
            # cycle, so the count is the cycles that hold it less one, whichever of them is first.
            # A refused row or a problem of an unread cycle may belong to a cycle not counted
            # here, so the count is a lower bound then: at least the known cycles less one.
            came_back = max(len(hit) - 1, 0)
            open_rows.append([name, counted(came_back, refused + not_read),
                              counted(len(members), refused), counted(not_read, refused), days,
                              str(refused)])
        else:
            dropped_rows.append([name, counted(len(hit), refused), counted(len(members), refused),
                                 counted(not_read, refused), str(refused)])
    listed = list(dict.fromkeys(unknown))
    if len(listed) > MAX_LISTED:
        # A register far larger than a real one would make the result as large as itself.
        more = len(listed) - MAX_LISTED
        listed = listed[:MAX_LISTED] + [(THE_WAY, NONE, "values of the register not listed",
                                         f"{more} more values the register leaves unknown are not "
                                         "listed here; the register holds them")]
    return Analysis(cycle_rows, fixed_rows, open_rows, dropped_rows, cost_rows, listed)


# The process versions (WAY-339, WAY-341)


@dataclass
class Version:
    """A version of the process: the full commit of the-way that cycles pin, its committer date
    as a Unix time and as a day, the price list its costs are priced by, and its cycles."""
    commit: str
    stamp: int
    day: str
    price: str
    cycles: list[Cycle]


@dataclass
class Series:
    """A run of versions between which no change splits a series: why it begins with its first
    version, its versions, and the rows of its table."""
    begins: str
    versions: list[Version]
    rows: list[list[str]] = field(default_factory=list)


@dataclass
class Versions:
    series: list[Series] = field(default_factory=list)
    no_version: list[Cycle] = field(default_factory=list)
    unknown: list[tuple[str, str, str, str]] = field(default_factory=list)


VERSION_HEADER = ["Version (commit)", "Committed", "Cycles", "Cycles with a known cost",
                  "Median cost (USD)", "Q1: contradiction only after code", "Plans read",
                  "Q2: more than a third of slices too large", "Q3: cost falls"]


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


def series_boundary(earlier: Version, later: Version, register: Register,
                    ancestry: Ancestry) -> str | None:
    """Why a new series begins at `later`, or None where both versions share one series."""
    if earlier.price != later.price:
        return "the price list changed"
    if register.class_dates_unknown:
        return "the register's list of classes is not given in full, so it may have changed"
    # A date on the day of either version counts: the test errs toward more series.
    at = bisect.bisect_left(register.class_dates, earlier.day)
    if at < len(register.class_dates) and register.class_dates[at] <= later.day:
        return "the register's list of classes changed between the two versions"
    if ancestry.changed(earlier.commit, later.commit):
        return "the reviewed files of the-way changed between the two versions"
    return None


def contradiction_of(version: Version) -> tuple[str, str | None]:
    """Q1 for a version: yes where a cycle answers yes, no where every cycle answers no."""
    answers = [cycle.contradiction for cycle in version.cycles]
    if "yes" in answers:
        return "yes", None
    if answers and all(answer == "no" for answer in answers):
        return "no", None
    return "unknown", "a cycle's answer is unknown, so the question is not settled for the version"


def too_large_of(version: Version) -> tuple[str, str, str | None]:
    """Q2 for a version, with the cell *Plans read*: the sums of the slices of the version's plans,
    too-large over planned, above one third is yes. Where a plan is not read, its slices could
    turn either answer, so the answer is unknown."""
    planned_cycles = [cycle for cycle in version.cycles if not cycle.plan_left_out]
    read = [cycle for cycle in planned_cycles
            if cycle.planned is not None and cycle.too_large is not None]
    plans_read = f"{len(read)} of {len(planned_cycles)}"
    if not read:
        return plans_read, "unknown", "no cycle's plan can be read"
    if len(read) < len(planned_cycles):
        return plans_read, "unknown", (f"the plans of {len(planned_cycles) - len(read)} cycle(s) "
                                       "are not read, so the share of the version's slices is "
                                       "not known")
    planned = sum(cycle.planned for cycle in read if cycle.planned is not None)
    large = sum(cycle.too_large for cycle in read if cycle.too_large is not None)
    if planned == 0:
        return plans_read, "unknown", "the plans that are read hold no slice"
    return plans_read, ("yes" if 3 * large > planned else "no"), None


def process_versions(reads: list[Read], register: Register, ancestry: Ancestry,
                     prices: Prices) -> Versions:
    """Group the cycles by their version, split the versions into series, and answer the three
    questions of each version within its own series (WAY-339, WAY-341)."""
    result = Versions()
    groups: dict[str, list[Cycle]] = {}
    for read in reads:
        for cycle in read.cycles:
            if cycle.pin is None:
                result.no_version.append(cycle)
                continue
            commit, why = ancestry.commit(cycle.pin)
            if commit is None:
                result.no_version.append(cycle)
                result.unknown.append((cycle.repository, cycle.record, "Process pin", why or ""))
                continue
            groups.setdefault(commit, []).append(cycle)
    versions: list[Version] = []
    for commit, members in groups.items():
        stamp, why = ancestry.stamp(commit)
        day = committed_date(str(stamp)) if stamp is not None else None
        if day is None:
            why = why or "the commit's date lies outside the years the command can read"
            result.no_version += members
            result.unknown.append((THE_WAY, NONE, f"version {commit}", why))
            result.unknown += [(cycle.repository, cycle.record, "Process pin",
                                "its version has no readable date") for cycle in members]
            continue
        versions.append(Version(commit, stamp or 0, day, prices.date, members))
    versions.sort(key=lambda version: (version.stamp, version.commit))
    for version in versions:
        if not result.series:
            result.series.append(Series("the first version of the result", [version]))
            continue
        reason = series_boundary(result.series[-1].versions[-1], version, register, ancestry)
        if reason is None:
            result.series[-1].versions.append(version)
        else:
            result.series.append(Series(reason, [version]))
    for block in result.series:
        previous: Version | None = None
        previous_median: Decimal | None = None
        for version in block.versions:
            costs = [cycle.cost for cycle in version.cycles if cycle.cost is not None]
            median = median_of(costs)
            answer1, why1 = contradiction_of(version)
            plans, answer2, why2 = too_large_of(version)
            if previous is None:
                answer3, why3 = "unknown", "no previous version in the series"
            elif median is None or previous_median is None:
                answer3, why3 = "unknown", "a median cost is not known"
            else:
                answer3 = "yes" if median < previous_median else "no"
                why3 = None
            for label, why in (("contradiction only after code", why1),
                               ("slices too large", why2), ("cost falls", why3)):
                if why:
                    result.unknown.append((THE_WAY, NONE, f"{label}, version {version.commit}",
                                           why))
            block.rows.append([version.commit, version.day, str(len(version.cycles)),
                               str(len(costs)), money(median), answer1, plans, answer2, answer3])
            previous, previous_median = version, median
    return result


def versions_lines(versions: Versions) -> list[str]:
    """The section *Process versions*: a table per series and a note of the cycles in no version."""
    lines = [
        "## Process versions",
        "",
        "A version of the process is the commit of the-way that its cycles' *Process pin* "
        "resolves to, ordered by the commit's date. WAY-339 starts a new series at a new price "
        "list, or at a change of the form of a stage report, of the list of classes or of the "
        "instructions of the reviewer. This count splits more often than that: at a new price "
        "list, at a date of the register's list of classes, and at any change of the files of "
        "the-way under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and "
        "`task-cycle/spec` or of `task-cycle/cycle_stages.py`, whatever the change, so that it "
        "compares less and never across a change WAY-339 names. Measures are compared only "
        "within one series, and no cell sets a number of one series beside a number of another. "
        "Q1, Q2 and Q3 are `yes`, `no` or `unknown`; *Unknown values* says why an answer is "
        "unknown.",
        "",
    ]
    for number, block in enumerate(versions.series, 1):
        lines += [f"### Series {number}", "", f"Begins at this version: {block.begins}.", ""]
        lines += table(VERSION_HEADER, block.rows)
        lines.append("")
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
    rows = [[cycle.repository, cycle.record,
             *[cycle.measures.get(label, UNKNOWN) for label in MEASURE_LABELS]]
            for cycle in cycles]
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
    return lines + table(["Repository", "Record", "Started (UTC)", "Exit code", "Total seconds",
                          "Other gate runs at the same time", "Directories"], rows)


def render(reads: list[Read], prices: Prices, analysis: Analysis, versions: Versions) -> str:
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
        "list starts a new one (WAY-339). A stretch of the orchestrator with no token usage costs "
        "nothing. A cycle whose stage report has no section of stages is priced from its table of "
        "tokens by model at the same prices, and its share of the cost in fix rounds is unknown "
        "(WAY-352). *Fix rounds* is the number of findings files the record's *Review rounds* "
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
    lines += ["", *measures_lines(cycles), "", *gate_lines(cycles), "", *versions_lines(versions),
              ""]
    lines += [
        "## Problems by cycle",
        "",
        "The problems of the register by class and weight, each problem once (WAY-334); a cycle "
        "with no problem has one row, `none`. *Refused rows* are rows of *Problems* that name this "
        "cycle and were refused for a class, weight, cost of an occurrence or issue the register "
        "lacks; a count with one reads `at least n`, as the refused row is not in it. A count "
        "reads `at least n` also where a problem names as its *Record* a commit that adds the "
        "records of more than one cycle: it counts in none of them. Problems whose cycle no named repository holds, or "
        "whose *Record* names more than one cycle, are in *Unknown values*.",
        "",
    ]
    lines += table(["Repository", "Record", "Class", "No problem", "Minor", "Important",
                    "Critical", "Refused rows"], analysis.cycle_rows)
    lines += [
        "",
        "## Fixed issues",
        "",
        "A fixed issue's problems count apart by whether the *Process pin* of their cycle holds "
        "the fix, by the commit and never by date (WAY-335). `unknown` where the fix is not in the "
        "checkout of the-way, and the reasons are in *Unknown values*. *Refused rows* are refused "
        "rows of *Problems* that name this issue; a count with one reads `at least n`.",
        "",
    ]
    lines += table(["Issue", "Fix", "Problems in cycles whose pin holds the fix",
                    "Problems in cycles whose pin lacks it", "Problems with an unknown pin",
                    "Problems whose cycle is not read", "Refused rows"], analysis.fixed_rows)
    lines += [
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
        "ranked by their counts (WAY-336), and the weighing is the human's.",
        "",
    ]
    lines += table(["Issue", "Cycles its problems came back in", "Problems",
                    "Problems whose cycle is not read", "Days waiting", "Refused rows"],
                   analysis.open_rows)
    lines += [
        "",
        "## Dropped issues",
        "",
        "A dropped issue's problems are counted apart; it has no waiting. A count with refused "
        "rows of the issue reads `at least n`.",
        "",
    ]
    lines += table(["Issue", "Cycles", "Problems", "Problems whose cycle is not read",
                    "Refused rows"], analysis.dropped_rows)
    lines += [
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
        "costs (WAY-336), and the weighing is the human's.",
        "",
    ]
    lines += table(["Issue", "Fate", *COST_LEVELS, "Refused rows"], analysis.cost_rows)
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
    for repository, record, value, why in analysis.unknown:
        lines.append(f"| {cell(repository)} | {cell(record)} | {cell(value)} | {cell(why)} |")
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


def day_of(text: str) -> date:
    """A day written YYYY-MM-DD, for `--today`."""
    if DATE_TEXT.fullmatch(text) is None:
        raise argparse.ArgumentTypeError("the day is not written YYYY-MM-DD")
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError("the day is no date") from None


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--locations", default=DEFAULT_LOCATIONS, metavar="FILE")
    parser.add_argument("--repository", action="append", default=[], metavar="KEY")
    parser.add_argument("--prices", default=str(PRICES), metavar="FILE")
    parser.add_argument("--today", type=day_of, default=None, metavar="YYYY-MM-DD")
    try:
        args = parser.parse_args(argv)
        today = args.today if args.today is not None else datetime.now(timezone.utc).date()
        locations = read_locations(args.locations)
        register_path = entry_path(locations, THE_WAY, REGISTER_ENTRY, "file")
        results = entry_path(locations, THE_WAY, RESULTS_ENTRY, "directory")
        named = repositories(locations, args.repository)
        the_way = the_way_checkout(locations)
        # No repository holds the results, the-way's included, whether this run reads it or not
        # (WAY-332).
        for key, path in [*named.items(), (THE_WAY, the_way)]:
            if inside(results, path):
                raise AuditCountError(f"the directory of the entry `{RESULTS_ENTRY}` under "
                                      f"`{THE_WAY}` lies inside the repository "
                                      f"`{display(key)}`; the result is never written into a "
                                      f"repository")
        prices = read_prices(args.prices)
        register = read_register(register_path)
        ancestry = Ancestry(Git(the_way))
        reads = [read_repository(key, path, prices) for key, path in named.items()]
        analysis = analyse(reads, register, ancestry, today)
        versions = process_versions(reads, register, ancestry, prices)
        analysis.unknown = list(dict.fromkeys(analysis.unknown + versions.unknown))
        text = render(reads, prices, analysis, versions)
        dated = f"count-{today.isoformat()}.md"
        write(results, dated, text)
        write(results, LATEST, text)
    except AuditCountError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    failed = [read for read in reads if read.error]
    for read in failed:
        print(f"Error: repository `{display(read.key)}`: {read.error}", file=sys.stderr)
    for why in register.errors:
        print(f"Error: the register of problems: {display(why)}", file=sys.stderr)
    # A field a copy's `stages.md` lacks is no reason to withhold the result (WAY-344): each is
    # named here after the result is written. The folder is text of the history, so it is cut.
    lacking = [(read, cycle, missing_reason(name)) for read in reads for cycle in read.cycles
               for name in cycle.missing]
    # The fields of mechanism_measures.md and gate_times.md are named the same way (WAY-347, WAY-349).
    lacking += [(read, cycle, missing_reason(name, file)) for read in reads
                for cycle in read.cycles for file, name in cycle.missing_in]
    for read, cycle, reason in lacking:
        print(f"Error: repository `{display(read.key[:TEXT_CAP])}`: cycle "
              f"`{display(cycle.folder[:TEXT_CAP])}`: {reason}", file=sys.stderr)
    count = sum(len(read.cycles) for read in reads)
    print(f"Wrote {dated} and {LATEST}: {count} cycles in {len(reads) - len(failed)} of "
          f"{len(reads)} repositories.")
    return 1 if failed or register.errors or lacking else 0


if __name__ == "__main__":
    sys.exit(main())
