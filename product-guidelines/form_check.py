"""Form check of a product's guidelines (WAY-170).

Checks every file `guidelines/<name>.md` of a repository against the template every product's
guidelines share, `product-guidelines/template.md`, and, where the-way gives one, the template of
the file's discipline, `product-guidelines/<discipline>/template.md`. Both are read from the
checkout of the-way this script lies in: in a product, its pinned `.the-way`; in the-way itself, the
repository checked (WAY-170). The form is read from the fenced block of each template's section
`## Required form`, so the rules of form live in the templates alone (WAY-171).

Usage, from the root of the repository:

    python -B <the-way>/product-guidelines/form_check.py [ROOT] [--merge-onto REF|none]
        [--record PATH]

ROOT defaults to the working directory and must be what `git rev-parse --show-toplevel` prints
there. --merge-onto names the commit of the main branch a merge goes onto, `none` where there is
none (WAY-61); it selects the checks of references for the record, so a run given it records no
check of form. --record names a JSON Lines file, its path ending in `.jsonl`, created or
overwritten, which receives the-way's own record of the run (WAY-74): a verdict for each invariant
cited by a check the run's options select — the checks of form with no option, the checks of
references with --merge-onto — and every failure of the run itself. Every check runs and prints in
every run, so a run given no option that meets a reference error prints it and exits 1, its record
holding the checks of form alone. The check of references after a merge runs only with a commit
given to --merge-onto: given `none`, it is recorded `unchecked` with the reason the guards share;
given no option, a note says it does not run.

The run prints one report for itself — the guidelines it lists, the part map, decision log and
invariants file it reads, the commit it merges onto — under the path `guidelines`, and one for each
file of guidelines under that file's path; each report ends with its count line. A run finding no
`guidelines/` says so in a note and records `pass`.

What it reports, each finding an error of `guidelines-form` (spec §5.3, items 1–6 and 5a): a header
line, section, required rule or rule field missing or out of order; a rule naming no decision, and
in a discipline whose template requires it, no invariant; in a table of roles, a *Kind* outside its
list, a background role whose *Text on it* names no text role of the table, a row naming no
decision, and a decision of the table that the rule of each role's meaning does not name unless that
rule is dropped; a dropped section or rule holding anything but `none — <PREFIX-NN>@<fingerprint>`;
a part named in *Applies to* or in the file's name that the map does not hold; a file whose name and
*Discipline* disagree; a path of `## Where in code` that is absolute, holds a `..` segment, a drive,
a UNC prefix, a backslash or a `:`, or names nothing git tracks. A decision is named by a number
with the prefix of the product's log, an invariant by an identifier its invariants file holds as an
entry or a withdrawn identifier. A path git lists under `guidelines/` that is not
`guidelines/<name>.md`, one level deep with a lower-case `.md`, gets a warning and is not read.

What it reports as an error of `guidelines-reference-current` (spec §5.3, item 7): a reference
anywhere outside fenced code — a decision number of the log or an identifier of the invariants file
followed by `@` and a run of letters and digits, or any identifier followed by `@` and eight
lower-case hexadecimal characters (spec §3.2) — whose part after `@` is no fingerprint, that names a
decision the log does not hold or holds with no binding sentences, or an invariant the file does not
hold or has withdrawn, or whose fingerprint is not the entry's current one on the commit checked
and, given a commit to merge onto, after the merge: the decisions as the decisions guard merges the
log, an invariant as on the branch where its sentence differs from the fork point and as on that
commit otherwise. Every fingerprint is computed by `relation-model/fingerprint.py`; a message names
the reference, the entry and its current fingerprint, and never offers to renew one (WAY-31). The
parsers of the decisions and invariants guards are borrowed with reports of this script's own,
discarded after the call: only a failure of git carries over, never a finding of the log's own
rules.

The files it reads are the product's, so it trusts none of them (WAY-48): it reads a file only
through components that are no link or other reparse point, only a regular file of at most 1048576
bytes, only UTF-8 text, and nothing through a link; a path named in a file is never opened and
never given to git, which is asked once for every path it tracks; it calls no program but git,
opens no socket, writes nothing but the record, and prints every value taken from a file escaped
and cut to 200 characters. It reads the decision log and the invariants file of the working tree
as it reads guidelines, and their copies on other commits from git by their fixed paths. Its
regular expressions are anchored or bounded by a look-behind, with no nested repetition, so a long
line cannot make matching run away.

Exit code: 0 without errors, 1 with errors, 2 when it cannot run — ROOT is not the top of a git
repository, a template of the-way or the code it borrows cannot be read, or the record path does not
end in `.jsonl` or cannot be written.
"""

import argparse
import importlib.util
import json
import os
import re
import stat
import sys
import types
from dataclasses import dataclass, field

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
THE_WAY = os.path.dirname(HERE)
TEMPLATE = os.path.join(HERE, "template.md")

# The name a record gives this program, and each of its checks as PROGRAM::<function>.
PROGRAM = "product-guidelines/form_check.py"
# The invariants the checks give a verdict for, at the versions this script checks.
FORM = "guidelines-form/1"
REFERENCES = "guidelines-reference-current/1"
# The checks of references, on the commit checked and after the merge.
SAME_COMMIT, AFTER_MERGE = "check_references", "check_merged_references"
# The checks each option selects for the record; every other check is recorded only by a run given
# no option (WAY-74). The checks of form are selected by none.
SELECTED_BY = {SAME_COMMIT: "--merge-onto", AFTER_MERGE: "--merge-onto"}

GUIDELINES = "guidelines"
PART_MAP = "foundations/part_map.md"
DECISION_LOG = "foundations/decisions.md"
INVARIANTS = "foundations/invariants.md"
# Why `read_untrusted` reads no file where none stands at the path.
ABSENT = "does not exist"
# What the parsers borrowed from the guards may raise on a file a product wrote.
PARSE_ERRORS = (ValueError, IndexError, KeyError, AttributeError, TypeError)
MAX_BYTES = 1048576
MAX_SHOWN = 200

# The structural words of the form the checks below act on, each read back from the templates.
FORM_SECTION = "Required form"
RULES = "Rules"
WHERE = "Where in code"
DISCIPLINE = "Discipline"
APPLIES_TO = "Applies to"
DECISION = "Decision"
INVARIANT = "Invariant"
ROLE, KIND, TEXT_ON_IT = "Role", "Kind", "Text on it"
BACKGROUND, TEXT = "background", "text"
ROLE_MEANING_RULE = "Each role in its meaning"

FIELD_LINE = re.compile(r"^- \*\*(.+?):\*\*(?: (.*))?$")
OPEN_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
CODE_SPAN = re.compile(r"`([^`\n]*)`")
# A word of letters, digits and hyphens followed by `@` and a run of letters and digits: what may
# be a reference, the word read afterwards as a decision number or an identifier. The look-behind
# keeps a match from starting inside a longer word, so from each place a scan starts at most once
# and stays linear on a long line; neither repetition is nested.
REFERENCE_TOKEN = re.compile(r"(?<![A-Za-z0-9-])([A-Za-z0-9][A-Za-z0-9-]*)@([A-Za-z0-9]+)")
# A decision number, its digits bounded so that no crafted run of digits reaches int().
DECISION_NUMBER = re.compile(r"([A-Z][A-Z0-9]*)-([0-9]{1,9})")
IDENTIFIER = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FINGERPRINT = re.compile(r"[0-9a-f]{8}")
DROPPED = re.compile(r"^none(?:\s*$|\s*[—–-])")
DROP_LINE = re.compile(r"^none — ([A-Z][A-Z0-9]*-[0-9]+)@[0-9a-f]{8}$")
SEPARATOR_CELL = re.compile(r"^:?-+:?$")


class TemplateError(Exception):
    """A template of the-way does not hold a form this script reads."""


# --- code borrowed from the format guards, loaded by its path ---------------------------------


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def borrow():
    """(the code the format guards share, the part-map, decisions and invariants guards and the
    relation model's fingerprint, by name), or (None, the reason they cannot load)."""
    paths = {"shared": ("elements", "common", "guard_shared.py"),
             "part_map": ("elements", "part-map", "format_guard.py"),
             "decisions": ("elements", "decisions", "format_guard.py"),
             "invariants": ("elements", "invariants", "format_guard.py"),
             "fingerprint": ("relation-model", "fingerprint.py")}
    loaded = {}
    try:
        for name, path in paths.items():
            loaded[name] = _load("product_guidelines_borrowed_%s" % name,
                                 os.path.join(THE_WAY, *path))
    except (OSError, ImportError, SyntaxError, AttributeError) as problem:
        return None, "cannot load the code the form check borrows: %s" % problem
    return types.SimpleNamespace(**loaded), None


# --- values taken from a product's files ----------------------------------------------------


def shown(value):
    """A value from a product's file as a person may read it: cut, then escaped."""
    value = str(value)
    text = "".join(character if character.isprintable() else "\\x%02x" % ord(character)
                   for character in value[:MAX_SHOWN])
    return text if len(value) <= MAX_SHOWN else text + "…"


def bare(value):
    """A value without the backticks that mark it as a literal word."""
    value = (value or "").strip()
    if len(value) > 1 and value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        return value[1:-1].strip()
    return value


def is_link_like(info):
    return bool(stat.S_ISLNK(info.st_mode)
                or getattr(info, "st_file_attributes", 0)
                & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def read_untrusted(root, relative):
    """(text, None) for the file at the relative path below root, or (None, why it is not read).
    Every component is looked at with `lstat`, and none that is a link or another reparse point
    is passed through; the file is opened only as a regular file of at most MAX_BYTES bytes, and
    the file opened must be the one looked at."""
    current, parts = root, relative.split("/")
    info = None
    for index, part in enumerate(parts):
        current = os.path.join(current, part)
        try:
            info = os.lstat(current)
        except FileNotFoundError:
            return None, ABSENT
        except OSError as problem:
            return None, "cannot be read: %s" % (problem.strerror or problem)
        last = index == len(parts) - 1
        if is_link_like(info):
            return None, ("is a symbolic link or another reparse point; nothing is read through "
                          "it" if last else "lies below `%s`, a symbolic link or another reparse "
                          "point; nothing is read through it" % "/".join(parts[:index + 1]))
        if not last and not stat.S_ISDIR(info.st_mode):
            return None, "lies below `%s`, which is not a directory" % "/".join(parts[:index + 1])
    if stat.S_ISDIR(info.st_mode):
        return None, "is a directory, not a file; nothing is read from it"
    if not stat.S_ISREG(info.st_mode):
        return None, "is not a regular file; nothing is read from it"
    if info.st_size > MAX_BYTES:
        return None, "holds more than %d bytes; it is not read" % MAX_BYTES
    flags = (os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
             | getattr(os, "O_NONBLOCK", 0))
    try:
        handle = os.open(current, flags)
    except OSError as problem:
        return None, "cannot be read: %s" % (problem.strerror or problem)
    try:
        opened = os.fstat(handle)
        if (not stat.S_ISREG(opened.st_mode)
                or (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino)):
            return None, "changed while it was opened; it is not read"
        chunks, size = [], 0
        while size <= MAX_BYTES:
            chunk = os.read(handle, MAX_BYTES + 1 - size)
            if not chunk:
                break
            chunks.append(chunk)
            size += len(chunk)
    except OSError as problem:
        return None, "cannot be read: %s" % (problem.strerror or problem)
    finally:
        os.close(handle)
    data = b"".join(chunks)
    if len(data) > MAX_BYTES:
        return None, "holds more than %d bytes; it is not read" % MAX_BYTES
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as problem:
        return None, "is not UTF-8 text (byte %d); it is not read" % problem.start
    return text.lstrip("\ufeff").replace("\r\n", "\n"), None


# --- the forms read from the templates ------------------------------------------------------


@dataclass
class Form:
    header: list                                   # header line names, in order
    sections: list                                 # section titles, in order
    required: dict                                 # section title -> required `### ` headings
    tables: dict                                   # section title -> the columns of its table
    fields: list = field(default_factory=list)     # the fields of a rule, in order
    requires_invariant: bool = False               # every rule names an invariant
    per_part: bool = False                         # files are named <discipline>-<part>.md alone
    kinds: list = field(default_factory=list)      # the closed list of a role's *Kind*


def template_section(text, title):
    """The text under `## title` of a template, up to the next `## ` outside a code block."""
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


def parse_form(text, where):
    """The form a template's section `## Required form` gives in its fenced block."""
    section = template_section(text, FORM_SECTION)
    block = re.search(r"```markdown\n(.*?)```", section, re.S)
    if not block:
        raise TemplateError("%s holds no form in its section %s" % (where, FORM_SECTION))
    header, sections, required, tables, fields = [], [], {}, {}, []
    current = None
    for line in block.group(1).split("\n"):
        if line.startswith("## "):
            current = line[3:].strip()
            sections.append(current)
            required[current] = []
        elif line.startswith("### "):
            name = line[4:].strip()
            if current is not None and "<" not in name:
                required[current].append(name)
        elif FIELD_LINE.match(line):
            name = FIELD_LINE.match(line).group(1)
            (header if current is None else fields).append(name)
        elif line.startswith("|") and current is not None and current not in tables:
            tables[current] = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return Form(header, sections, required, tables, fields), section


def read_templates(here=HERE):
    """(the form every file of guidelines shares, {discipline: its merged form})."""
    with open(os.path.join(here, "template.md"), encoding="utf-8") as handle:
        common, _ = parse_form(handle.read(), "product-guidelines/template.md")
    for needed in (DISCIPLINE, APPLIES_TO):
        if needed not in common.header:
            raise TemplateError("the form of guidelines has no header line %s" % needed)
    for needed in (RULES, WHERE):
        if needed not in common.sections:
            raise TemplateError("the form of guidelines has no section %s" % needed)
    if DECISION not in common.fields or INVARIANT not in common.fields:
        raise TemplateError("the form of guidelines gives a rule no field %s or %s"
                            % (DECISION, INVARIANT))
    disciplines = {}
    for name in sorted(os.listdir(here)):
        path = os.path.join(here, name, "template.md")
        if not IDENTIFIER.fullmatch(name) or not os.path.isfile(path):
            continue
        where = "product-guidelines/%s/template.md" % name
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        form, section = parse_form(text, where)
        if form.header != common.header:
            raise TemplateError("%s gives header lines other than the form of guidelines" % where)
        positions = [form.sections.index(title) for title in common.sections
                     if title in form.sections]
        if len(positions) != len(common.sections) or positions != sorted(positions):
            raise TemplateError("%s does not hold the sections of the form of guidelines in "
                                "their order" % where)
        form.fields = list(common.fields)
        form.requires_invariant = bool(re.search(r"its \*Invariant\* names at least one "
                                                 r"invariant", " ".join(section.split())))
        form.per_part = ("`guidelines/%s-<part>.md`" % name) in text
        if form.tables:
            for title, columns in form.tables.items():
                for needed in (ROLE, KIND, TEXT_ON_IT, DECISION):
                    if needed not in columns:
                        raise TemplateError("the table of %s in %s has no column %s"
                                            % (title, where, needed))
            kinds = re.search(r"\*Kind\*: one of (.*?);", " ".join(text.split()))
            form.kinds = re.findall(r"`([^`]+)`", kinds.group(1)) if kinds else []
            if BACKGROUND not in form.kinds or TEXT not in form.kinds:
                raise TemplateError("%s gives no list of kinds holding %s and %s"
                                    % (where, BACKGROUND, TEXT))
            if ROLE_MEANING_RULE not in form.required.get(RULES, []):
                raise TemplateError("%s requires no rule %s" % (where, ROLE_MEANING_RULE))
        disciplines[name] = form
    return common, disciplines


# --- a file of guidelines as headings, fields and code --------------------------------------


@dataclass
class Block:
    title: str
    line: int          # the line of its heading, from 1
    start: int         # the index of the first line of its body
    end: int           # the index after its last line


class Document:
    def __init__(self, text):
        self.lines = text.split("\n")
        self.code = fenced_lines(self.lines)
        self.sections = self.blocks("## ", 0, len(self.lines))
        self.header_end = self.sections[0].line - 1 if self.sections else len(self.lines)

    def blocks(self, mark, start, end):
        starts = [index for index in range(start, end)
                  if not self.code[index] and self.lines[index].startswith(mark)]
        return [Block(self.lines[index][len(mark):].strip(), index + 1, index + 1,
                      starts[position + 1] if position + 1 < len(starts) else end)
                for position, index in enumerate(starts)]

    def prose(self, start, end):
        """The lines from start to end, those inside fenced code blanked."""
        return ["" if self.code[index] else self.lines[index] for index in range(start, end)]

    def text_lines(self, block):
        """(line number, stripped line) of every line of a block's body that is not blank."""
        return [(index + 1, self.lines[index].strip()) for index in range(block.start, block.end)
                if self.lines[index].strip()]


def fenced_lines(lines):
    """For each line, whether it stands in fenced code, its fences included: a fence of three or
    more backticks or tildes, closed by a fence of the same character at least as long."""
    flags, fence = [], None
    for line in lines:
        if fence is None:
            opening = OPEN_FENCE.match(line)
            if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                fence = opening.group(1)
                flags.append(True)
                continue
            flags.append(False)
        else:
            flags.append(True)
            stripped = line.strip()
            if (len(line) - len(line.lstrip(" ")) <= 3 and len(stripped) >= len(fence)
                    and set(stripped) == {fence[0]}):
                fence = None
    return flags


def is_dropped(lines):
    """Whether a body's first line that is not blank marks it as dropped."""
    return bool(lines) and bool(DROPPED.match(lines[0][1]))


# --- what references name -------------------------------------------------------------------


TO_DECISION, TO_INVARIANT = "decision", "invariant"


@dataclass
class Foundation:
    """The decisions and invariants a reference may name, as one commit, or a merge, holds them."""
    prefix: str = None                               # the log's prefix; None for a log of no entry
    decisions: dict = field(default_factory=dict)    # "ABC-01" -> (fingerprint, label) or
    #                                                  (None, label of a version binding nothing)
    invariants: dict = field(default_factory=dict)   # identifier -> (fingerprint, label)
    withdrawn: set = field(default_factory=set)      # identifiers the invariants file withdrew
    known: bool = True                               # False where the log or file is unread
    log_entries: list = field(default_factory=list)  # the log's entries, for the merged log
    entries: dict = field(default_factory=dict)      # identifier -> the invariant's entry

    def decision(self, word):
        """The decision number a word is, as the log writes it, or None: a number with the log's
        prefix; with any prefix where the log could not be read."""
        match = DECISION_NUMBER.fullmatch(word)
        if not match or (self.known and match.group(1) != self.prefix):
            return None
        return "%s-%02d" % (match.group(1), int(match.group(2)))

    def invariant(self, word):
        """Whether a word is an identifier the invariants file holds, as an entry or withdrawn;
        any identifier where the file could not be read."""
        if not self.known:
            return bool(IDENTIFIER.fullmatch(word))
        return word in self.invariants or word in self.withdrawn

    def current(self, kind, key):
        """(the entry's current fingerprint, the version that set it), or (None, why the entry is
        not in force)."""
        if kind == TO_DECISION:
            if key not in self.decisions:
                return None, "the decision log does not hold it"
            value, label = self.decisions[key]
            return (value, label) if value else (
                None, "its latest version, %s, holds no binding sentences" % label)
        if key in self.withdrawn:
            return None, "the invariants file has withdrawn it"
        if key not in self.invariants:
            return None, "the invariants file does not hold it"
        return self.invariants[key]


def decisions_named(value, foundation):
    """The decisions of the log a value names with a `@`, in their order."""
    return [key for key in (foundation.decision(match.group(1))
                            for match in REFERENCE_TOKEN.finditer(value)) if key]


def names_invariant(value, foundation):
    return any(foundation.invariant(match.group(1)) for match in REFERENCE_TOKEN.finditer(value))


def references(document, foundation):
    """(line, reference, kind, entry, its part after `@`) of every reference outside fenced code,
    in the two forms of spec §3.2: a decision number of the log or an identifier of the
    invariants file followed by `@` and a run of letters and digits, or any identifier followed by
    `@` and eight lower-case hexadecimal characters."""
    found = []
    for index, line in enumerate(document.lines):
        if document.code[index] or "@" not in line:
            continue
        for match in REFERENCE_TOKEN.finditer(line):
            word, after = match.groups()
            key = foundation.decision(word)
            if key is not None:
                found.append((index + 1, match.group(0), TO_DECISION, key, after))
            elif foundation.invariant(word) or (IDENTIFIER.fullmatch(word)
                                                and FINGERPRINT.fullmatch(after)):
                found.append((index + 1, match.group(0), TO_INVARIANT, word, after))
    return found


def entry_name(kind, key):
    return key if kind == TO_DECISION else "the invariant `%s`" % key


def latest_decisions(versions, same_binding):
    """number -> (its latest version, the version that set its current fingerprint: the first of
    the run of versions ending there with the same binding sentences), as the decisions guard
    reads the merged log."""
    latest = {}
    for entry in sorted(versions, key=lambda entry: (entry.number, entry.version)):
        previous = latest.get(entry.number)
        setter = (previous[1] if previous and same_binding(previous[0].binding, entry.binding)
                  else entry)
        latest[entry.number] = (entry, setter)
    return latest


def decision_fingerprints(latest, prefix, borrowed):
    """"<PREFIX-NN>" -> (current fingerprint, label of the version that set it), or (None, label of
    a latest version holding no binding sentences), of {number: (latest version, setter)}."""
    label, digest = borrowed.decisions.label_of, borrowed.fingerprint.fingerprint
    return {"%s-%02d" % (prefix, number): ((digest(entry.binding), label(setter, prefix))
                                           if entry.binding is not None
                                           else (None, label(entry, prefix)))
            for number, (entry, setter) in latest.items()}


def invariant_state(text, rules, borrowed):
    """({identifier: its entry of the highest version}, {withdrawn identifiers}) of an invariants
    file, read with the invariants guard's parser."""
    guard = borrowed.invariants
    entries, withdrawn, title = {}, set(), rules.lists[0][0]
    for item in guard.parse_file(text, rules):
        if isinstance(item, guard.Entry):
            if item.identifier not in entries or entries[item.identifier].version < item.version:
                entries[item.identifier] = item
        elif isinstance(item, guard.Table) and item.title == title:
            withdrawn.update(bare(cells[0]) for cells, _ in item.rows if cells and bare(cells[0]))
    return entries, withdrawn


def invariant_fingerprints(entries, borrowed):
    return {identifier: (borrowed.fingerprint.fingerprint(entry.sentence or ""),
                         borrowed.invariants.label_of(entry))
            for identifier, entry in entries.items()}


def read_foundation(top, report, borrowed, invariant_rules):
    """What references name on the commit checked, read from the working tree as a product's
    untrusted files; a Foundation not known, once the report says why, where the log or the
    invariants file cannot be read. A file absent is no failure: it holds no entry."""
    # invariant: guidelines-reference-current/1
    check = SAME_COMMIT
    texts = []
    for path, what in ((DECISION_LOG, "decision"), (INVARIANTS, "invariant")):
        text, why = read_untrusted(top, path)
        if text is None and why == ABSENT:
            report.notes.append("the repository holds no %s: no %s is in force" % (path, what))
            text = ""
        elif text is None:
            report.error(None, "%s %s, so no reference a file of guidelines makes can be checked"
                         % (path, why), check, (REFERENCES,))
            return Foundation(known=False)
        texts.append(text)
    guard = borrowed.decisions
    try:
        prefix = guard.detect_prefix(texts[0])
        log_entries = guard.parse_log(texts[0], prefix) if prefix else []
        latest = latest_decisions(guard.versions_of(log_entries), guard.same_binding)
        entries, withdrawn = invariant_state(texts[1], invariant_rules, borrowed)
    except PARSE_ERRORS as problem:
        report.error(None, "the decision log or the invariants file cannot be parsed, so no "
                           "reference can be checked: %s" % problem, check, (REFERENCES,))
        return Foundation(known=False)
    return Foundation(prefix, decision_fingerprints(latest, prefix, borrowed),
                      invariant_fingerprints(entries, borrowed), withdrawn,
                      log_entries=log_entries, entries=entries)


def merged_foundation(top, onto, foundation, borrowed, invariant_rules, report):
    """What references name in the foundation a merge onto `onto` leaves, or None once the report
    says why git cannot read it: the decisions as the decisions guard merges the log, given a
    report of this script's own that is discarded but for the failures of git it holds; each
    invariant as on the branch where its sentence differs from the fork point, as on `onto`
    otherwise."""
    # invariant: guidelines-reference-current/1
    def failed(message):
        report.error(None, message, AFTER_MERGE, (REFERENCES,))

    try:
        return merged_entries(top, onto, foundation, borrowed, invariant_rules, failed)
    except PARSE_ERRORS as problem:
        return failed("the foundation after a merge onto %s cannot be parsed: %s"
                      % (shown(onto), problem))


def merged_entries(top, onto, foundation, borrowed, invariant_rules, failed):
    """The work of merged_foundation, each failure given to `failed`, which returns None."""
    shared, guard = borrowed.shared, borrowed.decisions
    prefix = foundation.prefix
    if prefix is None:
        text, failure = shared.file_at(onto, DECISION_LOG, top)
        if failure:
            return failed(failure)
        prefix = guard.detect_prefix(text or "")
    decisions = {}
    if prefix is not None:
        discarded = shared.Report(DECISION_LOG)
        merged = guard.merged_log(os.path.join(top, *DECISION_LOG.split("/")),
                                  foundation.log_entries, onto, prefix, top, discarded)
        for owner, description in discarded.unowned:
            if owner is None:
                failed("the decision log after a merge onto %s cannot be read: %s"
                       % (shown(onto), description))
        if merged is None:
            return None
        decisions = decision_fingerprints({number: (entry, setter) for number, (entry, _, setter)
                                           in merged.items()}, prefix, borrowed)
    code, answer, message = shared.call_git(["merge-base", "HEAD", onto], top)
    if code != 0 and (code != 1 or message):
        return failed("git cannot find the merge base of HEAD and %s: %s"
                      % (shown(onto), message or "git merge-base exited with %d" % code))
    sides = []
    for commit in (answer.strip() if code == 0 else None, onto):
        text, failure = shared.file_at(commit, INVARIANTS, top) if commit else (None, None)
        if failure:
            return failed(failure)
        sides.append(invariant_state(text or "", invariant_rules, borrowed))
    branch = (foundation.entries, foundation.withdrawn)
    entries, withdrawn = merged_invariants(branch, sides[0], sides[1], borrowed)
    return Foundation(prefix, decisions, invariant_fingerprints(entries, borrowed), withdrawn)


def merged_invariants(branch, fork, onto, borrowed):
    """(entries, withdrawn identifiers) after a merge: each identifier as the branch holds it
    where its sentence differs from the fork point — added, reworded, withdrawn or removed there —
    and as the commit merged onto holds it otherwise; each side is (entries, withdrawn)."""
    digest = borrowed.fingerprint.fingerprint

    def sentence(side, identifier):
        entry = side[0].get(identifier)
        if entry is None or identifier in side[1]:
            return None
        return digest(entry.sentence or "")

    entries, withdrawn = {}, set()
    for identifier in set().union(*(set(side[0]) | side[1] for side in (branch, fork, onto))):
        side = branch if sentence(branch, identifier) != sentence(fork, identifier) else onto
        if identifier in side[1]:
            withdrawn.add(identifier)
        elif identifier in side[0]:
            entries[identifier] = side[0][identifier]
    return entries, withdrawn


# --- checks of one file ---------------------------------------------------------------------


def check_order(found, expected, label, report, check, missing_at=None):
    """An error for each item of `expected` missing from `found` ({name: line}), at the line
    `missing_at` of the heading that should hold it, and for each pair standing in the other
    order than `expected` gives; `label` writes an item's name."""
    present = [name for name in expected if name in found]
    for name in expected:
        if name not in found:
            report.error(missing_at, "%s is missing" % label(name), check, (FORM,))
    for before, after in zip(present, present[1:]):
        if found[after] < found[before]:
            report.error(found[after], "%s stands before %s; the template puts it after"
                         % (label(after), label(before)), check, (FORM,))


def check_header(document, form, report, shared):
    """The header lines the template gives, in its order, before the first section."""
    # invariant: guidelines-form/1
    check = "check_header"
    report.ran(check, FORM)
    fields = shared.parse_fields(document.prose(0, document.header_end), 1)
    check_order({name: fields[name][1] for name in fields}, form.header,
                lambda name: "the header line *%s*" % name, report, check)
    return fields


def check_sections(document, form, report, foundation):
    """The sections the template gives, in its order, each once; a dropped one holding only
    `none —` with a decision of the log."""
    # invariant: guidelines-form/1
    check = "check_sections"
    report.ran(check, FORM)
    found, sections = {}, {}
    for block in document.sections:
        if block.title in form.sections:
            if block.title in found:
                report.error(block.line, "the section `## %s` stands twice, also at line %d"
                             % (shown(block.title), found[block.title]), check, (FORM,))
                continue
            found[block.title] = block.line
            sections[block.title] = block
    check_order(found, form.sections, lambda title: "the section `## %s`" % title, report,
                check)
    kept = {}
    for title, block in sections.items():
        lines = document.text_lines(block)
        if is_dropped(lines):
            check_drop(lines, "the section `## %s`" % title, report, check, foundation)
        else:
            kept[title] = block
    return kept


def check_drop(lines, what, report, check, foundation):
    drop = DROP_LINE.match(lines[0][1]) if len(lines) == 1 else None
    if drop is None or foundation.decision(drop.group(1)) is None:
        report.error(lines[0][0], "%s is dropped, so it holds only `none — <PREFIX-NN>@"
                                  "<fingerprint>`, naming the product's decision that departs "
                                  "from the template, and nothing else; it holds `%s`"
                     % (what, shown(lines[0][1])), check, (FORM,))


def check_rules(document, sections, form, report, shared, foundation):
    """The required rules in the template's order; each rule kept with its fields in order, a
    decision in *Decision* and, where the discipline requires it, an invariant in *Invariant*;
    each dropped rule holding only `none —` with its decision. Returns {rule: its fields} of the
    rules kept."""
    # invariant: guidelines-form/1
    check = "check_rules"
    report.ran(check, FORM)
    block = sections.get(RULES)
    if block is None:
        return {}
    rules = document.blocks("### ", block.start, block.end)
    found = {}
    for rule in rules:
        if rule.title in form.required.get(RULES, []) and rule.title in found:
            report.error(rule.line, "the rule `### %s` stands twice, also at line %d"
                         % (shown(rule.title), found[rule.title]), check, (FORM,))
        found.setdefault(rule.title, rule.line)
    check_order(found, form.required.get(RULES, []),
                lambda title: "the required rule `### %s`" % title, report, check, block.line)
    kept = {}
    for rule in rules:
        name = "`### %s`" % shown(rule.title)
        lines = document.text_lines(rule)
        if is_dropped(lines):
            check_drop(lines, "the rule %s" % name, report, check, foundation)
            continue
        fields = shared.parse_fields(document.prose(rule.start, rule.end), rule.start + 1)
        check_order({key: fields[key][1] for key in fields}, form.fields,
                    lambda key, name=name: "the field *%s* of the rule %s" % (key, name),
                    report, check, rule.line)
        decision = fields.get(DECISION)
        if decision and not decisions_named(decision[0], foundation):
            report.error(decision[1], "the rule %s names no decision of the log in *Decision*, "
                                      "as `<PREFIX-NN>@<fingerprint>`" % name, check, (FORM,))
        invariant = fields.get(INVARIANT)
        if form.requires_invariant and invariant and not names_invariant(invariant[0],
                                                                         foundation):
            report.error(invariant[1], "the rule %s names no invariant in *Invariant*, as "
                                       "`<identifier>@<fingerprint>`; every rule of this "
                                       "discipline names one" % name, check, (FORM,))
        kept.setdefault(rule.title, fields)
    return kept


def table_cells(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def check_roles(document, sections, rules, form, report, foundation):
    """Each row of a table of roles: a *Kind* of the closed list, a background's *Text on it*
    naming a text role of the table, a decision; and each decision of the table named by the rule
    of each role's meaning, unless that rule is dropped."""
    # invariant: guidelines-form/1
    check = "check_roles"
    report.ran(check, FORM)
    for title, columns in form.tables.items():
        block = sections.get(title)
        if block is None:
            continue
        table = [(index + 1, document.lines[index]) for index in range(block.start, block.end)
                 if not document.code[index] and document.lines[index].lstrip().startswith("|")]
        if not table:
            report.error(block.line, "the section `## %s` holds no table" % title, check, (FORM,))
            continue
        header_line, header = table[0]
        if table_cells(header) != columns:
            report.error(header_line, "the table of `## %s` has the columns %s; the template "
                                      "gives %s" % (title, shown(" | ".join(table_cells(header))),
                                                    " | ".join(columns)), check, (FORM,))
            continue
        rows = []
        for line, text in table[1:]:
            cells = table_cells(text)
            if all(SEPARATOR_CELL.match(cell) for cell in cells):
                continue
            if len(cells) != len(columns):
                report.error(line, "the row holds %d cells; the table has %d columns"
                             % (len(cells), len(columns)), check, (FORM,))
                continue
            rows.append((line, dict(zip(columns, cells))))
        kinds = {bare(row[ROLE]): bare(row[KIND]) for _, row in rows}
        decisions = {}
        for line, row in rows:
            role, kind = shown(bare(row[ROLE])), bare(row[KIND])
            if kind not in form.kinds:
                report.error(line, "the role `%s` is of the kind `%s`, which is none of %s"
                             % (role, shown(kind), ", ".join(form.kinds)), check, (FORM,))
            if kind == BACKGROUND:
                text_on_it = bare(row[TEXT_ON_IT])
                if kinds.get(text_on_it) != TEXT:
                    report.error(line, "the background role `%s` names in *Text on it* `%s`, "
                                       "which is no role of the kind `%s` in the table"
                                 % (role, shown(text_on_it), TEXT), check, (FORM,))
            named = decisions_named(row[DECISION], foundation)
            if not named:
                report.error(line, "the role `%s` names no decision of the log in *Decision*, "
                                   "as `<PREFIX-NN>@<fingerprint>`" % role, check, (FORM,))
            for number in named:
                decisions.setdefault(number, line)
        meaning = rules.get(ROLE_MEANING_RULE)
        if meaning is None or DECISION not in meaning:
            continue
        value, at = meaning[DECISION]
        covered = set(decisions_named(value, foundation))
        for number, line in decisions.items():
            if number not in covered:
                report.error(at, "`%s`, which the table of `## %s` names at line %d, is not "
                                 "named in *Decision* of `### %s`"
                             % (number, title, line, ROLE_MEANING_RULE), check, (FORM,))


def check_parts(fields, name, discipline, form, disciplines, parts, report):
    """Each part *Applies to* names, and the part a file's name holds, is a part of the map; the
    file's name agrees with its *Discipline*, and no file carries the name of a discipline the-way
    gives a template of under another *Discipline*, which would hold it to the wrong form."""
    # invariant: guidelines-form/1
    check = "check_parts"
    report.ran(check, FORM)
    if parts is not None and APPLIES_TO in fields:
        value, line = fields[APPLIES_TO]
        named = [bare(item) for item in value.replace("\n", " ").split("·") if bare(item)]
        if not named:
            report.error(line, "*Applies to* names no part of the map", check, (FORM,))
        for part in named:
            if part not in parts:
                report.error(line, "*Applies to* names `%s`, which is no part of the map"
                             % shown(part), check, (FORM,))
    if discipline is None:
        return
    stem = name[:-len(".md")]
    for other in sorted(disciplines):
        if other != discipline and (stem == other or stem.startswith(other + "-")):
            report.error(None, "the file's name is one of guidelines of the discipline `%s`, "
                               "whose template the-way gives, but its *Discipline* reads `%s`; "
                               "it would be held to the wrong form"
                         % (other, shown(discipline)), check, (FORM,))
            return
    part = stem[len(discipline) + 1:] if stem.startswith(discipline + "-") else ""
    if (stem == discipline and not form.per_part) or part:
        if part and parts is not None and part not in parts:
            report.error(None, "the file's name names the part `%s`, which is no part of the map"
                         % shown(part), check, (FORM,))
        return
    given = ("`guidelines/%s-<part>.md`" if form.per_part
             else "`guidelines/%s.md` or `guidelines/%s-<part>.md`")
    report.error(None, "the file's name does not agree with its *Discipline* `%s`: guidelines of "
                       "that discipline stand in %s"
                 % (shown(discipline), given.replace("%s", shown(discipline))), check, (FORM,))


def refused(path):
    """Why a path of `## Where in code` is refused before git sees it, or None."""
    if any(not character.isprintable() for character in path):
        return "holds a character that is not printable"
    if "\\" in path:
        return "holds a backslash, as a drive or a UNC prefix written for Windows does"
    if ":" in path:
        return "holds a `:`, as a drive, a URL or git's pathspec magic does"
    if path.startswith("/"):
        return "is absolute or a UNC prefix"
    if ".." in path.split("/"):
        return "holds a `..` segment"
    return None


def check_paths(document, sections, tracked, report):
    """Each path in backticks under `## Where in code` is relative, stays in the repository and
    names a file or a directory git tracks."""
    # invariant: guidelines-form/1
    check = "check_paths"
    report.ran(check, FORM)
    block = sections.get(WHERE)
    if block is None:
        return
    for index in range(block.start, block.end):
        if document.code[index]:
            continue
        for span in CODE_SPAN.finditer(document.lines[index]):
            path = span.group(1).strip()
            if not path:
                continue
            why = refused(path)
            if why:
                report.error(index + 1, "the path `%s` %s; a path of `## %s` is relative to the "
                                        "root of the repository and stays in it"
                             % (shown(path), why, WHERE), check, (FORM,))
                continue
            files, directories = tracked()
            if files is None:   # `directories` then holds why git could not list them
                report.error(index + 1, "the path `%s` cannot be checked: %s"
                             % (shown(path), directories), check, (FORM,))
                continue
            normal = "/".join(piece for piece in path.split("/") if piece not in ("", "."))
            found = normal in directories if path.endswith("/") else (
                normal in files or normal in directories)
            if not found:
                report.error(index + 1, "the path `%s` names nothing git tracks"
                             % shown(path), check, (FORM,))


def check_references(document, foundation, report):
    """Each reference outside fenced code carries eight lower-case hexadecimal characters after
    its `@`, names an entry in force and carries its current fingerprint on the commit checked.
    Returns the references found current there, as (line, reference, kind, entry, fingerprint),
    for the check after the merge."""
    # invariant: guidelines-reference-current/1
    check = SAME_COMMIT
    report.ran(check, REFERENCES)
    current = []
    for line, token, kind, key, carried in references(document, foundation):
        what = entry_name(kind, key)
        if not FINGERPRINT.fullmatch(carried):
            report.error(line, "`%s` names %s, but `%s` after its `@` is no fingerprint: a "
                               "fingerprint is eight lower-case hexadecimal characters"
                         % (shown(token), what, shown(carried)), check, (REFERENCES,))
            continue
        value, setter = foundation.current(kind, key)
        if value is None:
            report.error(line, "`%s` names %s, which is not in force on the commit checked: %s"
                         % (shown(token), what, setter), check, (REFERENCES,))
        elif value != carried:
            report.error(line, "`%s` carries a fingerprint other than the current one: on the "
                               "commit checked, the current fingerprint of %s is %s, set by %s"
                         % (shown(token), what, value, setter), check, (REFERENCES,))
        else:
            current.append((line, token, kind, key, carried))
    return current


def check_merged_references(current, merged, onto, report):
    """Each reference current on the commit checked names an entry in force, and carries its
    current fingerprint, in the foundation a merge onto `onto` leaves."""
    # invariant: guidelines-reference-current/1
    check = AFTER_MERGE
    report.ran(check, REFERENCES)
    after = "after a merge onto %s" % shown(onto)
    for line, token, kind, key, carried in current:
        what = entry_name(kind, key)
        value, setter = merged.current(kind, key)
        if value is None:
            report.error(line, "`%s` names %s, which is not in force %s: %s"
                         % (shown(token), what, after, setter), check, (REFERENCES,))
        elif value != carried:
            report.error(line, "`%s` carries a fingerprint other than the current one: %s, the "
                               "current fingerprint of %s is %s, set by %s"
                         % (shown(token), after, what, value, setter), check, (REFERENCES,))


@dataclass
class Context:
    """What the checks of every file share."""
    shared: object
    common: Form
    disciplines: dict
    parts: object            # the parts of the map, or None where it cannot be read
    tracked: object          # the function giving what git tracks
    foundation: Foundation   # what references name on the commit checked
    merged: object = None    # what they name after the merge, or None where it is not checked
    onto: str = None


def check_file(name, text, context, report):
    """Every check of one file of guidelines, against the form of its *Discipline*: the
    discipline's template where the-way gives one, the form of guidelines otherwise; then its
    references, where the log and the invariants file could be read."""
    document = Document(text)
    shared, foundation = context.shared, context.foundation
    fields = check_header(document, context.common, report, shared)
    discipline = bare(fields[DISCIPLINE][0]) if DISCIPLINE in fields else None
    form = context.disciplines.get(discipline, context.common)
    sections = check_sections(document, form, report, foundation)
    rules = check_rules(document, sections, form, report, shared, foundation)
    check_roles(document, sections, rules, form, report, foundation)
    check_parts(fields, name, discipline, form, context.disciplines, context.parts, report)
    check_paths(document, sections, context.tracked, report)
    if foundation.known:
        current = check_references(document, foundation, report)
        if context.merged is not None:
            check_merged_references(current, context.merged, context.onto, report)


# --- the run --------------------------------------------------------------------------------


def list_guidelines(top, report, shared):
    """The names of the files `guidelines/<name>.md` git lists, tracked or not ignored; a warning
    for every other path it lists under `guidelines/`; None where `guidelines` is no directory."""
    # invariant: guidelines-form/1
    check = "read_guidelines"
    report.ran(check, FORM)
    try:
        info = os.lstat(os.path.join(top, GUIDELINES))
    except FileNotFoundError:
        report.notes.append("the repository holds no %s/: no file of guidelines to check"
                            % GUIDELINES)
        return []
    except OSError as problem:
        report.error(None, "`%s` cannot be read: %s" % (GUIDELINES, problem.strerror or problem),
                     check, (FORM,))
        return None
    if is_link_like(info):
        report.error(None, "`%s` is a symbolic link or another reparse point; nothing is read "
                           "through it" % GUIDELINES, check, (FORM,))
        return None
    if not stat.S_ISDIR(info.st_mode):
        report.error(None, "`%s` is not a directory; guidelines stand in files `%s/<name>.md`"
                     % (GUIDELINES, GUIDELINES), check, (FORM,))
        return None
    code, listing, message = shared.call_git(
        ["-c", "core.ignorecase=false", "ls-files", "-z", "--cached", "--others",
         "--exclude-standard", "--", ":(literal)%s/" % GUIDELINES], top)
    if code != 0:
        report.error(None, "git cannot list the files of %s/: %s"
                     % (GUIDELINES, message or "git ls-files exited with %d" % code),
                     check, (FORM,))
        return None
    names, seen = [], set()
    for path in listing.split("\0"):
        if not path or path in seen:
            continue
        seen.add(path)
        name = path[len(GUIDELINES) + 1:] if path.startswith(GUIDELINES + "/") else ""
        if is_guidelines_name(name):
            if name not in names:
                names.append(name)
            continue
        report.warning(None, "`%s` is not read: guidelines stand in files `%s/<name>.md`, one "
                             "level deep, with a lower-case `.md`" % (shown(path), GUIDELINES))
        # A directory, or a link to one, named like a file of guidelines: git lists only what
        # lies below it, and the read of its own name reports what it is.
        first = name.split("/")[0]
        if "/" in name and is_guidelines_name(first) and first not in names:
            names.append(first)
    if not names:
        report.notes.append("%s/ holds no file `%s/<name>.md`: no file of guidelines to check"
                            % (GUIDELINES, GUIDELINES))
    return sorted(names)


def is_guidelines_name(name):
    """Whether a name below `guidelines/` is one of a file of guidelines, `<name>.md`."""
    return name.endswith(".md") and len(name) > len(".md") and "/" not in name


def read_parts(top, report, part_map, map_rules):
    """The identifiers of the parts the product's map holds, or None once the report says why
    they cannot be read."""
    # invariant: guidelines-form/1
    check = "check_parts"
    report.ran(check, FORM)
    text, why = read_untrusted(top, PART_MAP)
    if text is None:
        report.error(None, "the part map %s %s, so no part a file of guidelines names can be "
                           "checked" % (PART_MAP, why), check, (FORM,))
        return None
    try:
        entries, _ = part_map.parse_map(text, map_rules)
    except (ValueError, IndexError, KeyError, AttributeError, TypeError) as problem:
        report.error(None, "the part map %s cannot be parsed: %s" % (PART_MAP, problem),
                     check, (FORM,))
        return None
    return {entry.identifier for entry in entries if entry.kind == "part"}


def tracked_paths(top, shared):
    """A function giving (the files git tracks, the directories holding them), asked of git once;
    (None, why) where git cannot list them."""
    answer = []

    def tracked():
        if not answer:
            code, listing, message = shared.call_git(
                ["-c", "core.ignorecase=false", "ls-files", "-z"], top)
            if code != 0:
                answer.append((None, "git cannot list the files it tracks: %s"
                               % (message or "git ls-files exited with %d" % code)))
            else:
                files = {path for path in listing.split("\0") if path}
                directories = set()
                for path in files:
                    pieces = path.split("/")
                    for end in range(1, len(pieces)):
                        directories.add("/".join(pieces[:end]))
                answer.append((files, directories))
        return answer[0]

    return tracked


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        for line in lines:
            handle.write(json.dumps(line, ensure_ascii=False) + "\n")


def merge_check(top, merge_onto, report, shared):
    """The commit whose merge the references are checked against, or None. Given no option, a
    note says that check does not run; given `none`, it is recorded `unchecked` with the reason the
    guards share; a commit that does not exist is an error of the run. The check on the commit
    itself runs in every run, with no file of guidelines too."""
    # invariant: guidelines-reference-current/1
    report.ran(SAME_COMMIT, REFERENCES)
    if merge_onto is None:
        report.notes.append("no --merge-onto given: the references are not compared with the "
                            "foundation a merge leaves; that check is not run, and is not "
                            "counted in the last line")
        return None
    if merge_onto == shared.NO_COMMIT:
        report.unchecked(AFTER_MERGE, shared.NO_COMMIT_REASON, shared.NO_MERGE_ONTO, REFERENCES)
        report.cannot_check("the references in the foundation a merge leaves",
                            shared.NO_MERGE_ONTO)
        return None
    if not shared.find_commit(top, "--merge-onto", merge_onto, report):
        return None
    report.ran(AFTER_MERGE, REFERENCES)
    return merge_onto


def run(root=".", merge_onto=None, record=None, stream=None):
    stream = stream or sys.stdout
    if record is not None:
        if not record.endswith(".jsonl"):
            stream.write("the record %s does not end in .jsonl\n" % record)
            return 2
        try:
            os.makedirs(os.path.dirname(os.path.abspath(record)), exist_ok=True)
            open(record, "w", encoding="utf-8").close()
        except OSError as problem:
            stream.write("cannot write the record: %s\n" % problem)
            return 2

    def stop(message):
        stream.write(message + "\n")
        if record is not None:
            write_lines(record, [{"check": PROGRAM, "verdict": "fail", "invariant": None,
                                  "description": message}])
        return 2

    try:
        common, disciplines = read_templates()
    except (OSError, UnicodeDecodeError, TemplateError) as problem:
        return stop("cannot read the templates of guidelines: %s" % problem)
    borrowed, failure = borrow()
    if failure:
        return stop(failure)
    shared, part_map = borrowed.shared, borrowed.part_map
    try:
        map_rules = part_map.read_rules()
    except (OSError, UnicodeDecodeError, part_map.TemplateError, AttributeError,
            IndexError) as problem:
        return stop("cannot read the rules of the part map from its template: %s" % problem)
    try:
        invariant_rules = borrowed.invariants.read_rules()
    except (OSError, UnicodeDecodeError, borrowed.invariants.TemplateError, AttributeError,
            IndexError) as problem:
        return stop("cannot read the rules of the invariants file from its template: %s"
                    % problem)
    code, top, message = shared.call_git(["rev-parse", "--show-toplevel"], root)
    try:
        at_top = code == 0 and os.path.samefile(top.strip(), root)
    except OSError:
        at_top = False
    if not at_top:
        return stop("%s is not the top of a git repository%s"
                    % (root, ": %s" % message if code != 0 and message else ""))
    top = top.strip()

    options = ["--merge-onto"] if merge_onto is not None else []
    reports = [shared.Report(GUIDELINES, options, program=PROGRAM, selected_by=SELECTED_BY)]
    onto = merge_check(top, merge_onto, reports[0], shared)
    names = list_guidelines(top, reports[0], shared)
    if names is None:
        # what cannot be listed cannot be checked for references either
        reports[0].fail(None, "the files of %s/ cannot be listed" % GUIDELINES, SAME_COMMIT,
                        (REFERENCES,))
    if names:
        foundation = read_foundation(top, reports[0], borrowed, invariant_rules)
        merged = (merged_foundation(top, onto, foundation, borrowed, invariant_rules, reports[0])
                  if onto is not None and foundation.known else None)
        context = Context(shared, common, disciplines,
                          read_parts(top, reports[0], part_map, map_rules),
                          tracked_paths(top, shared), foundation, merged, onto)
        for name in names:
            path = "%s/%s" % (GUIDELINES, name)
            report = shared.Report(shown(path), options, program=PROGRAM,
                                   selected_by=SELECTED_BY)
            reports.append(report)
            report.ran("read_guidelines", FORM)
            text, why = read_untrusted(top, path)
            if text is None:
                report.error(None, "`%s` %s" % (shown(path), why), "read_guidelines", (FORM,))
                report.fail(None, "`%s` %s, so its references cannot be checked"
                            % (shown(path), why), SAME_COMMIT, (REFERENCES,))
                continue
            check_file(name, text, context, report)

    for report in reports:
        report.print(stream)
    if record is not None:
        write_lines(record, [line for report in reports for line in report.record()])
    return 1 if any(report.errors for report in reports) else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a product's guidelines against the "
                                                 "templates of the-way.")
    parser.add_argument("root", nargs="?", default=".",
                        help="the top of the repository, by default the working directory")
    parser.add_argument("--merge-onto", help="the commit of the main branch a merge goes onto, "
                                             "`none` where there is none; selects the checks of "
                                             "references for the record")
    parser.add_argument("--record", help="the JSON Lines file, its path ending in `.jsonl`, "
                                         "that receives a verdict for each invariant a check "
                                         "the run's options select cites")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.root, arguments.merge_onto, arguments.record)


if __name__ == "__main__":
    sys.exit(main())
