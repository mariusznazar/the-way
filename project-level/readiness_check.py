"""The readiness check of a project definition: the conditions of the readiness gate a script can
decide (`TODO — decision pending: which decision sets the project level's readiness gate`).

Usage, from any directory:

    python -B <the-way>/project-level/readiness_check.py DEFINITION [--before-approval]
    python -B <the-way>/project-level/readiness_check.py DEFINITION --fingerprint

The definition follows `project-level/definition_template.md`. The check reports:

- structure — a `Status:` line under the title, and every heading of the template once, in its
  order, with no other second-level heading;
- a — no section holds the word `TODO`, and none is empty (`none` states that nothing is there);
- d — every item under "Open questions" ends with `— resolved in: breakdown` or
  `— resolved in: task: <name>`;
- b — no projected decision still reads `**Approved by:** on acceptance`;
- e — the gate record holds its three lines, and its fingerprint matches the definition.

With --before-approval the check leaves out b and e and the gate record, since the human has not
approved yet. --fingerprint prints the fingerprint the gate record is to carry, once the
structure holds. Exit codes: 0 nothing found, 1 findings, 2 the call or the file is wrong. The
check decides neither condition c (an agent's search of the foundation) nor what the human
approved.
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "relation-model"))
from fingerprint import fingerprint  # noqa: E402

SECTIONS = ("Goal", "Background", "In scope", "Out of scope", "Inputs and constraints",
            "Deliverables", "Success", "Risks", "Open questions", "Touched parts and decisions",
            "Projected foundation changes", "Gate record")
GATE_RECORD = "Gate record"
OPEN_QUESTIONS = "Open questions"
PROJECTED = "Projected foundation changes"

HEADING = re.compile(r"^## (?!#)(.*?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
TODO = re.compile(r"\bTODO\b")
ITEM = re.compile(r"^- ")
RESOLVED = re.compile(r"— resolved in: (breakdown|task: \S.*)$")
PENDING_APPROVAL = re.compile(r"^\s*- \*\*Approved by:\*\* on acceptance\s*$")
STATUS = re.compile(r"^Status: (definition — open: \S.*|ready for gate|approved \d{4}-\d{2}-\d{2})$")
GATE_LINES = (
    ("Approved by", re.compile(r"^- Approved by: \S.*, \d{4}-\d{2}-\d{2}$")),
    ("Foundation searched at", re.compile(r"^- Foundation searched at: [0-9a-f]{7,40}$")),
    ("Definition fingerprint", re.compile(r"^- Definition fingerprint: ([0-9a-f]{8})$")),
)


@dataclass
class Finding:
    condition: str
    line: int
    message: str

    def __str__(self):
        return "fail: %s — line %d: %s" % (self.condition, self.line, self.message)


@dataclass
class Section:
    name: str
    heading_line: int
    lines: list  # (line number, text) of every line up to the next heading


def split(text):
    """Return the lines of the definition outside its sections, and its sections in order.

    A line inside a fenced block is never a heading."""
    preamble, sections, fenced = [], [], False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE.match(line):
            fenced = not fenced
        heading = None if fenced else HEADING.match(line)
        if heading:
            sections.append(Section(heading.group(1), number, []))
        elif sections:
            sections[-1].lines.append((number, line))
        else:
            preamble.append((number, line))
    return preamble, sections


def check_structure(preamble, sections):
    findings = []
    status = [(n, line) for n, line in preamble if line.startswith("Status:")]
    if not status:
        findings.append(Finding("structure", 1, "no `Status:` line above the first section"))
    elif not STATUS.match(status[0][1].rstrip()):
        findings.append(Finding("structure", status[0][0], "the status reads none of "
                                "`definition — open: <sections>`, `ready for gate`, "
                                "`approved YYYY-MM-DD`"))
    names = [s.name for s in sections]
    for section in sections:
        if section.name not in SECTIONS:
            findings.append(Finding("structure", section.heading_line,
                                    "`## %s` is no section of the template" % section.name))
        elif names.count(section.name) > 1 and names.index(section.name) != sections.index(section):
            findings.append(Finding("structure", section.heading_line,
                                    "`## %s` stands a second time" % section.name))
    for name in SECTIONS:
        if name not in names:
            findings.append(Finding("structure", 1, "the section `## %s` is missing" % name))
    known = [name for name in dict.fromkeys(names) if name in SECTIONS]
    if known != [name for name in SECTIONS if name in known]:
        line = next(s.heading_line for s in sections if s.name in SECTIONS)
        findings.append(Finding("structure", line, "the sections stand out of the template's "
                                "order: %s" % ", ".join(known)))
    return findings


def content(section):
    return [(n, line) for n, line in section.lines if line.strip()]


def check_gaps(sections):
    findings = []
    for section in sections:
        lines = content(section)
        if not lines:
            findings.append(Finding("a", section.heading_line, "`## %s` is empty — write `none` "
                                    "or `TODO`" % section.name))
        for number, line in lines:
            if TODO.search(line):
                findings.append(Finding("a", number, "`## %s` holds TODO" % section.name))
    return findings


def items(section):
    """Return each list item of a section as (first line number, its text joined over the
    indented lines that continue it), and every other line of text as (number, None)."""
    result = []
    for number, line in content(section):
        if ITEM.match(line):
            result.append([number, line[2:].strip()])
        elif line.startswith((" ", "\t")) and result and result[-1][1] is not None:
            result[-1][1] += " " + line.strip()
        else:
            result.append([number, None])
    return result


def check_open_questions(section):
    findings = []
    lines = content(section)
    if [line.strip() for _, line in lines] == ["none"]:
        return findings
    for number, text in items(section):
        if text is None:
            findings.append(Finding("d", number, "a line under `## %s` that is no question "
                                    "item" % OPEN_QUESTIONS))
        elif not RESOLVED.search(text):
            findings.append(Finding("d", number, "the question names no place it is resolved "
                                    "in — end it with `— resolved in: breakdown` or "
                                    "`— resolved in: task: <name>`"))
    return findings


def check_approvals(section):
    return [Finding("b", number, "a projected decision still reads `Approved by: on acceptance`")
            for number, line in section.lines if PENDING_APPROVAL.match(line)]


def definition_fingerprint(text):
    """The fingerprint of the definition: of its text from the `## Goal` line up to the
    `## Gate record` line, that line left out."""
    lines = text.splitlines()
    _, sections = split(text)
    start = next(s.heading_line for s in sections if s.name == SECTIONS[0])
    end = next(s.heading_line for s in sections if s.name == GATE_RECORD)
    return fingerprint("\n".join(lines[start - 1:end - 1]))


def check_gate_record(section, text):
    findings = []
    lines = content(section)
    if len(lines) != len(GATE_LINES):
        return [Finding("e", section.heading_line, "the gate record holds %d lines, not the "
                        "three: Approved by, Foundation searched at, Definition fingerprint"
                        % len(lines))]
    for (number, line), (name, form) in zip(lines, GATE_LINES):
        match = form.match(line.rstrip())
        if not match:
            findings.append(Finding("e", number, "the line is not `- %s: …` in its form" % name))
        elif name == "Definition fingerprint" and match.group(1) != definition_fingerprint(text):
            findings.append(Finding("e", number, "the fingerprint %s does not match the "
                                    "definition, whose fingerprint is %s — the definition "
                                    "changed after the gate and goes through it again"
                                    % (match.group(1), definition_fingerprint(text))))
    return findings


def check(text, before_approval=False):
    preamble, sections = split(text)
    findings = check_structure(preamble, sections)
    if findings:
        return findings
    by_name = {s.name: s for s in sections}
    checked = [s for s in sections if not (before_approval and s.name == GATE_RECORD)]
    findings += check_gaps(checked)
    findings += check_open_questions(by_name[OPEN_QUESTIONS])
    if not before_approval:
        findings += check_approvals(by_name[PROJECTED])
        findings += check_gate_record(by_name[GATE_RECORD], text)
    return sorted(findings, key=lambda f: f.line)


def read(path):
    try:
        with open(path, encoding="utf-8", newline="") as handle:
            return handle.read(), None
    except FileNotFoundError:
        return None, "no file %s" % path
    except UnicodeDecodeError:
        return None, "%s is not UTF-8 text" % path
    except OSError as error:
        return None, "cannot read %s: %s" % (path, error.strerror)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a project definition against the "
                                     "conditions of the readiness gate a script decides.")
    parser.add_argument("definition", help="the project definition, a Markdown file")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--before-approval", action="store_true",
                      help="leave out the approvals and the gate record")
    mode.add_argument("--fingerprint", action="store_true",
                      help="print the fingerprint the gate record is to carry")
    args = parser.parse_args(argv)
    text, error = read(args.definition)
    if error:
        print("error: " + error, file=sys.stderr)
        return 2
    if args.fingerprint:
        findings = check_structure(*split(text))
        if findings:
            for finding in findings:
                print(finding)
            return 1
        print(definition_fingerprint(text))
        return 0
    findings = check(text, before_approval=args.before_approval)
    for finding in findings:
        print(finding)
    left_out = " (approvals and gate record left out: --before-approval)" \
        if args.before_approval else ""
    print("readiness: %s%s" % ("%d finding(s)" % len(findings) if findings else "nothing found",
                               left_out))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
