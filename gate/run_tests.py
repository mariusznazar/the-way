"""The test runner of the-way: one command runs every test of the repository (WAY-16).

Usage, from the root of the repository:

    python -B gate/run_tests.py [DIRECTORY]

Without DIRECTORY, it runs the tests of every directory that holds a `test_*.py` file git tracks
and the working tree still has, each directory in a process of its own, so that test modules of the
same name in two directories never meet. Given DIRECTORY, it runs only the tests
`python -m unittest discover -s DIRECTORY -p "test_*.py"` finds there. The report for a person is
the one `unittest` prints; without DIRECTORY, each directory's report follows a line naming it, and
a last line counts the tests and names each directory that failed. The tests import from the
working directory first, as under `python -m unittest`. The runner writes no record of a run.

Exit code: 0 when every test it runs passes; 1 when a test fails or errs, a test module cannot be
imported, or a directory holds no test (WAY-63), and, without DIRECTORY, when no directory holds
such a file or a directory's process exits 0 without a report that `unittest` ends with OK; 2 when
DIRECTORY is not a directory, or, without DIRECTORY, when git cannot list the files of the
repository.
"""

import argparse
import fnmatch
import os
import re
import subprocess
import sys
import unittest

sys.dont_write_bytecode = True

PATTERN = "test_*.py"
# The line `unittest` ends a run with, from which the count of every directory's tests is read.
RAN = re.compile(rb"^Ran (\d+) tests? in ")


def run(directory, stream=None):
    """Runs the tests of one directory; returns the exit code."""
    stream = stream or sys.stderr
    if not os.path.isdir(directory):
        stream.write("%s is not a directory\n" % directory)
        return 2
    suite = unittest.TestLoader().discover(os.path.abspath(directory), pattern=PATTERN)
    if not suite.countTestCases():
        stream.write("no test found in %s\n" % directory)
        return 1
    result = unittest.TextTestRunner(stream=stream).run(suite)
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


def run_all(stream=None):
    """Runs the tests of every directory `test_directories` gives, each in a process of its own;
    returns the exit code."""
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
    failed, count = [], 0
    for directory in directories:
        stream.write(("== %s\n" % directory).encode("utf-8"))
        stream.flush()
        child = subprocess.Popen([sys.executable, "-B", os.path.abspath(__file__), directory],
                                 cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ran, last = False, b""
        for line in child.stdout:
            stream.write(line)
            stream.flush()
            counted = RAN.match(line)
            if counted:
                ran = True
                count += int(counted.group(1))
            if line.strip():
                last = line.strip()
        if child.wait() != 0:
            failed.append("%s (exit code %d)" % (directory, child.returncode))
        elif not ran or not last.startswith(b"OK"):
            # An exit code of 0 counts only beside the report of a run unittest ended with OK.
            failed.append("%s (exit code 0 without unittest's OK)" % directory)
    summary = "%d tests in %d directories; " % (count, len(directories))
    summary += ("failed: " + ", ".join(failed)) if failed else "every directory passed"
    stream.write((summary + "\n").encode("utf-8"))
    stream.flush()
    return 1 if failed else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run every test of the repository, or the "
                                                 "unittest tests of one directory.")
    parser.add_argument("directory", nargs="?",
                        help="the directory whose test_*.py files hold the tests; without it, "
                             "every directory holding a test_*.py file git tracks")
    arguments = parser.parse_args(argv)
    if arguments.directory is None:
        return run_all()
    # Tests import the product's own modules from the working directory, the root of the
    # repository, as under `python -m unittest`, never from the folder of this script.
    sys.path[0] = os.getcwd()
    return run(arguments.directory)


if __name__ == "__main__":
    sys.exit(main())
