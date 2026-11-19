"""Comparison of the entries of two copies of a product's decision log, byte for byte.

Usage, from the root of a product or from anywhere; the script runs from the-way's copy it lies in:

    python -B <the-way>/elements/common/compare_log_entries.py BEFORE AFTER

BEFORE and AFTER are two copies of a decision log, each given by its path. The script reads both
and writes nothing; it needs no git. It serves the division of a log into topical sections, the-way's
or a product's: a copy from before the division and a copy from after it must hold the same entries,
each with the same bytes.

An entry is the block that a heading `### <PREFIX>-<NN> — ` opens: from that heading to the line
before the next heading of any level, the blank lines at its end left out, keyed by its identifier.
The block that a heading `## Withdrawn identifiers` opens is compared the same way, keyed by that
heading. Nothing else of a copy is compared, so a copy that adds topical section headings and their
sentences differs in no entry.

Each report is one of these:

- `<identifier> stands only in <file>`: an entry that one copy holds and the other lacks;
- `<identifier> stands <n> times in <file>, at lines <a>, <b> and <c>`: an identifier that a copy
  holds more than once; the two copies are then compared by their first block of that identifier;
- `<identifier> differs: the first line that differs is line <a> in BEFORE and line <b> in AFTER`,
  followed by the two lines, indented, one from each copy.

Exit code: 0 when every entry is the same byte for byte in both copies and nothing is reported,
1 when it reports any, and 2 with `Error: <message>` on stderr for a copy it cannot read as UTF-8
text or that holds no entry; the message names the file.
"""

import argparse
import collections
import re
import sys

sys.dont_write_bytecode = True

ENTRY = re.compile(r"^### ([A-Z][A-Z0-9]*-[0-9]+) — ")
HEADING = re.compile(r"^#{1,6}(\s|$)")
WITHDRAWN = "## Withdrawn identifiers"

Block = collections.namedtuple("Block", "key line lines")


class Failure(Exception):
    """A reason the script stops with exit code 2, its message written after `Error: `."""


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise Failure(message)


def read_blocks(path):
    """The entries and the withdrawn block of a copy, in the order of its lines. Each block holds its
    key, the line it opens at and its lines as (line number, text), its heading first and the blank
    lines at its end left out. A copy that holds no entry is a failure."""
    try:
        with open(path, "rb") as handle:
            text = handle.read().decode("utf-8")
    except OSError, UnicodeDecodeError:
        raise Failure("%s cannot be read as UTF-8 text" % path)
    found, current = [], None
    for number, line in enumerate(text.split("\n"), start=1):
        if HEADING.match(line):
            current, key = None, None
            match = ENTRY.match(line)
            if match:
                key = match.group(1)
            elif line.strip() == WITHDRAWN:
                key = WITHDRAWN
            if key is not None:
                current = [key, number, [(number, line)]]
                found.append(current)
        elif current is not None:
            current[2].append((number, line))
    blocks = []
    for key, number, lines in found:
        while lines and not lines[-1][1].strip():
            lines.pop()
        blocks.append(Block(key, number, lines))
    if not any(block.key != WITHDRAWN for block in blocks):
        raise Failure(
            "%s holds no entry: no heading `### PREFIX-NN — question` opens a block" % path
        )
    return blocks


def by_key(blocks):
    """{key: the blocks with that key, in the order of the copy}."""
    found = {}
    for block in blocks:
        found.setdefault(block.key, []).append(block)
    return found


def listing(numbers):
    """The numbers in words: `3`, `3 and 9`, `3, 9 and 12`."""
    texts = [str(number) for number in numbers]
    if len(texts) == 1:
        return texts[0]
    return " and ".join([", ".join(texts[:-1]), texts[-1]])


def first_difference(first, second):
    """The index of the first line that differs between two blocks, or None where they are the
    same, a line missing from the shorter one counting as a difference."""
    for index in range(max(len(first), len(second))):
        left = first[index][1] if index < len(first) else None
        right = second[index][1] if index < len(second) else None
        if left != right:
            return index
    return None


def line_at(block, index):
    """(line number, text) of a block's line at the index; where the block ends before that index,
    the line after its last line and the words saying so."""
    if index < len(block.lines):
        return block.lines[index]
    return block.lines[-1][0] + 1, "(the entry ends before this line)"


def compare(before, after, before_path, after_path):
    """The reports of the comparison of two copies, each a text of one or more lines, one report for
    each entry that stands in one copy only, each identifier standing more than once and each
    difference between the first blocks of an identifier."""
    left, right = by_key(before), by_key(after)
    keys = list(left) + [key for key in right if key not in left]
    reports = []
    for key in keys:
        first, second = left.get(key, []), right.get(key, [])
        if not first:
            reports.append("%s stands only in %s" % (key, after_path))
            continue
        if not second:
            reports.append("%s stands only in %s" % (key, before_path))
            continue
        for path, blocks in ((before_path, first), (after_path, second)):
            if len(blocks) > 1:
                reports.append(
                    "%s stands %d times in %s, at lines %s"
                    % (key, len(blocks), path, listing([block.line for block in blocks]))
                )
        index = first_difference(first[0].lines, second[0].lines)
        if index is not None:
            left_line = line_at(first[0], index)
            right_line = line_at(second[0], index)
            reports.append(
                "%s differs: the first line that differs is line %d in %s and line %d "
                "in %s\n  %s: %s\n  %s: %s"
                % (
                    key,
                    left_line[0],
                    before_path,
                    right_line[0],
                    after_path,
                    before_path,
                    left_line[1],
                    after_path,
                    right_line[1],
                )
            )
    return reports


def run(before_path, after_path):
    """The report's lines and the exit code, raising Failure where the script must stop."""
    before = read_blocks(before_path)
    after = read_blocks(after_path)
    reports = compare(before, after, before_path, after_path)
    if reports:
        return reports + ["%d report%s." % (len(reports), "" if len(reports) == 1 else "s")], 1
    entries_before = sum(1 for block in before if block.key != WITHDRAWN)
    entries_after = sum(1 for block in after if block.key != WITHDRAWN)
    return [
        "Compared %d entries of %s with %d of %s: all the same byte for byte."
        % (entries_before, before_path, entries_after, after_path)
    ], 0


def parser():
    found = Parser(
        prog="compare_log_entries.py",
        description="Comparison of the entries of two copies of a decision log.",
    )
    found.add_argument(
        "before", metavar="BEFORE", help="the copy of the log from before the change"
    )
    found.add_argument("after", metavar="AFTER", help="the copy of the log from after the change")
    return found


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    try:
        args = parser().parse_args(argv)
        lines, code = run(args.before, args.after)
    except Failure as failure:
        sys.stderr.write("Error: %s\n" % failure)
        return 2
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
