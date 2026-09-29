"""Format guard of a product's invariants file.

Checks the file against the rules of template.md, which lies next to this script, and against the
rules of form the elements share, in elements/common/rules.md. The fields of an entry and the words
each may hold, the titles and columns of the lists of quarantined and recovered invariants, the
file of violated invariants, the values the gate fills in and the words a sentence may not use are
read from the template; the fields the main branch holds `TODO` in, the list of withdrawn
identifiers and the file and row of human verdicts are read from the rules the elements share; so
each rule lives in one place (WAY-35, WAY-71). The words that open what was searched and what was
found in a row of the list of recovered invariants, `searched:` and `found:`, are written in this
script, as WAY-58 writes the row. An entry carrying *Recovered*, which is not a field
of the form, is reported, and every other check reads it as it reads any entry. The decision log
and the part map are read with the parsers of their own guards, and the record of a run is written
with the report the guards share. Each check cites the invariants it gives a verdict for, as
`invariant: <identifier>/<version>` (WAY-65).

Usage, from the root of the product's repository:

    python <the-way>/elements/invariants/format_guard.py [FILE] [--base REF] [--merge-onto REF]
        [--record PATH]

FILE defaults to foundations/invariants.md. --base names the commit the task branch left the main
branch from; only with it are the identifiers, versions, corrections and the list of violated
invariants compared with that commit. --merge-onto names the commit of the main branch a merge is
made onto; only with it is a `TODO` in a field the main branch does not hold it in reported as an
error, and every fingerprint in *Derives from* and *Rests on* compared with the current binding
part in the decision log that merge leaves (WAY-31, WAY-71). `none`, given to either option, is the value
the gate fills in where that commit does not exist (WAY-61): the checks that need the commit are
then recorded as `unchecked`, a note says so, and they give no error; a commit that is not `none`
and does not exist stays an error. --record names a JSON Lines file, created or overwritten, which
receives the-way's own record of the run (WAY-74): a verdict for each invariant cited by a check
the run's options select — the checks against the base with --base, the checks of a merge with
--merge-onto, the checks of the file alone with neither — a line for each error of those checks
that belongs to no cited invariant, and every failure of the run itself. The report for a person
holds every check. Exit code: 0 without errors, 1 with errors, 2 when the file or the template
cannot be read or the record cannot be written.
"""

import argparse
import importlib.util
import os
import re
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
# The rules of form the elements share (WAY-09, WAY-35).
COMMON_RULES = os.path.join(HERE, "..", "common", "rules.md")
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
# The code the format guards share (WAY-09), and the form of an identifier and of a version
# from the relation model.
shared = _load("elements_common_guard_shared",
               os.path.join(HERE, "..", "common", "guard_shared.py"))
identifier_form = _load("relation_model_identifier",
                        os.path.join(HERE, "..", "..", "relation-model", "identifier.py"))
fingerprint_module = _load("relation_model_fingerprint",
                           os.path.join(HERE, "..", "..", "relation-model", "fingerprint.py"))
fingerprint = decision_guard.fingerprint
FACTS_GUARD = os.path.join(HERE, "..", "environment-facts", "format_guard.py")
_facts_guard = []


def facts_guard():
    """The environment facts guard, loaded on first use, since it loads this guard itself."""
    if not _facts_guard:
        _facts_guard.append(_load("environment_facts_format_guard", FACTS_GUARD))
    return _facts_guard[0]


count_sentences = decision_guard.count_sentences
# A fingerprint as the script of `relation-model` gives it: its length in lower-case hex digits (WAY-02).
FINGERPRINT = r"[0-9a-f]{%d}" % fingerprint_module.LENGTH
# `TODO` as a word of its own anywhere in a value — whole, as an item, or inside a part such as
# `searched: TODO; found: …` — but not inside a path or a longer word, such as `docs/TODO.md`.
TODO_WORD = shared.TODO_WORD
# A value in braces in a command or a sentence, but not a shell variable such as `${HOME}`.
BRACED = r"(?<!\$)\{[^{}%s]*\}"

# The name a record gives this program, and each of its checks as PROGRAM::<function>.
PROGRAM = "elements/invariants/format_guard.py"
# The checks each option selects for the record; every other check reads the file alone and is
# recorded only by a run given neither option. A run records the checks its options select, and
# its own failures always (WAY-61, WAY-74).
SELECTED_BY = {"check_against_base": "--base", "check_merge_todo": "--merge-onto",
               "check_fingerprints": "--merge-onto"}
# The value the gate fills in for a commit that does not exist (WAY-61), and the reason a check
# that needs that commit records for being unchecked, word for word as the template lists it.
NO_COMMIT = shared.NO_COMMIT
NO_COMMIT_REASON = shared.NO_COMMIT_REASON
# Where a product's invariants stand, relative to the root of its repository (WAY-64).
FILE_PATH = "foundations/invariants.md"

IDENTIFIER = identifier_form.IDENTIFIER
DATE = r"\d{4}-\d{2}-\d{2}"
QUOTED = r'"[^"]*"|“[^”]*”'


# A template, or the rules the elements share, does not hold a form this guard reads.
TemplateError = shared.TemplateError


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
    main_todo: list = field(default_factory=list)   # fields the main branch holds `TODO` in
    verdicts_file: str = "human_verdicts.md"        # name of the file of human verdicts
    verdicts_columns: list = field(default_factory=list)


# Reading a template's sections and the rules the elements share is code the guards share.
_section = shared.template_section
_blocks = shared.markdown_blocks
_table_form = shared.table_form


def bare(value):
    """A value without the backticks that mark it as a literal word."""
    value = value.strip()
    if len(value) > 1 and value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        return value[1:-1]
    return value


def is_todo(value):
    value = bare(value)
    return value == "TODO" or value.startswith("TODO ")


def holds_todo(value):
    """Whether a value holds `TODO` as a word of its own anywhere in it (WAY-71)."""
    return bool(TODO_WORD.search(value or ""))


# The words a sentence may not hold outside quoted text, as "The sentence" lists them.
FORBIDDEN = re.compile(r'outside quoted text it holds neither the words ((?:"[^"]+"(?:\s+nor\s+)?)+)')


def read_rules(path=TEMPLATE, common=COMMON_RULES):
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
    main_todo, withdrawn, verdicts_file, verdicts_columns = shared.read_common(common)
    lists = [withdrawn] + [_table_form(block) for block in blocks[1:]]

    violated_section = _section(text, "Violated invariants")
    violated_file = re.search(r"`foundations/([^`]+\.md)`", violated_section)
    violated_blocks = _blocks(violated_section)
    if not violated_file or not violated_blocks:
        raise TemplateError("the section on violated invariants names no file or no form")
    violated_title, violated_columns = _table_form(violated_blocks[0])

    gate_values = re.findall(r"`(\{[a-z-]+\})`", _section(text, "Method"))
    if not gate_values:
        raise TemplateError("the section on the method lists no value the gate fills in")

    words = FORBIDDEN.search(" ".join(_section(text, "The sentence").split()))
    if not words:
        raise TemplateError("the section on the sentence names no words a sentence may not hold")
    return Rules(fields, lists, violated_file.group(1), violated_title, violated_columns,
                 gate_values, re.findall(r'"([^"]+)"', words.group(1)), main_todo,
                 verdicts_file, verdicts_columns)


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


@dataclass
class Unknown:
    """A heading that is neither an entry's `## <identifier>/<version>` nor a list's title."""
    line: int
    heading: str
    body: list


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
    for line, lines in shared.split_sections(text):
        heading = lines[0][3:].strip()
        match = re.match(r"^(.+?)/(\d+)$", heading)
        if heading in list_titles:
            items.append(parse_table(heading, line, lines[1:]))
            continue
        if not match:
            items.append(Unknown(line, heading, lines[1:]))
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
        entry.fields = shared.parse_fields(body[index:], line + 1 + index)
        entry.strays = stray_lines(body[index:], line + 1 + index)
        items.append(entry)
    return items


def flat(value):
    return " ".join(value.split())


def listed(value):
    return [item.strip() for item in flat(value).split(" · ") if item.strip()]


def label_of(entry):
    return "%s/%d" % (entry.identifier, entry.version)


def value_of(entry, name):
    return entry.fields.get(name, ["", entry.line])


def command_of(entry):
    """The command a method names, or None where the method is a path or `TODO`."""
    value = flat(value_of(entry, "Method")[0])
    if is_todo(value) or not (value.startswith("`") and value.endswith("`")):
        return None
    return bare(value)


def derived_numbers(entry, prefix):
    """The numbers of the decisions an entry's *Derives from* names, with or without a
    fingerprint."""
    if prefix is None:
        return set()
    derives = value_of(entry, "Derives from")[0]
    return {int(number) for number in
            re.findall(r"\b%s-(\d{2,})\b" % re.escape(prefix), " ".join(
                item for item in listed(derives) if not is_todo(item)))}


# --- the report and the record of a run -----------------------------------------------------


class Report(shared.Report):
    """The report the guards share, naming this program and its checks in the record."""

    def __init__(self, path, options=()):
        super().__init__(path, options, program=PROGRAM, selected_by=SELECTED_BY)


start_record = shared.start_record
write_record = shared.write_record


# --- what the checks read beside the invariants file ----------------------------------------


@dataclass
class Foundation:
    """What the checks read beside the invariants file."""
    root: str = None
    map_read: bool = False
    parts: set = field(default_factory=set)
    map_identifiers: set = field(default_factory=set)
    map_twice: list = field(default_factory=list)    # (identifier, line of its second holder)
    flow_invariants: set = field(default_factory=set)
    prose_flows: list = field(default_factory=list)  # flows naming their invariant in prose
    log_read: bool = False
    prefix: str = None
    latest: dict = field(default_factory=dict)       # number -> latest version of the decision
    decisions: dict = field(default_factory=dict)    # number -> fingerprint of its latest binding
    facts_read: bool = False
    facts: object = None                             # the facts guard's Facts, or None
    fact_holders: dict = field(default_factory=dict)  # identifier -> its line in the facts file

    @property
    def facts_have_entries(self):
        return bool(self.facts is not None and self.facts.entries)


def read_foundation(path, report, root):
    foundation = Foundation(root=root)
    directory = os.path.dirname(os.path.abspath(path))

    map_path = os.path.join(directory, "part_map.md")
    try:
        map_rules = map_guard.read_rules()
        with open(map_path, encoding="utf-8") as handle:
            entries, sections = map_guard.parse_map(handle.read(), map_rules)
        foundation.map_read = True
    except (OSError, UnicodeDecodeError, map_guard.TemplateError, AttributeError,
            IndexError) as problem:
        # a failure of the run, not of a check: every record holds it, whatever the options
        report.error(None, "cannot read the part map beside the file: %s" % problem)
        entries, sections, map_rules = [], {}, None
    holders = {}
    for entry in entries:
        if entry.identifier in holders:
            foundation.map_twice.append((entry.identifier, entry.line))
        holders.setdefault(entry.identifier, entry.line)
        if entry.kind == "part":
            foundation.parts.add(entry.identifier)
        if entry.kind == "critical flow" and "Invariant" in entry.fields:
            named = flat(entry.fields["Invariant"][0]).split(" — test:")[0].strip()
            if re.fullmatch(IDENTIFIER, named):
                foundation.flow_invariants.add(named)
            else:
                foundation.prose_flows.append(entry.identifier)
                report.cannot_check("whether a quarantine names the invariant of `%s`"
                                    % entry.identifier,
                                    "the flow names its invariant in prose, not by identifier")
    columns = map_rules.lists.get("Withdrawn identifiers") if map_rules else None
    for cells, line in map_guard.rows(sections, "Withdrawn identifiers"):
        if not cells or cells == columns:
            continue
        if cells[0] in holders:
            foundation.map_twice.append((cells[0], line))
        holders.setdefault(cells[0], line)
    foundation.map_identifiers = set(holders)

    facts_path = os.path.join(directory, "environment_facts.md")
    if not os.path.exists(facts_path):
        foundation.facts_read = True
        report.notes.append("there is no environment_facts.md beside the file: the environment "
                            "facts element has no entries")
    else:
        try:
            module = facts_guard()
            with open(facts_path, encoding="utf-8") as handle:
                foundation.facts = module.facts_of(handle.read(), module.read_rules())
            foundation.facts_read = True
            foundation.fact_holders = {identifier: entry.line for identifier, entry
                                       in foundation.facts.entries.items()}
            for identifier, line in foundation.facts.withdrawn.items():
                foundation.fact_holders.setdefault(identifier, line)
        except (OSError, UnicodeDecodeError, AttributeError, TemplateError) as problem:
            report.error(None, "cannot read the environment facts beside the file: %s" % problem)

    log_path = os.path.join(directory, "decisions.md")
    if not os.path.exists(log_path):
        foundation.log_read = True
        report.notes.append("there is no decisions.md beside the file: no decision is in force")
        return foundation
    log = shared.read_file(log_path, report, "the decision log beside the file")
    if log is None:
        return foundation
    foundation.log_read = True
    foundation.prefix = decision_guard.detect_prefix(log)
    if foundation.prefix:
        foundation.latest = latest_versions(decision_guard.parse_log(log, foundation.prefix))
        foundation.decisions = in_force(foundation.latest)
    return foundation


def latest_versions(log_entries):
    latest = {}
    for entry in log_entries:
        if entry.kind == "version" and (entry.number not in latest or
                                        latest[entry.number].version < entry.version):
            latest[entry.number] = entry
    return latest


def in_force(latest):
    """number -> the fingerprint of the binding sentences of each decision in force."""
    return {number: fingerprint(entry.binding) for number, entry in latest.items()
            if entry.binding is not None}


# --- checks of the file's shape -------------------------------------------------------------


def check_layout(items, rules, report):
    """Entries first, then the lists in the template's order, the last closing the file; a heading
    of an entry carries its version (WAY-57, WAY-64, WAY-68)."""
    # invariant: invariant-version-number/1
    check, version = "check_layout", "invariant-version-number/1"
    report.ran(check, version)
    titles = [title for title, _ in rules.lists]
    fields = re.compile(r"^- \*\*(%s):\*\*" % "|".join(re.escape(rule.name) for rule in rules.fields))
    seen = []
    for item in items:
        if isinstance(item, Unknown):
            if any(fields.match(line) for line in item.body):
                report.error(item.line, "heading `## %s` of an entry carries no version number; "
                                        "it reads `## <identifier>/<version>`" % item.heading,
                             check, (version,))
            else:
                report.error(item.line, "heading `## %s` is neither `## <identifier>/<version>` "
                                        "nor a list of the template" % item.heading, check)
        elif isinstance(item, Table):
            if item.title in seen:
                report.error(item.line, "the list `%s` stands twice" % item.title, check)
            seen.append(item.title)
            expected = dict(rules.lists)[item.title]
            if item.columns != expected:
                report.error(item.line, "the list `%s` has columns %s, not %s"
                             % (item.title, " | ".join(item.columns), " | ".join(expected)), check)
        elif seen:
            report.error(item.line, "entry `%s` stands after the list `%s`"
                         % (item.identifier, seen[-1]), check)
    for title in titles:
        if title not in seen:
            report.error(None, "the file has no list `%s`" % title, check)
    if [title for title in seen if title in titles] != [title for title in titles if title in seen]:
        report.error(None, "the lists closing the file are not in the order %s"
                     % ", ".join("`%s`" % title for title in titles), check)


def check_file(path, top, tracked, report):
    """The repository holds one file of invariant entries, at foundations/invariants.md (WAY-64).
    The path is compared, letter case included, as git lists it. Another such file is known by its
    content: a tracked Markdown file holding a section `## <identifier>/<version>` with a *Method*
    field and no *Holds for* field."""
    # invariant: invariants-file/1
    check, one_file = "check_file", "invariants-file/1"
    if top is None or tracked is None:
        if os.path.basename(path) != "invariants.md" or \
                os.path.basename(os.path.dirname(os.path.abspath(path))) != "foundations":
            report.error(None, "a product's invariants stand in %s" % FILE_PATH, check, (one_file,))
        return
    report.ran(check, one_file)
    given = os.path.relpath(os.path.abspath(path), top).replace(os.sep, "/")
    listed_as = [name for name in tracked if name.lower() == given.lower()]
    if listed_as:
        given = listed_as[0]
    if given != FILE_PATH:
        report.error(None, "a product's invariants stand in %s, not in %s" % (FILE_PATH, given),
                     check, (one_file,))
    for name in tracked:
        if name == given or not name.endswith(".md"):
            continue
        full = os.path.join(top, *name.split("/"))
        try:
            with open(full, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError):
            continue
        if holds_entries(text):
            report.error(None, "`%s` is a second file of invariant entries; the repository holds "
                               "one, %s" % (name, FILE_PATH), check, (one_file,))


def holds_entries(text):
    """Whether a Markdown text holds an entry of invariants: a section `## <identifier>/<version>`,
    outside a fenced block, carrying a *Method* field and no *Holds for* field, which an
    environment fact entry carries."""
    heading, fenced, method, holds = None, False, False, False
    for line in text.split("\n"):
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        elif fenced:
            continue
        elif line.startswith("#"):
            if heading and method and not holds:
                return True
            heading = re.match(r"^## .+/\d+\s*$", line)
            method = holds = False
        elif heading and line.startswith("- **Method:**"):
            method = True
        elif heading and line.startswith("- **Holds for:**"):
            holds = True
    # the last section, a block left open after it included
    return bool(heading and method and not holds)


def cell(cells, columns, name):
    """The cell of a row under the column of that name, or "" where the row or the list has
    none."""
    index = columns.index(name) if name in columns else None
    return cells[index] if index is not None and index < len(cells) else ""


def check_identifiers(entries, withdrawn, foundation, report, columns=()):
    """Every identifier has the form `elements/common/` gives and is held once among the entries and
    withdrawn identifiers of this file, of the environment facts and of the part map; every
    withdrawn identifier gives why, and names as successors only entries or withdrawn identifiers
    of this file, or `none` (WAY-64). The form of an entry's identifier answers to
    invariant-identifier-form, and that of a withdrawn one to withdrawal-successors. `columns` are
    those of the file's list of withdrawn identifiers."""
    # invariant: identifier-holders/1
    # invariant: invariant-identifier-form/1
    # invariant: withdrawal-successors/1
    check = "check_identifiers"
    holders, form, successors_named = ("identifier-holders/1", "invariant-identifier-form/1",
                                       "withdrawal-successors/1")
    report.ran(check, form, successors_named)
    if foundation.map_read and foundation.facts_read:
        report.ran(check, holders)
    for identifier, line in foundation.map_twice:
        report.error(None, "part_map.md:%d: identifier `%s` is held twice in the part map"
                     % (line, identifier), check, (holders,))
    # the sentence of identifier-holders covers every pair of the three files, so the facts are
    # compared with each other and with the part map here as well as with this file
    fact_seen = {}
    for identifier, line in (foundation.facts.holders if foundation.facts is not None else []):
        if identifier in fact_seen:
            report.error(None, "environment_facts.md:%d: identifier `%s` is held twice in the "
                               "environment facts (line %d)" % (line, identifier,
                                                                fact_seen[identifier]),
                         check, (holders,))
        elif identifier in foundation.map_identifiers:
            report.error(None, "environment_facts.md:%d: identifier `%s` is held by the part map"
                         % (line, identifier), check, (holders,))
        fact_seen.setdefault(identifier, line)
    seen = {}
    for identifier, line, is_entry in [(entry.identifier, entry.line, True) for entry in entries] + \
            [(cells[0], line, False) for cells, line in withdrawn]:
        if identifier == "none" or not re.fullmatch(IDENTIFIER, identifier):
            report.error(line, "`%s` is not an identifier of words in lower case joined by "
                               "hyphens" % identifier, check,
                         (form,) if is_entry else (successors_named,))
        elif identifier in seen:
            report.error(line, "identifier `%s` is used twice (line %d)" % (identifier, seen[identifier]),
                         check, (holders,))
        elif identifier in foundation.map_identifiers:
            report.error(line, "identifier `%s` is held by the part map" % identifier,
                         check, (holders,))
        elif identifier in foundation.fact_holders:
            report.error(line, "identifier `%s` is held by the environment facts (line %d)"
                         % (identifier, foundation.fact_holders[identifier]), check, (holders,))
        seen.setdefault(identifier, line)
    names = set(seen)
    for cells, line in withdrawn:
        why = cell(cells, columns, "Why")
        successors = cell(cells, columns, "Successors")
        if not why.strip() or bare(why) == "none" or holds_todo(why):
            report.error(line, "withdrawn `%s` gives no reason in *Why*" % cells[0],
                         check, (successors_named,))
        if bare(successors) == "none":
            continue
        for successor in listed(successors) or [""]:
            if successor not in names:
                report.error(line, "withdrawn `%s` names successor `%s`, which is neither an entry "
                                   "nor a withdrawn identifier of this file" % (cells[0], successor),
                             check, (successors_named,))


# *Recovered* is not a field of the form; a recovered invariant stands on the list of recovered
# invariants (WAY-58).
OLD_RECOVERED = "Recovered"


def check_fields(entries, rules, report, facts_have_entries=False):
    """Every field of the form is present, and holds `none` or `TODO` only where the form gives it
    that word; a `TODO` the form gives, in a field the main branch does not hold it in, is a
    warning — *Rests on* included once the environment facts element has entries (WAY-71)."""
    # invariant: invariant-entry-field-presence/1
    # invariant: invariant-entry-field-words/1
    check = "check_fields"
    presence, words = "invariant-entry-field-presence/1", "invariant-entry-field-words/1"
    report.ran(check, presence, words)
    names = [rule.name for rule in rules.fields]
    for entry in entries:
        label = label_of(entry)
        for name, (value, line) in entry.fields.items():
            if name == OLD_RECOVERED and name not in names:
                report.error(line, "%s: *%s* is not a field of the form; a recovered invariant "
                                   "stands on the list of recovered invariants" % (label, name),
                             check)
            elif name not in names:
                report.error(line, "%s: field *%s* is not in the template" % (label, name), check)
        for rule in rules.fields:
            if rule.name not in entry.fields or not entry.fields[rule.name][0].strip():
                report.error(entry.line, "%s: field *%s* is missing" % (label, rule.name),
                             check, (presence,))
                continue
            value, line = entry.fields[rule.name]
            if bare(value) == "none" and not rule.none:
                report.error(line, "%s: *%s* may not hold `none`" % (label, rule.name),
                             check, (words,))
            if holds_todo(value):
                if not rule.todo:
                    report.error(line, "%s: *%s* may not hold `TODO`" % (label, rule.name),
                                 check, (words,))
                elif rule.name not in rules.main_todo or \
                        (rule.name == "Rests on" and facts_have_entries):
                    report.warning(line, "%s: *%s* holds `TODO`, which a merge onto the main "
                                         "branch does not take" % (label, rule.name))


def check_sentence(entries, rules, report):
    # invariant: invariant-sentence-count/1
    # invariant: sentence-branch-names/1
    # invariant: sentence-gate-values/1
    check = "check_sentence"
    count, branch_names, gate_values = ("invariant-sentence-count/1", "sentence-branch-names/1",
                                        "sentence-gate-values/1")
    report.ran(check, count, branch_names, gate_values)
    for entry in entries:
        label = label_of(entry)
        if entry.sentence is None:
            report.error(entry.line, "%s: the sentence is missing" % label, check, (count,))
            continue
        line = entry.line + 2
        sentences = count_sentences(entry.sentence)
        if sentences != 1:
            report.error(line, "%s: %d sentences, an entry states one" % (label, sentences),
                         check, (count,))
        for offset in entry.strays:
            report.error(offset, "%s: text outside the sentence and the fields; an entry states one "
                                 "sentence" % label, check, (count,))
        unquoted = re.sub(QUOTED, " ", flat(entry.sentence))
        for words in rules.forbidden_words:
            if re.search(r"\b%s(?:es)?\b" % re.escape(words), unquoted, re.I):
                report.error(line, '%s: the sentence names "%s" outside quoted text'
                             % (label, words), check, (branch_names,))
        if re.search(r"~\s*\w", unquoted):
            report.error(line, "%s: the sentence states a bound with a tilde, not a number" % label,
                         check)
        command = command_of(entry)
        for value in re.findall(BRACED % r"\s", unquoted):
            if value not in rules.gate_values:
                report.error(line, "%s: `%s` is not a value the gate fills in (%s)"
                             % (label, value, ", ".join(rules.gate_values)), check, (gate_values,))
            elif command is not None and value not in command:
                report.error(line, "%s: the sentence names `%s`, which its command does not take"
                             % (label, value), check, (gate_values,))


# The name of a program: a word, not a path, a flag or an assignment of a variable.
PROGRAM_NAME = re.compile(r"[A-Za-z0-9_][\w.+-]*")


def check_method(entries, rules, top, report):
    # invariant: invariant-method-form/1
    # invariant: method-gate-values/1
    check, form, gate_values = "check_method", "invariant-method-form/1", "method-gate-values/1"
    report.ran(check, gate_values)
    decided = True
    for entry in entries:
        label = label_of(entry)
        raw, line = value_of(entry, "Method")
        value = flat(raw)
        if not value:
            report.fail(line, "%s: *Method* is empty" % label, check, (form,))
            continue
        if is_todo(value):
            continue
        command = command_of(entry)
        if command is not None:
            tokens = command.split()
            if not tokens or not PROGRAM_NAME.fullmatch(tokens[0]):
                report.error(line, "%s: a command begins with the name of the program it runs, not "
                                   "`%s`" % (label, tokens[0] if tokens else ""), check, (form,))
            for taken in re.findall(BRACED % "", command):
                if taken not in rules.gate_values:
                    report.error(line, "%s: the command takes `%s`, which is not a value the gate "
                                       "fills in (%s)" % (label, taken, ", ".join(rules.gate_values)),
                                 check, (gate_values,))
            continue
        if "`" in value or " " in value:
            report.error(line, "%s: *Method* is neither a command in backticks, the path of a file, "
                               "nor `TODO`" % label, check, (form,))
        elif top is None:
            decided = False
        elif not os.path.isfile(os.path.join(top, value)):
            report.error(line, "%s: *Method* names `%s`, which is not a file" % (label, value),
                         check, (form,))
    if decided:
        report.ran(check, form)


def check_links(entries, foundation, report):
    """Every name in *Rests on* and *Derives from*, other than `none` or `TODO`, carries a
    fingerprint, and every decision named is one in force (WAY-31). Whether the fingerprint is the
    current one is checked against a merge, in check_fingerprints."""
    # invariant: link-fingerprint-presence/1
    check, presence = "check_links", "link-fingerprint-presence/1"
    report.ran(check, presence)
    for entry in entries:
        label = label_of(entry)
        rests, line = value_of(entry, "Rests on")
        items = [item for item in listed(rests) if item != "none" and not is_todo(item)] \
            if bare(rests) != "none" else []
        if items and foundation.facts_read and not foundation.facts_have_entries:
            report.error(line, "%s: *Rests on* names a fact, but the environment facts element has "
                               "no entries; the fact is written as `TODO — <the fact, with its "
                               "source>`" % label, check)
            for item in items:
                if not re.search(r"@%s$" % FINGERPRINT, item):
                    report.fail(line, "%s: `%s` in *Rests on* carries no fingerprint"
                                % (label, item), check, (presence,))
            items = []
        for item in items:
            match = re.fullmatch(r"(%s)@%s" % (IDENTIFIER, FINGERPRINT), item)
            if not re.search(r"@%s$" % FINGERPRINT, item):
                report.error(line, "%s: `%s` in *Rests on* carries no fingerprint of %d hex digits; "
                                   "it reads `<fact>@<fingerprint>`"
                             % (label, item, fingerprint_module.LENGTH), check, (presence,))
            elif not match:
                report.error(line, "%s: `%s` in *Rests on* is not `<fact>@<fingerprint>`"
                             % (label, item), check)
            elif foundation.facts is None:
                continue
            elif match.group(1) in foundation.facts.withdrawn:
                report.error(line, "%s: *Rests on* names `%s`, a withdrawn environment fact"
                             % (label, match.group(1)), check)
            elif match.group(1) not in foundation.facts.entries:
                report.error(line, "%s: *Rests on* names `%s`, which is not an entry of the "
                                   "environment facts" % (label, match.group(1)), check)

        derives, line = value_of(entry, "Derives from")
        items = [item for item in listed(derives) if item != "none" and not is_todo(item)] \
            if bare(derives) != "none" else []
        if not items:
            continue
        if foundation.prefix is None:
            report.error(line, "%s: *Derives from* names decisions, but there is no decision log "
                               "beside the file" % label, check)
        for item in items:
            if not re.search(r"@%s$" % FINGERPRINT, item):
                report.error(line, "%s: `%s` carries no fingerprint of %d hex digits; it reads "
                                   "`%s-NN@<fingerprint>`"
                             % (label, item, fingerprint_module.LENGTH,
                                foundation.prefix or "<prefix>"), check, (presence,))
                continue
            if foundation.prefix is None:
                continue
            match = re.fullmatch(r"%s-(\d{2,})@(%s)" % (re.escape(foundation.prefix), FINGERPRINT),
                                 item)
            if not match:
                report.error(line, "%s: `%s` is not `%s-NN@<fingerprint>`"
                             % (label, item, foundation.prefix), check)
            elif int(match.group(1)) not in foundation.decisions:
                report.error(line, "%s: `%s` names a decision that does not exist or binds nothing "
                                   "any more" % (label, item), check)


def derives_from_a_decision(entry, prefix):
    """Whether an entry's *Derives from* names a decision of the product's own log, the one beside
    the file; a decision named anywhere else does not count (WAY-58)."""
    return bool(derived_numbers(entry, prefix))


def check_part(entries, foundation, report):
    # invariant: invariant-part-names/1
    # invariant: invariant-part-form/1
    check, names, form = "check_part", "invariant-part-names/1", "invariant-part-form/1"
    report.ran(check, form)
    if foundation.map_read:
        report.ran(check, names)
    for entry in entries:
        label = label_of(entry)
        value, line = value_of(entry, "Part")
        parts = [part for part in listed(value) if part != "none" and not is_todo(part)] \
            if not is_todo(value) and bare(value) != "none" else []
        if not parts:
            report.fail(line, "%s: *Part* names neither `every` nor a part" % label, check, (form,))
            continue
        if "every" in parts and len(parts) > 1:
            report.error(line, "%s: *Part* names `every` and parts at once" % label, check, (form,))
        if not foundation.map_read:
            continue
        for part in parts:
            if part != "every" and part not in foundation.parts:
                report.error(line, "%s: *Part* names `%s`, which is not a part of the part map"
                             % (label, part), check, (names,))


def check_corrections(entries, report):
    check = "check_corrections"
    for entry in entries:
        label = label_of(entry)
        correction, line = value_of(entry, "Correction")
        declared = re.fullmatch(r"([0-9a-f]+) → ([0-9a-f]+)", flat(correction))
        if correction.strip() and bare(correction) != "none" and not declared:
            report.error(line, "%s: *Correction* is neither `none` nor `<fingerprint> → "
                               "<fingerprint>`" % label, check)
        elif declared and entry.sentence is not None and \
                declared.group(2) != fingerprint(entry.sentence):
            report.error(line, "%s: *Correction* names %s as the current fingerprint, but it is %s"
                         % (label, declared.group(2), fingerprint(entry.sentence)), check)


# The words that open the cells of what was searched and what was found in a row of the list of
# recovered invariants, as WAY-58 writes the row: `searched: <…>` and `found: <…>`.
RECOVERED_OPENINGS = (("Searched", "searched:"), ("Found", "found:"))


def check_recovered(table, entries, foundation, report):
    """Every row of the list of recovered invariants names an entry at its current version and
    holds `searched: <…>` and `found: <…>`; no entry on the list names in *Derives from* a decision
    of the decision log beside the file (WAY-58)."""
    # invariant: invariant-recovered-form/1
    # invariant: invariant-recovered-derived/1
    check, form, derived = ("check_recovered", "invariant-recovered-form/1",
                            "invariant-recovered-derived/1")
    report.ran(check, form, derived)
    columns = table.columns if table else []
    for cells, line in table.rows if table else []:
        if len(cells) < 4:
            report.error(line, "a row of the list of recovered invariants names an identifier, a "
                               "version, what was searched and what was found", check, (form,))
            continue
        identifier = cell(cells, columns, "Identifier") or cells[0]
        version = cell(cells, columns, "Version") or cells[1]
        entry = entries.get(identifier)
        if entry is None:
            report.error(line, "the list of recovered invariants names `%s`, which is not an entry"
                         % identifier, check, (form,))
        elif version != str(entry.version):
            report.error(line, "the list of recovered invariants names `%s` at version %s; its "
                               "current version is %d" % (identifier, version, entry.version),
                         check, (form,))
        for name, opening in RECOVERED_OPENINGS:
            value = cell(cells, columns, name).strip()
            if value and not value.startswith(opening):
                report.error(line, "the row of `%s` on the list of recovered invariants holds `%s` "
                                   "in *%s*, which does not open with `%s`"
                             % (identifier, value, name, opening), check, (form,))
            elif not value[len(opening):].strip():
                report.error(line, "the row of `%s` on the list of recovered invariants names "
                                   "nothing in *%s*" % (identifier, name), check, (form,))
        if entry is not None and derives_from_a_decision(entry, foundation.prefix):
            report.error(line, "%s stands on the list of recovered invariants, while its *Derives "
                               "from* names a decision of `foundations/decisions.md`"
                         % label_of(entry), check, (derived,))


LEVEL_ONE = re.compile(r"(?:^|\.\s+)level 1\b", re.I)
LEVEL_ONE_NAMES = re.compile(r"(?:^|\.\s+)level 1 — invariants: (.*?)(?:\.(?=\s|$)|$)", re.I)


def check_verifications(entries, foundation, report):
    """Every decision in force verified at level 1 has an entry deriving from it, and every
    identifier the level 1 verification of a decision's latest version names is an entry deriving
    from that decision (WAY-12, WAY-17). The names are read from the form the decision template
    gives: `level 1 — invariants: <identifier> · <identifier>.`"""
    # invariant: level-one-decision-invariants/1
    # invariant: verification-invariant-derivation/1
    check = "check_verifications"
    derived, named = "level-one-decision-invariants/1", "verification-invariant-derivation/1"
    if not foundation.log_read:
        return
    report.ran(check, derived)
    by_identifier = {entry.identifier: entry for entry in entries}
    deriving = {}
    for entry in entries:
        for number in derived_numbers(entry, foundation.prefix):
            deriving.setdefault(number, []).append(entry.identifier)
    readable = True
    for number, version in sorted(foundation.latest.items()):
        value, line = version.fields.get("Verification", ("", version.line))
        value = flat(value)
        if not LEVEL_ONE.search(value):
            continue
        decision = "%s-%02d" % (foundation.prefix, number)
        where = "decisions.md:%d" % line
        if version.binding is not None and number not in deriving:
            report.error(None, "%s: %s is in force and verified at level 1, but no entry of the file "
                               "derives from it" % (where, decision), check, (derived,))
        names = LEVEL_ONE_NAMES.search(value)
        if not names:
            readable = False
            report.error(None, "%s: the level 1 verification of %s/%d names no invariants as "
                               "`level 1 — invariants: <identifier> · <identifier>.`"
                         % (where, decision, version.version), check, (named,))
            continue
        for name in [bare(item) for item in names.group(1).split(" · ") if item.strip()]:
            if name not in by_identifier:
                report.error(None, "%s: the level 1 verification of %s/%d names `%s`, which is not "
                                   "an entry of the file" % (where, decision, version.version, name),
                             check, (named,))
            elif number not in derived_numbers(by_identifier[name], foundation.prefix):
                report.error(by_identifier[name].line, "%s: the level 1 verification of %s/%d names "
                                                       "it, but its *Derives from* does not name %s"
                             % (label_of(by_identifier[name]), decision, version.version, decision),
                             check, (named,))
    if readable:
        report.ran(check, named)


def check_quarantine(table, entries, foundation, report):
    # invariant: quarantine-position-form/1
    # invariant: quarantine-flow-invariants/1
    check, form, flows = ("check_quarantine", "quarantine-position-form/1",
                          "quarantine-flow-invariants/1")
    positions = table.rows if table else []
    report.ran(check, form)
    if foundation.map_read and not (foundation.prose_flows and positions):
        report.ran(check, flows)
    for cells, line in positions:
        if len(cells) < 3:
            report.error(line, "a quarantine row needs an identifier, a version and a date",
                         check, (form,))
            continue
        identifier, version, until = cells[:3]
        entry = entries.get(identifier)
        if entry is None:
            report.error(line, "quarantine names `%s`, which is not an entry" % identifier,
                         check, (form,))
        elif version != str(entry.version):
            report.error(line, "quarantine names `%s` at version %s; its current version is %d"
                         % (identifier, version, entry.version), check, (form,))
        if not re.fullmatch(DATE, until) or not decision_guard.valid_date(until):
            report.error(line, "quarantine of `%s` ends on `%s`, which is not a date YYYY-MM-DD"
                         % (identifier, until), check, (form,))
        if identifier in foundation.flow_invariants:
            report.error(line, "quarantine names `%s`, which a critical flow names" % identifier,
                         check, (flows,))


def violated_tables(text, rules):
    return [parse_table(rules.violated_title, line, lines[1:])
            for line, lines in shared.split_sections(text)
            if lines[0][3:].strip() == rules.violated_title]


def violated_positions(text, rules):
    return [row for table in violated_tables(text, rules) for row in table.rows]


def check_violated(path, entries, rules, report):
    # invariant: violated-position-version/1
    check, position_version = "check_violated", "violated-position-version/1"
    violated_path = os.path.join(os.path.dirname(os.path.abspath(path)), rules.violated_file)
    if not os.path.exists(violated_path):
        report.notes.append("there is no %s; the list of violated invariants is read as empty"
                            % rules.violated_file)
        report.ran(check, position_version)
        return []
    text = shared.read_file(violated_path, report, "the list of violated invariants")
    if text is None:
        return []
    report.ran(check, position_version)
    tables = violated_tables(text, rules)
    for table in tables:
        if table.columns != rules.violated_columns:
            report.error(None, "%s:%d: the list has columns %s, not %s"
                         % (rules.violated_file, table.line, " | ".join(table.columns),
                            " | ".join(rules.violated_columns)), check, (position_version,))
    positions = [row for table in tables for row in table.rows]
    for cells, line in positions:
        identifier, version = (cells + ["", ""])[:2]
        entry = entries.get(identifier)
        where = "%s:%d" % (rules.violated_file, line)
        if entry is None:
            report.error(None, "%s: `%s` is not an entry" % (where, identifier),
                         check, (position_version,))
        elif version != str(entry.version):
            report.error(None, "%s: `%s` at version %s; its current version is %d"
                         % (where, identifier, version, entry.version), check, (position_version,))
    return [(cells[0], cells[1]) for cells, _ in positions if len(cells) > 1]


def check_human_verdicts(path, entries, foundation, rules, report):
    """Every row of the file of human verdicts names an entry of the invariants or of the
    environment facts; a row naming an invariant names an entry whose method is a path, gives
    `pass` or `fail`, and reads `none` in *Until* (WAY-83). A row naming neither is an invariant
    row unless it carries a fact's date in *Until*. The rows naming a fact are the environment
    facts guard's to check further."""
    # invariant: human-verdict-invariant-row/1
    check, invariant_row = "check_human_verdicts", "human-verdict-invariant-row/1"
    verdicts_path = os.path.join(os.path.dirname(os.path.abspath(path)), rules.verdicts_file)
    if not os.path.exists(verdicts_path):
        report.notes.append("there is no %s; no human verdict is given" % rules.verdicts_file)
        report.ran(check, invariant_row)
        return
    text = shared.read_file(verdicts_path, report, "the human verdicts")
    if text is None:
        return
    report.ran(check, invariant_row)
    rows, headers = facts_guard().verdict_rows(text, rules.verdicts_columns)
    for number, cells in headers:
        report.error(None, "%s:%d: the list has columns %s, not %s"
                     % (rules.verdicts_file, number, " | ".join(cells),
                        " | ".join(rules.verdicts_columns)), check)
    facts = foundation.facts.entries if foundation.facts is not None else {}
    for cells, number in rows:
        where = "%s:%d" % (rules.verdicts_file, number)
        values = dict(zip(rules.verdicts_columns, cells + [""] * len(rules.verdicts_columns)))
        name = values.get("Entry", "")
        entry = entries.get(name)
        if entry is None:
            if name not in facts and foundation.facts_read:
                # A row that does not carry a fact's date in *Until* has an invariant's form
                # (rules.md), so it names an invariant that is no entry; a dated row is the facts
                # guard's to judge.
                invariant = (() if re.fullmatch(DATE, values.get("Until", ""))
                             else (invariant_row,))
                report.error(None, "%s: `%s` is neither an invariant nor an environment fact"
                             % (where, name), check, invariant)
            continue
        method = flat(value_of(entry, "Method")[0])
        if is_todo(method) or command_of(entry) is not None or "`" in method or " " in method:
            report.error(None, "%s: the method of `%s` is not a path" % (where, name),
                         check, (invariant_row,))
        if values.get("Verdict") not in ("pass", "fail"):
            report.error(None, "%s: *Verdict* is neither `pass` nor `fail`" % where,
                         check, (invariant_row,))
        if values.get("Until") != "none":
            report.error(None, "%s: an invariant's verdict reads `none` in *Until*" % where,
                         check, (invariant_row,))


# --- checks against the repository ----------------------------------------------------------


def repository_root(path, report):
    """The root of the file's repository, or None once the report holds the failure."""
    code, top, _ = shared.call_git(["rev-parse", "--show-toplevel"],
                                      os.path.dirname(os.path.abspath(path)))
    if code != 0:
        report.error(None, "the file does not lie in a git repository, so no check that asks git "
                           "which files it tracks or ignores can run")
        return None
    return top.strip()


def tracked_files(top, report):
    code, listing, message = shared.call_git(["ls-files", "-z"], top)
    if code != 0:
        report.error(None, "git cannot list the files it tracks in %s: %s" % (top, message))
        return None
    return [name for name in listing.split("\0") if name]


CITATION = re.compile(r"^\s*(?:#|//|--|;|%|\*|/\*|<!--|REM\b)\s*(invariant|data):\s*(\S+)\s*"
                      r"(?:\*/|-->)?\s*$")


def check_citations(entries, withdrawn, top, tracked, report, columns=()):
    # invariant: invariant-citation-version/1
    # invariant: invariant-citation-target/1
    # invariant: data-line-target/1
    check = "check_citations"
    version, target, data = ("invariant-citation-version/1", "invariant-citation-target/1",
                             "data-line-target/1")
    report.ran(check, version, target, data)
    successors = {cells[0]: (cell(cells, columns, "Successors") or "none") for cells, _ in withdrawn}
    for name in tracked:
        if name.endswith(".md"):
            continue
        try:
            with open(os.path.join(top, name), encoding="utf-8") as handle:
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
                if not os.path.isfile(os.path.join(top, value)):
                    report.error(None, "%s: `data: %s` names no file" % (where, value),
                                 check, (data,))
                continue
            # a version is a number written without a leading zero
            cited = re.fullmatch(r"(\S+)/(%s)" % identifier_form.VERSION, value)
            identifier = cited.group(1) if cited else value.split("/")[0]
            if identifier in successors:
                report.error(None, "%s: cites `%s`, which is withdrawn (successors: %s)"
                             % (where, identifier, successors[identifier]), check, (target,))
            elif identifier not in entries:
                report.error(None, "%s: cites `%s`, which is not an entry" % (where, identifier),
                             check, (target,))
            elif not cited:
                report.error(None, "%s: `invariant: %s` does not cite `<identifier>/<version>`"
                             % (where, value), check, (version,))
            elif int(cited.group(2)) != entries[identifier].version:
                report.error(None, "%s: cites `%s`, whose current version is %d"
                             % (where, value, entries[identifier].version), check, (version,))


def record_paths(command):
    """The distinct paths ending in `.jsonl` a command names, in the order it names them."""
    paths = []
    for token in command.split():
        token = token.strip("\"'").split("=")[-1]
        if token.endswith(".jsonl") and token not in paths:
            paths.append(token)
    return paths


def fact_commands(facts):
    """(where, line, command) for every fact of the environment facts file whose method is a
    command: `where` names the file, the line and the entry, since the report's own lines are those
    of the invariants file."""
    if facts is None:
        return []
    module = facts_guard()
    found = []
    for entry in sorted(facts.entries.values(), key=lambda item: item.line):
        command = module.command_of(entry)
        if command is None:
            continue
        line = module.value_of(entry, "Method")[1]
        label = entry.identifier if entry.version is None else module.label_of(entry)
        found.append(("environment_facts.md:%d: %s" % (line, label), None, command))
    return found


def check_record_paths(entries, top, report, facts=None, facts_read=True):
    """Every `.jsonl` path a command of this file or of the environment facts beside it names is
    one git ignores, as git itself answers, and no command names two (WAY-74). Letter case always
    counts: git ignores it where core.ignorecase is set, which git init sets on Windows and macOS,
    and a path would then be ignored there and not on Linux. Where the environment facts could not
    be read, the check records no pass."""
    # invariant: run-record-path/1
    check, record_path = "check_record_paths", "run-record-path/1"
    commands = [(label_of(entry), value_of(entry, "Method")[1], command_of(entry))
                for entry in entries] + fact_commands(facts)
    named = {}   # path -> (where, line) of the first command naming it
    for where, line, command in commands:
        if command is None:
            continue
        paths = record_paths(command)
        if len(paths) > 1:
            report.error(line, "%s: the command names %d records of a run (%s); it names one"
                         % (where, len(paths), ", ".join("`%s`" % p for p in paths)),
                         check, (record_path,))
        for path in paths:
            named.setdefault(path, (where, line))
    inside = []
    for path, (where, line) in named.items():
        normal = os.path.normpath(path).replace(os.sep, "/")
        if os.path.isabs(path) or normal == ".." or normal.startswith("../"):
            report.error(line, "%s: `%s` lies outside the repository, where git ignores nothing"
                         % (where, path), check, (record_path,))
        else:
            inside.append(path)
    ignored = set()
    if inside:
        code, answer, message = shared.call_git(["-c", "core.ignorecase=false", "check-ignore",
                                                    "-z", "--stdin"], top,
                                                   stdin="\0".join(inside) + "\0")
        if code not in (0, 1):
            report.error(None, "git cannot tell which paths it ignores: %s"
                         % (message or "git check-ignore exited with %d" % code), check)
            return
        ignored = {path for path in answer.split("\0") if path}
    if facts_read:
        report.ran(check, record_path)
    for path in inside:
        if path not in ignored:
            where, line = named[path]
            report.error(line, "%s: git does not ignore `%s`, the record of a run the command names"
                         % (where, path), check, (record_path,))


# --- the commit the branch left the main branch from ---------------------------------------


BASE_INVARIANTS = ("invariant-version-new/1", "invariant-version-changed/1",
                   "invariant-version-unchanged/1", "invariant-earlier-wording/1",
                   "invariant-identifier-persistence/1", "invariant-withdrawal-persistence/1",
                   "violated-list-growth/1")


def check_against_base(path, entries, withdrawn, violated, rules, base, top, report,
                       no_commit=None):
    """Compares the file and the list of violated invariants with their state on the base. Given
    `no_commit`, which says why there is no base, records the checks unchecked instead."""
    # invariant: invariant-version-new/1
    # invariant: invariant-version-changed/1
    # invariant: invariant-version-unchanged/1
    # invariant: invariant-earlier-wording/1
    # invariant: invariant-identifier-persistence/1
    # invariant: invariant-withdrawal-persistence/1
    # invariant: violated-list-growth/1
    check = "check_against_base"
    new, changed, unchanged, wording, persistence, withdrawal, growth = BASE_INVARIANTS
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, *BASE_INVARIANTS)
        return
    relative = os.path.relpath(os.path.abspath(path), top).replace(os.sep, "/")
    violated_relative = "/".join(filter(None, [os.path.dirname(relative), rules.violated_file]))
    base_text, failure = shared.file_at(base, relative, top)
    if failure:
        report.error(None, failure)
        return
    base_violated, failure = shared.file_at(base, violated_relative, top)
    if failure:
        report.error(None, failure)
        return
    if base_text is None:
        report.notes.append("%s has no %s; every entry is new" % (base, relative))
        base_text = ""
    report.ran(check, *BASE_INVARIANTS)

    base_items = parse_file(base_text, rules)
    base_entries = {item.identifier: item for item in base_items if isinstance(item, Entry)}
    base_withdrawn = {cells[0] for item in base_items if isinstance(item, Table)
                      and item.title == rules.lists[0][0] for cells, _ in item.rows if cells}
    withdrawn_now = {cells[0] for cells, _ in withdrawn if cells}

    for identifier in sorted(set(base_entries) | base_withdrawn):
        if identifier not in entries and identifier not in withdrawn_now:
            report.error(None, "`%s` stands in the file on %s and is gone; it stays as an entry or "
                               "a withdrawn identifier" % (identifier, base), check,
                         (persistence, withdrawal) if identifier in base_withdrawn
                         else (persistence,))
    for identifier in sorted(base_withdrawn & set(entries)):
        report.error(entries[identifier].line, "`%s` is withdrawn on %s and stands as an entry "
                                               "again" % (identifier, base), check, (withdrawal,))

    for identifier, entry in entries.items():
        label = label_of(entry)
        correction = flat(value_of(entry, "Correction")[0])
        if entry.sentence is None:
            continue
        now = fingerprint(entry.sentence)
        before = base_entries.get(identifier)
        if before is None or before.sentence is None:
            if entry.version != 1:
                report.error(entry.line, "%s: a new entry carries version 1" % label, check, (new,))
            if bare(correction) != "none":
                report.error(entry.line, "%s: a new entry declares no correction" % label,
                             check, (new,))
            continue
        then = fingerprint(before.sentence)
        declared = re.fullmatch(r"([0-9a-f]+) → ([0-9a-f]+)", correction)
        if now == then:
            if entry.version != before.version:
                report.error(entry.line, "%s: the sentence is unchanged since %s, where the version "
                                         "is %d" % (label, base, before.version), check, (unchanged,))
            if declared and declared.group(2) != now:
                report.error(entry.line, "%s: the correction names %s, but the fingerprint is %s"
                             % (label, declared.group(2), now), check, (unchanged,))
        elif entry.version == before.version + 1:
            if declared:
                report.error(entry.line, "%s: a raised version declares no correction" % label,
                             check, (changed,))
        elif entry.version == before.version and declared and \
                (declared.group(1), declared.group(2)) == (then, now):
            report.cannot_check("the correction of `%s`" % identifier,
                                "correction declared, confirmation not checked")
        else:
            report.error(entry.line, "%s: the sentence changed since %s (%s → %s); the version is "
                                     "%d, or a correction names `%s → %s`"
                         % (label, base, then, now, before.version + 1, then, now),
                         check, (changed,))
        if now != then and flat(before.sentence) in flat(entry.text.replace(entry.sentence, "", 1)):
            report.error(entry.line, "%s: the entry still holds its wording from %s" % (label, base),
                         check, (wording,))

    allowed = {(cells[0], cells[1]) for cells, _ in violated_positions(base_violated or "", rules)
               if len(cells) > 1}
    for position in violated:
        if position not in allowed:
            report.error(None, "%s: `%s` at version %s is not on the list on %s; a row is "
                               "added only by a foundation change a human accepts"
                         % (rules.violated_file, position[0], position[1], base), check, (growth,))


# --- the commit a merge onto the main branch is made onto ----------------------------------


def check_merge_todo(entries, rules, report, no_commit=None, facts_have_entries=False):
    """Reports every field of every entry that holds `TODO` where the main branch does not hold it
    (WAY-71); *Rests on* holds it there only until the environment facts element has entries.
    Given `no_commit`, which says why there is no commit to merge onto, records it unchecked
    instead."""
    # invariant: invariant-entry-merge-todo/1
    check, merge_todo = "check_merge_todo", "invariant-entry-merge-todo/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, merge_todo)
        return
    report.ran(check, merge_todo)
    for entry in entries:
        for name, (value, line) in entry.fields.items():
            if not holds_todo(value):
                continue
            if name not in rules.main_todo:
                report.error(line, "%s: *%s* holds `TODO`, which a merge onto the main branch does "
                                   "not take" % (label_of(entry), name), check, (merge_todo,))
            elif name == "Rests on" and facts_have_entries:
                report.error(line, "%s: *Rests on* holds `TODO`, which a merge onto the main branch "
                                   "does not take once the environment facts element has entries"
                             % label_of(entry), check, (merge_todo,))


def merged_decisions(path, foundation, merge_onto, top, report):
    """(prefix, number -> fingerprint of the binding sentences of each decision in force) in the
    decision log a merge onto the given commit leaves, or None once the report says why git could
    not read it.

    The log is append-only, so the merge holds every version either side holds; where both hold
    one, the merge carries the branch's copy (WAY-07), as the decision guard reads it."""
    log = os.path.join(os.path.dirname(os.path.abspath(path)), "decisions.md")
    relative = os.path.relpath(log, top).replace(os.sep, "/")
    onto_text, failure = shared.file_at(merge_onto, relative, top)
    if failure:
        report.error(None, failure)
        return None
    if onto_text is None:
        report.notes.append("%s has no %s; the decision log after the merge is this log alone"
                            % (merge_onto, relative))
        onto_text = ""
    prefix = foundation.prefix or decision_guard.detect_prefix(onto_text)
    texts = [onto_text]
    if foundation.prefix and os.path.exists(log):
        log_text = shared.read_file(log, report, "the decision log beside the file")
        if log_text is None:
            return None
        texts.insert(0, log_text)
    merged = {}
    for text in texts if prefix else []:
        for entry in decision_guard.parse_log(text, prefix):
            if entry.kind == "version":
                merged.setdefault((entry.number, entry.version), entry)
    return prefix, in_force(latest_versions(merged.values()))


def entries_on(path, commit, rules, top, report):
    """The entries of the file on the commit, or None once the report says why git could not read
    it."""
    relative = os.path.relpath(os.path.abspath(path), top).replace(os.sep, "/")
    text, failure = shared.file_at(commit, relative, top)
    if failure:
        report.error(None, failure)
        return None
    return [item for item in parse_file(text or "", rules) if isinstance(item, Entry)]


def merged_facts(path, foundation, merge_onto, top, report):
    """identifier -> current fingerprint of every environment fact a merge onto the commit leaves,
    each the branch's copy where the branch changed it since the merge base and the main branch's
    otherwise, as the facts guard merges them; None once the report says why git could not read
    them."""
    module = facts_guard()
    facts_path = os.path.join(os.path.dirname(os.path.abspath(path)), "environment_facts.md")
    relative = os.path.relpath(facts_path, top).replace(os.sep, "/")
    base = module.merge_base(top, merge_onto)
    texts = []
    for commit in (merge_onto, base):
        text, failure = shared.file_at(commit, relative, top) if commit else (None, None)
        if failure:
            report.error(None, failure)
            return None
        texts.append(text)
    try:
        rules = module.read_rules()
        onto, before = (module.facts_of(text, rules) for text in texts)
    except (OSError, UnicodeDecodeError, AttributeError, TemplateError) as problem:
        report.error(None, "cannot read the environment facts on %s: %s" % (merge_onto, problem))
        return None
    own = foundation.facts or module.Facts()
    return {identifier: module.entry_fingerprint(entry) for identifier, entry
            in module.merged_facts(own, onto, before).items()}


def check_fingerprints(entries, merged, report, no_commit=None, facts=None):
    """Compares every fingerprint in *Derives from* and *Rests on*, of the entries the file holds
    after the merge, with the current fingerprint of the entry it names in the decision log or the
    environment facts that merge leaves (WAY-31). The entries are the branch's, and those only the
    commit merged onto holds, as (entry, None or that commit); `facts` maps each fact the merge
    leaves to its fingerprint. Given `no_commit`, which says why there is no commit to merge onto,
    records it unchecked instead."""
    # invariant: link-fingerprint-value/1
    check, value = "check_fingerprints", "link-fingerprint-value/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, value)
        return
    report.ran(check, value)
    prefix, current = merged
    facts = facts or {}
    for entry, onto in entries:
        where = "%s%s" % (label_of(entry), " (on %s)" % onto if onto else "")
        for name in ("Derives from", "Rests on"):
            raw, line = value_of(entry, name)
            line = None if onto else line
            for item in listed(raw) if bare(raw) != "none" else []:
                if is_todo(item) or not re.search(r"@[0-9a-f]+$", item):
                    continue
                if name == "Rests on":
                    fact = re.fullmatch(r"(%s)@([0-9a-f]+)" % IDENTIFIER, item)
                    if fact is None or fact.group(1) not in facts:
                        report.error(line, "%s: `%s` in *Rests on* names no environment fact the "
                                           "merge holds" % (where, item), check, (value,))
                    elif facts[fact.group(1)] != fact.group(2):
                        report.error(line, "%s: `%s` — the current fingerprint of `%s` after the "
                                           "merge is %s" % (where, item, fact.group(1),
                                                            facts[fact.group(1)]),
                                     check, (value,))
                    continue
                match = re.fullmatch(r"%s-(\d{2,})@([0-9a-f]+)" % re.escape(prefix), item) \
                    if prefix else None
                if match is None:
                    report.error(line, "%s: `%s` in *%s* names no entry whose fingerprint the merge "
                                       "holds" % (where, item, name), check, (value,))
                elif int(match.group(1)) not in current:
                    report.error(line, "%s: `%s` names a decision that binds nothing after the "
                                       "merge" % (where, item), check, (value,))
                elif current[int(match.group(1))] != match.group(2):
                    report.error(line, "%s: `%s` — the current fingerprint of %s-%s after the merge "
                                       "is %s" % (where, item, prefix, match.group(1),
                                                  current[int(match.group(1))]),
                                 check, (value,))


# --- the examples ---------------------------------------------------------------------------


def check_examples(entries, examples_path, report):
    """Every identifier `examples.md` names is the identifier of an entry of the invariants file: an
    example names an entry of the-way's invariants by its identifier instead of copying it (WAY-09,
    WAY-34). An item of a list names the identifier it opens with."""
    # invariant: invariant-example-target/1
    check, target = "check_examples", "invariant-example-target/1"
    examples = shared.read_file(examples_path, report, "the examples")
    if examples is None:
        return
    report.ran(check, target)
    for number, line in enumerate(examples.split("\n"), start=1):
        item = re.match(r"^- `?([^`\s]+)`?", line)
        if item and item.group(1) not in entries:
            report.error(None, "examples.md:%d: `%s` is not the identifier of an entry of the file"
                         % (number, item.group(1)), check, (target,))


# --- entry point ----------------------------------------------------------------------------


def find_commit(path, top, option, commit, report):
    """Whether the commit exists in the file's repository; where it does not, the report says so.
    A failure here is no rule's: it belongs to the run."""
    if top is None:
        report.error(None, "%s %s given, but the file is not in a git repository" % (option, commit))
        return False
    return shared.find_commit(top, option, commit, report)


def run(path, base=None, stream=None, template=TEMPLATE, merge_onto=None, record=None,
        examples=EXAMPLES, common=COMMON_RULES, own=None):
    """Checks the invariants file at the path. `own` says whether it is the-way's own file, whose
    examples are checked, and which by default is known by its path."""
    stream = stream or sys.stdout
    if record is not None:
        try:
            start_record(record)
        except OSError as problem:
            stream.write("cannot write the record: %s\n" % problem)
            return 2
    report = Report(path, [option for option, value in (("--base", base),
                                                         ("--merge-onto", merge_onto)) if value])

    def stop(message):
        stream.write(message + "\n")
        report.error(None, message)
        if record is not None:
            write_record(record, report)
        return 2

    try:
        rules = read_rules(template, common)
    except (OSError, UnicodeDecodeError, TemplateError, AttributeError) as problem:
        return stop("cannot read the rules from %s and %s: %s" % (template, common, problem))
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError) as problem:
        return stop("cannot read the invariants file: %s" % problem)

    top = repository_root(path, report)
    tracked = tracked_files(top, report) if top is not None else None
    foundation = read_foundation(path, report, top)
    items = parse_file(text, rules)
    entry_list = [item for item in items if isinstance(item, Entry)]
    entries = {}
    for entry in entry_list:
        entries.setdefault(entry.identifier, entry)
    tables = {item.title: item for item in items if isinstance(item, Table)}
    withdrawn_table = tables.get(rules.lists[0][0])
    withdrawn = withdrawn_table.rows if withdrawn_table else []
    withdrawn_columns = withdrawn_table.columns if withdrawn_table else rules.lists[0][1]

    check_layout(items, rules, report)
    check_file(path, top, tracked, report)
    check_identifiers(entry_list, withdrawn, foundation, report, withdrawn_columns)
    check_fields(entry_list, rules, report, foundation.facts_have_entries)
    check_sentence(entry_list, rules, report)
    check_method(entry_list, rules, top, report)
    check_links(entry_list, foundation, report)
    check_part(entry_list, foundation, report)
    check_corrections(entry_list, report)
    check_recovered(tables.get(rules.lists[2][0]), entries, foundation, report)
    check_verifications(entry_list, foundation, report)
    check_quarantine(tables.get(rules.lists[1][0]), entries, foundation, report)
    violated = check_violated(path, entries, rules, report)
    check_human_verdicts(path, entries, foundation, rules, report)
    if tracked is not None:
        check_citations(entries, withdrawn, top, tracked, report, withdrawn_columns)
        check_record_paths(entry_list, top, report, foundation.facts, foundation.facts_read)

    if base == NO_COMMIT:
        no_base = "--base none: there is no commit the branch left the main branch from"
        check_against_base(path, entries, withdrawn, violated, rules, None, None, report,
                           no_commit=no_base)
        report.notes.append(no_base + "; identifiers, versions, corrections and the list of "
                                      "violated invariants are not compared with it, and those "
                                      "checks are unchecked")
    elif base:
        if find_commit(path, top, "--base", base, report):
            check_against_base(path, entries, withdrawn, violated, rules, base, top, report)
    else:
        report.notes.append("no --base given: identifiers, versions, corrections and the list of "
                            "violated invariants are not compared with the main branch")

    if merge_onto == NO_COMMIT:
        no_onto = "--merge-onto none: there is no commit to merge onto"
        check_merge_todo(entry_list, rules, report, no_commit=no_onto)
        check_fingerprints(None, None, report, no_commit=no_onto)
        report.notes.append(no_onto + "; `TODO` in the entries and the fingerprints their links "
                                      "carry are not checked against a merge, and those checks "
                                      "are unchecked")
    elif merge_onto:
        if find_commit(path, top, "--merge-onto", merge_onto, report):
            facts = merged_facts(path, foundation, merge_onto, top, report)
            check_merge_todo(entry_list, rules, report, facts_have_entries=bool(facts))
            merged = merged_decisions(path, foundation, merge_onto, top, report)
            onto_entries = entries_on(path, merge_onto, rules, top, report)
            if merged is not None and onto_entries is not None and facts is not None:
                withdrawn_now = {cells[0] for cells, _ in withdrawn if cells}
                after = [(entry, None) for entry in entry_list] + \
                    [(entry, merge_onto) for entry in onto_entries
                     if entry.identifier not in entries and entry.identifier not in withdrawn_now]
                check_fingerprints(after, merged, report, facts=facts)
    else:
        report.notes.append("no --merge-onto given: `TODO` in the entries is not checked against a "
                            "merge, and the fingerprints their links carry are not compared with "
                            "the current binding part")

    if own is None:
        own = os.path.exists(OWN_FILE) and os.path.samefile(path, OWN_FILE)
    if own and os.path.exists(examples):
        check_examples(entries, examples, report)
    report.print(stream)
    if record is not None:
        write_record(record, report)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a product's invariants against the template.")
    parser.add_argument("file", nargs="?", default=os.path.join("foundations", "invariants.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from, to "
                                       "compare identifiers, versions, corrections and the list of "
                                       "violated invariants with; `none` where it does not exist, "
                                       "which records those checks as unchecked")
    parser.add_argument("--merge-onto", help="the commit of the main branch a merge is made onto; "
                                             "only with it is `TODO` reported in a field the main "
                                             "branch does not hold it in, and every fingerprint in "
                                             "*Derives from* and *Rests on* compared with the "
                                             "decision log the merge leaves; `none` where the main "
                                             "branch does not exist, which records those checks as "
                                             "unchecked")
    parser.add_argument("--record", help="the JSON Lines file, created or overwritten, that "
                                         "receives a verdict for each invariant a check cites")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.file, arguments.base, merge_onto=arguments.merge_onto,
               record=arguments.record)


if __name__ == "__main__":
    sys.exit(main())
