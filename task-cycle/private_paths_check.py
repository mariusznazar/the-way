"""The absolute paths and the note links in the text a task cycle publishes (WAY-309).

Usage:

    python -B task-cycle/private_paths_check.py TARGET

In a product, the path starts with `.the-way/`. TARGET is either the copy of a cycle record, the
directory `docs/task-cycles/<task-slug>/`, or the description file of a request,
`.runs/task-cycles/<task-slug>/request.md`. A directory is read through every file below it; a file
is read alone.

The script lists, with the file and the line, each text of these kinds, found by pattern alone. It
holds no list of words that are private, and it neither judges nor rewrites anything:

- an absolute path on Windows: a single letter, a colon and a slash or a backslash, as `C:\\dir`
  and `C:/dir`, which also covers the home directory `C:\\Users\\<name>`; a letter that ends a word
  (`https:` in a URL, `Note:` in prose) starts none;
- the POSIX form of a drive that some shells and Windows layers show: `/c/dir`, `/mnt/c/dir` and
  `/cygdrive/c/dir`;
- the home directory of a user on Linux and macOS: `/home/<name>` and `/Users/<name>`, and
  `\\Users\\<name>` with a backslash;
- a link to a note, `[[Title]]`, with an alias, a heading or an embed (`![[file]]`) in it. A
  `[[` followed by a space, as in the shell's `[[ -f x ]]`, and a `[[...]]` that holds no letter or
  digit, the form for writing about the link, are no link.

A path or a link inside a code span or a fenced block is listed like any other: a copy of the record
publishes it too. Not listed: a path that starts at `~`, a relative path (`../x`), a UNC path
(`\\\\host\\share`), `/root`, and a name of the user or the machine that stands in plain text.

Each hit is printed on stdout as `<file>:<line>: <kind>: <text>`, in the order of the files (sorted
by their paths) and of the lines, the text being the path up to the next space, quote or bracket
with a closing full stop, comma, colon or semicolon taken off, or the whole link; then a last line,
`checked: ...`. Exit code: 0 when nothing is listed; 1 with the hits listed; 2 with
`Error: <message>` on stderr when the argument is wrong or a file cannot be read as UTF-8. A file
with a NUL byte near its start is binary and is not read; the last line counts such files. The
script writes no file and runs nothing.

Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Where an absolute path may start: not inside a word, a URL or a longer path.
WINDOWS_DRIVE = r"(?<!\w)[A-Za-z]:[\\/]"
POSIX_DRIVE = r"(?<![\w.~/\\:-])(?:/mnt|/cygdrive)?/[A-Za-z]/(?=[\w.~-])"
HOME_DIRECTORY = r"(?<![\w.~/\\-])(?:/home|[\\/]Users)[\\/][\w.-]+"
# What a path runs through after its start, for showing it: up to a space, a quote or a bracket.
PATH_TAIL = r"""[^\s"'`<>|*?()\[\]{}]*"""
# `[[` followed by a first character that is no space, a letter or digit somewhere inside, and
# no line end before the closing `]]`.
NOTE_LINK = r"\[\[(?=[^\s\]])(?=[^\]\n]*[^\W_])[^\]\n]+\]\]"

FINDING = re.compile(
    r"(?P<path>(?:" + "|".join((WINDOWS_DRIVE, POSIX_DRIVE, HOME_DIRECTORY)) + r")" + PATH_TAIL
    + r")|(?P<link>" + NOTE_LINK + r")")
LINE_END = re.compile(r"\r\n|\r|\n")
BINARY_PROBE = 8192
KIND_PATH = "absolute path"
KIND_LINK = "note link"


class PrivatePathsError(Exception):
    """An argument that is wrong or a file that cannot be read."""


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise PrivatePathsError(message)


def display(value: object) -> str:
    """Keep text taken from the files inside one report line."""
    return "".join(char if char.isprintable() else ascii(char)[1:-1] for char in str(value))


@dataclass
class Result:
    listed: list[tuple[str, int, str, str]] = field(default_factory=list)
    files: int = 0
    binary: int = 0


def find_in_text(text: str) -> list[tuple[int, str, str]]:
    """Each hit of a text as its line number, kind and shown text."""
    hits = []
    for number, line in enumerate(LINE_END.split(text), start=1):
        for match in FINDING.finditer(line):
            if match.group("path") is not None:
                hits.append((number, KIND_PATH, match.group("path").rstrip(".,;:")))
            else:
                hits.append((number, KIND_LINK, match.group("link")))
    return hits


def check_file(path: Path, result: Result) -> None:
    try:
        data = path.read_bytes()
    except OSError as error:
        raise PrivatePathsError(f"cannot read {display(path)}: {display(error)}") from error
    if b"\0" in data[:BINARY_PROBE]:
        result.binary += 1
        return
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise PrivatePathsError(
            f"cannot read {display(path)} as UTF-8: {display(error)}") from error
    result.files += 1
    for number, kind, shown in find_in_text(text):
        result.listed.append((path.as_posix(), number, kind, shown))


def check(target: Path) -> Result:
    """The hits of a file, or of every file below a directory."""
    result = Result()
    if target.is_dir():
        for path in sorted(target.rglob("*"), key=lambda found: found.as_posix()):
            if path.is_file():
                check_file(path, result)
    elif target.is_file():
        check_file(target, result)
    else:
        raise PrivatePathsError(f"{display(target)} is no file or directory; give the copy of the "
                                f"record or the description file")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("target", type=Path, metavar="TARGET")
    try:
        args = parser.parse_args(argv)
        result = check(args.target)
    except PrivatePathsError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for path, number, kind, shown in result.listed:
        sys.stdout.write(f"{display(path)}:{number}: {kind}: {display(shown)}\n")
    skipped = f", {result.binary} binary files not read" if result.binary else ""
    sys.stdout.write(f"checked: {result.files} files, {len(result.listed)} listed{skipped}\n")
    return 1 if result.listed else 0


if __name__ == "__main__":
    sys.exit(main())
