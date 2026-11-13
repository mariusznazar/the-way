"""The test runner of the-way: one command runs every test of the repository (WAY-16).

Usage, from the root of the repository:

    python -B gate/run_tests.py [--jobs N] [--slowest N] [DIRECTORY]

Without DIRECTORY, it runs the tests of every directory that holds a `test_*.py` file git tracks
and the working tree still has, each directory in a process of its own, so that test modules of the
same name in two directories never meet. The directories run at the same time, all of them at once
unless `--jobs N` limits how many run at once; `--jobs 1` runs them one after another. Each
directory's report is printed whole when its run ends, under a line `== <directory>` and never
mixed with another's, so the reports stand in the order the directories end, not in the order of
their names. A last line counts the tests and names each directory that failed, in the order of
their names. Given DIRECTORY, it runs only the tests
`python -m unittest discover -s DIRECTORY -p "test_*.py"` finds there, and `--jobs` changes nothing.
The report for a person is the one `unittest` prints. A skipped test is named there, with its
reason, before the closing lines. With `--slowest N`, each directory's report also lists its N
slowest tests with their time, after the skipped tests and before the closing lines; it needs a
`unittest` that takes `durations` (Python 3.12 or later) and gives the exit code 2 and a message
where its Python has none. Without the option the report holds no such list. The tests import from
the working directory first, as under `python -m unittest`. The runner writes no record of a run.

Exit code: 0 when every test it runs passes; 1 when a test fails or errs, a test module cannot be
imported, or a directory holds no test (WAY-63), and, without DIRECTORY, when no directory holds
such a file or a directory's process exits 0 without a report that `unittest` ends with OK; 2 when
DIRECTORY is not a directory, when `--jobs` or `--slowest` is not a whole number of at least 1 or
`--slowest` finds no `durations` in `unittest`, or, without DIRECTORY, when git cannot list the
files of the repository.
"""

import argparse
import concurrent.futures
import fnmatch
import inspect
import os
import re
import subprocess
import sys
import unittest

sys.dont_write_bytecode = True

PATTERN = "test_*.py"
# The line `unittest` ends a run with, from which the count of every directory's tests is read.
RAN = re.compile(rb"^Ran (\d+) tests? in ")


class NamingSkipsResult(unittest.TextTestResult):
    """A test result that names each skipped test and its reason before the closing lines."""

    def printErrors(self):
        super().printErrors()
        for test, reason in self.skipped:
            self.stream.writeln("skipped: %s: %s" % (test.id(), reason))


def supports_durations():
    """Whether this Python's `unittest` can list the slowest tests of a run (3.12 and later)."""
    return "durations" in inspect.signature(unittest.TextTestRunner).parameters


def run(directory, stream=None, slowest=None):
    """Runs the tests of one directory, listing its `slowest` slowest tests where that is given;
    returns the exit code."""
    stream = stream or sys.stderr
    if not os.path.isdir(directory):
        stream.write("%s is not a directory\n" % directory)
        return 2
    suite = unittest.TestLoader().discover(os.path.abspath(directory), pattern=PATTERN)
    if not suite.countTestCases():
        stream.write("no test found in %s\n" % directory)
        return 1
    options = {} if slowest is None else {"durations": slowest}
    result = unittest.TextTestRunner(stream=stream, resultclass=NamingSkipsResult,
                                     **options).run(suite)
    return 0 if result.wasSuccessful() else 1


def test_directories(root):
    """Every directory, relative to `root` and written with `/`, holding a `test_*.py` file that
    git tracks and that stands in the working tree, sorted; None where git cannot list them."""
    listed = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True)
    if listed.returncode != 0:
        return None
    found = set()
    for path in listed.stdout.decode("utf-8").split("\0"):
        folder, _, name = path.rpartition("/")
        if fnmatch.fnmatchcase(name, PATTERN) and \
                os.path.isfile(os.path.join(root, *path.split("/"))):
            found.add(folder or ".")
    return sorted(found)


def run_directory(root, directory, slowest):
    """Runs the tests of one directory in a process of its own, from `root`; returns what the
    process printed, its output and its error output together, and its exit code."""
    command = [sys.executable, "-B", os.path.abspath(__file__), directory]
    if slowest is not None:
        command += ["--slowest", str(slowest)]
    done = subprocess.run(command, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return done.stdout, done.returncode


def run_all(jobs=None, slowest=None, stream=None):
    """Runs the tests of every directory `test_directories` gives, each in a process of its own, at
    most `jobs` of them at once (all at once where it is None); prints each directory's report whole
    as its process ends; returns the exit code."""
    stream = stream or sys.stdout.buffer
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                         text=True)
    root = top.stdout.strip() if top.returncode == 0 else None
    directories = test_directories(root) if root else None
    if directories is None:
        stream.write(b"git cannot list the files of the repository: run from inside it\n")
        stream.flush()
        return 2
    if not directories:
        stream.write(b"no directory holds a test_*.py file git tracks\n")
        stream.flush()
        return 1
    failed, count = {}, 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(jobs or len(directories),
                                                              len(directories))) as pool:
        try:
            pending = {pool.submit(run_directory, root, directory, slowest): directory
                       for directory in directories}
            for done in concurrent.futures.as_completed(pending):
                directory = pending[done]
                output, code = done.result()
                stream.write(("== %s\n" % directory).encode("utf-8") + output)
                if output and not output.endswith(b"\n"):
                    stream.write(b"\n")
                stream.flush()
                ran, last = False, b""
                for line in output.split(b"\n"):
                    counted = RAN.match(line)
                    if counted:
                        ran = True
                        count += int(counted.group(1))
                    if line.strip():
                        last = line.strip()
                if code != 0:
                    failed[directory] = "%s (exit code %d)" % (directory, code)
                elif not ran or not last.startswith(b"OK"):
                    # An exit code of 0 counts only beside the report of a run unittest
                    # ended with OK.
                    failed[directory] = "%s (exit code 0 without unittest's OK)" % directory
        except KeyboardInterrupt:
            # Directories still queued do not start; the ones running got the interrupt with us.
            pool.shutdown(wait=True, cancel_futures=True)
            raise
    summary = "%d tests in %d directories; " % (count, len(directories))
    summary += ("failed: " + ", ".join(failed[name] for name in directories if name in failed)) \
        if failed else "every directory passed"
    stream.write((summary + "\n").encode("utf-8"))
    stream.flush()
    return 1 if failed else 0


def whole_number(text):
    """An argument that is a whole number of at least 1."""
    try:
        number = int(text)
    except ValueError:
        number = 0
    if number < 1:
        raise argparse.ArgumentTypeError("%r is not a whole number of at least 1" % text)
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run every test of the repository, or the "
                                                 "unittest tests of one directory.")
    parser.add_argument("directory", nargs="?",
                        help="the directory whose test_*.py files hold the tests; without it, "
                             "every directory holding a test_*.py file git tracks")
    parser.add_argument("--jobs", type=whole_number, metavar="N",
                        help="how many directories run at once, without DIRECTORY; default: all "
                             "of them; 1 runs them one after another")
    parser.add_argument("--slowest", type=whole_number, metavar="N",
                        help="list the N slowest tests of each directory with their time")
    arguments = parser.parse_args(argv)
    if arguments.slowest is not None and not supports_durations():
        parser.error("--slowest needs a unittest that takes durations, Python 3.12 or later; "
                     "this is Python %d.%d" % sys.version_info[:2])
    if arguments.directory is None:
        return run_all(arguments.jobs, arguments.slowest)
    # Tests import the product's own modules from the working directory, the root of the
    # repository, as under `python -m unittest`, never from the folder of this script.
    sys.path[0] = os.getcwd()
    return run(arguments.directory, slowest=arguments.slowest)


if __name__ == "__main__":
    sys.exit(main())
