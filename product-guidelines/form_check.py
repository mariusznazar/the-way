"""Form check of a product's guidelines (WAY-170).

Checks every file `guidelines/<name>.md` of a repository against the template every product's
guidelines share, `product-guidelines/template.md`, and, where the-way gives one, the template of
the file's discipline, `product-guidelines/<discipline>/template.md`. Both are read from the
checkout of the-way this script lies in: in a product, its pinned `.the-way`; in the-way itself, the
repository checked (WAY-170). The form is read from the fenced block of each template's section
`## Required form`, so the rules of form live in the templates alone (WAY-171). A discipline whose
template also gives a section `## Required form of a kind` keeps its general file in the first form,
`guidelines/<discipline>.md`, and a file `guidelines/<discipline>-<kind>.md` for each kind in the
second, `<kind>` being words of lower-case letters and digits joined by single hyphens; the coding
discipline's template gives one (WAY-167). The words of the form its checks act on — the sections,
the columns of each table, the closed lists of *Kind* and of *Status* — are read back from the
templates, and a template lacking one cannot be run against.

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

What it reports, each finding an error of `guidelines-form` (WAY-167, WAY-170, WAY-171): a header
line, section, required rule or rule field missing or out of order; a rule naming no decision, and
in a form whose template section requires it, no invariant — each form of a discipline read for
that demand on its own; in every table the template gives, a section holding no table, a header
whose cells are not the template's columns, a header with no separator row right under it, a
separator row anywhere else, and a row whose number of cells — a bar in backticks splitting a cell,
as Markdown reads a row — is not that of the columns; in a table of roles, a *Kind* outside its
list, a background role whose *Text on it* names no text role of the table, a row naming no
decision, and a decision of the table that the rule of each role's meaning does not name unless that
rule is dropped; a dropped section or rule holding anything but `none — <PREFIX-NN>@<fingerprint>`;
a part named in *Applies to* or in the file's name that the map does not hold; a file whose name and
*Discipline* disagree, a file `<discipline>-<kind>.md` whose `<kind>` is not words of lower-case
letters and digits joined by single hyphens among them; a path of `## Where in code` that is
absolute, holds a `..` segment, a drive, a UNC prefix, a backslash or a `:`, or names nothing git
tracks. In coding guidelines (WAY-167, WAY-198, WAY-199, WAY-212): a file
`guidelines/coding-<kind>.md` git tracks that no row of the table under `## Kinds of code` of
`guidelines/coding.md` names by its path in *File*, or beside which git tracks no
`guidelines/coding.md` or that file cannot be read; a row of that table whose *File* names no file
of a kind git tracks, whose *Kind* is not the `<kind>` of the file its *File* names, or whose *When
to read* is empty; in the table under `## Files of this kind` of a file of a kind, no row or more
than one whose *Status* is `exemplar`, a row whose *Status* is off the template's list, whose
*File* names no file git tracks, or which is not the exemplar's and whose *Decision* is not `—`,
and an exemplar's row whose *Decision* names no decision of the log in force, or one whose binding
sentences, their whitespace collapsed, lack its *File* or the file's `<kind>` in backticks — that
reference's fingerprint being checked as every reference's is. A *File* of either table is one
path in backticks, refused as a path of `## Where in code` is. A file of a kind that the table of
its files leaves out is no error. In guidelines of every discipline, the test cases of a rule kept
under `## Rules` whose *Invariant* names an invariant other than `guidelines-form` (WAY-168): for
each invariant it names other than `guidelines-form`, a missing case after its fields — a fenced
block whose info string reads `good <identifier> <path>`, or one reading `bad <identifier> <path>`
— reported at *Invariant*; an optional `base <identifier> <path>` block supplies a prepared earlier
file (WAY-223), with the same path as both cases; at its opening line, a second block of the same
kind and invariant, a case
naming an invariant the rule does not name, or `guidelines-form`, a case whose path is absolute,
holds a `..` segment, a drive, a UNC prefix, a backslash, a `:` or a character that is not
printable, any other fenced block of the rule — one standing before the rule's fields end, opened
by anything but three backticks, or whose info string is of no such form, as a bare line of three
backticks closing a case early leaves the case's own closing line — reported as a malformed test
case, and every fenced block of the rule left open to the end of the file; a case closed by
anything but three backticks, at its closing line; and each line inside a case that, after any
leading whitespace, starts with three backticks or three tildes, which
`instruction-files/check_instructions.py` reads as a fence — a line split, as that script splits
it, at a carriage return, a separator or a next-line character too — at that line. The info string
is read from an opening fence alone, and a block opens and closes as Markdown reads fences: three
or more backticks or tildes after at most three spaces, closed by a line of the same character
alone, at least as long. A rule naming `guidelines-form` alone needs no case, its cases being
the-way's own tests of this script. A path of a case may name a file the product does not hold. A
decision is
named by a number
with the prefix of the product's log, an invariant by an identifier its invariants file holds as an
entry or a withdrawn identifier. A path git lists under `guidelines/` that is not
`guidelines/<name>.md`, one level deep with a lower-case `.md`, gets a warning and is not read.

What it reports as an error of `guidelines-reference-current` (WAY-169): a reference anywhere
outside fenced code — a decision number of the log or an identifier of the invariants file followed
by `@` and a run of letters and digits, or any identifier followed by `@` and eight lower-case
hexadecimal characters, as that invariant's sentence gives them — whose part after `@` is no
fingerprint, that names a decision the log does not hold or holds with no binding sentences, or an
invariant the file does not hold or has withdrawn, or whose fingerprint is not the entry's current
one on the commit checked and, given a commit to merge onto, after the merge: the decisions as the
decisions guard merges the log, an invariant as on the branch where its sentence differs from the
fork point and as on that commit otherwise. Every fingerprint is computed by
`relation-model/fingerprint.py`; a message names the reference, the entry and its current
fingerprint, and never offers to renew one (WAY-31). The parsers of the decisions and invariants
guards are borrowed with reports of this script's own, discarded after the call: only a failure of
git carries over, never a finding of the log's own rules.

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
repository, a template of the-way or the code it borrows cannot be read, a template lacks a word of
the form the checks act on, or the record path does not end in `.jsonl` or cannot be written.
"""

import argparse
import bisect
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
FORM_OF_A_KIND = "Required form of a kind"
RULES = "Rules"
WHERE = "Where in code"
DISCIPLINE = "Discipline"
APPLIES_TO = "Applies to"
DECISION = "Decision"
INVARIANT = "Invariant"
ROLE, KIND, TEXT_ON_IT = "Role", "Kind", "Text on it"
BACKGROUND, TEXT = "background", "text"
ROLE_MEANING_RULE = "Each role in its meaning"
# The discipline whose general file indexes its files of a kind, with the tables of its two forms.
CODING = "coding"
KINDS_OF_CODE, FILES_OF_A_KIND = "Kinds of code", "Files of this kind"
FILE, WHEN_TO_READ, STATUS = "File", "When to read", "Status"
STATUSES = ("exemplar", "copy", "do not copy")
EXEMPLAR, NO_DECISION = STATUSES[0], "—"
GENERAL_CODING = "%s/%s.md" % (GUIDELINES, CODING)
# The test cases of a rule: their outer fence, the first word of their info string, the identifier
# of the invariant they are never given for, and how a line that opens a fence starts.
CASE_FENCE, CASE_KINDS = "```", ("good", "bad")
BASE_KIND = "base"
FORM_IDENTIFIER = FORM.split("/")[0]
INNER_FENCES = ("```", "~~~")

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
    role_tables: list = field(default_factory=list)  # the titles of the tables of roles
    of_a_kind: object = None                       # the form of <discipline>-<kind>.md, if any
    statuses: list = field(default_factory=list)   # the closed list of a file's *Status*


def template_section(text, title, required=True):
    """The text under `## title` of a template, up to the next `## ` outside a code block; None
    where a section that is not required is missing."""
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
        if not required:
            return None
        raise TemplateError('section "%s" not found' % title)
    return "\n".join(lines)


def parse_form(text, where, title=FORM_SECTION):
    """The form a template's section `## title` gives in its fenced block, and the section."""
    section = template_section(text, title)
    block = re.search(r"```markdown\n(.*?)```", section, re.S)
    if not block:
        raise TemplateError("%s holds no form in its section %s" % (where, title))
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
            tables[current] = table_cells(line)
    return Form(header, sections, required, tables, fields), section


def read_templates(here=HERE):
    """(the form every file of guidelines shares, {discipline: its merged form}); a discipline's
    form holds in `of_a_kind` the form of its files of a kind, where its template gives one."""
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
        form = discipline_form(text, FORM_SECTION, common, where)
        form.per_part = ("`guidelines/%s-<part>.md`" % name) in text
        if template_section(text, FORM_OF_A_KIND, required=False) is not None:
            form.of_a_kind = discipline_form(text, FORM_OF_A_KIND, common, where)
        for each in (form, form.of_a_kind):
            if each is not None:
                read_roles(each, text, where)
        if name == CODING:
            read_coding_words(form, text, where)
        disciplines[name] = form
    return common, disciplines


def discipline_form(text, title, common, where):
    """The merged form the section `## title` of a discipline's template gives: the header lines
    and sections of the form of guidelines, in their order, with the fields of its rules, and
    whether the section requires an invariant in every rule."""
    form, section = parse_form(text, where, title)
    if form.header != common.header:
        raise TemplateError("%s gives in its section %s header lines other than the form of "
                            "guidelines" % (where, title))
    positions = [form.sections.index(name) for name in common.sections if name in form.sections]
    if len(positions) != len(common.sections) or positions != sorted(positions):
        raise TemplateError("%s does not hold in its section %s the sections of the form of "
                            "guidelines in their order" % (where, title))
    form.fields = list(common.fields)
    form.requires_invariant = bool(re.search(r"its \*Invariant\* names at least one "
                                             r"invariant", " ".join(section.split())))
    return form


def read_roles(form, text, where):
    """The tables of roles of a form, each one holding a column *Role*, with the columns, the
    closed list of *Kind* and the rule of each role's meaning their checks act on."""
    form.role_tables = [title for title, columns in form.tables.items() if ROLE in columns]
    for title in form.role_tables:
        for needed in (ROLE, KIND, TEXT_ON_IT, DECISION):
            if needed not in form.tables[title]:
                raise TemplateError("the table of %s in %s has no column %s"
                                    % (title, where, needed))
    meaning = ROLE_MEANING_RULE in form.required.get(RULES, [])
    if not form.role_tables:
        if meaning:
            raise TemplateError("%s requires the rule %s but gives no table of roles"
                                % (where, ROLE_MEANING_RULE))
        return
    kinds = re.search(r"\*Kind\*: one of (.*?);", " ".join(text.split()))
    form.kinds = re.findall(r"`([^`]+)`", kinds.group(1)) if kinds else []
    if BACKGROUND not in form.kinds or TEXT not in form.kinds:
        raise TemplateError("%s gives no list of kinds holding %s and %s"
                            % (where, BACKGROUND, TEXT))
    if not meaning:
        raise TemplateError("%s requires no rule %s" % (where, ROLE_MEANING_RULE))


def read_coding_words(form, text, where):
    """The words of the coding template the checks of its two forms act on: the form of a kind,
    the section and the columns of each form's table, and the closed list of *Status*."""
    if form.of_a_kind is None:
        raise TemplateError("%s gives no section %s" % (where, FORM_OF_A_KIND))
    for each, title, columns in ((form, KINDS_OF_CODE, (KIND, FILE, WHEN_TO_READ)),
                                 (form.of_a_kind, FILES_OF_A_KIND, (FILE, STATUS, DECISION))):
        if title not in each.sections or title not in each.tables:
            raise TemplateError("%s gives no section %s holding a table" % (where, title))
        for needed in columns:
            if needed not in each.tables[title]:
                raise TemplateError("the table of %s in %s has no column %s"
                                    % (title, where, needed))
    statuses = re.search(r"\*Status\*: one of (.*?);", " ".join(text.split()))
    form.of_a_kind.statuses = re.findall(r"`([^`]+)`", statuses.group(1)) if statuses else []
    for needed in STATUSES:
        if needed not in form.of_a_kind.statuses:
            raise TemplateError("%s gives no list of the values of *Status* holding %s"
                                % (where, needed))


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
        self.fences = fenced_blocks(self.lines)
        self.code = fenced_lines(self.lines, self.fences)
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


@dataclass
class Fence:
    opening: int       # the index of its opening line
    fence: str         # the run of backticks or tildes that opens it
    info: str          # the info string: what follows that run on the opening line
    closing: int       # the index of its closing line, None for a block left open to the end


def fenced_blocks(lines):
    """Every fenced block of the lines, in their order: opened by a fence of three or more
    backticks or tildes after at most three spaces — a run of backticks followed by no backtick
    — and closed by a line of the same character alone, at least as long, after at most three
    spaces."""
    blocks, current = [], None
    for index, line in enumerate(lines):
        if current is None:
            opening = OPEN_FENCE.match(line)
            if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                current = Fence(index, opening.group(1), opening.group(2), None)
                blocks.append(current)
            continue
        stripped = line.strip()
        if (len(line) - len(line.lstrip(" ")) <= 3 and len(stripped) >= len(current.fence)
                and set(stripped) == {current.fence[0]}):
            current.closing, current = index, None
    return blocks


def fenced_lines(lines, blocks):
    """For each line, whether it stands in one of the fenced blocks, its fences included."""
    flags = [False] * len(lines)
    for block in blocks:
        end = len(lines) - 1 if block.closing is None else block.closing
        flags[block.opening:end + 1] = [True] * (end + 1 - block.opening)
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
    bindings: dict = field(default_factory=dict)     # "ABC-01" -> the binding sentences of its
    #                                                  latest version, None for a repeal
    quoted: dict = field(default_factory=dict)       # "ABC-01" -> what its binding sentences
    #                                                  hold between two backticks, once asked

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

    def names_in_backticks(self, key, word):
        """Whether the binding sentences of a decision, their whitespace collapsed, hold
        `` `word` `` once its own whitespace is collapsed. For a word with no backtick that plain
        search of the text is the same as asking whether the word stands between two backticks
        with none between them, which is how it is asked: each decision's text is split on its
        backticks once, so a file naming many words costs no search of the log for each."""
        word = " ".join(word.split())
        text = " ".join((self.bindings.get(key) or "").split())
        if "`" in word:
            return "`%s`" % word in text
        if key not in self.quoted:
            self.quoted[key] = set(text.split("`")[1:-1])
        return word in self.quoted[key]


def decisions_named(value, foundation):
    """The decisions of the log a value names with a `@`, in their order."""
    return [key for key in (foundation.decision(match.group(1))
                            for match in REFERENCE_TOKEN.finditer(value)) if key]


def names_invariant(value, foundation):
    return any(foundation.invariant(match.group(1)) for match in REFERENCE_TOKEN.finditer(value))


def references(document, foundation):
    """(line, reference, kind, entry, its part after `@`) of every reference outside fenced code,
    in the two forms the sentence of `guidelines-reference-current` gives: a decision number
    of the log or an identifier of the invariants file followed by `@` and a run of letters and
    digits, or any identifier followed by `@` and eight lower-case hexadecimal characters."""
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
    # invariant: guidelines-reference-current
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
    bindings = {"%s-%02d" % (prefix, number): entry.binding
                for number, (entry, _) in latest.items()}
    return Foundation(prefix, decision_fingerprints(latest, prefix, borrowed),
                      invariant_fingerprints(entries, borrowed), withdrawn,
                      log_entries=log_entries, entries=entries, bindings=bindings)


def merged_foundation(top, onto, foundation, borrowed, invariant_rules, report):
    """What references name in the foundation a merge onto `onto` leaves, or None once the report
    says why git cannot read it: the decisions as the decisions guard merges the log, given a
    report of this script's own that is discarded but for the failures of git it holds; each
    invariant as on the branch where its sentence differs from the fork point, as on `onto`
    otherwise."""
    # invariant: guidelines-reference-current
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
    # invariant: guidelines-form
    check = "check_header"
    report.ran(check, FORM)
    fields = shared.parse_fields(document.prose(0, document.header_end), 1)
    check_order({name: fields[name][1] for name in fields}, form.header,
                lambda name: "the header line *%s*" % name, report, check)
    return fields


def check_sections(document, form, report, foundation):
    """The sections the template gives, in its order, each once; a dropped one holding only
    `none —` with a decision of the log."""
    # invariant: guidelines-form
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
    # invariant: guidelines-form
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


def invariants_named(value, foundation):
    """The invariants of the file a value names with a `@`, each once, in their order."""
    return list(dict.fromkeys(match.group(1) for match in REFERENCE_TOKEN.finditer(value)
                              if foundation.invariant(match.group(1))))


def case_of(block):
    """(kind, identifier, path) of a good, bad or prepared-base block opened by three backticks,
    its info words split by one space each; None for any other block."""
    if block.fence != CASE_FENCE:
        return None
    words = block.info.strip().split(" ")
    if (len(words) != 3 or words[0] not in (*CASE_KINDS, BASE_KIND)
            or not IDENTIFIER.fullmatch(words[1])
            or not words[2]):
        return None
    return tuple(words)


def check_cases(document, sections, report, shared, foundation):
    """In each rule kept under `## Rules` whose *Invariant* names an invariant other than
    `guidelines-form`, the test cases of WAY-168 (spec §5.2 item 5): after the rule's fields,
    exactly one good and one bad case of each such invariant, with at most one base block at the
    same path as both cases (WAY-223), and no other fenced block. A case is
    a block opened and closed by three backticks, not left open to the end of the file, whose info
    string — read from its opening fence alone — reads `good <identifier> <path>` or `bad
    <identifier> <path>` or `base <identifier> <path>`, the identifier one the rule names and the
    path relative and staying in
    the repository, and none of whose lines starts, after any leading whitespace, with three
    backticks or three tildes, on which `instruction-files/check_instructions.py` switches between
    code and text, a line being read as that script splits it. A rule naming `guidelines-form`
    alone gives no case: its cases are the-way's own tests of this script. No path of a case is
    opened or given to git. This form check does not authorize use of a prepared base: actual
    history and the empty protected set are checked during acceptance."""
    # invariant: guidelines-form
    check = "check_cases"
    report.ran(check, FORM)
    block = sections.get(RULES)
    if block is None:
        return
    rules = document.blocks("### ", block.start, block.end)
    starts = [rule.start for rule in rules]
    fences = {}     # the position of a rule -> the fenced blocks opening in its body
    for fence in document.fences:
        position = bisect.bisect_right(starts, fence.opening) - 1
        if position >= 0 and fence.opening < rules[position].end:
            fences.setdefault(position, []).append(fence)
    for position, rule in enumerate(rules):
        if is_dropped(document.text_lines(rule)):
            continue
        fields = shared.parse_fields(document.prose(rule.start, rule.end), rule.start + 1)
        named = invariants_named(fields[INVARIANT][0], foundation) if INVARIANT in fields else []
        required = [identifier for identifier in named if identifier != FORM_IDENTIFIER]
        rule_fences = fences.get(position, [])
        has_base = any(fence.info.split(maxsplit=1)[:1] == [BASE_KIND] for fence in rule_fences)
        if required or has_base:
            check_rule_cases(document, rule, fields, named, required, rule_fences, report, check)


def check_rule_cases(document, rule, fields, named, required, fences, report, check):
    """The test cases of one rule that needs them, `fences` being the fenced blocks opening in
    its body and `required` the invariants it names other than `guidelines-form`."""
    name = "`### %s`" % shown(rule.title)
    last_field = max((line for _, line in fields.values()), default=rule.line)
    seen = {}       # (kind, identifier) -> the line of its first block
    paths = {}      # (kind, identifier) -> the path of its first block
    for fence in fences:
        line = fence.opening + 1
        if fence.closing is None:
            report.error(line, "the fenced block opening here in the rule %s is left open to the "
                               "end of the file: no line of `%s` alone closes it"
                         % (name, shown(fence.fence)), check, (FORM,))
        case = case_of(fence)
        if case is None or line <= last_field:
            why = ("it stands before the rule's fields end" if line <= last_field
                   else "it opens with `%s`, not three backticks" % shown(fence.fence)
                   if fence.fence != CASE_FENCE
                   else "its info string reads `%s`" % shown(fence.info.strip()))
            report.error(line, "malformed test case: every fenced block of the rule %s, which "
                               "names an invariant other than `%s`, is a test case after the "
                               "rule's fields, opened by three backticks with the info string "
                               "`good <identifier> <path>`, `bad <identifier> <path>` or "
                               "`base <identifier> <path>`; %s"
                         % (name, FORM_IDENTIFIER, why), check, (FORM,))
            continue
        which, identifier, path = case
        if identifier in required:
            if (which, identifier) in seen:
                report.error(line, "a second `%s` case of the invariant `%s`, beside the one at "
                                   "line %d: a rule gives one good and one bad case and at most "
                                   "one base for each invariant it names" % (which, shown(identifier),
                                                 seen[(which, identifier)]), check, (FORM,))
            else:
                seen[(which, identifier)] = line
                paths[(which, identifier)] = path
        elif identifier in named:
            report.error(line, "the case names `%s`, whose cases are the-way's own tests of the "
                               "form check: a rule gives no case of it" % FORM_IDENTIFIER,
                         check, (FORM,))
        else:
            report.error(line, "the case names the invariant `%s`, which *%s* of the rule %s does "
                               "not name" % (shown(identifier), INVARIANT, name), check, (FORM,))
        why = refused(path)
        if why:
            report.error(line, "the path `%s` of the test case %s; the path of a test case is "
                               "relative to the root of the repository and stays in it"
                         % (shown(path), why), check, (FORM,))
        if (fence.closing is not None
                and document.lines[fence.closing].strip() != CASE_FENCE):
            report.error(fence.closing + 1, "the test case opened at line %d is closed by `%s`; "
                                            "the outer fence of a test case is three backticks"
                         % (line, shown(document.lines[fence.closing].strip())), check, (FORM,))
        end = len(document.lines) if fence.closing is None else fence.closing
        for index in range(fence.opening + 1, end):
            # `instruction-files/check_instructions.py` splits a file as `splitlines` does, at a
            # carriage return, a separator or a next-line character too, so a line is read in the
            # pieces that script reads.
            for piece in document.lines[index].splitlines():
                text = piece.lstrip()
                if text.startswith(INNER_FENCES):
                    report.error(index + 1, "the line inside the test case opened at line %d "
                                            "starts with `%s`, which opens a fence: the text of a "
                                            "test case holds no line that starts, after any "
                                            "leading whitespace, with three backticks or three "
                                            "tildes" % (line, text[:3]), check, (FORM,))
                    break
    at = fields[INVARIANT][1] if INVARIANT in fields else rule.line
    for identifier in required:
        for which in CASE_KINDS:
            if (which, identifier) not in seen:
                report.error(at, "the rule %s names the invariant `%s` in *%s* but gives no "
                                 "`%s %s <path>` case after its fields: a rule gives a good and "
                                 "a bad case of each invariant it names other than `%s`"
                             % (name, shown(identifier), INVARIANT, which, shown(identifier),
                                FORM_IDENTIFIER), check, (FORM,))
        base = (BASE_KIND, identifier)
        if base in paths:
            for which in CASE_KINDS:
                case = (which, identifier)
                if case in paths and paths[case] != paths[base]:
                    report.error(seen[case], "the `%s` case of `%s` has path `%s`, different "
                                 "from its base path `%s`: base, good and bad use the same path"
                                 % (which, shown(identifier), shown(paths[case]),
                                    shown(paths[base])), check, (FORM,))


def table_cells(line):
    """The cells of a row of a table: the text between its bars, a bar at either end set aside
    once, each cell stripped of the space around it. A bar in backticks splits a cell too, as
    Markdown reads a row."""
    text = line.strip()
    text = text[1:] if text.startswith("|") else text
    text = text[:-1] if text.endswith("|") else text
    return [cell.strip() for cell in text.split("|")]


def check_tables(document, sections, form, report):
    """Each table the template gives in a section the file keeps: a header holding its columns
    and, right under it, a separator row; no other separator row; every row with as many cells as
    the columns. Returns {section: [(line, {column: cell})]} of the tables whose header holds the
    columns, with each row whose number of cells is that of the columns."""
    # invariant: guidelines-form
    check = "check_tables"
    report.ran(check, FORM)
    tables = {}
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
        if len(table) == 1:
            report.error(header_line, "the table of `## %s` holds no separator row right under "
                                      "its header" % title, check, (FORM,))
        rows = []
        for position, (line, text) in enumerate(table[1:]):
            cells = table_cells(text)
            separator = all(SEPARATOR_CELL.match(cell) for cell in cells)
            if separator and position > 0:
                report.error(line, "a separator row stands among the rows of the table of "
                                   "`## %s`; it stands right under the header alone" % title,
                             check, (FORM,))
                continue
            if not separator and position == 0:
                report.error(line, "the table of `## %s` holds no separator row right under its "
                                   "header" % title, check, (FORM,))
            if len(cells) != len(columns):
                report.error(line, "the row holds %d cells; the table has %d columns"
                             % (len(cells), len(columns)), check, (FORM,))
                continue
            if not separator:
                rows.append((line, dict(zip(columns, cells))))
        tables[title] = rows
    return tables


def check_roles(tables, rules, form, report, foundation):
    """Each row of a table of roles: a *Kind* of the closed list, a background's *Text on it*
    naming a text role of the table, a decision; and each decision of the table named by the rule
    of each role's meaning, unless that rule is dropped."""
    # invariant: guidelines-form
    check = "check_roles"
    report.ran(check, FORM)
    for title in form.role_tables:
        rows = tables.get(title)
        if rows is None:
            continue
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
    # invariant: guidelines-form
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
    # A part in the name belongs to a discipline whose files stand one for each user interface,
    # the styleguide's; a kind in the name, to a discipline whose template gives a form of a kind,
    # the coding discipline's; every other discipline stands in `guidelines/<discipline>.md` alone
    # (WAY-167).
    rest = stem[len(discipline) + 1:] if stem.startswith(discipline + "-") else None
    if form.per_part:
        if rest:
            if parts is not None and rest not in parts:
                report.error(None, "the file's name names the part `%s`, which is no part of the "
                                   "map" % shown(rest), check, (FORM,))
            return
        given = "`guidelines/%s-<part>.md`"
    elif stem == discipline:
        return
    elif form.of_a_kind is not None:
        if rest is not None and IDENTIFIER.fullmatch(rest):
            return
        given = ("`guidelines/%s.md` or `guidelines/%s-<kind>.md`, `<kind>` being words of "
                 "lower-case letters and digits joined by single hyphens")
    else:
        given = "`guidelines/%s.md`"
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
    # invariant: guidelines-form
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


def kind_of(path):
    """The `<kind>` of a path `guidelines/coding-<kind>.md`, one level below `guidelines/`, or
    None for any other path."""
    head = "%s/%s-" % (GUIDELINES, CODING)
    if not path.startswith(head) or not is_guidelines_name(path[len(GUIDELINES) + 1:]):
        return None
    return path[len(head):-len(".md")]


def code_path(cell):
    """The path a cell of a table holds as one code span, `` `<path>` `` and nothing else, or
    None."""
    cell = cell.strip()
    if len(cell) > 2 and cell[0] == "`" and cell[-1] == "`" and cell.count("`") == 2:
        return cell[1:-1].strip() or None
    return None


def row_path(line, cell, report, check):
    """The path the *File* of a row names in backticks, once it is found to be relative and to
    stay in the repository; None, once the report says why, otherwise. The path is never given
    to git."""
    path = code_path(cell)
    if path is None:
        report.error(line, "*%s* holds `%s`, not one path in backticks" % (FILE, shown(cell)),
                     check, (FORM,))
        return None
    why = refused(path)
    if why:
        report.error(line, "the path `%s` of *%s* %s; a path of a table is relative to the root "
                           "of the repository and stays in it" % (shown(path), FILE, why),
                     check, (FORM,))
        return None
    return path


def check_exemplar(sections, tables, form, name, report, foundation, tracked):
    """The table of the files of a kind: exactly one row `exemplar`; every *Status* on the closed
    list; every *File* one path in backticks that stays in the repository and names a file git
    tracks; `—` in *Decision* on every row but the exemplar's, and on the exemplar's a decision
    of the log in force whose binding sentences, their whitespace collapsed, hold its *File* and
    the file's `<kind>`, each in backticks. A file of the kind the table leaves out is no error
    (C13)."""
    # invariant: guidelines-form
    check = "check_exemplar"
    report.ran(check, FORM)
    kind = kind_of("%s/%s" % (GUIDELINES, name))
    block = sections.get(FILES_OF_A_KIND)
    exemplar = None
    for line, row in tables.get(FILES_OF_A_KIND) or []:
        status = bare(row[STATUS])
        if status not in form.statuses:
            report.error(line, "the row's *%s* reads `%s`, which is none of %s"
                         % (STATUS, shown(status), ", ".join("`%s`" % each
                                                            for each in form.statuses)),
                         check, (FORM,))
        path = row_path(line, row[FILE], report, check)
        if path is not None:
            files, why = tracked()
            if files is None:   # `why` then holds why git could not list them
                report.error(line, "the path `%s` cannot be checked: %s" % (shown(path), why),
                             check, (FORM,))
            elif path not in files:
                report.error(line, "the path `%s` names no file git tracks" % shown(path),
                             check, (FORM,))
        if status != EXEMPLAR:
            if row[DECISION].strip() != NO_DECISION:
                report.error(line, "the row's *%s* is not `%s`, so its *%s* reads `%s`; it "
                                   "reads `%s`" % (STATUS, EXEMPLAR, DECISION, NO_DECISION,
                                                   shown(row[DECISION])), check, (FORM,))
            continue
        if exemplar is not None:
            report.error(line, "a second row whose *%s* is `%s`, beside the one at line %d: a "
                               "file of a kind names one exemplar" % (STATUS, EXEMPLAR, exemplar),
                         check, (FORM,))
        else:
            exemplar = line
        check_designation(line, row[DECISION], path, kind, report, check, foundation)
    if exemplar is None:
        report.error(block.line if block else None,
                     "the table under `## %s` holds no row whose *%s* is `%s`: a file of a kind "
                     "names its exemplar, with the decision that designates it"
                     % (FILES_OF_A_KIND, STATUS, EXEMPLAR), check, (FORM,))


def check_designation(line, cell, path, kind, report, check, foundation):
    """The *Decision* of an exemplar's row names a decision of the log in force whose binding
    sentences hold the row's path and the kind, each in backticks."""
    named = decisions_named(cell, foundation)
    if not named:
        report.error(line, "the exemplar's row names no decision of the log in *%s*, as "
                           "`<PREFIX-NN>@<fingerprint>`: the decision that designates the "
                           "exemplar" % DECISION, check, (FORM,))
        return
    if not foundation.known:
        return
    for key in named:
        value, why = foundation.current(TO_DECISION, key)
        if value is None:
            report.error(line, "the exemplar's row names %s, which is not in force: %s"
                         % (key, why), check, (FORM,))
            continue
        for word, what in ((path, "the row's *%s*" % FILE), (kind, "the kind of the file")):
            if word is not None and not foundation.names_in_backticks(key, word):
                report.error(line, "the binding sentences of %s do not name %s, `%s`, in "
                                   "backticks, so it does not designate the exemplar"
                             % (key, what, shown(word)), check, (FORM,))


def check_kind_index(general, reports, report, tracked):
    """Every file `guidelines/coding-<kind>.md` git lists is named by a row of the table under
    `## Kinds of code` of `guidelines/coding.md`, by its path in *File*, and git lists that
    general file; every row of the table names in *File* a file of a kind git lists, gives that
    file's `<kind>` in *Kind* and a condition in *When to read*. What git lists here is what it
    tracks, the one list it gives: a file written and not yet added names no kind, and a row
    naming it names no file. `general` is (its report, the rows of that table) where the general
    file is read, None otherwise; `reports` gives the report of each file of guidelines read,
    `report` the run's own."""
    # invariant: guidelines-form
    check = "check_kind_index"
    files, why = tracked()
    if files is None:   # `why` then holds why git could not list them
        report.error(None, "the table of `## %s` and the files of a kind cannot be checked: %s"
                     % (KINDS_OF_CODE, why), check, (FORM,))
        return
    kinds = {path: kind_of(path) for path in sorted(files) if kind_of(path) is not None}
    named = set()
    if general is not None:
        own, rows = general
        own.ran(check, FORM)
        for line, row in rows:
            if not row[WHEN_TO_READ].strip():
                own.error(line, "the row's *%s* is empty: it gives the condition under which an "
                                "agent reads the file" % WHEN_TO_READ, check, (FORM,))
            path = row_path(line, row[FILE], own, check)
            if path is None:
                continue
            kind = kind_of(path)
            if kind is None:
                own.error(line, "the path `%s` of *%s* names no file `%s/%s-<kind>.md`"
                          % (shown(path), FILE, GUIDELINES, CODING), check, (FORM,))
                continue
            if bare(row[KIND]) != kind:
                own.error(line, "the row's *%s* reads `%s`, but the file its *%s* names is of "
                                "the kind `%s`" % (KIND, shown(bare(row[KIND])), FILE,
                                                   shown(kind)), check, (FORM,))
            if path in kinds:
                named.add(path)
            else:
                own.error(line, "the path `%s` of *%s* names no file git tracks"
                          % (shown(path), FILE), check, (FORM,))
    for path in kinds:
        each = reports.get(path, report)
        each.ran(check, FORM)
        if GENERAL_CODING not in files:
            each.error(None, "git tracks no `%s`, whose table under `## %s` names each file of "
                             "a kind" % (GENERAL_CODING, KINDS_OF_CODE), check, (FORM,))
        elif general is None:
            each.error(None, "`%s` is not read, so no row of its table under `## %s` is found "
                             "naming this file" % (GENERAL_CODING, KINDS_OF_CODE), check, (FORM,))
        elif path not in named:
            each.error(None, "no row of the table under `## %s` in `%s` names this file by its "
                             "path in *%s*" % (KINDS_OF_CODE, GENERAL_CODING, FILE),
                       check, (FORM,))


def check_references(document, foundation, report):
    """Each reference outside fenced code carries eight lower-case hexadecimal characters after
    its `@`, names an entry in force and carries its current fingerprint on the commit checked.
    Returns the references found current there, as (line, reference, kind, entry, fingerprint),
    for the check after the merge."""
    # invariant: guidelines-reference-current
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
    # invariant: guidelines-reference-current
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
    named = context.disciplines.get(discipline, context.common)
    # A file `<discipline>-…` of a discipline whose template gives a form of a kind is held to
    # that form, its name checked apart.
    form = (named.of_a_kind if named.of_a_kind is not None
            and name[:-len(".md")].startswith("%s-" % discipline) else named)
    sections = check_sections(document, form, report, foundation)
    rules = check_rules(document, sections, form, report, shared, foundation)
    check_cases(document, sections, report, shared, foundation)
    tables = check_tables(document, sections, form, report)
    check_roles(tables, rules, form, report, foundation)
    if form.statuses:
        check_exemplar(sections, tables, form, name, report, foundation, context.tracked)
    check_parts(fields, name, discipline, named, context.disciplines, context.parts, report)
    check_paths(document, sections, context.tracked, report)
    if foundation.known:
        current = check_references(document, foundation, report)
        if context.merged is not None:
            check_merged_references(current, context.merged, context.onto, report)
    return tables


# --- the run --------------------------------------------------------------------------------


def list_guidelines(top, report, shared):
    """The names of the files `guidelines/<name>.md` git lists, tracked or not ignored; a warning
    for every other path it lists under `guidelines/`; None where `guidelines` is no directory."""
    # invariant: guidelines-form
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
    # invariant: guidelines-form
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
    # invariant: guidelines-reference-current
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
        by_path, general = {}, None
        for name in names:
            path = "%s/%s" % (GUIDELINES, name)
            report = shared.Report(shown(path), options, program=PROGRAM,
                                   selected_by=SELECTED_BY)
            reports.append(report)
            by_path[path] = report
            report.ran("read_guidelines", FORM)
            text, why = read_untrusted(top, path)
            if text is None:
                report.error(None, "`%s` %s" % (shown(path), why), "read_guidelines", (FORM,))
                report.fail(None, "`%s` %s, so its references cannot be checked"
                            % (shown(path), why), SAME_COMMIT, (REFERENCES,))
                continue
            tables = check_file(name, text, context, report)
            if path == GENERAL_CODING:
                general = (report, tables.get(KINDS_OF_CODE) or [])
        # The index of the files of a kind, where the-way gives the coding template and git
        # lists a file of that discipline under `guidelines/`: a file of a kind git tracks is
        # one it lists there, so a run that lists none needs no answer of git about it.
        if CODING in disciplines and any(path == GENERAL_CODING or kind_of(path) is not None
                                         for path in by_path):
            check_kind_index(general, by_path, reports[0], context.tracked)

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
