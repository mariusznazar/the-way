"""Format guard of a product's decision log.

Checks the log against the rules of template.md, which lies next to this script. Field names,
kinds of change, relation types, forms of a review record's *Result*, levels of verification, the
fields that never take `none` or `TODO`, the number of binding sentences and the words kept out of
them are read from the template, so the rules of the entry live in one place (WAY-05, WAY-35,
WAY-71). Each check cites the invariants it gives a verdict for, as
`invariant: <identifier>/<version>` (WAY-65). In the-way's own log, the guard also checks who
approved each version (WAY-14) and that every number `examples.md` names is a decision of the log
(WAY-05). The report and the record of a run are written with the code the format guards share
(WAY-09).

Usage, from the root of the product's repository:

    python <the-way>/elements/decisions/format_guard.py [LOG] [--base REF] [--merge-onto REF]
        [--today YYYY-MM-DD] [--record PATH]

LOG defaults to foundations/decisions.md. --base names the commit the task branch left the main
branch from, to compare the log with; without it, the checks that need it are skipped.
--merge-onto names the commit of the main branch a merge is made onto; without it, the checks of a
merge are skipped: the copies of a version both logs hold (WAY-07), the fingerprints relations carry
against the current binding part, and `TODO` in any field of the log, which the main branch does
not hold (WAY-71). `none`, given to either option, is the value the gate fills in where that commit
does not exist (WAY-61): the checks that need the commit are then recorded as `unchecked`, the
report names each on an `unchecked:` line and counts it in its last line, and they give no
error. --record names a
JSON Lines file, created or overwritten, which receives the-way's own record of the run (WAY-74):
a verdict for each invariant cited by a check the run's options select — the checks against the
base with --base, the checks of a merge with --merge-onto, the checks of the log alone with
neither — a line for each error of those checks that belongs to no cited invariant, and every
failure of the run itself. The report for a person holds every check. Exit code: 0 without
errors, 1 with errors, 2 when the log or the template cannot be read or the record cannot be
written.
"""

import argparse
import datetime
import importlib.util
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_LOG = os.path.join(HERE, "..", "..", "foundations", "decisions.md")

# The name a record gives this program, and each of its checks as PROGRAM::<function>.
PROGRAM = "elements/decisions/format_guard.py"
# The template a change may alter only together with a new version in the log, as the
# invariant decision-template-change names it, relative to the root of the repository.
TEMPLATE_PATH = "elements/decisions/template.md"
# Who approves a version of the-way's own log, as the invariant decision-approver names it (WAY-14).
OWN_APPROVER = "Mariusz"
# The checks each option selects for the record; every other check reads the log alone and is
# recorded only by a run given neither option. A run records the checks its options select, and
# its own failures always (WAY-61, WAY-74).
SELECTED_BY = {"check_against_base": "--base", "check_template_change": "--base",
               "check_fingerprints": "--merge-onto", "merged_log": "--merge-onto",
               "check_merge_todo": "--merge-onto"}

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "relation-model"))
from fingerprint import fingerprint  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The code the format guards share (WAY-09): the report of a run and the-way's own record of it.
shared = _load("elements_common_guard_shared",
               os.path.join(HERE, "..", "common", "guard_shared.py"))
NO_COMMIT = shared.NO_COMMIT
NO_COMMIT_REASON = shared.NO_COMMIT_REASON

DATE = r"\d{4}-\d{2}-\d{2}"
NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}


class TemplateError(Exception):
    pass


# --- rules read from the template -----------------------------------------------------------


@dataclass
class Rules:
    version_fields: list
    prose_fields: list
    renamed_after_first: dict
    review_fields: list
    kinds: dict  # kind -> binding sentences vs previous version: "—", "differ", "identical", "none"
    relation_types: dict  # type -> carries a fingerprint
    forbidden_words: list
    keywords: list
    max_sentences: int
    result_forms: list
    verification_levels: list
    word_errors: dict  # "none" or "TODO" -> fields of a version where the word is an error
    review_none: list  # fields of a review that take `none`
    inherited_marker: str  # the word *Origin* of an inherited decision opens with
    inherited_origin: str  # pattern of *Origin* of an inherited decision


def _section(text, title):
    match = re.search(r"^## %s\n(.*?)(?=^## |\Z)" % re.escape(title), text, re.M | re.S)
    if not match:
        raise TemplateError('section "%s" not found' % title)
    return match.group(1)


def _code_block(section_text, title):
    match = re.search(r"```markdown\n(.*?)```", section_text, re.S)
    if not match:
        raise TemplateError('no entry form in section "%s"' % title)
    return match.group(1)


def _bullets(section_text):
    """The text of every top-level bullet of a section, its indented continuation lines joined."""
    bullets = []
    for line in section_text.splitlines():
        if line.startswith("- "):
            bullets.append(line[2:].strip())
        elif bullets and line.startswith("  ") and line.strip():
            bullets[-1] += " " + line.strip()
    return bullets


def read_rules(path=TEMPLATE):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    version_section = _section(text, "Decision version")
    version_form = _code_block(version_section, "Decision version")
    version_fields = re.findall(r"^- \*\*(.+?):\*\*", version_form, re.M)
    prose_fields = re.findall(r"^\*(.+?):\*", version_form, re.M)
    renamed = dict(re.findall(r"\*([^*]+)\* becomes \*([^*]+)\*", version_section))

    review_section = _section(text, "Review")
    review_fields = re.findall(r"^- \*\*(.+?):\*\*", _code_block(review_section, "Review"), re.M)
    result_forms = []
    for form in re.findall(r"^- `([^`]+)`", review_section, re.M):
        result_forms.append(re.split(r"<|\b[A-Z]+-NN", form)[0].strip())
    review_none = sorted(set(re.findall(r"\*([^*]+)\* is [^;\n]*`none`", review_section)))

    kinds = {}
    for line in _section(text, "Kinds of change").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) >= 3 and cells[0] not in ("Kind", "") \
                and not set(cells[0]) <= set("-"):
            kinds[cells[0]] = cells[2]

    word_errors = {}
    for line in version_section.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        word = re.match(r"^`(none|TODO)`$", cells[0]) if line.startswith("|") else None
        if word and len(cells) == 2:
            word_errors[word.group(1)] = re.findall(r"\*([^*]+)\*", cells[1])
    if set(word_errors) != {"none", "TODO"}:
        raise TemplateError("cannot read which fields never take `none` or `TODO`")

    relations_line = re.search(r"^- \*\*Relations:\*\* (.*)$", version_form, re.M).group(1)
    relation_types = {}
    for item in relations_line.split(" | ")[0].split(" · "):
        match = re.match(r"^(.+?) [A-Z]+-\w+(@<fingerprint>)?$", item.strip())
        if not match:
            raise TemplateError("cannot read relation type from %r" % item)
        relation_types[match.group(1)] = bool(match.group(2))

    levels = re.search(r"^- \*\*Verification:\*\* level ([\d |]+?) —", version_form, re.M)
    if not levels:
        raise TemplateError("cannot read the levels of verification")
    verification_levels = [level.strip() for level in levels.group(1).split("|")]

    origin_line = re.search(r"^- \*\*Origin:\*\* (.*)$", version_form, re.M).group(1)
    inherited = next((form.strip() for form in origin_line.split(" | ")
                      if form.strip().startswith("inherited")), None)
    if inherited is None:
        raise TemplateError("cannot read the form of *Origin* of an inherited decision")
    inherited_origin = "^%s$" % "(\\S.*?)".join(re.escape(part) for part in inherited.split("<…>"))

    binding_rules = _bullets(_section(text, "Binding sentences"))
    count = next((match for match in (re.match(r"One to (\w+) sentences\b", rule)
                                      for rule in binding_rules) if match), None)
    if not count or count.group(1) not in NUMBER_WORDS:
        raise TemplateError("cannot read the number of binding sentences")
    kept_out = next((rule for rule in binding_rules if "do not appear" in rule), None)
    if kept_out is None:
        raise TemplateError("no rule on the words kept out of binding sentences")
    forbidden_words = re.findall(r"\*(\w+)\*", kept_out)
    keywords = re.search(r"keywords of RFC 2119 in capitals \(([^)]*)\)", kept_out)
    if not forbidden_words or not keywords:
        raise TemplateError("cannot read the words kept out of binding sentences")

    if not (version_fields and prose_fields and review_fields and kinds and result_forms):
        raise TemplateError("the entry forms are incomplete")
    return Rules(version_fields, prose_fields, renamed, review_fields, kinds, relation_types,
                 forbidden_words, [k.strip() for k in keywords.group(1).split(",")],
                 NUMBER_WORDS[count.group(1)], result_forms, verification_levels, word_errors,
                 review_none, inherited.split()[0], inherited_origin)


# --- parsing the log ------------------------------------------------------------------------


@dataclass
class Entry:
    line: int
    heading: str
    kind: str  # "version", "review" or "unknown"
    number: int = None
    version: int = None
    date: str = None
    binding: str = None
    fields: dict = field(default_factory=dict)  # name -> (value, line)
    text: str = ""


def detect_prefix(text):
    match = re.search(r"^### ([A-Z][A-Z0-9]*)-\d", text, re.M) or \
        re.search(r"^#+\s*([A-Z][A-Z0-9]*)-\d{2,}/\d", text, re.M)
    return match.group(1) if match else None


def split_entries(text, level="### "):
    """Yield (line number, lines) for each block that starts with a heading of the given level."""
    lines = text.split("\n")
    start = None
    for index, line in enumerate(lines):
        if line.startswith("#"):
            if start is not None:
                yield start + 1, lines[start:index]
                start = None
            if line.startswith(level):
                start = index
    if start is not None:
        yield start + 1, lines[start:]


def parse_entry(first_line, lines, prefix):
    heading = lines[0]
    entry = Entry(first_line, heading, "unknown", text="\n".join(lines).rstrip())
    version = re.match(r"^### %s-(\d{2,})/(\d+) — (\S.*)$" % re.escape(prefix), heading)
    review = re.match(r"^### %s-(\d{2,}) · review (%s)$" % (re.escape(prefix), DATE), heading)
    if version:
        entry.kind, entry.number, entry.version = "version", int(version.group(1)), int(version.group(2))
    elif review:
        entry.kind, entry.number, entry.date = "review", int(review.group(1)), review.group(2)
    else:
        return entry

    body = lines[1:]
    index = 0
    while index < len(body) and not body[index].strip():
        index += 1
    if entry.kind == "version" and index < len(body) and not body[index].startswith("- **"):
        paragraph = []
        while index < len(body) and body[index].strip():
            paragraph.append(body[index])
            index += 1
        entry.binding = "\n".join(paragraph)

    current = None
    for offset, line in enumerate(body[index:], start=first_line + 1 + index):
        bold = re.match(r"^- \*\*(.+?):\*\*(?: (.*))?$", line)
        prose = re.match(r"^\*(.+?):\*(?: (.*))?$", line)
        match = bold or prose
        if match:
            current = match.group(1)
            if current not in entry.fields:
                entry.fields[current] = [(match.group(2) or "").strip(), offset]
            else:
                current = None
        elif not line.strip():
            current = None
        elif current is not None and (prose is None and (line.startswith(" ") or
                                                         not line.startswith("- "))):
            entry.fields[current][0] = (entry.fields[current][0] + " " + line.strip()).strip()
    return entry


def parse_log(text, prefix):
    return [parse_entry(line, lines, prefix) for line, lines in split_entries(text)]


# --- the report and the record of a run -----------------------------------------------------


class Report(shared.Report):
    """The report the guards share, naming this program and its checks in the record."""

    def __init__(self, path, options=()):
        super().__init__(path, options, program=PROGRAM, selected_by=SELECTED_BY)


start_record = shared.start_record
write_record = shared.write_record


# --- checks ---------------------------------------------------------------------------------


def without_code(text):
    return re.sub(r"`[^`]*`", "Code", text)


def count_sentences(text):
    flat = " ".join(without_code(text).split())
    ends = len(re.findall(r"[.!?](?=\s+[\"'(A-Z]|$)", flat))
    return ends if re.search(r"[.!?]$", flat) else ends + 1


def bare(value):
    """A value without the backticks that mark it as a literal word, as the invariants guard
    reads it."""
    value = value.strip()
    if len(value) > 1 and value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        return value[1:-1]
    return value


def is_todo(value):
    value = bare(value)
    return value == "TODO" or value.startswith("TODO ")


def valid_date(value):
    try:
        datetime.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def label_of(entry, prefix):
    if entry.kind == "review":
        return "%s-%02d · review %s" % (prefix, entry.number, entry.date)
    return "%s-%02d/%d" % (prefix, entry.number, entry.version)


def versions_of(entries):
    return [entry for entry in entries if entry.kind == "version"]


def fields_of_version(entry, rules):
    prose = [rules.renamed_after_first.get(name, name) if entry.version > 1 else name
             for name in rules.prose_fields]
    return rules.version_fields + prose


def field_value(entry, name):
    value, line = entry.fields.get(name, ("", entry.line))
    return value, line


def takes_todo(rules, name):
    """Whether the table of states gives `TODO` to the field of a decision version (WAY-71)."""
    return name not in rules.word_errors["TODO"]


def change_kind(entry, rules, prefix):
    """The kind of change a version names, or None where it names none from the list."""
    value = field_value(entry, "Change")[0]
    if not value or is_todo(value):
        return None
    if entry.version == 1:
        return "new decision"
    return value if value in rules.kinds and value != "new decision" else None


def check_log(entries, text, rules, prefix, report, today, approver=None):
    """Runs every check of the log itself and returns the latest version of each number."""
    numbers, versions = check_headings(entries, text, rules, prefix, report)
    latest = {number: items[-1] for number, items in numbers.items()}
    check_fields(entries, rules, prefix, report)
    check_changes(entries, rules, prefix, report)
    check_bindings(entries, rules, prefix, report)
    check_binding_across_versions(entries, rules, prefix, report, versions)
    check_relations(entries, rules, prefix, report)
    check_verification(entries, rules, prefix, report)
    check_approval(entries, prefix, report)
    if approver:
        check_approver(entries, approver, prefix, report)
    check_review_when(entries, rules, prefix, report)
    check_inherited(entries, rules, prefix, report)
    check_references(text, entries, prefix, report, numbers, versions)
    check_reviews(entries, rules, prefix, report, numbers, versions)
    check_narrows(latest, prefix, report)
    check_review_dates(entries, latest, prefix, report, today)
    return latest


def version_blocks(text, rules):
    """Yield (line of the heading or None, heading, lines opening a decision version's first
    field) for each stretch of the log between two headings of any level.

    A decision version is known by its fields, not by its heading: a stretch holding the first
    field of the version form is a decision version, whatever heading stands above it."""
    opening = re.compile(r"^- \*\*%s:\*\*" % re.escape(rules.version_fields[0]))
    heading_line, heading, openings = None, None, []
    for number, line in enumerate(text.split("\n"), start=1):
        if line.startswith("#"):
            yield heading_line, heading, openings
            heading_line, heading, openings = number, line, []
        elif opening.match(line):
            openings.append(number)
    yield heading_line, heading, openings


def check_headings(entries, text, rules, prefix, report):
    # invariant: decision-heading-form/1
    # invariant: decision-version-sequence/1
    check, form, sequence = "check_headings", "decision-heading-form/1", "decision-version-sequence/1"
    report.ran(check, form, sequence)
    shape = "`### %s-NN/V — <question>`" % prefix
    version_heading = re.compile(r"^### %s-(\d{2,})/(\d+) — (\S.*)$" % re.escape(prefix))
    unknown = {entry.line for entry in entries if entry.kind == "unknown"}
    for line, heading, openings in version_blocks(text, rules):
        if heading is not None and version_heading.match(heading):
            for extra in openings[1:]:
                report.error(extra, "a decision version stands here with no heading of its own; "
                                    "its heading has the form %s" % shape, check, (form,))
        elif line in unknown:
            continue  # reported below with the heading of the entry
        elif heading is not None and re.match(r"^#+\s*%s-\d{2,}/\d+\b" % re.escape(prefix), heading):
            report.error(line, "the heading of a decision version is `%s`, not %s"
                         % (heading, shape), check, (form,))
        elif openings:
            report.error(openings[0], "a decision version stands under %s, not under a heading of "
                                      "the form %s" % ("`%s`" % heading if heading else
                                                       "no heading", shape), check, (form,))
    numbers = {}
    versions = {}
    for entry in entries:
        if entry.kind == "unknown":
            report.error(entry.line, "heading is neither `### %s-NN/V — <question>` nor "
                                     "`### %s-NN · review YYYY-MM-DD`" % (prefix, prefix),
                         check, (form,))
        elif entry.kind == "version":
            expected = len(numbers.get(entry.number, [])) + 1
            if entry.version != expected:
                report.error(entry.line, "%s-%02d: version %d where version %d is next"
                             % (prefix, entry.number, entry.version, expected), check, (sequence,))
            numbers.setdefault(entry.number, []).append(entry)
            versions[(entry.number, entry.version)] = entry
    return numbers, versions


# Fields a decision version may still carry that the form does not hold, with what stands in their
# place: precedence is a relation `narrows` (WAY-25), the approver is who *Approved by* names
# (WAY-14), and what a decision forces on later work stands in a binding sentence or a field
# (WAY-05).
DROPPED_FIELDS = {
    "Outranks": "the decision that prevails names the other in *Relations* as `narrows`",
    "Approver override": "*Approved by* names who approved the version",
    "Consequences": "what a decision forces on later work stands in a binding sentence or a field",
}


def check_fields(entries, rules, prefix, report):
    """Every field of the form is present, and holds `none` or `TODO` only where the table of
    states gives it that word (WAY-71). *Outranks*, *Approver override* and *Consequences* are
    reported with what stands in their place."""
    # invariant: log-entry-field-presence/1
    # invariant: log-entry-field-words/1
    check, presence, words = "check_fields", "log-entry-field-presence/1", "log-entry-field-words/1"
    report.ran(check, presence, words)
    for entry in entries:
        if entry.kind == "version":
            names = fields_of_version(entry, rules)
            takes_none = [name for name in names if name not in rules.word_errors["none"]]
            takes_todo = [name for name in names if name not in rules.word_errors["TODO"]]
        elif entry.kind == "review":
            names, takes_none, takes_todo = rules.review_fields, rules.review_none, rules.review_fields
        else:
            continue
        for name in names:
            value, line = field_value(entry, name)
            if not value:
                report.error(entry.line, "field *%s* is missing" % name, check, (presence,))
            elif is_todo(value):
                if name in takes_todo:
                    report.warning(line, "*%s* is `TODO`" % name)
                else:
                    report.error(line, "*%s* is `TODO`" % name, check, (words,))
            elif value == "none" and name not in takes_none:
                report.error(line, "*%s* is `none`" % name, check, (words,))
        if entry.kind == "version":
            for name, (value, line) in entry.fields.items():
                if name in DROPPED_FIELDS and name not in names:
                    report.error(line, "%s: *%s* is not a field of the form; %s"
                                 % (label_of(entry, prefix), name, DROPPED_FIELDS[name]), check)
            for name, renamed in rules.renamed_after_first.items():
                wrong = renamed if entry.version == 1 else name
                if wrong in entry.fields:
                    report.error(entry.fields[wrong][1], "%s: version %d uses *%s*"
                                 % (label_of(entry, prefix), entry.version, wrong), check)


def check_changes(entries, rules, prefix, report):
    # invariant: decision-change-kind/1
    check, kind_named = "check_changes", "decision-change-kind/1"
    report.ran(check, kind_named)
    for entry in versions_of(entries):
        label = label_of(entry, prefix)
        value, line = field_value(entry, "Change")
        if is_todo(value) and takes_todo(rules, "Change"):
            continue  # check_fields warns
        if not value or is_todo(value):
            if entry.version > 1:
                report.fail(line, "*Change* is `TODO`" if value else "field *Change* is missing",
                            check, (kind_named,))
            continue
        if entry.version == 1:
            if value != "new decision":
                report.error(line, "%s: *Change* of version 1 is not `new decision`" % label, check,
                             (kind_named,))
            continue
        if value not in rules.kinds or value == "new decision":
            report.error(line, "%s: `%s` is not a kind of change" % (label, value), check,
                         (kind_named,))


def check_bindings(entries, rules, prefix, report):
    # invariant: binding-sentence-count/1
    # invariant: binding-sentence-words/1
    # invariant: repeal-binding-sentences/1
    check = "check_bindings"
    count, words, repeal = ("binding-sentence-count/1", "binding-sentence-words/1",
                            "repeal-binding-sentences/1")
    report.ran(check, count, words, repeal)
    for entry in versions_of(entries):
        label = label_of(entry, prefix)
        kind = change_kind(entry, rules, prefix)
        line = entry.line + 2
        if rules.kinds.get(kind) == "none":
            if entry.binding is not None:
                report.error(line, "%s: a %s has no binding sentences" % (label, kind),
                             check, (repeal,))
            continue
        if entry.binding is None:
            report.error(entry.line, "%s: binding sentences are missing" % label, check, (count,))
            continue
        sentences = count_sentences(entry.binding)
        if not 1 <= sentences <= rules.max_sentences:
            report.error(line, "%s: %d binding sentences, at most %d"
                         % (label, sentences, rules.max_sentences), check, (count,))
        plain = re.sub(r"`[^`]*`", "", entry.binding)
        for word in rules.forbidden_words:
            if re.search(r"\b%s\b" % re.escape(word), plain, re.I):
                report.error(line, "%s: binding sentences use *%s*" % (label, word), check, (words,))
        for keyword in rules.keywords:
            if re.search(r"\b%s\b" % re.escape(keyword), plain):
                report.error(line, "%s: binding sentences use %s" % (label, keyword), check, (words,))


def check_binding_across_versions(entries, rules, prefix, report, versions):
    # invariant: decision-binding-across-versions/1
    check, kept = "check_binding_across_versions", "decision-binding-across-versions/1"
    report.ran(check, kept)
    for entry in versions_of(entries):
        kind = change_kind(entry, rules, prefix)
        previous = versions.get((entry.number, entry.version - 1))
        if rules.kinds.get(kind) != "identical" or previous is None:
            continue
        label = label_of(entry, prefix)
        if entry.binding is None:
            report.fail(entry.line, "%s: binding sentences are missing" % label, check, (kept,))
        elif previous.binding is None or fingerprint(previous.binding) != fingerprint(entry.binding):
            report.error(entry.line + 2, "%s: a version of the kind %s keeps the binding sentences "
                                         "of %s" % (label, kind, label_of(previous, prefix)),
                         check, (kept,))


def check_relations(entries, rules, prefix, report):
    # invariant: relation-type/1
    # invariant: relation-fingerprint-presence/1
    check, typed, presence = "check_relations", "relation-type/1", "relation-fingerprint-presence/1"
    report.ran(check, typed, presence)
    types = sorted(rules.relation_types, key=len, reverse=True)
    for entry in versions_of(entries):
        label = label_of(entry, prefix)
        value, line = field_value(entry, "Relations")
        if value in ("none", "") or is_todo(value):
            continue
        for item in [item.strip() for item in value.split(" · ")]:
            kind = next((kind for kind in types if item.startswith(kind + " ")), None)
            if kind is None:
                report.error(line, "%s: relation `%s` is not of a known type" % (label, item),
                             check, (typed,))
                # a fingerprint only a relation of a type on the list carries
                if re.search(r"@[0-9a-f]+$", item):
                    report.error(line, "%s: `%s` carries a fingerprint" % (label, item),
                                 check, (presence,))
                continue
            match = re.fullmatch(r"(%s-\d{2,})(?:@(\S*))?" % re.escape(prefix), item[len(kind) + 1:])
            if not match:
                report.error(line, "%s: relation `%s` names no decision as `%s-NN`"
                             % (label, item, prefix), check)
            elif rules.relation_types[kind] and not re.fullmatch(r"[0-9a-f]+", match.group(2) or ""):
                report.error(line, "%s: `%s` carries no fingerprint" % (label, item),
                             check, (presence,))
            elif not rules.relation_types[kind] and match.group(2) is not None:
                report.error(line, "%s: `%s` carries a fingerprint" % (label, item),
                             check, (presence,))


def check_verification(entries, rules, prefix, report):
    # invariant: decision-verification-level/1
    check, level = "check_verification", "decision-verification-level/1"
    report.ran(check, level)
    for entry in versions_of(entries):
        value, line = field_value(entry, "Verification")
        if not value:
            report.fail(entry.line, "field *Verification* is missing", check, (level,))
        elif is_todo(value):
            if not takes_todo(rules, "Verification"):
                report.fail(line, "*Verification* is `TODO`", check, (level,))
        else:
            match = re.match(r"^level (\d+)\b", value)
            if not match or match.group(1) not in rules.verification_levels:
                report.error(line, "%s: *Verification* names no level of verification, as "
                                   "`level %s`" % (label_of(entry, prefix),
                                                   " | ".join(rules.verification_levels)),
                             check, (level,))


def check_approval(entries, prefix, report):
    # invariant: decision-approval-record/1
    check, record = "check_approval", "decision-approval-record/1"
    report.ran(check, record)
    for entry in versions_of(entries):
        value, line = field_value(entry, "Approved by")
        if not value:
            report.fail(entry.line, "field *Approved by* is missing", check, (record,))
        elif is_todo(value):
            report.fail(line, "*Approved by* is `TODO`", check, (record,))
        else:
            match = re.match(r"^.+, (%s)$" % DATE, value)
            if not match or not valid_date(match.group(1)):
                report.error(line, "%s: *Approved by* is not `<who>, YYYY-MM-DD`"
                             % label_of(entry, prefix), check, (record,))


def check_approver(entries, approver, prefix, report):
    # invariant: decision-approver/1
    check, named = "check_approver", "decision-approver/1"
    report.ran(check, named)
    for entry in versions_of(entries):
        value, line = field_value(entry, "Approved by")
        if not value:
            report.fail(entry.line, "field *Approved by* is missing", check, (named,))
            continue
        if is_todo(value):
            report.fail(line, "*Approved by* is `TODO`", check, (named,))
            continue
        match = re.match(r"^(.+), %s$" % DATE, value)
        who = match.group(1) if match else value
        if who != approver:
            report.error(line, "%s: *Approved by* names %s, not %s"
                         % (label_of(entry, prefix), who, approver), check, (named,))


def check_review_when(entries, rules, prefix, report):
    # invariant: review-when-form/1
    check, form = "check_review_when", "review-when-form/1"
    report.ran(check, form)
    for entry in versions_of(entries):
        value, line = field_value(entry, "Review when")
        if value in ("none", ""):
            continue
        if is_todo(value):
            if not takes_todo(rules, "Review when"):
                report.fail(line, "*Review when* is `TODO`", check, (form,))
            continue
        match = re.match(r"^.+ · check by: (%s)$" % DATE, value)
        if not match or not valid_date(match.group(1)):
            report.error(line, "%s: *Review when* is not `<observable state> · check by: "
                               "YYYY-MM-DD`" % label_of(entry, prefix), check, (form,))


def check_inherited(entries, rules, prefix, report):
    # invariant: inherited-origin-form/1
    check, form = "check_inherited", "inherited-origin-form/1"
    report.ran(check, form)
    for entry in versions_of(entries):
        value, line = field_value(entry, "Origin")
        if re.match(r"^%s\b" % re.escape(rules.inherited_marker), value) and \
                not re.match(rules.inherited_origin, value):
            report.error(line, "%s: *Origin* of an inherited decision is not "
                               "`inherited — searched: <…>; found: <…>`" % label_of(entry, prefix),
                         check, (form,))


def check_references(text, entries, prefix, report, numbers, versions):
    # invariant: log-reference-target/1
    check, target = "check_references", "log-reference-target/1"
    report.ran(check, target)
    opens = {}
    for entry in entries:
        for name, (_, line) in entry.fields.items():
            opens[line] = name
    ref = re.compile(r"\b%s-(\d{2,})(?:/(\d+))?\b" % re.escape(prefix))
    current, start = None, None
    for number, line in enumerate(text.split("\n"), start=1):
        if line.startswith("#"):
            current = None
            if line.startswith("### "):
                # the number a heading opens is its own, or is checked with its review
                line = ref.sub("", line, count=1)
        elif number in opens:
            current, start = opens[number], number
        elif not line.strip():
            current = None
        if current is None:
            what, where = "the text", number
        else:
            what, where = "*%s*" % current, start
        for match in ref.finditer(line):
            if int(match.group(1)) not in numbers:
                report.error(where, "%s names %s, which does not exist" % (what, match.group(0)),
                             check, (target,))
            elif match.group(2) and current in ("Relations", "Outranks") and \
                    (int(match.group(1)), int(match.group(2))) not in versions:
                report.error(where, "%s names %s, which does not exist" % (what, match.group(0)),
                             check)


def check_reviews(entries, rules, prefix, report, numbers, versions):
    # invariant: review-next-check/1
    # invariant: review-named-version/1
    # invariant: log-reference-target/1
    check = "check_reviews"
    dated, named, target = "review-next-check/1", "review-named-version/1", "log-reference-target/1"
    report.ran(check, dated, named, target)
    ref = re.compile(r"\b%s-(\d{2,})/(\d+)\b" % re.escape(prefix))
    for entry in entries:
        if entry.kind != "review":
            continue
        label = label_of(entry, prefix)
        if entry.number not in numbers:
            report.error(entry.line, "%s: %s-%02d does not exist" % (label, prefix, entry.number),
                         check, (target,))
        result = entry.fields.get("Result", ["", entry.line])
        next_check = entry.fields.get("Next check", ["", entry.line])
        not_met, checked_line = False, None
        if result[0] and not is_todo(result[0]):
            form = next((form for form in sorted(rules.result_forms, key=len, reverse=True)
                         if result[0].startswith(form)), None)
            if form is None:
                report.error(result[1], "%s: *Result* has none of the forms in the template"
                             % label, check)
            elif form.startswith("condition not met"):
                not_met = True
                if is_todo(next_check[0]):
                    pass  # check_fields warns
                elif not re.match(r"^%s$" % DATE, next_check[0]):
                    report.error(next_check[1], "%s: `condition not met` needs a date in "
                                                "*Next check*" % label, check, (dated,))
            elif "changed in" in form:
                match = re.match(r"^%s-(\d{2,})/(\d+)$" % re.escape(prefix),
                                 result[0][len(form):].strip())
                if not match:
                    report.error(result[1], "%s: *Result* names a version that does not exist"
                                 % label, check)
                else:
                    checked_line = result[1]
                    if (int(match.group(1)), int(match.group(2))) not in versions:
                        report.error(result[1], "%s: *Result* names a version that does not "
                                                "exist" % label, check, (named,))
        if next_check[0] and not is_todo(next_check[0]) and next_check[0] != "none" and not (
                re.match(r"^%s$" % DATE, next_check[0]) and valid_date(next_check[0])):
            report.error(next_check[1], "%s: *Next check* is neither a date nor `none`" % label,
                         check, (dated,))
        for number, line in enumerate(entry.text.split("\n")[1:], start=entry.line + 1):
            if number == checked_line:
                continue
            for match in ref.finditer(line):
                if (int(match.group(1)), int(match.group(2))) not in versions:
                    report.error(number, "%s: names %s, a version that does not exist"
                                 % (label, match.group(0)), check, (named,))


def merged_log(log_path, entries, merge_onto, prefix, top, report, no_commit=None):
    """The latest version of each number in the log as it stands after the merge onto the given
    commit, as {number: (entry, None or the commit whose log alone holds it, the version that set
    its current fingerprint)}, or None once the
    report says why git could not read the log on that commit. Given `no_commit`, which says why
    there is no commit to merge onto, records the check of the copies unchecked instead.

    Each version is decided against the merge base of HEAD and that commit, as git's merge does.
    The merge holds every version either side added since the merge base, and every version of
    the merge base that neither side removed. A version of the merge base that one side removed
    and the other left as the merge base holds it is gone after the merge; where the other side
    changed it, the changed copy is kept (a conflict git leaves to a person, which no invariant
    covers: log-merge-copies speaks of versions both sides hold). Where both sides hold a version
    with different text, the copy kept is the copy on the commit merged onto where the branch's
    copy reads as on the merge base, so that an edit made on that side alone survives; the
    branch's copy otherwise, where the branch changed the version or both sides wrote it (a
    conflict too). That difference is a failure of log-merge-copies: it is either an edit of an
    entry one side holds, or two versions written under one heading on both sides. Where the
    commit merged onto holds no log, the log after the merge is this log alone."""
    # invariant: log-merge-copies/1
    check, copies = "merged_log", "log-merge-copies/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, copies)
        report.cannot_check("the copies of a version both logs hold", no_commit)
        return None
    relative = os.path.relpath(os.path.abspath(log_path), top).replace(os.sep, "/")
    onto_text, failure = file_at(merge_onto, relative, top)
    if failure:
        report.error(None, failure)
        return None
    report.ran(check, copies)
    if onto_text is None:
        report.notes.append("%s has no %s; the log after the merge is this log alone"
                            % (merge_onto, relative))
    ours = {(entry.number, entry.version): entry for entry in versions_of(entries)}
    theirs = {(entry.number, entry.version): entry
              for entry in versions_of(parse_log(onto_text or "", prefix))}
    # (number, version) -> text on the merge base; a version one side alone holds is decided by it
    on_base = ({} if onto_text is None or ours.keys() == theirs.keys()
               and all(ours[key].text == theirs[key].text for key in ours)
               else log_on_merge_base(relative, merge_onto, prefix, top, report))
    merged = {}
    for key in sorted(ours.keys() | theirs.keys()):
        mine, other = ours.get(key), theirs.get(key)
        if mine is not None and other is not None:
            merged[key] = (mine, None)
            if mine.text == other.text:
                continue
            kept = "this copy"
            if on_base.get(key) == mine.text:
                merged[key] = (other, merge_onto)
                kept = "the copy on %s" % merge_onto
            report.error(mine.line, "%s differs from its copy on %s; the log after the merge "
                                    "holds %s" % (label_of(mine, prefix), merge_onto, kept),
                         check, (copies,))
        # held by one side alone: gone where the other side removed it from the merge base
        # unchanged; kept where it is new since the merge base or this side changed it
        elif mine is not None:
            if on_base.get(key) != mine.text:
                merged[key] = (mine, None)
        elif on_base.get(key) != other.text:
            merged[key] = (other, merge_onto)
    latest, setters = {}, {}
    for (number, _), item in sorted(merged.items()):
        current = item[0].binding
        previous = latest.get(number)
        # the version that set the fingerprint: the first of the run that ends here with it
        if previous is None or not same_binding(previous[0].binding, current):
            setters[number] = item[0]
        latest[number] = item
    return {number: (entry, onto, setters[number]) for number, (entry, onto) in latest.items()}


def same_binding(one, other):
    """Whether two versions' binding sentences give one fingerprint, a repeal's none included."""
    if one is None or other is None:
        return one is None and other is None
    return fingerprint(one) == fingerprint(other)


def log_on_merge_base(relative, merge_onto, prefix, top, report):
    """{(number, version): text} of the log on the merge base of HEAD and the commit merged onto;
    empty where the two have no common ancestor or that commit holds no log, and where git fails,
    once the report says why."""
    code, answer, message = git(["merge-base", "HEAD", merge_onto], top)
    if code != 0 or not answer.strip():
        if code != 1 or message:
            report.error(None, "git cannot find the merge base of HEAD and %s: %s"
                         % (merge_onto, message or "git merge-base exited with %d" % code))
        return {}
    text, failure = file_at(answer.strip(), relative, top)
    if failure:
        report.error(None, failure)
    return {(entry.number, entry.version): entry.text
            for entry in versions_of(parse_log(text or "", prefix))}


def check_merge_todo(entries, prefix, report, no_commit=None):
    """Reports every field of every entry of the log that holds `TODO`, which the main branch does
    not hold (WAY-71). Given `no_commit`, which says why there is no commit to merge onto, records
    it unchecked instead."""
    # invariant: log-entry-merge-todo/1
    check, merge_todo = "check_merge_todo", "log-entry-merge-todo/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, merge_todo)
        report.cannot_check("`TODO` in the log", no_commit)
        return
    report.ran(check, merge_todo)
    for entry in entries:
        if entry.kind not in ("version", "review"):
            continue
        for name, (value, line) in entry.fields.items():
            if is_todo(value):
                report.error(line, "%s: *%s* is `TODO`, which a merge onto the main branch does "
                                   "not take" % (label_of(entry, prefix), name),
                             check, (merge_todo,))


def check_fingerprints(latest, rules, prefix, report, no_commit=None):
    """Compares every fingerprint a relation carries, in the latest version of each number of the
    log after the merge, with the current fingerprint of the decision it names there; a stale one
    is reported with the version that set the current fingerprint and its kind of change. Given
    `no_commit`, which says why there is no commit to merge onto, records it unchecked instead."""
    # invariant: relation-fingerprint-value/1
    check, current_value = "check_fingerprints", "relation-fingerprint-value/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, current_value)
        report.cannot_check("the fingerprints relations carry", no_commit)
        return
    report.ran(check, current_value)
    current = {number: fingerprint(entry.binding) for number, (entry, _, _) in latest.items()
               if entry.binding is not None}
    pattern = re.compile(r"^(.+?) %s-(\d{2,})@([0-9a-f]+)$" % re.escape(prefix))
    for entry, onto, _ in latest.values():
        relations = entry.fields.get("Relations")
        if not relations:
            continue
        where = " (on %s)" % onto if onto else ""
        for item in relations[0].split(" · "):
            match = pattern.match(item.strip())
            if not match or not rules.relation_types.get(match.group(1)):
                continue
            number = int(match.group(2))
            if number in latest and current.get(number) != match.group(3):
                # the flag names the kind of change that raised it (template: Kinds of change)
                setter = latest[number][2]
                kind = change_kind(setter, rules, prefix)
                raised = ("a change of the kind %s" % kind if kind else
                          "whose *Change* names no kind of change")
                report.error(None if onto else relations[1],
                             "%s%s: `%s` — the current fingerprint of %s-%02d is %s, set by %s, %s"
                             % (label_of(entry, prefix), where, item.strip(), prefix, number,
                                current.get(number, "none (no binding sentences)"),
                                label_of(setter, prefix), raised),
                             check, (current_value,))


def check_narrows(latest, prefix, report):
    """No two decisions name each other as `narrows` in their latest versions: the one that
    prevails names the other, never both (WAY-25)."""
    # invariant: narrows-pairs/1
    check, pairs = "check_narrows", "narrows-pairs/1"
    report.ran(check, pairs)
    relation = re.compile(r"^narrows %s-(\d{2,})\b" % re.escape(prefix))
    narrowed = {}
    for number, entry in latest.items():
        value = field_value(entry, "Relations")[0] or ""
        narrowed[number] = {int(match.group(1)) for match in
                            (relation.match(item.strip()) for item in
                             " ".join(value.split()).split(" · ")) if match}
    for number, others in sorted(narrowed.items()):
        for other in sorted(others):
            if other > number and number in narrowed.get(other, set()):
                report.error(field_value(latest[number], "Relations")[1],
                             "%s-%02d and %s-%02d narrow each other"
                             % (prefix, number, prefix, other), check, (pairs,))


def check_review_dates(entries, latest, prefix, report, today):
    for number, version in latest.items():
        review_when = version.fields.get("Review when", ["none"])[0]
        match = re.search(r"check by: (%s)$" % DATE, review_when)
        if not match or not valid_date(match.group(1)):
            continue
        due = match.group(1)
        after = False
        for entry in entries:
            if entry is version:
                after = True
            elif after and entry.kind == "review" and entry.number == number:
                due = entry.fields.get("Next check", ["none"])[0]
        if re.match(r"^%s$" % DATE, due) and valid_date(due) and \
                datetime.date.fromisoformat(due) < today:
            report.warning(version.line, "%s-%02d: check-by date %s has passed without a review "
                                         "record" % (prefix, number, due))


# --- the main branch and the examples ------------------------------------------------------


def git(arguments, cwd):
    """Exit code, output and error output of a call to git."""
    result = subprocess.run(["git"] + arguments, cwd=cwd, capture_output=True)
    return (result.returncode, result.stdout.decode("utf-8", "replace").replace("\r\n", "\n"),
            result.stderr.decode("utf-8", "replace").strip())


def file_at(commit, path, top):
    """(text, None) for the file at the path, relative to the root of the repository, on the
    commit; (None, None) where the commit holds no such path; (None, git's message) where git
    fails for any other reason, so that no check reads a failure as an absent file."""
    code, text, message = git(["show", "%s:%s" % (commit, path)], top)
    if code == 0:
        return text, None
    listed, listing, listing_message = git(["ls-tree", "--full-tree", "-z", "--name-only", commit,
                                            "--", path], top)
    if listed == 0 and not listing:
        return None, None
    return None, "git cannot read %s at %s: %s" % (
        path, commit, message or listing_message or "git show exited with %d" % code)


def find_commit(log_path, option, commit, report):
    """The root of the log's repository, or None once the report says why the commit is not
    there. A failure here is no rule's: it belongs to the run."""
    directory = os.path.dirname(os.path.abspath(log_path))
    code, top, _ = git(["rev-parse", "--show-toplevel"], directory)
    if code != 0:
        report.error(None, "%s %s given, but the log is not in a git repository" % (option, commit))
        return None
    code, _, _ = git(["rev-parse", "--verify", "--quiet", commit + "^{commit}"], directory)
    if code != 0:
        report.error(None, "%s %s does not exist" % (option, commit))
        return None
    return top.strip()


def check_against_base(log_path, text, base, prefix, report, top, no_commit=None):
    """Compares the log with its state on the base, and returns the versions it gains there. Given
    `no_commit`, which says why there is no base, records it unchecked instead."""
    # invariant: log-existing-lines/1
    # invariant: log-versions-added-per-number/1
    check = "check_against_base"
    existing, added_per_number = "log-existing-lines/1", "log-versions-added-per-number/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, existing, added_per_number)
        report.cannot_check("the lines the log holds on the main branch, and the versions it gains "
                            "per number", no_commit)
        return None
    relative = os.path.relpath(os.path.abspath(log_path), top).replace(os.sep, "/")
    base_text, failure = file_at(base, relative, top)
    if failure:
        report.error(None, failure)
        return None
    if base_text is None:
        report.notes.append("%s has no %s; the log is compared with an empty one" % (base, relative))
        base_text = ""
    report.ran(check, existing, added_per_number)

    trimmed = base_text.rstrip("\n")
    base_lines, lines = (trimmed.split("\n") if trimmed else []), text.split("\n")
    if lines[:len(base_lines)] != base_lines:
        line = next((i + 1 for i, (a, b) in enumerate(zip(base_lines, lines)) if a != b),
                    len(lines) + 1)
        report.error(line, "the log differs from %s here; on the main branch it only grows at the "
                           "end" % base, check, (existing,))

    base_versions = {(e.number, e.version) for e in parse_log(base_text, prefix) if e.kind == "version"}
    added = {}
    for entry in parse_log(text, prefix):
        if entry.kind == "version" and (entry.number, entry.version) not in base_versions:
            added.setdefault(entry.number, []).append(entry)
    for number, items in sorted(added.items()):
        if len(items) > 1:
            report.error(items[1].line, "%s-%02d: %d versions added against %s, at most one"
                         % (prefix, number, len(items), base), check, (added_per_number,))
    return added


def check_template_change(top, base, added, report, no_commit=None):
    """Given `no_commit`, which says why there is no base, records the check unchecked."""
    # invariant: decision-template-change/1
    check, change = "check_template_change", "decision-template-change/1"
    if no_commit:
        report.unchecked(check, NO_COMMIT_REASON, no_commit, change)
        report.cannot_check("a change to the template without a new version in the log", no_commit)
        return
    base_template, failure = file_at(base, TEMPLATE_PATH, top)
    if failure:
        report.error(None, failure)
        return
    report.ran(check, change)
    path = os.path.join(top, *TEMPLATE_PATH.split("/"))
    current = None
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            current = handle.read()
    if base_template != current and not added:
        report.error(None, "%s differs from %s, and the log gains no version against it"
                     % (TEMPLATE_PATH, base), check, (change,))


def check_examples(entries, examples_path, prefix, report):
    """Every decision number `examples.md` names is the number of a decision in the log: an
    example names a decision by its number instead of copying it (WAY-05)."""
    # invariant: decision-example-numbers/1
    check, named = "check_examples", "decision-example-numbers/1"
    report.ran(check, named)
    with open(examples_path, encoding="utf-8") as handle:
        examples = handle.read()
    numbers = {entry.number for entry in versions_of(entries)}
    reference = re.compile(r"\b%s-(\d{2,})\b" % re.escape(prefix))
    for line, text in enumerate(examples.split("\n"), start=1):
        for match in reference.finditer(text):
            if int(match.group(1)) not in numbers:
                report.error(None, "examples.md:%d: %s is not a number of the log"
                             % (line, match.group(0)), check, (named,))


# --- entry point ----------------------------------------------------------------------------


def run(log_path, base=None, today=None, template=TEMPLATE, examples=EXAMPLES, stream=None,
        merge_onto=None, record=None, approver=None):
    stream = stream or sys.stdout
    if record is not None:
        try:
            start_record(record)
        except OSError as problem:
            stream.write("cannot write the record: %s\n" % problem)
            return 2
    report = Report(log_path, [option for option, value in (("--base", base),
                                                             ("--merge-onto", merge_onto)) if value])

    def stop(message):
        stream.write(message + "\n")
        report.error(None, message)
        if record is not None:
            write_record(record, report)
        return 2

    try:
        rules = read_rules(template)
    except (OSError, TemplateError, AttributeError) as problem:
        return stop("cannot read the rules from %s: %s" % (template, problem))
    try:
        with open(log_path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as problem:
        return stop("cannot read the log: %s" % problem)

    prefix = detect_prefix(text)
    if prefix is None:
        report.notes.append("the log has no entries")
        report.print(stream)
        if record is not None:
            write_record(record, report)
        return 0
    entries = parse_log(text, prefix)
    own = os.path.exists(OWN_LOG) and os.path.samefile(log_path, OWN_LOG)
    if approver is None and own:
        approver = OWN_APPROVER
    check_log(entries, text, rules, prefix, report, today or datetime.date.today(), approver)
    if approver is None:
        report.notes.append("who approves a version is checked only in the-way's own log")

    if base == NO_COMMIT:
        no_base = shared.NO_BASE
        check_against_base(log_path, text, None, prefix, report, None, no_commit=no_base)
        check_template_change(None, None, None, report, no_commit=no_base)
    elif base:
        top = find_commit(log_path, "--base", base, report)
        if top is not None:
            added = check_against_base(log_path, text, base, prefix, report, top)
            if added is not None:
                check_template_change(top, base, added, report)
    else:
        report.notes.append("no --base given: the checks against the main branch are not run, and "
                            "are not counted in the last line")

    if merge_onto == NO_COMMIT:
        no_onto = shared.NO_MERGE_ONTO
        check_merge_todo(entries, prefix, report, no_commit=no_onto)
        merged_log(log_path, entries, merge_onto, prefix, None, report, no_commit=no_onto)
        check_fingerprints(None, rules, prefix, report, no_commit=no_onto)
    elif merge_onto:
        top = find_commit(log_path, "--merge-onto", merge_onto, report)
        if top is not None:
            check_merge_todo(entries, prefix, report)
            latest = merged_log(log_path, entries, merge_onto, prefix, top, report)
            if latest is not None:
                check_fingerprints(latest, rules, prefix, report)
    else:
        report.notes.append("no --merge-onto given: `TODO` in the log is not checked against a "
                            "merge, the copies of a version both logs hold are not compared, and "
                            "the fingerprints relations carry are not compared with the current "
                            "binding part; those checks are not run, and are not counted in the "
                            "last line")

    if os.path.exists(examples) and own:
        check_examples(entries, examples, prefix, report)

    report.print(stream)
    if record is not None:
        write_record(record, report)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a decision log against its template.")
    parser.add_argument("log", nargs="?", default=os.path.join("foundations", "decisions.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from, "
                                         "to compare the log with; `none` where it does not "
                                         "exist, which records those checks as unchecked")
    parser.add_argument("--merge-onto", help="the commit of the main branch a merge is made onto; "
                                             "only with it are the copies of a version both logs "
                                             "hold compared, the fingerprints relations carry "
                                             "compared with the current binding part, and `TODO` in "
                                             "the log reported as an error; `none` where the main "
                                             "branch does not exist, which records those checks "
                                             "as unchecked")
    parser.add_argument("--today", type=datetime.date.fromisoformat,
                        help="the date passed check-by dates are measured against")
    parser.add_argument("--record", help="the JSON Lines file, created or overwritten, that "
                                         "receives a verdict for each invariant a check cites")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.log, arguments.base, arguments.today, merge_onto=arguments.merge_onto,
               record=arguments.record)


if __name__ == "__main__":
    sys.exit(main())
