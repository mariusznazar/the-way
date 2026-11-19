"""The count that tells whether a request's description reminds the human of a review of the
foundation.

Usage, from the root of the repository:

    python -B task-cycle/review_reminder.py BRANCH [--repository DIRECTORY]

In a product, the path starts with `.the-way/`. BRANCH is the branch the request merges into, as
the cycle sees it after a fetch that brings the tags (`origin/<branch>`). The script finds the
nearest tag of the form `foundation-review/*` that BRANCH contains, as `git describe --tags
--abbrev=0 --match 'foundation-review/*' BRANCH` gives it, and counts the merges on the first-parent
history of BRANCH since that tag, as `git rev-list --merges --first-parent --count <tag>..BRANCH`
gives it; with no such tag it counts from the start of history. No tag is told from an error of git
by the list of the tags BRANCH contains (`git tag --list --merged BRANCH 'foundation-review/*'`),
never by the words of a message of git, which its locale may translate. A merge of BRANCH into a
task branch is no merge of BRANCH, and the first-parent history leaves it out. A product whose
merges are squashed or rebased has no merge commits, and the count reads 0.

Standard output, four lines:

    tag: <the tag, or none>
    merges: <the count>
    threshold: <the number of merges from which the reminder is written>
    reminder: <yes when the count has reached the threshold, no otherwise>

The reminder blocks nothing; whoever writes the request's description reads the lines. The
threshold is one number for every product.

Exit code: 0 on success; 2 with `Error: <message>` on stderr when BRANCH names no commit or starts
with a hyphen, or when git cannot run in the repository or fails to list or describe the tags. The
script reads the repository and writes nothing.

Standard library only; the only program started is git.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

# One number for every product. At 60 merges a review falls every 2 to 10 weeks when the-way merges
# 6 to 26 requests a week and every 3 to 15 weeks when a product merges 4 to 21, and about every 10
# days at the pace of 49 merges in 8 days; at 30 it fell about once a week, and each review reads
# the whole foundation anew. The price taken: a mismatch of the foundation with the code lives
# longer, and one review has more remarks to read.
THRESHOLD = 60
TAG_PATTERN = "foundation-review/*"


class ReminderError(Exception):
    """A branch that cannot be counted on or a repository git cannot read."""


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise ReminderError(message)


def git(directory: Path, *arguments: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            ["git", "-C", str(directory), *arguments],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
    except OSError as error:
        raise ReminderError(f"git cannot run: {error}") from error


def last_review_tag(directory: Path, branch: str) -> str | None:
    """The nearest review tag BRANCH contains; none when no review tag is reachable from it.

    No tag is told from an error of git by the list of the tags BRANCH contains, never by the
    message of a failed `git describe`, which git words in the language of its locale: a list that
    git gives with success and empty is no tag, a list it cannot give is an error, and a
    `git describe` that fails where the list names a tag is an error too."""
    listed = git(directory, "tag", "--list", "--merged", branch, TAG_PATTERN)
    if listed.returncode != 0:
        raise ReminderError(f"git tag failed: {listed.stderr.strip()}")
    if not listed.stdout.strip():
        return None
    found = git(directory, "describe", "--tags", "--abbrev=0", "--match", TAG_PATTERN, branch)
    if found.returncode != 0:
        raise ReminderError(f"git describe failed: {found.stderr.strip()}")
    return found.stdout.strip()


def merges_since(directory: Path, branch: str, tag: str | None) -> int:
    span = f"{tag}..{branch}" if tag else branch
    counted = git(directory, "rev-list", "--merges", "--first-parent", "--count", span)
    if counted.returncode != 0:
        raise ReminderError(f"git rev-list failed: {counted.stderr.strip()}")
    return int(counted.stdout.strip())


def count(directory: Path, branch: str) -> tuple[str | None, int]:
    if branch.startswith("-"):
        raise ReminderError(f"'{branch}' is no branch name")
    named = git(directory, "rev-parse", "--verify", "--quiet", f"{branch}^{{commit}}")
    if named.returncode != 0:
        raise ReminderError(f"'{branch}' names no commit in {directory}")
    tag = last_review_tag(directory, branch)
    return tag, merges_since(directory, branch, tag)


def main(argv: list[str] | None = None) -> int:
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("branch", metavar="BRANCH")
    parser.add_argument("--repository", type=Path, default=Path("."), metavar="DIRECTORY")
    try:
        args = parser.parse_args(argv)
        tag, merges = count(args.repository, args.branch)
    except ReminderError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(
        f"tag: {tag or 'none'}\nmerges: {merges}\nthreshold: {THRESHOLD}\n"
        f"reminder: {'yes' if merges >= THRESHOLD else 'no'}\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
