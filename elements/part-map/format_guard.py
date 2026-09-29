"""Format guard of a product's part map.

Checks a map against template.md, which lies next to this script. The fields of each kind of
entry, the words `none` and `TODO` each field takes and the titles of the lists are read from the
forms of the template, so the rules of an entry live in one place (WAY-35, WAY-71). Each check
cites the invariants it gives a verdict for, as `invariant: <identifier>/<version>` (WAY-65).

An entry's heading is its identifier alone, and a critical flow's test is found by a comment line
`# flow: <identifier>` in a file git tracks, never by a path in the map. An entry that carries what
the form does not have — a heading `## <identifier> — <title>`, a test named after `— test:` in a
flow's *Invariant*, a pattern of *Files* marked `(generated)` — is reported, and the identifier,
the invariant and the pattern are still read from it, so that every other check runs on it.

Usage, from the root of the product's repository:

    python <the-way>/elements/part-map/format_guard.py [MAP] [--base REF] [--record PATH]

MAP defaults to foundations/part_map.md. --base names the commit the task branch left the main
branch from, which the list of known violations is compared with; without it, that check is
skipped. Given it, the report for a person also warns of every part whose computed criticality is
lower than on that commit, for the human who accepts the lowering (WAY-46). `none` in place of that
commit is the value the gate fills in where it does not exist (WAY-61): the check is then recorded
as `unchecked`, a note says that no criticality is compared, and the run gives no error; a commit
that is not `none` and does not exist stays an error. A `TODO` in any field of an entry is an
error on every run, since the template gives it to no field (WAY-71). --record names a JSON Lines
file, created or overwritten, which receives the-way's own record of the run (WAY-74): a verdict
for each invariant cited by a check the run's options select — the check against the base with
--base, the checks of the map alone without it — a line for each error of those checks that
belongs to no cited invariant, and every failure of the run itself. The report for a person holds
every check.
Exit code: 0 without errors, 1 with errors, 2 when the map or the template cannot be read or the
record cannot be written.
"""

import argparse
import importlib.util
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_MAP = os.path.join(HERE, "..", "..", "foundations", "part_map.md")

# The name a record gives this program, and each of its checks as PROGRAM::<function>.
PROGRAM = "elements/part-map/format_guard.py"
# The checks each option selects for the record; every other check reads the map alone and is
# recorded only by a run given neither option. A run records the checks its options select, and
# its own failures always (WAY-61, WAY-74).
SELECTED_BY = {"check_violations_growth": "--base"}
# A reason a check records for being unchecked, word for word as the invariants template lists it
# (WAY-63); the value the gate fills in for a commit that does not exist, and the reason that goes
# with it, come from the code the guards share.
NOT_PRODUCED_REASON = "the method's command or file is not declared or produced by the product"
# Where a product's part map stands, relative to the root of its repository (WAY-40).
MAP_PATH = "foundations/part_map.md"
# The directory every critical flow's test of the-way's own map lies under (WAY-55).
GATE_DIRECTORY = "gate/"

sys.dont_write_bytecode = True


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The code the format guards share (WAY-09), and the form of an identifier from the relation model.
shared = _load("elements_common_guard_shared",
               os.path.join(HERE, "..", "common", "guard_shared.py"))
identifier_form = _load("relation_model_identifier",
                        os.path.join(HERE, "..", "..", "relation-model", "identifier.py"))
NO_COMMIT = shared.NO_COMMIT
NO_COMMIT_REASON = shared.NO_COMMIT_REASON
TODO_WORD = shared.TODO_WORD
read_file = shared.read_file
split_sections = shared.split_sections
parse_fields = shared.parse_fields
describe = shared.describe
start_record = shared.start_record
write_record = shared.write_record
git = shared.git
call_git = shared.call_git
file_at = shared.file_at
find_commit = shared.find_commit

IDENTIFIER = identifier_form.IDENTIFIER
LIST_SECTIONS = ["Criticality scale", "External context", "Change paths",
                 "Files left out on purpose", "Withdrawn identifiers", "Known violations"]
# The lists of the map itself; the list of known violations stands in its own file (WAY-51).
MAP_LISTS = [title for title in LIST_SECTIONS if title != "Known violations"]
# The columns of the list of withdrawn identifiers the guard reads (WAY-41); the list's form
# stands in the rules the elements share.
WITHDRAWN_COLUMNS = ("Identifier", "Why", "Successors")
WITHDRAWN = "Withdrawn identifiers"
DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
# The heading of an entry, `## <identifier>`, told from the heading of a list by the fields the
# entry holds; and the heading with a title, `## <identifier> — <title>`, which the form does not
# use.
HEADING = re.compile(r"^## (\S+)[ \t]*$")
TITLED_HEADING = re.compile(r"^## (.+?) — (.+)$")
FIELD = re.compile(r"^- \*\*.+?:\*\*")
# The mark `(generated)` after a pattern of *Files*, which the form does not use.
GENERATED = re.compile(r"\s*\(generated\)\s*$")
# A comment line standing alone on its line that names the critical flow a test checks.
FLOW_LINE = re.compile(r"^[ \t]*#[ \t]*flow:[ \t]*(.*?)[ \t\r]*$", re.M)


TemplateError = shared.TemplateError


# --- words and values -----------------------------------------------------------------------


def bare(value):
    """A value without the backticks that mark it as a literal word."""
    value = (value or "").strip()
    if len(value) > 1 and value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        return value[1:-1]
    return value


def is_todo(value):
    value = bare(value)
    return value == "TODO" or value.startswith("TODO ")


def is_none(value):
    return bare(value) == "none"


def holds_todo(value):
    """Whether a value holds `TODO` as a word of its own anywhere in it (WAY-71)."""
    return bool(TODO_WORD.search(value or ""))


# --- rules read from the template -----------------------------------------------------------


@dataclass
class Rules:
    kinds: dict          # kind -> the field names of that kind, in the order of the template
    marks: dict          # field name -> kind, for the fields that name one kind alone
    lists: dict          # section title -> column names, empty for a numbered list
    values: dict         # section title -> the values a column allows, None where it is free
    violations: str      # the path of the derived list of known violations
    words: dict = field(default_factory=dict)   # kind -> field -> the words `none`, `TODO` it takes


def _section(text, title):
    """The body of a `## title` section, cut at the next heading outside a fenced block."""
    lines, body, inside, fenced = text.split("\n"), None, False, False
    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip() == title
            if inside:
                body = []
                continue
        if inside:
            body.append(line)
    if body is None:
        raise TemplateError('section "%s" not found' % title)
    return "\n".join(body)


def _code_block(text, title):
    match = re.search(r"```markdown\n(.*?)```", _section(text, title), re.S)
    if not match:
        raise TemplateError('no form in section "%s"' % title)
    return match.group(1)


def _field_words(form):
    """field name -> the words `none` and `TODO` the form gives it as an alternative of its own,
    read from the text of the field, its wrapped lines included, split at ` | `."""
    texts, current = {}, None
    for line in form.split("\n"):
        match = re.match(r"^- \*\*(.+?):\*\*(?: (.*))?$", line)
        if match:
            current = match.group(1)
            texts[current] = match.group(2) or ""
        elif current is not None and line.startswith(" "):
            texts[current] += " " + line.strip()
        else:
            current = None
    return {name: [word for word in ("none", "TODO")
                   if word in [bare(choice) for choice in text.split(" | ")]]
            for name, text in texts.items()}


def read_rules(path=TEMPLATE, common=shared.COMMON_RULES):
    """The rules of the map read from its template, and the form of the list of withdrawn
    identifiers from the rules the elements share (WAY-35, WAY-41)."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    kinds, words = {}, {}
    for title in ("Part", "Critical flow", "Surface"):
        form = _code_block(text, title)
        fields = re.findall(r"^- \*\*(.+?):\*\*", form, re.M)
        if not fields:
            raise TemplateError('no fields in the form of "%s"' % title)
        kinds[title.lower()] = fields
        words[title.lower()] = _field_words(form)

    marks = {}
    for kind, fields in kinds.items():
        for name in fields:
            if sum(name in other for other in kinds.values()) == 1:
                marks[name] = kind
    if len(set(marks.values())) != len(kinds):
        raise TemplateError("the kinds of entry cannot be told apart by their fields")

    lists, values = {}, {}
    for title in LIST_SECTIONS:
        if title == WITHDRAWN:
            continue
        form = _code_block(text, title)
        heading = re.search(r"^## (.+)$", form, re.M)
        if not heading:
            raise TemplateError('no heading in the form of "%s"' % title)
        table = [row for row in re.findall(r"^\|(.+)\|$", form, re.M)
                 if not set(row.replace("|", "").strip()) <= set("- ")]
        lists[heading.group(1)] = [cell.strip() for cell in table[0].split("|")] if table else []
        values[heading.group(1)] = [None if "<" in cell else
                                    [choice.strip() for choice in cell.split(" · ")]
                                    for cell in table[1].split("|")] if len(table) > 1 else []
    withdrawn_title, withdrawn_columns = shared.read_common(common)[1]
    if withdrawn_title != WITHDRAWN:
        raise TemplateError("the rules the elements share give no list `%s`" % WITHDRAWN)
    lists[WITHDRAWN], values[WITHDRAWN] = withdrawn_columns, []
    if not set(WITHDRAWN_COLUMNS) <= set(lists[WITHDRAWN]):
        raise TemplateError("the list of withdrawn identifiers has no column %s"
                            % " or ".join(WITHDRAWN_COLUMNS))
    violations = re.search(r"`([^`]+known_violations[^`]*)`", _section(text, "Known violations"))
    if not violations:
        raise TemplateError("the section on known violations names no file")
    return Rules(kinds, marks, lists, values, violations.group(1), words)


# --- parsing the map ------------------------------------------------------------------------


@dataclass
class Entry:
    line: int
    identifier: str
    title: str                                    # None, where the heading has no title
    kind: str = None
    binding: str = None
    fields: dict = field(default_factory=dict)   # name -> [value, line]
    text: str = ""                                # the entry as it stands in the file


@dataclass
class Section:
    line: int
    title: str
    rows: list = field(default_factory=list)     # (cells, line)


def entry_heading(lines):
    """(identifier, title) of a section that is an entry, its title None for a heading of the
    identifier alone; None for a section that is no entry. A heading of one word is an entry's
    when the section holds a field, and a list's otherwise."""
    titled = TITLED_HEADING.match(lines[0])
    if titled:
        return titled.group(1).strip(), titled.group(2).strip()
    heading = HEADING.match(lines[0])
    if heading and any(FIELD.match(line) for line in lines[1:]):
        return heading.group(1), None
    return None


def parse_map(text, rules):
    entries, sections = [], {}
    for line, lines in split_sections(text):
        heading = entry_heading(lines)
        if not heading:
            title = lines[0][3:].strip()
            section = Section(line, title)
            for offset, row in enumerate(lines[1:], start=line + 1):
                if row.startswith("|") and not set(row.replace("|", "").strip()) <= set("- "):
                    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
                    section.rows.append((cells, offset))
                elif re.match(r"^\d+\. ", row):
                    section.rows.append(([row.split(". ", 1)[1].strip()], offset))
            sections[title] = section
            continue

        entry = Entry(line, *heading)
        body = lines[1:]
        index = 0
        while index < len(body) and not body[index].strip():
            index += 1
        paragraph = []
        while index < len(body) and body[index].strip() and not body[index].startswith("- **"):
            paragraph.append(body[index])
            index += 1
        entry.binding = "\n".join(paragraph) or None
        entry.fields = parse_fields(body[index:], line + 1 + index)
        entry.kind = next((rules.marks[name] for name in entry.fields if name in rules.marks), None)
        entry.text = "\n".join(lines).rstrip()
        entries.append(entry)
    return entries, sections


def rows(sections, title):
    section = sections.get(title)
    return section.rows if section else []


def listed_rows(sections, title):
    """The rows of a list, without a row whose first cell is `TODO`, which names nothing; a `TODO`
    in any cell is reported by check_lists, and in the list of withdrawn identifiers by
    check_withdrawn."""
    return [(cells, line) for cells, line in rows(sections, title)
            if cells and not is_todo(cells[0])]


def identifiers(value):
    """The identifiers a field lists, from `first · second (separated — why)`; `none` lists none,
    and an item holding `TODO` is no identifier, which check_fields reports."""
    if not value or is_none(value):
        return []
    found = []
    for item in value.replace("\n", " ").split(" · "):
        if holds_todo(item):
            continue
        match = re.match(r"^(%s)\b" % IDENTIFIER, item.strip())
        if match:
            found.append(match.group(1))
    return found


def flow_invariant(value):
    """(invariant, test path) a flow's *Invariant* names, each None where it names none. A test
    path follows `— test:` only where the form is not kept."""
    flat = " ".join((value or "").split())
    test = re.search(r"(?:^|\s)test:\s*(\S.*)$", flat)
    name = flat[:test.start()] if test else flat
    name = re.sub(r"\s*—\s*$", "", name).strip()
    path = test.group(1).strip() if test else None
    return (name if name and not holds_todo(name) and not is_none(name) else None,
            path if path and not holds_todo(path) else None)


def flow_tests(top, tracked):
    """{identifier: [paths]} of the files git tracks holding a comment line `# flow: <identifier>`
    standing alone on its line; a value that is no identifier names no flow."""
    named = {}
    for path in tracked:
        try:
            with open(os.path.join(top, *path.split("/")), "rb") as handle:
                data = handle.read()
        except OSError:
            continue
        if b"flow:" not in data:
            continue
        for value in FLOW_LINE.findall(data.decode("utf-8", errors="replace")):
            if re.fullmatch(IDENTIFIER, value) and path not in named.get(value, []):
                named.setdefault(value, []).append(path)
    return named


# --- the report and the record of a run -----------------------------------------------------


class Report(shared.Report):
    """The report the guards share (WAY-74), naming this program and its checks in the record."""

    def __init__(self, path, options=()):
        super().__init__(path, options, program=PROGRAM, selected_by=SELECTED_BY)


# --- checks of the map's shape --------------------------------------------------------------


def check_sections(text, report):
    """Every `## ` section of the map is an entry or one of the lists the template names for the
    map (WAY-40)."""
    # invariant: map-section-kinds/1
    check, kinds = "check_sections", "map-section-kinds/1"
    report.ran(check, kinds)
    for line, lines in split_sections(text):
        if entry_heading(lines):
            continue
        title = lines[0][3:].strip()
        if title not in MAP_LISTS:
            report.error(line, "section `## %s` is neither an entry nor one of the lists the "
                               "template names for the map (%s)"
                         % (title, ", ".join(MAP_LISTS)), check, (kinds,))


def check_kinds(entries, rules, report):
    # invariant: map-entry-kinds/1
    # invariant: part-criticality-field/1
    check, kinds, criticality = "check_kinds", "map-entry-kinds/1", "part-criticality-field/1"
    report.ran(check, kinds, criticality)
    for entry in entries:
        carried = {rules.marks[name] for name in entry.fields if name in rules.marks}
        present = [kind for kind in rules.kinds if kind in carried]
        written = [name for name in entry.fields if "criticality" in name.lower()]
        if entry.kind is None:
            report.error(entry.line, "`%s` is neither a part, a critical flow nor a surface: "
                                     "no field of the template names its kind" % entry.identifier,
                         check, (kinds,))
        elif len(present) > 1:
            report.error(entry.line, "`%s` carries the fields of a %s: an entry is of one kind, "
                                     "and a part's criticality is computed, never written"
                         % (entry.identifier, " and of a ".join(present)), check,
                         (kinds, criticality) if "part" in present and written else (kinds,))
        elif entry.kind == "part" and written:
            report.error(entry.fields[written[0]][1], "%s: a part carries *%s*; its criticality is "
                                                      "computed, never written"
                         % (entry.identifier, written[0]), check, (criticality,))


def check_identifiers(entries, sections, report):
    # invariant: map-identifier-form/1
    # invariant: map-entry-version/1
    check, form, version = "check_identifiers", "map-identifier-form/1", "map-entry-version/1"
    report.ran(check, form, version)
    withdrawn = {cells[0]: line for cells, line in listed_rows(sections, "Withdrawn identifiers")}
    seen = {}
    for entry in entries:
        if entry.title is not None:
            report.error(entry.line, "`%s` carries a title after its identifier; an entry's "
                                     "heading is `## <identifier>`" % entry.identifier, check)
        if not re.match(r"^%s$" % IDENTIFIER, entry.identifier):
            report.error(entry.line, "`%s` is not an identifier of words in lower case joined by "
                                     "hyphens" % entry.identifier, check, (form,))
        if re.search(r"/\d+$", entry.identifier):
            report.error(entry.line, "`%s` carries a version; an entry of the map is edited in "
                                     "place" % entry.identifier, check, (version,))
        for name, (_, line) in entry.fields.items():
            if name.lower() == "version":
                report.error(line, "%s: *%s* is written; an entry of the map carries no version"
                             % (entry.identifier, name), check, (version,))
        if entry.identifier in seen:
            report.error(entry.line, "identifier `%s` is used twice, here and at line %d"
                         % (entry.identifier, seen[entry.identifier].line), check)
        else:
            seen[entry.identifier] = entry
        if entry.identifier in withdrawn:
            report.error(entry.line, "`%s` is withdrawn: a withdrawn identifier is never reused"
                         % entry.identifier, check)


def check_fields(entries, rules, report):
    """Every field of an entry's kind is present, and holds `none` or `TODO` only where the form
    of its kind gives it that word; a `TODO` the form gives is a warning (WAY-71)."""
    # invariant: map-entry-field-presence/1
    # invariant: map-entry-field-words/1
    check, presence, words = "check_fields", "map-entry-field-presence/1", "map-entry-field-words/1"
    report.ran(check, presence, words)
    for entry in entries:
        if entry.binding is None:
            report.error(entry.line, "%s: the binding sentence is missing" % entry.identifier,
                         check)
        if entry.kind is None:
            continue
        value, line = entry.fields.get("Files", ["", entry.line])
        for pattern in (value or "").split("\n"):
            pattern = pattern.strip()
            if pattern.startswith("- "):
                pattern = pattern[2:].strip()
            if GENERATED.search(pattern):
                report.error(line, "%s: `(generated)` follows the pattern `%s`; *Files* holds git "
                                   "path patterns alone"
                             % (entry.identifier, GENERATED.sub("", pattern)), check)
        for name in rules.kinds[entry.kind]:
            if name not in entry.fields or not entry.fields[name][0]:
                report.error(entry.line, "%s: field *%s* is missing" % (entry.identifier, name),
                             check, (presence,))
        given = rules.words.get(entry.kind, {})
        for name, (value, line) in entry.fields.items():
            if is_none(value) and "none" not in given.get(name, []):
                report.error(line, "%s: *%s* is `none`, which its form does not give it"
                             % (entry.identifier, name), check, (words,))
            elif holds_todo(value):
                if "TODO" in given.get(name, []):
                    report.warning(line, "%s: *%s* holds `TODO`" % (entry.identifier, name))
                else:
                    report.error(line, "%s: *%s* holds `TODO`, which its form does not give it"
                                 % (entry.identifier, name), check, (words,))


def check_references(entries, sections, report):
    # invariant: flow-part-names/1
    check, flow_parts = "check_references", "flow-part-names/1"
    report.ran(check, flow_parts)
    withdrawn = {cells[0] for cells, _ in listed_rows(sections, "Withdrawn identifiers")}
    parts = {entry.identifier for entry in entries if entry.kind == "part"}
    for entry in entries:
        for name in ("Depends on", "Parts"):
            if name not in entry.fields:
                continue
            cited = (name == "Parts" and entry.kind == "critical flow"
                     or name == "Depends on" and entry.kind == "part")
            invariants = (flow_parts,) if cited else ()
            value, line = entry.fields[name]
            for identifier in identifiers(value):
                if identifier in parts:
                    continue
                if identifier in withdrawn:
                    report.error(line, "%s: *%s* names `%s`, which is withdrawn"
                                 % (entry.identifier, name, identifier), check, invariants)
                else:
                    report.error(line, "%s: *%s* names `%s`, which is not in the map as a part"
                                 % (entry.identifier, name, identifier), check, invariants)


# --- criticality ----------------------------------------------------------------------------


def scale(sections):
    """The degrees of the criticality scale, lowest first."""
    return [cells[0].split(" — ")[0].strip() for cells, _ in listed_rows(sections,
                                                                         "Criticality scale")]


def failure_modes(value):
    """Yield (mode, parts) for every failure mode listed in a part's field, wrapping included."""
    modes = []
    for line in (value or "").split("\n"):
        text = line.strip()
        if not text:
            continue
        if text.startswith("- "):
            modes.append(text[2:].strip())
        elif modes:
            modes[-1] = (modes[-1] + " " + text).strip()
        else:
            modes.append(text)
    for mode in modes:
        mode = " ".join(mode.split())
        if mode and not is_none(mode):
            yield mode, [piece.strip() for piece in mode.split(" — ")]


def is_detection(piece):
    """Whether a piece reads `not detected` or names a detecting invariant; `detected by TODO`
    names none."""
    return piece == "not detected" or (piece.startswith("detected by ") and
                                       bool(piece[len("detected by "):].strip()) and
                                       not holds_todo(piece))


def dependencies(value):
    """Yield (identifier, separated) for every dependency a part records."""
    if not value or is_none(value):
        return
    for item in value.replace("\n", " ").split(" · "):
        if holds_todo(item):
            continue
        match = re.match(r"^(%s)\b(.*)$" % IDENTIFIER, item.strip())
        if match:
            yield match.group(1), "separated" in match.group(2)


def criticality(entries, sections):
    """The computed degree of every part: its own failure modes, its flows, and what leans on it."""
    degrees = scale(sections)
    rank = {degree: position for position, degree in enumerate(degrees)}
    highest = len(degrees) - 1
    parts = [entry for entry in entries if entry.kind == "part"]

    computed = {}
    for entry in parts:
        own = [rank[pieces[2]] for _, pieces in failure_modes(entry.fields.get("Failure modes",
                                                                              [""])[0])
               if len(pieces) > 2 and pieces[2] in rank]
        computed[entry.identifier] = max(own) if own else highest
    for entry in entries:
        if entry.kind != "critical flow":
            continue
        degree = rank.get(entry.fields.get("Criticality", [""])[0])
        if degree is None:
            continue
        for identifier in identifiers(entry.fields.get("Parts", [""])[0]):
            if identifier in computed:
                computed[identifier] = max(computed[identifier], degree)

    edges = [(entry.identifier, target) for entry in parts
             for target, separated in dependencies(entry.fields.get("Depends on", [""])[0])
             if not separated and target in computed]
    for _ in range(len(computed) + 1):
        changed = False
        for source, target in edges:
            if computed[target] < computed[source]:
                computed[target] = computed[source]
                changed = True
        if not changed:
            break
    return {identifier: degrees[position] if degrees else None
            for identifier, position in computed.items()}


def check_criticality(entries, sections, rules, report):
    # invariant: failure-mode-severity/1
    # invariant: failure-mode-detection/1
    check, severity, detection = ("check_criticality", "failure-mode-severity/1",
                                  "failure-mode-detection/1")
    report.ran(check, severity, detection)
    degrees = scale(sections)
    computed = criticality(entries, sections)
    for entry in entries:
        if entry.kind == "critical flow":
            value, line = entry.fields.get("Criticality", ["", entry.line])
            if value and value not in degrees:
                report.error(line, "%s: `%s` is not on the criticality scale"
                             % (entry.identifier, value), check)
        if entry.kind != "part":
            continue
        value, line = entry.fields.get("Failure modes", ["", entry.line])
        for mode, pieces in failure_modes(value):
            no_severity = len(pieces) < 3 or (len(pieces) == 3 and is_detection(pieces[-1]))
            if no_severity:
                report.error(line, "%s: `%s` is not `<what fails> — <damage> — <severity> — "
                                   "<detection>`" % (entry.identifier, mode), check,
                             (severity,) if is_detection(pieces[-1]) else (severity, detection))
                continue
            if not is_detection(pieces[-1]):
                report.error(line, "%s: `%s` names neither a detecting invariant nor "
                                   "`not detected`" % (entry.identifier, mode), check, (detection,))
            if pieces[2] not in degrees:
                # a word off the scale, `TODO` included, names no severity of this map
                report.error(line, "%s: `%s` is not on the criticality scale"
                             % (entry.identifier, pieces[2]), check, (severity,))

    by_identifier = entries_by_identifier(entries)
    for entry in entries:
        if entry.kind != "part":
            continue
        value, line = entry.fields.get("Depends on", ["", entry.line])
        for target, separated in dependencies(value):
            if separated or target not in computed or target not in by_identifier:
                continue
            own = [pieces[2] for _, pieces in
                   failure_modes(by_identifier[target].fields.get("Failure modes", [""])[0])
                   if len(pieces) > 2 and pieces[2] in degrees]
            if own and max(own, key=degrees.index) != computed[target]:
                report.warning(line, "%s depends on %s with no separation recorded, so %s is "
                                     "computed as `%s`, above its own failure modes"
                               % (entry.identifier, target, target, computed[target]))


def entries_by_identifier(entries):
    return {entry.identifier: entry for entry in entries}


def named_invariants(entries):
    """Yield (invariant, line, entry) for every invariant the map names: a flow's *Invariant* and
    the detecting invariant of a failure mode."""
    for entry in entries:
        if entry.kind == "critical flow":
            value, line = entry.fields.get("Invariant", ["", entry.line])
            name = flow_invariant(value)[0]
            if name:
                yield name, line, entry
        elif entry.kind == "part":
            value, line = entry.fields.get("Failure modes", ["", entry.line])
            for _, pieces in failure_modes(value):
                if pieces[-1].startswith("detected by "):
                    name = pieces[-1][len("detected by "):].strip()
                    if name and not holds_todo(name):
                        yield name, line, entry


def check_invariant_names(entries, map_path, report):
    """Every invariant the map names is an entry of the invariants file beside it (WAY-64)."""
    # invariant: map-invariant-names/1
    check, names = "check_invariant_names", "map-invariant-names/1"
    path = os.path.join(os.path.dirname(os.path.abspath(map_path)), "invariants.md")
    if not os.path.isfile(path):
        report.notes.append("there is no invariants.md beside the map: the invariants the map "
                            "names are not checked")
        return
    text = read_file(path, report, "the invariants file beside the map")
    if text is None:
        return
    held = set(re.findall(r"^## (%s)/\d+[ \t]*$" % IDENTIFIER, text, re.M))
    report.ran(check, names)
    for name, line, entry in named_invariants(entries):
        if name not in held:
            report.error(line, "%s: invariant `%s` is not an entry of foundations/invariants.md"
                         % (entry.identifier, name), check, (names,))


# --- checks against the repository ----------------------------------------------------------


def patterns(entry, name="Files"):
    """Yield the path patterns a field lists, one per line. The mark `(generated)`, which the form
    does not use, is set aside, so the pattern it follows is still matched; check_fields
    reports the mark."""
    for line in (entry.fields.get(name, [""])[0] or "").split("\n"):
        pattern = line.strip()
        if pattern.startswith("- "):
            pattern = pattern[2:].strip()
        pattern = GENERATED.sub("", pattern).strip()
        if pattern and not is_none(pattern) and not is_todo(pattern):
            yield pattern


def repository_root(map_path, report):
    """The root of the map's repository, or None once the report holds the failure of the run."""
    code, top = git(["rev-parse", "--show-toplevel"], os.path.dirname(os.path.abspath(map_path)))
    if code != 0:
        report.error(None, "the map does not lie in a git repository, so no check that asks git "
                           "which files it tracks can run")
        return None
    return top.strip()


def tracked_files(top, report):
    code, listing = git(["ls-files", "-z"], top)
    if code != 0:
        report.error(None, "git cannot list the files it tracks in %s" % top)
        return None
    return [path for path in listing.split("\0") if path]


def matched_by_git(root, wanted, paths):
    """Ask git which of the paths each pattern matches: {attribute: [paths]}, or None when git
    cannot. Letter case always counts: git ignores it where core.ignorecase is set, which git
    init sets on Windows and macOS, and a map would then assign files differently there."""
    handle, attributes_file = tempfile.mkstemp(prefix="part-map-", suffix=".attributes", text=True)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as attributes:
            for attribute, pattern in wanted.items():
                attributes.write("%s %s\n" % (pattern, attribute))
        code, answer = git(["-c", "core.attributesFile=%s" % attributes_file.replace(os.sep, "/"),
                            "-c", "core.ignorecase=false", "check-attr", "--all", "-z", "--stdin"], root,
                           stdin=chr(0).join(paths) + chr(0))
    finally:
        os.unlink(attributes_file)
    if code != 0:
        return None

    found = {attribute: [] for attribute in wanted}
    pieces = answer.split("\0")
    for index in range(0, len(pieces) - 2, 3):
        path, attribute, value = pieces[index], pieces[index + 1], pieces[index + 2]
        if attribute in found and value == "set":
            found[attribute].append(path)
    return found


def check_map_file(map_path, top, tracked, report):
    """The repository holds one part map, at foundations/part_map.md (WAY-40). Another map is
    known by its name: a tracked file named part_map.md anywhere else."""
    # invariant: part-map-file/1
    check, one_file = "check_map_file", "part-map-file/1"
    report.ran(check, one_file)
    expected = os.path.join(top, *MAP_PATH.split("/"))
    given = os.path.relpath(os.path.abspath(map_path), top).replace(os.sep, "/")
    if not os.path.isfile(expected) or not os.path.samefile(map_path, expected):
        report.error(None, "the part map stands in %s, not in %s" % (MAP_PATH, given),
                     check, (one_file,))
    for path in tracked:
        if path.split("/")[-1] == os.path.basename(MAP_PATH) and path not in (MAP_PATH, given):
            report.error(None, "`%s` is a second part map; the repository holds one, %s"
                         % (path, MAP_PATH), check, (one_file,))


def check_files(entries, sections, report, top, tracked):
    """Returns {tracked path: [parts whose patterns claim it]}, or None where git cannot match."""
    # invariant: file-part-assignment/1
    # invariant: path-pattern-reach/1
    # invariant: left-out-file-assignment/1
    # invariant: trust-boundary-pattern/1
    check = "check_files"
    assignment, reach, left_out_claim, boundary = (
        "file-part-assignment/1", "path-pattern-reach/1", "left-out-file-assignment/1",
        "trust-boundary-pattern/1")
    wanted, owner = {}, {}
    for entry in entries:
        if entry.kind != "part":
            continue
        for name in ("Files", "Trust boundary"):
            for pattern in patterns(entry, name):
                attribute = "partmap%d" % len(wanted)
                wanted[attribute] = pattern
                owner[attribute] = (entry, name, pattern)

    left_out = {cells[0]: line
                for cells, line in listed_rows(sections, "Files left out on purpose")}
    known = set(tracked)
    paths = tracked + [path for path in left_out if path not in known]
    found = matched_by_git(top, wanted, paths)
    if found is None:
        report.error(None, "git cannot match the path patterns of the map to files")
        return None
    report.ran(check, assignment, reach, left_out_claim, boundary)

    claims, left_out_claims = {}, {}
    for attribute, matched in found.items():
        entry, name, pattern = owner[attribute]
        if not [path for path in matched if path in known]:
            line = entry.fields.get(name, ["", entry.line])[1]
            if name == "Files":
                report.error(line, "pattern `%s` of `%s` matches no file git tracks"
                             % (pattern, entry.identifier), check, (reach,))
            else:
                report.error(line, "trust boundary `%s` of `%s` matches no file git tracks"
                             % (pattern, entry.identifier), check, (reach, boundary))
        if name != "Files":
            continue
        for path in matched:
            (claims if path in known else left_out_claims).setdefault(path, []).append(entry)

    for path, line in left_out.items():
        for entry in claims.get(path, []) + left_out_claims.get(path, []):
            report.error(line, "`%s` is left out on purpose and claimed by `%s`"
                         % (path, entry.identifier), check, (left_out_claim,))
    for path in tracked:
        owners = claims.get(path, [])
        if path in left_out:
            continue
        if not owners:
            report.error(None, "no part claims `%s`: give it to a part or put it on the list of "
                               "files left out on purpose" % path, check, (assignment,))
        elif len(owners) > 1:
            report.error(owners[1].line, "`%s` is claimed by `%s` and `%s`"
                         % (path, owners[0].identifier, owners[1].identifier), check,
                         (assignment,))
    return claims


def check_flows(entries, report, top, tracked, claims):
    """Every critical flow names an invariant and is named by a test, in a comment line
    `# flow: <identifier>` of a file git tracks (WAY-45); the map names no test. Returns the
    tests found for each flow, or None where git lists no file."""
    # invariant: flow-invariant-link/1
    # invariant: flow-coverage-parts/1
    check, link, coverage_parts = "check_flows", "flow-invariant-link/1", "flow-coverage-parts/1"
    if top is None or tracked is None:
        return None
    report.ran(check, link)
    if claims is not None:
        report.ran(check, coverage_parts)
    named = flow_tests(top, tracked)
    for entry in entries:
        if entry.kind != "critical flow":
            continue
        value, line = entry.fields.get("Invariant", ["", entry.line])
        invariant, relative = flow_invariant(value)
        if invariant is None:
            report.error(line, "%s: *Invariant* names no invariant" % entry.identifier,
                         check, (link,))
        if relative is not None:
            report.error(line, "%s: *Invariant* names a test after `— test:`; the flow's test "
                               "names the flow in a line `# flow: %s` instead"
                         % (entry.identifier, entry.identifier), check)
        if not named.get(entry.identifier):
            report.error(line, "%s: no test names the flow in a line `# flow: %s`"
                         % (entry.identifier, entry.identifier), check, (link,))

        if claims is None:
            continue
        listed = set(identifiers(entry.fields.get("Parts", [""])[0]))
        value, line = entry.fields.get("Coverage", ["", entry.line])
        value = bare(value)
        if not value or value == "none":
            report.cannot_check("the list of parts of `%s`" % entry.identifier,
                                "its test leaves no coverage file")
            report.unchecked(check, NOT_PRODUCED_REASON,
                             "the test of `%s` leaves no coverage file" % entry.identifier,
                             coverage_parts)
            continue
        full = os.path.join(top, value.replace("/", os.sep))
        if not os.path.isfile(full):
            report.error(line, "%s: coverage file `%s` does not exist" % (entry.identifier, value),
                         check)
            report.cannot_check("the list of parts of `%s`" % entry.identifier,
                                "its coverage file `%s` does not exist" % value)
            report.unchecked(check, NOT_PRODUCED_REASON,
                             "coverage file `%s` of `%s` does not exist"
                             % (value, entry.identifier), coverage_parts)
            continue
        with open(full, encoding="utf-8", errors="replace") as handle:
            covered = [row[3:].strip() for row in handle if row.startswith("SF:")]
        if not covered:
            # A file with no record the guard reads is silence, not agreement (WAY-47).
            report.cannot_check("the list of parts of `%s`" % entry.identifier,
                                "its coverage file `%s` holds no `SF:` record the guard reads"
                                % value)
            report.unchecked(check, NOT_PRODUCED_REASON,
                             "coverage file `%s` of `%s` holds no `SF:` record the guard reads"
                             % (value, entry.identifier), coverage_parts)
            continue
        for path in covered:
            if os.path.isabs(path):
                path = os.path.relpath(path, top)
            path = path.replace(os.sep, "/")
            for owner in claims.get(path, []):
                if owner.identifier not in listed:
                    report.error(line, "%s: coverage of `%s` runs through `%s`, which is not in "
                                       "its list of parts"
                                 % (entry.identifier, entry.identifier, owner.identifier),
                                 check, (coverage_parts,))
                    listed.add(owner.identifier)
    return named


def check_flow_tests(entries, named, report):
    """Every test naming a critical flow of the-way's own map in a line `# flow: <identifier>`
    lies under gate/ (WAY-55)."""
    # invariant: flow-test-location/1
    check, location = "check_flow_tests", "flow-test-location/1"
    report.ran(check, location)
    for entry in entries:
        if entry.kind != "critical flow":
            continue
        line = entry.fields.get("Invariant", ["", entry.line])[1]
        for path in named.get(entry.identifier, []):
            if not path.startswith(GATE_DIRECTORY):
                report.error(line, "%s: `%s` names the flow in a line `# flow: %s` and lies "
                                   "outside `%s`" % (entry.identifier, path, entry.identifier,
                                                     GATE_DIRECTORY), check, (location,))


def promise_levels(sections):
    return [cells[0] for cells, _ in listed_rows(sections, "Change paths")]


def check_surfaces(entries, sections, rules, text, report, top):
    # invariant: surface-declaration/1
    # invariant: map-withdrawal-date/1
    # invariant: surface-change-path/1
    check = "check_surfaces"
    declaration, withdrawal, change_path = ("surface-declaration/1", "map-withdrawal-date/1",
                                            "surface-change-path/1")
    report.ran(check, withdrawal, change_path)
    if top is not None:
        report.ran(check, declaration)
    levels = promise_levels(sections)
    surfaces = [entry for entry in entries if entry.kind == "surface"]
    dated = {}   # line -> what the date stands in
    for number, line in enumerate(text.split("\n"), start=1):
        if DATE.search(line) and re.search(r"withdraw", line, re.I):
            dated.setdefault(number, "a line that speaks of withdrawal")
    for cells, line in listed_rows(sections, "Withdrawn identifiers"):
        if any(DATE.search(cell) for cell in cells):
            dated.setdefault(line, "the list of withdrawn identifiers")

    columns = rules.lists.get("Change paths", [])
    for entry in surfaces:
        value, line = entry.fields.get("Declared at", ["", entry.line])
        if DATE.search(value):
            dated[line] = "`%s`" % entry.identifier
        pieces = [piece.strip() for piece in value.split(" · ")]
        for level in levels:
            if any(re.search(r"\b%s\b" % re.escape(level), piece) for piece in pieces):
                report.error(line, "%s: the promise level `%s` belongs at the declaration, not "
                                   "in the map" % (entry.identifier, level), check)
        for name, (_, at) in entry.fields.items():
            if name != "Declared at" and ("change" in name.lower() or name in columns):
                report.error(at, "%s: *%s* gives the surface a change path of its own; a change "
                                 "path belongs to a promise level" % (entry.identifier, name),
                             check, (change_path,))
        if top is None:
            continue
        test = re.search(r"test:\s*(\S.*)$", " ".join(value.split()))
        if value.startswith("not markable"):
            if not test:
                report.error(line, "%s: a surface that cannot be marked names the test that "
                                   "protects it" % entry.identifier, check, (declaration,))
            elif not os.path.isfile(os.path.join(top, test.group(1).strip().replace("/", os.sep))):
                report.error(line, "%s: test `%s` of `%s` does not exist"
                             % (entry.identifier, test.group(1).strip(), entry.identifier),
                             check, (declaration,))
            continue
        declared = pieces[0] if pieces else ""
        full = os.path.join(top, declared.replace("/", os.sep))
        if not declared or not os.path.isfile(full):
            report.error(line, "%s: declaration `%s` of `%s` does not exist"
                         % (entry.identifier, declared, entry.identifier), check, (declaration,))
        elif len(pieces) > 1 and pieces[1]:
            with open(full, encoding="utf-8", errors="replace") as handle:
                if pieces[1] not in handle.read():
                    report.error(line, "%s: `%s` does not stand in `%s`"
                                 % (entry.identifier, pieces[1], declared), check, (declaration,))
    for cells, line in listed_rows(sections, "Change paths"):
        if cells[0] in {entry.identifier for entry in surfaces}:
            report.error(line, "the change path `%s` names a surface; a change path belongs to a "
                               "promise level, never to one surface" % cells[0],
                         check, (change_path,))
    for line, where in sorted(dated.items()):
        report.error(line, "a withdrawal date belongs at the declaration, not in the map "
                           "(written in %s)" % where, check, (withdrawal,))


def check_promise_levels(entries, report):
    """The levels of promise sit at the declarations, and no command of the product reports them,
    so what the map says of them cannot be read against the code (WAY-49, WAY-50)."""
    # invariant: surface-promise-level/1
    # invariant: promise-level-policy/1
    check = "check_promise_levels"
    why = "the levels sit at the declarations, and no command of the product reports them"
    if any(entry.kind == "surface" for entry in entries):
        report.cannot_check("the change path of every promise level in use", why)
    report.unchecked(check, NOT_PRODUCED_REASON, why, "surface-promise-level/1",
                     "promise-level-policy/1")


def check_lists(sections, rules, report):
    # invariant: external-exchange-row/1
    check, exchange = "check_lists", "external-exchange-row/1"
    report.ran(check, exchange)
    for title, columns in rules.lists.items():
        if title == "Withdrawn identifiers":
            continue  # check_withdrawn
        invariants = (exchange,) if title == "External context" else ()
        for cells, line in rows(sections, title):
            if cells == columns:
                continue
            todo = [cell for cell in cells if is_todo(cell)]
            if todo:
                report.error(line, "the list `%s` holds `TODO`" % title, check, invariants)
            if not columns:
                continue
            allowed = rules.values.get(title, [])
            for index, column in enumerate(columns):
                if index >= len(cells) or not cells[index]:
                    report.error(line, "the row records no *%s*" % column, check, invariants)
                    continue
                choices = allowed[index] if index < len(allowed) else None
                if choices and cells[index] not in choices and not is_todo(cells[index]):
                    report.error(line, "`%s` is not one of %s"
                                 % (cells[index], ", ".join("`%s`" % choice
                                                            for choice in choices)),
                                 check, invariants)


def check_withdrawn(entries, sections, rules, report):
    """Every withdrawn identifier of the map gives why it was withdrawn and names one or more
    successors, each an entry or a withdrawn identifier of the map, never `none`: the map withdraws
    an identifier only on a split or a merge, which leaves entries in its place (WAY-41)."""
    # invariant: map-withdrawal-successors/1
    check, successors = "check_withdrawn", "map-withdrawal-successors/1"
    report.ran(check, successors)
    section = sections.get("Withdrawn identifiers")
    if section is None:
        return
    expected = rules.lists["Withdrawn identifiers"]
    columns, listed = expected, []
    for cells, line in section.rows:
        if cells and cells[0] == expected[0]:
            columns = cells
            if cells != expected:
                report.error(line, "the list of withdrawn identifiers has the columns %s, not %s"
                             % (", ".join(cells), ", ".join(expected)), check, (successors,))
        else:
            listed.append((cells, line))
    known = {entry.identifier for entry in entries}
    withdrawn = {cells[0] for cells, _ in listed if cells and not is_todo(cells[0])}

    def cell(cells, name):
        index = columns.index(name) if name in columns else None
        return cells[index] if index is not None and index < len(cells) else ""

    for cells, line in listed:
        if any(is_todo(value) for value in cells):
            report.error(line, "the list `%s` holds `TODO`" % WITHDRAWN, check)
        identifier = cell(cells, "Identifier")
        why = cell(cells, "Why")
        if not why or is_todo(why) or holds_todo(why) or is_none(why):
            report.error(line, "`%s` gives no why it was withdrawn" % identifier,
                         check, (successors,))
        named = [bare(item) for item in cell(cells, "Successors").split(" · ")
                 if bare(item)]
        if not named or all(is_none(item) for item in named):
            report.error(line, "`%s` names no successor; the map withdraws an identifier only on "
                               "a split or a merge, which leaves entries in its place"
                         % identifier, check, (successors,))
            continue
        for item in named:
            if holds_todo(item):
                continue
            if item == identifier:
                report.error(line, "`%s` names itself as a successor" % identifier,
                             check, (successors,))
            elif item not in known and item not in withdrawn:
                report.error(line, "`%s` names `%s` as a successor, which is neither an entry nor "
                                   "a withdrawn identifier of the map" % (identifier, item),
                             check, (successors,))


def check_examples(entries, examples_path, report):
    """Every identifier `examples.md` names is the identifier of an entry of the map: an example
    names an entry of the-way's map by its identifier instead of copying it (WAY-09, WAY-34). An
    item of a list names the identifier it opens with."""
    # invariant: map-example-target/1
    check, target = "check_examples", "map-example-target/1"
    text = read_file(examples_path, report, "the examples")
    if text is None:
        return
    report.ran(check, target)
    known = {entry.identifier for entry in entries}
    for number, line in enumerate(text.split("\n"), start=1):
        item = re.match(r"^- `?([^`\s]+)`?", line)
        if item and item.group(1) not in known:
            report.error(None, "examples.md:%d: `%s` is not the identifier of an entry of the map"
                         % (number, item.group(1)), check, (target,))


def latest_scopes(text):
    """{number: (label, scope, line)} for the latest version of each decision in a log, its
    *Scope* read whole, wrapped lines included."""
    latest, current = {}, None
    lines = text.split("\n")
    for index, line in enumerate(lines):
        if line.startswith("#"):
            heading = re.match(r"^### ([A-Z][A-Z0-9]*-(\d{2,}))/(\d+) — ", line)
            current = None
            if heading:
                number, version = heading.group(2), int(heading.group(3))
                if number not in latest or latest[number][0] < version:
                    current = number
                    latest[number] = (version, "%s/%d" % (heading.group(1), version), None, None)
            continue
        scope = re.match(r"^- \*\*Scope:\*\*(?: (.*))?$", line)
        if not scope or current is None:
            continue
        value = scope.group(1) or ""
        following = index + 1
        while following < len(lines) and lines[following].startswith(" ") \
                and lines[following].strip():
            value += " " + lines[following].strip()
            following += 1
        version, label, _, _ = latest[current]
        latest[current] = (version, label, value, index + 1)
    return {number: (label, scope, line) for number, (_, label, scope, line) in latest.items()
            if scope is not None}


def check_scopes(entries, sections, report, map_path):
    """Every name in the scope of the latest version of a decision is a part of the map (WAY-21)."""
    # invariant: decision-scope-names/1
    check, names = "check_scopes", "decision-scope-names/1"
    log = os.path.join(os.path.dirname(os.path.abspath(map_path)), "decisions.md")
    if not os.path.isfile(log):
        report.notes.append("there is no decisions.md beside the map: the scopes of decisions are "
                            "not checked")
        return
    text = read_file(log, report, "the decision log beside the map")
    if text is None:
        return
    scopes = latest_scopes(text)
    report.ran(check, names)
    known = {entry.identifier for entry in entries if entry.kind == "part"}
    withdrawn = {cells[0] for cells, _ in listed_rows(sections, "Withdrawn identifiers")}
    for number in sorted(scopes, key=int):
        label, scope, line = scopes[number]
        for named in (bare(piece) for piece in scope.split(",")):
            if not named or named in known or is_todo(named) or named == "none":
                continue
            if named in withdrawn:
                report.error(None, "decisions.md:%d: the scope of %s names `%s`, which is "
                                   "withdrawn" % (line, label, named), check, (names,))
            else:
                report.error(None, "decisions.md:%d: the scope of %s names `%s`, which is not in "
                                   "the map as a part" % (line, label, named), check, (names,))


# --- known violations -----------------------------------------------------------------------


def violations_path(map_path, rules):
    root_of_map = os.path.dirname(os.path.dirname(os.path.abspath(map_path)))
    return os.path.join(root_of_map, rules.violations.replace("/", os.sep))


def check_violations(entries, rules, report, map_path):
    """Checks the rows of the list of known violations and returns them (WAY-51)."""
    # invariant: known-violation-fields/1
    # invariant: known-violation-line-number/1
    check, fields, line_number = ("check_violations", "known-violation-fields/1",
                                  "known-violation-line-number/1")
    path = violations_path(map_path, rules)
    if not os.path.exists(path):
        report.ran(check, fields, line_number)
        return []
    text = read_file(path, report, "the list of known violations")
    if text is None:
        return []
    report.ran(check, fields, line_number)
    _, violation_sections = parse_map(text, rules)
    columns = rules.lists.get("Known violations", [])
    parts = {entry.identifier for entry in entries if entry.kind == "part"}

    positions = []
    for cells, line in rows(violation_sections, "Known violations"):
        if cells == columns:
            continue
        positions.append(tuple(cells))
        for index, column in enumerate(columns):
            if index >= len(cells) or not cells[index] or is_todo(cells[index]):
                report.error(None, "%s:%d: the known violation records no *%s*"
                             % (rules.violations, line, column), check, (fields,))
        for index in (0, 1):
            if index < len(cells) and cells[index] and not is_todo(cells[index]) \
                    and cells[index] not in parts:
                report.error(None, "%s:%d: the known violation names `%s`, which is not in the "
                                   "map as a part" % (rules.violations, line, cells[index]),
                             check, (fields,))
        if any(re.search(r":\d+\b|\bline \d+\b", cell) for cell in cells):
            report.error(None, "%s:%d: the known violation names a line number, which goes stale "
                               "at the next edit" % (rules.violations, line),
                         check, (line_number,))
    return positions


def check_dependencies(report):
    """What the code holds against the map's dependencies comes from the product's dependency
    graph, which no command of the product reports yet (WAY-51, WAY-38)."""
    # invariant: known-violation-coverage/1
    # invariant: known-violation-currency/1
    check = "check_dependencies"
    why = "no command of the product reports the dependency graph"
    report.cannot_check("the dependencies between parts, and new or stale violations", why)
    report.unchecked(check, NOT_PRODUCED_REASON, why, "known-violation-coverage/1",
                     "known-violation-currency/1")


def check_violations_growth(map_path, rules, positions, base, top, report, no_commit=None):
    """The list of known violations is a subset of its version on the base (WAY-51). Given
    `no_commit`, which says why there is no base, records it unchecked instead."""
    # invariant: known-violations-growth/1
    check, growth = "check_violations_growth", "known-violations-growth/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, growth)
        return
    relative = os.path.relpath(violations_path(map_path, rules), top).replace(os.sep, "/")
    base_text, failure = file_at(base, relative, top)
    if failure:
        report.error(None, failure)
        return
    if base_text is None:
        if positions:
            report.notes.append("%s has no %s; every row counts as added" % (base, relative))
        base_text = ""
    report.ran(check, growth)
    _, base_sections = parse_map(base_text, rules)
    on_base = {tuple(cells) for cells, _ in rows(base_sections, "Known violations")}
    for position in positions:
        if position not in on_base:
            report.error(None, "%s: `%s` is not on the list of %s: a row is added only by a "
                               "change of the foundation a human accepts"
                         % (rules.violations, " · ".join(position), base), check, (growth,))


def report_lowering(entries, sections, rules, map_path, base, top, report):
    """Warns of every part whose computed criticality is lower than on the base, so that the human
    deciding the change has the lowered criticality in front of them (WAY-46)."""
    relative = os.path.relpath(os.path.abspath(map_path), top).replace(os.sep, "/")
    base_text, failure = file_at(base, relative, top)
    if failure:
        report.error(None, failure)
        return
    if base_text is None:
        report.notes.append("%s has no %s, so no part's computed criticality is compared with it"
                            % (base, relative))
        return
    base_entries, base_sections = parse_map(base_text, rules)
    before = criticality(base_entries, base_sections)
    degrees = scale(sections)
    by_identifier = entries_by_identifier(entries)
    for identifier, degree in sorted(criticality(entries, sections).items(),
                                     key=lambda item: by_identifier[item[0]].line):
        was = before.get(identifier)
        if was is None or degree is None:
            continue
        if was not in degrees:
            report.notes.append("%s: `%s` on %s is not on the criticality scale, so its computed "
                                "criticality is not compared" % (identifier, was, base))
        elif degrees.index(degree) < degrees.index(was):
            report.warning(by_identifier[identifier].line,
                           "%s: the computed criticality is `%s`, lower than `%s` on %s"
                           % (identifier, degree, was, base))


# --- entry point ----------------------------------------------------------------------------


def run(map_path, base=None, stream=None, template=TEMPLATE, record=None,
        own=None, examples=EXAMPLES):
    stream = stream or sys.stdout
    if record is not None:
        try:
            start_record(record)
        except OSError as problem:
            stream.write("cannot write the record: %s\n" % problem)
            return 2
    report = Report(map_path, ["--base"] if base else [])

    def stop(message):
        stream.write(message + "\n")
        report.error(None, message)
        if record is not None:
            write_record(record, report)
        return 2

    try:
        rules = read_rules(template)
    except (OSError, UnicodeDecodeError, TemplateError, AttributeError, IndexError) as problem:
        return stop("cannot read the rules from %s: %s" % (template, problem))
    try:
        with open(map_path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError) as problem:
        return stop("cannot read the map: %s" % problem)
    if own is None:
        own = os.path.exists(OWN_MAP) and os.path.samefile(map_path, OWN_MAP)

    entries, sections = parse_map(text, rules)
    top = repository_root(map_path, report)
    tracked = tracked_files(top, report) if top is not None else None
    check_sections(text, report)
    check_kinds(entries, rules, report)
    check_identifiers(entries, sections, report)
    check_fields(entries, rules, report)
    check_references(entries, sections, report)
    check_criticality(entries, sections, rules, report)
    check_invariant_names(entries, map_path, report)
    claims = None
    if tracked is not None:
        check_map_file(map_path, top, tracked, report)
        claims = check_files(entries, sections, report, top, tracked)
    named = check_flows(entries, report, top, tracked, claims)
    if own and named is not None:
        check_flow_tests(entries, named, report)
    check_surfaces(entries, sections, rules, text, report, top)
    check_promise_levels(entries, report)
    check_lists(sections, rules, report)
    check_withdrawn(entries, sections, rules, report)
    check_scopes(entries, sections, report, map_path)
    positions = check_violations(entries, rules, report, map_path)
    check_dependencies(report)

    if base == NO_COMMIT:
        no_base = "--base none: there is no commit the branch left the main branch from"
        check_violations_growth(map_path, rules, positions, None, None, report, no_commit=no_base)
        report.notes.append(no_base + "; the list of known violations is not compared with it, "
                                      "and that check is unchecked")
        report.notes.append(no_base + ", so the computed criticality of the parts is not compared "
                                      "with it and no lowering is reported")
    elif base:
        if top is not None and find_commit(top, "--base", base, report):
            check_violations_growth(map_path, rules, positions, base, top, report)
            report_lowering(entries, sections, rules, map_path, base, top, report)
    else:
        report.notes.append("no --base given: the list of known violations is not compared with "
                            "the main branch")
        report.notes.append("no --base given: the computed criticality of the parts is not "
                            "compared with the main branch, so no lowering is reported")

    if own and os.path.exists(examples):
        check_examples(entries, examples, report)
    report.print(stream)
    if record is not None:
        write_record(record, report)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a part map against its template.")
    parser.add_argument("map", nargs="?", default=os.path.join("foundations", "part_map.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from, "
                                         "to compare the list of known violations and the "
                                         "computed criticality of the parts with; `none` "
                                         "where it does not exist, which records that check as "
                                         "unchecked")
    parser.add_argument("--record", help="the JSON Lines file, created or overwritten, that "
                                         "receives a verdict for each invariant a check cites")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.map, arguments.base, record=arguments.record)


if __name__ == "__main__":
    sys.exit(main())
