"""Tests of the invariant cross-part-imports: a Python file of a part imports only files of its own
part and of the parts its part's *Depends on* names, but for the two exceptions the invariant gives;
running another file as a script counts as importing it.

The check reads with `ast` every Python file git tracks, so that what a string holds — a fixture a
test writes out — is neither an import nor a run. It reads:

- every `import` and `from ... import` statement. A module name resolves to the Python files git
  tracks that it names against the importing file's own directory, the repository's root and each
  directory the file adds to `sys.path`; a relative import, against the file's package. A name of
  the standard library (`sys.stdlib_module_names`) that resolves to no such file is no dependency;
  any other name that resolves to none fails the check, since the import reaches a file the check
  does not see;
- every run of a file as a script: `runpy.run_path(<path>)` and `runpy.run_module(<name>)`, and a
  command line of the running interpreter, `sys.executable`, written out as a list or as the
  arguments of a call, given a script's path or `-m <module>`. A path resolves as an expression of
  the file (below); a path in a directory made at run time by `tempfile` lies outside the
  repository and is no dependency, and so is a path outside the repository's root. Code given with
  `-c` runs no file. A use of `sys.executable` the check cannot read as a command line fails it.

An expression naming a path is worked out from string constants, `__file__`, `os.getcwd()` (the
repository's root, from which the tests and scripts run), `os.path` joins and parents, `Path` and
its `/`, `.parent`, `.resolve()`, `.absolute()` and `.with_name()`, and the names and `self.<name>`
attributes the file assigns, where every plain assignment of the name gives the same value.
Parameters and names bound by unpacking, loops or `with` are not read. A directory added to
`sys.path` or a file run that the check cannot work out fails the check, as does a file that no
part or two parts claim: a check that quietly sees less would pass.

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
# A directory made at run time in the system's temporary directory, outside the repository.
TEMPORARY = "\0temporary"
TEMPORARY_CALLS = ("tempfile.mkdtemp", "tempfile.TemporaryDirectory", "tempfile.gettempdir")
# The functions of `runpy` that run a file, and what their first argument names.
RUNPY = {"run_path": "path", "run_module": "module"}
RUNPY_KEYWORDS = {"path": "path_name", "module": "mod_name"}
INTERPRETER = "sys.executable"
# The options of the interpreter that take the next argument as their value.
VALUED_OPTIONS = ("-W", "-X")


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


def passing(operation, *values):
    """None where a value is unknown, TEMPORARY where one lies in a temporary directory, and
    otherwise what the operation gives."""
    if None in values:
        return None
    if TEMPORARY in values:
        return TEMPORARY
    return operation(*values)


class Resolver:
    """Works out, without running it, the path an expression of one file names."""

    def __init__(self, root, path, tree):
        self.root, self.file = root, os.path.normpath(os.path.join(root, *path.split("/")))
        self.assigned = {}
        self.runpy = {"runpy." + name: kind for name, kind in RUNPY.items()}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    key = self.key(target)
                    if key:
                        self.assigned.setdefault(key, []).append(node.value)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == "runpy" and alias.asname:
                        self.runpy.update({alias.asname + "." + name: kind
                                           for name, kind in RUNPY.items()})
            elif isinstance(node, ast.ImportFrom) and node.module == "runpy" and not node.level:
                for alias in node.names:
                    if alias.name in RUNPY:
                        self.runpy[alias.asname or alias.name] = RUNPY[alias.name]

    @staticmethod
    def key(target):
        """The name a target of a plain assignment binds — `name` or `self.name` — or None."""
        if isinstance(target, ast.Name):
            return target.id
        if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and \
                target.value.id == "self":
            return "self." + target.attr
        return None

    def named(self, key, depth):
        values = {self.value(value, depth + 1) for value in self.assigned.get(key, [])}
        return values.pop() if len(values) == 1 else None

    def value(self, node, depth=0):
        """The path an expression names, TEMPORARY for one in a temporary directory, or None
        where it cannot be worked out."""
        if depth > 20:
            return None
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return self.file if node.id == "__file__" else self.named(node.id, depth)
        if isinstance(node, ast.Attribute):
            key = self.key(node)
            if key:
                return self.named(key, depth)
            inner = self.value(node.value, depth + 1)
            if node.attr == "parent":
                return passing(lambda path: os.path.dirname(self.absolute(path)), inner)
            if node.attr == "name" and inner == TEMPORARY:
                return TEMPORARY
            return None
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            return passing(os.path.join, self.value(node.left, depth + 1),
                           self.value(node.right, depth + 1))
        if not isinstance(node, ast.Call):
            return None
        name = ast.unparse(node.func)
        if name in TEMPORARY_CALLS:
            return TEMPORARY
        if node.keywords:
            return None
        arguments = [self.value(argument, depth + 1) for argument in node.args]
        if name == "os.path.join" and arguments:
            return passing(os.path.join, *arguments)
        if name == "os.path.dirname" and len(arguments) == 1:
            return passing(lambda path: os.path.dirname(self.absolute(path)), *arguments)
        if name in ("os.path.abspath", "os.path.realpath", "os.path.normpath", "str", "Path",
                    "pathlib.Path") and len(arguments) == 1:
            return passing(self.absolute, *arguments)
        if name == "os.getcwd" and not arguments:
            # The tests and the scripts of the-way run from the repository's root.
            return self.root
        if isinstance(node.func, ast.Attribute):
            inner = self.value(node.func.value, depth + 1)
            if node.func.attr in ("resolve", "absolute") and not arguments:
                return passing(self.absolute, inner)
            if node.func.attr == "with_name" and len(arguments) == 1:
                return passing(lambda path, other: os.path.join(
                    os.path.dirname(self.absolute(path)), other), inner, *arguments)
        return None

    def absolute(self, path):
        return path if path == TEMPORARY else os.path.normpath(os.path.join(self.root, path))

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
                elif directory != TEMPORARY:
                    directories.append(self.absolute(directory))
        return directories, unknown

    @staticmethod
    def elements(node):
        """The expressions of a list or tuple written out, or [None] for anything else."""
        if isinstance(node, (ast.List, ast.Tuple)):
            return list(node.elts)
        return [None]

    def runs(self, tree):
        """([(line, "path" or "module", path or module name)] of each file the file runs as a
        script, [(line, why)] of each run it cannot work out)."""
        found, unknown, read_as_command = [], [], set()

        def interpreter(node):
            return isinstance(node, ast.Attribute) and ast.unparse(node) == INTERPRETER

        def command(node):
            if isinstance(node, (ast.List, ast.Tuple)) and node.elts and interpreter(node.elts[0]):
                return node.elts
            return None

        def target(line, kind, node):
            if node is None:
                unknown.append((line, "runs a file the check cannot work out"))
                return
            if kind == "path":
                path = self.value(node)
            else:
                path = node.value if isinstance(node, ast.Constant) and \
                    isinstance(node.value, str) else None
            if path is None:
                unknown.append((line, "runs a file the check cannot work out"))
            else:
                found.append((line, kind, path))

        def command_line(line, elements):
            index = 0
            while index < len(elements):
                element = elements[index]
                if isinstance(element, ast.Starred):
                    unknown.append((line, "runs a command line the check cannot read"))
                    return
                text = element.value if isinstance(element, ast.Constant) and \
                    isinstance(element.value, str) else None
                if text is None or not text.startswith("-"):
                    target(line, "path", element)
                    return
                if text in VALUED_OPTIONS:
                    index += 2
                elif text.startswith("-c") or text == "-":
                    return  # code or standard input, no file
                elif text.startswith("-m"):
                    if len(text) > 2:
                        found.append((line, "module", text[2:]))
                    else:
                        following = elements[index + 1] if index + 1 < len(elements) else None
                        target(line, "module", following)
                    return
                else:
                    index += 1

        for node in ast.walk(tree):
            elements = command(node)
            if elements is not None:
                read_as_command.add(id(elements[0]))
                command_line(node.lineno, elements[1:])
            if not isinstance(node, ast.Call):
                continue
            kind = self.runpy.get(ast.unparse(node.func))
            if kind:
                argument = node.args[0] if node.args else next(
                    (keyword.value for keyword in node.keywords
                     if keyword.arg == RUNPY_KEYWORDS[kind]), None)
                target(node.lineno, kind, argument)
            for position, argument in enumerate(node.args):
                if not interpreter(argument):
                    continue
                read_as_command.add(id(argument))
                rest = node.args[position + 1:]
                if rest and (interpreter(rest[0]) or command(rest[0]) is not None):
                    continue  # os.execl or os.execv: the command line follows
                command_line(node.lineno, rest)
        for node in ast.walk(tree):
            if interpreter(node) and id(node) not in read_as_command:
                unknown.append((node.lineno, "uses sys.executable where the check cannot read "
                                             "what it runs"))
        return found, unknown


def imports(root, path, tracked):
    """([(line, imported or run file)], [problems]) of one Python file."""
    try:
        with open(os.path.join(root, *path.split("/")), encoding="utf-8") as handle:
            tree = ast.parse(handle.read(), path)
    except (OSError, UnicodeDecodeError, SyntaxError) as error:
        return [], ["%s: cannot be read as Python: %s" % (path, error)]
    resolver = Resolver(root, path, tree)
    added, unknown = resolver.added(tree)
    problems = [(line, "adds to sys.path a directory the check cannot work out")
                for line in unknown]
    own = os.path.dirname(resolver.file)
    directories = list(dict.fromkeys([own, os.path.normpath(root)] + added))
    found = []

    def relative(candidate):
        """The path of a file below the root, written with `/`, or None for one outside it."""
        try:
            written = os.path.relpath(candidate, root).replace(os.sep, "/")
        except ValueError:  # another drive
            return None
        return None if written == ".." or written.startswith("../") else written

    def resolve(line, name, bases):
        """Adds each tracked file the module name names below a base; True where one does."""
        before = len(found)
        for base in bases:
            stem = os.path.join(base, *name.split("."))
            for candidate in (stem + ".py", os.path.join(stem, "__init__.py")):
                if relative(candidate) in tracked:
                    found.append((line, relative(candidate)))
        return len(found) > before

    def prefixes(name):
        pieces = name.split(".")
        return [".".join(pieces[:end]) for end in range(1, len(pieces) + 1)]

    def unseen(line, name, standard):
        if not standard or name.split(".")[0] not in sys.stdlib_module_names:
            problems.append((line, "imports `%s`, which is neither a module of the standard "
                                   "library nor a file the check sees" % name))

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                seen = [resolve(node.lineno, name, directories) for name in prefixes(alias.name)]
                if not any(seen):
                    unseen(node.lineno, alias.name, True)
        elif isinstance(node, ast.ImportFrom):
            bases = directories
            if node.level:
                base = own
                for _ in range(node.level - 1):
                    base = os.path.dirname(base)
                bases = [base]
            names = prefixes(node.module) if node.module else []
            seen = [resolve(node.lineno, name, bases) for name in names]
            seen += [resolve(node.lineno, ".".join(names[-1:] + [alias.name]), bases)
                     for alias in node.names if alias.name != "*"]
            if not any(seen):
                written = node.module or ", ".join(alias.name for alias in node.names)
                unseen(node.lineno, "." * node.level + written, not node.level)
    runs, trouble = resolver.runs(tree)
    problems += trouble
    for line, kind, target in runs:
        if kind == "module":
            if not any([resolve(line, name, directories) for name in prefixes(target)]):
                unseen(line, target, True)
        elif target != TEMPORARY:
            written = relative(resolver.absolute(target))
            if written is None:
                continue  # a file outside the repository is no file git tracks
            if written in tracked:
                found.append((line, written))
            elif written + "/__main__.py" in tracked:
                found.append((line, written + "/__main__.py"))
            else:
                problems.append((line, "runs `%s`, which is no Python file git tracks" % written))
    return sorted(set(found)), ["%s:%d: %s" % (path, line, why) for line, why in sorted(problems)]


def check(root, helper_parts):
    """([(file, line, imported or run file, its part, that file's part)] of each import the
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
  app/core/**
- **Depends on:** none
- **Trust boundary:** none

## shell

The part answers for the screens.

- **Files:** shell/**
  app/shell/**
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
# The import of `shell/screen.py` from a file of `core`, which `core`'s *Depends on* forbids.
FORBIDDEN = ("core/engine.py", 7, "shell/screen.py", "core", "shell")


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


class Imports(unittest.TestCase):
    """The check of imports on small repositories, each made to make one import pass or fail."""

    def test_import_from_a_part_depends_on_does_not_name_fails(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\n"
            "import screen\n")})
        self.assertEqual(([FORBIDDEN], []), repository.check())

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
            "core/f.py": "sys.path.extend([os.path.join(HERE, '..', 'shell')])\nimport screen\n",
            "core/g.py": "sys.path = [os.path.join(HERE, '..', 'shell')]\nimport screen\n",
            "core/h.py": "sys.path += [os.path.join(HERE, '..', 'shell')]\nimport screen\n",
        }
        repository = Repository(self, {path: HEADER + text for path, text in forms.items()})
        forbidden, problems = repository.check()
        self.assertEqual([], problems)
        self.assertEqual([("core/a.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/b.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/c.py", 8, "shell/screen.py", "core", "shell"),
                          ("core/d.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/e.py", 8, "shell/screen.py", "core", "shell"),
                          ("core/f.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/g.py", 7, "shell/screen.py", "core", "shell"),
                          ("core/h.py", 7, "shell/screen.py", "core", "shell")], forbidden)

    def test_import_through_the_root_is_seen(self):
        repository = Repository(self, {"core/top.py": "from shell import screen\n"})
        self.assertEqual(([("core/top.py", 1, "shell/screen.py", "core", "shell")], []),
                         repository.check())

    def test_import_through_the_own_directory_is_seen(self):
        # Without its own directory among those searched, `rules` would be a name the check
        # does not see.
        repository = Repository(self, {"core/engine.py": "import rules\n"})
        self.assertEqual(([], []), repository.check())

    def test_package_and_each_prefix_of_a_dotted_name_are_seen(self):
        repository = Repository(self, {"shell/__init__.py": "",
                                       "core/package.py": "import shell\n",
                                       "core/dotted.py": "import shell.screen\n"})
        self.assertEqual(([("core/dotted.py", 1, "shell/__init__.py", "core", "shell"),
                           ("core/dotted.py", 1, "shell/screen.py", "core", "shell"),
                           ("core/package.py", 1, "shell/__init__.py", "core", "shell")], []),
                         repository.check())

    def test_relative_import_resolves_against_the_package(self):
        # From the root, the same names would reach `shell/screen.py`, not `app/shell/screen.py`.
        repository = Repository(self, {"app/shell/screen.py": "VALUE = 4\n",
                                       "app/core/view.py": "from ..shell import screen\n"})
        self.assertEqual(([("app/core/view.py", 1, "app/shell/screen.py", "core", "shell")], []),
                         repository.check())

    def test_import_inside_a_string_is_no_import(self):
        repository = Repository(self, {"core/fixture.py": HEADER + (
            "TEXT = '''\nsys.path.insert(0, os.path.join(HERE, '..', 'shell'))\n"
            "import screen\n'''\n")})
        self.assertEqual(([], []), repository.check())

    def test_standard_library_is_no_dependency(self):
        repository = Repository(self, {"core/engine.py": "import json\nfrom os import path\n"})
        self.assertEqual(([], []), repository.check())

    def test_name_the_check_does_not_see_fails(self):
        # At run time a test of `shell` that puts `core` on sys.path lets `core/lib.py` reach
        # `shell/helper.py`; the check sees no file for `helper` from `core`.
        repository = Repository(self, {
            "shell/helper.py": "VALUE = 5\n",
            "shell/test_lib.py": HEADER + "sys.path.insert(0, os.path.join(HERE, '..', 'core'))\n"
                                          "import lib\n",
            "core/lib.py": "import helper\nfrom . import nothing\n"})
        self.assertEqual(([], ["core/lib.py:1: imports `helper`, which is neither a module of the "
                               "standard library nor a file the check sees",
                               "core/lib.py:2: imports `.nothing`, which is neither a module "
                               "of the "
                               "standard library nor a file the check sees"]),
                         repository.check())

    def test_sys_path_the_check_cannot_work_out_fails(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "sys.path.insert(0, os.environ['SHELL_DIRECTORY'])\nimport screen\n")})
        self.assertEqual(([], ["core/engine.py:6: adds to sys.path a directory the check cannot "
                               "work out",
                               "core/engine.py:7: imports `screen`, which is neither a module of "
                               "the standard library nor a file the check sees"]),
                         repository.check())

    def test_file_no_part_claims_fails(self):
        repository = Repository(self, {"tools/build.py": "import json\n"})
        self.assertEqual(([], ["tools/build.py: claimed by 0 parts"]), repository.check())


class Exceptions(unittest.TestCase):
    """The two exceptions of the invariant, each letting an import pass and no other."""

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
        self.assertEqual(([FORBIDDEN], []), unmarked.check())

    def test_marked_sentence_wrapped_over_lines_is_read(self):
        wrapped = MARKED_TEXT.format(violated="yes").replace(
            "The part `core` does not depend on `shell`.",
            "The part `core` does not depend\non `shell`.")
        repository = Repository(self, {
            "core/engine.py": HEADER + (
                "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\nimport screen\n"),
            "foundations/invariants.md": wrapped})
        self.assertEqual(([], []), repository.check())

    def test_marked_invariant_of_the_other_direction_lets_no_import_pass(self):
        reversed_text = MARKED_TEXT.format(violated="yes").replace(
            "The part `core` does not depend on `shell`.",
            "The part `shell` does not depend on `core`.")
        repository = Repository(self, {
            "core/engine.py": HEADER + (
                "sys.path.insert(0, os.path.join(HERE, '..', 'shell'))\nimport screen\n"),
            "foundations/invariants.md": reversed_text})
        self.assertEqual(([FORBIDDEN], []), repository.check())

    def test_run_a_marked_invariant_names_passes(self):
        repository = Repository(self, {
            "core/engine.py": HEADER + "import runpy\n"
                                       "runpy.run_path(os.path.join(HERE, '..', 'shell', "
                                       "'screen.py'))\n",
            "foundations/invariants.md": MARKED_TEXT.format(violated="yes")})
        self.assertEqual(([], []), repository.check())


class Runs(unittest.TestCase):
    """The check of files run as scripts, each form on a small repository of its own."""

    def run_from_core(self, line):
        """The check of a repository whose `core/engine.py` holds HEADER, the imports a run
        needs on line 6 and the line given on line 7."""
        return Repository(self, {"core/engine.py": HEADER + "import runpy, subprocess\n" +
                                 line + "\n"}).check()

    def test_each_form_of_a_run_is_seen(self):
        screen = "os.path.join(HERE, '..', 'shell', 'screen.py')"
        for line in (
                "runpy.run_path(%s)" % screen,
                "runpy.run_path(path_name=%s, run_name='__main__')" % screen,
                "runpy.run_module('shell.screen')",
                "subprocess.run([sys.executable, '-B', %s])" % screen,
                "subprocess.Popen([sys.executable, '-X', 'utf8', %s, '--apply'])" % screen,
                "subprocess.run([sys.executable, '-m', 'shell.screen'])",
                "subprocess.run([sys.executable, '-mshell.screen'])",
                "subprocess.run([sys.executable, '-B', %s] + list(sys.argv))" % screen,
                "command(sys.executable, '-B', %s, cwd=HERE)" % screen,
                "os.execv(sys.executable, [sys.executable, %s])" % screen,
                "os.execl(sys.executable, sys.executable, %s)" % screen,
                "subprocess.run([sys.executable, str((Path(__file__).resolve().parent.parent"
                " / 'shell' / 'other.py').with_name('screen.py'))])",
        ):
            with self.subTest(line=line):
                self.assertEqual(([FORBIDDEN], []), self.run_from_core(line))

    def test_run_through_from_runpy_import_is_seen(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "from runpy import run_path as run\n"
            "run(os.path.join(HERE, '..', 'shell', 'screen.py'))\n")})
        self.assertEqual(([FORBIDDEN], []), repository.check())

    def test_run_of_a_directory_runs_its_main(self):
        repository = Repository(self, {
            "shell/__main__.py": "VALUE = 6\n",
            "core/engine.py": HEADER + "import runpy\n"
                                       "runpy.run_path(os.path.join(HERE, '..', 'shell'))\n"})
        self.assertEqual(([("core/engine.py", 7, "shell/__main__.py", "core", "shell")], []),
                         repository.check())

    def test_run_through_names_the_file_assigns_is_seen(self):
        repository = Repository(self, {"core/engine.py": HEADER + (
            "import subprocess\n"
            "class Case:\n"
            "    def setUp(self):\n"
            "        self.script = os.path.join(HERE, '..', 'shell', 'screen.py')\n"
            "    def first(self):\n"
            "        script = str(self.script)\n"
            "        subprocess.run([sys.executable, script])\n"
            "    def second(self):\n"
            "        script = str(self.script)\n"
            "        subprocess.run([sys.executable, script])\n")})
        self.assertEqual(([("core/engine.py", 12, "shell/screen.py", "core", "shell"),
                           ("core/engine.py", 15, "shell/screen.py", "core", "shell")], []),
                         repository.check())

    def test_run_from_a_part_depends_on_names_passes(self):
        repository = Repository(self, {"shell/app.py": HEADER + (
            "import runpy\nrunpy.run_path(os.path.join(HERE, '..', 'core', 'rules.py'))\n")})
        self.assertEqual(([], []), repository.check())

    def test_code_and_standard_modules_run_no_file_of_a_part(self):
        for line in ("subprocess.run([sys.executable, '-c', 'import shell.screen'])",
                     "subprocess.run([sys.executable, '-m', 'unittest'])",
                     "subprocess.run([sys.executable])",
                     "runpy.run_module('json.tool')"):
            with self.subTest(line=line):
                self.assertEqual(([], []), self.run_from_core(line))

    def test_run_of_a_file_in_a_temporary_directory_is_no_dependency(self):
        for line in ("subprocess.run([sys.executable, os.path.join(tempfile.mkdtemp(), "
                     "'shell', 'screen.py')])",
                     "subprocess.run([sys.executable, str(Path(tempfile.TemporaryDirectory()"
                     ".name) / 'screen.py')])"):
            with self.subTest(line=line):
                self.assertEqual(([], []), self.run_from_core(line))

    def test_run_inside_a_string_is_no_run(self):
        self.assertEqual(([], []), self.run_from_core(
            "TEXT = \"runpy.run_path(os.path.join(HERE, '..', 'shell', 'screen.py'))\""))

    def test_run_the_check_cannot_work_out_fails(self):
        for line, why in (
                ("runpy.run_path(os.environ['SCRIPT'])", "runs a file the check cannot work out"),
                ("subprocess.run([sys.executable, os.environ['SCRIPT']])",
                 "runs a file the check cannot work out"),
                ("subprocess.run([sys.executable, *sys.argv])",
                 "runs a command line the check cannot read"),
                ("runpy.run_module(sys.argv[1])", "runs a file the check cannot work out"),
                ("python = sys.executable", "uses sys.executable where the check cannot read what "
                                            "it runs"),
                ("subprocess.run([sys.executable, 'shell/missing.py'])",
                 "runs `shell/missing.py`, which is no Python file git tracks"),
                ("runpy.run_module('missing')", "imports `missing`, which is neither a module of "
                                                "the standard library nor a file the check sees")):
            with self.subTest(line=line):
                self.assertEqual(([], ["core/engine.py:7: " + why]), self.run_from_core(line))


if __name__ == "__main__":
    unittest.main()
