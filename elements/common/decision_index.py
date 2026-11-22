"""Index of the decisions a product's decision log selects, written to a file the agent names.

Usage, from the root of a product or from anywhere; the script runs from the-way's copy it lies in:

    python -B <the-way>/elements/common/decision_index.py --output PATH
        [--part ID]... [--section HEADING]... [--decision ID]... [ROOT]
    python -B <the-way>/elements/common/decision_index.py --sections --output PATH [ROOT]

ROOT is a directory of the product, the working directory by default. The script reads
`foundations/decisions.md` under it, with or without a byte-order mark and with CRLF or LF line
endings, and writes the file named by --output in UTF-8. It reads nothing else and needs no git.

The selection is given by switches, and the decisions it takes are listed in the order of the log:

- `--part ID` (repeatable) takes each decision whose *Scope* names the part ID as a whole item, read
  as the reading rule reads *Scope*: each `- **Scope:**` line with its indented continuation lines,
  the items joined by `,` or ` · `;
- `--section HEADING` (repeatable) takes every decision of the topical section named by the text of
  its `## ` heading, other than the section "Withdrawn identifiers";
- `--decision ID` (repeatable) takes the decision with that number. The value of the number decides,
  not its prefix or its zeros, since a product keeps one log with one prefix (WAY-18): `107`,
  `WAY-107`, `D-7` and `D-07` name the decisions numbered 107 and 7 of the log. An ID that the
  log's list of withdrawn identifiers holds takes its successors in full, those of a successor that
  is withdrawn itself too, down to the decisions that live; the index then holds, above its list,
  the line `<ID> is withdrawn: <why>; its successors are listed in full`, with the `<ID>` of the
  list and the reason it gives, or, where the chain ends in `none` and no decision lives at its end,
  the line `<ID> is withdrawn: <why>; it has no successor`; a successor that is withdrawn stands in
  the line as `its successor <ID> is withdrawn: <why>` before that ending.

Where `--section` and `--part` are both given, the decisions outside those sections whose *Scope*
names a given part are listed by heading alone, after the others. `--sections` writes instead the
list of the log's sections, each with its heading, its sentence and the number of its entries; it
takes no other switch.

The file opens with one fixed title line that holds the script's name, `# decision_index.py: ...`,
and a line stating how many decisions it lists in full and how many by heading alone (for
`--sections`, how many sections it lists). Where a part given by `--part` is named by the *Scope*
of no decision of the log, a line after it names each such part, so that a misspelled part shows;
a part no decision names yet is no error.

Exit code: 0 when it has written the file. 2 with `Error: <message>` on stderr and nothing written
for a log it cannot read, a section the log does not hold, a number the log holds neither as a
decision nor as a withdrawn identifier, a selection given no switch, a decision that lacks *Scope* or a heading of the form
`### NUMBER — question`, a section that lacks its sentence in the list of sections and, where
`--decision` is given, a list of withdrawn identifiers that lacks the column Identifier, Why or
Successors, a row of it with no value in Why or Successors, or a successor that is neither a decision
nor a withdrawn identifier nor `none`; the message names the file, the entry and the field.
"""

import argparse
import collections
import os
import re
import sys

from foundation_check import binding, blocks, fields, items, located

sys.dont_write_bytecode = True

DECISIONS = "foundations/decisions.md"
WITHDRAWN = "Withdrawn identifiers"
WITHDRAWN_COLUMNS = ("Identifier", "Why", "Successors")
TITLE = "# decision_index.py: index of the decisions of the log"
TITLE_SECTIONS = "# decision_index.py: list of the sections of the log"
SWITCHES = "--part, --section, --decision or --sections"
HEADING = re.compile(r"^### ([A-Za-z][A-Za-z0-9]*-[0-9]+) — (\S.*)$")

NUMBER = re.compile(r"(?:[A-Za-z][A-Za-z0-9]*-)?([0-9]+)")

Decision = collections.namedtuple("Decision", "number question line body section")
Section = collections.namedtuple("Section", "name sentence line")
Withdrawn = collections.namedtuple("Withdrawn", "identifier why successors")


class Failure(Exception):
    """A reason the script stops with exit code 2, its message written after `Error: `."""


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise Failure(message)


def read_log(root):
    """The lines of the log, its line endings made LF and a byte-order mark dropped."""
    try:
        with open(os.path.join(root, *DECISIONS.split("/")), encoding="utf-8-sig") as handle:
            return handle.read().split("\n")
    except OSError, UnicodeDecodeError:
        raise Failure("%s is missing or cannot be read as UTF-8 text" % DECISIONS)


def parse_log(lines):
    """(sections, decisions) of the log. A section is every `## ` heading but the withdrawn one,
    with its sentence; a decision is every `### ` heading, with the line of the section it stands
    in, read from its heading and the lines of its body."""
    headings = [
        (number, line[3:].strip())
        for number, line in enumerate(lines, start=1)
        if line.startswith("## ")
    ]
    sections = []
    for start, heading, body in blocks(lines, "## "):
        name = heading[3:].strip()
        if name != WITHDRAWN:
            sections.append(Section(name, " ".join(binding(body)), start))
    decisions = []
    for start, heading, body in blocks(lines, "### "):
        match = HEADING.match(heading)
        if not match:
            raise Failure(
                '%s:%d: the heading "%s" is not of the form "### NUMBER — question"'
                % (DECISIONS, start, heading)
            )
        section = max((number for number, _ in headings if number < start), default=None)
        decisions.append(Decision(match.group(1), match.group(2), start, body, section))
    return sections, decisions


def scope_items(decision):
    """(the value of *Scope*, its items). Where the field is missing or empty, the entry has no
    *Scope* and the script stops."""
    found = fields(decision.body)
    value = found.get("Scope", ("", []))[0]
    if not value.strip():
        raise Failure("%s: entry %s has no field Scope" % (DECISIONS, decision.number))
    return value, {word for word, _ in located(found, "Scope")}


def number_value(text):
    """The value of a number written as `107`, `WAY-107`, `D-07` or `007`, or None for any other
    text."""
    found = NUMBER.fullmatch(text.strip())
    return int(found.group(1)) if found else None


def withdrawn_numbers(lines):
    """{value of the number: Withdrawn} of the log's list of withdrawn identifiers, read by the
    names of its columns. A list that lacks the column Identifier, Why or Successors, a row that
    has no cell in one of them, and a row whose Why or Successors cell is empty stop the script,
    with a message that names the file and the field; a row whose identifier is no number is left
    out, as the check of the foundation reports it. A log with no such list gives {}."""
    found = {}
    for _, heading, body in blocks(lines, "## "):
        if heading[3:].strip() != WITHDRAWN:
            continue
        rows = [
            [cell.strip() for cell in line.strip().strip("|").split("|")]
            for _, line in body
            if line.strip().startswith("|")
        ]
        header = rows[0] if rows else []
        place = {}
        for column in WITHDRAWN_COLUMNS:
            if column not in header:
                raise Failure(
                    "%s: the list of withdrawn identifiers has no column %s" % (DECISIONS, column)
                )
            place[column] = header.index(column)
        for cells in rows[1:]:
            if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue
            value = (
                number_value(cells[place["Identifier"]])
                if len(cells) > place["Identifier"]
                else None
            )
            if value is None or value in found:
                continue
            row = cells[place["Identifier"]]
            for column in ("Why", "Successors"):
                if len(cells) <= place[column] or not cells[place[column]]:
                    raise Failure(
                        "%s: the withdrawn identifier %s has no value in the column %s"
                        % (DECISIONS, row, column)
                    )
            found[value] = Withdrawn(row, cells[place["Why"]], items(cells[place["Successors"]]))
    return found


def chain(value, withdrawn, living):
    """(the withdrawn entries met from the withdrawn number VALUE on, in the order met, each once;
    the numbers of the decisions that live at the end of the chain). The successor `none` ends its
    branch; any other successor that is neither a decision nor withdrawn stops the script, since
    reading it as no successor would say that no decision took the place of the number."""
    met, reached, seen, stack = [], [], set(), [value]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        met.append(withdrawn[current])
        for successor in reversed(withdrawn[current].successors):
            following = number_value(successor)
            if following in living:
                if living[following] not in reached:
                    reached.append(living[following])
            elif following in withdrawn:
                stack.append(following)
            elif successor != "none":
                raise Failure(
                    "%s: the successor %s of the withdrawn identifier %s is neither a decision "
                    "nor a withdrawn identifier"
                    % (DECISIONS, successor, withdrawn[current].identifier)
                )
    return met, reached


def withdrawn_line(met, reached):
    """The line above the list for a withdrawn number: its reason and that of each withdrawn
    successor it led through, and whether decisions that live are listed."""
    text = "%s is withdrawn: %s" % (met[0].identifier, met[0].why)
    for entry in met[1:]:
        text += "; its successor %s is withdrawn: %s" % (entry.identifier, entry.why)
    return text + ("; its successors are listed in full" if reached else "; it has no successor")


def resolve_decisions(requested, decisions, withdrawn):
    """(numbers of the decisions to list in full for the IDs requested, the lines for the withdrawn
    ones among them). An ID is met by the value of its number: a decision of the log, else a
    withdrawn number whose chain leads to the decisions that live."""
    living = {}
    for decision in decisions:
        living.setdefault(number_value(decision.number), decision.number)
    numbers, lines = [], []
    for text in requested:
        value = number_value(text)
        if value in living:
            numbers.append(living[value])
        elif value in withdrawn:
            met, reached = chain(value, withdrawn, living)
            numbers += reached
            line = withdrawn_line(met, reached)
            if line not in lines:
                lines.append(line)
        else:
            raise Failure("%s: no decision %s" % (DECISIONS, text))
    return numbers, lines


def select(sections, decisions, parts, names, numbers):
    """(decisions listed in full, decisions listed by heading alone), each in the order of the log."""
    known_sections = {section.name for section in sections}
    for name in names:
        if name not in known_sections:
            raise Failure('%s: no section "%s"' % (DECISIONS, name))
    chosen = {section.line for section in sections if section.name in names}
    full, alone = [], []
    for decision in decisions:
        _, items = scope_items(decision)
        by_part = bool(items & set(parts))
        if decision.number in numbers or decision.section in chosen or (by_part and not names):
            full.append(decision)
        elif by_part:
            alone.append(decision)
    return full, alone


def unnamed_parts(decisions, parts):
    """The given parts that no decision's *Scope* names, in the order given, each once."""
    named = set()
    for decision in decisions:
        named |= scope_items(decision)[1]
    return [part for part in dict.fromkeys(parts) if part not in named]


def selection_text(full, alone, unnamed, withdrawn=()):
    text = [
        TITLE,
        "",
        "Log: %s" % DECISIONS,
        "Listed in full: %d. Listed by heading alone: %d." % (len(full), len(alone)),
    ]
    if unnamed:
        text.append("Parts that no Scope names: %s." % ", ".join(unnamed))
    text += list(withdrawn)
    text += ["", "## Listed in full", ""]
    for decision in full:
        text += ["### %s — %s" % (decision.number, decision.question), ""]
        for paragraph in binding(decision.body):
            text += [paragraph, ""]
        value, _ = scope_items(decision)
        text += ["- **Scope:** %s" % " ".join(value.split()), ""]
    text += ["## Listed by heading alone", ""]
    for decision in alone:
        text.append("- %s — %s" % (decision.number, decision.question))
    return "\n".join(text) + "\n"


def sections_text(sections, decisions):
    text = [TITLE_SECTIONS, "", "Log: %s" % DECISIONS, "Sections: %d." % len(sections), ""]
    for section in sections:
        if not section.sentence:
            raise Failure('%s: section "%s" has no sentence' % (DECISIONS, section.name))
        count = sum(1 for decision in decisions if decision.section == section.line)
        text += ["## %s" % section.name, "", section.sentence, "", "Entries: %d." % count, ""]
    return "\n".join(text) + "\n"


def run(args):
    """The text the script writes for the arguments, raising Failure where it must stop."""
    if args.sections and (args.part or args.section or args.decision):
        raise Failure("--sections takes no other switch")
    if not args.sections and not (args.part or args.section or args.decision):
        raise Failure("no selection given: give %s" % SWITCHES)
    lines = read_log(args.root)
    sections, decisions = parse_log(lines)
    if args.sections:
        return sections_text(sections, decisions)
    listed = withdrawn_numbers(lines) if args.decision else {}
    numbers, withdrawn = resolve_decisions(args.decision, decisions, listed)
    full, alone = select(sections, decisions, args.part, args.section, numbers)
    return selection_text(full, alone, unnamed_parts(decisions, args.part), withdrawn)


def parser():
    found = Parser(prog="decision_index.py", description="Index of a product's decisions.")
    found.add_argument(
        "root",
        nargs="?",
        default=".",
        help="directory of the product; the working directory by default",
    )
    found.add_argument("--output", required=True, metavar="PATH", help="file to write, in UTF-8")
    found.add_argument(
        "--part",
        action="append",
        default=[],
        metavar="ID",
        help="take the decisions whose Scope names the part ID",
    )
    found.add_argument(
        "--section",
        action="append",
        default=[],
        metavar="HEADING",
        help="take the decisions of the topical section HEADING",
    )
    found.add_argument(
        "--decision",
        action="append",
        default=[],
        metavar="ID",
        help="take the decision ID, found by the value of its number (107, WAY-107, D-07); the "
        "successors of a withdrawn number are taken in full",
    )
    found.add_argument(
        "--sections", action="store_true", help="write the list of the log's sections instead"
    )
    return found


def main(argv=None):
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    try:
        args = parser().parse_args(argv)
        text = run(args)
        try:
            with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        except OSError as error:
            raise Failure("%s cannot be written: %s" % (args.output, error))
    except Failure as failure:
        sys.stderr.write("Error: %s\n" % failure)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
