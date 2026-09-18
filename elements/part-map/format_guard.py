"""Format guard of a product's part map.

Runs the checks listed in "What the checker checks" in template.md, which lies next to this
script. The fields of each kind of entry and the titles of the five lists are read from the
template, so the rules of an entry live in one place (WAY-35).

Usage, from the root of the product's repository:

    python <the-way>/elements/part-map/format_guard.py [MAP] [--base REF]

MAP defaults to foundations/part_map.md. --base names the main branch the list of known
violations is compared with; without it, that check is skipped. Exit code: 0 without errors,
1 with errors, 2 when the map or the template cannot be read.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_MAP = os.path.join(HERE, "..", "..", "foundations", "part_map.md")

sys.dont_write_bytecode = True

IDENTIFIER = r"[a-z0-9]+(?:-[a-z0-9]+)*"
LIST_SECTIONS = ["Criticality scale", "External context", "Change paths",
                 "Files left out on purpose", "Withdrawn identifiers", "Known violations"]


class TemplateError(Exception):
    pass


# --- rules read from the template -----------------------------------------------------------


@dataclass
class Rules:
    kinds: dict          # kind -> the field names of that kind, in the order of the template
    marks: dict          # field name -> kind, for the fields that name one kind alone
    lists: dict          # section title -> column names, empty for a numbered list
    values: dict         # section title -> the values a column allows, None where it is free
    violations: str      # the path of the derived list of known violations


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


def read_rules(path=TEMPLATE):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    kinds = {}
    for title in ("Part", "Critical flow", "Surface"):
        form = _code_block(text, title)
        fields = re.findall(r"^- \*\*(.+?):\*\*", form, re.M)
        if not fields:
            raise TemplateError('no fields in the form of "%s"' % title)
        kinds[title.lower()] = fields

    marks = {}
    for kind, fields in kinds.items():
        for name in fields:
            if sum(name in other for other in kinds.values()) == 1:
                marks[name] = kind
    if len(set(marks.values())) != len(kinds):
        raise TemplateError("the kinds of entry cannot be told apart by their fields")

    lists, values = {}, {}
    for title in LIST_SECTIONS:
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
    violations = re.search(r"`([^`]+known_violations[^`]*)`", _section(text, "Known violations"))
    if not violations:
        raise TemplateError("the section on known violations names no file")
    return Rules(kinds, marks, lists, values, violations.group(1))


# --- parsing the map ------------------------------------------------------------------------


@dataclass
class Entry:
    line: int
    identifier: str
    title: str
    kind: str = None
    binding: str = None
    fields: dict = field(default_factory=dict)   # name -> [value, line]
    text: str = ""                                # the entry as it stands in the file


@dataclass
class Section:
    line: int
    title: str
    rows: list = field(default_factory=list)     # (cells, line)


def split_sections(text):
    lines = text.split("\n")
    starts = [index for index, line in enumerate(lines) if line.startswith("## ")]
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        yield start + 1, lines[start:end]


def parse_fields(body, first_line):
    fields, current = {}, None
    for offset, line in enumerate(body, start=first_line):
        match = re.match(r"^- \*\*(.+?):\*\*(?: (.*))?$", line)
        if match:
            current = match.group(1)
            fields.setdefault(current, [(match.group(2) or "").strip(), offset])
        elif not line.strip():
            current = None
        elif current is not None and line.startswith(" "):
            value, at = fields[current]
            fields[current] = [(value + "\n" + line.rstrip()).strip("\n"), at]
    return fields


def parse_map(text, rules):
    entries, sections = [], {}
    for line, lines in split_sections(text):
        heading = re.match(r"^## (.+?) — (.+)$", lines[0])
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

        entry = Entry(line, heading.group(1).strip(), heading.group(2).strip())
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


def identifiers(value):
    """The identifiers a field lists, from `first · second (separated — why)` or `none`."""
    if not value or value.strip() in ("none", "TODO"):
        return []
    found = []
    for item in value.replace("\n", " ").split(" · "):
        match = re.match(r"^(%s)\b" % IDENTIFIER, item.strip())
        if match:
            found.append(match.group(1))
    return found


# --- checks ---------------------------------------------------------------------------------


def scale(sections):
    """The degrees of the criticality scale, lowest first."""
    degrees = []
    for cells, _ in rows(sections, "Criticality scale"):
        degrees.append(cells[0].split(" — ")[0].strip())
    return degrees


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
        if mode and mode != "none":
            yield mode, [piece.strip() for piece in mode.split(" — ")]


def is_detection(piece):
    return piece == "not detected" or piece.startswith("detected by ")


def dependencies(value):
    """Yield (identifier, separated) for every dependency a part records."""
    if not value or value.strip() == "none":
        return
    for item in value.replace("\n", " ").split(" · "):
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
    degrees = scale(sections)
    computed = criticality(entries, sections)
    for entry in entries:
        if entry.kind == "critical flow":
            value, line = entry.fields.get("Criticality", ["", entry.line])
            if value and value not in degrees:
                report.error(line, "%s: `%s` is not on the criticality scale"
                             % (entry.identifier, value))
        if entry.kind != "part":
            continue
        value, line = entry.fields.get("Failure modes", ["", entry.line])
        for mode, pieces in failure_modes(value):
            if len(pieces) < 3 or (len(pieces) == 3 and is_detection(pieces[-1])):
                report.error(line, "%s: `%s` is not `<what fails> — <damage> — <severity> — "
                                   "<detection>`" % (entry.identifier, mode))
            elif not is_detection(pieces[-1]):
                report.error(line, "%s: `%s` names neither a detecting invariant nor "
                                   "`not detected`" % (entry.identifier, mode))
            elif pieces[2] not in degrees:
                report.error(line, "%s: `%s` is not on the criticality scale"
                             % (entry.identifier, pieces[2]))

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


def patterns(entry, name="Files"):
    """Yield the path patterns a field lists, one per line, without the mark of a generated file."""
    for line in (entry.fields.get(name, [""])[0] or "").split("\n"):
        pattern = line.strip()
        if pattern.startswith("- "):
            pattern = pattern[2:].strip()
        pattern = re.sub(r"\s*\(generated\)\s*$", "", pattern).strip()
        if pattern and pattern != "none":
            yield pattern


def matched_by_git(root, wanted, report):
    """Ask git which files each pattern matches: {attribute: [paths]}, or None when git cannot."""
    code, listing = git(["ls-files", "-z"], root)
    if code != 0:
        return None
    tracked = [path for path in listing.split("\0") if path]
    handle, attributes_file = tempfile.mkstemp(prefix="part-map-", suffix=".attributes", text=True)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as attributes:
            for attribute, pattern in wanted.items():
                attributes.write("%s %s\n" % (pattern, attribute))
        code, answer = git(["-c", "core.attributesFile=%s" % attributes_file.replace(os.sep, "/"),
                            "check-attr", "--all", "-z", "--stdin"], root,
                           stdin=chr(0).join(tracked) + chr(0))
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
    return found, tracked


def promise_levels(sections):
    return [cells[0] for cells, _ in rows(sections, "Change paths") if cells]


def check_surfaces(entries, sections, report, root):
    levels = promise_levels(sections)
    for entry in entries:
        if entry.kind != "surface":
            continue
        value, line = entry.fields.get("Declared at", ["", entry.line])
        pieces = [piece.strip() for piece in value.split(" · ")]
        for level in levels:
            if any(re.search(r"\b%s\b" % re.escape(level), piece) for piece in pieces):
                report.error(line, "%s: the promise level `%s` belongs at the declaration, not "
                                   "in the map" % (entry.identifier, level))
        if re.search(r"\b\d{4}-\d{2}-\d{2}\b", value):
            report.error(line, "%s: a withdrawal date belongs at the declaration, not in the map"
                         % entry.identifier)

        test = re.search(r"test:\s*(\S.*)$", value)
        if value.startswith("not markable"):
            if not test:
                report.error(line, "%s: a surface that cannot be marked names the test that "
                                   "guards it" % entry.identifier)
            elif root and not os.path.exists(os.path.join(root, test.group(1).strip()
                                                          .replace("/", os.sep))):
                report.error(line, "%s: test `%s` of `%s` does not exist"
                             % (entry.identifier, test.group(1).strip(), entry.identifier))
        elif root and pieces and pieces[0]:
            declared = pieces[0]
            if not os.path.exists(os.path.join(root, declared.replace("/", os.sep))):
                report.error(line, "%s: declaration `%s` of `%s` does not exist"
                             % (entry.identifier, declared, entry.identifier))
    if any(entry.kind == "surface" for entry in entries):
        report.cannot_check("the change path of every promise level in use",
                            "the levels sit at the declarations, and no command of the product "
                            "reports them")


def check_lists(sections, rules, report):
    for title, columns in rules.lists.items():
        if not columns:
            continue
        allowed = rules.values.get(title, [])
        for cells, line in rows(sections, title):
            if cells == columns:
                continue
            for index, column in enumerate(columns):
                if index >= len(cells) or not cells[index]:
                    report.error(line, "the row records no *%s*" % column)
                    continue
                choices = allowed[index] if index < len(allowed) else None
                if choices and cells[index] not in choices:
                    report.error(line, "`%s` is not one of %s"
                                 % (cells[index], ", ".join("`%s`" % choice
                                                            for choice in choices)))


def check_examples(entries, examples_path, report):
    """Every example is an entry of the map copied word for word (WAY-05)."""
    with open(examples_path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")
    by_identifier = entries_by_identifier(entries)
    index = 0
    while index < len(lines):
        heading = re.match(r"^## (.+?) — ", lines[index])
        if not heading:
            index += 1
            continue
        start = index
        index += 1
        while index < len(lines) and not lines[index].startswith("## ") \
                and not re.match(r"^\*.*\*$", lines[index].strip()):
            index += 1
        copy = "\n".join(lines[start:index]).rstrip()
        entry = by_identifier.get(heading.group(1).strip())
        if entry is None:
            report.error(None, "examples.md:%d: `%s` is not in the map"
                         % (start + 1, heading.group(1).strip()))
        elif entry.text != copy:
            copy_lines, entry_lines = copy.split("\n"), entry.text.split("\n")
            offset = next((position for position, (a, b) in enumerate(zip(copy_lines, entry_lines))
                           if a != b), min(len(copy_lines), len(entry_lines)))
            report.error(entry.line + offset, "examples.md:%d differs from the map"
                         % (start + 1 + offset))


def check_scopes(entries, sections, report, map_path):
    """Every part a decision's scope names exists in the map (WAY-21)."""
    log = os.path.join(os.path.dirname(os.path.abspath(map_path)), "decisions.md")
    if not os.path.exists(log):
        return
    with open(log, encoding="utf-8") as handle:
        lines = handle.read().split("\n")
    known = {entry.identifier for entry in entries if entry.kind == "part"}
    withdrawn = {cells[0] for cells, _ in rows(sections, "Withdrawn identifiers") if cells}
    label = None
    for number, line in enumerate(lines, start=1):
        heading = re.match(r"^### (\S+) — ", line)
        if heading:
            label = heading.group(1)
        scope = re.match(r"^- \*\*Scope:\*\* (.*)$", line)
        if not scope or label is None:
            continue
        for named in (piece.strip() for piece in scope.group(1).split(",")):
            if not named or named in known:
                continue
            if named in withdrawn:
                report.error(None, "decisions.md:%d: the scope of %s names `%s`, which is "
                                   "withdrawn" % (number, label, named))
            else:
                report.error(None, "decisions.md:%d: the scope of %s names `%s`, which is not in "
                                   "the map" % (number, label, named))


def check_violations(entries, sections, rules, report, map_path, base):
    """The listed debt: a subset of the list on the main branch, with no stale position (WAY-51)."""
    root_of_map = os.path.dirname(os.path.dirname(os.path.abspath(map_path)))
    path = os.path.join(root_of_map, rules.violations.replace("/", os.sep))
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    _, violation_sections = parse_map(text, rules)
    columns = rules.lists.get("Known violations", [])
    parts = {entry.identifier for entry in entries if entry.kind == "part"}

    positions = []
    for cells, line in rows(violation_sections, "Known violations"):
        if cells == columns:
            continue
        positions.append(tuple(cells))
        for index, column in enumerate(columns):
            if index >= len(cells) or not cells[index]:
                report.error(None, "%s:%d: the known violation records no *%s*"
                             % (rules.violations, line, column))
        for index in (0, 1):
            if index < len(cells) and cells[index] and cells[index] not in parts:
                report.error(None, "%s:%d: the known violation names `%s`, which is not in the "
                                   "map as a part" % (rules.violations, line, cells[index]))
        if any(re.search(r":\d+\b", cell) for cell in cells):
            report.error(None, "%s:%d: the known violation names a line number, which goes stale "
                               "at the next edit" % (rules.violations, line))

    report.cannot_check("new and stale violations",
                        "no command of the product reports the dependency graph")

    if not base:
        return
    directory = os.path.dirname(path)
    code, top = git(["rev-parse", "--show-toplevel"], directory)
    if code != 0:
        return
    relative = os.path.relpath(path, top.strip()).replace(os.sep, "/")
    code, base_text = git(["show", "%s:%s" % (base, relative)], directory)
    if code != 0:
        report.notes.append("%s has no %s; every position counts as added" % (base, relative))
        base_text = ""
    _, base_sections = parse_map(base_text, rules)
    on_base = {tuple(cells) for cells, _ in rows(base_sections, "Known violations")}
    for position in positions:
        if position not in on_base:
            report.error(None, "%s: `%s` is not on the list of %s: a position is added only by a "
                               "change of the foundation a human accepts"
                         % (rules.violations, " · ".join(position), base))


def check_flows(entries, sections, report, root, claims):
    if root is None and any(entry.kind == "critical flow" for entry in entries):
        report.cannot_check("the tests of the critical flows",
                            "the map does not lie in a git repository")
    for entry in entries:
        if entry.kind != "critical flow":
            continue
        value, line = entry.fields.get("Invariant", ["", entry.line])
        match = re.search(r"test:\s*(\S.*)$", value)
        if root is not None and not match:
            report.error(line, "%s: *Invariant* names no test of the flow" % entry.identifier)
        elif root is not None:
            relative = match.group(1).strip()
            full = os.path.join(root, relative.replace("/", os.sep))
            if not os.path.exists(full):
                report.error(line, "%s: test `%s` of `%s` does not exist"
                             % (entry.identifier, relative, entry.identifier))
            else:
                with open(full, encoding="utf-8", errors="replace") as handle:
                    if entry.identifier not in handle.read():
                        report.error(line, "%s: test `%s` does not name `%s`"
                                     % (entry.identifier, relative, entry.identifier))

        listed = set(identifiers(entry.fields.get("Parts", [""])[0]))
        value, line = entry.fields.get("Coverage", ["", entry.line])
        if not value or value == "none":
            report.cannot_check("the list of parts of `%s`" % entry.identifier,
                                "its test leaves no coverage file")
            continue
        full = os.path.join(root, value.replace("/", os.sep))
        if not os.path.exists(full):
            report.error(line, "%s: coverage file `%s` does not exist" % (entry.identifier, value))
            continue
        if claims is None:
            report.cannot_check("the list of parts of `%s`" % entry.identifier,
                                "git could not map the covered files to parts")
            continue
        with open(full, encoding="utf-8", errors="replace") as handle:
            covered = [row[3:].strip() for row in handle if row.startswith("SF:")]
        for path in covered:
            if os.path.isabs(path):
                path = os.path.relpath(path, root)
            path = path.replace(os.sep, "/")
            for owner in claims.get(path, []):
                if owner.identifier not in listed:
                    report.error(line, "%s: coverage of `%s` runs through `%s`, which is not in "
                                       "its list of parts"
                                 % (entry.identifier, entry.identifier, owner.identifier))
                    listed.add(owner.identifier)


def check_files(entries, sections, report, map_path):
    directory = os.path.dirname(os.path.abspath(map_path))
    code, top = git(["rev-parse", "--show-toplevel"], directory)
    if code != 0:
        report.cannot_check("the assignment of files to parts",
                            "the map does not lie in a git repository")
        return None, None
    root = top.strip()

    wanted, owner = {}, {}
    for entry in entries:
        if entry.kind != "part":
            continue
        for name in ("Files", "Trust boundary"):
            for pattern in patterns(entry, name):
                attribute = "partmap%d" % len(wanted)
                wanted[attribute] = pattern
                owner[attribute] = (entry, name, pattern)

    answer = matched_by_git(root, wanted, report)
    if answer is None:
        report.cannot_check("the assignment of files to parts", "git could not match the patterns")
        return root, None
    found, tracked = answer

    claims = {}
    for attribute, paths in found.items():
        entry, name, pattern = owner[attribute]
        if not paths:
            line = entry.fields.get(name, ["", entry.line])[1]
            what = "pattern" if name == "Files" else "trust boundary"
            report.error(line, "%s `%s` of `%s` matches no file git tracks"
                         % (what, pattern, entry.identifier))
        if name != "Files":
            continue
        for path in paths:
            claims.setdefault(path, []).append(entry)

    left_out = {cells[0]: line for cells, line in rows(sections, "Files left out on purpose")
                if cells}
    for path in tracked:
        owners = claims.get(path, [])
        if path in left_out:
            for entry in owners:
                report.error(left_out[path], "`%s` is left out on purpose and claimed by `%s`"
                             % (path, entry.identifier))
            continue
        if not owners:
            report.error(None, "no part claims `%s`: give it to a part or put it on the list of "
                               "files left out on purpose" % path)
        elif len(owners) > 1:
            report.error(owners[1].line, "`%s` is claimed by `%s` and `%s`"
                         % (path, owners[0].identifier, owners[1].identifier))
    return root, claims


def check_entries(entries, sections, rules, report):
    withdrawn = {cells[0]: line for cells, line in rows(sections, "Withdrawn identifiers") if cells}
    seen = {}
    for entry in entries:
        carried = {rules.marks[name] for name in entry.fields if name in rules.marks}
        present = [kind for kind in rules.kinds if kind in carried]
        if entry.kind is None:
            report.error(entry.line, "`%s` is neither a part, a critical flow nor a surface: "
                                     "no field of the template names its kind" % entry.identifier)
        elif len(present) > 1:
            report.error(entry.line, "`%s` carries the fields of a %s: an entry is of one kind, "
                                     "and a part's criticality is computed, never written"
                         % (entry.identifier, " and of a ".join(present)))
        if not re.match(r"^%s$" % IDENTIFIER, entry.identifier):
            report.error(entry.line, "`%s` is not an identifier of words in lower case joined by "
                                     "hyphens" % entry.identifier)
        if entry.identifier in seen:
            report.error(entry.line, "identifier `%s` is used twice, here and at line %d"
                         % (entry.identifier, seen[entry.identifier].line))
        else:
            seen[entry.identifier] = entry
        if entry.identifier in withdrawn:
            report.error(entry.line, "`%s` is withdrawn: a withdrawn identifier is never reused"
                         % entry.identifier)
        if entry.binding is None:
            report.error(entry.line, "%s: the binding sentence is missing" % entry.identifier)
        for name in rules.kinds.get(entry.kind, []):
            if name not in entry.fields or not entry.fields[name][0]:
                report.error(entry.line, "%s: field *%s* is missing" % (entry.identifier, name))

    parts = {entry.identifier for entry in entries if entry.kind == "part"}
    for entry in entries:
        for name in ("Depends on", "Parts"):
            if name not in entry.fields:
                continue
            value, line = entry.fields[name]
            for identifier in identifiers(value):
                if identifier in parts:
                    continue
                if identifier in withdrawn:
                    report.error(line, "%s: *%s* names `%s`, which is withdrawn"
                                 % (entry.identifier, name, identifier))
                else:
                    report.error(line, "%s: *%s* names `%s`, which is not in the map as a part"
                                 % (entry.identifier, name, identifier))


# --- the report -----------------------------------------------------------------------------


class Report:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.unchecked = []
        self.notes = []

    def error(self, line, message):
        self.errors.append((line, message))

    def warning(self, line, message):
        self.warnings.append((line, message))

    def cannot_check(self, what, why):
        self.unchecked.append((what, why))

    def print(self, stream):
        for level, items in (("error", self.errors), ("warning", self.warnings)):
            for line, message in sorted(items, key=lambda item: item[0] or 0):
                stream.write("%s:%s: %s: %s\n" % (self.path, line or 0, level, message))
        for what, why in self.unchecked:
            stream.write("unchecked: %s — %s\n" % (what, why))
        for note in self.notes:
            stream.write("note: %s\n" % note)
        stream.write("%d error(s), %d warning(s), %d unchecked\n"
                     % (len(self.errors), len(self.warnings), len(self.unchecked)))


# --- entry point ----------------------------------------------------------------------------


def git(arguments, cwd, stdin=None):
    result = subprocess.run(["git"] + arguments, cwd=cwd, capture_output=True,
                            input=stdin.encode("utf-8") if stdin is not None else None)
    return result.returncode, result.stdout.decode("utf-8", "replace").replace("\r\n", "\n")


def run(map_path, base=None, stream=None, template=TEMPLATE):
    stream = stream or sys.stdout
    try:
        rules = read_rules(template)
    except (OSError, TemplateError, AttributeError) as problem:
        stream.write("cannot read the rules from %s: %s\n" % (template, problem))
        return 2
    try:
        with open(map_path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as problem:
        stream.write("cannot read the map: %s\n" % problem)
        return 2

    report = Report(map_path)
    entries, sections = parse_map(text, rules)
    check_entries(entries, sections, rules, report)
    check_criticality(entries, sections, rules, report)
    root, claims = check_files(entries, sections, report, map_path)
    check_flows(entries, sections, report, root, claims)
    check_surfaces(entries, sections, report, root)
    check_lists(sections, rules, report)
    check_scopes(entries, sections, report, map_path)
    check_violations(entries, sections, rules, report, map_path, base)
    if os.path.exists(EXAMPLES) and os.path.exists(OWN_MAP) and os.path.samefile(map_path, OWN_MAP):
        check_examples(entries, EXAMPLES, report)
    report.print(stream)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a part map against its template.")
    parser.add_argument("map", nargs="?", default=os.path.join("foundations", "part_map.md"))
    parser.add_argument("--base", help="the main branch to compare the map with, e.g. origin/main")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.map, arguments.base)


if __name__ == "__main__":
    sys.exit(main())
