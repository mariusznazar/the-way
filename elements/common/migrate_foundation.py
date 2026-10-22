"""Migration of a product's foundation from the earlier form of the-way to the current one.

Usage, from anywhere:

    python -B <the-way>/elements/common/migrate_foundation.py [ROOT] [--apply] [--report PATH]

ROOT is a directory of the product's git repository, the working directory by default; the
foundation is read from `foundations/` at the repository's root, the guidelines from `guidelines/`,
and the code from every other file git tracks. Without --apply the run is a trial: it changes no
file and writes only its report. With --apply it writes its changes, keeping each file's byte order
mark and line endings, and removes the files the current form has no place for. A run on a
foundation it has already migrated changes nothing. The report, Markdown in UTF-8, goes to PATH,
by default `.runs/foundation_migration.md` under the repository's root; the console gets counts.

What it changes, to the form the templates `elements/*/template.md` and `elements/common/rules.md`
give:

- a reference `ID@<fingerprint>` becomes `ID`, and `ID/<version>` becomes `ID`, in the foundation
  and the guidelines outside code spans and quotation marks, in comments of code outside code spans
  and quotation marks, and in the docstrings of a Python file; a line `invariant: <id>/<version>` or
  `fact: <id>/<version>` in a comment of code loses its version;
- decisions: of the versions of one number, the highest stays, in the place of the first, under a
  heading without its version; *Change*, *Approved by*, *Review when*, review records and the
  level of *Verification* go; a later version's *Rationale for change* becomes *Rationale*;
- invariants: the heading loses its version and the entry *Correction*; *Method* `TODO` becomes
  `review` and a command becomes `test`; *Violated* is added, `yes` for an invariant on the list of
  violated invariants and `no` for the rest, and a path of a file git tracks becomes `test`; the
  lists of quarantined and recovered invariants go,
  and a recovered invariant deriving from nothing reads in *Derives from* `recovered from code —`
  and the place in the code its row found, where the row names a file git tracks;
- environment facts lose the heading's version, *Holds for* and *Method*; glossary entries lose
  *Avoid*;
- the part map loses failure modes, critical flows, the separation beside a dependency, the
  criticality scale, the change paths of promise levels and the column of the external context on
  whether a partner updates with the product;
- `foundations/violated_invariants.md`, `foundations/human_verdicts.md` and
  `foundations/known_violations.md` are removed, with their patterns in the part map's *Files*.

What it leaves as it is and lists in the report for a human: the text of every *Review when*; the
rows of every list it removes; a decision whose last version repeals it, a review record, a level
of *Verification* it does not recognise, an *Origin* of an inherited decision, a *Based on*, a
*Relations* or a *Source* of a form it does not recognise; a *Method* that is a path of no file git
tracks; a surface still declared at the code; every place an old reference stands inside code, a
quotation, a string or a file it does not migrate; the decision numbers missing from the log; the
opening text of each file it changes.

Outside Python, a comment is a line opening with a comment mark, `#`, `//`, `--`, `;`, `%`, `*`,
`/*`, `<!--` or `REM`: a line of a string spanning several lines that opens with such a mark is
taken for a comment, and a comment following code on its line is not read.

Exit code: 0 when the report lists nothing for a human, 1 when it does, 2 when it cannot run —
ROOT lies in no git repository, git cannot list its files, or it holds no foundation.
"""

import ast
import codecs
import io
import os
import re
import subprocess
import sys
import textwrap
import tokenize
from collections import Counter

sys.dont_write_bytecode = True

DECISIONS = "foundations/decisions.md"
INVARIANTS = "foundations/invariants.md"
FACTS = "foundations/environment_facts.md"
GLOSSARY = "foundations/glossary.md"
PART_MAP = "foundations/part_map.md"
VIOLATED = "foundations/violated_invariants.md"
VERDICTS = "foundations/human_verdicts.md"
KNOWN_VIOLATIONS = "foundations/known_violations.md"
FOUNDATION = (DECISIONS, INVARIANTS, FACTS, GLOSSARY, PART_MAP)
REMOVED = {VIOLATED: "Violated invariants", VERDICTS: "Human verdicts",
           KNOWN_VIOLATIONS: "Known violations"}
GUIDELINES = re.compile(r"^guidelines/[^/]+\.md$")
DEFAULT_REPORT = ".runs/foundation_migration.md"

WORDS = r"[a-z0-9]+(?:-[a-z0-9]+)*"
FIELD = re.compile(r"^- \*\*(.+?):\*\*(?: (.*))?$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
ENTRY = re.compile(r"^## (%s)(?:/([0-9]+))?\s*$" % WORDS)
FINGERPRINT = re.compile(r"(?<![\w.@/-])([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)@[0-9a-f]{8}"
                         r"(?![0-9A-Za-z]|\.[0-9A-Za-z])")
CITED = re.compile(r"\b(invariant|fact):(\s*)(%s)/[0-9]+(?![\w/])" % WORDS)
CITATION = re.compile(r"\binvariant:\s*(%s)\b" % WORDS)
COMMENT_LINE = re.compile(r"^\s*(?:#|//|--|;|%|\*|/\*|<!--|REM\b)")
SPAN = re.compile(r"(`[^`]*`)")
SPAN_OR_QUOTE = re.compile(r"(`[^`]*`|\"[^\"]*\")")
QUOTED = re.compile(r"\"[^\"]*\"|\u201c[^\u201d]*\u201d")
ADDRESS = re.compile(r"https?://\S")
READ_ON = re.compile(r"\bread [0-9]{4}-[0-9]{2}-[0-9]{2}\b")
LEVEL = re.compile(r"\b[Ll]evel [0-9]\b")
OLD_CHECK = re.compile(r"format_guard\.py|form_check\.py|(?:^|/)probes/")
WIDTH = 100


class Text:
    """A foundation file as lines without their endings, and what writing it back keeps: the byte
    order mark and the line ending most of its lines end with."""

    def __init__(self, raw):
        self.bom = raw.startswith(codecs.BOM_UTF8)
        text = raw.decode("utf-8-sig" if self.bom else "utf-8")
        self.newline = "\r\n" if text.count("\r\n") * 2 > text.count("\n") else "\n"
        self.lines = text.replace("\r\n", "\n").split("\n")

    def dump(self, lines):
        return (codecs.BOM_UTF8 if self.bom else b"") + self.newline.join(lines).encode("utf-8")


def git(root, *args):
    """(exit code, output) of git, or (None, why) where git cannot be started."""
    try:
        result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True,
                                encoding="utf-8")
    except OSError as error:
        return None, str(error)
    return result.returncode, result.stdout


def read_bytes(root, path):
    try:
        with open(os.path.join(root, *path.split("/")), "rb") as handle:
            return handle.read()
    except OSError:
        return None


def segments(lines, deepest):
    """The lines cut where a heading of level 1 to `deepest` stands outside fenced code; the first
    piece holds what stands before the first such heading."""
    found, fenced = [[]], None
    heading = re.compile(r"^#{1,%d} " % deepest)
    for line in lines:
        fence = FENCE.match(line)
        if fence:
            mark = fence.group(1)
            if fenced is None:
                fenced = mark
            elif mark[0] == fenced[0] and len(mark) >= len(fenced):
                fenced = None
        if fenced is None and not fence and heading.match(line):
            found.append([line])
        else:
            found[-1].append(line)
    return found


def spans(lines):
    """(name, first, end) of each field `- **Name:** value` of an entry's lines; a field goes on
    over the indented lines that follow it."""
    found, index = [], 0
    while index < len(lines):
        match = FIELD.match(lines[index])
        if not match:
            index += 1
            continue
        end = index + 1
        while end < len(lines) and lines[end].strip() and lines[end][:1].isspace():
            end += 1
        found.append((match.group(1), index, end))
        index = end
    return found


def value(lines, span):
    """A field's value, its lines joined by one space."""
    _, first, end = span
    head = FIELD.match(lines[first]).group(2) or ""
    return " ".join([head.strip()] + [line.strip() for line in lines[first + 1:end]]).strip()


def field(lines, name):
    return next((span for span in spans(lines) if span[0] == name), None)


def table(lines, title=None):
    """(header cells, [(line index, cells)]) of the first table in the lines, or of the table under
    `## title`; the separator row is left out."""
    header, rows, inside = None, [], title is None
    for index, line in enumerate(lines):
        if line.startswith("#"):
            inside = title is None or line.strip() == "## " + title
            continue
        if inside and line.strip().startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue
            if header is None:
                header = cells
            else:
                rows.append((index, cells))
    return header or [], rows


def row(cells):
    return "| " + " | ".join(cells) + " |"


def items(text):
    """The items of a list joined by ` · `, a ` · ` inside quotation marks joining nothing; a piece
    opening with `§`, another place of the same source, or with a quotation mark, another passage
    of the same place, goes on the item before it."""
    masked = QUOTED.sub(lambda match: "\0" * len(match.group(0)), text)
    found, start = [], 0
    for piece in masked.split("·"):
        item = text[start:start + len(piece)].strip()
        start += len(piece) + 1
        if found and item[:1] in ("§", '"', chr(0x201c)):
            found[-1] += " · " + item
        elif item:
            found.append(item)
    return found


def quoted_source(item):
    return bool(ADDRESS.search(item) and QUOTED.search(item) and READ_ON.search(item))


class References:
    """Old references in a text: `ID@<fingerprint>`, a decision `PREFIX-NN/<version>`, and an
    identifier of the invariants, the facts or the part map with `/<version>`."""

    def __init__(self, prefix, names):
        self.decision = re.compile(r"(?<![\w/-])(%s-[0-9]+)/[0-9]+(?![\w/]|\.\w)"
                                   % re.escape(prefix)) if prefix else None
        alternatives = "|".join(re.escape(name) for name in sorted(names, key=len, reverse=True))
        self.named = re.compile(r"(?<![\w./-])(%s)/[0-9]+(?![\w/]|\.\w)"
                                % alternatives) if names else None

    def fix(self, text, counts, path, citations=False):
        if citations:
            text, number = CITED.subn(r"\1:\2\3", text)
            counts[(path, "version removed from a citation line")] += number
        text, number = FINGERPRINT.subn(r"\1", text)
        counts[(path, "fingerprint removed from a reference")] += number
        for pattern in (self.decision, self.named):
            if pattern:
                text, number = pattern.subn(r"\1", text)
                counts[(path, "version removed from a reference")] += number
        return text

    def found(self, text):
        return any(pattern and pattern.search(text)
                   for pattern in (FINGERPRINT, CITED, self.decision, self.named))


class Migration:
    def __init__(self, root, tracked):
        self.root, self.tracked = root, tracked
        self.counts = Counter()           # (path, kind) -> number
        self.findings = {}                # section -> [(where, text)]
        self.samples = []                 # (path, title, before, after)
        self.writes, self.removals = {}, []
        self.texts = {}
        for path in FOUNDATION + tuple(REMOVED):
            raw = read_bytes(root, path)
            if raw is not None:
                self.texts[path] = Text(raw)
        self.prefix, self.padded = None, False
        self.names = set()
        self.citations = {}               # invariant -> [path of a file of code citing it]
        self.methods = {}                 # invariant -> its *Method* before the migration

    def lines(self, path):
        return self.texts[path].lines if path in self.texts else []

    def find(self, section, where, text):
        self.findings.setdefault(section, []).append((where, text))

    def sample(self, path, title, before, after):
        if before != after:
            self.samples.append((path, title, before, after))

    # --- references in Markdown ----------------------------------------------------------------

    def fix_markdown(self, lines, path, where):
        """The lines with old references fixed outside code; one standing inside code is left and
        found for a human."""
        fixed, fenced = [], None
        for line in lines:
            fence = FENCE.match(line)
            if fence:
                mark = fence.group(1)
                if fenced is None:
                    fenced = mark
                elif mark[0] == fenced[0] and len(mark) >= len(fenced):
                    fenced = None
                fixed.append(line)
                continue
            if fenced is not None:
                if self.refs.found(line):
                    self.find("Old references left inside code or quotation marks", where,
                              line.strip())
                fixed.append(line)
                continue
            fixed.append(self.fix_outside(line, path, where, SPAN_OR_QUOTE))
        return fixed

    def fix_outside(self, text, path, where, quoting, citations=False):
        """The text with old references fixed outside the code spans, or quotations, a pattern
        cuts out of it; one standing inside them is left and found for a human, since it may be
        an example of the earlier form rather than a reference."""
        pieces = quoting.split(text)
        for index, piece in enumerate(pieces):
            if index % 2 == 0:
                pieces[index] = self.refs.fix(piece, self.counts, path, citations)
            elif self.refs.found(piece):
                self.find("Old references left inside code or quotation marks", where, piece)
        return "".join(pieces)

    # --- reading before changing ---------------------------------------------------------------

    def read_names(self):
        first = next((re.match(r"^### ([A-Z][A-Z0-9]*)-[0-9]", line)
                      for line in self.lines(DECISIONS)
                      if re.match(r"^### [A-Z][A-Z0-9]*-[0-9]", line)), None)
        self.prefix = first.group(1) if first else None
        for path in (INVARIANTS, FACTS, PART_MAP):
            for line in self.lines(path):
                match = ENTRY.match(line)
                if match:
                    self.names.add(match.group(1))
            for _, cells in table(self.lines(path), "Withdrawn identifiers")[1]:
                if re.fullmatch(WORDS, cells[0].strip("`")):
                    self.names.add(cells[0].strip("`"))
        self.refs = References(self.prefix, self.names)

    def read_lists(self):
        """The invariants the removed lists name, each list's rows found for a human."""
        self.violated = set()
        for path, title in REMOVED.items():
            if path not in self.texts:
                continue
            for _, cells in table(self.lines(path))[1]:
                self.find("Rows of %s (`%s`, removed)" % (title.lower(), path), path,
                          row(cells))
                if path == VIOLATED:
                    self.violated.add(cells[0].strip("`"))
            self.removals.append(path)
            self.counts[(path, "file removed")] += 1
        lines = self.lines(INVARIANTS)
        self.recovered = {}
        header, rows = table(lines, "Recovered invariants")
        for _, cells in rows:
            cells = cells + [""] * (len(header) - len(cells))
            self.recovered[cells[0].strip("`")] = dict(zip(header, cells))
        for _, cells in table(lines, "Quarantined invariants")[1]:
            self.find("Rows of the quarantined invariants (removed)", INVARIANTS, row(cells))

    # --- decisions -----------------------------------------------------------------------------

    def migrate_decisions(self):
        lines = self.lines(DECISIONS)
        if not lines or not self.prefix:
            return lines
        heading = re.compile(r"^### %s-([0-9]+)(?:/([0-9]+))? — " % re.escape(self.prefix))
        review = re.compile(r"^### %s-[0-9]+(?:/[0-9]+)? · review\b" % re.escape(self.prefix))
        pieces = segments(lines, 3)
        versions = {}
        for index, piece in enumerate(pieces):
            match = heading.match(piece[0]) if index else None
            if match:
                version = int(match.group(2)) if match.group(2) else None
                versions.setdefault(int(match.group(1)), []).append((version, index))
                if match.group(1).startswith("0"):
                    self.padded = True
        out, first = [], {chain[0][1]: number for number, chain in versions.items()}
        kept = set()
        for number, chain in versions.items():
            label = self.label(number)
            numbered = [version for version, _ in chain]
            if len(chain) > 1 and None in numbered:
                self.find("Decisions left as they are", label,
                          "the number stands both with and without a version")
                kept.update(index for _, index in chain)
                continue
            last = max(chain, key=lambda pair: pair[0] or 0)
            change = field(pieces[last[1]], "Change")
            if change and value(pieces[last[1]], change).startswith("repeal"):
                self.find("Decisions left as they are", label,
                          "its last version repeals it: withdraw the number by hand")
                kept.update(index for _, index in chain)
        removed = False
        for index, piece in enumerate(pieces):
            where = piece[0].strip() if index else DECISIONS
            if index in kept:
                out += self.fix_markdown(piece, DECISIONS, where)
            elif index in first:
                chain = versions[first[index]]
                last_version, last = max(chain, key=lambda pair: pair[0] or 0)
                before = pieces[last]
                after = self.decision(before, len(chain) > 1, chain, pieces)
                if len(chain) > 1:
                    self.counts[(DECISIONS, "older version of a decision removed")] += len(
                        chain) - 1
                    removed = True
                self.sample(DECISIONS, after[0], "\n".join(
                    line for _, i in chain for line in pieces[i]), "\n".join(after))
                out += after
            elif index and heading.match(piece[0]):
                continue
            elif index and review.match(piece[0]):
                self.find("Review records (removed)", where, "\n".join(piece).strip())
                self.counts[(DECISIONS, "review record removed")] += 1
                removed = True
            else:
                out += self.fix_markdown(piece, DECISIONS, where)
        self.decision_gaps(versions)
        return tail(out, lines) if removed else out

    def decision(self, piece, later, chain, pieces):
        lines = list(piece)
        label = re.match(r"^### (\S+)", lines[0]).group(1).split("/")[0]
        stripped = re.sub(r"^(### [A-Z][A-Z0-9]*-[0-9]+)/[0-9]+ — ", r"\1 — ", lines[0])
        if stripped != lines[0]:
            self.counts[(DECISIONS, "version removed from a heading")] += 1
            lines[0] = stripped
        if later:
            kinds = []
            for version, index in sorted(chain, key=lambda pair: pair[0] or 0):
                span = field(pieces[index], "Change")
                kinds.append("%s/%s: %s" % (label, version, value(pieces[index], span)
                                            if span else "no Change"))
            self.find("Decisions kept from their last version", label, "; ".join(kinds))
        for name in ("Change", "Approved by", "Review when"):
            span = field(lines, name)
            if not span:
                continue
            text = value(lines, span)
            if name == "Review when" and text != "none":
                self.find("Review when (to the task of the periodic review of the foundation)",
                          label, text)
            del lines[span[1]:span[2]]
            self.counts[(DECISIONS, "field removed: %s" % name)] += 1
        lines = self.fix_markdown(lines, DECISIONS, label)
        span = field(lines, "Verification")
        if span:
            new = verification(lines[span[1]:span[2]])
            if new is None:
                self.find("Verification left as it is", label, "\n".join(lines[span[1]:span[2]]))
            elif new != lines[span[1]:span[2]]:
                lines[span[1]:span[2]] = new
                self.counts[(DECISIONS, "level removed from Verification")] += 1
        span = field(lines, "Origin")
        if span and value(lines, span).startswith("inherited"):
            self.find("Origin of an inherited decision, left as it is", label,
                      value(lines, span))
        for index, line in enumerate(lines):
            if line.startswith("*Rationale for change:*"):
                lines[index] = "*Rationale:*" + line[len("*Rationale for change:*"):]
                self.counts[(DECISIONS, "Rationale for change renamed Rationale")] += 1
                first = pieces[min(chain, key=lambda pair: pair[0] or 0)[1]]
                self.find("Rationale for change, now the Rationale: rewrite it to describe the "
                          "decision, not the change", label, "\n".join(
                              paragraph(lines, index) + ["", "The first version's:"] +
                              paragraph(first, next((number for number, text in enumerate(first)
                                                     if text.startswith("*Rationale:*")), None))))
        span = field(lines, "Based on")
        if span and any(item != "none" and not re.fullmatch(WORDS, item) and not
                        quoted_source(item) for item in items(value(lines, span))):
            self.find("Based on of a form not recognised: a fact by its identifier alone, or a "
                      "source with its address, a passage quoted and the date read", label,
                      value(lines, span))
        span = field(lines, "Relations")
        for item in items(value(lines, span)) if span else []:
            if item != "none" and not re.fullmatch(r"(derives from|narrows) %s-[0-9]+"
                                                   % re.escape(self.prefix), item):
                self.find("Relations of a form not recognised", label, item)
        return lines

    def decision_gaps(self, versions):
        withdrawn = set()
        for _, cells in table(self.lines(DECISIONS), "Withdrawn identifiers")[1]:
            match = re.fullmatch(r"%s-([0-9]+)" % re.escape(self.prefix), cells[0].strip("`"))
            if match:
                withdrawn.add(int(match.group(1)))
        missing = [number for number in range(1, max(versions, default=0))
                   if number not in versions and number not in withdrawn]
        if missing:
            self.find("Decision numbers neither in the log nor on its list of withdrawn numbers",
                      DECISIONS, ", ".join(self.label(number) for number in missing))

    def label(self, number):
        """A decision number as the log writes its numbers, with a leading zero or without."""
        return "%s-%0*d" % (self.prefix, 2 if self.padded else 1, number)

    # --- invariants ----------------------------------------------------------------------------

    def migrate_invariants(self):
        lines = self.lines(INVARIANTS)
        out, removed = [], False
        for index, piece in enumerate(segments(lines, 2)):
            title = piece[0].strip()[3:] if index else ""
            if title in ("Quarantined invariants", "Recovered invariants"):
                self.counts[(INVARIANTS, "list removed: %s" % title)] += 1
                removed = True
                continue
            match = ENTRY.match(piece[0]) if index else None
            if not match:
                out += self.fix_markdown(piece, INVARIANTS, title or INVARIANTS)
                continue
            after = self.invariant(piece, match.group(1))
            self.sample(INVARIANTS, match.group(1), "\n".join(piece), "\n".join(after))
            out += after
        for name in self.recovered:
            if not any(ENTRY.match(line) and ENTRY.match(line).group(1) == name
                       for line in lines):
                self.find("Recovered invariants (list removed)", name,
                          "the list names it, the file holds no such entry")
        return tail(out, lines) if removed else out

    def invariant(self, piece, name):
        lines = list(piece)
        if ENTRY.match(lines[0]).group(2):
            lines[0] = "## " + name
            self.counts[(INVARIANTS, "version removed from a heading")] += 1
        span = field(lines, "Method")
        if span:
            method = value(lines, span)
            self.methods[name] = method
            new = {"`TODO`": "review", "TODO": "review"}.get(method)
            if new is None and (re.fullmatch(r"`[^`]+`", method) or method in self.tracked):
                new = "test"
            if new:
                lines[span[1]:span[2]] = ["- **Method:** " + new]
                kind = ("TODO" if new == "review" else "path" if method in self.tracked
                        else "command")
                self.counts[(INVARIANTS, "Method %s -> %s" % (kind, new))] += 1
            elif method not in ("test", "review"):
                self.find("Method left as it is: `test` or `review`?", name, method)
        span = field(lines, "Correction")
        if span:
            if value(lines, span) != "none":
                self.find("Correction removed", name, value(lines, span))
            del lines[span[1]:span[2]]
            self.counts[(INVARIANTS, "field removed: Correction")] += 1
        if not field(lines, "Violated"):
            found = spans(lines)
            part = field(lines, "Part") or (found[-1] if found else None)
            at = part[2] if part else len(lines)
            mark = "yes" if name in self.violated else "no"
            lines[at:at] = ["- **Violated:** " + mark]
            self.counts[(INVARIANTS, "Violated added: %s" % mark)] += 1
        if name in self.recovered:
            cells = self.recovered[name]
            span = field(lines, "Derives from")
            place = code_place(cells.get("Found", ""), self.tracked)
            text = " | ".join("%s: %s" % pair for pair in cells.items())
            if span and value(lines, span) == "none" and place:
                lines[span[1]:span[2]] = ["- **Derives from:** recovered from code — " + place]
                self.counts[(INVARIANTS, "recovered: Derives from filled")] += 1
                self.find("Recovered invariants (list removed): Derives from filled", name, text)
            else:
                self.find("Recovered invariants (list removed): Derives from not filled — no "
                          "place in tracked code, or it derives from something already", name,
                          text)
        return self.fix_markdown(lines, INVARIANTS, name)

    # --- environment facts and the glossary ----------------------------------------------------

    def migrate_facts(self):
        out = []
        for index, piece in enumerate(segments(self.lines(FACTS), 2)):
            match = ENTRY.match(piece[0]) if index else None
            if not match:
                out += self.fix_markdown(piece, FACTS, piece[0].strip() if index else FACTS)
                continue
            name, lines = match.group(1), list(piece)
            if match.group(2):
                lines[0] = "## " + name
                self.counts[(FACTS, "version removed from a heading")] += 1
            for removed in ("Holds for", "Method"):
                span = field(lines, removed)
                if span:
                    if removed == "Holds for":
                        self.find("Holds for removed", name, value(lines, span))
                    del lines[span[1]:span[2]]
                    self.counts[(FACTS, "field removed: %s" % removed)] += 1
            lines = self.fix_markdown(lines, FACTS, name)
            span = field(lines, "Source")
            if not span or not all(quoted_source(item) for item in items(value(lines, span))):
                self.find("Source of a form not recognised: an address, a passage quoted and the "
                          "date read", name, value(lines, span) if span else "no Source")
            self.sample(FACTS, name, "\n".join(piece), "\n".join(lines))
            out += lines
        return out

    def migrate_glossary(self):
        out = []
        for index, piece in enumerate(segments(self.lines(GLOSSARY), 2)):
            lines = list(piece)
            span = field(lines, "Avoid") if index else None
            if span:
                if value(lines, span) != "none":
                    self.find("Avoid removed", lines[0][3:].strip(), value(lines, span))
                del lines[span[1]:span[2]]
                self.counts[(GLOSSARY, "field removed: Avoid")] += 1
            lines = self.fix_markdown(lines, GLOSSARY, lines[0].strip() if index else GLOSSARY)
            if index:
                self.sample(GLOSSARY, lines[0][3:].strip(), "\n".join(piece), "\n".join(lines))
            out += lines
        return out

    # --- the part map --------------------------------------------------------------------------

    def migrate_part_map(self):
        lines = self.lines(PART_MAP)
        out, removed = [], False
        for index, piece in enumerate(segments(lines, 2)):
            title = piece[0].strip()[3:] if index else ""
            where = title or PART_MAP
            if title in ("Criticality scale", "Change paths"):
                body = "\n".join(piece[1:]).strip()
                if table(piece)[1] or title == "Criticality scale":
                    self.find("%s (removed)" % title, PART_MAP, body)
                self.counts[(PART_MAP, "section removed: %s" % title)] += 1
                removed = True
                continue
            if title == "External context":
                out += self.fix_markdown(self.external_context(piece), PART_MAP, where)
                continue
            names = [span[0] for span in spans(piece)] if index else []
            if "Criticality" in names or "Coverage" in names or (
                    "Parts" in names and "Invariant" in names):
                self.find("Critical flows (removed; the invariant's Part names the parts the "
                          "flow runs through)", title, "\n".join(piece).strip())
                self.counts[(PART_MAP, "critical flow removed")] += 1
                removed = True
                continue
            if "Declared at" in names:
                self.find("Surfaces left as they are: Relied on by in place of Declared at",
                          title, "\n".join(piece).strip())
                out += self.fix_markdown(piece, PART_MAP, where)
                continue
            after = self.part(piece, title) if "Files" in names else piece
            after = self.fix_markdown(after, PART_MAP, where)
            if index and "Files" in names:
                self.sample(PART_MAP, title, "\n".join(piece), "\n".join(after))
            out += after
        return tail(out, lines) if removed else out

    def part(self, piece, title):
        lines = list(piece)
        span = field(lines, "Failure modes")
        if span:
            del lines[span[1]:span[2]]
            self.counts[(PART_MAP, "field removed: Failure modes")] += 1
        span = field(lines, "Depends on")
        if span:
            text = "\n".join(lines[span[1]:span[2]])
            new = re.sub(r"\s*\(separated — [^)]*\)", "", text)
            if new != text:
                self.find("Separation of a dependency removed", title, text)
                lines[span[1]:span[2]] = new.split("\n")
                self.counts[(PART_MAP, "separation of a dependency removed")] += 1
        span = field(lines, "Files")
        if span:
            patterns = [FIELD.match(lines[span[1]]).group(2) or ""] + [
                line.strip() for line in lines[span[1] + 1:span[2]]]
            kept = [pattern for pattern in patterns
                    if pattern.strip().lstrip("/") not in self.removals]
            if len(kept) != len(patterns):
                self.counts[(PART_MAP, "pattern of a removed file removed")] += len(
                    patterns) - len(kept)
                kept = kept or ["none"]
                lines[span[1]:span[2]] = ["- **Files:** " + kept[0]] + [
                    "  " + pattern for pattern in kept[1:]]
        return lines

    def external_context(self, piece):
        header, rows = table(piece)
        if "Updates with the product" not in header:
            return piece
        column = header.index("Updates with the product")
        lines, seen = list(piece), 0
        for index, line in enumerate(lines):
            if not line.strip().startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            seen += 1
            if len(cells) <= column:
                continue
            if seen > 2:
                self.find("External context: column `Updates with the product` removed",
                          cells[0], cells[column])
            del cells[column]
            lines[index] = "|" + "|".join(["---"] * len(cells)) + "|" if seen == 2 else row(cells)
        self.counts[(PART_MAP, "external context column removed")] += 1
        return lines

    # --- guidelines and code -------------------------------------------------------------------

    def migrate_tracked(self):
        for path in sorted(self.tracked):
            if path in self.texts or path.startswith("foundations/"):
                continue
            raw = read_bytes(self.root, path)
            if raw is None or b"\0" in raw:
                continue
            try:
                text = raw.decode("utf-8-sig" if raw.startswith(codecs.BOM_UTF8) else "utf-8")
            except UnicodeDecodeError:
                continue
            if GUIDELINES.match(path):
                guide = Text(raw)
                new = self.fix_markdown(guide.lines, path, path)
                if new != guide.lines:
                    self.writes[path] = guide.dump(new)
                    changed = [(old, line) for old, line in zip(guide.lines, new) if old != line]
                    self.sample(path, "the lines it changes", "\n".join(
                        old for old, _ in changed), "\n".join(line for _, line in changed))
            elif path.endswith(".md"):
                count = sum(1 for line in text.split("\n") if self.refs.found(line))
                if count:
                    self.find("Files holding old references that the migration does not reach",
                              path, "%d line%s" % (count, "" if count == 1 else "s"))
            else:
                new = self.code(path, text)
                if new != text:
                    bom = codecs.BOM_UTF8 if raw.startswith(codecs.BOM_UTF8) else b""
                    self.writes[path] = bom + new.encode("utf-8")

    def code(self, path, text):
        """The text of a file of code with old references fixed in its comments, and in the
        docstrings of a Python file; one in any other string, or in code, is left and found for a
        human."""
        parts = re.split(r"(\r\n|\n)", text)
        contents = parts[0::2]
        comments, strings, docstrings = None, set(), set()
        if path.endswith(".py"):
            try:
                for node in ast.walk(ast.parse(text)):
                    body = getattr(node, "body", None)
                    if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef,
                                         ast.AsyncFunctionDef)) and body and isinstance(
                            body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and \
                            isinstance(body[0].value.value, str):
                        docstrings.update(range(body[0].lineno - 1, body[0].end_lineno))
                comments = []
                plain = io.StringIO(text.replace("\r\n", "\n"))
                tokens = tokenize.generate_tokens(plain.readline)
                for token in tokens:
                    if token.type == tokenize.COMMENT:
                        comments.append((token.start[0] - 1, token.start[1], token.string))
                    elif token.type in (tokenize.STRING, getattr(tokenize, "FSTRING_MIDDLE", -1),
                                        getattr(tokenize, "TSTRING_MIDDLE", -1)) and \
                            token.start[0] - 1 not in docstrings:
                        for offset, line in enumerate(token.string.split("\n")):
                            if self.refs.found(line):
                                strings.add(token.start[0] + offset)
            except (tokenize.TokenError, SyntaxError, ValueError):
                comments, strings, docstrings = None, set(), set()
        before, cited = list(contents), []
        if comments is not None:
            for number, column, comment in comments:
                fixed = self.fix_outside(comment, path, "%s:%d" % (path, number + 1),
                                         SPAN_OR_QUOTE, citations=True)
                line = contents[number]
                contents[number] = line[:column] + fixed + line[column + len(comment):]
                cited.append(fixed)
            for number in sorted(docstrings):
                contents[number] = self.fix_outside(contents[number], path, "%s:%d" % (
                    path, number + 1), SPAN)
            left = sorted(strings)
        else:
            left = []
            for number, line in enumerate(contents):
                if COMMENT_LINE.match(line):
                    contents[number] = self.fix_outside(line, path, "%s:%d" % (
                        path, number + 1), SPAN_OR_QUOTE, citations=True)
                    cited.append(contents[number])
                elif self.refs.found(line):
                    left.append(number + 1)
        if left:
            self.find("Old references left in code outside comments and docstrings", path,
                      "line%s %s" % ("" if len(left) == 1 else "s",
                                     ", ".join(str(number) for number in left)))
        for comment in cited:
            for match in CITATION.finditer(comment):
                self.citations.setdefault(match.group(1), []).append(path)
        changed = [(old, new) for old, new in zip(before, contents) if old != new]
        if changed and len([s for s in self.samples if s[0] == "code"]) < 3:
            self.samples.append(("code", path, changed[0][0].strip(), changed[0][1].strip()))
        parts[0::2] = contents
        return "".join(parts)

    # --- what only a human settles -------------------------------------------------------------

    def check_methods(self):
        for name, method in self.methods.items():
            if method == "`TODO`" or not (re.fullmatch(r"`[^`]+`", method) or
                                          method in self.tracked):
                continue
            citing = sorted(set(self.citations.get(name, [])))
            if OLD_CHECK.search(method):
                self.find("Invariants whose method ran a format guard, a form check or a probe",
                          name, method)
            elif not citing:
                self.find("Invariants now `test` that no test of code cites "
                          "(`invariant: <id>`)", name, method)
            elif all(OLD_CHECK.search(path) for path in citing):
                self.find("Invariants now `test` cited only by format guards, form checks or "
                          "probes", name, ", ".join(citing))

    def violated_tests(self):
        for name in sorted(self.violated):
            citing = sorted(set(self.citations.get(name, [])))
            self.find("Violated: yes — mark each test citing it as an expected failure", name,
                      ", ".join(citing) if citing else "no test of code cites it")

    def opening_texts(self):
        for path in FOUNDATION:
            if path in self.writes:
                lines = self.lines(path)
                end = next((index for index, line in enumerate(lines)
                            if re.match(r"^#{2,3} ", line)), len(lines))
                text = "\n".join(lines[:end]).strip()
                if text:
                    self.find("Opening text of each file the run changes (read whether it still "
                              "holds)", path, text)


def verification(lines):
    """The lines of a decision's *Verification* without the level of the earlier form, the same
    lines where it names none, or None where a level stays that this does not recognise."""
    end = next((index for index in range(1, len(lines))
                if re.match(r"^\s+- ", lines[index])), len(lines))
    head = " ".join([FIELD.match(lines[0]).group(2) or ""] +
                    [line.strip() for line in lines[1:end]]).strip()
    new = re.sub(r"^level [12] — ", "", head)
    new = re.sub(r"\.\s+Level [12] for (.+?) — (?=an agent\b)", r". For \1, ", new)
    new = re.sub(r"\.\s+Level [12] — an agent\b", ". An agent", new)
    if LEVEL.search(new):
        return None
    if new == head:
        return lines
    wrapped = textwrap.wrap("- **Verification:** " + new, width=WIDTH, subsequent_indent="  ",
                            break_long_words=False, break_on_hyphens=False)
    return wrapped + lines[end:]


def paragraph(lines, start):
    """The lines from `start` to the next blank line or the next *Rejected:*."""
    if start is None:
        return ["none"]
    end = start + 1
    while end < len(lines) and lines[end].strip() and not lines[end].startswith("*Rejected:*"):
        end += 1
    return lines[start:end]


def code_place(found, tracked):
    """The pieces of a recovered invariant's *Found* that open with a file git tracks outside the
    foundation, joined by `; `."""
    places = []
    for piece in re.split(r";|\s·\s", re.sub(r"^\s*found:\s*", "", found)):
        piece = piece.strip()
        if not piece or QUOTED.search(piece):
            continue
        first = re.split(r"[\s,]", piece, maxsplit=1)[0].strip("`")
        path = re.sub(r":[0-9][0-9,-]*$", "", first)
        if path in tracked and not path.startswith("foundations/"):
            places.append(piece)
    return "; ".join(places)


def tail(out, original):
    """The lines with the blank lines at their end cut to what the original ends with."""
    while out and not out[-1].strip():
        out.pop()
    return out + ([""] if original and original[-1] == "" else [])


def render(migration, apply):
    counts = migration.counts
    kinds = Counter()
    files = {}
    for (path, kind), number in counts.items():
        if number:
            kinds[kind] += number
            files.setdefault(path, Counter())[kind] += number
    out = ["# Foundation migration — %s" % ("applied" if apply else "trial run, nothing written"),
           "", "Repository: `%s`" % migration.root, ""]
    out += ["## Changes by kind", "", "| Kind | Number |", "|---|---|"]
    out += ["| %s | %d |" % (kind, number) for kind, number in sorted(kinds.items())]
    out += ["", "## Changes by file", "", "| File | Kind | Number |", "|---|---|---|"]
    for path in sorted(files):
        for kind, number in sorted(files[path].items()):
            out.append("| `%s` | %s | %d |" % (path, kind, number))
    out += ["", "## For a human", ""]
    if not migration.findings:
        out += ["Nothing.", ""]
    for section, found in migration.findings.items():
        out += ["### %s (%d)" % (section, len(found)), ""]
        for where, text in found:
            if "\n" in text or len(text) > 300:
                out += ["- **%s**" % where, "", "  ~~~~text"] + [
                    "  " + line for line in text.split("\n")] + ["  ~~~~", ""]
            else:
                out.append("- **%s** — %s" % (where, text))
        out.append("")
    out += ["## Samples, before and after", ""]
    for path in dict.fromkeys(sample[0] for sample in migration.samples):
        found = [sample for sample in migration.samples if sample[0] == path]
        chosen = [found[0], max(found, key=lambda sample: len(sample[2]) - len(sample[3]))]
        chosen += [sample for sample in found if "\n### " in sample[2]][:1]
        for _, title, before, after in dict.fromkeys(chosen):
            out += ["### `%s` — %s" % (path, title), "", "Before:", "", "~~~~text", before,
                    "~~~~", "", "After:", "", "~~~~text", after, "~~~~", ""]
    return "\n".join(out) + "\n"


def run(root, apply=False, report=None):
    """The console's lines and the exit code."""
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
    migration = Migration(root, set(tracked))
    if not any(path in migration.texts for path in FOUNDATION):
        return ["%s holds no foundation: no file of foundations/ to migrate" % root], 2
    migration.read_names()
    migration.read_lists()
    new = {DECISIONS: migration.migrate_decisions(), INVARIANTS: migration.migrate_invariants(),
           FACTS: migration.migrate_facts(), GLOSSARY: migration.migrate_glossary(),
           PART_MAP: migration.migrate_part_map()}
    migration.migrate_tracked()
    migration.check_methods()
    migration.violated_tests()
    for path, lines in new.items():
        if path in migration.texts and lines != migration.lines(path):
            migration.writes[path] = migration.texts[path].dump(lines)
    migration.opening_texts()
    report = report or os.path.join(root, *DEFAULT_REPORT.split("/"))
    os.makedirs(os.path.dirname(os.path.abspath(report)), exist_ok=True)
    with open(report, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(render(migration, apply))
    if apply:
        for path, data in migration.writes.items():
            with open(os.path.join(root, *path.split("/")), "wb") as handle:
                handle.write(data)
        for path in migration.removals:
            os.remove(os.path.join(root, *path.split("/")))
    changes = sum(migration.counts.values())
    places = sum(len(found) for found in migration.findings.values())
    lines = ["%s: %d change%s in %d file%s, %d file%s removed; %d place%s for a human" % (
        "applied" if apply else "trial run, nothing written", changes, "" if changes == 1 else "s",
        len(migration.writes), "" if len(migration.writes) == 1 else "s",
        len(migration.removals), "" if len(migration.removals) == 1 else "s",
        places, "" if places == 1 else "s"), "report: %s" % report]
    return lines, 1 if places else 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    apply, report, rest = False, None, []
    arguments = iter(argv)
    for argument in arguments:
        if argument == "--apply":
            apply = True
        elif argument == "--report":
            report = next(arguments, None)
            if report is None:
                rest.append(argument)
        else:
            rest.append(argument)
    if len(rest) > 1 or any(argument.startswith("-") for argument in rest):
        print("usage: migrate_foundation.py [ROOT] [--apply] [--report PATH]")
        return 2
    sys.stdout.reconfigure(encoding="ascii", errors="backslashreplace")
    lines, code = run(rest[0] if rest else ".", apply, report)
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
