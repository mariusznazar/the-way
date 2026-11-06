"""Tests of the invariant cross-part-imports: a Python file of a part imports only files of its own
part and of the parts its part's *Depends on* names, but for the two exceptions the invariant gives.

The check reads, with `ast`, every `import` and `from ... import` statement of every Python file
git tracks, so that an import written inside a string — a fixture a test writes out — is no
import. A module name resolves to the Python files git tracks that it names against the importing
file's own directory, the repository's root and each directory the file adds to `sys.path`; a name
that resolves to no such file, a module of the standard library among them, is no dependency.
Running another file as a script or in a process of its own is no import. A directory added to
`sys.path` by an expression the check cannot work out fails the check, as does a file that no part
or two parts claim: a check that quietly sees less would pass.

A file belongs to the part whose *Files* claims it, by patterns git matches (WAY-44). A test is a
file named `test_*.py`, the files the gate runs. The parts of test helpers are named by identifier
in `TEST_HELPER_PARTS`; the-way has none. An import from a file of part X to a file of part Y also
passes where `foundations/invariants.md` holds an invariant "the part `X` does not depend on `Y`"
that reads `Violated: yes`.

Run from the root of the-way: python -B gate/run_tests.py elements/part-map
"""

import ast
import os
import re
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
THE_WAY = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(HERE, "..", "common"))

from foundation_check import (EMPTY, ENTRY, INVARIANTS, PART_MAP, WORDS, blocks,  # noqa: E402
                              fields, git, items, read)

# The parts of the-way's map that hold the files serving the tests of several parts.
TEST_HELPER_PARTS = ()

MARKED = re.compile(r"^[Tt]he part `(%s)` does not depend on `(%s)`\.?$" % (WORDS, WORDS))
# The calls on `sys.path` that add a directory, and the position of the argument naming it.
ADDING = {"insert": 1, "append": 0}


def parts(root, tracked):
    """({path: part} of every tracked file one part claims, {part: allowed parts}, [problems]),
    the files matched to the patterns of *Files* by git."""
    wanted, owner, allowed = [], {}, {}
    for _, heading, body in blocks(read(root, PART_MAP), "## "):
        match = ENTRY.match(heading)
        found = fields(body)
        if not match or "Files" not in found:
            continue
        name = match.group(1)
        allowed[name] = {part for part in items(found.get("Depends on", ("", []))[0])
                         if part not in EMPTY}
        for text in found["Files"][0].split("\n"):
            pattern = re.sub(r"\(generated\)", "", text.strip().removeprefix("- ")).strip()
            if pattern and pattern not in EMPTY:
                attribute = "the-way-part-%d" % len(wanted)
                wanted.append("%s %s\n" % (pattern, attribute))
                owner[attribute] = name
    handle, attributes = tempfile.mkstemp(suffix=".attributes", text=True)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write("".join(wanted))
        code, answer = git(root, "-c", "core.attributesFile=" + attributes.replace(os.sep, "/"),
                           "-c", "core.ignorecase=false", "check-attr", "--all", "-z", "--stdin",
                           stdin="".join(path + "\0" for path in tracked))
    finally:
        os.unlink(attributes)
    if code != 0:
        raise RuntimeError("git cannot match the patterns of the part map in %s" % root)
    claims = {}
    pieces = answer.split("\0")
    for index in range(0, len(pieces) - 2, 3):
        path, attribute, value = pieces[index:index + 3]
        if attribute in owner and value == "set":
            claims.setdefault(path, set()).add(owner[attribute])
    assigned, problems = {}, []
    for path in tracked:
        claimed = claims.get(path, set())
        if len(claimed) == 1:
            assigned[path] = next(iter(claimed))
        elif path.endswith(".py"):
            problems.append("%s: claimed by %d parts" % (path, len(claimed)))
    return assigned, allowed, problems


def marked_dependencies(root):
    """The pairs (X, Y) of each invariant "the part `X` does not depend on `Y`" that reads
    `Violated: yes`."""
    pairs = set()
    for _, heading, body in blocks(read(root, INVARIANTS), "## "):
        if not ENTRY.match(heading):
            continue
        sentence = []
        for _, line in body:
            if line.startswith("- **"):
                break
            if line.strip():
                sentence.append(line.strip())
        match = MARKED.match(" ".join(sentence))
        if match and fields(body).get("Violated", ("",))[0] == "yes":
            pairs.add((match.group(1), match.group(2)))
    return pairs


class Resolver:
    """Works out, without running it, the directory an expression of one file names."""

    def __init__(self, root, path, tree):
        self.root, self.file = root, os.path.normpath(os.path.join(root, *path.split("/")))
        self.assigned = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.assigned.setdefault(target.id, []).append(node.value)

    def value(self, node, depth=0):
        """The path an expression names, or None where it cannot be worked out."""
        if depth > 20:
            return None
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            if node.id == "__file__":
                return self.file
            values = self.assigned.get(node.id, [])
            return self.value(values[0], depth + 1) if len(values) == 1 else None
        if isinstance(node, ast.Attribute) and node.attr == "parent":
            inner = self.value(node.value, depth + 1)
            return None if inner is None else os.path.dirname(self.absolute(inner))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            left, right = self.value(node.left, depth + 1), self.value(node.right, depth + 1)
            return None if left is None or right is None else os.path.join(left, right)
        if isinstance(node, ast.Call) and not node.keywords:
            name = ast.unparse(node.func)
            arguments = [self.value(argument, depth + 1) for argument in node.args]
            if None in arguments:
                return None
            if name == "os.path.join" and arguments:
                return os.path.join(*arguments)
            if name == "os.path.dirname" and len(arguments) == 1:
                return os.path.dirname(self.absolute(arguments[0]))
            if name in ("os.path.abspath", "os.path.realpath", "os.path.normpath", "str", "Path",
                        "pathlib.Path") and len(arguments) == 1:
                return self.absolute(arguments[0])
            if name == "os.getcwd" and not arguments:
                # The tests and the scripts of the-way run from the repository's root.
                return self.root
            if isinstance(node.func, ast.Attribute) and node.func.attr in ("resolve", "absolute") \
                    and not arguments:
                inner = self.value(node.func.value, depth + 1)
                return None if inner is None else self.absolute(inner)
        return None

    def absolute(self, path):
        return os.path.normpath(os.path.join(self.root, path))

    def added(self, tree):
        """([directory], [line of each addition it cannot work out]) the file adds to
        `sys.path`."""
        directories, unknown = [], []
        for node in ast.walk(tree):
            named = []
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and \
                    ast.unparse(node.func.value) == "sys.path":
                if node.func.attr in ADDING:
                    position = ADDING[node.func.attr]
                    named = [node.args[position] if len(node.args) > position else None]
                elif node.func.attr == "extend":
                    named = self.elements(node.args[0] if node.args else None)
            elif isinstance(node, (ast.Assign, ast.AugAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target in targets:
                    if isinstance(target, ast.Subscript) and \
                            ast.unparse(target.value) == "sys.path":
                        named += [node.value] if isinstance(target.slice, ast.Constant) \
                            else self.elements(node.value)
                    elif ast.unparse(target) == "sys.path":
                        named += self.elements(node.value)
            for expression in named:
                directory = None if expression is None else self.value(expression)
                if directory is None:
                    unknown.append(node.lineno)
                else:
                    directories.append(self.absolute(directory))
        return directories, unknown

    @staticmethod
    def elements(node):
        """The expressions of a list or tuple written out, or [None] for anything else."""
        if isinstance(node, (ast.List, ast.Tuple)):
            return list(node.elts)
        return [None]


def imports(root, path, tracked):
    """([(line, imported file)], [problems]) of one Python file."""
    try:
        with open(os.path.join(root, *path.split("/")), encoding="utf-8") as handle:
            tree = ast.parse(handle.read(), path)
    except (OSError, UnicodeDecodeError, SyntaxError) as error:
        return [], ["%s: cannot be read as Python: %s" % (path, error)]
    resolver = Resolver(root, path, tree)
    added, unknown = resolver.added(tree)
    problems = ["%s:%d: adds to sys.path a directory the check cannot work out" % (path, line)
                for line in unknown]
    own = os.path.dirname(resolver.file)
    directories = list(dict.fromkeys([own, os.path.normpath(root)] + added))
    found = []

    def resolve(line, name, bases):
        for base in bases:
            stem = os.path.join(base, *name.split("."))
            for candidate in (stem + ".py", os.path.join(stem, "__init__.py")):
                try:
                    relative = os.path.relpath(candidate, root).replace(os.sep, "/")
                except ValueError:  # a directory on another drive holds no file git tracks
                    continue
                if relative in tracked:
                    found.append((line, relative))

    def prefixes(name):
        pieces = name.split(".")
        return [".".join(pieces[:end]) for end in range(1, len(pieces) + 1)]

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                for name in prefixes(alias.name):
                    resolve(node.lineno, name, directories)
        elif isinstance(node, ast.ImportFrom):
            bases = directories
            if node.level:
                base = own
                for _ in range(node.level - 1):
                    base = os.path.dirname(base)
                bases = [base]
            names = prefixes(node.module) if node.module else []
            for name in names:
                resolve(node.lineno, name, bases)
            for alias in node.names:
                if alias.name != "*":
                    resolve(node.lineno, ".".join(names[-1:] + [alias.name]), bases)
    return sorted(set(found)), problems


def check(root, helper_parts):
    """([(file, line, imported file, its part, the imported file's part)] of each import the
    invariant forbids, [problems]) of the repository at `root`."""
    code, listing = git(root, "ls-files", "-z")
    if code != 0:
        raise RuntimeError("git cannot list the files of %s" % root)
    tracked = [path for path in listing.split("\0") if path]
    assigned, allowed, problems = parts(root, tracked)
    marked = marked_dependencies(root)
    known = set(tracked)
    forbidden = []
    for path in tracked:
        if not path.endswith(".py") or path not in assigned:
            continue
        test = path.rpartition("/")[2].startswith("test_")
        found, trouble = imports(root, path, known)
        problems += trouble
        for line, imported in found:
            part, other = assigned[path], assigned.get(imported)
            if other is None:
                continue  # reported among the problems of `parts`
            if other == part or other in allowed.get(part, set()) or \
                    (test and other in helper_parts) or (part, other) in marked:
                continue
            forbidden.append((path, line, imported, part, other))
    return forbidden, problems


# --- small repositories made for the tests ---------------------------------------------------

PART_MAP_TEXT = """# Part map

## core

The part answers for the rules.

- **Files:** core/**
- **Depends on:** none
- **Trust boundary:** none

## shell

The part answers for the screens.

- **Files:** shell/**
- **Depends on:** core
- **Trust boundary:** none

## support

The part holds the files that serve the tests of several parts.

- **Files:** support/**
- **Depends on:** none
- **Trust boundary:** none

## repository

The part answers for the foundation.

- **Files:** foundations/**
- **Depends on:** none
- **Trust boundary:** none
"""

MARKED_TEXT = """# Invariants

## core-shell-dependency

The part `core` does not depend on `shell`.

- **Method:** test
- **Rests on:** none
- **Derives from:** none
- **Part:** core
- **Violated:** {violated}
"""

# Five lines, so that the first line a test adds after it is line 6.
HEADER = ("import os\nimport sys\nfrom pathlib import Path\n\n"
          "HERE = os.path.dirname(os.path.abspath(__file__))\n")


class Repository:
    """A repository in a temporary directory, its files added to git's index."""

    def __init__(self, test, files):
        directory = tempfile.TemporaryDirectory()
        test.addCleanup(directory.cleanup)
        self.root = directory.name
        files = dict({"foundations/part_map.md": PART_MAP_TEXT,
                      "core/rules.py": "VALUE = 1\n",
                      "shell/screen.py": "VALUE = 2\n",
                      "support/fixtures.py": "VALUE = 3\n"}, **files)
        for path, text in files.items():
            full = os.path.join(self.root, *path.split("/"))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True, capture_output=True)
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True, capture_output=True)

    def check(self, helper_parts=()):
        return check(self.root, helper_parts)


class TheWay(unittest.TestCase):

    def test_the_way_imports_only_from_allowed_parts(self):
        # invariant: cross-part-imports
        forbidden, problems = check(THE_WAY, TEST_HELPER_PARTS)
        self.assertEqual([], problems)
        self.assertEqual([], forbidden)


class Check(unittest.TestCase):
    """The check on small repositories, each made to make one import pass or fail."""

    def test_import_from_a_part_depends_on_does_not_name_fails(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\n"
            "import screen\n")})
        self.assertEqual(([("core/engine.py", 7, "shell/screen.py", "core", "shell")], []),
                         repository.check())

    def test_import_from_a_part_depends_on_names_passes(self):
        repository = Repository(self, {"shell/app.py": HEADER + (
            "sys.path.insert(0, os.path.join(HERE, '..', 'core'))\n"
            "import rules\n")})
        self.assertEqual(([], []), repository.check())

    def test_import_through_each_form_of_sys_path_is_seen(self):
        forms = {
            "core/a.py": "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\nimport screen\n",
            "core/b.py": "sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'shell'))"
                         "\nimport screen\n",
            "core/c.py": "SOURCE = Path(__file__).resolve().parent.parent\n"
                         "sys.path.insert(0, str(SOURCE / 'shell'))\nimport screen\n",
            "core/d.py": "sys.path.append(os.path.join(os.path.dirname(HERE), 'shell'))\n"
                         "import screen\n",
            "core/e.py": "def main():\n    sys.path[0] = os.getcwd()\n    import shell.screen\n",
        }
        repository = Repository(self, {path: HEADER + text for path, text in forms.items()})
        forbidden, problems = repository.check()
        self.assertEqual([], problems)
        self.assertEqual([("core/a.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/b.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/c.py", 8, "shell/screen.py", "core", "shell"),
                          ("core/d.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/e.py", 8, "shell/screen.py", "core", "shell")], forbidden)

    def test_import_through_the_root_is_seen(self):
        repository = Repository(self, {"core/top.py": "from shell import screen\n"})
        self.assertEqual(([("core/top.py", 1, "shell/screen.py", "core", "shell")], []),
                         repository.check())

    def test_import_inside_a_string_is_no_import(self):
        repository = Repository(self, {"core/fixture.py": HEADER + (
            "TEXT = '''\nsys.path.insert(0, os.path.join(HERE, '..', 'shell'))\n"
            "import screen\n'''\n")})
        self.assertEqual(([], []), repository.check())

    def test_standard_library_is_no_dependency(self):
        repository = Repository(self, {"core/engine.py": "import json\nfrom os import path\n"})
        self.assertEqual(([], []), repository.check())

    def test_sys_path_the_check_cannot_work_out_fails(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "sys.path.insert(0, os.environ['SHELL_DIRECTORY'])\nimport screen\n")})
        self.assertEqual(([], ["core/engine.py:6: adds to sys.path a directory the check cannot "
                               "work out"]), repository.check())

    def test_file_no_part_claims_fails(self):
        repository = Repository(self, {"tools/build.py": "import json\n"})
        self.assertEqual(([], ["tools/build.py: claimed by 0 parts"]), repository.check())

    def test_test_importing_a_part_of_test_helpers_passes(self):
        repository = Repository(self, {"core/test_rules.py": HEADER + (
            "sys.path.insert(0, os.path.join(HERE, '..', 'support'))\n"
            "import fixtures\n")})
        self.assertEqual(([], []), repository.check(helper_parts=("support",)))
        self.assertEqual(([("core/test_rules.py", 7, "support/fixtures.py", "core", "support")],
                          []), repository.check())

    def test_code_that_is_no_test_importing_a_part_of_test_helpers_fails(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "sys.path.insert(0, os.path.join(HERE, '..', 'support'))\n"
            "import fixtures\n")})
        self.assertEqual(([("core/engine.py", 7, "support/fixtures.py", "core", "support")], []),
                         repository.check(helper_parts=("support",)))

    def test_import_a_marked_invariant_names_passes(self):
        engine = HEADER + "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\nimport screen\n"
        marked = Repository(self, {"core/engine.py": engine,
                                   "foundations/invariants.md": MARKED_TEXT.format(violated="yes")})
        self.assertEqual(([], []), marked.check())
        unmarked = Repository(self, {
            "core/engine.py": engine,
            "foundations/invariants.md": MARKED_TEXT.format(violated="no")})
        self.assertEqual(([("core/engine.py", 7, "shell/screen.py", "core", "shell")], []),
                         unmarked.check())

    def test_marked_invariant_of_the_other_direction_lets_no_import_pass(self):
        reversed_text = MARKED_TEXT.format(violated="yes").replace(
            "The part `core` does not depend on `shell`.",
            "The part `shell` does not depend on `core`.")
        repository = Repository(self, {
            "core/engine.py": HEADER + (
                "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\nimport screen\n"),
            "foundations/invariants.md": reversed_text})
        self.assertEqual(([("core/engine.py", 7, "shell/screen.py", "core", "shell")], []),
                         repository.check())


if __name__ == "__main__":
    unittest.main()
