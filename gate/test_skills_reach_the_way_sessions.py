"""End-to-end test of the invariant `skill-entry-points`.

Someone adds, renames or moves a skill of the-way, or changes its description; a skill that a
human on the-way could not start under its `the-way-` name, or whose entry points would be offered
to the model by Claude Code, has to be reported before the change reaches the main branch. This
test runs the whole path a session takes: the skills of the-way as git lists them, and the entry
points a session finds for them in `.claude/skills/` and `.agents/skills/`, against each property
the invariant `skill-entry-points` names.

Every value the test expects is written out below, taken from the sentence of that invariant. It
imports nothing that computes entry points and finds the skills with its own call to git: were it
to ask the generator of the entry points what they should be, a change to that generator would
move both sides together and the test would stay green.

Run from the root of the-way: python -B gate/run_tests.py gate
"""

import os
import re
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The values the sentence of `skill-entry-points` names.
CLAUDE_SKILLS = ".claude/skills"
AGENTS_SKILLS = ".agents/skills"
PREFIX = "the-way-"
REQUIRED_WORDS = (
    "--show-superproject-working-tree",
    "git ls-files --stage -- ':/.the-way'",
    "git rev-parse --show-toplevel",
    "If the skill tells you to resolve a link to find the-way, skip that",
    "do not call it",
    "read that skill's `SKILL.md`",
)
HIDING_FIELD = "disable-model-invocation"

# The command that writes the entry points, named in the failure message.
GENERATOR = "python -B agent-instructions/skill_entry_points.py --write"

# Two skills of the-way that discovery has to find: a positive control of the population.
CONTROL = ("elements/decisions/skill/SKILL.md", "task-cycle/skill/SKILL.md")


def collapse(text):
    """The text with every run of whitespace collapsed to one space, and none at either end."""
    return " ".join(text.split())


def discover(root):
    """The paths, from `root`, of every file named `SKILL.md` that git tracks there, or that
    stands untracked and not ignored, outside the `.claude/` and `.agents/` directories at the
    root."""
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "-z",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            ":(glob)**/SKILL.md",
        ],
        cwd=root,
        capture_output=True,
        check=True,
    )
    paths = sorted({path for path in result.stdout.decode("utf-8").split("\0") if path})
    return [path for path in paths if not path.startswith((".claude/", ".agents/"))]


def _unquote_double(value):
    return re.sub(
        r"\\(.)", lambda match: {"n": "\n", "t": "\t"}.get(match.group(1), match.group(1)), value
    )


def frontmatter(text):
    """The top-level fields of the YAML frontmatter `text` opens with, as strings, or None when
    the text opens with none. Reads the forms a skill's name and description take: a plain value,
    continued on indented lines; a single- or double-quoted value, over one line or several; and
    a `>` or `|` block."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if end is None:
        return None
    body = lines[1:end]
    fields = {}
    index = 0
    while index < len(body):
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s+(.*))?$", body[index])
        index += 1
        if not match:
            continue
        key, value = match.group(1), (match.group(2) or "").strip()
        continuation = []
        while index < len(body) and (body[index][:1] in (" ", "\t") or not body[index].strip()):
            continuation.append(body[index])
            index += 1
        if value[:1] in (">", "|"):
            fields[key] = " ".join(line.strip() for line in continuation)
        elif value[:1] in ('"', "'"):
            quote = value[0]
            whole = " ".join([value] + [line.strip() for line in continuation])
            if quote == "'":
                inner = re.match(r"^'((?:[^']|'')*)'", whole)
                fields[key] = inner.group(1).replace("''", "'") if inner else whole[1:]
            else:
                inner = re.match(r'^"((?:[^"\\]|\\.)*)"', whole)
                fields[key] = _unquote_double(inner.group(1)) if inner else whole[1:]
        else:
            whole = " ".join([value] + [line.strip() for line in continuation])
            fields[key] = re.split(r"\s#", whole, maxsplit=1)[0]
    return fields


def entry_problems(copy, data, skill_path, name, description, skills):
    """The properties of the sentence that the entry point `copy`, holding the bytes `data`, of
    the skill at `skill_path` fails, one line each. `skills` holds the name and the path of every
    skill of the-way."""
    found = []
    text = data.decode("utf-8", errors="replace")
    fields = frontmatter(text)
    if fields is None:
        return [copy + ": opens with no frontmatter"]
    if collapse(fields.get("name", "")) != PREFIX + name:
        found.append(
            "%s: its frontmatter names %r, not `%s%s`" % (copy, fields.get("name"), PREFIX, name)
        )
    if not collapse(fields.get("description", "")).startswith(collapse(description)):
        found.append(
            "%s: its description does not start with the description of %s" % (copy, skill_path)
        )
    if collapse(fields.get(HIDING_FIELD, "")) != "true":
        found.append("%s: its frontmatter does not hold `%s: true`" % (copy, HIDING_FIELD))
    if "`" + skill_path + "`" not in text:
        found.append("%s: its text does not contain `%s` in backticks" % (copy, skill_path))
    collapsed = collapse(text)
    for words in REQUIRED_WORDS:
        if collapse(words) not in collapsed:
            found.append("%s: its text does not contain %s" % (copy, words))
    lines = [collapse(line) for line in text.splitlines()]
    for other_name, other_path in skills:
        named = "`" + other_name + "`"
        placed = "`" + other_path + "`"
        if not any(named in line and placed in line for line in lines):
            found.append(
                "%s: no line of its text names %s with %s in backticks" % (copy, named, placed)
            )
    return found


def problems(root):
    """One line per property of the sentence of `skill-entry-points` that the repository at
    `root` fails, naming the file."""
    found = []
    skills = []
    for path in discover(root):
        try:
            with open(os.path.join(root, *path.split("/")), "rb") as handle:
                data = handle.read()
        except OSError as error:
            found.append("%s: cannot be read (%s)" % (path, error.strerror))
            continue
        fields = frontmatter(data.decode("utf-8", errors="replace"))
        name = collapse((fields or {}).get("name", ""))
        if not name:
            found.append(path + ": its frontmatter gives no name")
            continue
        if not collapse((fields or {}).get("description", "")):
            found.append(path + ": its frontmatter gives no description")
        skills.append((path, name, fields.get("description", "")))
    names = [name for _, name, _ in skills]
    listed = [(name, path) for path, name, _ in skills]
    for path, name, description in skills:
        contents = {}
        for base in (CLAUDE_SKILLS, AGENTS_SKILLS):
            copy = "%s/%s%s/SKILL.md" % (base, PREFIX, name)
            full = os.path.join(root, *copy.split("/"))
            if not os.path.isfile(full):
                found.append("%s: no file %s" % (path, copy))
                continue
            with open(full, "rb") as handle:
                contents[copy] = handle.read()
        if len(contents) == 2 and len(set(contents.values())) == 2:
            found.append("%s and %s: not byte-identical" % tuple(contents))
        seen = set()
        for copy, data in contents.items():
            if data in seen:
                continue
            seen.add(data)
            found.extend(entry_problems(copy, data, path, name, description, listed))
    expected = {PREFIX + name for name in names}
    for base in (CLAUDE_SKILLS, AGENTS_SKILLS):
        full = os.path.join(root, *base.split("/"))
        if not os.path.isdir(full):
            continue
        for entry in sorted(os.listdir(full)):
            if (
                entry.startswith(PREFIX)
                and os.path.isdir(os.path.join(full, entry))
                and entry not in expected
            ):
                found.append(
                    "%s/%s: no skill of the-way is named %s" % (base, entry, entry[len(PREFIX) :])
                )
    return found


class SkillsReachTheWaySessions(unittest.TestCase):
    def test_every_skill_reaches_a_session_on_the_way(self):
        # invariant: skill-entry-points
        discovered = discover(ROOT)
        for path in CONTROL:
            self.assertIn(path, discovered)
        found = problems(ROOT)
        self.assertEqual(
            found,
            [],
            "a skill of the-way whose entry points break the invariant `skill-entry-points`: a "
            "skill file that cannot be read or has no name or description; an entry point that "
            "is missing, or a pair that differs in bytes; an entry point with no frontmatter, "
            "whose header does not name the skill, does not start with its description or lacks "
            "`disable-model-invocation: true`, whose text lacks the path of its skill, a command "
            "or sentence the invariant requires, or the line of another skill; or a directory "
            "`the-way-*` that no skill produces; write the entry points with `"
            + GENERATOR
            + "`:\n"
            + "\n".join(found),
        )

    def test_problems_reports_a_skill_the_session_does_not_see(self):
        """On a repository with no commit, where every file stands untracked: `alpha` has no
        entry point, `beta` only the `.claude` one, `gamma` two copies that differ in bytes
        alone, `delta` two good copies, `epsilon` two copies whose header lacks the field that hides
        the skill from the model, `zeta` two copies whose list of skills leaves out `alpha`, `eta`
        two copies that say not to call a skill and do not send the session to its file, and
        `the-way-orphan` names no skill."""
        names = ("alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta")

        def skill(name):
            return (
                "---\nname: %s\ndescription: Use when the %s of a product changes.\n---\n\n"
                "# %s\n" % (name, name, name)
            )

        def entry(name, hidden=True, leaving_out=None, reading=True):
            listed = "".join(
                "- `%s`: `%s/skill/SKILL.md`\n" % (each, each)
                for each in names
                if each != leaving_out
            )
            return (
                "---\nname: the-way-%s\ndescription: Use when the %s of a product changes. "
                "Found in the-way.\n%s---\n\n"
                "Read `%s/skill/SKILL.md` in the-way. Find the-way with "
                "`git rev-parse --show-superproject-working-tree`, "
                "`git ls-files --stage -- ':/.the-way'` and `git rev-parse --show-toplevel`. "
                "If the skill tells you to resolve a link to find the-way, skip that.\n\n"
                "Where a skill is named, do not call it%s The skills and their files:\n\n%s"
                % (
                    name,
                    name,
                    "disable-model-invocation: true\n" if hidden else "",
                    name,
                    ": read that skill's `SKILL.md` under the same root." if reading else ".",
                    listed,
                )
            )

        files = {name + "/skill/SKILL.md": skill(name) for name in names}
        files[".claude/skills/the-way-beta/SKILL.md"] = entry("beta")
        files[".claude/skills/the-way-gamma/SKILL.md"] = entry("gamma")
        files[".agents/skills/the-way-gamma/SKILL.md"] = entry("gamma").replace("\n", "\r\n")
        files[".claude/skills/the-way-delta/SKILL.md"] = entry("delta")
        files[".agents/skills/the-way-delta/SKILL.md"] = entry("delta")
        for base in (".claude/skills", ".agents/skills"):
            files[base + "/the-way-epsilon/SKILL.md"] = entry("epsilon", hidden=False)
            files[base + "/the-way-zeta/SKILL.md"] = entry("zeta", leaving_out="alpha")
            files[base + "/the-way-eta/SKILL.md"] = entry("eta", reading=False)
        files[".claude/skills/the-way-orphan/SKILL.md"] = entry("orphan")
        clean = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        with (
            tempfile.TemporaryDirectory() as directory,
            mock.patch.dict(os.environ, clean, clear=True),
        ):
            subprocess.run(["git", "init", "-q"], cwd=directory, check=True, capture_output=True)
            for path, text in files.items():
                full = os.path.join(directory, *path.split("/"))
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "wb") as handle:
                    handle.write(text.encode("utf-8"))
            self.assertEqual(
                discover(directory), sorted(name + "/skill/SKILL.md" for name in names)
            )
            found = problems(directory)
        report = "\n".join(found)
        self.assertIn(
            "alpha/skill/SKILL.md: no file .claude/skills/the-way-alpha/SKILL.md", found, report
        )
        self.assertIn(
            "alpha/skill/SKILL.md: no file .agents/skills/the-way-alpha/SKILL.md", found, report
        )
        self.assertIn(
            "beta/skill/SKILL.md: no file .agents/skills/the-way-beta/SKILL.md", found, report
        )
        self.assertNotIn(
            "beta/skill/SKILL.md: no file .claude/skills/the-way-beta/SKILL.md", found, report
        )
        self.assertIn(
            ".claude/skills/the-way-gamma/SKILL.md and "
            ".agents/skills/the-way-gamma/SKILL.md: not byte-identical",
            found,
            report,
        )
        self.assertIn(
            ".claude/skills/the-way-orphan: no skill of the-way is named orphan", found, report
        )
        self.assertEqual([line for line in found if "delta" in line], [], report)
        self.assertIn(
            ".claude/skills/the-way-epsilon/SKILL.md: its frontmatter does not hold "
            "`disable-model-invocation: true`",
            found,
            report,
        )
        self.assertIn(
            ".claude/skills/the-way-zeta/SKILL.md: no line of its text names `alpha` with "
            "`alpha/skill/SKILL.md` in backticks",
            found,
            report,
        )
        self.assertIn(
            ".claude/skills/the-way-eta/SKILL.md: its text does not contain "
            "read that skill's `SKILL.md`",
            found,
            report,
        )
        self.assertEqual(len(found), 8, report)


if __name__ == "__main__":
    unittest.main()
