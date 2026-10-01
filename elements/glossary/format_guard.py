"""Format guard of a product's glossary.

Checks the file against the rules of template.md, which lies next to this script; each check cites
the invariants it gives a verdict for, as `invariant: <identifier>/<version>` (WAY-65). Read from
the templates, so that the rules of an entry live in one place (WAY-35, WAY-71): the fields of an
entry and the words each may hold, from the template's section "Entry"; the words a definition may
not hold, from its section "The definition" and from the decision template; and the values of the
closed lists a *Not* may name — the kinds of change, the results of a check and the values the gate
fills in — from the decision and invariants templates. A template that no longer says what the
guard reads stops the run. Written in this script and its tests alone: the names *Avoid* and *Not*,
the endings of a word's forms, what a use of a term leaves out and what the count of a word of
*Avoid* leaves out (WAY-97, WAY-98), and the file's path. The part map, the invariants and the
environment facts are read with the parsers of their own guards, and the record of a run is written
with the report the guards share.

The text the checks search is every file git tracks in `foundations/`, the elements' templates and
the Markdown files of the part the elements share, `elements/common/` (WAY-95, WAY-97, WAY-98,
WAY-99): those beside this script's directory, or those given to run(). A word is found in any
letter case, across a line break, and in the forms its endings give.

In the-way's own glossary, a term naming an element raises no warning against the part whose files
include `elements/<identifier>/` (WAY-93); in a product's glossary it does.

A product's glossary is known by the submodule `.the-way` at the root of its repository, whose
gitlink records the commit of the-way the product pins, as the installer adds it (WAY-34). In a
product's glossary, a term the glossary of the-way holds at that commit, in any of its forms, is an
error (WAY-95, WAY-104); the-way's glossary is read from the submodule's repository at that commit,
never from its working tree. The-way's own glossary is no product's glossary, and its terms are
compared with nothing; in a repository with no such gitlink, the comparison is reported unchecked.

Usage, from the root of the product's repository:

    python <the-way>/elements/glossary/format_guard.py [FILE] [--base REF] [--merge-onto REF]
        [--record PATH]
    python <the-way>/elements/glossary/format_guard.py [FILE] --uses WORD

FILE defaults to foundations/glossary.md. --base names the commit the task branch left the main
branch from; only with it is each word of *Avoid* counted against that commit, a term and an
identifier that came to read alike reported, and the uses of every term whose definition changed
listed (WAY-93, WAY-97, WAY-98). --merge-onto names the commit of the main branch a merge is made
onto; only with it are `TODO` in *Not* and a term with no use outside the glossary errors rather
than warnings, a term's uses then read as the merge leaves the files (WAY-71, WAY-95, WAY-99).
`none`, given to either option, is the value the gate fills in where that commit does not exist
(WAY-61): the checks that need the commit are then recorded as `unchecked`, the report names what
each leaves unchecked on `unchecked:` lines and counts them in its last line, and they give no
error; a commit that is not `none` and does not exist stays an error. --record names a
JSON Lines file, created or overwritten, which receives the-way's own record of the run (WAY-74):
a verdict for each invariant cited by a check the run's options select — the checks against the
base with --base, the checks of a merge with --merge-onto, the checks of the file alone with
neither — a line for each error of those checks that belongs to no cited invariant, and every
failure of the run itself. The report for a person holds every check. --uses lists the uses of a
word, with the definitions of the glossary's entries for other terms, and runs no check: the list
the skill reads before judging a word.
Exit code: 0 without errors, 1 with errors, 2 when the file or the template cannot be read or the
record cannot be written.
"""

import argparse
import glob
import importlib.util
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_FILE = os.path.join(HERE, "..", "..", "foundations", "glossary.md")
# The part the elements share, whose files the checks search as they search the templates (WAY-95).
COMMON = os.path.join(HERE, "..", "common")

sys.dont_write_bytecode = True


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


decision_guard = _load("decision_format_guard", os.path.join(HERE, "..", "decisions", "format_guard.py"))
map_guard = _load("part_map_format_guard", os.path.join(HERE, "..", "part-map", "format_guard.py"))
# The code the format guards share (WAY-09).
shared = _load("elements_common_guard_shared",
               os.path.join(HERE, "..", "common", "guard_shared.py"))
invariant_guard = _load("invariants_format_guard",
                        os.path.join(HERE, "..", "invariants", "format_guard.py"))
facts_guard = invariant_guard.facts_guard()
count_sentences = decision_guard.count_sentences
bare = invariant_guard.bare
flat = invariant_guard.flat
listed = invariant_guard.listed
is_todo = invariant_guard.is_todo
stray_lines = invariant_guard.stray_lines
FieldRule = invariant_guard.FieldRule
TODO_WORD = shared.TODO_WORD

# The name a record gives this program, and each of its checks as PROGRAM::<function>.
PROGRAM = "elements/glossary/format_guard.py"
# The checks each option selects for the record; every other check reads the file alone and is
# recorded only by a run given neither option (WAY-61, WAY-74).
SELECTED_BY = {"check_against_base": "--base", "check_merge_todo": "--merge-onto",
               "check_term_use": "--merge-onto"}
NO_COMMIT = shared.NO_COMMIT
NO_COMMIT_REASON = shared.NO_COMMIT_REASON
# Where a product's glossary stands, relative to the root of its repository (WAY-93).
FILE_PATH = "foundations/glossary.md"
# Where a product holds the-way, relative to the root of its repository: the submodule whose gitlink
# records the commit the product pins (WAY-34), at the path the installer gives it; the-way holds
# none.
PINNED = ".the-way"
GITLINK = "160000"
FOUNDATIONS = "foundations/"
# The two fields of an entry, which the checks of *Avoid* and *Not* read by name (WAY-94). *Avoid*
# marks a section of a Markdown file as a glossary entry (WAY-93).
AVOID, NOT = "Avoid", "Not"
MARK_FIELD = AVOID

# What a use of a term leaves out (WAY-97), and what the count of a word of *Avoid* leaves out
# besides (WAY-98): this code and its tests are the one place these are written. A span in backticks
# or quotation marks may run onto the next line, never across a blank one.
FENCE = re.compile(r"^(```|~~~)[^\n]*\n.*?(?:^\1[^\n]*$|\Z)", re.M | re.S)
BACKTICKS = re.compile(r"`(?:[^`\n]|\n(?![ \t]*\n))*`")
QUOTES = re.compile(r'"(?:[^"\n]|\n(?![ \t]*\n))*"|“(?:[^”\n]|\n(?![ \t]*\n))*”')
FIELD_LABEL = re.compile(r"^[ \t]*- \*\*([^*\n]+?):\*\*|^\*([^*\n]+?):\*", re.M)
FIELD_MENTION = re.compile(r"\*\*?([^*\n]+?)\*\*?")
# The fields whose values the uses leave out (WAY-97): their values are identifiers and kinds.
LEFT_OUT_VALUES = ("Scope", "Part", "Change")
LEFT_OUT_VALUE = re.compile(r"^[ \t]*- \*\*(?:%s):\*\*[^\n]*(?:\n[ \t]+\S[^\n]*)*"
                            % "|".join(LEFT_OUT_VALUES), re.M)
# A cell of a table row, and a heading's text: a field's name standing as either is no use.
TABLE_CELL = re.compile(r"(?m)(?<=\|)([ \t]*)([^|\n]+?)(?=[ \t]*\|)")
HEADING_TEXT = re.compile(r"(?m)^(#{1,6}[ \t]+)(.+)$")
# A field's value, its continuation lines included, and a token an identifier could be.
FIELD_VALUE = re.compile(r"(?m)^([ \t]*- \*\*[^*\n]+?:\*\*)([^\n]*(?:\n[ \t]+\S[^\n]*)*)")
IDENTIFIER_TOKEN = re.compile(r"(?<![\w-])[\w-]+(?![\w-])")
# A sentence ends where the decision guard counts the end of a binding sentence.
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[\"'(A-Z“])")
CONSONANT = re.compile(r"[b-df-hj-np-tv-z]$", re.I)
# A Markdown heading: one to six `#` followed by a space or the end of the line; `#tag` is text.
HEADING = re.compile(r"^#{1,6}(?:[ \t]|$)")


# A template, or the rules the elements share, does not hold a form this guard reads.
TemplateError = shared.TemplateError


# --- rules read from the template -----------------------------------------------------------


@dataclass
class Rules:
    fields: list             # FieldRule, in the order of the form
    must_words: list         # words "The definition" of the glossary template keeps out
    forbidden_words: list    # words the decision template keeps out of binding sentences
    keywords: list           # keywords of RFC 2119 in capitals, kept out likewise
    closed: set = field(default_factory=set)   # values of the closed lists a *Not* may name

    @property
    def names(self):
        return [rule.name for rule in self.fields]


# Reading a template's sections is code the guards share.
_section = shared.template_section
_blocks = shared.markdown_blocks


def read_rules(path=TEMPLATE):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    blocks = _blocks(_section(text, "Entry"))
    if not blocks:
        raise TemplateError('the section "Entry" does not hold the form of an entry')
    fields = []
    for name, form in re.findall(r"^- \*\*(.+?):\*\* (.*)$", blocks[0], re.M):
        choices = [bare(choice) for choice in form.split(" | ")]
        fields.append(FieldRule(name, "none" in choices, bool(re.search(r"\bTODO\b", form))))
    names = [rule.name for rule in fields]
    for name in (AVOID, NOT):
        # the checks of *Avoid* and *Not* read these fields by name; a template that renames one
        # stops the run rather than leaving its checks with nothing to read
        if name not in names:
            raise TemplateError("the entry form has no field *%s*" % name)
    definition = " ".join(_section(text, "The definition").split())
    words = re.search(r"The definition is one sentence.*? neither (.*?) nor (?:any )?word the "
                      r"decision template", definition)
    must_words = re.findall(r"\*(\w+)\*", words.group(1)) if words else []
    if not must_words:
        raise TemplateError('the section "The definition" names no words a definition may not '
                            'hold')
    decision_rules = decision_guard.read_rules()
    return Rules(fields, must_words, decision_rules.forbidden_words, decision_rules.keywords,
                 closed_lists(decision_rules))


def closed_lists(decision_rules):
    """The values of the closed lists a guard reads, which stay in their templates and take no
    glossary entry (WAY-95), as their templates write them: the kinds of change of a decision
    (WAY-20), the results of a check (WAY-63, WAY-74), the words `none` and `TODO` (WAY-71) and the
    values the gate fills in (WAY-61). This is the one place the lists are named; a *Not* names one
    of their values in backticks (WAY-99)."""
    invariant_rules = invariant_guard.read_rules()
    with open(invariant_guard.TEMPLATE, encoding="utf-8") as handle:
        results = " ".join(_section(handle.read(), "Result, report and debt").split())
    result = re.search(r"An entry's result on the commit being checked is (.*?)(?:\(WAY-|$)", results)
    values = re.findall(r"`([^`]+)`", result.group(1)) if result else []
    if not values or not decision_rules.kinds or not invariant_rules.gate_values:
        raise TemplateError("cannot read the closed lists a *Not* may name")
    return set(decision_rules.kinds) | set(values) | {"none", "TODO"} | \
        set(invariant_rules.gate_values)


# --- parsing the file -----------------------------------------------------------------------


@dataclass
class Entry:
    line: int
    term: str
    versioned: bool = False                       # the heading carries `/<number>`
    definition: str = None
    definition_line: int = None
    fields: dict = field(default_factory=dict)    # name -> [value, line]
    strays: list = field(default_factory=list)    # lines of text outside the definition and fields
    repeated: list = field(default_factory=list)  # (name, line) of a field written a second time
    text: str = ""


@dataclass
class Unknown:
    """A section `## <heading>` holding no field of an entry."""
    line: int
    heading: str


@dataclass
class Head:
    """The text above the first section: the title and the paragraph under it."""
    title_line: int = None       # line of `# <title>` where the file opens with one
    first_line: int = 1          # line of the first text of the file
    paragraphs: list = field(default_factory=list)   # first line of each paragraph after the title
    headings: list = field(default_factory=list)     # (line, heading) of every other heading


def other_headings(text):
    """(line, heading) of every heading outside a fenced block that is neither the title opening
    the file nor a section `## <term>`."""
    found, fenced, title_seen = [], False, False
    for number, line in enumerate(text.split("\n"), start=1):
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        elif fenced or not HEADING.match(line):
            if line.strip():
                title_seen = True
            continue
        elif line.startswith("## "):
            title_seen = True
        elif line.startswith("# ") and not title_seen:
            title_seen = True
        else:
            found.append((number, line.strip()))
    return found


def parse_file(text, rules):
    """(head, items): the text above the first section, and the entries and sections holding no
    field of an entry, in file order."""
    lines = text.split("\n")
    head = Head(headings=other_headings(text))
    first = next((index for index, line in enumerate(lines) if line.startswith("## ")), len(lines))
    opening = [(index + 1, line) for index, line in enumerate(lines[:first])]
    content = [(number, line) for number, line in opening if line.strip()]
    if content:
        head.first_line = content[0][0]
        if content[0][1].startswith("# "):
            head.title_line = content[0][0]
    previous_blank = True
    for number, line in opening:
        if number == head.title_line or HEADING.match(line):
            previous_blank = True
            continue
        if line.strip() and previous_blank:
            head.paragraphs.append(number)
        previous_blank = not line.strip()

    items = []
    field_line = re.compile(r"^- \*\*(%s):\*\*" % "|".join(re.escape(name) for name in rules.names))
    for line, section in shared.split_sections(text):
        heading = section[0][3:].strip()
        body = section[1:]
        if not any(field_line.match(row) for row in body):
            items.append(Unknown(line, heading))
            continue
        versioned = re.match(r"^(.+?)\s*/\s*\d+$", heading)
        entry = Entry(line, versioned.group(1) if versioned else heading, bool(versioned),
                      text="\n".join(section).rstrip())
        index = 0
        while index < len(body) and not body[index].strip():
            index += 1
        paragraph = []
        start = index
        while index < len(body) and body[index].strip() and not body[index].startswith("- **"):
            paragraph.append(body[index])
            index += 1
        if paragraph:
            entry.definition = "\n".join(paragraph)
            entry.definition_line = line + 1 + start
        entry.fields = shared.parse_fields(body[index:], line + 1 + index)
        entry.strays = stray_lines(body[index:], line + 1 + index)
        # the shared parser keeps the first of two fields of one name and drops the second
        seen = set()
        for offset, row in enumerate(body[index:], start=line + 1 + index):
            label = re.match(r"^- \*\*(.+?):\*\*", row)
            if label and label.group(1) in seen:
                entry.repeated.append((label.group(1), offset))
            elif label:
                seen.add(label.group(1))
        items.append(entry)
    return head, items


def entries_of(items):
    return [item for item in items if isinstance(item, Entry)]


def value_of(entry, name):
    return entry.fields.get(name, ["", entry.line])


def pairs(value):
    """(word, what follows ` — `) for each item a field lists as `<word> — <text> · …`; `none` lists
    none. The text is None for an item with no ` — `."""
    value = flat(value or "")
    if not value or bare(value) == "none":
        return []
    found = []
    for item in listed(value):
        word, dash, rest = item.partition(" — ")
        found.append((word.strip(), rest.strip() if dash else None))
    return found


def terms_of(text, rules):
    """term -> definition, flattened, of every entry of a glossary text; None for no text."""
    if text is None:
        return {}
    _, items = parse_file(text, rules)
    found = {}
    for entry in entries_of(items):
        found.setdefault(entry.term.lower(), flat(entry.definition or ""))
    return found


# --- words and their forms ------------------------------------------------------------------


def last_word_forms(word):
    """A word and the forms the endings give it: `-s`, `-es`, `-ies` in place of a final `y`, `-'s`,
    `-d`, `-ed` and `-ing`, a final consonant doubled before the last two. This code and its tests
    are the one place the endings are written; a form they miss is found by the review of uses
    (WAY-97)."""
    forms = {word, word + "s", word + "es", word + "'s", word + "’s", word + "d", word + "ed",
             word + "ing"}
    if word.lower().endswith("y"):
        forms.add(word[:-1] + "ies")
    if CONSONANT.search(word):
        forms |= {word + word[-1] + "ed", word + word[-1] + "ing"}
    return forms


def forms_of(term):
    """Every form of a term, in lower case, its ending on its last word."""
    words = term.split()
    if not words:
        return set()
    return {" ".join(words[:-1] + [form]).lower() for form in last_word_forms(words[-1])}


def same_word(first, second):
    """Whether two words are one: either, its hyphens read as spaces, is the other in one of its
    forms, in any letter case."""
    first, second = first.replace("-", " "), second.replace("-", " ")
    return second.lower() in forms_of(first) or first.lower() in forms_of(second)


def word_pattern(term, edges):
    """A pattern finding a term in any of its forms, in any letter case, its words split by any
    white space, a line break included, and not touching any character of `edges`."""
    words = term.split()
    if not words:
        return None
    forms = sorted(last_word_forms(words[-1]), key=len, reverse=True)
    body = "".join(re.escape(word) + r"\s+" for word in words[:-1])
    body += "(?:%s)" % "|".join(re.escape(form) for form in forms)
    return re.compile(r"(?<![\w%s])%s(?![\w%s])" % (edges, body, edges), re.I)


def use_pattern(term):
    # a token holding `/` or a hyphen the term does not hold is no use (WAY-97)
    return word_pattern(term, "/-")


def blank(text, pattern):
    """The text with every match of the pattern replaced by spaces, its line breaks kept, so that
    positions and line numbers stay where they were."""
    return pattern.sub(lambda match: re.sub(r"[^\n]", " ", match.group(0)), text)


def line_at(text, offset):
    return text.count("\n", 0, offset) + 1


def field_names(texts):
    """Every name a field carries in the texts: `- **<name>:**` and `*<name>:*` at a line's start."""
    names = set()
    for text in texts:
        for bold, prose in FIELD_LABEL.findall(text):
            names.add(bold or prose)
    return names


def use_text(text, names):
    """The text a term's uses are searched in: text in backticks or a fenced block, a field's name
    and the values of *Scope*, *Part* and *Change* left out (WAY-97)."""
    text = blank(text, FENCE)
    text = blank(text, BACKTICKS)
    text = blank(text, LEFT_OUT_VALUE)
    text = blank(text, FIELD_LABEL)
    text = FIELD_MENTION.sub(lambda match: spaces(match.group(0))
                             if match.group(1).rstrip(":") in names else match.group(0), text)
    text = TABLE_CELL.sub(lambda match: match.group(1) + spaces(match.group(2))
                          if re.sub(r"\s*\(.*\)$", "", match.group(2).strip()) in names
                          else match.group(0), text)
    return HEADING_TEXT.sub(lambda match: match.group(1) + spaces(match.group(2))
                            if match.group(2).strip() in names else match.group(0), text)


def spaces(text):
    return re.sub(r"[^\n]", " ", text)


def longer_terms(term, terms):
    """The terms that hold the term, in one of its forms, among their words."""
    pattern = use_pattern(term)
    return [other for other in terms if other.lower() != term.lower() and pattern.search(other)]


def find_uses(term, searched, terms):
    """(offset, matched text) of every use of the term in a searched text, the span of a longer
    term of the glossary that holds it left out."""
    found = [(match.start(), match.end(), match.group(0))
             for match in use_pattern(term).finditer(searched)]
    if not found:
        return []
    spans = [(match.start(), match.end()) for other in longer_terms(term, terms)
             for match in use_pattern(other).finditer(searched)]
    return [(start, text) for start, end, text in found
            if not any(left <= start and end <= right for left, right in spans)]


# --- the text the checks search -------------------------------------------------------------


@dataclass
class Text:
    name: str            # the path relative to the repository's root, or the template's name
    text: str
    in_repo: bool        # whether git holds it, so that it can be read on another commit
    glossary: bool = False


def template_paths(templates=None):
    if templates is not None:
        return list(templates)
    return sorted(glob.glob(os.path.join(HERE, "..", "*", "template.md")))


def common_paths(common=None):
    """The Markdown files git tracks in the part the elements share, standing directly in its
    directory: the one given, or `elements/common/` beside this script's directory (WAY-95, WAY-98,
    WAY-99); none for `False`. Where the directory lies in no repository git can read, the files
    on disk stand in their place. Its code is not searched: the rules of a use and of a count are
    written for prose."""
    if common is False:
        return []
    directory = COMMON if common is None else common
    if not os.path.isdir(directory):
        return []
    code, listing = shared.git(["ls-files", "-z", "--", "."], directory)
    if code == 0:
        names = [name for name in listing.split("\0") if name and "/" not in name]
    else:
        names = [name for name in os.listdir(directory)
                 if os.path.isfile(os.path.join(directory, name))]
    return sorted(os.path.join(directory, name) for name in names
                  if name.lower().endswith((".md", ".markdown")))


def inside(path, top):
    if top is None:
        return False
    path, top = os.path.normcase(os.path.abspath(path)), os.path.normcase(os.path.abspath(top))
    return os.path.commonpath([path, top]) == top


def relative(path, top):
    return os.path.relpath(os.path.abspath(path), top).replace(os.sep, "/")


def read_corpus(path, top, tracked, report, templates=None, common=None):
    """Every file git tracks in `foundations/` at the root of the repository, the glossary itself
    marked, the elements' templates and the files of the part the elements share (WAY-95, WAY-97,
    WAY-98, WAY-99). Without git, the files of the directory the glossary stands in, on disk, in
    place of `foundations/`."""
    directory = os.path.dirname(os.path.abspath(path))
    texts, names = [], []
    if top is not None and tracked is not None:
        names = [(name, os.path.join(top, *name.split("/"))) for name in tracked
                 if name.startswith(FOUNDATIONS)]
    else:
        names = [(name, os.path.join(directory, name)) for name in sorted(os.listdir(directory))
                 if os.path.isfile(os.path.join(directory, name))]
    for name, full in names:
        try:
            with open(full, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as problem:
            report.cannot_check("the words of %s" % name, "it cannot be read as UTF-8 text: %s"
                                % problem)
            continue
        own = os.path.exists(full) and os.path.exists(path) and os.path.samefile(full, path)
        texts.append(Text(name, text, top is not None and tracked is not None, own))
    for template in template_paths(templates):
        try:
            with open(template, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as problem:
            report.error(None, "cannot read the template %s: %s" % (template, problem))
            continue
        if inside(template, top):
            texts.append(Text(relative(template, top), text, tracked is not None))
        else:
            name = "elements/%s/template.md" % os.path.basename(os.path.dirname(template))
            texts.append(Text(name, text, False))
    for shared_file in common_paths(common):
        try:
            with open(shared_file, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as problem:
            report.error(None, "cannot read %s of the part the elements share: %s"
                         % (shared_file, problem))
            continue
        if inside(shared_file, top):
            texts.append(Text(relative(shared_file, top), text, tracked is not None))
        else:
            texts.append(Text("elements/common/%s" % os.path.basename(shared_file), text, False))
    return texts


# --- what the checks read beside the glossary -----------------------------------------------


@dataclass
class Foundation:
    """The identifiers of the part map, the invariants and the environment facts."""
    entries: set = field(default_factory=set)      # identifiers of entries
    withdrawn: set = field(default_factory=set)    # withdrawn identifiers
    parts: dict = field(default_factory=dict)      # identifier of a part -> its path patterns


def foundation_of(map_text, invariants_text, facts_text):
    """The identifiers the three files hold; a file given as None holds none."""
    foundation = Foundation()
    if map_text is not None:
        map_rules = map_guard.read_rules()
        entries, sections = map_guard.parse_map(map_text, map_rules)
        columns = map_rules.lists.get("Withdrawn identifiers")
        for entry in entries:
            foundation.entries.add(entry.identifier)
            foundation.parts[entry.identifier] = list(map_guard.patterns(entry))
        foundation.withdrawn |= {cells[0] for cells, _ in
                                 map_guard.rows(sections, "Withdrawn identifiers")
                                 if cells and cells != columns and cells[0]}
    if invariants_text is not None:
        invariant_rules = invariant_guard.read_rules()
        for item in invariant_guard.parse_file(invariants_text, invariant_rules):
            if isinstance(item, invariant_guard.Entry):
                foundation.entries.add(item.identifier)
            elif isinstance(item, invariant_guard.Table) and \
                    item.title == invariant_rules.lists[0][0]:
                foundation.withdrawn |= {cells[0] for cells, _ in item.rows if cells and cells[0]}
    if facts_text is not None:
        facts = facts_guard.facts_of(facts_text, facts_guard.read_rules())
        foundation.entries |= set(facts.entries)
        foundation.withdrawn |= set(facts.withdrawn)
    return foundation


BESIDE = ("part_map.md", "invariants.md", "environment_facts.md")


def foundations_directory(path, top):
    """`foundations/` at the root of the repository, where the part map, the invariants and the
    environment facts stand wherever the glossary does; without git, the glossary's directory."""
    if top is None:
        return os.path.dirname(os.path.abspath(path))
    return os.path.join(top, *FOUNDATIONS.strip("/").split("/"))


def read_foundation(path, top, report):
    directory = foundations_directory(path, top)
    texts = []
    for name in BESIDE:
        full = os.path.join(directory, name)
        if not os.path.exists(full):
            report.notes.append("there is no %s beside the file: it holds no identifier" % name)
            texts.append(None)
            continue
        texts.append(shared.read_file(full, report, "%s beside the file" % name))
    try:
        return foundation_of(*texts)
    except (TemplateError, AttributeError, IndexError) as problem:
        report.error(None, "cannot read the identifiers beside the file: %s" % problem)
        return Foundation()


# --- the report and the record of a run -----------------------------------------------------


class Report(shared.Report):
    """The report the guards share, naming this program and its checks in the record."""

    def __init__(self, path, options=()):
        super().__init__(path, options, program=PROGRAM, selected_by=SELECTED_BY)


start_record = shared.start_record
write_record = shared.write_record


# --- checks of the file's shape -------------------------------------------------------------


def check_layout(head, items, report):
    """The file holds a title, the paragraph under it and its entries, and no other heading
    (WAY-93)."""
    # invariant: glossary-file-sections/1
    check, sections = "check_layout", "glossary-file-sections/1"
    report.ran(check, sections)
    if head.title_line is None:
        report.error(head.first_line, "the file opens with no title `# <title>`", check, (sections,))
    elif len(head.paragraphs) != 1:
        report.error(head.title_line, "%d paragraphs under the title; the file holds one, saying "
                                      "what it holds" % len(head.paragraphs), check, (sections,))
    for line, heading in head.headings:
        report.error(line, "heading `%s` is neither the file's title nor an entry's `## <term>`"
                     % heading, check, (sections,))
    for item in items:
        if isinstance(item, Unknown):
            report.error(item.line, "section `## %s` holds no field of an entry; the file holds a "
                                    "title, its paragraph and entries" % item.heading,
                         check, (sections,))


def holds_entries(text):
    """Whether a Markdown text holds a glossary entry: a section `## <term>`, outside a fenced
    block, carrying an *Avoid* field."""
    heading, fenced = False, False
    for line in text.split("\n"):
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        elif fenced:
            continue
        elif HEADING.match(line):
            heading = line.startswith("## ")
        elif heading and line.startswith("- **%s:**" % MARK_FIELD):
            return True
    return False


def check_file(path, top, tracked, report):
    """The repository holds one file of glossary entries, at foundations/glossary.md (WAY-93). The
    path is compared, letter case included, as git lists it. Another such file is known by its
    content (holds_entries)."""
    # invariant: glossary-file/1
    check, one_file = "check_file", "glossary-file/1"
    if top is None or tracked is None:
        if os.path.basename(path) != "glossary.md" or \
                os.path.basename(os.path.dirname(os.path.abspath(path))) != "foundations":
            report.error(None, "a product's glossary stands in %s" % FILE_PATH, check, (one_file,))
        return
    report.ran(check, one_file)
    given = relative(path, top)
    listed_as = [name for name in tracked if name.lower() == given.lower()]
    if listed_as:
        given = listed_as[0]
    if given != FILE_PATH:
        report.error(None, "a product's glossary stands in %s, not in %s" % (FILE_PATH, given),
                     check, (one_file,))
    for name in tracked:
        if name == given or not name.lower().endswith((".md", ".markdown")):
            continue
        full = os.path.join(top, *name.split("/"))
        try:
            with open(full, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as problem:
            report.cannot_check("whether %s holds glossary entries" % name,
                                "it cannot be read as UTF-8 text: %s" % problem)
            continue
        if holds_entries(text):
            report.error(None, "`%s` is a second file of glossary entries; the repository holds "
                               "one, %s" % (name, FILE_PATH), check, (one_file,))


def check_terms(entries, report):
    """No term heads two entries (WAY-93), and no heading carries a version (WAY-97)."""
    # invariant: glossary-term-holder/1
    # invariant: glossary-entry-version/1
    check = "check_terms"
    holder, version = "glossary-term-holder/1", "glossary-entry-version/1"
    report.ran(check, holder, version)
    seen = {}
    for entry in entries:
        if entry.versioned:
            report.error(entry.line, "`## %s` carries a version; a glossary entry has none and is "
                                     "edited in place" % entry.text.split("\n")[0][3:].strip(),
                         check, (version,))
        if not entry.term:
            report.error(entry.line, "the heading names no term", check)
            continue
        other = next((term for term in seen if same_word(term, entry.term)), None)
        if other is not None:
            report.error(entry.line, "term `%s` heads two entries (`%s`, line %d)"
                         % (entry.term, other, seen[other]), check, (holder,))
        seen.setdefault(entry.term, entry.line)


def check_fields(entries, rules, report):
    """Every field of the form is present, and holds `none` or `TODO` only where the form gives it
    that word; no entry carries a field the form does not hold (WAY-71, WAY-94). `TODO` in *Not*
    stands only in place of what carries a meaning, which check_not reads."""
    # invariant: glossary-entry-field-presence/1
    # invariant: glossary-entry-field-words/1
    # invariant: glossary-entry-version/1
    check = "check_fields"
    presence, words, version = ("glossary-entry-field-presence/1", "glossary-entry-field-words/1",
                                "glossary-entry-version/1")
    report.ran(check, presence, words, version)
    for entry in entries:
        for name, line in entry.repeated:
            report.error(line, "%s: field *%s* is written a second time; an entry carries each field "
                               "once" % (entry.term, name), check)
        for line in entry.strays:
            report.error(line, "%s: text outside the definition and the fields" % entry.term, check)
        for name, (value, line) in entry.fields.items():
            if name not in rules.names:
                report.error(line, "%s: field *%s* is not in the template" % (entry.term, name),
                             check, (version,) if name.lower() == "version" else ())
        if entry.definition is not None and (bare(flat(entry.definition)) == "none"
                                             or TODO_WORD.search(entry.definition)):
            report.error(entry.definition_line, "%s: the definition holds `%s`, which the form does "
                                                "not give it" % (entry.term, "none" if bare(
                                                    flat(entry.definition)) == "none" else "TODO"),
                         check, (words,))
        for rule in rules.fields:
            if rule.name not in entry.fields or not entry.fields[rule.name][0].strip():
                report.error(entry.line, "%s: field *%s* is missing" % (entry.term, rule.name),
                             check, (presence,))
                continue
            value, line = entry.fields[rule.name]
            if bare(flat(value)) == "none" and not rule.none:
                report.error(line, "%s: *%s* may not hold `none`" % (entry.term, rule.name),
                             check, (words,))
            if TODO_WORD.search(value) and not rule.todo:
                report.error(line, "%s: *%s* may not hold `TODO`" % (entry.term, rule.name),
                             check, (words,))
            elif rule.todo and is_todo(flat(value)):
                report.error(line, "%s: *%s* reads `TODO` whole; `TODO` stands only in place of what "
                                   "carries a meaning, as `<meaning> — TODO`" % (entry.term, rule.name),
                             check, (words,))


# Contractions of a word kept out of a definition that are not the word followed by `n't`.
CONTRACTED = {"will": ["wo"], "shall": ["sha"]}


def check_definitions(entries, rules, report):
    """Every definition is one sentence, counted as the decision guard counts binding sentences,
    with no text outside it and the fields; outside backticks it holds no word the template or the
    decision template keeps out (WAY-96)."""
    # invariant: glossary-definition-count/1
    # invariant: glossary-definition-words/1
    check = "check_definitions"
    count, words = "glossary-definition-count/1", "glossary-definition-words/1"
    report.ran(check, count, words)
    for entry in entries:
        if entry.definition is None:
            report.error(entry.line, "%s: the definition is missing" % entry.term, check, (count,))
        else:
            sentences = count_sentences(entry.definition)
            if sentences != 1:
                report.error(entry.definition_line, "%s: the definition is %d sentences, not one"
                             % (entry.term, sentences), check, (count,))
            plain = re.sub(r"`[^`]*`", " ", entry.definition)
            for word in rules.must_words + rules.forbidden_words:
                forms = [word] + CONTRACTED.get(word.lower(), [])
                if re.search(r"\b(?:%s)(?:n['’]t)?\b" % "|".join(re.escape(form) for form in forms),
                             plain, re.I):
                    report.error(entry.definition_line, "%s: the definition holds *%s*"
                                 % (entry.term, word), check, (words,))
            for keyword in rules.keywords:
                if re.search(r"\b%s\b" % re.escape(keyword), plain):
                    report.error(entry.definition_line, "%s: the definition holds %s"
                                 % (entry.term, keyword), check, (words,))


# Marks a word of *Avoid* is written without: backticks, quotation marks, emphasis.
MARKS = r'[`"“”*]'


def check_avoid(entries, report):
    """No word stands in the *Avoid* of two entries, and no word of an *Avoid* is a term or a word a
    *Not* names (WAY-98); every word there gives what a reader takes it for (WAY-94)."""
    # invariant: glossary-avoid-single/1
    # invariant: glossary-avoid-term/1
    # invariant: glossary-avoid-carrier/1
    check = "check_avoid"
    single, not_term, carrier = ("glossary-avoid-single/1", "glossary-avoid-term/1",
                                 "glossary-avoid-carrier/1")
    report.ran(check, single, not_term, carrier)
    terms = [entry.term for entry in entries if entry.term]
    carriers = [(other.term, what) for other in entries
                for _, named in pairs(value_of(other, NOT)[0]) if named
                for kind, what in [carrier_of(named)] if kind in ("code", "quoted")]
    seen = []    # (word, term of the entry whose *Avoid* lists it)
    for entry in entries:
        value, line = value_of(entry, AVOID)
        for word, reason in pairs(value):
            if reason is None or not reason:
                report.error(line, "%s: *Avoid* lists `%s` without what a reader takes it for, as "
                                   "`<word> — <what>`" % (entry.term, word), check)
            if re.search(MARKS, word):
                report.error(line, "%s: *Avoid* lists %s with marks around it; the form writes the "
                                   "word plain" % (entry.term, word), check)
            word = re.sub(MARKS, "", word).strip()
            if not word:
                continue
            term = next((term for term in terms if same_word(term, word)), None)
            if term is not None:
                report.error(line, "%s: *Avoid* lists `%s`, which is the term `%s`"
                             % (entry.term, word, term), check, (not_term,))
            for holder, named in carriers:
                if same_word(named, word):
                    report.error(line, "%s: *Avoid* lists `%s`, which the *Not* of `%s` names as "
                                       "the word for another meaning" % (entry.term, word, holder),
                                 check, (carrier,))
            for other, holder in seen:
                if holder != entry.term and same_word(other, word):
                    report.error(line, "%s: *Avoid* lists `%s`, which the *Avoid* of `%s` lists too"
                                 % (entry.term, word, holder), check, (single,))
            seen.append((word, entry.term))


def used_outside(word, corpus):
    """Whether the text searched uses a word, as a use is found, outside quotation marks and outside
    the glossary (WAY-98, WAY-99)."""
    pattern = use_pattern(word)
    if pattern is None:
        return False
    _, texts = prepared(corpus)
    return any(pattern.search(blank(searched, QUOTES)) for _, searched, _ in texts)


def holds_term(term, text):
    """Whether a text holds the term or one of its forms, the hyphens of both read as spaces
    (WAY-99)."""
    pattern = use_pattern(term.replace("-", " "))
    return bool(pattern and pattern.search(text.replace("-", " ")))


def carrier_of(text):
    """(kind, what) of what a *Not* says carries a meaning: `todo`, `code` for a text in backticks,
    `quoted` for a word between quotation marks, and `term` for anything else."""
    text = text.strip()
    if is_todo(text):
        return "todo", "TODO"
    if len(text) > 1 and text.startswith("`") and text.endswith("`") and text.count("`") == 2:
        return "code", text[1:-1]
    quoted = re.fullmatch(r'"([^"]+)"|“([^”]+)”', text)
    if quoted:
        return "quoted", quoted.group(1) or quoted.group(2)
    return "term", text


def check_not(entries, rules, foundation, corpus, report, warn_todo=True):
    """Everything *Not* names in backticks, and every term it names, exists; nothing it names
    holds the term or its forms; every word it names between quotation marks stands outside
    quotation marks and outside the glossary (WAY-99). A `TODO` in place of what carries a meaning
    is a warning; a merge onto the main branch fails on it, in check_merge_todo."""
    # invariant: glossary-not-target/1
    # invariant: glossary-not-quoted-word/1
    # invariant: glossary-entry-field-words/1
    check = "check_not"
    target, quoted_word, words = ("glossary-not-target/1", "glossary-not-quoted-word/1",
                                  "glossary-entry-field-words/1")
    report.ran(check, target, quoted_word, words)
    terms = {entry.term.lower() for entry in entries}
    for entry in entries:
        value, line = value_of(entry, NOT)
        if is_todo(flat(value)):
            continue  # check_fields reports it
        for meaning, carrier in pairs(value):
            if carrier is None or not carrier:
                report.error(line, "%s: *Not* gives `%s` without what carries it, as `<meaning> — "
                                   "<what carries it>`" % (entry.term, meaning), check)
                continue
            if TODO_WORD.search(meaning):
                report.error(line, "%s: *Not* reads `TODO` in place of a meaning; `TODO` stands only "
                                   "in place of what carries one" % entry.term, check, (words,))
            kind, what = carrier_of(carrier)
            if kind == "todo":
                if warn_todo:
                    report.warning(line, "%s: *Not* reads `TODO` in place of what carries \"%s\"; a "
                                         "merge onto the main branch fails on it"
                                   % (entry.term, meaning))
                continue
            if entry.term and holds_term(entry.term, what):
                report.error(line, "%s: *Not* names %s, which holds the term" % (entry.term, carrier),
                             check, (quoted_word,))
            if kind == "code":
                if what not in foundation.entries and what not in rules.closed:
                    report.error(line, "%s: *Not* names `%s`, which is neither the identifier of an "
                                       "entry of the part map, the invariants or the environment "
                                       "facts nor a value of a closed list of a template"
                                 % (entry.term, what),
                                 check, (target,))
            elif kind == "quoted":
                if not used_outside(what, corpus):
                    report.error(line, "%s: *Not* names \"%s\", which the foundation does not use "
                                       "outside quotation marks and outside the glossary"
                                 % (entry.term, what), check, (quoted_word,))
            elif what.lower() not in terms:
                report.error(line, "%s: *Not* names `%s`, which is no term of the glossary; a word "
                                   "that is not a term stands between quotation marks"
                             % (entry.term, what), check, (target,))


# --- the words of the process ---------------------------------------------------------------


def pinned_commit(top):
    """(the commit of the-way the repository pins, None): the gitlink `.the-way` at the root of the
    repository, as the index holds it; (None, None) where the repository holds no such gitlink, so
    that its glossary is no product's; (None, why) where git fails or the gitlink is unmerged."""
    code, listing, message = shared.call_git(["ls-files", "--stage", "-z", "--", PINNED], top)
    if code != 0:
        return None, "git cannot list %s: %s" % (PINNED, message or "git ls-files exited with %d"
                                                  % code)
    stages = {}
    for item in listing.split("\0"):
        info, _, name = item.partition("\t")
        fields = info.split()
        if name == PINNED and len(fields) == 3 and fields[0] == GITLINK:
            stages[fields[2]] = fields[1]
    if "0" in stages:
        return stages["0"], None
    if stages:
        return None, ("the gitlink %s is unmerged, so the commit the product pins is not known; "
                      "settle the pin and run the guard again" % PINNED)
    return None, None


def check_process_terms(entries, rules, top, own, report):
    """In a product's glossary, no term is, in any of its forms, a term the glossary of the-way
    holds at the commit the product pins (WAY-95, WAY-104). The-way's own glossary is no product's,
    and the check does not run on it; on a glossary in a repository holding no gitlink `.the-way`,
    or pinning a commit of the-way that holds no glossary, it does not run either, and the report
    says it is unchecked."""
    # invariant: glossary-process-terms/1
    check, process = "check_process_terms", "glossary-process-terms/1"
    what = "whether the glossary defines a word the glossary of the-way holds"
    if own:
        report.notes.append("the-way's own glossary is no product's: its terms are not compared "
                            "with the glossary of the-way")
        return
    if top is None:
        report.cannot_check(what, "the file is in no git repository, so no commit of the-way it "
                                  "pins can be read")
        return
    commit, failure = pinned_commit(top)
    if failure:
        report.error(None, failure)
        return
    if commit is None:
        report.cannot_check(what, "the repository holds no gitlink %s at its root, so it pins no "
                                  "commit of the-way" % PINNED)
        return
    checkout = os.path.join(top, PINNED)
    if not os.path.exists(os.path.join(checkout, ".git")):
        report.error(None, "the submodule %s is not initialized, so the glossary of the-way at %s "
                           "cannot be read; run `git submodule update --init -- %s`"
                     % (PINNED, commit, PINNED))
        return
    code, _, _ = shared.call_git(["cat-file", "-e", commit + "^{commit}"], checkout)
    if code != 0:
        report.error(None, "the submodule %s does not hold %s, the commit the product pins; run "
                           "`git submodule update --init -- %s`" % (PINNED, commit, PINNED))
        return
    text, failure = shared.file_at(commit, FILE_PATH, checkout)
    if failure:
        report.error(None, failure)
        return
    if text is None:
        report.cannot_check(what, "the-way at %s, the commit the product pins, holds no %s to "
                                  "compare the terms with" % (commit, FILE_PATH))
        return
    report.ran(check, process)
    held = list(terms_of(text, rules))
    for entry in entries:
        if not entry.term:
            continue
        term = next((word for word in held if same_word(word, entry.term)), None)
        if term is not None:
            report.error(entry.line, "%s: the glossary of the-way holds `%s` at %s, the commit the "
                                     "product pins; a word of the product's domain that it holds "
                                     "is written with a qualifier, and the bare word keeps the "
                                     "meaning of the process (WAY-104)" % (entry.term, term, commit),
                         check, (process,))


# --- uses of a term -------------------------------------------------------------------------


@dataclass
class Use:
    name: str
    line: int
    text: str           # the line the use starts on


_prepared = {}


def prepared(corpus):
    """(field names, [(text, the text searched for uses, its lines)] outside the glossary) of a
    corpus, computed once for each corpus a run reads."""
    key = id(corpus)
    if key not in _prepared or _prepared[key][0] is not corpus:
        names = field_names(text.text for text in corpus)
        _prepared[key] = (corpus, names, [(text, use_text(text.text, names), text.text.split("\n"))
                                          for text in corpus if not text.glossary])
    return _prepared[key][1], _prepared[key][2]


def uses_of(term, corpus, entries, with_definitions):
    """Every use of a term outside the glossary, in file order; with_definitions adds its uses in
    the definitions of the glossary's other entries (WAY-97)."""
    names, texts = prepared(corpus)
    terms = [entry.term for entry in entries if entry.term]
    found = []
    for text, searched, lines in texts:
        for offset, _ in find_uses(term, searched, terms):
            number = line_at(searched, offset)
            found.append(Use(text.name, number, lines[number - 1].strip()))
    if with_definitions:
        glossary = next((text.name for text in corpus if text.glossary), FILE_PATH)
        for entry in entries:
            if entry.definition is None or entry.term.lower() == term.lower():
                continue
            searched = use_text(entry.definition, names)
            lines = entry.definition.split("\n")
            for offset, _ in find_uses(term, searched, terms):
                number = line_at(searched, offset)
                found.append(Use(glossary, entry.definition_line + number - 1,
                                 lines[number - 1].strip()))
    return found


def check_term_use(entries, corpus, report, merge, no_commit=None):
    """Every term has a use outside the glossary; one that has none is a warning, and, checking a
    merge, an error (WAY-95). Given `no_commit`, records the merge's check unchecked instead."""
    # invariant: glossary-term-use/1
    check, use = "check_term_use", "glossary-term-use/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, use)
        report.cannot_check("the terms with no use after the merge", no_commit)
        return
    if merge:
        report.ran(check, use)
    for entry in entries:
        if not entry.term or uses_of(entry.term, corpus, entries, False):
            continue
        message = "%s: the term has no use outside the glossary" % entry.term
        if merge:
            report.error(entry.line, message + "; on the main branch every term has one",
                         check, (use,))
        else:
            report.warning(entry.line, message + "; a merge onto the main branch fails on it")


# --- the commit the branch left the main branch from ---------------------------------------


def sentences_of(block):
    """The sentences of a decision version, each flattened: its question, then every sentence of
    its paragraphs, fields and list items, each item read as a paragraph of its own, a field's name
    left out, since the template renames a field after a decision's first version."""
    units = [block[0].split(" — ", 1)[1] if " — " in block[0] else ""]
    units += re.split(r"\n(?=[ \t]*- |\*[^*\n]+:\*)|\n[ \t]*\n", "\n".join(block[1:]))
    sentences = []
    for unit in units:
        unit = re.sub(r"^\s*(?:- \*\*[^*\n]+?:\*\*|\*[^*\n]+?:\*)", "", unit)
        sentences += [sentence for sentence in SENTENCE_END.split(flat(unit)) if sentence]
    return sentences


def restated_spans(text):
    """(start, end) of every sentence a version of a decision restates word for word from the
    version before it (WAY-98), found in the text as sentences_of reads it."""
    prefix = decision_guard.detect_prefix(text)
    if not prefix:
        return []
    starts = [0]
    for line in text.split("\n"):
        starts.append(starts[-1] + len(line) + 1)
    blocks = []
    for first, block in decision_guard.split_entries(text):
        version = re.match(r"^### %s-(\d{2,})/(\d+) — " % re.escape(prefix), block[0])
        if version:
            blocks.append(((int(version.group(1)), int(version.group(2))), starts[first - 1],
                           starts[first - 1 + len(block)] - 1, sentences_of(block)))
    sentences = {key: set(found) for key, _, _, found in blocks}
    spans = []
    for (number, version), start, end, found in blocks:
        before = sentences.get((number, version - 1), set())
        cursor = start
        for sentence in found:
            match = re.compile(r"\s+".join(re.escape(word) for word in sentence.split())).search(
                text, cursor, end)
            if not match:
                continue
            cursor = match.end()
            if sentence in before:
                spans.append((match.start(), match.end()))
    return spans


def without_entries(text):
    """The text of a glossary with its entries blanked: its title and paragraph stay."""
    lines = text.split("\n")
    first = next((index for index, line in enumerate(lines) if line.startswith("## ")), len(lines))
    return "\n".join(lines[:first] + [spaces(line) for line in lines[first:]])


def count_text(text, identifiers, names, glossary=False):
    """A text as *Avoid* counts it (WAY-98): an identifier of the part map, the invariants or the
    environment facts standing in a field's value, the sentences a new version of a decision
    restates, the glossary's entries, what a use of a term leaves out and text in quotation marks
    blanked, positions kept."""
    text = FIELD_VALUE.sub(lambda match: match.group(1) + IDENTIFIER_TOKEN.sub(
        lambda token: spaces(token.group(0)) if token.group(0).lower() in identifiers
        else token.group(0), match.group(2)), text)
    for start, end in restated_spans(text):
        text = text[:start] + spaces(text[start:end]) + text[end:]
    if glossary:
        text = without_entries(text)
    return blank(use_text(text, names), QUOTES)


def count_word(word, text, identifiers, names, terms, glossary=False):
    """How many times a word of *Avoid* stands in a text: in any letter case and form, outside the
    text count_text leaves out and outside the span of a longer term of the glossary (WAY-98)."""
    if text is None:
        return 0
    return len(find_uses(word, count_text(text, identifiers, names, glossary), terms))


def glossary_at(path, commit, top, report):
    text, failure = shared.file_at(commit, relative(path, top), top)
    if failure:
        report.error(None, failure)
        raise LookupError
    return text


def foundation_at(path, commit, top, report):
    directory = foundations_directory(path, top)
    texts = []
    for name in BESIDE:
        text, failure = shared.file_at(commit, relative(os.path.join(directory, name), top), top)
        if failure:
            report.error(None, failure)
            raise LookupError
        texts.append(text)
    return foundation_of(*texts)


def read_alike(term, identifier):
    """Whether a term and an identifier read alike: the identifier, its hyphens read as spaces, is
    the term in one of its forms (WAY-93)."""
    return same_word(term, identifier)


def names_its_element(identifier, foundation):
    """Whether the identifier is a part whose files include `elements/<identifier>/`: in the-way,
    whose parts answer for its elements, a term naming that element raises no warning against it
    (WAY-93)."""
    return any(pattern.startswith("elements/%s/" % identifier)
               for pattern in foundation.parts.get(identifier, []))


def check_against_base(path, entries, rules, corpus, foundation, base, top, report, no_commit=None,
                       own=False):
    """Against the base: no word of *Avoid* stands in a file more times than on the base (WAY-98);
    a term and an identifier that came to read alike are a warning, save, in the-way's own glossary
    (`own`), a term naming the element of a part whose files include `elements/<identifier>/`
    (WAY-93); the report lists the uses of every term whose definition changed (WAY-97). Given
    `no_commit`, which says why there is no base, records the count unchecked instead."""
    # invariant: glossary-avoid-growth/1
    check, growth = "check_against_base", "glossary-avoid-growth/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, growth)
        report.cannot_check("the count of the words of *Avoid*", no_commit)
        report.cannot_check("terms and identifiers that came to read alike", no_commit)
        report.cannot_check("the uses of every term whose definition changed", no_commit)
        return
    try:
        base_glossary = glossary_at(path, base, top, report)
        base_foundation = foundation_at(path, base, top, report)
    except LookupError:
        return
    except (TemplateError, AttributeError, IndexError) as problem:
        report.error(None, "cannot read the identifiers on %s: %s" % (base, problem))
        return
    identifiers = foundation.entries | foundation.withdrawn
    base_identifiers = base_foundation.entries | base_foundation.withdrawn
    words = [(entry, re.sub(MARKS, "", word).strip()) for entry in entries
             for word, _ in pairs(value_of(entry, AVOID)[0])]
    words = [(entry, word) for entry, word in words if word]
    outside = [text.name for text in corpus if not text.in_repo and not text.glossary]
    if words and outside:
        report.cannot_check("the words of *Avoid* in %s" % ", ".join(outside),
                            "git does not hold them in this repository, so nothing reads them on %s"
                            % base)
    befores = {}
    for text in corpus:
        if text.in_repo and words:
            befores[text.name], failure = shared.file_at(base, text.name, top)
            if failure:
                # a failure of the run, not of the check, which then records no verdict (WAY-63)
                report.error(None, failure)
                return
    report.ran(check, growth)
    names = field_names(text.text for text in corpus)
    terms = [entry.term for entry in entries if entry.term]
    for text in corpus:
        if text.name not in befores:
            continue
        before = befores[text.name]
        for entry, word in words:
            now = count_word(word, text.text, identifiers, names, terms, text.glossary)
            then = count_word(word, before, base_identifiers, names, terms, text.glossary)
            if now > then:
                report.error(None, "%s: `%s`, which the *Avoid* of `%s` lists, stands %d time(s), "
                                   "%d on %s" % (text.name, word, entry.term, now, then, base),
                             check, (growth,))

    base_terms = terms_of(base_glossary, rules)
    base_pairs = {(term, identifier) for term in base_terms
                  for identifier in base_foundation.entries if read_alike(term, identifier)}
    for entry in entries:
        for identifier in sorted(foundation.entries):
            if not read_alike(entry.term, identifier) or \
                    (entry.term.lower(), identifier) in base_pairs:
                continue
            if own and names_its_element(identifier, foundation):
                continue
            report.warning(entry.line, "term `%s` and identifier `%s` read alike, and did not on "
                                       "%s: where they name the same thing the entry stays, where "
                                       "not, one side is renamed" % (entry.term, identifier, base))

    for entry in entries:
        before = base_terms.get(entry.term.lower())
        if before is None or before == flat(entry.definition or ""):
            continue
        uses = uses_of(entry.term, corpus, entries, True)
        report.notes.append("uses of `%s`, whose definition differs from %s — the input of the "
                            "review of its uses: %d%s" % (
                                entry.term, base, len(uses),
                                "".join("\n  %s:%d: %s" % (use.name, use.line, use.text)
                                        for use in uses)))


# --- the commit a merge onto the main branch is made onto ----------------------------------


def check_merge_todo(entries, report, no_commit=None):
    """Reports every field of every entry that holds `TODO` (WAY-71, WAY-99). Given `no_commit`,
    records it unchecked instead."""
    # invariant: glossary-entry-merge-todo/1
    check, merge_todo = "check_merge_todo", "glossary-entry-merge-todo/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, merge_todo)
        report.cannot_check("`TODO` in the entries", no_commit)
        return
    report.ran(check, merge_todo)
    for entry in entries:
        for name, (value, line) in entry.fields.items():
            if TODO_WORD.search(value):
                report.error(line, "%s: *%s* holds `TODO`, which a merge onto the main branch does "
                                   "not take" % (entry.term, name), check, (merge_todo,))


def merge_base(top, commit):
    """(the merge base of HEAD and the commit or None where they have none, git's message where
    git fails): `git merge-base` exits 1 for no common ancestor and otherwise for a failure."""
    code, answer, message = shared.call_git(["merge-base", "HEAD", commit], top)
    if code == 0 and answer.strip():
        return answer.strip(), None
    if code == 1 and not message:
        return None, None
    return None, "git cannot find the merge base of HEAD and %s: %s" % (
        commit, message or "git merge-base exited with %d" % code)


def merge_texts(mine, before, theirs, top):
    """(the text git's three-way merge leaves, None) or (None, why it leaves none): a conflict, or
    git failing."""
    directory = tempfile.mkdtemp(prefix="glossary-merge-")
    try:
        paths = []
        for name, text in (("mine", mine), ("base", before or ""), ("theirs", theirs)):
            paths.append(os.path.join(directory, name))
            with open(paths[-1], "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        code, merged, message = shared.call_git(["merge-file", "-p"] + paths, top)
    finally:
        shutil.rmtree(directory, ignore_errors=True)
    if code == 0:
        return merged, None
    if 0 < code < 128:
        # git counts conflicts up to 127; a negative exit, read as 128 or more, is a failure
        return None, "%d conflict(s)" % code
    return None, message or "git merge-file exited with %d" % code


def merged_corpus(path, corpus, merge_onto, top, report):
    """The files of `foundations/` and the templates as git's merge onto the commit leaves them: a
    file only one side changed since the merge base is that side's, and a file both changed is
    merged by git line by line (WAY-95). None once the report says why the merge cannot be read:
    a conflict, or git failing, is a failure of the run (WAY-63)."""
    base, failure = merge_base(top, merge_onto)
    if failure:
        report.error(None, failure)
        return None
    code, listing, message = shared.call_git(["ls-tree", "-r", "--full-tree", "-z",
                                                 "--name-only", merge_onto, "--", FOUNDATIONS], top)
    if code != 0:
        report.error(None, "git cannot list %s at %s: %s" % (FOUNDATIONS, merge_onto, message))
        return None
    names = [name for name in listing.split("\0") if name]
    own = {text.name: text for text in corpus}
    merged = [text for text in corpus if not text.in_repo or text.glossary]
    if base is None:
        report.notes.append("HEAD and %s have no merge base; every file is merged as added on both "
                            "sides" % merge_onto)
    for name in sorted(set(names) | {text.name for text in corpus
                                     if text.in_repo and not text.glossary}):
        if name in own and own[name].glossary:
            continue
        theirs, failure = shared.file_at(merge_onto, name, top)
        before = None
        if not failure and base is not None:
            before, failure = shared.file_at(base, name, top)
        if failure:
            report.error(None, failure)
            return None
        mine = own[name].text if name in own else None
        if mine == theirs or theirs == before:
            chosen = mine
        elif mine == before:
            chosen = theirs
        elif mine is None or theirs is None:
            report.error(None, "%s: one side of the merge onto %s deletes the file and the other "
                               "changes it; the merge cannot be read" % (name, merge_onto))
            return None
        else:
            chosen, why = merge_texts(mine, before, theirs, top)
            if why:
                report.error(None, "%s: git cannot merge the file onto %s (%s); the merge cannot be "
                                   "read" % (name, merge_onto, why))
                return None
        if chosen is not None:
            merged.append(Text(name, chosen, True))
    return merged


# --- the examples ---------------------------------------------------------------------------


def check_examples(entries, examples_path, report):
    """Every term `examples.md` names is the term of an entry of the glossary: an example names an
    entry of the-way's glossary by its term instead of copying it (WAY-09, WAY-34). An item of a
    list names the term it opens with: the words in backticks, or else its first word."""
    # invariant: glossary-example-target/1
    check, target = "check_examples", "glossary-example-target/1"
    examples = shared.read_file(examples_path, report, "the examples")
    if examples is None:
        return
    report.ran(check, target)
    terms = {entry.term for entry in entries}
    for number, line in enumerate(examples.split("\n"), start=1):
        item = re.match(r"^- (?:`([^`]+)`|([^`\s]+))", line)
        term = item and (item.group(1) or item.group(2))
        if term and term not in terms:
            report.error(None, "examples.md:%d: `%s` is not the term of an entry of the glossary"
                         % (number, term), check, (target,))


# --- entry point ----------------------------------------------------------------------------


def find_commit(top, option, commit, report):
    if top is None:
        report.error(None, "%s %s given, but the file is not in a git repository" % (option, commit))
        return False
    return shared.find_commit(top, option, commit, report)


def list_uses(word, corpus, entries, report, stream):
    """Lists the uses of a word, then what the run could not read: a use list is no agreement that
    nothing was missed (WAY-38)."""
    uses = uses_of(word, corpus, entries, True)
    for use in uses:
        stream.write("%s:%d: %s\n" % (use.name, use.line, use.text))
    stream.write("%d use(s) of `%s`\n" % (len(uses), word))
    report.print(stream)
    return 1 if report.errors else 0


def run(path, base=None, stream=None, template=TEMPLATE, merge_onto=None, record=None,
        examples=EXAMPLES, templates=None, uses=None, common=None, own=None):
    """Checks the glossary at the path. `templates` names the elements' templates and `common` the
    directory of the part the elements share that the checks search; given templates in place of
    those beside this script, the part the elements share is searched only where it is given too.
    `own` says whether the file is the-way's own glossary, which by default is known by its path."""
    stream = stream or sys.stdout
    if common is None and templates is not None:
        common = False
    if uses is not None and (base or merge_onto or record):
        stream.write("--uses lists the uses of a word and runs no check; it takes neither --base, "
                     "--merge-onto nor --record\n")
        return 2
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
    except (OSError, UnicodeDecodeError, TemplateError, decision_guard.TemplateError,
            AttributeError) as problem:
        return stop("cannot read the rules from %s: %s" % (template, problem))
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except FileNotFoundError as problem:
        if uses is None:
            return stop("cannot read the glossary: %s" % problem)
        text = ""   # the uses of a word are listed before the glossary has its first entry
    except (OSError, UnicodeDecodeError) as problem:
        return stop("cannot read the glossary: %s" % problem)

    if own is None:
        own = os.path.exists(OWN_FILE) and os.path.exists(path) and os.path.samefile(path, OWN_FILE)
    top = invariant_guard.repository_root(path, report)
    tracked = invariant_guard.tracked_files(top, report) if top is not None else None
    head, items = parse_file(text, rules)
    entries = entries_of(items)
    corpus = read_corpus(path, top, tracked, report, templates, common)
    if uses is not None:
        return list_uses(uses, corpus, entries, report, stream)
    foundation = read_foundation(path, top, report)

    merging = bool(merge_onto) and merge_onto != NO_COMMIT
    check_layout(head, items, report)
    check_file(path, top, tracked, report)
    check_terms(entries, report)
    check_fields(entries, rules, report)
    check_definitions(entries, rules, report)
    check_avoid(entries, report)
    check_not(entries, rules, foundation, corpus, report, warn_todo=not merging)
    check_process_terms(entries, rules, top, own, report)

    if base == NO_COMMIT:
        no_base = "--base none: there is no commit the branch left the main branch from"
        check_against_base(path, entries, rules, corpus, foundation, None, None, report,
                           no_commit=no_base)
    elif base:
        if find_commit(top, "--base", base, report):
            check_against_base(path, entries, rules, corpus, foundation, base, top, report,
                               own=own)
    else:
        report.notes.append("no --base given: the words of *Avoid* are not counted against the main "
                            "branch, terms and identifiers that read alike are not reported, and "
                            "no changed definition has its uses listed; those checks are not run, "
                            "and are not counted in the last line")

    if merge_onto == NO_COMMIT:
        no_onto = "--merge-onto none: there is no commit to merge onto"
        check_merge_todo(entries, report, no_commit=no_onto)
        check_term_use(entries, corpus, report, False)
        check_term_use(entries, corpus, report, True, no_commit=no_onto)
    elif merge_onto:
        if find_commit(top, "--merge-onto", merge_onto, report):
            check_merge_todo(entries, report)
            merged = merged_corpus(path, corpus, merge_onto, top, report)
            if merged is not None:
                check_term_use(entries, merged, report, True)
    else:
        check_term_use(entries, corpus, report, False)
        report.notes.append("no --merge-onto given: `TODO` in *Not* and a term with no use are only "
                            "warnings; the checks of a merge are not run, and are not counted in "
                            "the last line")

    if own and os.path.exists(examples):
        check_examples(entries, examples, report)
    report.print(stream)
    if record is not None:
        write_record(record, report)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a product's glossary against the template.")
    parser.add_argument("file", nargs="?", default=os.path.join("foundations", "glossary.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from, to "
                                       "count the words of *Avoid* against, report terms and "
                                       "identifiers that came to read alike and list the uses of "
                                       "changed definitions; `none` where it does not exist, which "
                                       "records the count as unchecked")
    parser.add_argument("--merge-onto", help="the commit of the main branch a merge is made onto; "
                                             "only with it are `TODO` in *Not* and a term with no "
                                             "use errors; `none` where the main branch does not "
                                             "exist, which records those checks as unchecked")
    parser.add_argument("--record", help="the JSON Lines file, created or overwritten, that "
                                         "receives a verdict for each invariant a check cites")
    parser.add_argument("--uses", metavar="WORD", help="list the uses of a word and run no check; "
                                                       "takes no other option")
    arguments = parser.parse_args(argv)
    if arguments.uses is not None and (arguments.base or arguments.merge_onto or arguments.record):
        parser.error("--uses takes neither --base, --merge-onto nor --record")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.file, arguments.base, merge_onto=arguments.merge_onto,
               record=arguments.record, uses=arguments.uses)


if __name__ == "__main__":
    sys.exit(main())
