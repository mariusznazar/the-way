"""The analysis of the versions of the process, moved out of `audit_count.py`.

The version of the-way each cycle ran on and the series the versions are cut into (WAY-339,
WAY-350): whether the checkout of the-way holds a commit (`Ancestry`), the register's problems
counted against the cycles (`analyse`), the versions, their series and the boundaries between them,
the medians and the answers Q1, Q2 and Q3 of each version (`process_versions`, `measure_versions`),
and the values of a cycle that changed the tool that wrote them (`note_changed_tools`), as
`process-audit/audit_count.py` counts them. It holds the paths of the scripts whose change starts a
series. The cycles it reads are those of `record_reading.py` and the register that of
`problem_register.py`; no file outside the product is read here, and git runs only to read. It is
imported, never run, and runs nothing when imported. Standard library only.
"""

from __future__ import annotations

import bisect
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

from problem_register import (
    COST_LEVELS,
    FIXED,
    FULL_HASH,
    LEVELS,
    NONE,
    SHORT_HASH,
    Problem,
    Register,
)
from audit_shared import THE_WAY, Git, GitError
from record_reading import (
    ABSENCE_CAUSES,
    GATE_FILE,
    MEASURE_LABELS,
    MEASURES_FILE,
    SHARE_LABEL,
    Cycle,
    Read,
)
from stage_pricing import TEXT_CAP, UNKNOWN, Prices

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

display = remarks_check.display

MONEY = Decimal("0.000001")
# The script that measures the cost spans two files, `cycle_stages.py` and the module
# `stage_transcripts.py` it imports, and no other: a change of either between two versions starts a
# series of the cost (and so of the count of remarks), with a new price list (WAY-339).
COST_SCRIPT = "task-cycle/cycle_stages.py"
COST_MODULE = "task-cycle/stage_transcripts.py"
COST_SCRIPTS = (COST_SCRIPT, COST_MODULE)
# The files of the-way that give the form of a stage report and the instructions of the reviewer: a
# change of any of them between two versions starts a series of the count of remarks and none of the
# cost. The type of agent `the-way-stage.md` is here because the reviewer receives its text as its
# instruction.
COUNT_PATHS = (
    "task-cycle/change",
    "task-cycle/plan",
    "task-cycle/review",
    "task-cycle/spec",
    "task-cycle/agent-types/the-way-stage.md",
)
# *Unknown values* gives every value the count did not establish one line for each field and
# reason: the number of values of the pair and its first EXAMPLES values, each as its repository,
# record and value, and the field is the value with the number of its row, the name of its issue
# and the commit of its version taken out (WAY-330).
EXAMPLES = 3
ROW_NUMBER = re.compile(r"^row [0-9]+ of ")
ISSUE_VALUE = re.compile(r"^(the fix|waiting) of issue `.*`$")
VERSION_SUFFIX = re.compile(r"\bversion \S+$")
# The instruments that start a series of the measures they give (WAY-339): a change of the one
# starts a series of the mechanism measures, a change of one of the gate's scripts a series of the
# gate times, and nothing else does. The test runner of the gate is one of them: its output gives
# the time of each directory. The measures of a gate time are the total and each directory (WAY-350).
MEASURES_SCRIPT = "task-cycle/cycle_measures.py"
GATE_SCRIPT = "task-cycle/gate_times.py"
GATE_TEST_RUNNER = "gate/run_tests.py"
GATE_SCRIPTS = (GATE_SCRIPT, GATE_TEST_RUNNER)
TOTAL_MEASURE = "Total time of the run"
DIRECTORY_MEASURE = "Directory: "
# The three groups of tools that write the files of a cycle's copy, each as the file and the paths
# of the tools that wrote it: the paths are those that start the series of what they measure
# (COST_SCRIPTS, MEASURES_SCRIPT and GATE_SCRIPTS above), not a second list. A cycle of the-way
# whose own change changes one of them gives the values of that file as unknown (WAY-339).
STAGES_FILE = "stages.md"
WORKING_NAME = "Working time without waiting for tools"
WAITING_NAME = "Waiting for tools"
STAGES_VALUES = (WORKING_NAME, WAITING_NAME, "Cost", "Fix rounds share")
TOOL_GROUPS = (
    (STAGES_FILE, COST_SCRIPTS),
    (MEASURES_FILE, (MEASURES_SCRIPT,)),
    (GATE_FILE, GATE_SCRIPTS),
)


def committed_date(stamp: str) -> str | None:
    """The UTC date of a commit's timestamp as `git log` gives it, or None where the commit holds
    a value outside the years the platform can read: a commit's date is written by whoever made
    it, and one such commit must not end the count of every repository."""
    try:
        return datetime.fromtimestamp(int(stamp), timezone.utc).date().isoformat()
    except OSError, OverflowError, ValueError:
        return None


class Ancestry:
    """Whether the checkout of the-way holds a version: the answer of `git merge-base
    --is-ancestor`, asked of the checkout the key `repository` under `the-way` names.
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
                return None, (
                    "the version lacks the fix in a shallow clone of the-way, which may "
                    "lack its history"
                )
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

    def differs(self, earlier: str, later: str, paths: tuple[str, ...]) -> bool:
        """Whether the files at `paths` differ between two full commit hashes of the-way, by
        `git diff --quiet`: exit 1, or any failure, counts as changed."""
        try:
            return self.git.code("diff", "--quiet", earlier, later, "--", *paths) != 0
        except GitError:
            return True


def counted(count: int, refused: int) -> str:
    """A count as a cell: exact where no refused row belongs to it, `at least n` where some does."""
    return f"at least {count}" if refused else str(count)


@dataclass
class Analysis:
    """The tables the register adds to the result, as rows of text; the values it leaves unknown
    as (repository, record, value, why) (`unknown`), and the values the register holds back, its
    refused rows and problems whose cycle is not read (`held`); both go into the pairs of
    *Unknown values* alike."""

    cycle_rows: list[list[str]]
    fixed_rows: list[list[str]]
    open_rows: list[list[str]]
    dropped_rows: list[list[str]]
    cost_rows: list[list[str]]
    unknown: list[tuple[str, str, str, str]]
    held: list[tuple[str, str, str, str]]


@dataclass
class Placed:
    """The register's problems placed in the cycles the reads found: each problem with its cycle
    (None where it has none), the values the register holds back, the problems per cycle by class
    and weight, and for each cycle the problems that count in none of them (`uncounted`)."""

    found: list[tuple[Problem, Cycle | None]]
    held: list[tuple[str, str, str, str]]
    counts: dict[tuple[str, str], Counter]
    uncounted: Counter


def cycles_by_record(
    cycles: list[Cycle],
) -> tuple[dict[tuple[str, str], Cycle], dict[tuple[str, str], list[Cycle]]]:
    """The cycle each commit that adds a copy of a record names, and apart the commits that add the
    copies of several cycles, with those cycles."""
    # Each commit that adds a copy of a record, with the cycles whose copy it adds: one commit may
    # add the records of several cycles, and then it names none of them.
    owners: dict[tuple[str, str], list[Cycle]] = {}
    for cycle in cycles:
        for record in dict.fromkeys([cycle.record, *cycle.later]):
            owners.setdefault((cycle.repository, record), []).append(cycle)
    index = {key: found[0] for key, found in owners.items() if len(found) == 1}
    shared = {key: found for key, found in owners.items() if len(found) > 1}
    return index, shared


def place_problems(
    register: Register,
    index: dict[tuple[str, str], Cycle],
    shared: dict[tuple[str, str], list[Cycle]],
) -> Placed:
    """Place each problem of the register in the cycle its *Record* names, and count it there by
    class and weight; one whose cycle is not read is held back with its reason."""
    # The problems of a *Record* that names several cycles count in none of them, so the counts of
    # each of those cycles read `at least n`.
    uncounted: Counter = Counter()
    found = [
        (problem, index.get((problem.repository, problem.record))) for problem in register.problems
    ]
    # The values the register holds back are its refused rows and the problems whose cycle is not
    # read; every unknown value, those included, is grouped by field and reason in `unknown_rows`.
    held = list(register.refused)
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
            why = (
                "its Record is a commit that adds the records of more than one cycle, so the "
                "cycle it belongs to is not known"
            )
        else:
            why = (
                "no named repository holds the cycle of its record; name its key with --repository"
            )
        held.append(
            (
                problem.repository[:TEXT_CAP],
                problem.record,
                f"row {problem.number} of `Problems`",
                why,
            )
        )
    return Placed(found, held, counts, uncounted)


def count_refused_rows(
    register: Register,
    index: dict[tuple[str, str], Cycle],
    shared: dict[tuple[str, str], list[Cycle]],
    uncounted: Counter,
) -> tuple[Counter, Counter]:
    """The refused rows of *Problems* that belong to each cycle and to each issue, as (per cycle,
    per issue); a row that names a commit that adds the records of several cycles adds to the
    `uncounted` of each of them."""
    # A refused row belongs to the cycle its Repository and Record name, and to the issue its Issue
    # names, when each is usable; a row with neither stays in *Unknown values* only. Its count shows
    # as `at least n`, since the row's own figure is not in the count.
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
    return refused_cycle, refused_issue


def problems_by_cycle(
    cycles: list[Cycle], register: Register, placed: Placed, refused_cycle: Counter
) -> list[list[str]]:
    """The rows of the table of the problems per cycle: a row for each class the cycle has problems
    of, and one row `none` where it has none."""
    rows = []
    for cycle in cycles:
        key = (cycle.repository, cycle.record)
        mine = placed.counts.get(key, Counter())
        refused = refused_cycle[key]
        partial = refused + placed.uncounted[key]
        head = [cycle.repository, cycle.record]
        rows_here = []
        for cls in register.classes:
            tally = [mine[(cls, weight)] for weight in LEVELS]
            if any(tally):
                rows_here.append(
                    head + [cls] + [counted(count, partial) for count in tally] + [str(refused)]
                )
        if not rows_here:
            rows_here.append(head + [NONE] + [counted(0, partial)] * 4 + [str(refused)])
        rows += rows_here
    return rows


def fixed_issue_row(
    name: str,
    fix: str,
    members: list[tuple[Problem, Cycle | None]],
    refused: int,
    ancestry: Ancestry,
    unknown: list[tuple[str, str, str, str]],
) -> list[str]:
    """The row of a fixed issue: its problems in the cycles whose pin holds the fix, in those whose
    pin lacks it, in those whose pin is unknown and in the cycles not read; each answer that is
    unknown is added to `unknown` with its reason."""
    not_read = sum(1 for _, cycle in members if cycle is None)
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
    shown = (
        ["unknown", "unknown"]
        if fixed is None
        else [counted(holding, refused), counted(lacking, refused)]
    )
    return (
        [name, fix]
        + shown
        + [counted(pin_unknown, refused), counted(not_read, refused), str(refused)]
    )


def unknown_waiting(name: str, why: str, unknown: list[tuple[str, str, str, str]]) -> str:
    """The days an open issue has waited where they are not known: `unknown`, with the reason added
    to `unknown`."""
    unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`", why))
    return UNKNOWN


def waiting_days(
    name: str,
    members: list[tuple[Problem, Cycle | None]],
    refused: int,
    today: date,
    unknown: list[tuple[str, str, str, str]],
) -> str:
    """The days an open issue has waited, from the earliest commit date of the copies its problems'
    *Record* names to the day of the run; `—` where it has no problem yet, and `unknown`, with its
    reason in `unknown`, where the days are not known."""
    not_read = sum(1 for _, cycle in members if cycle is None)
    # Each problem waits from the copy its Record names, which after a correction may be
    # a later copy than the cycle's first.
    dates = [
        cycle.copies.get(problem.record, cycle.committed)
        for problem, cycle in members
        if cycle is not None
    ]
    if refused:
        return unknown_waiting(
            name, "some of its problem rows are refused, so its waiting is not known", unknown
        )
    if not members:
        return "—"
    if not_read:
        return unknown_waiting(
            name,
            "a problem's cycle is not known, so the day it came back first is not known",
            unknown,
        )
    if UNKNOWN in dates:
        return unknown_waiting(
            name, "the commit date of the copy one of its problems names is unknown", unknown
        )
    waited = (today - date.fromisoformat(min(dates))).days
    if waited < 0:
        return unknown_waiting(name, "its earliest copy is dated after the day of the run", unknown)
    return str(waited)


def open_issue_row(
    name: str,
    members: list[tuple[Problem, Cycle | None]],
    refused: int,
    today: date,
    unknown: list[tuple[str, str, str, str]],
) -> list[str]:
    """The row of an open issue: the cycles its problems came back in, its problems, those whose
    cycle is not read and the days it has waited."""
    hit = {(cycle.repository, cycle.record): cycle for _, cycle in members if cycle is not None}
    not_read = sum(1 for _, cycle in members if cycle is None)
    days = waiting_days(name, members, refused, today, unknown)
    # The problem stands in the first cycle it is found in and comes back in each other
    # cycle, so the count is the cycles that hold it less one, whichever of them is first.
    # A refused row or a problem of an unread cycle may belong to a cycle not counted
    # here, so the count is a lower bound then: at least the known cycles less one.
    came_back = max(len(hit) - 1, 0)
    return [
        name,
        counted(came_back, refused + not_read),
        counted(len(members), refused),
        counted(not_read, refused),
        days,
        str(refused),
    ]


def dropped_issue_row(
    name: str, members: list[tuple[Problem, Cycle | None]], refused: int
) -> list[str]:
    """The row of a dropped issue: its cycles, its problems and those whose cycle is not read."""
    hit = {(cycle.repository, cycle.record): cycle for _, cycle in members if cycle is not None}
    not_read = sum(1 for _, cycle in members if cycle is None)
    return [
        name,
        counted(len(hit), refused),
        counted(len(members), refused),
        counted(not_read, refused),
        str(refused),
    ]


def analyse(reads: list[Read], register: Register, ancestry: Ancestry, today: date) -> Analysis:
    """Count the register's problems against the cycles the reads found: per cycle by class and
    weight, per fixed issue by whether the pin of its cycles holds the fix, and
    per open issue the cycles it came back in and the days it has waited."""
    cycles = [cycle for read in reads for cycle in read.cycles]
    index, shared = cycles_by_record(cycles)
    placed = place_problems(register, index, shared)
    refused_cycle, refused_issue = count_refused_rows(register, index, shared, placed.uncounted)
    cycle_rows = problems_by_cycle(cycles, register, placed, refused_cycle)
    # The problems of each issue, gathered once rather than by a scan of every problem per issue.
    by_issue: dict[str, list[tuple[Problem, Cycle | None]]] = {}
    for problem, cycle in placed.found:
        by_issue.setdefault(problem.issue, []).append((problem, cycle))
    unknown: list[tuple[str, str, str, str]] = []
    fixed_rows, open_rows, dropped_rows, cost_rows = [], [], [], []
    for name, fate, fix in register.issues:
        members = by_issue.get(name, [])
        refused = refused_issue[name]
        # The cost of an occurrence stands in the problem's row, so the cycle is not needed: a
        # problem of a cycle that is not read is counted, and a refused row makes the count a lower
        # bound.
        levels = Counter(problem.cost for problem, _ in members)
        cost_rows.append(
            [name, fate]
            + [counted(levels[level], refused) for level in COST_LEVELS]
            + [str(refused)]
        )
        if fate == FIXED:
            fixed_rows.append(fixed_issue_row(name, fix, members, refused, ancestry, unknown))
        elif fate == "open":
            open_rows.append(open_issue_row(name, members, refused, today, unknown))
        else:
            dropped_rows.append(dropped_issue_row(name, members, refused))
    return Analysis(
        cycle_rows,
        fixed_rows,
        open_rows,
        dropped_rows,
        cost_rows,
        list(dict.fromkeys(unknown)),
        list(dict.fromkeys(placed.held)),
    )


def unknown_field(value: str) -> str:
    """The field of an unknown value: the value with the number of its row, the name of its issue
    and the commit of its version taken out, so that the values of one kind make one pair."""
    value = ROW_NUMBER.sub("row of ", value, count=1)
    value = ISSUE_VALUE.sub(r"\1 of an issue", value, count=1)
    return VERSION_SUFFIX.sub("a version", value, count=1)


def unknown_rows(unknown: list[tuple[str, str, str, str]]) -> list[list[str]]:
    """The unknown values as one row for each pair of a field and a reason, in the order each pair
    first occurs: the count is the values of the pair, and the examples are the first EXAMPLES of
    them, each as repository, record and value."""
    counts: Counter = Counter()
    examples: dict[tuple[str, str], list[str]] = {}
    for repository, record, value, why in unknown:
        key = (unknown_field(value), why)
        counts[key] += 1
        shown = examples.setdefault(key, [])
        if len(shown) < EXAMPLES:
            shown.append(f"{repository} {record}: {value}")
    return [
        [field_text, str(counts[(field_text, why)]), why, "; ".join(examples[(field_text, why)])]
        for field_text, why in counts
    ]


# The process versions (WAY-339)


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
    # The two kinds of series of the process versions (WAY-339): the series of the cost, the
    # median cost and Q3 are compared in; and the series of the count of remarks, Q1 and Q2 are
    # compared in, which ends wherever a series of the cost ends and at more changes.
    cost: list[Series] = field(default_factory=list)
    count: list[Series] = field(default_factory=list)
    no_version: list[Cycle] = field(default_factory=list)
    unknown: list[tuple[str, str, str, str]] = field(default_factory=list)
    # Every version, in the order of their dates: the series of the measures are made of them.
    ordered: list[Version] = field(default_factory=list)


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


FIRST_VERSION = "the first version of the result"


def changed_paths(
    ancestry: Ancestry, earlier: str, later: str, paths: tuple[str, ...]
) -> list[str]:
    """The paths of `paths` whose files differ between two full commit hashes of the-way, none
    where no file does: `git diff --quiet` of each, a failure counting as changed, so that a series
    is never joined by mistake (WAY-339)."""
    if not ancestry.differs(earlier, later, paths):
        return []
    return [path for path in paths if ancestry.differs(earlier, later, (path,))] or list(paths)


def names_of(paths: list[str]) -> str:
    return " and ".join(f"`{path}`" for path in paths)


def changed_reason(
    ancestry: Ancestry, earlier: str, later: str, paths: tuple[str, ...]
) -> str | None:
    """None where the files at `paths` do not differ between two full commit hashes of the-way,
    else a reason that names the paths that changed (WAY-339)."""
    changed = changed_paths(ancestry, earlier, later, paths)
    return f"{names_of(changed)} changed between the two versions" if changed else None


# A cycle that changed the tool that wrote a file of its copy (WAY-339)


def withdraw_values(cycle: Cycle, file: str, reason: str) -> None:
    """Give the values the tool that wrote `file` measured as unknown, with the reason, in place of
    what the file gave and of the reasons and the missing fields of its reading: the file is not
    read for this cycle. The number of fix rounds stands, since the record gives it, not the
    script."""
    if file == STAGES_FILE:
        cycle.working = cycle.waiting = cycle.cost = cycle.share = None
        names = STAGES_VALUES
        cycle.missing = []
    elif file == MEASURES_FILE:
        cycle.measures = {}
        names = ("Mechanism measures",)
        cycle.unknown = [pair for pair in cycle.unknown if pair[0] not in MEASURE_LABELS]
        cycle.missing_in = [pair for pair in cycle.missing_in if pair[0] != MEASURES_FILE]
    else:
        cycle.gate_runs, cycle.gate_timed = [], []
        names = ("Gate runs",)
        cycle.unknown = [pair for pair in cycle.unknown if not pair[0].startswith("Gate runs")]
        cycle.missing_in = [pair for pair in cycle.missing_in if pair[0] != GATE_FILE]
    cycle.unknown = [pair for pair in cycle.unknown if pair[0] not in names]
    cycle.unknown += [(name, reason) for name in names]


def note_changed_tools(reads: list[Read], ancestry: Ancestry) -> None:
    """For each cycle of the-way, give as unknown the values of each file of its copy whose tool
    the cycle's own change changed (WAY-339): the files of the tool differ between the version the
    cycle ran on and the commit of the last copy of its record in the-way's own history, by `git
    diff --quiet`, a failure counting as changed. Only a cycle of the-way is read so: the change of
    a cycle of another repository lies in that repository, which holds none of these tools, and its
    copy is not a commit of the-way's history. A cycle whose version does not resolve, and a copy
    that holds no such file, which is of an earlier form, are left as they are."""
    for read in reads:
        if read.key != THE_WAY:
            continue
        for cycle in read.cycles:
            version = ancestry.commit(cycle.pin)[0] if cycle.pin is not None else None
            if version is None:
                continue
            last = cycle.later[-1] if cycle.later else cycle.record
            for file, paths in TOOL_GROUPS:
                changed = (
                    changed_paths(ancestry, version, last, paths) if file in cycle.held else []
                )
                if changed:
                    withdraw_values(
                        cycle,
                        file,
                        f"the cycle changed the tool that wrote them: "
                        f"{names_of(changed)} changed between the "
                        f"version it ran on and the last copy of its "
                        f"record",
                    )


def cost_boundary(earlier: Version, later: Version, ancestry: Ancestry) -> str | None:
    """Why a new series of the cost begins at `later`, or None where both versions share one: a
    new price list, or a change of the script that measures the cost, and nothing else."""
    if earlier.price != later.price:
        return "the price list changed"
    return changed_reason(ancestry, earlier.commit, later.commit, COST_SCRIPTS)


def count_boundary(
    earlier: Version, later: Version, register: Register, ancestry: Ancestry
) -> str | None:
    """Why a new series of the count of remarks begins at `later`, or None where both versions
    share one: wherever a series of the cost begins, and at a date of the register's list of
    classes or a change of the files that give the form of a stage report or the reviewer's
    instructions."""
    why = cost_boundary(earlier, later, ancestry)
    if why is not None:
        return why
    if register.class_dates_unknown:
        return "the register's list of classes is not given in full, so it may have changed"
    # A date on the day of either version counts: the test errs toward more series.
    at = bisect.bisect_left(register.class_dates, earlier.day)
    if at < len(register.class_dates) and register.class_dates[at] <= later.day:
        return "the register's list of classes changed between the two versions"
    return changed_reason(ancestry, earlier.commit, later.commit, COUNT_PATHS)


def split_series(versions: list[Version], boundary) -> list[Series]:
    """Split the versions, in the order of their dates, into runs: a new one begins at a version
    for which `boundary(previous version, version)` gives a reason, which the series keeps."""
    blocks: list[Series] = []
    for number, version in enumerate(versions):
        why = boundary(versions[number - 1], version) if number else None
        if why is None and blocks:
            blocks[-1].versions.append(version)
        else:
            blocks.append(Series(why or FIRST_VERSION, [version]))
    return blocks


def instrument_series(
    versions: list[Version], ancestry: Ancestry, scripts: tuple[str, ...]
) -> list[Series]:
    """Split the versions, in the order of their dates, into series by the change of the scripts
    alone: a series begins at a version whose files at `scripts` differ from the previous
    version's (WAY-339), and its reason names the scripts that changed. Nothing else splits it:
    not the price list, the register's list of classes or the files of the count of remarks."""
    return split_series(
        versions,
        lambda earlier, later: changed_reason(ancestry, earlier.commit, later.commit, scripts),
    )


@dataclass
class MeasureVersions:
    """The series of the mechanism measures and of the gate times, each with its rows, and the
    answers of *Falls* that are unknown as (repository, record, value, why)."""

    mechanism: list[Series] = field(default_factory=list)
    gate: list[Series] = field(default_factory=list)
    unknown: list[tuple[str, str, str, str]] = field(default_factory=list)


NO_MEASURE = "—"  # the measure cell of the one row of a version that gives no value


def median_text(median: Decimal | None, suffix: str = "") -> str:
    """A median as the exact value of its Decimal, a half with its decimal, never in exponent
    form."""
    return UNKNOWN if median is None else format(median, "f") + suffix


def falls_answer(
    version: Version,
    first: bool,
    median: Decimal | None,
    previous: Decimal | None,
    subject: str,
    rest: str,
    what: str,
    unknown: list[tuple[str, str, str, str]],
    name: str,
) -> str:
    """`yes` where the median is lower than the previous version's of the same measure in the same
    series, `no` where it is not, and `unknown`, with its reason kept in `unknown`, where the
    version is the first of its series or either median is not known."""
    if first:
        why = "no previous version in the series"
    elif median is None:
        why = f"no {subject} of the version{rest} gives {what}, so its median is not known"
    elif previous is None:
        why = f"no {subject} of the previous version{rest} gives {what}"
    else:
        return "yes" if median < previous else "no"
    unknown.append((THE_WAY, NONE, f"{name}, version {version.commit}", why))
    return UNKNOWN


def measure_number(label: str, text: str) -> Decimal:
    """The value of a cycle-level line that `read_measures` kept: a whole number, or for the share
    a number of percent with one decimal."""
    return Decimal(text[:-1] if label == SHARE_LABEL else text)


def mechanism_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the mechanism measures: for each version and each cycle-level
    measure, the median of the cycles that give a value and whether it falls."""
    previous: dict[str, Decimal | None] = {}
    for index, version in enumerate(block.versions):
        medians: dict[str, Decimal | None] = {}
        if not any(label in cycle.measures for cycle in version.cycles for label in MEASURE_LABELS):
            # A version no cycle of which gives a value has one row and one line of reason.
            block.rows.append([version.commit, NO_MEASURE, "0", UNKNOWN, UNKNOWN])
            unknown.append(
                (
                    THE_WAY,
                    NONE,
                    f"Mechanism measures of version {version.commit}",
                    "no cycle of this version gives a value: its copies hold no "
                    f"`{MEASURES_FILE}` (an earlier cycle, or a script that failed; the "
                    "record's *Verification* says which) or give none",
                )
            )
            previous = {}
            continue
        for label in MEASURE_LABELS:
            values = [
                measure_number(label, cycle.measures[label])
                for cycle in version.cycles
                if label in cycle.measures
            ]
            median = median_of(values)
            medians[label] = median
            falls = falls_answer(
                version,
                index == 0,
                median,
                previous.get(label),
                "cycle",
                "",
                "a value",
                unknown,
                f"Measure falls: {label}",
            )
            block.rows.append(
                [
                    version.commit,
                    label,
                    str(len(values)),
                    median_text(median, "%" if label == SHARE_LABEL else ""),
                    falls,
                ]
            )
        previous = medians


def gate_values(version: Version) -> dict[str, tuple[list[Decimal], list[Decimal]]]:
    """The times of the runs of a version, over all its cycles, by measure: the total first and
    then each directory that any run has, by name. Each measure holds the values of the runs that
    passed with no other gate and apart those of the runs not compared: with another gate, with an
    unknown count, that failed or whose exit code is unknown; a run that does not give the time
    adds to neither (WAY-350)."""
    found: dict[str, tuple[list[Decimal], list[Decimal]]] = {TOTAL_MEASURE: ([], [])}
    for cycle in version.cycles:
        for run in cycle.gate_timed:
            side = 0 if run.others == 0 and run.code == 0 else 1
            if run.total is not None:
                found[TOTAL_MEASURE][side].append(run.total)
            for name, seconds in run.directories:
                lists = found.setdefault(DIRECTORY_MEASURE + name, ([], []))
                if seconds is not None:
                    lists[side].append(seconds)
    return {name: found[name] for name in [TOTAL_MEASURE, *sorted(found.keys() - {TOTAL_MEASURE})]}


def gate_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the gate times: for each version and each measure, the median of the
    runs that passed with no other gate and whether it falls, and the runs not compared apart,
    never compared (WAY-350). A version no run of which gives a time has one row and one line of
    reason."""
    previous: dict[str, Decimal | None] = {}
    for index, version in enumerate(block.versions):
        medians: dict[str, Decimal | None] = {}
        values = gate_values(version)
        if all(not alone and not apart for alone, apart in values.values()):
            block.rows.append([version.commit, NO_MEASURE, "0", UNKNOWN, UNKNOWN, "0", UNKNOWN])
            unknown.append(
                (
                    THE_WAY,
                    NONE,
                    f"Gate times of version {version.commit}",
                    "no run of this version gives a time: its copies hold no "
                    f"`{GATE_FILE}` ({ABSENCE_CAUSES[GATE_FILE]}; the "
                    "record's *Verification* says which) or give none",
                )
            )
            previous = {}
            continue
        for name, (alone, apart) in values.items():
            median = median_of(alone)
            medians[name] = median
            falls = falls_answer(
                version,
                index == 0,
                median,
                previous.get(name),
                "run",
                " that passed with no other gate",
                "this time",
                unknown,
                f"Gate time falls: {name}",
            )
            block.rows.append(
                [
                    version.commit,
                    name,
                    str(len(alone)),
                    median_text(median),
                    falls,
                    str(len(apart)),
                    median_text(median_of(apart)),
                ]
            )
        previous = medians


def measure_versions(versions: Versions, ancestry: Ancestry) -> MeasureVersions:
    """Group the versions into the series of each instrument and give the medians and the
    comparison of each version within its own series (WAY-339, WAY-350)."""
    result = MeasureVersions()
    result.mechanism = instrument_series(versions.ordered, ancestry, (MEASURES_SCRIPT,))
    result.gate = instrument_series(versions.ordered, ancestry, GATE_SCRIPTS)
    for block in result.mechanism:
        mechanism_rows(block, result.unknown)
    for block in result.gate:
        gate_rows(block, result.unknown)
    return result


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
    read = [
        cycle
        for cycle in planned_cycles
        if cycle.planned is not None and cycle.too_large is not None
    ]
    plans_read = f"{len(read)} of {len(planned_cycles)}"
    if not read:
        return plans_read, "unknown", "no cycle's plan can be read"
    if len(read) < len(planned_cycles):
        return (
            plans_read,
            "unknown",
            (
                f"the plans of {len(planned_cycles) - len(read)} cycle(s) "
                "are not read, so the share of the version's slices is "
                "not known"
            ),
        )
    planned = sum(cycle.planned for cycle in read if cycle.planned is not None)
    large = sum(cycle.too_large for cycle in read if cycle.too_large is not None)
    if planned == 0:
        return plans_read, "unknown", "the plans that are read hold no slice"
    return plans_read, ("yes" if 3 * large > planned else "no"), None


def process_versions(
    reads: list[Read], register: Register, ancestry: Ancestry, prices: Prices
) -> Versions:
    """Group the cycles by their version, split the versions into series, and answer the three
    questions of each version within its own series (WAY-339)."""
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
            result.unknown += [
                (cycle.repository, cycle.record, "Process pin", "its version has no readable date")
                for cycle in members
            ]
            continue
        versions.append(Version(commit, stamp or 0, day, prices.date, members))
    versions.sort(key=lambda version: (version.stamp, version.commit))
    result.ordered = versions
    result.count = split_series(
        versions, lambda earlier, later: count_boundary(earlier, later, register, ancestry)
    )
    result.cost = split_series(
        versions, lambda earlier, later: cost_boundary(earlier, later, ancestry)
    )
    for block in result.count:
        count_rows(block, result.unknown)
    for block in result.cost:
        cost_rows(block, result.unknown)
    return result


def count_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the count of remarks: for each version its answers Q1 and Q2, each
    with its reason in `unknown` where it is not known. No number of the cost stands in them."""
    for version in block.versions:
        answer1, why1 = contradiction_of(version)
        plans, answer2, why2 = too_large_of(version)
        for label, why in (("contradiction only after code", why1), ("slices too large", why2)):
            if why:
                unknown.append((THE_WAY, NONE, f"{label}, version {version.commit}", why))
        block.rows.append(
            [version.commit, version.day, str(len(version.cycles)), answer1, plans, answer2]
        )


def cost_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the cost: for each version the median cost of its cycles with a
    known cost, and Q3, whether it is lower than the previous version's of the same series."""
    previous: Version | None = None
    previous_median: Decimal | None = None
    for version in block.versions:
        costs = [cycle.cost for cycle in version.cycles if cycle.cost is not None]
        median = median_of(costs)
        if previous is None:
            answer3, why3 = "unknown", "no previous version in the series"
        elif median is None or previous_median is None:
            answer3, why3 = "unknown", "a median cost is not known"
        else:
            answer3 = "yes" if median < previous_median else "no"
            why3 = None
        if why3:
            unknown.append((THE_WAY, NONE, f"cost falls, version {version.commit}", why3))
        block.rows.append(
            [
                version.commit,
                version.day,
                str(len(version.cycles)),
                str(len(costs)),
                money(median),
                answer3,
            ]
        )
        previous, previous_median = version, median


def money(value: Decimal | None) -> str:
    return UNKNOWN if value is None else format(value.quantize(MONEY), "f")
