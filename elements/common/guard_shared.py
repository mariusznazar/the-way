"""Code the format guards of the elements share (WAY-09): reading a file and the sections and
fields of an entry, reading the rules of form the elements share from `rules.md` beside this
module, the report of a run and the-way's own record of it (WAY-74), and the calls to git. A guard
loads this module by its path; the form of an identifier and of a version comes from the relation
model (`relation-model/identifier.py`), and what each guard checks stays in the guard of its
element.
"""

import json
import os
import re
import subprocess

# The rules of form the elements share (WAY-09, WAY-35).
COMMON_RULES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rules.md")

# The value the gate fills in for a commit that does not exist (WAY-61), and the reason a check
# that needs that commit records for being unchecked, word for word as the invariants template
# lists it (WAY-63).
NO_COMMIT = "none"
NO_COMMIT_REASON = "the method takes a commit the gate filled in as not existing"

# `TODO` as a word of its own anywhere in a value — whole, as an item, or inside a part such as
# `detected by TODO` or `searched: TODO; found: …` — but not inside a path or a longer word, such
# as `docs/TODO.md` (WAY-71).
TODO_WORD = re.compile(r"(?:^|[\s;,:(`])TODO(?=$|[\s;,:)`])")


# --- files, sections and fields -------------------------------------------------------------


def read_file(path, report, what):
    """The text of a file, or None once the report holds why it cannot be read: a failure of the
    run, recorded by every run whatever its options."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError) as problem:
        report.error(None, "cannot read %s: %s" % (what, problem))
        return None


def split_sections(text):
    """(line number of the heading, the lines of the section) for every `## ` section."""
    lines = text.split("\n")
    starts = [index for index, line in enumerate(lines) if line.startswith("## ")]
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        yield start + 1, lines[start:end]


def parse_fields(body, first_line):
    """field name -> [value, line] for every `- **Name:** value` of an entry, its indented
    continuation lines included; the first occurrence of a name counts."""
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


# --- rules read from a template and from the rules the elements share ------------------------


class TemplateError(Exception):
    """A template, or the rules the elements share, does not hold a form a guard reads."""


def template_section(text, title):
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


def markdown_blocks(section_text):
    """The Markdown code blocks of a section, without their fences."""
    return re.findall(r"```markdown\n(.*?)```", section_text, re.S)


def table_form(block):
    """(title, columns) of a list whose form a code block gives as a heading and a table header."""
    title = re.search(r"^## (.+)$", block, re.M)
    header = re.search(r"^\|(.+)\|$", block, re.M)
    if not title or not header:
        raise TemplateError("a list form has no title or no columns")
    return title.group(1).strip(), [cell.strip() for cell in header.group(1).split("|")]


def _dedented(block):
    """A block of a list item, its lines freed of the indentation that places it in the item."""
    return "\n".join(line.strip() for line in block.split("\n"))


def read_common(path=COMMON_RULES):
    """(fields the main branch holds `TODO` in for an invariant, (title, columns) of the list of
    withdrawn identifiers, name of the file of human verdicts, columns of its row), read from the
    rules of form the elements share."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    main = re.search(r"The main branch holds `TODO` only in (.*?)\(WAY-71\)",
                     " ".join(text.split()))
    if not main:
        raise TemplateError("the rules the elements share do not say which fields the main branch "
                            "holds `TODO` in")
    main_todo = re.findall(r"an invariant's (?:or an environment fact's )?\*([^*]+)\*",
                           main.group(1))
    withdrawn = [_dedented(block)
                 for block in markdown_blocks(template_section(text, "Withdrawn identifiers"))]
    if not withdrawn:
        raise TemplateError("the rules the elements share give no form of the list of withdrawn "
                            "identifiers")
    verdicts = template_section(text, "Human verdicts")
    verdicts_file = re.search(r"`foundations/(human_[^`]+\.md)`", verdicts)
    verdicts_header = re.search(r"^\s*\|(.+)\|\s*$", "\n".join(markdown_blocks(verdicts)), re.M)
    if not verdicts_file or not verdicts_header:
        raise TemplateError("the rules the elements share name no file of human verdicts or no "
                            "form of its row")
    return (main_todo, table_form(withdrawn[0]), verdicts_file.group(1),
            [cell.strip() for cell in verdicts_header.group(1).split("|")])


# --- the report and the record of a run -----------------------------------------------------


def describe(line, message):
    return "line %d: %s" % (line, message) if line else message


class Report:
    """What a person reads, and the record of the run the gate reads (WAY-74).

    A check that runs names the invariants it cites with ran(); an error or a failure it finds
    names the check and the invariants the finding makes false. A check with no finding for an
    invariant it cites records `pass`; a check that cannot decide an invariant for a reason on the
    invariants template's list names it with unchecked() and records `unchecked` beside that
    reason and a description of the case, unless it found a failure of that invariant as well. An
    error that names no invariant is a failure recorded for no entry, and one that names no check
    is a failure of the run itself. The record holds the checks of the options the run was given,
    or of the file alone when it was given none; the report for a person holds every check.

    The last line of the report counts what the person is told was left unchecked, one for each
    `unchecked:` line a check names with cannot_check(): a check needing a commit given as `none`,
    a command the product does not yet declare or produce, a file that cannot be read. It is not a
    count of the record's `unchecked` verdicts, which stand one for each check and invariant.
    Checks left out because an option was not given stand in notes, and are not counted.

    Each guard gives the name of its program and the checks each of its options selects
    (`selected_by`: check -> option); every other check reads the file alone.
    """

    def __init__(self, path, options=(), program=None, selected_by=None):
        self.path = path
        self.options = set(options)
        self.program = program
        self.selected_by = selected_by or {}
        self.errors = []
        self.warnings = []
        self.not_checked = []   # (what, why), printed for a person as `unchecked:`
        self.notes = []
        self.order = []         # (check, invariant) in the order a check first named it
        self.verdicts = {}      # (check, invariant) -> descriptions of its failures
        self.skipped = {}       # (check, invariant) -> (the reason it is unchecked, description)
        self.unowned = []       # (check or None, description) of errors that belong to no invariant

    def _name(self, check, invariant):
        if (check, invariant) not in self.verdicts and (check, invariant) not in self.skipped:
            self.order.append((check, invariant))

    def ran(self, check, *invariants):
        for invariant in invariants:
            self._name(check, invariant)
            self.verdicts.setdefault((check, invariant), [])

    def unchecked(self, check, reason, description, *invariants):
        for invariant in invariants:
            self._name(check, invariant)
            self.skipped.setdefault((check, invariant), (reason, description))

    def fail(self, line, message, check, invariants):
        """Records a failure of each invariant, without a line in the report for a person."""
        for invariant in invariants:
            self._name(check, invariant)
            self.verdicts.setdefault((check, invariant), []).append(describe(line, message))

    def error(self, line, message, check=None, invariants=()):
        self.errors.append((line, message))
        if invariants:
            self.fail(line, message, check, invariants)
        else:
            self.unowned.append((check, describe(line, message)))

    def warning(self, line, message):
        self.warnings.append((line, message))

    def cannot_check(self, what, why):
        self.not_checked.append((what, why))

    def print(self, stream):
        for level, items in (("error", self.errors), ("warning", self.warnings)):
            for line, message in sorted(items, key=lambda item: item[0] or 0):
                stream.write("%s:%s: %s: %s\n" % (self.path, line or 0, level, message))
        for what, why in self.not_checked:
            stream.write("unchecked: %s — %s\n" % (what, why))
        for note in self.notes:
            stream.write("note: %s\n" % note)
        stream.write("%d error(s), %d warning(s), %d unchecked\n"
                     % (len(self.errors), len(self.warnings), len(self.not_checked)))

    def recorded(self, check):
        if check is None:
            return True
        if self.options:
            return self.selected_by.get(check) in self.options
        return check not in self.selected_by

    def record(self):
        lines = []
        for check, invariant in self.order:
            if not self.recorded(check):
                continue
            name = "%s::%s" % (self.program, check)
            failures = self.verdicts.get((check, invariant), [])
            for description in failures:
                lines.append({"check": name, "verdict": "fail", "invariant": invariant,
                              "description": description})
            if failures:
                continue
            if (check, invariant) in self.skipped:
                reason, description = self.skipped[(check, invariant)]
                lines.append({"check": name, "verdict": "unchecked", "invariant": invariant,
                              "reason": reason, "description": description})
            else:
                lines.append({"check": name, "verdict": "pass", "invariant": invariant})
        for check, description in self.unowned:
            if self.recorded(check):
                lines.append({"check": "%s::%s" % (self.program, check) if check else self.program,
                              "verdict": "fail", "invariant": None, "description": description})
        return lines


def start_record(path):
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    open(path, "w", encoding="utf-8").close()


def write_record(path, report):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        for line in report.record():
            handle.write(json.dumps(line, ensure_ascii=False) + "\n")


# --- git ------------------------------------------------------------------------------------


def git(arguments, cwd, stdin=None):
    """Exit code and output of a call to git."""
    return call_git(arguments, cwd, stdin)[:2]


def call_git(arguments, cwd, stdin=None):
    """Exit code, output and error output of a call to git."""
    try:
        result = subprocess.run(["git"] + arguments, cwd=cwd, capture_output=True,
                                input=stdin.encode("utf-8") if stdin is not None else None)
    except OSError as problem:
        return 127, "", str(problem)
    return (result.returncode, result.stdout.decode("utf-8", "replace").replace("\r\n", "\n"),
            result.stderr.decode("utf-8", "replace").strip())


def file_at(commit, path, top):
    """(text, None) for the file at the path, relative to the root of the repository, on the
    commit; (None, None) where the commit holds no such path; (None, git's message) where git
    fails for any other reason, so that no check reads a failure as an absent file."""
    code, text, message = call_git(["show", "%s:%s" % (commit, path)], top)
    if code == 0:
        return text, None
    listed, listing, listing_message = call_git(["ls-tree", "--full-tree", "-z", "--name-only",
                                                 commit, "--", path], top)
    if listed == 0 and not listing:
        return None, None
    return None, "git cannot read %s at %s: %s" % (
        path, commit, message or listing_message or "git show exited with %d" % code)


def find_commit(top, option, commit, report):
    """Whether the commit exists; where it does not, the report says so. A failure here is no
    rule's: it belongs to the run."""
    code, _, _ = call_git(["rev-parse", "--verify", "--quiet", commit + "^{commit}"], top)
    if code != 0:
        report.error(None, "%s %s does not exist" % (option, commit))
        return False
    return True
