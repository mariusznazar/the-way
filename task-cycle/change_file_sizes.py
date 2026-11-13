"""The number of lines of each file a change touches, before the change and after it — the numbers
the review of the whole change reads for the structure of the code it leaves (WAY-357).

Usage:

    python -B task-cycle/change_file_sizes.py BASE HEAD [--root DIR]

BASE and HEAD are two commits of the repository at DIR, which defaults to the current directory; any
name `git rev-parse` resolves to a commit does, and the files compared are those that differ between
the trees of the two commits, as `git diff BASE HEAD` gives them, a rename found as `git diff -M`
finds one. The number of lines of a file is the number of line feeds in it, plus one where its last
line has none; an empty file has none. A file with a null byte in its first 8000 bytes, as git
reads one, is binary, and a submodule has no lines: their cells read `binary` and `submodule`, and
no number of them enters the summary.

The report is Markdown, printed: a row for each changed file with its lines before the change
(`—` where the file did not exist), its lines after it (`—` where it is gone), their difference and
a note — `added`, `deleted`, `modified`, `renamed from <path>`, or `type changed` — and, last, one
line that begins `Summary:` with the count of files of each kind and the totals of lines before,
after and their difference. Exit code: 0 when the report was written; 2 with `Error: <message>` on
stderr, and no report, when DIR is no directory or holds no repository, when git cannot be started,
when BASE or HEAD names no commit, or when git's answer cannot be read.

Standard library only; git is started with a list of arguments and never through a shell, and file
names are read from git's output separated by null bytes, so a name with a space, a quotation mark
or a letter outside ASCII is read as it is, and a file's content is read by the identifier of its
blob, so no name is ever passed back to git.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

BINARY_PROBE_BYTES = 8000
GITLINK_MODE = "160000"
ABSENT_MODE = "000000"


class FileSizesError(Exception):
    """The sizes cannot be read."""


@dataclass
class Entry:
    path: str
    before: int | str | None  # lines, "binary" or "submodule"; None where the file did not exist
    after: int | str | None  # the same; None where the file is gone
    note: str


def git(root: Path, *arguments: str) -> bytes:
    try:
        run = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True)
    except OSError as error:
        raise FileSizesError(f"cannot start git: {error}") from error
    if run.returncode != 0:
        message = run.stderr.decode("utf-8", errors="replace").strip() or f"exit code {run.returncode}"
        raise FileSizesError(f"`git {' '.join(arguments[:2])}` failed in {root}: {message}")
    return run.stdout


def resolve(root: Path, name: str) -> str:
    """The identifier of the commit `name` stands for."""
    try:
        run = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--verify", "--quiet", "--end-of-options",
             f"{name}^{{commit}}"], capture_output=True)
    except OSError as error:
        raise FileSizesError(f"cannot start git: {error}") from error
    found = run.stdout.decode("utf-8", errors="replace").strip()
    if run.returncode != 0 or not found:
        git(root, "rev-parse", "--git-dir")  # a directory with no repository ends here, with git's words
        raise FileSizesError(f"`{name}` names no commit in {root}")
    return found


def count_lines(data: bytes) -> int | str:
    if b"\0" in data[:BINARY_PROBE_BYTES]:
        return "binary"
    return data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)


class Blobs:
    """Reads blobs of a repository by identifier through one `git cat-file --batch` process."""

    def __init__(self, root: Path) -> None:
        try:
            self.process = subprocess.Popen(
                ["git", "-C", str(root), "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        except OSError as error:
            raise FileSizesError(f"cannot start git: {error}") from error

    def read(self, identifier: str) -> bytes:
        assert self.process.stdin is not None and self.process.stdout is not None
        try:
            self.process.stdin.write(identifier.encode("ascii") + b"\n")
            self.process.stdin.flush()
            header = self.process.stdout.readline().split()
            if len(header) != 3 or header[1] != b"blob":
                raise FileSizesError(f"git gives no blob for {identifier}")
            size = int(header[2])
            data = self.process.stdout.read(size)
            self.process.stdout.read(1)  # the line feed that ends each answer
        except (OSError, ValueError) as error:
            raise FileSizesError(f"cannot read the blob {identifier} from git: {error}") from error
        if len(data) != size:
            raise FileSizesError(f"git gave {len(data)} bytes of the blob {identifier}, not {size}")
        return data

    def close(self) -> None:
        if self.process.stdin is not None:
            self.process.stdin.close()
        self.process.wait()


def lines_of(blobs: Blobs, mode: str, identifier: str) -> int | str | None:
    if mode == ABSENT_MODE:
        return None
    if mode == GITLINK_MODE:
        return "submodule"
    return count_lines(blobs.read(identifier))


def parse_raw(output: bytes) -> list[tuple[list[str], list[str]]]:
    """The records of `git diff --raw -z`: for each, the fields of its header and its paths."""
    tokens = output.split(b"\0")
    if tokens and tokens[-1] == b"":
        tokens.pop()
    records = []
    index = 0
    while index < len(tokens):
        header = tokens[index].decode("ascii", errors="replace")
        fields = header[1:].split(" ") if header.startswith(":") else []
        if len(fields) != 5:
            raise FileSizesError(f"cannot read a line of the answer of git diff: {header[:80]!r}")
        count = 2 if fields[4][:1] in ("R", "C") else 1
        paths = [token.decode("utf-8", errors="replace") for token in tokens[index + 1:index + 1 + count]]
        if len(paths) != count:
            raise FileSizesError("the answer of git diff ends in the middle of a record")
        records.append((fields, paths))
        index += 1 + count
    return records


def measure(root: Path, base: str, head: str) -> list[Entry]:
    output = git(root, "diff", "--raw", "-z", "-M", "--no-ext-diff", "--no-color", base, head, "--")
    entries = []
    blobs = Blobs(root)
    try:
        for (mode_before, mode_after, id_before, id_after, status), paths in parse_raw(output):
            before = lines_of(blobs, mode_before, id_before)
            after = lines_of(blobs, mode_after, id_after)
            kind = status[0]
            if kind == "A":
                note = "added"
            elif kind == "D":
                note = "deleted"
            elif kind == "R":
                note = f"renamed from `{paths[0]}`"
            elif kind == "T":
                note = "type changed"
            elif kind == "M":
                note = "modified"
            else:
                raise FileSizesError(f"git diff gives the status {status} of {paths[-1]!r}")
            entries.append(Entry(paths[-1], before, after, note))
    finally:
        blobs.close()
    return entries


def cell(value: int | str | None) -> str:
    return "—" if value is None else str(value)


def difference(entry: Entry) -> int | None:
    if entry.before is None and isinstance(entry.after, int):
        return entry.after
    if entry.after is None and isinstance(entry.before, int):
        return -entry.before
    if isinstance(entry.before, int) and isinstance(entry.after, int):
        return entry.after - entry.before
    return None


def report(entries: list[Entry], base: str, head: str) -> str:
    lines = [
        "# Sizes of the changed files",
        "",
        f"Lines of each file that differs between `{base}` and `{head}`, before the change and "
        "after it.",
        "",
        "| File | Before | After | Change | Note |",
        "|---|---|---|---|---|",
    ]
    before_total = after_total = 0
    counts = {"added": 0, "deleted": 0, "renamed": 0, "modified": 0, "not measured": 0}
    for entry in entries:
        delta = difference(entry)
        name = entry.path.replace("|", "\\|")
        lines.append(f"| `{name}` | {cell(entry.before)} | {cell(entry.after)} | "
                     f"{'—' if delta is None else format(delta, '+d')} | {entry.note} |")
        if isinstance(entry.before, int):
            before_total += entry.before
        if isinstance(entry.after, int):
            after_total += entry.after
        if isinstance(entry.before, str) or isinstance(entry.after, str):
            counts["not measured"] += 1
        elif entry.note == "added":
            counts["added"] += 1
        elif entry.note == "deleted":
            counts["deleted"] += 1
        elif entry.note.startswith("renamed"):
            counts["renamed"] += 1
        else:
            counts["modified"] += 1
    kinds = ", ".join(f"{number} {name}" for name, number in counts.items())
    lines.append("")
    lines.append(f"Summary: {len(entries)} files changed ({kinds}); lines before {before_total}, "
                 f"after {after_total}, change {after_total - before_total:+d}.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("base")
    parser.add_argument("head")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if not root.is_dir():
            raise FileSizesError(f"{args.root} is not a directory")
        base = resolve(root, args.base)
        head = resolve(root, args.head)
        entries = measure(root, base, head)
    except FileSizesError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.stdout.write(report(entries, args.base, args.head))
    return 0


if __name__ == "__main__":
    sys.exit(main())
