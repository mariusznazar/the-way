"""Tests of the invariant cross-part-imports: a Python file of a part imports only files of its own
part and of the parts its part's *Depends on* names, but for the two exceptions the invariant gives;
running another file as a script counts as importing it.

The check reads with `ast` every Python file git tracks, so that what a string holds — a fixture a
test writes out — is neither an import nor a run, unless the file runs it as code. It reads:

- every `import` and `from ... import` statement, and every call of `importlib.import_module`
  and `__import__` with a name the check can work out. A module name resolves to the Python files
  git tracks that it names against the importing file's own directory, the repository's root and
  each directory the file adds to `sys.path`; a relative import, against the file's package. A
  name of the standard library (`sys.stdlib_module_names`) that resolves to no such file is no
  dependency; any other name that resolves to none fails the check, since the import reaches a
  file the check does not see;
- every run of a file as a script: `runpy.run_path(<path>)` and `runpy.run_module(<name>)`; a
  command line of the running interpreter, `sys.executable`, written out as a list, a list joined
  with `+` to more elements, or the arguments of a call, given a script's path, `-m <module>` or
  `-c <code>`; and `exec`, `eval` and `compile` given the text of a file, read with
  `open(<path>).read()` or `<path>.read_text()`. A path resolves as an expression of the file
  (below); a path in a directory made at run time by `tempfile` lies outside the repository and is
  no dependency, and so is a path outside the repository's root;
- code given as a string — to `-c`, or to `exec`, `eval` or `compile` — parsed as the code of a
  file and read as above: code given to `-c` from the repository's root, the working directory of
  the gate and the scripts, with `sys.argv` taken from the command line; code given to `exec`,
  `eval` or `compile` from the directories of the file that runs it.

A use of `sys.executable` the check cannot read as a command line fails it, and so does a command
line whose script, code or module is not written out where the check reads it — joined on later,
by `+` of what is no list, or given on standard input — and code, a module name or a file to run
that the check cannot work out.

An expression naming a path is worked out from string constants, `__file__`, `os.getcwd()` (the
repository's root, from which the tests and scripts run), `os.path` joins and parents, `Path` and
its `/`, `.parent`, `.resolve()`, `.absolute()` and `.with_name()`, and the names and `self.<name>`
attributes the file assigns, where every plain assignment of the name gives the same value; in
code given to `-c`, also the names it assigns from `sys.argv`. Parameters and names bound by
unpacking, loops or `with` are not read. A directory added to `sys.path` or a file run that the
check cannot work out fails the check, as does a Python file that no part or two parts claim and
the map does not leave out on purpose: a check that quietly sees less would pass.

A file belongs to the part whose *Files* claims it, by patterns git matches (WAY-44); a file the
map lists under "Files left out on purpose" belongs to none, and its imports cross no boundary the
map draws. A test is a file named `test_*.py`, the files the gate runs. The parts of test helpers
are named by identifier in `TEST_HELPER_PARTS`; the-way has none. An import from a file of part X
to a file of part Y also passes where `foundations/invariants.md` holds an invariant "the part `X`
does not depend on `Y`" that reads `Violated: yes`.

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

from foundation_check import (EMPTY, ENTRY, INVARIANTS, LEFT_OUT, PART_MAP,  # noqa: E402
                              WORDS, blocks, fields, git, items, read, table)

# The parts of the-way's map that hold the files serving the tests of several parts.
TEST_HELPER_PARTS = ()

MARKED = re.compile(r"^[Tt]he part `(%s)` does not depend on `(%s)`\.?$" % (WORDS, WORDS))
# The calls on `sys.path` that add a directory, and the position of the argument naming it.
ADDING = {"insert": 1, "append": 0}
# A directory made at run time in the system's temporary directory, outside the repository: no
# path, so that a step taking it for one fails.
TEMPORARY = type("Temporary", (), {"__repr__": lambda self: "TEMPORARY"})()
TEMPORARY_CALLS = ("tempfile.mkdtemp", "tempfile.TemporaryDirectory", "tempfile.gettempdir")
# The functions that import a module or run a file or code, by the modules that hold them, and
# the keyword that may give their first argument.
FUNCTIONS = {"runpy": ("run_path", "run_module"), "importlib": ("import_module", "__import__"),
             "builtins": ("exec", "eval", "compile", "__import__")}
BUILTINS = ("exec", "eval", "compile", "__import__")
KEYWORDS = {"run_path": "path_name", "run_module": "mod_name", "import_module": "name",
            "__import__": "name", "compile": "source"}
INTERPRETER = "sys.executable"
# The options of the interpreter that take the next argument as their value.
VALUED_OPTIONS = ("-W", "-X")
# How deep code given as a string may hold code given as a string.
NESTING = 5


def parts(root, tracked):
    """({path: part} of every tracked file one part claims, {part: allowed parts}, [problems]),
    the files matched to the patterns of *Files* by git, as `foundation_check.check_files`
    matches them, and the files the map leaves out on purpose left out."""
    lines = read(root, PART_MAP)
    wanted, owner, allowed = [], {}, {}
    for _, heading, body in blocks(lines, "## "):
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
    left_out = {cells[0] for _, cells in table(lines, LEFT_OUT)[1:]}
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
        if path in left_out and not claimed:
            continue
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
    if any(value is None for value in values):
        return None
    if any(value is TEMPORARY for value in values):
        return TEMPORARY
    return operation(*values)


class Resolver:
    """Works out, without running it, the path or text an expression of one file or of code given
    as a string names.

    `file` is the file's path, or None for code given to `-c`; `argv` is, for such code, the
    values of its command line from `-c` on, None standing for one the check cannot work out."""

    def __init__(self, root, file, tree, argv=None):
        self.root, self.file = root, file
        self.assigned, self.known = {}, {}
        self.functions = {name: name for name in BUILTINS}
        for module, names in FUNCTIONS.items():
            self.functions.update({"%s.%s" % (module, name): name for name in names})
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    key = self.key(target)
                    if key:
                        self.assigned.setdefault(key, []).append(node.value)
                    if argv is not None:
                        self.from_argv(target, node.value, argv)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in FUNCTIONS and alias.asname:
                        self.functions.update({"%s.%s" % (alias.asname, name): name
                                               for name in FUNCTIONS[alias.name]})
            elif isinstance(node, ast.ImportFrom) and node.module in FUNCTIONS and not node.level:
                for alias in node.names:
                    if alias.name in FUNCTIONS[node.module]:
                        self.functions[alias.asname or alias.name] = alias.name

    def from_argv(self, target, value, argv):
        """Records the names code given to `-c` assigns from `sys.argv[<i>]` or
        `sys.argv[<i>:]`."""
        if not (isinstance(value, ast.Subscript) and ast.unparse(value.value) == "sys.argv"):
            return
        index = value.slice
        if isinstance(index, ast.Constant) and isinstance(index.value, int) and \
                isinstance(target, ast.Name):
            self.known[target.id] = argv[index.value] if 0 <= index.value < len(argv) else None
        elif isinstance(index, ast.Slice) and index.upper is None and index.step is None and \
                isinstance(target, (ast.Tuple, ast.List)):
            start = index.lower.value if isinstance(index.lower, ast.Constant) else 0 \
                if index.lower is None else None
            if isinstance(start, int):
                for offset, element in enumerate(target.elts):
                    if isinstance(element, ast.Name):
                        position = start + offset
                        self.known[element.id] = argv[position] if position < len(argv) else None

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
        if key in self.known:
            return self.known[key]
        values = [self.value(value, depth + 1) for value in self.assigned.get(key, [])]
        if not values or any(value is None for value in values):
            return None
        first = values[0]
        return first if all(value is first or value == first for value in values) else None

    def follow(self, node):
        """The expression a name stands for, where every plain assignment of it is the same
        expression; the node itself where it is no name."""
        for _ in range(20):
            key = self.key(node) if isinstance(node, (ast.Name, ast.Attribute)) else None
            if not key or key in self.known:
                return node
            values = self.assigned.get(key, [])
            if not values or len({ast.dump(value) for value in values}) != 1:
                return None
            node = values[0]
        return None

    def value(self, node, depth=0):
        """The path or text an expression names, TEMPORARY for a path in a temporary directory, or
        None where it cannot be worked out."""
        if depth > 20 or node is None:
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
            if node.attr == "name" and inner is TEMPORARY:
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

    def text(self, node):
        """The string an expression names — a module name, code — or None."""
        value = self.value(node)
        return value if isinstance(value, str) else None

    def absolute(self, path):
        if path is TEMPORARY:
            return path
        return os.path.normpath(os.path.join(self.root, path))

    def added(self, tree):
        """([directory], [line of each addition it cannot work out]) the code adds to
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
                elif directory is not TEMPORARY:
                    directories.append(self.absolute(directory))
        return directories, unknown

    @staticmethod
    def elements(node):
        """The expressions of a list or tuple written out, or [None] for anything else."""
        if isinstance(node, (ast.List, ast.Tuple)):
            return list(node.elts)
        return [None]

    @staticmethod
    def argument(node, position, keyword):
        if len(node.args) > position:
            return node.args[position]
        return next((given.value for given in node.keywords if given.arg == keyword), None)

    def runs(self, tree):
        """([(line, kind, what)] of each file, module or code the code imports by a function or
        runs — kind "path" with a path, "module" with a module name, "code" with (text, argv,
        mode) — and [(line, why)] of each it cannot work out)."""
        found, unknown, read_as_command, joined = [], [], set(), set()

        def interpreter(node):
            return isinstance(node, ast.Attribute) and ast.unparse(node) == INTERPRETER

        def command(node):
            """The elements of a command line of the interpreter written out — a list, or a list
            joined with `+` to more elements, None standing for those not written out — or None
            where the node holds none."""
            if isinstance(node, (ast.List, ast.Tuple)) and node.elts and interpreter(node.elts[0]):
                return list(node.elts)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                left = command(node.left)
                if left is not None:
                    right = node.right
                    return left + (list(right.elts) if isinstance(right, (ast.List, ast.Tuple))
                                   else [None])
            return None

        def target(line, kind, node):
            what = self.value(node) if kind == "path" else self.text(node)
            if what is None:
                unknown.append((line, "runs a file the check cannot work out"))
            else:
                found.append((line, kind, what))

        def module(line, call, function):
            """An import by `importlib.import_module` or `__import__`."""
            name = self.text(self.argument(call, 0, KEYWORDS[function]))
            if function == "import_module":
                package = self.argument(call, 1, "package")
                if name and name.startswith("."):
                    base = self.text(package) if package is not None else None
                    level = len(name) - len(name.lstrip("."))
                    pieces = base.split(".") if base else []
                    name = ".".join(pieces[:len(pieces) - level + 1] + [name.lstrip(".")]) \
                        if base and level <= len(pieces) else None
            else:
                level = self.argument(call, 4, "level")
                if level is not None and not (isinstance(level, ast.Constant) and
                                              level.value == 0):
                    name = None
            if name is None:
                unknown.append((line, "imports a module the check cannot work out"))
            else:
                found.append((line, "module", name))

        def source(line, node, mode):
            """Code given to `exec`, `eval` or `compile`."""
            node = self.follow(node)
            if isinstance(node, ast.Call) and self.functions.get(ast.unparse(node.func)) == \
                    "compile":
                return  # read at the call of `compile`
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                opened = node.func.value
                if node.func.attr == "read" and isinstance(opened, ast.Call) and \
                        ast.unparse(opened.func) in ("open", "io.open") and opened.args:
                    target(line, "path", opened.args[0])
                    return
                if node.func.attr in ("read_text", "read_bytes") and not node.args:
                    target(line, "path", opened)
                    return
            text = node.value if isinstance(node, ast.Constant) else None
            if isinstance(text, bytes):
                text = text.decode("utf-8", "replace")
            if isinstance(text, str):
                found.append((line, "code", (text, None, mode)))
            else:
                unknown.append((line, "runs code the check cannot read"))

        def command_line(line, elements):
            index = 0
            while index < len(elements):
                element = elements[index]
                if element is None or isinstance(element, ast.Starred):
                    unknown.append((line, "runs a command line the check cannot read"))
                    return
                text = element.value if isinstance(element, ast.Constant) and \
                    isinstance(element.value, str) else None
                if text is None or not text.startswith("-"):
                    target(line, "path", element)
                    return
                if text in VALUED_OPTIONS:
                    index += 2
                elif text.startswith("-c"):
                    given = elements[index + 1] if len(text) == 2 and index + 1 < len(elements) \
                        else None
                    code = text[2:] if len(text) > 2 else self.text(given)
                    rest = elements[index + (1 if len(text) > 2 else 2):]
                    if code is None:
                        unknown.append((line, "runs code the check cannot read"))
                    else:
                        argv = ["-c"] + [None if part is None or isinstance(part, ast.Starred)
                                         else self.value(part) for part in rest]
                        found.append((line, "code", (code, argv, "exec")))
                    return
                elif text.startswith("-m"):
                    if len(text) > 2:
                        found.append((line, "module", text[2:]))
                    else:
                        following = elements[index + 1] if index + 1 < len(elements) else None
                        target(line, "module", following)
                    return
                elif text == "-":
                    break  # code on standard input
                else:
                    index += 1
            # No script, code or module written out: what it runs is given elsewhere.
            unknown.append((line, "runs a command line the check cannot read"))

        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and command(node) is not None:
                inner = node.left
                while isinstance(inner, ast.BinOp):
                    joined.add(id(inner))
                    inner = inner.left
                joined.add(id(inner))  # read here, with what is joined to it
            elements = None if id(node) in joined else command(node)
            if elements is not None:
                read_as_command.add(id(elements[0]))
                command_line(node.lineno, elements[1:])
            if not isinstance(node, ast.Call):
                continue
            function = self.functions.get(ast.unparse(node.func))
            if function == "run_path":
                target(node.lineno, "path", self.argument(node, 0, KEYWORDS[function]))
            elif function == "run_module":
                target(node.lineno, "module", self.argument(node, 0, KEYWORDS[function]))
            elif function in ("import_module", "__import__"):
                module(node.lineno, node, function)
            elif function in ("exec", "eval", "compile"):
                mode = {"exec": "exec", "eval": "eval"}.get(function)
                if function == "compile":
                    given = self.argument(node, 2, "mode")
                    mode = given.value if isinstance(given, ast.Constant) and \
                        given.value in ("exec", "eval", "single") else None
                if mode is None:
                    unknown.append((node.lineno, "runs code the check cannot read"))
                else:
                    source(node.lineno, self.argument(node, 0, KEYWORDS.get(function, "")),
                           mode)
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
    file = os.path.normpath(os.path.join(root, *path.split("/")))
    found, problems = [], []
    Reading(root, tracked, found, problems).code(tree, Resolver(root, file, tree),
                                                 [os.path.dirname(file), os.path.normpath(root)])
    return sorted(set(found)), ["%s:%d: %s" % (path, line, why) for line, why in sorted(problems)]


class Reading:
    """What one file imports and runs, the code it runs as a string included."""

    def __init__(self, root, tracked, found, problems):
        self.root, self.tracked, self.found, self.problems = root, tracked, found, problems

    def relative(self, candidate):
        """The path of a file below the root, written with `/`, or None for one outside it."""
        try:
            written = os.path.relpath(candidate, self.root).replace(os.sep, "/")
        except ValueError:  # another drive
            return None
        return None if written == ".." or written.startswith("../") else written

    def resolve(self, line, name, bases):
        """Adds each tracked file the module name names below a base; True where one does."""
        before = len(self.found)
        for base in bases:
            stem = os.path.join(base, *name.split("."))
            for candidate in (stem + ".py", os.path.join(stem, "__init__.py")):
                if self.relative(candidate) in self.tracked:
                    self.found.append((line, self.relative(candidate)))
        return len(self.found) > before

    @staticmethod
    def prefixes(name):
        pieces = name.split(".")
        return [".".join(pieces[:end]) for end in range(1, len(pieces) + 1)]

    def unseen(self, line, name, standard):
        if not standard or name.split(".")[0] not in sys.stdlib_module_names:
            self.problems.append((line, "imports `%s`, which is neither a module of the standard "
                                        "library nor a file the check sees" % name))

    def code(self, tree, resolver, bases, at=None, depth=0):
        """Reads the imports and runs of one file's code, or of code it runs as a string, which
        counts at the line `at` of the file."""

        def where(line):
            return line if at is None else at

        added, unknown = resolver.added(tree)
        self.problems.extend((where(line), "adds to sys.path a directory the check cannot work "
                                           "out") for line in unknown)
        own = bases[0]
        directories = list(dict.fromkeys(bases + added))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    seen = [self.resolve(where(node.lineno), name, directories)
                            for name in self.prefixes(alias.name)]
                    if not any(seen):
                        self.unseen(where(node.lineno), alias.name, True)
            elif isinstance(node, ast.ImportFrom):
                bases_of_node = directories
                if node.level:
                    base = own
                    for _ in range(node.level - 1):
                        base = os.path.dirname(base)
                    bases_of_node = [base]
                names = self.prefixes(node.module) if node.module else []
                seen = [self.resolve(where(node.lineno), name, bases_of_node) for name in names]
                seen += [self.resolve(where(node.lineno), ".".join(names[-1:] + [alias.name]),
                                      bases_of_node)
                         for alias in node.names if alias.name != "*"]
                if not any(seen):
                    written = node.module or ", ".join(alias.name for alias in node.names)
                    self.unseen(where(node.lineno), "." * node.level + written, not node.level)
        runs, trouble = resolver.runs(tree)
        self.problems.extend((where(line), why) for line, why in trouble)
        for line, kind, what in runs:
            line = where(line)
            if kind == "module":
                if not any([self.resolve(line, name, directories)
                            for name in self.prefixes(what)]):
                    self.unseen(line, what, True)
            elif kind == "code":
                self.given(line, what, resolver, directories, depth)
            elif what is not TEMPORARY:
                written = self.relative(resolver.absolute(what))
                if written is None:
                    continue  # a file outside the repository is no file git tracks
                if written in self.tracked:
                    self.found.append((line, written))
                elif written + "/__main__.py" in self.tracked:
                    self.found.append((line, written + "/__main__.py"))
                else:
                    self.problems.append((line, "runs `%s`, which is no Python file git tracks"
                                          % written))

    def given(self, line, what, resolver, directories, depth):
        """Reads code given as a string: to `-c` from the root, to `exec`, `eval` or `compile`
        from the directories of the file that runs it."""
        text, argv, mode = what
        try:
            tree = ast.parse(text, "<code>", mode)
        except (SyntaxError, ValueError):
            self.problems.append((line, "runs code the check cannot read"))
            return
        if depth >= NESTING:
            self.problems.append((line, "runs code given as a string nested too deep for the "
                                        "check"))
        elif argv is not None:
            self.code(tree, Resolver(self.root, None, tree, argv), [os.path.normpath(self.root)],
                      line, depth + 1)
        else:
            self.code(tree, Resolver(self.root, resolver.file, tree), directories, line,
                      depth + 1)


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
                continue  # left out on purpose, or reported among the problems of `parts`
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
                "subprocess.run([sys.executable, '-B'] + [%s])" % screen,
                "subprocess.run(([sys.executable] + ['-B']) + [%s, '--apply'])" % screen,
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

    def test_standard_modules_and_code_of_them_run_no_file_of_a_part(self):
        for line in ("subprocess.run([sys.executable, '-c', 'import json; print(1)'])",
                     "subprocess.run([sys.executable, '-m', 'unittest'])",
                     "runpy.run_module('json.tool')"):
            with self.subTest(line=line):
                self.assertEqual(([], []), self.run_from_core(line))

    def test_run_of_a_file_in_a_temporary_directory_is_no_dependency(self):
        # Taken for a path, the temporary directory would fail the check.
        for line in ("subprocess.run([sys.executable, os.path.join(tempfile.mkdtemp(), "
                     "'shell', 'screen.py')])",
                     "subprocess.run([sys.executable, str(Path(tempfile.TemporaryDirectory()"
                     ".name) / 'screen.py')])"):
            with self.subTest(line=line):
                self.assertEqual(([], []), self.run_from_core(line))

    def test_run_of_a_file_outside_the_root_is_no_dependency(self):
        # Taken for a file below the root, `../outside/screen.py` would be one git does not track.
        self.assertEqual(([], []), self.run_from_core(
            "runpy.run_path(os.path.join(HERE, '..', '..', 'outside', 'screen.py'))"))

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
                ("subprocess.run([sys.executable])", "runs a command line the check cannot read"),
                ("subprocess.run([sys.executable, '-B'] + sys.argv[1:])",
                 "runs a command line the check cannot read"),
                ("cmd = [sys.executable]; cmd.append(os.path.join(HERE, '..', 'shell', "
                 "'screen.py')); subprocess.run(cmd)", "runs a command line the check cannot read"),
                ("command(sys.executable, '-B')", "runs a command line the check cannot read"),
                ("runpy.run_module(sys.argv[1])", "runs a file the check cannot work out"),
                ("python = sys.executable", "uses sys.executable where the check cannot read what "
                                            "it runs"),
                ("subprocess.run([sys.executable, 'shell/missing.py'])",
                 "runs `shell/missing.py`, which is no Python file git tracks"),
                ("runpy.run_module('missing')", "imports `missing`, which is neither a module of "
                                                "the standard library nor a file the check sees"),
                ("subprocess.run([sys.executable, '-'], input=b'')",
                 "runs a command line the check cannot read")):
            with self.subTest(line=line):
                self.assertEqual(([], ["core/engine.py:7: " + why]), self.run_from_core(line))


class Code(unittest.TestCase):
    """Code given as a string — to `-c`, `exec`, `eval` or `compile` — and Python's import
    functions, each form on a small repository of its own."""

    run_from_core = Runs.run_from_core

    def assertEachFails(self, cases):
        for line, why in cases:
            with self.subTest(line=line):
                self.assertEqual(([], ["core/engine.py:7: " + why]), self.run_from_core(line))

    def test_each_form_of_code_given_to_the_interpreter_is_read(self):
        for line in (
                "subprocess.run([sys.executable, '-c', 'import shell.screen'])",
                "subprocess.run([sys.executable, '-cimport shell.screen'])",
                "subprocess.run([sys.executable, '-B', '-c', "
                "'import runpy; runpy.run_path(\"shell/screen.py\")'])",
                "subprocess.run([sys.executable, '-c', 'import sys; sys.path.insert(0, "
                "\"shell\"); import screen'])",
                "CODE = 'import runpy, sys; script = sys.argv[1]; runpy.run_path(script)'; "
                "subprocess.run([sys.executable, '-c', CODE, "
                "os.path.join(HERE, '..', 'shell', 'screen.py')])",
                "subprocess.run([sys.executable, '-c', 'import runpy, sys; first, script = "
                "sys.argv[1:]; runpy.run_path(script)', 'x', "
                "os.path.join(HERE, '..', 'shell', 'screen.py')])",
        ):
            with self.subTest(line=line):
                self.assertEqual(([FORBIDDEN], []), self.run_from_core(line))

    def test_code_given_to_the_interpreter_the_check_cannot_read_fails(self):
        self.assertEachFails((
            ("subprocess.run([sys.executable, '-c', os.environ['CODE']])",
             "runs code the check cannot read"),
            ("subprocess.run([sys.executable, '-c'])", "runs code the check cannot read"),
            ("subprocess.run([sys.executable, '-c', 'import ('])",
             "runs code the check cannot read"),
            ("subprocess.run([sys.executable, '-c', 'import runpy, sys; "
             "runpy.run_path(sys.argv[3])', 'x'])", "runs a file the check cannot work out")))

    def test_each_import_function_is_read(self):
        for line in (
                "importlib.import_module('shell.screen')",
                "importlib.import_module(name='shell.screen')",
                "importlib.import_module('.screen', 'shell')",
                "importlib.import_module('.screen', package='shell')",
                "from importlib import import_module as load; load('shell.screen')",
                "import importlib as il; il.import_module('shell.screen')",
                "MODULE = 'shell.screen'; importlib.import_module(MODULE)",
                "__import__('shell.screen')",
                "builtins.__import__('shell.screen', globals(), locals(), [], 0)",
        ):
            with self.subTest(line=line):
                self.assertEqual(([FORBIDDEN], []), self.run_from_core(line))

    def test_import_function_of_the_standard_library_is_no_dependency(self):
        self.assertEqual(([], []), self.run_from_core("importlib.import_module('json')"))

    def test_import_function_the_check_cannot_work_out_fails(self):
        self.assertEachFails((
            ("importlib.import_module(os.environ['MODULE'])",
             "imports a module the check cannot work out"),
            ("importlib.import_module('.screen')", "imports a module the check cannot work out"),
            ("__import__('screen', globals(), locals(), [], 1)",
             "imports a module the check cannot work out"),
            ("importlib.import_module('missing')", "imports `missing`, which is neither a module "
                                                   "of the standard library nor a file the check "
                                                   "sees")))

    def test_each_form_of_code_run_by_exec_eval_or_compile_is_read(self):
        screen = "os.path.join(HERE, '..', 'shell', 'screen.py')"
        for line in (
                "exec('import shell.screen')",
                "exec(b'import shell.screen')",
                "exec(compile('import shell.screen', 'shell', 'exec'))",
                "eval(\"__import__('shell.screen')\")",
                "exec(open(%s).read())" % screen,
                "exec(open(%s, encoding='utf-8').read(), {})" % screen,
                "exec((Path(HERE) / '..' / 'shell' / 'screen.py').read_text())",
                "code = open(%s).read(); exec(code)" % screen,
                "compile(open(%s).read(), 'screen', mode='exec')" % screen,
        ):
            with self.subTest(line=line):
                self.assertEqual(([FORBIDDEN], []), self.run_from_core(line))

    def test_code_given_as_a_string_is_read_down_to_its_limit(self):
        def nested(times):
            code = "import shell.screen"
            for _ in range(times):
                code = "exec(%r)" % code
            return code
        self.assertEqual(([FORBIDDEN], []), self.run_from_core(nested(NESTING)))
        self.assertEqual(([], ["core/engine.py:7: runs code given as a string nested too deep for "
                               "the check"]), self.run_from_core(nested(NESTING + 1)))

    def test_code_of_the_standard_library_run_by_exec_is_no_dependency(self):
        for line in ("eval('1 + 1')", "exec('import json')"):
            with self.subTest(line=line):
                self.assertEqual(([], []), self.run_from_core(line))

    def test_code_run_by_exec_eval_or_compile_the_check_cannot_read_fails(self):
        self.assertEachFails((
            ("exec(os.environ['CODE'])", "runs code the check cannot read"),
            ("exec(sys.stdin.read())", "runs code the check cannot read"),
            ("compile('import json', 'x', MODE)", "runs code the check cannot read"),
            ("exec('import (')", "runs code the check cannot read"),
            ("exec(open(os.environ['SCRIPT']).read())", "runs a file the check cannot work out")))


class LeftOut(unittest.TestCase):

    def test_python_file_left_out_on_purpose_is_no_failure(self):
        # Without the list, `tools/build.py` would be a file no part claims.
        repository = Repository(self, {
            "foundations/part_map.md": PART_MAP_TEXT + (
                "\n## Files left out on purpose\n\n| File | Why |\n|---|---|\n"
                "| tools/build.py | a script of one person's set-up |\n"),
            "tools/build.py": "import json\n",
            "core/engine.py": "from tools import build\n"})
        self.assertEqual(([], []), repository.check())


if __name__ == "__main__":
    unittest.main()
