"""Format guard of a product's environment facts file.

Runs the checks listed in "What the format guard checks" in template.md, which lies next to this
script. The fields of an entry and the words each may hold, the title and columns of the list of
withdrawn identifiers, the file and columns of human verdicts and the words *Holds for* may not read
are taken from the template, so the rules of an entry live in one place (WAY-05, WAY-35, WAY-71).
The decision log, the invariants and the part map are read with the parsers of their own guards,
and the record of a run is written with the part map guard's report. Each check cites the
invariants it gives a verdict for, as `invariant: <identifier>/<version>` (WAY-65).

Usage, from the root of the product's repository:

    python <the-way>/elements/environment-facts/format_guard.py [FILE] [--base REF]
        [--merge-onto REF] [--record PATH]

FILE defaults to foundations/environment_facts.md. --base names the commit the task branch left the
main branch from; only with it are identifiers and versions compared with that commit (WAY-75,
WAY-79). --merge-onto names the commit of the main branch a merge is made onto; only with it is
`TODO` outside *Method* reported against a merge, every fingerprint a decision's *Based on* carries
for a fact compared with the fact's current fingerprint after that merge, and a fact that nothing
names reported as an error rather than a warning (WAY-71, WAY-88, WAY-90). `none`, given to either
option, is the value the gate fills in where that commit does not exist (WAY-61): the checks that
need the commit are then recorded as `unchecked`, a note says so, and they give no error; a commit
that is not `none` and does not exist stays an error. --record names a JSON Lines file, created or
overwritten, which receives the-way's own record of the run (WAY-74): a verdict for each invariant
cited by a check the run's options select — the checks against the base with --base, the checks of
a merge with --merge-onto, the checks of the file alone with neither — a line for each error of
those checks that belongs to no cited invariant, and every failure of the run itself. The report
for a person holds every check. Exit code: 0 without errors, 1 with errors, 2 when the file or the
template cannot be read or the record cannot be written.
"""

import argparse
import importlib.util
import os
import posixpath
import re
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_FILE = os.path.join(HERE, "..", "..", "foundations", "environment_facts.md")

sys.dont_write_bytecode = True


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


decision_guard = _load("decision_format_guard", os.path.join(HERE, "..", "decisions", "format_guard.py"))
map_guard = _load("part_map_format_guard", os.path.join(HERE, "..", "part-map", "format_guard.py"))
invariant_guard = _load("invariants_format_guard",
                        os.path.join(HERE, "..", "invariants", "format_guard.py"))
fingerprint_module = invariant_guard.fingerprint_module
fingerprint = decision_guard.fingerprint
count_sentences = decision_guard.count_sentences
FINGERPRINT = invariant_guard.FINGERPRINT
TODO_WORD = map_guard.TODO_WORD
bare = invariant_guard.bare
is_todo = invariant_guard.is_todo
flat = invariant_guard.flat
listed = invariant_guard.listed
parse_table = invariant_guard.parse_table
stray_lines = invariant_guard.stray_lines
Table = invariant_guard.Table
Unknown = invariant_guard.Unknown
QUOTED = invariant_guard.QUOTED
PROGRAM_NAME = invariant_guard.PROGRAM_NAME
record_paths = invariant_guard.record_paths

# The name a record gives this program, and each of its checks as PROGRAM::<function>.
PROGRAM = "elements/environment-facts/format_guard.py"
# The checks each option selects for the record; every other check reads the file alone and is
# recorded only by a run given neither option (WAY-61, WAY-74).
SELECTED_BY = {"check_against_base": "--base", "check_merge_todo": "--merge-onto",
               "check_fingerprints": "--merge-onto", "check_dependants": "--merge-onto"}
NO_COMMIT = map_guard.NO_COMMIT
NO_COMMIT_REASON = map_guard.NO_COMMIT_REASON
# Where a product's environment facts stand, relative to the root of its repository (WAY-75).
FILE_PATH = "foundations/environment_facts.md"

IDENTIFIER = map_guard.IDENTIFIER
DATE = r"\d{4}-\d{2}-\d{2}"
# A commit as a row of human verdicts names it: an abbreviated or full object name.
COMMIT = r"[0-9a-f]{7,40}"

# The forms of a source (WAY-80), checked for form alone. A cited page gives its address, its
# archived copy where it has no editions, a place and its passage word for word; further passages
# of the same place, and further places of the same page with theirs, follow joined by ` · `; the
# date read closes the page. An observation names the command, the tool and its version, the
# platform and the date it ran. Several pages or observations are joined by ` · `.
_URL = r"https?://(?:[^\s()]|\([^\s()]*\))+"
_PASSAGE = r'(?:"[^"\n]+"|“[^”\n]+”)'
_PLACE = r'[^\s—"“][^—"“]*?'
_AT_PLACE = r"§ %s — %s" % (_PLACE, _PASSAGE)
_CITED = r"%s(?: \(archived: %s, %s\))? %s(?: · (?:%s|%s))*; read %s" % (
    _URL, _URL, DATE, _AT_PLACE, _AT_PLACE, _PASSAGE, DATE)
_OBSERVED = r"observed: `[^`]+` on [^;]+, [^;]+; run %s" % DATE
SOURCE = re.compile(r"(?:%s|%s)(?: · (?:%s|%s))*" % (_CITED, _OBSERVED, _CITED, _OBSERVED))
SOURCE_DATES = re.compile(r"(?:; read |; run |, )(%s)(?=$|\)| ·)" % DATE)


class TemplateError(Exception):
    pass


def holds_todo(value):
    """Whether a value holds `TODO` as a word of its own outside quoted text and outside a command
    in backticks: a passage quoted word for word, or an observed command, may hold the word
    (WAY-71, WAY-80)."""
    text = re.sub(QUOTED, " ", value or "")
    text = re.sub(r"`([^`]*)`", lambda match: match.group(0) if is_todo(match.group(1)) else " ",
                  text)
    return invariant_guard.holds_todo(text)


# --- rules read from the template -----------------------------------------------------------


@dataclass
class Rules:
    fields: list                 # invariant_guard.FieldRule, in the order of the form
    lists: list                  # (title, columns) of the lists closing the file, in order
    verdicts_file: str           # name of the file of human verdicts beside the facts file
    verdicts_columns: list
    scope_words: list            # words no *Holds for* reads

    @property
    def todo_fields(self):
        return [rule.name for rule in self.fields if rule.todo]


_section = invariant_guard._section
_blocks = invariant_guard._blocks
_table_form = invariant_guard._table_form


def read_rules(path=TEMPLATE):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    blocks = _blocks(_section(text, "Entry"))
    if len(blocks) < 2:
        raise TemplateError('the section "Entry" does not hold the entry and its list')
    fields = []
    for name, form in re.findall(r"^- \*\*(.+?):\*\* (.*)$", blocks[0], re.M):
        choices = [bare(choice) for choice in form.split(" | ")]
        fields.append(invariant_guard.FieldRule(
            name, "none" in choices,
            any(choice == "TODO" or choice.startswith("TODO ") for choice in choices)))
    if not fields:
        raise TemplateError("the entry form has no fields")
    lists = [_table_form(block) for block in blocks[1:]]

    runs = _section(text, "When a method runs")
    verdicts_file = re.search(r"`foundations/([^`]+\.md)`", runs)
    header = re.search(r"^\s*\|(.+)\|\s*$", "\n".join(_blocks(runs)), re.M)
    if not verdicts_file or not header:
        raise TemplateError("the section on when a method runs names no file of human verdicts or "
                            "no form of its row")
    columns = [cell.strip() for cell in header.group(1).split("|")]

    checks = " ".join(_section(text, "What the format guard checks").split())
    words = re.search(r"no \*Holds for\* reads (.*?)\(WAY-", checks)
    if not words:
        raise TemplateError("the list of checks names no words *Holds for* may not read")
    return Rules(fields, lists, verdicts_file.group(1), columns,
                 re.findall(r'"([^"]+)"', words.group(1)))


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


def parse_file(text, rules):
    """Entries, the lists closing the file, and headings that are neither, in file order."""
    items, list_titles = [], [title for title, _ in rules.lists]
    for line, lines in map_guard.split_sections(text):
        heading = lines[0][3:].strip()
        # a version is a number from 1, written without a leading zero (WAY-79)
        match = re.match(r"^(.+?)/([1-9][0-9]*)$", heading)
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
        entry.fields = map_guard.parse_fields(body[index:], line + 1 + index)
        entry.strays = stray_lines(body[index:], line + 1 + index)
        items.append(entry)
    return items


def label_of(entry):
    return "%s/%d" % (entry.identifier, entry.version)


def value_of(entry, name):
    return entry.fields.get(name, ["", entry.line])


def entry_fingerprint(entry):
    """The fingerprint of an entry: its sentence and the value of *Holds for* joined by a line
    break, as WAY-39 computes it (WAY-78); None for an entry with no sentence."""
    if entry.sentence is None:
        return None
    return fingerprint(entry.sentence + "\n" + value_of(entry, "Holds for")[0])


def command_of(entry):
    """The command a method names, or None where the method is a path or `TODO`."""
    value = flat(value_of(entry, "Method")[0])
    if is_todo(value) or not (value.startswith("`") and value.endswith("`")):
        return None
    return bare(value)


def method_is_path(entry):
    value = flat(value_of(entry, "Method")[0])
    return bool(value) and not is_todo(value) and command_of(entry) is None and \
        "`" not in value and " " not in value


@dataclass
class Facts:
    """The entries and withdrawn identifiers of a facts file, as other guards read them."""
    entries: dict = field(default_factory=dict)    # identifier -> Entry
    withdrawn: dict = field(default_factory=dict)  # identifier -> line of its row
    holders: list = field(default_factory=list)    # (identifier, line) of every entry and row
    successors: dict = field(default_factory=dict)  # withdrawn identifier -> its *Successors*


def facts_of(text, rules):
    items = parse_file(text or "", rules)
    facts = Facts()
    for item in items:
        if isinstance(item, Entry):
            facts.entries.setdefault(item.identifier, item)
            facts.holders.append((item.identifier, item.line))
        elif isinstance(item, Table) and item.title == rules.lists[0][0]:
            for cells, line in item.rows:
                if cells and cells[0]:
                    facts.withdrawn.setdefault(cells[0], line)
                    facts.successors.setdefault(cells[0], cells[2] if len(cells) > 2 else "")
                    facts.holders.append((cells[0], line))
    return facts


def merged_facts(branch, onto, base):
    """identifier -> the entry a merge of the branch onto the main branch leaves, from the facts
    of each side and of their merge base, as git merges them: the branch's copy where the branch
    changed the entry since the base, the main branch's otherwise; a fact either side withdrew
    that the other did not change is gone."""
    merged = {}
    for identifier in list(branch.entries) + list(onto.entries):
        if identifier in merged:
            continue
        mine, theirs = branch.entries.get(identifier), onto.entries.get(identifier)
        before = base.entries.get(identifier)
        then = entry_fingerprint(before) if before is not None else None
        changed_here = mine is not None and entry_fingerprint(mine) != then
        if identifier in branch.withdrawn or (identifier in onto.withdrawn and not changed_here):
            continue
        if changed_here or theirs is None:
            merged[identifier] = mine
        else:
            merged[identifier] = theirs
    return merged


def merge_base(top, commit):
    """The merge base of HEAD and the commit, or None where git finds none."""
    code, answer, _ = map_guard.call_git(["merge-base", "HEAD", commit], top)
    return answer.strip() if code == 0 and answer.strip() else None


def holds_entries(text):
    """Whether a Markdown text holds an environment fact entry: a section
    `## <identifier>/<version>`, outside a fenced block, carrying a *Holds for* field."""
    heading, fenced = None, False
    for line in text.split("\n"):
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        elif fenced:
            continue
        elif line.startswith("#"):
            heading = re.match(r"^## .+/\d+\s*$", line)
        elif heading and line.startswith("- **Holds for:**"):
            return True
    return False


def verdict_rows(text, columns):
    """(rows, headers) of a file of human verdicts: every table row with its line, and the lines of
    rows that name columns other than the form's."""
    rows, headers, header_seen = [], [], False
    for number, line in enumerate(text.split("\n"), start=1):
        if not line.startswith("|"):
            header_seen = False if not line.strip() else header_seen
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        if not header_seen:
            header_seen = True
            if cells != columns:
                headers.append((number, cells))
            continue
        rows.append((cells, number))
    return rows, headers


# --- the report and the record of a run -----------------------------------------------------


class Report(map_guard.Report):
    """The part map guard's report, naming this program and its checks in the record."""

    def __init__(self, path, options=()):
        super().__init__(path, options, program=PROGRAM, selected_by=SELECTED_BY)


start_record = map_guard.start_record
write_record = map_guard.write_record


# --- what the checks read beside the facts file ---------------------------------------------


@dataclass
class Foundation:
    """What the checks read beside the facts file."""
    root: str = None
    others_read: bool = False      # the invariants and the part map were both read
    holders: list = field(default_factory=list)      # (identifier, where) held outside this file
    invariants: list = field(default_factory=list)   # the entries of the invariants file
    invariants_withdrawn: set = field(default_factory=set)  # withdrawn identifiers of invariants
    log_read: bool = False
    prefix: str = None
    latest: dict = field(default_factory=dict)       # number -> latest version of the decision


def read_foundation(path, report, root):
    foundation = Foundation(root=root)
    directory = os.path.dirname(os.path.abspath(path))
    read = 0

    map_path = os.path.join(directory, "part_map.md")
    if not os.path.exists(map_path):
        report.notes.append("there is no part_map.md beside the file: it holds no identifier")
        read += 1
    else:
        try:
            map_rules = map_guard.read_rules()
            with open(map_path, encoding="utf-8") as handle:
                entries, sections = map_guard.parse_map(handle.read(), map_rules)
            columns = map_rules.lists.get("Withdrawn identifiers")
            foundation.holders += [(entry.identifier, "part_map.md:%d" % entry.line)
                                   for entry in entries]
            foundation.holders += [(cells[0], "part_map.md:%d" % line) for cells, line in
                                   map_guard.rows(sections, "Withdrawn identifiers")
                                   if cells and cells != columns]
            read += 1
        except (OSError, UnicodeDecodeError, map_guard.TemplateError, AttributeError,
                IndexError) as problem:
            report.error(None, "cannot read the part map beside the file: %s" % problem)

    invariants_path = os.path.join(directory, "invariants.md")
    if not os.path.exists(invariants_path):
        report.notes.append("there is no invariants.md beside the file: no invariant rests on a "
                            "fact")
        read += 1
    else:
        try:
            invariant_rules = invariant_guard.read_rules()
            with open(invariants_path, encoding="utf-8") as handle:
                items = invariant_guard.parse_file(handle.read(), invariant_rules)
            for item in items:
                if isinstance(item, invariant_guard.Entry):
                    foundation.invariants.append(item)
                    foundation.holders.append((item.identifier, "invariants.md:%d" % item.line))
                elif isinstance(item, Table) and item.title == invariant_rules.lists[0][0]:
                    foundation.holders += [(cells[0], "invariants.md:%d" % line)
                                           for cells, line in item.rows if cells and cells[0]]
                    foundation.invariants_withdrawn |= {cells[0] for cells, _ in item.rows
                                                        if cells and cells[0]}
            read += 1
        except (OSError, UnicodeDecodeError, invariant_guard.TemplateError,
                AttributeError) as problem:
            report.error(None, "cannot read the invariants beside the file: %s" % problem)
    foundation.others_read = read == 2

    log_path = os.path.join(directory, "decisions.md")
    if not os.path.exists(log_path):
        foundation.log_read = True
        report.notes.append("there is no decisions.md beside the file: no decision rests on a fact")
        return foundation
    log = map_guard.read_file(log_path, report, "the decision log beside the file")
    if log is None:
        return foundation
    foundation.log_read = True
    foundation.prefix = decision_guard.detect_prefix(log)
    if foundation.prefix:
        foundation.latest = invariant_guard.latest_versions(
            decision_guard.parse_log(log, foundation.prefix))
    return foundation


def rests_on_names(invariant_entries):
    """identifier of a fact -> [(invariant, fingerprint)] for every name an invariant's *Rests on*
    carries as `<identifier>@<fingerprint>`."""
    names = {}
    for entry in invariant_entries:
        rests = invariant_guard.value_of(entry, "Rests on")[0]
        for item in listed(rests) if bare(rests) != "none" else []:
            match = re.fullmatch(r"(%s)@([0-9a-f]+)" % IDENTIFIER, item)
            if match:
                names.setdefault(match.group(1), []).append((entry.identifier, match.group(2)))
    return names


# A fact a *Based on* names with its fingerprint, outside a path, an address or a longer word.
# Hex digits in either case are read, so that a fingerprint in capitals is reported, not skipped.
FACT_LINK = re.compile(r"(?<![\w/.@=?&#:%%-])(%s)@([0-9a-fA-F]+)(?![\w@/-])" % IDENTIFIER)


def based_on_links(text):
    """(identifier, fingerprint) for every fact a *Based on* names as `<identifier>@<fingerprint>`
    outside quoted text."""
    return FACT_LINK.findall(re.sub(QUOTED, " ", flat(text or "")))


def bare_mentions(text, identifiers):
    """The identifiers a *Based on* names outside quoted text, as a word of its own and with no
    fingerprint — not inside a path, an address or a longer word."""
    unquoted = re.sub(QUOTED, " ", flat(text or ""))
    return [identifier for identifier in sorted(identifiers)
            if re.search(r"(?<![\w/.@=?&#:%%-])%s(?![\w@/-]|\.\S)" % re.escape(identifier),
                         unquoted)]


def wrong_links(text, identifiers):
    """(identifier, what is written) for every fact a *Based on* names outside quoted text in a
    form the process teaches elsewhere: `<identifier>/<version>`, as a `fact:` line and a heading
    write it, or `<identifier>@` followed by something other than hex digits — the placeholder
    `<fingerprint>` copied from a message included, or nothing."""
    unquoted = re.sub(QUOTED, " ", flat(text or ""))
    found = []
    for identifier in sorted(identifiers):
        for match in re.finditer(r"(?<![\w/.@=?&#:%%-])%s(/[0-9]+|@\S*)" % re.escape(identifier),
                                 unquoted):
            tail = match.group(1)
            if tail.startswith("@") and re.match(r"@[0-9a-fA-F]+(?![\w@/-])", tail):
                continue  # a link, which based_on_links reads
            found.append((identifier, identifier + tail))
    return found


def decision_label(prefix, version):
    return "%s-%02d/%d" % (prefix, version.number, version.version)


def based_on(version):
    return version.fields.get("Based on", ["", version.line])


# --- checks of the file's shape -------------------------------------------------------------


def check_layout(items, rules, report):
    """Entries first, then the list of withdrawn identifiers closing the file; a heading of an
    entry carries its version as a number (WAY-75, WAY-79)."""
    check = "check_layout"
    titles = [title for title, _ in rules.lists]
    fields = re.compile(r"^- \*\*(%s):\*\*" % "|".join(re.escape(rule.name) for rule in rules.fields))
    seen = []
    for item in items:
        if isinstance(item, Unknown):
            if any(fields.match(line) for line in item.body):
                report.error(item.line, "heading `## %s` of an entry carries no version number; "
                                        "it reads `## <identifier>/<version>`" % item.heading, check)
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


def check_file(path, top, tracked, report):
    """The repository holds one file of fact entries, at foundations/environment_facts.md
    (WAY-75). The path is compared, letter case included, as git lists it. Another such file is
    known by its content: a tracked Markdown file holding a section `## <identifier>/<version>`
    with a *Holds for* field. The examples file beside the template this guard reads holds copies
    of entries, as the template sets it, and is no file of entries."""
    # invariant: environment-facts-file/1
    check, one_file = "check_file", "environment-facts-file/1"
    if top is None or tracked is None:
        if os.path.basename(path) != "environment_facts.md" or \
                os.path.basename(os.path.dirname(os.path.abspath(path))) != "foundations":
            report.error(None, "a product's environment facts stand in %s" % FILE_PATH, check,
                         (one_file,))
        return
    report.ran(check, one_file)
    given = os.path.relpath(os.path.abspath(path), top).replace(os.sep, "/")
    listed_as = [name for name in tracked if name.lower() == given.lower()]
    if listed_as:
        given = listed_as[0]
    if given != FILE_PATH:
        report.error(None, "a product's environment facts stand in %s, not in %s"
                     % (FILE_PATH, given), check, (one_file,))
    for name in tracked:
        if name == given or not name.endswith(".md"):
            continue
        full = os.path.join(top, *name.split("/"))
        if os.path.exists(EXAMPLES) and os.path.isfile(full) and os.path.samefile(full, EXAMPLES):
            continue
        try:
            with open(full, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError):
            continue
        if holds_entries(text):
            report.error(None, "`%s` is a second file of environment fact entries; the repository "
                               "holds one, %s" % (name, FILE_PATH), check, (one_file,))


def check_identifiers(entries, withdrawn, foundation, report):
    """Every identifier has the form the template gives and is held once among the entries and
    withdrawn identifiers of this file, of the invariants and of the part map; every withdrawn
    identifier gives why, and names as successors only entries or withdrawn identifiers of this
    file, or `none` (WAY-75)."""
    # invariant: fact-identifier-form/1
    # invariant: identifier-holders/1
    # invariant: fact-withdrawal-successors/1
    check = "check_identifiers"
    form, holders, successors_named = ("fact-identifier-form/1", "identifier-holders/1",
                                       "fact-withdrawal-successors/1")
    report.ran(check, form, successors_named)
    if foundation.others_read:
        report.ran(check, holders)
    outside = {}
    for identifier, where in foundation.holders:
        if identifier in outside:
            report.error(None, "%s: identifier `%s` is held twice outside this file (%s)"
                         % (where, identifier, outside[identifier]), check, (holders,))
        outside.setdefault(identifier, where)
    seen = {}
    for identifier, line, is_entry in [(entry.identifier, entry.line, True) for entry in entries] + \
            [(cells[0] if cells else "", line, False) for cells, line in withdrawn]:
        if identifier == "none" or not re.fullmatch(IDENTIFIER, identifier):
            report.error(line, "`%s` is not an identifier of words in lower case joined by "
                               "hyphens" % identifier, check, (form,) if is_entry else ())
        elif identifier in seen:
            report.error(line, "identifier `%s` is used twice (line %d)" % (identifier, seen[identifier]),
                         check, (holders,))
        elif identifier in outside:
            report.error(line, "identifier `%s` is held by %s" % (identifier, outside[identifier]),
                         check, (holders,))
        seen.setdefault(identifier, line)
    names = set(seen)
    for cells, line in withdrawn:
        identifier = cells[0] if cells else ""
        why = cells[1] if len(cells) > 1 else ""
        successors = cells[2] if len(cells) > 2 else ""
        if not why.strip() or bare(why) == "none" or holds_todo(why):
            report.error(line, "withdrawn `%s` gives no reason in *Why*" % identifier,
                         check, (successors_named,))
        if bare(successors) == "none":
            continue
        for successor in listed(successors) or [""]:
            if successor not in names:
                report.error(line, "withdrawn `%s` names successor `%s`, which is neither an entry "
                                   "nor a withdrawn identifier of this file" % (identifier, successor),
                             check, (successors_named,))


def check_fields(entries, rules, report):
    """Every field of the form is present, and holds `none` or `TODO` only where the form gives
    it that word; no entry carries a field the form does not hold (WAY-71)."""
    # invariant: fact-entry-field-presence/1
    # invariant: fact-entry-field-words/1
    check = "check_fields"
    presence, words = "fact-entry-field-presence/1", "fact-entry-field-words/1"
    report.ran(check, presence, words)
    names = [rule.name for rule in rules.fields]
    for entry in entries:
        label = label_of(entry)
        for name, (value, line) in entry.fields.items():
            if name not in names:
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
            if holds_todo(value) and not rule.todo:
                report.error(line, "%s: *%s* may not hold `TODO`" % (label, rule.name),
                             check, (words,))


def check_sentence(entries, report):
    """Every entry states its fact in one sentence, with no text outside the sentence and its
    fields (WAY-76)."""
    # invariant: fact-sentence-count/1
    check, count = "check_sentence", "fact-sentence-count/1"
    report.ran(check, count)
    for entry in entries:
        label = label_of(entry)
        if entry.sentence is None:
            report.error(entry.line, "%s: the sentence is missing" % label, check, (count,))
            continue
        sentences = count_sentences(entry.sentence)
        if sentences != 1:
            report.error(entry.line + 2, "%s: %d sentences, an entry states one" % (label, sentences),
                         check, (count,))
        for offset in entry.strays:
            report.error(offset, "%s: text outside the sentence and the fields; an entry states one "
                                 "sentence" % label, check, (count,))


def check_scope(entries, rules, report):
    """No *Holds for* reads a word whose meaning moves with the date (WAY-77)."""
    # invariant: fact-scope-word/1
    check, scope = "check_scope", "fact-scope-word/1"
    report.ran(check, scope)
    for entry in entries:
        value, line = value_of(entry, "Holds for")
        for word in rules.scope_words:
            if re.search(r"\b%s\b" % re.escape(word), value, re.I):
                report.error(line, '%s: *Holds for* reads "%s", which names another release as the '
                                   "date moves" % (label_of(entry), word), check, (scope,))


def check_source(entries, report):
    """Every *Source* has one of the forms the template gives; the form alone is checked
    (WAY-80)."""
    # invariant: fact-source-form/1
    check, form = "check_source", "fact-source-form/1"
    report.ran(check, form)
    for entry in entries:
        raw, line = value_of(entry, "Source")
        value = flat(raw)
        if not value or bare(value) == "none" or is_todo(value):
            continue  # check_fields reports a missing source and the words it may not hold
        label = label_of(entry)
        if not SOURCE.fullmatch(value):
            report.error(line, '%s: *Source* is neither `<address> § <place> — "<passage>"; read '
                               "<YYYY-MM-DD>`, with an archived copy where the page has no editions, "
                               "nor `observed: `<command>` on <tool and version, platform>; run "
                               "<YYYY-MM-DD>`, each joined by ` · `" % label, check, (form,))
            continue
        for date in SOURCE_DATES.findall(value):
            if not decision_guard.valid_date(date):
                report.error(line, "%s: *Source* gives `%s`, which is not a date YYYY-MM-DD"
                             % (label, date), check, (form,))


def check_method(entries, tracked, report):
    """Every method is a command that begins with a program's name, the path alone of a file that
    exists — one git tracks, letter case included — or `TODO` (WAY-81)."""
    # invariant: fact-method-form/1
    check, form = "check_method", "fact-method-form/1"
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
            continue
        if "`" in value or " " in value:
            report.error(line, "%s: *Method* is neither a command in backticks, the path of a file, "
                               "nor `TODO`" % label, check, (form,))
        elif tracked is None:
            decided = False
        elif posixpath.normpath(value.replace("\\", "/")) not in tracked:
            # as git lists the file, letter case included, so that the verdict is one on every
            # machine; a file git does not track is none the gate can read on another machine
            report.error(line, "%s: *Method* names `%s`, which is not a file git tracks, letter "
                               "case included" % (label, value), check, (form,))
    if decided:
        report.ran(check, form)


def check_corrections(entries, report):
    """A declared correction names two fingerprints, the second the entry's current one
    (WAY-79)."""
    check = "check_corrections"
    for entry in entries:
        label = label_of(entry)
        correction, line = value_of(entry, "Correction")
        declared = re.fullmatch(r"([0-9a-f]+) → ([0-9a-f]+)", flat(correction))
        now = entry_fingerprint(entry)
        if correction.strip() and bare(correction) != "none" and not declared:
            report.error(line, "%s: *Correction* is neither `none` nor `<fingerprint> → "
                               "<fingerprint>`" % label, check)
        elif declared and now is not None and declared.group(2) != now:
            report.error(line, "%s: *Correction* names %s as the current fingerprint, but it is %s"
                         % (label, declared.group(2), now), check)


def check_human_verdicts(path, facts, foundation, rules, report):
    """Every row of the file of human verdicts names an entry of the invariants or of the
    environment facts; a row naming a fact names an entry whose method is a path, gives `pass` or
    `fail`, names who gave it, when and the commit assessed, and carries a date in *Until*
    (WAY-83). The rows naming an invariant are the invariants guard's to check further."""
    # invariant: human-verdict-fact-row/1
    check, fact_row = "check_human_verdicts", "human-verdict-fact-row/1"
    verdicts_path = os.path.join(os.path.dirname(os.path.abspath(path)), rules.verdicts_file)
    if not os.path.exists(verdicts_path):
        report.notes.append("there is no %s; no human verdict is given" % rules.verdicts_file)
        report.ran(check, fact_row)
        return
    text = map_guard.read_file(verdicts_path, report, "the human verdicts")
    if text is None:
        return
    report.ran(check, fact_row)
    rows, headers = verdict_rows(text, rules.verdicts_columns)
    for number, cells in headers:
        report.error(None, "%s:%d: the list has columns %s, not %s"
                     % (rules.verdicts_file, number, " | ".join(cells),
                        " | ".join(rules.verdicts_columns)), check)
    for cells, number in rows:
        where = "%s:%d" % (rules.verdicts_file, number)
        values = dict(zip(rules.verdicts_columns, cells + [""] * len(rules.verdicts_columns)))
        name = values.get("Entry", "")
        if name in facts.entries:
            entry = facts.entries[name]
            problems = []
            if not method_is_path(entry):
                problems.append("the method of `%s` is not a path" % name)
            if not re.fullmatch(r"[1-9][0-9]*", values.get("Version", "")):
                problems.append("*Version* is not a number")
            if values.get("Verdict") not in ("pass", "fail"):
                problems.append("*Verdict* is neither `pass` nor `fail`")
            by = values.get("By", "")
            if not by or bare(by) == "none" or holds_todo(by):
                problems.append("*By* names nobody")
            for column in ("On", "Until"):
                value = values.get(column, "")
                if not re.fullmatch(DATE, value) or not decision_guard.valid_date(value):
                    problems.append("*%s* is not a date YYYY-MM-DD" % column)
            if not re.fullmatch(COMMIT, values.get("Commit", "")):
                problems.append("*Commit* names no commit")
            for problem in problems:
                report.error(None, "%s: %s" % (where, problem), check, (fact_row,))
        elif name not in {entry.identifier for entry in foundation.invariants}:
            report.error(None, "%s: `%s` is neither an invariant nor an environment fact"
                         % (where, name), check)


def check_based_on(facts, foundation, report):
    """Every fact the *Based on* of the latest version of a decision names carries a fingerprint
    (WAY-90). A fact is named as `<identifier>@<fingerprint>`; an identifier of the file standing
    as a word of its own, outside quoted text, a path or an address, is a fact named without one.
    Whether the fingerprint is the current one is checked against a merge, in
    check_fingerprints."""
    # invariant: based-on-fact-fingerprint/1
    check, presence = "check_based_on", "based-on-fact-fingerprint/1"
    if not foundation.log_read:
        return
    report.ran(check, presence)
    # `none` is no identifier, and check_identifiers reports an entry holding it
    known = (set(facts.entries) | set(facts.withdrawn)) - {"none"}
    for number, version in sorted(foundation.latest.items()):
        value, line = based_on(version)
        where = "decisions.md:%d: %s" % (line, decision_label(foundation.prefix, version))
        for identifier, digest in based_on_links(value):
            if identifier not in known:
                report.error(None, "%s: *Based on* names `%s@%s`, which is no environment fact"
                             % (where, identifier, digest), check)
            elif not re.fullmatch(FINGERPRINT, digest):
                report.error(None, "%s: `%s@%s` carries no fingerprint of %d hex digits"
                             % (where, identifier, digest, fingerprint_module.LENGTH),
                             check, (presence,))
        for identifier in bare_mentions(value, known):
            report.error(None, "%s: *Based on* names the fact `%s` with no fingerprint; it reads "
                               "`%s@<fingerprint>`" % (where, identifier, identifier),
                         check, (presence,))
        for identifier, written in wrong_links(value, known):
            report.error(None, "%s: *Based on* names the fact `%s` as `%s`; it reads "
                               "`%s@<fingerprint>`" % (where, identifier, written, identifier),
                         check, (presence,))


# --- checks against the repository ----------------------------------------------------------


CITATION = re.compile(r"^\s*(?:#|//|--|;|%|\*|/\*|<!--|REM\b)\s*fact:\s*(.*?)\s*"
                      r"(?:\*/|-->)?\s*$")


def citation_value(value):
    """What a `fact:` comment cites, or None where it is prose: one word, or words whose first
    holds a `/`, as `storage-quota/1 (the MDN page)` — a citation off the form, not silence, as
    the test runner reads it."""
    words = value.split()
    if len(words) == 1 or (words and "/" in words[0]):
        return value
    return None


def check_citations(facts, top, tracked, report):
    """Every `fact:` line in a check names an entry at its current version, never a withdrawn
    identifier (WAY-79, WAY-81). A Markdown file holds no check; a file is read as holding checks
    once one of its `fact:` lines names something of an identifier's form."""
    # invariant: fact-citation-target/1
    # invariant: fact-citation-version/1
    check = "check_citations"
    target, version = "fact-citation-target/1", "fact-citation-version/1"
    report.ran(check, target, version)
    for name in tracked:
        if name.endswith(".md"):
            continue
        try:
            with open(os.path.join(top, name), encoding="utf-8") as handle:
                lines = handle.read().split("\n")
        except (OSError, UnicodeDecodeError):
            continue
        found = [(number, citation_value(match.group(1))) for number, match in
                 ((number, CITATION.match(line)) for number, line in enumerate(lines, start=1))
                 if match]
        found = [(number, value) for number, value in found if value is not None]
        if not any(re.match(r"%s(?:/\S*)?(?:\s|$)" % IDENTIFIER, value) for _, value in found):
            continue
        for number, value in found:
            where = "%s:%d" % (name, number)
            # a version is a number written without a leading zero
            cited = re.fullmatch(r"(\S+)/([1-9][0-9]*)", value)
            identifier = cited.group(1) if cited else value.split()[0].split("/")[0]
            if identifier in facts.withdrawn:
                report.error(None, "%s: cites `%s`, which is withdrawn" % (where, identifier),
                             check, (target,))
            elif identifier not in facts.entries:
                report.error(None, "%s: cites `%s`, which is not an environment fact"
                             % (where, identifier), check, (target,))
            elif not cited:
                report.error(None, "%s: `fact: %s` does not cite `<identifier>/<version>`"
                             % (where, value), check, (version,))
            elif int(cited.group(2)) != facts.entries[identifier].version:
                report.error(None, "%s: cites `%s`, whose current version is %d"
                             % (where, value, facts.entries[identifier].version), check, (version,))


def check_record_paths(entries, top, report):
    """Every `.jsonl` path a command names is one git ignores, as git itself answers, and no
    command names two (WAY-74). Letter case always counts: git ignores it where core.ignorecase
    is set, which git init sets on Windows and macOS."""
    check = "check_record_paths"
    named = {}   # path -> (entry, line) of the first command naming it
    for entry in entries:
        command = command_of(entry)
        if command is None:
            continue
        line = value_of(entry, "Method")[1]
        paths = record_paths(command)
        if len(paths) > 1:
            report.error(line, "%s: the command names %d records of a run (%s); it names one"
                         % (label_of(entry), len(paths), ", ".join("`%s`" % p for p in paths)),
                         check)
        for path in paths:
            named.setdefault(path, (entry, line))
    inside = []
    for path, (entry, line) in named.items():
        normal = os.path.normpath(path).replace(os.sep, "/")
        if os.path.isabs(path) or normal == ".." or normal.startswith("../"):
            report.error(line, "%s: `%s` lies outside the repository, where git ignores nothing"
                         % (label_of(entry), path), check)
        else:
            inside.append(path)
    if not inside:
        return
    code, answer, message = map_guard.call_git(["-c", "core.ignorecase=false", "check-ignore",
                                                "-z", "--stdin"], top,
                                               stdin="\0".join(inside) + "\0")
    if code not in (0, 1):
        # a failure of the run, not of a check (WAY-63)
        report.error(None, "git cannot tell which paths it ignores: %s"
                     % (message or "git check-ignore exited with %d" % code))
        return
    ignored = {path for path in answer.split("\0") if path}
    for path in inside:
        if path not in ignored:
            entry, line = named[path]
            report.error(line, "%s: git does not ignore `%s`, the record of a run the command names"
                         % (label_of(entry), path), check)


# --- the commit the branch left the main branch from ---------------------------------------


BASE_INVARIANTS = ("fact-version-new/1", "fact-version-changed/1", "fact-version-unchanged/1",
                   "fact-identifier-persistence/1", "fact-withdrawal-persistence/1")


def check_against_base(path, facts, rules, base, top, report, no_commit=None):
    """Compares identifiers and versions with the file on the base (WAY-75, WAY-79). Given
    `no_commit`, which says why there is no base, records the checks unchecked instead."""
    # invariant: fact-version-new/1
    # invariant: fact-version-changed/1
    # invariant: fact-version-unchanged/1
    # invariant: fact-identifier-persistence/1
    # invariant: fact-withdrawal-persistence/1
    check = "check_against_base"
    new, changed, unchanged, persistence, withdrawal = BASE_INVARIANTS
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, *BASE_INVARIANTS)
        return
    relative = os.path.relpath(os.path.abspath(path), top).replace(os.sep, "/")
    base_text, failure = map_guard.file_at(base, relative, top)
    if failure:
        report.error(None, failure)
        return
    if base_text is None:
        report.notes.append("%s has no %s; every entry is new" % (base, relative))
    report.ran(check, *BASE_INVARIANTS)
    before_facts = facts_of(base_text, rules)

    for identifier in sorted(set(before_facts.entries) | set(before_facts.withdrawn)):
        if identifier not in facts.entries and identifier not in facts.withdrawn:
            report.error(None, "`%s` stands in the file on %s and is gone; it stays as an entry or "
                               "a withdrawn identifier" % (identifier, base), check,
                         (persistence, withdrawal) if identifier in before_facts.withdrawn
                         else (persistence,))
    for identifier in sorted(set(before_facts.withdrawn) & set(facts.entries)):
        report.error(facts.entries[identifier].line, "`%s` is withdrawn on %s and stands as an "
                                                     "entry again" % (identifier, base),
                     check, (withdrawal,))

    for identifier, entry in facts.entries.items():
        label = label_of(entry)
        correction = flat(value_of(entry, "Correction")[0])
        now = entry_fingerprint(entry)
        if now is None:
            continue
        before = before_facts.entries.get(identifier)
        then = entry_fingerprint(before) if before is not None else None
        if then is None:
            if entry.version != 1:
                report.error(entry.line, "%s: a new entry carries version 1" % label, check, (new,))
            if bare(correction) != "none":
                report.error(entry.line, "%s: a new entry declares no correction" % label,
                             check, (new,))
            continue
        declared = re.fullmatch(r"([0-9a-f]+) → ([0-9a-f]+)", correction)
        if now == then:
            if entry.version != before.version:
                report.error(entry.line, "%s: the sentence and *Holds for* are unchanged since %s, "
                                         "where the version is %d" % (label, base, before.version),
                             check, (unchanged,))
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
            report.error(entry.line, "%s: the sentence or *Holds for* changed since %s (%s → %s); "
                                     "the version is %d, or a correction names `%s → %s`"
                         % (label, base, then, now, before.version + 1, then, now),
                         check, (changed,))


# --- the commit a merge onto the main branch is made onto ----------------------------------


def check_merge_todo(entries, rules, report, no_commit=None):
    """Reports every field of every entry, other than those the form gives `TODO`, that holds
    `TODO` (WAY-71). Given `no_commit`, records it unchecked instead."""
    # invariant: fact-entry-merge-todo/1
    check, merge_todo = "check_merge_todo", "fact-entry-merge-todo/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, merge_todo)
        return
    report.ran(check, merge_todo)
    for entry in entries:
        for name, (value, line) in entry.fields.items():
            if name not in rules.todo_fields and holds_todo(value):
                report.error(line, "%s: *%s* holds `TODO`, which a merge onto the main branch does "
                                   "not take" % (label_of(entry), name), check, (merge_todo,))


@dataclass
class Merged:
    """The foundation a merge onto the main branch leaves."""
    facts: dict = field(default_factory=dict)       # identifier -> fingerprint of each entry
    prefix: str = None
    latest: dict = field(default_factory=dict)      # number -> latest version of the decision
    invariants: list = field(default_factory=list)  # the entries of the invariants file
    withdrawn: dict = field(default_factory=dict)   # fact either side withdrew -> successors


def merged_foundation(path, facts, foundation, rules, merge_onto, top, report):
    """What a merge onto the commit leaves, or None once the report says why git could not read
    it. Each fact is the branch's copy where the branch changed it since the merge base, and the
    main branch's otherwise (merged_facts); the invariants are the branch's, and those only the
    commit merged onto holds that the branch has not withdrawn; the decision log is append-only,
    so the merge holds every version either side holds, the branch's copy where both do
    (WAY-07)."""
    directory = os.path.dirname(os.path.abspath(path))

    def on_commit(commit, name):
        relative = os.path.relpath(os.path.join(directory, name), top).replace(os.sep, "/")
        text, failure = map_guard.file_at(commit, relative, top)
        if failure:
            report.error(None, failure)
            raise LookupError
        return text

    base = merge_base(top, merge_onto)
    try:
        onto_facts = facts_of(on_commit(merge_onto, os.path.basename(path)), rules)
        base_facts = facts_of(on_commit(base, os.path.basename(path)) if base else None, rules)
        onto_invariants = on_commit(merge_onto, "invariants.md")
        onto_log = on_commit(merge_onto, "decisions.md")
    except LookupError:
        return None
    if base is None:
        report.notes.append("HEAD and %s have no merge base; every fact the branch holds is read "
                            "as the branch's copy" % merge_onto)
    merged = Merged()
    merged.facts = {identifier: entry_fingerprint(entry) for identifier, entry
                    in merged_facts(facts, onto_facts, base_facts).items()}
    merged.withdrawn = dict(onto_facts.successors)
    merged.withdrawn.update(facts.successors)

    merged.invariants = list(foundation.invariants)
    if onto_invariants:
        own = {entry.identifier for entry in foundation.invariants} | \
            foundation.invariants_withdrawn
        merged.invariants += [item for item in invariant_guard.parse_file(
            onto_invariants, invariant_guard.read_rules())
            if isinstance(item, invariant_guard.Entry) and item.identifier not in own]

    merged.prefix = foundation.prefix or decision_guard.detect_prefix(onto_log or "")
    versions = {}
    if merged.prefix:
        texts = [onto_log or ""]
        log_path = os.path.join(directory, "decisions.md")
        if foundation.prefix and os.path.exists(log_path):
            log_text = map_guard.read_file(log_path, report, "the decision log beside the file")
            if log_text is None:
                return None
            texts.insert(0, log_text)
        for text in texts:
            for entry in decision_guard.parse_log(text, merged.prefix):
                if entry.kind == "version":
                    versions.setdefault((entry.number, entry.version), entry)
    merged.latest = invariant_guard.latest_versions(versions.values())
    return merged


def check_fingerprints(merged, report, no_commit=None):
    """Compares every fingerprint the *Based on* of the latest version of a decision carries for a
    fact with that fact's current fingerprint after the merge (WAY-90). Given `no_commit`, records
    it unchecked instead."""
    # invariant: based-on-fact-fingerprint-value/1
    check, value = "check_fingerprints", "based-on-fact-fingerprint-value/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, value)
        return
    report.ran(check, value)
    for number, version in sorted(merged.latest.items()):
        text, line = based_on(version)
        where = "decisions.md:%d: %s" % (line, decision_label(merged.prefix, version))
        for identifier, digest in based_on_links(text):
            current = merged.facts.get(identifier)
            if current is None and identifier in merged.withdrawn:
                successors = merged.withdrawn[identifier]
                follow = "the decision goes to review" if not successors or \
                    bare(successors) == "none" else \
                    "the decision is renewed on its successors, %s" % successors
                report.error(None, "%s: `%s@%s` names a withdrawn environment fact, which has no "
                                   "current fingerprint; %s" % (where, identifier, digest, follow),
                             check, (value,))
            elif current is None:
                report.error(None, "%s: `%s@%s` names no environment fact the merge holds"
                             % (where, identifier, digest), check, (value,))
            elif digest != current:
                report.error(None, "%s: `%s@%s` — the current fingerprint of `%s` after the merge is "
                                   "%s" % (where, identifier, digest, identifier, current),
                             check, (value,))


def check_dependants(entries, invariants, latest, report, merge, no_commit=None):
    """Every entry is named by an invariant's *Rests on* or by the *Based on* of the latest version
    of a decision; one that is not is a warning, and, checking a merge, an error (WAY-88). Given
    `no_commit`, records the merge's check unchecked instead."""
    # invariant: fact-dependants/1
    check, dependants = "check_dependants", "fact-dependants/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, dependants)
        return
    named = set(rests_on_names(invariants))
    for version in latest.values():
        named |= {identifier for identifier, _ in based_on_links(based_on(version)[0])}
    if merge:
        report.ran(check, dependants)
    for entry in entries:
        if entry.identifier in named:
            continue
        message = "%s: no invariant's *Rests on* and no decision's *Based on* names it" \
            % label_of(entry)
        if merge:
            report.error(entry.line, message + "; a fact nothing rests on is withdrawn",
                         check, (dependants,))
        else:
            report.warning(entry.line, message + "; a merge onto the main branch fails on it")


# --- the examples ---------------------------------------------------------------------------


def check_examples(items, examples_path, report):
    check = "check_examples"
    examples = map_guard.read_file(examples_path, report, "the examples")
    if examples is None:
        return
    by_heading = {item.text.split("\n")[0]: item for item in items if isinstance(item, Entry)}
    for line, lines in map_guard.split_sections(examples):
        copy = "\n".join(lines).rstrip()
        entry = by_heading.get(lines[0])
        if entry is None:
            report.error(None, "examples.md:%d: `%s` is not in the file" % (line, lines[0]), check)
        elif entry.text != copy:
            report.error(entry.line, "examples.md:%d differs from the file" % line, check)


# --- entry point ----------------------------------------------------------------------------


def find_commit(path, top, option, commit, report):
    if top is None:
        report.error(None, "%s %s given, but the file is not in a git repository" % (option, commit))
        return False
    return map_guard.find_commit(top, option, commit, report)


def run(path, base=None, stream=None, template=TEMPLATE, merge_onto=None, record=None,
        examples=EXAMPLES):
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
        rules = read_rules(template)
    except (OSError, UnicodeDecodeError, TemplateError, invariant_guard.TemplateError,
            AttributeError) as problem:
        return stop("cannot read the rules from %s: %s" % (template, problem))
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError) as problem:
        return stop("cannot read the environment facts file: %s" % problem)

    top = invariant_guard.repository_root(path, report)
    tracked = invariant_guard.tracked_files(top, report) if top is not None else None
    foundation = read_foundation(path, report, top)
    items = parse_file(text, rules)
    entry_list = [item for item in items if isinstance(item, Entry)]
    facts = facts_of(text, rules)
    withdrawn_table = next((item for item in items if isinstance(item, Table)
                            and item.title == rules.lists[0][0]), None)
    withdrawn = withdrawn_table.rows if withdrawn_table else []

    check_layout(items, rules, report)
    check_file(path, top, tracked, report)
    check_identifiers(entry_list, withdrawn, foundation, report)
    check_fields(entry_list, rules, report)
    check_sentence(entry_list, report)
    check_scope(entry_list, rules, report)
    check_source(entry_list, report)
    check_method(entry_list, tracked, report)
    check_corrections(entry_list, report)
    check_human_verdicts(path, facts, foundation, rules, report)
    check_based_on(facts, foundation, report)
    if tracked is not None:
        check_citations(facts, top, tracked, report)
        check_record_paths(entry_list, top, report)

    if base == NO_COMMIT:
        no_base = "--base none: there is no commit the branch left the main branch from"
        check_against_base(path, facts, rules, None, None, report, no_commit=no_base)
        report.notes.append(no_base + "; identifiers and versions are not compared with it, and "
                                      "those checks are unchecked")
    elif base:
        if find_commit(path, top, "--base", base, report):
            check_against_base(path, facts, rules, base, top, report)
    else:
        report.notes.append("no --base given: identifiers and versions are not compared with the "
                            "main branch")

    if merge_onto == NO_COMMIT:
        no_onto = "--merge-onto none: there is no commit to merge onto"
        check_merge_todo(entry_list, rules, report, no_commit=no_onto)
        check_fingerprints(None, report, no_commit=no_onto)
        check_dependants(entry_list, foundation.invariants, foundation.latest, report, False)
        check_dependants(entry_list, [], {}, report, True, no_commit=no_onto)
        report.notes.append(no_onto + "; `TODO` in the entries, the fingerprints decisions carry "
                                      "for facts and the facts nothing names are not checked "
                                      "against a merge, and those checks are unchecked")
    elif merge_onto:
        if find_commit(path, top, "--merge-onto", merge_onto, report):
            check_merge_todo(entry_list, rules, report)
            merged = merged_foundation(path, facts, foundation, rules, merge_onto, top, report)
            if merged is not None:
                check_fingerprints(merged, report)
                check_dependants(entry_list, merged.invariants, merged.latest, report, True)
    else:
        check_dependants(entry_list, foundation.invariants, foundation.latest, report, False)
        report.notes.append("no --merge-onto given: `TODO` in the entries is not checked against a "
                            "merge, the fingerprints decisions carry for facts are not compared "
                            "with the current binding part, and a fact nothing names is only a warning")

    if os.path.exists(examples) and os.path.exists(OWN_FILE) and os.path.samefile(path, OWN_FILE):
        check_examples(items, examples, report)
    report.print(stream)
    if record is not None:
        write_record(record, report)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a product's environment facts against "
                                                 "the template.")
    parser.add_argument("file", nargs="?", default=os.path.join("foundations", "environment_facts.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from, to "
                                       "compare identifiers and versions with; `none` where it "
                                       "does not exist, which records those checks as unchecked")
    parser.add_argument("--merge-onto", help="the commit of the main branch a merge is made onto; "
                                             "only with it is `TODO` outside *Method* reported, "
                                             "every fingerprint a decision's *Based on* carries for "
                                             "a fact compared with the fact after the merge, and a "
                                             "fact nothing names an error; `none` where the main "
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
