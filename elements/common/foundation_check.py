"""Check of a product's foundation: identifiers, references and the files of the part map.

Usage, from anywhere:

    python -B <the-way>/elements/common/foundation_check.py [ROOT]

ROOT is a directory of the product's git repository, the working directory by default; the whole
repository it lies in is checked: the files of `foundations/`, the files of `guidelines/` and
every other file git tracks. The script reads files and asks git; it writes nothing.

What it reports, each as `path:line: message`:

- an identifier standing twice: a decision number in the decision log; an identifier among the
  entries and withdrawn identifiers of the invariants, the environment facts and the part map
  together; a term of the glossary. Old headings are read too: a decision `PREFIX-NN/V` may stand
  in several versions, each once, and a heading `identifier/V` names `identifier`;
- a withdrawn identifier naming an entry again, which is the same identifier standing twice, and a
  successor of a withdrawn identifier that is neither an entry nor a withdrawn identifier of the
  same file;
- a reference that names no entry, or a withdrawn one: a decision number with the log's prefix
  anywhere in a file git tracks; the parts a decision's *Scope*, an invariant's *Part*, a part's
  *Depends on*, a flow's *Parts* and guidelines' *Applies to* name; the invariants a decision's
  *Verification* (after `invariants:`), a flow's *Invariant*, a failure mode's `detected by`, the
  lists of violated, quarantined and recovered invariants, a guidelines rule's *Invariant* and a
  comment line `invariant: <identifier>` in a file other than Markdown name; the facts an
  invariant's *Rests on* and a comment line `fact: <identifier>` name; and a reference written
  `<identifier>@<fingerprint>` in a decision's *Based on* (a fact) and in guidelines outside
  fenced code (an invariant). Old references are read too: `ID@<fingerprint>` and `ID/<version>`
  name `ID`;
- a file git tracks that no part's *Files* claims, or that two parts claim, by path patterns git
  itself matches, letter case counting, unless the map lists it under `Files left out on purpose`;
  and a file on that list that a part claims.

Exit code: 0 without errors, 1 with errors, 2 when it cannot run — ROOT lies in no git repository,
or git cannot list or match its files.
"""

import os
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

DECISIONS = "foundations/decisions.md"
INVARIANTS = "foundations/invariants.md"
FACTS = "foundations/environment_facts.md"
GLOSSARY = "foundations/glossary.md"
PART_MAP = "foundations/part_map.md"
VIOLATED = "foundations/violated_invariants.md"
GUIDELINES = re.compile(r"^guidelines/[^/]+\.md$")
WITHDRAWN = "Withdrawn identifiers"
LEFT_OUT = "Files left out on purpose"

WORDS = r"[a-z0-9]+(?:-[a-z0-9]+)*"
# An identifier, with what the old form put after it: `@<fingerprint>` or `/<version>`.
NAMED = re.compile(r"(%s)(?:@[0-9a-z]+|/[0-9]+)?" % WORDS)
ENTRY = re.compile(r"^## (%s)(?:/[0-9]+)?\s*$" % WORDS)
FINGERPRINTED = re.compile(r"(?<![A-Za-z0-9./@-])(%s)@[0-9a-f]{8}(?![0-9A-Za-z])" % WORDS)
NAMED_ANY = r"(?:%s)(?:[@/][0-9a-z]+)?" % WORDS
VERIFIED = re.compile(r"invariants:\s*(%s(?:\s*·\s*%s)*)" % (NAMED_ANY, NAMED_ANY))
DETECTED = re.compile(r"detected\s+by\s+(%s)" % WORDS)
# A comment line reading `invariant:` or `fact:` cites all that follows, which is one word.
CITATION = re.compile(r"^\s*(?:#|//|--|;|%|\*|/\*|<!--|REM\b)\s*(invariant|fact):(.*?)"
                      r"(?:\*/|-->)?\s*$")
ITEM = re.compile(r"[^·,\n]+")
FIELD = re.compile(r"^- \*\*(.+?):\*\*(?: (.*))?$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
EMPTY = ("none", "TODO")


class Report:
    def __init__(self):
        self.errors = {}

    def error(self, path, line, message):
        where = "%s:%d" % (path, line) if line else path
        self.errors.setdefault("%s: %s" % (where, message), None)


def git(root, *args, stdin=None):
    """(exit code, output) of git, or (None, why) where git cannot be started."""
    try:
        result = subprocess.run(["git", *args], cwd=root, input=stdin, capture_output=True,
                                text=True, encoding="utf-8")
    except OSError as error:
        return None, str(error)
    return result.returncode, result.stdout


def read(root, path):
    """The lines of a file, or none where it cannot be read as UTF-8 text."""
    try:
        with open(os.path.join(root, *path.split("/")), encoding="utf-8") as handle:
            return handle.read().split("\n")
    except (OSError, UnicodeDecodeError):
        return []


def blocks(lines, level):
    """(line number, heading, [(line number, line)]) of each block a heading of a level opens."""
    found, current = [], None
    for number, line in enumerate(lines, start=1):
        if line.startswith("#"):
            current = [] if line.startswith(level) else None
            if current is not None:
                found.append((number, line, current))
        elif current is not None:
            current.append((number, line))
    return found


def fields(body):
    """{name: (value, [line number of each line of the value])} of the fields `- **Name:**
    value` of a block; a field's value goes on over the indented lines that follow it."""
    found, current = {}, None
    for number, line in body:
        match = FIELD.match(line)
        if match:
            current = match.group(1) if match.group(1) not in found else None
            if current:
                found[current] = [(match.group(2) or "").strip(), [number]]
        elif current and line.strip() and line[:1].isspace():
            found[current][0] += "\n" + line.strip()
            found[current][1].append(number)
        else:
            current = None
    return {name: tuple(value) for name, value in found.items()}


def located(found, name, pattern=None):
    """(word, line number) of each item of a field's list joined by ` · ` or `, `, or of each
    item inside what the first group of a pattern matches in the field's value."""
    value, lines = found.get(name, ("", [0]))
    spans = ([(match.start(1), match.group(1)) for match in pattern.finditer(value)]
             if pattern else [(0, value)])
    for start, text in spans:
        for item in ITEM.finditer(text):
            word = item.group(0).strip().strip("`").strip()
            if word:
                yield word, lines[value.count("\n", 0, start + item.start())]


def table(lines, title):
    """(line number, cells) of each row of the table under `## title`, header and separator
    row left out, the header's cells first as row 0."""
    rows, inside = [], False
    for number, line in enumerate(lines, start=1):
        if line.startswith("#"):
            inside = line.strip() == "## " + title
        elif inside and line.strip().startswith("|"):
            cells = [cell.strip().strip("`").strip() for cell in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                rows.append((number, cells))
    return rows


def items(value):
    """The items of a list joined by ` · ` or `, `, over its lines."""
    return [item.strip().strip("`").strip() for item in re.split(r"[·,\n]", value)
            if item.strip()]


class Foundation:
    def __init__(self, root, report):
        self.root, self.report = root, report
        self.files = {path: read(root, path) for path in
                      (DECISIONS, INVARIANTS, FACTS, GLOSSARY, PART_MAP, VIOLATED)}
        self.prefix, self.numbers = None, set()
        self.entries = {}    # path -> {identifier: (line, fields)}
        self.withdrawn = {}  # path -> {identifier: (line, successors)}
        self.parts = set()

    # --- identifiers ----------------------------------------------------------------------------

    def read_decisions(self):
        lines = self.files[DECISIONS]
        first = next((re.match(r"^### ([A-Z][A-Z0-9]*)-[0-9]", line) for line in lines
                      if re.match(r"^### [A-Z][A-Z0-9]*-[0-9]", line)), None)
        if not first:
            return
        self.prefix = first.group(1)
        seen = {}
        for number, heading, _ in blocks(lines, "### "):
            match = re.match(r"^### %s-([0-9]+)(?:/([0-9]+))? — " % self.prefix, heading)
            if not match:
                continue
            key = int(match.group(1))
            version = int(match.group(2)) if match.group(2) else None
            label = "%s-%02d" % (self.prefix, key)
            self.numbers.add(key)
            for earlier, line in seen.get(key, []):
                if version is None or earlier is None or earlier == version:
                    twice = label if version is None or earlier is None else "%s/%d" % (
                        label, version)
                    self.report.error(DECISIONS, number, "`%s` stands twice; it also stands at "
                                                         "line %d" % (twice, line))
                    break
            seen.setdefault(key, []).append((version, number))

    def read_named(self):
        """The entries and withdrawn identifiers of the invariants, the facts and the part map,
        which share one set of identifiers."""
        held = {}
        for path in (INVARIANTS, FACTS, PART_MAP):
            lines = self.files[path]
            self.entries[path], self.withdrawn[path] = {}, {}
            names = []
            for number, heading, body in blocks(lines, "## "):
                match = ENTRY.match(heading)
                if match:
                    self.entries[path].setdefault(match.group(1), (number, fields(body)))
                    names.append((number, match.group(1)))
            rows = table(lines, WITHDRAWN)
            header = rows[0][1] if rows else []
            column = header.index("Successors") if "Successors" in header else 2
            for number, cells in rows[1:]:
                successors = cells[column] if len(cells) > column else ""
                self.withdrawn[path].setdefault(cells[0], (number, successors))
                names.append((number, cells[0]))
            for number, name in names:
                if name in held:
                    self.report.error(path, number, "`%s` stands twice; it also stands at %s:%d"
                                      % ((name,) + held[name]))
                else:
                    held[name] = (path, number)
        self.parts = {name for name, (_, found) in self.entries[PART_MAP].items()
                      if "Files" in found}

    def read_glossary(self):
        held = {}
        for number, heading, _ in blocks(self.files[GLOSSARY], "## "):
            term = heading[3:].strip()
            if term == WITHDRAWN:
                continue
            if term.lower() in held:
                self.report.error(GLOSSARY, number, "`%s` stands twice; it also stands at line %d"
                                  % (term, held[term.lower()]))
            else:
                held[term.lower()] = number

    def check_successors(self):
        for path, withdrawn in self.withdrawn.items():
            for name, (number, successors) in withdrawn.items():
                for successor in items(successors):
                    if successor not in EMPTY + tuple(self.entries[path]) + tuple(withdrawn):
                        self.report.error(path, number, "withdrawn `%s` names the successor "
                                                        "`%s`, which this file does not hold"
                                          % (name, successor))

    # --- references -----------------------------------------------------------------------------

    def refer(self, path, line, word, kind, allowed=EMPTY):
        """Report a word that names no entry of its kind: a part, an invariant or a fact."""
        if word in allowed:
            return
        match = NAMED.fullmatch(word)
        if not match:
            self.report.error(path, line, "`%s` is no identifier of a %s" % (word, kind))
            return
        name = match.group(1)
        target = {"part": PART_MAP, "invariant": INVARIANTS, "fact": FACTS}[kind]
        known = self.parts if kind == "part" else self.entries[target]
        if name in known:
            return
        if name in self.withdrawn[target]:
            self.report.error(path, line, "`%s` is withdrawn; name its successor" % name)
        else:
            self.report.error(path, line, "`%s` names no %s" % (name, kind))

    def check_decision_numbers(self, path, lines):
        if not self.prefix:
            return
        pattern = re.compile(r"(?<![A-Za-z0-9-])%s-([0-9]+)(?![0-9])" % self.prefix)
        for number, line in enumerate(lines, start=1):
            for match in pattern.finditer(line):
                if int(match.group(1)) not in self.numbers:
                    self.report.error(path, number, "`%s` names no decision of the log"
                                      % match.group(0))

    def check_foundation_references(self):
        for _, _, body in blocks(self.files[DECISIONS], "### "):
            found = fields(body)
            for word, line in located(found, "Scope"):
                self.refer(DECISIONS, line, word, "part")
            for word, line in located(found, "Based on", FINGERPRINTED):
                self.refer(DECISIONS, line, word, "fact")
            for word, line in located(found, "Verification", VERIFIED):
                self.refer(DECISIONS, line, word, "invariant")
        for _, (_, found) in self.entries[INVARIANTS].items():
            for word, line in located(found, "Rests on"):
                self.refer(INVARIANTS, line, word, "fact")
            for word, line in located(found, "Part"):
                self.refer(INVARIANTS, line, word, "part", EMPTY + ("every",))
        for _, (_, found) in self.entries[PART_MAP].items():
            for name, kind in (("Depends on", "part"), ("Parts", "part"),
                               ("Invariant", "invariant")):
                for word, line in located(found, name):
                    self.refer(PART_MAP, line, word, kind)
            for word, line in located(found, "Failure modes", DETECTED):
                self.refer(PART_MAP, line, word, "invariant")
        for path, title in ((INVARIANTS, "Quarantined invariants"),
                            (INVARIANTS, "Recovered invariants"),
                            (VIOLATED, "Violated invariants")):
            for number, cells in table(self.files[path], title)[1:]:
                self.refer(path, number, cells[0], "invariant")

    def check_citations(self, path, lines):
        for number, line in enumerate(lines, start=1):
            match = CITATION.match(line)
            if not match:
                continue
            value = match.group(2).strip()
            if len(value.split()) != 1:
                self.report.error(path, number, "`%s: %s` cites no one identifier"
                                  % (match.group(1), value))
            else:
                self.refer(path, number, value, match.group(1))

    def check_guidelines(self, path, lines):
        fenced, kind = None, None
        for number, line in enumerate(lines, start=1):
            fence = FENCE.match(line)
            if fence:
                mark = fence.group(1)
                if fenced is None:
                    fenced = mark
                elif mark[0] == fenced[0] and len(mark) >= len(fenced) and \
                        not line.strip()[len(mark):]:
                    fenced = None
                continue
            if fenced is not None:
                continue
            field = FIELD.match(line)
            if field:
                kind = {"Applies to": "part", "Invariant": "invariant"}.get(field.group(1))
                value = field.group(2) or ""
            elif kind and line.strip() and line[:1].isspace():
                value = line
            else:
                kind = None
            if kind:
                for word in items(value):
                    self.refer(path, number, word, kind)
            for match in FINGERPRINTED.finditer(line):
                self.refer(path, number, match.group(0), "invariant")

    # --- files and parts ------------------------------------------------------------------------

    def check_files(self, tracked):
        wanted, owner = [], {}
        for name, (_, found) in self.entries[PART_MAP].items():
            if name not in self.parts:
                continue
            for line in found["Files"][0].split("\n"):
                pattern = re.sub(r"\(generated\)", "", line.strip().removeprefix("- ")).strip()
                if pattern and pattern not in EMPTY:
                    attribute = "the-way-part-%d" % len(wanted)
                    wanted.append("%s %s" % (pattern, attribute))
                    owner[attribute] = name
        left_out = {cells[0]: number for number, cells in table(self.files[PART_MAP], LEFT_OUT)[1:]}
        handle, attributes = tempfile.mkstemp(suffix=".attributes", text=True)
        try:
            with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
                stream.write("".join(line + "\n" for line in wanted))
            code, answer = git(self.root, "-c", "core.attributesFile=" + attributes.replace(
                os.sep, "/"), "-c", "core.ignorecase=false", "check-attr", "--all", "-z",
                "--stdin", stdin="".join(path + "\0" for path in tracked))
        finally:
            os.unlink(attributes)
        if code != 0:
            return False
        claims = {}
        pieces = answer.split("\0")
        for index in range(0, len(pieces) - 2, 3):
            path, attribute, value = pieces[index:index + 3]
            if attribute in owner and value == "set":
                claims.setdefault(path, []).append(owner[attribute])
        for path in tracked:
            parts = list(dict.fromkeys(claims.get(path, [])))
            if path in left_out:
                for part in parts:
                    self.report.error(PART_MAP, left_out[path], "`%s` is left out on purpose and "
                                                                "claimed by `%s`" % (path, part))
            elif not parts:
                self.report.error(path, 0, "no part claims it: give it to a part or list it as "
                                           "left out on purpose")
            elif len(parts) > 1:
                self.report.error(path, 0, "claimed by %s" % " and ".join(
                    "`%s`" % part for part in parts))
        return True


def run(root):
    """The report's lines and the exit code."""
    code, top = git(root, "rev-parse", "--show-toplevel")
    if code is None:
        return ["git cannot run: %s" % top], 2
    if code != 0:
        return ["%s lies in no git repository" % root], 2
    root = top.strip()
    code, listing = git(root, "ls-files", "-z")
    if code != 0:
        return ["git cannot list the files it tracks in %s" % root], 2
    tracked = [path for path in listing.split("\0") if path]

    report = Report()
    foundation = Foundation(root, report)
    foundation.read_decisions()
    foundation.read_named()
    foundation.read_glossary()
    foundation.check_successors()
    foundation.check_foundation_references()
    for path in tracked:
        lines = foundation.files.get(path) or read(root, path)
        foundation.check_decision_numbers(path, lines)
        if not path.endswith(".md"):
            foundation.check_citations(path, lines)
        if GUIDELINES.match(path):
            foundation.check_guidelines(path, lines)
    if not foundation.check_files(tracked):
        return ["git cannot match the path patterns of the part map"], 2
    lines = list(report.errors)
    count = len(lines)
    return lines + ["%d error%s" % (count, "" if count == 1 else "s")], 1 if count else 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) > 1:
        print("usage: foundation_check.py [ROOT]")
        return 2
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    lines, code = run(argv[0] if argv else ".")
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
