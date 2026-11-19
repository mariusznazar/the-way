"""The ways `foundation_check.py` reads a repository: git, a file of the working tree, and a file as
the commit the branch left the main branch from holds it.

The module is imported by `foundation_check.py`, which writes the report; importing it runs nothing.
It reads files and asks git, and writes nothing.
"""

import os
import subprocess
import sys

sys.dont_write_bytecode = True

# The branches that may be the main branch, in the order the script takes the first that exists.
MAIN_BRANCHES = ("refs/remotes/origin/HEAD", "refs/heads/main", "refs/heads/master")


def git(root, *args, stdin=None):
    """(exit code, output) of git, or (None, why) where git cannot be started."""
    try:
        result = subprocess.run(
            ["git", *args], cwd=root, input=stdin, capture_output=True, text=True, encoding="utf-8"
        )
    except OSError as error:
        return None, str(error)
    return result.returncode, result.stdout


def fork_point(root):
    """The commit the branch left the main branch from, as `git merge-base HEAD` the first of
    MAIN_BRANCHES that exists gives it, or None where there is no such branch or no merge base."""
    for branch in MAIN_BRANCHES:
        code, tip = git(root, "rev-parse", "--verify", "--quiet", branch + "^{commit}")
        if code == 0 and tip.strip():
            code, base = git(root, "merge-base", "HEAD", tip.strip())
            return base.strip() if code == 0 and base.strip() else None
    return None


def at_commit(root, commit, path):
    """The lines of a file as a commit holds it, or None where the commit holds no file of that
    name or git cannot give it as UTF-8 text. A file the commit lacks is no empty file."""
    try:
        result = subprocess.run(
            ["git", "show", "%s:%s" % (commit, path)], cwd=root, capture_output=True
        )
        text = result.stdout.decode("utf-8")
    except OSError, UnicodeDecodeError:
        return None
    return text.replace("\r\n", "\n").split("\n") if result.returncode == 0 else None


def read(root, path):
    """The lines of a file, or none where it cannot be read as UTF-8 text."""
    try:
        with open(os.path.join(root, *path.split("/")), encoding="utf-8") as handle:
            return handle.read().split("\n")
    except OSError, UnicodeDecodeError:
        return []
