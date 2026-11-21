"""Runs the product's gate for the task cycle, relays its output, and appends the times of the run to
the cycle's record (WAY-350). The script reads the times from the run, so that none is copied
wrongly, and the audit reads a file whose form the script holds.

Usage, from the root of the repository:

    python -B task-cycle/gate_times.py --output PATH [--registry DIR] -- COMMAND [ARG ...]

COMMAND is the gate the product declares, run with no shell in the current directory, its error output
joined to its output. Everything it prints goes to stdout unchanged and as it comes; the script keeps
only the lines it reads for the times. The exit code is the command's own.

The times: the total wall time of the run, in seconds to three decimals; and for each block that
`gate/run_tests.py` opens with a line `== <directory>`, the time of the first line `Ran <n> tests in
<s>s` before the next block, kept as printed, or `unknown` where there is none. Text before the first
block belongs to no directory. A failing test of the gate may print, in its failure message, the
output of a nested run of the runner, whose lines `== <directory>` are no blocks of this run. The
last line `<n> tests in <m> directories; …` of the output is the run's own, each earlier one closes
the output of a nested run; where there is an earlier one and more than `<m>` lines `== ` stand at
the start of a line, the surplus lines are the nested run's, taken from those directly before an
earlier summary line, last to first, each such line taking at most its own `<m>`, or `<m>` less one
where a line that holds `== ` after text stands before exactly `<m>` less one of the lines `== `
that follow it up to the summary line: the nested run's first directory stands after text there. A
block that holds an earlier summary line takes the first `Ran` line after the last of them. A run
with no earlier summary line is read as above. The numbers of a `Ran` line and of a summary line are
ASCII digits, at most nine before a point and nine after it; a line with more or other digits is no
such line. A run lists at most 50 directories, the number the audit reads, and a directory cell is
cut at 200 characters, ending in `…` where cut; the directories after the fiftieth are not listed,
and a last row of the run says how many (`… <n> more directories not listed`, with `—` for its
seconds), so that the record stays small and no cut is read as a time. The memory the script keeps
stays bounded whatever the output holds: it keeps the first 100 lines `== ` and the last 100 summary
lines that stand after one, and, in the whole output, the last 100 different places of lines that
hold `== ` after text, each place once.

The runs at the same time: each run makes an empty file in the registry (default `~/.the-way/gate_runs`)
named `<start ms>_running_<token>.run` and renames it on its end to `<start ms>_<end ms>_<token>.run`.
The other runs counted are those whose interval met this run's: an ended one that started before this
run ended and ended after it started; a running one that started before this run ended and no more
than six hours before it. Ended runs over a day old and running runs over six hours old are deleted at
the start of a run. A file whose time cannot be (an end or a start more than a minute after the
present, or an end before its start) is deleted at the start of a run as well and counted for nothing,
so that one damaged or hand-made file cannot count as another run for ever. A name of another form is
left alone and counted for nothing. Where the registry cannot be made or listed, a `Warning:` goes to stderr and the count is `unknown`.

The record is Markdown in UTF-8 with LF line ends, appended to PATH. Where PATH is missing or empty, its
heading and table header are written first.

Exit code: the command's own; a command killed by a signal gives 128 plus the signal number. Exit code
2 with a first line `Error: gate_times.py: ...` on stderr for the script's own failures: no command, no
--output, a PATH that cannot be appended to (all found before the command starts), a command that cannot
be started, or a record that cannot be written.

Standard library only.
"""

from __future__ import annotations

import argparse
import os
import re
import secrets
import subprocess
import sys
import time
import unicodedata
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

HOUR_MS = 3600 * 1000
DAY_MS = 24 * HOUR_MS
RUNNING_LIMIT_MS = 6 * HOUR_MS
CLOCK_SLACK_MS = 60 * 1000  # a time this far after the present is still a clock's difference
CHUNK = 65536
LINE_LIMIT = (
    1 << 20
)  # a line is read for the times up to this many bytes, so that memory stays bounded
MAX_DIRECTORIES = 50  # the audit lists no more directories of a run
DIRECTORY_CAP = 200  # the audit keeps no more characters of a directory
PIECES_KEPT = 2 * MAX_DIRECTORIES  # the lines `== ` kept, so that nested ones can be left out of 50
SUMMARIES_KEPT = 100  # the summary lines kept for the lines `== ` before them
UNKNOWN = "unknown"
NONE = "—"
BLOCK = "== "
RAN = re.compile(r"Ran [0-9]{1,9} tests? in ([0-9]{1,9}(?:\.[0-9]{1,9})?)s")
# The last line of the runner: the tests and directories it counts, and whether every one passed.
SUMMARY = re.compile(
    r"[0-9]{1,9} tests in ([0-9]{1,9}) directories; (?:every directory passed|failed: .*)"
)
RUNNING = re.compile(r"(\d+)_running_([A-Za-z0-9]+)\.run")
ENDED = re.compile(r"(\d+)_(\d+)_([A-Za-z0-9]+)\.run")

HEADING = "# Gate runs of the cycle"
NOTE = "Each row is one run by this script; times are seconds."
TABLE_HEADER = (
    "| Started (UTC) | Exit code | Total seconds | Other gate runs at the same time "
    "| Directory | Directory seconds |"
)
TABLE_RULE = "| --- | --- | --- | --- | --- | --- |"


class GateError(Exception):
    """A failure of the script itself, found before or after the command runs."""


class Parser(argparse.ArgumentParser):
    """Raises the parser's complaints as GateError, so that they get the script's own form."""

    def error(self, message: str) -> None:
        raise GateError(message)


def parse(argv: list[str]) -> tuple[Path, Path | None, list[str]]:
    """The output, the registry given (or None for the default) and the command, checked before the
    command is started."""
    if "--" in argv:
        split = argv.index("--")
        options, command = argv[:split], argv[split + 1 :]
    else:
        options, command = argv, []
    parser = Parser(prog="gate_times.py", description="Run the gate and record its times.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--registry", type=Path)
    arguments = parser.parse_args(options)
    if not command:
        raise GateError("no command; name the gate after --")
    if arguments.output is None:
        raise GateError("no --output PATH")
    try:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        with arguments.output.open("ab"):
            pass
    except OSError as error:
        raise GateError(f"cannot append to {arguments.output}: {error}") from error
    return arguments.output, arguments.registry, command


def warn(message: str) -> None:
    print(f"Warning: gate_times.py: {message}", file=sys.stderr)


def now_ms() -> int:
    return time.time_ns() // 1_000_000


def stamp(ms: int) -> str:
    """A time in milliseconds since the epoch as `YYYY-MM-DD HH:MM:SS.mmm` in UTC."""
    moment = datetime.fromtimestamp(ms // 1000, tz=timezone.utc)
    return f"{moment:%Y-%m-%d %H:%M:%S}.{ms % 1000:03d}"


def cell(text: str) -> str:
    """Text from a gate's output on one line, with each bar and control character replaced, so that
    it cannot break the table."""
    cleaned = "".join(" " if unicodedata.category(char).startswith("C") else char for char in text)
    return " ".join(cleaned.split()).replace("|", "/")


def cut(text: str) -> str:
    """The text as it is, or cut to DIRECTORY_CAP characters ending in `…`."""
    return text if len(text) <= DIRECTORY_CAP else text[: DIRECTORY_CAP - 1] + "…"


class Piece:
    """The text of one line `== <directory>` at the start of a line, up to the next such line: the
    directory as the record shows it, and what the text gives of its time."""

    def __init__(self, directory: str) -> None:
        self.directory = directory
        self.own: str | None = None  # the first `Ran` line of the text, as printed
        self.holds = False  # the text holds a summary line that is not the last of the run
        self.after: str | None = None  # the first `Ran` line after the last such summary line


class Times:
    """The blocks of the gate's output and the time each block gives, read line by line.

    A line `== <directory>` at the start of a line may be the nested run's, a run of the runner that
    a failing test printed in its failure message; whether it is, the last summary line of the output
    tells, so the lines are kept as pieces and the blocks are settled by `result` at the end. Of the
    pieces only the first PIECES_KEPT are kept, and of the summary lines only the last SUMMARIES_KEPT
    that stand after a piece, so that memory stays bounded whatever the output holds."""

    def __init__(self) -> None:
        self.pieces: list[Piece] = []
        self.count = 0  # the lines `== ` at the start of a line, kept or not
        self.current: Piece | None = None  # the piece the lines now read belong to, if kept
        self.segment = 0  # the number of those lines before the latest summary line
        # The summary lines read, each as (index of the first piece line after the one before it,
        # number of piece lines since, its number of directories, whether a line that holds `== `
        # after text stands before exactly one piece line fewer than that number). The latest is
        # the run's own until another comes.
        self.latest: tuple[int, int, int, bool] | None = None
        self.earlier: deque[tuple[int, int, int, bool]] = deque(maxlen=SUMMARIES_KEPT)
        # The number of piece lines when each of the last lines that holds `== ` after text was
        # read, each number once.
        self.marks: deque[int] = deque(maxlen=SUMMARIES_KEPT)
        self.pending: Piece | None = None  # the piece that holds the latest summary line
        self.pending_after: str | None = None  # the first `Ran` line after it, in that piece
        self.waiting = False  # whether that line is still to come

    def line(self, raw: bytes) -> None:
        text = raw.rstrip(b"\r").decode("utf-8", errors="replace")
        if text.startswith(BLOCK):
            self.open(text[len(BLOCK) :])
            return
        if BLOCK in text and (not self.marks or self.marks[-1] != self.count):
            self.marks.append(self.count)
        text = text.rstrip()
        summary = SUMMARY.fullmatch(text)
        if summary:
            self.summarise(int(summary.group(1)))
            return
        matched = RAN.fullmatch(text)
        if matched and self.current is not None:
            if self.current.own is None:
                self.current.own = matched.group(1)
            if self.waiting:
                self.waiting = False
                self.pending_after = matched.group(1)

    def open(self, directory: str) -> None:
        self.waiting = False
        self.count += 1
        if len(self.pieces) < PIECES_KEPT:
            self.current = Piece(cut(cell(directory)))
            self.pieces.append(self.current)
        else:
            self.current = None

    def summarise(self, directories: int) -> None:
        """A summary line: the one before it, if any, is no longer the last, so its piece holds it."""
        if self.pending is not None:
            self.pending.holds = True
            self.pending.after = self.pending_after
        if self.latest is not None and self.latest[1] > 0:
            self.earlier.append(self.latest)
        opened = any(self.count - mark == directories - 1 for mark in self.marks)
        self.latest = (self.segment, self.count - self.segment, directories, opened)
        self.segment = self.count
        self.pending = self.current
        self.pending_after = None
        self.waiting = True

    def nested(self) -> list[tuple[int, int]]:
        """The ranges of the lines that are the nested runs': where an earlier summary line stands,
        the lines `== ` beyond the directories of the last summary line are taken from those
        directly before an earlier summary line, last to first, each such line taking no more than
        its own number of directories, less one where a line that holds `== ` after text stands
        before exactly that many lines fewer than the directories: that line is then the nested
        run's first directory, which stands after text and is no line of the kind."""
        if self.latest is None:
            return []
        surplus = self.count - self.latest[2]
        ranges = []
        for first, lines, directories, opened in reversed(self.earlier):
            if surplus <= 0:
                break
            taken = min(lines, directories - 1 if opened else directories, surplus)
            ranges.append((first + lines - taken, first + lines))
            surplus -= taken
        return ranges

    def result(self) -> tuple[list[list[str | None]], int]:
        """The listed blocks, each as [directory, seconds as printed or None], and the number of
        blocks not listed."""
        ranges = self.nested()
        groups: list[list[Piece]] = []
        for index, piece in enumerate(self.pieces):
            if any(first <= index < last for first, last in ranges):
                if groups:
                    groups[-1].append(piece)
            else:
                groups.append([piece])
        blocks = [[group[0].directory, seconds(group)] for group in groups[:MAX_DIRECTORIES]]
        taken = sum(last - first for first, last in ranges)
        return blocks, max(self.count - taken - len(blocks), 0)


def seconds(group: list[Piece]) -> str | None:
    """The time of a block made of the pieces of the group: where it holds a summary line that is
    not the run's last, the first `Ran` line after the last such line, and none from the nested
    run's; otherwise the first `Ran` line of its text."""
    held = [index for index, piece in enumerate(group) if piece.holds]
    if held:
        last = group[held[-1]]
        following = group[held[-1] + 1 :]
        if last.after is not None:
            return last.after
    else:
        following = group
    return next((piece.own for piece in following if piece.own is not None), None)


def relay(stream, sink, on_line) -> None:
    """Copies the stream to the sink as its bytes come, and hands each complete line to `on_line`
    without its line end. An unfinished line is kept only up to LINE_LIMIT bytes."""
    fd = stream.fileno()
    pending = b""
    while True:
        chunk = os.read(fd, CHUNK)
        if not chunk:
            break
        sink.write(chunk)
        sink.flush()
        pieces = chunk.split(b"\n")
        pieces[0] = pending + pieces[0]
        pending = pieces.pop()
        for piece in pieces:
            on_line(piece)
        pending = pending[:LINE_LIMIT]
    if pending:
        on_line(pending)


def parse_name(name: str) -> tuple[int, int | None, str] | None:
    """The start, the end (None while running) and the token of a file; None for another form."""
    running = RUNNING.fullmatch(name)
    if running:
        return int(running.group(1)), None, running.group(2)
    ended = ENDED.fullmatch(name)
    if ended:
        return int(ended.group(1)), int(ended.group(2)), ended.group(3)
    return None


def malformed(start: int, end: int | None, now: int) -> bool:
    """Whether a file has a time that cannot be: a start or an end more than a minute after
    `now`, or an end before its start."""
    if start > now + CLOCK_SLACK_MS:
        return True
    return end is not None and (end > now + CLOCK_SLACK_MS or end < start)


def prepare(folder: Path, now: int) -> bool:
    """Makes the registry and deletes the files that are too old to count; False where it cannot be
    made or listed."""
    try:
        folder.mkdir(parents=True, exist_ok=True)
        for name in os.listdir(folder):
            run = parse_name(name)
            if run is None:
                continue
            start, end, _ = run
            stale = start < now - RUNNING_LIMIT_MS if end is None else end < now - DAY_MS
            if stale or malformed(start, end, now):
                try:
                    (folder / name).unlink()
                except OSError as error:
                    warn(f"cannot delete {name} in the registry: {error}")
    except OSError as error:
        warn(f"cannot use the registry {folder}: {error}")
        return False
    return True


def count_others(folder: Path, token: str, start: int, end: int) -> str:
    """The number of other runs whose interval met this run's, or unknown where the registry cannot
    be listed."""
    try:
        names = os.listdir(folder)
    except OSError as error:
        warn(f"cannot list the registry {folder}: {error}")
        return UNKNOWN
    count = 0
    for name in names:
        run = parse_name(name)
        if run is None or run[2] == token:
            continue
        begin, finish, _ = run
        if malformed(begin, finish, end):
            continue
        if finish is None:
            met = begin < end and begin >= end - RUNNING_LIMIT_MS
        else:
            met = begin < end and finish > start
        if met:
            count += 1
    return str(count)


def record(path: Path, lines: list[str]) -> None:
    """Appends the rows to the record, first its heading and table header where it is missing or
    empty."""
    fresh = path.stat().st_size == 0
    text = "".join(line + "\n" for line in lines)
    if fresh:
        text = f"{HEADING}\n\n{NOTE}\n\n{TABLE_HEADER}\n{TABLE_RULE}\n" + text
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def rows(started: str, code: int, total: str, others: str, times: Times) -> list[str]:
    head = [started, str(code), total, others]
    blocks, not_listed = times.result()
    if not blocks:
        return ["| " + " | ".join(head + [NONE, NONE]) + " |"]
    listed = [[directory, seconds or UNKNOWN] for directory, seconds in blocks]
    if not_listed:
        listed.append([f"… {not_listed} more directories not listed", NONE])
    return ["| " + " | ".join(head + pair) + " |" for pair in listed]


def exit_code(code: int) -> int:
    return code if code >= 0 else 128 - code


def main(argv: list[str] | None = None) -> int:
    try:
        output, registry_option, command = parse(sys.argv[1:] if argv is None else argv)
    except GateError as error:
        print(f"Error: gate_times.py: {error}", file=sys.stderr)
        return 2

    folder: Path | None
    try:
        folder = registry_option or Path.home() / ".the-way" / "gate_runs"
    except RuntimeError as error:
        warn(f"cannot find the home directory for the registry: {error}")
        folder = None
    start = now_ms()
    usable = folder is not None and prepare(folder, start)
    token = secrets.token_hex(8)
    own = None
    if usable:
        own = folder / f"{start}_running_{token}.run"
        try:
            own.open("x").close()
        except OSError as error:
            warn(f"cannot record this run in the registry: {error}")
            own = None

    clock = time.perf_counter()
    try:
        child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except OSError as error:
        if own is not None:
            own.unlink(missing_ok=True)
        print(f"Error: gate_times.py: cannot start {command[0]!r}: {error}", file=sys.stderr)
        return 2
    times = Times()
    relay(child.stdout, sys.stdout.buffer, times.line)
    child.stdout.close()
    code = exit_code(child.wait())
    seconds = time.perf_counter() - clock
    end = now_ms()

    if own is not None:
        try:
            os.replace(own, folder / f"{start}_{end}_{token}.run")
        except OSError as error:
            warn(f"cannot end this run's file in the registry: {error}")
    others = count_others(folder, token, start, end) if usable else UNKNOWN

    try:
        record(output, rows(stamp(start), code, f"{seconds:.3f}", others, times))
    except OSError as error:
        print(f"Error: gate_times.py: cannot append to {output}: {error}", file=sys.stderr)
        return 2
    return code


if __name__ == "__main__":
    sys.exit(main())
