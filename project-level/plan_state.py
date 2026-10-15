"""Read evidence for project-plan progress without changing project documents (WAY-153).

Usage: python -B <the-way>/project-level/plan_state.py PLAN PRODUCT_REPOSITORY

Exit codes: 0 for a completed observation (unchecked evidence can remain), 1 for source
findings or conflicting task states, 2 for invocation, source-read or Git operational errors.
Only Git metadata is refreshed; proposals never apply changes to the plan or task documents.
"""

import argparse
import os
from pathlib import Path
import re
import subprocess
import sys
from dataclasses import dataclass, field

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import plan_check  # noqa: E402
import readiness_check  # noqa: E402

GIT_TIMEOUT = 30
PR_LINK = re.compile(r"https?://[^\s<>\[\]()`\"']+/(?:pull|merge_requests)/[0-9]+"
                     r"(?:[?#][^\s<>\[\]()`\"']*)?")


def display(value):
    """Keep untrusted paths, Git diagnostics and record text inside one report line."""
    return "".join(char if char.isprintable() else ascii(char)[1:-1] for char in str(value))


class GitError(Exception):
    pass


class Git:
    def __init__(self, repository):
        self.repository = repository

    def run(self, *arguments, allowed=(0,)):
        environment = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
        try:
            result = subprocess.run(["git", "-C", str(self.repository), *arguments],
                                    capture_output=True, timeout=GIT_TIMEOUT, env=environment)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitError("git %s: %s" % (arguments[0], display(error))) from error
        if result.returncode not in allowed:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise GitError("git %s failed (%d): %s" %
                           (arguments[0], result.returncode, display(detail)))
        return result

    def text(self, *arguments, allowed=(0,)):
        return self.run(*arguments, allowed=allowed).stdout.decode("utf-8").strip()


@dataclass
class Observation:
    worktrees: list = field(default_factory=list)
    refs: list = field(default_factory=list)
    integration: str | None = None
    commit: str | None = None
    unchecked: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    complete: bool = True


def observe(git):
    """Inventory only Git-listed worktrees and branches; refresh the declared origin route."""
    observation = Observation()
    git.text("rev-parse", "--git-dir")
    try:
        raw = git.run("worktree", "list", "--porcelain", "-z").stdout
        for token in raw.split(b"\0"):
            if token.startswith(b"worktree "):
                path = Path(os.fsdecode(token[9:]))
                if not path.is_dir():
                    observation.unchecked.append("unavailable Git-listed worktree " + display(path))
                    observation.complete = False
                else:
                    observation.worktrees.append(path)
        if git.text("rev-parse", "--is-shallow-repository") != "false":
            observation.unchecked.append("shallow history cannot establish completion")
            observation.complete = False
        remotes = git.text("remote").splitlines()
        if "origin" not in remotes:
            observation.unchecked.append("origin remote unavailable; integration is not established")
        else:
            route = git.run("symbolic-ref", "--quiet", "refs/remotes/origin/HEAD", allowed=(0, 1))
            ref = route.stdout.decode("utf-8").strip()
            if route.returncode or not ref.startswith("refs/remotes/origin/") or ref.endswith("/HEAD"):
                observation.unchecked.append("origin/HEAD does not establish one integration branch")
            else:
                branch = ref[len("refs/remotes/origin/"):]
                remote_head = git.text("ls-remote", "--symref", "origin", "HEAD")
                declared = [line.split("\t")[0][5:] for line in remote_head.splitlines()
                            if line.startswith("ref: ") and line.endswith("\tHEAD")]
                if declared != ["refs/heads/" + branch]:
                    observation.unchecked.append("origin/HEAD disagrees with the remote default or "
                                                 "the remote has no unambiguous HEAD")
                else:
                    git.run("fetch", "--no-tags", "origin",
                            "+refs/heads/*:refs/remotes/origin/*")
                    commit = git.text("rev-parse", "--verify", ref + "^{commit}")
                    observation.integration, observation.commit = ref, commit
    except (GitError, UnicodeError) as error:
        observation.errors.append(display(error))
        observation.complete = False
    try:
        # Tags and detached HEADs do not declare branches. Symbolic remote HEAD is redundant.
        refs = git.text("for-each-ref", "--format=%(refname) %(symref)",
                        "refs/heads/", "refs/remotes/")
        observation.refs = [line.split()[0] for line in refs.splitlines()
                            if len(line.split()) == 1]
    except (GitError, UnicodeError) as error:
        observation.errors.append(display(error))
        observation.complete = False
    return observation


def commits_touching(git, refs, path):
    if not refs:
        return []
    return git.text("log", "--full-history", "--format=%H", *refs, "--",
                    ":(literal)" + path).splitlines()


def archived_files(git, commit, archive):
    """The archive directory is the record contract; basenames and prose are not a schema."""
    raw = git.run("ls-tree", "-r", "-z", "--full-tree", commit, "--",
                  ":(literal)" + archive).stdout
    paths = []
    for entry in raw.split(b"\0"):
        if entry:
            metadata, path = entry.split(b"\t", 1)
            mode, kind, _ = metadata.split()
            if mode.startswith(b"100") and kind == b"blob":
                paths.append(path.decode("utf-8"))
    return paths


def record_pointers(git, commit, archive):
    """Read pointer text as data, without executing or printing the archive's instructions."""
    result = git.run("grep", "-I", "-z", "-n", "-E",
                     r"https?://[^ ]+/(pull|merge_requests)/[0-9]+", commit, "--",
                     ":(literal)" + archive, allowed=(0, 1))
    pointers = []
    for row in result.stdout.splitlines():
        parts = row.split(b"\0", 2)
        if len(parts) == 3:
            source = parts[0].decode("utf-8")
            for link in PR_LINK.findall(parts[2].decode("utf-8", errors="replace")):
                pointers.append((source, link))
    return sorted(set(pointers))


def task_report(git, observation, task):
    prefix = "%d %s" % (task.number, task.name)
    lines = ["task %s: %s" % (prefix, task.state)]
    active, archived, merged = [], [], []
    unchecked, errors = [], []
    working = ".runs/task-cycles/" + task.name
    archive = "docs/task-cycles/" + task.name + "/"
    try:
        for worktree in observation.worktrees:
            path = worktree / working
            try:
                if path.is_dir():
                    active.append(path)
            except OSError as error:
                unchecked.append("cannot read working-cycle path %s: %s" % (path, error))
        archived = commits_touching(git, observation.refs, archive)
        for commit in archived:
            refs = git.text("for-each-ref", "--contains=" + commit, "--format=%(refname)",
                            "refs/heads/", "refs/remotes/")
            lines.append("evidence %s: archived cycle %s commit %s on %s" %
                         (prefix, archive, commit, display(", ".join(refs.splitlines()))))
            for source, link in record_pointers(git, commit, archive):
                lines.append("evidence %s: PR pointer from %s: %s" %
                             (prefix, display(source), display(link)))
        # A deletion is a cycle trace, but cannot stand for actual archived content.
        if observation.commit and observation.complete:
            for commit in commits_touching(git, [observation.commit], archive):
                paths = archived_files(git, commit, archive)
                if paths:
                    merged.append(commit)
                    lines.append("evidence %s: cycle record %s commit %s reachable from %s %s" %
                                 (prefix, display(", ".join(paths)), commit,
                                  observation.integration, observation.commit))
    except (GitError, UnicodeError) as error:
        errors.append(display(error))
        merged = []
    for path in active:
        lines.append("evidence %s: working cycle %s" % (prefix, display(path)))
    trace = bool(active or archived or merged)
    conflict = False
    if task.state in ("ready for cycle", "in cycle"):
        if task.state == "ready for cycle" and trace:
            lines.append("propose %s: ready for cycle -> in cycle" % prefix)
        if merged and not errors:
            lines.append("propose %s: in cycle -> done" % prefix)
        else:
            unchecked.append("PR outcome unchecked; cycle evidence is outside established fresh "
                             "integration history" if trace else "no sufficient cycle trace; PR outcome unchecked")
    elif trace and (task.state != "done" or active or (
            observation.commit and observation.complete and not merged and not errors)):
        conflict = True
        lines.append("conflict %s: cycle trace conflicts with plan state %s; human reconciliation "
                     "required" % (prefix, task.state))
    elif task.state == "done" and not merged:
        unchecked.append("plan says done but completion cannot be established from fresh Git history")
    elif not trace:
        unchecked.append("no sufficient cycle trace; no progress inferred")
    for reason in observation.unchecked + unchecked:
        lines.append("unchecked %s: %s" % (prefix, display(reason)))
    for error in errors:
        lines.append("error: " + error)
    return lines, conflict, bool(errors)


def sources(plan_path):
    """Validate original whole sources with the existing checkers, then reuse their parser."""
    text, error = plan_check.read(plan_path)
    if error:
        return None, ["error: " + display(error)], 2
    relative = plan_check.definition_path(text)
    definition, error = None, None
    if relative is not None:
        definition, error = plan_check.read(os.path.join(os.path.dirname(plan_path), relative))
        if error:
            return None, ["error: " + display(error)], 2
    findings = [str(finding) for finding in plan_check.check(text, definition, error)]
    preamble, sections = plan_check.split(text)
    statuses = [line.rstrip() for _, line in preamble if line.startswith("Status:")]
    if len(statuses) != 1 or not statuses[0].startswith("Status: handed over "):
        findings.append("fail: plan must have one handed-over Status line")
    if definition is not None:
        findings.extend("definition " + str(finding) for finding in readiness_check.check(definition))
        header, _ = readiness_check.split(definition)
        approvals = [line.rstrip() for _, line in header if line.startswith("Status:")]
        if len(approvals) != 1 or not re.fullmatch(r"Status: approved [0-9]{4}-[0-9]{2}-[0-9]{2}", approvals[0]):
            findings.append("fail: definition must have one approved Status line")
        elif not plan_check.calendar_date(approvals[0][-10:]):
            findings.append("fail: definition approval date is not a calendar date")
    if findings:
        return None, findings, 1
    section = next(section for section in sections if section.name == plan_check.TASKS)
    _, tasks, _ = plan_check.read_tasks(section)
    return tasks, [], 0


def main(argv=None):
    # surface: project-plan-state-command — pinned
    parser = argparse.ArgumentParser(description="Report Git evidence for project plan task states.")
    parser.add_argument("plan", help="original handed-over project plan")
    parser.add_argument("product_repository", help="product Git repository")
    args = parser.parse_args(argv)
    try:
        plan_path = os.path.abspath(args.plan)
        repository = Path(args.product_repository).resolve()
        tasks, findings, code = sources(plan_path)
        for finding in findings:
            print(display(finding))
        if code:
            return code
        print("repository: " + display(repository))
        git = Git(repository)
        observation = observe(git)
        if observation.integration:
            print("integration: %s %s" % (observation.integration, observation.commit))
        for reason in observation.unchecked:
            print("unchecked: " + display(reason))
        for error in observation.errors:
            print("error: " + display(error))
        conflicts, failures = False, bool(observation.errors)
        for task in tasks:
            lines, conflict, failure = task_report(git, observation, task)
            for line in lines:
                print(line)
            conflicts |= conflict
            failures |= failure
        return 2 if failures else 1 if conflicts else 0
    except (GitError, OSError, ValueError, UnicodeError) as error:
        print("error: " + display(error))
        return 2


if __name__ == "__main__":
    sys.exit(main())
