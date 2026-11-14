"""Lists the working directories of a repository's earlier tasks and removes the ones no longer needed
(WAY-375, WAY-376).

Usage, from the root of the repository:

    python -B task-cycle/remove_merged_worktrees.py [--apply] [--target BRANCH] [--remote NAME]
                                                    [--repository DIRECTORY] [--no-fetch]

In a product, the path starts with `.the-way/`. Without `--apply` the script only prints, for each
working directory that `git worktree list` names for the repository, `remove` or `keep` with the
reason; with `--apply` it removes each directory marked `remove` with `git worktree remove` and
nothing else. A removal cannot be undone.

The remote is `origin` unless `--remote` names another, and the target branch, the one pull requests
merge into, is the branch `--target` names on it, else the branch the remote's `HEAD` names, else
`main`, else `master`. Before it judges, the script fetches the remote (`git fetch --no-tags
--no-prune`, so that no setting of `fetch.prune` takes away a remote-tracking ref), unless
`--no-fetch` has it judge by the remote-tracking refs as they stand, which can only make it keep a
directory it would remove. Where the fetch fails the script stops and judges nothing.

A directory is marked `remove` only where all of these hold at once:

- the tree is clean as git's own check of `git worktree remove` reads it: no change in a tracked file
  or in a submodule, whatever the configuration says of ignoring submodules, and no new file git does
  not ignore; files git ignores do not count;
- every commit of the directory is on the remote, as a remote-tracking ref of the remote contains
  it;
- its branch is merged: the branch's tip is the second parent of a merge commit on the first-parent
  history of the target branch, which git alone tells, with no question to the host; a branch merged
  by squash or rebase, a branch that stands at the target's tip with no commit of its own, and a
  branch of a request closed unmerged are not merged. The first-parent history leaves out the merge
  of the target branch into a task branch, whose second parent is a commit of the target;
- the directory belongs to a cycle: it stands on a branch whose name begins with `task/`, or on any
  other branch whose directory holds `.runs/task-cycles/`, the record directory of a cycle; or it
  is a detached copy of a base, a directory directly under a `.runs/` directory named `base`,
  `base-check`, `base-fix`, `base-check-<task>` or `base-fix-<task>`, where the copy named for a
  task (`<task>` being the name of its branch `task/<task>`, local or on the remote) is removed only
  where that branch is merged and a copy named for no task never stands alone;
- it is not locked, its path is no symbolic link or junction, and git reads it as a checkout of this
  repository.

Detached checkouts nested in a directory marked `remove` go with it: each is removed first, and only
where it is detached, clean and on the remote, whatever its name; otherwise the directory that holds
it stays. A directory is never removed that is the main checkout, a bare repository, the directory
the script is run from or `--repository` names, or one that holds the checkout of the script itself,
nor any directory git does not name. The script removes no branch, local or remote.

Standard output, in UTF-8: one line for each directory, `remove` or `keep`, its path, its branch (`detached`
where it has none) and the reasons; under each `remove` the paths git ignores in it outside `.runs/`,
skipping the known caches (`__pycache__`, `node_modules`, `dist` and the like), which end with the
directory; with `--apply`, a line `removed` or `failed` for each removal; then the directories of a
cycle that stay, as lines `- <name> | <branch> | <reason>`, with no absolute path, which the cycle
carries to its record and to the description of its request.

Exit code: 0 on success; 1 with `--apply` when a removal failed or left the directory standing; 2
with `Error: <message>` on stderr for the script's own failure (a repository git cannot read, no
target branch, a fetch that fails). With no `--apply` the script changes no file, and the fetch
changes only the remote-tracking refs.

Standard library only; the only program started is git.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

# Ignored paths that a command makes again, which the listing of ignored paths leaves out.
KNOWN_CACHES = frozenset({
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".cache", ".tox", ".nox",
    ".venv", "venv", "node_modules", "dist", "build", ".next", ".nuxt", ".turbo", ".parcel-cache",
    "coverage", ".gradle", "target", ".DS_Store", "Thumbs.db",
})
BASE_COPY = re.compile(r"base(?:-(?:check|fix)(?:-(?P<task>[A-Za-z0-9][A-Za-z0-9._-]*))?)?")
# The sentence of git's refusal to remove a checkout that holds a populated submodule; the rest of its
# message names the path, which can hold any word.
SUBMODULE_REFUSAL = b"working trees containing submodules cannot be moved or removed"
IGNORED_SHOWN = 12  # the ignored paths shown for one directory; the rest are counted
ENVIRONMENT = {"GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C"}


class CleanupError(Exception):
    """A failure of the script itself: a repository git cannot read, no target branch, no fetch."""


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise CleanupError(message)


@dataclass
class Entry:
    """A working directory as `git worktree list` names it, and what the script finds of it."""

    path: str
    head: str | None = None
    branch: str | None = None
    detached: bool = False
    bare: bool = False
    locked: bool = False
    prunable: bool = False
    hard: list[str] = field(default_factory=list)  # forbids removal in any place
    soft: list[str] = field(default_factory=list)  # forbids removal on its own, not with a parent
    owned: bool = False
    task: str | None = None  # the task a base copy is named for
    decision: str = "keep"
    reasons: list[str] = field(default_factory=list)
    ignored: list[str] = field(default_factory=list)
    in_use: bool = False  # the directory the script runs in or from, no matter of a human's

    @property
    def name(self) -> str:
        return os.path.basename(self.path.rstrip("/\\")) or self.path

    @property
    def branch_label(self) -> str:
        return self.branch if self.branch else "detached"


def git(directory: str, *arguments: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", directory, *arguments], capture_output=True,
                              stdin=subprocess.DEVNULL, env={**os.environ, **ENVIRONMENT},
                              check=False)
    except OSError as error:
        raise CleanupError(f"git cannot run: {error}") from error


def text(data: bytes) -> str:
    return data.decode("utf-8", errors="surrogateescape")


def first_line(data: bytes) -> str:
    lines = text(data).strip().splitlines()
    return lines[0] if lines else "no message"


def parse_worktrees(data: bytes) -> list[Entry]:
    """The entries of `git worktree list --porcelain -z`: attributes ended by NUL, a record by an
    empty one."""
    entries: list[Entry] = []
    current: Entry | None = None
    for item in data.split(b"\0"):
        if not item:
            if current is not None:
                entries.append(current)
                current = None
            continue
        key, _, value = text(item).partition(" ")
        if key == "worktree":
            current = Entry(path=value)
        elif current is None:
            raise CleanupError("git worktree list gave an attribute before its first worktree")
        elif key == "HEAD":
            current.head = value
        elif key == "branch":
            current.branch = value.removeprefix("refs/heads/")
        elif key == "detached":
            current.detached = True
        elif key == "bare":
            current.bare = True
        elif key == "locked":
            current.locked = True
        elif key == "prunable":
            current.prunable = True
    if current is not None:
        entries.append(current)
    return entries


def same(first: str, second: str) -> bool:
    try:
        return os.path.samefile(first, second)
    except OSError:
        return False


def holds(directory: str, place: str) -> bool:
    """Whether `place` is `directory` or lies below it."""
    current = os.path.abspath(place)
    while True:
        if same(current, directory):
            return True
        parent = os.path.dirname(current)
        if parent == current:
            return False
        current = parent


def inside(child: Entry, parent: Entry) -> bool:
    return not same(child.path, parent.path) and holds(parent.path, child.path)


def is_link(path: str) -> bool:
    return os.path.islink(path) or os.path.isjunction(path)


class Repository:
    """The repository the script judges: its remote, target branch and what its history holds."""

    def __init__(self, directory: str, remote: str) -> None:
        if remote.startswith("-") or not remote:
            raise CleanupError(f"'{remote}' is no remote name")
        self.remote = remote
        top = git(directory, "rev-parse", "--show-toplevel")
        if top.returncode != 0:
            raise CleanupError(f"{directory} is no repository git reads: {first_line(top.stderr)}")
        self.top = text(top.stdout).strip()
        self.common = self.absolute_git_path("--git-common-dir")
        self.target = ""
        self.second_parents: set[str] | None = None

    def absolute_git_path(self, option: str) -> str:
        found = git(self.top, "rev-parse", "--path-format=absolute", option)
        if found.returncode != 0:
            raise CleanupError(f"git cannot tell {option}: {first_line(found.stderr)}")
        return text(found.stdout).strip()

    def fetch(self) -> None:
        done = git(self.top, "fetch", "--no-tags", "--no-prune", self.remote)
        if done.returncode != 0:
            raise CleanupError(f"git fetch {self.remote} failed: {first_line(done.stderr)}")

    def resolves(self, reference: str) -> bool:
        return git(self.top, "rev-parse", "--verify", "--quiet",
                   f"{reference}^{{commit}}").returncode == 0

    def choose_target(self, target: str | None) -> None:
        self.target = self.find_target(target)

    def find_target(self, target: str | None) -> str:
        prefix = f"refs/remotes/{self.remote}/"
        if target is not None:
            if not target or target.startswith("-"):
                raise CleanupError(f"'{target}' is no branch name")
            if not self.resolves(prefix + target):
                raise CleanupError(f"no remote-tracking branch {self.remote}/{target}")
            return prefix + target
        named = git(self.top, "symbolic-ref", "--quiet", prefix + "HEAD")
        if named.returncode == 0 and self.resolves(text(named.stdout).strip()):
            return text(named.stdout).strip()
        for branch in ("main", "master"):
            if self.resolves(prefix + branch):
                return prefix + branch
        raise CleanupError(f"no target branch found on {self.remote}; name it with --target")

    @property
    def target_name(self) -> str:
        return self.target.removeprefix("refs/remotes/")

    def merged(self, commit: str | None) -> bool:
        """Whether the commit is the second parent of a merge on the first-parent history of the
        target branch."""
        if commit is None:
            return False
        if self.second_parents is None:
            listed = git(self.top, "rev-list", "--first-parent", "--merges", "--parents",
                         self.target)
            if listed.returncode != 0:
                raise CleanupError(f"git rev-list failed: {first_line(listed.stderr)}")
            self.second_parents = set()
            for line in text(listed.stdout).splitlines():
                parts = line.split()
                if len(parts) >= 3:
                    self.second_parents.add(parts[2])
        return commit in self.second_parents

    def pushed(self, commit: str) -> bool:
        found = git(self.top, "for-each-ref", "--contains", commit, "--count=1",
                    "--format=%(refname)", f"refs/remotes/{self.remote}/")
        return found.returncode == 0 and bool(text(found.stdout).strip())

    def task_branch_tips(self, task: str) -> list[str]:
        """The tips of the branch `task/<task>` where it exists, local and on the remote."""
        tips = []
        for reference in (f"refs/heads/task/{task}", f"refs/remotes/{self.remote}/task/{task}"):
            found = git(self.top, "rev-parse", "--verify", "--quiet", f"{reference}^{{commit}}")
            if found.returncode == 0:
                tips.append(text(found.stdout).strip())
        return tips


class Cleanup:
    def __init__(self, repository: Repository, entries: list[Entry], places: list[str]) -> None:
        self.repository = repository
        self.entries = entries
        self.places = places  # directories that no removed directory may hold

    def not_merged(self, subject: str) -> str:
        return (f"{subject} has no merge git can see on {self.repository.target_name}: not merged, "
                f"merged by squash or rebase, or its request open or closed")

    def inspect(self, entry: Entry) -> None:
        """Fills `hard` and `soft` of an entry, and its ownership."""
        main = self.entries[0]
        if entry is main:
            entry.hard.append("the main checkout")
            return
        if entry.bare:
            entry.hard.append("a bare repository")
            return
        if any(holds(entry.path, place) for place in self.places):
            entry.in_use = True
            entry.hard.append("the directory the script runs in or from, or one that holds it")
        self.describe_owner(entry)
        if entry.prunable or not os.path.isdir(entry.path):
            entry.hard.append("its directory is missing; `git worktree prune` removes the "
                              "registration")
            return
        if is_link(entry.path):
            entry.hard.append("its path is a symbolic link or a junction")
            return
        if not self.reads_as_checkout(entry):
            entry.hard.append("git does not read it as a checkout of this repository")
            return
        if entry.locked:
            entry.hard.append("locked")
        self.inspect_state(entry)

    def reads_as_checkout(self, entry: Entry) -> bool:
        found = git(entry.path, "rev-parse", "--path-format=absolute", "--show-toplevel",
                    "--git-common-dir")
        lines = text(found.stdout).splitlines()
        return (found.returncode == 0 and len(lines) == 2 and same(lines[0], entry.path)
                and same(lines[1], self.repository.common))

    def inspect_state(self, entry: Entry) -> None:
        # `--ignore-submodules=none` is git's own check in `git worktree remove`, which a submodule
        # declared `ignore` in the configuration would otherwise hide.
        status = git(entry.path, "status", "--porcelain", "-z", "--untracked-files=normal",
                     "--ignore-submodules=none")
        if status.returncode != 0:
            entry.hard.append("git cannot read its state")
        elif status.stdout:
            entry.hard.append("uncommitted changes: a tracked file changed or a new file that "
                              "git does not ignore")
        if entry.head is None or not self.repository.pushed(entry.head):
            entry.hard.append(f"commits not on {self.repository.remote}")
        if entry.branch is not None:
            if not self.repository.merged(entry.head):
                entry.soft.append(self.not_merged("the branch"))
        elif entry.owned and entry.task is not None:
            tips = self.repository.task_branch_tips(entry.task)
            if not tips:
                entry.soft.append(f"the branch task/{entry.task} its name gives is not found")
            elif not all(self.repository.merged(tip) for tip in tips):
                entry.soft.append(self.not_merged(f"its task branch task/{entry.task}"))
        elif entry.owned:
            entry.soft.append("a base copy named for no task, which goes only with the directory "
                              "that holds it")

    def describe_owner(self, entry: Entry) -> None:
        if entry.branch is not None:
            record = os.path.isdir(os.path.join(entry.path, ".runs", "task-cycles"))
            entry.owned = entry.branch.startswith("task/") or record
            if not entry.owned:
                entry.soft.append("not a cycle's directory: its branch has no `task/` prefix and "
                                  "it holds no cycle record")
            return
        named = BASE_COPY.fullmatch(entry.name)
        under_runs = os.path.basename(os.path.dirname(entry.path.rstrip("/\\"))) == ".runs"
        if entry.detached and named and under_runs:
            entry.owned = True
            entry.task = named.group("task")
        else:
            entry.soft.append("not a cycle's directory: a detached checkout that is no copy of a "
                              "base under a `.runs/` directory")

    def judge(self) -> None:
        for entry in self.entries:
            self.inspect(entry)
        candidates = [entry for entry in self.entries
                      if entry.owned and not entry.hard and not entry.soft]
        for parent in sorted(candidates, key=lambda entry: len(os.path.abspath(entry.path))):
            if parent.decision == "remove":
                continue
            held = [entry for entry in self.entries if inside(entry, parent)]
            blocking = [entry for entry in held if entry.hard or entry.branch is not None]
            if blocking:
                for entry in blocking:
                    why = entry.hard or ["it stands on the branch " + str(entry.branch)]
                    parent.reasons.append(f"holds {entry.name}, which stays: {'; '.join(why)}")
                continue
            parent.decision = "remove"
            parent.reasons = [self.removal_reason(parent)]
            for entry in held:
                entry.decision = "remove"
                entry.reasons = [f"nested in {parent.name}, which is removed; clean and on "
                                 f"{self.repository.remote}"]
        for entry in self.entries:
            if entry.decision == "keep":
                entry.reasons = (entry.hard + entry.soft + entry.reasons) or ["kept"]

    def removal_reason(self, entry: Entry) -> str:
        if entry.branch is not None:
            return (f"clean, on {self.repository.remote}, branch merged into "
                    f"{self.repository.target_name}")
        return (f"clean copy of a base on {self.repository.remote}; its task branch "
                f"task/{entry.task} is merged into {self.repository.target_name}")

    def list_ignored(self, entry: Entry) -> None:
        found = git(entry.path, "ls-files", "--others", "--ignored", "--exclude-standard",
                    "--directory", "-z")
        if found.returncode != 0:
            entry.ignored = [f"cannot be listed: {first_line(found.stderr)}"]
            return
        for item in text(found.stdout).split("\0"):
            parts = [part for part in item.split("/") if part]
            if not parts or parts[0] == ".runs" or item.endswith(".pyc"):
                continue
            if any(part in KNOWN_CACHES for part in parts):
                continue
            entry.ignored.append(item)


def removal_order(entries: list[Entry]) -> list[Entry]:
    """The directories marked `remove`, the deepest first, so that a nested checkout goes before the
    directory that holds it."""
    chosen = [entry for entry in entries if entry.decision == "remove"]
    return sorted(chosen, key=lambda entry: (-len(os.path.abspath(entry.path).split(os.sep)),
                                             entry.path))


def remove_entry(repository: Repository, entry: Entry) -> str | None:
    """Removes one directory with `git worktree remove`; None on success, else what went wrong."""
    done = git(repository.top, "worktree", "remove", entry.path)
    if done.returncode != 0 and SUBMODULE_REFUSAL in done.stderr:
        # Git refuses to remove a checkout holding a populated submodule without `--force`; the
        # tree and the submodule were found clean above.
        done = git(repository.top, "worktree", "remove", "--force", entry.path)
    if done.returncode != 0:
        return first_line(done.stderr)
    if os.path.lexists(entry.path):
        return "git removed the checkout but the directory still stands"
    return None


def apply_removals(repository: Repository, entries: list[Entry]) -> list[str]:
    failed: dict[str, str] = {}
    lines = []
    for entry in removal_order(entries):
        blocked = [other for other in entries
                   if other.path in failed and inside(other, entry)]
        if blocked:
            failed[entry.path] = f"{blocked[0].name} inside it was not removed"
            lines.append(f"failed   {entry.path}: {failed[entry.path]}")
            continue
        problem = remove_entry(repository, entry)
        if problem is None:
            lines.append(f"removed  {entry.path}")
        else:
            failed[entry.path] = problem
            lines.append(f"failed   {entry.path}: {problem}")
    for entry in entries:
        if entry.path in failed:
            entry.decision = "keep"
            entry.reasons = ["removal failed; see the output of the script"]
    return lines


def report(entries: list[Entry], applied: list[str] | None) -> list[str]:
    lines = []
    for entry in entries:
        lines.append(f"{entry.decision:<7} {entry.path}  [{entry.branch_label}]  "
                     + "; ".join(entry.reasons))
        if entry.decision == "remove" and entry.ignored:
            for shown in entry.ignored[:IGNORED_SHOWN]:
                lines.append(f"          ignored: {shown}")
            if len(entry.ignored) > IGNORED_SHOWN:
                lines.append(f"          ignored: ... and {len(entry.ignored) - IGNORED_SHOWN} more")
    marked = sum(1 for entry in entries if entry.decision == "remove")
    if applied is None:
        lines.append(f"Dry run: nothing was removed; {marked} directories are marked `remove`. "
                     "Run again with --apply to remove them; a removal cannot be undone.")
    else:
        lines.extend(applied)
    left = [entry for entry in entries
            if entry.owned and entry.decision == "keep" and not entry.in_use]
    lines.append("Directories of cycles that stay for a human decision (name | branch | reason):"
                 + ("" if left else " none"))
    for entry in left:
        reason = "; ".join(entry.reasons)
        lines.append(f"- {entry.name} | {entry.branch_label} | {reason}")
    return lines


def parse_arguments(argv: list[str]) -> argparse.Namespace:
    parser = Parser(prog="remove_merged_worktrees.py", description=__doc__.split("\n\n")[0])
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--target", metavar="BRANCH")
    parser.add_argument("--remote", default="origin", metavar="NAME")
    parser.add_argument("--repository", default=".", metavar="DIRECTORY")
    parser.add_argument("--no-fetch", action="store_true")
    return parser.parse_args(argv)


def run(argv: list[str]) -> int:
    arguments = parse_arguments(argv)
    repository = Repository(arguments.repository, arguments.remote)
    if not arguments.no_fetch:
        repository.fetch()
    repository.choose_target(arguments.target)
    listed = git(repository.top, "worktree", "list", "--porcelain", "-z")
    if listed.returncode != 0:
        raise CleanupError(f"git worktree list failed: {first_line(listed.stderr)}")
    entries = parse_worktrees(listed.stdout)
    if not entries:
        raise CleanupError("git worktree list names no worktree")
    places = [os.getcwd(), repository.top, os.path.dirname(os.path.abspath(__file__))]
    cleanup = Cleanup(repository, entries, places)
    cleanup.judge()
    for entry in entries:
        if entry.decision == "remove":
            cleanup.list_ignored(entry)
    applied = apply_removals(repository, entries) if arguments.apply else None
    ordered = [entries[0], *sorted(entries[1:], key=lambda entry: entry.path.lower())]
    lines = report(ordered, applied)
    sys.stdout.write("\n".join(lines) + "\n")
    return 1 if applied is not None and any(line.startswith("failed") for line in applied) else 0


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    try:
        return run(sys.argv[1:] if argv is None else argv)
    except CleanupError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
