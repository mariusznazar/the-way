"""The absolute paths and the note links in the files a repository tracks (WAY-324).

Usage, from a directory of the repository to check, which in a product is its root:

    python -B task-cycle/tracked_private_paths_check.py INVARIANT

In a product, the path starts with `.the-way/`. INVARIANT is the identifier of an invariant in
`foundations/invariants.md` of the repository, whose sentence says: no file git tracks, other than
the files it names, contains an absolute path or a note link. Every text between backticks in that
sentence is the path of a file the check skips, as git writes it, with `/`; the files are those
that write example paths in order to find or to test them.

The script reads each other file git tracks that the working tree still has and lists, as
`private_paths_check.py` does and in its format, every absolute path in it, and every note link in
a Markdown file, a file whose name ends in `.md` in any letter case: in code, `[[a, b]]` is a
list inside a list and `[[ -f x ]]` a test of the shell. The rules for what a path and a link are
stand in `private_paths_check.py` (WAY-323). A file that is binary is not read and is counted on
the last line, as there.

Exit code: 0 when nothing is listed; 1 with the hits listed; 2 with `Error: <message>` on stderr
when the argument is missing, the directory lies in no git repository, the invariants file or the
invariant is not there, the sentence names a file git does not track, or a file cannot be read as
UTF-8. The script writes no file and runs only `git`.

Standard library only.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import private_paths_check  # noqa: E402
from private_paths_check import PrivatePathsError  # noqa: E402

INVARIANTS_FILE = "foundations/invariants.md"
MARKDOWN_SUFFIX = ".md"


def git(root: Path | None, *arguments: str) -> bytes:
    try:
        run = subprocess.run(["git", *arguments], cwd=root, capture_output=True)
    except OSError as error:
        raise PrivatePathsError(f"cannot run git: {private_paths_check.display(error)}") from error
    if run.returncode != 0:
        message = run.stderr.decode("utf-8", "replace").strip()
        raise PrivatePathsError(f"git {arguments[0]} failed: {private_paths_check.display(message)}")
    return run.stdout


def repository_root() -> Path:
    return Path(git(None, "rev-parse", "--show-toplevel").decode("utf-8").strip())


def tracked_files(root: Path) -> list[str]:
    """The files git tracks below `root`, as paths with `/`, sorted."""
    listed = git(root, "ls-files", "-z").decode("utf-8")
    return sorted(name for name in listed.split("\0") if name)


def sentence_of(root: Path, invariant: str) -> str:
    """The sentence of an invariant: the first paragraph under its heading, as one line."""
    path = root / INVARIANTS_FILE
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        raise PrivatePathsError(
            f"cannot read {INVARIANTS_FILE}: {private_paths_check.display(error)}") from error
    heading = f"## {invariant}"
    for index, line in enumerate(lines):
        if line.rstrip() == heading:
            break
    else:
        raise PrivatePathsError(f"{INVARIANTS_FILE} holds no invariant {invariant}")
    sentence = []
    for line in lines[index + 1:]:
        if sentence and not line.strip():
            break
        if line.strip():
            sentence.append(line.strip())
    if not sentence:
        raise PrivatePathsError(f"the invariant {invariant} has no sentence")
    return " ".join(sentence)


def skipped_files(root: Path, invariant: str, tracked: list[str]) -> list[str]:
    """The files the sentence of the invariant names, each of which git must track."""
    names = re.findall(r"`([^`]+)`", sentence_of(root, invariant))
    untracked = [name for name in names if name not in tracked]
    if untracked:
        raise PrivatePathsError(
            f"the sentence of {invariant} names files git does not track: "
            + ", ".join(private_paths_check.display(name) for name in untracked))
    return names


def check_tracked(root: Path, skipped: list[str], tracked: list[str]) -> private_paths_check.Result:
    """The hits in the tracked files not skipped that the working tree still has."""
    result = private_paths_check.Result()
    for name in tracked:
        path = root / name
        if name in skipped or not path.is_file():
            continue
        private_paths_check.check_file(
            path, result, note_links=name.lower().endswith(MARKDOWN_SUFFIX), name=name)
    return result


def main(argv: list[str] | None = None) -> int:
    arguments = sys.argv[1:] if argv is None else argv
    try:
        if len(arguments) != 1 or arguments[0].startswith("-"):
            raise PrivatePathsError("give the identifier of the invariant, once")
        root = repository_root()
        tracked = tracked_files(root)
        skipped = skipped_files(root, arguments[0], tracked)
        result = check_tracked(root, skipped, tracked)
    except PrivatePathsError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    return private_paths_check.report(result)


if __name__ == "__main__":
    sys.exit(main())
