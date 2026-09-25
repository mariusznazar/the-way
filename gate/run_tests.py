"""The test runner of the-way: runs the `unittest` tests of one directory and records a verdict for
each invariant a test cites (WAY-61, WAY-65, WAY-74).

Usage, from the root of the repository:

    python -B gate/run_tests.py DIRECTORY [--record PATH]

The tests are the ones `python -m unittest discover -s DIRECTORY -p "test_*.py"` finds, and the
report for a person is the one `unittest` prints. --record names a JSON Lines file, its path
ending in `.jsonl`, created or overwritten, which receives the-way's own record of the run
(WAY-74); without it, the run writes no record anywhere.

A test cites an invariant by a comment line `invariant: <identifier>/<version>` standing alone on
its line inside the body of the test method (WAY-65); a comment at the top of the file or of the
class is no citation of any test. A comment line reading `invariant:` with anything else after it,
or a version written with a leading zero, is a citation off the form; `Invariant:`, `invariants:`
and text inside a string are no citation. The tests import from the working directory first, as
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
- a citing test method that a `test_*.py` file below DIRECTORY defines but the suite never runs —
  its folder is one discovery does not enter, having no `__init__.py`, or its module's `load_tests`
  leaves it out — gives `fail` for what it cites;
- a citation comment a `test_*.py` file below DIRECTORY holds outside the body of any test method
  — at the top of the file, at class level, in a helper or `setUp` — cites for no check, and gives
  a null line naming its file and line.

A line's `check` names a test as `<file>::<Class>.<method>`, where the file's path is DIRECTORY, as
the command gives it, joined with the file's path below it; a fixture as `<file>::<Class>.<fixture>`
or `<file>::<fixture>`; a module that cannot be imported as its file; and a failure of the run
itself as this program.

Exit code: 0 when the run holds no failure; 1 when some line of the record is `fail` or `unittest`
counts the run as failed; 2 when the directory is not one, --record is given twice or names a path
not ending in `.jsonl`, the record cannot be written, or the run is interrupted (KeyboardInterrupt)
before its end. A process killed outright — by `os._exit` or a signal — leaves the exit code to
whatever ended it, and its record holds the lines written until then.
"""

import argparse
import ast
import fnmatch
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
# A version is a number written without a leading zero, as the invariants guard reads it.
CITED = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*/[1-9][0-9]*")
# A comment line reading `invariant:` cites what follows it, all of it: a value of more than one
# word, or of none, is a citation off the form, never silence.
CITATION = re.compile(r"#\s*invariant:\s*(.*?)\s*")
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
            return [(number, match.group(1)) for number, match in
                    ((number, CITATION.fullmatch(text.strip()))
                     for number, text in enumerate(handle, start=1)) if match]
    found = []
    for token in tokens:
        if token.type != tokenize.COMMENT or token.line[:token.start[1]].strip():
            continue
        match = CITATION.fullmatch(token.string)
        if match:
            found.append((token.start[0], match.group(1)))
    return found


def cited_between(path, first, last, cache):
    if path not in cache:
        cache[path] = comment_citations(path)
    values = []
    for number, value in cache[path]:
        if first <= number <= last and value not in values:
            values.append(value)
    return values


def source_key(path):
    return os.path.normcase(os.path.abspath(path))


def method_citations(test, cache):
    """The citations inside the body of a test's method, read from its source, and where that
    source stands, as (file, first line) — None where it cannot be read."""
    function = getattr(type(test), getattr(test, "_testMethodName", ""), None)
    if function is None:
        return [], None
    function = inspect.unwrap(function)
    try:
        path = inspect.getsourcefile(function)
        lines, first = inspect.getsourcelines(function)
    except (OSError, TypeError):
        return [], None
    if path is None:
        return [], None
    return cited_between(path, first, first + len(lines) - 1, cache), (source_key(path), first)


def module_tests(path, cache):
    """(Class.method, citations, first line, last line) of every test method a module's source
    defines; None where its source cannot be parsed."""
    try:
        with open(path, "rb") as handle:
            tree = ast.parse(handle.read(), filename=path)
    except (OSError, SyntaxError, ValueError):
        return None
    found = []

    def visit(body, prefix):
        for node in body:
            if isinstance(node, ast.ClassDef):
                visit(node.body, prefix + node.name + ".")
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and prefix and \
                    node.name.startswith("test"):
                first = min([node.lineno] + [item.lineno for item in node.decorator_list])
                found.append((prefix + node.name,
                              cited_between(path, first, node.end_lineno, cache), first,
                              node.end_lineno))

    visit(tree.body, "")
    return found


def test_files(start):
    """Every file below `start` whose name matches the pattern, in whatever folder, as discovery
    would reach it with every folder a package."""
    found = []
    for folder, folders, names in os.walk(start):
        folders[:] = sorted(item for item in folders
                            if not item.startswith(".") and item != "__pycache__")
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
            self.handle = open(path, "w", encoding="utf-8", newline="\n")

    def write(self, check, verdict, invariant, description=None):
        if verdict != "pass":
            self.failed = True
        if self.handle is None:
            return
        line = {"check": check, "verdict": verdict, "invariant": invariant}
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
    text = [line.strip() for line in str(value).strip().splitlines() if line.strip()]
    if not text:
        return kind.__name__
    return text[-1] if last else "%s: %s" % (kind.__name__, text[0])


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

    def first(self, kind):
        return next((description for found, description, _ in self.outcomes if found == kind),
                    None)


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
        for invariant in check.citations:
            if CITED.fullmatch(invariant):
                self.pending.setdefault(invariant, []).append(key)

    def collect(self, suite):
        for test in iterate(suite):
            kind = type(test)
            if kind.__module__ == LOADER:
                self.collect_placeholder(test)
                continue
            module = kind.__module__
            name = "%s::%s.%s" % (self.file_of(module), kind.__qualname__,
                                  getattr(test, "_testMethodName", "?"))
            citations, source = method_citations(test, self.cache)
            if source is not None:
                self.sources.add(source)
            self.add(test.id(), Check(name, citations,
                                      "%s.%s" % (module, kind.__qualname__), module))

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
        keys = []
        for method, citations, first, _ in tests:
            key = "%s::%s" % (test.id(), method)
            self.add(key, Check("%s::%s" % (name, method) if method else name, citations))
            if first is not None:
                self.sources.add((source_key(path), first))
            keys.append(key)
        self.placeholders[test.id()] = (name, keys)

    def left_out(self):
        """Every citing test method a `test_*.py` file below the directory defines that the suite
        does not run — a file in a folder discovery does not enter, or a method its module's
        `load_tests` leaves out: it never runs, so it gives `fail` for what it cites."""
        imported = {source_key(module.__file__) for module in list(sys.modules.values())
                    if getattr(module, "__file__", None)}
        for path in test_files(self.start):
            tests = module_tests(path, self.cache)
            if tests is None:
                continue
            why = ("not run: its module's suite leaves it out" if source_key(path) in imported
                   else "not run: discovery does not reach its file")
            for method, citations, first, _ in tests:
                if not citations or (source_key(path), first) in self.sources:
                    continue
                key = "%s::%s" % (source_key(path), method)
                self.add(key, Check("%s::%s" % (self.named(path), method), citations))
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
            for number, value in self.cache[path]:
                if not any(first <= number <= last for first, last in inside):
                    self.record.write(self.named(path), "fail", None,
                                      "%s:%d: `invariant: %s` stands outside any test, and a "
                                      "check cites at the check (WAY-65)"
                                      % (self.named(path), number, value))

    # --- outcomes

    def outcome(self, key, kind, description, counted):
        check = self.checks.get(key)
        if check is not None and not check.done:
            check.outcomes.append((kind, description, counted))

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
        check.done = True
        valid = [value for value in check.citations if CITED.fullmatch(value)]
        for value in check.citations:
            if value not in valid:
                self.record.write(check.name, "fail", None,
                                  "cites `%s`, which is not `<identifier>/<version>`" % value)
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
                              % (", ".join(valid), skipped))
        else:
            verdict = "pass"
            if stale:
                self.record.write(check.name, "fail", None, stale)
        for invariant in valid:
            if verdict == "fail":
                self.record.write(check.name, "fail", invariant, failed)
            elif verdict is None:
                self.voided.add(invariant)
                self.held.pop(invariant, None)
            elif invariant not in self.voided:
                self.held.setdefault(invariant, []).append(check.name)
            self.pending[invariant].remove(key)
            if not self.pending[invariant]:
                for name in self.held.pop(invariant, []):
                    self.record.write(name, "pass", invariant)

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


def recording_result(plan):
    class RecordingResult(unittest.TextTestResult):
        """unittest's report for a person, with the outcome of every test passed to the plan."""

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
        runner = unittest.TextTestRunner(stream=stream, resultclass=recording_result(plan))
        try:
            result = runner.run(suite)
        except KeyboardInterrupt:
            message = "the run stopped before every test ran"
            stream.write("\n%s\n" % message)
            record.write(PROGRAM, "fail", None, message)
            return 2
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
                                                 "a verdict for each invariant a test cites.")
    parser.add_argument("directory", help="the directory whose test_*.py files hold the tests")
    parser.add_argument("--record", action=OneRecord,
                        help="the JSON Lines file, ending in .jsonl, created or overwritten, that "
                             "receives a verdict for each invariant a test cites")
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
