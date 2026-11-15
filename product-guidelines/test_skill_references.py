"""Tests that a skill of `product-guidelines/` or `project-level/` points at what exists.

A session follows a pointer of a skill file: a file of the-way it names, a step of a file, a heading
of a file. A pointer that names what is not there is found only by the session that follows it, so
the test finds it first. The skill files read are `SKILL.md` and the method files beside it and
below it, in the directories of those two parts that hold a `SKILL.md`; the other skills of the-way
are not read (the pointers a skill of another part makes are that part's). Three kinds of pointer
are read, each from the text of a skill file as it stands:

- A file: a code span, or each word of one, ending in `.md`, `.py`, `.json`, `.yml`, `.yaml` or
  `.txt`, and the target of a link to a relative path. A `<the-way>/` or `.the-way/` prefix names
  a file of the-way; so does the first directory of a path, where that is a directory of the-way
  that no product has under the same name. A path under `.runs/`, `.github/`, `guidelines/` or
  `foundations/`, `AGENTS.md`, `CLAUDE.md`, a path in the home directory or an absolute one, and
  a path that begins with another `<placeholder>` are a product's, or outside any repository,
  and pass. A bare file name names the file of that name beside the skill or below it. A path whose
  first directory is none of these is reported: it is neither a file of the-way nor a path the
  rule knows as a product's. A placeholder inside a path, `<kind>`, stands for any text of one
  segment, and so does `*`; such a path names a file where one file of the-way matches.
- A step: "step N of `file`", "`file` step N" and the same with the name of a skill in place of
  the file, in any number of steps ("steps 1 and 2"). The steps of a file are its headings that
  begin with a number, or, where it has none, the items of a numbered list at the start of a line.
- A heading: a quotation followed by "in" or "of" and a file or a skill, optionally with "step N
  of" between: `"Reading the foundation" in `elements/common/way_of_working.md``. The headings of a
  file are its Markdown headings and the bold lead-ins that open a list item or a paragraph
  (`- **A new kind.** Where...`), which the skills name the way they name a heading, each without
  its number, emphasis and code marks and the full stop that ends a lead-in.

The text a pointer is read from is never run: a pointer is looked up in the list of the files of
the-way made by listing its directories, so that a crafted path opens nothing, and a text of a skill
file reaches a message only quoted.

Run from the root of the-way: python -B gate/run_tests.py product-guidelines
"""

import os
import posixpath
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
THE_WAY = Path(__file__).resolve().parent.parent

# The parts whose skills are read.
PARTS = ("product-guidelines", "project-level")
# The endings that make a word of a code span a file.
EXTENSIONS = (".md", ".py", ".json", ".yml", ".yaml", ".txt")
# The first directories whose paths are a product's, though the-way has a directory of the name.
PRODUCT_DIRECTORIES = (".runs", ".github", "guidelines", "foundations")
# The files a product has at its root, though the-way has one of the name.
PRODUCT_FILES = ("AGENTS.md", "CLAUDE.md")
# The prefixes that name a file of the-way, whatever else the first directory is.
THE_WAY_PREFIXES = ("<the-way>/", ".the-way/")

FENCE = re.compile(r"^(```|~~~).*?^\1[ \t]*$", re.MULTILINE | re.DOTALL)
SPAN = re.compile(r"`([^`\n]+)`")
LINK = re.compile(r"\]\(([^)\s]+)\)")
URL_LINK = re.compile(r"\[[^\]]*\]\([a-zA-Z][a-zA-Z0-9+.-]*:[^)]*\)")
STEP_NUMBERS = r"[Ss]teps?\s+(\d+(?:\s*(?:,|and|or|to)\s*\d+)*)"
STEPS_OF = re.compile(STEP_NUMBERS + r"\s+(?:of|in)\s+(?:the\s+)?(?:skill\s+)?`([^`\n]+)`")
STEPS_AFTER = re.compile(r"`([^`\n]+)`(?:'s)?\s+(?:its\s+)?" + STEP_NUMBERS)
HEADING_OF = re.compile(
    r"[\"\u201c]([^\"\u201d\n]{2,80})[\"\u201d]\s+(?:in|of)\s+(?:step\s+\d+\s+of\s+)?"
    r"(?:the\s+)?(?:skill\s+)?`([^`\n]+)`")
NAME_LINE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)
NUMBERED_HEADING = re.compile(r"^#{1,6}[ \t]+(?:Step[ \t]+)?(\d+)[.:)]?(?:[ \t]|$)", re.MULTILINE)
NUMBERED_ITEM = re.compile(r"^(\d+)[.)][ \t]", re.MULTILINE)
HEADING_LINE = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
LEAD_IN = re.compile(r"^[ \t]*(?:[-*][ \t]+|\d+[.)][ \t]+)?\*\*([^*\n]{2,80}?)[.:]?\*\*",
                     re.MULTILINE)
PLACEHOLDER = re.compile(r"<[^<>/\s]*>|\*")
SKILL_NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def shown(text):
    """The text quoted for a message: one line, with every control character escaped."""
    return ascii(text)[:200]


def list_files(root):
    """The paths, with `/`, of every file under `root`, outside the directories whose name begins
    with a dot (`.git`, `.runs`, the entry points of the skills)."""
    found = set()
    for directory, names, files in os.walk(root):
        names[:] = [name for name in names if not name.startswith(".")]
        for name in files:
            full = os.path.join(directory, name)
            found.add(os.path.relpath(full, root).replace(os.sep, "/"))
    return found


def read_text(root, path):
    """The text of a file, or None where it cannot be read as UTF-8."""
    try:
        return (Path(root) / path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError, ValueError):
        return None


class World:
    """The files of a checkout of the-way and what the pointers of a skill file look up in them."""

    def __init__(self, root):
        self.root = Path(root)
        self.files = list_files(self.root)
        self.roots = {path.split("/")[0] for path in self.files}
        self.skills = {}
        for path in sorted(self.files):
            if path.endswith("/SKILL.md"):
                name = skill_name(read_text(self.root, path) or "")
                if name:
                    self.skills.setdefault(name, path)
        self._texts = {}

    def text(self, path):
        if path not in self._texts:
            self._texts[path] = read_text(self.root, path)
        return self._texts[path]

    def skill_files(self):
        """The skill files of the parts read, each with the directory of its skill."""
        skill_dirs = sorted(posixpath.dirname(path) for path in self.files
                            if path.endswith("/SKILL.md") and path.split("/")[0] in PARTS)
        found = {}
        for path in sorted(self.files):
            if path.endswith(".md") and path.split("/")[0] in PARTS:
                owners = [d for d in skill_dirs if path.startswith(d + "/")]
                if owners:
                    found[path] = max(owners, key=len)
        return found

    def steps(self, path):
        text = self.text(path) or ""
        numbered = NUMBERED_HEADING.findall(text)
        return {int(number) for number in (numbered or NUMBERED_ITEM.findall(text))}

    def headings(self, path):
        found = set()
        text = self.text(path) or ""
        for raw in HEADING_LINE.findall(text) + LEAD_IN.findall(text):
            found.add(plain_heading(raw))
        return found


def skill_name(text):
    """The `name:` of a skill's front matter, or None."""
    if not text.startswith("---"):
        return None
    match = NAME_LINE.search(text[3:].split("\n---", 1)[0])
    return match.group(1) if match else None


def plain_heading(text):
    """A heading or a quotation as compared: no number, emphasis or code marks, one space between
    words."""
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"^\s*(?:Step\s+)?\d+[.:)]\s*", "", text)
    return " ".join(text.split())


def word_of(span):
    """The words of a code span that can name a file, cleaned of what stands around a name."""
    for word in span.split():
        word = word.strip("\"'(),;:").rstrip(".")
        word = word.split("#")[0]
        if word.lower().endswith(EXTENSIONS) and not word.startswith("-") and "=" not in word:
            yield word


def locate(word, skill_dir, world, base=None):
    """What a path names, as (kind, value): ("outside", None) for a product's path or one outside
    any repository; ("file", path) where it names a file of the-way; ("dead", reason) where it
    names none. `base` is the directory of a link, which the target is relative to."""
    if word.startswith(("~", "/")) or re.match(r"^[A-Za-z]:", word) or "\\" in word:
        return "outside", None
    prefixed = False
    for prefix in THE_WAY_PREFIXES:
        if word.startswith(prefix):
            word, prefixed = word[len(prefix):], True
            break
    if "/" not in word:
        if not prefixed and word in PRODUCT_FILES:
            return "outside", None
        if base is not None:
            relative = posixpath.normpath(posixpath.join(base, word))
            return resolve(relative, world)
        beside = sorted(path for path in world.files
                        if path.startswith(skill_dir + "/") and path.rsplit("/", 1)[-1] == word)
        if beside:
            return "file", beside[0]
        return "dead", "no file of that name beside the skill or below it"
    first = word.split("/")[0]
    if not prefixed:
        if base is not None:
            return resolve(posixpath.normpath(posixpath.join(base, word)), world)
        if first in PRODUCT_DIRECTORIES or (first.startswith("<") and first.endswith(">")):
            return "outside", None
        if first not in world.roots:
            return "dead", "neither a directory of the-way nor a path the test knows as a product's"
    return resolve(posixpath.normpath(word), world)


def resolve(path, world):
    """("file", path) where `path` names a file of the-way (a placeholder or `*` standing for any
    text of one segment), ("dead", reason) where it names none."""
    if path.startswith("../") or path == ".." or path.startswith("/") or "\0" in path:
        return "dead", "a path that leaves the-way"
    if PLACEHOLDER.search(path):
        pattern = "".join("[^/]*" if PLACEHOLDER.fullmatch(piece) else re.escape(piece)
                          for piece in re.split("(<[^<>/\\s]*>|\\*)", path))
        matches = sorted(candidate for candidate in world.files
                         if re.fullmatch(pattern, candidate))
        return ("file", matches[0]) if matches else ("dead", "no file matches")
    if path in world.files:
        return "file", path
    return "dead", "no such file in the-way"


def target_of(name, skill_dir, world):
    """The file a pointer's name stands for: ("file", path), ("outside", None) or ("dead", why).
    A name with no extension is the name of a skill."""
    if "." in name or "/" in name:
        word = next(word_of(name), None)
        if word is None:
            return "outside", None
        return locate(word, skill_dir, world)
    if SKILL_NAME.match(name):
        if name in world.skills:
            return "file", world.skills[name]
        return "dead", "no skill of that name in the-way"
    return "outside", None


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def numbers_of(text):
    return [int(number) for number in re.findall(r"\d+", text)]


def check_text(text, path, skill_dir, world):
    """The problems of one skill file, and how many pointers of each kind it made: a tuple
    (problems, counts), a problem a line "path:line: what"."""
    problems = []
    counts = {"file": 0, "step": 0, "heading": 0}

    def report(offset, message):
        problems.append("%s:%d: %s" % (path, line_of(text, offset), message))

    def check_file(offset, word, base=None):
        counts["file"] += 1
        kind, value = locate(word, skill_dir, world, base)
        if kind == "dead":
            report(offset, "%s names no file of the-way: %s" % (shown(word), value))

    blank = FENCE.sub(lambda match: re.sub(r"[^\n]", " ", match.group(0)), text)
    for match in FENCE.finditer(text):
        offset = match.start()
        for line in match.group(0).split("\n"):
            for word in word_of(line):
                check_file(offset, word)
            offset += len(line) + 1
    prose = URL_LINK.sub(lambda match: " " * len(match.group(0)), blank)
    for match in SPAN.finditer(prose):
        for word in word_of(match.group(1)):
            check_file(match.start(), word)
    here = posixpath.dirname(path)
    for match in LINK.finditer(prose):
        target = match.group(1).split("#")[0]
        if target and not target.startswith(("mailto:", "<")):
            counts["file"] += 1
            kind, value = locate(target, skill_dir, world, base=here)
            if kind == "dead":
                report(match.start(), "link %s names no file of the-way: %s" % (
                    shown(target), value))

    def named(offset, name):
        """The file of a step or heading pointer, None where it is not a file of the-way."""
        kind, value = target_of(name, skill_dir, world)
        if kind == "dead":
            report(offset, "%s names no file or skill of the-way: %s" % (shown(name), value))
        return value if kind == "file" else None

    for pattern, name_group, numbers_group in ((STEPS_OF, 2, 1), (STEPS_AFTER, 1, 2)):
        for match in pattern.finditer(prose):
            target = named(match.start(), match.group(name_group))
            if target is None:
                continue
            for number in numbers_of(match.group(numbers_group)):
                counts["step"] += 1
                if number not in world.steps(target):
                    report(match.start(), "step %d of %s, which has no such step" % (
                        number, shown(target)))
    for match in HEADING_OF.finditer(prose):
        target = named(match.start(), match.group(2))
        if target is None:
            continue
        counts["heading"] += 1
        if plain_heading(match.group(1)) not in world.headings(target):
            report(match.start(), "heading %s of %s, which has no such heading" % (
                shown(match.group(1)), shown(target)))
    return problems, counts


def check_tree(root):
    """(problems, counts, number of skill files) of the skill files of the parts read under
    `root`."""
    world = World(root)
    problems = []
    counts = {"file": 0, "step": 0, "heading": 0}
    files = world.skill_files()
    for path, skill_dir in files.items():
        text = world.text(path)
        if text is None:
            problems.append("%s: cannot be read as UTF-8 text" % shown(path))
            continue
        found, made = check_text(text, path, skill_dir, world)
        problems.extend(found)
        for kind in counts:
            counts[kind] += made[kind]
    return sorted(set(problems)), counts, len(files)


class TheSkillsOfTheWay(unittest.TestCase):

    def test_no_skill_file_holds_a_dead_pointer(self):
        # Break caught: a method file renamed, moved or dropped, or a step or a heading of a file
        # renumbered or reworded, while a skill file still points at the old one; the session that
        # follows the pointer finds nothing there.
        problems, _, _ = check_tree(THE_WAY)
        self.assertEqual([], problems)

    def test_the_test_reads_the_skills_and_the_pointers_of_each_kind(self):
        # Break caught: a rule that matches no skill file or no pointer of a kind, which would
        # leave the test above passing over an empty reading. The counts are well below what the
        # skills hold when the test is written (84 skill files, 463 file pointers, 43 of steps
        # and 30 of headings), so that a few pointers removed do not fail it.
        _, counts, skill_files = check_tree(THE_WAY)
        self.assertGreaterEqual(skill_files, 60)
        self.assertGreaterEqual(counts["file"], 300)
        self.assertGreaterEqual(counts["step"], 30)
        self.assertGreaterEqual(counts["heading"], 15)


FIXTURE = {
    "elements/common/way.md": "# Way\n\n## Reading the foundation\n\n## 1. Read\n\n## 2. Search\n",
    "elements/common/numbered.md": "# N\n\nIntro.\n\n1. **First.** x\n2. **Second.** y\n",
    "elements/common/tool.py": "",
    "foundations/decisions.md": "# The-way's own decisions\n",
    "relation-model/other/skill/SKILL.md": "---\nname: elsewhere\ndescription: x\n---\n\n"
                                           "## 0. Start\n\n## 1. Next\n",
    "product-guidelines/area/SKILL.md": "---\nname: area-skill\ndescription: x\n---\n\n"
                                        "# The area\n\n## 0. Read\n\n## 1. Do\n\n"
                                        "- **A lead-in.** Text.\n\n**Another lead-in** text.\n\n"
                                        "A line with **bold** inside.\n",
    "product-guidelines/area/sibling.md": "# Sibling\n",
    "product-guidelines/area/deep/inner.md": "# Inner\n\n## 1. Only\n",
    "product-guidelines/area/template.md": "# T\n",
    "product-guidelines/other/template.md": "# Other T\n",
    "product-guidelines/plain.md": "# Not a skill file, beside no SKILL.md\n",
}


class Reading(unittest.TestCase):
    """The rule, run on a tree of its own: each pointer made in the text of a skill file, with the
    problems it gives."""

    def problems_of(self, text, extra=None, path="product-guidelines/area/method.md"):
        files = dict(FIXTURE)
        files.update(extra or {})
        files[path] = text
        with tempfile.TemporaryDirectory() as root:
            for name, content in files.items():
                target = Path(root) / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content if isinstance(content, bytes) else content.encode())
            problems, _, _ = check_tree(root)
        return problems

    def test_a_file_of_the_way_is_found_and_a_dead_one_reported(self):
        # Break caught: a path looked up wrongly (a directory missing, a name compared in part),
        # so that a dead pointer passes or a live one is reported.
        self.assertEqual([], self.problems_of("See `elements/common/way.md` and `elements/common/"
                                              "tool.py`."))
        problems = self.problems_of("See `elements/common/gone.md`.")
        self.assertEqual(1, len(problems))
        self.assertIn("elements/common/gone.md", problems[0])
        self.assertIn(":1:", problems[0])

    def test_a_product_path_passes_and_a_path_of_nobody_is_reported(self):
        # Break caught: a path of a product taken for one of the-way, so that every skill that
        # names the product's `guidelines/coding.md` fails; or a path with an unknown first
        # directory taken for a product's, so that a mistyped directory passes.
        product = ("`guidelines/coding.md` `guidelines/coding-<kind>.md` `AGENTS.md` "
                   "`CLAUDE.md` `foundations/decisions.md` `.runs/coding/<question>.md` "
                   "`.github/workflows/deploy.yml` `<product-repository>/.runs/x/<name>.md` "
                   "`~/.the-way/locations.json` `/etc/hosts.txt` `C:/Users/x/file.md`")
        self.assertEqual([], self.problems_of(product))
        problems = self.problems_of("`src/app.py` and `elements/commn/way.md`")
        self.assertEqual(2, len(problems))

    def test_a_prefix_names_a_file_of_the_way_whatever_its_first_directory(self):
        # Break caught: the prefixes `<the-way>/` and `.the-way/` ignored, so that
        # `<the-way>/foundations/decisions.md` is taken for the product's and a dead one passes.
        self.assertEqual([], self.problems_of("`<the-way>/foundations/decisions.md` "
                                              "`.the-way/elements/common/way.md`"))
        problems = self.problems_of("`<the-way>/foundations/gone.md` `.the-way/foundations/x.md`")
        self.assertEqual(2, len(problems))

    def test_a_bare_name_is_the_sibling_beside_the_skill_or_below_it(self):
        # Break caught: a bare name looked up in all of the-way (a file of another part passes),
        # or not looked up below the skill (a file in a subdirectory is reported), or taken for
        # a product's (a dead one passes).
        self.assertEqual([], self.problems_of("`SKILL.md` `sibling.md` `inner.md` `template.md`"))
        problems = self.problems_of("`tool.py` `way.md` `gone.md`")
        self.assertEqual(3, len(problems))

    def test_a_bare_name_in_a_directory_below_a_skill_looks_beside_that_skill(self):
        # Break caught: the skill of a file taken to be the first one found, not the nearest above.
        problems = self.problems_of("`template.md` `sibling.md`",
                                    path="product-guidelines/other/method.md",
                                    extra={"product-guidelines/other/SKILL.md":
                                           "---\nname: other-skill\ndescription: x\n---\n"})
        self.assertEqual(1, len(problems))
        self.assertIn("sibling.md", problems[0])

    def test_a_placeholder_stands_for_any_one_segment(self):
        # Break caught: a path with `<name>` looked up as written, so that a the-way path with a
        # placeholder is always reported, or matched across directories.
        self.assertEqual([], self.problems_of("`product-guidelines/<discipline>/template.md`"))
        problems = self.problems_of("`product-guidelines/<discipline>/gone.md` "
                                    "`product-guidelines/<d>/inner.md`")
        self.assertEqual(2, len(problems))

    def test_a_step_of_a_file_is_found_and_a_missing_one_reported(self):
        # Break caught: steps read from the wrong headings, a list of steps not read where a file
        # has no numbered heading, or a number compared as text.
        self.assertEqual([], self.problems_of(
            "step 1 of `elements/common/way.md`, `elements/common/way.md` step 2, steps 0 and 1 "
            "of `SKILL.md`, step 2 of `elements/common/numbered.md`, step 1 of `inner.md`."))
        problems = self.problems_of("step 3 of `elements/common/way.md`; "
                                    "`elements/common/numbered.md` steps 1 and 3; "
                                    "step 2 of `inner.md`.")
        self.assertEqual(3, len(problems))
        self.assertTrue(all("no such step" in problem for problem in problems))

    def test_a_step_of_a_skill_named_by_its_name_is_read_in_its_file(self):
        # Break caught: the name of a skill not looked up in the skills of the-way, so that a step
        # of a renamed or removed skill passes.
        self.assertEqual([], self.problems_of("`elsewhere` step 1, step 0 of the skill `area-skill`"
                                              ", `elsewhere` steps 0 to 1"))
        problems = self.problems_of("`elsewhere` step 2 and `no-such-skill` step 1")
        self.assertEqual(2, len(problems))

    def test_a_heading_of_a_file_is_found_and_a_missing_one_reported(self):
        # Break caught: a heading compared with its number, its emphasis or a different case, or
        # not compared at all.
        self.assertEqual([], self.problems_of(
            '"Reading the foundation" in `elements/common/way.md`, "Read" of step 1 of '
            '`elements/common/way.md`, the section "Do" in `SKILL.md`, "A lead-in" in `SKILL.md`, '
            '"Another lead-in" in `SKILL.md`, and \u201cNext\u201d of `elsewhere`.'))
        problems = self.problems_of('"Reading foundation" in `elements/common/way.md` and '
                                    '"reading the foundation" in `elements/common/way.md` and '
                                    '"bold" in `SKILL.md` (a word in a line is no lead-in)')
        self.assertEqual(3, len(problems))
        self.assertTrue(all("no such heading" in problem for problem in problems))

    def test_a_pointer_in_a_fence_and_one_in_a_link_are_read_and_a_url_is_not(self):
        # Break caught: a fenced block or a link target skipped, or a file named in the text of a
        # link to a page of the web, which is no file of the-way, reported.
        text = ("```\nsee elements/common/gone.md here\nalso/gone.md\n```\n"
                "[a link](sibling.md) and [dead](missing.md) and "
                "[`SKILL.md`](https://example.org/x/SKILL.md) and "
                "[web](https://example.org/a.md)\n")
        problems = self.problems_of(text)
        self.assertEqual(3, len(problems))
        self.assertTrue(any(":2:" in problem for problem in problems))
        self.assertTrue(any(":3:" in problem for problem in problems))
        self.assertTrue(any("missing.md" in problem for problem in problems))

    def test_a_file_outside_a_skill_directory_is_not_read(self):
        # Break caught: every file of the two parts read, so that a template or a procedure beside
        # no skill, which the row of the task leaves out, fails the test.
        self.assertEqual([], self.problems_of("`elements/common/gone.md`",
                                              path="product-guidelines/plain2.md"))
        self.assertEqual([], self.problems_of("`elements/common/gone.md`",
                                              path="elements/common/readme.md"))

    def test_crafted_text_gives_problems_and_no_error(self):
        # Break caught: a path that leaves the-way or holds a character that opens no file, a
        # text that cannot be read, or a quotation of a pointer with a line break, crashing the
        # reading or putting a line of the input into a message unescaped.
        crafted = ("`../../../etc/passwd.md` `elements/../../x.md` `a\x00b.md` `" + "a/" * 5000 +
                   "x.md` `a\u2028b.md` \"" + "x" * 70 + "\" in `elements/common/way.md`\n"
                   "step 99999999999999999999 of `elements/common/way.md`\n")
        problems = self.problems_of(crafted)
        self.assertGreaterEqual(len(problems), 4)
        for problem in problems:
            self.assertEqual(1, len(problem.splitlines()))
            self.assertLessEqual(len(problem), 400)
            self.assertTrue(problem.isascii())
        undecodable = self.problems_of(
            "x", extra={"product-guidelines/area/bad.md": b"\xff\xfe\x00"})
        self.assertEqual(1, len(undecodable))
        self.assertIn("UTF-8", undecodable[0])


if __name__ == "__main__":
    unittest.main()
