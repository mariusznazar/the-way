"""The items the stage reports of a task cycle give under **Searches not found or unclear** that the
cycle record's process remarks do not hold (WAY-260).

Usage:

    python -B task-cycle/remarks_check.py RECORD

In a product, the path starts with `.the-way/`. RECORD is the cycle-record directory,
`.runs/task-cycles/<task-slug>/` or its committed copy under `docs/task-cycles/`: it holds
`cycle.md` and `reports/`.

The reports are the `.md` files of `reports/` whose name holds neither `handoff` nor `findings`,
read in the order of their names; a handoff, a findings file and a log are not read. A report gives
its section in either of two forms, and may give both:

- a heading, at any level, whose text is `Searches not found or unclear`, after an optional section
  number such as `12.`, with an optional trailing colon, emphasis or parenthesis; the section runs
  to the next heading of the same or a higher level;
- a bold label `**Searches not found or unclear**`, its colon inside or outside the bold or absent,
  at the start of a line or of a list item; the text after the label on its line belongs to the
  section. A label that is a list item ends at the next line indented no deeper than its marker. A
  label that is no list item ends at the next heading, the next rule, or the next line that is no
  list item and starts with bold text, so that `**Choices:** ...` ends it.

A mention of the name inside a sentence, a section inside fenced code, and a report with no
section are not read. The items of a section are its list items, each with the lines that continue
it and its sub-items, and its paragraphs, a paragraph after a list included, so that nothing written
in the section goes unread; a sub-heading is no item. An item
reads `none` when, with emphasis marks, backticks and a final full stop taken off, it is `none` in
any case; every other item is listed, `none found` and `None unresolved. Unclear: ...` among them.

The process remarks are the blocks of `cycle.md` that open as the nightly review of cycles cuts
them: a list item, a heading or a paragraph that begins with `Process remark`,
`Process improvements`, `Other process remarks` or `Searches not found`, with the lines under it
as that review cuts them. An item is in the remarks when its words, with each run of whitespace
taken as one space, stand in them word for word and in the same case. An item that two
reports give stands once for each report that gives it: the remarks hold it as many times as the
reports do, since repeated items are kept apart.

Each item the remarks do not hold is printed on stdout as `<report path>: <item>`, the item as one
line, in the order of the reports and of the items in each; then a last line, `checked: ...`.
Exit code: 0 when nothing is listed; 1 with the items listed; 2 with `Error: <message>` on stderr
when the argument is wrong or `cycle.md` or a report cannot be read as UTF-8. The script reads the
record and nothing else, runs nothing and writes no file. A record with no `reports/` directory has
no reports and lists nothing.

Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

SECTION = "searches not found or unclear"
REMARKS_PREFIXES = ("process remark", "process improvements", "other process remarks",
                    "searches not found")

# The number a report may put before a section's name: `12.`, `12)`, `3.1`, `3.1.`.
SECTION_NUMBER = re.compile(r"\d+(?:\.\d+)*[.)]?[ \t]+")
HEADING = re.compile(r" {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*")
FENCE = re.compile(r" {0,3}(`{3,}|~{3,})")
LABEL = re.compile(r"(?P<indent>[ \t]*)(?:(?P<marker>[-*+]|\d+[.)])[ \t]+)?"
                   r"\*\*[ \t]*Searches not found or unclear[ \t]*:?[ \t]*\*\*[ \t]*:?[ \t]*"
                   r"(?P<rest>.*)", re.I)
MARKER = re.compile(r"(?P<indent>[ \t]*)(?P<marker>[-*+]|\d+[.)])[ \t]+(?P<text>.*)")
RULE = re.compile(r" {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*")
BOLD_START = re.compile(r"[ \t]{0,3}\*\*")
# The opening and the cutting of a block of remarks, as the nightly review of cycles has them.
DIGEST_MARKER = re.compile(r"^(?:[-*]|\d+\.)\s+")
DIGEST_HEADING = re.compile(r"^(#{1,6})\s")
BLOCK_SEPARATOR = "\x00"


class RemarksCheckError(Exception):
    """An argument that is wrong or a file that cannot be read."""


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise RemarksCheckError(message)


def display(value: object) -> str:
    """Keep text taken from the files inside one report line."""
    return "".join(char if char.isprintable() else ascii(char)[1:-1] for char in str(value))


def split_lines(text: str) -> list[str]:
    lines = re.split(r"\r\n|\r|\n", text)
    lines = lines[:-1] if lines and lines[-1] == "" else lines
    return [line.expandtabs(4) for line in lines]


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def collapse(text: str) -> str:
    return " ".join(text.split())


def fenced_flags(lines: list[str]) -> list[bool]:
    """Whether each line is a fence line or stands inside fenced code."""
    flags = []
    fence = ""
    for line in lines:
        match = FENCE.match(line)
        if fence:
            flags.append(True)
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) \
                    and not line.strip().strip(fence[0]):
                fence = ""
        elif match:
            fence = match.group(1)
            flags.append(True)
        else:
            flags.append(False)
    return flags


def names_section(heading_text: str) -> bool:
    text = re.sub(r"[*_`]", "", heading_text).strip().rstrip(":").strip().casefold()
    number = SECTION_NUMBER.match(text)
    text = text[number.end():] if number else text
    return text.startswith(SECTION) and not text[len(SECTION):len(SECTION) + 1].isalnum()


def is_report(path: Path) -> bool:
    """A file of `reports/` the script reads: a `.md` file whose name holds neither word."""
    return (path.is_file() and path.name.endswith(".md")
            and "handoff" not in path.name and "findings" not in path.name)


def reads_none(item: str) -> bool:
    return item.strip(" \t*_`.").casefold() == "none"


@dataclass
class Item:
    kind: str  # "list" or "paragraph"
    parts: list[str] = field(default_factory=list)


def split_items(body: list[tuple[str, bool]]) -> list[str]:
    """The items of a section's lines, each as one line of text."""
    items: list[Item] = []
    current: Item | None = None
    base: int | None = None
    blank = False
    for text, fenced in body:
        if fenced:
            if current is None:
                current = Item("paragraph")
                items.append(current)
            current.parts.append(text)
            blank = False
            continue
        if not text.strip() or HEADING.fullmatch(text):
            # A sub-heading inside a section is no item; it parts what comes before and after it.
            blank = True
            current = None if HEADING.fullmatch(text) else current
            continue
        indent = indent_of(text)
        marker = MARKER.fullmatch(text)
        if marker and (base is None or indent <= base):
            base = indent if base is None else min(base, indent)
            current = Item("list", [marker.group("text")])
            items.append(current)
        elif marker and current is not None:
            current.parts.append(text.strip())
        elif current is None or (blank and (current.kind == "paragraph"
                                            or indent <= (base or 0))):
            current = Item("paragraph", [text.strip()])
            items.append(current)
        else:
            current.parts.append(text.strip())
        blank = False
    return [text for text in (collapse(" ".join(item.parts)) for item in items) if text]


def label_end(lines: list[str], fenced: list[bool], start: int, indent: int, is_list: bool) -> int:
    """The index of the line that ends the section a bold label opens on line `start`."""
    end = start + 1
    while end < len(lines):
        line = lines[end]
        if not fenced[end]:
            if HEADING.fullmatch(line):
                break
            if line.strip():
                if is_list:
                    if indent_of(line) <= indent:
                        break
                elif RULE.fullmatch(line) or (BOLD_START.match(line)
                                              and not MARKER.fullmatch(line)):
                    break
        end += 1
    return end


def section_items(text: str) -> list[str]:
    """The items other than `none`'s of every **Searches not found or unclear** section of a
    report's text, each as one line."""
    lines = split_lines(text)
    fenced = fenced_flags(lines)
    found: list[str] = []
    index = 0
    while index < len(lines):
        if fenced[index]:
            index += 1
            continue
        heading = HEADING.fullmatch(lines[index])
        if heading and names_section(heading.group(2) or ""):
            level = len(heading.group(1))
            end = index + 1
            while end < len(lines):
                other = None if fenced[end] else HEADING.fullmatch(lines[end])
                if other and len(other.group(1)) <= level:
                    break
                end += 1
            found += split_items(list(zip(lines[index + 1:end], fenced[index + 1:end])))
            index = end
            continue
        label = LABEL.fullmatch(lines[index])
        if label:
            end = label_end(lines, fenced, index, len(label.group("indent")),
                            label.group("marker") is not None)
            body = list(zip(lines[index + 1:end], fenced[index + 1:end]))
            if label.group("rest").strip():
                body.insert(0, (label.group("rest"), False))
            found += split_items(body)
            index = end
            continue
        index += 1
    return [item for item in found if not reads_none(item)]


def heading_level(line: str) -> int:
    match = DIGEST_HEADING.match(line)
    return len(match.group(1)) if match else 0


def opens_block(line: str) -> str | None:
    """The kind of block of remarks a line opens: "heading", "bullet", "paragraph" or None."""
    if heading_level(line):
        opens = line.lstrip("#").strip().lower().startswith(REMARKS_PREFIXES)
        return "heading" if opens else None
    body = line.lstrip(" \t")
    marker = DIGEST_MARKER.match(body)
    if marker:
        return "bullet" if body[marker.end():].lower().startswith(REMARKS_PREFIXES) else None
    return "paragraph" if body.lower().startswith(REMARKS_PREFIXES) else None


def remark_blocks(text: str) -> list[str]:
    """Every block of the record's text that opens as a block of process remarks.

    A heading block runs to the next heading of the same or a higher rank; a list item to the first
    non-blank line indented no deeper than its marker; a paragraph to the first blank line; any
    heading ends a list item or a paragraph. A list item followed by a blank line and another item
    at its level is a lead-in to a list, which runs to the next heading.
    """
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    blocks = []
    index = 0
    while index < len(lines):
        kind = opens_block(lines[index])
        if kind is None:
            index += 1
            continue
        start = index
        level = heading_level(lines[index])
        indent = len(lines[index]) - len(lines[index].lstrip(" \t"))
        listing = False
        end = index + 1
        while end < len(lines):
            line = lines[end]
            line_level = heading_level(line)
            if kind == "heading":
                if line_level and line_level <= level:
                    break
            elif line_level:
                break
            elif kind == "bullet":
                if line.strip() and len(line) - len(line.lstrip(" \t")) <= indent:
                    after_blank = not lines[end - 1].strip()
                    if not (listing or (after_blank and DIGEST_MARKER.match(line.lstrip()))):
                        break
                    listing = True
            elif not line.strip():
                break
            end += 1
        body = lines[start:end]
        while body and not body[-1].strip():
            body.pop()
        blocks.append("\n".join(body))
        index = end
    return blocks


@dataclass
class Result:
    listed: list[tuple[Path, str]] = field(default_factory=list)
    reports: int = 0
    items: int = 0


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError) as error:
        raise RemarksCheckError(
            f"cannot read {display(path)} as UTF-8: {display(error)}") from error


def check(record: Path) -> Result:
    """The items of the reports of `record` that its process remarks do not hold."""
    cycle = record / "cycle.md"
    if not cycle.is_file():
        raise RemarksCheckError(f"{display(record)} holds no cycle.md; give the cycle-record "
                                f"directory")
    remarks = collapse(BLOCK_SEPARATOR.join(remark_blocks(read(cycle))))
    result = Result()
    reports_dir = record / "reports"
    names = sorted(path.name for path in reports_dir.glob("*.md") if is_report(path)) \
        if reports_dir.is_dir() else []
    held: dict[str, int] = {}
    seen: Counter[str] = Counter()
    for name in names:
        path = reports_dir / name
        result.reports += 1
        for item in section_items(read(path)):
            result.items += 1
            if item not in held:
                held[item] = remarks.count(item)
            seen[item] += 1
            if seen[item] > held[item]:
                result.listed.append((path, item))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("record", type=Path, metavar="RECORD")
    try:
        args = parser.parse_args(argv)
        result = check(args.record)
    except RemarksCheckError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for path, item in result.listed:
        sys.stdout.write(f"{display(path.as_posix())}: {display(item)}\n")
    sys.stdout.write(f"checked: {result.reports} reports, {result.items} items other than none, "
                     f"{len(result.listed)} not in the process remarks\n")
    return 1 if result.listed else 0


if __name__ == "__main__":
    sys.exit(main())
