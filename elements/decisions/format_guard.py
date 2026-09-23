"""Format guard of a product's decision log.

Runs the checks listed in "What the format guard checks" in template.md, which lies next to this
script. Field names, kinds of change, relation types, forms of a review result and forbidden
words are read from the template, so the rules of the entry live in one place (WAY-05, WAY-35).

Usage, from the root of the product's repository:

    python <the-way>/elements/decisions/format_guard.py [LOG] [--base REF] [--today YYYY-MM-DD]

LOG defaults to foundations/decisions.md. --base names the commit the task branch left the main
branch from, to compare the log with; without it, the two checks that need it are skipped. Exit
code: 0 without errors, 1 with errors, 2 when the log or the template cannot be read.
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "template.md")
EXAMPLES = os.path.join(HERE, "examples.md")
OWN_LOG = os.path.join(HERE, "..", "..", "foundations", "decisions.md")

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "relation-model"))
from fingerprint import fingerprint  # noqa: E402

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

    kinds = {}
    for line in _section(text, "Kinds of change").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) >= 3 and cells[0] not in ("Kind", "") \
                and not set(cells[0]) <= set("-"):
            kinds[cells[0]] = cells[2]

    relations_line = re.search(r"^- \*\*Relations:\*\* (.*)$", version_form, re.M).group(1)
    relation_types = {}
    for item in relations_line.split(" | ")[0].split(" · "):
        match = re.match(r"^(.+?) [A-Z]+-\w+(@<fingerprint>)?$", item.strip())
        if not match:
            raise TemplateError("cannot read relation type from %r" % item)
        relation_types[match.group(1)] = bool(match.group(2))

    checks = _section(text, "What the format guard checks")
    binding_check = re.search(r"^- Binding sentences: (.*)$", checks, re.M)
    if not binding_check:
        raise TemplateError("no check of binding sentences in the list of checks")
    count = re.search(r"to (\w+);", binding_check.group(1))
    if not count or count.group(1) not in NUMBER_WORDS:
        raise TemplateError("cannot read the number of binding sentences")
    forbidden_words = re.findall(r"\*(\w+)\*", binding_check.group(1))

    keywords = re.search(r"keywords of RFC 2119 in capitals \(([^)]*)\)",
                         " ".join(_section(text, "Binding sentences").split()))
    if not keywords:
        raise TemplateError("no list of RFC 2119 keywords")

    if not (version_fields and prose_fields and review_fields and kinds and result_forms):
        raise TemplateError("the entry forms are incomplete")
    return Rules(version_fields, prose_fields, renamed, review_fields, kinds, relation_types,
                 forbidden_words, [k.strip() for k in keywords.group(1).split(",")],
                 NUMBER_WORDS[count.group(1)], result_forms)


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
    match = re.search(r"^### ([A-Z][A-Z0-9]*)-\d", text, re.M)
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


# --- checks ---------------------------------------------------------------------------------


class Report:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.notes = []

    def error(self, line, message):
        self.errors.append((line, message))

    def warning(self, line, message):
        self.warnings.append((line, message))

    def print(self, stream):
        for level, items in (("error", self.errors), ("warning", self.warnings)):
            for line, message in sorted(items, key=lambda item: item[0] or 0):
                stream.write("%s:%s: %s: %s\n" % (self.path, line or 0, level, message))
        for note in self.notes:
            stream.write("note: %s\n" % note)
        stream.write("%d error(s), %d warning(s)\n" % (len(self.errors), len(self.warnings)))


def without_code(text):
    return re.sub(r"`[^`]*`", "Code", text)


def count_sentences(text):
    flat = " ".join(without_code(text).split())
    ends = len(re.findall(r"[.!?](?=\s+[\"'(A-Z]|$)", flat))
    return ends if re.search(r"[.!?]$", flat) else ends + 1


def is_todo(value):
    return value == "TODO" or value.startswith("TODO ")


def valid_date(value):
    try:
        datetime.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def check_log(entries, rules, prefix, report, today):
    numbers = {}
    versions = {}
    for entry in entries:
        if entry.kind == "unknown":
            report.error(entry.line, "heading is neither `### %s-NN/V — <question>` nor "
                                     "`### %s-NN · review YYYY-MM-DD`" % (prefix, prefix))
        elif entry.kind == "version":
            expected = len(numbers.get(entry.number, [])) + 1
            if entry.version != expected:
                report.error(entry.line, "%s-%02d: version %d where version %d is next"
                             % (prefix, entry.number, entry.version, expected))
            numbers.setdefault(entry.number, []).append(entry)
            versions[(entry.number, entry.version)] = entry

    latest = {number: items[-1] for number, items in numbers.items()}
    ref = re.compile(r"\b%s-(\d{2,})(?:/(\d+))?\b" % re.escape(prefix))

    def check_reference(entry, line, text, what):
        for match in ref.finditer(text):
            number, version = int(match.group(1)), match.group(2)
            if number not in numbers:
                report.error(line, "%s names %s, which does not exist" % (what, match.group(0)))
            elif version and (number, int(version)) not in versions:
                report.error(line, "%s names %s, which does not exist" % (what, match.group(0)))

    for entry in entries:
        if entry.kind == "version":
            check_version(entry, rules, prefix, report, versions, check_reference)
        elif entry.kind == "review":
            check_review(entry, rules, prefix, report, numbers, versions)

    check_fingerprints(latest, rules, prefix, report)
    check_outranks(latest, prefix, report)
    check_review_dates(entries, latest, prefix, report, today)


def check_fields(entry, names, report, allow_todo_warning=True):
    for name in names:
        if name not in entry.fields or not entry.fields[name][0]:
            report.error(entry.line, "field *%s* is missing" % name)
        elif is_todo(entry.fields[name][0]):
            if name == "Approved by":
                report.error(entry.fields[name][1], "*Approved by* is `TODO`")
            else:
                report.warning(entry.fields[name][1], "*%s* is `TODO`" % name)


def check_version(entry, rules, prefix, report, versions, check_reference):
    label = "%s-%02d/%d" % (prefix, entry.number, entry.version)
    prose = [rules.renamed_after_first.get(name, name) if entry.version > 1 else name
             for name in rules.prose_fields]
    check_fields(entry, rules.version_fields + prose, report)
    for name, renamed in rules.renamed_after_first.items():
        wrong = renamed if entry.version == 1 else name
        if wrong in entry.fields:
            report.error(entry.fields[wrong][1], "%s: version %d uses *%s*"
                         % (label, entry.version, wrong))

    change = entry.fields.get("Change", ["", entry.line])
    kind = None
    if change[0] and not is_todo(change[0]):
        if entry.version == 1:
            if change[0] != "new decision":
                report.error(change[1], "%s: *Change* of version 1 is not `new decision`" % label)
            kind = "new decision"
        else:
            match = re.match(r"^(.+?) · previous: (%s-\d{2,}/\d+)$" % re.escape(prefix), change[0])
            if not match:
                report.error(change[1], "%s: *Change* is not `<kind> · previous: %s-NN/V`"
                             % (label, prefix))
            else:
                kind = match.group(1)
                if kind not in rules.kinds or kind == "new decision":
                    report.error(change[1], "%s: `%s` is not a kind of change" % (label, kind))
                    kind = None
                expected = "%s-%02d/%d" % (prefix, entry.number, entry.version - 1)
                if match.group(2) != expected:
                    report.error(change[1], "%s: `previous:` names %s instead of %s"
                                 % (label, match.group(2), expected))
                check_reference(entry, change[1], match.group(2), "`previous:`")

    rule = rules.kinds.get(kind)
    if rule == "none":
        if entry.binding is not None:
            report.error(entry.line + 2, "%s: a %s has no binding sentences" % (label, kind))
    elif entry.binding is None:
        report.error(entry.line, "%s: binding sentences are missing" % label)
    else:
        check_binding(entry, label, rules, report)
        previous = versions.get((entry.number, entry.version - 1))
        if rule == "identical" and previous is not None and (
                previous.binding is None or fingerprint(previous.binding) != fingerprint(entry.binding)):
            report.error(entry.line + 2, "%s: a %s keeps the binding sentences of %s-%02d/%d"
                         % (label, kind, prefix, entry.number, entry.version - 1))

    for name in ("Relations", "Outranks"):
        if name in entry.fields:
            check_reference(entry, entry.fields[name][1], entry.fields[name][0], "*%s*" % name)
    relations = entry.fields.get("Relations")
    if relations and relations[0] not in ("none", "") and not is_todo(relations[0]):
        for item in relations[0].split(" · "):
            match = re.match(r"^(.+?) (%s-\d{2,})(@[0-9a-f]+)?$" % re.escape(prefix), item.strip())
            if not match or match.group(1) not in rules.relation_types:
                report.error(relations[1], "%s: relation `%s` is not of a known type"
                             % (label, item.strip()))
            elif rules.relation_types[match.group(1)] and not match.group(3):
                report.error(relations[1], "%s: `%s` carries no fingerprint" % (label, item.strip()))
            elif not rules.relation_types[match.group(1)] and match.group(3):
                report.error(relations[1], "%s: `%s` carries a fingerprint" % (label, item.strip()))

    approved = entry.fields.get("Approved by")
    if approved and approved[0] and not is_todo(approved[0]):
        match = re.match(r"^.+, (%s)$" % DATE, approved[0])
        if not match or not valid_date(match.group(1)):
            report.error(approved[1], "%s: *Approved by* is not `<who>, YYYY-MM-DD`" % label)

    review_when = entry.fields.get("Review when")
    if review_when and review_when[0] not in ("none", "") and not is_todo(review_when[0]):
        match = re.match(r"^.+ · check by: (%s)$" % DATE, review_when[0])
        if not match or not valid_date(match.group(1)):
            report.error(review_when[1], "%s: *Review when* is not "
                                         "`<observable state> · check by: YYYY-MM-DD`" % label)


def check_binding(entry, label, rules, report):
    line = entry.line + 2
    sentences = count_sentences(entry.binding)
    if not 1 <= sentences <= rules.max_sentences:
        report.error(line, "%s: %d binding sentences, at most %d"
                     % (label, sentences, rules.max_sentences))
    plain = re.sub(r"`[^`]*`", "", entry.binding)
    for word in rules.forbidden_words:
        if re.search(r"\b%s\b" % re.escape(word), plain, re.I):
            report.error(line, "%s: binding sentences use *%s*" % (label, word))
    for keyword in rules.keywords:
        if re.search(r"\b%s\b" % re.escape(keyword), plain):
            report.error(line, "%s: binding sentences use %s" % (label, keyword))


def check_review(entry, rules, prefix, report, numbers, versions):
    label = "%s-%02d · review %s" % (prefix, entry.number, entry.date)
    check_fields(entry, rules.review_fields, report)
    if entry.number not in numbers:
        report.error(entry.line, "%s: %s-%02d does not exist" % (label, prefix, entry.number))
    result = entry.fields.get("Result", ["", entry.line])
    next_check = entry.fields.get("Next check", ["", entry.line])
    if result[0] and not is_todo(result[0]):
        form = next((form for form in sorted(rules.result_forms, key=len, reverse=True)
                     if result[0].startswith(form)), None)
        if form is None:
            report.error(result[1], "%s: *Result* has none of the forms in the template" % label)
        elif form.startswith("condition not met") and not re.match(r"^%s$" % DATE, next_check[0]):
            report.error(next_check[1], "%s: `condition not met` needs a date in *Next check*"
                         % label)
        elif "changed in" in form:
            match = re.match(r"^%s-(\d{2,})/(\d+)$" % re.escape(prefix),
                             result[0][len(form):].strip())
            if not match or (int(match.group(1)), int(match.group(2))) not in versions:
                report.error(result[1], "%s: *Result* names a version that does not exist" % label)
    if next_check[0] and not is_todo(next_check[0]) and next_check[0] != "none" and not (
            re.match(r"^%s$" % DATE, next_check[0]) and valid_date(next_check[0])):
        report.error(next_check[1], "%s: *Next check* is neither a date nor `none`" % label)


def check_fingerprints(latest, rules, prefix, report):
    current = {number: fingerprint(entry.binding) for number, entry in latest.items()
               if entry.binding is not None}
    pattern = re.compile(r"^(.+?) %s-(\d{2,})@([0-9a-f]+)$" % re.escape(prefix))
    for entry in latest.values():
        relations = entry.fields.get("Relations")
        if not relations:
            continue
        for item in relations[0].split(" · "):
            match = pattern.match(item.strip())
            if not match or not rules.relation_types.get(match.group(1)):
                continue
            number = int(match.group(2))
            if number in latest and current.get(number) != match.group(3):
                report.error(relations[1], "%s-%02d/%d: `%s` — the current fingerprint of %s-%02d "
                             "is %s" % (prefix, entry.number, entry.version, item.strip(), prefix,
                                        number, current.get(number, "none (no binding sentences)")))


def check_outranks(latest, prefix, report):
    outranks = {}
    for number, entry in latest.items():
        value = entry.fields.get("Outranks", ["none"])[0]
        outranks[number] = {int(n) for n in re.findall(r"\b%s-(\d{2,})\b" % re.escape(prefix), value)}
    for number, others in sorted(outranks.items()):
        for other in sorted(others):
            if other > number and number in outranks.get(other, set()):
                report.error(latest[number].fields["Outranks"][1],
                             "%s-%02d and %s-%02d outrank each other" % (prefix, number, prefix, other))


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
            report.warning(version.line, "%s-%02d: check-by date %s has passed without a review"
                           % (prefix, number, due))


# --- the main branch and the examples ------------------------------------------------------


def git(arguments, cwd):
    result = subprocess.run(["git"] + arguments, cwd=cwd, capture_output=True)
    return result.returncode, result.stdout.decode("utf-8", "replace").replace("\r\n", "\n")


def check_against_base(log_path, text, base, prefix, report):
    directory = os.path.dirname(os.path.abspath(log_path))
    code, top = git(["rev-parse", "--show-toplevel"], directory)
    if code != 0:
        report.error(None, "--base %s given, but the log is not in a git repository" % base)
        return
    code, _ = git(["rev-parse", "--verify", "--quiet", base + "^{commit}"], directory)
    if code != 0:
        report.error(None, "--base %s does not exist" % base)
        return
    relative = os.path.relpath(os.path.abspath(log_path), top.strip()).replace(os.sep, "/")
    code, base_text = git(["show", "%s:%s" % (base, relative)], directory)
    if code != 0:
        report.notes.append("%s has no %s; the log is compared with an empty one" % (base, relative))
        base_text = ""

    trimmed = base_text.rstrip("\n")
    if not text.startswith(trimmed):
        base_lines, lines = trimmed.split("\n"), text.split("\n")
        line = next((i + 1 for i, (a, b) in enumerate(zip(base_lines, lines)) if a != b),
                    min(len(base_lines), len(lines)) + 1)
        report.error(line, "the log differs from %s here; on the main branch it only grows at the "
                           "end" % base)

    base_versions = {(e.number, e.version) for e in parse_log(base_text, prefix) if e.kind == "version"}
    added = {}
    for entry in parse_log(text, prefix):
        if entry.kind == "version" and (entry.number, entry.version) not in base_versions:
            added.setdefault(entry.number, []).append(entry)
    for number, items in sorted(added.items()):
        if len(items) > 1:
            report.error(items[1].line, "%s-%02d: %d versions added against %s, at most one"
                         % (prefix, number, len(items), base))


def check_examples(entries, examples_path, report):
    with open(examples_path, encoding="utf-8") as handle:
        examples = handle.read()
    by_heading = {entry.heading: entry for entry in entries}
    for line, lines in split_entries(examples):
        heading = lines[0]
        copy = "\n".join(lines).rstrip()
        entry = by_heading.get(heading)
        if entry is None:
            report.error(None, "examples.md:%d: `%s` is not in the log" % (line, heading))
        elif entry.text != copy:
            copy_lines, log_lines = copy.split("\n"), entry.text.split("\n")
            offset = next((i for i, (a, b) in enumerate(zip(copy_lines, log_lines)) if a != b),
                          min(len(copy_lines), len(log_lines)))
            report.error(entry.line + offset, "examples.md:%d differs from the log"
                         % (line + offset))


# --- entry point ----------------------------------------------------------------------------


def run(log_path, base=None, today=None, template=TEMPLATE, examples=EXAMPLES, stream=None):
    stream = stream or sys.stdout
    try:
        rules = read_rules(template)
    except (OSError, TemplateError, AttributeError) as problem:
        stream.write("cannot read the rules from %s: %s\n" % (template, problem))
        return 2
    try:
        with open(log_path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as problem:
        stream.write("cannot read the log: %s\n" % problem)
        return 2

    report = Report(log_path)
    prefix = detect_prefix(text)
    if prefix is None:
        report.notes.append("the log has no entries")
        report.print(stream)
        return 0
    entries = parse_log(text, prefix)
    check_log(entries, rules, prefix, report, today or datetime.date.today())

    if base:
        check_against_base(log_path, text, base, prefix, report)
    else:
        report.notes.append("no --base given: the checks against the main branch are skipped")

    if os.path.exists(examples) and os.path.exists(OWN_LOG) and \
            os.path.samefile(log_path, OWN_LOG):
        check_examples(entries, examples, report)

    report.print(stream)
    return 1 if report.errors else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a decision log against its template.")
    parser.add_argument("log", nargs="?", default=os.path.join("foundations", "decisions.md"))
    parser.add_argument("--base", help="the commit the task branch left the main branch from, "
                                         "to compare the log with")
    parser.add_argument("--today", type=datetime.date.fromisoformat,
                        help="the date passed check-by dates are measured against")
    arguments = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    return run(arguments.log, arguments.base, arguments.today)


if __name__ == "__main__":
    sys.exit(main())
