"""Tests of the invariants `instruction-file-imports` and `root-claude-md-import`.

A session that opens a repository of the-way reads its repository instruction files: every
`AGENTS.md` and `CLAUDE.md` git tracks, and the Markdown files the root `AGENTS.md` or `CLAUDE.md`
names by its path. None of them may hold an `@` a tool would take for an import of another file,
save the one line that makes the root `CLAUDE.md` load the root `AGENTS.md`; and where git tracks a
root `CLAUDE.md`, its text begins with that line.

Every value the tests expect is written out below, taken from the sentences of the two invariants.
The file imports nothing from `instruction-files/` and nothing from
`agent-instructions/skill_entry_points.py`, and finds the files of each sentence with its own call
to git and its own pattern: were it to ask the check script which files to read or what counts as
an import, a change to that script would move both sides together and the tests would stay green.

Run from the root of the-way:
python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl
"""

import os
import re
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from unittest import mock

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The values the sentence of `instruction-file-imports/1` and the glossary entry
# `repository instruction file` name.
INSTRUCTION_NAMES = ("AGENTS.md", "CLAUDE.md")
MARKDOWN_ENDINGS = (".md", ".markdown")
# The characters, besides the start of a line and whitespace, that may stand right before a
# counted `@`.
BEFORE_AT = ("(", "[", "{", '"', "'", "“", "‘", "„")
# What must follow a counted `@` somewhere before the next whitespace.
AFTER_AT = (".", "/")
# The characters, besides an ASCII letter or digit, that keep a path from naming its file when
# they stand right before it.
NOT_BEFORE_PATH = (".", "-", "_", "/", "\\")
ASCII_ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
FENCES = ("```", "~~~")
# The one line the root `CLAUDE.md` may open with: the import of the root `AGENTS.md`.
ROOT_IMPORT_LINE = "@AGENTS.md"

# The values the sentence of `root-claude-md-import/1` names.
ROOT_CLAUDE = "CLAUDE.md"
ROOT_IMPORT = b"@AGENTS.md"
LINE_BREAKS = (b"\n", b"\r\n")

# Three files the population of the-way has to hold: a positive control.
CONTROL = ("AGENTS.md", "CLAUDE.md", "agent-instructions/README.md")


def tracked(root):
    """Every path, from `root`, that git tracks there, with `/` between directories."""
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True,
                            check=True)
    return sorted({path for path in result.stdout.decode("utf-8").split("\0") if path})


def read(root, path):
    with open(os.path.join(root, *path.split("/")), "rb") as handle:
        return handle.read()


def names(text, path):
    """Whether `text` names `path`: the path, written with `/` or with `\\` between directories,
    stands somewhere in it with no ASCII letter or digit and none of `.`, `-`, `_`, `/` and `\\`
    right before it."""
    for written in {path, path.replace("/", "\\")}:
        start = text.find(written)
        while start != -1:
            if start == 0 or (text[start - 1] not in ASCII_ALNUM
                              and text[start - 1] not in NOT_BEFORE_PATH):
                return True
            start = text.find(written, start + 1)
    return False


def population(root):
    """The repository instruction files of the repository at `root`: every tracked `AGENTS.md`
    and `CLAUDE.md`, and every tracked Markdown file the root `AGENTS.md` or `CLAUDE.md` names by
    its path."""
    files = tracked(root)
    found = {path for path in files if path.split("/")[-1] in INSTRUCTION_NAMES}
    texts = []
    for root_file in INSTRUCTION_NAMES:
        if root_file in files:
            try:
                texts.append(read(root, root_file).decode("utf-8", errors="replace"))
            except OSError:
                pass
    for path in files:
        if path.endswith(MARKDOWN_ENDINGS) and any(names(text, path) for text in texts):
            found.add(path)
    return sorted(found)


def code_span_mask(line):
    """For each character of `line`, whether it lies in a code span: a span runs from a run of
    backticks to the next run of as many backticks on the same line."""
    masked = [False] * len(line)
    runs = [(match.start(), match.end()) for match in re.finditer(r"`+", line)]
    index = 0
    while index < len(runs):
        start, end = runs[index]
        width = end - start
        closing = next((other for other in range(index + 1, len(runs))
                        if runs[other][1] - runs[other][0] == width), None)
        if closing is None:
            index += 1
            continue
        for position in range(start, runs[closing][1]):
            masked[position] = True
        index = closing + 1
    return masked


def fenced_lines(lines):
    """The indexes of the lines that lie in a fenced code block: a block runs from a line whose
    first characters other than spaces are three backticks or three tildes to the next such line,
    both lines included. An opening line with no such line after it opens no block."""
    fence_lines = [index for index, line in enumerate(lines)
                   if line.lstrip(" ").startswith(FENCES)]
    inside = set()
    for opening, closing in zip(fence_lines[0::2], fence_lines[1::2]):
        inside.update(range(opening, closing + 1))
    return inside


def counted_ats(line):
    """The columns, from 0, of each `@` of `line` that the sentence counts, ignoring code spans
    and fences: one at the start of the line or right after whitespace or one of `BEFORE_AT`,
    followed, before the next whitespace, by a `.` or a `/`."""
    masked = code_span_mask(line)
    columns = []
    for column, character in enumerate(line):
        if character != "@" or masked[column]:
            continue
        if column > 0 and not (line[column - 1].isspace() or line[column - 1] in BEFORE_AT):
            continue
        word = re.match(r"\S*", line[column + 1:]).group(0)
        if any(mark in word for mark in AFTER_AT):
            columns.append(column)
    return columns


def import_problems(root):
    """One line per `@` that a repository instruction file of the repository at `root` holds
    against the sentence of `instruction-file-imports/1`, naming its file, line and column."""
    found = []
    for path in population(root):
        try:
            text = read(root, path).decode("utf-8", errors="replace")
        except OSError as error:
            found.append("%s: cannot be read (%s)" % (path, error.strerror))
            continue
        lines = [line[:-1] if line.endswith("\r") else line for line in text.split("\n")]
        fenced = fenced_lines(lines)
        for index, line in enumerate(lines):
            if index in fenced:
                continue
            if path == ROOT_CLAUDE and index == 0 and line == ROOT_IMPORT_LINE:
                continue
            for column in counted_ats(line):
                word = re.match(r"\S*", line[column:]).group(0)
                found.append("%s:%d:%d: an import-like `%s` outside code spans and fenced code "
                             "blocks" % (path, index + 1, column + 1, word))
    return found


def root_import_problems(root):
    """One line, naming the file, when the repository at `root` tracks a root `CLAUDE.md` whose
    text does not begin with `@AGENTS.md` followed directly by `\\n`, `\\r\\n` or the end of the
    text; none when it tracks no root `CLAUDE.md`."""
    if ROOT_CLAUDE not in tracked(root):
        return []
    try:
        data = read(root, ROOT_CLAUDE)
    except OSError as error:
        return ["%s: cannot be read (%s)" % (ROOT_CLAUDE, error.strerror)]
    rest = data[len(ROOT_IMPORT):]
    if data.startswith(ROOT_IMPORT) and (rest == b"" or rest.startswith(LINE_BREAKS)):
        return []
    return ["%s:1: its text begins with %r, not with `@AGENTS.md` followed by a line break or "
            "the end of the text" % (ROOT_CLAUDE, data[:len(ROOT_IMPORT) + 2])]


def build(directory, files, untracked=()):
    """Write `files` (path -> text) and `untracked` into a fresh repository at `directory` and
    let git track `files` only."""
    subprocess.run(["git", "init", "-q"], cwd=directory, check=True, capture_output=True)
    for path, text in list(files.items()) + list(dict(untracked).items()):
        full = os.path.join(directory, *path.split("/"))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "wb") as handle:
            handle.write(text if isinstance(text, bytes) else text.encode("utf-8"))
    if files:
        subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "core.safecrlf=false", "add",
                        "--"] + sorted(files), cwd=directory, check=True, capture_output=True)


def clean_environment():
    return mock.patch.dict(os.environ, {key: value for key, value in os.environ.items()
                                        if not key.startswith("GIT_")}, clear=True)


def located(found):
    """The (file, line) of each reported problem."""
    return Counter((match.group(1), int(match.group(2)))
                   for match in (re.match(r"^(.*?):(\d+):", line) for line in found) if match)


# A root `AGENTS.md` holding every kind of `@` the sentence counts and every kind it lets pass,
# and the paths that name, or fail to name, the files beside it.
ROOT_AGENTS = "\n".join([
    "# Agents",                                                        # 1
    "See @docs/rules.md for the rules.",                               # 2 counted
    "Mail a@example.com or ping @someone today.",                      # 3
    "Inline `@docs/rules.md` and ``a ` @b.md`` stay quiet.",           # 4
    "```",                                                             # 5
    "@fenced.md",                                                      # 6
    "```",                                                             # 7
    "  ~~~",                                                           # 8
    "@tilde.md",                                                       # 9
    "~~~",                                                             # 10
    "(@p.md) [@b.md] {@c.md} \"@d.md\" '@e.md' “@f.md” ‘@g.md’ „@h.md",
    "x@letter.md -@dash.md @@twice @nothing here",                     # 12
    "@./relative",                                                     # 13 counted
    "Unclosed ` @open.md here",                                        # 14 counted
    "Across ``lines @split.md",                                        # 15 counted
    "end`` of it.",                                                    # 16
    "\t```",                                                           # 17 no fence
    "@tabbed.md",                                                      # 18 counted
    "\t```",                                                           # 19
    "    ```",                                                         # 20
    "@deep.md",                                                        # 21
    "```",                                                             # 22
    "```",                                                             # 23
    "@mixed.md",                                                       # 24
    "~~~",                                                             # 25
    "@after.md",                                                       # 26 counted
    "@AGENTS.md",                                                      # 27 counted
    "Rules: [linked](docs/linked.md), docs/untracked.md, docs/notes.txt.",
    "Not named: xdocs/l1.md 9docs/l2.md .docs/l3.md -docs/l4.md _docs/l5.md /docs/l6.md "
    "\\docs\\l7.md",
    "Named: łdocs/accent.md",                                     # 30
    "",
])

ROOT_CLAUDE_TEXT = "@AGENTS.md\n@AGENTS.md\nAlso docs\\other.markdown, docs/unnamed.txt.\n"

IMPORT_FIXTURE = {
    "AGENTS.md": ROOT_AGENTS,
    "CLAUDE.md": ROOT_CLAUDE_TEXT,
    "docs/rules.md": "Rule one.\n@named.md\n",
    "docs/linked.md": "(@linked.md)\n",
    "docs/other.markdown": "Text @other.md\n",
    "docs/accent.md": "@accent.md\n",
    "docs/l1.md": "@l.md\n",
    "docs/l2.md": "@l.md\n",
    "docs/l3.md": "@l.md\n",
    "docs/l4.md": "@l.md\n",
    "docs/l5.md": "@l.md\n",
    "docs/l6.md": "@l.md\n",
    "docs/l7.md": "@l.md\n",
    "docs/unnamed.md": "@unnamed.md\n",
    "docs/notes.txt": "@notes.md\n",
    "docs/nested.md": "@nested.md\n",
    "sub/CLAUDE.md": "@AGENTS.md\n",
    "pkg/AGENTS.md": "Read docs/nested.md first.\nThen @x/y and `@z.md`.\n",
}

IMPORT_UNTRACKED = {
    "docs/untracked.md": "@untracked.md\n",
    "extra/AGENTS.md": "@extra.md\n",
}

IMPORT_POPULATION = [
    "AGENTS.md", "CLAUDE.md", "docs/accent.md", "docs/linked.md", "docs/other.markdown",
    "docs/rules.md", "pkg/AGENTS.md", "sub/CLAUDE.md",
]

IMPORT_EXPECTED = Counter({
    ("AGENTS.md", 2): 1, ("AGENTS.md", 11): 8, ("AGENTS.md", 13): 1, ("AGENTS.md", 14): 1,
    ("AGENTS.md", 15): 1, ("AGENTS.md", 18): 1, ("AGENTS.md", 26): 1, ("AGENTS.md", 27): 1,
    ("CLAUDE.md", 2): 1, ("docs/rules.md", 2): 1, ("docs/linked.md", 1): 1,
    ("docs/other.markdown", 1): 1, ("docs/accent.md", 1): 1, ("sub/CLAUDE.md", 1): 1,
    ("pkg/AGENTS.md", 2): 1,
})


class InstructionFiles(unittest.TestCase):
    def test_no_instruction_file_holds_an_import(self):
        # invariant: instruction-file-imports/1
        found_population = population(ROOT)
        for path in CONTROL:
            self.assertIn(path, found_population)
        found = import_problems(ROOT)
        self.assertEqual(found, [], "a repository instruction file of the-way holds an `@` a "
                         "tool would take for an import:\n" + "\n".join(found))

    def test_the_root_claude_md_begins_with_the_import_of_agents_md(self):
        # invariant: root-claude-md-import/1
        found_population = population(ROOT)
        for path in CONTROL:
            self.assertIn(path, found_population)
        self.assertIn(ROOT_CLAUDE, tracked(ROOT))
        found = root_import_problems(ROOT)
        self.assertEqual(found, [], "the root `CLAUDE.md` of the-way does not begin with the "
                         "import of `AGENTS.md`:\n" + "\n".join(found))

    def test_import_problems_reports_each_counted_at_and_passes_the_rest(self):
        """On a repository whose root files hold every kind of `@` the sentence counts and every
        kind it lets pass, and name, or fail to name, the files beside them."""
        with tempfile.TemporaryDirectory() as directory, clean_environment():
            build(directory, IMPORT_FIXTURE, IMPORT_UNTRACKED)
            self.assertEqual(population(directory), IMPORT_POPULATION)
            found = import_problems(directory)
        report = "\n".join(found)
        self.assertEqual(len(found), sum(located(found).values()), report)
        self.assertEqual(located(found), IMPORT_EXPECTED, report)

    def test_import_problems_reads_the_first_line_of_the_root_claude_md_alone(self):
        """The first line of the root `CLAUDE.md` passes when it reads `@AGENTS.md` and nothing
        else, whatever line break ends it; with anything more it counts."""
        cases = (
            ("@AGENTS.md\r\nText.\r\n", []),
            ("@AGENTS.md", []),
            ("@AGENTS.md \nText.\n", [("CLAUDE.md", 1)]),
            ("@AGENTS.md and more\n", [("CLAUDE.md", 1)]),
            ("Text.\n@AGENTS.md\n", [("CLAUDE.md", 2)]),
        )
        for text, expected in cases:
            with self.subTest(text=text), tempfile.TemporaryDirectory() as directory, \
                    clean_environment():
                build(directory, {"AGENTS.md": "# Agents\n", "CLAUDE.md": text})
                found = import_problems(directory)
            self.assertEqual(located(found), Counter(expected), "\n".join(found))

    def test_root_import_problems_reports_a_root_claude_md_without_the_import(self):
        """Each root `CLAUDE.md` text the sentence refuses gives one problem naming the file;
        each it allows, and a repository with no tracked root `CLAUDE.md`, gives none."""
        allowed = (b"@AGENTS.md", b"@AGENTS.md\n", b"@AGENTS.md\nText.\n",
                   b"@AGENTS.md\r\nText.\r\n")
        refused = (b"", b"@AGENTS.md \n", b"@AGENTS.mdx\n", b"\n@AGENTS.md\n",
                   b"\xef\xbb\xbf@AGENTS.md\n", b"@agents.md\n", b"@AGENTS.md\rText.\n",
                   b"# Title\n@AGENTS.md\n", b" @AGENTS.md\n")
        for data in allowed + refused:
            with self.subTest(data=data), tempfile.TemporaryDirectory() as directory, \
                    clean_environment():
                build(directory, {"AGENTS.md": "# Agents\n", "CLAUDE.md": data})
                found = root_import_problems(directory)
            if data in allowed:
                self.assertEqual(found, [], "\n".join(found))
            else:
                self.assertEqual(len(found), 1, "\n".join(found))
                self.assertTrue(found[0].startswith("CLAUDE.md:"), found[0])
        nothing_required = (
            ({"AGENTS.md": "# Agents\n", "sub/CLAUDE.md": "Text.\n"}, {}),
            ({"AGENTS.md": "# Agents\n"}, {"CLAUDE.md": "Text.\n"}),
            ({}, {}),
        )
        for files, untracked in nothing_required:
            with self.subTest(files=files, untracked=untracked), \
                    tempfile.TemporaryDirectory() as directory, clean_environment():
                build(directory, files, untracked)
                self.assertEqual(root_import_problems(directory), [])


if __name__ == "__main__":
    unittest.main()
