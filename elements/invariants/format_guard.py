"""Format guard of a product's invariants file.

Runs the checks listed in "What the format guard checks" in template.md, which lies next to this
script. The fields of an entry and the words each may hold, the titles and columns of the lists,
the values the gate fills in and the words a sentence may not use are read from the template, so
the rules of an entry live in one place (WAY-05, WAY-35). The decision log and the part map are
read with the parsers of their own guards.

Usage, from the root of the product's repository:

    python <the-way>/elements/invariants/format_guard.py [FILE] [--base REF]

FILE defaults to foundations/invariants.md. --base names the commit the task branch left the main
branch from; without it, the checks against that commit are reported as unchecked. Exit code: 0
without errors, 1 with errors, 2 when the file or the template cannot be read.
"""

import argparse
import importlib.util
import os
import re
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_FILE = os.path.join(HERE, "..", "..", "foundations", "invariants.md")

sys.dont_write_bytecode = True


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


decision_guard = _load("decision_format_guard", os.path.join(HERE, "..", "decisions", "format_guard.py"))
map_guard = _load("part_map_format_guard", os.path.join(HERE, "..", "part-map", "format_guard.py"))
fingerprint = decision_guard.fingerprint
count_sentences = decision_guard.count_sentences

IDENTIFIER = map_guard.IDENTIFIER
DATE = r"\d{4}-\d{2}-\d{2}"
QUOTED = r'"[^"]*"|“[^”]*”'


class TemplateError(Exception):
    pass


# --- rules read from the template -----------------------------------------------------------


@dataclass
class FieldRule:
    name: str
    none: bool      # the form gives the field the word `none`
    todo: bool      # the form gives the field the word `TODO`


@dataclass
class Rules:
    fields: list                 # FieldRule, in the order of the form
    lists: list                  # (title, columns) of the lists closing the file, in order
    violated_file: str           # name of the derived file beside the invariants file
    violated_title: str
    violated_columns: list
    gate_values: list            # values the gate fills in, e.g. {fork-point}
    forbidden_words: list        # words no sentence holds outside quoted text


def _section(text, title):
    """The text under a heading of the template, up to the next one outside a code block."""
    found, fenced, lines = None, False, []
    for line in text.split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        elif line.startswith("## ") and not fenced:
            if found:
                break
            found = line[3:].strip() == title
            continue
        if found:
            lines.append(line)
    if not found:
        raise TemplateError('section "%s" not found' % title)
    return "\n".join(lines)


def _blocks(section_text):
    return re.findall(r"```markdown\n(.*?)```", section_text, re.S)


def _table_form(block):
    title = re.search(r"^## (.+)$", block, re.M)
    header = re.search(r"^\|(.+)\|$", block, re.M)
    if not title or not header:
        raise TemplateError("a list form has no title or no columns")
    return title.group(1).strip(), [cell.strip() for cell in header.group(1).split("|")]


def bare(value):
    """A value without the backticks that mark it as a literal word."""
    value = value.strip()
    if len(value) > 1 and value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        return value[1:-1]
    return value


def is_todo(value):
    value = bare(value)
    return value == "TODO" or value.startswith("TODO ")


def read_rules(path=TEMPLATE):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    entry_section = _section(text, "Entry")
    blocks = _blocks(entry_section)
    if len(blocks) < 2:
        raise TemplateError('the section "Entry" does not hold the entry and its lists')
    fields = []
    for name, form in re.findall(r"^- \*\*(.+?):\*\* (.*)$", blocks[0], re.M):
        choices = [bare(choice) for choice in form.split(" | ")]
        fields.append(FieldRule(name, "none" in choices,
                                any(choice == "TODO" or choice.startswith("TODO ") for choice in choices)))
    if not fields:
        raise TemplateError("the entry form has no fields")
    lists = [_table_form(block) for block in blocks[1:]]

    violated_section = _section(text, "Violated invariants")
    violated_file = re.search(r"`foundations/([^`]+\.md)`", violated_section)
    violated_blocks = _blocks(violated_section)
    if not violated_file or not violated_blocks:
        raise TemplateError("the section on violated invariants names no file or no form")
    violated_title, violated_columns = _table_form(violated_blocks[0])

    gate_values = re.findall(r"`(\{[a-z-]+\})`", _section(text, "Method"))
    if not gate_values:
        raise TemplateError("the section on the method lists no value the gate fills in")

    checks = _section(text, "What the format guard checks")
    words = re.search(r"^- No sentence, outside quoted text, contains the words (.*)$", checks, re.M)
    if not words:
        raise TemplateError("the list of checks names no words a sentence may not hold")
    return Rules(fields, lists, violated_file.group(1), violated_title, violated_columns,
                 gate_values, re.findall(r'"([^"]+)"', words.group(1)))


# --- parsing the file -----------------------------------------------------------------------


@dataclass
class Entry:
    line: int
    identifier: str
    version: int
    sentence: str = None
    fields: dict = field(default_factory=dict)   # name -> [value, line]
    strays: list = field(default_factory=list)   # lines of text outside the sentence and fields
    text: str = ""


@dataclass
class Table:
    line: int
    title: str
    columns: list
    rows: list = field(default_factory=list)     # (cells, line)


def parse_table(title, line, lines):
    table = Table(line, title, [])
    for offset, row in enumerate(lines, start=line + 1):
        if not row.startswith("|"):
            continue
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if set(row.replace("|", "").strip()) <= set("-: "):
            continue
        if not table.columns:
            table.columns = cells
        else:
            table.rows.append((cells, offset))
    return table


def stray_lines(body, first_line):
    """Lines after the sentence that are neither a field nor a field's continuation."""
    in_field, strays = False, []
    for offset, line in enumerate(body, start=first_line):
        if re.match(r"^- \*\*(.+?):\*\*", line):
            in_field = True
        elif not line.strip():
            in_field = False
        elif not (in_field and line.startswith(" ")):
            strays.append(offset)
    return strays


def parse_file(text, rules):
    """Entries, the lists closing the file, and headings that are neither, in file order."""
    items, list_titles = [], [title for title, _ in rules.lists]
    for line, lines in map_guard.split_sections(text):
        heading = lines[0][3:].strip()
        match = re.match(r"^(\S+)/(\d+)$", heading)
        if heading in list_titles:
            items.append(parse_table(heading, line, lines[1:]))
            continue
        if not match:
            items.append(("unknown", line, heading))
            continue
        entry = Entry(line, match.group(1), int(match.group(2)), text="\n".join(lines).rstrip())
        body = lines[1:]
        index = 0
        while index < len(body) and not body[index].strip():
            index += 1
        paragraph = []
        while index < len(body) and body[index].strip() and not body[index].startswith("- **"):
            paragraph.append(body[index])
            index += 1
        entry.sentence = "\n".join(paragraph) or None
        entry.fields = map_guard.parse_fields(body[index:], line + 1 + index)
        entry.strays = stray_lines(body[index:], line + 1 + index)
        items.append(entry)
    return items


def flat(value):
    return " ".join(value.split())


def listed(value):
    return [item.strip() for item in flat(value).split(" · ") if item.strip()]


# --- the report -----------------------------------------------------------------------------


Report = map_guard.Report


# --- checks ---------------------------------------------------------------------------------


@dataclass
class Foundation:
    """What the checks read beside the invariants file."""
    root: str = None
    parts: set = field(default_factory=set)
    map_identifiers: set = field(default_factory=set)
    flow_invariants: set = field(default_factory=set)
    prefix: str = None
    decisions: dict = field(default_factory=dict)    # number -> fingerprint of its latest binding


def read_foundation(path, report):
    foundation = Foundation()
    directory = os.path.dirname(os.path.abspath(path))
    code, top = map_guard.git(["rev-parse", "--show-toplevel"], directory)
    foundation.root = top.strip() if code == 0 else None

    map_path = os.path.join(directory, "part_map.md")
    try:
        map_rules = map_guard.read_rules()
        with open(map_path, encoding="utf-8") as handle:
            entries, sections = map_guard.parse_map(handle.read(), map_rules)
    except (OSError, map_guard.TemplateError, AttributeError) as problem:
        report.error(None, "cannot read the part map beside the file: %s" % problem)
        entries, sections = [], {}
    for entry in entries:
        foundation.map_identifiers.add(entry.identifier)
        if entry.kind == "part":
            foundation.parts.add(entry.identifier)
        if entry.kind == "critical flow" and "Invariant" in entry.fields:
            named = flat(entry.fields["Invariant"][0]).split(" — test:")[0].strip()
            if re.fullmatch(IDENTIFIER, named):
                foundation.flow_invariants.add(named)
            else:
                report.cannot_check("whether a quarantine names the invariant of `%s`"
                                    % entry.identifier,
                                    "the flow names its invariant in prose, not by identifier")
    for cells, _ in map_guard.rows(sections, "Withdrawn identifiers"):
        if cells:
            foundation.map_identifiers.add(cells[0])

    log_path = os.path.join(directory, "decisions.md")
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as handle:
            log = handle.read()
        foundation.prefix = decision_guard.detect_prefix(log)
        if foundation.prefix:
            latest = {entry.number: entry for entry in decision_guard.parse_log(log, foundation.prefix)
                      if entry.kind == "version"}
            foundation.decisions = {number: fingerprint(entry.binding)
                                    for number, entry in latest.items() if entry.binding is not None}
    return foundation


def check_layout(items, rules, report):
    """Entries first, then the lists in the template's order, the last closing the file."""
    titles = [title for title, _ in rules.lists]
    seen = []
    for item in items:
        if isinstance(item, tuple):
            report.error(item[1], "heading `## %s` is neither `## <identifier>/<version>` nor a "
                                  "list of the template" % item[2])
        elif isinstance(item, Table):
            if item.title in seen:
                report.error(item.line, "the list `%s` stands twice" % item.title)
            seen.append(item.title)
            expected = dict(rules.lists)[item.title]
            if item.columns != expected:
                report.error(item.line, "the list `%s` has columns %s, not %s"
                             % (item.title, " | ".join(item.columns), " | ".join(expected)))
        elif seen:
            report.error(item.line, "entry `%s` stands after the list `%s`"
                         % (item.identifier, seen[-1]))
    for title in titles:
        if title not in seen:
            report.error(None, "the file has no list `%s`" % title)
    if [title for title in seen if title in titles] != [title for title in titles if title in seen]:
        report.error(None, "the lists closing the file are not in the order %s"
                     % ", ".join("`%s`" % title for title in titles))


def check_identifiers(entries, withdrawn, foundation, report):
    seen = {}
    for identifier, line in [(entry.identifier, entry.line) for entry in entries] + \
            [(cells[0], line) for cells, line in withdrawn]:
        if identifier == "none" or not re.fullmatch(IDENTIFIER, identifier):
            report.error(line, "`%s` is not an identifier of words in lower case joined by "
                               "hyphens" % identifier)
        elif identifier in seen:
            report.error(line, "identifier `%s` is used twice (line %d)" % (identifier, seen[identifier]))
        elif identifier in foundation.map_identifiers:
            report.error(line, "identifier `%s` is held by the part map" % identifier)
        seen.setdefault(identifier, line)
    names = set(seen)
    for cells, line in withdrawn:
        successors = cells[1] if len(cells) > 1 else ""
        if successors == "none":
            continue
        for successor in listed(successors) or [""]:
            if successor not in names:
                report.error(line, "withdrawn `%s` names successor `%s`, which is neither an entry "
                                   "nor a withdrawn identifier of this file" % (cells[0], successor))


def check_fields(entry, rules, report):
    label = "%s/%d" % (entry.identifier, entry.version)
    names = [rule.name for rule in rules.fields]
    for name, (value, line) in entry.fields.items():
        if name not in names:
            report.error(line, "%s: field *%s* is not in the template" % (label, name))
    for rule in rules.fields:
        if rule.name not in entry.fields or not entry.fields[rule.name][0].strip():
            report.error(entry.line, "%s: field *%s* is missing" % (label, rule.name))
            continue
        value, line = entry.fields[rule.name]
        if bare(value) == "none" and not rule.none:
            report.error(line, "%s: *%s* may not hold `none`" % (label, rule.name))
        if is_todo(value) and not rule.todo:
            report.error(line, "%s: *%s* may not hold `TODO`" % (label, rule.name))


def value_of(entry, name):
    return entry.fields.get(name, ["", entry.line])


def command_of(entry):
    """The command a method names, or None where the method is a path or `TODO`."""
    value = flat(value_of(entry, "Method")[0])
    if is_todo(value) or not (value.startswith("`") and value.endswith("`")):
        return None
    return bare(value)


def check_sentence(entry, rules, report):
    label = "%s/%d" % (entry.identifier, entry.version)
    if entry.sentence is None:
        report.error(entry.line, "%s: the sentence is missing" % label)
        return
    line = entry.line + 2
    sentences = count_sentences(entry.sentence)
    if sentences != 1:
        report.error(line, "%s: %d sentences, an entry states one" % (label, sentences))
    for offset in entry.strays:
        report.error(offset, "%s: text outside the sentence and the fields; an entry states one "
                             "sentence" % label)
    unquoted = re.sub(QUOTED, " ", flat(entry.sentence))
    for words in rules.forbidden_words:
        if re.search(r"\b%s(?:es)?\b" % re.escape(words), unquoted, re.I):
            report.error(line, '%s: the sentence names "%s" outside quoted text' % (label, words))
    if re.search(r"~\s*\w", unquoted):
        report.error(line, "%s: the sentence states a bound with a tilde, not a number" % label)
    command = command_of(entry)
    for value in re.findall(r"\{[^{}\s]*\}", unquoted):
        if value not in rules.gate_values:
            report.error(line, "%s: `%s` is not a value the gate fills in (%s)"
                         % (label, value, ", ".join(rules.gate_values)))
        elif command is not None and value not in command:
            report.error(line, "%s: the sentence names `%s`, which its command does not take"
                         % (label, value))


def check_method(entry, rules, foundation, report):
    label = "%s/%d" % (entry.identifier, entry.version)
    raw, line = value_of(entry, "Method")
    value = flat(raw)
    if not value or is_todo(value):
        return
    command = command_of(entry)
    if command is not None:
        tokens = command.split()
        if not tokens or re.search(r"[/\\]", tokens[0]):
            report.error(line, "%s: a command begins with the name of the program it runs, not a "
                               "path" % label)
        for taken in re.findall(r"\{[^{}]*\}", command):
            if taken not in rules.gate_values:
                report.error(line, "%s: the command takes `%s`, which is not a value the gate fills "
                                   "in (%s)" % (label, taken, ", ".join(rules.gate_values)))
        return
    if "`" in value or " " in value:
        report.error(line, "%s: *Method* is neither a command in backticks, the path of a file, "
                           "nor `TODO`" % label)
    elif foundation.root is None:
        report.cannot_check("the path in the method of `%s`" % entry.identifier,
                            "the file is not in a git repository")
    elif not os.path.isfile(os.path.join(foundation.root, value)):
        report.error(line, "%s: *Method* names `%s`, which is not a file" % (label, value))


def check_links(entry, foundation, report):
    label = "%s/%d" % (entry.identifier, entry.version)
    rests, line = value_of(entry, "Rests on")
    if rests.strip() and bare(rests) != "none" and not is_todo(rests):
        report.error(line, "%s: *Rests on* names a fact, but the environment facts element has "
                           "no entries; the fact is written as `TODO — <the fact, with its "
                           "source>`" % label)

    derives, line = value_of(entry, "Derives from")
    if not derives.strip() or bare(derives) == "none" or is_todo(derives):
        return
    if foundation.prefix is None:
        report.error(line, "%s: *Derives from* names decisions, but there is no decision log "
                           "beside the file" % label)
        return
    for item in listed(derives):
        match = re.fullmatch(r"%s-(\d{2,})@([0-9a-f]+)" % re.escape(foundation.prefix), item)
        if not match:
            report.error(line, "%s: `%s` is not `%s-NN@<fingerprint>`" % (label, item, foundation.prefix))
        elif int(match.group(1)) not in foundation.decisions:
            report.error(line, "%s: `%s` names a decision that does not exist or binds nothing "
                               "any more" % (label, item))
        elif foundation.decisions[int(match.group(1))] != match.group(2):
            report.error(line, "%s: `%s` — the current fingerprint of %s-%s is %s"
                         % (label, item, foundation.prefix, match.group(1),
                            foundation.decisions[int(match.group(1))]))


def derives_from_a_decision(entry):
    derives = value_of(entry, "Derives from")[0]
    return bool(derives.strip()) and bare(derives) != "none" and not is_todo(derives)


def check_part(entry, foundation, report):
    label = "%s/%d" % (entry.identifier, entry.version)
    value, line = value_of(entry, "Part")
    if not value.strip() or is_todo(value) or bare(value) == "none":
        return
    parts = listed(value)
    if "every" in parts and len(parts) > 1:
        report.error(line, "%s: *Part* names `every` and parts at once" % label)
    for part in parts:
        if part != "every" and part not in foundation.parts:
            report.error(line, "%s: *Part* names `%s`, which is not a part of the part map"
                         % (label, part))


def check_correction_and_recovered(entry, report):
    label = "%s/%d" % (entry.identifier, entry.version)
    correction, line = value_of(entry, "Correction")
    declared = re.fullmatch(r"([0-9a-f]+) → ([0-9a-f]+)", flat(correction))
    if correction.strip() and bare(correction) != "none" and not declared:
        report.error(line, "%s: *Correction* is neither `none` nor `<fingerprint> → <fingerprint>`"
                     % label)
    elif declared and entry.sentence is not None and \
            declared.group(2) != fingerprint(entry.sentence):
        report.error(line, "%s: *Correction* names %s as the current fingerprint, but it is %s"
                     % (label, declared.group(2), fingerprint(entry.sentence)))
    recovered, line = value_of(entry, "Recovered")
    if not recovered.strip() or bare(recovered) == "none":
        return
    if not re.fullmatch(r"recovered — searched: .+; found: .+", flat(recovered)):
        report.error(line, "%s: *Recovered* is neither `none` nor `recovered — searched: …; "
                           "found: …`" % label)
    elif derives_from_a_decision(entry):
        report.error(line, "%s: *Recovered* is not `none`, while *Derives from* names a decision"
                     % label)


def check_quarantine(table, entries, foundation, report):
    for cells, line in table.rows if table else []:
        if len(cells) < 3:
            report.error(line, "a quarantine position needs an identifier, a version and a date")
            continue
        identifier, version, until = cells[:3]
        entry = entries.get(identifier)
        if entry is None:
            report.error(line, "quarantine names `%s`, which is not an entry" % identifier)
        elif version != str(entry.version):
            report.error(line, "quarantine names `%s` at version %s; its current version is %d"
                         % (identifier, version, entry.version))
        if not re.fullmatch(DATE, until) or not decision_guard.valid_date(until):
            report.error(line, "quarantine of `%s` ends on `%s`, which is not a date YYYY-MM-DD"
                         % (identifier, until))
        if identifier in foundation.flow_invariants:
            report.error(line, "quarantine names `%s`, which a critical flow names" % identifier)


def violated_tables(text, rules):
    return [parse_table(rules.violated_title, line, lines[1:])
            for line, lines in map_guard.split_sections(text)
            if lines[0][3:].strip() == rules.violated_title]


def violated_positions(text, rules):
    return [row for table in violated_tables(text, rules) for row in table.rows]


def check_violated(path, entries, rules, report):
    violated_path = os.path.join(os.path.dirname(os.path.abspath(path)), rules.violated_file)
    if not os.path.exists(violated_path):
        report.notes.append("there is no %s; the list of violated invariants is read as empty"
                            % rules.violated_file)
        return []
    with open(violated_path, encoding="utf-8") as handle:
        tables = violated_tables(handle.read(), rules)
    for table in tables:
        if table.columns != rules.violated_columns:
            report.error(None, "%s:%d: the list has columns %s, not %s"
                         % (rules.violated_file, table.line, " | ".join(table.columns),
                            " | ".join(rules.violated_columns)))
    positions = [row for table in tables for row in table.rows]
    for cells, line in positions:
        identifier, version = (cells + ["", ""])[:2]
        entry = entries.get(identifier)
        where = "%s:%d" % (rules.violated_file, line)
        if entry is None:
            report.error(None, "%s: `%s` is not an entry" % (where, identifier))
        elif version != str(entry.version):
            report.error(None, "%s: `%s` at version %s; its current version is %d"
                         % (where, identifier, version, entry.version))
    return [(cells[0], cells[1]) for cells, _ in positions if len(cells) > 1]


# --- the commit the branch left the main branch from ---------------------------------------


def check_against_base(path, entries, withdrawn, violated, rules, base, report):
    directory = os.path.dirname(os.path.abspath(path))
    code, top = map_guard.git(["rev-parse", "--show-toplevel"], directory)
    if code != 0:
        report.error(None, "--base %s given, but the file is not in a git repository" % base)
        return
    code, _ = map_guard.git(["rev-parse", "--verify", "--quiet", base + "^{commit}"], directory)
    if code != 0:
        report.error(None, "--base %s does not exist" % base)
        return
    relative = os.path.relpath(os.path.abspath(path), top.strip()).replace(os.sep, "/")
    code, base_text = map_guard.git(["show", "%s:%s" % (base, relative)], directory)
    if code != 0:
        report.notes.append("%s has no %s; every entry is new" % (base, relative))
        base_text = ""
    base_items = parse_file(base_text, rules)
    base_entries = {item.identifier: item for item in base_items if isinstance(item, Entry)}
    base_withdrawn = {cells[0] for item in base_items if isinstance(item, Table)
                      and item.title == rules.lists[0][0] for cells, _ in item.rows if cells}
    withdrawn_now = {cells[0] for cells, _ in withdrawn if cells}

    for identifier in sorted(set(base_entries) | base_withdrawn):
        if identifier not in entries and identifier not in withdrawn_now:
            report.error(None, "`%s` stands in the file on %s and is gone; it stays as an entry or "
                               "a withdrawn identifier" % (identifier, base))
    for identifier in sorted(base_withdrawn & set(entries)):
        report.error(entries[identifier].line, "`%s` is withdrawn on %s and stands as an entry "
                                               "again" % (identifier, base))

    for identifier, entry in entries.items():
        label = "%s/%d" % (identifier, entry.version)
        correction = flat(value_of(entry, "Correction")[0])
        if entry.sentence is None:
            continue
        now = fingerprint(entry.sentence)
        before = base_entries.get(identifier)
        if before is None or before.sentence is None:
            if entry.version != 1:
                report.error(entry.line, "%s: a new entry carries version 1" % label)
            if bare(correction) != "none":
                report.error(entry.line, "%s: a new entry declares no correction" % label)
            continue
        then = fingerprint(before.sentence)
        declared = re.fullmatch(r"([0-9a-f]+) → ([0-9a-f]+)", correction)
        if now == then:
            if entry.version != before.version:
                report.error(entry.line, "%s: the sentence is unchanged since %s, where the version "
                                         "is %d" % (label, base, before.version))
            if declared and declared.group(2) != now:
                report.error(entry.line, "%s: the correction names %s, but the fingerprint is %s"
                             % (label, declared.group(2), now))
        elif entry.version == before.version + 1:
            if declared:
                report.error(entry.line, "%s: a raised version declares no correction" % label)
        elif entry.version == before.version and declared and \
                (declared.group(1), declared.group(2)) == (then, now):
            report.cannot_check("the correction of `%s`" % identifier,
                                "correction declared, confirmation not checked")
        else:
            report.error(entry.line, "%s: the sentence changed since %s (%s → %s); the version is "
                                     "%d, or a correction names `%s → %s`"
                         % (label, base, then, now, before.version + 1, then, now))
        if now != then and flat(before.sentence) in flat(entry.text.replace(entry.sentence, "", 1)):
            report.error(entry.line, "%s: the entry still holds its wording from %s" % (label, base))

    code, base_violated = map_guard.git(["show", "%s:%s" % (
        base, os.path.join(os.path.dirname(relative), rules.violated_file).replace(os.sep, "/"))],
        directory)
    allowed = {(cells[0], cells[1]) for cells, _ in violated_positions(base_violated, rules)
               if len(cells) > 1} if code == 0 else set()
    for position in violated:
        if position not in allowed:
            report.error(None, "%s: `%s` at version %s is not on the list on %s; a position is "
                               "added only by a foundation change a human accepts"
                         % (rules.violated_file, position[0], position[1], base))


# --- citations in checks --------------------------------------------------------------------


CITATION = re.compile(r"^\s*(?:#|//|--|;|%|\*|/\*|<!--|REM\b)\s*(invariant|data):\s*(\S+)\s*"
                      r"(?:\*/|-->)?\s*$")


def check_citations(entries, withdrawn, foundation, report):
    if foundation.root is None:
        report.cannot_check("the `invariant:` and `data:` lines of checks",
                            "the file is not in a git repository")
        return
    code, listing = map_guard.git(["ls-files", "-z"], foundation.root)
    successors = {cells[0]: (cells[1] if len(cells) > 1 else "none") for cells, _ in withdrawn}
    for name in [name for name in listing.split("\0") if name]:
        if name.endswith(".md"):
            continue
        try:
            with open(os.path.join(foundation.root, name), encoding="utf-8") as handle:
                lines = handle.read().split("\n")
        except (OSError, UnicodeDecodeError):
            continue
        found = [(number, match.group(1), match.group(2))
                 for number, match in ((number, CITATION.match(line))
                                       for number, line in enumerate(lines, start=1)) if match]
        if not any(kind == "invariant" and re.fullmatch(r"%s(?:/\S*)?" % IDENTIFIER, value)
                   for _, kind, value in found):
            continue
        for number, kind, value in found:
            where = "%s:%d" % (name, number)
            if kind == "data":
                if not os.path.isfile(os.path.join(foundation.root, value)):
                    report.error(None, "%s: `data: %s` names no file" % (where, value))
                continue
            cited = re.fullmatch(r"(\S+)/(\d+)", value)
            if not cited:
                report.error(None, "%s: `invariant: %s` does not cite `<identifier>/<version>`"
                             % (where, value))
            elif cited.group(1) in successors:
                report.error(None, "%s: cites `%s`, which is withdrawn (successors: %s)"
                             % (where, cited.group(1), successors[cited.group(1)]))
            elif cited.group(1) not in entries:
                report.error(None, "%s: cites `%s`, which is not an entry" % (where, cited.group(1)))
            elif int(cited.group(2)) != entries[cited.group(1)].version:
                report.error(None, "%s: cites `%s`, whose current version is %d"
                             % (where, value, entries[cited.group(1)].version))


# --- the examples ---------------------------------------------------------------------------


def check_examples(items, examples_path, report):
    with open(examples_path, encoding="utf-8") as handle:
        examples = handle.read()
    by_heading = {item.text.split("\n")[0]: item for item in items if isinstance(item, Entry)}
    for line, lines in map_guard.split_sections(examples):
        copy = "\n".join(lines).rstrip()
        entry = by_heading.get(lines[0])
        if entry is None:
            report.error(None, "examples.md:%d: `%s` is not in the file" % (line, lines[0]))
        elif entry.text != copy:
            report.error(entry.line, "examples.md:%d differs from the file" % line)


# --- entry point ----------------------------------------------------------------------------


def run(path, base=None, stream=None, template=TEMPLATE):
    stream = stream or sys.stdout
    try:
        rules = read_rules(template)
    except (OSError, TemplateError, AttributeError) as problem:
        stream.write("cannot read the rules from %s: %s\n" % (template, problem))
        return 2
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as problem:
        stream.write("cannot read the invariants file: %s\n" % problem)
        return 2

    report = Report(path)
    if os.path.basename(path) != "invariants.md" or \
            os.path.basename(os.path.dirname(os.path.abspath(path))) != "foundations":
        report.error(None, "a product's invariants stand in foundations/invariants.md")
    foundation = read_foundation(path, report)
    items = parse_file(text, rules)
    check_layout(items, rules, report)
    entry_list = [item for item in items if isinstance(item, Entry)]
    entries = {}
    for entry in entry_list:
        entries.setdefault(entry.identifier, entry)
    tables = {item.title: item for item in items if isinstance(item, Table)}
    withdrawn_table = tables.get(rules.lists[0][0])
    withdrawn = withdrawn_table.rows if withdrawn_table else []

    check_identifiers(entry_list, withdrawn, foundation, report)
    for entry in entry_list:
        check_fields(entry, rules, report)
        check_sentence(entry, rules, report)
        check_method(entry, rules, foundation, report)
        check_links(entry, foundation, report)
        check_part(entry, foundation, report)
        check_correction_and_recovered(entry, report)
    check_quarantine(tables.get(rules.lists[-1][0]), entries, foundation, report)
    violated = check_violated(path, entries, rules, report)
    check_citations(entries, withdrawn, foundation, report)

    if base:
        check_against_base(path, entries, withdrawn, violated, rules, base, report)
    else:
        report.cannot_check("identifiers, versions and corrections against the commit the branch "
                            "left the main branch from", "no --base given")
        report.cannot_check("the list of violated invariants against that commit", "no --base given")

    if os.path.exists(EXAMPLES) and os.path.exists(OWN_FILE) and os.path.samefile(path, OWN_FILE):
        check_examples(items, EXAMPLES, report)
    report.print(stream)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a product's invariants against the template.")
    parser.add_argument("file", nargs="?", default=os.path.join("foundations", "invariants.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.file, arguments.base)


if __name__ == "__main__":
    sys.exit(main())
