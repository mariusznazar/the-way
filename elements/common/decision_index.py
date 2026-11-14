"""Index of the decisions a product's decision log selects, written to a file the agent names.

Usage, from the root of a product or from anywhere; the script runs from the-way's copy it lies in:

    python -B <the-way>/elements/common/decision_index.py --output PATH
        [--part ID]... [--section HEADING]... [--decision NUMBER]... [ROOT]
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
- `--decision NUMBER` (repeatable) takes the decision with that number.

Where `--section` and `--part` are both given, the decisions outside those sections whose *Scope*
names a given part are listed by heading alone, after the others. `--sections` writes instead the
list of the log's sections, each with its heading, its sentence and the number of its entries; it
takes no other switch.

The file opens with one fixed title line that holds the script's name, `# decision_index.py: ...`,
and a line stating how many decisions it lists in full and how many by heading alone (for
`--sections`, how many sections it lists).

Exit code: 0 when it has written the file. 2 with `Error: <message>` on stderr and nothing written
for a log it cannot read, a section the log does not hold, a number the log does not hold, a
selection given no switch, a decision that lacks *Scope* or a heading of the form
`### NUMBER — question`, and a section that lacks its sentence in the list of sections; the message
names the file, the entry and the field.
"""

import argparse
import collections
import os
import re
import sys

from foundation_check import binding, blocks, fields, located

sys.dont_write_bytecode = True

DECISIONS = "foundations/decisions.md"
WITHDRAWN = "Withdrawn identifiers"
TITLE = "# decision_index.py: index of the decisions of the log"
TITLE_SECTIONS = "# decision_index.py: list of the sections of the log"
SWITCHES = "--part, --section, --decision or --sections"
HEADING = re.compile(r"^### ([A-Za-z][A-Za-z0-9]*-[0-9]+) — (\S.*)$")

Decision = collections.namedtuple("Decision", "number question line body section")
Section = collections.namedtuple("Section", "name sentence line")


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
    except (OSError, UnicodeDecodeError):
        raise Failure("%s is missing or cannot be read as UTF-8 text" % DECISIONS)


def parse_log(lines):
    """(sections, decisions) of the log. A section is every `## ` heading but the withdrawn one,
    with its sentence; a decision is every `### ` heading, with the line of the section it stands
    in, read from its heading and the lines of its body."""
    headings = [(number, line[3:].strip()) for number, line in enumerate(lines, start=1)
                if line.startswith("## ")]
    sections = []
    for start, heading, body in blocks(lines, "## "):
        name = heading[3:].strip()
        if name != WITHDRAWN:
            sections.append(Section(name, " ".join(binding(body)), start))
    decisions = []
    for start, heading, body in blocks(lines, "### "):
        match = HEADING.match(heading)
        if not match:
            raise Failure('%s:%d: the heading "%s" is not of the form "### NUMBER — question"'
                          % (DECISIONS, start, heading))
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


def select(sections, decisions, parts, names, numbers):
    """(decisions listed in full, decisions listed by heading alone), each in the order of the log."""
    known_sections = {section.name for section in sections}
    for name in names:
        if name not in known_sections:
            raise Failure('%s: no section "%s"' % (DECISIONS, name))
    known_numbers = {decision.number for decision in decisions}
    for number in numbers:
        if number not in known_numbers:
            raise Failure("%s: no decision %s" % (DECISIONS, number))
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


def selection_text(full, alone):
    text = [TITLE, "", "Log: %s" % DECISIONS,
            "Listed in full: %d. Listed by heading alone: %d." % (len(full), len(alone)), "",
            "## Listed in full", ""]
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
    sections, decisions = parse_log(read_log(args.root))
    if args.sections:
        return sections_text(sections, decisions)
    full, alone = select(sections, decisions, args.part, args.section, args.decision)
    return selection_text(full, alone)


def parser():
    found = Parser(prog="decision_index.py", description="Index of a product's decisions.")
    found.add_argument("root", nargs="?", default=".",
                       help="directory of the product; the working directory by default")
    found.add_argument("--output", required=True, metavar="PATH",
                       help="file to write, in UTF-8")
    found.add_argument("--part", action="append", default=[], metavar="ID",
                       help="take the decisions whose Scope names the part ID")
    found.add_argument("--section", action="append", default=[], metavar="HEADING",
                       help="take the decisions of the topical section HEADING")
    found.add_argument("--decision", action="append", default=[], metavar="NUMBER",
                       help="take the decision NUMBER")
    found.add_argument("--sections", action="store_true",
                       help="write the list of the log's sections instead")
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
