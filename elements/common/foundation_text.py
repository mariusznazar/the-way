"""The ways `foundation_check.py` reads the text of the entries of a foundation: the blocks a heading
opens, the fields of a block, the items of a list, the rows of a table and the binding sentences of
a decision, cut into paragraphs, with the place where a sentence of one begins.

The module is imported by `foundation_check.py`, which reports what the text breaks; the scripts
that import names from that file get these through it. Importing it runs nothing. It reads no file
and asks no git.
"""

import re
import sys

sys.dont_write_bytecode = True

FIELD = re.compile(r"^- \*\*(.+?):\*\*(?: (.*))?$")
ITEM = re.compile(r"[^·,\n]+")
QUOTED = re.compile(r"\"[^\"]*\"|[\u201c\u201e][^\u201d]*\u201d")


def blocks(lines, level):
    """(line number, heading, [(line number, line)]) of each block a heading of a level opens."""
    found, current = [], None
    for number, line in enumerate(lines, start=1):
        if line.startswith("#"):
            current = [] if line.startswith(level) else None
            if current is not None:
                found.append((number, line, current))
        elif current is not None:
            current.append((number, line))
    return found


def fields(body):
    """{name: (value, [line number of each line of the value])} of the fields `- **Name:**
    value` of a block; a field's value goes on over the indented lines that follow it."""
    found, current = {}, None
    for number, line in body:
        match = FIELD.match(line)
        if match:
            current = match.group(1) if match.group(1) not in found else None
            if current:
                found[current] = [(match.group(2) or "").strip(), [number]]
        elif current and line.strip() and line[:1].isspace():
            found[current][0] += "\n" + line.strip()
            found[current][1].append(number)
        else:
            current = None
    return {name: tuple(value) for name, value in found.items()}


def located(found, name, pattern=None):
    """(word, line number) of each item of a field's list joined by ` · ` or `, `, or of each
    item inside what the first group of a pattern matches in the field's value."""
    value, lines = found.get(name, ("", [0]))
    spans = (
        [(match.start(1), match.group(1)) for match in pattern.finditer(value)]
        if pattern
        else [(0, value)]
    )
    for start, text in spans:
        for item in ITEM.finditer(text):
            word = item.group(0).strip().strip("`").strip()
            if word:
                yield word, lines[value.count("\n", 0, start + item.start())]


def binding(body):
    """The binding sentences of an entry, as paragraphs: the lines before its first field, or
    before its *Rationale* or *Rejected*, cut into paragraphs at blank lines, each with every run of
    spaces and line breaks made one space and its ends trimmed."""
    paragraphs, current = [], []
    for _, line in body:
        if FIELD.match(line) or line.startswith(("*Rationale:*", "*Rejected:*")):
            break
        if line.strip():
            current.append(line)
        elif current:
            paragraphs.append(" ".join(" ".join(current).split()))
            current = []
    if current:
        paragraphs.append(" ".join(" ".join(current).split()))
    return paragraphs


def begins_sentence(paragraph, start):
    """Whether a sentence of the paragraph begins at `start`: at the start of the paragraph, or after
    a full stop and a space, the full stop standing outside a passage between quotation marks."""
    if start == 0:
        return True
    stop = start - 2
    if paragraph[stop:start] != ". ":
        return False
    return not any(match.start() <= stop < match.end() for match in QUOTED.finditer(paragraph))


def table(lines, title):
    """(line number, cells) of each row of the table under `## title`, header and separator
    row left out, the header's cells first as row 0."""
    rows, inside = [], False
    for number, line in enumerate(lines, start=1):
        if line.startswith("#"):
            inside = line.strip() == "## " + title
        elif inside and line.strip().startswith("|"):
            cells = [cell.strip().strip("`").strip() for cell in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                rows.append((number, cells))
    return rows


def items(value):
    """The items of a list joined by ` · ` or `, `, over its lines."""
    return [item.strip().strip("`").strip() for item in re.split(r"[·,\n]", value) if item.strip()]
