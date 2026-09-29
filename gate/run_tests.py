"""The test runner of the-way: runs the `unittest` tests of one directory and records a verdict for
each invariant and each environment fact a test cites (WAY-61, WAY-65, WAY-74, WAY-81).

Usage, from the root of the repository:

    python -B gate/run_tests.py DIRECTORY [--record PATH]

The tests are the ones `python -m unittest discover -s DIRECTORY -p "test_*.py"` finds, and the
report for a person is the one `unittest` prints. --record names a JSON Lines file, its path
ending in `.jsonl`, created or overwritten, which receives the-way's own record of the run
(WAY-74); without it, the run writes no record anywhere.

A test cites an invariant by a comment line `invariant: <identifier>/<version>` standing alone on
its line inside the body of the test method (WAY-65), and an environment fact by a line
`fact: <identifier>/<version>` (WAY-81); a comment at the top of the file or of the class is no
citation of any test. A comment line reading `invariant:` or `fact:` with anything else after it,
or a version written with a leading zero, is a citation off the form; `Invariant:`, `invariants:`
and text inside a string are no citation. Everything below said of an invariant holds for a fact
alike, and a fact's verdict stands under the key `fact` where an invariant's stands under
`invariant` (WAY-74). The tests import from the working directory first, as
under `python -m unittest`.

A verdict is what a test gave (WAY-61, WAY-63). The record holds a line per test and invariant it
gives a verdict for, and a line with `invariant` null for each failure no citing test owns:

- a test that succeeds gives `pass` for each invariant it cites; the pass lines of an invariant are
  written only once every test citing it has an outcome, so that a run that stops halfway leaves
  no pass for an invariant another check of it did not reach, while every line written so far
  stays readable, flushed as it is written;
- a test that fails or errs (in `setUp` or `tearDown` included), or is marked as an expected
  failure and fails, gives `fail` for each invariant it cites;
- a test marked as an expected failure that passes gives `pass` for what it cites, since its
  assertions held, and a null line saying the mark is stale;
- a test that is skipped — by a decorator, `skipTest`, a skipped subtest, a skip in `setUpClass`
  or `setUpModule`, or its module skipping itself — gives no verdict for what it cites, and a null
  line saying which test skipped and why; an invariant it cites then gets no `pass` from any test
  of the run, while a `fail` another test gives it stands, so the gate reads `error` for it unless
  a real `fail` exists;
- a test that cites nothing gives a null line where `unittest` counts it as failed, an error and
  an unexpected success included, and no line otherwise;
- a failure of a class or module fixture, a module that cannot be imported, a citation off the
  form, a directory holding no test, and a run interrupted before its end each give a null line;
  the tests a failed set-up or import kept from running give `fail` for what they cite;
- the body of a citing test method — the function its citation stands in, as its source defines
  it — is watched through `sys.monitoring` while its test runs: a test `unittest` counts as passed
  whose body never executed (a coroutine or generator never driven, a method replaced or never
  called, a `run()` that only reports success), never returned, or had something raised out of it
  (an assertion caught around it, a retry) gives `fail` for what it cites; a test run a second
  time whose later run fails, or raises out of its body, gives `fail` again;
- a citing test method that a `test_*.py` file below DIRECTORY, in whatever folder, a hidden one
  included, defines but the suite never runs — its folder is one discovery does not enter, having
  no `__init__.py`, its module's `load_tests` leaves it out, or its class stands under an `if`, a
  `try`, a `with` or a function that never defines it — gives `fail` for what it cites; in such a
  file that Python cannot parse, every citation gives `fail`;
- a citation comment a `test_*.py` file below DIRECTORY holds outside the body of any test method
  — at the top of the file, at class level, in a helper or `setUp` — cites for no check, and gives
  a null line naming its file and line; a function defined outside a class, at module level or by
  a factory, that a class assigns as a test method is that test's body, and a citation in it is
  that test's.

A line's `check` names a test as `<file>::<Class>.<method>`, where the file's path is DIRECTORY, as
the command gives it, joined with the file's path below it; a fixture as `<file>::<Class>.<fixture>`
or `<file>::<fixture>`; a module that cannot be imported as its file; and a failure of the run
itself as this program. A character the record cannot hold in UTF-8, as a lone surrogate, is
written as its `\\u` escape, and an exception whose text cannot be read is described as
`<exception str() failed>`.

Exit code: 0 when the run holds no failure; 1 when some line of the record is `fail` or `unittest`
counts the run as failed; 2 when the directory is not one, --record is given twice or names a path
not ending in `.jsonl`, the record cannot be written, no `sys.monitoring` tool id is free to watch
the bodies, or the run is interrupted (KeyboardInterrupt) before its end. A process killed
outright — by `os._exit` or a signal — leaves the exit code to whatever ended it, and its record
holds the lines written until then.
"""

import argparse
import ast
import fnmatch
import importlib.util
import inspect
import json
import os
import posixpath
import re
import sys
import tokenize
import unittest

sys.dont_write_bytecode = True

# The name a record gives this program, as the check of a failure no test gave.
PROGRAM = "gate/run_tests.py"
PATTERN = "test_*.py"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The form of an identifier at a version, from the relation model, as the format guards read it
# (WAY-57, WAY-79); how a citation stands in a test is this program's own, below (WAY-65).
identifier_form = _load("relation_model_identifier",
                        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                     "relation-model", "identifier.py"))
CITED = re.compile(identifier_form.CITED)
# A comment line reading `invariant:` or `fact:` cites what follows it, all of it: a value of
# more than one word, or of none, is a citation off the form, never silence. A citation is kept as
# (kind, value), and the kind is the key its verdict stands under in the record (WAY-74, WAY-81).
CITATION = re.compile(r"#\s*(invariant|fact):\s*(.*?)\s*")
FIXTURE = re.compile(r"^(setUpClass|tearDownClass|setUpModule|tearDownModule) \((.+)\)$")
# The module unittest's loader defines its placeholders in: a test for a module it could not
# import, and a test for a module that raised a skip on import.
LOADER = "unittest.loader"


# --- citations ------------------------------------------------------------------------------


def comment_citations(path):
    """(line number, value) of every citation comment standing alone on its line in a file; in
    a file Python cannot read as tokens, of every line that reads as such a comment."""
    try:
        with open(path, "rb") as handle:
            tokens = list(tokenize.tokenize(handle.readline))
    except OSError:
        return []
    except (SyntaxError, tokenize.TokenError, UnicodeDecodeError):
        with open(path, encoding="utf-8", errors="replace") as handle:
            return [(number, match.groups()) for number, match in
                    ((number, CITATION.fullmatch(text.strip()))
                     for number, text in enumerate(handle, start=1)) if match]
    found = []
    for token in tokens:
        if token.type != tokenize.COMMENT or token.line[:token.start[1]].strip():
            continue
        match = CITATION.fullmatch(token.string)
        if match:
            found.append((token.start[0], match.groups()))
    return found


def cited_between(path, first, last, cache):
    if path not in cache:
        cache[path] = comment_citations(path)
    values = []
    for number, value in cache[path]:
        if first <= number <= last and value not in values:
            values.append(value)
    return values


def label(citation):
    """How a message names a citation: an invariant by its value, a fact as `fact <value>`."""
    kind, value = citation
    return value if kind == "invariant" else "%s %s" % (kind, value)


def named(citation):
    """A citation quoted in a message: an invariant as `<value>`, a fact as fact `<value>`, since
    a line with no entry holds `invariant` null whichever kind it was (WAY-74)."""
    kind, value = citation
    return "`%s`" % value if kind == "invariant" else "%s `%s`" % (kind, value)


def source_key(path):
    return os.path.normcase(os.path.abspath(path))


def method_citations(test, cache):
    """The citations inside the body of a test's method — the function `unittest` resolves on
    its class, wherever that function is defined — read from its source; where that source
    stands, as (file, first line), and its last line; and the function. None where it cannot be
    read."""
    function = getattr(type(test), getattr(test, "_testMethodName", ""), None)
    if function is None:
        return [], None, None, None
    function = inspect.unwrap(function)
    try:
        path = inspect.getsourcefile(function)
        lines, first = inspect.getsourcelines(function)
    except (OSError, TypeError):
        return [], None, None, function
    if path is None:
        return [], None, None, function
    last = first + len(lines) - 1
    return cited_between(path, first, last, cache), (source_key(path), first), last, function


def module_tests(path, cache):
    """(Class.method, citations, first line, last line) of every test method a module's source
    defines; None where its source cannot be parsed."""
    try:
        with open(path, "rb") as handle:
            tree = ast.parse(handle.read(), filename=path)
    except (OSError, SyntaxError, ValueError):
        return None
    found = []

    def visit(body, prefix, in_class):
        """Classes at any depth — in a class, or under an `if`, a `try`, a `with`, a loop or a
        function — and the test methods standing in a class's body."""
        for node in body:
            if isinstance(node, ast.ClassDef):
                visit(node.body, prefix + node.name + ".", True)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if in_class and node.name.startswith("test"):
                    first = min([node.lineno] + [item.lineno for item in node.decorator_list])
                    found.append((prefix + node.name,
                                  cited_between(path, first, node.end_lineno, cache), first,
                                  node.end_lineno))
                else:
                    visit(node.body, prefix + node.name + ".<locals>.", False)
            else:
                for field in ("body", "orelse", "finalbody"):
                    inner = getattr(node, field, None)
                    if isinstance(inner, list):
                        visit(inner, prefix, in_class)
                for part in getattr(node, "handlers", []) + getattr(node, "cases", []):
                    visit(part.body, prefix, in_class)

    visit(tree.body, "", False)
    return found


def test_files(start):
    """Every file below `start` whose name matches the pattern, in whatever folder, a hidden one
    included, as discovery would reach it with every folder a package."""
    found = []
    for folder, folders, names in os.walk(start):
        folders[:] = sorted(folders)
        found += [os.path.join(folder, name) for name in sorted(names)
                  if fnmatch.fnmatch(name, PATTERN)]
    return found


# --- the record -----------------------------------------------------------------------------


class Record:
    """The-way's own record of a run (WAY-74), each line flushed as it is written."""

    def __init__(self, path):
        self.handle = None
        self.failed = False
        if path is not None:
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
            # A character UTF-8 cannot hold, as a lone surrogate in a message, is written as its
            # `\u` escape, which JSON reads back, rather than stopping the run.
            self.handle = open(path, "w", encoding="utf-8", errors="backslashreplace",
                               newline="\n")

    def write(self, check, verdict, citation, description=None):
        """A line for a verdict on a citation (kind, value), or with `invariant` null for a
        failure no citation owns."""
        if verdict != "pass":
            self.failed = True
        if self.handle is None:
            return
        kind, value = citation or ("invariant", None)
        line = {"check": check, "verdict": verdict, kind: value}
        if description is not None:
            line["description"] = description
        self.handle.write(json.dumps(line, ensure_ascii=False) + "\n")
        self.handle.flush()

    def close(self):
        if self.handle is not None:
            self.handle.close()


def exception_text(error, last=False):
    """`<exception>: <first line of its message>`; with `last`, the last line of the message, for
    a message that carries a traceback, as unittest's message of a failed import does."""
    kind, value = error[0], error[1]
    try:
        message = str(value)
    except Exception:
        message = "<exception str() failed>"
    text = [line.strip() for line in message.strip().splitlines() if line.strip()]
    if not text:
        return kind.__name__
    return text[-1] if last else "%s: %s" % (kind.__name__, text[0])


# --- watching the bodies --------------------------------------------------------------------


MONITORING = sys.monitoring
# The tool ids the runner may take, the unassigned ones first; never DEBUGGER_ID or COVERAGE_ID,
# so that a debugger or coverage.py runs beside it.
TOOLS = (3, 4, MONITORING.PROFILER_ID, MONITORING.OPTIMIZER_ID)
EVENTS = MONITORING.events


class Monitor:
    """Watches, through `sys.monitoring` (the standard library, WAY-38), the body of each citing
    test method while its own test runs: how often it started, returned, and had something raised
    out of it. A code object is known by its file, its first line and its name, as its source
    defines it; every other code object is let go at its first event."""

    def __init__(self, bodies):
        self.bodies = bodies        # (file, first line, name) of every watched body
        self.known = {}             # id of a code object -> (it, its key when watched)
        self.current = None         # (key, check) of the test running now
        self.tool = None

    def key(self, code):
        # By the object's identity: code objects compiled from two files compare equal when
        # their bytecode, name and first line do. The object is kept, so its id stays its own.
        entry = self.known.get(id(code))
        if entry is None or entry[0] is not code:
            found = (source_key(code.co_filename), code.co_firstlineno, code.co_name)
            entry = (code, found if found in self.bodies else None)
            self.known[id(code)] = entry
        return entry[1]

    def counted(self, code, field):
        key = self.key(code)
        if key is None:
            return False
        if self.current is not None and self.current[0] == key:
            check = self.current[1]
            setattr(check, field, getattr(check, field) + 1)
        return True

    def started(self, code, offset):
        return None if self.counted(code, "started") else MONITORING.DISABLE

    def returned(self, code, offset, value):
        return None if self.counted(code, "returned") else MONITORING.DISABLE

    def unwound(self, code, offset, exception):
        self.counted(code, "unwound")

    def start(self):
        """Takes a free tool id, or says none is free."""
        free = [tool for tool in TOOLS if MONITORING.get_tool(tool) is None]
        if not free:
            raise RuntimeError("no sys.monitoring tool id is free to watch the test bodies "
                               "(%s are taken)" % ", ".join(str(tool) for tool in TOOLS))
        self.tool = free[0]
        MONITORING.use_tool_id(self.tool, "the-way test runner")
        MONITORING.register_callback(self.tool, EVENTS.PY_START, self.started)
        MONITORING.register_callback(self.tool, EVENTS.PY_RETURN, self.returned)
        MONITORING.register_callback(self.tool, EVENTS.PY_UNWIND, self.unwound)
        MONITORING.set_events(self.tool, EVENTS.PY_START | EVENTS.PY_RETURN | EVENTS.PY_UNWIND)

    def stop(self):
        if self.tool is None:
            return
        MONITORING.set_events(self.tool, 0)
        for event in (EVENTS.PY_START, EVENTS.PY_RETURN, EVENTS.PY_UNWIND):
            MONITORING.register_callback(self.tool, event, None)
        MONITORING.free_tool_id(self.tool)
        self.tool = None


# --- the plan of a run ----------------------------------------------------------------------


# What a test's outcome gives what it cites: a verdict it gave, or none (WAY-61, WAY-63).
FAILED = "failed"           # its assertions did not hold, or it erred: `fail`
NO_VERDICT = "no verdict"   # it did not run to a verdict — skipped, or never run: no line
STALE_MARK = "stale mark"   # marked as an expected failure, yet passed: `pass`, and a null line


class Check:
    """A test the run found, the invariants it cites and what happened to it."""

    def __init__(self, name, citations, group=None, module=None):
        self.name = name
        self.citations = citations
        self.group = group          # "module.Class" of its class
        self.module = module        # the module it stands in
        self.outcomes = []          # (kind, description, whether unittest counts it failed)
        self.succeeded = False
        self.done = False
        self.body = None            # (file, first line, name) of its method's body, watched
        self.started = self.returned = self.unwound = 0
        self.late = None            # a failure of a run of it after its lines were written

    def first(self, kind):
        return next((description for found, description, _ in self.outcomes if found == kind),
                    None)

    def observed(self):
        """What the watch of its body saw go wrong, or None."""
        if self.unwound:
            return "raised out of its body"
        if not self.started:
            return "its body never executed"
        if self.returned < self.started:
            return "its body never returned"
        return None


class Plan:
    """Every test of the run with its citations, and the pass lines held until every test citing
    an invariant has an outcome. An invariant a citing test gives no verdict for gets no pass from
    any test of the run."""

    def __init__(self, record, directory, start):
        self.record = record
        self.directory = directory
        self.start = start
        self.checks = {}            # key -> Check
        self.placeholders = {}      # test id of a loader's placeholder -> (name, keys)
        self.pending = {}           # invariant -> keys of citing tests without an outcome
        self.held = {}              # invariant -> the names of tests that passed it
        self.voided = set()         # invariants a citing test gave no verdict for
        self.sources = set()        # (file, first line) of every test method the suite runs
        self.spans = set()          # (file, first line, last line) of the same, from the run
        self.bodies = set()         # (file, first line, name) of every citing method's body
        self.running = None         # the key of the test running now
        self.cache = {}

    def file_of(self, module):
        """The path a check names for a module: the directory as the command gives it, joined
        with the module's file below it."""
        path = getattr(sys.modules.get(module), "__file__", None)
        if not path or not os.path.isfile(path):
            path = self.module_path(module)
        return self.named(path)

    def named(self, path):
        relative = os.path.relpath(os.path.abspath(path), self.start).replace(os.sep, "/")
        return posixpath.normpath(posixpath.join(self.directory.replace(os.sep, "/"), relative))

    def module_path(self, module):
        base = os.path.join(self.start, *module.split("."))
        package = os.path.join(base, "__init__.py")
        return package if os.path.isfile(package) else base + ".py"

    def add(self, key, check):
        self.checks[key] = check
        for citation in check.citations:
            if CITED.fullmatch(citation[1]):
                self.pending.setdefault(citation, []).append(key)

    def collect(self, suite):
        for test in iterate(suite):
            kind = type(test)
            if kind.__module__ == LOADER:
                self.collect_placeholder(test)
                continue
            module = kind.__module__
            name = "%s::%s.%s" % (self.file_of(module), kind.__qualname__,
                                  getattr(test, "_testMethodName", "?"))
            citations, source, last, function = method_citations(test, self.cache)
            check = Check(name, citations, "%s.%s" % (module, kind.__qualname__), module)
            if source is not None:
                self.sources.add(source)
                self.spans.add(source + (last,))
                if citations:
                    check.body = self.body_of(source, function)
            self.add(test.id(), check)

    def body_of(self, source, function):
        """The key of the code object of the test method whose source starts at `source`: its
        file, its first line and its name, as the file defines it — a `def` in a class, or a
        function defined elsewhere, at module level or by a factory, that the class assigns,
        whose code starts at that line of that file."""
        path, first = source
        body = None
        for method, _, start, _ in module_tests(path, self.cache) or []:
            if start == first:
                body = (path, first, method.rpartition(".")[2])
        code = getattr(function, "__code__", None)
        if body is None and code is not None and \
                (source_key(code.co_filename), code.co_firstlineno) == source:
            body = (path, first, code.co_name)
        if body is not None:
            self.bodies.add(body)
        return body

    def collect_placeholder(self, test):
        """A test the loader made for a module it could not import, or that raised a skip on
        import: the test methods the module's source defines stand for the checks it holds, or,
        where the source cannot be parsed, every citation in the file."""
        module = test._testMethodName
        path = self.module_path(module)
        name = self.file_of(module)
        tests = module_tests(path, self.cache) if os.path.isfile(path) else []
        if tests is None:
            cited = list(dict.fromkeys(value for _, value in comment_citations(path)))
            tests = [(None, cited, None, None)] if cited else []
            self.sources.add((source_key(path), None))
        keys = []
        for method, citations, first, _ in tests:
            key = "%s::%s:%s" % (test.id(), method, first)
            self.add(key, Check("%s::%s" % (name, method) if method else name, citations))
            if first is not None:
                self.sources.add((source_key(path), first))
            keys.append(key)
        self.placeholders[test.id()] = (name, keys)

    def left_out(self):
        """Every citing test method a `test_*.py` file below the directory defines that the suite
        does not run — a file in a folder discovery does not enter, a method its module's
        `load_tests` leaves out, or a class never defined: it never runs, so it gives `fail` for
        what it cites. In such a file that cannot be parsed, every citation gives `fail`."""
        imported = {source_key(module.__file__) for module in list(sys.modules.values())
                    if getattr(module, "__file__", None)}
        for path in test_files(self.start):
            tests = module_tests(path, self.cache)
            if tests is None:
                if (source_key(path), None) in self.sources:
                    continue
                cited = list(dict.fromkeys(value for _, value in comment_citations(path)))
                tests = [(None, cited, None, None)] if cited else []
                why = "not run: its file cannot be parsed"
            else:
                why = ("not run: its module's suite leaves it out"
                       if source_key(path) in imported
                       else "not run: discovery does not reach its file")
            for method, citations, first, _ in tests:
                if not citations or (source_key(path), first) in self.sources:
                    continue
                key = "%s::%s:%s" % (source_key(path), method, first)
                self.add(key, Check("%s::%s" % (self.named(path), method) if method
                                    else self.named(path), citations))
                self.outcome(key, FAILED, why, False)
                self.finish(key)

    def stray_citations(self):
        """Every citation comment a `test_*.py` file below the directory holds outside the body
        of any test method — at the top of the file, at class level, in a helper or `setUp` —
        cites for no check (WAY-65: at the check), and gives a null line naming where it stands."""
        for path in test_files(self.start):
            tests = module_tests(path, self.cache)
            if tests is None:
                continue
            if path not in self.cache:
                self.cache[path] = comment_citations(path)
            inside = [(first, last) for _, _, first, last in tests]
            inside += [(first, last) for where, first, last in self.spans
                       if where == source_key(path)]
            for number, value in self.cache[path]:
                if not any(first <= number <= last for first, last in inside):
                    self.record.write(self.named(path), "fail", None,
                                      "%s:%d: `%s: %s` stands outside any test, and a "
                                      "check cites at the check (WAY-65)"
                                      % ((self.named(path), number) + tuple(value)))

    # --- outcomes

    def outcome(self, key, kind, description, counted):
        check = self.checks.get(key)
        if check is None:
            return
        if not check.done:
            check.outcomes.append((kind, description, counted))
        elif kind == FAILED and key == self.running and check.late is None:
            check.late = description

    def begin(self, key, monitor):
        """A test starts: its body is watched until it stops."""
        self.running = key
        check = self.checks.get(key)
        monitor.current = (check.body, check) if check and check.body else None
        if check is not None:
            check.window = check.unwound

    def end(self, key, monitor):
        """A test stops. A test run again after its lines were written, whose later run failed or
        raised out of its body, gives `fail` again for what it cites."""
        monitor.current = None
        self.running = None
        check = self.checks.get(key)
        if check is None or not check.done:
            return
        if check.late is None and check.unwound > getattr(check, "window", check.unwound):
            check.late = "raised out of its body"
        if check.late is not None:
            for citation in check.citations:
                if CITED.fullmatch(citation[1]):
                    self.record.write(check.name, "fail", citation, check.late)
            check.late = None

    def finish(self, key, final=False):
        """Writes what a test's outcome gives what it cites. A test that has no outcome yet —
        stopped by an interruption — stays pending, unless the run ran to its end (`final`)."""
        check = self.checks.get(key)
        if check is None or check.done:
            return
        failed, skipped = check.first(FAILED), check.first(NO_VERDICT)
        stale = check.first(STALE_MARK)
        if not (failed or skipped or stale or check.succeeded):
            if not final:
                return
            skipped = "the test gave no outcome"
        if not (failed or skipped) and check.body is not None:
            failed = check.observed()
            if failed:
                check.outcomes.append((FAILED, failed, False))
        check.done = True
        valid = [citation for citation in check.citations if CITED.fullmatch(citation[1])]
        for citation in check.citations:
            if citation not in valid:
                self.record.write(check.name, "fail", None,
                                  "cites %s, which is not `<identifier>/<version>`"
                                  % named(citation))
        if not valid:
            counted = [description for _, description, count in check.outcomes if count]
            if counted:
                self.record.write(check.name, "fail", None, counted[0])
            return
        if failed:
            verdict = "fail"
        elif skipped:
            verdict = None
            self.record.write(check.name, "fail", None, "no verdict for %s: %s"
                              % (", ".join(label(citation) for citation in valid), skipped))
        else:
            verdict = "pass"
            if stale:
                self.record.write(check.name, "fail", None, stale)
        for citation in valid:
            if verdict == "fail":
                self.record.write(check.name, "fail", citation, failed)
            elif verdict is None:
                self.voided.add(citation)
                self.held.pop(citation, None)
            elif citation not in self.voided:
                self.held.setdefault(citation, []).append(check.name)
            self.pending[citation].remove(key)
            if not self.pending[citation]:
                for name in self.held.pop(citation, []):
                    self.record.write(name, "pass", citation)

    def keep_from_running(self, keys, kind, description):
        for key in keys:
            self.outcome(key, kind, description, False)
            self.finish(key)

    def fixture(self, holder, error, skipped=False):
        """A failure, or a skip, of a class or module fixture, which unittest reports without a
        test of its own; a set-up that fails or skips keeps the tests it serves from running."""
        match = FIXTURE.match(holder.description)
        if not match:
            if not skipped:
                self.record.write(PROGRAM, "fail", None,
                                  "%s: %s" % (holder.description, exception_text(error)))
            return
        method, owner_name = match.groups()
        if method.endswith("Class"):
            module, _, qualname = owner_name.rpartition(".")
            while module and module not in sys.modules:
                module, _, part = module.rpartition(".")
                qualname = part + "." + qualname
            members = [key for key, check in self.checks.items() if check.group == owner_name]
            name = "%s::%s.%s" % (self.file_of(module), qualname, method)
        else:
            members = [key for key, check in self.checks.items() if check.module == owner_name]
            name = "%s::%s" % (self.file_of(owner_name), method)
        if skipped:
            kind, description = NO_VERDICT, "not run: %s skipped it: %s" % (method, error)
        else:
            failure = "%s failed: %s" % (method, exception_text(error))
            self.record.write(name, "fail", None, failure)
            kind, description = FAILED, "not run: " + failure
        if method.startswith("setUp"):
            self.keep_from_running(members, kind, description)

    def placeholder(self, test, description, failed):
        name, keys = self.placeholders.get(test.id(), (self.file_of(test._testMethodName), []))
        if failed:
            self.record.write(name, "fail", None, description)
        self.keep_from_running(keys, FAILED if failed else NO_VERDICT, "not run: " + description)

    def unfinished(self):
        """Every citing test left without an outcome at the end of a run that ran to its end."""
        for key, check in list(self.checks.items()):
            if not check.done and check.citations:
                self.finish(key, final=True)


def iterate(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from iterate(item)
        else:
            yield item


def owner(test):
    """The test a subtest belongs to."""
    return getattr(test, "test_case", test)


def recording_result(plan, monitor):
    class RecordingResult(unittest.TextTestResult):
        """unittest's report for a person, with the outcome of every test passed to the plan."""

        def startTest(self, test):
            super().startTest(test)
            plan.begin(test.id(), monitor)

        def addSuccess(self, test):
            super().addSuccess(test)
            check = plan.checks.get(test.id())
            if check is not None:
                check.succeeded = True

        def addFailure(self, test, err):
            super().addFailure(test, err)
            plan.outcome(test.id(), FAILED, "failed: " + exception_text(err), True)

        def addError(self, test, err):
            super().addError(test, err)
            if isinstance(test, unittest.suite._ErrorHolder):
                plan.fixture(test, err)
            elif type(test).__module__ == LOADER:
                plan.placeholder(test, "cannot be imported: " + exception_text(err, last=True),
                                 failed=True)
            else:
                plan.outcome(test.id(), FAILED, "error: " + exception_text(err), True)

        def addSkip(self, test, reason):
            super().addSkip(test, reason)
            if isinstance(test, unittest.suite._ErrorHolder):
                plan.fixture(test, reason, skipped=True)
            elif type(test).__module__ == LOADER:
                plan.placeholder(test, "the module is skipped: %s" % reason, failed=False)
            else:
                parent = owner(test)
                where = test.id()[len(parent.id()):].strip() if parent is not test else ""
                plan.outcome(parent.id(), NO_VERDICT,
                             "skipped%s: %s" % (" in " + where if where else "", reason), False)

        def addExpectedFailure(self, test, err):
            super().addExpectedFailure(test, err)
            plan.outcome(test.id(), FAILED, "marked as an expected failure, and failed: "
                         + exception_text(err), False)

        def addUnexpectedSuccess(self, test):
            super().addUnexpectedSuccess(test)
            plan.outcome(test.id(), STALE_MARK, "marked as an expected failure, yet passed: the "
                         "mark is stale", True)

        def addSubTest(self, test, subtest, err):
            super().addSubTest(test, subtest, err)
            if err is not None:
                failed = issubclass(err[0], test.failureException)
                plan.outcome(test.id(), FAILED, "%s in %s: %s"
                             % ("failed" if failed else "error",
                                subtest.id()[len(test.id()):].strip(), exception_text(err)), True)

        def stopTest(self, test):
            super().stopTest(test)
            plan.end(test.id(), monitor)
            plan.finish(test.id())

    return RecordingResult


# --- entry point ----------------------------------------------------------------------------


def run(directory, record_path=None, stream=None):
    stream = stream or sys.stderr
    try:
        record = Record(record_path)
    except OSError as problem:
        stream.write("cannot write the record: %s\n" % problem)
        return 2
    try:
        if not os.path.isdir(directory):
            message = "%s is not a directory" % directory
            stream.write(message + "\n")
            record.write(PROGRAM, "fail", None, message)
            return 2
        start = os.path.abspath(directory)
        suite = unittest.TestLoader().discover(start, pattern=PATTERN)
        plan = Plan(record, directory, start)
        plan.collect(suite)
        plan.stray_citations()
        plan.left_out()
        monitor = Monitor(plan.bodies)
        try:
            monitor.start()
        except RuntimeError as problem:
            stream.write("%s\n" % problem)
            record.write(PROGRAM, "fail", None, str(problem))
            return 2
        runner = unittest.TextTestRunner(stream=stream,
                                         resultclass=recording_result(plan, monitor))
        try:
            result = runner.run(suite)
        except KeyboardInterrupt:
            message = "the run stopped before every test ran"
            stream.write("\n%s\n" % message)
            record.write(PROGRAM, "fail", None, message)
            return 2
        finally:
            monitor.stop()
        if not plan.checks and not plan.placeholders:
            record.write(PROGRAM, "fail", None, "no test found in %s" % directory)
            return 1
        plan.unfinished()
        return 0 if result.wasSuccessful() and not record.failed else 1
    finally:
        record.close()


def main(argv=None):
    # Tests import the product's own modules from the working directory, the root of the
    # repository, as under `python -m unittest`, never from the folder of this script.
    sys.path[0] = os.getcwd()
    parser = argparse.ArgumentParser(description="Run the unittest tests of a directory and record "
                                                 "a verdict for each invariant and fact a "
                                                 "test cites.")
    parser.add_argument("directory", help="the directory whose test_*.py files hold the tests")
    parser.add_argument("--record", action=OneRecord,
                        help="the JSON Lines file, ending in .jsonl, created or overwritten, that "
                             "receives a verdict for each invariant and fact a test cites")
    arguments = parser.parse_args(argv)
    return run(arguments.directory, arguments.record)


class OneRecord(argparse.Action):
    """--record names one path, and a JSON Lines one (WAY-74): given twice, or naming a path that
    does not end in `.jsonl`, the command is refused with exit code 2 and writes nothing."""

    def __call__(self, parser, namespace, value, option_string=None):
        if getattr(namespace, self.dest) is not None:
            parser.error("%s is given twice; a run writes one record" % option_string)
        if not value.endswith(".jsonl"):
            parser.error("%s %s: the record of a run is a JSON Lines file, whose path ends in "
                         ".jsonl" % (option_string, value))
        setattr(namespace, self.dest, value)


if __name__ == "__main__":
    sys.exit(main())
